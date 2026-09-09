# -*- coding: utf-8 -*-
"""إزالة بنود `related` المحقونة بلا مسوّغ في المتن، وتوحيد المكرّر منها.

علّتان لُوحظتا في دفعةٍ من ملفات `branches/`:

1. **حقنُ slug واحدٍ في ملفاتٍ لا صلةَ لها به.** كان `br-ml-personalized-therapy`
   (العلاجُ المشخَّص بالتعلّم الآلي) مُدرجاً في `related` في 32 ملفاً، منها
   `br-curanderismo` (الطبُّ الشعبي المكسيكي) و`br-alchemical-psychology`
   (علمُ النفس الألكيميائي) و`br-bodynamic-analysis` — ولا يذكر متنُ أيٍّ منها
   التعلّمَ الآلي ولا ما يتّصل به. أي أن الرابطَ ليس خطأً في التوجيه بل **بندٌ
   مُقحَم**: يُنتج في الواجهة صلةً بين موضوعين لا صلةَ بينهما.
   تُستثنى الملفاتُ التي يسوّغ متنُها الصلةَ فعلاً (الرقمية والحاسوبية).

2. **تكرارُ البند نفسه** في الملف الواحد مرّتين أو ثلاثاً، فيُعرَض للمستخدم
   مكرّراً.

    python3 scripts/remove_spurious_related_links.py           # فحص
    python3 scripts/remove_spurious_related_links.py --apply   # تنفيذ
"""
import os, re, sys, glob, collections

APPLY = "--apply" in sys.argv

# slug مُقحَم -> الملفاتُ التي يسوّغ متنُها الصلةَ فعلاً فتُستثنى من التنظيف
INJECTED = {
    'br-ml-personalized-therapy': {
        'br-digital-therapeutics', 'br-teletherapy', 'br-serious-games-therapy',
        'br-predictive-processing-informed', 'br-medical-model-addiction',
    },
}
REL_LINE = re.compile(r'^-\s*id:\s*"([^"]+)".*$', re.M)

removed = dedup = nfiles = 0
for f in sorted(glob.glob(os.path.join('content', 'ar', '*', '*.md'))):
    if '_merged' in f or 'drafts' in f:
        continue
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    slug = (re.search(r'^slug:\s*"(.*?)"', fm, re.M) or [None, ''])[1]
    out, seen, changed = [], set(), False

    for line in fm.split('\n'):
        m = REL_LINE.match(line.strip())
        if not m:
            out.append(line)
            continue
        rid = m.group(1)
        # 1. بند مُقحَم
        if rid in INJECTED and slug != rid and slug not in INJECTED[rid]:
            removed += 1
            changed = True
            print(f"  حُذف مُقحَم: {slug} -/-> {rid}")
            continue
        # 2. تكرار
        if rid in seen:
            dedup += 1
            changed = True
            print(f"  حُذف مكرَّر: {slug} -> {rid}")
            continue
        seen.add(rid)
        out.append(line)

    if not changed:
        continue
    nfiles += 1
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + '\n'.join(out) + '---' + body)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {nfiles} ملفاً")
print(f"  بنود مُقحَمة حُذفت : {removed}")
print(f"  بنود مكرَّرة حُذفت: {dedup}")
