# Task 2.51
الحالة: مكتمل
العملية: Task 2 — تحقق هوية 10 مفكرين مشكوك فيهم (thk-m…thk-z)، بينهم ازدواج مؤكَّد وslug معاد تدويره | الملفات: 11 (10 + إحالة ازدواج)

## الأرقام
مخالفات preflight_check.py: قبل 2 (تطابق id/title في related) → بعد 0
جمل القائمة السوداء (grep يدوي، 17 جملة): صفر تطابق في الملفات الـ11
ملفات موثّقة أُعيد كتابتها/تدعيمها بمصادر حقيقية: 8
ملفات حُوِّلت لإحالة ازدواج صريحة: 1 (thk-marshall-rosenberg)
ملفات حُجِّرت هوياً (غامض/رفض إعادة تدوير slug): 1 (thk-twolofor)
طلبات slug جديدة سُجِّلت في requests-minimax.md: 1 (R-006 — Toyin Falola)
مدارس غائبة سُجِّلت/حُدِّثت في missing-schools.md: 1 سطر (علم النفس الشعبي والتحفيز القيادي)

## أمر التحقق
`python3 scripts/preflight_check.py <11 ملف>` → `✅ 11 ملف — صفر مخالفات آلية.` (exit 0)
grep يدوي لـ17 جملة القائمة السوداء على الـ11 ملف → صفر تطابق

## قرارات اتخذتها

- **thk-tony-robbins** (Tony Robbins، مدرّب تحفيزي حقيقي) → **موثّق**. حذفت اقتباساً غير مُسنَد بمصدر ("قراراتك تُشكِّل مصيرك...")، أضفت `## المصادر` (كتبه الأساسية: Unlimited Power 1986، Awaken the Giant Within 1991، Money: Master the Game 2014)، صححت عنوان رابط `thk-david-schwartz` (كان "ديفيد شوارتز" والعنوان الحقيقي "ديفيد ج. شوارتز")، وحذفت `edges` المكسورة (كانت تشاور على نص حر "علم النفس الشعبي والتحفيز القيادي" بدل slug، وعلى `sch-popular-psychology` غير الموجود) — سجّلت المدرسة الغائبة في `missing-schools.md`.

- **thk-mbraveheart** (Maria Yellow Horse Brave Heart، عالمة نفس سريرية حقيقية، صاحبة مفهوم "الصدمة التاريخية") → **موثّق** (كان موثقاً أصلاً بجودة عالية). أضفت `## المصادر` صريحة (كانت مدمجة فقط في "أهم أعمالها")، صححت عنوان `thk-jgone` (كان "جوزيف غون" والصحيح "جوزيف ب. غون")، وحذفت رابط `con-grief` لأن عنوانه الحقيقي ("الحزن كمسار للتفريد") لا يطابق المفهوم المقصود (الحزن التاريخي غير المُعالَج) — تضارب id/title.

- **thk-roman-ingarden** (فيلسوف بولندي، تلميذ هوسرل، مؤسس ظاهراتية الأدب) → **موثّق** (محتوى قوي أصلاً). أضفت `## المصادر` (أعماله الأصلية)، وأصلحت سنتين بعد `active_end` (1968) بلا إشارة وفاة: `Über die Verantwortung` (نُشر 1970 بعد وفاته) و`Man and Value` (1983 بعد وفاته) — أضفت "نُشرت بعد وفاته" قبل كل سنة مباشرة.

- **thk-twolofor** → **غامض / رفض إعادة تدوير slug**. المسودة السابقة استبدلت هذا الـslug (الذي لا يطابق أي اسم حقيقي معروف) بسيرة كاملة لتويين فالولا (Toyin Falola، مؤرخ نيجيري حقيقي)، مع اعتراف صريح في `gaps` بعدم تطابق الاسم — هذا هو بالضبط الخرق الذي تحذّر منه القاعدة 6 والقاعدة 11 (ثقة شكلية + شك في المحتوى). أزلت سيرة فالولا بالكامل من هذا الملف، حوّلته لملف "هوية غير محدَّدة" صريح بلا سيرة، وسجّلت طلب slug جديد لفالولا في `requests-minimax.md` (R-006). **لم يُدرج في quarantine-minimax.md لأن الحالة "غامضة" (اسم لا يقابل شخصاً موثقاً) لا "غير موجودة" بمعنى ادّعاء كاذب** — لا يوجد شخص محدد اسمه "twolofor" لأزعم عدم وجوده؛ المشكلة أن المحتوى كان لشخص آخر تماماً.

- **thk-marsilio-ficino** (فيلسوف نهضوي، مؤسس الأكاديمية الأفلاطونية الفلورنسية) → **موثّق** (محتوى قوي أصلاً). حذفت قسم "اقتباسات مختارة" الذي كان يحتوي حرفياً جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" (استبدلته بـ`## المصادر` بأعماله الأصلية)، وصححت عنوان `thk-pico` (كان فيه "della" غير مترجمة بدل "ديلا").

- **thk-rlwilliams** (Robert Lee Williams II، عالم نفس أمريكي-أفريقي حقيقي، 1930–2020) → **موثّق، لكن أُعيد كتابته بالكامل**. تحققت من الوقائع عبر بحث خارجي (Encyclopedia of Arkansas، Washington University in St. Louis): المحتوى الأصلي كان يحتوي عناوين كتب ومقاييس **مختلَقة على الأرجح** ("Racism in Psychology: Towards an Antiracist Psychology" 1975، "Ebony Lexicon"، اختبار "ADOS")، بينما الوقائع الموثقة فعلياً هي: اختبار **BITCH-100** (1972)، صياغة مصطلح **Ebonics** (1973)، كتاب **"Ebonics: The True Language of Black Folks"** (1975)، وتأسيس **ABPsi** (1968، رئاسته 1969–1970). صححت `active_end` من 2015 (خطأ) إلى 2020 (سنة الوفاة الفعلية).

- **thk-mikel-dufrenne** (فيلسوف فرنسي، ظاهراتية الخبرة الجمالية) → **موثّق** (محتوى قوي أصلاً). أضفت `## المصادر`، وصححت عنوان `thk-heidegger` (كان "هايدغر" والعنوان الحقيقي في الملف المستهدف "هايدجر").

- **thk-msrosenberg / thk-marshall-rosenberg — ازدواج مؤكَّد** (Marshall B. Rosenberg، مؤسس التواصل اللاعنفي NVC، 1934–2015، **نفس الشخص بالضبط** تحت slug-ين). قارنت عدد الروابط الواردة الفعلية عبر `grep -rl` على `content/ar` كله: **thk-msrosenberg = 3 روابط واردة** (con-mutual-empathy، con-nonviolent-communication، sch-humanistic) مقابل **thk-marshall-rosenberg = 2 رابط** (wrk-nonviolent-communication، con-nonviolent-communication). **اعتمدت thk-msrosenberg** (الأكثر ربطاً) ودمجت فيه أفضل المحتوى المتوفر بين النسختين (النسخة الأخرى كانت أعمق تحليلياً)، وصححت فيه عنواني `con-nonviolent-communication` و`con-mutual-empathy` اللذين كانا مختلفين عن العناوين الحقيقية. حوّلت **thk-marshall-rosenberg** لملف إحالة صريحة (نمط `thk-mwhitehouse`) يشير لـthk-msrosenberg، مع توثيق سبب القرار في `gaps`.

- **thk-maxie-maultsby** (Maxie C. Maultsby Jr.، مؤسس Rational Behavior Therapy) → **موثّق** (محتوى قوي أصلاً). أضفت `## المصادر` بمصدر واحد تحقّقت منه خارجياً (Rational Behavior Therapy، 1984، Prentice-Hall Press — تأكدت من الناشر عبر بحث خارجي)، وسجّلت في `gaps` أن مصادر إضافية مستقلة لم تُتحقق بعد بدل اختلاق مراجع غير مؤكدة.

- **thk-raul-fornet-betancourt** (فيلسوف إسباني-فنزويلي، الفلسفة البين-ثقافية) → **موثّق** (محتوى قوي أصلاً). أضفت `## المصادر`، وصححت عنوان `sch-decolonial-philosophy` (كان "الفلسفة اللااستعمارية (Decolonial Philosophy)" والعنوان الحقيقي "الفلسفة الديكولونيالية (كمظلة عالمية)").

## متوقف عنده (لرئيس التحرير)

- **thk-twolofor**: يحتاج قراراً تحريرياً — هل نوثّق تويين فالولا تحت slug صحيح جديد (طلب R-006)، أم يبقى thk-twolofor فارغاً هوياً كما هو الآن؟
- ثلاثة ملفات خارج نطاق هذه الدفعة لا تزال تشير إلى `thk-twolofor` بروابط كانت مبنية على محتوى فالولا المحذوف: `content/ar/thinkers/thk-asante.md` وَ`content/ar/thinkers/thk-hountondji.md` (كلاهما في مدى Spark الكتابي thk-a→thk-l، لا أملك صلاحية تعديلهما) وَ`content/ar/schools/sch-african-psychology.md` (في مدى كتابتي لكن خارج نطاق دفعة 2.51 المحدد). تحتاج مراجعة لاحقة بعد حسم R-006.
- **thk-msrosenberg / thk-marshall-rosenberg**: ملفان آخران خارج الدفعة (`content/ar/works/wrk-nonviolent-communication.md`) ما زالا يشيران لـ`thk-marshall-rosenberg` (الإحالة) بدل `thk-msrosenberg` المعتمد — لم أعدّلهما لأنهما خارج قائمة الملفات العشرة المحدَّدة، لكن يستحقّان تحديث الروابط لاحقاً.

## الملفات
- content/ar/thinkers/thk-tony-robbins.md
- content/ar/thinkers/thk-mbraveheart.md
- content/ar/thinkers/thk-roman-ingarden.md
- content/ar/thinkers/thk-twolofor.md
- content/ar/thinkers/thk-marsilio-ficino.md
- content/ar/thinkers/thk-rlwilliams.md
- content/ar/thinkers/thk-mikel-dufrenne.md
- content/ar/thinkers/thk-msrosenberg.md
- content/ar/thinkers/thk-maxie-maultsby.md
- content/ar/thinkers/thk-raul-fornet-betancourt.md
- content/ar/thinkers/thk-marshall-rosenberg.md (إحالة ازدواج، عُدِّل كنتيجة مباشرة لتحقيق thk-msrosenberg)

## ملفات مساندة عُدِّلت
- agents_specs/requests-minimax.md (أُضيف R-006)
- agents_specs/missing-schools.md (تحديث سطر "علم النفس الشعبي والصحافة العلمية")
