#!/usr/bin/env python3
"""
Orphan-closing pass: take a list of new files (concepts, thinkers, etc.)
and ensure they appear in the related sections of other files where they're
naturally relevant.

For each new file, find existing files that should mention it, and add the
new file to their related.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import re
import os
import json
import sys

APPROVED_BASE = _ATLAS_ROOT + '/content/ar'


def parse_frontmatter(content):
    """Lenient frontmatter parser."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return None, None
    fm = m.group(1)
    slug_m = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?\s*$', fm, re.MULTILINE)
    title_m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    type_m = re.search(r'^type:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    return {
        'slug': slug_m.group(1).strip() if slug_m else '',
        'title': title_m.group(1).strip() if title_m else '',
        'type': type_m.group(1).strip() if type_m else '',
        'related': re.findall(r'^\s*-\s*id:\s*["\']([^"\']+)["\']', fm, re.MULTILINE),
    }, fm


def add_related(referrer_path, new_slug, new_title, new_type):
    """Add a new related entry to a file."""
    with open(referrer_path) as f:
        content = f.read()
    fm_data, fm_text = parse_frontmatter(content)
    if not fm_data:
        return False, "no fm"

    if new_slug in fm_data['related']:
        return False, "already linked"

    m_rel = re.search(r'(related:\s*\n)((?:[ \t]*-\s*id:.*\n?)+)', content)
    if m_rel:
        rel_start = m_rel.start(1)
        rel_text = m_rel.group(2)
        new_entry = f'  - id: "{new_slug}", title: "{new_title}", type: "{new_type}"\n'
        new_rel_text = rel_text + new_entry
        new_content = content[:rel_start] + 'related:\n' + new_rel_text + content[m_rel.end():]
    else:
        # Create related section before gaps
        m_gaps = re.search(r'(gaps:\s*\n)', content)
        if m_gaps:
            insert_pos = m_gaps.start(1)
            new_block = f"related:\n  - id: \"{new_slug}\", title: \"{new_title}\", type: \"{new_type}\"\n\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
        else:
            m_end = re.search(r'\n---\s*\n', content)
            if not m_end:
                return False, "no end of fm"
            insert_pos = m_end.start()
            new_block = f"\nrelated:\n  - id: \"{new_slug}\", title: \"{new_title}\", type: \"{new_type}\"\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]

    with open(referrer_path, 'w') as f:
        f.write(new_content)
    return True, "added"


def main(dry_run=False):
    """Pass to close orphans: add new concepts to existing related sections."""
    # New concepts to close orphans for
    new_concepts = [
        # concept_slug, concept_title, concept_type, list_of_referrer_slugs_to_add_to
        ('con-attachment-styles', 'أنماط التعلق', 'مفهوم',
         ['thk-ainsworth', 'thk-bowlby', 'thk-marymain', 'thk-fonagy',
          'sch-developmental', 'br-attachment-theory']),
        ('con-zpd', 'منطقة النمو القريب (ZPD)', 'مفهوم',
         ['thk-vygotsky', 'thk-piaget', 'sch-developmental']),
        ('con-cognitive-development-stages', 'مراحل النمو المعرفي (Piaget)', 'مفهوم',
         ['thk-piaget', 'thk-vygotsky', 'sch-developmental']),
        ('con-flow', 'التدفق (Flow)', 'مفهوم',
         ['thk-mcsikszentmihalyi', 'thk-mseligman', 'sch-positive-psychology']),
        ('con-learned-helplessness', 'العجز المتعلم', 'مفهوم',
         ['thk-mseligman', 'sch-positive-psychology']),
        ('con-neuroplasticity', 'اللدونة العصبية', 'مفهوم',
         ['thk-adamasio', 'thk-jledoux', 'thk-panksepp', 'sch-biological-neuro']),
        ('con-piaget-schema', 'المخطط (Schema)', 'مفهوم',
         ['thk-piaget', 'sch-developmental', 'con-cognitive-development-stages']),
        ('con-differentiation-self', 'التمايز عن الذات', 'مفهوم',
         ['thk-mbowen', 'sch-systemic-family', 'br-bowen-systems']),
        ('con-triangulation', 'التثليث', 'مفهوم',
         ['thk-mbowen', 'thk-gbateson', 'sch-systemic-family']),
        ('con-double-bind', 'الرباط المزدوج', 'مفهوم',
         ['thk-gbateson', 'thk-jhaley', 'thk-jweakland', 'sch-systemic-family']),
        ('con-genogram', 'الجنوجرام', 'مفهوم',
         ['thk-mbowen', 'thk-mmcgoldrick', 'sch-systemic-family']),
        ('con-family-structure', 'البنية الأسرية', 'مفهوم',
         ['thk-sminuchin', 'thk-mbowen', 'sch-systemic-family', 'br-structural-family']),
        ('con-emotional-cutoff', 'القطع العاطفي', 'مفهوم',
         ['thk-mbowen', 'thk-mkerr', 'sch-systemic-family']),
        ('con-family-projection-process', 'عملية الإسقاط الأسري', 'مفهوم',
         ['thk-mbowen', 'sch-systemic-family']),
        ('con-enmeshment-disengagement', 'الانغماس والانفصال الأسري', 'مفهوم',
         ['thk-sminuchin', 'sch-systemic-family', 'br-structural-family']),
        ('con-joining', 'الانضمام العلاجي', 'مفهوم',
         ['thk-sminuchin', 'sch-systemic-family']),
        ('con-paradoxical-intervention', 'التدخل المتناقض', 'مفهوم',
         ['thk-mselvini', 'sch-systemic-family']),
        ('con-circular-questioning', 'الأسئلة الدائرية', 'مفهوم',
         ['thk-mselvini', 'sch-systemic-family']),
        ('con-multigenerational-transmission', 'النقل متعدد الأجيال', 'مفهوم',
         ['thk-mbowen', 'sch-systemic-family']),
        ('con-subsystems', 'الأنظمة الفرعية الأسرية', 'مفهوم',
         ['thk-sminuchin', 'sch-systemic-family']),
        ('con-psychosocial-stages', 'المراحل النفسية-الاجتماعية', 'مفهوم',
         ['thk-erikson', 'sch-developmental']),
        ('con-secure-attachment', 'التعلق الآمن', 'مفهوم',
         ['con-attachment-styles', 'thk-ainsworth', 'thk-bowlby', 'thk-marymain', 'sch-developmental', 'br-attachment-theory']),
        ('con-anxious-attachment', 'التعلق القلق', 'مفهوم',
         ['con-attachment-styles', 'thk-ainsworth']),
        ('con-avoidant-attachment', 'التعلق التجنبي', 'مفهوم',
         ['con-attachment-styles', 'thk-ainsworth']),
        ('con-disorganized-attachment', 'التعلق غير المنظَّم', 'مفهوم',
         ['con-attachment-styles', 'thk-marymain']),
        ('con-scaffolding', 'السقالة (Scaffolding)', 'مفهوم',
         ['thk-vygotsky', 'con-zpd']),
        ('con-somatic-marker', 'العلامة الجسدية', 'مفهوم',
         ['thk-adamasio', 'sch-biological-neuro']),
        # New from this session
        ('con-tawakkul', 'التوكل (Tawakkul)', 'مفهوم',
         ['sch-islamic-psychology', 'thk-mbadri', 'thk-maburaiya']),
        ('con-taqwa', 'التقوى (Taqwa)', 'مفهوم',
         ['sch-islamic-psychology', 'thk-mbadri']),
        ('con-3min-breathing-space', 'مساحة التنفس الثلاث دقائق (MBCT)', 'مفهوم',
         ['sch-mbct', 'thk-zsegal']),
        ('con-oars', 'تقنية OARS (المقابلة التحفيزية)', 'مفهوم',
         ['sch-motivational-interviewing', 'thk-wmiller']),
    ]
    # Find paths for all slugs
    all_slugs = set()
    for cs, _, _, refs in new_concepts:
        all_slugs.add(cs)
        all_slugs.update(refs)
    slug_to_path = {}
    for d in os.listdir(APPROVED_BASE):
        dir_path = os.path.join(APPROVED_BASE, d)
        if not os.path.isdir(dir_path) or d == 'drafts':
            continue
        for fn in os.listdir(dir_path):
            if not fn.endswith('.md'):
                continue
            slug = fn[:-3]
            if slug in all_slugs and slug not in slug_to_path:
                slug_to_path[slug] = os.path.join(dir_path, fn)
    # Also check drafts
    drafts_path = os.path.join(APPROVED_BASE, 'drafts')
    if os.path.isdir(drafts_path):
        for d in os.listdir(drafts_path):
            dir_path = os.path.join(drafts_path, d)
            if not os.path.isdir(dir_path):
                continue
            for fn in os.listdir(dir_path):
                if not fn.endswith('.md'):
                    continue
                slug = fn[:-3]
                if slug in all_slugs and slug not in slug_to_path:
                    slug_to_path[slug] = os.path.join(dir_path, fn)

    print(f"Found paths for {len(slug_to_path)}/{len(all_slugs)} slugs")
    missing = all_slugs - set(slug_to_path.keys())
    if missing:
        print(f"Missing slugs (first 10): {sorted(missing)[:10]}")

    success = 0
    skipped = 0
    for concept_slug, concept_title, concept_type, refs in new_concepts:
        for ref_slug in refs:
            if ref_slug not in slug_to_path:
                continue
            ok, msg = add_related(slug_to_path[ref_slug], concept_slug, concept_title, concept_type)
            if ok:
                success += 1
            else:
                if "already" in msg:
                    skipped += 1
    print(f"\nSuccess: {success}, Skipped: {skipped}")


if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    main(dry_run=dry)
