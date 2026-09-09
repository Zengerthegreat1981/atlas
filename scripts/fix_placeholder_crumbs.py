# -*- coding: utf-8 -*-
"""إصلاح مسارات التنقّل القالبية التي تحمل اسمَ المجلد بالإنجليزية.

185 ملفَّ مفكّرٍ يحمل `crumb: "الأطلس ← thinkers ← <العنوان>"` — وهو مسارٌ
قالبي من دفعة إنشاءٍ لم يُستكمَل: يعرض على مستخدمٍ عربي **اسمَ المجلد
بالإنجليزية** (`thinkers`) في موضع اسم القسم، ويجعل جذرَ المسار «الأطلس»
وهو جذرٌ عامّ لا يفيد موضعاً — فيظهر 185 مدخلاً بلا موقعٍ في الشجرة.

العلاج، بحسب ما هو متاح في الملف نفسه:
  1. **إن كان له أبٌ مصرَّح** (ضلعُ `belongs_to`، أو أوّلُ بندٍ في `related`
     نوعُه مدرسة/تيار/تقنية): يُبنى المسارُ على اصطلاح المجلد الغالب
     «<عنوان الأب> ← الناس ← <العنوان>».
  2. **وإن لم يكن له أب**: يُكتب «الناس ← <العنوان>» — وهو اصطلاحٌ ثنائي قائم
     فعلاً في 160 ملفاً — **ولا يُختلق له أب**.

    python3 scripts/fix_placeholder_crumbs.py           # فحص
    python3 scripts/fix_placeholder_crumbs.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
PARENT_TYPES = ("مدرسة", "تيار", "تقنية/تدخل علاجي", "تقنية", "اضطراب")
PLACEHOLDER = re.compile(r'^crumb:\s*"الأطلس\s*←\s*thinkers\s*←', re.M)

index = {}
for f in glob.glob(os.path.join('content', 'ar', '*', '*.md')):
    if '_merged' in f or 'drafts' in f:
        continue
    raw = open(f, encoding='utf-8').read()
    s = re.search(r'^slug:\s*"(.*?)"', raw, re.M)
    t = re.search(r'^title:\s*"(.*?)"', raw, re.M)
    if s:
        index[s.group(1)] = t.group(1) if t else ''

n_parent = n_flat = 0
for f in sorted(glob.glob(os.path.join('content', 'ar', 'thinkers', '*.md'))):
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    if not PLACEHOLDER.search(fm):
        continue
    title = (re.search(r'^title:\s*"(.*?)"', fm, re.M) or [None, ''])[1]

    parent = None
    m = re.search(r'-\s*rel:\s*"belongs_to",\s*target:\s*"([^"]+)"', fm)
    if m and m.group(1) in index:
        parent = m.group(1)
    if not parent:
        for rid, _rt, rty in re.findall(
                r'-\s*id:\s*"([^"]*)",\s*title:\s*"([^"]*)",\s*type:\s*"([^"]*)"', fm):
            if rty in PARENT_TYPES and rid in index:
                parent = rid
                break

    if parent:
        crumb = f'{index[parent]} ← الناس ← {title}'
        n_parent += 1
    else:
        crumb = f'الناس ← {title}'
        n_flat += 1

    nfm = re.sub(r'^crumb:\s*".*"$', f'crumb: "{crumb}"', fm, count=1, flags=re.M)
    print(f"  {os.path.basename(f)[:-3]:<30} {crumb[:70]}")
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + body)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {n_parent + n_flat} ملفاً")
print(f"  بُني على أبٍ مصرَّح : {n_parent}")
print(f"  مسارٌ ثنائي بلا أب : {n_flat}")
