# Task 8.4
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40 (كل الـ40 التزموا بصيغة slug القصيرة من البداية — صفر تطبيع لازم هالمرة، بفضل توجيه أوضح فأوضح عبر الدفعات)
باقي مجلد schools/ بلا ## المصادر: 290 → 250

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تشغيل** (تحسّن كامل عن 8.2 و8.3 — التوجيه الصريح بـ"لا تلمس شيء تاني إلا مخالفة قديمة فعلية لازمة" قلّل التوسّع غير المقصود)

## قرارات اتخذتها
- تصحيحات إلزامية صغيرة عملها الـsubagents أنفسهم قبل التسليم (بدل ما أعمل تصحيحاً لاحقاً): إعادة صياغة عبارات `gaps` مطابقة للقائمة السوداء (sch-conceptualism، sch-confucian-early، sch-continental-rationalism، sch-contractualism)، حذف edges بنص حر بلا slug بديل (sch-conservatism-philosophical: حذف "الفلسفة السياسية المعاصرة"، sch-confucian-psychology: حذف "علم النفس عبر الثقافي" — كلاهما مسجّل بحاجة slug جديد).
- توحيد عناوين أقسام مصادر قديمة مكرّرة المعنى بدل تكرارها: sch-developmental (## المرجع الأساسي)، sch-emdr (## المرجع الأساسي)، sch-existential-therapy (## المرجع الموصى) — كل واحد أُعيدت تسميته لـ"## المصادر" فقط بلا تكرار محتوى.
- **sch-dbt.md**: كان فيه قسمان متداخلان تقريباً ("## المطبوعات التأسيسية الرئيسية" و"## المرجع الموصى للقراءة المُعمَّقة") — الـsubagent دمجهما بنفسه في "## المصادر" واحد بلا تكرار (قرار جيد، لم يحتج تدخلي).
- **sch-deism.md**: قسمان منفصلان شرعيان — "## المؤلفات المرجعية" (نصوص ربوبية أولية: تولاند، بولنجبروك، إلخ) و"## المصادر" الجديد (دراسات ثانوية أكاديمية عن الحركة) — تحققت إنهما مختلفا المضمون فعلاً، سِيبا كما هما.
- ملفات اكتفت بعدد مصادر أقل من 4 عمداً بدل الاختراع: `sch-dvaita-vedanta.md`، `sch-dogon.md`، `sch-donghak.md`، `sch-dreamtime.md`، `sch-eclecticism.md`، `sch-daoism-religious.md`، `sch-ethiopian-hataata.md` (3 لكل) — مادة أكاديمية محدودة لمدارس صغيرة/غير غربية، القرار الصحيح.
- `sch-decolonial-philosophy.md`: سجّل في gaps ملاحظة دقيقة أن `cultural_origin: "latin-american"` تغطي المفهوم المؤسِّس (كيخانو) لكن الحركة تضم روافد أفريقية/جنوب-جنوب لا يعكسها slug واحد بدقة — قرار صحيح بدل اختراع قيمة مركّبة تخالف الاتفاقية.

## متوقف عنده (لرئيس التحرير)
- طلبا slug جديد اتسجلوا (لازم إضافتهم لـ`requests-minimax.md`): "الفلسفة السياسية المعاصرة" (umbrella مفقود، ذُكر أيضاً كأولوية غائبة في MINIMAX.md Task 13) و"علم النفس عبر الثقافي" (umbrella مفقود لمدرسة/فرع أكاديمي).

## الملفات
content/ar/schools/sch-conceptualism.md
content/ar/schools/sch-confucian-early.md
content/ar/schools/sch-confucian-psychology.md
content/ar/schools/sch-existentialism.md
content/ar/schools/sch-conservatism-philosophical.md
content/ar/schools/sch-continental-rationalism.md
content/ar/schools/sch-contractualism.md
content/ar/schools/sch-cosmopolitanism.md
content/ar/schools/sch-critical-realism.md
content/ar/schools/sch-cynicism.md
content/ar/schools/sch-cyrenaic.md
content/ar/schools/sch-daoism-philosophical.md
content/ar/schools/sch-daoism-religious.md
content/ar/schools/sch-dbt.md
content/ar/schools/sch-decolonial-latin.md
content/ar/schools/sch-decolonial-philosophy.md
content/ar/schools/sch-deconstruction.md
content/ar/schools/sch-deep-ecology.md
content/ar/schools/sch-deism.md
content/ar/schools/sch-deliberative-democracy.md
content/ar/schools/sch-dependency-theory.md
content/ar/schools/sch-developmental.md
content/ar/schools/sch-dogon.md
content/ar/schools/sch-donghak.md
content/ar/schools/sch-dreamtime.md
content/ar/schools/sch-dvaita-vedanta.md
content/ar/schools/sch-eclecticism.md
content/ar/schools/sch-ecofeminism.md
content/ar/schools/sch-egyptian-maat.md
content/ar/schools/sch-eleatic.md
content/ar/schools/sch-emdr.md
content/ar/schools/sch-engaged-buddhism.md
content/ar/schools/sch-enlightenment.md
content/ar/schools/sch-environmental-ethics.md
content/ar/schools/sch-epicureanism.md
content/ar/schools/sch-ethiopian-hataata.md
content/ar/schools/sch-ethnophilosophy.md
content/ar/schools/sch-existential-therapy.md
content/ar/schools/sch-existentialism-atheist.md
content/ar/schools/sch-existentialism-religious.md
