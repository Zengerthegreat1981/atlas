# Task 9.12
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط | الملفات: 30

## الأرقام
جمل القائمة السوداء: عشرات → 0
سقّالة ظاهرة (edges بنص حر): 3 حالات مصححة → 0
تطابق id/title مكسور: 10+ حالات مصححة → 0
gaps بتؤكد حقيقة بدل تسمية فجوة: 2 حالة مصححة → 0
## المصادر: 0/30 (متوقع، خارج نطاق Task 9)

## أمر التحقق
`python3 scripts/task.py verify minimax 9.12` → صفر قائمة سوداء، صفر سقّالة
`python3 scripts/preflight_check.py` على الـ30 ملف → صفر مخالفات (بعد جولتين تصحيح)

## قرارات اتخذتها
- 10 subagents متوازية، 3 ملفات لكل واحد، أعادوا بناء `related` بعد تحقق فعلي من كل ملف مستهدف.
- صححت بنفسي بعد preflight: `con-four-noble-truths-buddha` و`con-free-association` (صياغة gaps كانت تؤكد حقيقة بدل تسمية فجوة — أُعيدت الصياغة لتسمية الناقص بدقة: نص خطبة بنارس، موقف رينيك).
- edges بنص حر مصححة: `con-four-agreements` (→ sch-popular-psychology)، `con-gaslighting-popular` (→ sch-popular-psychology)، `con-framing-effect` (لا مدرسة مطابقة → edges:[]، سُجّل في missing-schools.md)، `con-getting-things-done-gtd` (→ sch-popular-psychology)، `con-god-complex` (→ sch-psychoanalysis)، `con-general-will-rousseau` (sch-enlightenment→sch-social-contract، أدق تصنيفياً).
- ازدواجات مؤكدة (لم تُدمج، خارج نطاق Task 9، سُجّلت في gaps الملفين لكل زوج): `con-fusion-horizons`/`con-fusion-of-horizons-gadamer`، `con-functionalism-mind`/`con-functionalism-mind-putnam`، `con-gender-performativity`/`con-gender-performativity-concept`.
- مشكلة هوية مكتشفة: `con-ghost-in-the-machine-ryle` — الرابط المفترض `thk-ryle` الموجود في الأطلس هو أنتوني رايل (CAT) لا جيلبرت رايل صاحب المصطلح؛ لم يُربط، وسُجّل طلب slug جديد `thk-gilbert-ryle`.
- طلبات slug جديدة في `requests-minimax.md`: `thk-gilbert-ryle`، `wrk-subjects-of-analysis-ogden`.
- تصحيح ذاتي من أحد الـsubagents: كتب طلب `thk-tversky` بالخطأ ثم اكتشف أن `thk-amos-tversky` موجود فعلاً معتمداً، فحذف الطلب الخاطئ وربط الملف الصحيح.

## متوقف عنده (لرئيس التحرير)
- ثلاث ازدواجات مؤكدة تحتاج قرار دمج/تمييز عنوان (مذكورة أعلاه).
- `con-gettier-problem`: `belongs_to: br-logical-positivism-vienna-circle` غير دقيق موضوعياً (جيتيير إبستمولوجيا تحليلية لاحقة على الوضعية المنطقية) لكنه slug حقيقي فلم يُعدَّل ضمن Task 9 — يحتاج مراجعة تصنيف Task 5/13.
- `con-four-fundamentals-langle`: `belongs_to: sch-humanistic` بينما thk-langle نفسه منتمٍ لـsch-existential-therapy — تعارض تصنيفي يحتاج مراجعة.

## الملفات
- content/ar/concepts/con-four-agreements.md
- content/ar/concepts/con-four-causes-aristotle.md
- content/ar/concepts/con-four-fundamentals-langle.md
- content/ar/concepts/con-four-noble-truths-buddha.md
- content/ar/concepts/con-four-principles-ogden.md
- content/ar/concepts/con-framing-effect.md
- content/ar/concepts/con-free-association.md
- content/ar/concepts/con-freedom.md
- content/ar/concepts/con-fully-functioning-person.md
- content/ar/concepts/con-functional-contextualism.md
- content/ar/concepts/con-functionalism-mind-putnam.md
- content/ar/concepts/con-functionalism-mind.md
- content/ar/concepts/con-fundamental-attribution-error.md
- content/ar/concepts/con-fundamental-existential-motivations.md
- content/ar/concepts/con-fusion-horizons.md
- content/ar/concepts/con-fusion-of-horizons-gadamer.md
- content/ar/concepts/con-gaslighting-popular.md
- content/ar/concepts/con-gelassenheit.md
- content/ar/concepts/con-gender-performativity-concept.md
- content/ar/concepts/con-gender-performativity.md
- content/ar/concepts/con-general-will-rousseau.md
- content/ar/concepts/con-genogram.md
- content/ar/concepts/con-gestell.md
- content/ar/concepts/con-gettier-problem.md
- content/ar/concepts/con-getting-things-done-gtd.md
- content/ar/concepts/con-geworfenheit-thrownness.md
- content/ar/concepts/con-gewu-investigation-of-things.md
- content/ar/concepts/con-ghost-in-the-machine-ryle.md
- content/ar/concepts/con-gnosis.md
- content/ar/concepts/con-god-complex.md
