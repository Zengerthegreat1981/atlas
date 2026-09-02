# Task 5.10
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 18 رابط edges بنص حر، 7 تعارضات title/id، 8 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.10 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- طلبات slugs جديدة سُجّلت (بلا اختراع): مارك جونسون (wrk-metaphors-we-live-by)، نجم الدين النسفي، لويس تيرمان، رودلف هرمان لوتسه، جيفري شوارتز (wrk-mind-and-brain — لا علاقة بـthk-barry/david/richard-schwartz الموجودين، أشخاص مختلفون).
- wrk-mbt-manual.md: عمل بثلاثة مؤلفين، صححت author_slug من قائمة مفصولة بفواصل (غير صالحة) إلى قيمة واحدة (thk-zsegal).
- بعد preflight: حذفت 12 رابط belongs_to/authored_by بنص حر، صححت 4 روابط لـslugs حقيقية (مينكوفسكي، فرانكل، لايكوف، أدلر)، صححت 7 تعارضات title/id، ووسّعت active_end في 8 ملفات.

## متوقف عنده (لرئيس التحرير)
- 5 طلبات slugs جديدة مسجّلة في requests-spark.md هذه الدفعة.
- wrk-mans-search.md وملفات أخرى فيها edges باسم حر (فرانكل) قبل التصحيح — نمط متكرر عبر دفعات كثيرة، يستحق فحص شامل منفصل لكل edges في works/ بدل انتظار اكتشافه ملفاً ملفاً.

## الملفات
40 ملفاً في content/ar/works/ (wrk-listening-projective-identification → wrk-minderwertigkeit-organen، ترتيب أبجدي)
