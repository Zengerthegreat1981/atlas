# Task 5.6
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 13 رابط edges بنص حر، 10 تعارضات title/id، 13 مشكلة سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.6 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- wrk-eger-the-choice.md: إديث إيجر (Edith Eger) بلا ملف مفكر (فقط ملف خبرة معيشة exp-) — سُجّلت في requests-spark.md.
- wrk-fasus-al-hikam-farabi-pseudo.md: مؤلف منحول/منازع — لا author_slug ولا publication_year عمداً (لا اختراع).
- wrk-etude-experimentale-intelligence.md: ألفريد بينيه بلا slug — سُجّل في requests-spark.md، وحُذف الرابط الحر المقابل.
- بعد preflight: حذفت 13 رابط belongs_to/authored_by بنص حر، صححت 3 روابط authored_by/written_by لصياغة slug حقيقي (ريتشارد ديفيدسون، إيفان طومسون، إدوارد تيتشنر، رولو ماي، يالوم)، صححت 10 تعارضات title/id، ووسّعت active_end في 13 ملفاً لتطابق سنوات مذكورة فعلاً بالمتن.

## متوقف عنده (لرئيس التحرير)
- طلبات slugs جديدة في requests-spark.md: thk-edith-eger، thk-alfred-binet.
- wrk-emotional-understanding.md: تضارب موجود مسبقاً بين edges/related (thk-dorange) ومتن الملف (يذكر Donna M. Orange مختلفة) — يحتاج تدقيق قرائي منفصل، لم يُمس.
- عدة ملفات (goleman، robert-kegan، sapolsky سابقاً) فيها gaps قديمة تزعم غياب ملف مفكر رغم وجوده فعلاً — تراكمت من دفعات سابقة، تحتاج تنظيف مجمّع في Task 3/4.

## الملفات
40 ملفاً في content/ar/works/ (wrk-ecrits → wrk-fear-of-freedom-1941، ترتيب أبجدي)
