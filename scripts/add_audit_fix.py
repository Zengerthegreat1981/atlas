# -*- coding: utf-8 -*-
"""يضيف تصحيحات جديدة لملف thinkers_audit_fixes.json من stdin (JSON) ثم يطبّقها."""
import json, sys, os
P = os.path.join(os.path.dirname(__file__), "thinkers_audit_fixes.json")
cur = json.load(open(P, encoding="utf-8"))
new = json.load(sys.stdin)
added = 0
for fn, subs in new.items():
    cur.setdefault(fn, [])
    have = {tuple(x) for x in cur[fn]}
    for a, b in subs:
        if (a, b) not in have:
            cur[fn].append([a, b]); added += 1
json.dump(cur, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"added {added} fixes; file now holds {sum(len(v) for v in cur.values())} across {len(cur)} files")
