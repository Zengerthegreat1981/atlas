#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_en_related.py — resolve EN `related` items whose id has no EN file (audit §6.1.2).

For each unresolved item:
  1. unique fuzzy candidate in EN (same type prefix, slug tokens contained) -> repoint (logged)
  2. otherwise remove the item from the EN file (logged, restorable) — the target is not in the
     EN scope yet; re-add when the node is created. Arabic tree is never consulted/modified.
Edits only the `related:` block lines; everything else is left byte-identical.
Writes reports/en-related-decisions.csv. Use --dry to preview.
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN = os.path.join(ROOT, "content", "en")
ITEM_ID = re.compile(r'^(\s*-\s*id:\s*)(["\']?)([^"\',\s]+)\2')


def files():
    for root, dirs, fs in os.walk(EN):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("drafts", "_merged")]
        for f in fs:
            if f.endswith(".md") and not f.startswith("._") and f.upper() != "README.MD":
                yield os.path.join(root, f)


def candidate(tid, slugs):
    pre = tid.split("-", 1)[0]
    toks = set(tid.split("-")[1:])
    if not toks:
        return None
    c = [s for s in slugs if s.split("-", 1)[0] == pre and toks <= set(s.split("-")[1:])]
    return c[0] if len(c) == 1 else None


def main():
    dry = "--dry" in sys.argv
    paths = list(files())
    slugs = {os.path.splitext(os.path.basename(p))[0] for p in paths}
    log = []
    for p in paths:
        text = open(p, encoding="utf-8", newline="").read()
        m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n.*)$", text, re.S)
        if not m:
            continue
        fm_lines = m.group(2).split("\n")
        out, in_rel, changed = [], False, False
        slug = os.path.splitext(os.path.basename(p))[0]
        i = 0
        while i < len(fm_lines):
            line = fm_lines[i]
            if re.match(r"^related:\s*$", line.rstrip("\r")):
                in_rel = True
                out.append(line); i += 1; continue
            if in_rel and re.match(r"^[A-Za-z_][\w-]*:", line):
                in_rel = False
            if in_rel:
                im = ITEM_ID.match(line)
                if im:
                    tid = im.group(3)
                    # gather continuation lines (multi-line item)
                    j = i + 1
                    cont = []
                    while j < len(fm_lines) and fm_lines[j][:1].isspace() and not re.match(r"^\s*-\s", fm_lines[j]):
                        cont.append(fm_lines[j]); j += 1
                    if tid not in slugs:
                        cand = candidate(tid, slugs)
                        if cand:
                            out.append(line.replace(tid, cand, 1)); out.extend(cont)
                            log.append([os.path.relpath(p, ROOT), tid, "repointed", cand])
                        else:
                            log.append([os.path.relpath(p, ROOT), tid, "removed", ""])
                        changed = True
                        i = j
                        continue
            out.append(line); i += 1
        if changed and not dry:
            new = m.group(1) + "\n".join(out) + m.group(3)
            open(p, "w", encoding="utf-8", newline="").write(new)
    if not dry:
        os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
        with open(os.path.join(ROOT, "reports", "en-related-decisions.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["file", "unresolved_id", "decision", "new_id"])
            w.writerows(log)
    from collections import Counter
    print(Counter(r[2] for r in log), "files:", len({r[0] for r in log}))


if __name__ == "__main__":
    main()
