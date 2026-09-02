# Task 12.11
الحالة: مكتمل — **آخر دفعة في Task 12 (386/386 ملف)**
المسار: spark | العملية: metaphors (16/16 met- خالصة) | الملفات: 16

## الأرقام
جمل القائمة السوداء: → بعد 0
سقّالة gaps قالبية ظاهرة: → بعد 0
ملفات فيها `## المصادر`: → بعد 16/16
**إجمالي Task 12 المُنجَز: 386/386 ملف (contexts + experiences + metaphors)**

## أمر التحقق
python3 scripts/task.py verify spark 12.11
→
```
=== تحقق Task 12.11 (16 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 16 / 16
```
preflight_check.py على الـ16 ملف: ✅ صفر مخالفات آلية.

## قرارات اتخذتها
- **met-therapy-as-gardening**: **إعادة بناء كاملة لتفادي تكرار met-mind-as-garden** — رُكّز حصراً على فعل المعالج (الري بالتقطير، حدود قدرة البستاني)، مع فقرة تمايز صريحة؛ تصحيح `edges` لـ`sch-humanistic`.
- **met-therapy-as-journey**: مصدر جوزيف كامبل 1949؛ تصحيح `edges` لـ`sch-existential-therapy` وعنوان يالوم.
- **met-therapy-as-levitation**: **توثيق صريح لضعف المصدر** — لا يوجد نص أولي واحد يستخدم "رفع" حرفياً؛ حُذفت روابط لمفكرين غير موجودين (تيك نات هانه، تشودرون) بدل اختراعها.
- **met-therapy-as-mirror**: **تمييز ثلاثي** عن `met-mind-as-mirror` (فلسفي) و`met-lacan-mirror-stage` و`met-winnicott-mirror-mother-face` — هذا يركز حصراً على موقف المعالج (فرويد 1912 مقابل روجرز 1951)؛ تصحيح `edges` غير موجود.
- **met-therapy-as-mountain-climbing**: **إعادة بناء كاملة** (كان حشواً بلا مصدر) — التوثيق الوحيد الحقيقي هو "تجربة الذروة" عند ماسلو (1943/1962)، ووُثِّق ذلك بصراحة بدل اختلاق أصل موحّد للاستعارة الكاملة.
- **met-therapy-as-rewiring**: هب 1949 → سيغل 1999/2010 → كوزولينو 2002/2016؛ تصحيح اكتشاف أن `thk-dsiegel` و`thk-lcozolino` موجودان فعلاً (كانا مُفترَضين خطأً كغائبين).
- **met-therapy-as-translation**: فرويد "تفسير الأحلام" 1900 (الكتابة التصويرية Bilderschrift)؛ تصحيح `edges` من `sch-constructivist` (غير موجود) إلى `sch-psychoanalysis`.
- **met-triune-brain-maclean**: **توثيق نقد علمي صارم وصريح** — النموذج **منتقد بشدة** من علم الأعصاب المعاصر (لوليدو)، ونص المتن يقول صراحة "لا يجب تقديمه كحقيقة علمية راسخة" بدل عرضه كنموذج مقبول.
- **met-turing-test-imitation-game**: مقالة تورينغ 1950؛ تصحيح عنوان `thk-john-searle`، ربط صريح بـ`met-chinese-room-searle`.
- **met-unconscious-as-sea**: تصحيح عنوان `thk-jung`؛ فجوة صريحة عن نسبة الصورة لفرويد (تفسير تأويلي شائع لا اقتباس حرفي مؤكد).
- **met-veil-of-ignorance-rawls**: **تمييز صريح عن met-rawls-original-position** — هذا يركز حصراً على آلية الحجاب نفسها (ماذا يُحجب بالضبط)، والآخر على التجربة الفكرية التعاقدية كاملة.
- **met-wax-tablet-aristotle**: **تمييز صريح عن met-locke-tabula-rasa** — توثيق الترتيب التاريخي (أرسطو ~2000 سنة قبل لوك 1690).
- **met-winnicott-mirror-mother-face** و**met-winnicott-transitional-object**: مقالتا وينيكوت 1967/1953؛ **تمييز صريح عن met-lacan-mirror-stage** (انعكاس انفعالي متبادل بين وجهين حيين مقابل انعكاس بصري حرفي في مرآة مادية).
- **met-wittgenstein-beetle-box**: بحوث فلسفية، فقرة 293 (1953)؛ نقد كريبكي 1982.
- **met-zeno-achilles-tortoise**: **تصحيح edge غير موجود** من `sch-presocratics` إلى `sch-eleatic` (المدرسة الفعلية لزينون).

## متوقف عنده (لرئيس التحرير)
- **met-therapy-as-levitation**: أضعف ملف توثيقاً في الدفعة كلها — يستحق مراجعة تحريرية لتقرير هل يبقى بصياغته الحالية المتحفظة أم يُعاد النظر فيه بالكامل.
- **met-therapy-as-mountain-climbing**: `active_start` غُيِّر من 1980 (غير مبرر) إلى 1943 (تجربة الذروة عند ماسلو) — يستحق تأكيداً أن هذا التأريخ مقبول رغم عدم وجود نص تأسيسي واحد للاستعارة الكاملة.
- **met-therapy-as-mirror/mountain-climbing/rewiring، met-therapy-as-gardening/journey/levitation**: جميعها ملفات family جديدة تستحق مراجعة شاملة لتأكيد عدم تكرار مضموني خفي مع باقي عائلة "العلاج كـ..." (alchemy, archaeology, detective, dialogue من دفعة سابقة).
- **met-unconscious-as-sea**: نسبة الصورة لفرويد تحديداً غير موثقة باقتباس حرفي مباشر.
- **met-winnicott-mirror-mother-face**: النقد النسوي المذكور بناء تحليلي أصلي من محتوى المصدرين لا اقتباس مباشر — يستحق مراجعة ثانية.

## ملخص إغلاق Task 12 الكامل
- 386/386 ملف contexts+experiences+metaphors مُعمَّق وموثَّق (11 دفعة: 12.1-12.2 كانت جزءاً من الشغل الأسبق قبل هذه الجلسة، 12.3-12.11 أُنجزت في هذه الجلسة عبر subagents متوازية).
- تكرارات محتملة حُسمت جميعها بتمييز حقيقي بلا حذف: جبل الجليد (فرويد×2)، تبدد الشخصية/الواقع، فرانكل (وقائع/فلسفة)، يونغ (القطيعة/مواجهة اللاشعور)، العقل كـ...×8، الذات كـ...×3، القناع/البرسونا، العلاج كآثار/مرآة×2/بستنة/حاوية، حجاب الجهل/الوضع الأصلي، لوح الشمع/صفحة لوك، مرايا لاكان/وينيكوت.
- أخطاء واقعية جوهرية صُححت (لا مجرد تعميق): خزي/ذنب (أرندت→لويس)، مستشفى ماكلين (فيرجينيا→ماساتشوستس)، نيتشه (نمر→أسد)، كتاب يونغ مختلَق، تسميات الخيمياء (Citrinitas/Rubedo)، إدوارد لورنز مقابل كونراد لورنز، نلسون غودمان مقابل بول غودمان، جيلبرت رايل مقابل أنتوني رايل.
- طلب slug جديد رسمي واحد (`sch-sociology`) مسجَّل في `agents_specs/requests-spark.md`.

## الملفات
content/ar/metaphors/met-therapy-as-gardening.md
content/ar/metaphors/met-therapy-as-journey.md
content/ar/metaphors/met-therapy-as-levitation.md
content/ar/metaphors/met-therapy-as-mirror.md
content/ar/metaphors/met-therapy-as-mountain-climbing.md
content/ar/metaphors/met-therapy-as-rewiring.md
content/ar/metaphors/met-therapy-as-translation.md
content/ar/metaphors/met-triune-brain-maclean.md
content/ar/metaphors/met-turing-test-imitation-game.md
content/ar/metaphors/met-unconscious-as-sea.md
content/ar/metaphors/met-veil-of-ignorance-rawls.md
content/ar/metaphors/met-wax-tablet-aristotle.md
content/ar/metaphors/met-winnicott-mirror-mother-face.md
content/ar/metaphors/met-winnicott-transitional-object.md
content/ar/metaphors/met-wittgenstein-beetle-box.md
content/ar/metaphors/met-zeno-achilles-tortoise.md
