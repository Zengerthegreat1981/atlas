# -*- coding: utf-8 -*-
"""تعبئة الخانات الفارغة في دفعة `relations/` المولَّدة من قالب.

المشكلة: دفعة قديمة من ملفات `rel-*` وُلّدت من قالب يحلّ طرفَي العلاقة من
فهرس الـslugs. حين لم يجد المولِّد الـslug، كتب الخانة **فارغة** ومضى: فصار
في الملفّ `target: ""` و`title: ""` و`crumb` ينتهي بـ«← × » و`****` في المتن
(اسم بين علامتَي تشديد بلا اسم). النتيجة على الموقع: عناوين وروابط فارغة.

هذا السكريبت يحلّ كل طرف إلى slug **موجود فعلاً** في `content/ar` بحسب
الخريطة التحريرية أدناه (كل سطر قرار مراجَع، لا تخمين آلي)، ثم:
  - يعبّئ `edges` و`related` و`crumb` والمتن بالاسم الحقيقي،
  - ولا يلمس أي ملف ليس فيه خانة فارغة.

    python3 scripts/fill_relation_template_holes.py           # فحص
    python3 scripts/fill_relation_template_holes.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
REL_DIR = os.path.join('content', 'ar', 'relations')

# slug -> (طرف أول، طرف ثانٍ). كل طرف slug موجود في الأطلس.
SIDES = {
    'rel-psychodynamic-attachment':   ('sch-psychoanalysis', 'br-attachment-theory'),
    'rel-cognitive-revolution':       ('sch-cognitive-behavioral', 'sch-behaviorism'),
    'rel-neuropsychoanalysis':        ('sch-psychoanalysis', 'sch-biological-neuro'),
    'rel-somatic-trauma':             ('sch-somatic-experiencing', 'br-sensorimotor-trauma-applications'),
    'rel-transpersonal-jungian':      ('sch-transpersonal', 'br-jungian'),
    'rel-emdr-trauma':                ('sch-emdr', 'dis-ptsd'),
    'rel-family-systems-bowen':       ('sch-systemic-family', 'tec-bowen-family-systems'),
    'rel-experimental-phenomenology': ('sch-phenomenology', 'stu-descriptive-phenomenological-method-giorgi'),
    'rel-cft-compassion':             ('sch-cft', 'sch-buddhist-psychology'),
    'rel-cbt-psychodynamic':          ('sch-cognitive-behavioral', 'sch-psychoanalysis'),
    'rel-ipmb-evidence-based':        ('con-evidence-based-practice', 'dbt-common-factors-vs-specific-ingredients'),
    'rel-gestalt-existential':        ('sch-gestalt-therapy', 'sch-existential-therapy'),
    'rel-existential-phenomenology':  ('sch-existential-therapy', 'sch-phenomenology'),
    'rel-mbt-mentalization':          ('tec-mbt', 'con-mentalization'),
    'rel-cbt-mindfulness':            ('sch-cognitive-behavioral', 'sch-mbct'),
    'rel-narrative-constructionist':  ('sch-narrative-therapy', 'br-social-constructionism'),
    'rel-cultural-feminist':          ('br-feminist-therapy', 'br-relational-cultural'),
    'rel-trauma-ptsd-therapy':        ('dis-ptsd', 'sch-emdr'),
    'rel-positive-humanistic':        ('sch-positive-psychology', 'sch-humanistic'),
}


def build_index():
    idx = {}
    for f in glob.glob(os.path.join('content', 'ar', '*', '*.md')):
        if '_merged' in f or 'drafts' in f:
            continue
        raw = open(f, encoding='utf-8').read()
        s = re.search(r'^slug:\s*"(.*?)"', raw, re.M)
        t = re.search(r'^title:\s*"(.*?)"', raw, re.M)
        ty = re.search(r'^type:\s*"(.*?)"', raw, re.M)
        if s:
            idx[s.group(1)] = (t.group(1) if t else '', ty.group(1) if ty else '')
    return idx


idx = build_index()
for slug, (a, b) in SIDES.items():
    for side in (a, b):
        if side not in idx:
            raise SystemExit(f"خريطة معطوبة: {slug} يشير إلى {side} وهو غير موجود")

n = 0
for slug, (a, b) in sorted(SIDES.items()):
    p = os.path.join(REL_DIR, slug + '.md')
    raw = open(p, encoding='utf-8').read()
    pre, fm, body = raw.split('---', 2)
    ta, tya = idx[a]
    tb, tyb = idx[b]
    nfm, nbody = fm, body

    # 1. edges: يُعاد بناء ضلعَي connects كاملين بالاسمين الحقيقيين
    nfm = re.sub(
        r'^edges:.*?(?=^related:|^gaps:|\Z)',
        f'edges:\n- rel: "connects", target: "{a}", target_type: "{tya}"\n'
        f'- rel: "connects", target: "{b}", target_type: "{tyb}"\n',
        nfm, flags=re.M | re.S)

    # 2. related: كل بند فارغ العنوان يُعبَّأ من الفهرس (لا يُحذف بند)
    def fill_rel(m):
        rid, title, typ = m.group(1), m.group(2), m.group(3)
        if title.strip() or rid not in idx:
            return m.group(0)
        t, ty = idx[rid]
        return f'- id: "{rid}", title: "{t}", type: "{ty}"'
    nfm = re.sub(r'-\s*id:\s*"([^"]*)",\s*title:\s*"([^"]*)",\s*type:\s*"([^"]*)"',
                 fill_rel, nfm)

    # 3. crumb: «العلاقات بين المدارس ←  × » -> بالاسمين
    nfm = re.sub(r'^crumb:\s*".*"$',
                 f'crumb: "العلاقات بين المدارس ← {ta} × {tb}"', nfm, flags=re.M)

    # 4. المتن: **** -> الاسم الحقيقي، بالترتيب (الطرف الأول ثم الثاني)
    if '****' in nbody:
        line_re = re.compile(r'^(تشير العلاقة بين ).*?( إلى تقاطع.*)$', re.M)
        nbody = line_re.sub(lambda m: f'{m.group(1)}**{ta}** و **{tb}**{m.group(2)}', nbody)
    # 5. «انظر أيضاً» ببنود فارغة
    nbody = re.sub(r'^##\s*انظر أيضاً\s*\n((?:-.*\n|\s*\n)*)',
                   f'## انظر أيضاً\n\n- {ta}\n- {tb}\n\n', nbody, flags=re.M)

    if (nfm, nbody) == (fm, body):
        continue
    n += 1
    print(f"  {slug:<34} {ta[:26]} × {tb[:26]}")
    if APPLY:
        open(p, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + nbody)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {n} ملفاً")
