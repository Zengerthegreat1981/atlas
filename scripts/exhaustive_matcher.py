# -*- coding: utf-8 -*-
"""
Exhaustive matcher for all unverified lines in all 122 draft files.
"""

import os
import glob
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

# Load all thinkers from markdown files
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

# Also parse EXISTING_SLUGS.md for exact title mappings
existing_slug_titles = {}
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line.strip())
        if m:
            existing_slug_titles[m.group(1).strip()] = m.group(2).strip()

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
target_files = study_files + instrument_files

# Collect all unverified thinker lines
all_unverified_thinkers = []
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
                all_unverified_thinkers.append({
                    "file": fname,
                    "fpath": fpath,
                    "name": name,
                    "type": item_type,
                    "desc": desc,
                    "line": line
                })

print("Total unverified thinkers to check: " + str(len(all_unverified_thinkers)))

# Let's inspect each unverified thinker against all thinkers
matched_actions = []

for item in all_unverified_thinkers:
    name = item["name"]
    desc = item["desc"]
    
    # Let's see all potential candidates in all_thinkers
    candidates = []
    
    # 1. Direct name mappings
    # e.g. "مارتن سليجمان" -> Martin Seligman -> thk-mseligman
    # "آرون بيك" -> Aaron Beck -> thk-beck
    # "جون ب. واطسون" -> John Watson -> thk-jwatson
    # "إدوارد ثورندايك" -> Edward Thorndike -> thk-thorndike
    # "ب. ف. سكينر" -> B.F. Skinner -> thk-fskinner
    # "ليون فستنجر" -> Leon Festinger -> thk-lfestinger
    # "إدنا فوا" -> Edna Foa -> thk-foa
    # "روبرت إيمونز" -> Robert Emmons -> thk-emmons
    
    for slug, t in all_thinkers.items():
        t_title = t['title']
        t_en = t['en']
        
        # Check matching
        # Same exact person check
        is_match = False
        
        if slug == "thk-sasch" and "آش" in name:
            is_match = True
        elif slug == "thk-abandura" and "باندورا" in name:
            is_match = True
        elif slug == "thk-bowlby" and "بولبي" in name:
            is_match = True
        elif slug == "thk-ipavlov" and "بافلوف" in name:
            is_match = True
        elif slug == "thk-cpeterson" and "بيترسون" in name and "كريستوفر" in name:
            is_match = True
        elif slug == "thk-tachenbach" and "أشنباخ" in name:
            is_match = True
        elif slug == "thk-jung" and "يونغ" in name:
            is_match = True
        elif slug == "thk-rspitzer" and "سبيتزر" in name:
            is_match = True
        elif slug == "thk-beck" and ("بيك" in name or "آرون" in name):
            is_match = True
        elif slug == "thk-mseligman" and ("سليجمان" in name or "سليغمان" in name):
            is_match = True
        elif slug == "thk-jwatson" and ("واطسون" in name or "واتسون" in name) and "جون" in name:
            is_match = True
        elif slug == "thk-lfestinger" and ("فستنجر" in name or "فستنغر" in name):
            is_match = True
        elif slug == "thk-fskinner" and "سكينر" in name:
            is_match = True
        elif slug == "thk-thorndike" and ("ثورندايك" in name or "ثورنديك" in name):
            is_match = True
        elif slug == "thk-foa" and "فوا" in name:
            is_match = True
        elif slug == "thk-emmons" and "إيمونز" in name:
            is_match = True
            
        if is_match:
            candidates.append(t)
            
    if candidates:
        matched_thinker = candidates[0]
        # Title from EXISTING_SLUGS.md
        exact_title = existing_slug_titles.get(matched_thinker['slug'], matched_thinker['title'])
        matched_actions.append({
            "file": item["file"],
            "fpath": item["fpath"],
            "original_name": item["name"],
            "line": item["line"],
            "target_slug": matched_thinker['slug'],
            "target_title": exact_title,
            "target_type": "مفكر"
        })

print("Total matched thinker actions: " + str(len(matched_actions)))
for a in matched_actions:
    print("In [" + a["file"] + "]: transfer '" + a["original_name"] + "' -> id: \"" + a["target_slug"] + "\", title: \"" + a["target_title"] + "\", type: \"مفكر\"")
