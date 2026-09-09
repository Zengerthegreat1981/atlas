# -*- coding: utf-8 -*-
"""دمج دفعة `relations/` القالبية في نظائرها المكتوبة، وتحويلها إلى إحالات.

الدفعة القالبية القديمة (ملفات ~2 كيلوبايت بمتن مولَّد واحد: «التقارب /
الاختلاف / التكامل») تتقاطع مع ملفات علاقات **مكتوبة فعلاً** بـslugs أخرى.
كل زوج أدناه قرار مراجَع: تحقّقتُ أن الملف الهدف يغطّي **طرفَي العلاقة معاً**
وليس طرفاً واحداً — فما غطّى طرفاً واحداً لم يُدمج بل يُكتب متنه (خارج نطاق
هذا السكريبت).

القاعدة المتَّبعة (قاعدة المستودع): لا يُحذف ملف ولا يُعاد تسمية slug. تُحفظ
النسخة الأصلية في `agents_specs/merge-archive-2026-09-07/`، ويصير الملف إحالة
دائمة تحفظ كل رابط وارد إليه.

    python3 scripts/merge_duplicate_relations.py           # فحص
    python3 scripts/merge_duplicate_relations.py --apply   # تنفيذ
"""
import os, re, sys, shutil

APPLY = "--apply" in sys.argv
REL = os.path.join('content', 'ar', 'relations')
ARCH = os.path.join('agents_specs', 'merge-archive-2026-09-07')

# القالبي -> (المكتوب، مسوّغ الدمج)
MERGES = {
    'rel-cbt-psychodynamic': (
        'rel-psychoanalysis-cbt',
        'الملف الهدف يعالج الزوج نفسه (التحليل النفسي × CBT) في 11 ألف حرف، '
        'ويبدأ من حيث يقف هذا الملف: أن بيك وإيليس كلاهما بدأ محلِّلاً.'),
    'rel-positive-humanistic': (
        'rel-humanistic-positive',
        'الزوج نفسه (الإنسانية × علم النفس الإيجابي) ونفس المسار المعلَن '
        '«من ماسلو إلى سليغمان»، مكتوباً في 11.7 ألف حرف.'),
    'rel-cognitive-revolution': (
        'rel-behaviorism-cognitive',
        'الثورة المعرفية هي بالضبط موضوع الملف الهدف (قسم «الثورة المعرفية '
        'الصريحة 1956–1970»)، وفيه تولمان وباندورا وبيك التي يسمّيها هذا الملف.'),
    'rel-gestalt-existential': (
        'rel-humanistic-existential-gestalt',
        'الملف الهدف يخصّص قسماً للجشطالتية بوصفها «أختاً فلسفية» للوجودية، '
        'ويردّ الطرفين إلى الظاهراتية — وهو ما يختصره هذا الملف في سطر.'),
    'rel-somatic-trauma': (
        'rel-trauma-somatic',
        'الزوج نفسه (الجسدية × الصدمة) و«من ليفين إلى فان دير كولك» هو مسار '
        'الملف الهدف نفسه، في 18 ألف حرف مع مقارنة بعلاجات الصدمة الأخرى.'),
    'rel-existential-phenomenology': (
        'rel-phenomenology-existential-therapy',
        'الملف الهدف يشترك مع هذا الملف في **طرفَي** العلاقة معاً، ويفصّل '
        'مسار «هوسرل ← هايدغر ← العلاج» عبر ياسبرز وبينسفانغر وبوس وماي.'),
    'rel-cbt-mindfulness': (
        'rel-mbct-cbt',
        'ملفان قالبيان على موضوع واحد (CBT × اليقظة، MBSR ← MBCT). '
        'الـslug الهدف أدقّ تسميةً للزوج، وقد كُتب متنه في هذه الجلسة.'),
    'rel-emdr-trauma': (
        'rel-trauma-ptsd-therapy',
        'ملفان قالبيان على موضوع واحد بطرفين متطابقين (`sch-emdr` × `dis-ptsd`). '
        'الملف الهدف أوسع صياغةً (علاج الصدمة وPTSD عموماً، وEMDR داخله) وقد '
        'كُتب متنه في هذه الجلسة.'),
}


def title_of(slug):
    raw = open(os.path.join(REL, slug + '.md'), encoding='utf-8').read()
    return re.search(r'^title:\s*"(.*?)"', raw, re.M).group(1)


os.makedirs(ARCH, exist_ok=True)
n = 0
for src, (dst, why) in sorted(MERGES.items()):
    p = os.path.join(REL, src + '.md')
    raw = open(p, encoding='utf-8').read()
    if 'إحالة' in raw.split('---')[1]:
        print(f"  {src}: إحالة بالفعل — يُتخطّى")
        continue
    fm = raw.split('---')[1]
    keep = {k: (re.search(rf'^{k}:\s*(.*)$', fm, re.M).group(1)
                if re.search(rf'^{k}:\s*(.*)$', fm, re.M) else '""')
            for k in ('id', 'type', 'level', 'part', 'language')}
    old_title = title_of(src)
    dst_title = title_of(dst)

    new = f'''---
slug: "{src}"
id: {keep['id']}
type: {keep['type']}
level: {keep['level']}
part: {keep['part']}
title: "{old_title} — إحالة، انظر {dst}"
en: "Merged — see {dst}"
crumb: "العلاقات بين المدارس ← [إحالة]"
active_start: null
active_end: null
edges: []
related:
- id: "{dst}", title: "{dst_title}", type: "علاقة بين مدرستين"
gaps:
  - "**دُمج 2026-09-07:** هذا الملف من دفعة قالبية قديمة في `relations/` (متن مولَّد واحد: «التقارب / الاختلاف / التكامل» بلا خصوصية للزوج) تتقاطع مع علاقات مكتوبة بـslugs أخرى. مسوّغ الدمج: {why}"
  - "لا يُعاد كتابة متن تحت هذا الـslug. الـslug باقٍ ولم يُحذف عملاً بقاعدة عدم إعادة التسمية، فكل رابط وارد يصل إلى هذه الإحالة. النسخة الأصلية في `agents_specs/merge-archive-2026-09-07/{src}.md.archived.2026-09-07`."
---

# {old_title} — إحالة

**دُمج هذا الملف.** المعالجة الكاملة لهذه العلاقة في `{dst}` — «{dst_title}».

{why}

## المصادر

التوثيق البيبليوغرافي في الملف المُحال إليه `{dst}`، لا في هذه الإحالة.
'''
    print(f"  {src:<34} → {dst}")
    n += 1
    if APPLY:
        shutil.copy(p, os.path.join(ARCH, f'{src}.md.archived.2026-09-07'))
        open(p, 'w', encoding='utf-8').write(new)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {n} ملفاً حُوِّل إلى إحالة")
