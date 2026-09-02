# Task 11.3
الحالة: مكتمل
المسار: spark | العملية: events: event_date/event_place + إجابة صريحة على (ماذا/متى/أين/من حضر بالاسم/ماذا تغيّر/النص الناتج) | الملفات: 30

## الأرقام
event_date موجود: 0/30 → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 11.3
→
=== تحقق Task 11.3 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 3 / 30
فيها الحقل event_date: 30 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **مواضيع حساسة عولجت بجدية وأمانة تامة**: evt-frankfurt-auschwitz-trials-1963.md (تفاصيل موثقة: 22 متهماً، فريتز باور، هانز هوفماير، الحكم النهائي)، evt-frankl-camps.md (تيريزينشتاط/أوشفيتز/كاوفرينغ، أسماء العائلة، تاريخ التحرير)، evt-goering-institute-nazi-psychology-1936.md (تطهير جمعية برلين للتحليل النفسي، دور يونغ المتنازع عليه وُثِّق كخلاف تاريخي في gaps)، evt-hoffman-report-apa-torture-2015.md (ميتشل وجيسين، ديفيد هوفمان، قرار مجلس مندوبي APA).
- **ملفات أُعيد كتابتها بالكامل** لكونها حشواً قالبياً فارغاً: evt-first-african-philosophy-conference-1970.md (مع اعتراف صريح بعدم القدرة على التحقق من تفاصيل مؤتمر نيروبي بعينه)، evt-founding-of-epicurus-garden-306bc.md، evt-founding-of-frankfurt-institute-1923.md، evt-founding-of-kyoto-school-1911.md، evt-founding-of-platos-academy-387bc.md، evt-founding-of-psychoanalysis-vienna-1902.md، evt-founding-of-stoic-porch-300bc.md، evt-house-of-wisdom-translations-baghdad.md.
- **evt-immigration-act-iq-testing-1924.md**: موضوع حساس (اختبارات ذكاء عنصرية أثّرت على تشريع هجرة أمريكي).
- تصحيحات active_end متعددة عبر الدفعة لحل مخالفة "سنة بعد active_end بلا توضيح" — بتوسيع النطاق الزمني الحقيقي بدل حذف وقائع صحيحة (أمثلة: evt-founding-of-university-of-paris-1150 → 1215، evt-fourth-world-conference-women-beijing-1995 → 2015، evt-haitian-revolution-1804 → 1825، evt-icd-6-mental-disorders-1948 → 1952).
- لا اختراع أسماء حضور — حيث لم تُعرف بثقة (متهمو أوشفيتز الـ20 الباقون، ممثلو الوفود بمؤتمر EABCT سابقاً، مكان إعلان تقرير هوفمان)، وُثِّق الغياب في gaps.
- تصحيحات preflight إضافية: حذف روابط related غير ذات صلة موضوعية (evt-founding-of-kyoto-school-1911.md)، إصلاح تكرار مزدوج في related (evt-false-memory-syndrome-foundation-1992.md).

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل. الفجوات المتبقية (تواريخ/أماكن غير مؤكدة، أسماء حضور غير موثقة، خلافات تاريخية مثل دور يونغ في معهد غورينغ) مسجّلة داخل gaps كل ملف.

## الملفات
content/ar/events/evt-expulsion-of-jews-and-muslims-spain-1492.md
content/ar/events/evt-fall-of-berlin-wall-1989-end-of-history.md
content/ar/events/evt-false-memory-syndrome-foundation-1992.md
content/ar/events/evt-first-african-philosophy-conference-1970.md
content/ar/events/evt-first-international-congress-psychology-1889.md
content/ar/events/evt-fluoxetine-prozac-launch-1987.md
content/ar/events/evt-foucault-chomsky-televised-debate-1971.md
content/ar/events/evt-founding-of-al-azhar-970.md
content/ar/events/evt-founding-of-aristotles-lyceum-335bc.md
content/ar/events/evt-founding-of-epicurus-garden-306bc.md
content/ar/events/evt-founding-of-frankfurt-institute-1923.md
content/ar/events/evt-founding-of-kyoto-school-1911.md
content/ar/events/evt-founding-of-platos-academy-387bc.md
content/ar/events/evt-founding-of-psychoanalysis-vienna-1902.md
content/ar/events/evt-founding-of-stoic-porch-300bc.md
content/ar/events/evt-founding-of-university-of-paris-1150.md
content/ar/events/evt-fourth-world-conference-women-beijing-1995.md
content/ar/events/evt-frankfurt-auschwitz-trials-1963.md
content/ar/events/evt-frankl-camps.md
content/ar/events/evt-frege-russell-paradox-letter-1902.md
content/ar/events/evt-french-revolution-1789-philosophical.md
content/ar/events/evt-goering-institute-nazi-psychology-1936.md
content/ar/events/evt-haitian-revolution-1804-philosophical.md
content/ar/events/evt-hinckley-verdict-insanity-reform-1984.md
content/ar/events/evt-hoffman-report-apa-torture-2015.md
content/ar/events/evt-house-of-wisdom-translations-baghdad.md
content/ar/events/evt-iaap-jungian-1955.md
content/ar/events/evt-icd-11-cddi-2018.md
content/ar/events/evt-icd-6-mental-disorders-1948.md
content/ar/events/evt-immigration-act-iq-testing-1924.md
