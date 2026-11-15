#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""select_scope.py <module> — candidate scope list from the Arabic inventory (read-only), ranked by
inbound links and body length; excludes merged stubs and slugs already in EN.
Writes reports/scope/<module>-candidates.csv."""
import csv, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from atlas_frontmatter import parse_frontmatter
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
mod = sys.argv[1]
def walk(lang):
    for root, dirs, fs in os.walk(os.path.join(ROOT, "content", lang)):
        dirs[:] = [d for d in dirs if d not in ("drafts", "_merged") and not d.startswith(".")]
        for f in fs:
            if f.endswith(".md") and not f.startswith("._") and f.upper() != "README.MD":
                yield os.path.join(root, f), os.path.basename(root), f[:-3]
en = {s for _, _, s in walk("en")}
nodes = {}; inbound = collections.Counter()
for p, folder, slug in walk("ar"):
    t = open(p, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$", t, re.S)
    if not m: continue
    n, _ = parse_frontmatter(m.group(1))
    body = re.sub(r"<!--.*?-->", "", m.group(2), flags=re.S)
    nodes[slug] = dict(n, _folder=folder, _words=len(body.split()), _file=os.path.relpath(p, ROOT).replace("\\", "/"), _body=body)
    for r in n.get("related", []): inbound[r[0]] += 1
rows = []
for s, n in nodes.items():
    if str(n.get("part", "")).lower() != mod: continue
    if s in en or "merged, see" in str(n.get("en", "")) or "merged" in str(n.get("title", "")).lower(): continue
    rows.append([s, n["_folder"], n.get("en") or n.get("title"), inbound[s], n["_words"], n["_file"]])
rows.sort(key=lambda r: (r[1], -r[3], -r[4]))
os.makedirs(os.path.join(ROOT, "reports", "scope"), exist_ok=True)
with open(os.path.join(ROOT, "reports", "scope", f"{mod}-candidates.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f); w.writerow(["slug", "folder", "name", "inbound", "ar_words", "ar_file"]); w.writerows(rows)
print(len(rows), collections.Counter(r[1] for r in rows))
