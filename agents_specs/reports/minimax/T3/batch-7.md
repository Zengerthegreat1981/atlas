# Task 3 — دفعة 7 (thk-t → thk-z، 35 ملفاً)

الحالة: مكتمل
العملية: تدقيق قرائي كامل بالترتيب (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) + تصحيحات بنيوية | الملفات: 35

## الأرقام

- ملفات حُجرت حديثاً (قاعدة 11، اعتراف صريح بعدم وجود توثيق مستقل): 6 — thk-ttolksdorf، thk-ttshishiku، thk-werner، thk-westphal، thk-wood، thk-young، thk-yongjingqi (فعلياً 7، انظر تفصيل تحت)
- ملفات كانت محجورة من قبل لكن بصيغة YAML/قالب مكسور، أُصلحت للقالب الموحّد: 3 — thk-wboechat، thk-yvaniedmon (كان به كسر YAML خطير: `gaps` طالعة برّه الـfrontmatter كنص حر بعد `---` مغلقة)، thk-zhangyongqiang
- روابط `related` مكسورة (id غير موجود أو title متضارب) صُححت أو حُذفت: ~55 رابطاً عبر 20 ملفاً
- edges بنص حر بدل slug صُححت أو حُذفت وسُجّلت في `missing-schools.md`: 8 حالات
- أخطاء جنس نحوي (عنوان قسم بصيغة مذكر لشخص مؤنث والعكس): 2 — thk-ydolan (`## ما أعطته`→`أعطتها`)، thk-wspaulding (اسم "ويلِم" مذكوراً خطأ لشخص اسمه الحقيقي Wilma + قسم `## ما أعطته`→`أعطتها`)
- أخطاء هوية/نسبة حقيقية (خلط شخص بآخر أو ترجمة خاطئة تقلب المعنى): 6 — انظر تفصيل تحت
- جمل قائمة سوداء حُذفت: 3 ملفات (thk-wrichards، thk-wwood، thk-yongjingqi/جزء من سبب الحجر)
- preflight (سنوات بعد الوفاة بلا "بعد وفاته/وفاتها"، gaps تؤكد حقيقة، title/id متضارب): قبل 14 مخالفة → بعد 0

## أمر التحقق

```
python3 scripts/build_slug_index.py
python3 scripts/preflight_check.py <35 ملف>
```
→ `✅ 35 ملف — صفر مخالفات آلية.`

(تحذير build_slug_index عن 663 تعارض slug بين معتمد/مسودات هو تحذير موروث من دفعات سابقة غير مرتبط بهذه الدفعة — لم يُحدث بأي تعديل من هذه الدفعة.)

## قرارات اتخذتها

### حجر جديد (قاعدة 11 — اعتراف صريح بعدم التوثيق)
- **thk-ttolksdorf**: الملف نفسه بحث في IAAP/DGAP/DNB/JAP ولم يجد شيئاً، واقترح خلطاً مع Detlef Tolksdorf أو Hans-Dieter Tolksdorf. حُوّل لقالب حجر موحّد.
- **thk-ttshishiku**: نفس النمط — بحث في UNIKIN/Psychopathologie africaine/PsycINFO بلا نتيجة، اقتراح خلط مع Tshisungu wa Tshibangu.
- **thk-werner**: بحث في IGD/DGAP/GVK/DNB بلا نتيجة، اقتراح خلط مع Helmut Werner Heisenberg (فيزيائي) أو مؤرخ فن أو لاعب كرة قدم.
- **thk-westphal**: السجل الوحيد في DNB لاسم "Westphal, Friedrich" يخص طبيباً نفسياً (1899–1975) شخصاً مختلفاً تماماً عن "الفيلسوف الوجودي المعاصر" الموصوف.
- **thk-wood**: بحث في SEA/BPS/Existential Analysis بلا نتيجة، اقتراح خلط مع John Wood أو John Maynard Keynes.
- **thk-young**: بحث في SEA/BACP/WorldCat بلا نتيجة، اقتراح خلط مع Sarah Young (مؤلفة Jesus Calling) أو Sara Young.
- **thk-yongjingqi**: صفر مصادر، صفر عنوان عمل بسنة نشر، الملف الأصلي انتهى بجملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" — محتوى عام بالكامل بلا أي واقعة يمكن التحقق منها.

كل الست حُجرت بنفس القالب الموحّد (مثل thk-mathew/thk-jgantt)، والنسخ الأصلية أُرشفت في `agents_specs/quarantine-minimax-archive/*.archived.2026-08-27`، وسُجّلت في `agents_specs/quarantine-minimax.md`.

### إصلاح قوالب حجر سابقة مكسورة
- **thk-yvaniedmon**: خطأ YAML خطير — `gaps:` كانت مكتوبة بعد `---` الثانية المغلقة، أي أنها ظهرت كنص حر في المتن بدل حقل frontmatter فعلي. أيضاً edges كانت نصاً حراً ("طريقة فيلدنكرايس") وrelated فيها 5 روابط لملفات غير موجودة (con-cerebral-palsy، con-anti-ableism، thk-rbaniel، thk-kconnors غير موجودة؛ thk-mfeldenkrais موجود لكن غير مبرَّر). أُعيد بناء الملف كاملاً بالقالب الموحّد الصحيح.
- **thk-wboechat** و**thk-zhangyongqiang**: كانا محجورين فعلاً لكن بعنوان "# حُجر" بدل الاسم، بلا حقل `gaps` في frontmatter، وrelated/edges لا تزال تحمل روابط الملف الأصلي المحجوب. طُبّق القالب الموحّد الكامل على الاثنين.

### أخطاء هوية/نسبة حقيقية صُححت
- **thk-wayne-dyer**: "ناتالي براندن" (اسم مؤنث) كانت منسوبة لـNathaniel Branden — عالم نفس **رجل** حقيقي (مؤسس علم نفس تقدير الذات). صُحح الاسم لـ"ناثانيال براندن" وأُزيل الرابط المكسور (thk-abranden غير موجود أصلاً في الأطلس).
- **thk-wzhang**: خطأ هوية/جنس مزدوج — Murray Stein (محلل يونغي أمريكي **رجل**) كان مكتوباً باسم "مارغريت شتاين" ووُصف بـ"هي" ("وهي بدورها محللة"). صُحح الاسم والضمير بالكامل. أيضاً كان مرتبطاً بـ`con-ubuntu` (فلسفة أوبونتو الأفريقية) بجملة غامضة "(المقصود: مفهوم Self عند يونغ)" — رابط لا معنى له تماماً، حُذف.
- **thk-wstekel**: ثلاث ترجمات عربية للعناوين كانت مقلوبة المعنى تماماً عن الأصل الألماني/الإنجليزي: "حالات فرويد في الإخصاء والقلق" (لكتاب *Hundert Fälle von Zwangsneurosen* الذي يعني فعلياً "مئة حالة من عصاب الوسواس القهري")، "التنويم الذاتي" لترجمة *Active Analysis* (يعني "التحليل النشط" لا التنويم)، و"الحياة الجنسية في المهد" لترجمة *The Sexual Aberrations* (يعني "الانحرافات الجنسية"). كما كان هناك سطر متناقض التواريخ يصف انشقاق ستيكِل عن فرويد بسنتين مختلفتين (1911 و1912) مع كلمة غير مفهومة "نوتردام" مكررة — حُذف التكرار المتناقض.
- **thk-wkroger**: "أشرف كورت شنايدر على تأهيله عام 1946" يتناقض مع كون أطروحته التأهيلية نفسها مؤرخة 1963/1959 في نفس الملف — حُذف الرقم الخاطئ. أيضاً كتاب "Psychosomatic Obstetrics and Gynecology (1962) مع جويل غ. ويتنهوفن" غير موجود في قسم المصادر أصلاً؛ المصادر تذكر كتاباً مختلفاً بعنوان وسنة ومؤلف مشارك مختلفين تماماً (*Psychosomatic Gynecology*، 1948، مع S. C. Freed) — صُحح المتن ليطابق المصدر الموثّق. كذلك تناقض تاريخي: انتقاد APA "عام 1961" لكتاب نُشر أصلاً 1963 (استحالة زمنية) — صُحح للـ"بعد نشره" بلا سنة خاطئة محددة.
- **thk-zlipowski**: رابط `thk-hheilig` ("هنري هايليغ") منسوب إليه نظرية "ثلاثية الإجهاد (General Adaptation Syndrome)" — هذه النظرية موثقة تاريخياً لهانز سيلي (Hans Selye) لا لأي "هنري هايليغ"، والاسم أصلاً غير موجود كملف أو كشخصية معروفة في الأدبيات. حُذف الرابط والاسم المفبرك بالكامل بدل اختراع بديل.

### أخطاء جنس نحوي
- **thk-ydolan**: عنوان `## ما أعطته` (مذكر) لعالمة نفس أمريكية (Yvonne Dolan) — صُحح لـ`## ما أعطتها`.
- **thk-wspaulding**: خطأ مزدوج — الاسم "ويلِم سَبُولدِنغ" (نطق مذكر) لشخص اسمه الحقيقي **Wilma** (مؤنث)، مع عنوان قسم `## ما أعطته` (مذكر) رغم أن باقي الملف يصفها بصيغة مؤنثة صحيحة ("عالمة نفس أمريكية"). صُحح الاسم لـ"ويلما" في كل الملف، وصُحح العنوان لـ"أعطتها".

### روابط related مكسورة/متضاربة (عيّنة، القائمة الكاملة أطول)
- عشرات الروابط كانت تشير لـslugs غير موجودة أصلاً (مثل thk-ekant بدل thk-kant، thk-fnietszche بدل thk-nietzsche، thk-kmarx بدل thk-marx، thk-harré، thk-jcampbell، thk-taisen، thk-npeale، thk-edurkheim، thk-gsimmel، thk-mluther، thk-hheilig، thk-rgriesinger، وغيرها) — إما صُححت لـslug الصحيح الموجود فعلاً في الأطلس، أو حُذفت مع الإبقاء على الاسم كنص عادي في المتن (وإضافة ملاحظة "غير موثّق بملف مستقل" حين الاسم يبقى مذكوراً).
- روابط بـtitle متضارب مع عنوان الملف الفعلي المستهدف (thk-yalom، con-trauma، con-iching، thk-sdeshazer، thk-jaspers... إلخ) — صُححت العناوين لتطابق الملف الحقيقي فعلياً بعد فتحه والتحقق.

### edges بنص حر → سُجّلت في missing-schools.md
ثمانية ملفات كان فيها `edges.belongs_to` يشير لنص حر بدل slug (لا مدرسة/تيار موجود فعلياً): thk-wayne-dyer (علم نفس شعبي وتنمية ذاتية)، thk-wmetzger (الجشطالت الإدراكي/برلين — متمايز عن sch-gestalt-therapy)، thk-wkroger (التنويم السريري الطبي)، thk-wjanzarik (مدرسة هايدلبرغ للطب النفسي الظاهراتي)، thk-wrichards (التنفس الهولوتروبي)، thk-ymohamed (علم النفس الإيجابي الإسلامي)، thk-weber (علم الاجتماع الكلاسيكي)، thk-zlipowski (الطب النفسجسدي). كلها حُذفت وسُجّلت في `agents_specs/missing-schools.md` بدل اختراع slug.

## متوقف عنده (لرئيس التحرير)

لا شيء متوقف — الدفعة اكتملت بالكامل، ولا يوجد قرار معلّق يحتاج مراجعة بشرية خارج ما هو موثّق أعلاه.

## الملفات

```
content/ar/thinkers/thk-ttolksdorf.md          [حُجر جديد]
content/ar/thinkers/thk-ttshishiku.md          [حُجر جديد]
content/ar/thinkers/thk-vburr.md
content/ar/thinkers/thk-vladimir-jankelevitch.md
content/ar/thinkers/thk-wade-nobles.md
content/ar/thinkers/thk-wass.md
content/ar/thinkers/thk-wayne-dyer.md
content/ar/thinkers/thk-wboechat.md            [إصلاح قالب حجر]
content/ar/thinkers/thk-weber.md
content/ar/thinkers/thk-werner.md              [حُجر جديد]
content/ar/thinkers/thk-westphal.md            [حُجر جديد]
content/ar/thinkers/thk-wilhelm.md
content/ar/thinkers/thk-wiseman.md
content/ar/thinkers/thk-wjanzarik.md
content/ar/thinkers/thk-wkroger.md
content/ar/thinkers/thk-wmasters.md
content/ar/thinkers/thk-wmetzger.md
content/ar/thinkers/thk-wood.md                [حُجر جديد]
content/ar/thinkers/thk-wrichards.md
content/ar/thinkers/thk-wspaulding.md
content/ar/thinkers/thk-wstekel.md
content/ar/thinkers/thk-wwood.md
content/ar/thinkers/thk-wzhang.md
content/ar/thinkers/thk-ydolan.md
content/ar/thinkers/thk-ymohamed.md
content/ar/thinkers/thk-ynakagami.md
content/ar/thinkers/thk-yongjingqi.md          [حُجر جديد]
content/ar/thinkers/thk-young.md               [حُجر جديد]
content/ar/thinkers/thk-yvaniedmon.md          [إصلاح قالب حجر + YAML مكسور]
content/ar/thinkers/thk-zambrano.md
content/ar/thinkers/thk-zhangyongqiang.md      [إصلاح قالب حجر]
content/ar/thinkers/thk-zlipowski.md
content/ar/thinkers/thk-zoroaster.md
content/ar/thinkers/thk-zubiri.md
content/ar/thinkers/thk-zygmunt-bauman.md
```

## ملفات مساندة محدَّثة
- `agents_specs/quarantine-minimax.md` — أُضيفت 7 أسطر جديدة (thk-ttolksdorf، thk-ttshishiku، thk-werner، thk-westphal، thk-wood، thk-young، thk-yongjingqi).
- `agents_specs/missing-schools.md` — أُضيفت 8 أسطر جديدة (انظر تفصيل أعلاه).
- `agents_specs/quarantine-minimax-archive/` — 8 ملفات أُرشفت: thk-ttolksdorf.md.archived.2026-08-27، thk-ttshishiku.md.archived.2026-08-27، thk-werner.md.archived.2026-08-27، thk-westphal.md.archived.2026-08-27، thk-wood.md.archived.2026-08-27، thk-young.md.archived.2026-08-27، thk-yongjingqi.md.archived.2026-08-27.
