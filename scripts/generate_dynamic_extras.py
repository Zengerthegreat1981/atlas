import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os
import re
import json
from pathlib import Path
from collections import defaultdict

ATLAS_ROOT = Path(_ATLAS_ROOT)
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'
EXTRAS_FILE = ATLAS_ROOT / 'scripts' / 'template' / 'data_extras.json'

with open(EXTRAS_FILE, 'r', encoding='utf-8') as f:
    extras = json.load(f)

# 1. Parse all thinkers and extract metadata
thinkers = []
schools = []
events = []

DATE_RE = re.compile(r'(\d{3,4})\s*[–—-]\s*(\d{3,4}|مستمر)')

for f in CONTENT_AR.glob('**/*.md'):
    if 'drafts' in f.parts or '_merged' in f.parts:
        continue
    txt = f.read_text(encoding='utf-8')
    if not txt.startswith('---'):
        continue
    raw_yaml = txt.split('---', 2)[1]
    
    slug = f.stem
    m_title = re.search(r'^title:\s*"([^"]*)"', raw_yaml, re.M)
    m_part = re.search(r'^part:\s*"([^"]*)"', raw_yaml, re.M)
    m_dates = re.search(r'^dates:\s*"([^"]*)"', raw_yaml, re.M)
    m_start = re.search(r'^active_start:\s*(-?\d+)', raw_yaml, re.M)
    m_end = re.search(r'^active_end:\s*(-?\d+|"مستمر")', raw_yaml, re.M)
    m_type = re.search(r'^type:\s*"([^"]*)"', raw_yaml, re.M)
    
    title = m_title.group(1).strip() if m_title else slug
    part = m_part.group(1).strip() if m_part else 'psychology'
    ntype = m_type.group(1).strip() if m_type else ''
    
    if ntype == 'مفكر':
        b_year = None
        d_year = None
        if m_dates:
            d_str = m_dates.group(1)
            dm = DATE_RE.search(d_str)
            if dm:
                b_year = int(dm.group(1))
                d_year = int(dm.group(2)) if dm.group(2) != 'مستمر' else 2026
        if not b_year and m_start:
            b_year = int(m_start.group(1))
            if m_end:
                d_year = int(m_end.group(1)) if m_end.group(1) != '"مستمر"' else 2026
            else:
                d_year = b_year + 50
                
        if b_year and d_year and b_year < d_year and b_year > -600 and d_year <= 2026:
            group = 'phil' if part == 'philosophy' else ('bridge' if part == 'bridge' else 'psych')
            short_name = re.sub(r'\(.*?\)', '', title).strip().split(' — ')[0].strip()
            thinkers.append({
                'n': short_name,
                'b': b_year,
                'd': d_year,
                'g': group,
                'k': slug
            })

print(f"Extracted {len(thinkers)} thinkers with valid timelines.")

# 2. Select top canonical thinkers for the Gantt chart across ages (up to 120 key figures)
# Sort by birth year and filter
thinkers_sorted = sorted(thinkers, key=lambda x: x['b'])
# Sample evenly and preserve original core figures
core_keys = set(g.get('k', '') for g in extras.get('gantt', []))
selected_gantt = []
seen_keys = set()

# Always include core existing gantt items
for g in extras.get('gantt', []):
    selected_gantt.append(g)
    if 'k' in g:
        seen_keys.add(g['k'])

# Add new prominent figures from philosophy, psychology, and bridge
step = max(1, len(thinkers_sorted) // 80)
for i in range(0, len(thinkers_sorted), step):
    thk = thinkers_sorted[i]
    if thk['k'] not in seen_keys and len(selected_gantt) < 120:
        selected_gantt.append({
            'n': thk['n'],
            'b': thk['b'],
            'd': thk['d'],
            'g': thk['g'],
            'k': thk['k']
        })
        seen_keys.add(thk['k'])

extras['gantt'] = sorted(selected_gantt, key=lambda x: x.get('b', 1900))
print(f"Updated Gantt Chart: {len(extras['gantt'])} thinkers spanning history.")

# 3. Update people list with all key thinkers
people_list = []
seen_people = set()
for g in extras['gantt']:
    k = g.get('k')
    n = g.get('n')
    if k and k not in seen_people:
        people_list.append([k, n])
        seen_people.add(k)

extras['people'] = people_list
print(f"Updated People Index: {len(extras['people'])} key figures.")

# 4. Save updated data_extras.json
with open(EXTRAS_FILE, 'w', encoding='utf-8') as f:
    json.dump(extras, f, ensure_ascii=False, indent=2)

print("Saved updated data_extras.json successfully.")
