# Task 11.5
الحالة: مكتمل
العملية: debates/ — تسمية الطرفين الحقيقيين بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.5): صفر مخالفات آلية (30/30 ملف)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء الـ18 على الملفات الـ30): صفر تطابق

## ⚠️ دمج فعلي مطبَّق حسب القاعدة 6 — ازدواج ثلاثي حقيقي مكتشف
`dbt-categorical-vs-dimensional-rdoc-vs-dsm.md` و`dbt-categorical-vs-dimensional.md` كانا تكراراً فعلياً لمحتوى موجود مسبقاً في `dbt-rdoc-critique.md` و`dbt-categorical-vs-dimensional-diagnosis.md` (نفس النزاع، نفس الأسماء، بدون زاوية مستقلة حقيقية) — حُوِّلا لملفين موجزين مُحيلين (تفسير الازدواج + إحالة) بدل حذف الـslug، حسب القاعدة 6. أما `dbt-categorical-vs-hitop-dimensional.md` فله زاوية مستقلة حقيقية (البنية الإحصائية-الهرمية HiTOP وليس RDoC العصبي ولا DSM عموماً) — أُعيد كتابته بمحتوى حقيقي (Kotov, Krueger, Watson et al. 2017) ولم يُدمج.

## ⚠️ تداخل موضوعي مسجَّل بدون دمج (يحتاج قرار رئيس التحرير)
`dbt-diagnostic-concept-creep.md` و`dbt-concept-creep-psychiatry.md` (من نفس الدفعة، subagents مختلفان) يغطيان نفس الظاهرة تقريباً (هاسلام/فرانسيس vs. هورفيتز/ويكفيلد) — لم يُدمجا لأن كل ملف كان قيد تحرير من subagent مختلف بالتوازي؛ سُجِّل التداخل صراحة في `gaps` مع رابط `related` متبادل بينهما ليقرر رئيس التحرير الدمج لاحقاً.

## قرارات محتوى بارزة
- dbt-bundle-theory-vs-substance-self: هيوم (1739) ضد ديكارت (1641)، مع ربط للأناتا البوذية وامتداد بارفيت (1984).
- dbt-care-ethics-vs-justice-ethics: صُحح العنوان من "رولز وكانط" الخاطئ إلى الطرفين الفعليين — غيليغان (1982) ضد كولبرغ — مع إحالة صريحة لتفادي التكرار مع dbt-heinz-dilemma-kohlberg-gilligan الموجود مسبقاً (لم يُلمس، لا يزال قالبياً، يحتاج معالجة مستقبلية).
- dbt-divine-attributes-kalam-tanzih-vs-tashbih / dbt-divine-command-theory-vs-autonomous-ethics: أُعيدا حول نزاعات كلامية إسلامية حقيقية (المعتزلة/الأشعرية/الأثرية) بدل القالب العام، وصُحح `belongs_to` من نص حر ("علم الكلام") إلى slugs حقيقية (sch-ashariyya، sch-mutazila).
- dbt-decolonial-delinking-vs-global-modernity: مينيولو (2007) ضد أريف ديرليك (2007) — لا ملف thk- لديرليك، سُجِّل بدل الاختراع.
- dbt-deliberative-vs-agonistic-democracy / dbt-deliberative-vs-radical-democracy: فُرِّق بينهما تحريرياً بوضوح (خلاف موف الفردي مع هابرماس حول agonism vs. نظرية الهيمنة المشتركة لموف ولاكلاو) — لم يُدمجا، إحالة متبادلة مضافة.
- dbt-disability-social-model-vs-medical-model: مايك أوليفر (1983) لا يملك ملف مفكر — طُلب slug جديد بدل الاختراع.

صفر slugs مخترعة. عدة حالات غموض (أوليفر، ديرليك، فان إنواغن، فرانكفورت، هورفيتز/ويكفيلد كأشخاص) سُجِّلت في `agents_specs/requests-minimax.md`/`gaps` بدل الربط أو الاختراع.

## متوقف عنده (لرئيس التحرير)
- **تداخل يحتاج قرار دمج**: dbt-diagnostic-concept-creep / dbt-concept-creep-psychiatry.
- dbt-heinz-dilemma-kohlberg-gilligan.md لا يزال قالبياً — يستحق نفس معالجة Task 11 في دفعة لاحقة رغم وجوده خارج نطاق أرقام debates/critiques الرسمية لهذه الدفعة.
- طلبات slug جديدة: thk-mike-oliver، thk-arif-dirlik، thk-van-inwagen، thk-harry-frankfurt، thk-ge-moore، thk-aj-ayer (تحقق من عدم وجودهم أولاً قبل الإنشاء الفعلي في Task 15/13).

## الملفات
dbt-bundle-theory-vs-substance-self, dbt-care-ethics-vs-justice-ethics, dbt-categorical-vs-dimensional-diagnosis, dbt-categorical-vs-dimensional-rdoc-vs-dsm, dbt-categorical-vs-dimensional, dbt-categorical-vs-hitop-dimensional, dbt-cbt-third-wave-vs-second-wave, dbt-chemical-imbalance-myth-neuroplasticity, dbt-cognitive-deficit-vs-distortion, dbt-cognitivism-vs-non-cognitivism-ethics, dbt-common-factors-vs-specific-ingredients, dbt-compatibilism-vs-incompatibilism, dbt-concept-creep-psychiatry, dbt-conversion-therapy-harm, dbt-cosmopolitanism-vs-communitarian-patriotism, dbt-cosmopolitanism-vs-nationalism, dbt-couples-therapy-vs-individual-depression, dbt-creation-ex-nihilo-vs-eternity-of-world, dbt-creativity-vs-pathology, dbt-cult-recovery-methods, dbt-cultural-bias-iq-testing, dbt-decolonial-delinking-vs-global-modernity, dbt-deliberative-vs-agonistic-democracy, dbt-deliberative-vs-radical-democracy, dbt-deontology-vs-virtue-ethics, dbt-diagnostic-concept-creep, dbt-disability-social-model-vs-medical-model, dbt-divine-attributes-kalam-tanzih-vs-tashbih, dbt-divine-command-theory-vs-autonomous-ethics, dbt-ect-efficacy-and-ethics
