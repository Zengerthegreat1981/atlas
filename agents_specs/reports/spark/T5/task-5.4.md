# Task 5.4
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 13 رابط edges بنص حر، 6 تعارضات title/id، 6 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.4 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author بالكامل؛ author_slug فقط للموثقين فعلياً.
- wrk-chinese-mirror-rosemont.md، wrk-buddhas-brain.md (مؤلف مشارك)، wrk-cognitive-therapy-personality.md (مؤلف مشارك): مؤلفون بلا slug — سُجّلوا في requests-spark.md (thk-rosemont، thk-richard-mendius، thk-arthur-freeman) بدون اختراع.
- wrk-communist-manifesto-marx-engels.md وwrk-contexts-of-being.md: أعمال متعددة المؤلفين، author_slug للمؤلف الأول فقط (القالب أحادي القيمة)، بقية الأسماء مذكورة في author نصاً.
- بعد preflight: حذفت 8 روابط belongs_to بنص حر، صححت 5 روابط authored_by/written_by من اسم حر لـslug حقيقي (thk-besselvanderkolk، thk-bowlby ×2، thk-kierkegaard، thk-beck، thk-brandchaft)، حذفت رابط أرثر فريمان (بلا slug)، صححت 6 تعارضات title/id في related، ووسّعت active_end في 5 ملفات لتطابق سنوات مذكورة فعلاً في المتن.

## متوقف عنده (لرئيس التحرير)
- طلبات slugs جديدة في requests-spark.md: thk-rosemont، thk-richard-mendius، thk-arthur-freeman.
- wrk-body-keeps-score.md: يوجد slug مكرر لفان دير كولك (thk-besselvanderkolk وthk-bvdkolk) — يحتاج توحيد لاحق، خارج نطاق هذا التاسك.

## الملفات
40 ملفاً في content/ar/works/ (wrk-black-skin-white-masks-fanon → wrk-cur-deus-homo-anselm، ترتيب أبجدي)
