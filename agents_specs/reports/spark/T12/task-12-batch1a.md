# Task 12 — batch 1a (contexts)
الحالة: مكتمل
العملية: تعميق `ctx-` بمادة موثقة بأسماء/تواريخ + إصلاح روابط `related` + `## المصادر` + `gaps` دقيقة | الملفات: 10

## الأرقام
حجم المتن (تقريبي، بالحروف): قبل ~2,300–2,650 لكل ملف (وسيط عام واحد سطحي بلا مصادر) → بعد ~3,500–4,800 لكل ملف (فقرات بأسماء وسنوات محددة + `## المصادر`)

## أمر التحقق
`python3 scripts/build_slug_index.py` → ✅ فهرس الـ slugs: 6906 عنصر (6621 معتمد + 285 مسودة). التعارضات الظاهرة (1116) قائمة سابقاً بين المعتمد والمسودات ولا علاقة لها بهذه الدفعة.

## قرارات اتخذتها
- `ctx-1848-spring-of-nations-europe`: أزلت رابط `thk-mill` لعدم وجود إسناد نصي حقيقي لموقف ميل من ثورات 1848 داخل المتن؛ أضفت تواريخ دقيقة (24 فبراير، 13/18 مارس، بيان 1848، أيام يونيو، معركة فرانكفورت 1848-49).
- `ctx-african-colonial-partition-berlin`: صححت الرقم (13 دولة أوروبية + أمريكا، لا 14 دولة كما في النص الأصلي) وأضفت حالة الكونغو البلجيكية بالتفصيل (هوشيلد 1998) ورواندا-بوروندي كمثال ملموس للتمزيق الإثني، وتركت رقم ضحايا الكونغو في `gaps` تجنباً لعرض تقدير متنازع عليه كحقيقة.
- `ctx-alexandria-library-hellenism`: استبدلت الادعاء العام بتشريح "الجهاز العصبي والدماغ" بتفصيل هيروفيلوس/إراسيستراتوس التاريخي (تمييز الأعصاب الحسية/الحركية)، وربطت مقتل هيباتيا (415م) بالسياق السياسي-الديني بدقة بدل جملة عامة عن "الأفول".
- `ctx-algerian-revolution-fanon-anti-colonialism`: أهم قرار — رقم الشهداء (1.5 مليون) كان معروضاً كحقيقة مؤكدة في النص الأصلي بينما هو محل خلاف تاريخي حاد (ستورا: 300-400 ألف)؛ حوّلته إلى `gaps` صريحة بدل تأكيد أحادي.
- `ctx-american-pragmatism-tradition`: أزلت جملتي القائمة السوداء ("لا يوجد اقتباس مباشر موثوق متاح" مكررة مرتين) بالكامل، واستبدلتهما بمادة تاريخية موثقة (بيرس 1878، جيمس 1890/1907، ديوي 1916).
- `ctx-american-transcendentalism-concord`: صححت مدة إقامة ثورو في فالدن (عامان وشهران ويومان، لا "عامين" فقط) وربطت تأثيره بغاندي وكينغ بشكل محدد بدل جملة عامة.
- `ctx-ancient-athens-agora`: أضفت رابط توثيقي لمنهج آرون بيك في الاستجواب السقراطي (السبعينيات) كحلقة وصل فعلية للـ"الأثر السريري" بدل جملة مطاطة، وأشرت لتضارب الروايات حول رقم أصوات محاكمة سقراط (280 مقابل 220 تقريبي).
- `ctx-ancient-egypt-maat-cosmic-order`: أضفت رابطاً جديداً لـ `thk-amenemope` (موجود في الأطلس) لأن المتن الآن يناقشه صراحة (تعاليم آمنمؤبي مقابل سفر الأمثال)؛ صححت عدد قضاة الآخرة (42) بدل وصف عام.
- `ctx-ancient-sparta-discipline`: أضفت رابط `thk-aristotle` (تحقق وجوده في `EXISTING_SLUGS.md`) لأن نقده لدستور إسبرطة في *السياسة* الكتاب الثاني أصبح محور فقرة كاملة؛ نقلت أسطورة "apothetae" (ترك المولودين الضعاف) إلى `gaps` لأنها رواية متأخرة مثيرة للجدل تاريخياً بين الباحثين المعاصرين.
- `ctx-andalusian-philosophical-renaissance`: أضفت رابط `thk-ibn-bajjah` (موجود في الأطلس) بعد أن أصبح جزءاً فعلياً من سردية النسب الفكري في المتن؛ فصّلت تسلسل إدانات باريس (1270 و1277) بدل جملة عامة عن "ثورة فكرية".

## متوقف عنده (لرئيس التحرير)
- لا يوجد توقف؛ كل الملفات العشرة أُنجزت بالكامل ضمن معيار القبول.

## الملفات
content/ar/contexts/ctx-1848-spring-of-nations-europe.md
content/ar/contexts/ctx-african-colonial-partition-berlin.md
content/ar/contexts/ctx-alexandria-library-hellenism.md
content/ar/contexts/ctx-algerian-revolution-fanon-anti-colonialism.md
content/ar/contexts/ctx-american-pragmatism-tradition.md
content/ar/contexts/ctx-american-transcendentalism-concord.md
content/ar/contexts/ctx-ancient-athens-agora.md
content/ar/contexts/ctx-ancient-egypt-maat-cosmic-order.md
content/ar/contexts/ctx-ancient-sparta-discipline.md
content/ar/contexts/ctx-andalusian-philosophical-renaissance.md
