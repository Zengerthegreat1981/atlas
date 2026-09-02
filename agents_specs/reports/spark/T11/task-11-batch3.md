# Task 11 — دفعة 3

الحالة: مكتمل
العملية: إضافة event_date/event_place + تدقيق أسماء وتواريخ خارجي + إزالة القائمة السوداء | الملفات: 9

## الأرقام
event_date/event_place مضافة: 0 → 9 ملفات
جمل من القائمة السوداء محذوفة: 2 ملف (manifesto، world-congress) → 0

## أمر التحقق
`python3 scripts/build_slug_index.py` → ✅ فهرس الـ slugs: 6906 عنصر (6621 معتمد + 285 مسودة). التعارضات الـ1116 المطبوعة قائمة موجودة أصلاً في المستودع (thk-* بين معتمد/مسودة) ولا علاقة لها بملفات events هذه الدفعة.

## قرارات اتخذتها
- **evt-vienna-circle-manifesto-1929**: كان المتن بالكامل قائمة سوداء (جمل عامة + "لا يوجد اقتباس"). أعيد كتابته بالكامل: بيان "الفهم العلمي للعالم" 1929، كاتبه الرئيسي أوتو نويرات بمساعدة هان وكارناب، أُهدي لموريتس شليك، نُشر بمناسبة مؤتمر براغ سبتمبر 1929. رابط `thk-rcarnap` (تأكدت من الـslug الصحيح — مش thk-carnap).
- **evt-vienna-psychoanalytic-institute-1925**: أضفت event_date/place، صححت crumb الخاطئ ("المدرسة الوجودية" ← "التحليل النفسي")، واستبدلت روابط `related` غير المبرَّرة في المتن (evt-europsy-standard-2001 وevt-founding-of-kyoto-school-1911 لا علاقة لهما) بروابط حقيقية مذكورة في النص: thk-freud، thk-deutsch، thk-afreud، thk-meitingon، وربط بملف الجمعية 1908.
- **evt-vienna-psychoanalytic-society-1908**: أضفت event_date/place. المتن كان يذكر بلويَر وأبراهام ويونغ ضمن "الأعضاء الأربعة عشر الحاضرين" فعلياً في اجتماع 11 يناير 1908 بفيينا — هذا غير مرجّح تاريخياً لأنهم كانوا في زيورخ/برلين وقتها؛ عدّلت الصياغة إلى "أعضاء مراسلين" بدل "حاضرين"، وحذفت عنوان شارع غير موثَّق ("فيرنغِل") كنت غير متأكد من صحته، وأضفت الفجوة في `gaps`.
- **evt-vietnam-veterans-ptsd-advocacy-1980**: صححت crumb الخاطئ، أضفت event_date/place، وصححت اسماً مشوَّهاً "تشيم سيتون" إلى "حاييم شاتان" (Chaim Shatan) — أحد قادة Rap Groups الموثّقين تاريخياً مع روبرت جاي ليفتون وتشارلز فيغلي.
- **evt-wednesday-psychological-society-1902**: أضفت event_date/place، صححت crumb، وصححت خطأ إملائي في اسم الشارع ("بيرغاس" ← "بيرغاسه 19" / Berggasse 19).
- **evt-weimar-congress-split-1911**: أخطر ملف في الدفعة — العنوان والـslug يشيران لـ"مؤتمر فايمار" لكن المتن بالكامل كان يصف استقالة أدلر من الرئاسة في فبراير 1911 فقط، بلا أي ذكر فعلي لمؤتمر فايمار (المؤتمر الدولي الثالث للتحليل النفسي، فايمار، 21–22 سبتمبر 1911 برئاسة يونغ). أعدت الكتابة لتصل الحدثين معاً بدقة تاريخية: استقالة الرئاسة فبراير 1911 → ظهور الانقسام دولياً في مؤتمر فايمار سبتمبر 1911 → الانشقاق النهائي وتأسيس "جمعية علم النفس الفردي" 1912. صححت crumb.
- **evt-world-congress-of-philosophy-first-1900**: قائمة سوداء بالكامل زي ملف حلقة فيينا. أعيد كتابته بمادة حقيقية: المؤتمر الدولي الأول للفلسفة، باريس 1–5 أغسطس 1900 ضمن المعرض العالمي، بتنظيم الجمعية الفلسفية الفرنسية، حضور راسل ووايتهيد وبوانكاريه، ولقاء راسل ببيانو الذي غيّر مسار عمله المنطقي.
- **evt-wyatt-v-stickney-1971**: أضفت event_date/place (فرّقت بين حكم مارس 1971 الأولي ومعايير أبريل 1972 التفصيلية)، صححت crumb وpart (من philosophy إلى psychology لأنه حدث في الطب النفسي/حقوق المرضى).
- **evt-yale-hull-neo-behaviorism-1935**: أضفت event_date/place. المتن الأصلي فيه تفاصيل مفرطة الدقة غير قابلة للتحقق (16 محاضرة بعينها، "قاعة جريفيث/Sterling Law Building"، اسم "أوسكار هِمِكَر" المشوَّه الذي لا يطابق أي اسم معروف في حلقة ييل — الأقرب هو O. H. Mowrer لكن التهجئة لا تطابق، فحذفته من المتن كاسم مؤكد ونقلته كسؤال مفتوح في gaps بدل تثبيته كحقيقة). أبقيت الأسماء الموثقة فعلاً: نيل ميللر، جون دولارد، كينيث سبنس.

## متوقف عنده (لرئيس التحرير)
- لا يوجد توقف كامل. الفجوات المتبقية (محاضر أرشيفية أصلية، تواريخ دقيقة لبعض الوقائع) موثّقة في `gaps` بكل ملف.

## الملفات
content/ar/events/evt-vienna-circle-manifesto-1929.md
content/ar/events/evt-vienna-psychoanalytic-institute-1925.md
content/ar/events/evt-vienna-psychoanalytic-society-1908.md
content/ar/events/evt-vietnam-veterans-ptsd-advocacy-1980.md
content/ar/events/evt-wednesday-psychological-society-1902.md
content/ar/events/evt-weimar-congress-split-1911.md
content/ar/events/evt-world-congress-of-philosophy-first-1900.md
content/ar/events/evt-wyatt-v-stickney-1971.md
content/ar/events/evt-yale-hull-neo-behaviorism-1935.md
