# -*- coding: utf-8 -*-
"""إصلاح الإحالات المعلَّقة: `related.id` و`edges.target` إلى slugs غير موجودة.

نوعان من العلّة، ولكلٍّ علاجه:

1. **مُوازٍ موجود بـslug آخر** (`thk-buber` والملف الفعلي `thk-mbuber`،
   `sch-psychodrama` والملف `br-psychodrama`). العلاج: تحويل الإحالة إلى
   الـslug الصحيح. كل زوج في `ALIASES` أدناه **مُتحقَّق منه بالاسم** (طابقتُ
   العنوان المسجَّل في الإحالة نفسها بعنوان الملف الهدف)، لا بتشابه الـslug.

2. **لا وجود للهدف في الأطلس**. العلاج ليس تصحيح الرابط بل الاعتراف به:
   - في `related`: يُحذف البند ويُسجَّل بدلاً منه بند `gaps` صريح يسمّي
     العنوان المفقود — فلا يبقى رابط ميت ولا تُفقد المعلومة.
   - في `edges.target`: يُستبدل الـslug بالاسم العربي نصّاً حرّاً (وهو
     الاصطلاح القائم فعلاً في الأطلس لأهداف بلا ملف) — فلا يبقى ما يبدو
     رابطاً وهو ليس رابطاً.

    python3 scripts/repair_dangling_refs.py           # فحص
    python3 scripts/repair_dangling_refs.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv

# مُتحقَّق منها بمطابقة الاسم المسجَّل بعنوان الملف الهدف
ALIASES = {
    'thk-buber': 'thk-mbuber',
    'thk-cgilligan': 'thk-gilligan',
    'thk-daniel-stern': 'thk-dstern',
    'wrk-studies-hysteria-freud': 'wrk-studien-hysterie',
    'sch-antipsychiatry': 'br-antipsychiatry',
    'sch-ericksonian-hypnosis': 'tec-ericksonian-hypnotherapy',
    'sch-gestalt-psychology': 'br-gestalt-berlin',
    'sch-psychodrama': 'br-psychodrama',
    'sch-transactional-analysis': 'br-transactional-analysis',
    'sch-drama-therapy': 'tec-drama-therapy',
    'sch-music-therapy': 'tec-music-therapy',
    'sch-naikan-therapy': 'tec-naikan-therapy',
    'sch-open-dialogue': 'tec-open-dialogue',
    'sch-adlerian': 'br-adlerian',
    'sch-dir-floortime': 'tec-dir-floortime',
    'sch-authentic-movement': 'tec-authentic-movement',
    'sch-general-systems-theory': 'br-general-systems-cybernetics',
    # دفعة ثانية: ظهرت بعد توحيد ترتيب الحقول (بنود كانت تُهمَل بصمت).
    # كلها مطابقة اسم-باسم؛ رُفض ما تشابه فيه اللقب واختلف الشخص
    # (thk-cbrode «كريستينا رود» ≠ thk-cgrof «كريستينا غروف»،
    #  thk-evandeurzen «إيريكا» ≠ thk-vandeurzen «إيمي»،
    #  thk-handersen «هارجيت» ≠ thk-handerson «هارلين»).
    'br-british-existential': 'br-british',
    'thk-cgj': 'thk-jung',
    'thk-dkrauss': 'thk-david-krauss',
    'thk-dwfisher': 'thk-dan-fisher',
    'thk-ecoue': 'thk-emilecoue',
    'thk-gmack': 'thk-gcraig',
    'thk-hzehr': 'thk-zehr',
    'thk-jbraithwaite': 'thk-john-braithwaite',
    'thk-jhillman': 'thk-hillman',
    'thk-jlmoreno': 'thk-jmoreno',
    'thk-jloehr': 'thk-jim-loehr',
    'thk-jweiser': 'thk-judy-weiser',
    'thk-masondurie': 'thk-trore',
    'thk-mcooper': 'thk-cooper',
    'thk-mcsikszentmihalyi': 'thk-csikszentmihalyi',
    'thk-mestherharding': 'thk-meharding',
    'thk-ovaas': 'thk-lovaas',
    'thk-pkerr': 'thk-mkerr',
    'thk-rjlandy': 'thk-rlandy-md',
    'thk-tschoop': 'thk-trudi-schoop',
    'thk-tstonge': 'thk-thomas-harris',
    'thk-twhite': 'thk-tony-white',
}

# أهداف edges بلا ملف في الأطلس: تُكتب بالاسم العربي نصّاً حرّاً
EDGE_NAMES = {
    'sch-cognitive-psychology': 'علم النفس المعرفي',
    'sch-trauma-psychology': 'علم نفس الصدمة',
    'sch-cross-cultural-psychology': 'علم النفس عبر الثقافي',
    'sch-cognitive-neuroscience': 'علم الأعصاب المعرفي',
    'sch-art-therapy': 'العلاج بالفن',
    'sch-multicultural-counseling': 'الإرشاد متعدد الثقافات',
    'sch-critical-psychology': 'علم النفس النقدي',
    'sch-clinical-mindfulness': 'اليقظة الذهنية الإكلينيكية',
    'sch-ecotherapy': 'العلاج البيئي',
    'sch-addiction-psychology': 'علم نفس الإدمان',
    'sch-school-bullying-research': 'بحوث التنمّر المدرسي',
    'sch-phenomenological-research-methodology': 'منهجية البحث الظاهراتي',
    'sch-analytic-ethics': 'الأخلاق التحليلية',
    'sch-socratic': 'السقراطية',
    'sch-pre-socratic': 'ما قبل السقراطية',
    'sch-group-therapy': 'العلاج الجماعي',
    'sch-child-psychiatry': 'طب نفس الطفل',
    'sch-psychology-of-religion': 'علم نفس الدين',
    'sch-thanatology': 'علم الموت (Thanatology)',
    'sch-symbolic-interactionism': 'التفاعلية الرمزية',
    'sch-psychology-of-love': 'علم نفس الحب',
    'sch-structuralism-wundt-titchener': 'البنيوية (فونت وتيتشنر)',
    'sch-ecological-psychology': 'علم النفس الإيكولوجي',
    'sch-cultural-psychology': 'علم النفس الثقافي',
    'sch-existential-phenomenology-therapy': 'العلاج الظاهراتي الوجودي',
    'sch-taoist-cognitive-therapy': 'العلاج المعرفي الطاوي',
    'sch-strategic-family': 'العلاج الأسري الاستراتيجي',
    'sch-contemplative-psychotherapy': 'العلاج النفسي التأملي',
    'sch-sleep-neuroscience': 'علم أعصاب النوم',
    'sch-positive-psychotherapy-peseschkian': 'العلاج النفسي الإيجابي (بسشكيان)',
    'sch-eft-tapping': 'تقنيات التحرر الانفعالي (EFT Tapping)',
    'sch-political-philosophy': 'الفلسفة السياسية',
    'sch-emotion-psychology': 'علم نفس الانفعال',
    'thk-gardner': 'هوارد غاردنر',
    'thk-goffman': 'إرفينغ غوفمان',
    'thk-spearman': 'تشارلز سبيرمان',
    'br-adolescent-development': 'نمو المراهقة',
    'br-behavioral-neurology': 'طب الأعصاب السلوكي',
    'br-clinical-neuropsychology': 'علم النفس العصبي الإكلينيكي',
    'br-cognitive-development': 'النمو المعرفي',
    'br-experiential-family': 'العلاج الأسري الخبراتي',
    'br-language-development': 'النمو اللغوي',
    'br-metta-meditation': 'تأمّل المحبة (Metta)',
    'br-moral-development': 'النمو الأخلاقي',
    'br-psychopharmacology': 'علم الأدوية النفسية',
    'br-psychosocial-development': 'النمو النفسي-الاجتماعي',
}

SLUGISH = re.compile(r'^(thk|con|sch|tec|wrk|dis|dbt|evt|met|que|trm|rel|exp|stu|ctx|ins|crt|axm|dia|br|syn|eth)-')
REL = re.compile(r'^(\s*)-\s*id:\s*"([^"]*)",\s*title:\s*"([^"]*)",\s*type:\s*"([^"]*)"\s*$', re.M)
EDG = re.compile(r'^(\s*)-\s*rel:\s*"([^"]*)",\s*target:\s*"([^"]*)",\s*target_type:\s*"([^"]*)"\s*$', re.M)


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
for a, b in ALIASES.items():
    if b not in idx:
        raise SystemExit(f"خريطة معطوبة: البديل {b} غير موجود")

stats = dict(alias_rel=0, alias_edge=0, gap_rel=0, freetext_edge=0, files=0)
left = set()

for f in sorted(glob.glob(os.path.join('content', 'ar', '*', '*.md'))):
    if '_merged' in f or 'drafts' in f:
        continue
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    nfm = fm
    new_gaps = []

    def do_rel(m):
        ind, rid, title, typ = m.groups()
        if not rid or rid in idx:
            return m.group(0)
        if rid in ALIASES:
            tgt = ALIASES[rid]
            stats['alias_rel'] += 1
            return f'{ind}- id: "{tgt}", title: "{idx[tgt][0]}", type: "{idx[tgt][1]}"'
        # لا وجود للهدف: يُحذف البند ويُسجَّل كفجوة صريحة
        stats['gap_rel'] += 1
        new_gaps.append(
            f'إحالة معلَّقة أُزيلت: «{title}» ({rid}) — لا ملف بهذا الـslug في '
            f'الأطلس، فلا يصحّ إبقاؤه رابطاً. المدخل ناقص حتى يُكتب هدفه.')
        return '\x00'

    nfm = REL.sub(do_rel, nfm)
    nfm = re.sub(r'\n?\x00', '', nfm)

    def do_edge(m):
        ind, rel, tgt, tt = m.groups()
        if not tgt or tgt in idx or not SLUGISH.match(tgt):
            return m.group(0)
        if tgt in ALIASES:
            stats['alias_edge'] += 1
            return f'{ind}- rel: "{rel}", target: "{ALIASES[tgt]}", target_type: "{tt}"'
        if tgt in EDGE_NAMES:
            stats['freetext_edge'] += 1
            return f'{ind}- rel: "{rel}", target: "{EDGE_NAMES[tgt]}", target_type: "{tt}"'
        left.add(tgt)
        return m.group(0)

    nfm = EDG.sub(do_edge, nfm)

    if new_gaps:
        block = "".join(f'  - "{g}"\n' for g in new_gaps)
        if re.search(r'^gaps:\s*$', nfm, re.M):
            nfm = re.sub(r'^gaps:\s*\n', 'gaps:\n' + block, nfm, count=1, flags=re.M)
        else:
            nfm = nfm.rstrip('\n') + '\ngaps:\n' + block

    if nfm == fm:
        continue
    stats['files'] += 1
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + body)

print(f"{'APPLIED' if APPLY else 'DRY RUN'} — {stats['files']} ملفاً")
print(f"  related مُحال إلى slug صحيح : {stats['alias_rel']}")
print(f"  related مُحوَّل إلى فجوة صريحة: {stats['gap_rel']}")
print(f"  edges مُحال إلى slug صحيح   : {stats['alias_edge']}")
print(f"  edges مُحوَّل إلى نصّ حرّ      : {stats['freetext_edge']}")
if left:
    print("  ما زال بلا معالجة (يلزم اسم في EDGE_NAMES): " + ", ".join(sorted(left)))
