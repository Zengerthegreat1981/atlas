# -*- coding: utf-8 -*-
"""إصلاح ملفات كُتبت بتشكيل كامل مع ماركداون مكسور.

المشكلة: دفعة من الملفات وردت بتشكيل حرفي كامل («مُعَالِج نَفْسِيّ بْرِيطَانِيّ»)،
وبعلامات تشديد ماركداون متداخلة ومكسورة (`لِـ**«**تَحْوِيل**»`)، وبترجمة إنجليزية
حرفية بعد كل اسم («**تَحْرِير**» (Liberation)) — فصارت غير مقروءة.

هذا السكريبت:
  1. ينزع التشكيل من الجسم (يُبقيه في العناوين/الأسماء داخل frontmatter).
  2. يفكّ تداخل علامات ** المكسورة ويوازنها.
  3. يزيل الترجمة الحرفية الزائدة بعد المصطلحات العربية العادية،
     ويُبقي الأقواس التي تحمل مصطلحاً تقنياً حقيقياً.
  4. يفصل البنود المرقّمة المحشورة في بند واحد إلى بنود مستقلّة.

    python3 scripts/fix_vocalized_thinkers.py           # فحص
    python3 scripts/fix_vocalized_thinkers.py --apply   # تنفيذ
"""
import glob, os, re, sys

APPLY = "--apply" in sys.argv
DIA = re.compile(r'[ً-ْٰـ]')   # الحركات والتنوين والسكون والشدّة والتطويل
AR  = re.compile(r'[ء-غف-ي]')

def density(body):
    a = len(AR.findall(body))
    return (len(DIA.findall(body)) / a) if a else 0

def fix(body):
    t = DIA.sub('', body)
    # ** ملتصقة بعلامات التنصيص العربية: **«**كلمة**»  ->  «كلمة»
    t = re.sub(r'\*\*«\*\*(.+?)\*\*»\*?\*?', r'«\1»', t)
    t = re.sub(r'«\*\*(.+?)\*\*»', r'«\1»', t)
    t = re.sub(r'\*\*«(.+?)»\*\*', r'«\1»', t)
    # ** معلّقة بعد ـ أو حرف جرّ:  لِـ**«كلمة»  ->  لـ«كلمة»
    t = re.sub(r'كَـ?\*\*', 'كـ', t)
    t = re.sub(r'لِـ?\*\*', 'لـ', t)
    t = re.sub(r'(?<=\S)ـ\*\*', 'ـ', t)
    # ترجمة حرفية زائدة: «مشاكل» (Problems) -> «مشاكل»
    t = re.sub(r'(«[^»]{1,28}»)\s*\((?:[A-Z][A-Za-z\-]*)(?:\s+[A-Za-z\-]+){0,3}\)', r'\1', t)
    # بنود مرقّمة محشورة داخل بند واحد: ". (2) **x**" -> سطر جديد
    t = re.sub(r'\.\s*\((\d)\)\s*', lambda m: '.\n- ', t)
    # ** غير متوازنة في السطر: أزلها كلها من ذلك السطر
    out = []
    for line in t.split('\n'):
        if line.count('**') % 2:
            line = line.replace('**', '')
        out.append(line)
    t = '\n'.join(out)
    t = re.sub(r'[ \t]{2,}', ' ', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t

n = 0
for f in sorted(glob.glob(os.path.join('content', 'ar', 'thinkers', '*.md'))):
    raw = open(f, encoding='utf-8').read()
    if not raw.startswith('---'): continue
    pre, fm, body = raw.split('---', 2)
    if density(body) <= 0.08: continue
    nb = fix(body)
    if nb == body: continue
    n += 1
    print(f"  {os.path.basename(f)[:-3]:<34} {density(body):.0%} -> {density(nb):.0%}")
    if APPLY:
        open(f, 'w', encoding='utf-8').write(pre + '---' + fm + '---' + nb)
print(f"{'APPLIED' if APPLY else 'DRY RUN'} — {n} ملفاً")
