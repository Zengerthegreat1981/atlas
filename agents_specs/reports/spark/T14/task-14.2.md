# Task 14.2
الحالة: مكتمل جزئياً
العملية: دراسات وأدوات حديثة — الدفعة الثانية (5 دراسات + 5 أدوات، 10 subagent متوازي) | الملفات: 10

## الأرقام
مسودات الأطلس الكلية: 214 → 233 (+19 صافي)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل الـ10 ملفات → صفر مخالفات آلية
`python3 scripts/build_slug_index.py` → 6851 عنصر (6618 معتمد + 233 مسودة)

## قرارات اتخذتها
- الدراسات الخمس: Many Labs 2، دراستا وايتهول (I/II)، تجربة مينيسوتا للتجويع، تجارب غريفيثس للسيلوسيبين على قلق السرطان (2016)، تجارب MAPS للمرحلة الثالثة لـMDMA-PTSD. كل ملف اتربط بالمفاهيم المكتوبة في دفعات سابقة من نفس الجلسة (con-open-science-reform-psychology، con-psychedelic-renaissance) بدل تكرار نفس الصياغات.
- ملف `stu-whitehall-studies.md` مُصمَّم عمداً ليكمل (لا يكرر) `syn-whitehall` المعتمد أصلاً — الأول يوثّق تصميم الدراسة نفسها، الثاني يصف المتلازمة الناتجة.
- من الأدوات الخمس: SCL-90-R، CTQ، MINI، OQ-45، CAT-Q. لاحظت واستبدلت أثناء المراجعة رابطاً خاطئاً لأداة OQ-45 — الـsubagent اخترع slug غير موجود (`thk-mlambert`) رغم إن مايكل لامبرت (مبتكر الأداة) **موجود فعلاً** بـslug صحيح `thk-lambert` من دفعة الترحيل في Task 13 — صحّحت الرابط للـslug الحقيقي بدل ترك الفجوة أو استخدام الاسم الخاطئ.
- تجنبت اختراع thk-derogatis، thk-bernstein، thk-sheehan/thk-lecrubier، thk-laura-hull، thk-ancel-keys، thk-marmot — كلهم مسجَّلون كطلبات gaps.

## متوقف عنده (لرئيس التحرير)
- Task 14 قارب الاكتمال تقريباً — العناصر المتبقية غير المكتوبة: فشل تكرار استنزاف الأنا ووضعية القوة تحديداً (Many Labs 2 غطّى الإطار العام لكن مش هذين التأثيرين بالاسم)، ودراسة روبنز عن هيروين فيتنام سبق كتابتها في 14.1، وWHODAS 2.0 من الأدوات.
- **درس مستفاد لباقي الدفعات**: لازم أراجع روابط thk- المقترحة من الـsubagents ضد EXISTING_SLUGS.md بنفسي بعد كل دفعة، مش بس أثق في preflight الآلي — لأن الفحص الآلي بيتأكد إن الـslug (لو موجود) title متطابق، لكن مش بيتأكد إن الـsubagent "فوّت" ربط شخص موجود فعلاً تحت اسم مختلف قليلاً (زي thk-mlambert بدل thk-lambert).

## الملفات
content/ar/drafts/spark/studies/stu-many-labs-2.md
content/ar/drafts/spark/studies/stu-whitehall-studies.md
content/ar/drafts/spark/studies/stu-minnesota-starvation.md
content/ar/drafts/spark/studies/stu-griffiths-psilocybin-cancer.md
content/ar/drafts/spark/studies/stu-maps-mdma-phase3.md
content/ar/drafts/spark/instruments/ins-scl-90-r.md
content/ar/drafts/spark/instruments/ins-ctq.md
content/ar/drafts/spark/instruments/ins-mini-neuropsychiatric.md
content/ar/drafts/spark/instruments/ins-oq-45.md
content/ar/drafts/spark/instruments/ins-cat-q.md
