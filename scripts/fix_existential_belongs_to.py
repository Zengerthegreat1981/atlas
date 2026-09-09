"""
يصحّح حقلَ `belongs_to` في العقد التي تُصرِّح خطأً بانتمائها إلى مدرسةٍ وجودية.

## الخلل
355 عقدةً تقول `belongs_to: sch-existential-therapy` — و«الوجودية العلاجية»
مدرسةٌ **علاجيةٌ إكلينيكية**. والحقلُ مختومٌ ختماً قالبياً لا يوصف بيانات: فيه
**أوغسطينوس** (`active_start` = 397) و**سقراط** (−470) و**ريمون آرون** (عالمُ
اجتماع) و**هنري برغسون** و**إدموند هوسرل** — الذي يقول لِيدُ ملفِّه نفسِه «ليس
وجودياً». و**223 منها `part: philosophy`**، ومدخلٌ فلسفيٌّ لا ينتمي إلى مدرسةِ
علاجٍ نفسيّ.

وهذا **خللٌ بنيويٌّ في الرسم البياني** لا في العرض: `belongs_to` هو ما يُبنى
عليه انتماءُ العنصر إلى مدرسته، وعليه تقوم إحصاءاتُ الأعضاء وتصفّحُ المدارس.

## المصدر
الوسمُ الأولُ في `crumb` — وقد صُحِّح قبلَ هذا في ثلاث مراحل بمراجعةٍ اسميةٍ
يدويةٍ لـ223 ملفاً (انظر `EXISTENTIAL_CRUMB_FIX_2026-09-08.md`). فالخريطةُ أدناه
تترجم ذلك الوسمَ إلى **slug مدرسةٍ قائمةٍ في الأطلس**، وكلُّ هدفٍ فيها مُتحقَّقٌ
من وجوده.

## ثلاثُ قواعدَ حكمت العمل
1. **ما وسمُه وجوديٌّ يُترك** — سارتر وكيركغارد وكامو ويالوم وفرانكل: انتماؤهم
   صحيح. و«الفلسفة الوجودية» تُنقل إلى `sch-existentialism` (مدرسةُ الفلسفة) لا
   إلى `sch-existential-therapy` (مدرسةُ العلاج) — وهذا هو تصحيحُ الخلل الأصلي.
2. **ما لا مدرسةَ له في الأطلس يُفرَّغ حقلُه ويُسجَّل** — على اصطلاح المستودع
   («لا مدرسةَ أمّ في الأطلس تُنسب إليها: `edges` باقٍ فارغاً»). ولا تُختلق
   مدرسةٌ ولا يُوضَع أبٌ تقريبيّ: أبٌ خاطئٌ أسوأُ من غياب أب.
3. **الأوسامُ العامّةُ لا تُلمس** — «الفلسفة»، «المكتبة الفلسفية»، «المفاهيم
   الفلسفية الكبرى» وأمثالُها ليست حكماً على الانتماء، فقد يكون العنصرُ وجودياً
   بحقّ. لا يُغيَّر شيءٌ بغير سببٍ موجب.

    python3 scripts/fix_existential_belongs_to.py            # فحص
    python3 scripts/fix_existential_belongs_to.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXSCH = {"sch-existential-therapy", "sch-existentialism", "sch-existentialism-atheist",
         "sch-existentialism-religious", "sch-phenomenology-existential", "sch-kierkegaardian",
         "sch-black-existentialism", "sch-feminism-existential", "sch-judaism-existential"}

# الوسمُ الأول في crumb -> slug المدرسة، أو None لتفريغ الحقل مع تسجيل الفجوة
MAP = {
  # ── الفلسفة الوجودية: تُنقل إلى مدرسة الفلسفة لا مدرسة العلاج ──
  "الفلسفة الوجودية": "sch-existentialism",
  "الفلسفة الوجودية وعلم النفس": "sch-existentialism",
  "الفلسفة الوجودية وسيكولوجيا الأعماق": "sch-existentialism",
  "الفلسفة الوجودية وسيكولوجيا الحرية": "sch-existentialism",
  "الفلسفة الوجودية والأدب الروسي": "sch-existentialism",
  "الفلسفة الوجودية الفرنسية": "sch-existentialism",
  "الفلسفة الوجودية الدينية": "sch-existentialism-religious",
  "الفلسفة السياسية والأخلاقية الوجودية": "sch-existentialism",
  "الفلسفة الأخلاقية والوجودية": "sch-existentialism",
  "الفلسفة العبثية والوجودية": "sch-existentialism",
  "الفلسفة النيتشوية والوجودية": "sch-existentialism",
  "الأنطولوجيا والميتافيزيقا الوجودية": "sch-existentialism",
  "أخلاقيات الشهادة والفلسفة الوجودية": "sch-existentialism",
  "فلسفة الصدمة والوجودية النقدية": "sch-existentialism",
  "فلسفة الزمان والوجودية": "sch-existentialism",
  "الإنسانية والوجودية": "sch-existentialism",
  "الأدب الوجودي والفلسفة السياسية": "sch-existentialism",
  "الأدب الوجودي وسيكولوجيا الأعماق": "sch-existentialism",
  "الفكر الروسي والأدب الوجودي": "sch-existentialism",
  "الوجودية": "sch-existentialism",
  "النسوية الفلسفية": "sch-feminism-existential",
  "الوجودية السوداء": "sch-black-existentialism",
  "الظاهراتية الوجودية": "sch-phenomenology-existential",
  "الفينومينولوجيا النفسية": "sch-phenomenology",
  # ── العلاج الوجودي: صحيحٌ كما هو ──
  "العلاج النفسي الوجودي": "sch-existential-therapy",
  "العلاج النفسي الوجودي والفينومينولوجيا": "sch-existential-therapy",
  "العلاج بالمعنى والوجودية": "br-logotherapy",
  "العلاج بالمعنى (اللوغوثيراپيا)": "br-logotherapy",
  "اللاهوت الوجودي": "sch-existentialism-religious",
  # ── مدارسُ أخرى قائمةٌ في الأطلس ──
  "علم النفس الإنساني": "sch-humanistic",
  "الإنسانية": "sch-humanistic",
  "التحليل النفسي": "sch-psychoanalysis",
  "التحليل النفسي العلائقي": "br-relational-psychoanalysis",
  "الظاهراتية": "sch-phenomenology",
  "التأويليات": "sch-hermeneutics",
  "التأويليات وعلوم الروح": "sch-hermeneutics",
  "علم النفس الاجتماعي": "sch-social-psychology",
  "النظرية النقدية": "sch-frankfurt-school",
  "فلسفة التكنولوجيا": "sch-philosophy-of-technology",
  "مدرسة كيوتو": "sch-kyoto",
  "الفلسفة اليابانية": None,   # كيمورا طبيبٌ نفسيٌّ ظاهراتيٌّ متأثِّرٌ بنيشيدا، لا عضوٌ في مدرسة كيوتو
  "التشاؤمية الفلسفية": "sch-pessimism",
  "البراغماتية": "sch-pragmatism-classical",
  "الفلسفة السياسية المعاصرة": None,   # آرندت وتشارلز تايلور ليسا رولزيَّين
  "التجاوزية الأمريكية": "sch-transcendentalism",
  "علاج الجشطالت": "sch-gestalt-therapy",
  "الرواقية": "sch-stoicism",
  "فلسفة التنوير": "sch-enlightenment",
  "مناهضة الطب النفسي": "br-antipsychiatry",
  "الآبائية اللاتينية": "sch-patristics",
  "الأفلاطونية المحدثة": "sch-neoplatonism",
  "الهيغلية": "sch-hegelianism",
  "النيتشوية": "sch-nietzscheanism",
  "الفلسفة النيتشوية وتاريخ المفاهيم": "sch-nietzscheanism",
  "الميتافيزيقا النيتشوية وفلسفة الحياة": "sch-nietzscheanism",
  "المثالية الألمانية": "sch-german-idealism",
  "الرومانسية الألمانية": "sch-romanticism",
  "فلسفة الحياة": "sch-lebensphilosophie",
  "الشخصانية": "sch-personalism-contemporary",
  "الزنوجة ومناهضة الاستعمار": "sch-negritude",
  "علم نفس التحرر": "sch-liberation-psychology",
  "علم النفس عبر الشخصي": "sch-transpersonal",
  "الفلسفة الدينية": "sch-philosophy-of-religion",
  "الفلسفة التحليلية": "sch-phil-mind-analytic",
  "الفلسفة اليهودية": "sch-judaism-existential",
  "البوذية الزن": "sch-zen-rinzai",
  "البنائية في العلاج النفسي": "br-constructivist-cognitive",
  "العلاج الأسري النسقي": "sch-systemic-family",
  "الروحانية المسيحية": None,   # ميرتون راهبٌ في القرن العشرين، و«التصوّف المسيحي الوسيط» ليس مدرستَه
  "الفكر العربي الحديث": None,   # الوسمُ يجمع النهضةَ (طه حسين) والماركسيين (مروة، طرابيشي، العالم) والوضعيَّ المنطقي (زكي نجيب) — فلا مدرسةَ واحدةً تصلح
  "الفلسفة الإسلامية الحديثة": None,   # إقبال (ت. 1938) سابقٌ لـ«الفكر الإسلامي النقدي المعاصر»
  # ── لا مدرسةَ لها في الأطلس: يُفرَّغ الحقل وتُسجَّل الفجوة ──
  "الطب النفسي الظاهراتي": None,
  "مناهج البحث الظاهراتي": None,
  "مناهج البحث النوعي": None,
  "علم نفس الانفعال": None,
  "تاريخ الطب النفسي": None,
  "تاريخ الطب": None,
  "تاريخ علم النفس": None,
  "التاريخ النفسي": None,
  "الأدب والفكر اللاتيني الأمريكي": None,
  "الأدب العربي الحديث": None,
  "الأدب الأمريكي الأفريقي": None,
  "الفلسفة الفرنسية المعاصرة": None,
  "الفلسفة الفرنسية الحديثة": None,
  "الفلسفة الفرنسية في القرن التاسع عشر": None,
  "الفلسفة اليونانية القديمة": None,
  "الفلسفة الأخلاقية": None,
  "الأنطولوجيا الواقعية": None,
  "الفردانية الأنانية": None,
  "اللاهوت البروتستانتي": None,
  "علم دراسة الانتحار": None,
  "علم النفس الإكلينيكي": None,
  "علم النفس الإكلينيكي وعلاج الصدمات": None,
  "علم نفس الصدمة والتعافي": None,
  "سيكولوجيا الفقد والحداد المعاصر": None,
  "القياس النفسي والتشخيص": None,
  "الطب النفسي والتشخيص": None,
  "التكامل في العلاج النفسي": None,
  "أبحاث فعالية العلاج النفسي": None,
  "علم الاجتماع والفلسفة السياسية": None,
  "الفلسفة السياسية وأدب المعارضة": None,
  "الفلسفة السياسية وأدب المعسكرات": None,
  "التاريخ السياسي الأوروبي والحركات المناهضة للفاشية": None,
  "السيميائيات وعلوم الحاسوب": None,
  "فلسفة الشهادة وأخلاقيات الصدمة": None,
  "فلسفة الصدمة والشهادة الأخلاقية": None,
  "علم النفس": None,
}
# نقضٌ بالـslug يسبق الخريطةَ ووسمَ «لا تُلمس» — حالاتٌ مفردةٌ راجعتُها بعينها
SLUG_OVERRIDE = {
  # عناصرُ وسمُها عامٌّ لكنّ انتماءها المُصرَّحَ به خاطئٌ قطعاً
  "thk-james": ("sch-pragmatism-classical", "وليم جيمس براغماتيٌّ ووظيفي، لا معالِجاً وجودياً"),
  "wrk-twilight-of-the-idols-nietzsche": ("sch-nietzscheanism", "«أفول الأصنام» نصُّ نيتشه، لا نصَّ مدرسةِ علاج"),
  "thk-mbuber": ("sch-judaism-existential", "بوبر من الفلسفة اليهودية الحوارية، وللأطلس ملفُّها"),
  "thk-bachelard": ("sch-phenomenology", "باشلار ظاهراتيُّ الخيال وفيلسوفُ علم، لا ظاهراتياً وجودياً"),
  # مدارسُ نِدٌّ أُدرِجت خطأً أعضاءً في الوجودية. والوجوديةُ نشأت **على** الظاهراتية
  # لا العكس، والهرمنيوطيقا والبنيوية وما بعدها مدارسُ مستقلّةٌ عنها.
  # ويبقى ما هو فرعٌ حقيقيٌّ كما هو: الملحدة، والدينية، والعبثية.
  "sch-phenomenology":              (None, "الظاهراتيةُ أصلُ الوجودية لا فرعُها"),
  "sch-hermeneutics":               (None, "الهرمنيوطيقا مدرسةٌ مستقلّة"),
  "sch-structuralism":              (None, "البنيوية مدرسةٌ مستقلّة، وخصمٌ للوجودية تاريخياً"),
  "sch-post-structuralism":         (None, "ما بعد البنيوية مدرسةٌ مستقلّة"),
  "sch-postmodernism-philosophical":(None, "ما بعد الحداثة مدرسةٌ مستقلّة"),
  "sch-speculative-realism":        (None, "الواقعية المضاربة مدرسةٌ مستقلّةٌ معاصرة"),
  "sch-new-materialism":            (None, "المادية الجديدة مدرسةٌ مستقلّةٌ معاصرة"),
  "sch-western-marxism":            (None, "الماركسية الغربية مدرسةٌ مستقلّة"),
  "sch-personalism-contemporary":   (None, "الشخصانيةُ تأثّرت بالوجودية ولم تكن فرعاً منها"),
}

# أوسامٌ عامّةٌ لا تُلمس (ليست حكماً على الانتماء)
UNTOUCHED = {"الفلسفة", "المكتبة الفلسفية", "المفاهيم الفلسفية الكبرى", "المباحث الفلسفية الكبرى",
             "الفلسفة النقدية", "الفلسفة القارية", "الفلسفة والميتافيزيقا",
             "الجسر (فلسفة ↔ علم نفس)"}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    bad_targets = [v for v in MAP.values() if v and v not in d]
    if bad_targets:
        print("!! أهدافٌ غير موجودة:", bad_targets); return
    stats = collections.Counter(); unknown = collections.Counter(); missing_schools = collections.Counter()
    for slug in sorted(d):
        n = d[slug]
        bt = [e for e in n.get("edges", []) if e[0] == "belongs_to" and e[1] in EXSCH]
        if not bt: continue
        cur = bt[0][1]
        lab = (n.get("crumb") or "").split("←")[0].strip()
        if slug in SLUG_OVERRIDE:
            new, ovwhy = SLUG_OVERRIDE[slug]; lab = lab + " / " + ovwhy
        elif lab in UNTOUCHED: stats["تُرك (وسمٌ عامّ)"] += 1; continue
        elif lab not in MAP: unknown[lab] += 1; stats["تُرك (وسمٌ غير مُصنَّف)"] += 1; continue
        else: new = MAP[lab]
        if new == cur: stats["صحيحٌ كما هو"] += 1; continue
        p = find_file(slug)
        if not p: print("!! not found", slug); continue
        t = open(p, encoding="utf-8").read()
        line = re.search(r'^- rel: "belongs_to", target: "' + re.escape(cur) + r'".*$', t, re.M)
        if not line: stats["تعذّر (شكلٌ غير متوقَّع)"] += 1; continue
        if new:
            newline = f'- rel: "belongs_to", target: "{new}", target_type: "{d[new].get("type")}"'
            t2 = t[:line.start()] + newline + t[line.end():]
            note = ('  - "**صُحِّح الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    f'`{cur}` ختماً قالبياً، ونُقل إلى `{new}` بحسب المجال المُصحَّح في '
                    'مسار التنقّل («' + lab + '»). '
                    + ('ومدخلٌ فلسفيٌّ لا ينتمي إلى مدرسةِ علاجٍ نفسيٍّ إكلينيكي."'
                       if cur == "sch-existential-therapy" and new == "sch-existentialism"
                       else 'ولم يُشتقَّ من الحقل السابق لأنه كان مختوماً آلياً."'))
            stats[f"نُقل -> {new}"] += 1
            act = f"-> {new}"
        else:
            # حذفُ السطر؛ وإن خلا edges تماماً كُتب edges: []
            t2 = t[:line.start()] + t[line.end():]
            t2 = re.sub(r'\n\n+', '\n', t2)
            if not re.search(r'^edges:\n- rel:', t2, re.M):
                t2 = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t2, count=1, flags=re.M)
            note = ('  - "**فُرِّغ حقلُ الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    f'`{cur}` ختماً قالبياً، ولا صلةَ لهذا الملفّ بالوجودية — مجالُه «'
                    + lab + '». و**لا مدرسةَ لهذا المجال في الأطلس** تُنسب إليه، '
                    'فبقي الحقلُ فارغاً على اصطلاح المستودع؛ ولم يُوضَع أبٌ تقريبيٌّ '
                    'لأنّ أباً خاطئاً أسوأُ من غياب أب."')
            missing_schools[lab] += 1
            stats["فُرِّغ (لا مدرسة)"] += 1
            act = "-> (فُرِّغ)"
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        print(f"{'APPLY' if apply else 'DRY'}  {slug:44} [{lab[:26]}] {act}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    print("\n" + "="*60)
    for k, v in stats.most_common(): print(f"   {v:4}  {k}")
    if unknown:
        print(f"\nأوسامٌ لم تُصنَّف ({len(unknown)}) — تُركت بلا تغيير:")
        for k, v in unknown.most_common(): print(f"   {v:4}  {k}")
    if missing_schools:
        print(f"\nمجالاتٌ لا مدرسةَ لها في الأطلس ({len(missing_schools)}) — تستحقّ إنشاءً:")
        for k, v in missing_schools.most_common(): print(f"   {v:4}  {k}")

if __name__ == "__main__":
    main()
