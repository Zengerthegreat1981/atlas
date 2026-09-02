# Task 5.8
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 13 رابط belongs_to/authored_by بنص حر، 2 تعارض title/id، 7 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.8 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- wrk-huanglao-texts.md: تجميع نصوص جماعي مجهول المؤلف — بلا author_slug ولا publication_year عمداً، موثّق في gaps.
- wrk-inquiries-human-faculty.md: فرانسيس غالتون بلا slug — سُجّل في requests-spark.md، وحُذف الرابط الحر المقابل.
- wrk-horney-inner-conflicts.md وwrk-horney-neurotic-personality.md: صُحح authored_by من "كارين هورناي" النص الحر إلى slug thk-khorney الصحيح (وليس thk-horney).
- بعد preflight: حذفت 11 رابط belongs_to بنص حر، صححت رابط authored_by لهلمهولتز، صححت تعارضي title/id (ابن ميمون، ابن رشد)، ووسّعت active_end في 7 ملفات.

## متوقف عنده (لرئيس التحرير)
- طلب slug جديد في requests-spark.md: thk-galton.
- عدة gaps قديمة (هايدت، كوهين) لسه تزعم غياب ملف مفكر رغم وجوده — تراكمت عبر عدة دفعات، تحتاج تنظيف مجمّع في Task 3/4.

## الملفات
40 ملفاً في content/ar/works/ (wrk-grundzuge-physiologische-psychologie → wrk-inquiries-human-faculty، ترتيب أبجدي)
