# -*- coding: utf-8 -*-
"""إصلاح عرضِ الهوية في المدخلات غير المتحقَّق منها، وحذفِ الأقسام الفارغة.

علّتان في ملفاتٍ أقرّت هي نفسُها في `gaps` بأن هويّةَ صاحبها غيرُ محقَّقة:

1. **اسمُ شخصٍ حقيقي معروضاً على مدخلٍ لا يخصّه.** أظهرُ مثالٍ `thk-jroddy`:
   حقلُ `en` فيه «J. Luke Wood»، وهو **أستاذُ تربيةٍ أمريكي موثَّق حقيقي**
   لا صلةَ له بـTEACCH ولا بعلم نفس التوحّد — كما تقرّ فجوةُ الملف نفسها.
   فالأطلسُ يعرض اسمَ شخصٍ حيّ مقروناً بمجالٍ لا يعمل فيه وبانتماءٍ لم يُثبت.
   وهذا **مسٌّ بشخصٍ حقيقي** لا نقصٌ في التوثيق. العلاجُ: أن يُنقل الاسمُ
   إلى `gaps` بوصفه اسماً وارداً في المدخل يحتاج حسماً، وأن يُعرَض العنوانُ
   بعلامةِ «هويّة غير محقَّقة» — فلا يبقى الاسمُ في موضع الإخبار.
   (والـslug باقٍ كما هو عملاً بقاعدة عدم إعادة التسمية.)

2. **أقسامٌ فارغة** عنوانُها قائم ومحتواها بديلٌ نائب — `[لم يُراجع]` أو
   `[بيانات غير متاحة]`. وعنوانٌ فارغٌ أسوأُ من غيابه: يُوهم المستخدمَ أن
   ثمّة مضموناً حُجب. العلاجُ: يُحذَف القسمُ ويُسجَّل في `gaps`.

    python3 scripts/fix_unverified_identity_display.py           # فحص
    python3 scripts/fix_unverified_identity_display.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
TH = os.path.join('content', 'ar', 'thinkers')

# ملفاتٌ يحمل حقلُ `en` فيها اسمَ شخصٍ حقيقي لا صلةَ له بالمدخل،
# بحسب ما تقرّ به فجواتُ الملفات نفسها.
MISATTRIBUTED = {
    'thk-jroddy': ('J. Luke Wood',
                   'أستاذُ تربيةٍ أمريكي موثَّق (عُرف بأبحاث الطلاب السود في '
                   'الكليات المجتمعية وبمصطلح Racelighting) **لا صلةَ موثَّقة له '
                   'بـTEACCH ولا بعلم نفس التوحّد**'),
    'thk-cwhitaker-pt': ('John Marsh',
                         'اسمٌ لا يطابق الـslug ولا يُوثَّق في سياق TEACCH'),
    'thk-jjoyce': ('Margaret P. Be',
                   'اسمٌ ناقصٌ لا يطابق الـslug ولا يُوثَّق في سياق المدخل'),
}

EMPTY_MARK = re.compile(r'^\s*-?\s*\[(?:لم يُراجع|لم تُراجع|بيانات غير متاحة[^\]]*|غير متاح)\]\s*$')

nid = nsec = nfiles = 0
for f in sorted(glob.glob(os.path.join(TH, '*.md'))):
    slug = os.path.basename(f)[:-3]
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    nfm, nbody, changed = fm, body, False

    # 1. اسمٌ منسوبٌ خطأً
    if slug in MISATTRIBUTED:
        name, why = MISATTRIBUTED[slug]
        if re.search(rf'^en:\s*"{re.escape(name)}"', nfm, re.M):
            nfm = re.sub(rf'^en:\s*"{re.escape(name)}"',
                         'en: "Unverified identity — see gaps"', nfm, flags=re.M)
            nfm = re.sub(r'^title:\s*"(.*?)"',
                         r'title: "[هويّة غير محقَّقة] \1"', nfm, count=1, flags=re.M)
            note = (f'  - "**أُزيل الاسمُ من موضع الإخبار 2026-09-07:** كان حقلُ `en` '
                    f'يحمل «{name}» — وهو {why}. فعرضُ الاسم في ترويسة المدخل '
                    f'يقرن شخصاً بمجالٍ وانتماءٍ لم يُثبتا له، وهذا مسٌّ به لا نقصٌ '
                    f'في التوثيق. نُقل الاسمُ إلى هذه الملاحظة، وصار العنوانُ يحمل '
                    f'علامةَ «هويّة غير محقَّقة». **والـslug باقٍ** عملاً بقاعدة عدم '
                    f'إعادة التسمية."')
            if re.search(r'^gaps:\s*$', nfm, re.M):
                nfm = re.sub(r'^gaps:\s*\n', 'gaps:\n' + note + '\n', nfm, count=1, flags=re.M)
            else:
                nfm = nfm.rstrip('\n') + '\ngaps:\n' + note + '\n'
            nid += 1
            changed = True

    # 2. أقسامٌ محتواها بديلٌ نائب فقط
    lines = nbody.split('\n')
    out, i, removed = [], 0, []
    while i < len(lines):
        if lines[i].startswith('## '):
            j = i + 1
            block = []
            while j < len(lines) and not lines[j].startswith('## '):
                block.append(lines[j])
                j += 1
            meat = [b for b in block if b.strip()]
            if meat and all(EMPTY_MARK.match(b) for b in meat):
                removed.append(lines[i][3:].strip())
                i = j
                continue
        out.append(lines[i])
        i += 1
    if removed:
        nbody = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
        note = ('  - "**حُذفت أقسامٌ فارغة 2026-09-07:** كان في الملف '
                + '، '.join(f'«{r}»' for r in removed)
                + ' بعنوانٍ قائم ومحتواه بديلٌ نائب (`[لم يُراجع]` أو '
                '`[بيانات غير متاحة]`). والعنوانُ الفارغ يُوهم المستخدمَ أن ثمّة '
                'مضموناً حُجب، فحُذف — ويبقى النقصُ مسجَّلاً هنا."')
        if re.search(r'^gaps:\s*$', nfm, re.M):
            nfm = re.sub(r'^gaps:\s*\n', 'gaps:\n' + note + '\n', nfm, count=1, flags=re.M)
        else:
            nfm = nfm.rstrip('\n') + '\ngaps:\n' + note + '\n'
        nsec += len(removed)
        changed = True

    if not changed:
        continue
    nfiles += 1
    print(f"  {slug}: " + (" هويّة" if slug in MISATTRIBUTED else "") +
          (f" أقسام فارغة: {len(removed)}" if removed else ""))
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + nbody)

print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {nfiles} ملفاً")
print(f"  أسماء أُزيلت من موضع الإخبار: {nid}")
print(f"  أقسام فارغة حُذفت           : {nsec}")
