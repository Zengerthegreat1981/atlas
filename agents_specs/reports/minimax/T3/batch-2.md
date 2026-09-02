# Task 3 — batch-2 (thk-m → thk-o)

الحالة: مكتمل
العملية: تدقيق قرائي (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) + تصحيح مخالفات preflight | الملفات: 39

## الأرقام

- preflight قبل التصحيح: 148 مخالفة (36 من 39 ملف مخالف)
- preflight بعد التصحيح: 0 مخالفة على الـ39 ملفاً
- ملفات تحوّلت للحجر أو نُظّفت كملفات حجر قائمة أصلاً: 9
  (thk-mingshengli، thk-minopaulin، thk-mking، thk-mmejia، thk-mrothery، thk-mschwarz،
  thk-nbustos، thk-nepstein، thk-niosepa، thk-mworden، thk-nwatanabe — 11 فعلياً)
- روابط `related` محذوفة لعدم وجود ملف مستهدف: ~55 رابطاً عبر الدفعة
- روابط `related` بعنوان مصحَّح ليطابق الملف الحقيقي: 11
- `edges.belongs_to` بنص حر استُبدلت بslug حقيقي أو حُذفت: 14
- مدارس جديدة سُجّلت في `missing-schools.md`: 8

## أمر التحقق

```
python3 scripts/preflight_check.py <الملفات الـ39> → ✅ 39 ملف — صفر مخالفات آلية
python3 scripts/build_slug_index.py → ✅ فهرس الـ slugs محدَّث (6905 عنصر)
```

## قرارات اتخذتها

- **thk-mingshengli / thk-minopaulin**: كانا محجورين مسبقاً لكن الـYAML frontmatter كان مكسوراً
  (قسم `gaps` خارج حدود الـfrontmatter، علامتا `---` زائدتان) مع روابط `related`/`edges` متروكة من
  قبل الحجر. أعدت كتابة الملفين بقالب الحجر الموحّد النظيف.
- **thk-mking**: كان مسجَّلاً في quarantine-minimax.md لكن الملف الحي لم يكن بقالب الحجر الموحّد
  (بلا عنوان "هذا الملف في الحجر" الرسمي). حوّلته للقالب الموحّد اتساقاً مع بقية الحجر.
- **thk-mmejia**: نفس الحالة — الجسم كان بالفعل نص حجر، لكن الـfrontmatter احتفظ بـ`edges`/`related`
  الأصليين (7 روابط) رغم الحجر. نظّفتهما لـ`[]`.
- **thk-mrothery**: الملف اعترف صراحة في متنه الظاهر بعدم وجود توثيق مستقل ("لم يتم العثور على
  مصدر مستقل") رغم صيغة سيرة شبه-واثقة. طبّقت قاعدة 11: حوّلته لقالب حجر موحّد وسجّلته في
  `quarantine-minimax.md`.
- **thk-mschwarz / thk-nbustos / thk-nepstein**: الثلاثة كانوا "عناصر تحتاج مراجعة" (Task 2 leftover
  بصيغة "محاولة التوثيق" + بحث سلبي في قواعد بيانات متعددة). طبّقت قاعدة 11 وحوّلتهم لقالب حجر
  موحّد، وسجّلتهم في `quarantine-minimax.md`.
- **thk-mkerr**: عمله موثَّق كوريث مباشر لموراي بوين (نظرية بوين الأسرية)، لا لبوسورميني-ناجي
  (العلاج الأسري السياقي) كما كان `edge`/`crumb` يوحيان. صحّحت الـ`edge` إلى `br-bowen-systems`
  (الموجود فعلاً)، وصحّحت الـ`crumb`، وحذفت الرابط الخاطئ لـthk-boszormenyi.
- **thk-mramose**: رابطا `thk-amncube` و`thk-bdanner` كانا يشيران لملفين حقيقيين موجودين لكن عن
  شخصين مختلفين تماماً (نكازيلو نكوبي وديبورا دانر، لا ألبرت مْنكوبِي وبيرنارد دانِفَر كما كتب النص) —
  حذفتهما بدل تصحيح العنوان لأن الهوية المقصودة أصلاً غير موجودة كملف. صحّحت اسم `thk-nmanganyi`
  (المفروض "إن تشاباني مَنغاني" لا "نيلسون مَغَنْي").
- **thk-miguel-ruiz**: رابط `thk-kcahill` وصف "كلير كاهيل" بـ"ابنه الروحي" في `related` بينما المتن
  وصفها بـ"زوجته وشريكته" — تناقض جندري/علائقي داخلي. حذفت الرابط (غير موجود أصلاً كملف) بدل حسم
  التناقض بالتخمين.
- **thk-mrowland / thk-msolomon**: preflight أشار خطأً لتضارب جندري (checker heuristic بسيط يعدّ
  كلمات مثل "معالج" العامة بلا سياق). أعدت صياغة عبارات عامة ("المعالج يقود" ← "فريق العلاج يقود")
  لأن الشخصين فعلاً مؤنثتان والمتن الفعلي صحيح، والمشكلة كانت في كلمات جنسانية عامة غير متعلقة
  بالشخص نفسه.
- **thk-nazrin / thk-nassim-taleb**: أسماء مغلوطة داخل المتن نفسه ("دان جيلبوت" بدل "دانيال كانمان"
  لـDaniel Kahneman) صحّحتها كأخطاء نسخ ظاهرة، لا كهوية بديلة.
- **8 مدارس/تيارات** كانت مربوطة بنص حر بدل slug حقيقي حُذفت أو استُبدلت بـslug حقيقي، وسُجّلت في
  `agents_specs/missing-schools.md`: العلاج المستنير بعلم الأعصاب الوجداني، الطاوية المعرفية،
  العلاج الحسي-الحركي، العلاج بمساعدة psilocybin، العلاج بالفن، علم نفس الأوبونتو (مرتين)، CBCT.

## متوقف عنده (لرئيس التحرير)

- لا شيء متوقف — preflight صفر مخالفات على كل الـ39 ملفاً.

## الملفات

thk-michelle-weiner-davis.md, thk-miguel-ruiz.md, thk-mimordino-yang.md, thk-mingshengli.md,
thk-minopaulin.md, thk-minsungkil.md, thk-mjohnson.md, thk-mkerr.md, thk-mking.md, thk-mmejia.md,
thk-mnaumburg.md, thk-mpolster.md, thk-mramose.md, thk-mrand.md, thk-mricard.md, thk-mrothery.md,
thk-mrowland.md, thk-mschwarz.md, thk-msolomon.md, thk-mtselvini.md, thk-mviederman.md,
thk-mvilanova.md, thk-mworden.md, thk-napoleon-hill.md, thk-nassim-taleb.md, thk-nazrin.md,
thk-nbepstein.md, thk-nbustos.md, thk-nchomsky.md, thk-nel-noddings.md, thk-nepstein.md,
thk-ngoldberg.md, thk-niosepa.md, thk-nkhanna.md, thk-nmanganyi.md, thk-norman-vincent-peale.md,
thk-nwatanabe.md, thk-obecker.md, thk-oliver-sacks.md
