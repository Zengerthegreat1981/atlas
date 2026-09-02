# تدقيق شامل لتعارضات slug بين المعتمد والمسودات (2026-09-01)

## الخلفية
1116 تعارض slug كانت موجودة (نفس اسم الملف موجود في `content/ar/` المعتمد وفي
`content/ar/drafts/` معاً — `build_slug_index.py` يرصدها تلقائياً). الافتراض الأول كان أنها كلها
مسودات قديمة متروكة بعد الاعتماد (نفس المحتوى). **الفحص الفعلي (بمقارنة كل زوج ملفين حرفياً عبر
28 دفعة تدقيق متوازية، كل دفعة ~40 زوجاً) كشف أن هذا الافتراض خاطئ لنسبة كبيرة من الحالات.**

## المنهجية
- بُني ديف (`diff`) نصي بين كل ملف معتمد ومسودة يحملان نفس الـslug.
- 28 subagent متوازٍ، كل واحد راجع ~40 زوجاً وأصدر حكماً واحداً من أربعة:
  - **DELETE**: المسودة نسخة قديمة زائدة، صفر معلومة فريدة ستُفقد بحذفها.
  - **APPROVED_DEFECT**: **الملف المعتمد نفسه فيه خطأ حقيقي** (اسم خطأ، تاريخ خطأ، إسناد خطأ،
    رابط/edge تالف) **والمسودة هي الأصح** — لا يجوز حذف المسودة، والملف المعتمد يحتاج تصحيحاً
    بشرياً (كلود) لأن Spark ممنوع من تعديل المعتمد.
  - **IDENTITY_CONFLICT**: الملفان يصفان **شخصين مختلفين حقيقيين** تحت نفس الـslug — الحالة الخطرة
    المذكورة صراحة في قاعدة SPARK.md رقم 6.
  - **UNCERTAIN**: تعذّر الحسم من الديف وحده، يحتاج بحثاً بشرياً إضافياً.

## الإجراء المتخذ فوراً
- **274 ملف DELETE** حُذفت فعلياً بعد المراجعة (تراجع تعارضات build_slug_index من 1116+2 إلى 836
  بعد هذه الدفعة، وسينخفض أكثر بعد معالجة الدفعات المتبقية).
- **لم يُلمَس أي ملف معتمد** (Spark ممنوع من هذا أصلاً) — كل حالات APPROVED_DEFECT موثّقة هنا فقط.
- **لم تُحذف** أي حالة APPROVED_DEFECT أو IDENTITY_CONFLICT أو UNCERTAIN — بقيت المسودة كما هي
  لحين مراجعة بشرية.

## ⚠️ حالات IDENTITY_CONFLICT (الأخطر — شخصان مختلفان تحت نفس الـslug)

| Slug | المعتمد يصف | المسودة تصف | ملاحظة |
|---|---|---|---|
| thk-gunnel-cederblad | Gunnel Cederblad (TA) | Marianne Cederblad (طب نفس أطفال) | اسمان أولان مختلفان تماماً |
| thk-amncube | "Albert Mncube" جنوب أفريقيا (غير موثّق) | Ncazelo Ncube، زيمبابوي | شخص حقيقي مختلف موثَّق |
| thk-dmercieca | "Eva Drewek-Mericka" (placeholder غير محلول) | Daniela Mercieca، أكاديمية حقيقية | placeholder احتل slug شخص حقيقي |
| thk-jacqueline-astington | "Jacqueline A. Astington" مرتبطة بـTA | Janet Wilde Astington، عالمة نفس نمو حقيقية | اسم أول مختلف بالكامل |
| thk-fkfu | F. K. Fu، باحث TEACCH | Frank H. Fu، أستاذ علوم حركية HKBU | شخصان مختلفان بنفس الحرفين الأولين |
| thk-dhanna | Frank Goldstein | Michael J. Goldstein | اسمان أولان مختلفان تماماً |
| thk-anajam | شخصية إسلامية نفسية مختلَقة | Adil Najam، أستاذ علاقات دولية حقيقي | المعتمد على الأرجح مختلَق بالكامل |
| thk-jlueger | John Lueger، مدرسة ألمانية | Robert J. Lueger، أستاذ Marquette الأمريكي | شخصان مختلفان |
| thk-calbright | Karen Albright | Ann Cooper Albright | شخصان مختلفان بنفس اللقب |
| thk-bdanner | Bernard Dannefer | Deborah Danner | جنس واسم مختلفان تماماً |
| thk-isaac-blind | إسحاق الإسرائيلي (طبيب، ق9-10) | إسحاق الأعمى (قبّالي، ق12-13) | القرون مختلفة بثلاثة قرون |
| thk-lonan | Lorena Onnis (معالجة أسرية) | Luigi Onnis (أستاذ رجل) | جنس مختلف تماماً |

**قرار مطلوب من رئيس التحرير لكل حالة أعلاه:** أيهما يحتفظ بالـslug؟ والآخر يحتاج slug جديداً
(يُسجَّل في `agents_specs/requests-spark.md`) بدل حذف محتواه — كلا الشخصين على الأرجح حقيقي ويستحق
ملفاً، فالحل ليس حذفاً بل فصل slug.

## 🔧 حالات APPROVED_DEFECT (الملف المعتمد فيه خطأ حقيقي — يحتاج تصحيح بشري، ~330+ حالة من 19 دفعة)

هذا أكبر فئة اكتشاف. أمثلة ذات وزن يستحق أولوية تصحيح عالية (ليست القائمة الكاملة — القائمة الكاملة
في ملفات JSON الخام إن احتجتها، لكن الحجم الكبير يجعل تلخيصها هنا أوضح):

**أخطاء إسناد/هوية جوهرية:**
- thk-amy-cuddy: المعتمد ينسب تراجع 2016 عن "وضعية القوة" لـ**داتشر كِلتنر**؛ الصحيح **دانا كارني**
  (المؤلفة الأولى الفعلية للورقة 2010، والمتراجعة الفعلية 2016) — تأكد هذا مستقلاً في
  `stu-power-posing-replication-failure.md` المكتوب هذه الجلسة.
- thk-jmitchell: المعتمد يسمّيها "Julia Mitchell" أمريكية؛ الصحيح Juliet Mitchell، بريطانية، محللة
  نفسية نسوية معروفة (مواليد 1940).
- thk-berne: خلط بين لعبة "Rapo" ومفهوم NIGYYSOB، وتوقيت نشر كتاب بعد الوفاة غير دقيق.
- thk-bhooks: يغفل اسمها الحقيقي (Gloria Jean Watkins) وينسب لها ابتكار "التقاطعية" خطأً.
- thk-carlos-castaneda: بلد ميلاد خطأ (البرازيل بدل بيرو).
- thk-james-allen: ينسب تأسيس New Thought لـ"فيلبس بروكس" بدل فينياس كويمبي الصحيح.
- thk-lgreenberg: يسمّي شريكة تأسيس EFT "روبرت رايس" بدل لورا إن رايس الصحيحة (خطأ جنس واسم معاً).
- thk-fperls: ينسب لبيرلز شريكة باسم خاطئ بدل لورا بيرلز الصحيحة.
- thk-cdenborough: David Denborough (الشخصية الحقيقية الموثقة في مركز Dulwich) مكتوب خطأ Chris.
- thk-gcecchin: رابط حقيقي (Boscolo، شريك تأسيس حقيقي) أُزيل خطأً من المعتمد.
- thk-al-mawardi: خطأ تاريخي (كلَّفه الخليفة العباسي القادر لا السلاجقة) + ادّعاء تأثير على
  مونتسكيو/لوك غير موثّق.
- thk-imartinbaro: خطأ جوهري في مسيرته الدراسية (لم يدرس في مدريد، بل تدرّب يسوعياً في بوغوتا/شيكاغو).
- thk-galileo-galilei: حقل `part` مضبوط خطأً "psychology" بدل "philosophy".
- thk-albert-einstein: نفس الخطأ (part خطأ يناقض crumb فلسفة الفيزياء).
- thk-khorney: حقل `part` خطأ (فلسفة بدل علم نفس) + حقل بلد ناقص (يغفل أصلها الألماني).
- thk-adam-smith: تصنيف خطأ (نفسي بدل فلسفي).
- thk-breuer: تصنيف خطأ (فلسفة بدل علم نفس) + active_start مخمَّن.
- thk-ganscombe: أخطاء نحوية جسيمة — يستخدم صيغ التذكير طوال الملف لفيلسوفة (أنسكومب امرأة).
- thk-fmodestin: نفس النمط — صيغ تأنيث لشخص ذكر (باتريك كوريغان).
- thk-fechner: يصفه بدراسة الفلسفة وتخرّج 1835؛ الصحيح دراسة الطب وتخرّج 1822.
- thk-hartmannheinz: تصنيف مدرسي خطأ (نيو-فرويدية بدل مدرسة الأنا المضادة لها فعلياً).
- thk-kets: ربط خطأ بالأدلريين رغم تدريبه الفرويدي/علاقات الموضوع الفعلي.
- thk-gaos: تصنيف خطأ (مدرسة علاجية إكلينيكية بدل فيلسوف وجودي بحت).
- thk-lmiller / thk-llosi / thk-elevine / thk-brueger / thk-bbadenoch / thk-ahill: كلها بنفس
  النمط — تصنيف `part` خطأ (فلسفة بدل علم نفس) لأشخاص هم علماء نفس فعلياً.

**تواريخ وفاة/ميلاد خاطئة أو ناقصة (عيّنة كبيرة، القائمة الكاملة في الملفات الخام):**
camus (active_end خطأ رغم وفاته 1960)، ellenberger (active_start=active_end=1970!)، eimber
(تُعرض حية رغم وفاتها 2024)، hstein (وفاته 2024 مفقودة)، bertrand-russell (1959 بدل 1970 الصحيح!)،
ctart (وفاته 2025 مفقودة)، john-search (وفاته 2025 ومنصبه الفخري المسحوب مفقودان)، lchodorow
(وفاتها 2025 مفقودة)، acatania (1939-2018 بدل 1936-2022 الصحيح)، erikson (تناقض داخلي: active_end
1985 رغم كتاب نُشر 1987؛ الصحيح وفاته 1994)، ewolf (2016 بدل 2018)، dabrowski (سنة نشر كتاب خطأ:
1936 بدل 1972 الصحيحة).

**روابط/edges تالفة بنيوياً (نمط متكرر جداً — عشرات الحالات):** حقل `belongs_to` يحتوي **نصاً
حراً بدل slug فعلي** (مثال: `target: "الهاكومي (Hakomi)"` بدل `target: "tec-hakomi"`) — هذا خلل
بنيوي يكسر شبكة الروابط في الأطلس بصمت (لا يظهر كخطأ واضح إلا بالفحص اليدوي). ظهر في عشرات الملفات:
thk-hweiss، thk-cgrof، thk-jseikkula، thk-fdolto، thk-jflax، thk-ken-blanchard، thk-bboyesen،
thk-john-gray، thk-jbanmen، thk-jframo، thk-dchamberlain، thk-josselson، thk-dan-ariely،
thk-jkornfield، thk-ibn-khaldun، thk-jean-baudrillard، thk-jay-shetty، thk-james-clear،
thk-goleman، thk-fmesmer، thk-charles-duhigg، thk-jrosenberg، وغيرها كثير — **هذا النمط وحده
يستحق دفعة تصحيح منفصلة مركّزة على حقل `edges` عبر كل الأطلس المعتمد، ليس فقط ضمن هذا التعارض.**

**اقتباسات/أعمال/مصادر مفبركة أو غير موثقة احتُفظ بها كحقيقة في المعتمد:**
thk-akaptchuk (استشهادات غير موثقة)، thk-flake (ادّعاءات مختلَقة)، thk-earl-nightingale (سرد غير
مسنود)، thk-bmontalvo (تواريخ وميلاد على الأرجح مفبركة)، thk-jcawley (شخص/برنامج لا مصدر مستقل
له)، thk-jwpark (لا مصدر يؤكد الشخص المزعوم)، thk-lhecker (لا مصدر أساسي يؤكد الباحث)، thk-krischer
(لا دليل على الإسناد المزعوم)، thk-icheolhong (لا مصدر مستقل يؤكد الهوية/العمل)، thk-dparfit (عنوان
كتاب مختلَق "The Metaphysics of Creation" 2013)، thk-cheikh-anta-diop (مكان ميلاد ومسرحية مفبركان)،
thk-baker (مذكرات محتملة الاختلاق)، thk-charles-swenson (كتاب ونقل تقنية للبرازيل غير موثقين)،
thk-al-mawardi (تأثير على مونتسكيو/لوك غير موثق)، thk-gary-wells (مقارنة غير موثقة)، thk-jrubin
(روابط ذاتية التناقض مع متن الملف نفسه).

## ❓ حالات UNCERTAIN (تحتاج بحثاً بشرياً، ~16 حالة)
thk-jkabat، thk-cel-bejjani، thk-kastrinidis، thk-edward-de-bono (قرار دمج/حجر سابق يحتاج مراجعة)،
thk-leon-festinger (احتمال ازدواج مع thk-lfestinger)، thk-jchales، thk-bidwell، thk-david-krauss،
thk-bodunrin، thk-fgutier، thk-benthall، thk-dluo، thk-kstinshoff، thk-boszormenyi، thk-deng-yuanhai،
thk-kholzkamp، thk-davoine، thk-chrysippus، thk-akelman، thk-david-schwartz، thk-jrotter، thk-cmadanes،
thk-lfinlay، thk-dsharp، thk-clarissa، thk-jcarlson.

## ملاحظة إضافية: حجم نمط `edges.belongs_to` بنص حر بدل slug
بعد اكتمال الدفعات الـ28 كلها، اتضح أن هذا النمط **أكثر انتشاراً بكثير** مما بدا أول الأمر — عشرات
إضافية ظهرت في الدفعات الأخيرة (thk-kkambon، thk-efriedman، thk-klew، thk-jjordan-suicide،
thk-afghani، thk-bj-fogg، thk-haponte، thk-lhubbard، thk-louise-hay، thk-gretchen-rubin، thk-kafka،
thk-dgrand، thk-gabor-mate، thk-ainsworth، thk-jordan، thk-kelley، thk-agreen، thk-kcrenshaw،
thk-jean-francois-lyotard، thk-jnicolosi، thk-duckworth، thk-alazm، thk-dweck، thk-kalff، thk-janet،
thk-brihaspati، thk-ibn-sabin، thk-jcgibbs، thk-ahofmann، thk-hobbes، thk-leopoldo-zea، thk-hmurray،
thk-jburns، thk-daniel-gilbert، thk-lorange، thk-kmaclean، thk-kumarila-bhatta، thk-bachelard،
thk-kosik، thk-kgolding، وغيرها). **هذا يؤكد التوصية أعلاه: يستحق فحصاً آلياً شاملاً منفصلاً عبر كل
`content/ar/` المعتمد لا فقط عيّنة الملفات المتعارضة مع مسودة.**

## الحالة النهائية (28 من 28 دفعة اكتملت — كل الـ1116 تعارضاً فُحص فعلياً)
- **487 ملف محذوف** (DELETE مؤكَّد بمقارنة محتوى فعلية عبر كل الدفعات الـ28: 274 من الدفعة الأولى
  + 213 من الدفعة الثانية) + **thk-jaustin** (من طلب المستخدم الأصلي، فروق تافهة فقط) = **488 حذف
  إجمالي**.
- **thk-amy-cuddy** (من طلب المستخدم الأصلي) **لم يُحذف** — تأكَّد أنه APPROVED_DEFECT حقيقي (خطأ
  إسناد اسم مؤلفة في المعتمد)، مذكور أعلاه بالتفصيل، ومؤكَّد مرتين من دفعتين مستقلتين (chunk 000
  وchunk 025).
- **تعارضات build_slug_index.py الآن: 622** (من أصل 1116) — وهذا الرقم **متوقَّع وليس عيباً**: كل
  ما تبقّى هو حالات APPROVED_DEFECT أو IDENTITY_CONFLICT أو UNCERTAIN المفصَّلة في هذا التقرير،
  وحذفها كان سيفقد تصحيحات حقيقية أو يمحو هوية شخص حقيقي مختلف. **هذا الرقم لن ينخفض أكثر إلا بعد
  قرار بشري (كلود) يعدّل الملفات المعتمدة فعلياً** — وهو ما لا يملك Spark صلاحيته.
- **صفر عملية تعديل على أي ملف معتمد** طوال هذا التدقيق (ملتزم بقاعدة SPARK.md رقم 1).

## التوصية لرئيس التحرير
هذا الحجم من الأخطاء المكتشفة في المحتوى **المعتمد** (لا المسودات) غير متوقَّع ويستحق أولوية:
1. **12 حالة IDENTITY_CONFLICT** يجب حسمها أولاً — كل واحدة فيها شخص حقيقي محتمل الضياع كاملاً.
2. **نمط edges.belongs_to بنص حر بدل slug** يستحق فحصاً آلياً شاملاً منفصلاً عبر كل `content/ar/`
   المعتمد (ليس فقط الملفات المتعارضة) — قد يكون منتشراً في ملفات لا تملك مسودة مطابقة أصلاً فما
   يظهر هنا مجرد "العيّنة المرئية" من مشكلة أوسع.
3. **~330+ خطأ حقيقي في المعتمد** موثّقة في القوائم أعلاه تحتاج تصحيحاً يدوياً بشرياً (كلود) — Spark
   ممنوع من تعديل المعتمد مهما كان الدليل واضحاً.
