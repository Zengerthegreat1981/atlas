#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""auto_paths.py <part> <root-slug> — write scripts/scope/<part>_paths.json: field intros first, then the
largest entries per type (file size as an importance proxy) for modules without a hand-curated path list."""
import glob, json, os, re, sys
part, root = sys.argv[1], sys.argv[2]
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
bytype, fields = {}, []
for p in glob.glob(f"{ROOT}/content/en/*/*.md"):
    s = open(p, encoding="utf-8").read(2500)
    if not re.search(rf'^part:\s*"?{re.escape(part)}', s, re.M): continue
    sl = os.path.basename(p)[:-3]; folder = p.replace(chr(92), "/").split("/")[-2]
    if sl.startswith("fld-"):
        if sl != root: fields.append(sl)
    else: bytype.setdefault(folder, []).append((os.path.getsize(p), sl))
labels = {"schools": "Schools and Approaches", "branches": "Branches", "thinkers": "Key Figures", "concepts": "Core Concepts",
          "works": "Landmark Works", "studies": "Studies and Evidence", "debates": "Major Debates"}
paths = [["Start Here: Fields", sorted(fields)]]
for f, lab in labels.items():
    top = [s for _, s in sorted(bytype.get(f, []), reverse=True)[:12]]
    if top: paths.append([lab, top])
json.dump({"root": root, "root_folder": "fields", "paths": paths}, open(f"{ROOT}/scripts/scope/{part}_paths.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(part, sum(len(p[1]) for p in paths))
