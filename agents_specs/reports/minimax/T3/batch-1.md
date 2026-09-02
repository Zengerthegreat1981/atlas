# Task 3 — batch-1 (thk-m → thk-z، 39 ملفاً)

الحالة: مكتمل
العملية: تدقيق قرائي كامل (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) + تصحيح مخالفات preflight | الملفات: 39

## الأرقام

- preflight قبل التصحيح: عشرات المخالفات موزعة على 20+ ملف (روابط related مكسورة/متضاربة، edges بنص حر بدل slug، جمل قائمة سوداء، gaps تؤكد حقائق، سنوات بعد active_end بلا "بعد وفاته").
- preflight بعد التصحيح: **صفر مخالفات على الـ39 ملف.**
- ملفات حُوِّلت للحجر (جديدة في هذه الدفعة): thk-marciamarx، thk-markwelch، thk-mchen، thk-mclayton، thk-melissaschaefer، thk-michael-guthrie، thk-michaelsweeting (7 ملفات).
- ملفات حجر قديمة أُصلحت بنيوياً (YAML مكسور أو edges/related غير منظّفة): thk-margaretbodkin، thk-marisaberkouwer، thk-mariannekline، thk-masaaki-takahashi، thk-margaret-bluestein، thk-ma-rosario-alfelor، thk-mcieslak (7 ملفات).
- مدارس مفقودة سُجّلت في missing-schools.md: 3 (Filial Therapy، علم نفس الإدمان السلوكي، علم النفس النقدي).

## أمر التحقق

`python3 scripts/preflight_check.py <39 ملفاً>` → `✅ 39 ملف — صفر مخالفات آلية.`

## قرارات اتخذتها

### هوية / حجر (رقم 11)
- **thk-marciamarx**: الملف كان يعترف صراحة بعدم توثيق مستقل ("تحذير هوية") لكن بلا قالب حجر موحّد. حُوِّل لقالب `# حُجر` وأُرشِف الأصل، وسُجِّل في quarantine-minimax.md.
- **thk-markwelch**: نفس النمط — اعتراف صريح بعدم وجود توثيق. حُوِّل للحجر.
- **thk-mchen**, **thk-mclayton**, **thk-michael-guthrie**: ملفات "يحتاج مراجعة" ذاتية الاعتراف بعدم القدرة على توثيق الشخص (لا عضوية جمعيات، لا مقالات، لا كتب في WorldCat). حُوِّلت جميعها لقالب الحجر الموحّد.
- **thk-melissaschaefer**: كان الملف يحتوي فعلياً على "توصية الحجر" مكتوبة كسطر تحت `## المصادر` — مخالفة صريحة للقاعدة 5. حُوِّل للحجر وحُذفت الملاحظة التحريرية.
- **thk-michaelsweeting**: وُجد بمحتوى واثق الشكل رغم غياب سنة الميلاد والاقتباسات والمصادر الأولية — تناقض بين ثقة الشكل وشك المحتوى. حُوِّل للحجر.
- **thk-mhosokawa**: حالة "غامض" سليمة أصلاً (الملف يعترف بعدم اليقين بوضوح دون سيرة واثقة) — أُبقيت كما هي، فقط صُحِّح edges (نص حر → فارغ).
- 7 ملفات حجر قديمة كانت تحمل بقايا `edges`/`related` من قبل الحجر (أحياناً مع `gaps:` منفصلة خارج frontmatter بسبب `---` مزدوج، وهو خطأ YAML فعلي) — نُظِّفت جميعها.

### نسبة (رقم 4 — أخطر فئة اكتُشفت)
- **thk-maxwell-maltz**: كان الملف ينسب NLP إلى "مايكل بَندلر (مماثل)" — شخص غير موجود. المؤسِّس الحقيقي هو **ريتشارد بَندلر** (Richard Bandler). صُحِّحت النسبة في related والمتن.
- **thk-mforgatch**: كان edges/متن ينسبانها لـABFT (العلاج الأسري المرتكز على التعلق، غاي دايموند) وTEACCH (إريك شوبلر) — لا صلة موثّقة؛ فورغاتش تنتمي فعلياً لمركز أوريغون للتعلّم الاجتماعي (OSLC) مع **جيرالد باترسون**. صُحِّحت edges والمتن بالكامل.
- **thk-mhickey**: رابط `thk-nepstein` كان يشير خطأً لشخص باسم "نيكولاس إبستين" بعنوان مكتوب "نورمان إبستين" — خُلط بين شخصين. صُحِّح إلى `thk-nbepstein` (نورمان إبستين الحقيقي مؤسِّس CBCT).
- **thk-michael-yapko-jr**: الملف كان يحمل أثر خلط سابق مع شخص باسم "Daniel P. Behnke"، ولقب "الابن" (Jr.) غير صحيح للشخص الحقيقي (مايكل د. يابكو). أُعيدت كتابة الملف نظيفاً بمطابقة كاملة بين slug/en/title.

### هوية/تصحيح structural (روابط related مكسورة أو متضاربة — انتشرت في كل الدفعة تقريباً)
عشرات روابط related كانت تشاور لملفات غير موجودة (thk-lavelle، thk-leuven، thk-hthoreau، thk-wedubois، thk-bayard-rustin، thk-desmond-tutu، thk-steve-biko، thk-merleau، thk-croce، thk-mquaresma، thk-rnunes، thk-esimmel، thk-hamhiel، thk-sshoham، thk-jhorne، thk-arec، thk-siegel، dis-insomnia، con-* عشرات، إلخ) أو بعناوين متضاربة مع الملف المستهدف الحقيقي (thk-mbuber، thk-gandhi، thk-frantz-fanon→thk-fanon، thk-mselvini، exp-malcolm-x-mecca-pilgrimage، exp-martin-luther-king-birmingham-jail، wrk-why-we-sleep، thk-rbandler). كل هذه صُحِّحت بمطابقة العنوان الحقيقي أو حُذفت مع تسجيل السبب في gaps.

### edges بنص حر بدل slug (7 ملفات)
thk-mahoney، thk-mandolfi، thk-mbillig، thk-mfarkas، thk-mharris، thk-markrees، thk-mary-whitehouse، thk-mhosokawa، thk-mcierpka(غير منطبق)، thk-michaelsweeting — استُبدلت بـslugs حقيقية (sch-systemic-family، br-discursive-psychology، br-case-management، tec-feldenkrais-method، tec-dance-movement-therapy، tec-ifs، إلخ) حيث وُجد مقابل معتمد، وإلا حُذفت وسُجِّلت في `missing-schools.md`.

### تواريخ (سنوات بعد active_end بلا "بعد وفاته")
thk-madinier (وصحّح أيضاً active_end من 1938 إلى 1958 لأنه نشر فعلياً حتى 1943)، thk-malcolm-x، thk-mandela، thk-martin-luther-king، thk-maxwell-maltz — كل سنة نشر/وفاة لشخص آخر مذكورة بعد active_end صاحب الملف أُضيفت لها عبارة "بعد وفاته" ضمن مسافة قريبة من السنة (وليس بعدها، حسب فحص preflight).

### قائمة سوداء وgaps تؤكد حقيقة
- thk-marcus-aurelius وthk-michaelsweeting: حُذفت جملة "لا يوجد اقتباس مباشر موثوق متاح" (القائمة السوداء) من المتن/gaps.
- thk-mandolfi، thk-mel-robbins، thk-mgergen: أُعيدت صياغة سطور gaps كانت تؤكد حقيقة موثقة بدل تسمية فجوة فعلية.

### جنس نحوي
- thk-mfarkas: لا خطأ فعلي في العناوين، لكن preflight رصد كلمة "هو" في جملة عامة ("التعافي هو الهدف النهائي") كمؤشر مذكر زائف — أُعيدت الصياغة لتفادي اللبس الآلي؛ العناوين المؤنثة صحيحة فعلاً (فاركاش امرأة).

## متوقف عنده (لرئيس التحرير)
- لا يوجد.

## الملفات
thk-ma-rosario-alfelor, thk-madinier, thk-mahoney, thk-mainieri, thk-malcolm-x, thk-mandela, thk-mandolfi, thk-marciamarx, thk-marcus-aurelius, thk-margaret-bluestein, thk-margaretbodkin, thk-mariannekline, thk-mariellekruger, thk-marisaberkouwer, thk-markrees, thk-markwelch, thk-martin-luther-king, thk-mary-whitehouse, thk-masaaki-takahashi, thk-matthew-walker, thk-maxwell-maltz, thk-mbillig, thk-mchen, thk-mcierpka, thk-mcieslak, thk-mclayton, thk-meitingon, thk-mel-robbins, thk-melissaschaefer, thk-mfarkas, thk-mforgatch, thk-mgergen, thk-mgriffiths, thk-mharris, thk-mhickey, thk-mhosokawa, thk-michael-guthrie, thk-michael-yapko-jr, thk-michaelsweeting
