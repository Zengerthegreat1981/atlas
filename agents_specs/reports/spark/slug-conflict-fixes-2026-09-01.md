# تنفيذ تصحيحات تدقيق تعارضات slug (2026-09-01، بعد إذن مستخدم صريح)

## الخلفية
بعد `slug-conflict-audit-2026-09-01.md` (التدقيق الذي حدد 622 حالة متبقية: APPROVED_DEFECT +
IDENTITY_CONFLICT + UNCERTAIN)، طلب المستخدم صراحة: **"can u fix them؟"** — إذن مباشر من المستخدم
الحقيقي (لا "كلود" الشخصية الافتراضية داخل SPARK.md) لتعديل الملفات المعتمدة، وهو تفويض يتجاوز قيد
"Spark ممنوع من تعديل المعتمد" لأن هذا القيد كان لتنسيق العمل بين Spark وMiniMax، لا قيداً من
المستخدم نفسه.

## المنهجية
25 دفعة إصلاح متوازية (~25 عنصراً لكل دفعة)، كل دفعة:
1. أعادت التحقق من كل عنصر من الصفر (قراءة الديف الكامل، لا الملخص فقط) بدل الاعتماد على أحكام
   دفعة التدقيق الأولى — لتفادي تراكم الخطأ.
2. لكل عنصر APPROVED_DEFECT حقيقي: عدّلت **الحقل/الحقيقة الخاطئة تحديداً فقط** في الملف المعتمد
   (لا إعادة كتابة شاملة)، ثم حذفت المسودة بعد أن أصبحت زائدة.
3. لكل IDENTITY_CONFLICT حقيقي: تركت الملف المعتمد كما هو للشخص الأصلي، وأنشأت ملف **slug جديد**
   للشخص الآخر بمحتواه الحقيقي، وحذفت المسودة القديمة.
4. لكل UNCERTAIN حقيقي: تُركت الحالتان (معتمد ومسودة) بلا أي تعديل.
5. **تعليمة أضيفت من الموجة الثانية فصاعداً**: قبل تفريغ أي `edges.belongs_to` بحجة "نص حر بلا slug
   حقيقي"، لازم تحقق فعلي بالبحث في `content/ar/` — دفعة مبكرة اكتشفت أن `sch-popular-psychology`
   فعلاً موجود وكانت دفعات تدقيق سابقة ستفرّغه خطأً؛ التعليمة المضافة صانت من تكرار هذا الخطأ في
   باقي الدفعات (والدفعات التالية فعلاً أمسكت حالات مشابهة وصححتها).

## النتيجة الكمية
- تعارضات slug: **622 → 75** (547 حالة حُسمت فعلياً في هذه الجولة).
- **12 حالة IDENTITY_CONFLICT حُسمت بالكامل** بفصل slug حقيقي لكل شخص:
  1. `thk-gunnel-cederblad` (بقي) ↔ `thk-marianne-cederblad` (جديد)
  2. `thk-andrew-barnes` (بقي لإيميلي بلاك) ↔ `thk-andrew-j-barnes` (جديد، أندرو بارنز الحقيقي)
  3. `thk-amncube` (بقي) ↔ `thk-ncazelo-ncube` (جديد)
  4. `thk-dhanna` (بقي، فرانك غولدستين) ↔ `thk-michael-goldstein` (جديد)
  5. `thk-hkrystal` (بقي، هيروشي كاواشيما) ↔ `thk-henry-krystal` (جديد، هنري كريستال الحقيقي)
  6. `thk-kastrinidis` (بقي) ↔ `thk-perikles-kastrinidis-ch` (جديد)
  7. `thk-isaac-blind` (أعيد كتابته ليصف إسحاق الأعمى فعلاً) ↔ `thk-isaac-israeli` (جديد، أُنقذ محتواه)
  8. `thk-jacqueline-astington` (بقي) ↔ `thk-janet-wilde-astington` (جديد، عالمة النفس الحقيقية)
  9. `thk-lonan` (بقي، لورينا أونيس) ↔ `thk-luigi-onnis` (جديد، لويجي أونيس الحقيقي)
  10. `thk-jlueger` (بقي، جون لوغر) ↔ `thk-robert-lueger` (جديد، روبرت جيه لوغر الحقيقي)
  11. `thk-jgantt` (بقي محجوراً — جوزيف غانت غير موثّق) ↔ `thk-susan-gantt` (جديد، سوزان بي غانت الحقيقية)
  12. `thk-bdanner` (بقي، برنارد دانفر) ↔ `thk-deborah-danner` (جديد، ديبورا دانر الحقيقية)
- **thk-amy-cuddy مُصحَّح**: الاسم الخطأ "داتشر كِلتنر" استُبدل بـ"دانا كارني" الصحيحة في الملف المعتمد.
- **مئات التصحيحات الحقيقية** طُبِّقت على ملفات معتمدة: تواريخ ميلاد/وفاة خاطئة، أسماء مؤلفين
  مُساء نسبتها، اقتباسات وكتب مفبركة أو غير موثقة أُزيلت، تصنيفات `part` خاطئة (فلسفة/علم نفس)،
  أخطاء توافق نحوي في الجنس، وعشرات (ربما أكثر من 100) حالة `edges.belongs_to` كانت نصاً حراً بدل
  slug حقيقي — أُصلحت لتشير لـslug صحيح، أو أُفرغت بعد تأكيد عدم وجود بديل حقيقي.

## الـ75 حالة UNCERTAIN المتبقية (بقيت بلا أي لمس، بشكل متعمَّد)
هذه ليست فشلاً — كل واحدة منها فيها تعارض حقيقي في الحقائق (تاريخ ميلاد مختلف، بلد مختلف، مؤسسة
مختلفة) لم تستطع الدفعات المتوازية حسمه بثقة كافية من الديف وحده، وتحتاج بحثاً بشرياً مباشراً أو
مصدراً خارجياً موثوقاً لا أملكه. القائمة الكاملة:

thk-bodunrin، thk-fain، thk-angel، thk-krischer، thk-dimen، thk-john-searle، thk-cmadanes،
thk-downing، thk-kimkwansung، thk-lfinlay، thk-bobbeck، thk-kaarlokeranen، thk-ifrom، thk-bidwell،
thk-jdelozier، thk-louise-guerney، thk-cyamanaka، thk-benthall، thk-akaptchuk، thk-caruso-amedeo،
thk-edward-de-bono، thk-bob-proctor، thk-lowinsky، thk-kfeeney، thk-duplock، thk-beebe،
thk-john-friedman، thk-jabra، thk-kmithoefer (تعارض بين 3 ملفات معتمدة: amithoefer/mmithoefer/kmithoefer)،
thk-alam، thk-jchales، thk-jonathanbaylin، thk-amo، thk-jcawley، thk-hschlesinger، thk-ccrowther،
thk-akelman، thk-kraus، thk-everettshostrom، thk-bmontalvo، thk-depston، thk-cherylfairbairn،
thk-johann-hari، thk-gcombs، thk-dwchen، thk-idmarshall، thk-john-makransky، thk-brian-victoria،
thk-jgone، thk-greenwald، thk-acatania، thk-adams، thk-donaldatkinson، thk-freeman،
thk-george-thompson، thk-icheolhong، thk-fgutier، thk-anajam، thk-keizan، thk-flake، thk-dluo،
thk-kunzli، thk-lwalker، thk-deng-yuanhai، thk-delman، thk-kogan، thk-eburne، thk-leon-festinger
(تعارض مرجّح مع thk-lfestinger — يحتاج قرار دمج)، thk-frankanderson، thk-lmyers، thk-greenberg،
thk-larrynims، thk-jkabat (قرار دمج/حجر سابق مع thk-jkabat-zinn يحتاج مراجعة صريحة)،
thk-alasdair-macleod، thk-knoblauch.

## أمر التحقق
`python3 scripts/build_slug_index.py` → 6944 عنصر (6621 معتمد + 323 مسودة)، 75 تعارض متبقٍ (كلها
UNCERTAIN موثّقة أعلاه، لا خطأ في الفحص).

## ملاحظة مهمة اكتُشفت أثناء التنفيذ
دفعة تدقيق مبكرة (قبل التنفيذ) افترضت أن `sch-popular-psychology` slug غير موجود وأوصت بتفريغ
`edges` في عدة ملفات (dale-carnegie، goleman، joseph-murphy، gladwell، james-clear، charles-duhigg،
harville-hendrix، dan-millman، dan-kiley). **دفعات التنفيذ تحققت فعلياً وأثبتت أن الـslug موجود
بالفعل** (`content/ar/schools/sch-popular-psychology.md`) — فتم تصحيح المسار بدل تكرار الخطأ: تُرك
الرابط الصحيح في مكانه، وحُذفت المسودة فقط. هذا يوضح قيمة "تحقق قبل التعديل" التي أُضيفت كتعليمة
صريحة للدفعات من الموجة الثانية فصاعداً.

## ما لم يُلمَس عمداً
- الـ75 حالة UNCERTAIN أعلاه — بانتظار توجيه بشري أو مصدر خارجي.
- أي ملف معتمد لم يظهر في قائمة الـ622 الأصلية (خارج نطاق هذا التدقيق تحديداً).
