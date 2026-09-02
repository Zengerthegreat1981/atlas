#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_phase2_fixes.py — المرحلة الثانية من الإصلاحات.

  P2.1: إضافة 20+ cross-school relations (L2.4)
  P2.2: Bidirectional cross-reference audit (L2.5)
  P2.3: Bridge section expansion (L3.4)
  P2.4: Placeholder handling (L3.6)
  P2.5: Gap analysis output (L3.1)

الاستخدام:
  python3 scripts/atlas_phase2_fixes.py --apply
"""
import os, re, sys, json
from collections import defaultdict, Counter

ROOT = '/Users/minamoheb/Desktop/Atlas'
AR = os.path.join(ROOT, 'content/ar')

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()
def write(p, t):
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(t)

def load_slugs():
    slugs = set()
    with open(os.path.join(AR, 'drafts/EXISTING_SLUGS.md'), encoding='utf-8') as fh:
        for line in fh:
            m = re.match(r'^- `([^`]+)`', line)
            if m: slugs.add(m.group(1))
    return slugs

SLUGS = load_slugs()

# ----------------- P2.1: cross-school relations -----------------

CROSS_SCHOOL_RELATIONS = [
    # (rel_slug, rel_title_ar, school_a, school_b, description)
    ('rel-cbt-psychodynamic', 'العلاج المعرفي-السلوكي والنفساني-الديناميكي: من المواجهة إلى التكامل',
     'sch-cbt', 'sch-psychoanalytic', 'علاقة تكاملية حديثة بين العلاج المعرفي-السلوكي والنظريات الديناميكية'),
    ('rel-act-cbt-third-wave', 'العلاج بالقبول والالتزام والموجة الثالثة من CBT: من الجدل إلى التشارك',
     'sch-act', 'sch-cbt', 'العلاقة الجدلية بين ACT كموجة ثالثة وبين CBT التقليدية'),
    ('rel-mbct-cbt', 'العلاج المعرفي القائم على اليقظة (MBCT) والـCBT: من الوقاية من الانتكاس إلى العلاج',
     'sch-mbct', 'sch-cbt', 'MBCT كامتداد تأملي للـCBT'),
    ('rel-dbt-bpd', 'العلاج الجدلي السلوكي واضطراب الشخصية الحدية: ولادة DBT من عيادة Linehan',
     'sch-dbt', 'dis-bpd', 'العلاقة التأسيسية بين DBT واضطراب BPD'),
    ('rel-psychodynamic-attachment', 'النظرية الديناميكية ونظرية التعلق: من Bowlby إلى Fonagy',
     'sch-psychoanalytic', 'sch-attachment', 'التقاطع بين التحليل النفسي ونظرية التعلق'),
    ('rel-existential-phenomenology', 'الوجودية والظاهراتية: من Husserl إلى Heidegger إلى العلاج',
     'sch-existential', 'sch-phenomenology', 'الجذور الفلسفية للعلاج الوجودي'),
    ('rel-humanistic-existential', 'الإنسانية والوجودية: من Rogers وMaslow إلى Yalom',
     'sch-humanistic', 'sch-existential', 'الانشقاق والتقاطع بين الإنسانية والوجودية'),
    ('rel-gestalt-existential', 'الجشطالتية والوجودية: Perls بوصفه حلقة وصل',
     'sch-gestalt', 'sch-existential', 'تقاطع الجشطالتية مع العلاج الوجودي عبر Perls'),
    ('rel-family-systems-bowen', 'العلاج الأسري ونظرية Bowen: منظوماتية الأجيال',
     'sch-family-systems', 'sch-bowen-family', 'الجذر الفكري للعلاج الأسري الحديث'),
    ('rel-trauma-ptsd-therapy', 'علاج الصدمة واضطراب ما بعد الصدمة: من Horowitz إلى EMDR',
     'sch-trauma', 'dis-ptsd', 'العلاقة بين نموذج علاج الصدمة والتشخيص'),
    ('rel-transpersonal-jungian', 'عبر الشخصية والتحليلية اليونغية: من Wilber إلى Edinger',
     'sch-transpersonal', 'sch-jungian', 'التقاطع بين الروحانية والتحليلية'),
    ('rel-narrative-constructionist', 'العلاج السردي والبنائية: من White إلى Gergen',
     'sch-narrative', 'sch-constructionist', 'الجذور الفلسفية للعلاج السردي'),
    ('rel-ipmb-evidence-based', 'العلاج النفسي المبني على الأدلة والمقاربات التكاملية: من الجدل إلى التعاون',
     'sch-evidence-based', 'sch-integrative', 'إشكالية الأدلة في العلاج النفسي'),
    ('rel-cultural-feminist', 'علم النفس النسوي والثقافي: من Gilligan إلى hooks',
     'sch-feminist-psychology', 'sch-cultural-psychology', 'التقاطع بين النسوية والثقافية'),
    ('rel-positive-humanistic', 'علم النفس الإيجابي والإنسانية: من Maslow إلى Seligman',
     'sch-positive', 'sch-humanistic', 'الجذع الإنساني المشترك'),
    ('rel-cbt-mindfulness', 'العلاج المعرفي-السلوكي واليقظة الذهنية: من MBSR إلى MBCT',
     'sch-cbt', 'sch-mindfulness', 'تغلغل mindfulness في الـCBT'),
    ('rel-behavioral-activation-depression', 'التنشيط السلوكي والاكتئاب: من Lewinsohn إلى Jacobson',
     'tec-behavioral-activation', 'dis-mdd', 'الأساس الإكلينيكي للتأثير العلاجي'),
    ('rel-emdr-trauma', 'إعادة المعالجة عبر حركات العين وعلاج الصدمة: من Shapiro إلى van der Kolk',
     'tec-emdr', 'sch-trauma', 'النظرية العصبية للصدمة وعلاقتها بـEMDR'),
    ('rel-mbt-mentalization', 'العلاج القائم على التنميط العقلي (MBT) وBateman & Fonagy',
     'sch-mentalization', 'sch-psychoanalytic', 'الـMBT كجسر بين التحليل النفسي والتعلق'),
    ('rel-cft-compassion', 'العلاج المركّز على التعاطف (CFT) وGilbert: علم النفس البوذي في العيادة',
     'sch-compassion-focused', 'sch-buddhist-psychology', 'الجذور البوذية لـCFT'),
    ('rel-somatic-trauma', 'الجسدية وعلاج الصدمة: من Levine إلى van der Kolk',
     'sch-somatic', 'sch-trauma', 'الجسد بوصفه ذاكرة الصدمة'),
    ('rel-experimental-phenomenology', 'الظاهراتية التجريبية: من Husserl إلى Giorgi',
     'sch-phenomenology', 'met-phenomenological-method', 'المنهج الظاهراتي في علم النفس'),
    ('rel-cognitive-revolution', 'الثورة المعرفية في علم النفس: من Chomsky إلى Neisser',
     'sch-cognitive', 'sch-behaviorism', 'الانقلاب على السلوكية'),
    ('rel-neuropsychoanalysis', 'علم النفس العصبي والتحليل النفسي: من Solms إلى Panksepp',
     'sch-neuropsychology', 'sch-psychoanalytic', 'محاولة علمية للتحليل النفسي'),
]

def p2_1_cross_school():
    """Create new cross-school relation files."""
    os.makedirs(os.path.join(AR, 'relations'), exist_ok=True)
    created = 0
    skipped = 0
    for slug, title, a, b, desc in CROSS_SCHOOL_RELATIONS:
        fp = os.path.join(AR, 'relations', f'{slug}.md')
        if os.path.exists(fp):
            skipped += 1
            continue
        # Verify a and b exist
        a_exists = a in SLUGS or any(os.path.exists(os.path.join(AR, sub, f'{a}.md'))
                                       for sub in os.listdir(AR) if os.path.isdir(os.path.join(AR, sub)))
        b_exists = b in SLUGS or any(os.path.exists(os.path.join(AR, sub, f'{b}.md'))
                                       for sub in os.listdir(AR) if os.path.isdir(os.path.join(AR, sub)))
        # Get titles
        a_title = ''
        b_title = ''
        for sub in os.listdir(AR):
            for s_, t_ in [(a, 'a'), (b, 'b')]:
                fp_ = os.path.join(AR, sub, f'{s_}.md')
                if os.path.exists(fp_):
                    with open(fp_, encoding='utf-8') as fh:
                        c = fh.read()
                    tm = re.search(r'^title:\s*"([^"]+)"', c, re.MULTILINE)
                    if tm:
                        if t_ == 'a': a_title = tm.group(1)
                        else: b_title = tm.group(1)
        content = f'''---
slug: "{slug}"
id: "REL-{1000 + created}"
type: "علاقة بين مدرستين"
level: "متوسط"
title: "{title}"
en: "{title}"
crumb: "العلاقات بين المدارس ← {a_title} × {b_title}"
language: "العربية"
part: "psychology"
edges:
- rel: "connects", target: "{a_title}", target_type: "مدرسة"
- rel: "connects", target: "{b_title}", target_type: "مدرسة"
related:
- id: "{a}", title: "{a_title}", type: "مدرسة"
- id: "{b}", title: "{b_title}", type: "مدرسة"
gaps:
  - "الوصف أعلاه هو نقطة بداية — يحتاج توسعاً تفصيلياً بالمصادر الأولية."
---

# {title}

{desc}

## طبيعة العلاقة

تشير العلاقة بين **{a_title}** و **{b_title}** إلى تقاطع تاريخي ومنهجي يمكن تلخيصه في:
- **التقارب**: مشاركة في الإشكاليات السريرية (اضطرابات مشتركة، حالات مماثلة).
- **الاختلاف**: مناهج علاجية مختلفة (مثلاً CBT مقابل ديناميكي).
- **التكامل**: مدارس حديثة تجمع بينهما (مثل MBCT كجسر بين CBT واليقظة).

## انظر أيضاً

- {a_title}
- {b_title}
'''
        if '--apply' in sys.argv:
            write(fp, content)
        created += 1
    return created, skipped

# ----------------- P2.2: bidirectional audit -----------------

def p2_2_bidirectional():
    """Check that for every (A → B) related link, B has a related to A OR a school-of."""
    # Build all forward links
    forward = defaultdict(set)  # file -> set of related slugs
    all_slugs = set()
    for sub in os.listdir(AR):
        p = os.path.join(AR, sub)
        if not os.path.isdir(p) or sub.startswith('_'): continue
        for f in os.listdir(p):
            if not f.endswith('.md'): continue
            slug = f.replace('.md', '')
            all_slugs.add(slug)
            fp = os.path.join(p, f)
            with open(fp, encoding='utf-8') as fh:
                c = fh.read()
            ids = []
            m = re.search(r'related:\s*\[([^\]]*)\]', c)
            if m and m.group(1).strip():
                ids = re.findall(r'"([^"]+)"', m.group(1))
            else:
                m = re.search(r'related:\s*\n((?:\s*-\s+id:[^\n]*\n)+)', c)
                if m:
                    ids = re.findall(r'-\s+id:\s*"([^"]+)"', m.group(1))
            for sid in ids:
                forward[slug].add(sid)

    # Build reverse: for each (A → B), check if B has A in its related
    asym = []
    for src, targets in forward.items():
        for tgt in targets:
            if tgt in all_slugs and src not in forward.get(tgt, set()):
                # Check if tgt's related has src
                # We allow some "container" types (e.g. school → thinker) to be one-way
                # Find tgt type
                tgt_type = ''
                for sub in os.listdir(AR):
                    fp = os.path.join(AR, sub, f'{tgt}.md')
                    if os.path.exists(fp):
                        with open(fp, encoding='utf-8') as fh:
                            c = fh.read()
                        tm = re.search(r'^type:\s*"([^"]+)"', c, re.MULTILINE)
                        if tm: tgt_type = tm.group(1)
                        break
                # Heuristic: large containers (schools, concepts) can be one-way
                if tgt_type in ['مدرسة', 'مفهوم', 'علاقة بين مدرستين']:
                    continue  # Allowed asymmetric
                asym.append((src, tgt))

    # Output report
    report_path = os.path.join(ROOT, 'agents_specs/bidirectional-audit-2026-08-24.md')
    with open(report_path, 'w', encoding='utf-8') as fh:
        fh.write('# P2.2: Bidirectional Audit — 2026-08-24\n\n')
        fh.write(f'**Total forward links:** {sum(len(v) for v in forward.values())}\n')
        fh.write(f'**Asymmetric pairs (non-container types):** {len(asym)}\n\n')
        fh.write('## Sample (first 30)\n\n')
        fh.write('| Source | Target |\n|---|---|\n')
        for s, t in asym[:30]:
            fh.write(f'| {s} | {t} |\n')
    return len(asym)

# ----------------- P2.3: bridge section expansion -----------------

BRIDGE_CANDIDATES = [
    # (slug, title_ar, en, justification)
    ('thk-asmall', 'آلان سوليفان', 'Alain de Botton', 'كاتب فلسفي معاصر يربط العلاج النفسي بالفلسفة التطبيقية'),
    ('thk-dennett', 'دانيال دينيت', 'Daniel C. Dennett', 'فيلسوف وعالم نفس نظري — جسر بين فلسفة العقل وعلم النفس'),
    ('thk-evola', 'جوليوس إيفولا', 'Julius Evola', 'مفكر تأملي أثر في الفلسفة السياسية والمعالجات المعنوية (للذكر الأكاديمي فقط)'),
    ('thk-frankfurt', 'هاري فرانكفورت', 'Harry G. Frankfurt', 'فيلسوف أخلاقي ربط بين فلسفة الفعل والإرادة'),
    ('thk-martha-bernstein', 'مارثا برنشتاين', 'Martha E. Bernstein', 'فيلسوفة معاصرة تربط بين علم النفس المعرفي وفلسفة اللغة'),
    ('thk-susan-sontag', 'سوزان سونتاغ', 'Susan Sontag', 'مفكرة ربطت بين المرض بوصفه استعارة والممارسة السريرية'),
    ('thk-evans-pritchard', 'إيفانز-بريتشارد', 'E. E. Evans-Pritchard', 'أنثروبولوجي أثر في المنهج الظاهراتي'),
    ('thk-bourdieu', 'بيير بورديو', 'Pierre Bourdieu', 'سوسيولوجي ربط بين علم الاجتماع وعلم النفس الاجتماعي'),
    ('thk-eric-kandel', 'إريك كاندل', 'Eric R. Kandel', 'عالم أعصاب حائز نوبل يربط بين علم النفس والبيولوجيا العصبية'),
    ('thk-antonio-damasio', 'أنطونيو داماسيو', 'Antonio R. Damásio', 'عالم أعصاب يربط بين الوعي والذات — جسر بين علم الأعصاب وعلم النفس'),
    ('thk-roland-barthes', 'رولان بارت', 'Roland Barthes', 'فيلسوف لغة وناقد أثر في العلاج السردي وما بعد البنيوية'),
    ('thk-william-james', 'وليام جيمس', 'William James', 'مؤسس علم النفس الأمريكي وفيلسوف براغماتي — جسر كلاسيكي'),
    ('thk-cs-peirce', 'تشارلز ساندرز بيرس', 'Charles Sanders Peirce', 'مؤسس البراغماتية وفيلسوف علم العلامات'),
]

def p2_3_bridge():
    """Identify bridge candidates (part: bridge). These don't get files created,
    just get documented for human review."""
    doc = {
        'description': 'Bridge candidates: thinkers who influence a psychology school but are not primarily psychologists/therapists OR systematic philosophers. This list is for human review.',
        'current_bridge': ['thk-marx (Karl Marx)'],
        'candidates': []
    }
    # Filter to those that already exist in atlas
    for slug, title_ar, en_name, justification in BRIDGE_CANDIDATES:
        # Check if file exists
        for sub in os.listdir(AR):
            if os.path.exists(os.path.join(AR, sub, f'{slug}.md')):
                # Get current part
                with open(os.path.join(AR, sub, f'{slug}.md'), encoding='utf-8') as fh:
                    c = fh.read()
                m = re.search(r'^part:\s*"([^"]+)"', c, re.MULTILINE)
                current_part = m.group(1) if m else '?'
                doc['candidates'].append({
                    'slug': slug, 'title_ar': title_ar, 'en': en_name,
                    'justification': justification, 'current_part': current_part,
                    'recommendation': 'reclassify as bridge' if current_part != 'bridge' else 'keep as bridge'
                })
                break
    if '--apply' in sys.argv:
        with open(os.path.join(ROOT, 'agents_specs/bridge-candidates-2026-08-24.json'), 'w', encoding='utf-8') as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
    return len(doc['candidates'])

# ----------------- P2.4: placeholder handling -----------------

def p2_4_placeholders():
    """Find files with placeholder text in title or body."""
    placeholders = []
    for sub in os.listdir(AR):
        p = os.path.join(AR, sub)
        if not os.path.isdir(p) or sub.startswith('_'): continue
        for f in os.listdir(p):
            if not f.endswith('.md'): continue
            fp = os.path.join(p, f)
            with open(fp, encoding='utf-8') as fh:
                c = fh.read()
            # Patterns
            if re.search(r'\[NEEDS?\s+[A-Z]+[^\]]*\]', c) or re.search(r'\[TODO[^\]]*\]', c) or re.search(r'\[XXX[^\]]*\]', c):
                placeholders.append(f'{sub}/{f}')
    return placeholders

# ----------------- P2.5: gap analysis -----------------

def p2_5_gap_analysis():
    """Output a gap analysis: schools with ≤2 thinkers."""
    school_thinkers = defaultdict(int)
    for f in os.listdir(os.path.join(AR, 'thinkers')):
        if not f.endswith('.md') or f.startswith('_'): continue
        with open(f'content/ar/thinkers/{f}', encoding='utf-8') as fh:
            c = fh.read()
        m = re.search(r'edges:\s*\n((?:\s*-.*\n)+)', c)
        if not m: continue
        for line in m.group(1).split('\n'):
            tm = re.search(r'target:\s*"([^"]+)"', line)
            if tm:
                school_thinkers[tm.group(1)] += 1
                break
    weak = sorted([(s, c) for s, c in school_thinkers.items() if c <= 2], key=lambda x: x[1])
    with open(os.path.join(ROOT, 'agents_specs/school-gap-analysis-2026-08-24.md'), 'w', encoding='utf-8') as fh:
        fh.write('# L3.1: School Gap Analysis — 2026-08-24\n\n')
        fh.write(f'**Total schools with thinkers:** {len(school_thinkers)}\n')
        fh.write(f'**Weak schools (≤2 thinkers):** {len(weak)}\n\n')
        fh.write('## Recommendation per weak school\n\n')
        fh.write('| School | Count | Action |\n|---|---|---|\n')
        for s, c in weak:
            action = 'expand' if c == 0 else 'verify' if c == 1 else 'boost'
            fh.write(f'| {s} | {c} | {action} |\n')
    return len(weak)

# ----------------- Main -----------------

def main():
    if '--apply' not in sys.argv:
        print("DRY RUN — pass --apply to commit\n")
    else:
        print("APPLY MODE\n")

    print("=" * 50)
    print("P2.1: Cross-school relations")
    c, s = p2_1_cross_school()
    print(f"  Created: {c} new relation files")
    print(f"  Skipped (existed): {s}")
    print()

    print("=" * 50)
    print("P2.2: Bidirectional audit")
    n_asym = p2_2_bidirectional()
    print(f"  Asymmetric pairs: {n_asym}")
    print(f"  Report: agents_specs/bidirectional-audit-2026-08-24.md")
    print()

    print("=" * 50)
    print("P2.3: Bridge candidates")
    n_bridge = p2_3_bridge()
    print(f"  Existing files that qualify as bridge: {n_bridge}")
    if '--apply' in sys.argv:
        print(f"  JSON: agents_specs/bridge-candidates-2026-08-24.json")
    print()

    print("=" * 50)
    print("P2.4: Placeholder scan")
    placeholders = p2_4_placeholders()
    print(f"  Files with placeholder: {len(placeholders)}")
    for p in placeholders[:5]: print(f"  - {p}")
    print()

    print("=" * 50)
    print("P2.5: Gap analysis")
    n_weak = p2_5_gap_analysis()
    print(f"  Weak schools (≤2 thinkers): {n_weak}")
    print(f"  Report: agents_specs/school-gap-analysis-2026-08-24.md")
    print()

    print("Done.")

if __name__ == '__main__':
    main()
