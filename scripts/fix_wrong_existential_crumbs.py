"""
يصحّح الجزء الأول من `crumb` في أدوات القياس والدراسات التي وُسمت خطأً
بـ«المدرسة الوجودية».

الخلل: دفعةٌ آليةٌ ولّدت هذه الملفات بقالبٍ وجودي، فصار مسارُ التنقّل المعروض
للقارئ يقول إنّ «مقياس بيك للاكتئاب» و«تجربة آش للامتثال» و«دراسة بروكا للمريض
تان» تنتمي إلى المدرسة الوجودية. وهو خطأٌ ظاهرٌ للمستخدم لا لبسَ فيه.

نطاقُ المعالجة **مضيَّقٌ عن قصد** إلى نوعين فقط: «أداة قياس» و«دراسة وبحث» —
لأنّ نسبةَ أداةِ قياسٍ أو تجربةٍ معمليةٍ إلى مدرسةٍ فلسفيةٍ خطأٌ قاطع. وتُستثنى
الملفاتُ التي يذكر متنُها الوجوديةَ أو التي تُحيل إلى عقدةٍ وجودية — تُطبع
للمراجعة البشرية ولا تُلمس. ولا يُلمس المفكِّرون ولا الأعمال: فيهم مَن انتسابُه
الوجوديُّ صحيح (مثل `wrk-being-nothingness` و`thk-wong`)، والتمييزُ فيهم يحتاج
حكماً بشرياً لا قاعدةً آلية.

ويُستبدَل **الجزء الأول وحده**؛ والجزءان الثاني والثالث صحيحان ومتّسقان مع النوع.

    python3 scripts/fix_wrong_existential_crumbs.py            # فحص
    python3 scripts/fix_wrong_existential_crumbs.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BAD = "المدرسة الوجودية"
TYPES = ("أداة قياس", "دراسة وبحث")
EXIST = ("وجودي", "الوجودية", "existential", "Existential")

# لا تصنيفَ موضوعيّ: جُرِّب تصنيفٌ بالكلمات الدالّة فأخطأ (نسب «التيسير الاجتماعي»
# لتريبليت إلى علم النفس العصبي)، فأُسقط. تُستعمل قيمٌ صادقةٌ دائماً ولو كانت أعمّ،
# ويُسجَّل في `gaps` أنّ المجال الأدقّ لم يُحدَّد — أعمُّ وصادقٌ خيرٌ من أخصَّ وخاطئ.
PART_AR = {"psychology": "علم النفس", "philosophy": "الفلسفة", "sociology": "علم الاجتماع"}

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
    changed = 0; held = []
    counts = {}
    for slug, n in sorted(d.items()):
        crumb = n.get("crumb") or ""
        if not crumb.startswith(BAD) or n.get("type") not in TYPES: continue
        body = (n.get("lede") or "") + " ".join(x[1] for x in n.get("sections", []))
        rel_ex = any("existen" in r[0] or "وجودي" in (d.get(r[0], {}).get("title") or "")
                     for r in n.get("related", []) if r[0] in d)
        if any(w in body for w in EXIST) or rel_ex:
            held.append(slug); continue
        parts = [p.strip() for p in crumb.split("←")]
        if len(parts) < 2: continue
        if n.get("type") == "أداة قياس":
            new = "القياس النفسي والتشخيص"
        else:
            new = PART_AR.get(n.get("part"), "علم النفس")
        parts[0] = new
        newcrumb = " ← ".join(parts)
        counts[new] = counts.get(new, 0) + 1
        changed += 1
        print(f"{'APPLY' if apply else 'DRY'}  {slug}\n    - {crumb}\n    + {newcrumb}")
        if apply:
            p = find_file(slug)
            if not p: print("   !! not found"); continue
            s = open(p, encoding="utf-8").read()
            s = re.sub(r'^crumb: ".*"$', 'crumb: "' + newcrumb + '"', s, count=1, flags=re.M)
            note = ('  - "**صُحِّح مسار التنقّل 2026-09-08:** كان الجزء الأول يقول «المدرسة '
                    'الوجودية»، وهو خطأٌ موروثٌ من دفعةٍ قالبية — لا صلةَ لمتن هذا الملف '
                    'بالوجودية. واستُبدل الجزء الأول وحده بقيمةٍ صادقةٍ عامّة، '
                    'والمجالُ الأدقُّ لم يُحدَّد بعد."')
            s = re.sub(r'^gaps:$', 'gaps:\n' + note, s, count=1, flags=re.M)
            open(p, "w", encoding="utf-8").write(s)
    print(f"\nصُحِّح: {changed}   التوزيع: {counts}")
    print(f"أُوقِف للمراجعة البشرية (متنُه أو روابطُه وجودية): {len(held)} -> {held}")

if __name__ == "__main__":
    main()
