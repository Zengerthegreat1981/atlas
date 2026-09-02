# Task 2.32
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها (Task 2): توثيق أو حجْر أو gaps دقيقة — دفعة مخصَّصة من 10 ملفات (thk-wiredu, thk-siger-brabant, thk-spivak, thk-mtsai, thk-nackerman, thk-rizzo, thk-rlindsl, thk-rscaer, thk-yishin, thk-mtutufurth) | الملفات: 10

## الأرقام
جمل القائمة السوداء: قبل 10 (سطر واحد في كل ملف تقريباً) → بعد 0
ملفات فيها `## المصادر`: قبل 0/10 → بعد 10/10
مخالفات preflight_check.py: قبل (لم يُفحص) → بعد 0/10 (بعد إصلاح مخالفتين ظهرتا أول تشغيلة)
قرار "غير موجود" (حجْر): 0
قرار "غامض" (سيبته زي ما هو): 0
قرار "موثّق" (أعيدت كتابته): 10

## أمر التحقق
`python3 scripts/preflight_check.py <الملفات العشرة>` → أول تشغيلة: مخالفتان (تطابق id/title في thk-rlindsl، وجملة gaps بصيغة تأكيد في thk-rscaer) — صُحّحتا. التشغيلة الثانية: `✅ 10 ملف — صفر مخالفات آلية.` (exit 0)

grep يدوي على القائمة السوداء الكاملة (17 جملة) على الملفات العشرة → 0 تطابقات.

ملاحظة: `python3 scripts/task.py verify minimax 2.32` لا ينطبق حرفياً على هذه الدفعة لأن أرقام الدفعات في `task.py` مولَّدة آلياً من ترتيب الملفات الكامل ولا تطابق قائمة الـ10 ملفات المخصَّصة يدوياً من رئيس التحرير (تجربة `task.py get minimax 2 32` أعطت مجموعة ملفات مختلفة تماماً). التحقق الفعلي تم بـ`preflight_check.py` + grep يدوي على القائمة السوداء كاملة كما هو موضح أعلاه.

## قرارات اتخذتها
- **thk-wiredu** (Kwasi Wiredu، 1931–2022، فيلسوف غاني): موثّق. صحّحت سنة الوفاة (كانت 2024 خطأً؛ توفي 2022). أضفت `## المصادر` بثلاث مراجع حقيقية (Philosophy and an African Culture 1980، Cultural Universals and Particulars 1996، A Companion to African Philosophy 2004). حذفت جملة القائمة السوداء من gaps واستبدلتها بفجوة محدَّدة عن تفاصيل حواراته مع Gyekye وMenkiti.
- **thk-siger-brabant** (Siger of Brabant، فيلسوف رشدي لاتيني، ق.13): موثّق. أضفت `## المصادر` (Van Steenberghen 1977، Putallaz & Imbach 1997، Dales 1984). حذفت جملة القائمة السوداء من gaps.
- **thk-spivak** (Gayatri Chakravorty Spivak): موثّق. صححت خطأ نسبة: النص كان ينسب كتاب *Of Grammatology* لديكارت خطأً — الكتاب لجاك دريدا وسبيفاك مترجمته فقط. أضفت `## المصادر`. حذفت جملة القائمة السوداء.
- **thk-mtsai** (Mavis Tsai، مؤسسة مشاركة لـFAP): موثّق. حذفت من `related` ثلاثة روابط (thk-shiggins، thk-ellis، thk-ecker) لأن المتن لا يذكر سبب علاقتها بأي منهم (مخالفة معيار القبول #4)، وأبقيت thk-fskinner بعد إضافة جملة تبرّرها في المتن (الأساس السلوكي الراديكالي لـFAP). أضفت `## المصادر`.
- **thk-nackerman** (Nathan Ackerman، رائد العلاج الأسري التحليلي): موثّق. حوّلت `edges.belongs_to` من نص حر "العلاج الديناميكي للأزواج والأسرة" إلى slug حقيقي موجود `br-dynamic-couples-family-therapy` (العنوان مطابق). أضفت `## المصادر`. حذفت جملة القائمة السوداء.
- **thk-rizzo** (Albert "Skip" Rizzo، الواقع الافتراضي وPTSD): موثّق. حوّلت `edges.belongs_to` من نص حر إلى slug حقيقي `br-vr-therapy`. صححت تضارب id/title في `related` (thk-jdifede كان مكتوباً "جوان ديفيد" والعنوان الحقيقي "جوان ديفيدي"). حذفت نص عربطة/رموز غريبة (Motion堂، DHAMMAD) من المتن. أضفت `## المصادر`.
- **thk-rlindsl** (Ogden R. Lindsley، تلميذ سكينر ومؤسس Precision Teaching): موثّق. صححت التواريخ (كانت "1922–[غير مؤكد]"؛ ليندزلي توفي 2004، مطابق لـactive_end الموجود أصلاً). صححت خطأ إسناد ذاتي في المتن ("مع Ogden Lindsley نفسه" — الشخص نفسه صاحب الملف). صححت تضارب id/title لـthk-fskinner في preflight الثانية. أضفت `## المصادر`.
- **thk-rscaer** (Robert Scaer، طبيب أعصاب وصدمة جسدية): موثّق. حوّلت `edges.belongs_to` من نص حر إلى slug حقيقي `sch-polyvagal-informed-therapy`. صححت خطأ إسناد ذاتي في المتن ("The Body Bears the Burden، مع R. Scaer" — هو نفسه المؤلف). أضفت `## المصادر`. أعدت صياغة سطر gaps الخاص بتواريخ الميلاد/الوفاة بعد أن رفضه preflight بصفته "تأكيد حقيقة" بدل تسمية فجوة.
- **thk-yishin** (Yoshimoto Ishin، مؤسس علاج نايكان): موثّق لكن بمصحّحات جوهرية. حذفت ادّعاءً خاطئاً بأن يوشيموتو "تلميذ موريتا في الجامعة" — لا علاقة أستاذية موثّقة بين الاثنين؛ نايكان نشأ من ممارسة "ميشيرابه" في مذهب الأرض الطاهرة البوذي، لا من مدرسة موريتا. حذفت ادّعاءً خاطئاً بأن "نايكان امتداد لمورينو" (Moreno مؤسس السيكودراما، لا علاقة له بنايكان). أزلت `edges.belongs_to` لأن الهدف `sch-naikan-therapy` موجود فقط كمسودة غير معتمدة في `drafts/minimax/schools/` وليس ملفاً حياً — سجّلت هذا في gaps بدل اختراع رابط لمسودة. أضفت `## المصادر` (Reynolds 1983، Krech 2001).
- **thk-mtutufurth** (Mpho Tutu van Furth): موثّقة كشخص حقيقي (ابنة ديزموند توتو، قسيسة أنغليكانية/أسقفية)، لكن المتن الأصلي كان يحتوي محتوى مختلقاً بالكامل تقريباً: إطار علاجي وهمي باسم "Ubuntu Therapy"، مقاربة وهمية "Shared Wound"، وكتاب غير موجود بعنوان *Feast on the Slaughter*، وادّعاء مشاركة في لجنة الحقيقة والمصالحة في التسعينيات لا دليل عليه. الفرونتماتر نفسه كان يحمل علامة تحذير صريحة `[DRAFT-UNKNOWN]` والمتن يقول "[تفاصيل السيرة غير موثّقة بدقة]" — وهو بالضبط نمط "التناقض بين ثقة الشكل وشك المحتوى" المذكور في القاعدة 11. أعدت كتابة الملف بالكامل بمواد حقيقية موثّقة فقط: كتابها المشترك مع والدها *Made for Goodness* (2010) وكتابها *Everyday Ubuntu* (2018)، ودورها في مؤسسة إرث ديزموند وليا توتو. حذفت روابط `related` الثلاثة غير المبرَّرة في المتن (thk-bdanner، thk-ttshishiku، thk-amncube) وسجّلتها في gaps. حوّلت `edges.belongs_to` إلى slug حقيقي `br-ubuntu-psychology`. أضفت `## المصادر`.

## متوقف عنده (لرئيس التحرير)
- لا يوجد. الدفعة كلها "موثّق" — لا حالات "غير موجود" (فلا إضافة لـ`quarantine-minimax.md`) ولا حالات "غامض".
- `thk-yishin`: `sch-naikan-therapy` موجودة فقط كمسودة (`content/ar/drafts/minimax/schools/sch-naikan-therapy.md`) — لو تمت ترقيتها لملف معتمد، يُضاف `edges.belongs_to` وقتها.
- الفجوة العامة: `python3 scripts/task.py verify minimax 2.32` غير قابل للتطبيق حرفياً على دفعة مخصَّصة يدوياً (راجع ملاحظة أمر التحقق أعلاه) — التحقق تم بالبديل الموصوف (preflight + grep يدوي شامل).

## الملفات
content/ar/thinkers/thk-wiredu.md
content/ar/thinkers/thk-siger-brabant.md
content/ar/thinkers/thk-spivak.md
content/ar/thinkers/thk-mtsai.md
content/ar/thinkers/thk-nackerman.md
content/ar/thinkers/thk-rizzo.md
content/ar/thinkers/thk-rlindsl.md
content/ar/thinkers/thk-rscaer.md
content/ar/thinkers/thk-yishin.md
content/ar/thinkers/thk-mtutufurth.md
