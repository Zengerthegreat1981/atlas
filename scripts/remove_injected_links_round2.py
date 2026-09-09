"""
يحذف الدفعةَ الثانيةَ من الروابط المُقحَمة، ويسدُّ عزلتين رصدهما `audit_atlas.py`.

## أ) `br-sikolohiyang-pilipino` مُقحَمٌ في 14 ملفاً
علمُ النفس الفلبيني الأصيل (إنريكيز) مُدرَجٌ في `related` لـ**الشفاء الشعبي
المكسيكي** و**ABA للتوحّد** و**Theraplay** و**العلاج الأسري الوظيفي** و**حركة
الذاكرة المستعادة** و**نماذج الإدمان** — ولا يُذكَر الفلبينُ ولا «kapwa» ولا
إنريكيز في متن أيٍّ منها.

وهذا الهدفُ **رُصد من قبل** في تقرير 2026-09-07 (سُجِّل في فجوات
`br-bodynamic-analysis`: «كان الملف يشير إلى `br-ml-personalized-therapy`
و`br-sikolohiyang-pilipino` بلا أي مسوّغ»)، لكنّ سكريبت التنظيف حينها عالج
الهدفَ الأولَ وحده وأغفل الثاني. فهذا **نقصٌ في عملي السابق** كشفته المراجعةُ
الشاملة.

## ب) `br-ml-personalized-therapy`: حالةٌ واحدةٌ باقية
أُبقيت ثلاثةُ روابطَ بحكمٍ تحريريّ — **العلاجات الرقمية** و**العلاج عن بُعد**
و**العلاج بالألعاب** و**المعالجة التوقعية** تيّاراتٌ تقنيةٌ شقيقةٌ للعلاج
المخصّص بالتعلّم الآلي، والصلةُ بينها موضوعيةٌ وإن لم يذكر متنُها لفظَ «تعلّم
الآلة». أمّا **النموذج الطبي للإدمان** فلا صلةَ تقنيةَ له بحال، فحُذف.

## ج) عزلتان
`dbt-foundationalism-vs-coherentism` و`ins-whoqol-bref` صارتا معزولتين: الأولى
بعد نقل نسبها إلى `sch-epistemology`، والثانية تُشير إلى نظيرتها ولا تُشار
إليها. فأُضيف الرابطُ العكسيُّ في كلٍّ (وكلاهما عكسُ علاقةٍ يؤكّدها المستودع).

    python3 scripts/remove_injected_links_round2.py            # فحص
    python3 scripts/remove_injected_links_round2.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIKO = "br-sikolohiyang-pilipino"
SIKO_WORDS = ("فلبين", "Sikolohiyang", "Filipino", "إنريكيز", "kapwa")
ML = "br-ml-personalized-therapy"
ML_DROP = ["br-medical-model-addiction"]
# روابطُ ML المُبقاةُ بحكمٍ تحريريٍّ مُعلَن (تيّاراتٌ تقنيةٌ شقيقة)
ML_KEEP = ["br-digital-therapeutics", "br-teletherapy",
           "br-serious-games-therapy", "br-predictive-processing-informed"]
# عزلتان: المضيف -> المعزولة
DEORPHAN = {
    "sch-epistemology": ("dbt-foundationalism-vs-coherentism",
                         "عكسُ نسبٍ يُعلنه الملفُّ نفسُه (`belongs_to`)"),
    "ins-warwick-edinburgh-wellbeing": ("ins-whoqol-bref",
                         "عكسُ إشارةٍ يُعلنها الملفُّ نفسُه في `related`"),
}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def safe_title(t):
    t = (t or "").replace('\\"', '"')
    if '"' not in t: return t
    out = []; op = True
    for ch in t:
        if ch == '"': out.append('«' if op else '»'); op = not op
        else: out.append(ch)
    return ''.join(out)

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    n_rm = 0
    # أ) سيكولوهيانغ
    for s, node in sorted(d.items()):
        if s == SIKO or not any(r[0] == SIKO for r in node.get("related", [])): continue
        body = (node.get("lede") or "") + " ".join(x[1] for x in node.get("sections", []))
        if any(w in body for w in SIKO_WORDS): continue
        p = find_file(s); t = open(p, encoding="utf-8").read()
        t2 = re.sub(r'^- id: "' + SIKO + r'",.*\n', '', t, flags=re.M)
        if t2 == t: continue
        note = ('  - "**حُذف رابطٌ مُقحَم 2026-09-08:** كان `related` يحمل '
                '`br-sikolohiyang-pilipino` (علم النفس الفلبيني الأصيل) بلا أيِّ مسوّغ — '
                'ولا يُذكَر الفلبينُ ولا إنريكيز ولا «kapwa» في متن هذا الملفّ. '
                'وهو من دفعةٍ قالبيةٍ رُصد هدفُها الأوّل من قبل وأُغفل هذا."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        n_rm += 1
        print(f"{'APPLY' if apply else 'DRY'}  [siko] {s}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    # ب) ML
    for s in ML_DROP:
        p = find_file(s); t = open(p, encoding="utf-8").read()
        t2 = re.sub(r'^- id: "' + ML + r'",.*\n', '', t, flags=re.M)
        if t2 == t: continue
        note = ('  - "**حُذف رابطٌ مُقحَم 2026-09-08:** كان `related` يحمل '
                '`br-ml-personalized-therapy` بلا مسوّغ — لا صلةَ تقنيةَ بين نماذج '
                'الإدمان والعلاج المخصّص بالتعلّم الآلي."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        n_rm += 1
        print(f"{'APPLY' if apply else 'DRY'}  [ml]   {s}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    # ج) العزلتان
    for host, (orphan, why) in DEORPHAN.items():
        p = find_file(host); t = open(p, encoding="utf-8").read()
        if f'id: "{orphan}"' in t: print(f"   {host}: يشير إليها بالفعل"); continue
        line = f'- id: "{orphan}", title: "{safe_title(d[orphan].get("title"))}", type: "{d[orphan].get("type")}"\n'
        m = re.search(r'^related:\n((?:- .*\n)*)', t, re.M)
        if m: t2 = t[:m.end(1)] + line + t[m.end(1):]
        else: t2 = re.sub(r'^gaps:$', 'related:\n' + line + 'gaps:', t, count=1, flags=re.M)
        note = ('  - "**رُبطت عقدةٌ معزولة 2026-09-08:** أُضيفت الإشارةُ إلى '
                f'`{orphan}` — {why}؛ ولم يكن يشير إليها أيُّ ملفّ فكانت غيرَ قابلةٍ '
                'للوصول بالتنقّل."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        print(f"{'APPLY' if apply else 'DRY'}  [orph] {host} -> {orphan}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    print(f"\nحُذف: {n_rm}   |  أُبقي بحكمٍ تحريريّ: {ML_KEEP}")

if __name__ == "__main__":
    main()
