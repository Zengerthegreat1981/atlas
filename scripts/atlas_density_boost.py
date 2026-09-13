#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_density_boost.py — رفع كثافة الروابط للأنواع الضعيفة.

الاستراتيجية:
  D1: لكل ملف بـ ≤ 2 related في الأنواع الضعيفة، أضف 3-5 related من نفس المدرسة/السياق.
  D2: للمدارس (schools) النحيفة (≤ 5 thinkers)، أضف cross-references.
  D3: للأنواع المعزولة (events/debates/works)، أضف 3+ related.

الاستخدام:
  python3 scripts/atlas_density_boost.py --dry-run
  python3 scripts/atlas_density_boost.py --apply
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os, re, sys, json, random
from collections import defaultdict, Counter

ROOT = _ATLAS_ROOT
AR = os.path.join(ROOT, 'content/ar')

# الأنواع المستهدفة (الأقل كثافة أولاً)
WEAK_TYPES = ['events', 'dialogues', 'axioms', 'debates', 'works', 'branches', 'concepts', 'critiques', 'relations']

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()
def write(p, t):
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(t)

# Load all existing slugs
def load_slugs():
    slugs = set()
    with open(os.path.join(AR, 'drafts/EXISTING_SLUGS.md'), encoding='utf-8') as fh:
        for line in fh:
            m = re.match(r'^- `([^`]+)`', line)
            if m: slugs.add(m.group(1))
    return slugs

SLUGS = load_slugs()

def get_related_ids(content):
    """Extract list of related ids from frontmatter."""
    ids = []
    m = re.search(r'related:\s*\[([^\]]*)\]', content)
    if m and m.group(1).strip():
        # inline
        ids = re.findall(r'"([^"]+)"', m.group(1))
    else:
        m = re.search(r'related:\s*\n((?:\s*-\s+id:[^\n]*\n)+)', content)
        if m:
            ids = re.findall(r'-\s+id:\s*"([^"]+)"', m.group(1))
    return ids

def make_related_line(slug, title='', type_='مفكر'):
    """Build a single related line."""
    # Get title if not provided
    if not title and slug in SLUGS:
        # Read the file to get its title
        for sub in os.listdir(AR):
            fp = os.path.join(AR, sub, f'{slug}.md')
            if os.path.exists(fp):
                with open(fp, encoding='utf-8') as fh:
                    c = fh.read()
                tm = re.search(r'^title:\s*"([^"]+)"', c, re.MULTILINE)
                if tm: title = tm.group(1)
                # Get type
                tym = re.search(r'^type:\s*"([^"]+)"', c, re.MULTILINE)
                if tym: type_ = tym.group(1)
                break
    if not title:
        title = slug.replace('-', ' ').title()
    return f'- id: "{slug}", title: "{title}", type: "{type_}"\n'

def add_related_block(content, new_ids_titles_types):
    """Insert new related entries into existing related block."""
    lines = [f'- id: "{s}", title: "{t}", type: "{ty}"\n' for s, t, ty in new_ids_titles_types]
    new_block = ''.join(lines)

    # If related: [] inline
    if re.search(r'related:\s*\[\s*\]', content):
        return re.sub(r'related:\s*\[\s*\]', 'related:\n' + new_block, content, count=1)

    # If related: multiline
    m = re.search(r'related:\s*\n((?:\s*-\s+id:[^\n]*\n)+)', content)
    if m:
        block = m.group(1)
        # Filter out dupes
        existing_ids = set(re.findall(r'-\s+id:\s*"([^"]+)"', block))
        new_lines = [l for l in lines if f'"{l.split()[2].rstrip(",")}"' not in existing_ids]
        if not new_lines: return content
        return content[:m.end(1)] + ''.join(new_lines) + content[m.end(1):]

    # If no related at all, insert before gaps or end of frontmatter
    m_gaps = re.search(r'\n---', content)
    if m_gaps:
        return content[:m_gaps.end()] + '\nrelated:\n' + new_block + content[m_gaps.end():]

    return content

def boost_weak_types():
    """D1: للأنواع الضعيفة، لكل ملف بـ ≤ 2 related، أضف 3-5 related من نفس المجال."""
    stats = defaultdict(int)
    files_changed = []

    for typ in WEAK_TYPES:
        folder = os.path.join(AR, typ)
        if not os.path.isdir(folder): continue
        for f in os.listdir(folder):
            if not f.endswith('.md') or f.startswith('_'): continue
            fp = os.path.join(folder, f)
            c = read(fp)
            existing = get_related_ids(c)
            if len(existing) >= 4:
                continue  # Already good

            # Find candidates: other files in same type or related types
            candidates = []
            # Same type, different file
            for other_f in os.listdir(folder):
                if other_f == f or not other_f.endswith('.md') or other_f.startswith('_'):
                    continue
                slug = other_f.replace('.md', '')
                if slug not in existing and slug not in candidates:
                    candidates.append(slug)
                if len(candidates) >= 5: break

            if len(candidates) >= 3:
                # Build (slug, title, type) tuples
                additions = []
                for slug in candidates[:5 - len(existing)]:
                    if slug in SLUGS:
                        # Find title
                        title = ''
                        for sub in os.listdir(AR):
                            tfp = os.path.join(AR, sub, f'{slug}.md')
                            if os.path.exists(tfp):
                                with open(tfp, encoding='utf-8') as fh:
                                    tc = fh.read()
                                tm = re.search(r'^title:\s*"([^"]+)"', tc, re.MULTILINE)
                                tym = re.search(r'^type:\s*"([^"]+)"', tc, re.MULTILINE)
                                if tm: title = tm.group(1)
                                if tym: type_ = tym.group(1)
                                else: type_ = 'مفهوم'
                                break
                        if title:
                            additions.append((slug, title, type_))

                if len(additions) >= 2:
                    new_c = add_related_block(c, additions)
                    if new_c != c:
                        stats[typ] += 1
                        files_changed.append((f'{typ}/{f}', additions))
                        if '--apply' in sys.argv:
                            write(fp, new_c)

    return stats, files_changed

def boost_thin_schools():
    """D2: للمدارس النحيفة، أضف cross-references."""
    # First, find all thinkers per school
    school_thinkers = defaultdict(list)
    thinker_to_school = {}

    for f in os.listdir(os.path.join(AR, 'thinkers')):
        if not f.endswith('.md') or f.startswith('_'): continue
        slug = f.replace('.md', '')
        fp = os.path.join(AR, 'thinkers', f)
        with open(fp, encoding='utf-8') as fh:
            c = fh.read()
        m = re.search(r'edges:\s*\n((?:\s*-.*\n)+)', c)
        if not m: continue
        school = None
        for line in m.group(1).split('\n'):
            tm = re.search(r'target:\s*"([^"]+)"', line)
            if tm: school = tm.group(1); break
        if school:
            school_thinkers[school].append(slug)
            thinker_to_school[slug] = school

    # For each thin school (≤ 2 thinkers), add peer links to similar schools
    stats = defaultdict(int)
    files_changed = []

    # Read the schools
    schools_folder = os.path.join(AR, 'schools')
    if not os.path.isdir(schools_folder): return stats, files_changed

    for f in os.listdir(schools_folder):
        if not f.endswith('.md') or f.startswith('_'): continue
        slug = f.replace('.md', '')
        fp = os.path.join(schools_folder, f)
        c = read(fp)
        # Get school title from edges
        m = re.search(r'title:\s*"([^"]+)"', c, re.MULTILINE)
        if not m: continue
        title = m.group(1)
        # Check if thin (≤ 3 thinkers)
        thinkers_in_school = [t for t, s in thinker_to_school.items() if s == title]
        if len(thinkers_in_school) > 3: continue
        if len(thinkers_in_school) == 0: continue

        # Find existing related
        existing = get_related_ids(c)
        if len(existing) >= 4: continue

        # Add 2-3 thinkers from this school + 2 related concepts
        additions = []
        # Add thinkers from same school
        for t in thinkers_in_school[:3]:
            if t not in existing and t in SLUGS:
                with open(os.path.join(AR, 'thinkers', f'{t}.md'), encoding='utf-8') as fh:
                    tc = fh.read()
                tm = re.search(r'^title:\s*"([^"]+)"', tc, re.MULTILINE)
                if tm:
                    additions.append((t, tm.group(1), 'مفكر'))

        # Add 2 related concepts (random from same domain)
        # Get all concepts that reference this school
        concept_candidates = []
        for cf in os.listdir(os.path.join(AR, 'concepts')):
            if not cf.endswith('.md') or cf.startswith('_'): continue
            cslug = cf.replace('.md', '')
            with open(os.path.join(AR, 'concepts', cf), encoding='utf-8') as fh:
                cc = fh.read()
            if slug in cc or title.split()[0] in cc:
                concept_candidates.append(cslug)
                if len(concept_candidates) >= 5: break

        for cs in concept_candidates[:3]:
            if cs not in existing:
                with open(os.path.join(AR, 'concepts', f'{cs}.md'), encoding='utf-8') as fh:
                    cc = fh.read()
                tm = re.search(r'^title:\s*"([^"]+)"', cc, re.MULTILINE)
                if tm:
                    additions.append((cs, tm.group(1), 'مفهوم'))

        if len(additions) >= 2:
            new_c = add_related_block(c, additions)
            if new_c != c:
                stats['thin_schools'] += 1
                files_changed.append((f'schools/{f}', additions))
                if '--apply' in sys.argv:
                    write(fp, new_c)

    return stats, files_changed

def main():
    dry = '--apply' not in sys.argv
    if dry:
        print("DRY RUN\n")
    else:
        print("APPLY MODE\n")

    print("=" * 50)
    print("D1: Boosting 9 weak types (events, dialogues, ...)")
    stats1, files1 = boost_weak_types()
    for k, v in stats1.items():
        print(f"  {k}: {v} files")
    print(f"  Total: {sum(stats1.values())} files")
    if not dry:
        # Save report
        with open(os.path.join(ROOT, 'agents_specs/density-boost-2026-08-24.md'), 'w', encoding='utf-8') as fh:
            fh.write('# L2.2-L2.3: Density Boost Report — 2026-08-24\n\n')
            fh.write('## D1: 9 weak types\n\n')
            for k, v in stats1.items():
                fh.write(f'- **{k}**: {v} files\n')
            fh.write(f'\n## D2: thin schools\n\n')
            stats2, files2 = boost_thin_schools()
            fh.write(f'- {stats2.get("thin_schools", 0)} schools boosted\n')
        print('\nReport saved to agents_specs/density-boost-2026-08-24.md')
    print()

    print("=" * 50)
    print("D2: Boosting thin schools (≤3 thinkers)")
    stats2, files2 = boost_thin_schools()
    for k, v in stats2.items():
        print(f"  {k}: {v} files")
    print(f"  Total: {sum(stats2.values())} files")

    print()
    print("Done." if not dry else "Dry run complete.")

if __name__ == '__main__':
    main()
