#!/usr/bin/env python3
"""
MiniMax school connection script — finds orphan schools and connects them
via their structural relationships (edges), matching Arabic name targets
to actual slugs.

For each orphan school:
- Find branches (split_into) and add school to their related
- Find parent school (belongs_to / evolved_from) and add orphan to its related
- Find related schools and link them
"""
import os
import re
import json
from collections import defaultdict

APPROVED_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar"


def build_index():
    """Build {slug: {...}} index, plus a {normalized_arabic_title: slug} map."""
    index = {}
    title_to_slug = defaultdict(list)
    for d in os.listdir(APPROVED_BASE):
        dir_path = os.path.join(APPROVED_BASE, d)
        if not os.path.isdir(dir_path):
            continue
        if d == 'drafts':
            continue
        for fn in os.listdir(dir_path):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(dir_path, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)
            m_slug = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?\s*$', fm, re.MULTILINE)
            m_type = re.search(r'^type:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            m_title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if not m_slug:
                continue
            slug = m_slug.group(1).strip()
            related = re.findall(r'^\s*-\s*id:\s*["\']([^"\']+)["\']', fm, re.MULTILINE)
            title = m_title.group(1).strip() if m_title else ''
            type_ = m_type.group(1).strip() if m_type else ''
            index[slug] = {
                'path': fp,
                'dir': d,
                'type': type_,
                'title': title,
                'related': related,
            }
            # Build normalized title -> slug map
            norm = normalize_arabic(title)
            if norm:
                title_to_slug[norm].append(slug)
    return index, title_to_slug


def normalize_arabic(s):
    if not s:
        return ''
    s = s.strip()
    s = re.sub(r'[\u064B-\u065F\u0670]', '', s)
    s = re.sub(r'[إأآا]', 'ا', s)
    s = re.sub(r'[يى]', 'ي', s)
    s = re.sub(r'ة', 'ه', s)
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s)  # remove (English) in parens
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


def find_school_for_arabic_name(arabic_name, title_to_slug, index, prefer_dir=None):
    """Find the slug for an Arabic name. Try exact, then normalized."""
    if not arabic_name:
        return None
    norm = normalize_arabic(arabic_name)
    # Try exact normalized match
    if norm in title_to_slug:
        candidates = title_to_slug[norm]
        if prefer_dir:
            for c in candidates:
                if c in index and index[c]['dir'] == prefer_dir:
                    return c
        return candidates[0]
    # Try partial match: take first 4 words
    words = norm.split()[:4]
    short = ' '.join(words)
    if short in title_to_slug:
        return title_to_slug[short][0]
    return None


def add_related(referrer_slug, new_slug, new_title, new_type, slug_index, dry_run=False):
    """Add new_slug to referrer's related section."""
    if referrer_slug not in slug_index:
        return False, "referrer not in index"
    info = slug_index[referrer_slug]
    if new_slug in info['related']:
        return False, "already linked"
    fp = info['path']
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    m_rel = re.search(r'(related:\s*\n)((?:[ \t]*-\s*id:.*\n?)+)', content)
    if m_rel:
        rel_start = m_rel.start(1)
        rel_text = m_rel.group(2)
        new_entry = f'  - id: "{new_slug}", title: "{new_title}", type: "{new_type}"\n'
        new_rel_text = rel_text + new_entry
        new_content = content[:rel_start] + 'related:\n' + new_rel_text + content[m_rel.end():]
    else:
        # No related section — create before gaps
        m_gaps = re.search(r'(gaps:\s*\n)', content)
        if m_gaps:
            insert_pos = m_gaps.start(1)
            new_block = f"related:\n  - id: \"{new_slug}\", title: \"{new_title}\", type: \"{new_type}\"\n\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
        else:
            # Add at end of frontmatter
            m_end = re.search(r'\n---\s*\n', content)
            if not m_end:
                return False, "no end of frontmatter found"
            insert_pos = m_end.start()
            new_block = f"\nrelated:\n  - id: \"{new_slug}\", title: \"{new_title}\", type: \"{new_type}\"\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]

    if not dry_run:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        info['related'].append(new_slug)
    return True, "added"


def get_school_edges(school_slug, slug_index):
    """Get edges (rel, target) for a school file."""
    if school_slug not in slug_index:
        return []
    fp = slug_index[school_slug]['path']
    with open(fp) as f:
        content = f.read()
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return []
    fm = m.group(1)
    edges = re.findall(r'rel:\s*["\']([^"\']+)["\'],\s*target:\s*["\']([^"\']+)["\']', fm)
    return edges


def main():
    slug_index, title_to_slug = build_index()
    print(f"Indexed {len(slug_index)} files, {len(title_to_slug)} unique titles")

    # Load orphan list
    with open('/tmp/minimax_orphans.json') as f:
        orphans = json.load(f)

    orphan_schools = orphans['by_type'].get('schools', [])
    print(f"Orphan schools: {len(orphan_schools)}")

    actions = []
    for o in orphan_schools:
        slug = o['slug']
        edges = get_school_edges(slug, slug_index)
        # For each edge, find the target slug by Arabic name and add action
        for rel, target in edges:
            # Splitting into: should add school to the branch
            if rel == 'split_into':
                target_slug = find_school_for_arabic_name(target, title_to_slug, slug_index, prefer_dir='branches')
                if target_slug and target_slug != slug:
                    actions.append((slug, target_slug, f"school->branch via split_into: {target[:50]}"))
            # belongs_to / evolved_from / superseded_by / evolved_into: should add orphan school to the parent
            elif rel in ('belongs_to', 'evolved_from', 'superseded_by', 'evolved_into'):
                target_slug = find_school_for_arabic_name(target, title_to_slug, slug_index, prefer_dir='schools')
                if target_slug and target_slug != slug:
                    actions.append((target_slug, slug, f"parent<-child via {rel}: {target[:50]}"))

    # Dedupe
    seen = set()
    unique = []
    for a in actions:
        key = (a[0], a[1])
        if key in seen:
            continue
        seen.add(key)
        unique.append(a)

    print(f"\nTotal school connection actions: {len(unique)}")
    print(f"\n=== By direction ===")
    forward = sum(1 for a in unique if a[0].startswith('sch-'))
    backward = sum(1 for a in unique if not a[0].startswith('sch-'))
    print(f"  School->Branch (forward): {forward}")
    print(f"  Parent<-Orphan school (backward): {backward}")

    print(f"\n=== Sample (first 20) ===")
    for a in unique[:20]:
        o_title = slug_index.get(a[0], {}).get('title', '?')
        r_title = slug_index.get(a[1], {}).get('title', '?')
        print(f"  {a[0]} ({o_title}) -> {a[1]} ({r_title}): {a[2]}")

    # Save
    out = []
    for a in unique:
        out.append({
            'source': a[0],
            'target': a[1],
            'rationale': a[2],
            'source_path': slug_index[a[0]]['path'],
            'source_related': slug_index[a[0]]['related'],
            'source_type': slug_index[a[0]]['type'],
            'target_title': slug_index[a[1]]['title'],
        })
    with open('/tmp/minimax_school_actions.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nActions saved to /tmp/minimax_school_actions.json")


if __name__ == '__main__':
    main()
