#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""assign_en_part.py — write an explicit `part:` into EN files that lack one (audit P0.4).
Derived from the crumb head (see MAP); unmapped files are listed, not guessed. Logs to
reports/en-part-assignments.csv. Inserts the line right after `type:`; nothing else changes."""
import csv, os, re, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN = os.path.join(ROOT, "content", "en")
MAP = {
 "psychology":"psychology","philosophy":"philosophy","sociology":"sociology","anthropology":"anthropology",
 "linguistics":"linguistics","historiography":"historiography","history":"historiography",
 "existential philosophy":"philosophy","existential school":"philosophy","existentialist school":"philosophy",
 "existentialism":"philosophy",
 "existential psychotherapy":"psychology","existential therapy":"psychology","humanistic psychology":"psychology",
 "emotion psychology":"psychology","symbolic anthropology":"anthropology","structural anthropology":"anthropology",
}
EXISTENTIAL_THEMES = {  # single-theme crumbs under the existential-psychotherapy module
 "aging","authenticity-inauthenticity","being and becoming","choice and constraint","depression","despair",
 "existential crises","fulfillment","grief","hope","individuation","love","meaninglessness","mortality",
 "presence and absence","rage","relationships","resilience","self and other","shame",
}
BY_SLUG = {  # manual decisions for crumbs that name a sub-field instead of a module
 "con-spiritual-crisis":"psychology","con-therapy":"psychology","con-trauma":"psychology",
 "ctx-arabic-self":"arab-thought","stu-ekman-original-facial":"psychology","stu-terror-management-theory":"psychology",
 "thk-carlos-castaneda":"psychology","thk-husserl":"philosophy","thk-nietzsche":"philosophy","thk-tillich":"philosophy",
 "thk-natalie-zemon-davis":"historiography",
 "stu-evans-pritchard-the-nuer":"anthropology","stu-leach-political-systems-highlands-burma":"anthropology",
 "thk-arnold-van-gennep":"anthropology","thk-clifford-geertz":"anthropology","thk-sherry-ortner":"anthropology",
 "thk-ulf-hannersson":"anthropology","wrk-coming-of-age-samoa-mead":"anthropology","wrk-elementary-structures":"anthropology",
 "wrk-forest-symbols":"anthropology","wrk-hawaiian-kinship":"anthropology","wrk-interpretation-of-cultures-geertz":"anthropology",
 "wrk-kinship-and-marriage":"anthropology","wrk-kung-bushmen":"anthropology","wrk-patterns-of-culture-benedict":"anthropology",
 "wrk-savage-mind":"anthropology","wrk-the-gift":"anthropology","wrk-tiwi-wives":"anthropology","wrk-totemism":"anthropology",
}
def main():
    log, unmapped = [], []
    old = os.path.join(ROOT, "reports", "en-part-assignments.csv")
    if os.path.exists(old):
        log = [r for r in list(csv.reader(open(old, encoding="utf-8")))[1:]]
    for root, dirs, fs in os.walk(EN):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("drafts", "_merged")]
        for f in fs:
            if not f.endswith(".md") or f.startswith("._") or f.upper() == "README.MD": continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf-8", newline="").read()
            m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n.*)$", t, re.S)
            if not m or re.search(r"^part:", m.group(2), re.M): continue
            cm = re.search(r"^crumb:\s*(.*)$", m.group(2), re.M)
            head = (cm.group(1).strip().strip("\"'").split("←")[0].strip().lower() if cm else "")
            part = BY_SLUG.get(os.path.splitext(f)[0]) or MAP.get(head) or ("psychology" if head in EXISTENTIAL_THEMES else None)
            if not part:
                unmapped.append((os.path.relpath(p, ROOT), head)); continue
            nl = "\r\n" if "\r\n" in m.group(2) else "\n"
            new_fm, n = re.subn(r"^(type:.*)$", lambda mm: mm.group(1).rstrip("\r") + nl + f'part: {part}', m.group(2), count=1, flags=re.M)
            if not n: unmapped.append((os.path.relpath(p, ROOT), "no-type-line")); continue
            open(p, "w", encoding="utf-8", newline="").write(m.group(1) + new_fm + m.group(3))
            log.append([os.path.relpath(p, ROOT).replace("\\","/"), part, head])
    with open(os.path.join(ROOT, "reports", "en-part-assignments.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh); w.writerow(["file","part","crumb_head"]); w.writerows(log)
    print("assigned", len(log), "unmapped", len(unmapped))
    for u in unmapped[:40]: print(" ", u)
main()
