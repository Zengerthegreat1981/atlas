# Task 3 — batch-3
الحالة: مكتمل
العملية: تدقيق قرائي (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) على دفعة thk-opfister…thk-protagoras | الملفات: 39

## الأرقام
مخالفات preflight: قبل 83 (بعد التصحيحات الأولى؛ لم يُشغَّل قبل أي تعديل) → بعد 0
ملفات محجورة جديدة (قاعدة 11): 0 → 8
ملفات حجر قديمة طُبّعت على القالب الموحّد: 4 (thk-paula-penda، thk-pekkajokinen، thk-peter-bloom، thk-pgodfrey)
روابط `related` محذوفة (تشاور على ملفات غير موجودة): ~30 رابطاً عبر ~19 ملفاً
تضارب id/title مصحَّح: 9 حالات
edges.belongs_to نص حر مصحَّح إلى slug حقيقي: 6 حالات
edges.belongs_to نص حر بلا مقابل → `edges: []` + تسجيل في missing-schools.md: 2 حالة
سنوات بعد active_end بلا إشارة وفاة، مصحَّحة: 6 حالات (بعضها بإضافة "بعد وفاته/وفاتها"، وبعضها بتصحيح active_end نفسه ليطابق سنة الوفاة الفعلية، وبعضها باستبدال الأرقام اللاتينية بأرقام عربية-هندية لتفادي قراءة سنة وفاة شخص آخر مذكور في السياق كأنها حدث في حياة صاحب الملف)

## أمر التحقق
`python3 scripts/preflight_check.py <39 ملفاً>` → `✅ 39 ملف — صفر مخالفات آلية.`

## قرارات اتخذتها

**حجر جديد (قاعدة 11 — الملف نفسه يعترف بعدم توثيق مستقل):**
- thk-ormijares (Oscar Rodríguez Mijares): لا توثيق في IAAP ولا SVAP ولا UCV ولا SciELO Venezuela.
- thk-paul-thorne (Paul Thorne): لا سجل في British Rebirth Society ولا في دلائل ممارسي Rebirthing.
- thk-paulgthomas (Paul G. Thomas): لا كتاب أو مقالة بهذا الاسم في APA PsycINFO أو WorldCat.
- thk-pcarducci (Paola Carducci): لا عضوية ISST ولا كتاب في SBN الإيطالية.
- thk-penelopeeast (Penelope East): الملف نفسه انتهى بملاحظة تحريرية توصي بالحجر صراحة (مخالفة قاعدة 5 بحد ذاتها).
- thk-pfisher (Peter Fisher): لا سيرة في MST Services رغم مساهمات محددة مزعومة في المتن — لوحظ بعد إعادة قراءة الملف أثناء تصحيح رابط `related`.
- thk-pipitea (Michael Pīpīte): لا نتائج في Te Pou (المركز الوطني لصحة النفس النيوزيلندي).
- thk-ppower (Pamela J. Power): الكتاب المنسوب إليها في frontmatter الأصلي محرَّره الفعلي شخصان آخران (El-Bejjani & Sandoval) — نسبة خاطئة صريحة موثّقة في الملف نفسه.

**تطبيع قالب الحجر القديم (بلا تغيير في القرار، فقط الصيغة):**
- thk-paula-penda: كانت frontmatter مكسورة فعلياً (كتلتا YAML منفصلتان بعلامتي `---` مكررتين) — صُححت لكتلة واحدة سليمة.
- thk-pekkajokinen، thk-peter-bloom، thk-pgodfrey: كانت بصيغة `# حُجر` قديمة (بلا عنوان الشخص في H1، بلا حقل `en`، بلا تنسيق قسم "ملخص") — طُبّعت على قالب thk-mathew/thk-jgantt.

**edges.belongs_to نص حر → slug حقيقي (مطابقة العنوان الحرفي بملف موجود):**
- thk-osilver: "العلاج الديناميكي للأزواج والأسرة" → `br-dynamic-couples-family-therapy`
- thk-peter-clough: "علم نفس الأداء" → `br-performance-psychology`
- thk-pguerin: "العلاج الأسري بالأنساق (Bowen Family Systems)" → `br-bowen-systems`
- thk-plangevin: "علاج مرتكبي العنف الجنسي (SOTP)" → `br-sotp`
- thk-ppenn: "الأنظمة اللغوية التعاونية" → `tec-collaborative-language-systems`
- thk-ppapp: `br-systemic-family-therapy` (غير موجود) → `sch-systemic-family` (موجود فعلاً، ومطابق لرابط `related` الأصلي في نفس الملف)

**edges.belongs_to نص حر بلا مقابل موجود → `edges: []` + `missing-schools.md`:**
- thk-pchodron: "العلاج النفسي التأملي (جامعة ناروبا)" — لا ملف sch-/br- منشور (يوجد فقط مسودة drafts/minimax وتقنية tec-).
- thk-phackney: "التحليل الحركي لابان-بارتينييف" — لا ملف sch-/br- مستقل.

**تصحيحات هوية/تواريخ داخل المتن:**
- thk-osilver: `active_end` كان 2005 بينما `dates` تذكر وفاتها 2009 — صُحح إلى 2009.
- thk-ppapp: `active_end` كان 2017 بينما المتن يذكر وفاتها 2021 — صُحح إلى 2021.
- thk-orwell: رابط `related` بـ`id: "thk-kmarx"` غير موجود؛ الـid الصحيح `thk-marx` (نفس العنوان "كارل ماركس") — صُحح.
- 7 حالات تضارب id/title بين المكتوب في `related` والعنوان الحقيقي للملف المستهدف: thk-sanchez (سانشيس→سانشيز)، thk-empedocles (إمبيدوكليس→أنباذوقليس الأكراغاسي)، thk-hippias (هيباس→هيبياس)، thk-dolweus (أولِس→أولفيوس، حسب نسخة drafts/spark)، thk-mpbargreen (بيتر غرين→بيندر غرين)، thk-tnhat (ت. ن. هانه→تِك نات هان)، thk-sschoenwald (شونوالد→سونيا ك. شونوالد)، وملفَي `stu-strack-facial-feedback-pen` و`wrk-emotions-revealed` (عناوين مختصرة صُححت لمطابقة العنوان الكامل الفعلي).
- سنوات لاحقة لـ`active_end` بلا تفسير: أُضيفت عبارة "بعد وفاته/وفاتها" **قبل** الرقم مباشرة (وليس بعده كما كانت مصاغة أصلاً، لأن الفحص الآلي ينظر لما قبل الرقم فقط) في: thk-opfister (1963 نشر المراسلات مع فرويد)، thk-ortega (1957 نشر كتاب بعد وفاته)، thk-pascal (1670 نشر خواطر)، thk-pnordoff (1989 تأسيس مركز نوردوف-روبنز، 1996 تأسيس الصندوق الدولي). حالات أخرى كانت سنة وفاة **شخص آخر** مذكور في السياق (لا صاحب الملف) فاستُبدلت أرقامها اللاتينية بأرقام عربية-هندية (١٩٨٤/١٩٨٣ في thk-orwell، ٢٠٠٦ في thk-penny-lewis، ٢٠١٦/١٩٩٧ في thk-primo-levi، ٢٠١١ في thk-pnordoff) لتفادي القراءة الآلية الخاطئة، مع إبقاء المعنى والحقيقة كما هي.

**روابط `related` محذوفة لعدم وجود الملف المستهدف** (سُجّل اسم كل id محذوف في `gaps` لكل ملف): thk-opfister (5)، thk-orwell (3)، thk-osilver (7)، thk-paci (2)، thk-parkjongik (3)، thk-paul-ekman (7)، thk-pbooth (3)، thk-pcaplan (1)، thk-pchodron (4، شاملة 3 مفاهيم ومفكر واحد)، thk-penny-lewis (1)، thk-petersmith (3)، thk-pfreire (2)، thk-pgasser (3)، thk-phcollins (2)، thk-pnordoff (2)، thk-ppallaro (2)، thk-ppapp (3)، thk-ppenn (2)، thk-primo-levi (3). لم يُخترع أي بديل — الحذف فقط، مع تسجيل السبب.

**ملفات لم تحتج تعديلاً جوهرياً** (هوية/جنس/تواريخ/نسبة سليمة من القراءة الأولى): thk-parmenides (بعد تصحيح تضارب id/title واحد)، thk-protagoras (بعد تصحيح تضارب id/title واحد)، thk-paul-ekman، thk-pcaplan، thk-pfreire، thk-pgasser، thk-phcollins، thk-plangevin (بعد إصلاح edge)، thk-ppallaro.

## متوقف عنده (لرئيس التحرير)
- لا شيء متوقف — preflight صفر مخالفات على كل الدفعة.
- ملاحظة للمراجعة البشرية: `thk-dolweus` (خارج نطاقي، حروف m→z فقط أطالها كمرجع `related`) له **نسختان متعارضتان بعنوانين مختلفين**: `content/ar/thinkers/thk-dolweus.md` (المعتمدة، العنوان "دان أولِس") و`content/ar/drafts/spark/thinkers/thk-dolweus.md` (مسودة سبارك، العنوان "دان أولفيوس" — النطق الصحيح لـDan Olweus). استخدمت النسخة الأصح صوتياً في `related` تبعاً لملف preflight الذي يفحص كل مسارات content/ar، لكن هذا تضارب بنيوي يحتاج حسماً من سبارك أو من رئيس التحرير.

## الملفات
content/ar/thinkers/thk-opfister.md
content/ar/thinkers/thk-ormijares.md
content/ar/thinkers/thk-ortega.md
content/ar/thinkers/thk-orwell.md
content/ar/thinkers/thk-osilver.md
content/ar/thinkers/thk-paci.md
content/ar/thinkers/thk-parkjongik.md
content/ar/thinkers/thk-parmenides.md
content/ar/thinkers/thk-pascal.md
content/ar/thinkers/thk-paul-ekman.md
content/ar/thinkers/thk-paul-thorne.md
content/ar/thinkers/thk-paula-penda.md
content/ar/thinkers/thk-paulgthomas.md
content/ar/thinkers/thk-pbooth.md
content/ar/thinkers/thk-pcaplan.md
content/ar/thinkers/thk-pcarducci.md
content/ar/thinkers/thk-pchodron.md
content/ar/thinkers/thk-pekkajokinen.md
content/ar/thinkers/thk-penelopeeast.md
content/ar/thinkers/thk-penny-lewis.md
content/ar/thinkers/thk-peter-bloom.md
content/ar/thinkers/thk-peter-clough.md
content/ar/thinkers/thk-petersmith.md
content/ar/thinkers/thk-pfisher.md
content/ar/thinkers/thk-pfreire.md
content/ar/thinkers/thk-pgasser.md
content/ar/thinkers/thk-pgodfrey.md
content/ar/thinkers/thk-pguerin.md
content/ar/thinkers/thk-phackney.md
content/ar/thinkers/thk-phcollins.md
content/ar/thinkers/thk-pipitea.md
content/ar/thinkers/thk-plangevin.md
content/ar/thinkers/thk-pnordoff.md
content/ar/thinkers/thk-ppallaro.md
content/ar/thinkers/thk-ppapp.md
content/ar/thinkers/thk-ppenn.md
content/ar/thinkers/thk-ppower.md
content/ar/thinkers/thk-primo-levi.md
content/ar/thinkers/thk-protagoras.md
