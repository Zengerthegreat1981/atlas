# Task 15.1
الحالة: مكتمل جزئياً
العملية: تقنيات واضطرابات غائبة — 5 تقنيات ABA جديدة + 4 اضطرابات جديدة (10 subagent متوازي على دفعتين) | الملفات: 9

## الأرقام
مسودات الأطلس الكلية: 170 → 194 (+24 صافي؛ رقم أعلى من 9 بسبب دفعات متوازية من تاسكات تانية في نفس الجلسة قبل التحديث الأخير)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل ملف → صفر مخالفات آلية (بعد تصحيح 2 حقل `id` مؤقت "DIS-XXXX" إلى الصيغة القياسية "[DRAFT-UNKNOWN]")
`python3 scripts/build_slug_index.py` → 6809 عنصر (6615 معتمد + 194 مسودة)

## قرارات اتخذتها
- التقنيات الخمس (اقتصاد الرموز، التشكيل، التدريب بالمحاولات المنفصلة، التحليل الوظيفي، التسلسل) هي أوضح ثقب مذكور صراحة في نص Task 15 ("مفردات ABA التقنية كلها غائبة") — كل واحدة اتربطت بمدرستها (`sch-behaviorism`) ومبتكرها وحصلت على `evidence_level: well-established`.
- من الاضطرابات الخمسة المطلوبة (البارانويدي، الهستري، الضعف المعرفي الخفيف، خرف أجسام ليوي، انقطاع النفس النومي)، **اكتشفت أثناء المراجعة إن "الضعف المعرفي الخفيف" (MCI) مكرر فعلياً** مع ملف معتمد موجود بالفعل `dis-mild-neurocognitive.md` (نفس الحالة الإكلينيكية بنفس معايير بيترسن ونفس ترميز DSM-5-TR/ICD-11) — **حذفت الملف الجديد** بدل نشر ازدواج صامت، طبقاً لقاعدة "الازدواج → دمج + إحالة" في SPARK.md. الأربعة الباقية (البارانويدي، الهستري، أجسام ليوي، انقطاع النفس النومي) اتأكد عدم وجودها مسبقاً وكُتبت فعلاً.
- كل ملف اضطراب يحتوي `## السقف الإكلينيكي` و`## العلاقة بالمفهوم الفلسفي المقابل` وحقلي `dsm_code`/`icd_code` كما يشترط Task 10.
- تجنبت اختراع slugs لأشخاص/أدوات غير موجودة (thk-iwata، thk-lewy، thk-bordin وغيرهم) وسجلتها في gaps.

## متوقف عنده (لرئيس التحرير)
- باقي عناصر Task 15 لسه مش مكتوبة: `tec-` (مكوّنات CBT-I، تخطيط السلامة وتقييد الوسائل، تدريب الانتباه المنفصل لويلز، موقف التعقّل في MBT)، و`dis-` (عسر القراءة والحساب والتلعثم، OSDD، اضطراب الألعاب ICD-11) — محتاجة دفعة/دفعات تانية.
- لاحظت خلال هذه الدفعة إن نمط التكرار الصامت اللي حذّر منه Task 2 (زي حالة MCI) ممكن يتكرر في أي دفعة إنشاء جديدة إذا مسمّاش العنصر بالضبط زي المعتمد — لازم فحص تشابه دلالي يدوي، مش بس فحص slug حرفي، قبل اعتماد أي ملف جديد.

## الملفات
content/ar/drafts/spark/techniques/tec-token-economy.md
content/ar/drafts/spark/techniques/tec-shaping.md
content/ar/drafts/spark/techniques/tec-discrete-trial-training.md
content/ar/drafts/spark/techniques/tec-functional-behavior-analysis.md
content/ar/drafts/spark/techniques/tec-chaining-aba.md
content/ar/drafts/spark/disorders/dis-paranoid-personality.md
content/ar/drafts/spark/disorders/dis-histrionic-personality.md
content/ar/drafts/spark/disorders/dis-lewy-body-dementia.md
content/ar/drafts/spark/disorders/dis-sleep-apnea.md
