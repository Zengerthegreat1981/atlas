"""
مسحٌ منهجيٌّ للغياب في الأطلس — يُعيد إنتاج تقرير GAP_SURVEY.
    python3 scripts/survey_gaps.py            # كل الممرّات
    python3 scripts/survey_gaps.py --orphans  # ممرٌّ واحد

الممرّات الأربعة المشتقّة من بنية المستودع (موضوعية، لا تعتمد تقديراً):
  1) unresolved : أهداف edges التي لا تُحلّ إلى ملفّ ولا إلى عنوان
  2) authorless : أعمال (wrk-) بلا أيِّ مفكّرٍ مربوط
  3) orphans    : عقد بلا رابطٍ وارد (لا related ولا edges تشير إليها)
  4) staleg     : بنود gaps التي تدّعي غياب slug صار موجوداً — فجوة متقادمة

تحذيرٌ لمن يُوسِّع هذا السكريبت بمطابقة الأسماء (تعلَّمته بالخطأ):
  - وحِّد Unicode: `Ricœur` لا يطابق `Ricoeur`؛ 81 ملفّاً فيه حرفٌ مركّب.
  - الحرفُ الأوسط يكسر المطابقة: `Gordon Allport` ≠ `Gordon W. Allport`.
  - المطابقةُ باللقب وحده تُعطي أشخاصاً مختلفين: thk-alecmiller ليس جورج ميلر.
  فكلُّ مطابقةٍ باللقب لازمٌ أن تُراجَع يدوياً قبل إعلان غياب.
"""
import json, re, sys, os, collections, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data.json")

def fold(s):
    s = (s or "")
    for a, b in [('œ','oe'),('Œ','OE'),('æ','ae'),('Æ','AE'),('ø','o'),('ß','ss')]:
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()

def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)["nodes"]

def inbound(d):
    inb = collections.defaultdict(set)
    for s, n in d.items():
        for r in n.get("related", []):
            if r[0] in d: inb[r[0]].add(s)
        for e in n.get("edges", []):
            if e[1] in d: inb[e[1]].add(s)
    return inb

def p_unresolved(d):
    by_title = {(n.get("title") or "").strip() for n in d.values()}
    unres = collections.Counter(); ex = {}
    for s, n in d.items():
        for rel, target, ttype in n.get("edges", []):
            if target in d or target in by_title: continue
            unres[(rel, target, ttype)] += 1; ex.setdefault((rel, target, ttype), s)
    print(f"\n[1] أهداف edges غير المحلولة: {len(unres)} مميَّزاً ({sum(unres.values())} وروداً)")
    for k, c in unres.most_common(30):
        print(f"   {c:3}  [{k[2]}] {k[1][:60]}  (rel={k[0]}, مثال {ex[k]})")

def p_authorless(d):
    out = []
    for s, n in d.items():
        if not s.startswith("wrk-"): continue
        if any(r[0] in d and d[r[0]].get("type") == "مفكر" for r in n.get("related", [])): continue
        if any(e[1] in d and d[e[1]].get("type") == "مفكر" for e in n.get("edges", [])): continue
        out.append(s)
    tot = sum(1 for s in d if s.startswith("wrk-"))
    print(f"\n[2] أعمال بلا مؤلِّفٍ مربوط: {len(out)} من {tot}")
    print("    (الأغلبُ رابطٌ غائبٌ لا ملفٌّ غائب — راجِع كلَّ حالةٍ قبل الكتابة)")
    for s in out: print("   ", s, "|", (d[s].get("title") or "")[:60])

def p_orphans(d):
    inb = inbound(d)
    by = collections.Counter(); lst = collections.defaultdict(list)
    for s, n in d.items():
        if not inb[s]:
            by[n.get("type", "?")] += 1; lst[n.get("type", "?")].append(s)
    print(f"\n[3] عقد معزولة (بلا رابطٍ وارد): {sum(by.values())} من {len(d)} "
          f"({100*sum(by.values())/len(d):.1f}%)")
    for k, v in by.most_common(): print(f"   {k}: {v}")
    print(f"   بلا related إطلاقاً: {sum(1 for n in d.values() if not n.get('related'))}")
    print(f"   بلا edges إطلاقاً:   {sum(1 for n in d.values() if not n.get('edges'))}")
    return lst

def p_staleg(d):
    pat = re.compile(r'لا ملفَّ|لا ملف |بلا ملف|بلا ملفّ|بلا ملفٍّ|لا يوجد ملف|يستحقّ ملفاً')
    SLUG = re.compile(r'`((?:thk|con|sch|br|tec|wrk|rel|dbt|que|met|trm|ins|stu|evt|exp|crt|dia|syn|dis|ctx|axm)-[a-z0-9\-]+)`')
    claims = 0; stale = []
    for s, n in d.items():
        for g in n.get("gaps", []):
            if not pat.search(g): continue
            claims += 1
            for m in SLUG.findall(g):
                if m in d: stale.append((s, m, g[:120])); break
    print(f"\n[4] بنود gaps تُصرِّح بغياب: {claims}")
    print(f"    منها تذكر slug صار موجوداً (مرشَّحة للتقادم — تحتاج مراجعةً يدوية): {len(stale)}")
    for s, m, g in stale[:30]: print(f"   {s} -> `{m}` موجود الآن\n      {g}")

def p_empty_schools(d):
    for pref, label in [("sch-", "مدرسة"), ("br-", "تيار")]:
        empty = [s for s in d if s.startswith(pref) and not any(
            any(e[0] == "belongs_to" and e[1] == s for e in d[x].get("edges", [])) for x in d)]
        tot = sum(1 for s in d if s.startswith(pref))
        print(f"\n[5] {label} بلا أعضاء belongs_to: {len(empty)} من {tot}")

if __name__ == "__main__":
    d = load()
    args = set(sys.argv[1:])
    run_all = not args
    print(f"الأطلس: {len(d)} عقدة")
    if run_all or "--unresolved" in args: p_unresolved(d)
    if run_all or "--authorless" in args: p_authorless(d)
    if run_all or "--orphans" in args: p_orphans(d)
    if run_all or "--stale" in args: p_staleg(d)
    if run_all or "--empty" in args: p_empty_schools(d)
