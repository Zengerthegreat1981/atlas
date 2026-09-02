# Task 9.10
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: 0/30 (مصادر حقيقية ذُكرت نصياً في المتن للعديد من الملفات، لكن بلا slug مستقل موجود في الأطلس فلم تُضف كقسم منفصل)

## أمر التحقق
python3 scripts/task.py verify spark 9.10
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-matrix-model.md: **إصلاح جوهري** — edges.belongs_to كان نص حر "الإدمان" → sch-cognitive-behavioral. المؤسس الحقيقي (Richard Rawson/UCLA) غير موجود بslug — النص القديم كان ينسبها خطأً لـthk-jkadden (كاثلين كارول، باحثة ييل مختلفة تماماً) — أُزيل هذا الخلط وسُجِّل الفجوة.
- tec-mbct.md وtec-mbrp.md: صُححت title لـ tec-mbsr.
- tec-mbct-3min-breathing-space.md وtec-mbct-three-minute-breathing.md: تكرار مؤكد لنفس التمرين (بالإضافة لملف con- ثالث) — سُجِّل بدقة في gaps بدون دمج. صُحح slug مكسور thk-zsegalsegal → thk-zsegal، وخطأ إملائي "تيسديل" → "تيزديل".
- tec-mbt.md: صُحح اسم المبتكر من "أنطوني باتمن" إلى "أنتوني بيتمان" (مطابق لـ thk-bateman).
- tec-milieu-therapy.md: **إصلاح** — رابط المؤسس الحقيقي (ماكسويل جونز، مذكور بالمتن أصلاً) كان مفقوداً من related رغم وجود slug له — أُضيف thk-mjones.
- tec-parent-management-training.md: **إصلاح هوية جوهري** — الملف كان ينسب PMT خطأً لاسم "Alan Kazantzakis" (غير موجود، خلط أسماء واضح) بدل المؤسس الحقيقي **آلان كازدين (Alan Kazdin)**، جامعة ييل — صُحح الاسم في المتن. كازدين بلا slug — طُلب في requests-spark.md.
- tec-past-life-regression.md: evidence_level = discredited بوضوح — غياب أي دليل تجريبي، الذاكرة الزائفة تحت التنويم (آلية فشل مشتركة مع حركة الذاكرة المستعادة). أُصلح edges بـtarget="حركات مثيرة للجدل" نص حر → sch-transpersonal.
- tec-mesmerism-historical.md: evidence_level = traditional (سلف تاريخي للتنويم الحديث، لا ادعاء علاجي قائم بذاته) — صُححت title لـ thk-fmesmer.
- tec-metaphor-therapy.md: أُصلح edges بـtarget="التنويم الإريكسوني" نص حر → sch-ericksonian-hypnosis.
- tec-naikan-therapy.md: حُذفت ملاحظة gaps باطلة تدّعي غياب slug ليوشيموتو إيشين رغم وجوده فعلاً (thk-yishin معتمد).
- كل الروابط تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- تكرار مؤكد بين tec-mbct-3min-breathing-space.md وtec-mbct-three-minute-breathing.md (وملف con- ثالث) — يحتاج قرار دمج/إحالة بشري.
- عدة مؤسسين حقيقيين بلا ملف thk- (Richard Rawson لـMatrix Model، Alan Kazdin لـPMT، Helen Wambach وIan Stevenson لـPast-Life Regression، Barbara Myerhoff لـNarrative Definitional Ceremony، Tom Erik Arnkil لـOpen Dialogue): مسجَّلون في requests-spark.md أو gaps.
- عدة دراسات حقيقية مذكورة بالاسم بلا ملف stu- مستقل (Bateman & Fonagy 1999/2008 لـMBT، Rawson et al. 2004 لـMatrix Model، Kuyken 2010/2015 لـMBCT، Grossman 2004 لـMBSR، Bowen 2014 لـMBRP) — الأدلة موجودة نصياً لكن بلا رابط قابل للتحقق آلياً.

## الملفات
content/ar/techniques/tec-matrix-model.md
content/ar/techniques/tec-mbct-3min-breathing-space.md
content/ar/techniques/tec-mbct-three-minute-breathing.md
content/ar/techniques/tec-mbct.md
content/ar/techniques/tec-mbrp.md
content/ar/techniques/tec-mbsr.md
content/ar/techniques/tec-mbt.md
content/ar/techniques/tec-meaning-centered-psychotherapy.md
content/ar/techniques/tec-meaning-technique-socratic.md
content/ar/techniques/tec-memory-reconsolidation.md
content/ar/techniques/tec-mental-imagery.md
content/ar/techniques/tec-mesmerism-historical.md
content/ar/techniques/tec-metacognitive-therapy.md
content/ar/techniques/tec-metaphor-therapy.md
content/ar/techniques/tec-mi-oars-protocol.md
content/ar/techniques/tec-milan-systemic.md
content/ar/techniques/tec-milieu-therapy.md
content/ar/techniques/tec-morita-therapy.md
content/ar/techniques/tec-motivational-interviewing.md
content/ar/techniques/tec-multimodal-therapy.md
content/ar/techniques/tec-multisystemic-therapy.md
content/ar/techniques/tec-music-therapy.md
content/ar/techniques/tec-naikan-therapy.md
content/ar/techniques/tec-narrative-definitional-ceremony.md
content/ar/techniques/tec-narrative-therapy.md
content/ar/techniques/tec-net.md
content/ar/techniques/tec-open-dialogue.md
content/ar/techniques/tec-paradoxical-intention.md
content/ar/techniques/tec-parent-management-training.md
content/ar/techniques/tec-past-life-regression.md
