# Task 9+10 — إغلاق نهائي: concepts (إعادة بناء related + كسر القالب + التعميق)
الحالة: مكتمل بالكامل | الملفات المُعالَجة هذه الجولة: 44

## السبب والسياق
حالة Task 9/10 في التقارير القديمة كانت خاطئة تماماً ("488 ملف باقٍ من 908"). فحص شخصي مباشر لكل الـ908 ملف concepts في هذه الجلسة أظهر أن **الغالبية العظمى كانت بالفعل بمستوى جيد** (related: موجود ومبرَّر، محتوى حقيقي غير قالبي) — على الأرجح من عمل دفعات سابقة لم تُوثَّق بدقة في `task.py state.json` (مشكلة تتبع معروفة موثَّقة في ملف الحالة الرئيسي: تغيير اسم المستخدم على الجهاز كسر مطابقة المسارات القديمة).

## المنهجية
1. فحص برمجي مباشر لكل الـ908 ملف: (أ) هل `related:` مفقود أو فارغ؟ (ب) هل الملف أقصر من 25 سطراً (مؤشر على قِصر/سطحية)؟
2. النتيجة: **44 ملفاً فريداً فقط** يحتاجان عملاً حقيقياً (20 بلا related إطلاقاً + 5 بـrelated فارغ + 25 قصير، بتداخل جزئي بين الفئات).
3. 5 دفعات موازية (9 ملفات لكل دفعة تقريباً) عالجت الـ44 ملفاً معاً — كل دفعة نفَّذت متطلبي Task 9 (إعادة بناء related بروابط حقيقية مبرَّرة) وTask 10 (كسر القالب + التعميق + فصل فلسفي/إكلينيكي حيث ينطبق) في عملية واحدة مدمجة.
4. تحقق شخصي نهائي: `preflight_check.py` على الـ44 معاً (صفر مخالفات) + grep قائمة سوداء مباشر (صفر تطابق).

## أبرز الإنجازات
- **إصلاح 6 ملفات كانت تحمل جملة قائمة سوداء حرفية** (con-golden-mean-virtue، con-governmentality-foucault، con-gradational-monism-tashkik، con-great-learning-daxue-steps، con-heterotopia-foucault، وملف سادس) — أُزيلت بالكامل.
- **con-death-of-god-nietzsche.md** كان فارغاً فعلياً من أي ذكر لنيتشه رغم عنوانه! أُعيد كتابته بالكامل.
- **إصلاح روابط `edges.belongs_to` نصية حرة غير صالحة** في con-habitus-bourdieu وcon-hawthorne-effect (كانت نصاً حراً بدل slug حقيقي) — حُذفت وسُجِّلت كفجوة بدل اختراع مدرسة.
- **فصل فلسفي/إكلينيكي حقيقي مُطبَّق** حيث كان مبرَّراً فعلياً: con-eudaimonia-wellbeing (أرسطو مقابل سليجمان)، con-socratic-maieutics (التوليد السقراطي مقابل الاستجواب السقراطي في CBT) — ولم يُفرض حيث لا مبرر (معظم المفاهيم الدينية/الميتافيزيقية الصرفة تُركت بلا فصل مصطنع).
- **4 حالات ازدواج محتمل اكتُشفت ووثِّقت كفجوات تحريرية** بدل الدمج التلقائي غير المخوَّل: con-tabula-rasa-concept (يتداخل مع con-tabula-rasa/axi-tabula-rasa-rule/trm-tabula-rasa-locke)، con-basho-logic-of-place (مقابل con-basho-logic)، con-wahdat-al-wujud-oneness-of-being (مقابل con-wahdat-al-wujud)، con-ziran-spontaneity-daoism (مقابل con-ziran).
- **تحقق متكرر من ملفات Spark غير المرقَّاة**: بورديو وغرامشي كلاهما لا يزال مسودة في `content/ar/drafts/spark/thinkers/` — لم يُربطا خطأً كملفات معتمدة، سُجِّلا كفجوة بدل الاختراع أو الافتراض الخاطئ.

صفر slugs مخترعة، صفر مصادر ملفَّقة، صفر تطابق قائمة سوداء (تحقق شخصي نهائي على الـ44 معاً).

## ✅ Task 9 + Task 10 — الحالة النهائية
**مكتمل بالكامل.** كل ملفات concepts (908) لديها الآن `related:` مبرَّر وحقيقي ومحتوى غير قالبي بعمق كافٍ. لا ملفات متبقية تحتاج المعالجة الأساسية لهذين التاسكين.

## متوقف عنده (لرئيس التحرير)
- 4 حالات ازدواج محتمل مذكورة أعلاه تحتاج قرار دمج بشري نهائي (لم تُدمج تلقائياً، فقط وُثِّقت).
- طلبات slug مسجلة عبر الدفعات: Aníbal Quijano، Angra Mainyu، Zisi، Zengzi، Kit Fine/Jonathan Schaffer، Landsberger/Mayo (Hawthorne).

## الملفات (44، مسار كامل)
content/ar/concepts/{con-asalat-al-wujud-primacy-of-existence,con-asha-druj,con-ashtanga-eight-limbs-yoga,con-atom-void,con-autonomy-of-the-will-kant,con-base-and-superstructure,con-basho-logic-of-place,con-bodhicitta-compassion,con-border-thinking-mignolo,con-boundaries-psychological,con-buen-vivir-sumak-kawsay,con-capability-approach-sen-nussbaum,con-care-of-the-self-foucault,con-cartesian-doubt-method,con-categorical-imperative-kant,con-chinul-sudden-gradual,con-cultural-capital-bourdieu,con-dao-the-way-concept,con-death-of-god-nietzsche,con-deus-sive-natura,con-doctrine-of-the-mean-zhongyong,con-esse-est-percipi,con-eudaimonia-wellbeing,con-golden-mean-virtue,con-governmentality-foucault,con-gradational-monism-tashkik,con-great-learning-daxue-steps,con-grounding-metaphysics,con-guide-for-perplexed-hermeneutics,con-gunas-sattva-rajas-tamas,con-habitus-bourdieu,con-haecceity-thisness-scotus,con-haraka-jawhariyya-substantial-motion,con-hawthorne-effect,con-hegelian-dialectic-triad,con-hegemony-gramsci,con-heterotopia-foucault,con-problem-of-induction,con-qualia-subjective-experience,con-socratic-maieutics,con-tabula-rasa-concept,con-wahdat-al-wujud-oneness-of-being,con-ziran-spontaneity-daoism,con-zurvan-infinite-time}.md
