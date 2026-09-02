# -*- coding: utf-8 -*-
"""يتحقق أن كل تصحيح في thinkers_audit_fixes.json انطبق فعلاً (النص القديم اختفى والجديد حاضر)."""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
THK  = os.path.join(ROOT, "content", "ar", "thinkers")
FIX  = json.load(open(os.path.join(os.path.dirname(__file__), "thinkers_audit_fixes.json"), encoding="utf-8"))
only = set(sys.argv[1:])
bad = 0
for fn, subs in FIX.items():
    if only and fn not in only: continue
    p = os.path.join(THK, fn)
    if not os.path.exists(p):
        print("MISSING FILE", fn); bad += 1; continue
    t = open(p, encoding="utf-8").read()
    for a, b in subs:
        if b and b not in t:
            print("NOT APPLIED", fn, "|", a[:70].replace("\n", "\\n")); bad += 1
        elif not b and a in t:
            print("NOT REMOVED", fn, "|", a[:70].replace("\n", "\\n")); bad += 1
print("unapplied:", bad)
