"""
المرحلة 1.1 — رفعُ النسب المختوم قالبياً عن المتلازمات والاضطرابات.

المشكلة: 183 عقدةً من `syn-`/`dis-`/`evt-` تُعلن `belongs_to: sch-cognitive-behavioral`.
منها متلازماتٌ تاريخيةٌ سابقةٌ للعلاج المعرفي السلوكي (1955) بقرون: التارانتيسم
(1374) ورقصة القديس فيتوس (1374) وأموك (1770) وكاسبار هاوزر (1828). ولا يذكر
متنُ مدرسة CBT واحدةً منها.

والـ21 التي تذكر CBT في متنها تذكره **علاجاً يُستعمل معها** لا مدرسةً تنتمي
إليها («العلاج المعرفي السلوكي لإدارة الألم»)، فهي كذلك ليست أعضاءً.

القرار: يُحذف الحرف ولا يُعوَّض. المتلازمةُ كيانٌ وصفيٌّ تصنيفيٌّ لا عضوٌ في
مدرسةٍ علاجية — وهذا هو الحالُ القائمُ فعلاً في 15 متلازمةً لا أبَ لها.
ويُستثنى `evt-cbt-founding-1950s-60s` وحده: حدثُ تأسيس المدرسة نفسِها.

مسارُ التنقّل (crumb) لا يُلمَس: هو «الاضطرابات والمتلازمات ← …» أصلاً، فالعقدُ
تبقى قابلةً للوصول من فهرس النوع ومن روابطها الواردة (لا واحدةَ منها بلا
`related`).
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

ROOT = E.ROOT
PARENT = "sch-cognitive-behavioral"
KEEP = {"evt-cbt-founding-1950s-60s"}
GAP = ("**رُفع نسبٌ مختومٌ قالبياً 2026-09-10:** كان هذا الملفُّ يُعلن "
       "`sch-cognitive-behavioral` أباً له، وهو ختمٌ قالبيٌّ من دفعة إنشاءٍ سابقة: "
       "لا يذكر متنُ المدرسة هذه العقدةَ، ولا يُسند المتنُ هنا انتماءً إليها "
       "(وحيث ذُكر العلاجُ المعرفيُّ السلوكيُّ فبوصفه علاجاً يُستعمل، لا مدرسةً "
       "تنتمي إليها العقدة). فحُذف الحرفُ ولم يُعوَّض — والمتلازمةُ كيانٌ وصفيٌّ "
       "لا عضوٌ في مدرسةٍ علاجية.")

CBT_WORDS = ("المعرفي السلوكي", "المعرفية السلوكية", "المعرفي-السلوكي", "CBT", "العلاج المعرفي")


def main():
    d = json.load(open(os.path.join(ROOT, "data.json"), encoding="utf-8"))["nodes"]
    targets = [s for s, n in d.items()
               if s.split("-")[0] in ("syn", "dis", "evt")
               and any(e[0] == "belongs_to" and e[1] == PARENT for e in n.get("edges", []))
               and s not in KEEP]
    done, skipped = [], []
    for s in sorted(targets):
        p, t = E.load(s)
        t2 = E.remove_edge(t, rel="belongs_to", target=PARENT)
        if t2 is None:
            skipped.append(s)
            continue
        t3 = E.add_gap(t2, GAP) or t2
        E.save(p, t3)
        done.append(s)
    print(f"رُفع النسبُ عن {len(done)} ملفاً" + (f" · تُرك {len(skipped)}: {skipped}" if skipped else ""))
    print(f"استُثني بقصد: {sorted(KEEP)}")
    by = {}
    for s in done:
        by[s.split("-")[0]] = by.get(s.split("-")[0], 0) + 1
    print("بالنوع:", by)


if __name__ == "__main__":
    main()
