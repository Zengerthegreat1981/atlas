# -*- coding: utf-8 -*-
"""
Search thinkers for debates.
"""

import os
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")

all_entries = []
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line)
        if m:
            all_entries.append((m.group(1).strip(), m.group(2).strip()))

names_to_check = [
    ("plomin", "بلومين"),
    ("galton", "غالتون"),
    ("lewontin", "ليونتين"),
    ("nosek", "نوزيك"),
    ("ioannidis", "إيوانيديس"),
    ("spitzer", "سبيتزر"),
    ("achenbach", "أشنباخ"),
    ("frances", "فرانسيس"),
    ("insel", "إنسل"),
    ("krueger", "كروغر"),
    ("gould", "غولد"),
    ("jensen", "جنسن"),
    ("sternberg", "ستيرنبرغ"),
    ("barkley", "باركلي"),
    ("breggin", "بريغين"),
    ("szasz", "ساس"),
    ("fink", "فينك"),
    ("cerletti", "سيرليتي"),
    ("anderson", "أندرسون"),
    ("ferguson", "فيرغسون"),
    ("haslam", "هاسلام"),
    ("lilienfeld", "ليلينفيلد"),
    ("garb", "غارب"),
    ("exner", "إكسنر"),
    ("kirsch", "كيرش"),
    ("derubeis", "ديروبيس"),
    ("hollon", "هولون"),
    ("beck", "بيك"),
    ("bandura", "باندورا"),
    ("jung", "يونغ")
]

for en, ar in names_to_check:
    matches = []
    for slug, title in all_entries:
        if en in slug.lower() or ar in title:
            matches.append((slug, title))
    if matches:
        print(f"{en}/{ar}: {matches}")
