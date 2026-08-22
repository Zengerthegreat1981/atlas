#!/usr/bin/env python3
"""
MiniMax orphan connection script — adds incoming related links to orphan files
based on structural relationships (edges).

Optimized: builds a reverse index of edges once, then looks up each orphan.
"""
import os
import re
import json
from collections import defaultdict

APPROVED_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar"

# Slug -> type mapping
SLUG_INDEX = {}


def build_slug_index_and_reverse_edges():
    """Build {slug: (path, type, title, related)} for all approved files.
    Returns: (index, reverse_edges) where reverse_edges[target_slug] = [referrer_slug, ...]
    """
    index = {}
    reverse_edges = defaultdict(list)
    for d in os.listdir(APPROVED_BASE):
        dir_path = os.path.join(APPROVED_BASE, d)
        if not os.path.isdir(dir_path):
            continue
        if d in ('drafts',):
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
            # Find edges
            edges = re.findall(r'rel:\s*["\']([^"\']+)["\'],\s*target:\s*["\']([^"\']+)["\']', fm)
            edge_targets = set(t for _, t in edges)
            index[slug] = {
                'path': fp,
                'dir': d,
                'type': m_type.group(1).strip() if m_type else '',
                'title': m_title.group(1).strip() if m_title else '',
                'related': related,
                'edges': edges,
                'edge_targets': edge_targets,
            }
            for rel, target in edges:
                reverse_edges[target].append((slug, rel))

    return index, reverse_edges


def add_related_to_file(slug, new_related_id, new_related_title, new_related_type, dry_run=True):
    """Add a new related item to a file's frontmatter."""
    info = SLUG_INDEX.get(slug)
    if not info:
        return False, "slug not in index"
    fp = info['path']
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    if new_related_id in info['related']:
        return False, "already in related"

    m_rel = re.search(r'(related:\s*\n)((?:[ \t]*-\s*id:.*\n?)+)', content)
    if not m_rel:
        return False, "no related section found"

    rel_start = m_rel.start(1)
    rel_text = m_rel.group(2)
    new_entry = f'  - id: "{new_related_id}", title: "{new_related_title}", type: "{new_related_type}"\n'
    new_rel_text = rel_text + new_entry

    new_content = content[:rel_start] + 'related:\n' + new_rel_text + content[m_rel.end():]

    if not dry_run:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        info['related'].append(new_related_id)
    return True, "added"


def main():
    global SLUG_INDEX
    SLUG_INDEX, reverse_edges = build_slug_index_and_reverse_edges()
    print(f"Indexed {len(SLUG_INDEX)} approved files")
    print(f"Reverse edges: {len(reverse_edges)} unique targets")

    # Load orphan list
    with open('/tmp/minimax_orphans.json', 'r') as f:
        orphans_data = json.load(f)

    all_orphans = []
    for d, files in orphans_data['by_type'].items():
        for o in files:
            all_orphans.append(o)

    print(f"Total orphans: {len(all_orphans)}")

    # For each orphan, find structural referrers via reverse_edges
    # Edges by Arabic name only — but most referrers use slugs in `related`.
    # So this approach won't work for edge->related matching.
    # Instead: find any file that has an edge TO the orphan and the orphan
    # is in their `edge_targets`, and add the orphan's slug to the referrer's `related`.

    actions = []
    for o in all_orphans:
        slug = o['slug']
        # Find referrers that have an edge to this slug
        # But edges are by Arabic name not slug! We need to match by:
        # 1. Direct slug match in edge_targets
        # 2. Match by title (Arabic)
        # 3. Match by the orphan's own `edges` reverse direction

        if slug not in reverse_edges:
            continue
        for ref_slug, rel in reverse_edges[slug]:
            if ref_slug == slug:
                continue
            ref_info = SLUG_INDEX[ref_slug]
            # Don't add if already linked
            if slug in ref_info['related']:
                continue
            actions.append((slug, ref_slug, rel, SLUG_INDEX[slug]['type']))

    # Dedupe
    unique_actions = []
    seen = set()
    for a in actions:
        key = (a[0], a[1])
        if key in seen:
            continue
        seen.add(key)
        unique_actions.append(a)

    print(f"\n=== Structural connection candidates (edge->related back-link) ===")
    print(f"Total: {len(unique_actions)}")
    print(f"\n=== By orphan type ===")
    type_counts = defaultdict(int)
    for a in unique_actions:
        type_counts[a[3]] += 1
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # Save
    out = []
    for a in unique_actions:
        out.append({
            'orphan_slug': a[0],
            'orphan_title': SLUG_INDEX[a[0]]['title'],
            'referrer_slug': a[1],
            'referrer_title': SLUG_INDEX[a[1]]['title'],
            'referrer_path': SLUG_INDEX[a[1]]['path'],
            'edge_rel': a[2],
        })
    with open('/tmp/minimax_orphan_actions.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nActions saved to /tmp/minimax_orphan_actions.json")


if __name__ == '__main__':
    main()
