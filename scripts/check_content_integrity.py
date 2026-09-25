# -*- coding: utf-8 -*-
"""فحوصُ سلامةٍ تُشغَّل بعد كل دفعة تحرير على `content/ar` و`content/en`.

خمسةُ فحوص، كلُّها كشفت أخطاءً واقعة في هذا المستودع فعلاً:

1. **انزياحُ `id`**: أن يُعاد كتابة ملفٍ بمعرِّفٍ مختلف عمّا في HEAD. وقع هذا
   في 14 ملفاً في جلسة 2026-09-07 لأن الكاتب أثبت المعرِّف من تقديره لا من
   الملف. المعرِّفُ مرجعٌ ثابت ولا يُغيَّر مع المتن.
2. **تكرارُ `id`** بين ملفين، داخل شجرة الشجرة الواحدة (ar أو en).
3. **إحالاتٌ معلَّقة** في `related.id` و`edges.target` بصيغة slug. شجرةُ
   `content/en` مرآةٌ جزئيةٌ لِـ`content/ar`؛ فإحالةُ ملفٍ en إلى slug غيرِ
   موجودٍ في en لكنه موجودٌ في ar تُصنَّف تحذيراً لا خطأً.
4. **`slug` لا يطابق اسم الملف**.
5. **بنودٌ يُهملها البناء بصمت**: ترتيبُ حقول `related`/`edges` المخالف لِما
   يقرأه `build_atlas.py`.

    python3 scripts/check_content_integrity.py                 # كل الملفات (ar وen)
    python3 scripts/check_content_integrity.py <ملفات...>       # ملفاتٌ بعينها
    python3 scripts/check_content_integrity.py --lang ar        # شجرة ar فقط
    python3 scripts/check_content_integrity.py --lang en        # شجرة en فقط
    python3 scripts/check_content_integrity.py --lang all       # كلتا الشجرتين (الافتراضي)
"""
import os, re, sys, glob, argparse, subprocess, collections

SKIP = ('_merged', 'drafts')
SLUGISH = re.compile(r'^(thk|con|sch|tec|wrk|dis|dbt|evt|met|que|trm|rel|exp|stu|ctx|ins|crt|axm|dia|br|syn|eth)-')
OK_REL = re.compile(r'-\s*id:\s*"[^"]*"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"[^"]*"')
OK_EDG = re.compile(r'-\s*rel:\s*"[^"]*"\s*,\s*target:\s*"[^"]*"\s*,\s*target_type:\s*"[^"]*"')

LANG_NAME = {'ar': 'ar', 'en': 'en'}


def build_index(base):
    """يبني فهرس slug->ملف وقاموس id->[ملفات] لشجرة لغةٍ بعينها."""
    all_files = [f for f in glob.glob(os.path.join(base, '*', '*.md'))
                 if not any(s in f for s in SKIP)]
    index, ids = {}, collections.defaultdict(list)
    for f in all_files:
        raw = open(f, encoding='utf-8').read()
        s = re.search(r'^slug:\s*"(.*?)"', raw, re.M)
        i = re.search(r'^id:\s*"(.*?)"', raw, re.M)
        if s:
            index[s.group(1)] = f
        if i:
            ids[i.group(1)].append(f)
    return all_files, index, ids


def check_lang(lang, targets_arg):
    """يُشغِّل الفحوصَ الخمسة على شجرة لغةٍ واحدة، ويعيد (problems, warnings, n_checked, n_all)."""
    base = os.path.join('content', lang)
    other_lang = 'ar' if lang == 'en' else 'en'
    other_base = os.path.join('content', other_lang)

    all_files, index, ids = build_index(base)
    # فهرسُ الشجرة الأخرى يُستخدَم فقط في en لتمييز التحذير عن الخطأ
    _, other_index, _ = build_index(other_base) if os.path.isdir(other_base) else ([], {}, {})

    targets = [a for a in targets_arg
               if a.endswith('.md') and a.startswith(base + os.sep) and not any(s in a for s in SKIP)]
    if not targets_arg:
        targets = all_files

    problems = []
    warnings = []

    for i, fs in ids.items():
        if len(fs) > 1:
            problems.append(f"[{lang}] تكرار id {i}: " + ", ".join(os.path.basename(x) for x in fs))

    for f in targets:
        raw = open(f, encoding='utf-8').read()
        base_name = os.path.basename(f)[:-3]
        fm = raw.split('---')[1] if raw.startswith('---') else ''

        s = re.search(r'^slug:\s*"(.*?)"', fm, re.M)
        if s and s.group(1) != base_name:
            problems.append(f"[{lang}] {base_name}: slug «{s.group(1)}» لا يطابق اسم الملف")

        # انزياح id عن HEAD
        head = subprocess.run(['git', 'cat-file', '-p', f'HEAD:{f}'],
                              capture_output=True, text=True)
        if head.returncode == 0:
            mo = re.search(r'^id:\s*"(.*?)"', head.stdout, re.M)
            mn = re.search(r'^id:\s*"(.*?)"', fm, re.M)
            if mo and mn and mo.group(1) != mn.group(1):
                problems.append(
                    f"[{lang}] {base_name}: انزياح id — في HEAD «{mo.group(1)}» وفي الملف «{mn.group(1)}». "
                    f"أعِده إلى قيمة HEAD.")

        for rid in re.findall(r'-\s*id:\s*"([^"]+)"', fm):
            if rid not in index:
                if lang == 'en' and rid in other_index:
                    warnings.append(f"[{lang}] {base_name}: related غيرُ موجودٍ في en لكنه موجودٌ في ar -> {rid}")
                else:
                    problems.append(f"[{lang}] {base_name}: related معلَّق -> {rid}")
        for tgt in re.findall(r'target:\s*"([^"]+)"', fm):
            if SLUGISH.match(tgt) and tgt not in index:
                if lang == 'en' and tgt in other_index:
                    warnings.append(f"[{lang}] {base_name}: edge غيرُ موجودٍ في en لكنه موجودٌ في ar -> {tgt}")
                else:
                    problems.append(f"[{lang}] {base_name}: edge معلَّق -> {tgt}")

        for line in fm.split('\n'):
            st = line.strip()
            if st.startswith('- id:') and not OK_REL.search(line):
                problems.append(f"[{lang}] {base_name}: بند related بترتيبٍ يُهمله البناء: {st[:70]}")
            if st.startswith('- rel:') and not OK_EDG.search(line):
                problems.append(f"[{lang}] {base_name}: بند edges بترتيبٍ يُهمله البناء: {st[:70]}")

    return problems, warnings, len(targets), len(all_files)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--lang', choices=['ar', 'en', 'all'], default='all')
    args, rest = parser.parse_known_args()
    targets_arg = rest

    langs = ['ar', 'en'] if args.lang == 'all' else [args.lang]
    # إن كانت الملفاتُ المُمرَّرةُ صراحةً كلُّها من شجرةٍ واحدة، فلا داعيَ لفحص
    # الشجرة الأخرى بلا أهداف (تبقى فحوصُ التكرار العامة قائمة).
    if targets_arg:
        present = set()
        for a in targets_arg:
            if a.startswith('content' + os.sep + 'ar' + os.sep):
                present.add('ar')
            elif a.startswith('content' + os.sep + 'en' + os.sep):
                present.add('en')
        if present:
            langs = [l for l in langs if l in present]

    all_problems, all_warnings = [], []
    total_checked, total_all = 0, 0
    for lang in langs:
        if not os.path.isdir(os.path.join('content', lang)):
            continue
        problems, warnings, n_checked, n_all = check_lang(lang, targets_arg)
        all_problems += problems
        all_warnings += warnings
        total_checked += n_checked
        total_all += n_all

    print(f"فُحص {total_checked} ملفاً من {total_all}.")
    if all_warnings:
        print(f"⚠️  {len(all_warnings)} تحذيراً:")
        for w in all_warnings:
            print("   " + w)
    if not all_problems:
        print("✅ سليم — لا مشكلات.")
        sys.exit(0)
    print(f"❌ {len(all_problems)} مشكلة:")
    for p in all_problems:
        print("   " + p)
    sys.exit(1)


if __name__ == '__main__':
    main()
