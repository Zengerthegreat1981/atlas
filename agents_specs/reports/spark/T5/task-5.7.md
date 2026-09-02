# Task 5.7
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 16 رابط edges بنص حر أو معطوب، 9 تعارضات title/id، 16 مشكلة سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.7 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- wrk-gathas.md: publication_year: null (لا تاريخ تدوين قاطع — نص شفهي قديم) مع توضيح في gaps.
- بعد preflight: حذفت 9 روابط belongs_to بنص حر، صححت 7 روابط authored_by/written_by من اسم حر لـslug حقيقي (جاسبرز، كوهلر، غاردنر، هندريكس، غوفمان، غونغسون لونغ، داكوورث)، أصلحت رابط edges معطوب في wrk-gestalt-psychology-kohler.md كان يشير self-reference لملفه نفسه بدل مدرسة، صححت 9 تعارضات title/id، ووسّعت active_end في 16 ملفاً لتطابق سنوات مذكورة فعلاً بالمتن.

## متوقف عنده (لرئيس التحرير)
- لا طلبات slug جديدة هذه الدفعة — كل المؤلفين موثقون.
- عدة ملفات فيها gaps قديمة (غاردنر، داكوورث) تزعم غياب ملف مفكر رغم وجوده فعلاً — تراكمت من دفعات سابقة أيضاً، تحتاج تنظيف مجمّع.
- wrk-frames-of-mind.md: author_slug يشير لـ thk-gardner وهو حالياً مسودة (🕓) لا معتمد (✅) — الرابط صحيح لكن يعتمد على ترقية الملف لاحقاً.

## الملفات
40 ملفاً في content/ar/works/ (wrk-feeling-good → wrk-grundlagen-psychischen-entwicklung، ترتيب أبجدي)
