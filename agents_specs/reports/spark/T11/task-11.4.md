# Task 11.4
الحالة: مكتمل
المسار: spark | العملية: events: event_date/event_place + إجابة صريحة على (ماذا/متى/أين/من حضر بالاسم/ماذا تغيّر/النص الناتج) | الملفات: 30

## الأرقام
event_date موجود: 0/30 → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 11.4
→
=== تحقق Task 11.4 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30
فيها الحقل event_date: 30 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **تصحيحات لأخطاء واقعية/أسماء مختلَقة اكتُشفت أثناء العمل (أهم نتيجة في هذه الدفعة)**:
  - **evt-rogers-v-o-kin-1979.md**: النسخة الأصلية نسبت الحكم لقاضٍ باسم "توماس جيزا" — اسم غير موثق يبدو مختلَقاً بالكامل. صُحح إلى القاضي الحقيقي **جوزيف تاورو (Joseph L. Tauro)**، وأُضيفت المدعية الحقيقية **روبي روجرز (Ruby Rogers)** ومسار الاستئناف الفعلي.
  - **evt-nimh-founding-1949.md**: أول مدير لـNIMH كان مكتوباً باسم مختلَق "رِمَان فِسْتَلو (Rex Stalnaker)" — صُحح إلى **روبرت فيليكس (Robert H. Felix)** الحقيقي. صُحح أيضاً خلط بين تاريخ توقيع قانون الصحة العقلية الوطني 1946 وتاريخ بدء عمل NIMH فعلياً 1949.
  - **evt-munich-congress-jung-freud-split-1913.md**: رقم تصويت (52/22) نُقل كحقيقة مؤكدة — أُعيد تصنيفه كحاجة لمراجعة أرشيفية في gaps بدل تركه كواقعة قاطعة.
- **مواضيع حساسة عولجت بجدية نقدية بلا تبرير أو تبسيط**: evt-rectorate-address-heidegger-1933.md (خطاب هايدغر عند توليه رئاسة جامعة فرايبورغ، انضمامه للحزب النازي، سياسات التنسيق).
- **ملفات أُعيد كتابتها بالكامل** لكونها حشواً قالبياً فارغاً: evt-launch-of-internet-www-1991.md، evt-lisbon-earthquake-1755-philosophical.md، evt-nietzsche-collapse-turin-1889.md، evt-nuremberg-trials-1945-crimes-against-humanity.md، evt-publication-of-communist-manifesto-1848.md، evt-publication-of-rawls-theory-of-justice-1971.md، evt-rectorate-address-heidegger-1933.md.
- تصحيحات active_end متعددة عبر الدفعة لحل مخالفة "سنة بعد active_end بلا توضيح" — بتوسيع النطاق الزمني الحقيقي بدل حذف وقائع صحيحة (أمثلة: evt-luther-95-theses → 1521، evt-royal-society-founding-london-1660 → 1665، evt-nietzsche-collapse-turin-1889 → 1900، evt-rosenhan-study-publication-1973 → 1980).
- لا اختراع أسماء حضور — حيث لم تُعرف بثقة (حضور اجتماع الجمعية الملكية الكامل، أسماء متطوعي روزنهان السبعة الآخرين، أسماء أطباء شهود قضية ماكناتن)، وُثِّق الغياب في gaps.

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل. الفجوات المتبقية (تواريخ/أماكن غير مؤكدة، أسماء حضور غير موثقة) مسجّلة داخل gaps كل ملف. الأسماء المختلَقة المكتشفة (روجرز، NIMH) صُححت بالفعل ولا تحتاج مراجعة إضافية.

## الملفات
content/ar/events/evt-jahrbuch-psychoanalyse-1909.md
content/ar/events/evt-journal-analytical-psychology-1955.md
content/ar/events/evt-jung-institute-zurich-1948.md
content/ar/events/evt-lanterman-petris-short-act-1967.md
content/ar/events/evt-launch-of-internet-www-1991.md
content/ar/events/evt-lisbon-earthquake-1755-philosophical.md
content/ar/events/evt-little-albert-ethical-controversy-1970.md
content/ar/events/evt-luther-95-theses-wittenberg-1517.md
content/ar/events/evt-may-1968-student-revolt-paris.md
content/ar/events/evt-mental-health-parity-act-2008.md
content/ar/events/evt-mihna-inquisition-mutazila-833.md
content/ar/events/evt-mnaghten-rule-1843.md
content/ar/events/evt-munich-congress-jung-freud-split-1913.md
content/ar/events/evt-nietzsche-collapse-turin-1889.md
content/ar/events/evt-nimh-founding-1949.md
content/ar/events/evt-nuremberg-congress-ipa-1910.md
content/ar/events/evt-nuremberg-trials-1945-crimes-against-humanity.md
content/ar/events/evt-old-saybrook-conference-1964.md
content/ar/events/evt-open-science-collaboration-2015.md
content/ar/events/evt-peace-of-westphalia-1648.md
content/ar/events/evt-philosophische-studien-1881.md
content/ar/events/evt-psychonomic-society-1959.md
content/ar/events/evt-publication-of-communist-manifesto-1848.md
content/ar/events/evt-publication-of-rawls-theory-of-justice-1971.md
content/ar/events/evt-rectorate-address-heidegger-1933.md
content/ar/events/evt-rogers-v-o-kin-1979.md
content/ar/events/evt-rosenhan-study-publication-1973.md
content/ar/events/evt-royal-society-founding-london-1660.md
content/ar/events/evt-sakel-insulin-shock-therapy-1933.md
content/ar/events/evt-sartre-existentialism-is-a-humanism-lecture-1945.md
