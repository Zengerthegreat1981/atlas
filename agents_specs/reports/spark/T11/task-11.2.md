# Task 11.2
الحالة: مكتمل
المسار: spark | العملية: events: event_date/event_place + إجابة صريحة على (ماذا/متى/أين/من حضر بالاسم/ماذا تغيّر/النص الناتج) | الملفات: 30

## الأرقام
event_date موجود: 0/30 → 30/30
## المصادر موجود: 2/30 (إضافة اختيارية من بعض الوكلاء، غير مطلوبة في نص المهمة)

## أمر التحقق
python3 scripts/task.py verify spark 11.2
→
=== تحقق Task 11.2 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 2 / 30
فيها الحقل event_date: 30 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **ملفات أُعيد كتابتها بالكامل** لكونها حشواً قالبياً فارغاً من الوقائع (بعضها يحمل جمل قائمة سوداء حرفية): evt-council-of-nicaea-325.md، evt-encyclopedie-publication-diderot-1751.md، evt-emdr-founding-1987.md، evt-einstein-relativity-papers-1905.md، evt-decolonization-wave-africa-1960.md، evt-end-of-ww1-league-of-nations-1919.md، evt-destruction-of-alexandria-library.md، evt-condemnations-of-1270-1277-paris.md، evt-council-of-chalcedon-451.md.
- **evt-drapetomania-cartwright-1851.md**: موضوع عنصري تاريخي حساس (تشخيص مزيف اخترعه كارترايت لتبرير العبودية) — عولج بدقة تاريخية نقدية واضحة لا بحياد زائف؛ صُحح مصدر النشر الفعلي (De Bow's Review).
- **evt-destruction-of-alexandria-library.md**: وُضِّح التعقيد التاريخي الحقيقي (تدمير تدريجي عبر 4 حلقات منفصلة عبر ~7 قرون، لا حدث واحد) بدل تبسيطه؛ رواية عمر بن الخطاب/عمرو بن العاص وُسمت صراحة كرواية متأخرة غير موثقة معاصرةً يعدّها أغلب المؤرخين أسطورة.
- **evt-dsm-homosexuality-removal-1973.md**: وُثِّق روبرت سبيتزر ونتيجة التصويت.
- **أحداث بلا مكان واحد**: evt-decolonization-wave-africa-1960.md (17 استقلالاً منفصلاً)، evt-destruction-of-alexandria-library.md — تُرك event_place/event_date عامّاً أو null مع توثيق السبب صراحة.
- تصحيحات active_end متعددة عبر الدفعة لحل مخالفة "سنة مذكورة بعد active_end بلا توضيح" — بتوسيع النطاق الزمني الحقيقي (evt-connecticut-licensing-law-1945 → 1977، evt-dsm-1-publication-1952 → "مستمر"، evt-emdr-founding-1987 → 2001، evt-encyclopedie-publication-diderot-1751 → 1772، evt-end-of-ww1-league-of-nations-1919 → 1946، evt-einstein-relativity-papers-1905 → 1921) بدل حذف الوقائع الحقيقية.
- لا اختراع أسماء حضور — حيث لم تُعرف الأسماء بثقة (مثل أعضاء لجنة DSM-II، حضور حفل نوبل مونيز 1949 الفعلي)، وُثِّق الغياب في gaps.
- تصحيحات preflight إضافية: عناوين related غير مطابقة، حذف روابط related غير مبرَّرة في المتن (evt-drapetomania-cartwright-1851.md).

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل. الفجوات المتبقية (تواريخ/أماكن غير مؤكدة، أسماء حضور غير موثقة) مسجّلة داخل gaps كل ملف.

## الملفات
content/ar/events/evt-condemnations-of-1270-1277-paris.md
content/ar/events/evt-connecticut-licensing-law-1945.md
content/ar/events/evt-council-of-chalcedon-451.md
content/ar/events/evt-council-of-nicaea-325.md
content/ar/events/evt-cyril-burt-twin-data-controversy-1976.md
content/ar/events/evt-darwin-origin-of-species-1859.md
content/ar/events/evt-davos-conference-cassirer-heidegger-1929.md
content/ar/events/evt-dbt-founding-1990s.md
content/ar/events/evt-death-of-hypatia-415.md
content/ar/events/evt-decolonization-wave-africa-1960.md
content/ar/events/evt-deinstitutionalization-movement-1960.md
content/ar/events/evt-destruction-of-alexandria-library.md
content/ar/events/evt-dgps-founding-1904.md
content/ar/events/evt-drapetomania-cartwright-1851.md
content/ar/events/evt-dsm-1-publication-1952.md
content/ar/events/evt-dsm-2-publication-1968.md
content/ar/events/evt-dsm-3-publication-1980.md
content/ar/events/evt-dsm-4-publication-1994.md
content/ar/events/evt-dsm-5-publication-2013.md
content/ar/events/evt-dsm-homosexuality-removal-1973.md
content/ar/events/evt-eabct-founding-1971.md
content/ar/events/evt-egaz-moniz-nobel-lobotomy-1949.md
content/ar/events/evt-egyptian-psychological-association-1948.md
content/ar/events/evt-einstein-relativity-papers-1905.md
content/ar/events/evt-emdr-founding-1987.md
content/ar/events/evt-encyclopedie-publication-diderot-1751.md
content/ar/events/evt-end-of-ww1-league-of-nations-1919.md
content/ar/events/evt-esalen-institute-founding-1962.md
content/ar/events/evt-europsy-standard-2001.md
content/ar/events/evt-excommunication-of-spinoza-1656.md
