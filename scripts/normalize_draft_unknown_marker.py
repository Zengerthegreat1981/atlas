# -*- coding: utf-8 -*-
"""توحيد علامة النقص `[DRAFT-UNKNOWN]` على اصطلاح الأطلس `[غير مؤكد]`.

`[DRAFT-UNKNOWN]` رمز أنبوب توليد إنجليزي بقي في **141 ملفاً معتمداً** ويُطبع
حرفياً في ترويسة المدخل على موقع عربي (`الولايات المتحدة · [DRAFT-UNKNOWN]`).
الأطلس له علامته العربية المعتمدة لنفس المعنى بالضبط — `[غير مؤكد]` — وهي
مستعملة في 365 ملفاً. فالمطلوب توحيد، لا إخفاء: تبقى العلامة **ظاهرة** بوصفها
إقراراً بالنقص، ولا تُبدَّل بقيمة مُختلقة.

  - `dates` / `country` / `language`: تُصبح `[غير مؤكد]`.
  - `active_start` / `active_end`: تُصبح `null` — وهو اصطلاح الأطلس للمجهول
    في هذين الحقلين (1101 و41 ملفاً) لأنهما رقميان في البناء، ونصٌّ فيهما
    يُقرأ قيمةً لا علامة.
  - ملاحظات `gaps` التي **تسمّي الرمز نصّاً** تُحدَّث لتسمّي العلامة الجديدة،
    فلا تصير الملاحظة إحالة إلى رمز لم يبقَ في الملف.

    python3 scripts/normalize_draft_unknown_marker.py           # فحص
    python3 scripts/normalize_draft_unknown_marker.py --apply   # تنفيذ
"""
import os, re, sys, glob

APPLY = "--apply" in sys.argv
MARK = "[غير مؤكد]"
TOK = "[DRAFT-UNKNOWN]"
NULL_FIELDS = ("active_start", "active_end")
TEXT_FIELDS = ("dates", "country", "language", "id", "en", "title", "crumb")

stats = dict(files=0, nulled=0, marked=0, notes=0)
for f in sorted(glob.glob(os.path.join('content', 'ar', '*', '*.md'))):
    if '_merged' in f or 'drafts' in f:
        continue
    raw = open(f, encoding='utf-8').read()
    if TOK not in raw or not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    out = []
    for line in fm.split('\n'):
        if TOK not in line:
            out.append(line)
            continue
        m = re.match(r'^([a-zA-Z0-9_-]+):\s*"(.*)"\s*$', line.strip())
        if m and m.group(1) in NULL_FIELDS:
            out.append(f'{m.group(1)}: null')
            stats['nulled'] += 1
            continue
        if m and m.group(1) in TEXT_FIELDS:
            out.append(f'{m.group(1)}: "{m.group(2).replace(TOK, MARK)}"')
            stats['marked'] += 1
            continue
        # بند gaps أو أي سطر آخر يسمّي الرمز: يُحدَّث اسم العلامة فقط
        if TOK in line:
            stats['notes'] += 1
        out.append(line.replace(TOK, MARK).replace('DRAFT-UNKNOWN', 'غير مؤكد'))
    nfm = '\n'.join(out)
    nbody = body.replace(TOK, MARK).replace('DRAFT-UNKNOWN', 'غير مؤكد')
    if (nfm, nbody) == (fm, body):
        continue
    stats['files'] += 1
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + nfm + '---' + nbody)

print(f"{'APPLIED' if APPLY else 'DRY RUN'} — {stats['files']} ملفاً")
print(f"  حقول نصّية صارت [غير مؤكد]      : {stats['marked']}")
print(f"  active_start/end صارت null      : {stats['nulled']}")
print(f"  ملاحظات gaps حُدِّث فيها اسم العلامة: {stats['notes']}")
