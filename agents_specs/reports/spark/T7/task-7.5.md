# Task 7.5
الحالة: مكتمل
العملية: studies: إضافة study_year/design/sample_size/main_finding/replication_status | الملفات: 1

## الأرقام
study_year موجود: قبل 0 → بعد 1/1
preflight_check: 1/1 → صفر مخالفات

## أمر التحقق
python3 scripts/task.py verify spark 7.5 → study_year 1/1

## قرارات اتخذتها
- wrk-wundt-leipzig-1879.md: ملف حدث تأسيسي (تأسيس مختبر) لا تجربة بعينة مشاركين — sample_size: null مع gap يوضح عدم الانطباق، design موصوف نصياً بدل تصنيف قياسي، replication_status: "untested".
- أُصلح خلل YAML: قسم gaps كان يحتوي أسطراً بدون إزاحة `- "..."` في العمود صفر بدل الإزاحة تحت `gaps:`، ما يكسر تحليل الفرونتماتر بالكامل — أُعيدت الإزاحة الصحيحة.
- وسّع active_end من 1880 إلى 1920 ليطابق سنوات مذكورة فعلاً في المتن (تأسيس تيتشنر للبنيوية 1890، نقد واطسون 1913).

## متوقف عنده (لرئيس التحرير)
لا شيء يستدعي المراجعة.

## الملفات
content/ar/studies/stu-wundt-leipzig-1879.md
