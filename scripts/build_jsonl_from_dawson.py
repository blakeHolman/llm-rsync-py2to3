from pathlib import Path
import json

pairs = []
py2_dir = Path("work/py2_programs")
py3_dir = Path("work/py3_programs")

for py2_path in sorted(py2_dir.glob("*.py")):
    py3_path = py3_dir / py2_path.name
    if py3_path.exists():
        old = py2_path.read_text(encoding="utf-8")
        new = py3_path.read_text(encoding="utf-8")
        pairs.append({"id": py2_path.stem, "old": old, "new": new})

with open("work/anne_dawson_py2_to_py3.jsonl", "w", encoding="utf-8") as f:
    for ex in pairs:
        f.write(json.dumps(ex) + "\n")
