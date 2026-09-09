"""
يحوّل أسماءَ المدارس النصّيةَ في `belongs_to` إلى slugs المدارس المُنشأة حديثاً.

كان في الأطلس **25 اسماً نصّياً** يُستعمل أباً في `belongs_to` بلا ملفٍّ يقابله
(رصدها `audit_atlas.py`). وقد أُنشئت لعشرين منها مدارسُ، ويُصحَّح هنا انتماءُ
الملفات إليها.

## وخمسةٌ منها ليست مدارسَ، فلم تُنشأ — ومعالجتُها هنا
1. **«العلاج الظاهراتي الوجودي»** (`thk-calkins`): **خطأٌ في النسبة**. ماري
   ويتون كالكينز (1863–1930) أوّلُ رئيسةٍ للجمعية الأمريكية لعلم النفس، وعملُها
   في الاستبطان و«علم نفس الذات» بمعناه الخاصّ — ولا صلةَ لها بالعلاج الظاهراتي
   الوجودي الذي نشأ بعد وفاتها. فإنشاءُ مدرسةٍ لهذا الاسم كان سيُرسِّخ خطأً.
   يُفرَّغ حقلُها ويُسجَّل — و«البنائيةُ النفسية/الاستبطانية» نفسُها غائبةٌ عن
   الأطلس (سُجِّل غيابُها في `agents_specs/missing-schools.md`).
2. **«الفلسفة السياسية»** (`thk-orwell`): أورويل روائيٌّ وصحفيٌّ لا فيلسوفٌ
   سياسيّ، والاسمُ أعمُّ من أن يكون مدرسةً — وللأطلس مدارسُ سياسيةٌ محدَّدةٌ
   (`sch-rawlsianism` وغيرُها) لا ينتمي إليها. يُفرَّغ ويُسجَّل.
3. **«تأمّل المحبة (Metta)»** (`thk-ssalzberg`): **تقنيةٌ لا مدرسة**. ولِيدُ
   ملفِّها يسمّي انتماءَها: «تأمُّلُ الميتا وبوذيةُ الإشراك» — و
   `sch-engaged-buddhism` موجودةٌ في الأطلس. فيُنقَل الانتماءُ إليها.
4. **«تقنيات التحرر الانفعالي (EFT Tapping)»** (`thk-nicotole`): تقنيةٌ لا
   مدرسة، **والمدخلُ نفسُه غيرُ محقَّق** — لِيدُه يقول «الاسم المُسجَّل غير
   موثَّق في EFT». فلا تُبنى مدرسةٌ حول هويةٍ غيرِ متحقَّقة. يُفرَّغ ويُسجَّل.
5. **«علم النفس الإيكولوجي»**: أُدمج في `sch-ecopsychology` مع «العلاج البيئي»،
   فهما في الاستعمال حقلٌ واحد.

    python3 scripts/attach_new_school_members.py            # فحص
    python3 scripts/attach_new_school_members.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MAP = {
 "العلاج بالفن": "sch-art-therapy",
 "علم النفس النقدي": "sch-critical-psychology",
 "الإرشاد متعدد الثقافات": "sch-multicultural-counseling",
 "العلاج البيئي": "sch-ecopsychology",
 "علم النفس الإيكولوجي": "sch-ecopsychology",
 "منهجية البحث الظاهراتي": "sch-phenomenological-research",
 "علم النفس المعرفي": "sch-cognitive-psychology",
 "بحوث التنمّر المدرسي": "sch-bullying-research",
 "علم نفس الصدمة": "sch-trauma-psychology",
 "ما قبل السقراطية": "sch-presocratics",
 "علم النفس الثقافي": "sch-cultural-psychology",
 "علم أعصاب النوم": "sch-sleep-science",
 "علم الأعصاب المعرفي": "sch-cognitive-neuroscience",
 "علم نفس الانفعال": "sch-emotion-psychology",
 "العلاج النفسي الإيجابي (بسشكيان)": "sch-positive-psychotherapy",
 "العلاج النفسي التأملي": "sch-contemplative-psychotherapy",
 "طب الأعصاب السلوكي": "sch-behavioral-neurology",
 "العلاج المعرفي الطاوي": "sch-taoist-cognitive-therapy",
 "الأخلاق التحليلية": "sch-metaethics",
 "علم النفس عبر الثقافي": "sch-cross-cultural-psychology",
 # تقليدُ العون المتبادل: الاسمُ النصّيُّ كان «علم نفس الإدمان» وهو خطأٌ في
 # التصنيف — ويلسون وسميث أسّسا تقليداً في العون المتبادل لا حقلاً أكاديمياً.
 "علم نفس الإدمان": "sch-twelve-step",
 # تقنيةٌ لا مدرسة، والانتماءُ الصحيحُ موجودٌ في الأطلس
 "تأمّل المحبة (Metta)": "sch-engaged-buddhism",
}
# ليست مدارسَ: يُفرَّغ الحقلُ ويُسجَّل السبب
EMPTY = {
 "العلاج الظاهراتي الوجودي":
   "كالكينز (1863–1930) أوّلُ رئيسةٍ للجمعية الأمريكية لعلم النفس، وعملُها في "
   "الاستبطان و«علم نفس الذات» بمعناه الخاصّ. والعلاجُ الظاهراتيُّ الوجوديُّ نشأ "
   "بعد وفاتها، فنسبتُها إليه **خطأٌ في النسبة** لا مدرسةٌ غائبة. و«البنائيةُ "
   "النفسية/الاستبطانية» — وهي موضعُها الأقرب — غائبةٌ عن الأطلس",
 "الفلسفة السياسية":
   "أورويل روائيٌّ وصحفيٌّ لا فيلسوفٌ سياسيّ، و«الفلسفةُ السياسية» أعمُّ من أن "
   "تكون مدرسةً يُنسَب إليها؛ وللأطلس مدارسُ سياسيةٌ محدَّدةٌ لا ينتمي إليها",
 "تقنيات التحرر الانفعالي (EFT Tapping)":
   "تقنيةٌ لا مدرسة، **والمدخلُ نفسُه غيرُ محقَّق**: لِيدُه يقول إنّ الاسمَ "
   "المُسجَّل غيرُ موثَّقٍ في EFT. ولا تُبنى مدرسةٌ حول هويةٍ غيرِ متحقَّقة",
}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    missing = [v for v in MAP.values() if v not in d]
    if missing: print("!! مدارسُ غير موجودة:", missing); return
    stats = collections.Counter()
    for slug in sorted(d):
        for e in d[slug].get("edges", []):
            if e[0] != "belongs_to": continue
            name = e[1]
            if name in d: continue
            if name not in MAP and name not in EMPTY: continue
            p = find_file(slug)
            if not p: continue
            t = open(p, encoding="utf-8").read()
            m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(name) + r'".*$', t, re.M)
            if not m: continue
            if name in MAP:
                tgt = MAP[name]
                t2 = t[:m.start()] + f'- rel: "belongs_to", target: "{tgt}", target_type: "{d[tgt].get("type")}"' + t[m.end():]
                extra = ''
                if name == "علم نفس الإدمان":
                    extra = (' **ولم يُنسَب إلى «علم نفس الإدمان»** حرفياً: ويلسون وسميث '
                             'أسّسا تقليداً في العون المتبادل لا حقلاً أكاديمياً، فنسبتُهما '
                             'إلى حقلٍ أكاديميٍّ خطأٌ في التصنيف.')
                if name == "تأمّل المحبة (Metta)":
                    extra = (' **و«تأمّلُ المحبة» تقنيةٌ لا مدرسة**، وانتماءُ الملفّ '
                             'مذكورٌ في لِيده: «تأمُّلُ الميتا وبوذيةُ الإشراك».')
                note = ('  - "**صُحِّح الانتماء 2026-09-08:** كان `belongs_to` اسماً نصّياً '
                        f'«{name}» لا يُحلّ إلى ملفّ، وقد أُنشئت المدرسةُ `{tgt}` فأُسند '
                        'الانتماءُ إليها.' + extra + '"')
                stats[f"-> {tgt}"] += 1; act = f"-> {tgt}"
            else:
                t2 = t[:m.start()] + t[m.end():]
                t2 = re.sub(r'\n\n+', '\n', t2)
                if not re.search(r'^edges:\n- rel:', t2, re.M):
                    t2 = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t2, count=1, flags=re.M)
                note = ('  - "**فُرِّغ حقلُ الانتماء 2026-09-08:** كان `belongs_to` اسماً نصّياً '
                        f'«{name}» لا يُحلّ إلى ملفّ، **ولم تُنشأ له مدرسةٌ** لأنه ليس مدرسةً: '
                        + EMPTY[name] + '. فبقي الحقلُ فارغاً."')
                stats["فُرِّغ (ليست مدرسة)"] += 1; act = "(فُرِّغ)"
            t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
            print(f"{'APPLY' if apply else 'DRY'}  {slug:40} «{name[:26]}» {act}")
            if apply: open(p, "w", encoding="utf-8").write(t2)
    print("\n" + "="*54)
    for k, v in stats.most_common(): print(f"   {v:3}  {k}")
    print(f"   الإجمالي: {sum(stats.values())}")

if __name__ == "__main__":
    main()
