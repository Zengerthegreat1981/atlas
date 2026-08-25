#!/usr/bin/env python3
"""
assign_expansion_ids.py
Assigns sequential canonical IDs (e.g. CON-1236, MET-0004, QUE-0004, TRM-0004, EXP-0004, CTX-0024, DIA-0029, WRK-0762, DBT-0422, TEC-0341)
to all newly added nodes with [DRAFT-UNKNOWN].
"""

import re
from pathlib import Path
from collections import defaultdict

CONTENT_AR = Path('/Users/minamoheb/Desktop/Atlas/content/ar')

# 1. Map folder/type to prefix
PREFIX_MAP = {
    'metaphors': 'MET',
    'questions': 'QUE',
    'terms': 'TRM',
    'experiences': 'EXP',
    'contexts': 'CTX',
    'dialogues': 'DIA',
    'works': 'WRK',
    'debates': 'DBT',
    'concepts': 'CON',
    'techniques': 'TEC',
    'thinkers': 'THK',
    'schools': 'SCH',
    'branches': 'BRN',
    'disorders': 'DIS',
    'instruments': 'INS',
    'studies': 'STU',
    'symptoms': 'SYN',
    'axioms': 'AXM',
    'events': 'EVT',
    'critiques': 'CRT',
    'religions': 'REL',
    'classifications': 'CLS'
}

# 2. Find highest existing numeric ID per prefix
prefix_max = defaultdict(int)

for f in CONTENT_AR.rglob('*.md'):
    if 'drafts' in f.parts:
        continue
    txt = f.read_text(encoding='utf-8')
    m = re.search(r'^id:\s*\"?([A-Z]+)-(\d+)\"?', txt, re.MULTILINE)
    if m:
        p = m.group(1)
        n = int(m.group(2))
        prefix_max[p] = max(prefix_max[p], n)

print("Starting prefix maximums:")
for p, m in sorted(prefix_max.items()):
    print(f"  {p}: {m}")

# 3. Assign sequential IDs to all files with [DRAFT-UNKNOWN] or missing ID
updated_count = 0

for f in sorted(CONTENT_AR.rglob('*.md')):
    if 'drafts' in f.parts:
        continue
    txt = f.read_text(encoding='utf-8')
    m = re.search(r'^id:\s*\"?([^\n\"]+)\"?', txt, re.MULTILINE)
    if m and ('DRAFT' in m.group(1) or 'UNKNOWN' in m.group(1)):
        folder = f.parent.name
        prefix = PREFIX_MAP.get(folder, 'NOD')
        prefix_max[prefix] += 1
        new_id = f"{prefix}-{prefix_max[prefix]:04d}"
        
        new_txt = re.sub(r'^id:\s*\"?[^\n\"]+\"?', f'id: "{new_id}"', txt, count=1, flags=re.MULTILINE)
        f.write_text(new_txt, encoding='utf-8')
        updated_count += 1

print(f"\nSuccessfully assigned canonical sequential IDs to {updated_count} nodes.")

# Final verification
remaining_drafts = 0
for f in CONTENT_AR.rglob('*.md'):
    if 'drafts' in f.parts:
        continue
    txt = f.read_text(encoding='utf-8')
    if '[DRAFT-UNKNOWN]' in txt:
        remaining_drafts += 1

print(f"Remaining drafts: {remaining_drafts}")
