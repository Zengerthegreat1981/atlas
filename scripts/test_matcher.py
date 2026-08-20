# -*- coding: utf-8 -*-
"""
Script to test matching unverified links to EXISTING_SLUGS.md
"""

import os
import glob
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

slug_to_info = {}

with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    current_section_type = None
    for line in f:
        line = line.strip()
        sec_m = re.match(r'##\s+([^(]+)\s*\(\d+\)', line)
        if sec_m:
            current_section_type = sec_m.group(1).strip()
            continue
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line)
        if m:
            slug = m.group(1).strip()
            title = m.group(2).strip()
            item_type = current_section_type if current_section_type else "مفكر"
            slug_to_info[slug] = {'title': title, 'type': item_type}

print("Loaded slugs from EXISTING_SLUGS.md: " + str(len(slug_to_info)))

thinker_files = glob.glob(os.path.join(ROOT_DIR, "content/ar/thinkers/*.md")) + \
                glob.glob(os.path.join(ROOT_DIR, "content/ar/drafts/thinkers/*.md"))

thinker_lookup = {}
for tf in thinker_files:
    slug = os.path.basename(tf)[:-3]
    with open(tf, "r", encoding="utf-8") as f:
        content = f.read()
    title_m = re.search(r'title:\s*\"([^\"]+)\"', content)
    en_m = re.search(r'en:\s*\"([^\"]+)\"', content)
    title = title_m.group(1).strip() if title_m else ""
    en = en_m.group(1).strip() if en_m else ""
    info = {
        'slug': slug,
        'title': title,
        'en': en,
        'type': "مفكر"
    }
    if title:
        thinker_lookup[title.lower()] = info
        clean_title = re.sub(r'^(د\.|دكتور|البروفيسور|بروفيسور)\s+', '', title).strip()
        thinker_lookup[clean_title.lower()] = info
    if en:
        thinker_lookup[en.lower()] = info

def normalize_name(n):
    n = n.strip()
    n = re.sub(r'^(د\.|دكتور|البروفيسور|بروفيسور)\s+', '', n)
    n = n.replace("ـ", "")
    n = re.sub(r'[إأآا]', 'ا', n)
    n = n.replace("ى", "ي")
    n = n.replace("ة", "ه")
    n = re.sub(r'\s+', ' ', n)
    return n.strip().lower()

normalized_thinkers = {}
for slug, info in slug_to_info.items():
    if slug.startswith("thk-"):
        norm = normalize_name(info['title'])
        normalized_thinkers[norm] = {'slug': slug, 'title': info['title'], 'type': "مفكر"}

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
target_files = study_files + instrument_files

matches_found = []
unmatched_found = []

for fpath in target_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "## أفكار روابط لم تُتحقق" not in content:
        continue
    section = content.split("## أفكار روابط لم تُتحقق")[1].strip()
    lines = [l.strip() for l in section.splitlines() if l.strip().startswith("- ")]
    for line in lines:
        m = re.match(r'-\s*\"?([^\(\"—]+?)\"?\s*\(([^)]+)\)\s*—\s*(.*)', line)
        if m:
            raw_name = m.group(1).strip()
            raw_type = m.group(2).strip()
            desc = m.group(3).strip()
            
            matched_slug = None
            if "مفكر" in raw_type or "باحث" in raw_type:
                if raw_name.lower() in thinker_lookup:
                    matched_slug = thinker_lookup[raw_name.lower()]
                else:
                    norm = normalize_name(raw_name)
                    if norm in normalized_thinkers:
                        matched_slug = normalized_thinkers[norm]
                    else:
                        for t_norm, t_info in normalized_thinkers.items():
                            raw_tokens = set(norm.split())
                            t_tokens = set(t_norm.split())
                            if len(raw_tokens) >= 2 and raw_tokens == t_tokens:
                                matched_slug = t_info
                                break
            
            if matched_slug:
                matches_found.append({
                    'file': fname,
                    'fpath': fpath,
                    'raw_name': raw_name,
                    'raw_type': raw_type,
                    'matched': matched_slug,
                    'line': line
                })
            else:
                unmatched_found.append({
                    'file': fname,
                    'fpath': fpath,
                    'raw_name': raw_name,
                    'raw_type': raw_type,
                    'line': line
                })
        else:
            print("Could not parse line: " + line + " in " + fname)

print("================ MATCHES FOUND (" + str(len(matches_found)) + ") ================")
for m in matches_found:
    print("[" + m['file'] + "] '" + m['raw_name'] + "' -> " + m['matched']['slug'] + " (" + m['matched']['title'] + ")")

print("================ UNMATCHED (" + str(len(unmatched_found)) + ") ================")
for u in unmatched_found:
    print("[" + u['file'] + "] '" + u['raw_name'] + "' (" + u['raw_type'] + ")")
