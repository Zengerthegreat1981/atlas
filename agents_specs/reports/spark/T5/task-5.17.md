# Task 5.17
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 4

## الأرقام
author موجود: قبل 0 → بعد 4/4
preflight_check: 4/4 → صفر مخالفات (بعد حذف جمل قائمة سوداء من wrk-you-can-heal-your-life.md وwrk-zhuangzi-text.md، وتصحيح رابط edges بنص حر لهايدجر/بوس)

## أمر التحقق
python3 scripts/task.py verify spark 5.17 → author 4/4، قائمة سوداء 0/4

## قرارات اتخذتها
- wrk-zollikon.md: عمل مشترك (هايدجر وبوس) — author_slug للأول (thk-heidegger)، مع رابطي edges منفصلين لكلا المؤلفين (thk-heidegger وthk-boss، كلاهما موجود فعلاً).
- كل الأربعة مؤلفين موثقون فعلاً في الأطلس — لا طلبات slug جديدة.
- حذفت جملتي قائمة سوداء متبقيتين من دفعات سابقة (you-can-heal-your-life، zhuangzi-text).

## متوقف عنده (لرئيس التحرير)
لا شيء يستدعي المراجعة هذه الدفعة.

## الملفات
content/ar/works/wrk-yoga-sutras-patanjali.md
content/ar/works/wrk-you-can-heal-your-life.md
content/ar/works/wrk-zhuangzi-text.md
content/ar/works/wrk-zollikon.md
