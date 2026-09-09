# -*- coding: utf-8 -*-
"""تحويل صيغة `[[slug]]` الغريبة على الأطلس إلى اصطلاحه الفعلي.

ثمانية ملفات في `techniques/` (دفعة واحدة: tec-t*/tec-v*) كُتبت بصيغة ويكي
`[[slug]]` و`[[slug|تسمية]]`. الأطلس لا يفسّر هذه الصيغة في أي مكان — لا
`build_atlas.py` ولا `app.js` — فتُطبع حرفياً للمستخدم (`[[thk-rothbaum]]`).
اصطلاح الأطلس: **اسم صريح في المتن + الـslug في حقل `related`**.

هذا السكريبت:
  1. يستبدل `[[slug|تسمية]]` بالتسمية، و`[[slug]]` بعنوان الملف من الفهرس.
  2. يضيف الـslug إلى `related` إن لم يكن موجوداً — فلا تُفقد صلة من الرسم.
     (تُستثنى الملفات المحجورة: لا يُربط الأطلس بإحالة حجْر.)
  3. يتوقّف بخطأ إن لم يُحلّ slug واحد — فلا يُطبَق تحويل ناقص.

    python3 scripts/convert_wikilinks_to_atlas_convention.py           # فحص
    python3 scripts/convert_wikilinks_to_atlas_convention.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
W = re.compile(r'\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]')


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
targets = sorted(f for f in glob.glob(os.path.join('content', 'ar', '*', '*.md'))
                 if '_merged' not in f and 'drafts' not in f
                 and '[[' in open(f, encoding='utf-8').read())

missing = {s for f in targets for s, _ in W.findall(open(f, encoding='utf-8').read())
           if s not in idx}
if missing:
    raise SystemExit("slugs غير موجودة، لا يُطبَّق شيء: " + ", ".join(sorted(missing)))

n = 0
for f in targets:
    raw = open(f, encoding='utf-8').read()
    pre, fm, body = raw.split('---', 2)
    refs = []

    def repl(m):
        slug, label = m.group(1), m.group(2)
        refs.append(slug)
        return label if label else idx[slug][0]

    nbody = W.sub(repl, body)

    # أضف كل slug مُحال إليه إلى related إن غاب (ما لم يكن محجوراً)
    have = set(re.findall(r'-\s*id:\s*"([^"]+)"', fm))
    add = [s for s in dict.fromkeys(refs)
           if s not in have and 'حجر' not in idx[s][0]]
    nfm = fm
    if add:
        lines = "".join(f'- id: "{s}", title: "{idx[s][0]}", type: "{idx[s][1]}"\n'
                        for s in add)
        if re.search(r'^related:\s*$', nfm, re.M):
            nfm = re.sub(r'^related:\s*\n', 'related:\n' + lines, nfm, count=1, flags=re.M)
        else:
            nfm = re.sub(r'^(gaps:)', lines.rstrip('\n') + r'\n\1', nfm, count=1, flags=re.M) \
                if re.search(r'^gaps:', nfm, re.M) else nfm.rstrip('\n') + '\nrelated:\n' + lines

    if (nfm, nbody) == (fm, body):
        continue
    n += 1
    print(f"  {os.path.basename(f)[:-3]:<34} روابط: {len(refs)}  أُضيف لـrelated: {len(add)}")
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + nbody)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {n} ملفاً")
