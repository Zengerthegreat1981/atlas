# Task 5.11
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 13 رابط edges بنص حر، 8 تعارضات title/id، 9 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.11 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- طلبات slugs جديدة سُجّلت: أوليڤيه سيبوني وكاس سونشتاين (wrk-noise-kahneman)، كاس سونشتاين (wrk-nudge — نفس الشخص، طلب مكرر يوحَّد لاحقاً).
- wrk-object-relations-1983.md: عمل بمؤلفين، استخدمت author_slug للأول (thk-jgreenberg) وauthor_slug_2 للثاني (thk-mitchell).
- بعد preflight: حذفت 10 روابط belongs_to بنص حر، صححت 4 روابط authored_by/written_by لـslugs حقيقية (سبيرمان، أدلر، كوزولينو، كانمان، غرينبرغ)، صححت 8 تعارضات title/id، ووسّعت active_end في 9 ملفات.

## متوقف عنده (لرئيس التحرير)
- طلبات slugs جديدة مكررة (سونشتاين) في requests-spark.md — يُنصح بمراجعة لدمجها في طلب واحد.
- wrk-naming-and-necessity-kripke.md وwrk-naming-necessity.md ملفان مكرران لنفس الكتاب — يحتاجان دمج، خارج نطاق هذا التاسك.

## الملفات
40 ملفاً في content/ar/works/ (wrk-mindful-way-through-depression → wrk-on-tranquility-of-mind-seneca، ترتيب أبجدي)
