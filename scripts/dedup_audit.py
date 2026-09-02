#!/usr/bin/env python3
"""
Dedup audit script for Atlas drafts (lenient parser).
"""
import os
import re
from collections import defaultdict

DRAFTS_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar/drafts"
APPROVED_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar"

TYPE_DIRS = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]

def normalize_arabic(s):
    if not s: return ""
    s = s.strip()
    s = re.sub(r'[\u064B-\u065F\u0670]', '', s)
    s = re.sub(r'[إأآا]', 'ا', s)
    s = re.sub(r'[يى]', 'ي', s)
    s = re.sub(r'ة', 'ه', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

def normalize_english(s):
    if not s: return ""
    s = s.strip().lower()
    s = re.sub(r'[^a-z\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def parse_frontmatter(content):
    """Lenient frontmatter parser - extracts slug, title, en."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return None
    fm_text = m.group(1)
    rec = {'path': None, 'slug': '', 'title_ar': '', 'title_en': ''}
    # Extract slug (block scalar)
    m_slug = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?\s*$', fm_text, re.MULTILINE)
    if m_slug:
        rec['slug'] = m_slug.group(1).strip()
    # Extract title (the 'title' field, not 'title_en')
    m_title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    if m_title:
        rec['title_ar'] = m_title.group(1).strip().strip('"\'')
    # Extract en
    m_en = re.search(r'^en:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    if m_en:
        rec['title_en'] = m_en.group(1).strip().strip('"\'')
    return rec

def parse_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None
    rec = parse_frontmatter(content)
    if not rec:
        return None
    rec['path'] = path
    return rec

def gather_files():
    files = []
    for tdir in TYPE_DIRS:
        draft_dir = os.path.join(DRAFTS_BASE, tdir)
        approved_dir = os.path.join(APPROVED_BASE, tdir)
        for base, status in [(draft_dir, 'draft'), (approved_dir, 'approved')]:
            if not os.path.isdir(base):
                continue
            for fn in os.listdir(base):
                if not fn.endswith('.md'):
                    continue
                path = os.path.join(base, fn)
                rec = parse_file(path)
                if rec:
                    rec['type_dir'] = tdir
                    rec['status'] = status
                    files.append(rec)
    return files

def find_same_type_duplicates(files):
    by_type = defaultdict(list)
    for f in files:
        if not f.get('title_ar'):
            continue
        key = (f['type_dir'], normalize_arabic(f['title_ar']))
        by_type[key].append(f)
    return {k: v for k, v in by_type.items() if len(v) >= 2}

def find_cross_type_duplicates(files):
    by_title = defaultdict(list)
    for f in files:
        if not f.get('title_ar'):
            continue
        key = normalize_arabic(f['title_ar'])
        by_title[key].append(f)
    result = {}
    for k, v in by_title.items():
        type_dirs = set(f['type_dir'] for f in v)
        if len(type_dirs) >= 2 and len(v) >= 2:
            result[k] = v
    return result

def find_english_dupes_by_type(files):
    by_type = defaultdict(list)
    for f in files:
        if not f.get('title_en'):
            continue
        key = (f['type_dir'], normalize_english(f['title_en']))
        by_type[key].append(f)
    return {k: v for k, v in by_type.items() if len(v) >= 2}

if __name__ == '__main__':
    files = gather_files()
    print(f"Total files parsed: {len(files)}")
    print(f"  with title_ar: {sum(1 for f in files if f.get('title_ar'))}")
    print(f"  with title_en: {sum(1 for f in files if f.get('title_en'))}")

    same_type_dupes = find_same_type_duplicates(files)
    print(f"\nSame-type (ar) potential duplicates: {len(same_type_dupes)} groups")

    cross_type_dupes = find_cross_type_duplicates(files)
    print(f"Cross-type (ar) potential duplicates: {len(cross_type_dupes)} groups")

    english_dupes = find_english_dupes_by_type(files)
    print(f"Same-type (en) potential duplicates: {len(english_dupes)} groups")

    # Save
    with open('/tmp/dedup_same_type.txt', 'w', encoding='utf-8') as f:
        for k, group in sorted(same_type_dupes.items()):
            f.write(f"\n=== {k[0]} / '{k[1]}' ===\n")
            for item in group:
                f.write(f"  - [{item['status']}] slug={item['slug']} | en='{item['title_en']}' | {item['path']}\n")

    with open('/tmp/dedup_cross_type.txt', 'w', encoding='utf-8') as f:
        for k, group in sorted(cross_type_dupes.items()):
            types = set(item['type_dir'] for item in group)
            f.write(f"\n=== '{k}' (across types: {types}) ===\n")
            for item in group:
                f.write(f"  - [{item['status']}/{item['type_dir']}] slug={item['slug']} | en='{item['title_en']}' | {item['path']}\n")

    with open('/tmp/dedup_same_type_en.txt', 'w', encoding='utf-8') as f:
        for k, group in sorted(english_dupes.items()):
            f.write(f"\n=== {k[0]} / en='{k[1]}' ===\n")
            for item in group:
                f.write(f"  - [{item['status']}] slug={item['slug']} | ar='{item['title_ar']}' | {item['path']}\n")

    print("Wrote /tmp/dedup_same_type.txt, /tmp/dedup_cross_type.txt, /tmp/dedup_same_type_en.txt")
