# Task 3.4
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد). تغطي شخصيات فلسفية/لاهوتية كبرى (أوغسطين، بيكونين، بارث، بوفوار) وشخصيات إكلينيكية مؤسِّسة (آرون بيك).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-becker، thk-ben-sira)
- **أخطر اكتشاف في الدفعة**: `thk-attig` كان يحمل تاريخ وفاة مختلَق بالكامل (2019) — الشخص **حي فعلاً** حتى الآن. صُحح لمواليد 1945 بلا تاريخ وفاة.
- **أخطاء هوية/جغرافيا جسيمة**:
  - `thk-augustine`: خلط بين مسقط رأسه (طاغاست) ومقر أسقفيته (هيبو/عنابة) — صُحح التمييز.
  - `thk-aulagnier`: بلد ميلادها كان خطأً "بولندا"؛ الصحيح إيطاليا (ميلانو) — صُحح بمصدر خارجي.
  - `thk-basilides`: خلط بين "سيمون الساحر" و"سمعان القيرواني" في رواية الصلب الغنوصية — صُحح.
  - `thk-benthall`: شك جوهري في هوية صاحب الملف نفسه (لا يوجد أنثروبولوجي بريطاني موثّق بهذا الاسم كتب عن السيانتولوجيا؛ الاسم الأقرب Jonathan Benthall مختلف) — **لم يُصحَّح، وُثِّق كشك يحتاج قرار Task 2**.
- **أخطاء تصنيف/ربط (id/title متضاربة أو slug مختلَق)**:
  - `thk-bas-van-fraassen`: رابط `thk-kuhn` كان يُستخدم للإشارة لتوماس كون (فيلسوف العلم) بينما الـslug الفعلي "رولاند كون" (طبيب نفسي مختلف تماماً) — صُحح إلى `thk-thomas-kuhn`. **نمط خطر يستحق فحصاً أوسع.**
  - `thk-aurobindo`: رابط `thk-sheena-iyengar` مقروناً بعنوان "ب.ك.س. آينغار" (شخص مختلف) — صُحح.
  - `thk-bartlett`: عنوان رابط لا يطابق عنوان الملف الحقيقي حرفياً — صُحح.
- **أخطاء نسبة/تواريخ نشر**:
  - `thk-bakunin`: عمل مؤرَّخ خطأً 1842 (فعلياً عمل مختلف تماماً)؛ العمل الصحيح 1862 — صُحح.
  - `thk-basil-caesarea`: تأريخ عظاته صُحح من 370 إلى ~378.
  - `thk-bataille`: `active_end` كان يقطع 5 سنوات من نشاطه الفعلي — صُحح من 1957 إلى 1962.
  - `thk-beauvoir`: `active_end` كان يقطع 16 سنة من نشاطها — صُحح من 1970 إلى 1986.
  - `thk-beck`: خلط بين عنوان الكتاب الأصلي 1967 وإعادة إصداره 1972 — صُحح.
- **محتوى مختلَق حُذف بالكامل**: `thk-bas-van-fraassen` (مقال ونسبة عمل غير موجودين)، `thk-bakunin`/`thk-baker` (كتب غير موثقة)، `thk-benthall` (عمل 2018 غير موثّق)، `thk-bbcohen` (8 روابط related بلا أي سند في المتن).
- **محتوى تفسيري حساس أُضيف بتوجيه صريح من التاسك**: `thk-bbettelheim` — فقرة توضح أن نظرية "الأم الثلاجة" مرفوضة علمياً وتاريخياً (المتن الأصلي كان صامتاً عن هذا التفنيد رغم أن الكتاب المذكور يفترضها).
- **تعارض عابر للتاسكات**: `thk-batkinson` كانت لسه رابطة بـ`thk-ecolle` المحجورة في Task 2 — حُذفت.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{attig,augustine,aulagnier,aurobindo,axel-honneth,baal-shem-tov,bacal,bachelard,badawi,badiou,baker,bakunin,bally,bargdill,barlow,barnes,barrett,barth,bartlett,bas-van-fraassen,basaglia,basil-caesarea,basilides,bataille,bateman,batkinson,baynes,bbcohen,bbettelheim,bboyesen,beauvoir,beck,benthall}.md
→ مخالفة واحدة false positive في thk-barnes (كلمة "العالم" بمعنى "the world" التقطها فحص الجندر الميكانيكي كـ"عالم" مذكر — متن الملف مؤنث صحيح بالكامل، لم يُعدَّل). باقي 32 ملفاً: ✅ صفر مخالفات.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. جميع الملفات الـ33 التي كتبت لها مسودة خضعت للترتيب الستة كاملاً، وحُذفت منها جملة/جمل القائمة السوداء أينما وُجدت.

## متوقف عنده (لرئيس التحرير)
- **thk-benthall**: هوية صاحب الملف نفسها مشكوكة — مرشح مباشر لتطبيق Task 2 (موثّق/غير موجود/غامض) بدل ترقيته كما هو.
- **thk-bas-van-fraassen ↔ thk-kuhn**: خطأ ربط توماس كون بـslug شخص آخر تماماً — يستحق فحصاً أفقياً في ملفات أخرى قد تستخدم نفس الـslug الخاطئ. لاحظ الـsubagent أيضاً ازدواج slug فعلي (`thk-thomas-kuhn` و`thk-pkuhn` كلاهما لتوماس كون نفسه) يستحق دمجاً منفصلاً.
- **thk-attig**: خطأ "تاريخ وفاة مختلَق لشخص حي" فئة أعلى خطورة من المعتاد — يستحق فحصاً مماثلاً في ملفات أخرى بنفس النمط.
- **thk-aulagnier**: تصحيح بلد الميلاد (بولندا→إيطاليا) مبني على بحث خارجي، يستحق مراجعة بشرية إضافية.
- **thk-bachelard**: `belongs_to` صُحح بالاجتهاد إلى `sch-phenomenology-existential` (تحققت من وجوده في EXISTING_SLUGS) — يستحق تأكيد رئيس التحرير أنه التصنيف المقصود.
- **thk-bbcohen**: تفريغ شبكة `related` بالكامل (8 روابط غير مسندة) — الملف الآن بلا أي رابط، يحتاج تعميقاً لاحقاً (Task 4).
- **thk-bbettelheim**: إضافة فقرة نقدية عن "الأم الثلاجة" محتوى تفسيري إضافي وليس تصحيح واقعة بحتة — يستحق مراجعة.
- **thk-basilides**: خطأ خلط الأسماء الغنوصية قد يتكرر في ملفات أخرى تتحدث عن نفس الرواية (مثل thk-valentinus).

## الملفات
content/ar/thinkers/thk-attig.md
content/ar/thinkers/thk-augustine.md
content/ar/thinkers/thk-aulagnier.md
content/ar/thinkers/thk-aurobindo.md
content/ar/thinkers/thk-axel-honneth.md
content/ar/thinkers/thk-baal-shem-tov.md
content/ar/thinkers/thk-bacal.md
content/ar/thinkers/thk-bachelard.md
content/ar/thinkers/thk-badawi.md
content/ar/thinkers/thk-badiou.md
content/ar/thinkers/thk-baker.md
content/ar/thinkers/thk-bakunin.md
content/ar/thinkers/thk-bally.md
content/ar/thinkers/thk-bargdill.md
content/ar/thinkers/thk-barlow.md
content/ar/thinkers/thk-barnes.md
content/ar/thinkers/thk-barrett.md
content/ar/thinkers/thk-barth.md
content/ar/thinkers/thk-bartlett.md
content/ar/thinkers/thk-bas-van-fraassen.md
content/ar/thinkers/thk-basaglia.md
content/ar/thinkers/thk-basil-caesarea.md
content/ar/thinkers/thk-basilides.md
content/ar/thinkers/thk-bataille.md
content/ar/thinkers/thk-bateman.md
content/ar/thinkers/thk-batkinson.md
content/ar/thinkers/thk-baynes.md
content/ar/thinkers/thk-bbcohen.md
content/ar/thinkers/thk-bbettelheim.md
content/ar/thinkers/thk-bboyesen.md
content/ar/thinkers/thk-beauvoir.md
content/ar/thinkers/thk-beck.md
content/ar/thinkers/thk-becker.md
content/ar/thinkers/thk-ben-sira.md
content/ar/thinkers/thk-benthall.md
