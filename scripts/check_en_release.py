#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_en_release.py — English release gate + scope registry (audit P0-04, P0.4/P0.5, P2.1, P1.5).

Reads content/en/ with the same tolerant reader the builder uses, and reports:
  parse warnings, placeholders, missing title/part/crumb, duplicate ids, filename/slug mismatch,
  unresolved related/edges targets (EN only), pending markers, short bodies,
  and source-vs-output consistency (data-en.json / index-en.html).

Outputs:
  reports/en-release-check.json        machine-readable counts + examples
  reports/en-scope-registry.csv        one row per file: module, status, flags, words

Usage:
  python scripts/check_en_release.py            # report only, exit 0
  python scripts/check_en_release.py --strict   # exit 1 if any release blocker exists
"""
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from atlas_frontmatter import parse_frontmatter  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN = os.path.join(ROOT, "content", "en")
PLACEHOLDER = "[EN TRANSLATION NEEDED]"
CRUMB_MODULES = {
    "psychology": "psychology", "philosophy": "philosophy", "sociology": "sociology",
    "anthropology": "anthropology", "linguistics": "linguistics", "historiography": "historiography",
    "history": "historiography", "political economy": "political-economy",
    "religious studies": "religious-studies", "comparative religion": "religious-studies",
    "legal theory": "legal-theory", "ethics": "ethics", "psychiatry": "psychiatry",
    "arab thought": "arab-thought", "bridges": "bridges", "bridge": "bridges",
}
STUB_RE = re.compile(r"\[Brief description|for translator reference", re.I)
PENDING_RE = re.compile(r"\bpending\b", re.I)
SLUGISH = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def load():
    nodes, warns = {}, []
    for root, dirs, files in os.walk(EN):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("drafts", "_merged")]
        for f in files:
            if not f.endswith(".md") or f.startswith("._") or f.upper() == "README.MD":
                continue
            path = os.path.join(root, f)
            text = open(path, encoding="utf-8").read()
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
            if not m:
                continue
            node, w = parse_frontmatter(m.group(1), path)
            warns += [(os.path.relpath(path, ROOT), ln, t) for ln, t in w]
            body = re.sub(r"<!--.*?-->", "", m.group(2), flags=re.S)
            node["_body"] = body
            node["_file"] = os.path.relpath(path, ROOT).replace("\\", "/")
            node["_fslug"] = os.path.splitext(f)[0]
            nodes[node["_fslug"]] = node
    return nodes, warns


def module_of(n):
    part = n.get("part")
    if part:
        return part, "explicit"
    crumb = str(n.get("crumb") or "")
    head = crumb.split("←")[0].strip().lower()
    if head in CRUMB_MODULES:
        return CRUMB_MODULES[head], "crumb"
    return "unclassified", "none"


def main():
    strict = "--strict" in sys.argv
    nodes, warns = load()
    ids = defaultdict(list)
    c = Counter()
    ex = defaultdict(list)

    def flag(name, slug):
        c[name] += 1
        if len(ex[name]) < 15:
            ex[name].append(slug)

    rows = []
    for slug, n in nodes.items():
        ids[n.get("id")].append(slug)
        text_fields = [str(n.get(k, "")) for k in ("title", "en", "crumb")] + [n["_body"]]
        ph = any(PLACEHOLDER in t or STUB_RE.search(t) for t in text_fields)
        title = str(n.get("title") or "")
        flags = []
        if ph:
            flags.append("placeholder"); flag("placeholder", slug)
        if not title or PLACEHOLDER in title:
            flags.append("no-title"); flag("no-title", slug)
        mod, how = module_of(n)
        if how != "explicit":
            flags.append("part-not-explicit"); flag("part-not-explicit", slug)
        if mod == "unclassified":
            flag("unclassified", slug)
        if n.get("slug") and n["slug"] != slug:
            flags.append("slug-mismatch"); flag("slug-mismatch", slug)
        if not n.get("crumb"):
            flags.append("no-crumb"); flag("no-crumb", slug)
        pend = bool(PENDING_RE.search(n["_body"])) or any(PENDING_RE.search(g) for g in n.get("gaps", []))
        if pend:
            flags.append("pending"); flag("pending", slug)
        words = len(n["_body"].split())
        if words < 150:
            flags.append("short"); flag("short", slug)
        # relations
        for r in n.get("related", []):
            if r[0] not in nodes:
                flags.append("related-unresolved"); flag("related-unresolved", f"{slug}->{r[0]}")
        for e in n.get("edges", []):
            if SLUGISH.match(e[1]) and e[1] not in nodes:
                flag("edge-target-slug-unresolved", f"{slug}->{e[1]}")
            elif not SLUGISH.match(e[1]):
                flag("edge-target-by-name", f"{slug}->{e[1]}")
        if ph:
            status = "placeholder"
        elif pend:
            status = "draft-pending"
        elif words < 150:
            status = "draft-short"
        else:
            status = "review-candidate"  # NOT reviewed: needs source verification
        rows.append([slug, n.get("id"), n.get("type"), mod, how, status, ";".join(sorted(set(flags))), words, n["_file"]])

    dup = {k: v for k, v in ids.items() if k and len(v) > 1}
    c["duplicate-id-groups"] = len(dup)

    out_consistency = {}
    jp = os.path.join(ROOT, "data-en.json")
    if os.path.exists(jp):
        built = json.load(open(jp, encoding="utf-8")).get("nodes", {})
        out_consistency["data-en.json nodes"] = len(built)
        out_consistency["source nodes"] = len(nodes)
        out_consistency["missing from output"] = len(set(nodes) - set(built))
        out_consistency["stale in output (no source)"] = len(set(built) - set(nodes))
    hp = os.path.join(ROOT, "index-en.html")
    if os.path.exists(hp):
        head = open(hp, encoding="utf-8").read(3000)
        out_consistency["html lang/dir"] = re.search(r"<html[^>]*>", head).group(0) if "<html" in head else "?"

    status_counts = Counter(r[5] for r in rows)
    by_module = defaultdict(Counter)
    for r in rows:
        by_module[r[3]][r[5]] += 1

    report = {
        "total_files": len(nodes),
        "parse_warnings": len(warns),
        "parse_warning_examples": [f"{p}:{ln}: {t[:70]}" for p, ln, t in warns[:15]],
        "flag_counts": dict(c),
        "flag_examples": dict(ex),
        "duplicate_ids": dup,
        "status_counts": dict(status_counts),
        "by_module": {k: dict(v) for k, v in sorted(by_module.items())},
        "output_consistency": out_consistency,
    }
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    json.dump(report, open(os.path.join(ROOT, "reports", "en-release-check.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    with open(os.path.join(ROOT, "reports", "en-scope-registry.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["slug", "id", "type", "module", "module_source", "status", "flags", "words", "file"])
        w.writerows(sorted(rows))

    print(f"EN files: {len(nodes)}   parse warnings: {len(warns)}")
    print("status:", dict(status_counts))
    for k in sorted(c):
        print(f"  {k}: {c[k]}")
    if dup:
        print("duplicate ids:", dup)
    print("output consistency:", out_consistency)

    blockers = (len(warns) + c["placeholder"] + c["no-title"] + c["related-unresolved"]
                + c["pending"] + len(dup) + c["slug-mismatch"])
    if out_consistency.get("missing from output") or out_consistency.get("stale in output (no source)"):
        blockers += 1
    print("BLOCKERS" if blockers else "CLEAN", blockers)
    if strict and blockers:
        sys.exit(1)


if __name__ == "__main__":
    main()
