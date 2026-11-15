#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_en_scope_matrix.py — module-level scope matrix (audit P0.5): EN status counts per module vs
Arabic asset counts (AR part field, read-only inventory — not a target count). Writes
reports/en-scope-matrix.md. Run check_en_release.py first (reads reports/en-scope-registry.csv)."""
import collections, csv, os, re, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODULES = ["psychology","philosophy","sociology","anthropology","linguistics","political-economy","historiography",
           "religious-studies","legal-theory","ethics","psychiatry","arab-thought","bridges"]
AR_ALIAS = {"history":"historiography","political_economy":"political-economy","religious_studies":"religious-studies",
            "legal_theory":"legal-theory","arab_thought":"arab-thought","bridge":"bridges"}
def ar_counts():
    c = collections.Counter(); base = os.path.join(ROOT, "content", "ar")
    for root, dirs, fs in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("drafts","_merged")]
        for f in fs:
            if not f.endswith(".md") or f.startswith("._"): continue
            head = open(os.path.join(root, f), encoding="utf-8", errors="replace").read(1500)
            m = re.search(r'^part:\s*["\']?([\w-]+)', head, re.M)
            p = m.group(1).lower() if m else "unclassified"
            c[AR_ALIAS.get(p, p)] += 1
    return c
def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT,"reports","en-scope-registry.csv"),encoding="utf-8")))
    en = collections.defaultdict(collections.Counter)
    for r in rows: en[r["module"]][r["status"]] += 1
    ar = ar_counts()
    out = ["# EN scope matrix (generated)", "",
           "EN counts come from `check_en_release.py`; AR counts are an inventory of existing Arabic assets, not targets.",
           "`review-candidate` means no automatic flag, NOT reviewed.", "",
           "| module | EN total | placeholder | draft | review-candidate | AR assets | next action |","|---|--:|--:|--:|--:|--:|---|"]
    for m in MODULES + sorted(set(en) - set(MODULES)):
        e = en.get(m, collections.Counter()); tot = sum(e.values())
        draft = e["draft-pending"] + e["draft-short"]
        act = ("define scope list, then author/review" if tot == 0 else
               "source review + close drafts" if e["review-candidate"] else "complete drafts")
        out.append(f"| {m} | {tot} | {e['placeholder']} | {draft} | {e['review-candidate']} | {ar.get(m,0)} | {act} |")
    out.append(f"| (AR unclassified) |  |  |  |  | {ar.get('unclassified',0)} | classify before counting coverage |")
    open(os.path.join(ROOT,"reports","en-scope-matrix.md"),"w",encoding="utf-8").write("\n".join(out)+"\n")
    print("\n".join(out))
main()
