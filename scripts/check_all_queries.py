# -*- coding: utf-8 -*-
"""
Check all candidate names against EXISTING_SLUGS.md and all thinker files.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import re

ROOT_DIR = _ATLAS_ROOT
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")

thinker_files = glob.glob(os.path.join(ROOT_DIR, "content/ar/thinkers/*.md")) + \
                glob.glob(os.path.join(ROOT_DIR, "content/ar/drafts/thinkers/*.md"))

all_thinkers = {}
for tf in thinker_files:
    slug = os.path.basename(tf)[:-3]
    with open(tf, "r", encoding="utf-8") as f:
        content = f.read()
    title_m = re.search(r'title:\s*\"([^\"]+)\"', content)
    en_m = re.search(r'en:\s*\"([^\"]+)\"', content)
    title = title_m.group(1).strip() if title_m else ""
    en = en_m.group(1).strip() if en_m else ""
    all_thinkers[slug] = {
        "slug": slug,
        "title": title,
        "en": en,
        "file": tf
    }

queries = [
    "foa", "seligman", "milgram", "zimbardo", "sherif", "piaget", "ebbinghaus",
    "watson", "harlow", "ainsworth", "loftus", "sperry", "gazzaniga", "broca",
    "dweck", "rosenhan", "binet", "terman", "wechsler", "raven", "cattell",
    "eysenck", "rorschach", "rotter", "hamilton", "bender", "diener", "ryff",
    "argyle", "festinger", "skinner", "thorndike", "beck", "spitzer", "aschenbach",
    "achenbach", "peterson", "emmons", "jung", "asch", "bandura", "bowlby"
]

print("=== CHECKING SLUGS AND NAMES ===")
for q in queries:
    matches = []
    for slug, t in all_thinkers.items():
        if q in slug.lower() or q in t['en'].lower() or q in t['title'].lower():
            matches.append((slug, t['title'], t['en']))
    print(f"Query '{q}': {matches}")
