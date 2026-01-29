#!/usr/bin/env python3
# scripts/rsync_dir_formater.py

import os, json
from pathlib import Path

OLD_DIR = Path("work/rsync_old")
NEW_DIR = Path("work/rsync_new")
OLD_DIR.mkdir(exist_ok=True)
NEW_DIR.mkdir(exist_ok=True)

with open("work/code_changes.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        rec = json.loads(line)
        old = rec["old"]
        new = rec["new"]
        file_id = rec.get("id", i)

        # give them some extension so editors/rsync don't care
        old_path = OLD_DIR / f"sample_{file_id:06d}.txt"
        new_path = NEW_DIR / f"sample_{file_id:06d}.txt"

        old_path.write_text(old, encoding="utf-8")
        new_path.write_text(new, encoding="utf-8")