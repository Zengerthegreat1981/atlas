"""
المرحلة 2 — حلُّ أهدافِ الحروف النصّية، وربطُ الملفات المُنشأة.

كانت 35 حرفاً في `edges` هدفُها **نصٌّ** لا slug، فلا يقرأها الرسمُ البيانيُّ ولا
يُوصِل منها التنقّل. وقد انقسمت ثلاثةَ أقسام:

  (1) **تُحلّ الآن** إلى ملفاتٍ صارت قائمة — أكثرُها مدارسُ أُنشئت في جلسة
      2026-09-09 (علمُ النفس المعرفي، علمُ الأعصاب المعرفي، طبُّ الأعصاب
      السلوكي، علمُ نفس الصدمة، علمُ النفس عبر الثقافي)، وثلاثةُ مؤلّفين
      أُنشئوا في هذه الجلسة (غوفمان وغاردنر وسبيرمان) — وملفاتُ أعمالهم كانت
      تُعلن `author_slug` نحوهم وتُسجّل غيابَهم في `gaps`.

  (2) **هدفٌ خاطئ**: `ctx-ancient-athens-agora` كان يشير نصّاً إلى «السقراطية»
      و`stu-wundt-leipzig-1879` إلى «البنيوية (فونت وتيتشنر)». وأقربُ ما في
      الأطلس اسماً إليهما — `sch-presocratics` و`sch-structuralism` — **شيءٌ
      آخرُ تماماً**: ما قبلَ السقراطية ليست السقراطية، والبنيويةُ الفرنسيةُ
      (ليفي-شتراوس) ليست بنيويةَ فونت وتيتشنر في علم النفس. فلا يصحُّ التوجيهُ
      إليهما، وتُسجَّل الفجوةُ كما هي.

  (3) **مدرسةٌ غائبةٌ فعلاً** (13 اسماً في 17 حرفاً): يُحذف الحرفُ الميتُ —
      لأنه لا يُنتج رابطاً ولا يقرأه أحد — ويُسجَّل الاسمُ الغائبُ في `gaps`
      تسجيلاً صريحاً ليُنشأ لاحقاً. فلا معلومةَ تضيع: تنتقل من حرفٍ ميتٍ إلى
      فجوةٍ مقروءة.
"""
import os, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

# النصُّ → (الـslug, النوع)
RESOLVE = {
    "علم النفس المعرفي": ("sch-cognitive-psychology", "مدرسة"),
    "علم الأعصاب المعرفي": ("sch-cognitive-neuroscience", "مدرسة"),
    "طب الأعصاب السلوكي": ("sch-behavioral-neurology", "مدرسة"),
    "علم نفس الصدمة": ("sch-trauma-psychology", "مدرسة"),
    "علم النفس عبر الثقافي": ("sch-cross-cultural-psychology", "مدرسة"),
    "العلاج الأسري الاستراتيجي": ("tec-strategic-family-therapy", "تقنية/تدخل علاجي"),
    "إرفينغ غوفمان": ("thk-goffman", "مفكر"),
    "هوارد غاردنر": ("thk-gardner", "مفكر"),
    "تشارلز سبيرمان": ("thk-spearman", "مفكر"),
}

# النصُّ → سببُ عدم التوجيه (مدرسةٌ غائبةٌ أو هدفٌ خاطئ)
ABSENT = {
    "اليقظة الذهنية الإكلينيكية": "لا ملفَّ لليقظة الذهنية الإكلينيكية كمدرسةٍ جامعة؛ والموجودُ "
        "`sch-mbct` وهو برنامجٌ بعينه لا المظلّة",
    "السقراطية": "لا ملفَّ للسقراطية؛ و`sch-presocratics` **ما قبلَ** السقراطية أي شيءٌ آخرُ تماماً فلا يصحُّ التوجيهُ إليه",
    "البنيوية (فونت وتيتشنر)": "لا ملفَّ للبنيوية الاستبطانية في علم النفس (فونت وتيتشنر)؛ و`sch-structuralism` "
        "في الأطلس هي البنيويةُ الفرنسيةُ (ليفي-شتراوس) وهي شيءٌ آخرُ تماماً",
    "التفاعلية الرمزية": "لا ملفَّ للتفاعلية الرمزية — وهي إطارٌ سوسيولوجيٌّ خارجَ القسمَين الحاليَّين",
    "علم نفس الدين": "لا ملفَّ لعلم نفس الدين كمدرسة",
    "علم الموت (Thanatology)": "لا ملفَّ لعلم الموت (Thanatology)",
    "علم نفس الحب": "لا ملفَّ لعلم نفس الحب كمدرسة",
    "العلاج الجماعي": "لا ملفَّ للعلاج الجماعي كمدرسةٍ أو تيّار",
    "طب نفس الطفل": "لا ملفَّ لطبِّ نفس الطفل كمدرسة؛ والموجودُ `br-child-psychoanalysis` وهو تيّارٌ تحليليٌّ بعينه",
    "علم النفس العصبي الإكلينيكي": "لا ملفَّ لعلم النفس العصبي الإكلينيكي",
    "علم الأدوية النفسية": "لا ملفَّ لعلم الأدوية النفسية",
    "العلاج الأسري الخبراتي": "لا ملفَّ للعلاج الأسري الخبراتي (ويتاكر)",
    "النمو المعرفي": "لا ملفَّ لفروع علم النفس النمائي الخمسة التي يسمّيها المتن",
    "النمو النفسي-الاجتماعي": "لا ملفَّ لفروع علم النفس النمائي الخمسة التي يسمّيها المتن",
    "النمو الأخلاقي": "لا ملفَّ لفروع علم النفس النمائي الخمسة التي يسمّيها المتن",
    "النمو اللغوي": "لا ملفَّ لفروع علم النفس النمائي الخمسة التي يسمّيها المتن",
    "نمو المراهقة": "لا ملفَّ لفروع علم النفس النمائي الخمسة التي يسمّيها المتن",
}

# روابطُ `related` تُضاف للعقد التي صار لها مؤلِّف
ADD_RELATED = {
    "wrk-goffman-presentation-self": ("thk-goffman", "إرفينغ غوفمان", "مفكر"),
    "wrk-frames-of-mind": ("thk-gardner", "هوارد غاردنر", "مفكر"),
    "wrk-nature-intelligence": ("thk-spearman", "تشارلز سبيرمان", "مفكر"),
}
ADD_RELATED_MULTI = {
    "sch-stoicism": [("thk-zeno-citium", "زينون الرواقي (زينون القِبرصي)", "مفكر")],
    "sch-cognitive-psychology": [("thk-gardner", "هوارد غاردنر", "مفكر")],
    "sch-social-psychology": [("thk-goffman", "إرفينغ غوفمان", "مفكر")],
    "ctx-stoa-poikile-athens": [("thk-zeno-citium", "زينون الرواقي (زينون القِبرصي)", "مفكر")],
}
STAMP = "**حُلَّ هدفٌ نصّيٌّ 2026-09-10:** "


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    dead = [(s, e[0], e[1]) for s, n in d.items() for e in n.get("edges", []) if e[1] not in d]
    res = absent = 0
    by_file = collections.defaultdict(list)
    for s, rel, txt in dead:
        by_file[s].append((rel, txt))

    for s, items in sorted(by_file.items()):
        p, t = E.load(s)
        notes = []
        for rel, txt in items:
            if txt in RESOLVE:
                slug, tt = RESOLVE[txt]
                t2 = E.replace_edge_target(t, txt, slug, tt)
                if t2 is None:
                    print("  ⚠️ ", s, rel, txt); continue
                t = t2
                notes.append(f"وُجِّه `{rel}` من النصِّ «{txt}» إلى `{slug}`")
                res += 1
            elif txt in ABSENT:
                t2 = E.remove_edge(t, rel=rel, target=txt)
                if t2 is None:
                    print("  ⚠️ ", s, rel, txt); continue
                t = t2
                notes.append(f"حُذف حرفٌ ميتٌ `{rel} → «{txt}»` — {ABSENT[txt]}")
                absent += 1
            else:
                print("  ⚠️  غيرُ مصنَّف:", s, rel, txt)
        if notes:
            t = E.add_gap(t, STAMP + "؛ و".join(notes) + ".") or t
            E.save(p, t)

    # روابطُ related للمؤلِّفين والمؤسِّس الجديد
    added = 0
    for s, one in ADD_RELATED.items():
        p, t = E.load(s)
        cur = [tuple(r) for r in d[s]["related"]]
        if any(r[0] == one[0] for r in cur):
            continue
        t2 = E.set_related(t, cur + [one])
        if t2:
            E.save(p, t2); added += 1
    for s, many in ADD_RELATED_MULTI.items():
        p, t = E.load(s)
        cur = [tuple(r) for r in d[s]["related"]]
        new = [x for x in many if not any(r[0] == x[0] for r in cur)]
        if not new:
            continue
        t2 = E.set_related(t, cur + new)
        if t2:
            E.save(p, t2); added += len(new)

    print(f"وُجِّه {res} حرفاً · حُذف {absent} حرفاً ميتاً مع تسجيل الغياب · أُضيف {added} رابطَ related")


if __name__ == "__main__":
    main()
