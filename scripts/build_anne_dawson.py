#!/usr/bin/env python3
import re
from pathlib import Path

# run from home code dir

INPUT = "data/anne_dawson_py2/pythonprograms.txt"
OUTDIR = Path("work/py2_programs")
OUTDIR.mkdir(exist_ok=True)

# Matches lines like:
#   #01-01.py
#   #01-01.py  print "Hello World!"
#   # File: 04-01.py
#   # Program: 04-13.py
header_re = re.compile(
    r'^\s*#\s*(?:File:\s*|Program:\s*)?(\d{2}-\d{2}\.py)\s*(.*)$',
    re.IGNORECASE,
)

def flush(current_name, current_lines):
    if current_name and current_lines:
        # Remove trailing blank/whitespace-only lines
        while current_lines and current_lines[-1].strip() == "":
            current_lines.pop()

        if not current_lines:
            return None, []

        out_path = OUTDIR / current_name
        # Join, strip trailing newlines, then add exactly one at the end
        text = "".join(current_lines).rstrip() + "\n"

        print(f"Writing {out_path}")
        out_path.write_text(text, encoding="utf-8")

    return None, []

current_name = None
current_lines = []

with open(INPUT, encoding="utf-8") as f:
    for raw_line in f:
        line = raw_line.rstrip("\n")

        m = header_re.match(line)
        if m:
            # Start a new file
            current_name, current_lines = flush(current_name, current_lines)
            filename = m.group(1)
            rest = m.group(2)  # any code after the header on the same line

            current_name = filename
            # Optionally keep the header as a comment in the file:
            current_lines.append(f"# {filename}\n")

            if rest.strip():
                # If there is code after the header, put it on its own line
                current_lines.append(rest.lstrip() + "\n")
        else:
            # Ordinary line, just add it to the current file (if any)
            if current_name is not None:
                current_lines.append(raw_line)

# Flush the last file
flush(current_name, current_lines)
