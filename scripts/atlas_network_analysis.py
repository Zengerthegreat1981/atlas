#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_network_analysis.py — تحليل شبكة الأطلس (L4.1 + L4.2).

  N1: مصفوفة cross-school (أي مدرستين تتشاركان أي مفاهيم)
  N2: ترتيب الـhubs بناءً على degree centrality
"""
import os, re, sys, json
from collections import defaultdict, Counter

ROOT = '/Users/minamoheb/Desktop/Atlas'
AR = os.path.join(ROOT, 'content/ar')

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()

def load_slugs():
    slugs = set()
    with open(os.path.join(AR, 'drafts/EXISTING_SLUGS.md'), encoding='utf-8') as fh:
        for line in fh:
            m = re.match(r'^- `([^`]+)`', line)
            if m: slugs.add(m.group(1))
    return slugs

SLUGS = load_slugs()

def get_related(content):
    ids = []
    m = re.search(r'related:\s*\[([^\]]*)\]', content)
    if m and m.group(1).strip():
        ids = re.findall(r'"([^"]+)"', m.group(1))
    else:
        m = re.search(r'related:\s*\n((?:\s*-\s+id:[^\n]*\n)+)', content)
        if m:
            ids = re.findall(r'-\s+id:\s*"([^"]+)"', m.group(1))
    return ids

# Build the full graph
forward = defaultdict(set)  # file_slug → set of related slugs
school_of_thinker = {}  # thinker_slug → school_name
all_files = {}  # slug → (type, title, path)

for sub in os.listdir(AR):
    p = os.path.join(AR, sub)
    if not os.path.isdir(p) or sub.startswith('_'): continue
    for f in os.listdir(p):
        if not f.endswith('.md'): continue
        slug = f.replace('.md', '')
        fp = os.path.join(p, f)
        with open(fp, encoding='utf-8') as fh:
            c = fh.read()
        ids = get_related(c)
        forward[slug] = set(ids)
        # Get type and title
        tm = re.search(r'^type:\s*"([^"]+)"', c, re.MULTILINE)
        ttm = re.search(r'^title:\s*"([^"]+)"', c, re.MULTILINE)
        all_files[slug] = {
            'type': tm.group(1) if tm else '?',
            'title': ttm.group(1) if ttm else slug,
            'folder': sub,
        }
        # For thinkers, get their school
        if sub == 'thinkers':
            em = re.search(r'edges:\s*\n((?:\s*-.*\n)+)', c)
            if em:
                for line in em.group(1).split('\n'):
                    tm2 = re.search(r'target:\s*"([^"]+)"', line)
                    if tm2:
                        school_of_thinker[slug] = tm2.group(1)
                        break

# Reverse: for each file, count incoming references
incoming = defaultdict(int)
for src, targets in forward.items():
    for tgt in targets:
        if tgt in SLUGS:
            incoming[tgt] += 1

# L4.2: Top 20 hubs by degree centrality
total_degree = Counter()
for slug, targets in forward.items():
    total_degree[slug] = len(targets) + incoming.get(slug, 0)

# Filter to real files only
real_hubs = [(s, d) for s, d in total_degree.most_common(50) if s in all_files]

hubs_report = []
for slug, deg in real_hubs[:20]:
    info = all_files.get(slug, {})
    hubs_report.append({
        'slug': slug,
        'title': info.get('title', ''),
        'type': info.get('type', ''),
        'out_degree': len(forward[slug]),
        'in_degree': incoming.get(slug, 0),
        'total_degree': deg,
    })

with open(os.path.join(ROOT, 'agents_specs/network-hubs-2026-08-24.md'), 'w', encoding='utf-8') as fh:
    fh.write('# L4.2: Network Hubs — Top 20 by Degree Centrality (2026-08-24)\n\n')
    fh.write('**Total files in graph:** {}\n'.format(len(all_files)))
    fh.write('**Total related edges:** {}\n\n'.format(sum(len(v) for v in forward.values())))
    fh.write('## Top 20 hubs\n\n')
    fh.write('| Rank | Slug | Type | Out | In | Total | Title |\n|---|---|---|---|---|---|---|\n')
    for i, h in enumerate(hubs_report, 1):
        fh.write(f"| {i} | `{h['slug']}` | {h['type']} | {h['out_degree']} | {h['in_degree']} | {h['total_degree']} | {h['title']} |\n")

# Save JSON too
with open(os.path.join(ROOT, 'data/network-hubs-2026-08-24.json'), 'w', encoding='utf-8') as fh:
    json.dump(hubs_report, fh, ensure_ascii=False, indent=2)

# L4.1: Cross-school matrix
# For each pair of schools (by their thinkers), count shared concepts
school_concepts = defaultdict(set)  # school_name → set of concept slugs
for thinker, school in school_of_thinker.items():
    for related in forward.get(thinker, set()):
        if related.startswith('con-'):
            school_concepts[school].add(related)

# For pairs of schools with shared concepts
shared = defaultdict(int)
schools_list = list(school_concepts.keys())
for i, s1 in enumerate(schools_list):
    for s2 in schools_list[i+1:]:
        common = school_concepts[s1] & school_concepts[s2]
        if common:
            shared[(s1, s2)] = len(common)

# Sort and take top 100
top_pairs = sorted(shared.items(), key=lambda x: -x[1])[:100]

# Write matrix
with open(os.path.join(ROOT, 'data/cross_school_matrix.json'), 'w', encoding='utf-8') as fh:
    json.dump({
        'total_schools': len(schools_list),
        'total_concepts_by_school': {s: len(c) for s, c in school_concepts.items()},
        'top_shared_pairs': [
            {'school_a': a, 'school_b': b, 'shared_concepts': n} for (a, b), n in top_pairs
        ],
    }, fh, ensure_ascii=False, indent=2)

# Markdown report
with open(os.path.join(ROOT, 'agents_specs/cross-school-matrix-2026-08-24.md'), 'w', encoding='utf-8') as fh:
    fh.write('# L4.1: Cross-School Matrix — 2026-08-24\n\n')
    fh.write(f'**Total schools with concept data:** {len(schools_list)}\n')
    fh.write(f'**Schools with most concepts:**\n\n')
    for s, c in sorted(school_concepts.items(), key=lambda x: -len(x[1]))[:15]:
        fh.write(f'- {s}: {len(c)} concepts\n')
    fh.write(f'\n## Top 30 school pairs by shared concepts\n\n')
    fh.write('| School A | School B | Shared concepts |\n|---|---|---|\n')
    for (a, b), n in top_pairs[:30]:
        fh.write(f'| {a} | {b} | {n} |\n')

print(f'Total files: {len(all_files)}')
print(f'Total edges: {sum(len(v) for v in forward.values())}')
print(f'Top 5 hubs:')
for h in hubs_report[:5]:
    print(f'  {h["slug"]} ({h["type"]}): {h["total_degree"]} (out={h["out_degree"]}, in={h["in_degree"]})')
print(f'Schools with concepts: {len(schools_list)}')
print(f'Top shared school pair: {top_pairs[0] if top_pairs else "none"}')
