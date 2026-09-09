# -*- coding: utf-8 -*-
"""توحيد ترتيب حقول بنود `related` و`edges` إلى الترتيب الذي يقرأه البناء.

`build_atlas.py` يقرأ البنود بتعبير ثابت الترتيب:
    RELATED_ITEM_RE : - id: "…", title: "…", type: "…"
    EDGE_ITEM_RE    : - rel: "…", target: "…", target_type: "…"
كل بند بترتيب مخالف (`id, type, title`) أو باسم حقل مخالف (`type` بدل
`target_type` في الأضلاع) **لا يُطابَق فيُهمَل بصمت**: البند مكتوب في الملف،
ولا وجود له في `data.json` ولا على الموقع. لا يظهر هذا في أي فحص للروابط
المكسورة لأن الرابط ليس مكسوراً — هو غير موجود أصلاً.

هذا السكريبت يعيد كتابة البند بالترتيب المتوقَّع، بالقيم نفسها حرفياً.

    python3 scripts/normalize_frontmatter_field_order.py           # فحص
    python3 scripts/normalize_frontmatter_field_order.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
OK_REL = re.compile(r'-\s*id:\s*"[^"]*"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"[^"]*"')
OK_EDG = re.compile(r'-\s*rel:\s*"[^"]*"\s*,\s*target:\s*"[^"]*"\s*,\s*target_type:\s*"[^"]*"')
FIELD = re.compile(r'(\w+):\s*"([^"]*)"')

nrel = nedg = nfiles = 0
skipped = []

for f in sorted(glob.glob(os.path.join('content', 'ar', '*', '*.md'))):
    if '_merged' in f or 'drafts' in f:
        continue
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    out = []
    changed = False
    for line in fm.split('\n'):
        s = line.strip()
        if s.startswith('- id:') and not OK_REL.search(line):
            d = dict(FIELD.findall(s))
            if {'id', 'title', 'type'} <= set(d):
                line = f'- id: "{d["id"]}", title: "{d["title"]}", type: "{d["type"]}"'
                nrel += 1
                changed = True
            else:
                skipped.append((f, s))
        elif s.startswith('- rel:') and not OK_EDG.search(line):
            d = dict(FIELD.findall(s))
            tt = d.get('target_type') or d.get('type')
            if 'rel' in d and 'target' in d and tt:
                line = f'- rel: "{d["rel"]}", target: "{d["target"]}", target_type: "{tt}"'
                nedg += 1
                changed = True
            else:
                skipped.append((f, s))
        out.append(line)
    if not changed:
        continue
    nfiles += 1
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + '\n'.join(out) + '---' + body)

print(f"{'APPLIED' if APPLY else 'DRY RUN'} — {nfiles} ملفاً")
print(f"  بنود related أُعيد ترتيبها: {nrel}")
print(f"  بنود edges أُعيد ترتيبها  : {nedg}")
if skipped:
    print(f"  بنود بلا حقول كافية (تُترك للمراجعة اليدوية): {len(skipped)}")
    for f, s in skipped[:10]:
        print(f"     {os.path.basename(f)}: {s[:90]}")
