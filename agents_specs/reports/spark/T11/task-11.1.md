# Task 11.1
الحالة: مكتمل
المسار: spark | العملية: events: event_date/event_place + إجابة صريحة على (ماذا/متى/أين/من حضر بالاسم/ماذا تغيّر/النص الناتج) | الملفات: 30

## الأرقام
event_date موجود: 0/30 → 30/30
event_place: أضيف بقيمة حقيقية حيث تتوفر، أو null موثق السبب في gaps حيث لا مكان واحد محدد (مثل الأحداث الممتدة زمنياً/جغرافياً: هزيمة 1967، تأسيس CBT).

## أمر التحقق
python3 scripts/task.py verify spark 11.1
→
=== تحقق Task 11.1 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30
فيها الحقل event_date: 30 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **evt-closing-of-athens-schools-justinian-529.md وevt-burning-of-averroes-books-cordoba-1195.md وevt-burning-of-giordano-bruno-1600.md وevt-ai-breakthrough-deep-learning-2012.md**: كانت تحتوي محتوى قالبياً فارغاً من الوقائع (بما فيه جمل قائمة سوداء حرفية مثل "شكل هذا الحدث منعطفاً حاسماً"). أُعيدت كتابتها بالكامل بوقائع حقيقية موثقة (أسماء، تواريخ، نتائج) بدل الحشو العام.
- **أحداث بلا مكان/تاريخ واحد محدد**: evt-arab-defeat-1967-philosophical-turn.md (حرب متعددة الجبهات)، evt-cbt-founding-1950s-60s.md (سلسلة وقائع منفصلة في مدن مختلفة عبر 15 عاماً) — تُرك event_place/event_date بقيمة عامة (شهر/سنة فقط أو null) مع توثيق السبب صراحة في gaps بدل اختراع توحيد زائف.
- **evt-apa-founding-1892.md**: تصحيح خلط تاريخي كان موجوداً في الملف الأصلي بين اجتماع التأسيس الفعلي (مكتب هول بجامعة كلارك) والاجتماع السنوي الأول الرسمي (جامعة بنسلفانيا، ديسمبر 1892) — تم التحقق والتصحيح.
- **evt-apa-apology-racism-2021.md**: event_place تُرك null (لم يُعرف بثقة إن كان الاجتماع حضورياً أو افتراضياً) بدل التخمين.
- لا اختراع أسماء حضور في أي ملف — حيث لم تُعرف الأسماء بثقة (مثل قائمة النواب المصوتين على قانون بازاليا، أو حضور حفل توقيع Community Mental Health Act 1963)، وُثِّق الغياب في gaps.
- تصحيحات preflight إضافية: إصلاح مخالفة "سنة مذكورة بعد active_end بلا إشارة توضيحية" في عدة ملفات (evt-arab-defeat-1967 عبر تغيير active_end إلى "مستمر"، evt-cbt-founding عبر تصحيح active_end إلى 1997 وتوضيح السياق الزمني، evt-burning-of-giordano-bruno-1600 عبر صياغة "بعد وفاته").

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل. الفجوات المتبقية (تواريخ/أماكن غير مؤكدة بدقة، أسماء حضور غير موثقة) مسجّلة داخل gaps كل ملف.

## الملفات
content/ar/events/evt-aaap-founding-1937.md
content/ar/events/evt-aabt-abct-founding-1966.md
content/ar/events/evt-aamft-founding-1942.md
content/ar/events/evt-abpp-founding-1947.md
content/ar/events/evt-ahp-founding-1961.md
content/ar/events/evt-ai-breakthrough-deep-learning-2012.md
content/ar/events/evt-american-journal-psychology-1887.md
content/ar/events/evt-anti-psychiatry-network-london-1967.md
content/ar/events/evt-apa-apology-racism-2021.md
content/ar/events/evt-apa-founding-1892.md
content/ar/events/evt-aps-split-1988.md
content/ar/events/evt-arab-defeat-1967-philosophical-turn.md
content/ar/events/evt-army-alpha-beta-ww1-ww2-selection.md
content/ar/events/evt-aub-psychology-department-1950.md
content/ar/events/evt-bad-homburg-international-psychotherapy-1924.md
content/ar/events/evt-bandung-conference-1955-decolonial.md
content/ar/events/evt-basaglia-law-italy-1978.md
content/ar/events/evt-battle-of-jena-hegel-1806.md
content/ar/events/evt-boulder-conference-scientist-practitioner-1949.md
content/ar/events/evt-bps-founding-1901.md
content/ar/events/evt-buenos-aires-psychology-institute-1908.md
content/ar/events/evt-burning-of-averroes-books-cordoba-1195.md
content/ar/events/evt-burning-of-giordano-bruno-1600.md
content/ar/events/evt-calcutta-psychology-department-1916.md
content/ar/events/evt-cbt-founding-1950s-60s.md
content/ar/events/evt-cerletti-bini-first-ect-1938.md
content/ar/events/evt-chlorpromazine-discovery-1952.md
content/ar/events/evt-clark-university-lectures-1909.md
content/ar/events/evt-closing-of-athens-schools-justinian-529.md
content/ar/events/evt-community-mental-health-act-1963.md
