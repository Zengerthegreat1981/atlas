"""
يحذف روابط `con-authenticity` («الأصالة») المُقحَمة حشواً في `related`.

الخلل: نفسُ الدفعة القالبية التي وسمت الملفات بمسارٍ وجوديٍّ خاطئ حشَت أيضاً
`con-authenticity` في `related` لملء الحقل الفارغ. فصار القارئُ يجد في «تجربة
آش للامتثال» و«دراسة بروكا للمريض تان» و«مقياس وكسلر للذاكرة» رابطاً وحيداً
اسمه «الأصالة» — ومفهومُ الأصالة لا يُذكَر في متن أيٍّ منها ولا صلةَ له بها.

المعيار: يُحذف الرابط فقط إذا **لم يُذكَر** جذرُ «أصالة/أصيل/authentic» في متن
الملف (اللِّيدِ + الأقسام). فإن ذُكر تُرك — فالرابط حينها مسوَّغٌ بالمتن.
وهذا هو نفسُ معيار `remove_spurious_related_links.py` لدفعة
`br-ml-personalized-therapy`.

ملاحظة: يبقى بعد الحذف ملفٌّ بـ`related` فارغ في الحالات التي كان الحشوُ فيها
الرابطَ الوحيد. وهذا مقصود: غيابُ رابطٍ أصدقُ من رابطٍ خاطئ، ويُسجَّل في `gaps`.

    python3 scripts/remove_filler_authenticity_links.py
    python3 scripts/remove_filler_authenticity_links.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TARGET = "con-authenticity"
SUPPORT = ("أصالة", "أصيل", "أصيلة", "authentic", "Authentic", "Eigentlichkeit")

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p
    return None

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    removed = kept = emptied = 0
    for slug, n in sorted(d.items()):
        if slug == TARGET: continue
        if not any(r[0] == TARGET for r in n.get("related", [])): continue
        body = (n.get("lede") or "") + " ".join(x[1] for x in n.get("sections", []))
        if any(w in body for w in SUPPORT):
            kept += 1; continue
        only = len(n.get("related", [])) == 1
        removed += 1; emptied += 1 if only else 0
        print(f"{'APPLY' if apply else 'DRY'}  {slug}"
              f"{'   (كان الرابط الوحيد -> related فارغ)' if only else ''}")
        if not apply: continue
        p = find_file(slug)
        if not p: print("   !! not found"); continue
        s = open(p, encoding="utf-8").read()
        s = re.sub(r'^- id: "' + TARGET + r'",.*\n', '', s, flags=re.M)
        note = ('  - "**حُذف رابطٌ مُقحَم 2026-09-08:** كان `related` يحمل '
                '`con-authenticity` («الأصالة») حشواً من دفعةٍ قالبية، ولا يُذكَر '
                'المفهومُ في متن هذا الملف ولا صلةَ له بموضوعه'
                + ('، وكان الرابطَ الوحيد — فبقي `related` فارغاً حتى يُراجَع، '
                   'وغيابُ الرابط أصدقُ من رابطٍ خاطئ."' if only else '."'))
        s = re.sub(r'^gaps:$', 'gaps:\n' + note, s, count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(s)
    print(f"\nحُذف: {removed}  (منها {emptied} كان الرابطَ الوحيد)   | أُبقي لأنّ المتن يسوّغه: {kept}")

if __name__ == "__main__":
    main()
