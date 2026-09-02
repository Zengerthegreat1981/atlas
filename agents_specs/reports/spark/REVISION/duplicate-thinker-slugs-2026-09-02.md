# Spark — تكرار المفكّرين: الصورة الكاملة المصحَّحة

**التاريخ:** 2026-09-02 · **الحالة: ⛔ يحتاج قراراً بشرياً — لم يُنفَّذ أي دمج أو نقل**

## ⚠️ تصحيح لتقريري الأول من اليوم نفسه

النسخة الأولى من هذا التقرير قالت **18 حالة تكرار**. الرقم الصحيح **100**.

سبب الخطأ أنني طابقتُ **شكل الـslug** (`thk-<لقب>` مقابل `thk-<حرف><لقب>`) بدل أن أطابق
**حقل `en:`**. فحجب ذلك عني كل حالة لا تتبع هذين الشكلين — وهي الأغلبية: `thk-<الاسم>-<اللقب>`
(مثل `thk-dan-fisher`)، والـslugs المكتوبة بهجاء مختلف (`thk-orsigen` مقابل `thk-origen`)،
والـslugs التي **لا تحتوي اسم صاحبها إطلاقاً**.

انكشف الخطأ لأن وكيل الدفعة 4.3 أبلغ عن زوج `thk-dfisher`/`thk-dan-fisher` — وهو زوج حقيقي
**لم يكن في قائمة الـ18**. الدرس نفسه المتكرّر في هذه المراجعة: **قِس على الحقيقة (حقل `en:`)،
لا على الاصطلاح المفترَض.**

## الأرقام

| الفئة | العدد |
|---|---|
| أسماء لها **slugs مختلفة متعدّدة** | **100** |
| ملفات داخلة في هذه المجموعات | **203** |
| (أ) كعب صغير (<1,400 حرف) يظلّل ملفاً حقيقياً | 37 |
| (ب) ملفان جوهريان أو أكثر — دمج حقيقي | 63 |
| نفس الـslug في مسارَين (مشكلة ملفات لا أشخاص) | 38 |

لا يرى `build_slug_index.py` من هذا **شيئاً** إلا الفئة الأخيرة (الـ22 المعروفة): فهو يرصد
*نفس الـslug في مسارَين*، لا *slugs مختلفة لنفس الشخص*. وpreflight لا يراه أصلاً.

## (أ) كعوب صغيرة تظلّل ملفات حقيقية — الفئة الأكبر والأسهل

نمط واضح: ملف نحيل (840–1,400 حرف) بـ`refs=1` غالباً، مكتوب بالاسم الكامل، يقابله ملف حقيقي
مطوَّل ومرتبط بكثافة. هذه **أقلّ الحالات خطراً**: الكعب لا يحمل محتوى يُفقَد.

| الشخص | الكعب | حرف | روابط | الملف الحقيقي | حرف | روابط |
|---|---|---|---|---|---|---|
| Martin Heidegger | `thk-martin-heidegger` | 1155 | 1 | `thk-heidegger` | 6152 | **167** |
| William James | `thk-william-james` | 978 | 1 | `thk-james` | 3517 | **79** |
| Maurice Merleau-Ponty | `thk-maurice-merleau-ponty` | 973 | 1 | `thk-merleau-ponty` | 4258 | **65** |
| Karl Jaspers | `thk-karl-jaspers` | 1135 | 1 | `thk-jaspers` | 3156 | **49** |
| Frantz Fanon | `thk-frantz-fanon` | 1250 | 1 | `thk-fanon` | 4002 | **45** |
| Peter Fonagy | `thk-pfonel` | 1343 | 1 | `thk-fonagy` | 7848 | **26** |
| Stanislav Grof | `thk-mgrof` | 1062 | 2 | `thk-sgrof` | 5528 | **26** |
| Daniel J. Siegel | `thk-daniel-siegel` | 1149 | 1 | `thk-dsiegel` | 2758 | **22** |
| Henri Bergson | `thk-henri-bergson` | 984 | 1 | `thk-bergson` | 2486 | **21** |
| Hilary Putnam | `thk-hilary-putnam` | 1022 | 1 | `thk-hputnam` | 3173 | **16** |
| Gabriel Marcel | `thk-gabriel-marcel` | 994 | 1 | `thk-marcel` | 2264 | **13** |
| Arne Næss | `thk-anaess` | 1103 | 1 | `thk-arne-naess` | 2405 | **13** |
| Wilhelm Dilthey | `thk-wilhelm-dilthey` | 986 | 1 | `thk-dilthey` | 2214 | **12** |
| Gottlob Frege | `thk-gottlob-frege` | 1035 | 1 | `thk-gfrege` | 2771 | **11** |
| Han Feizi | `thk-han-feizi` | 1047 | 1 | `thk-hanfeizi` | 3647 | **10** |
| Moses Maimonides (Rambam) | `thk-maimonides-moses` | 1308 | 1 | `thk-maimonides` | 2816 | **9** |
| Paulin Hountondji | `thk-paulin-hountondji` | 967 | 1 | `thk-hountondji` | 2757 | **8** |
| Luce Irigaray | `thk-luce-irigaray` | 973 | 1 | `thk-irigaray` | 2440 | **7** |
| Chandra Talpade Mohanty | `thk-cmohanty` | 1111 | 1 | `thk-mohanty` | 2714 | **7** |
| Kwasi Wiredu | `thk-kwasi-wiredu` | 952 | 1 | `thk-wiredu` | 2754 | **6** |
| Moses Mendelssohn | `thk-moses-mendelssohn` | 840 | 1 | `thk-mendelssohn` | 2207 | **5** |
| Paul Feyerabend | `thk-paul-feyerabend` | 1044 | 1 | `thk-pfeyerabend` | 2062 | **5** |
| Mary Whitehouse | `thk-mwhitehouse` | 1373 | 6 | `thk-mary-whitehouse` | 2157 | **5** |
| Patricia E. Deegan | `thk-pdeegan` | 1289 | 4 | `thk-patdeegan` | 2181 | **5** |
| Max Stirner | `thk-max-stirner` | 1025 | 1 | `thk-stirner` | 3274 | **4** |
| Quentin Meillassoux | `thk-meillassoux` | 1309 | 1 | `thk-quentin-meillassoux` | 3936 | **4** |
| Marshall B. Rosenberg (Nonviolent Communication) | `thk-marshall-rosenberg` | 1330 | 2 | `thk-msrosenberg` | 3597 | **4** |
| Rifa'a al-Tahtawi | `thk-rifaa-al-tahtawi` | 1004 | 1 | `thk-tahtawi` | 3083 | **3** |
| Nasir al-Din al-Tusi | `thk-nasir-al-din-al-tusi` | 1144 | 1 | `thk-nasir-tusi` | 2681 | **3** |
| Origen of Alexandria | `thk-origen` | 1020 | 1 | `thk-orsigen` | 2380 | **2** |
| Francisco Suárez | `thk-francisco-suarez` | 943 | 1 | `thk-suarez` | 2456 | **2** |
| Philo of Alexandria (Philo Judaeus) | `thk-philo-judaeus` | 1015 | 1 | `thk-philo` | 3145 | **2** |
| Auguste Comte | `thk-auguste-comte` | 1278 | 1 | `thk-comte` | 3195 | **2** |
| Dan Olweus | `thk-dolweus` | 1053 | 5 | `thk-jeberenz` | 2383 | **2** |
| Roger T. Ames | `thk-rwilliams` | 1008 | 1 | `thk-rames` | 4677 | **2** |
| Abu al-Hasan al-Amiri | `thk-al-amiri` | 1032 | 1 | `thk-abu-al-hasan-al-amiri` | 3338 | **1** |
| Perikles Kastrinidis (Switzerland) | `thk-kastrinidis` | 1397 | 2 | `thk-perikles-kastrinidis-ch` | 2604 | **1** |

أبرزها: **مرلوبونتي** (كعب 973 حرفاً مقابل 4,258 بـ65 رابطاً)، و**تشومسكي**، و**تشيكسنتميهايي**،
و**موسى بن ميمون**، و**إيريغاراي**، و**شتيرنر**، و**مندلسون**.

## (ب) ملفان جوهريان — هنا القرار الحقيقي

في هذه الفئة **كلا الملفَّين يحمل محتوى موثَّقاً**، فالدمج يقتضي قراءة بشرية: أيُّهما الأساس،
وما يُنقَل من الآخر قبل تحويله إلى إحالة. و**المعيار الآلي يفشل**: «الأطول» و«الأكثر ارتباطاً»
يتناقضان في حالات كثيرة.

| الشخص | الملفات (حرف · روابط) | يتفق المعياران؟ |
|---|---|---|
| Immanuel Kant | `thk-kant` 6217ch/85 · `thk-immanuel-kant` 3973ch/1 | ✅ |
| Donald Winnicott | `thk-winnicott` 2579ch/43 · `thk-dwinnicott` 1741ch/1 | ✅ |
| Peter A. Levine | `thk-plevine` 6318ch/42 · `thk-peter-levine` 1529ch/3 | ✅ |
| Jon Kabat-Zinn | `thk-jkabat-zinn` 3209ch/35 · `thk-jkabat` 1782ch/1 | ✅ |
| Daniel Kahneman | `thk-kahneman` 7664ch/31 · `thk-rkahneman` 1736ch/1 | ✅ |
| Martin Buber | `thk-mbuber` 3003ch/28 · `thk-buber` 2295ch/2 | ✅ |
| Francine Shapiro | `thk-francine-shapiro` 5971ch/21 · `thk-francesharville` 5794ch/1 | ✅ |
| Steve de Shazer | `thk-sdeshacer` 5055ch/18 · `thk-sdeshazer` 1915ch/1 | ✅ |
| Bessel van der Kolk | `thk-besselvanderkolk` 4606ch/18 · `thk-bvdkolk` 2225ch/13 | ✅ |
| Alasdair MacIntyre | `thk-macintyre` 2461ch/17 · `thk-amacintyre` 2000ch/1 | ✅ |
| Eugene T. Gendlin | `thk-egendlin` 2452ch/2 · `thk-gendlin` 2352ch/17 | ⚠️ **لا** |
| Stephen Mitchell | `thk-mitchell` 2808ch/16 · `thk-smitchell` 1597ch/1 | ✅ |
| Thomas S. Kuhn | `thk-thomas-kuhn` 4563ch/16 · `thk-pkuhn` 1995ch/2 | ✅ |
| Mara Selvini Palazzoli | `thk-mselvini` 5754ch/15 · `thk-mselpalaz` 2061ch/1 | ✅ |
| Theodor W. Adorno | `thk-theodor-adorno` 4735ch/4 · `thk-adorno` 2401ch/15 | ⚠️ **لا** |
| Leslie Greenberg | `thk-lgreenberg` 5365ch/15 · `thk-greenberg-lisa` 3694ch/13 | ✅ |
| Carol Gilligan | `thk-gilligan` 3339ch/14 · `thk-cgilligan` 1677ch/2 | ✅ |
| Mihaly Csikszentmihalyi | `thk-csikszentmihalyi` 4780ch/13 · `thk-mcsikszent` 1615ch/1 | ✅ |
| Harville Hendrix | `thk-hhendrix` 5947ch/13 · `thk-harville-hendrix` 5019ch/2 | ✅ |
| Shahab al-Din Yahya ibn Habash Suhrawardi (Shaykh al-Ishraq) | `thk-suhrawardi` 6577ch/13 · `thk-sohrevardi` 2386ch/3 | ✅ |
| Steve Biko | `thk-jbiko` 2132ch/6 · `thk-biko` 1782ch/12 | ⚠️ **لا** |
| Noam Chomsky | `thk-noam-chomsky` 4185ch/2 · `thk-nchomsky` 3130ch/12 | ⚠️ **لا** |
| Aimé Césaire | `thk-cesaire` 1889ch/11 · `thk-aime-cesaire` 956ch/1 | ✅ |
| Rick Doblin | `thk-rmdoblin` 3683ch/11 · `thk-rick-doblin` 1825ch/5 | ✅ |
| Eric Berne | `thk-berne` 4058ch/2 · `thk-eburne` 3548ch/11 | ⚠️ **لا** |
| Leon Festinger | `thk-leon-festinger` 4807ch/2 · `thk-lfestinger` 4462ch/11 | ⚠️ **لا** |
| Roland R. Griffiths | `thk-roland-griffiths` 3637ch/10 · `thk-griffiths` 1667ch/4 | ✅ |
| Patricia Hill Collins | `thk-p-hill-collins` 4571ch/1 · `thk-phcollins` 3573ch/9 | ⚠️ **لا** |
| Kimberlé W. Crenshaw | `thk-kcrenshaw` 4592ch/5 · `thk-crenshaw` 2171ch/9 | ⚠️ **لا** |
| Jacob L. Moreno | `thk-jmoreno` 4034ch/9 · `thk-moreno` 2691ch/9 | ✅ |
| David Lewis | `thk-dlewis` 1964ch/8 · `thk-david-lewis` 1015ch/1 | ✅ |
| Alfred Schutz | `thk-schutz` 2263ch/8 · `thk-aschutz` 1829ch/1 | ✅ |
| Richard H. Thaler | `thk-rkthaler` 2216ch/7 · `thk-richard-thaler` 1424ch/1 | ✅ |
| Michael Mithoefer | `thk-mithoefer` 4032ch/5 · `thk-mmithoefer` 3811ch/7 | ⚠️ **لا** |
| Edward de Bono | `thk-de-bono` 4506ch/6 · `thk-edward-de-bono` 2590ch/2 · `thk-edward-de-bono` 1912ch/2 | ✅ |
| Paul Ekman | `thk-paul-ekman` 4393ch/5 · `thk-ekman` 3260ch/3 | ✅ |
| Laura N. Rice | `thk-lrice` 4044ch/5 · `thk-rice` 2689ch/3 | ✅ |
| Tu Weiming | `thk-ttu` 6613ch/4 · `thk-tfwang` 4803ch/1 | ✅ |
| J. Luke Wood | `thk-jlwood` 1982ch/1 · `thk-jroddy` 1214ch/4 | ⚠️ **لا** |
| Peter Felix Kellermann | `thk-tkellermann` 1817ch/1 · `thk-peterkellermann` 1481ch/4 | ⚠️ **لا** |

### مثال حاسم على فشل المعيار الآلي

`thk-gendlin` أقصر من `thk-egendlin` بمئة حرف، لكن **17 ملفاً يشير إليه مقابل 2**. الدمج نحو
الأطول يكسر 17 رابطاً ليربح 100 حرف. والعكس تماماً في **بوبر**: الأطول (`thk-mbuber`) هو أيضاً
الأكثر ارتباطاً (28 مقابل 2). فلا قاعدة واحدة تصلح للجميع.

## (ج) عطب مختلف وأخطر: slug لا يطابق صاحبه

أثناء هذا الفحص ظهرت فئة **ليست تكراراً**: ملفات الـslug فيها يسمّي شخصاً و`en:` يسمّي شخصاً آخر.

| الـslug | `en:` الفعلي | حرف | روابط |
|---|---|---|---|
| `thk-pfonel` | **Peter Fonagy** | 1343 | 1 |
| `thk-orsigen` | **Origen of Alexandria** | 2380 | 2 |
| `thk-mselvini` | **Mara Selvini Palazzoli** | 5754 | 15 |
| `thk-tfwang` | **Tu Weiming (杜维明)** | 4803 | 1 |
| `thk-ttu` | **Tu Weiming** | 6613 | 4 |
| `thk-sdeshacer` | **Steve de Shazer** | 5055 | 18 |
| `thk-hershman` | **Dina Wardi** | 1483 | 3 |
| `thk-hliddle-clin` | **Craig E. Henderson** | 1592 | 3 |
| `thk-lmorrnah` | **Abraham Kawai'ae'a** | 1554 | 2 |
| `thk-aulanc` | **Founders of Israel Jungian associations** | 2417 | 1 |
| `thk-rklenck` | **Founders of UK Jungian associations** | 1820 | 1 |
| `thk-francesharville` | **Francine Shapiro** | 5794 | 1 |
| `thk-jmertz` | **Mario Trevi** | 1671 | 1 |
| `thk-jeberenz` | **Dan Olweus** | 2383 | 2 |
| `thk-sohrevardi` | **Shahab al-Din Suhrawardi (Shaikh al-Ishraq)** | 2386 | 3 |
| `thk-jboss` | **David Berceli** | 1631 | 2 |
| `thk-jakhan` | **Wade W. Nobles** | 2640 | 4 |
| `thk-sadreddin-konevi` | **Sadr al-Din al-Qunawi (Sadruddin Konevi)** | 2272 | 2 |

بعض هذه الحالات هجاءٌ مغلوط لا أكثر (`thk-orsigen` لأوريجانوس، `thk-eburne` لإريك بيرن) وهي
هيّنة. لكن الباقي **محتوى شخص تحت اسم شخص آخر**، وأخطرها:

- `thk-francesharville` يحمل `en: "Francine Shapiro"` في 5,794 حرفاً — لكن **هذا الملف موسوم
  أصلاً** بعنوان «فرانسين شابيرو (ملف مكرّر)»، و`thk-francine-shapiro` موجود بـ5,971 حرفاً. أي أن
  الحالة **معروفة ومسجَّلة**، لا مكتشَفة. أوردتُها هنا لأن فحصي الأول قدّمها كأنها مجهولة وهذا خطأ.
- `thk-jboss` → **David Berceli** (والـslug يُقرأ «بوس»، وهناك `thk-boss` لميدارد بوس فعلاً).
- `thk-pfonel` → **Peter Fonagy**، و`thk-jeberenz` → **Dan Olweus**، و`thk-jmertz` → **Mario Trevi**،
  و`thk-hershman` → **Dina Wardi**، و`thk-hliddle-clin` → **Craig E. Henderson**، و`thk-jroddy` → **J. Luke Wood**.

**القاعدة 6 تمنع إعادة تدوير slug مؤسِّس لشخص آخر** — وهذه الحالات تخالفها فعلاً وهي قائمة الآن.

## (د) مدخلات جماعية أو موضوعية تحت بادئة `thk-`

فئة ثالثة ظهرت من نفس الفحص — `thk-` لما ليس شخصاً:

- **`thk-heidegger-technology`** (5,776 حرفاً): موضوع لا شخص. و`thk-heidegger` موجود
  بـ**167 رابطاً** ولا يمسّ التقنية إطلاقاً، و`thk-martin-heidegger` كعب ثالث بـ1,155 حرفاً.
  أي **هايدجر في ثلاثة ملفات**. والموضوع له بيوت صحيحة أصلاً: `wrk-question-concerning-technology`،
  `con-gestell`، `trm-gestell-enframing-heidegger`، `crt-heidegger-critique-of-technology`.
- **`thk-aulanc`** → `en: "Founders of Israel Jungian associations"`، و**`thk-rklenck`** →
  `en: "Founders of UK Jungian associations"`: مدخلات **جماعية** تحت بادئة شخص. ودفعة 4.2
  كانت قد وجدت أن محتوى `thk-aulanc` ملفَّق («Amit Maimon» لا وجود له).

## كم من هذا معروف أصلاً؟ — القياس الحاسم

سألتُ الملفات نفسها: هل يقول أيُّ عضو في المجموعة إنه مكرَّر أو حجر أو إحالة؟

| | العدد |
|---|---|
| مجموعات فيها **عضو واحد على الأقل موسوم** بأنه مكرَّر/حجر | **20** |
| مجموعات **لا شيء فيها يقول ذلك — صامتة تماماً** | **80** |

فالمشروع يعرف الخُمس ويجهل الأربعة أخماس. والصامتة تضمّ **أكثر مداخل الأطلس ارتباطاً**:

| الشخص | الملفات | الروابط الداخلة |
|---|---|---|
| **مارتن هايدجر** | `thk-heidegger` + `thk-heidegger-technology` + `thk-martin-heidegger` | **167** |
| إيمانويل كانط | `thk-kant` + `thk-immanuel-kant` | 85 |
| وليم جيمس | `thk-james` + `thk-william-james` | 79 |
| موريس مرلوبونتي | `thk-merleau-ponty` + `thk-maurice-merleau-ponty` | 65 |
| كارل ياسبرز | `thk-jaspers` + `thk-karl-jaspers` | 49 |
| فرانتز فانون | `thk-fanon` + `thk-frantz-fanon` | 45 |
| بيتر فوناغي | `thk-fonagy` + `thk-pfonel` | 26 |

## 🔑 السبب: موجة استيراد واحدة، لا أخطاء متفرّقة

هذه ليست حوادث مبعثرة. **17 ملفاً من الكعوب وُلدت من عملية واحدة**، وبصمتها قاطعة:

- **نفس العناوين الثلاثة حرفياً**: «الإسهام الفكري والموقع في تاريخ الفلسفة» ثم «الأثر والامتداد
  المعاصر» ثم «اقتباسات مختارة».
- **نطاق `id` متّصل**: THK-2275 … THK-2550.
- **الوسيط 1,004 أحرف** لكل ملف، و`level: متقدم` و`part: philosophy` في كلها.
- و`refs=1` في كلها — أي **لا أحد يشير إليها**؛ الشبكة كلها تشير إلى الملف الأصلي.

وحين فحصتُ كل ملف يحمل هذه البصمة الثلاثية في الأطلس بأكمله: **18 ملفاً، منها 17 يكرّر شخصاً
موجوداً بالفعل**. أي أن هذه الموجة **سبب 17 حالة تكرار بلا استثناء تقريباً**:

```
thk-kwasi-wiredu      952ch  ->  thk-wiredu       (2,754)
thk-aime-cesaire      956ch  ->  thk-cesaire      (1,889)
thk-paulin-hountondji 967ch  ->  thk-hountondji   (2,757)
thk-maurice-merleau-ponty 973 -> thk-merleau-ponty (4,258)
thk-luce-irigaray     973ch  ->  thk-irigaray     (2,440)
thk-william-james     978ch  ->  thk-james        (3,517)
thk-henri-bergson     984ch  ->  thk-bergson      (2,486)
thk-wilhelm-dilthey   986ch  ->  thk-dilthey      (2,214)
thk-gabriel-marcel    994ch  ->  thk-marcel       (2,264)
thk-david-lewis      1015ch  ->  thk-dlewis       (1,964)
thk-philo-judaeus    1015ch  ->  thk-philo (3,145) + thk-philo-alexandria (2,259)
thk-origen           1020ch  ->  thk-orsigen      (2,380)
thk-hilary-putnam    1022ch  ->  thk-hputnam      (3,173)
thk-max-stirner      1025ch  ->  thk-stirner      (3,274)
thk-al-amiri         1032ch  ->  thk-abu-al-hasan-al-amiri (3,338)
thk-paul-feyerabend  1044ch  ->  thk-pfeyerabend  (2,062)
thk-karl-jaspers     1135ch  ->  thk-jaspers      (3,156)
```

**لماذا هذا يغيّر القرار:** هذه السبعة عشر **أسهل الحالات على الإطلاق**. كلها كعوب ~1,000 حرف
بصفر روابط داخلة، ولا تحمل محتوى يُفقَد، ومنشؤها واحد. فتحويلها إلى إحالات عملٌ **واحد متجانس**
لا سبعة عشر قراراً. وهي تشمل مرلوبونتي وجيمس وياسبرز وكانط — أي أكبر عائد بأقل خطر.

وما يبقى بعدها للقراءة البشرية هو الحالات التي فيها **كلا الملفَّين جوهريّ** فعلاً.

## المطلوب منك — ثلاثة قرارات مستقلّة

**1. موجة الاستيراد (17 ملفاً) والكعوب الأخرى** — أقلّها خطراً وأعلاها عائداً. اقتراحي: يبقى
   الملف الحقيقي، ويصير الكعب **إحالة** إليه
   (لا يُحذف، القاعدة 6). 37 حالة، قابلة للتنفيذ دفعةً واحدة بعد موافقتك.

**2. الدمج الحقيقي (ب)** — يحتاج قراراً لكل زوج. قاعدة افتراضية مقترحة: **يبقى الأكثر ارتباطاً**
   (يحفظ سلامة الشبكة)، ويُنقَل إليه المحتوى الموثَّق الزائد من الآخر قبل الإحالة، فلا يُفقد شيء.
   63 حالة — وهذا هو العمل البشري الفعلي.

**3. عطب الهوية (ج) و(د)** — منفصل عن التكرار ويستحقّ أولوية أعلى في رأيي: ملف بـ5,794 حرفاً
   عن مؤسِّسة EMDR تحت slug باسم شخص آخر عطبٌ في الإحالة نفسها، لا في الطول.

## ما لم يُفحَص

هذا الفحص غطّى **`thk-` فقط**. نفس الاصطلاحات المتوازية قد تكون كرّرت مدخلات في `wrk-` و`stu-`
و`ins-` و`tec-` — ولم أفحصها بعد. كما أن الفحص يعتمد على وجود حقل `en:`؛ فأي ملف بلا `en:`
لا يظهر فيه إطلاقاً.
