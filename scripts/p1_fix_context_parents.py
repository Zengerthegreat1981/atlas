"""
المرحلة 1.2 — تصحيحُ أنساب السياقات التاريخية (`ctx-`).

القاعدةُ التحريرية المُعلَنة: السياقُ التاريخيُّ **ينتمي** (`belongs_to`) إلى
مدرسةٍ في حالتين فقط:
  (أ) أنّ السياقَ هو موضعُ نشأتها أو حاضنُها — «الستوا» للرواقية، «باريس
      والسوربون» للسكولاستية، «مانشستر الصناعية» للماركسية، «تافيستوك»
      للتحليل النفسي.
  (ب) أنّ المدرسةَ تُنشئ نفسَها صراحةً استعادةً لتقليدٍ سابق، فتكون سياقاتُ
      ذلك التقليد داخلَها — علمُ النفس الإسلامي (المدينة، دمشق، جنديسابور،
      الأزهر)، والبوذي (اليابان الإقطاعية)، والكونفوشي (الدول المتحاربة)،
      والأفريقي. فهذه لا تُمسّ وإن باعد الزمنُ بينها.

وما عدا ذلك — صلةٌ حقيقيةٌ لكنها ليست عضوية — يُحوَّل إلى `relates_to`: يبقى
الرابطُ والقصدُ التحريريُّ، ويسقط الادّعاءُ الهيكليُّ الخاطئ.

وأخطرُ ما وُجد **خطأُ تجانسٍ لفظي**: «الإنسانية» تُترجم both الإنسانيةَ
النهضوية (القرن 15) وعلمَ النفس الإنساني (1954). فوقعت أربعةُ سياقاتٍ نهضويةٍ
تحت مدرسةٍ نفسيةٍ أمريكيةٍ من الخمسينيات — منها أكاديميةُ فيتشينو الأفلاطونية
في كاريجي (1462) وهي بعينها موضعُ **الأفلاطونية المحدثة النهضوية**.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

# (أ) نسبٌ يُعاد توجيهُه إلى الأب الصحيح الموجود
REPOINT = {
    # خطأُ التجانس اللفظي: الإنسانيةُ النهضوية ≠ علمُ النفس الإنساني (1954)
    "ctx-florence-platonic-academy-medici": ("sch-humanistic", "sch-renaissance-neoplatonism",
        "أكاديميةُ فيتشينو في كاريجي (1462) بتكليف كوزيمو دي ميديتشي هي موضعُ الأفلاطونية "
        "المحدثة النهضوية بعينها، لا علمَ النفس الإنساني الأمريكيَّ (1954)"),
    "ctx-reformation-printing-press-europe": ("sch-humanistic", "sch-renaissance-humanism",
        "الإصلاحُ البروتستانتي والمطبعة (1517) سياقٌ للإنسانية النهضوية، لا لعلم النفس الإنساني (1954)"),
    "ctx-byzantine-constantinople-preservation": ("sch-humanistic", "sch-renaissance-humanism",
        "حفظُ القسطنطينية للمخطوطات اليونانية (330–1453) وهجرةُ علمائها إلى إيطاليا هو "
        "السياقُ المباشرُ للإنسانية النهضوية، لا لعلم النفس الإنساني (1954)"),
    "ctx-ancient-egypt-maat-cosmic-order": ("sch-humanistic", "sch-egyptian-maat",
        "ماعت المصريةُ القديمة موضعُها تقليدُ الحكمة المصرية الموجودُ في الأطلس، لا علمَ النفس الإنساني"),
    # أبٌ أدقُّ صار متاحاً
    "ctx-anthropocene-climate-crisis-grief": ("sch-humanistic", "sch-ecopsychology",
        "الحزنُ المناخيُّ والأنثروبوسين موضعُهما علمُ النفس الإيكولوجي، وهو أدقُّ من علم النفس الإنساني"),
    "ctx-algerian-revolution-fanon-anti-colonialism": ("sch-social-psychology", "sch-liberation-psychology",
        "الثورةُ الجزائرية وفانون أصلُ علم نفس التحرر لا علمِ النفس الاجتماعي التجريبي"),
    "ctx-haitian-revolution-black-jacobins": ("sch-social-psychology", "sch-postcolonial-philosophy",
        "الثورةُ الهايتية سياقٌ لفلسفة ما بعد الاستعمار لا لعلم النفس الاجتماعي"),
    "ctx-decolonization-bandung-nonaligned": ("sch-social-psychology", "sch-postcolonial-philosophy",
        "موجةُ التحرر وباندونغ سياقٌ لفلسفة ما بعد الاستعمار لا لعلم النفس الاجتماعي"),
    "ctx-dutch-golden-age-toleration": ("sch-british-empiricism", "sch-spinozism",
        "العصرُ الذهبيُّ الهولنديُّ وأمستردام سياقُ السبينوزية — وهو سياقٌ هولنديٌّ لا بريطاني"),
    "ctx-victorian-britain-morality-crisis": ("sch-british-empiricism", "sch-utilitarianism",
        "بريطانيا الفيكتورية (1837–1901) لاحقةٌ على التجريبية البريطانية (انتهت 1800)؛ "
        "والنفعيةُ (1789–1900) هي المعاصرةُ لها"),
    "ctx-french-revolution-terror-rights": ("sch-contractualism", "sch-social-contract",
        "الثورةُ الفرنسية (1789) سياقُ العقد الاجتماعي (1640–1900) لا التعاقدية الرولزية (1971)"),
}

# (ب) صلةٌ قائمةٌ لكنها ليست عضوية → relates_to
DEMOTE = {
    "ctx-ancient-sparta-discipline": "إسبرطةُ ليست جزءاً من الأكاديمية الأفلاطونية وإن أُعجب بها أفلاطون",
    "ctx-mesopotamia-code-of-hammurabi": "شريعةُ حمورابي (نحو 1750 ق.م) لا تنتمي إلى التعاقدية الأخلاقية المعاصرة (1971)",
    "ctx-nuremberg-trials-crimes-humanity": "محاكماتُ نورمبرغ (1945) سابقةٌ على التعاقدية (1971) فليست داخلَها",
    "ctx-fall-of-berlin-wall-1989": "سقوطُ الجدار حدثٌ سياسيٌّ لا يُنتظمه مبحثُ التعاقدية الأخلاقية",
    "ctx-oxford-franciscan-experimentalism": "التجريبيةُ الفرنسيسكانية الأوكسفوردية (القرن 13) سابقةٌ على "
        "فلسفة العلم كحقلٍ (1920)؛ صلةُ استباقٍ لا عضوية",
    "ctx-silicon-valley-techno-utopianism": "يوتوبيا الوادي سياقٌ تقنيٌّ-اقتصاديٌّ لا مبحثٌ في فلسفة العلم",
    "ctx-dot-com-bubble-internet-revolution": "فقاعةُ الدوت-كوم سياقٌ اقتصاديٌّ لا يُنتظمه مبحثُ فلسفة العقل التحليلية",
    "ctx-covid19-pandemic-global-lockdown": "الجائحةُ سياقٌ عامٌّ لا عضوٌ في علم النفس البيولوجي والعصبي",
    "ctx-american-transcendentalism-concord": "التعالويةُ (1836) سلفٌ فكريٌّ معترَفٌ به لعلم النفس الإنساني (1954) "
        "لا عضوٌ فيه — إمرسون سابقٌ على ماسلو بقرن",
    "ctx-belle-epoque-technology-alienation": "الحقبةُ الجميلة (1871) سياقٌ عامٌّ لا عضوٌ في علم النفس الإنساني (1954)",
    "ctx-post-war-welfare-state-europe": "دولةُ الرعاية سياقٌ سياسيٌّ-اقتصاديٌّ لا عضوٌ في علم النفس الإنساني",
    "ctx-me-too-movement-gender-accountability": "حركةُ مي-تو (2017) لا تنتمي إلى النسوية الليبرالية (1792) بعينها",
    "ctx-early-zionism-colonial-palestine": "الصهيونيةُ المبكرة سياقٌ سياسيٌّ-استعماريٌّ لا عضوٌ في علم النفس الاجتماعي",
}

STAMP = "**صُحِّح نسبُ السياق 2026-09-10:** "


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    n_rep = n_dem = 0
    for slug, (old, new, why) in REPOINT.items():
        assert new in d, new
        p, t = E.load(slug)
        t2 = E.replace_edge_target(t, old, new, d[new]["type"])
        if t2 is None:
            print("  ⚠️  لم يتغيّر:", slug); continue
        t2 = E.add_gap(t2, STAMP + f"كان أبوه `{old}` وصُحِّح إلى `{new}` — " + why + ".") or t2
        E.save(p, t2); n_rep += 1
    for slug, why in DEMOTE.items():
        par = [e[1] for e in d[slug]["edges"] if e[0] == "belongs_to"]
        if not par:
            print("  ⚠️  بلا أبٍ أصلاً:", slug); continue
        p, t = E.load(slug)
        t2 = E.replace_edge_rel(t, par[0], "relates_to")
        if t2 is None:
            print("  ⚠️  لم يتغيّر:", slug); continue
        t2 = E.add_gap(t2, STAMP + f"حُوِّل `belongs_to` إلى `relates_to` نحو `{par[0]}` — " + why
                       + ". الرابطُ باقٍ والقصدُ التحريريُّ محفوظ؛ الساقطُ هو ادّعاءُ العضوية.") or t2
        E.save(p, t2); n_dem += 1
    print(f"أُعيد توجيهُ نسبِ {n_rep} سياقاً · حُوِّل {n_dem} إلى relates_to")
    print("أُبقيت بقصدٍ سياقاتُ المدارس الاستعادية (الإسلامي، البوذي، الكونفوشي، الأفريقي) وإن باعد الزمن.")


if __name__ == "__main__":
    main()
