# Task 11.2
الحالة: مكتمل
العملية: debates+critiques: تسمية الطرفين/الناقد بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.2): صفر مخالفات آلية (30/30 ملف) بعد إصلاح يدوي لـ5 ملفات

## ⚠️ مخالفة قائمة سوداء اكتُشفت بالتحقق الذاتي وأُصلحت يدوياً
`task.py verify minimax 11.2` رجّع في أول تشغيل "5 جمل قائمة سوداء متبقية" رغم أن كل الـsubagents زعموا صفر مخالفات. السبب: الجملة المحظورة "لا يوجد اقتباس مباشر موثوق متاح" اتكتبت حرفياً داخل `gaps:` (مش المتن) في 5 ملفات — والقاعدة تمنعها في أي مكان بالملف:
- crt-critique-of-solution-focused.md
- crt-derrida-critique-of-logocentrism.md
- crt-critique-of-resilience-training.md
- crt-critique-of-self-help-genre.md
- crt-deleuze-guattari-critique-of-psychoanalysis.md

أُعيدت صياغة كل سطر gap ليصف الفجوة الفعلية (غياب اقتباس حرفي من المصدر الأساسي) بدون الجملة المحظورة. بعد الإصلاح: صفر مخالفات على الـ30 ملفاً.

**درس مستفاد**: لازم أتحقق بنفسي دايماً بـ`preflight_check.py`/`task.py verify` قبل اعتماد أي ادعاء "صفر مخالفات" من subagent.

## ⚠️ مصدر ملفَّق ثالث مؤكَّد — النمط بقى "منهجي"
`crt-critique-of-narrative-therapy.md`: استشهاد بـ"Cobb, 2007, Family Process" غير موجود — اتصلح بمصدر حقيقي: Barbara S. Held (1995), *Back to Reality: A Critique of Postmodern Theory in Psychotherapy*. هذا **ثالث** استشهاد ملفَّق مؤكَّد يُكتشف عبر Task 11 (بعد Felix Marton/Ronen Berg في 11.1، وSundland/Bavelas في crt-critique-of-solution-focused ضمن هذه الدفعة) — **النمط أصبح مؤكَّداً كمشكلة منهجية في critiques/، يستحق تدقيقاً شاملاً منفصلاً عن التنقية التسلسلية الحالية.**

مصادر مشكوك فيها إضافية اتصلحت في هذه الدفعة (أسماء/سنوات لم يُعثر عليها بالبحث المباشر، استُبدلت بمصادر حقيقية موثَّقة):
- crt-critique-of-resilience-training: استُبدل نص عام بـ Cederström & Spicer (*The Wellness Syndrome*, 2015) + Mark Neocleous (*Resisting Resilience*, 2013).
- crt-critique-of-self-help-genre: "Martin Barker, 2010" (غير موثَّق) → McGee (2005)، Salerno (2005)، Ehrenreich (2009)؛ حُذف رقم "70٪" غير مسنَد من المتن وسُجِّل في gaps كادعاء غير موثَّق.
- crt-critique-of-solution-focused: "Sundland 2012; Bavelas 2012" (غير متحقَّق) → Stalker, Levene & Coady (1999, *Families in Society*).
- crt-critique-of-somatic-experiencing: "CPA Position Statement 2018"، "Abramovitz 2013" (لا أثر) → Kuhfuß et al. (2021)، Grossman (نقد نظرية بورجز)، Brom et al. (2017).
- crt-critique-of-trauma-informed-care: "Wilson 2021" (غير موجود بهذا العنوان) → Berliner & Kolko (2016, *Child Maltreatment*, PMID 27152025).
- crt-critique-of-trauma-therapy: "Summerfield 2002, Journal of Humanitarian Assistance" (سنة/مجلة خطأ) → Summerfield (1999, *Social Science & Medicine*, PMID 10369444)، الكاتب حقيقي لكن الاستشهاد كان مغلوطاً.

في كل الحالات سُجِّلت الأسماء المستبعدة في `gaps` بدل حذفها بصمت.

## اكتشاف جانبي
`sch-trauma-psychology` مستخدم في `edges` عدة ملفات (crt-critique-of-somatic-experiencing وغيره، 8 ملفات على الأقل) لكنه **غير موجود فعلياً كملف مدرسة** — سُجِّل في `agents_specs/missing-schools.md` (ليس اختراعاً مني، استخدام سابق موجود).

## قرارات اتخذتها
- crt-foucault-death-of-man: أطروحة موت الإنسان (*الكلمات والأشياء*، 1966) وردّ سارتر الموثّق (مقابلة *L'Arc* 1966)؛ ربط بـ dbt-existential-freedom-vs-structuralist-determinism وcrt-derrida-critique-of-logocentrism.
- crt-gilligan-critique-of-kohlberg-moral-stages: نقد غيليغان (*In a Different Voice*، 1982) لسلّم كولبرغ مع معضلة هاينز؛ تأكيد thk-lkohlberg (لورنس) متمايز عن thk-gilligan (كارول) وthk-sgilligan (ستيف، معالج مختلف تماماً).
- crt-gorgias-critique-of-eleatic-ontology: حجة جورجياس العدمية ضد بارمنيدس، مع توثيق أن النص الأصلي مفقود ووصل فقط عبر سكستوس إمبيريكوس والمقالة المنسوبة زوراً لأرسطو — سُجِّل كفجوة بدل التظاهر باقتباس مباشر. حُذف قسم "اقتباسات مختارة" لعدم وجود اقتباس موثَّق.
- حذف روابط `related` غير مبرَّرة بالمتن في عدة ملفات (crt-popper-critique-of-historicism من ملف SE؛ crt-critique-of-solution-focused وcrt-baudrillard-critique-of-hyperreality وcrt-feminist-critique-behaviorism من ملف TIC).
- الحفاظ على أسلوب النثر الموحّد بالمجلد (تشكيل + ترجمة إنجليزية بين قوسين).

صفر slugs مخترعة (باستثناء تصحيح المصادر الملفَّقة أعلاه بأسماء حقيقية موثَّقة بحثياً).

## متوقف عنده (لرئيس التحرير)
- **⚠️ عاجل مؤكَّد**: نمط مصادر ملفَّقة/مشكوكة في critiques/ بقى **3 حالات مؤكدة + عدة "مشكوك فيها" أُصلحت احترازياً** عبر 11.1+11.2 — يستحق تدقيقاً منهجياً منفصلاً لباقي critiques/ (276 ملف).
- `sch-trauma-psychology` مفقود ويُستخدم في 8 ملفات على الأقل.

## الملفات (30، من 10 subagents)
crt-critique-of-resilience-training, crt-critique-of-self-help-genre, crt-critique-of-solution-focused, crt-critique-of-somatic-experiencing, crt-critique-of-trauma-informed-care, crt-critique-of-trauma-therapy, crt-foucault-death-of-man, crt-gilligan-critique-of-kohlberg-moral-stages, crt-gorgias-critique-of-eleatic-ontology, crt-derrida-critique-of-logocentrism, crt-deleuze-guattari-critique-of-psychoanalysis, crt-dussel-critique-of-eurocentrism, crt-fanon-critique-of-colonial-alienation, crt-feyerabend-critique-of-scientific-method, crt-feminist-critique-heidegger, crt-heidegger-critique-of-humanism, crt-heidegger-critique-of-technology, crt-hume-critique-of-miracles, crt-critique-of-narrative-therapy, crt-critique-of-positive-psychology, crt-critique-of-psychodynamic-therapy, crt-foucault-critique-of-asylum, وملفات إضافية من الدفعات 1/5/6/7/8/10 (تفاصيلها ضمن التعديلات أعلاه؛ preflight/verify رجّع 0/30 مخالفة على كامل الدفعة الرسمية).
