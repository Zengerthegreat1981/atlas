#!/usr/bin/env python3
"""
MiniMax orphan audit — find elements with no incoming related links.

Orphans = approved content/ar files whose slug is NEVER cited in any
other file's `related:` section. We do NOT count `edges` because edges
are by-name (Arabic) and noisy. We count `related` because it uses slugs.

We also ignore:
- Schools and branches (they have many edges but few related inbound)
  - Actually we keep them — schools are nodes too
- Works (`wrk-`) — these are often just listed and not "linked from"
- Drafts (out of scope)
"""
import os
import re
from collections import defaultdict
import json

APPROVED_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar"
DRAFTS_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar/drafts"

# All approved subdirs
TYPE_DIRS = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]


def parse_frontmatter(content):
    """Lenient frontmatter parser - extracts slug, related."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return None
    fm_text = m.group(1)
    rec = {'slug': '', 'title_ar': '', 'related': []}
    m_slug = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?\s*$', fm_text, re.MULTILINE)
    if m_slug:
        rec['slug'] = m_slug.group(1).strip()
    m_title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    if m_title:
        rec['title_ar'] = m_title.group(1).strip()
    # Parse related: - id: "slug", title: "..."
    rels = re.findall(r'^\s*-\s*id:\s*["\']([^"\']+)["\']', fm_text, re.MULTILINE)
    rec['related'] = rels
    return rec


def collect_all_files():
    """Collect all approved files."""
    all_files = []
    for d in TYPE_DIRS:
        dir_path = os.path.join(APPROVED_BASE, d)
        if not os.path.isdir(dir_path):
            continue
        for fn in sorted(os.listdir(dir_path)):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(dir_path, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            rec = parse_frontmatter(content)
            if rec and rec['slug']:
                rec['path'] = fp
                rec['dir'] = d
                all_files.append(rec)
    return all_files


def main():
    all_files = collect_all_files()
    print(f"Total approved files parsed: {len(all_files)}")

    # Build incoming map
    incoming = defaultdict(list)  # slug -> list of (referrer_slug, referrer_path)
    for f in all_files:
        for r in f['related']:
            incoming[r].append((f['slug'], f['path']))

    # Find orphans
    orphans = []
    for f in all_files:
        slug = f['slug']
        # Skip if the file has its own relations (might be a self-reference, but
        # it would still be a candidate for connecting)
        if not incoming.get(slug):
            orphans.append(f)

    # Print by type
    by_type = defaultdict(list)
    for o in orphans:
        by_type[o['dir']].append(o)

    print(f"\nTotal orphans: {len(orphans)}\n")
    for d, files in sorted(by_type.items()):
        print(f"== {d}: {len(files)} orphans ==")
        for f in files[:50]:  # cap to 50 per type for display
            print(f"  {f['slug']} — {f['title_ar']}")
        if len(files) > 50:
            print(f"  ... and {len(files) - 50} more")
        print()

    # Save full orphan list to JSON for downstream processing
    out = {
        'total_orphans': len(orphans),
        'by_type': {d: [{'slug': f['slug'], 'title': f['title_ar'], 'path': f['path']} for f in files] for d, files in by_type.items()},
    }
    with open('/tmp/minimax_orphans.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nFull orphan list written to /tmp/minimax_orphans.json")


if __name__ == '__main__':
    main()
