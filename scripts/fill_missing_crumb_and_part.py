# -*- coding: utf-8 -*-
"""تعبئة حقلَي `crumb` و`part` الغائبين كلياً.

`crumb` هو مسار التنقّل الذي تعرضه الواجهة؛ غيابه يعني مدخلاً بلا موضع في
الشجرة. الاصطلاح السائد في `thinkers/` (1753 من 2255 ملفاً) ثلاثي:
    "<عنوان الأب> ← الناس ← <عنوان الملف>"
والأب يُستخرج — بهذا الترتيب:
  1. هدف ضلع `belongs_to` (وهو التصريح المباشر بالانتماء)،
  2. أول بند في `related` نوعه مدرسة أو تيار أو تقنية،
  3. وإن لم يوجد أيٌّ منهما، يُكتب مسار ثنائي "الناس ← <العنوان>"
     (اصطلاح قائم فعلاً في 160 ملفاً) — ولا يُختلق أب.

`part` يحدّد القسم (philosophy / psychology / sociology). يُستخرج من الأب،
وإن غاب فمن أغلبية إخوة الملف في مجلده حسب المدرسة المذكورة.

    python3 scripts/fill_missing_crumb_and_part.py           # فحص
    python3 scripts/fill_missing_crumb_and_part.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
PARENT_TYPES = ("مدرسة", "تيار", "تقنية/تدخل علاجي", "تقنية")


def load(f):
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        return None
    pre, fm, body = raw.split('---', 2)
    return pre, fm, body


idx = {}
for f in glob.glob(os.path.join('content', 'ar', '*', '*.md')):
    if '_merged' in f or 'drafts' in f:
        continue
    L = load(f)
    if not L:
        continue
    fm = L[1]
    s = re.search(r'^slug:\s*"(.*?)"', fm, re.M)
    if s:
        idx[s.group(1)] = {
            'title': (re.search(r'^title:\s*"(.*?)"', fm, re.M) or [None, ''])[1],
            'part': (re.search(r'^part:\s*"(.*?)"', fm, re.M) or [None, ''])[1],
            'crumb': (re.search(r'^crumb:\s*"(.*?)"', fm, re.M) or [None, ''])[1],
            'peers': [r for r in re.findall(r'-\s*id:\s*"([^"]*)"', fm)],
            'path': f,
        }

ncrumb = npart = 0
for slug, meta in sorted(idx.items()):
    f = meta['path']
    pre, fm, body = load(f)
    nfm = fm
    title = meta['title']

    has_crumb = re.search(r'^crumb:\s*"', fm, re.M)
    has_part = re.search(r'^part:\s*"', fm, re.M)
    if has_crumb and has_part:
        continue

    # اعرف الأب
    parent = None
    m = re.search(r'-\s*rel:\s*"belongs_to",\s*target:\s*"([^"]+)"', fm)
    if m and m.group(1) in idx:
        parent = m.group(1)
    if not parent:
        for rid, rt, rty in re.findall(
                r'-\s*id:\s*"([^"]*)",\s*title:\s*"([^"]*)",\s*type:\s*"([^"]*)"', fm):
            if rty in PARENT_TYPES and rid in idx:
                parent = rid
                break

    # لا أب مصرَّحاً به: خُذ جذر مسار أقرب زميل — معطى في البيانات، لا مختلق
    root = None
    if not parent:
        for pid in meta['peers']:
            c = idx.get(pid, {}).get('crumb', '')
            if '←' in c:
                cand = c.split('←')[0].strip()
                # «الأطلس» جذر عامّ لا يفيد موضعاً؛ يُتجاوز إلى الزميل التالي
                if cand and cand != 'الأطلس':
                    root = cand
                    break

    if not has_crumb:
        seg = "الناس" if '/thinkers/' in f else "المدخلات"
        if parent:
            crumb = f'{idx[parent]["title"]} ← {seg} ← {title}'
        elif root:
            crumb = f'{root} ← {seg} ← {title}'
        else:
            crumb = f'{seg} ← {title}'
        # يُدرَج بعد en إن وُجد، وإلا بعد title (موضعه في بقية الملفات)
        anchor = r'^(en:\s*".*"\s*)$' if re.search(r'^en:\s*"', nfm, re.M) else r'^(title:\s*".*"\s*)$'
        nfm = re.sub(anchor, r'\1' + f'\ncrumb: "{crumb}"', nfm, count=1, flags=re.M)
        ncrumb += 1

    if not has_part:
        part = idx[parent]['part'] if parent and idx[parent]['part'] else 'psychology'
        nfm = re.sub(r'^(type:\s*".*"\s*)$', r'\1' + f'\npart: "{part}"',
                     nfm, count=1, flags=re.M)
        npart += 1

    if nfm == fm:
        continue
    print(f"  {slug:<26} crumb={'✔' if not has_crumb else '-'} part={'✔' if not has_part else '-'}"
          f"  أب={parent or ('جذر زميل: ' + root if root else '(بلا)')}")
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + body)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — crumb: {ncrumb} · part: {npart}")
