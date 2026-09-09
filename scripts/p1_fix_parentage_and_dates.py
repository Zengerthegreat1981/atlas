"""
المرحلة 1.5 — تصحيحُ الأنساب الخاطئة وتواريخِ المدارس التي تُقصي أعضاءَها.

أربعُ عللٍ مختلفة:

**(أ) خطأُ تجانسٍ لفظيٍّ في «المدرسة الأكبرية».** الاسمُ يحمل معنيين: مدرسةُ
**الشيخ الأكبر** ابن عربي (ت 1240) — وهو المعنى الغالبُ في الفلسفة الإسلامية —
ومدرسةُ **الإمبراطور أكبر** المغولي (1542–1605) وتوفيقِه بين الأديان. وملفُّ
`sch-akbari` يصف الثاني في متنه صراحةً («نشأ في الهند المغولية… حول الإمبراطور
جلال الدين أكبر… الدين الإلهي»)، لكنّ أحدَ عشرَ عضواً أُلحقوا به وكلُّهم من
الأوّل: الفتوحاتُ المكية (1202) وفصوصُ الحكم (1229) والقونويُّ والجيليُّ
والأعيانُ الثابتة والخيالُ ووحدةُ الوجود. فتاريخُ الملفِّ صحيحٌ وأعضاؤه خطأ.
والموضعُ الصحيحُ قائمٌ في الأطلس: `sch-wahdat-alwujud` («العرفان النظري — وحدة
الوجود»، 1160–1400، «تأسّس على يد محيي الدين ابن عربي») وفرعُه
`br-irfan-nazari-akbari` الذي يسمّي القونويَّ والجيليَّ في متنه.

**(ب) واحدٌ وعشرون مفهوماً فلسفياً أباها ملفُّ علاقة.** كانت القصدية والكواليا
والدازاين وعالَمُ الحياة والبراكسيس تُعلن `belongs_to` نحو
`rel-phenomenology-existential-therapy` — وهو ملفُّ «علاقةٍ بين مدرستين» لا
مدرسة. فوُزِّعت على مدارسها الحقيقية، ولكلِّ إسنادٍ سببُه.

**(ج) تواريخُ مدارسَ تُقصي مؤسِّسَها أو امتدادَها الموثَّق.** تشان تبدأ 600
وبوديدارما 510؛ وفايشيشيكا −200 وكانادا −300؛ والحكمةُ المتعالية تنتهي 1700
وطباطبائي ومطهري من أعلامها. فوُسِّع النطاقُ لا نُقل العضو.

**(د) أنسابٌ خاطئةٌ بعينها.** إريجينا (845) تحت السكولاستية (1050)، والطوسي
(1230) تحت مدرسة أصفهان (1570)، وشلايرماخر ودلتاي تحت هرمنيوطيقا غادامير
(1960)، وغاليليو ونيوتن وروجر بيكون تحت فلسفة العلم كحقلٍ (1920). وما وُجد له
موضعٌ أدقُّ نُقل إليه، وما كان سلفاً لا عضواً حُوِّل إلى `relates_to`.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

# ── (أ) + (ب) + (د): إعادةُ توجيهِ الأب  slug -> (الأبُ القديم, الأبُ الجديد, السبب)
REPOINT = {
    # (أ) المدرسة الأكبرية — من إمبراطورِ الهند إلى الشيخ الأكبر
    "br-irfan-nazari-akbari": ("sch-akbari", "sch-wahdat-alwujud",
        "العرفانُ النظريُّ الأكبريُّ فرعُ مدرسةِ ابن عربي (وحدة الوجود)، لا مدرسةِ الإمبراطور أكبر المغولي"),
    "wrk-al-futuhat-al-makkiyya-ibn-arabi": ("sch-akbari", "sch-wahdat-alwujud",
        "الفتوحاتُ المكية (1202) لابن عربي، وموضعُها مدرستُه لا مدرسةَ الإمبراطور أكبر (1580)"),
    "wrk-fusus-al-hikam-ibn-arabi": ("sch-akbari", "sch-wahdat-alwujud",
        "فصوصُ الحكم (1229) لابن عربي، وموضعُها مدرستُه لا مدرسةَ الإمبراطور أكبر"),
    "wrk-insha-al-dawa-ir-ibn-arabi": ("sch-akbari", "sch-wahdat-alwujud",
        "إنشاءُ الدوائر (1201) لابن عربي، وموضعُها مدرستُه لا مدرسةَ الإمبراطور أكبر"),
    "con-wahdat-al-wujud-oneness-of-being": ("sch-akbari", "sch-wahdat-alwujud",
        "وحدةُ الوجود هي أطروحةُ المدرسة نفسِها التي تحمل اسمَها"),
    "con-ayan-thabita-archetypes": ("sch-akbari", "sch-wahdat-alwujud",
        "الأعيانُ الثابتة من صميم ميتافيزيقا ابن عربي"),
    "con-khayal-creative-imagination": ("sch-akbari", "sch-wahdat-alwujud",
        "الخيالُ الخلاق من صميم ميتافيزيقا ابن عربي"),
    "con-al-insan-al-kamil-concept": ("sch-akbari", "sch-wahdat-alwujud",
        "الإنسانُ الكامل من صميم ميتافيزيقا ابن عربي"),
    "thk-sadr-al-din-al-qunawi": ("sch-akbari", "br-irfan-nazari-akbari",
        "القونويُّ (ت 1274) أبرزُ شارحي ابن عربي، ومتنُ `br-irfan-nazari-akbari` يسمّيه صراحةً"),
    "thk-abd-al-karim-al-jili": ("sch-akbari", "br-irfan-nazari-akbari",
        "الجيليُّ (ت 1424) صاحبُ «الإنسان الكامل» من شرّاح الفصوص، ومتنُ الفرع يسمّيه صراحةً"),
    "wrk-al-insan-al-kamil-jili": ("sch-akbari", "br-irfan-nazari-akbari",
        "عملُ الجيلي موضعُه فرعُ العرفان النظري الأكبري مع مؤلِّفه"),
    # (ب) واحدٌ وعشرون مفهوماً كان أبوها ملفَّ علاقة
    "con-intentionality-brentano": ("rel-phenomenology-existential-therapy", "sch-phenomenology",
        "القصديةُ عند برنتانو (1874) الأساسُ الذي بنى عليه هوسرل الظاهراتية"),
    "con-conscious-acts": ("rel-phenomenology-existential-therapy", "sch-phenomenology",
        "أفعالُ الوعي من علم النفس الوصفي عند برنتانو، أصلِ الظاهراتية"),
    "con-phenomenology": ("rel-phenomenology-existential-therapy", "sch-phenomenology",
        "المفهومُ المؤسِّسُ للمدرسة نفسِها"),
    "con-lifeworld": ("rel-phenomenology-existential-therapy", "sch-phenomenology",
        "عالَمُ الحياة (Lebenswelt) من «أزمة العلوم» لهوسرل (1936)"),
    "con-time-consciousness": ("rel-phenomenology-existential-therapy", "sch-phenomenology",
        "وعيُ الزمن الداخليِّ من محاضرات هوسرل"),
    "con-dasein-being-there": ("rel-phenomenology-existential-therapy", "sch-phenomenology-existential",
        "الدازاين من «الوجود والزمان» (1927) — وهو عامُ تأسيسِ الظاهراتية الوجودية بعينه"),
    "con-facticity": ("rel-phenomenology-existential-therapy", "sch-phenomenology-existential",
        "الواقعانيةُ (Faktizität) مقولةٌ هيدغريةٌ-سارترية في الظاهراتية الوجودية"),
    "con-anguish-angst": ("rel-phenomenology-existential-therapy", "sch-kierkegaardian",
        "القلقُ (Angest) عنوانُ كتاب كيركغارد 1844 — وهو تاريخُ المفهوم نفسُه"),
    "con-body-schema": ("rel-phenomenology-existential-therapy", "sch-phenomenology-somatic",
        "مخطّطُ الجسد محورُ الظاهراتية الجسدية عند ميرلوبونتي"),
    "con-embodied-cognition": ("rel-phenomenology-existential-therapy", "sch-phenomenology-somatic",
        "المعرفةُ المتجسّدة الامتدادُ المعاصرُ للظاهراتية الجسدية"),
    "con-hermeneutics": ("rel-phenomenology-existential-therapy", "sch-hermeneutics",
        "علمُ التأويل موضعُه مدرستُه؛ ويُسجَّل أنّ المصطلحَ (1654) أقدمُ من الهرمنيوطيقا الفلسفية (1960)"),
    "con-fusion-horizons": ("rel-phenomenology-existential-therapy", "sch-hermeneutics",
        "انصهارُ الآفاق مقولةُ غادامير في «الحقيقة والمنهج» (1960) — عامُ تأسيس المدرسة"),
    "con-narrative-identity": ("rel-phenomenology-existential-therapy", "sch-hermeneutics",
        "الهويةُ السردية عند ريكور، من صميم الهرمنيوطيقا الفلسفية"),
    "con-qualia": ("rel-phenomenology-existential-therapy", "sch-phil-mind-analytic",
        "الكواليا مقولةٌ في فلسفة العقل التحليلية (جاكسون 1982) لا في العلاج الظاهراتي"),
    "con-praxis": ("rel-phenomenology-existential-therapy", "sch-marxism",
        "البراكسيس من «أطروحات عن فويرباخ» (1845) — مقولةٌ ماركسيةٌ لا ظاهراتية"),
    "con-emergence": ("rel-phenomenology-existential-therapy", "sch-phil-science",
        "النشوءُ (Emergence) مقولةٌ في فلسفة العلم ومبحثِ الاختزال"),
    "con-stream-of-consciousness": ("rel-phenomenology-existential-therapy", "sch-pragmatism-classical",
        "تيّارُ الوعي من «مبادئ علم النفس» لوليم جيمس (1890)، وجيمس من مؤسِّسي البراغماتية"),
    "con-world-hypotheses-pepper": ("rel-phenomenology-existential-therapy", "sch-pragmatism-classical",
        "فروضُ العالَم لستيفن بيبر (1942) في التقليد البراغماتي، وعليها بُنيت السياقيةُ الوظيفية"),
    "con-ipseity": ("rel-phenomenology-existential-therapy", "sch-phenomenological-psychiatry",
        "الإنّيةُ (Ipseity) واضطرابُها محورُ الطب النفسي الظاهراتي عند ساس وبارناس"),
    "con-psychophysics-fechner": ("rel-phenomenology-existential-therapy", "sch-biological-neuro",
        "الفيزياءُ النفسية عند فِخنر (1860) أصلُ القياس النفسي التجريبي"),
    "con-unconscious-inference": ("rel-phenomenology-existential-therapy", "sch-biological-neuro",
        "الاستدلالُ اللاواعي عند هلمهولتز (1867) من أصول علم النفس التجريبي"),
    # (د) أنسابٌ خاطئةٌ بعينها
    "br-functional-contextualism-rft": ("rel-act", "sch-act",
        "السياقيةُ الوظيفية ونظريةُ إطار العلاقات الأساسُ النظريُّ لـACT؛ وأبوها كان ملفَّ علاقةٍ لا مدرسة"),
    "con-adaptation": ("con-evolutionary-psychoanalysis", "sch-phil-science",
        "أبوها كان **مفهوماً** لا مدرسة، ومعكوساً زمنياً (التكيّفُ الدارويني 1859 والتحليلُ التطوري 1985)"),
    "wrk-grundlagen-psychischen-entwicklung": ("wrk-gestalt-psychology-kohler", "br-gestalt-berlin",
        "أبوها كان **عملاً** آخرَ لا مدرسة، ومعكوساً زمنياً (1921 تحت 1929)"),
    "thk-erigena": ("sch-scholasticism", "sch-apophatic",
        "إريجينا (ت 877) سابقٌ على السكولاستية (1050) بقرنين؛ وموضعُه اللاهوتُ السلبي (400–1400) "
        "فهو مترجمُ ديونيسيوس الأريوباغي وأبرزُ ممثّليه اللاتينيين"),
    "thk-nasir-tusi": ("sch-isfahan", "sch-islamic-peripatetic",
        "الطوسيُّ (1201–1274) سابقٌ على مدرسة أصفهان (1570) بثلاثة قرون؛ وموضعُه المشائيةُ "
        "الإسلامية (850–1400) لشرحه إشاراتِ ابن سينا"),
    "thk-schleiermacher": ("sch-hermeneutics", "sch-romanticism",
        "شلايرماخر (1768–1834) سابقٌ على هرمنيوطيقا غادامير (1960) بقرنٍ ونصف؛ وموضعُه الرومانسيةُ "
        "الفلسفية (1790–1850) وهي حقبتُه — وتبقى صلتُه بالهرمنيوطيقا حرفَ `relates_to` لأنه مؤسِّسُ تأويلِها الحديث"),
    "thk-dilthey": ("sch-hermeneutics", "sch-lebensphilosophie",
        "دلتاي (1833–1911) سابقٌ على هرمنيوطيقا غادامير (1960)؛ وموضعُه فلسفةُ الحياة "
        "(1870–1920) وهو من أعلامها — وتبقى صلتُه بالهرمنيوطيقا حرفَ `relates_to`"),
    "thk-bentham": ("sch-utilitarianism-contemporary", "sch-utilitarianism",
        "بنثام (1748–1832) مؤسِّسُ النفعية الكلاسيكية (1789–1900) لا عضوٌ في النفعية المعاصرة (1950)"),
}

# حروفُ `relates_to` تُضاف بعد نقل الأب، حفظاً للصلة الحقيقية
ADD_RELATES = [
    ("thk-schleiermacher", "sch-hermeneutics", "مدرسة"),
    ("thk-dilthey", "sch-hermeneutics", "مدرسة"),
    ("con-hermeneutics", "sch-phenomenology-hermeneutic", "مدرسة"),
]

# ── سلفٌ لا عضو: يُحوَّل belongs_to إلى relates_to
DEMOTE = {
    "thk-galileo-galilei": ("sch-phil-science",
        "غاليليو (1564–1642) سابقٌ على فلسفة العلم كحقلٍ أكاديميٍّ (1920) بثلاثة قرون: "
        "موضوعُ الحقلِ لا عضوٌ فيه"),
    "thk-isaac-newton": ("sch-phil-science",
        "نيوتن (1643–1727) سابقٌ على فلسفة العلم كحقل (1920): موضوعُ الحقلِ لا عضوٌ فيه"),
    "thk-roger-bacon": ("sch-phil-science",
        "روجر بيكون (1214–1294) سابقٌ على فلسفة العلم كحقل (1920) بسبعة قرون؛ وهو سلفٌ "
        "للمنهج التجريبي لا عضوٌ في الحقل"),
    "thk-saadia-gaon": ("sch-judaism-andalusian",
        "سعديا الفيومي (882–942) جاونُ سورا في بابل، لا فيلسوفاً أندلسياً — والأندلسيةُ "
        "(1000–1300) لاحقةٌ عليه؛ ولا مدرسةَ للعصر الجاوني في الأطلس"),
    "thk-sojourner-truth": ("sch-feminism-black",
        "سوجورنر تروث (1797–1883) سلفٌ للنسوية السوداء (1970) لا عضوٌ فيها — بينهما قرن"),
    "thk-dostoevsky": ("sch-existentialism",
        "دوستويفسكي (1821–1881) سلفٌ أدبيٌّ للوجودية (1930) لا عضوٌ في مدرستها الفلسفية"),
    "thk-wolfe": ("sch-somatic-experiencing",
        "ثيودور وولف (ت 1954) مترجمُ رايش إلى الإنجليزية، توفّي قبل تأسيس التجربة الجسدية (1990)"),
    "thk-lsaari": ("sch-indigenous-psychology",
        "ليفي-برول (1857–1939) سلفٌ أنثروبولوجيٌّ مُتنازعٌ عليه لعلم النفس الأهلي (1993) لا عضوٌ فيه"),
}

# ── (ج) توسيعُ نطاقِ مدارسَ تُقصي مؤسِّسَها أو امتدادَها
WIDEN = {
    "sch-chan": ("active_start", 520,
        "بوديدارما (نحو 470–543) مؤسِّسُ تشان في الرواية التقليدية وعضوٌ في المدرسة، ونشاطُه "
        "من 510 — فبدايةُ 600 كانت تُقصي مؤسِّسَها"),
    "sch-vaisheshika": ("active_start", -300,
        "كانادا مؤسِّسُ فايشيشيكا ونشاطُه من نحو 300 ق.م، فبدايةُ 200 ق.م كانت تُقصيه"),
    "sch-samkhya": ("active_start", -600,
        "كابيلا مؤسِّسُ سامخيا ونشاطُه من نحو 600 ق.م، والملفُّ نفسُه يسمّيها «أقدمَ المدارس "
        "الأرثوذكسية» — فبدايةُ 400 ق.م كانت تُقصي مؤسِّسَها"),
    "sch-zoroastrian-philosophy": ("active_start", -1200,
        "تاريخُ زرادشت متنازعٌ عليه بين نحو 1500 و600 ق.م، وملفّاه في الأطلس يؤرّخانه بـ1500 "
        "و1000 ق.م — فبدايةُ 600 ق.م كانت تُقصي مؤسِّسَها. واعتُمد 1200 ق.م حدّاً وسطاً، "
        "والخلافُ في التأريخ مُسجَّلٌ لا محسوم"),
    "sch-lixue": ("active_end", 1700,
        "وانغ فوزهي (1619–1692) من أعلام المدرسة، ونهايةُ 1300 كانت تُقصيه — واللِّيشيويه "
        "امتدّت إلى عهد تشينغ"),
    "sch-augustinianism": ("active_end", 1600,
        "الأوغسطينيةُ تقليدٌ امتدّ قروناً بعد أوغسطين (بونافنتورا وأنسلم والرهبانيةُ "
        "الأوغسطينية)، وكان النطاقُ 354–430 عمرَ أوغسطين نفسِه لا عمرَ مدرستِه"),
    "sch-transcendent-theosophy": ("active_end", "مستمر",
        "طباطبائي (1904–1981) ومطهري (1919–1979) من أعلام الحكمة المتعالية وأعضاءٌ فيها، "
        "ونهايةُ 1700 كانت تُقصيهما — والمدرسةُ حيّةٌ في حوزات قم"),
    "sch-islamic-reform": ("active_start", 1730,
        "شاه ولي الله الدهلوي (1703–1762) عضوٌ في المدرسة ويُوصَف قياسياً بمُقدِّمِ الإصلاح "
        "الإسلاميِّ الحديث، وبدايةُ 1820 كانت تُقصيه"),
}

# ── انشقاقٌ معكوسٌ بين مدرستين
FLIP = [("sch-shiraz", "belongs_to", "sch-isfahan", "sch-isfahan", "evolved_from", "sch-shiraz", "مدرسة",
         "معكوس: مدرسةُ شيراز (1250) أقدمُ من أصفهان (1570) وأصلٌ لها — فالملا صدرا تلميذُ "
         "تقليدِ الدشتكي والدواني الشيرازي. فحُذف نسبُ شيراز إلى أصفهان وأُثبت في اتجاهه الصحيح")]

DROP_PARENT = {
    "sch-wahdat-alshuhud": ("sch-salafism-modern",
        "وحدةُ الشهود عند أحمد السرهندي (ت 1624) تيّارٌ نقشبنديٌّ صوفيٌّ، لا فرعٌ من السلفية "
        "الحديثة (1925) اللاحقةِ عليه بثلاثة قرون؛ ومتنُه يصفه قراءةً مغايرةً لوحدة الوجود "
        "فأُثبتت الصلةُ بها حرفَ `relates_to`"),
}
ADD_RELATES += [("sch-wahdat-alshuhud", "sch-wahdat-alwujud", "مدرسة")]

STAMP = "**صُحِّح النسب/النطاق 2026-09-10:** "


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    c = dict(rep=0, dem=0, wid=0, add=0, flip=0, drop=0, missed=[])

    for slug, (old, new, why) in REPOINT.items():
        p, t = E.load(slug)
        t2 = E.replace_edge_target(t, old, new, d[new]["type"])
        if t2 is None:
            c["missed"].append(f"REPOINT {slug} {old}->{new}"); continue
        t2 = E.add_gap(t2, STAMP + f"كان أبوه `{old}` وصُحِّح إلى `{new}` — " + why + ".") or t2
        E.save(p, t2); c["rep"] += 1

    for slug, (par, why) in DEMOTE.items():
        p, t = E.load(slug)
        t2 = E.replace_edge_rel(t, par, "relates_to")
        if t2 is None:
            c["missed"].append(f"DEMOTE {slug} {par}"); continue
        t2 = E.add_gap(t2, STAMP + f"حُوِّل `belongs_to → {par}` إلى `relates_to` — " + why
                       + ". الصلةُ باقيةٌ والساقطُ ادّعاءُ العضوية.") or t2
        E.save(p, t2); c["dem"] += 1

    for slug, (field, val, why) in WIDEN.items():
        p, t = E.load(slug)
        old = d[slug].get(field)
        t2 = E.set_field(t, field, val, quote=isinstance(val, str))
        if t2 is None:
            c["missed"].append(f"WIDEN {slug} {field}"); continue
        t2 = E.add_gap(t2, STAMP + f"وُسِّع `{field}` من {old} إلى {val} — " + why + ".") or t2
        E.save(p, t2); c["wid"] += 1

    for slug, tgt, tt in ADD_RELATES:
        p, t = E.load(slug)
        t2 = E.add_edge(t, "relates_to", tgt, tt)
        if t2 is None:
            c["missed"].append(f"ADDREL {slug} {tgt}"); continue
        E.save(p, t2); c["add"] += 1

    for s1, r1, t1, s2, r2, t2_, tt, why in FLIP:
        p, t = E.load(s1)
        x = E.remove_edge(t, rel=r1, target=t1)
        if x is None:
            c["missed"].append(f"FLIP-DEL {s1}")
        else:
            x = E.add_gap(x, STAMP + f"حُذف `{r1} → {t1}` — " + why + ".") or x
            E.save(p, x); c["flip"] += 1
        p2, t2s = E.load(s2)
        y = E.add_edge(t2s, r2, t2_, tt)
        if y is None:
            c["missed"].append(f"FLIP-ADD {s2}")
        else:
            E.save(p2, y); c["flip"] += 1

    for slug, (par, why) in DROP_PARENT.items():
        p, t = E.load(slug)
        t2 = E.remove_edge(t, rel="belongs_to", target=par)
        if t2 is None:
            c["missed"].append(f"DROP {slug} {par}"); continue
        t2 = E.add_gap(t2, STAMP + f"حُذف `belongs_to → {par}` — " + why + ".") or t2
        E.save(p, t2); c["drop"] += 1

    print(f"أُعيد توجيهُ {c['rep']} أباً · حُوِّل {c['dem']} إلى relates_to · وُسِّع نطاقُ "
          f"{c['wid']} مدرسةً · أُضيف {c['add']} حرفَ صلة · عُكس {c['flip']} · حُذف {c['drop']}")
    if c["missed"]:
        print("⚠️  لم تُطبَّق:", *c["missed"], sep="\n     ")


if __name__ == "__main__":
    main()
