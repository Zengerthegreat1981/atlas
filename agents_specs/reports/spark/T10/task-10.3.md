# Task 10.3
الحالة: مكتمل
المسار: spark | العملية: disorders+syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل + dsm5tr_code/icd11_code | الملفات: 30

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 10.3
→
=== تحقق Task 10.3 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **تكرار محتمل جديد اكتُشف**: dis-mdd.md (DIS-0002) ودis-major-depressive.md (DIS-0109) يغطيان نفس الكيان التشخيصي (اضطراب الاكتئاب الجسيم) بمحتوى مختلف تماماً (dis-mdd.md أكثر اكتمالاً بمعايير الأعراض التسعة واستثناء الفجيعة). لم يُحذف أو يُدمج أي ملف — كل ملف اكتمل بنفس المعيار، ووُثِّق في gaps كل ملف ملاحظة صريحة تسمّي الملف الآخر بدقة، تحتاج قرار محرر بشري. **هذا ثاني تكرار مكتشف بعد dis-bpd.md/dis-borderline-personality.md في 10.1.**
- dis-passive-aggressive-personality-historical.md: تشخيص تاريخي أُلغي رسمياً — dsm5tr_code/icd11_code = null مع سبب موثق.
- dis-other-specified-mental.md: فئة تصنيفية مظلة عامة لا اضطراب فردي محدد — القسم الفلسفي بُني على تناظر منطقي (معضلة Gettier) بدل مفهوم إكلينيكي مقابل مباشر، مع إفصاح صريح في النص إن هذا تناظر منطقي لا تطابق موضوعي.
- dis-frotteuristic (من 10.2) وملفات أخرى: أكواد null موثقة بسبب حيثما لا توجد ثقة كافية.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم حقيقية موجودة فعلاً (أمثلة: con-doing-mode-vs-being-mode, con-nafs-natiqa-rational-soul, con-dichotomy-of-control, con-god-complex, con-dream-interpretation, con-cartesian-doubt-method, con-freedom, con-sadness, con-memory, con-blind-will-to-life, con-body-schema, con-bad-faith, con-guilt, con-trauma, con-intersubjectivity, con-primary-emotion, con-grief, con-mind-body, con-addiction, con-fear, con-gettier-problem, con-pleasure, con-lived-body) — لا اختراع مفاهيم.
- تصحيحات preflight موجودة سلفاً عبر الدفعة (غير ناتجة عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة، حذف/تحويل كتل edges تشير لـ"classification-dsm-5-tr"/"classification-icd-11" (بعض الوكلاء حوّلوها إلى related بنفس الـid الصحيح بما أن هذين الملفين موجودان فعلاً بذلك الاسم، وبعضهم حذفها لعدم قبول شكل الـslug في edges تحديداً)، وحذف جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح".

## متوقف عنده (لرئيس التحرير)
- **dis-mdd.md ↔ dis-major-depressive.md**: تكرار كامل موثّق صراحة في gaps كل ملف — يحتاج قرار محرر بشري (دمج أم تمييز نطاق).
- **dis-bpd.md ↔ dis-borderline-personality.md** (من 10.1): نفس الحالة، لا يزال بانتظار قرار محرر.
- **dis-passive-aggressive-personality-historical.md**: تشخيص ملغى، قد يحتاج قرار دمج مع ملف حالي أو إبقاء منفصل للتوثيق التاريخي.

## الملفات
content/ar/disorders/dis-insomnia-disorder.md
content/ar/disorders/dis-intellectual-disability.md
content/ar/disorders/dis-intermittent-explosive.md
content/ar/disorders/dis-kleptomania.md
content/ar/disorders/dis-major-depressive.md
content/ar/disorders/dis-major-neurocognitive.md
content/ar/disorders/dis-male-hypoactive-sexual-desire.md
content/ar/disorders/dis-mdd.md
content/ar/disorders/dis-mild-neurocognitive.md
content/ar/disorders/dis-narcissistic-personality.md
content/ar/disorders/dis-narcolepsy.md
content/ar/disorders/dis-nightmare-disorder.md
content/ar/disorders/dis-obsessive-compulsive-personality.md
content/ar/disorders/dis-ocd.md
content/ar/disorders/dis-odd.md
content/ar/disorders/dis-opioid-use.md
content/ar/disorders/dis-other-specified-mental.md
content/ar/disorders/dis-panic-disorder.md
content/ar/disorders/dis-parkinsonism-medication.md
content/ar/disorders/dis-passive-aggressive-personality-historical.md
content/ar/disorders/dis-pedophilic-disorder.md
content/ar/disorders/dis-persistent-depressive-disorder.md
content/ar/disorders/dis-pica.md
content/ar/disorders/dis-premature-ejaculation.md
content/ar/disorders/dis-premenstrual-dysphoric-disorder.md
content/ar/disorders/dis-prolonged-grief.md
content/ar/disorders/dis-psychological-factors-medical.md
content/ar/disorders/dis-ptsd.md
content/ar/disorders/dis-pyromania.md
content/ar/disorders/dis-reactive-attachment.md
