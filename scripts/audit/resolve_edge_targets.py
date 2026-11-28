#!/usr/bin/env python3
"""Turn name-form edge targets into slugs and apply the relation renames.

  python3 scripts/audit/resolve_edge_targets.py          # dry run: reports/audit/edge-resolution.csv
  python3 scripts/audit/resolve_edge_targets.py --apply  # rewrite only rows marked resolved / renamed

A target is resolved only when it matches exactly one English title, that page is not the
source page, and the edge's target_type agrees with the target page's type.
"""
import json, os, re, sys
from inventory import EDGE, N, OUT, ROOT, load, target_status, title_index, write

TYPES_EN = {}  # target_type label -> page types seen for it, learned from edges that already use slugs


def main(apply):
    pages = load("en")
    idx = title_index(pages)
    renames = {k: v for k, v in json.load(open(os.path.join(ROOT, "scripts", "schema", "relations.json"),
                                               encoding="utf-8"))["_renames"].items() if k != v}
    rows, plan = [], {}
    for slug, p in pages.items():
        for rel, tgt, ttype in p["edges"]:
            st, hit = target_status(tgt, pages, idx)
            new_rel, new_tgt, status = renames.get(rel, rel), tgt, st
            if st == "name-exact":
                if hit == slug:
                    status = "self"
                elif ttype and pages[hit]["type"] and N(ttype) != N(pages[hit]["type"]):
                    status = "type-mismatch"
                else:
                    status, new_tgt = "resolved", hit
            rows.append([slug, rel, new_rel, tgt, hit, ttype, pages[hit]["type"] if hit else "", status])
            if new_rel != rel or new_tgt != tgt:
                plan.setdefault(slug, {})[(rel, tgt, ttype)] = (new_rel, new_tgt)
    os.makedirs(OUT, exist_ok=True)
    if not apply:
        write("edge-resolution.csv", "page rel new_rel old_target candidate target_type candidate_type status".split(), rows)
    count = {}
    for r in rows:
        count[r[-1]] = count.get(r[-1], 0) + 1
    print(count, "| relation renames:", sum(r[1] != r[2] for r in rows), "| pages to change:", len(plan))
    if not apply:
        return
    changed = 0
    for slug, edits in plan.items():
        path = os.path.join(ROOT, pages[slug]["path"])
        text = open(path, encoding="utf-8", newline="").read()
        head_end = text.index("\n---", 3)

        def sub(m):
            new = edits.get(m.groups())
            if not new:
                return m[0]
            s, base = m[0], m.start()
            for g, value in ((2, new[1]), (1, new[0])):  # right to left keeps offsets valid
                s = s[:m.start(g) - base] + value + s[m.end(g) - base:]
            return s

        out = EDGE.sub(sub, text[:head_end]) + text[head_end:]
        if out != text:
            open(path, "w", encoding="utf-8", newline="").write(out)
            changed += 1
    print("files changed:", changed)


if __name__ == "__main__":
    main("--apply" in sys.argv)
