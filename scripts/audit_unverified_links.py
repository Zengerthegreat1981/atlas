# -*- coding: utf-8 -*-
"""
Audit unverified links across all studies and instruments drafts.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import re

ROOT_DIR = _ATLAS_ROOT
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

# 1. Parse EXISTING_SLUGS.md
slug_dict = {}
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line)
        if m:
            slug = m.group(1).strip()
            title = m.group(2).strip()
            slug_dict[slug] = title

print(f"Total slugs in EXISTING_SLUGS.md: {len(slug_dict)}")

# 2. Parse Thinker files (both approved and drafts)
thinker_files = glob.glob(os.path.join(ROOT_DIR, "content/ar/thinkers/*.md")) + \
                glob.glob(os.path.join(ROOT_DIR, "content/ar/drafts/thinkers/*.md"))

thinkers_by_slug = {}
for tf in thinker_files:
    slug = os.path.basename(tf)[:-3]
    with open(tf, "r", encoding="utf-8") as f:
        content = f.read()
    title_m = re.search(r'title:\s*\"([^\"]+)\"', content)
    en_m = re.search(r'en:\s*\"([^\"]+)\"', content)
    title = title_m.group(1).strip() if title_m else ""
    en = en_m.group(1).strip() if en_m else ""
    thinkers_by_slug[slug] = {
        "slug": slug,
        "title": title,
        "en": en,
        "file": tf
    }

print(f"Total thinkers parsed from markdown files: {len(thinkers_by_slug)}")

# 3. Read all 120 target files
study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
target_files = study_files + instrument_files

print(f"Target files: {len(target_files)} (Studies: {len(study_files)}, Instruments: {len(instrument_files)})")

# Let's inspect all unverified items
unverified_list = []
for fpath in target_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "## أفكار روابط لم تُتحقق" in content:
        section = content.split("## أفكار روابط لم تُتحقق")[1].strip()
        lines = [l.strip() for l in section.splitlines() if l.strip().startswith("- ")]
        for line in lines:
            unverified_list.append({
                "file": fname,
                "fpath": fpath,
                "line": line
            })

print(f"Total unverified link lines found: {len(unverified_list)}")

# Let's print out the unverified lines and attempt matching
for item in unverified_list:
    line = item["line"]
    # Usually: - "الاسم" (مفكر/باحث) — سبب... OR - الاسم (مفكر/باحث) — سبب...
    print(f"[{item['file']}] {line}")
