#!/usr/bin/env python3
"""Build coverage matrix: count by type for each psychology school."""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os
import re
import json
from collections import defaultdict
from datetime import datetime

APPROVED_BASE = _ATLAS_ROOT + "/content/ar"

# All type dirs
TYPES = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]


def parse_frontmatter(content):
    """Lenient frontmatter parser."""
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    rec = {
        'part': '',
        'belongs_to': [],
        'related': [],
    }
    p = re.search(r'^part:\s*["\']?([^"\'\n]+)["\']?', fm, re.MULTILINE)
    if p:
        rec['part'] = p.group(1).strip()
    # Find edges.belongs_to
    m_bt = re.findall(r'rel:\s*["\']belongs_to["\'],\s*target:\s*["\']([^"\']+)["\']', fm)
    rec['belongs_to'] = m_bt
    return rec


def get_school_list():
    """Get all psychology school slugs and titles."""
    schools = {}
    sp = os.path.join(APPROVED_BASE, "schools")
    for fn in os.listdir(sp):
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(sp, fn)
        with open(fp) as f:
            content = f.read()
        m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not m:
            continue
        fm = m.group(1)
        slug_m = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?', fm, re.MULTILINE)
        part_m = re.search(r'^part:\s*["\']?([^"\'\n]+)["\']?', fm, re.MULTILINE)
        title_m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
        if not slug_m:
            continue
        slug = slug_m.group(1).strip()
        part = part_m.group(1).strip() if part_m else ''
        title = title_m.group(1).strip() if title_m else ''
        if part == 'psychology':
            schools[slug] = title
    return schools


def build_matrix():
    schools = get_school_list()
    print(f"Found {len(schools)} psychology schools")
    # Map: school_name (Arabic from belongs_to) -> slug
    # We'll match by Arabic title for now
    school_name_to_slug = {}
    sp = os.path.join(APPROVED_BASE, "schools")
    for slug, title in schools.items():
        school_name_to_slug[title] = slug
        # Also try without parenthetical
        clean = re.sub(r'\s*\(.*?\)\s*', '', title).strip()
        if clean != title:
            school_name_to_slug[clean] = slug
        # Also accept the slug directly
        school_name_to_slug[slug] = slug
        # Also try alternative names
        school_name_to_slug["المدرسة الوجودية"] = "sch-existential-therapy"
        school_name_to_slug["الوجودية"] = "sch-existential-therapy"
        school_name_to_slug["التحليل النفسي"] = "sch-psychoanalysis"
        school_name_to_slug["العلاج الأسري الاستراتيجي (Palo Alto/MRI)"] = "sch-systemic-family"
        school_name_to_slug["علم النفس الإيجابي (Seligman)"] = "sch-positive-psychology"
        school_name_to_slug["علم النفس الإيجابي"] = "sch-positive-psychology"
        school_name_to_slug["مدرسة التحليل النفسي"] = "sch-psychoanalysis"
        school_name_to_slug["العلاج الأسري"] = "sch-systemic-family"
        school_name_to_slug["علم النفس التطوري"] = "sch-developmental"
        school_name_to_slug["علم النفس البيولوجي"] = "sch-biological-neuro"
        school_name_to_slug["علم النفس العصبي"] = "sch-biological-neuro"
        school_name_to_slug["الطب النفسي البيولوجي"] = "sch-biological-neuro"

    # For each type, count by school
    matrix = {slug: defaultdict(int) for slug in schools}
    matrix['_no_school'] = defaultdict(int)
    matrix['_unset_part'] = defaultdict(int)

    totals = {t: 0 for t in TYPES}
    by_school_totals = {slug: 0 for slug in schools}

    for t in TYPES:
        dir_path = os.path.join(APPROVED_BASE, t)
        if not os.path.isdir(dir_path):
            continue
        for fn in os.listdir(dir_path):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(dir_path, fn)
            with open(fp) as f:
                content = f.read()
            fm_data = parse_frontmatter(content)
            if not fm_data:
                continue
            totals[t] += 1
            # Find which school
            schools_for_this = []
            for target in fm_data['belongs_to']:
                if target in school_name_to_slug:
                    schools_for_this.append(school_name_to_slug[target])
            if not schools_for_this:
                if fm_data['part'] == 'psychology':
                    matrix['_no_school'][t] += 1
                else:
                    matrix['_unset_part'][t] += 1
            else:
                for s in schools_for_this:
                    matrix[s][t] += 1
                    by_school_totals[s] += 1

    return {
        'generated_at': datetime.now().isoformat(),
        'totals': totals,
        'schools': schools,
        'matrix': {k: dict(v) for k, v in matrix.items()},
        'by_school_totals': by_school_totals,
    }


def main():
    data = build_matrix()
    out_path = _ATLAS_ROOT + '/data/coverage_matrix.json'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out_path}")

    # Print summary
    print(f"\n=== Totals ===")
    for t in TYPES:
        print(f"  {t}: {data['totals'][t]}")
    print(f"\n=== By school ===")
    for slug in sorted(data['schools'].keys()):
        total = data['by_school_totals'].get(slug, 0)
        print(f"  {slug}: {total} items")


if __name__ == '__main__':
    main()
