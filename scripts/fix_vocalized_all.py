# -*- coding: utf-8 -*-
"""إصلاح الماركداون المكسور من دفعة التشكيل — على كامل الأطلس، لا `thinkers/` وحده.

يوسّع `fix_vocalized_thinkers.py` (المجرَّب على thinkers/) إلى كل مجلدات
`content/ar` باستثناء `_merged/` و`drafts/`.

فرقان مقصودان عن السكريبت الأصلي:
  1. المعالجة تنطلق أيضاً على ملف بتشكيل خفيف لكن بماركداون مكسور فعلاً
     (`«**` أو `**` غير متوازنة) — الأصل كان يشترط كثافة تشكيل > 8% فيفوت
     38 ملف مفكّر مكسور الماركداون بلا تشكيل كثيف.
  2. نزع التشكيل يقتصر على الملفات كثيفة التشكيل؛ أما الملف الخفيف فيُصلَح
     ماركداونه فقط ولا يُمسّ تشكيله (كي لا نغيّر متناً سليماً).

    python3 scripts/fix_vocalized_all.py           # فحص
    python3 scripts/fix_vocalized_all.py --apply   # تنفيذ
"""
import os, re, sys, collections

APPLY = "--apply" in sys.argv
DIA = re.compile(r'[ً-ْٰـ]')
AR  = re.compile(r'[ء-غف-ي]')
SKIP_DIRS = ('_merged', 'drafts')


def density(body):
    a = len(AR.findall(body))
    return (len(DIA.findall(body)) / a) if a else 0


def broken_markdown(body):
    if '«**' in body or '**»' in body:
        return True
    return any(line.count('**') % 2 for line in body.split('\n'))


def strip_batch_overquoting(t):
    """دفعة التشكيل وضعت «» حول كل مصطلح عادي («انتشار» «بدون» «أخلاق») حتى صار
    السطر كله بين أقواس. تُنزع الأقواس عن الكلمة المفردة **فقط** في السطر الذي
    يحمل ثلاثة اقتباسات مفردة أو أكثر — وهي بصمة تلك الدفعة؛ أما الاقتباس المفرد
    أو المزدوج في سطر فيُحتمل أنه اقتباس مقصود فيُترك."""
    SINGLE = re.compile(r'«([^»«\s]{2,20})»')
    out = []
    for line in t.split('\n'):
        if len(SINGLE.findall(line)) >= 3:
            line = SINGLE.sub(r'\1', line)
        out.append(line)
    return '\n'.join(out)


def tidy_after_unquoting(t):
    """تنظيف ما يظهر بعد نزع الأقواس الزائدة: تطويل معلّق (بـتجريد -> بتجريد)
    وأقواس تنصيص غير متوازنة في سطر واحد (بقايا أسطر مكسورة أصلاً)."""
    t = re.sub(r'(?<![\w\u0621-\u064a])([بلك])ـ(?=[\u0621-\u064a])', r'\1', t)
    out = []
    for line in t.split('\n'):
        if line.count('«') != line.count('»'):
            line = line.replace('«', '').replace('»', '')
        out.append(line)
    return '\n'.join(out)


def fix_markdown(t):
    # ** معلّقة بعد ـ أو حرف جرّ (قبل أي مسّ بعلامات التنصيص):  بـ**«كلمة» -> بـ«كلمة»
    t = re.sub(r'(?<=\S)ـ\*\*', 'ـ', t)
    t = re.sub(r'كَـ?\*\*', 'كـ', t)
    t = re.sub(r'لِـ?\*\*', 'لـ', t)
    # ** ملتصقة بعلامات التنصيص العربية: **«**كلمة**»  ->  «كلمة»
    t = re.sub(r'\*\*«\*\*(.+?)\*\*»\*?\*?', r'«\1»', t)
    t = re.sub(r'«\*\*(.+?)\*\*»', r'«\1»', t)
    t = re.sub(r'\*\*«(.+?)»\*\*', r'«\1»', t)
    # ما تبقّى من «** أو **» بلا نظير
    t = t.replace('«**', '«').replace('**»', '»')
    # حرف جرّ ملتصق بقوس أو بـ** بلا تطويل: ل«تقنية» -> لـ«تقنية» / ب**ستراسبورغ** -> بـ**ستراسبورغ**
    t = re.sub(r'(?<![\w\u0621-\u064a])([بلك])(«|\*\*(?=[\u0621-\u064a]))', r'\1ـ\2', t)
    # بند مرقّم في بداية سطر: "(1) نصّ" -> "- نصّ" (بقيةُ إخوته صارت بنوداً)
    t = re.sub(r'^\((\d)\)\s+', '- ', t, flags=re.M)
    # ترجمة حرفية زائدة: «مشاكل» (Problems) -> «مشاكل»
    t = re.sub(r'(«[^»]{1,28}»)\s*\((?:[A-Z][A-Za-z\'\-]*)(?:\s+[A-Za-z\'\-]+){0,3}\)', r'\1', t)
    # بنود مرقّمة محشورة داخل بند واحد
    t = re.sub(r'\.\s*\((\d)\)\s*', '.\n- ', t)
    # ** فارغة تماماً (**** أو ** **)
    t = t.replace('****', '')
    # ** غير متوازنة في السطر: أزلها من ذلك السطر
    out = []
    for line in t.split('\n'):
        if line.count('**') % 2:
            line = line.replace('**', '')
        out.append(line)
    t = '\n'.join(out)
    t = re.sub(r'[ \t]{2,}', ' ', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t


files = []
for r, d, fs in os.walk(os.path.join('content', 'ar')):
    if any(s in r for s in SKIP_DIRS):
        continue
    files += [os.path.join(r, f) for f in fs if f.endswith('.md')]

n = 0
per_dir = collections.Counter()
for f in sorted(files):
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'):
        continue
    pre, fm, body = raw.split('---', 2)
    dens = density(body)
    heavy = dens > 0.08
    if not heavy and not broken_markdown(body):
        continue
    nb = DIA.sub('', body) if heavy else body
    nb = fix_markdown(nb)
    if heavy:
        nb = strip_batch_overquoting(nb)
        nb = tidy_after_unquoting(nb)
    if nb == body:
        continue
    n += 1
    per_dir[f.split(os.sep)[2]] += 1
    print(f"  {f.split(os.sep, 2)[2]:<52} تشكيل {dens:.0%} -> {density(nb):.0%}")
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + fm + '---' + nb)
print(f"\n{'APPLIED' if APPLY else 'DRY RUN'} — {n} ملفاً")
for k, v in per_dir.most_common():
    print(f"   {k}: {v}")
