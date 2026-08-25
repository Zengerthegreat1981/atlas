#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
phase0_structural_fixes.py — خطوة 0.5: الأعطال البنيوية.

كل إصلاح هنا **ميكانيكي بحت** (علامة اقتباس ناقصة، مفتاح ملتصق بسطر تاني،
حقل مكرر، بادئة شاذة) — صفر تدخل في المحتوى نفسه. كل إصلاح له تحقق قبل/بعد
بـ atlas_parse.py، ولقطة git منفصلة.

الاستعمال:
    python3 scripts/phase0_structural_fixes.py --check     # يطبع الخطة بلا تنفيذ
    python3 scripts/phase0_structural_fixes.py --apply      # ينفّذ ويتحقق
"""
import os, re, sys, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap

AR = ap.AR

# --- أ) علامة اقتباس ناقصة على en: (نفس العطل بالحرف في 8 ملفات، دايماً سطر 7) ---
MISSING_QUOTE_EN = [
    "content/ar/concepts/con-harm-reduction.md",
    "content/ar/concepts/con-neuroplasticity-trauma.md",
    "content/ar/concepts/con-shinrin-yoku.md",
    "content/ar/techniques/tec-animal-assisted-therapy.md",
    "content/ar/techniques/tec-biofeedback.md",
    "content/ar/techniques/tec-cra.md",
    "content/ar/techniques/tec-forest-therapy.md",
    "content/ar/techniques/tec-progressive-counting.md",
]

# --- ب) علامة اقتباس ناقصة على crumb: ---
MISSING_QUOTE_CRUMB = ["content/ar/thinkers/thk-gengel.md"]

# --- ج) فاصلة عربية بره الاقتباس تفصل قيمتين على نفس السطر ---
STRAY_COMMA = ["content/ar/schools/sch-nahua-aztec.md"]

# --- د) مفتاح ملتصق بنهاية سطر related السابق (بلا \n).
# نوعان مختلفان يحتاجان إصلاحاً مختلفاً:
#   1) ملتصق بـ"gaps:" → انتقال شرعي لقسم جديد، الإصلاح: سطر جديد قبله.
#   2) ملتصق بـ"related:" مكرر → المفتاح ده أصلاً موجود فوق، والالتصاق هنا
#      كرّره غلطاً وسط نفس القائمة. الإصلاح: احذف "related:" الزايدة (مش
#      تفصلها بسطر جديد، ده هيعمل مفتاحين related: في نفس الـfrontmatter
#      = عطل YAML جديد بدل القديم).
GLUED_GAPS_FILES = [
    "content/ar/critiques/crt-disability-studies-critique.md",
    "content/ar/critiques/crt-feminist-critique-psychoanalysis.md",
    "content/ar/critiques/crt-popper-critique-psychoanalysis.md",
    "content/ar/critiques/crt-postcolonial-critique-psychoanalysis.md",
    "content/ar/critiques/crt-postmodern-critique.md",
    "content/ar/critiques/crt-religious-conservative-critique-psychoanalysis.md",
    "content/ar/critiques/crt-research-ethics-historical.md",
    "content/ar/critiques/crt-scientific-critique-transpersonal.md",
]
GLUED_DUP_RELATED_FILES = [
    "content/ar/critiques/crt-anti-psychiatry-critique.md",
    "content/ar/critiques/crt-commodification-critique.md",
    "content/ar/critiques/crt-critical-race-critique-psychology.md",
    "content/ar/critiques/crt-feminist-critique-behaviorism.md",
    "content/ar/critiques/crt-marxist-critique-psychology.md",
    "content/ar/critiques/crt-neurodiversity-aba-critique.md",
    "content/ar/critiques/crt-postcolonial-critique-dsm.md",
    "content/ar/critiques/crt-replication-crisis.md",
]

# --- هـ) سطر related بلا title إطلاقاً (يحتاج قيمة حقيقية، لا تخمين) ---
MISSING_TITLE_FIX = {
    "content/ar/instruments/ins-hamilton-hdrs.md": (
        '- id: "dis-major-depressive", type: "مفهوم"',
        '- id: "dis-major-depressive", title: "اضطراب الاكتئاب الجسيم", type: "اضطراب/حالة إكلينيكية"',
    )
}

# --- و) edges مكسورة: مفتاح target مكرر، أو type_type بدل target_type ---
EDGE_FIXES = {
    "content/ar/schools/sch-academic-skepticism.md": (
        '- rel: "evolved_into", target: "الانتقائية الهلنستية-الرومانية", target: "مدرسة"',
        '- rel: "evolved_into", target: "الانتقائية الهلنستية-الرومانية", target_type: "مدرسة"',
    ),
    "content/ar/schools/sch-cft.md": (
        '- rel: "developed_by", target: "paul-gilbert", target_type: "مفكر", target: "paul-gilbert"',
        '- rel: "developed_by", target: "paul-gilbert", target_type: "مفكر"',
    ),
    "content/ar/schools/sch-conservatism-philosophical.md": (
        '- rel: "belongs_to", target: "الفلسفة السياسية المعاصرة", type_type: "مظلة"',
        '- rel: "belongs_to", target: "الفلسفة السياسية المعاصرة", target_type: "مظلة"',
    ),
    "content/ar/schools/sch-motivational-interviewing.md": (
        '- rel: "developed_by", target: "stephen-rollnick", target_type: "مفكر", target: "stephen-rollnick"',
        '- rel: "developed_by", target: "stephen-rollnick", target_type: "مفكر"',
    ),
    "content/ar/schools/sch-narrative-therapy.md": (
        '- rel: "developed_by", target: "david-epston", target_type: "مفكر", target: "david-epston"',
        '- rel: "developed_by", target: "david-epston", target_type: "مفكر"',
    ),
}

# --- ز) بادئات معرفات شاذة (CLS-/NOD-) ---
STRAY_PREFIX_PATTERNS = [r'id:\s*"CLS-\d+"', r'id:\s*"NOD-\d+"']


def _p(rel):
    return os.path.join(ap.ROOT, rel)


def fix_missing_quote_en(path, apply):
    lines = open(path, encoding="utf-8").readlines()
    changed = False
    for i, l in enumerate(lines):
        if l.startswith("en:") and l.rstrip("\n").count('"') == 1:
            lines[i] = l.rstrip("\n") + '"\n'
            changed = True
    if changed and apply:
        open(path, "w", encoding="utf-8").writelines(lines)
    return changed


def fix_missing_quote_crumb(path, apply):
    lines = open(path, encoding="utf-8").readlines()
    changed = False
    for i, l in enumerate(lines):
        if l.startswith("crumb:") and l.rstrip("\n").count('"') == 1:
            lines[i] = l.rstrip("\n") + '"\n'
            changed = True
    if changed and apply:
        open(path, "w", encoding="utf-8").writelines(lines)
    return changed


def fix_stray_comma(path, apply):
    text = open(path, encoding="utf-8").read()
    new = re.sub(
        r'^language:\s*"([^"]*)"،\s*"([^"]*)"\s*$',
        r'language: "\1 / \2"',
        text, flags=re.M,
    )
    changed = new != text
    if changed and apply:
        open(path, "w", encoding="utf-8").write(new)
    return changed


def fix_glued_gaps(path, apply):
    text = open(path, encoding="utf-8").read()
    new = re.sub(r'(type: "[^"]*")(gaps:)', r"\1\n\2", text)
    changed = new != text
    if changed and apply:
        open(path, "w", encoding="utf-8").write(new)
    return changed


def fix_glued_dup_related(path, apply):
    text = open(path, encoding="utf-8").read()
    new = re.sub(r'(type: "[^"]*")related:\n', r"\1\n", text)
    changed = new != text
    if changed and apply:
        open(path, "w", encoding="utf-8").write(new)
    return changed


def fix_literal_replace(path, old, new, apply):
    text = open(path, encoding="utf-8").read()
    if old not in text:
        return False
    changed_text = text.replace(old, new)
    if apply:
        open(path, "w", encoding="utf-8").write(changed_text)
    return True


def scan_stray_prefixes():
    hits = []
    for path in ap.iter_atlas_files():
        text = open(path, encoding="utf-8", errors="replace").read()
        for pat in STRAY_PREFIX_PATTERNS:
            if re.search(pat, text):
                hits.append((path, pat))
    return hits


def main():
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("--apply", action="store_true")
    args = ap_.parse_args()
    apply = args.apply

    print(f"=== {'تنفيذ' if apply else 'معاينة (--apply للتنفيذ)'} — الأعطال البنيوية 0.5 ===\n")

    n = 0
    for rel in MISSING_QUOTE_EN:
        if fix_missing_quote_en(_p(rel), apply):
            print(f"  [en quote] {rel}"); n += 1
    for rel in MISSING_QUOTE_CRUMB:
        if fix_missing_quote_crumb(_p(rel), apply):
            print(f"  [crumb quote] {rel}"); n += 1
    for rel in STRAY_COMMA:
        if fix_stray_comma(_p(rel), apply):
            print(f"  [stray comma] {rel}"); n += 1
    for rel in GLUED_GAPS_FILES:
        if fix_glued_gaps(_p(rel), apply):
            print(f"  [glued → gaps] {rel}"); n += 1
    for rel in GLUED_DUP_RELATED_FILES:
        if fix_glued_dup_related(_p(rel), apply):
            print(f"  [glued dup related] {rel}"); n += 1
    for rel, (old, new) in MISSING_TITLE_FIX.items():
        if fix_literal_replace(_p(rel), old, new, apply):
            print(f"  [missing title] {rel}"); n += 1
    for rel, (old, new) in EDGE_FIXES.items():
        if fix_literal_replace(_p(rel), old, new, apply):
            print(f"  [edge dup-key] {rel}"); n += 1

    print(f"\nإجمالي الملفات المتأثرة: {n}")

    print("\n--- بادئات شاذة (CLS-/NOD-) — تقرير فقط، بلا تعديل تلقائي ---")
    for path, pat in scan_stray_prefixes():
        print(f"  {os.path.relpath(path, ap.ROOT)}  ({pat})")

    if apply:
        print("\n--- تحقق atlas_parse بعد التعديل ---")
        fail = relbad = edgebad = gapbad = 0
        for path in ap.iter_atlas_files():
            try:
                d = ap.parse_file(path)
                if d.related_malformed: relbad += 1
                if d.edges_malformed: edgebad += 1
                if d.gaps_malformed: gapbad += 1
            except ap.AtlasParseError:
                fail += 1
        print(f"  فشل تحليل تام: {fail} (كان 10)")
        print(f"  related مكسورة: {relbad} (كان 17)")
        print(f"  edges مكسورة: {edgebad} (كان 5)")
        print(f"  gaps مكسورة: {gapbad} (كان 11 — متوقَّع يفضل قريب، دي مش هدف هذه الخطوة)")


if __name__ == "__main__":
    main()
