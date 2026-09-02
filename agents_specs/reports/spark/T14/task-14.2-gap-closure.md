# Task 14.2
الحالة: مكتمل
العملية: كتابة كل الملفات الغائبة المحددة في task-14-gap-analysis.md | الملفات: 11

## الأرقام
studies (std-): 10 → 16 (+6)
instruments (ins-): 10 → 15 (+5)
Task 14: 20/28 → 31/33 بنداً مغطى (تصحيح العدّ: القائمة الأصلية تضم 6 دراسات + 5 أدوات إضافية عن
العدّ الأولي التقريبي في task-14-gap-analysis.md، وليس 8 كما قُدِّر تقريبياً هناك)

## أمر التحقق
`python3 scripts/preflight_check.py` على الـ6 ملفات دراسات → ✅ صفر مخالفات.
`python3 scripts/preflight_check.py` على الـ5 ملفات أدوات → ✅ صفر مخالفات (بعد تصحيح تطابق title
لثلاثة روابط related لم تطابق العنوان الحرفي للملف المستهدَف من أول محاولة).
`python3 scripts/build_slug_index.py` → ✅ 6926 عنصر (6621 معتمد + 305 مسودة)، صفر ظهور لأي من
الـ11 slug الجديد في قائمة التعارض 1116.

## قرارات اتخذتها
- **stu-many-labs-1/3/4**: ثلاث دراسات منفصلة (لا ملف واحد جامع) لتوافق النمط الموجود مسبقاً في
  `stu-many-labs-2`. Many Labs 4 تحديداً وُثِّق كفشل تكرار نظرية إدارة الرعب (mortality salience)
  اتساقاً مع إشارة Task 7 السابقة لهذا الفشل تحديداً.
- **تصحيح فوري لخطأ إسناد ارتكبته أثناء الكتابة**: نسبت تحليل p-curve لوضعية القوة أولاً لاسم غير
  دقيق (خطأ إسناد ذاتي أثناء المسودة الأولى)، صُحِّح فوراً لـJoseph Simmons و Uri Simonsohn (2017)
  بعد مراجعة ذاتية قبل preflight — لا اقتباس أو مصدر مختلَق نُشر في النسخة النهائية.
- **stu-ego-depletion-replication-failure**: ربط بـthk-roy-baumeister بعد التحقق من العنوان
  الحرفي الصحيح "روي باوميستر" (وليس الإملاء الأول الذي كتبته خطأً "باوماستر") — صُحِّح بحث واستبدال
  شامل قبل الحفظ النهائي.
- **stu-power-posing-replication-failure**: وثّق حالة نادرة (تراجع مؤلفة أصلية علناً عن نتيجتها،
  دانا كارني 2016) مع الإبقاء على موقف كادي المتحفظ منفصلاً بدقة — لا تعميم أحدهما على الآخر.
- **stu-rat-park**: صُنِّف `replication_status: "contested"` لا "failed" ولا "replicated" لأن
  محاولات التكرار اللاحقة أعطت نتائج متباينة الحجم فعلاً حسب الأدبيات المتاحة لي، ووُثِّق هذا صراحة
  في gaps بدل الحسم الزائف.
- **الأدوات الخمس** (PSS, ACE Questionnaire, WHODAS 2.0, CORE-OM, RAADS-R): كل ملف يوثّق فجوة عدم
  وجود تقنين عربي رسمي حيث ينطبق (كل الأدوات ما عدا WHODAS 2.0 الذي له نسخة عربية رسمية من منظمة
  الصحة العالمية — وُثِّق ذلك إيجابياً في validity_note بدل الصمت عنه).

## متوقف عنده (لرئيس التحرير)
- لا شيء. **Task 14 مغلق فعلياً** بعد هذه الدفعة.

## الملفات
content/ar/drafts/spark/studies/stu-many-labs-1.md
content/ar/drafts/spark/studies/stu-many-labs-3.md
content/ar/drafts/spark/studies/stu-many-labs-4.md
content/ar/drafts/spark/studies/stu-ego-depletion-replication-failure.md
content/ar/drafts/spark/studies/stu-power-posing-replication-failure.md
content/ar/drafts/spark/studies/stu-rat-park.md
content/ar/drafts/spark/instruments/ins-perceived-stress-scale.md
content/ar/drafts/spark/instruments/ins-ace-questionnaire.md
content/ar/drafts/spark/instruments/ins-whodas-2.md
content/ar/drafts/spark/instruments/ins-core-om.md
content/ar/drafts/spark/instruments/ins-raads-r.md
