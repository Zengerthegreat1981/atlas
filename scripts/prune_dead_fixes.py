# -*- coding: utf-8 -*-
"""يحذف من ledger التصحيحات الأزواجَ الميتة: التي لم يعد نصُّها القديم ولا الجديد موجوداً في الملف
(أي أن جلسةً أخرى أعادت كتابة المقطع، فصار الزوج غير قابل للإعادة). --apply لتنفيذ الحذف."""
import io, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
THK  = os.path.join(ROOT, "content", "ar", "thinkers")
P    = os.path.join(os.path.dirname(__file__), "thinkers_audit_fixes.json")
FIX  = json.load(io.open(P, encoding="utf-8"))
apply = "--apply" in sys.argv
only  = set(a for a in sys.argv[1:] if a.endswith(".md"))
dead = 0
out = {}
for fn, subs in FIX.items():
    p = os.path.join(THK, fn)
    if (only and fn not in only) or not os.path.exists(p):
        out[fn] = subs; continue
    t = io.open(p, encoding="utf-8").read()
    keep = []
    for a, b in subs:
        if a not in t and b and b not in t:
            print("DEAD", fn, "|", a[:60].replace("\n", "\\n")); dead += 1
        else:
            keep.append([a, b])
    if keep: out[fn] = keep
print("dead pairs:", dead, "| apply:", apply)
if apply:
    json.dump(out, io.open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ledger now holds", sum(len(v) for v in out.values()), "across", len(out), "files")
