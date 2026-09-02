# Task 15.2
الحالة: مكتمل
العملية: كتابة الملفات الغائبة المحددة في task-15-gap-analysis.md | الملفات: 7 (لا 8 — تصحيح أدناه)

## الأرقام
techniques (tec-): +1 فعلياً (التحليل الوظيفي)
disorders (dis-): +6 (MCI، خرف جبهي-صدغي، خرف وعائي، عسر قراءة، عسر حساب، تلعثم)

## ⚠️ تصحيح اكتشفته أثناء التنفيذ
كتبت أولاً `tec-cbt-insomnia.md` (مكوّنات CBT-I) في drafts/spark/techniques، لكن `build_slug_index.py`
كشف فوراً أن **الملف موجود بالفعل معتمداً** في `content/ar/techniques/tec-cbt-insomnia.md` — بند
كان قد أُنجز فعلاً في وقت سابق ولم يظهر في فحص Task 15 الأولي لأن ذلك الفحص بحث فقط داخل
`drafts/spark/` لا في `content/ar/` المعتمد. **حذفت الملف المكرر فوراً** بعد اكتشافه (قبل كتابة أي
تقرير) واستبعدت هذا البند من فجوة Task 15 الفعلية. هذا يعني فجوة Task 15 الحقيقية كانت 7 ملفات لا 8
كما قُدِّر تقريبياً في task-15-gap-analysis.md.

## أمر التحقق
`python3 scripts/preflight_check.py` على الـ8 ملفات (قبل الحذف) → كشف التكرار عبر
`build_slug_index.py` لا preflight نفسه (preflight فحص فقط الروابط والقائمة السوداء، لم يفحص
تكرار slug مع المعتمد).
`python3 scripts/build_slug_index.py` بعد الحذف → ✅ 6932 عنصر (6621 معتمد + 311 مسودة)، صفر تعارض
جديد. تأكيد إضافي: بحث يدوي عن كل الـ7 slugs المتبقية في `content/ar/` كاملاً (لا drafts فقط) →
صفر تكرار مع المعتمد لأي منها.

## قرارات اتخذتها
- **tec-functional-behavior-analysis**: مستقل عن `tec-chaining-aba` الموجود (الأول تشخيصي/تقييمي
  يسبق التدخل، الثاني تدخلي لبناء سلوك جديد) — ربط توضيحي بينهما في المتن.
- **dis-mild-cognitive-impairment، dis-frontotemporal-dementia، dis-vascular-dementia**: الثلاثة
  تتبع نمط `dis-lewy-body-dementia` الحرفي (dsm_code/icd_code + السقف الإكلينيكي + العلاقة
  بالمفهوم الفلسفي المقابل)، مع تمييز صريح لكل نوع عن الأنواع الأخرى (نمط التدهور، الأعراض
  المبكرة المميِّزة) لتفادي التكرار الوصفي الفارغ بين الأربعة أنواع خرف الموجودة الآن.
- **dis-dyslexia وdis-dyscalculia**: رُبطا ببعضهما صراحة (تداخل جزئي، آليتان معرفيتان مختلفتان)؛
  لم أُدرج قسم "العلاقة بالمفهوم الفلسفي المقابل" لهذين الملفين تحديداً لعدم توفر رابط فلسفي حقيقي
  ومباشر بدرجة كافية في معرفتي الموثقة دون اختلاق صلة مصطنعة — مُسجَّل هذا كقرار واعٍ لا كسهو.
- **dis-stuttering**: رُبط بمفهوم "أفعال الكلام" لأوستن (`con-speech-acts-performatives`، مفهوم
  معتمد خارج مسار Spark، قراءة فقط) بصلة موضحة بالاسم والتاريخ في المتن.
- **dis-vascular-dementia**: أُضيف قسم فلسفي يربط بـ`axm-mind-body-problem` (بديهية معتمدة) بعد
  المسودة الأولى التي أغفلته سهواً — صُحِّح قبل preflight النهائي.

## متوقف عنده (لرئيس التحرير)
- لا شيء. **Task 15 مغلق فعلياً** بعد هذه الدفعة (الفجوة الحقيقية كانت 7 لا 8، والفرق مكوّن CBT-I
  الذي كان منجَزاً بالفعل في المسار المعتمد).

## الملفات
content/ar/drafts/spark/techniques/tec-functional-behavior-analysis.md
content/ar/drafts/spark/disorders/dis-mild-cognitive-impairment.md
content/ar/drafts/spark/disorders/dis-frontotemporal-dementia.md
content/ar/drafts/spark/disorders/dis-vascular-dementia.md
content/ar/drafts/spark/disorders/dis-dyslexia.md
content/ar/drafts/spark/disorders/dis-dyscalculia.md
content/ar/drafts/spark/disorders/dis-stuttering.md
