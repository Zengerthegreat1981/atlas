#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_scope.py <module> <quota-json> <new-json> — generate scripts/scope/<module>_scope.py from
reports/scope/<module>-candidates.csv (run select_scope.py first), the translate work list
reports/scope/<module>-translate.json and batch files in the scratchpad (<prefix>t<i>.txt)."""
import csv, collections, glob, json, os, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
mod, quota, new, sp, prefix, per = sys.argv[1], json.loads(sys.argv[2]), json.loads(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6])
rows = list(csv.DictReader(open(f"{ROOT}/reports/scope/{mod}-candidates.csv", encoding="utf-8")))
en = {os.path.basename(p)[:-3] for p in glob.glob(f"{ROOT}/content/en/*/*.md")}
by = collections.defaultdict(list)
for r in rows:
    if int(r["ar_words"]) >= 300: by[r["folder"]].append(r)
sel = {f: [r for r in sorted(by[f], key=lambda r: (-int(r["inbound"]), -int(r["ar_words"])))[:n]] for f, n in quota.items()}
def block(l):
    out, line = [], ""
    for s in l:
        if len(line) + len(s) > 110: out.append(line.strip()); line = ""
        line += s + " "
    out.append(line.strip()); return "\n".join(out)
txt = f"# Closed v1 scope for the English {mod} module (selected from AR assets by inbound links; AR slugs/ids reused).\nSCOPE = {{\n"
for f, l in sel.items(): txt += f'"{f}": """{block([r["slug"] for r in l])}""",\n'
txt += "}\nNEW = {\n" + "".join(f' "{k}": {tuple(v)!r},\n' for k, v in new.items()) + "}\n"
open(f"{ROOT}/scripts/scope/{mod}_scope.py", "w", encoding="utf-8").write(txt)
items = []
for f, l in sel.items():
    for r in l:
        if r["slug"] in en: continue
        items.append([r["slug"], r["ar_file"], f"content/en/{r['folder']}/{r['slug']}.md", f])
json.dump(items, open(f"{ROOT}/reports/scope/{mod}-translate.json", "w"), indent=0)
k = max(1, round(len(items) / per))
for i in range(k):
    open(f"{sp}/{prefix}{i}.txt", "w").write("\n".join("|".join(x[:3]) for x in items[i::k]))
open(f"{sp}/{prefix}new.txt", "w").write("\n".join(f"{s}|content/en/{v[0]}/{s}.md|{v[1]}|{v[2]}" for s, v in new.items()))
print(mod, len(items), "batches", k)
