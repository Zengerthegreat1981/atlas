# Task 5.5
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 9 روابط belongs_to/authored_by بنص حر، 6 تعارضات title/id، 9 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.5 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- wrk-design-everyday-things.md: دونالد نورمان (Donald A. Norman) غير موجود في الأطلس (تحققت أن thk-norman-vincent-peale شخص مختلف) — سُجّل في requests-spark.md، وحُذف رابط edges الحر المقابل.
- wrk-dialectic-of-enlightenment-adorno-horkheimer.md: عمل بمؤلفين، استُخدم author_slug لأدورنو فقط (thk-theodor-adorno، السلاج المصنّف صح تحت مدرسة فرانكفورت — يوجد ازدواج thk-adorno/thk-theodor-adorno يحتاج دمج لاحق خارج النطاق).
- بعد preflight: حذفت 9 روابط belongs_to/authored_by بنص حر (بدل اختراع slug مدرسة)، صححت authored_by لدانيال سيغل ولاينغ إلى slugs حقيقية، صححت 6 تعارضات title/id في related، ووسّعت active_end في 7 ملفات لتطابق سنوات مذكورة فعلاً بالمتن.

## متوقف عنده (لرئيس التحرير)
- طلب slug جديد في requests-spark.md: thk-donald-norman.
- ازدواج thk-adorno/thk-theodor-adorno يحتاج دمج تحريري.
- ملاحظات gaps قديمة غير دقيقة (برينيه براون، داماسيو) لسه موجودة في بعض الملفات — لم تُمس لأنها خارج نطاق Task 5، تحتاج Task 3/4.

## الملفات
40 ملفاً في content/ar/works/ (wrk-cured-rediger → wrk-economic-philosophic-manuscripts-1844، ترتيب أبجدي)
