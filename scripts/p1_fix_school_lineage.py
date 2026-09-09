"""
المرحلة 1.3/1.4 — تصحيحُ حروف النسب التاريخي بين المدارس.

فُحصت الـ657 حرفاً كلَّها، وتُركت الصحيحةُ (وهي الأكثر). والمعالَجُ هنا ثلاثةُ
أصناف:

  (1) **معكوسُ الاتجاه**: الحرفُ يقول إنّ المتقدِّمَ خرج من المتأخّر. أوضحُها
      أنّ الرواقيةَ (300 ق.م) «تطوّرت إلى» المشائية (335 ق.م)، وأنّ الأشعريةَ
      (900) «تجاوزتها» المعتزلة (720) — والحرفُ الصحيحُ مثبتٌ في ملفّ المعتزلة
      أصلاً، فالمعكوسُ تكرارٌ خاطئ.

  (2) **دفعةٌ مُختلقة**: ثلاثةُ حروفٍ تصبُّ في «الوجودية الدينية» (1944) من
      الرواقية والأبيقورية والأفلاطونية المحدثة — فجوةُ ألفي سنةٍ بلا سندٍ في
      أيِّ متن. وحلقةُ تجاوزٍ متبادلةٍ بين الميتافيزيقا التحليلية والواقعية
      العلمية (كلٌّ يتجاوز الآخر).

  (3) **تياراتٌ متعاصرةٌ حيّةٌ يُقال إنّ إحداها تجاوزت الأخرى**: أخلاقُ الفضيلة
      والنفعيةُ المعاصرة والكانطيةُ والتعاقدية — أربعتُها حيّةٌ متنازعةٌ اليوم،
      ولا واحدةَ منها «تجاوزت» غيرَها.

ومعها: هدفُ حرف النسب حيث لم يكن مدرسةً (سبعةُ حروف)، والإشارةُ الذاتية.

القاعدةُ المطبَّقة: لا يبقى حرفُ نسبٍ **معكوسٌ زمنياً** أو **لا يسنده متنُ
أحد الطرفين**. وما كان صحيحاً تاريخياً وإن لم يذكره المتنُ حرفياً — كالميليسية
إلى الإيلية، والهيغلية اليسارية إلى الماركسية — أُبقي.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

# (slug, rel, target) → سببُ الحذف
DELETE = {
    # ── دفعةٌ مُختلقةٌ تصبُّ في الوجودية الدينية (1944)
    ("sch-stoicism", "absorbed_by", "sch-existentialism-religious"):
        "فجوةُ ألفَي سنة، ولا يذكر متنُ أيٍّ من الطرفين استيعاباً — الرواقيةُ انقضت في القرن 3م",
    ("sch-neoplatonism", "absorbed_by", "sch-existentialism-religious"):
        "فجوةُ 1,400 سنة بلا سندٍ في المتن؛ الأفلاطونيةُ المحدثةُ انتقلت إلى الآبائية والإسلامية لا إلى وجودية القرن 20",
    ("sch-epicureanism", "superseded_by", "sch-existentialism-religious"):
        "فجوةُ 1,700 سنة بلا سند — والأبيقوريةُ لم تتجاوزها وجوديةٌ مسيحيةٌ حديثة",
    # ── معكوسُ الاتجاه زمنياً
    ("sch-stoicism", "evolved_into", "sch-aristotelianism"):
        "المشائيةُ (335 ق.م) أقدمُ من الرواقية (300 ق.م) فلا تكون ثمرةً لها",
    ("sch-ashariyya", "superseded_by", "sch-mutazila"):
        "معكوس: الأشعريةُ (900) هي التي تجاوزت المعتزلةَ (720)، والحرفُ الصحيحُ مثبتٌ في ملفّ المعتزلة",
    ("sch-comtian-positivism", "evolved_into", "sch-utilitarianism"):
        "النفعيةُ (1789) أقدمُ من الكومتية (1830)؛ وكومت وميل معاصران متأثّران متبادلاً لا سلفٌ وخلف",
    ("sch-experimental-philosophy", "superseded_by", "sch-quinean-naturalism"):
        "معكوس: الفلسفةُ التجريبية (2001) لاحقةٌ على الكواينية (1951)",
    ("sch-academic-skepticism", "evolved_into", "sch-academy-platonic"):
        "معكوس: الشكُّ الأكاديميُّ (265 ق.م) طورٌ داخل الأكاديمية (387 ق.م)، والحرفُ الصحيحُ مثبتٌ في ملفّ الأكاديمية",
    ("sch-scientific-realism", "superseded_by", "sch-analytic-metaphysics"):
        "نصفُ حلقةِ تجاوزٍ متبادلة: كلُّ ملفٍّ يقول إنّ الآخرَ تجاوزه — ولا أحدَ منهما تجاوز الآخر",
    ("sch-analytic-metaphysics", "superseded_by", "sch-scientific-realism"):
        "النصفُ الآخر من حلقة التجاوز المتبادلة؛ وهي مباحثُ متعاصرةٌ حيّةٌ لا متعاقبة",
    ("sch-feminism-marxist", "evolved_from", "sch-feminism-radical"):
        "معكوس: النسويةُ الماركسية (1884، إنجلز) أقدمُ من الراديكالية (1967)؛ ويبقى نسبُها إلى الماركسية",
    ("sch-new-materialism", "evolved_from", "sch-speculative-realism"):
        "معكوس: المادّيةُ الجديدة (1994) أقدمُ من الواقعية المضاربة (2007)",
    ("sch-pure-land", "evolved_from", "sch-tathagatagarbha"):
        "معكوس: الأرضُ الطاهرة (150) أقدمُ من تاثاغاتاغاربها (250)؛ ويبقى نسبُها إلى مادهياماكا",
    ("sch-tathagatagarbha", "evolved_from", "sch-yogacara"):
        "معكوس: تاثاغاتاغاربها (250) أقدمُ من يوغاكارا (350)؛ ويبقى نسبُها إلى مادهياماكا",
    ("sch-chan", "evolved_from", "sch-huayan"):
        "معكوس: تشان (600) أقدمُ من هوايان (660)؛ ويبقى نسبُها إلى تيانتاي وتاثاغاتاغاربها",
    ("sch-kokugaku", "split_into", "sch-mitogaku"):
        "معكوس: ميتوغاكو (1657) أقدمُ من كوكوغاكو (1728)",
    ("sch-german-idealism", "split_into", "sch-kant-critical"):
        "معكوس: الكانطيةُ النقدية (1781) سابقةٌ على المثالية الألمانية (1785) وأصلٌ لها لا فرعٌ منها "
        "— ويُضاف بدلَه حرفُ `evolved_from` في الاتجاه الصحيح",
    ("sch-biological-neuro", "evolved_from", "sch-developmental"):
        "معكوس وبلا سند: علمُ النفس البيولوجي (1879، فونت) أقدمُ من النمائي (1882) ولم يخرج منه",
    ("sch-social-psychology", "evolved_from", "sch-behaviorism"):
        "معكوس: علمُ النفس الاجتماعي (1908، مكدوغال وروس) أقدمُ من السلوكية (1913)",
    ("sch-virtue-ethics", "superseded_by", "sch-utilitarianism-contemporary"):
        "معكوس ومغلوطٌ معاً: أخلاقُ الفضيلة (1958، أنسكوم) نهضت **ضدّ** النفعية، ولا واحدةَ منهما تجاوزت الأخرى — وكلتاهما حيّة",
    # ── تياراتٌ متعاصرةٌ حيّةٌ لا متعاقبة
    ("sch-kantian-ethics-contemporary", "superseded_by", "sch-contractualism"):
        "التعاقديةُ (سكانلون) مشتقّةٌ من الكانطية لا متجاوزةٌ لها، وكلتاهما حيّةٌ اليوم",
    ("sch-utilitarianism-contemporary", "superseded_by", "sch-contractualism"):
        "النفعيةُ المعاصرة والتعاقديةُ خصمان متعاصران حيّان، لا سلفٌ وخلف",
    # ── نسبٌ بلا سندٍ تاريخي
    ("sch-british-idealism", "superseded_by", "sch-pragmatism-classical"):
        "المثاليةَ البريطانية تجاوزتها الفلسفةُ التحليلية في بريطانيا (مور ورَسل)، لا البراغماتيةُ الأمريكية",
    ("sch-hegel-right", "superseded_by", "sch-pragmatism-classical"):
        "لا صلةَ تاريخيةً بين الهيغلية اليمينية والبراغماتية الأمريكية",
    ("sch-atomism-greek", "superseded_by", "sch-aristotelianism"):
        "أرسطو نقد الذريةَ ولم يتجاوزها: استمرّت عند أبيقور — والحرفُ الصحيحُ (إلى الأبيقورية) مُبقًى",
    ("sch-eleatic", "superseded_by", "sch-academic-skepticism"):
        "فجوةُ 175 سنةً بلا تعاقب",
    ("sch-eleatic", "superseded_by", "sch-academy-platonic"):
        "أفلاطون استوعب بارمنيدس ولم «يتجاوز» الإيليةَ التي انقضت قبل تأسيس الأكاديمية",
    ("sch-pythagorean", "superseded_by", "sch-academy-platonic"):
        "الفيثاغوريةُ استُوعبت في الأفلاطونية واستمرّت فيثاغوريةً محدثة — والحرفُ الأدقُّ "
        "(evolved_into الأفلاطونية الوسطى) مُبقًى",
    ("sch-aristotelianism", "evolved_into", "sch-middle-platonism"):
        "الأفلاطونيةُ الوسطى ثمرةُ الأكاديمية لا المشائية — والحرفُ الصحيحُ مثبتٌ في ملفّ الأكاديمية",
    ("sch-aristotelianism", "evolved_into", "sch-neoplatonism"):
        "الأفلاطونيةُ المحدثة ثمرةُ الأفلاطونية (والحرفُ مثبتٌ من الأكاديمية والوسطى)؛ استيعابُها أرسطو ليس نسباً منه",
    ("sch-heraclitean", "evolved_into", "sch-academy-platonic"):
        "أثرُ هيراقليطس في أفلاطون (محاورة كراتيلوس) أثرٌ لا نسبٌ مؤسِّس — يتخطّى الحرفُ جيلين",
    ("sch-civic-republicanism", "evolved_from", "sch-enlightenment"):
        "الجمهوريةُ المدنية (1400) سابقةٌ على التنوير (1680)؛ ويبقى نسبُها إلى الإنسانية النهضوية",
    ("sch-deism", "evolved_from", "sch-enlightenment"):
        "الربوبيةُ (1620) سابقةٌ على التنوير (1680)؛ ويبقى نسبُها إلى الإنسانية النهضوية",
    ("sch-social-contract", "evolved_from", "sch-enlightenment"):
        "العقدُ الاجتماعي (1640، هوبز) سابقٌ على التنوير (1680)؛ ويبقى نسبُه إلى التجريبية البريطانية",
    ("sch-bon", "evolved_from", "sch-shramana"):
        "البون تقليدٌ تبتيٌّ سابقٌ للبوذية، لا فرعٌ من الشرامنية الهندية (600 ق.م) — والحرفُ معكوسٌ زمنياً أيضاً",
    ("sch-british-empiricism", "evolved_from", "br-scholasticism-second-salamanca"):
        "التجريبيةُ البريطانية خرجت من بيكون وهوبز، لا من مدرسة سلامنكا — ويبقى نسبُها إلى الإنسانية النهضوية "
        "(وأثرُ سواريز في ديكارت ولايبنتز موثَّقٌ فأُبقي هناك)",
    ("sch-existential-therapy", "evolved_from", "br-ego-psychology"):
        "العلاجُ الوجوديُّ (1930) سابقٌ على علم نفس الأنا (1937) ولم يخرج منه؛ ويبقى نسبُه إلى الوجودية والظاهراتية",
    ("sch-emdr", "evolved_from", "sch-behaviorism"):
        "EMDR نشأ من ملاحظة شابيرو وبراديغم التعرّض، ونسبُه المثبتُ إلى علم نفس الصدمة أدقُّ من السلوكية",
    ("sch-liberation-psychology", "evolved_from", "sch-psychoanalysis"):
        "مارتين-بارو خرج من علم النفس الاجتماعي ولاهوت التحرير وفريري، لا من التحليل النفسي",
    # ── إشارةٌ ذاتية
    ("sch-donghak", "evolved_into", "sch-donghak"):
        "إشارةٌ ذاتية: الملفُّ يُعلن أنه تطوّر إلى نفسِه",
}

# حروفٌ يُبدَّل نوعُ علاقتها (الهدفُ ليس مدرسةً فالنسبُ لا ينطبق)
RETYPE_REL = {
    ("br-logotherapy", "split_into", "thk-langle"): ("relates_to",
        "هدفُ الحرف **مفكّر** لا مدرسة: لانغله انشقّ عن اللوغوثيرابي وأسّس التحليلَ الوجودي، "
        "فالعلاقةُ صلةٌ لا انشقاقُ مدرسةٍ عن مدرسة"),
    ("br-nlp-systemic", "split_into", "tec-systemic-nlp-tad-james"): ("relates_to",
        "هدفُ الحرف **تقنية** لا مدرسة"),
    ("sch-transpersonal", "split_into", "tec-holotropic-breathwork"): ("relates_to",
        "التنفّسُ الهولوتروبي **تقنيةٌ** طوّرها غروف داخل المدرسة، لا مدرسةً انشقّت عنها"),
    ("sch-dbt", "evolved_from", "con-biosocial-dbt"): ("grounded_in",
        "النظريةُ البيولوجية-الاجتماعية **جزءٌ من** DBT لا سلفٌ خرج منه — فالحرفُ الصحيحُ تأسيسٌ لا نسب"),
}

# حروفٌ صحيحةُ المعنى وهدفُها مُصنَّفٌ خطأً في الأطلس: يُصحَّح target_type ويُسجَّل السبب
FIX_TYPE_ONLY = {
    ("sch-systemic-family", "split_into", "tec-structural-family-therapy"):
        "الانشقاقُ صحيحٌ تاريخياً (مينوتشين)، لكنّ الهدفَ مُصنَّفٌ في الأطلس «تقنية» ويستحقّ أن يكون تياراً (`br-`)",
    ("sch-systemic-family", "split_into", "tec-strategic-family-therapy"):
        "الانشقاقُ صحيحٌ تاريخياً (هيلي ومادانيس)، لكنّ الهدفَ مُصنَّفٌ «تقنية» ويستحقّ أن يكون تياراً (`br-`)",
    ("sch-behaviorism", "evolved_into", "con-applied-behavior-analysis"):
        "تحليلُ السلوك التطبيقي ثمرةُ السلوكية الراديكالية فعلاً، لكنه مُصنَّفٌ «مفهوم» ويستحقّ أن يكون تياراً (`br-`)",
}

# إعادةُ توجيهِ حرفٍ إلى ملفٍّ غيرِ مهجور
REPOINT = {
    ("sch-mbct", "evolved_from", "sch-cbt"): ("sch-cognitive-behavioral",
        "`sch-cbt` ملفُّ إحالةٍ مهجورٌ بعد دمجٍ سابق؛ والمدرسةُ الفعليةُ هي `sch-cognitive-behavioral`"),
}

ADD = [("sch-german-idealism", "evolved_from", "sch-kant-critical", "مدرسة")]
STAMP = "**صُحِّح حرفُ نسبٍ تاريخي 2026-09-10:** "


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    counts = dict(deleted=0, retyped=0, fixed_type=0, repointed=0, added=0, missed=[])

    for (s, rel, tgt), why in DELETE.items():
        p, t = E.load(s)
        t2 = E.remove_edge(t, rel=rel, target=tgt)
        if t2 is None:
            counts["missed"].append(f"DEL {s} {rel} {tgt}"); continue
        t2 = E.add_gap(t2, STAMP + f"حُذف `{rel} → {tgt}` — " + why + ".") or t2
        E.save(p, t2); counts["deleted"] += 1

    for (s, rel, tgt), (new_rel, why) in RETYPE_REL.items():
        p, t = E.load(s)
        t2 = E.replace_edge_rel(t, tgt, new_rel)
        if t2 is None:
            counts["missed"].append(f"RETYPE {s} {rel} {tgt}"); continue
        t2 = E.add_gap(t2, STAMP + f"حُوِّل `{rel} → {tgt}` إلى `{new_rel}` — " + why + ".") or t2
        E.save(p, t2); counts["retyped"] += 1

    for (s, rel, tgt), why in FIX_TYPE_ONLY.items():
        p, t = E.load(s)
        t2 = E.replace_edge_target(t, tgt, tgt, d[tgt]["type"])
        if t2 is None:
            counts["missed"].append(f"TYPE {s} {rel} {tgt}"); continue
        t2 = E.add_gap(t2, STAMP + f"صُحِّح `target_type` في `{rel} → {tgt}` إلى «{d[tgt]['type']}» — "
                       + why + ".") or t2
        E.save(p, t2); counts["fixed_type"] += 1

    for (s, rel, old), (new, why) in REPOINT.items():
        p, t = E.load(s)
        t2 = E.replace_edge_target(t, old, new, d[new]["type"])
        if t2 is None:
            counts["missed"].append(f"REPOINT {s} {rel} {old}"); continue
        t2 = E.add_gap(t2, STAMP + f"أُعيد توجيهُ `{rel}` من `{old}` إلى `{new}` — " + why + ".") or t2
        E.save(p, t2); counts["repointed"] += 1

    for s, rel, tgt, tt in ADD:
        p, t = E.load(s)
        t2 = E.add_edge(t, rel, tgt, tt)
        if t2 is None:
            counts["missed"].append(f"ADD {s} {rel} {tgt}"); continue
        E.save(p, t2); counts["added"] += 1

    print(f"حُذف {counts['deleted']} حرفاً · حُوِّل نوعُ {counts['retyped']} · صُحِّح نوعُ هدفِ "
          f"{counts['fixed_type']} · أُعيد توجيهُ {counts['repointed']} · أُضيف {counts['added']}")
    if counts["missed"]:
        print("⚠️  لم تُطبَّق:", *counts["missed"], sep="\n     ")


if __name__ == "__main__":
    main()
