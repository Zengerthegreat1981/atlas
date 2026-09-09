"""
يصحّح نسبَ تسعِ عقدٍ في **نظرية المعرفة المعاصرة** كانت مُدرَجةً تحت حلقة فيينا.

## كيف وقع الخلل، ومن أوقعه
كانت هذه التسعُ تُعلن `br-logical-positivism-vienna-circle` أباً لها ختماً
قالبياً. ولمّا دُمج ذلك الملفُّ في `sch-vienna-circle` (لأنهما مزدوجان)، نُقلت
أنسابُ أبنائه إلى المعتمد آلياً — **فحُمِل الخطأُ ولم يُصلَح**: صارت «مشكلة
غيتييه» و«الاعتمادية» و«السياقية المعرفية» أبناءً لحلقة فيينا.

وهذا خطأٌ من عملي في الخطوة السابقة، لا خللٌ موروث. ومشكلةُ غيتييه نُشرت 1963
وكلُّ هذه المباحث لاحقةٌ للوضعية المنطقية وناقدةٌ لها في كثيرٍ من مواضعها،
فنسبتُها إلى حلقة فيينا خطأٌ في التاريخ والمذهب معاً.

و`sch-epistemology` («نظرية المعرفة — إبستمولوجيا») موجودةٌ في الأطلس، وهي
موضعُها الصحيح.

    python3 scripts/fix_epistemology_parents.py            # فحص
    python3 scripts/fix_epistemology_parents.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WRONG = "sch-vienna-circle"
RIGHT = "sch-epistemology"
NODES = ["con-gettier-problem", "con-reliabilism-epistemology", "con-contextualism-epistemic",
         "con-virtue-epistemology", "con-pragmatic-encroachment", "con-principle-of-charity-davidson",
         "dbt-foundationalism-vs-coherentism", "dbt-internalism-vs-externalism-epistemic",
         "dbt-cognitivism-vs-non-cognitivism-ethics"]

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    if RIGHT not in d: print("!! غير موجود:", RIGHT); return
    n = 0
    for slug in NODES:
        if slug not in d: print("!! غير موجود:", slug); continue
        p = find_file(slug); t = open(p, encoding="utf-8").read()
        m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(WRONG) + r'".*$', t, re.M)
        if not m: print(f"   {slug}: لا يشير إلى {WRONG} — يُترك"); continue
        t = t[:m.start()] + f'- rel: "belongs_to", target: "{RIGHT}", target_type: "{d[RIGHT].get("type")}"' + t[m.end():]
        note = ('  - "**صُحِّح الانتماء 2026-09-08:** كان `belongs_to` يشير إلى حلقة فيينا — '
                'ختماً قالبياً حُمِل آلياً عند دمج ملفٍّ مزدوج. ومباحثُ نظرية المعرفة '
                'المعاصرة (مشكلةُ غيتييه 1963 وما بعدها) لاحقةٌ للوضعية المنطقية وناقدةٌ '
                f'لها، فنُقل الانتماءُ إلى `{RIGHT}`."')
        t = re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)
        n += 1
        print(f"{'APPLY' if apply else 'DRY'}  {slug:44} -> {RIGHT}")
        if apply: open(p, "w", encoding="utf-8").write(t)
    print(f"\nصُحِّح: {n}")

if __name__ == "__main__":
    main()
