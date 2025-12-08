#!/usr/bin/env python3
# scripts/predict_new.py

import argparse, os, json, sys, csv, difflib

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Phi-3 uses custom code, so trust_remote_code is recommended
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

# Causal LMs often have no pad token; use EOS as pad if needed
if TOKENIZER.pad_token is None:
    TOKENIZER.pad_token = TOKENIZER.eos_token

# Use half precision on GPU to save VRAM; full precision on CPU
DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

MODEL = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    torch_dtype=DTYPE,
    low_cpu_mem_usage=True,  # stream weights to reduce peak RAM
)

MODEL = MODEL.to(DEVICE)

METRICS_FILE = "../work/metrics.csv"
RESIDUAL_FILE = "../work/residuals.csv"

# Open old, new dataset. Pass old to LLM
def _open_data(path, len_prompt=False, stop_after=sys.maxsize):
    results = []
    residuals = []

    prev_old = None
    prev_new = None

    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            # Check we need to stop early
            if idx > stop_after:
                break
            
            # Read line and verify
            line = line.strip()
            if not line:
                continue

            # Try load line
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Skipping malformed JSON on line {idx}: {e}")
                continue

            old = rec.get("old")
            new = rec.get("new")

            # Ignore first line do to few-shot prompting
            if idx <= 1:
                prev_old = old
                prev_new = new
                continue

            if old is None or new is None:
                print(f"Skipping line {idx}: missing 'old' or 'new'")
                continue

            # Optionally include length of "new" in the prediction call
            target_len = len(TOKENIZER(new).input_ids) if len_prompt else None
            predicted = _predict(old, prev_old, prev_new, target_len=target_len)
            print("==============old=============")
            print(old)
            print("===============pred============")
            print(predicted)
            print("==============actual=============")
            print(new)

            prev_old = old
            prev_new = new

            metrics, residual = _compare(predicted, new)

            # Build a simple row for metrics
            row = {
                "index": idx,
                "old_len": len(old),
                "new_len": len(new),
                "pred_len": len(predicted) if predicted is not None else 0,
                **(metrics or {}),   # merge metrics dict if not None
            }
            results.append(row)

            residuals.append({
                "index": idx,
                "residual": residual,
            })

    _save_results(results)
    _save_residual(residuals)


# Given old data, predict new
def _predict(old, prev_old, prev_new, target_len=None):
    # Create prompt (prompt + old (+ optional len))
    prompt = (
        "Apply the same kind of edits as in the example.\n"
        "Copy all lines and change only what is necessary.\n"
        "Return only the edited code, no explanations.\n\n"
        "Example (before):\n"
        f"{prev_old}\n"
        "Example (after):\n"
        f"{prev_new}\n\n"
        "Code to edit:\n"
        f"{old}\n"
        "Edited code:\n"
    )


    max_ctx = _model_max_ctx()

    # Encode the full prompt
    enc = TOKENIZER(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=max_ctx,
    )
    input_ids = enc["input_ids"].to(DEVICE)
    attention_mask = enc["attention_mask"].to(DEVICE)
    prompt_len = input_ids.size(1)

    available_for_gen = max_ctx - prompt_len
    if available_for_gen <= 0:
        print("Warning: no room left for generation; returning empty prediction.")
        return ""

    # Decide how many tokens to generate
    if target_len is not None:
        # target_len is the tokenized length of the true "new" file
        approx_target_tokens = target_len + 64  # slack so it can finish the last line
        approx_target_tokens = max(32, approx_target_tokens)
        approx_target_tokens = min(approx_target_tokens, available_for_gen)
    else:
        # Fallback: scale with old length
        old_tokens = len(TOKENIZER(old).input_ids)
        approx_target_tokens = old_tokens + 64
        approx_target_tokens = max(32, approx_target_tokens)
        approx_target_tokens = min(approx_target_tokens, available_for_gen)

    # Let the model generate up to the approximate target length
    max_new = approx_target_tokens

    with torch.no_grad():
        outputs = MODEL.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=max_new,
            do_sample=False,                # greedy
            temperature=0.0,                # ignored when do_sample=False
            eos_token_id=TOKENIZER.eos_token_id,
            pad_token_id=TOKENIZER.pad_token_id,
            use_cache=False,                # <<< disable KV cache to avoid seen_tokens issue
        )

    # Only take tokens after the prompt
    new_tokens = outputs[0, prompt_len:]
    predicted = TOKENIZER.decode(new_tokens, skip_special_tokens=True)
    
    return predicted.strip()


def _model_max_ctx():
    """Get a reasonable max context length for this model."""
    max_ctx = getattr(MODEL.config, "max_position_embeddings", None)
    if max_ctx is None or max_ctx <= 0:
        max_ctx = getattr(TOKENIZER, "model_max_length", 2048)
    if max_ctx is None or max_ctx <= 0:
        max_ctx = 2048
    return int(max_ctx)
    


# Compare predicted data to actual "new"
def _compare(predicted, actual):
    """
    Compute rsync-style comparison metrics and a simple 'residual'.

    We treat 'residual' as the concatenation of all changed segments in `actual`
    relative to `predicted` (via difflib.SequenceMatcher). This is a crude,
    lower-bound approximation of what you'd need to send on top of the
    model's prediction to recover the true 'new' content.

    Returns:
        metrics (dict), residual (str)
    """
    if predicted is None:
        predicted = ""
    if actual is None:
        actual = ""

    # Byte sizes
    new_bytes = len(actual.encode("utf-8"))
    pred_bytes = len(predicted.encode("utf-8"))

    # Compute changed segments using SequenceMatcher
    sm = difflib.SequenceMatcher(a=predicted, b=actual)
    changed_segments = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        # Take the corresponding segment from the actual (new) string
        changed_segments.append(actual[j1:j2])

    residual = "".join(changed_segments)
    residual_bytes = len(residual.encode("utf-8"))
    residual_len = len(residual)

    # Approximate "percent predicted" as the fraction of new_bytes not covered by residual
    if new_bytes > 0:
        percent_predicted = max(0.0, 1.0 - (residual_bytes / new_bytes)) * 100.0
    else:
        percent_predicted = 0.0

    exact_match = int(predicted == actual)

    metrics = {
        "new_bytes": new_bytes,
        "pred_bytes": pred_bytes,
        "residual_len": residual_len,
        "residual_bytes": residual_bytes,
        "percent_predicted": percent_predicted,
        "exact_match": exact_match,
    }

    return metrics, residual


# Write metrics results to CSV
def _save_results(results):
    """
    Results rows contain:
        index, old_len, new_len, pred_len,
        new_bytes, pred_bytes, residual_len, residual_bytes,
        percent_predicted, exact_match
    """
    if not results:
        print("No results to save.")
        return

    os.makedirs(os.path.dirname(METRICS_FILE), exist_ok=True)

    # Collect all keys to be safe, but keep a stable ordering for important fields
    fieldnames = [
        "index",
        "old_len",
        "new_len",
        "pred_len",
        "new_bytes",
        "pred_bytes",
        "residual_len",
        "residual_bytes",
        "percent_predicted",
        "exact_match",
    ]
    # Add any unexpected keys at the end
    extra_keys = sorted({k for r in results for k in r.keys()} - set(fieldnames))
    fieldnames += extra_keys

    with open(METRICS_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"Saved metrics to {METRICS_FILE}")


# Write residuals to JSONL
def _save_residual(residuals):
    """
    Save residuals (index + residual string) to a JSONL file for later analysis
    and comparison vs rsync residuals.
    """
    if not residuals:
        print("No residuals to save.")
        return

    os.makedirs(os.path.dirname(RESIDUAL_FILE), exist_ok=True)

    with open(RESIDUAL_FILE, "w", encoding="utf-8") as f:
        for rec in residuals:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Saved residuals to {RESIDUAL_FILE}")

def main():
    ap = argparse.ArgumentParser(description="Predict \"new\" output from old data")
    ap.add_argument("--data_file", required=True, help="JSONL of {old,new,} pairs")
    ap.add_argument("--metrics", required=False, help="File to save metric results")
    ap.add_argument("--residuals", required=False, help="File to save residuals")
    ap.add_argument("--add_len", action="store_true", help="Provide \"new\" length to prompt for prediction")
    ap.add_argument("--stop_after", type=int, default=sys.maxsize, help="Number of lines to read")
    args = ap.parse_args()
    
    # Check if dataset is valid
    data = args.data_file
    if not os.path.isfile(data):
        print(f'Invalid data file path: {data}')
        return
    
    # Get output paths (optional)
    global METRICS_FILE
    global RESIDUAL_FILE
    if args.metrics is not None:
        METRICS_FILE = args.metrics
    if args.residuals is not None:
        RESIDUAL_FILE = args.residuals

    # Get flag for prompting length
    len_prompt = args.add_len

    # Get stop after var
    stop_after = args.stop_after
    
    # Open dataset and run LLM
    _open_data(data, len_prompt, stop_after)

if __name__ == "__main__":
    main()