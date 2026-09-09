# -*- coding: utf-8 -*-
"""فحوصُ سلامةٍ تُشغَّل بعد كل دفعة تحرير على `content/ar`.

خمسةُ فحوص، كلُّها كشفت أخطاءً واقعة في هذا المستودع فعلاً:

1. **انزياحُ `id`**: أن يُعاد كتابة ملفٍ بمعرِّفٍ مختلف عمّا في HEAD. وقع هذا
   في 14 ملفاً في جلسة 2026-09-07 لأن الكاتب أثبت المعرِّف من تقديره لا من
   الملف. المعرِّفُ مرجعٌ ثابت ولا يُغيَّر مع المتن.
2. **تكرارُ `id`** بين ملفين.
3. **إحالاتٌ معلَّقة** في `related.id` و`edges.target` بصيغة slug.
4. **`slug` لا يطابق اسم الملف**.
5. **بنودٌ يُهملها البناء بصمت**: ترتيبُ حقول `related`/`edges` المخالف لِما
   يقرأه `build_atlas.py`.

    python3 scripts/check_content_integrity.py            # كل الملفات
    python3 scripts/check_content_integrity.py <ملفات...>  # ملفاتٌ بعينها
"""
import os, re, sys, glob, subprocess, collections

BASE = os.path.join('content', 'ar')
SKIP = ('_merged', 'drafts')
SLUGISH = re.compile(r'^(thk|con|sch|tec|wrk|dis|dbt|evt|met|que|trm|rel|exp|stu|ctx|ins|crt|axm|dia|br|syn|eth)-')
OK_REL = re.compile(r'-\s*id:\s*"[^"]*"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"[^"]*"')
OK_EDG = re.compile(r'-\s*rel:\s*"[^"]*"\s*,\s*target:\s*"[^"]*"\s*,\s*target_type:\s*"[^"]*"')

all_files = [f for f in glob.glob(os.path.join(BASE, '*', '*.md'))
             if not any(s in f for s in SKIP)]
targets = [a for a in sys.argv[1:] if a.endswith('.md')] or all_files

index, ids = {}, collections.defaultdict(list)
for f in all_files:
    raw = open(f, encoding='utf-8').read()
    s = re.search(r'^slug:\s*"(.*?)"', raw, re.M)
    i = re.search(r'^id:\s*"(.*?)"', raw, re.M)
    if s:
        index[s.group(1)] = f
    if i:
        ids[i.group(1)].append(f)

problems = []

for i, fs in ids.items():
    if len(fs) > 1:
        problems.append(f"تكرار id {i}: " + ", ".join(os.path.basename(x) for x in fs))

for f in targets:
    raw = open(f, encoding='utf-8').read()
    base = os.path.basename(f)[:-3]
    fm = raw.split('---')[1] if raw.startswith('---') else ''

    s = re.search(r'^slug:\s*"(.*?)"', fm, re.M)
    if s and s.group(1) != base:
        problems.append(f"{base}: slug «{s.group(1)}» لا يطابق اسم الملف")

    # انزياح id عن HEAD
    head = subprocess.run(['git', 'cat-file', '-p', f'HEAD:{f}'],
                          capture_output=True, text=True)
    if head.returncode == 0:
        mo = re.search(r'^id:\s*"(.*?)"', head.stdout, re.M)
        mn = re.search(r'^id:\s*"(.*?)"', fm, re.M)
        if mo and mn and mo.group(1) != mn.group(1):
            problems.append(
                f"{base}: انزياح id — في HEAD «{mo.group(1)}» وفي الملف «{mn.group(1)}». "
                f"أعِده إلى قيمة HEAD.")

    for rid in re.findall(r'-\s*id:\s*"([^"]+)"', fm):
        if rid not in index:
            problems.append(f"{base}: related معلَّق -> {rid}")
    for tgt in re.findall(r'target:\s*"([^"]+)"', fm):
        if SLUGISH.match(tgt) and tgt not in index:
            problems.append(f"{base}: edge معلَّق -> {tgt}")

    for line in fm.split('\n'):
        st = line.strip()
        if st.startswith('- id:') and not OK_REL.search(line):
            problems.append(f"{base}: بند related بترتيبٍ يُهمله البناء: {st[:70]}")
        if st.startswith('- rel:') and not OK_EDG.search(line):
            problems.append(f"{base}: بند edges بترتيبٍ يُهمله البناء: {st[:70]}")

print(f"فُحص {len(targets)} ملفاً من {len(all_files)}.")
if not problems:
    print("✅ سليم — لا مشكلات.")
    sys.exit(0)
print(f"❌ {len(problems)} مشكلة:")
for p in problems:
    print("   " + p)
sys.exit(1)
