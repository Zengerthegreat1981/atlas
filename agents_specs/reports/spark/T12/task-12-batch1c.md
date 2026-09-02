# Task 12 (contexts — دفعة 1c)
الحالة: مكتمل | العملية: تعميق وتوثيق `ctx-` بأسماء وتواريخ محققة خارجياً | الملفات: 10

## الأرقام
ملفات معدَّلة: 10/10 — كل ملف أضيف له `## المصادر` (2-3 مراجع) وgaps دقيقة محددة الحقل الناقص بدل الصيغة القالبية.

## أمر التحقق
`python3 scripts/build_slug_index.py` → نجح، 6906 عنصر مفهرس (6621 معتمد + 285 مسودة). تحذير تعارض الـslugs الظاهر (1116) حالة موروثة سابقة على هذه الدفعة وغير متعلقة بالملفات العشرة.

## قرارات اتخذتها
- **ctx-bolshevik-revolution-soviet-state**: أضفت تواريخ محددة (أكتوبر 1917، كرونشتاد 1921، المؤتمر العاشر، وفاة فيغوتسكي 1934، بعثتا أوزبكستان 1931-32) بدل الفقرات العامة. أضفت `country` و`active_start/end`.
- **ctx-buddhist-psychology**: صححت/دققت تاريخ تأسيس MBSR (1979) وربطته بجامعة ماساتشوستس، وحددت عدد عوامل الأبهيدارما (52 في التيرافادا).
- **ctx-byzantine-constantinople-preservation**: أضفت أسماء دقيقة (خريسولوراس 1397، مجمع فلورنسا 1439، هبة بيساريون لسان ماركو 1468، نقد فالا النصي) لاستبدال الجمل العامة.
- **ctx-cairo-al-azhar-fatimid-mamluk**: صححت تاريخ تأسيس البيمارستان المنصوري/القلاووني (1284)، وربطت ابن خلدون بتاريخ استقراره الفعلي بالقاهرة (1382).
- **ctx-chestnut-lodge-inpatient-psychoanalysis**: أضفت اسم المؤسس (إرنست بولارد 1910)، تاريخ عمل فروم-رايخمان (1935)، والاسم الحقيقي لمؤلفة الرواية (جوانا غرينبرغ) وقضية أوسهيروف 1982 كنقطة تحول تاريخية موثقة.
- **ctx-civil-rights-liberation-psychology**: الملف كان غنياً بالفعل بروابط `exp-`؛ ركزت على تعميق المتن (اغتيال مارتين-بارو 1989، تاريخ اختبار الدمى، فانون بالتفصيل) بدل إضافة روابط جديدة. صححت gaps من الصيغة القالبية إلى فجوات محددة.
- **ctx-classical-islamic-golden-age**: صححت خطأ مطبعي في الأصل ("ابن والرازي" → "ابن سينا والرازي")، وأضفت تاريخ بيمارستان النوري (1154) ومقارنته ببدلام اللندني.
- **ctx-cognitive-revolution-1950s** و**ctx-cognitive-revolution-neuroscience**: ميّزت بينهما صراحة — الأول للحظة التأسيس 1956 (ميلر/تشومسكي/سايمون)، والثاني للاندماج مع علوم الأعصاب من أواخر السبعينيات (غازانيغا/سبيري/كانمان-تفرسكي)، مع إشارة متبادلة صريحة في متن ملف علوم الأعصاب لتفادي التكرار. صححت خطأ تكرار حقل `part` في frontmatter الثاني أثناء الكتابة.
- **ctx-cold-war-psychology-behavior**: أضفت تفاصيل MK-Ultra الدقيقة (1953، ألن دالاس، دونالد كاميرون، إتلاف الوثائق 1973، جلسات 1977).

جميع روابط `related` تحققت مقابل `EXISTING_SLUGS.md` وكلها ✅ معتمدة ومطابقة العنوان.

## متوقف عنده (لرئيس التحرير)
لا شيء — كل الملفات مكتملة بمعيار القبول الكامل (مصادر، gaps محددة، لا جمل من القائمة السوداء).

## الملفات
content/ar/contexts/ctx-bolshevik-revolution-soviet-state.md
content/ar/contexts/ctx-buddhist-psychology.md
content/ar/contexts/ctx-byzantine-constantinople-preservation.md
content/ar/contexts/ctx-cairo-al-azhar-fatimid-mamluk.md
content/ar/contexts/ctx-chestnut-lodge-inpatient-psychoanalysis.md
content/ar/contexts/ctx-civil-rights-liberation-psychology.md
content/ar/contexts/ctx-classical-islamic-golden-age.md
content/ar/contexts/ctx-cognitive-revolution-1950s.md
content/ar/contexts/ctx-cognitive-revolution-neuroscience.md
content/ar/contexts/ctx-cold-war-psychology-behavior.md
