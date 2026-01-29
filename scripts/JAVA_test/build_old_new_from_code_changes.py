#!/usr/bin/env python3
# scripts/build_old_new_from_code_changes.py

import argparse
import json
import os

from datasets import load_dataset

DEFAULT_OUTPUT_PATH = "../work/code_changes_old_new_pairs.jsonl"


def build_pairs(output_path: str):
    """
    Load the CodeXGLUE code refinement dataset and write {old,new} JSONL lines.
    old  = buggy code
    new  = fixed code
    """
    print("Loading dataset google/code_x_glue_cc_code_refinement (medium)...")
    ds = load_dataset("google/code_x_glue_cc_code_refinement", "medium")

    # Open output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    count = 0
    with open(output_path, "w", encoding="utf-8") as out_f:
        # Iterate over splits if they exist
        for split_name in ["train", "validation", "test", "valid"]:
            if split_name not in ds:
                continue
            split = ds[split_name]
            print(f"Writing split '{split_name}' with {len(split)} examples...")

            for example in split:
                buggy = example.get("buggy")
                fixed = example.get("fixed")

                if buggy is None or fixed is None:
                    continue

                rec = {
                    "old": buggy,
                    "new": fixed,
                    "split": split_name,
                }
                out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                count += 1

    print(f"Done. Wrote {count} examples to {output_path}.")


def main():
    ap = argparse.ArgumentParser(description="Build OLD→NEW pairs for training from CodeXGLUE code refinement dataset")
    ap.add_argument("--out", required=False, help="Output JSONL of {old,new} pairs")
    args = ap.parse_args()

    output_path = args.out if args.out is not None else DEFAULT_OUTPUT_PATH
    build_pairs(output_path)


if __name__ == "__main__":
    main()