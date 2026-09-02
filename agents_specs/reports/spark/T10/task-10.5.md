# Task 10.5
الحالة: مكتمل
المسار: spark | العملية: syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل (بلا dsm/icd code — كل الملفات syn-) | الملفات: 30

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30
أول دفعة تتكون بالكامل من syn- (لا dis- إطلاقاً).

## أمر التحقق
python3 scripts/task.py verify spark 10.5
→
=== تحقق Task 10.5 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **syn-anger.md**: الغضب انفعال إنساني عادي تكيفي لا اضطراب — وُضِّح صراحة في السقف الإكلينيكي أن التصنيف تحت "متلازمة" تنظيمي فقط، لا حكم مرضي على الانفعال نفسه.
- **متلازمات ثقافية متعددة في هذه الدفعة**: syn-ataque-de-nervios.md (لاتينية)، syn-bebes-enchilados.md (مكسيكية)، syn-bouffee-delirante.md (فرنسي/غرب أفريقي)، syn-brain-fag.md (غرب أفريقي، لامبو 1960) — وُضِّح طابعها الثقافي المحدد صراحة في كل ملف، مع تحذير من التعميم الثقافي الخاطئ حيث وُجد.
- **syn-broken-heart-takotsubo.md**: حالة قلبية طبية حقيقية موثقة تشخيصياً (لا استعارة) — وُضِّح صراحة.
- **syn-burnout.md**: مصنَّف في ICD-11 كـ"ظاهرة مهنية" (QD85) لا اضطراب نفسي — التمييز موثق صراحة، بما فيه استبعاد تطبيقه خارج سياق العمل.
- **syn-codependency.md**: مفهوم شعبي-علاجي مثير للجدل أكاديمياً، ليس فئة تشخيصية رسمية (لا DSM-5 ولا ICD-11) — وُثِّق هذا صراحة كما طلبت التعليمات.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم حقيقية موجودة فعلاً (أمثلة: con-eudaimonia-wellbeing, con-sense-and-reference-frege, con-primary-emotion, con-unconscious-inference, con-bad-faith-mauvaise-foi, con-blind-will-to-life, con-unity-of-knowledge-and-action, con-lived-body, con-grief, con-body-schema, con-embodied-perception-merleau-ponty, con-freedom, con-mind-body, con-boreout إلخ لا، con-boredom-existential, con-language-of-thought-mentalese, con-alienation-entfremdung-marx, con-phenomenology, con-hypnotic-suggestibility, con-speech-acts-performatives, con-ethics-of-care-concept, con-buddhist-compassion-karuna, con-recognition-theory-honneth, con-care-ethics, con-epistemic-injustice-fricker-concept) — لا اختراع مفاهيم.
- تصحيحات preflight موجودة سلفاً عبر الدفعة (غير ناتجة عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة (خاصة إشارات لملفات dis- تغيرت عناوينها في دفعات سابقة من نفس المهمة)، حذف جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" وأقسام "اقتباسات مختارة" الفارغة المرتبطة بها من عدة ملفات، وإصلاح كسر بنيوي في frontmatter (سطر `---` مكرر) في syn-anger.md.

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل جديد. الفجوات المتبقية (دراسات حقيقية بلا ملف stu- مقابل، مثل أبحاث Lambo 1960 وDaseleer/Vaillant، ومصادر أولية غير مراجَعة) موثقة داخل gaps كل ملف.

## الملفات
content/ar/syndromes/syn-angelman-happy-puppet.md
content/ar/syndromes/syn-anger.md
content/ar/syndromes/syn-anomic-aphasia.md
content/ar/syndromes/syn-anticholinergic-toxicity.md
content/ar/syndromes/syn-anton-babinski.md
content/ar/syndromes/syn-apathetic-frontal.md
content/ar/syndromes/syn-apraxia-ideomotor.md
content/ar/syndromes/syn-asomatognosia.md
content/ar/syndromes/syn-ataque-de-nervios.md
content/ar/syndromes/syn-autotopagnosia.md
content/ar/syndromes/syn-balint.md
content/ar/syndromes/syn-battered-woman.md
content/ar/syndromes/syn-bebes-enchilados.md
content/ar/syndromes/syn-biid.md
content/ar/syndromes/syn-boreout.md
content/ar/syndromes/syn-bouffee-delirante.md
content/ar/syndromes/syn-brain-fag.md
content/ar/syndromes/syn-briquet.md
content/ar/syndromes/syn-broca-aphasia.md
content/ar/syndromes/syn-broken-heart-takotsubo.md
content/ar/syndromes/syn-burnout.md
content/ar/syndromes/syn-capgras.md
content/ar/syndromes/syn-caregiver-burnout.md
content/ar/syndromes/syn-cassandra.md
content/ar/syndromes/syn-charles-bonnet.md
content/ar/syndromes/syn-chinese-restaurant.md
content/ar/syndromes/syn-chronic-fatigue.md
content/ar/syndromes/syn-cluttering.md
content/ar/syndromes/syn-codependency.md
content/ar/syndromes/syn-compassion-fatigue.md
