# Spark — تكرار المفكّرين: الملفات الحيّة

**التاريخ:** 2026-09-02 · **الحالة: ⛔ يحتاج قراراً بشرياً — لم يُنفَّذ أي دمج**

## ⚠️ تصحيحان لهذا التقرير نفسه

مرّ هذا التقرير بخطأين مني، والثاني هو الأهم لأنه يغيّر القرار:

**الخطأ الأول (رقم أقلّ من الحقيقة):** قلتُ **18 حالة**، لأنني طابقتُ *شكل الـslug*
(`thk-<لقب>` مقابل `thk-<حرف><لقب>`) بدل حقل `en:`. فحجب ذلك كل اصطلاح آخر — ومنه
`thk-<الاسم>-<اللقب>`. انكشف ببلاغ وكيل عن زوج `thk-dfisher`/`thk-dan-fisher`.

**الخطأ الثاني (رقم أكبر من الحقيقة):** ثم قلتُ **100 حالة**، وهذا مبالَغ فيه: كان فحصي يضمّ
شجرة `content/ar/_merged/`. و**`build_atlas.py` يستثني `_merged` من البناء نصّاً** (السطر 166:
`d != "drafts" and d != "_merged"`) — أي أن ملفاتها **مُتقاعدة أصلاً ولا تظهر في الأطلس**.

انكشف هذا لأن وكيل الدفعة 4.4 أبلغ أن `thk-kwasi-wiredu` و`thk-paulin-hountondji` لا وجود لهما
خلافاً لما كتبتُه. وكان مُحقّاً: هما في `_merged`.

| الفحص | العدد |
|---|---|
| بحساب `_merged` (ما قاله تقريري) | 100 |
| **بعد استثناء `_merged` — الأطلس الحيّ فعلاً** | **57** |
| تضخّم ناتج عن `_merged` | 43 |

### وأخطر ما سقط بهذا التصحيح

**«موجة الاستيراد» التي قدّمتها كأهمّ نتيجة — وأنها 17 إصلاحاً سهلاً يشمل كانط ووليم جيمس
ومرلوبونتي وياسبرز — كلّها في `_merged`. أي أن المشروع كان قد عالجها فعلاً بإحالتها إلى
الشجرة المتقاعدة.** عدد ملفات تلك الموجة الحيّة: **صفر**.

وكذلك سقطت أمثلتي الكبرى: كانط (85 رابطاً) ووليم جيمس (79) ومرلوبونتي (65) وياسبرز (49)
وفانون (45) وبوبر — كعوبها كلها متقاعدة. الشيء الوحيد الباقي من قائمتي البارزة هو **هايدجر**.

## الحالة الحقيقية: 57 مجموعة حيّة، منها 39 صامتة

18 مجموعة فيها عضو موسوم بأنه مكرَّر أو حجر — أي المشروع يعرفها. و**39
مجموعة لا شيء فيها يقول ذلك**. ولا يرى هذا `build_slug_index.py` (يرصد *نفس الـslug في مسارَين*،
وهي الـ22 المعروفة) ولا `preflight_check.py`.

## الجدول — الصامتة، مرتَّبة بالروابط الداخلة

| الشخص | الملفات (حرف · روابط) | يتفق «الأطول» و«الأكثر ارتباطاً»؟ |
|---|---|---|
| Martin Heidegger | `thk-heidegger` 6152/167 · `thk-heidegger-technology` 5880/4 | ✅ |
| Bessel van der Kolk | `thk-besselvanderkolk` 4606/18 · `thk-bvdkolk` 2225/11 | ✅ |
| Eugene Gendlin | `thk-gendlin` 2352/16 · `thk-egendlin` 2452/2 | ⚠️ **لا** |
| Theodor Adorno | `thk-adorno` 2401/15 · `thk-theodor-adorno` 4735/4 | ⚠️ **لا** |
| Leslie Greenberg | `thk-lgreenberg` 5365/15 · `thk-greenberg-lisa` 3694/13 | ✅ |
| Harville Hendrix | `thk-hhendrix` 5947/13 · `thk-harville-hendrix` 5019/2 | ✅ |
| Shahab al-Din Yahya ibn Habash Suh | `thk-suhrawardi` 6577/13 · `thk-sohrevardi` 2386/3 | ✅ |
| Steve Biko | `thk-biko` 1782/12 · `thk-jbiko` 2132/6 | ⚠️ **لا** |
| Noam Chomsky | `thk-nchomsky` 3130/12 · `thk-noam-chomsky` 4185/2 | ⚠️ **لا** |
| Eric Berne | `thk-eburne` 3548/11 · `thk-berne` 4058/3 | ⚠️ **لا** |
| Roland R. Griffiths | `thk-roland-griffiths` 3637/10 · `thk-griffiths` 1667/4 | ✅ |
| Jacob L. Moreno | `thk-jmoreno` 4034/9 · `thk-moreno` 2691/9 | ✅ |
| Kimberlé Crenshaw | `thk-crenshaw` 2171/8 · `thk-kcrenshaw` 4592/5 | ⚠️ **لا** |
| Dan Olweus | `thk-dolweus` 1053/5 · `thk-jeberenz` 2383/2 | ⚠️ **لا** |
| Paul Ekman | `thk-paul-ekman` 4393/5 · `thk-ekman` 3260/3 | ✅ |
| Laura N. Rice | `thk-lrice` 4044/5 · `thk-rice` 2689/3 | ✅ |
| J. Luke Wood | `thk-jroddy` 1214/4 · `thk-jlwood` 1982/1 مسودة | ⚠️ **لا** |
| Peter F. Kellermann | `thk-peterkellermann` 1481/4 · `thk-tkellermann` 1817/1 | ⚠️ **لا** |
| Helen LaKelly Hunt | `thk-hlkelly` 2343/4 · `thk-helen-lakelly-hunt` 5535/1 | ⚠️ **لا** |
| Wade W. Nobles | `thk-jakhan` 2640/4 · `thk-wade-nobles` 4539/3 | ⚠️ **لا** |
| Roberto Assagioli | `thk-assagioli` 2908/4 · `thk-robert-assagioli` 3642/2 | ⚠️ **لا** |
| Donald Meichenbaum | `thk-meichenbaum` 2559/4 · `thk-dmeichenbaum` 1719/1 | ✅ |
| Dan Zahavi | `thk-dzahavi` 4571/3 مسودة · `thk-zahavi` 4577/2 مسودة | ⚠️ **لا** |
| Dina Wardi | `thk-hershman` 1483/3 · `thk-dina-wardi` 1451/1 مسودة | ✅ |
| Craig E. Henderson | `thk-hliddle-clin` 1592/3 · `thk-craig-henderson` 1912/1 مسودة | ⚠️ **لا** |
| Donna M. Orange | `thk-dorange` 5187/3 · `thk-lorange` 2066/3 | ✅ |
| Philo of Alexandria | `thk-philo-alexandria` 2259/3 · `thk-philo` 3145/2 | ⚠️ **لا** |
| Edith Stein | `thk-stein` 2128/3 · `thk-edith-stein` 5902/1 | ⚠️ **لا** |
| Nancy J. Chodorow | `thk-lchodorow` 1817/3 · `thk-chodorow` 2131/3 | ⚠️ **لا** |
| Perikles Kastrinidis | `thk-kastrinidis` 1397/2 · `thk-perikles-kastrinidis-ch` 2604/1 مسودة | ⚠️ **لا** |
| Abraham Kawai'ae'a | `thk-lmorrnah` 1554/2 · `thk-abraham-kawai` 1479/1 مسودة | ✅ |
| Charles Brenner | `thk-ibrenner` 2637/2 · `thk-cbrenner` 1547/2 | ✅ |
| David Berceli | `thk-jboss` 1631/2 · `thk-david-berceli` 3538/2 | ⚠️ **لا** |
| Lester Luborsky | `thk-jluborsky` 4021/2 · `thk-lluborsky` 1638/2 | ✅ |
| Dale Carnegie | `thk-dale-carnegie` 3805/2 · `thk-carnegie` 4143/2 | ⚠️ **لا** |
| Ernest S. Wolf | `thk-ewolf` 2102/2 · `thk-wolf` 3560/2 | ⚠️ **لا** |
| Sadr al-Din al-Qunawi | `thk-sadr-al-din-al-qunawi` 3311/2 · `thk-sadreddin-konevi` 2272/2 | ✅ |
| Michael D. Yapko | `thk-michael-yapko-jr` 2146/2 · `thk-michael-yapko` 2768/1 | ⚠️ **لا** |
| Mario Trevi | `thk-mtrevi` 2870/1 · `thk-jmertz` 1671/1 | ✅ |

**22 من 39** يتعارض فيها المعياران — وهذه ما لا يُحسَم آلياً.

## لماذا لا قاعدة واحدة تصلح

`thk-gendlin` أقصر بمئة حرف من `thk-egendlin` لكن **16 ملفاً يشير إليه مقابل 2**: الدمج نحو
الأطول يكسر 16 رابطاً ليربح 100 حرف. وفي **أدورنو** العكس: `thk-theodor-adorno` أطول بالضعف
(4,735 مقابل 2,401) لكن `thk-adorno` هو المرتبط (15 مقابل 4) — والمحتوى الأكثر في الملف الأقلّ
ارتباطاً، فلا بدّ من نقله قبل الإحالة. و**كرينشو** و**إديث شتاين** و**هيلين لاكيلي هَنت** بنفس الشكل.

والحالتان الأصعب متعادلتان في الروابط تماماً — **مورينو** (9 و9) و**تشودورو** (3 و3) —
فلا مرجّح آلي فيهما بحال.

## أولوية مقترحة

**1. هايدجر أولاً.** `thk-heidegger` (6,152 حرفاً، **167 رابطاً**) و`thk-heidegger-technology`
(5,880 حرفاً، 4 روابط) — والثاني **موضوع لا شخص**، والأول لا يمسّ التقنية إطلاقاً. وللموضوع
بيوت صحيحة موجودة أصلاً: `wrk-question-concerning-technology`، `con-gestell`،
`trm-gestell-enframing-heidegger`، `crt-heidegger-critique-of-technology`. فهذه ليست دمج شخصَين
بل **نقل موضوع من بادئة `thk-` إلى بادئته الصحيحة** — أوضح قرار في القائمة وأثقلها وزناً.

**2. الأزواج التي يتفق فيها المعياران** — الأكثر ارتباطاً هو أيضاً الأطول. تنفيذها مباشر:
يبقى الأول، ويصير الثاني إحالة.

**3. الـ22 المتعارضة** — تحتاج قراراً لكل زوج. قاعدة افتراضية مقترحة: **يبقى الأكثر ارتباطاً**
(يحفظ سلامة الشبكة)، و**يُنقَل إليه المحتوى الموثَّق الزائد من الآخر قبل الإحالة** فلا يُفقد شيء.

**4. `thk-ieyberg`/`thk-seyberg`** — جاهز بتوصية مفصَّلة من الدفعة 4.4: يبقى `thk-ieyberg`
(5,003 حرفاً و5 روابط بعد التعميق)، ويُنقَل إليه من `thk-seyberg` ما يفتقده: مدّة عمله في
OHSU 1974–1985 وفصل Funderburk & Eyberg (2011). ويُلاحَظ أن رابطَي `thk-seyberg` الخارجيَّين
(`sch-humanistic` و`sch-positive-psychology`) خطأ على أي حال لطبيبة نفس أطفال سلوكية.

## فئة منفصلة وأخطر: slug باسم شخص ومحتوى شخص آخر

العطب هنا في **الإحالة** لا في الطول، والقاعدة 6 تمنع إعادة تدوير slug لشخص آخر:

| الـslug | `en:` الفعلي | ملاحظة |
|---|---|---|
| `thk-cwhitaker-pt` | **John Marsh** | slug أُعيد تدويره؛ جسمه «[بيانات غير متاحة]» |
| `thk-jboss` | **David Berceli** | و`thk-boss` لميدارد بوس موجود فعلاً |
| `thk-jroddy` | **J. Luke Wood** | |
| `thk-jeberenz` | **Dan Olweus** | و`thk-dolweus` موجود بـ5 روابط |
| `thk-jmertz` | **Mario Trevi** | و`thk-mtrevi` موجود |
| `thk-hershman` | **Dina Wardi** | |
| `thk-hliddle-clin` | **Craig E. Henderson** | |
| `thk-lmorrnah` | **Abraham Kawai'ae'a** | |
| `thk-jakhan` | **Wade W. Nobles** | |

## مدخلات ليست أشخاصاً تحت بادئة `thk-`

- `thk-heidegger-technology` — موضوع (انظر الأولوية 1 أعلاه).
- `thk-aulanc` و`thk-rklenck` — `en:` فيهما «Founders of … Jungian associations»: **مدخلات
  جماعية**. ومحتوى الأول ملفَّق («Amit Maimon» لا وجود له) كما أثبتت الدفعة 4.2.
- `thk-hermes-trismegistus` — مؤلِّف **منسوب** لـ*Corpus Hermeticum* لا شخص تاريخي، فلا
  مؤلِّف يستوفي القاعدة 5 بحال، ولا سيرة تُكتب له. (الدفعة 4.4 عالجته على هذا الأساس.)

## ما لم يُفحَص

هذا الفحص غطّى `thk-` فقط، والاصطلاحات المتوازية نفسها قد تكون كرّرت في `wrk-` و`stu-`
و`ins-` و`tec-`. كما أنه يعتمد على وجود حقل `en:`، فأي ملف بلا `en:` لا يظهر فيه.

## الدرس

قِياسان متتاليان أخطأ كلٌّ منهما في اتجاه: الأول لأنني قِستُ على **الاصطلاح المفترَض** لا على
البيانات، والثاني لأنني قِستُ على **شجرة الملفات كلها** لا على ما يبنيه المشروع فعلاً.
والتصحيحان جاءا من وكيلَين أبلغا بما يخالف ما كتبتُه — فالبلاغ المخالف أنفع من التأكيد.
