#!/usr/bin/env python3
# scripts/test/test_residuals.py

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.residuals import get_residual, apply_residual

old = "# 03-02.py\n\nsum = 10\nprint sum\n"
pred = "# 03-02.py\n\nsum = 10\nprint(sum)"     # missing final \n
new  = "# 03-02.py\n\nsum = 10\nprint(sum)\n"

patch = get_residual(new, pred)
print(patch)
rebuilt = apply_residual(pred, patch)
print(rebuilt)
assert rebuilt == new.encode("utf-8")