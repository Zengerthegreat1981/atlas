# تدقيق MiniMax — دفعات T1.1–1.14 وT2.1 (275+15 ملف)

تدقيق فعلي ملف-بملف لكل ما كتبه/عدّله MiniMax حتى الآن، بواسطة 15 وكيل قراءة مستقل (كل واحد غطى دفعة).
هدف الملف: قائمة أعمال محددة لـMiniMax يصلحها، مش نقد عام.

---

## 0) أخطر ملاحظة: `agents_specs/quarantine-minimax.md` غير موجود إطلاقاً

عشرات الملفات (thk-niosepa, thk-trudakova, thk-zhangyongqiang, thk-schulz, thk-mariannekline,
thk-margaret-bluestein, thk-michael-derm, thk-rrestrepo, thk-mcieslak, thk-pekkajokinen,
thk-peter-bloom, thk-masaaki-takahashi, thk-mmejia, thk-wboechat, thk-rosemaryalara,
thk-ma-rosario-alfelor, thk-michaelsweeting, thk-spiper, thk-pgodfrey, thk-rhooton، وغيرها كتير)
تحتوي **نصاً صريحاً في المتن أو gaps بيقول** "توصية الحجر في `agents_specs/quarantine-minimax.md`" —
لكن الملف ده **مش موجود على الإطلاق** في المستودع. يعني القرار اتاخد ومحدش نفّذه. الأخطر: بعض هذه
الملفات كتبت الجملة دي **كمصدر فعلي تحت `## المصادر`** (مثلاً thk-niosepa، thk-trudakova،
thk-zhangyongqiang، thk-schulz) — ملاحظة تحريرية داخلية اتحطت مكان استشهاد ببليوغرافي حقيقي.

**الفعل المطلوب:** أنشئ `agents_specs/quarantine-minimax.md` فوراً، وانقل له كل الأسماء اللي فعلاً
مش موثّقة (قايمة تحت في القسم 1) بدل ما تفضل منشورة كملفات سيرة عادية.

---

## 1) أشخاص منشورين كسيرة عادية بينما الملف نفسه بيعترف إنه مش قادر يوثّق وجودهم

نمط متكرر جداً عبر الدفعات: الملف بيكتب سيرة كاملة (تواريخ، أعمال، شبكة علاقات) لشخص، وفي نفس
الوقت الـ`gaps` أو المتن بيقول صراحة "الاسم لم أعثر عليه مستقلاً"، أو بيقترح 2-3 أشخاص حقيقيين
تانيين ممكن يكون فيه لبس معاهم. ده **مخالف مباشر** لقاعدة Task 2 في MINIMAX.md ("موثّق / غير موجود
/ غامض — فقط") — النتيجة الصح هنا "غامض → gaps بدقة" أو "غير موجود → حجر"، مش نشر سيرة موثوقة الشكل.

قائمة الملفات المتأثرة (غير شاملة بس الأوسع):
`thk-mcieslak، thk-pekkajokinen، thk-peter-bloom، thk-masaaki-takahashi، thk-mmejia، thk-wboechat،
thk-rosemaryalara، thk-ma-rosario-alfelor، thk-michaelsweeting، thk-spiper، thk-pgodfrey، thk-niosepa،
thk-trudakova، thk-zhangyongqiang، thk-schulz، thk-mariannekline، thk-margaret-bluestein،
thk-michael-derm، thk-rrestrepo، thk-rhooton، thk-paula-penda، thk-margaretbodkin، thk-rklenck،
thk-rmhinshaw (حالة أخف — الـdates نفسها "[غير مؤكد]" بس المتن واثق بشدة)`
+ 21 ملف "حجر ذاتي" صريح من دفعة 1.5 (thk-rbauer, thk-zmailloux, thk-sdouglas, thk-pfisher,
thk-young, thk-mclayton, thk-rick-levy, thk-m-amatos, thk-rupertpriest, thk-melanie-segall,
thk-michael-guthrie, thk-mary-elmquist, thk-skalama, thk-rvendramini) وباتشات 1.7 (16 ملف) و1.9
(7 ملفات) — راجع تقارير الوكلاء الأصلية للقائمة الكاملة.

**الفعل المطلوب:** لكل ملف من دول، رجّع لـTask 2 وطبّق القرار التلاتي الصحيح (موثّق بمصادر حقيقية /
حجر في quarantine-minimax.md / غامض بgaps دقيقة) — مش سيبانه منشور بشكل واثق.

---

## 2) خطأ جنس نحوي منهجي: `## أهم أعمالها` لرجل

نمط بيتكرر بكثافة عالية جداً في دفعات 1.11–1.14 خصوصاً — العنوان الفرعي `## أهم أعمالها` (صيغة
مؤنث "هي") بيتحط لرجل موصوف بصيغة مذكر في باقي الملف بالكامل. ده يبدو bug في قالب توليد ثابت
مش بيتراجع.

ملفات مؤكدة: `thk-mgold، thk-mtrevi، thk-pritz، thk-snygg، thk-snichols، thk-mahfouz، thk-tbarber،
thk-philippe-cunningham، thk-rryan، thk-rosenfeld، thk-spiegelberg، thk-robert-emery، thk-sstanley،
thk-wanthony، thk-yogananda، thk-russellrazzaque، thk-tgreening، thk-mithoefer، thk-nionescu،
thk-mmithoefer، thk-svami-akhilananda (كمان جمل متنية زي "تلتقي أعمالها")، thk-sothmer، thk-rlandy-md،
thk-rennie، thk-tbrazelton، thk-savodnik، thk-roland-tolentino، thk-william-hudson، thk-wolf،
thk-raphael، thk-wdowling، thk-rhanson، thk-mrolls، thk-moss، thk-mnichols، thk-rkaes، thk-peperzak،
thk-robert-rotella، thk-mayeroff، thk-rshort، thk-sleclaire، thk-mtotton، thk-michael-yarp`

**الفعل المطلوب:** مسح آلي (grep) عبر كل ملفاتك المكتوبة على `## أهم أعمالها` و`## علاقتها`، وتصحيح
الصيغة لمذكر (`أعماله` / `علاقته`) لأي رجل. راجع كل ملف فيه المشكلة دي كنموذج للتحقق أولاً.

---

## 3) `related` — تطابق id/title مكسور (نسخ-لصق من ملف تاني)

هذا مباشرة القاعدة 6 اللي Spark أضافها لـSPARK.md ("كل id في related لازم يطابق فعلياً الـtitle").
عندك نفس المشكلة بكثافة أعلى من Spark:

أمثلة موثقة: `thk-ppapp (id:thk-olitwak/title:أولغا سيلفرشتاين)`، `thk-pbooth (مرتين)`،
`thk-rbenenzon`، `thk-petersmith`، `thk-tandersen`، `thk-martin-luther-king (id يوحي برالف أبورن،
title يوصف رالف والدو إمرسون — خلط شخصين مختلفين تماماً)`، `thk-tim-ferriss (مرتين، وكمان id واحد
thk-rkoch مستخدم لشخصين مختلفين بين thk-tim-ferriss وthk-spencer-johnson)`، `thk-maxwell-maltz
(مايكل بندلر بدل ريتشارد باندلر الحقيقي)`، `thk-sschoenwald (id يشاور لنفس صفحته هو)`،
`thk-margaretbodkin (id واحد مستخدم مرتين لاسمين مختلفين تماماً)`، `thk-rklenck (id لشخص، والمحتوى
كله عن مؤسسي جمعيات — لا علاقة)`، `thk-mramose`، `thk-theresaglasser`، `thk-nassim-taleb
(دان جيلبوت = دانيال كانمان الحقيقي!)`، `thk-steven-pinker`، `thk-richard-dawkins (ملاحظة تحريرية
متروكة في title: "لا أرى تفسير")`، `thk-mgriffiths`، `thk-michaelsweeting (نفس الشخص بid مختلفين)`،
`thk-wood (مرتين، وأيضاً صياغة title="..." الخاطئة نحوياً)`، `thk-mary-stewart (title="..." خاطئة)`،
`thk-mayeroff (id يشاور لنفسه، title لإرنست بيكر)`، `thk-rhooton`، `thk-vjohnson (هارفي كابلان =
هارولد ليف الحقيقي، مش هيلين كابلان)`، `thk-strindberg`، `thk-rmdoblin (id يكرر الشخص نفسه بid تاني)`،
`thk-wrichards (نفس con- مربوط 3 مرات بtitles مختلفة)`، `thk-mithoefer`.

**الفعل المطلوب:** لكل رابط، افتح الـid المستهدف فعلياً وتأكد إن العنوان اللي كتبته جنبه هو نفسه
عنوان الملف الحقيقي. الصياغة `title="..."` بعلامة `=` مش صيغة YAML صحيحة — دور على كل الحالات دي
بالبحث النصي وصلّحها لـ`title: "..."`.

---

## 4) `gaps` بتكرر حقيقة مؤكدة أصلاً في المتن (مخالفة معيار القبول #5)

نمط منتشر بقوة في 1.12–1.14: الـgap بيقول "سنة الميلاد (كذا) موثّقة" أو "تأسيسه لكذا موثّق" —
ده مش gap، ده تأكيد. المعيار الحالي في MINIMAX.md بيرفض بالفعل "لم يُراجع من مصدر أولي" لكن مش واضح
بما يكفي إنه بيرفض كمان "X موثّق" كصيغة gap.

أمثلة: `thk-mrolls، thk-mnichols، thk-rkaes، thk-peperzak، thk-mayeroff، thk-rbarkley، thk-nazrin،
thk-wass، thk-rmhinshaw، thk-todes، thk-snygg، thk-pritz، thk-rmdoblin، thk-wrichards، thk-rosenfeld،
thk-mnaumburg، thk-tbarber، thk-mgergen، thk-msolomon، thk-mgold، thk-mharris`

**الفعل المطلوب:** راجع كل `gaps` كتبته وتأكد إنه بيسمي حاجة **غير موجودة** في الملف، مش بيعيد
حاجة موجودة بالفعل.

---

## 5) أخطاء نَسَب/هوية (خلط شخصين حقيقيين بنفس الاسم أو اسم قريب)

`thk-matthew-walker (تناقض: تدرّب عند رختشافن في هارفارد ولا شيكاغو؟)`، `thk-sbem (داريل بيم
اتكتب "داريك"، ووصفوه فيلسوف بدل عالم نفس، ووفاته بمساعدة طبيب في أوريغون غير موثقة)`،
`thk-rick-hanson (نسبوا تأسيس IPNB لـ"ماركوس سيغل" بدل دانيال سيغل الحقيقي)`، `thk-vjohnson
(هارفي كابلان = هارولد ليف مش هيلين كابلان)`، `thk-tgrandin (كلير دينيس بدل كلير دينس الممثلة)`،
`thk-wstekel (كرافت-إبينغ مش من مؤسسي جمعية الأربعاء)`، `thk-susan-anderson (نسبوا لها كتاب
"Black Swan" وهو كتاب طالب الحقيقي)`، `thk-mmithoefer (وليام ريتشاردز "أحد مؤسسي EMDR" — خطأ،
EMDR أسستها فرانسين شابيرو)`، `thk-rennie (نسبوا له تطوير IPR، والمنهج فعلياً لنورمان كيغان)`،
`thk-osilver (كتاب The First Three Years of Life منسوب مشاركة لها، والمعروف إنه لبيرتون وايت منفرداً)`،
`thk-michelle-weiner-davis (مصنّفة "مؤسِّسة" Imago رغم إن المتن نفسه بيقول المؤسس هارفيل هندريكس)`،
`thk-ymohamed (تناقض داخلي: نفس الشخص "النموذج الباكستاني" و"رائد في مصر" في نفس الملف)`.

---

## 6) تواريخ متناقضة داخلياً

`thk-wjanzarik (إشراف 1946 على أطروحة نُشرت 1959)`، `thk-wmasters (فجوة تواريخ زواج/طلاق)`،
`thk-mfarkas (مصدر منشور 2012 بعد وفاتها المزعومة 2010 من غير ذكر "بعد وفاتها")`،
`thk-rene-girard (تناقض بين "1981–" و"1981–1995" لنفس الوظيفة)`، `thk-paci (active_end 1963 بينما
المتن بيوصف نشاط فكري مستمر للستينات)`، `thk-ppenn (active_end 2010 بينما وفاتها مذكورة 2006-2007)`،
`thk-tgreening (active_start=active_end=1971 بينما عمل حتى 2005 ومات 2022)`، `thk-raphael
(active_end 1981 والمصادر فيها كتاب 1993)`، `thk-rennie (dates تقول "1939–" حي، وactive_end 2000)`،
`thk-wiseman (active_start=active_end=2008 لشخص "معاصرة" وفيها علامة تنصيص شاردة كمان)`.

**الفعل المطلوب:** أي `active_end` أو `dates` لازم يتفحص مقابل أحداث المتن نفسه — تناقض بين
frontmatter والمتن = خطأ لازم يتصحح فوراً.

---

## 7) إعادة استخدام slug لشخص تاني تماماً (القاعدة اللي Spark أضافها حديثاً)

`thk-mark-santross (المحتوى فعلياً عن Mark R. Dombeck)`، `thk-rklenck (id لشخص، محتوى عن مؤسسي
جمعيات ككل)`، `thk-saberg-abramovitz (شخصان مختلفان في ملف واحد بid واحد)`، `thk-rkeller (المحتوى
كله عن Robert M. Clark)`، `thk-sbooth (المحتوى عن Sandra Lindaman، والslug يوحي بـBooth الحقيقية
الموجودة فعلاً في نفس مجال Theraplay)`، `thk-wdowling (معترف بنفسه في gaps: خطأ كتابي، الشخص فعلياً
Na'im Akbar)`، `thk-michael-yarp (معترف بنفسه: يجب أن يكون thk-michael-yapko)`، `thk-rackoff
(معترف بنفسه: خطأ كتابي لـRussell Ackoff)`، `thk-tmoriiyama (الslug في frontmatter ما بيطابقش اسم
الملف على القرص نفسه)`.

**الفعل المطلوب:** هذه القاعدة موجودة الآن رسمياً في SPARK.md rule 6 — لازم تتضاف لـMINIMAX.md
بنفس الصيغة (تحت في التعديلات المقترحة).

---

## 8) مشاكل تقنية إضافية

- **صيغة YAML خاطئة** `title="..."` بدل `title: "..."` — `thk-wood` (مرتين)، `thk-mary-stewart`.
- **حقل تاريخ لسه placeholder منشور** `dates: "[DRAFT-UNKNOWN]"` — `thk-russellrazzaque`،
  `thk-sothmer`.
- **روابط Markdown متكسرة تظهر كنص حرفي** — `thk-minopaulin` (`[كولين كيلي](thk-alexandra-farkas —
  بالتبادل مع [ألكسندرا فاركاش]...)`).
- **حقل `edges` بصيغة غير موحّدة** (`type:` بدل `target_type:`) — `thk-susan-koch`.
- **روابط `related` مذكورة في المتن لكن غائبة من frontmatter، أو العكس** — `thk-tbrazelton`،
  `thk-mricard`، `thk-mjohnson`، عدد كبير من الملفات في 1.11-1.13 (mgergen، tony-white،
  mimordino-yang، osilver، pfreire، rrestrepo، إلخ) — روابط في `related` بلا أي ذكر أو تبرير في
  المتن (مخالفة مباشرة لمعيار القبول #4).

---

## ملخص الفعل المطلوب من MiniMax (أولويات بالترتيب)

1. أنشئ `agents_specs/quarantine-minimax.md` الآن، وابدأ ينقله كل الحالات في القسم 1.
2. مسح شامل (grep) على `## أهم أعمالها` و`## علاقتها` عبر كل ملفاتك، صحّح صيغة الجنس لأي رجل.
3. راجع كل رابط `related` كتبته: افتح الـid فعلياً، قارن العنوان — صحّح كل تطابق مكسور (القسم 3).
4. راجع كل `gaps` كتبته: احذف أي سطر بيؤكد حقيقة بدل ما يسمي فجوة حقيقية.
5. صحّح التناقضات الزمنية المذكورة في القسم 6 ملف بملف.
6. طبّق قاعدة منع إعادة استخدام slug (القسم 7) — لو لقيت حالة زي دي تانية مستقبلاً، اطلب slug
   جديد صحيح ولا تكتب "احتفظنا بالslug التاريخي."
