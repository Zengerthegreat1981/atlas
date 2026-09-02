# -*- coding: utf-8 -*-
"""
Detailed examination of all unverified thinker entries
"""

import os
import glob
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

# Load thinkers
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

existing_slug_titles = {}
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line.strip())
        if m:
            existing_slug_titles[m.group(1).strip()] = m.group(2).strip()

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
target_files = study_files + instrument_files

unverified_thinkers = []
for fpath in target_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "## أفكار روابط لم تُتحقق" not in content:
        continue
    section = content.split("## أفكار روابط لم تُتحقق")[1].strip()
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        m = re.match(r'-\s*\"?([^\(\"—]+?)\"?\s*\(([^)]+)\)\s*—\s*(.*)', line)
        if m:
            name = m.group(1).strip()
            item_type = m.group(2).strip()
            desc = m.group(3).strip()
            if "مفكر" in item_type or "باحث" in item_type:
                unverified_thinkers.append({
                    "file": fname,
                    "fpath": fpath,
                    "name": name,
                    "type": item_type,
                    "desc": desc,
                    "line": line
                })

print("=== CHECKING ALL UNVERIFIED THINKERS AGAINST ALL 1579 THINKERS ===")
confirmed_matches = []

for u in unverified_thinkers:
    name = u["name"]
    f = u["file"]
    
    # We will search each thinker in all_thinkers
    matched_t = None
    
    # Check specific confirmed cases
    for slug, t in all_thinkers.items():
        # Case 1: Asch
        if slug == "thk-sasch" and "آش" in name:
            matched_t = t
        # Case 2: Bandura
        elif slug == "thk-abandura" and "باندورا" in name:
            matched_t = t
        # Case 3: Bowlby
        elif slug == "thk-bowlby" and "بولبي" in name:
            matched_t = t
        # Case 4: Pavlov
        elif slug == "thk-ipavlov" and "بافلوف" in name:
            matched_t = t
        # Case 5: Christopher Peterson
        elif slug == "thk-cpeterson" and "بيترسون" in name and "كريستوفر" in name:
            matched_t = t
        # Case 6: Achenbach
        elif slug == "thk-tachenbach" and "أشنباخ" in name:
            matched_t = t
        # Case 7: Jung
        elif slug == "thk-jung" and "يونغ" in name and ("كارل" in name or "غوستاف" in name):
            matched_t = t
        # Case 8: Spitzer
        elif slug == "thk-rspitzer" and "سبيتزر" in name:
            matched_t = t
        # Case 9: Aaron Beck
        elif slug == "thk-beck" and ("بيك" in name and "آرون" in name):
            matched_t = t
        # Case 10: Martin Seligman
        elif slug == "thk-mseligman" and ("سليجمان" in name or "سليغمان" in name) and "مارتن" in name:
            matched_t = t
        # Case 11: John B. Watson
        elif slug == "thk-jwatson" and ("واطسون" in name or "واتسون" in name) and "جون" in name:
            matched_t = t
        # Case 12: Leon Festinger
        elif slug == "thk-lfestinger" and ("فستنجر" in name or "فستنغر" in name):
            matched_t = t
        # Case 13: B. F. Skinner
        elif slug == "thk-fskinner" and "سكينر" in name:
            matched_t = t
        # Case 14: Edward Thorndike
        elif slug == "thk-thorndike" and ("ثورندايك" in name or "ثورنديك" in name) and "إدوارد" in name:
            matched_t = t
        # Case 15: Edna Foa
        elif slug == "thk-foa" and "فوا" in name and "إدنا" in name:
            matched_t = t
        # Case 16: Robert Emmons
        elif slug == "thk-emmons" and "إيمونز" in name and "روبرت" in name:
            matched_t = t
        # Case 17: John C. Lilly
        elif slug == "thk-jlilly" and ("ليلي" in name or "للي" in name) and "جون" in name:
            matched_t = t
            
    if matched_t:
        exact_title = existing_slug_titles.get(matched_t['slug'], matched_t['title'])
        confirmed_matches.append({
            "file": u["file"],
            "fpath": u["fpath"],
            "unverified_name": name,
            "line": u["line"],
            "slug": matched_t['slug'],
            "title": exact_title,
            "type": "مفكر"
        })

print(f"Total Confirmed Matches: {len(confirmed_matches)}")
for cm in confirmed_matches:
    print(f"[{cm['file']}] '{cm['unverified_name']}' -> id: \"{cm['slug']}\", title: \"{cm['title']}\", type: \"مفكر\"")
