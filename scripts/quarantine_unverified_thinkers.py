# -*- coding: utf-8 -*-
"""نقل مداخل المفكرين غير القابلة للتحقق من المجلد المعتمد إلى `drafts/`.

القاعدة رقم 1 في `agents_specs/README.md`: أي محتوى لم يمرّ بمراجعة بشرية صريحة
لا مكان له في `content/ar/<نوع>/`. الملفات المستهدفة تحمل واحدة أو أكثر من:
  • علامة [DRAFT-UNKNOWN] في أي موضع
  • عنوان/H1/سطر تعريف ظاهر للقارئ فيه نص نائب
  • قسم أعمال نائب عن المحتوى بلا عنوان كتاب واحد
  • تعارض هوية بين الـslug وحقل en

الملفات التي جسمها قالب فارغ فقط (مفكّرون حقيقيون بلا محتوى مكتوب) **مستثناة** —
مشكلتها نقص كتابة لا انعدام تحقق.

كل رابط وارد من محتوى معتمد إلى ملف منقول يُستبدل بملاحظة gap صريحة، فلا يبقى
رابط مكسور ولا يُحذف أثر العلاقة صامتاً.

    python3 scripts/quarantine_unverified_thinkers.py           # فحص
    python3 scripts/quarantine_unverified_thinkers.py --apply   # تنفيذ
"""
import glob, json, os, re, shutil, sys

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR    = os.path.join(ROOT, "content", "ar")
THK   = os.path.join(AR, "thinkers")
DST   = os.path.join(AR, "drafts", "thinkers")
MAN   = os.path.join(ROOT, "scripts", "quarantined_thinkers.json")
APPLY = "--apply" in sys.argv

SHELL_PATS = ["قدم هذا المفكر مساهمات تأسيسية عميقة", "قدم هذا المفكر إسهامات جوهرية",
    "قدم هذا المفكر إسهامات تأسيسية صاغت معالم المدرسة", "تعد أفكاره ومؤلفاته مرجعاً رئيسياً",
    "إسهامات تأسيسية خالدة في تاريخ الفلسفة", "إسهامات نوعية ومؤثرة في مجال",
    "تعد أعماله مرجعاً رئيسياً لفهم الأسئلة الكبرى"]

def read(p): return open(p, encoding="utf-8").read()

def reasons(t):
    fm, body = t.split("---", 2)[1], t.split("---", 2)[2]
    title = (re.search(r'^title: "(.*)"$', fm, re.M) or [None, ""])[1]
    h1    = (re.search(r'^# (.*)$', body, re.M) or [None, ""])[1]
    lede  = (re.search(r'^# .*\n\n(.*)$', body, re.M) or [None, ""])[1]
    r = []
    if "DRAFT-UNKNOWN" in t:                      r.append("علامة [DRAFT-UNKNOWN]")
    if re.search(r'[\[\]]', title):               r.append("عنوان بين أقواس معقوفة")
    if "DRAFT-UNKNOWN" in h1 or "DRAFT-UNKNOWN" in lede: r.append("نص نائب ظاهر للقارئ")
    if re.search(r'مساهمات في كتب|فصول في كتب|أبحاث منشورة في \*', body): r.append("قسم أعمال نائب")
    if "تعارض هوية" in t:                          r.append("تعارض هوية slug/en")
    return r

def main():
    targets = {}
    for f in sorted(glob.glob(os.path.join(THK, "*.md"))):
        t = read(f); b = os.path.basename(f)[:-3]
        if any(p in t for p in SHELL_PATS): continue      # مفكّر حقيقي، ينقصه نص فقط
        r = reasons(t)
        if r:
            title = (re.search(r'^title: "(.*)"$', t.split("---",2)[1], re.M) or [None,""])[1]
            targets[b] = {"title": title, "reasons": r}
    if not targets:
        print("لا شيء للنقل."); return

    # تحويل كل رابط وارد إلى ملاحظة gap صريحة
    rewritten = 0; files_touched = 0
    for f in glob.glob(os.path.join(AR, "*", "*.md")):
        if os.sep+"drafts"+os.sep in f or os.sep+"_merged"+os.sep in f: continue
        if os.path.basename(f)[:-3] in targets: continue
        t = o = read(f); notes = []
        for m in re.finditer(r'^\s*- id: "([^"]+)", title: "([^"]*)".*$', t, re.M):
            if m.group(1) in targets:
                notes.append('  - "رابط أُزيل عند نقل مدخل غير متحقَّق منه إلى المسودات: '
                             f'{m.group(2)} ({m.group(1)})."')
        if not notes: continue
        for tid in targets:
            t = re.sub(r'^\s*- id: "%s".*\n' % re.escape(tid), "", t, flags=re.M)
        mg = re.search(r'^gaps:\n((?:  - ".*"\n)*)', t, re.M)
        if mg: t = t[:mg.end(1)] + "\n".join(dict.fromkeys(notes)) + "\n" + t[mg.end(1):]
        else:  t = t.replace("\n---\n", "\ngaps:\n" + "\n".join(dict.fromkeys(notes)) + "\n---\n", 1)
        if t != o:
            if APPLY: open(f, "w", encoding="utf-8").write(t)
            rewritten += len(notes); files_touched += 1

    if APPLY:
        os.makedirs(DST, exist_ok=True)
        for b in targets:
            shutil.move(os.path.join(THK, b + ".md"), os.path.join(DST, b + ".md"))
        json.dump(targets, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"{'APPLIED' if APPLY else 'DRY RUN'} — {len(targets)} ملفاً إلى drafts/thinkers/؛ "
          f"{rewritten} رابطاً وارداً تحوّل إلى ملاحظة gap في {files_touched} ملفاً.")
    from collections import Counter
    c = Counter(r for v in targets.values() for r in v["reasons"])
    for k, n in c.most_common(): print(f"   {n:>4}  {k}")

main()
