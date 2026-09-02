# Task 11.6
الحالة: مكتمل
العملية: debates/ — تسمية الطرفين الحقيقيين بالاسم والنص والسنة (10 subagents متوازية، 5 منهم أُعيد تشغيلهم بعد rate limit جلسة) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.6): صفر مخالفات آلية (30/30 ملف)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء الـ18 على الملفات الـ30): صفر تطابق

## ملاحظة تشغيلية
5 من 10 subagents في هذه الدفعة فشلوا بسبب rate limit في جلسة العمل (وليس مشكلة بالملفات)، وأُعيد تشغيلهم بنجاح بعد إعادة التشغيل — كل واحد فحص الحالة الحالية للملفات أولاً (بعضها كان مكتملاً جزئياً من المحاولة الأولى) قبل الإكمال.

## ✅ حل تداخل معلَّق من 11.5
`dbt-heinz-dilemma-kohlberg-gilligan.md` (كان قالبياً بالكامل) أُعيد كتابته بزاوية مستقلة فعلية (مثال معضلة هاينز التفصيلي: "إيمي" مقابل "جيك") مع إحالة صريحة إلى `dbt-care-ethics-vs-justice-ethics` (11.5، النظرية العامة) — التداخل المسجَّل سابقاً محسوم الآن بتمايز تحريري واضح، لا دمج.

## تحقق من عدم ازدواج — عدة عناقيد متشابهة الاسم فُحصت وتأكد استقلالها
- **ثلاثية الأدلة/الممارسة**: dbt-evidence-based-practice-clinical-decision-making / dbt-evidence-based-vs-practice-based-evidence / dbt-evidence — الثلاثة فُحصت وتأكد لكل واحد زاوية مستقلة (ساكيت العام، مارغيسون/باركهام-ميلور-كلارك ضد EBP تحديداً، بقاء المدرسة الوجودية تحديداً) — تداخل محتمل مسجَّل في gaps بدون دمج (يحتاج مراجعة بشرية).
- **رباعية الإرادة الحرة**: dbt-free-will-compatibilism-vs-hard-determinism / dbt-free-will-libertarianism-metaphysical-vs-compatibilist / dbt-free-will-vs-determinism / dbt-freewill-neuroscience-libet — الأربعة فُحصت وتأكدت زاوية مستقلة فعلية لكل واحد (توافقية/لاتوافقية صارمة، السؤال الميتافيزيقي الأسبق، الإطار الكلاسيكي التاريخي، تجارب ليبِت العصبية تحديداً) — لا دمج.
- dbt-husn-qubh-rational-ethics-kalam / dbt-divine-command-theory-vs-autonomous-ethics (11.5): تأكد الفرق (استمرار أصول الفقه المتأخر vs. الجدل الكلامي المؤسِّس) — موثَّق صراحة في gaps، لا دمج.

## قرارات محتوى بارزة
- dbt-embodied-cognition-vs-computationalism: صُحح `belongs_to` من `sch-cognitive-behavioral` غير المناسب إلى `sch-phil-mind-analytic`.
- dbt-foundationalism-vs-coherentism: كان قالبياً بالكامل — أُعيد حول تشيزوم (1966) ضد سيلرز (1956) وبونجور (1985).
- dbt-four-seven-debate-korean-confucianism: أُعيد حول الجولتين التاريخيتين الحقيقيتين (يي هوانغ/كي دايسونغ 1559–1566، يي إي/سونغ هون 1572) بدل خلط عام بينهما.
- dbt-human-nature-debate: حُذف رابط `dbt-nature-nurture-gene-environment-interaction` غير المبرر (جدل غربي مختلف تماماً) بدل تركه.
- dbt-evolutionary-psychology-adaptation-vs-spandrel: عُمِّق من 4 أسطر هزيلة لتوثيق كامل (كوزميدس/توبي/باس 1992/1989 ضد غولد/لوونتين 1979).

صفر slugs مخترعة. حالات غموض (تشمبلس، سلرز/تشيزوم كملفات مفكرين غير موجودة، مايك أوليفر من 11.5) سُجِّلت كفجوات.

## متوقف عنده (لرئيس التحرير)
- تداخل ثلاثية evidence-based لم يُحسم (3 ملفات، زوايا قريبة جداً) — يحتاج قرار دمج/إبقاء.
- الملفات الأخرى المتوقف عندها من 11.5 (dbt-diagnostic-concept-creep/dbt-concept-creep-psychiatry) لا تزال بانتظار قرار.

## الملفات
dbt-embodied-cognition-vs-computationalism, dbt-emdr-vs-cbt, dbt-empirically-validated-vs-evidence-based, dbt-epistemic-injustice-fricker, dbt-essentialism-vs-nominalism-gender, dbt-evidence-based-practice-clinical-decision-making, dbt-evidence-based-vs-practice-based-evidence, dbt-evidence, dbt-evolutionary-psychology-adaptation-vs-spandrel, dbt-existential-freedom-vs-structuralist-determinism, dbt-extended-mind-clark-chalmers, dbt-feminist-essentialism-vs-constructionism, dbt-feminist-universalism-vs-particularism, dbt-foundationalism-vs-coherentism, dbt-four-seven-debate-korean-confucianism, dbt-free-will-compatibilism-vs-hard-determinism, dbt-free-will-libertarianism-metaphysical-vs-compatibilist, dbt-free-will-vs-determinism, dbt-freewill-neuroscience-libet, dbt-gandhi-vs-machiavelli, dbt-general-factor-psychopathology-p, dbt-group-vs-individual-therapy, dbt-heinz-dilemma-kohlberg-gilligan, dbt-hindutva-vs-secularism-india, dbt-hitop-vs-dsm5-clinical-utility, dbt-hu-shi-vs-liang-shuming, dbt-human-nature-debate, dbt-human-rights-universalism-vs-cultural-relativism, dbt-humanistic-vs-existential, dbt-husn-qubh-rational-ethics-kalam
