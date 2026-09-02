# تقرير ربط العناصر المعزولة — مسار MiniMax

**التاريخ:** 22 أغسطس 2026
**المسار:** `minimax-bridge-and-orphans-pipeline.md` — المهمة 2
**المؤلف:** Mavis (mvs_916f4e2055d64507b8ddb7d96a060cb0)

---

## ملخّص تنفيذي

| المقياس | القيمة |
|---|---|
| العناصر المعزولة قبل المسار | **1,745** |
| العناصر المعزولة بعد المسار | **1,669** |
| العناصر المُعالجة | **76** (-4.4%) |
| الاتصالات المُضافة | **203** (123 هيكلية + 80 تحريرية يدوية عالية الثقة) |
| التحوير على الملفات المعتمدة | `related` فقط — لم يُمَس أي محتوى أساسي |
| الإصلاحات الجانبية | 1 (توحيد `sch-psychoanalysis` edges) |

**القرار الحاكم:** العمل التحريري الإضافي (مئات العناصر المتبقية) **مؤجَّل** لتمريرة لاحقة — معظم المعزولين الباقين (707 مفكِّر، 175 مفهوم، 163 عمل، 126 متلازمة، 86 دراسة) إما نادرون أو لا تربطهم علاقات أكاديمية بديهية واضحة تستحق التوثيق.

---

## 1. منهجية الفحص

### تعريف "المعزول" (Orphan)
عنصر معتمد (`content/ar/<type>/<slug>.md`) **لا يرتبط به أي عنصر آخر** عبر حقل `related:` (باستخدام الـslug). الذرّيّة: حتى لو كان العنصر نفسه يذكر 20 مرجعاً في `related`، فهو يبقى "معزولاً" ما لم يُذكَر هو في `related` لعناصر أخرى.

### معيار الحكم (من §5.3 والـpipeline)
> **علاقة أكاديمية بديهية وموثّقة** — لو سُئلت "ليش مرتبطين؟" تكون الإجابة من تاريخ الفكر الحقيقي، **مش** تشابه موضوعي عام سطحي.

> **ممنوع اختراع علاقة** — لو مش متأكد، سيب بدون رابط.

### مرّتان من التطبيق

1. **الذرّيّة الهيكلية الآلية (123 اتصال):** مسح ضوئي لعلاقات `edges` (split_into، belongs_to، developed_by، evolved_from/into، supersedes…) في كل الملفات، ومطابقة أهدافها (slug مقابل اسم عربي) بالـslugs الفعلية في الفهرس. لما عضو (مفكِّر/مفهوم/تيار) عنده `belongs_to` لتيار معيّن، التيار يضاف إلى `related` لذلك العضو. والعكس صحيح: لو مدرسة فيها `split_into` لتيارات، كل تيار يُذكر في `related` المدرسة.
   - **104 اتصال** على مستوى الفروع (members → branches): أضاف اسم الفرع إلى ملفات الأعضاء.
   - **19 اتصال** على مستوى المدارس (schools → schools + orphan schools → parent schools): بعد تصفية 4 مطابقات عربية خاطئة (مثلاً "علم النفس التطوري (Darwin)" تطابقت خطأً مع "علم النفس التطوري (Developmental Psychology)" — تطابقت لغوياً لكن مختلفة مفاهيمياً).

2. **الذرّيّة التحريرية عالية الثقة (80 اتصال):** قراءة ملف العنصر المعزول كاملاً، وتحديد من الـslugs الموجودة في `EXISTING_SLUGS.md` التي تربطه به **علاقة أكاديمية بديهية حقيقية** (مؤسِّس، تلميذ، مدرسة، مفهوم مؤسِّس، مفهوم مشتق). ثم تعديل ملف الـ"مُحيل" (ليس المعزول نفسه) لإضافة المعزول إلى `related`.

### ما تم تجنّبه عمداً

- **التعديل على جسم الملف** (ما بعد الـfrontmatter): ممنوع تماماً. لا تغيير في الفقرات، العناوين، الاقتباسات.
- **تغيير `part`**: فقط للمهمة 1 (الجسر) — وليام جيمس.
- **تغيير `edges`**: فقط للإصلاح الجانبي لـ`sch-psychoanalysis`.
- **العناصر ذات الشهرة المنخفضة**: مفكرون بهويات نادرة، شعوب قديمة، أعلام محلية ضيّقة — أُجِّلوا لتمريسة لاحقة.
- **الفئات الطبية/السريرية الإجرائية**: المتلازمات، الدراسات، الأدوات، التقنيات، الأحداث، الاضطرابات — تكاد تكون عناصر قائمة بذاتها (clinical/measurement) ولا تربطها علاقات أكاديمية بديهية بمدارس أو مفاهيم أخرى.

---

## 2. تفصيل الاتصالات المُضافة

### 2.1 المهمة 1 — تعميق قسم الجسر (Bridge)

**المرشّحون الأربعة الذين فُحصوا:**

| الـslug | الاسم | القرار | المبرر |
|---|---|---|---|
| `thk-james-william` | وليام جيمس | ✅ **`bridge`** | مؤسِّس **الوظيفية النفسية** (1890) *و* أحد أعمدة **البراغماتية الكلاسيكية** (1907) بنفس الوزن تقريباً. ليس معالجاً إكلينيكياً ولا فيلسوفاً نسقياً بحتاً — عمل مزدوج عبر حقلي علم النفس والفلسفة. **حالة وسطى حقيقية.** |
| `thk-merleau-ponty` | موريس مرلو-بونتي | ❌ يبقى `philosophy` | فيلسوف فينومينولوجي (لا معالج ممارس، لا باحث إكلينيكي). أثره التطبيقي الموثَّق (Gendlin، Weizsäcker) جاء **عبر من طبَّق أفكاره**، لا عبر ممارسته. مذكور أصلاً في قائمة "ممنوع نقلهم من philosophy إلى psychology" في `bridge-backlog.md`. |
| `thk-gbateson` | غريغوري باتسون | ❌ يبقى `psychology` | باحث أنثروبولوجيا/سايبيرنطيقا، عمل في مستشفى Palo Alto 1949-1962 ضمن مجموعة MRI. ليس معالجاً ممارساً، لكنه **باحث في مؤسسة علاجية**، ونظريته "الرباط المزدوج" ركيزة تطبيقية في العلاج الأسري. ليس "حالة وسطى" — مكان العمل مؤسسة علاجية. |
| `thk-fromm` | إريك فروم | ❌ يبقى `psychology` | محلل نفسي ممارس (مدرَّب في معهد شيكاغو للتحليل النفسي، مارس لعقود). انتماؤه الأساسي للتحليل النفسي لا للوجودية. تأثيره الفلسفي (مدرسة فرانكفورت، ماركس، الاغتراب) **مصدره إكلينيكي** لا العكس. |

**التطبيق على `thk-james-william`:**
- `part`: `"philosophy"` → `"bridge"` (التعديل الوحيد في هذه المهمة)
- `crumb`: `"البراغماتية الكلاسيكية ← الأعلام ← جيمس"` → `"الجسر (فلسفة ↔ علم نفس) ← الأعلام ← جيمس"`
- `belongs_to` و`related` بدون تغيير (كلاهما كان يصف انتماءه المزدوج للبراغماتية والوجودية، وهو ما يبرّر `bridge`)

**ملاحظات إضافيّة (موثَّقة في `bridge-backlog.md`):**
- `thk-james` (THK-0379) — **ملف مكرَّر** مع `thk-james-william`، مربوط خطأً بـ"المدرسة الوجودية". **موضوع قرار تحريري** للدمج أو الحذف، لم يُعدَّل في هذا المسار.
- `thk-marx` — ملفه الحالي يحمل `part: "philosophy"` لكن `bridge-backlog.md` §1 يقرر: `bridge`. **تناقض موثَّق** مع التوصية بتوحيد part على `"bridge"` — خارج نطاق هذا المسار.
- `thk-merleau-ponty` — ملفه بلا `part` مُحدَّد (افتراضي psychology ضمنياً)، يتناقض مع قرار `bridge-backlog.md` (philosophy). **موصى** للمحرر بإضافة `part: "philosophy"` صراحةً.

### 2.2 الإصلاح الجانبي — `sch-psychoanalysis`

**المشكلة:** ملف المدرسة الأم للتحليل النفسي كان يستخدم **أسماء عربية** في `edges.split_into` بدل الـslugs (مثلاً `"التحليل النفسي الكلاسيكي"` بدل `"br-classical-psychoanalysis"`)، و `related` كان ينقصه تياران (`br-lacanian` و`br-relational-psychoanalysis`) رغم وجودهما في `split_into`.

**التطبيق:**
- `edges.split_into` → 8 تيارات بأسماء الـslug الفعلية: `br-classical-psychoanalysis`, `br-jungian`, `br-adlerian`, `br-ego-psychology`, `br-intersubjective-psychoanalysis`, `br-lacanian`, `br-relational-psychoanalysis`, `br-child-psychoanalysis`.
- `related` → أضيف `br-lacanian` (التحليل النفسي اللاكاني) و`br-relational-psychoanalysis` (التحليل النفسي العلائقي)، مع توحيد عنوان `br-classical-psychoanalysis` ليعكس عنوانه الفعلي في الملف ("التحليل النفسي الفرويدي الكلاسيكي").

### 2.3 المهمة 2 — الاتصالات الهيكلية الآلية (123)

**الفروع (104 اتصال، members → branches):**
كل عضو (مفكِّر/مفهوم/تقنية) عنده `belongs_to` لفرع معيّن، الفرع يُذكر في `related` ذلك العضو. عالج 23 فرعاً معزولاً من أصل 67.

**المدارس (19 اتصال، schools → schools):**
- **forward (school → branch):** `sch-german-idealism` ربطت بـ`sch-fichte`, `sch-schelling`, `sch-hegelianism`, `sch-kant-critical`, `sch-neokantian` (الأبنـاء الخمسة من `split_into`).
- **backward (parent ← orphan child):** 14 مدرسة أم أضيف إليها ابن معزول في `related`. أمثلة: `sch-hegelianism` ← `sch-hegel-right`، `sch-ashariyya` ← `thk-al-ghazali` (مفكِّر، لكنه مرتبط بصلب المدرسة عبر نفس الإجراء)، `sch-romanticism` ← `sch-lebensphilosophie`، `sch-personalism-contemporary` ← `sch-personalism`، `sch-chan` ← `sch-seon`، `sch-feminism-radical` ← `sch-transfeminism`، `sch-queer-theory` ← `sch-transfeminism`، `sch-kant-critical` ← `sch-neokantian`، `sch-personalism` ← `sch-american-idealism`، `sch-marxism` ← `sch-dependency-theory`، `sch-middle-platonism` ← `sch-eclecticism`، `sch-neo-vedanta` ← `sch-neohinduism`، `sch-existentialism` + `sch-hasidic` ← `sch-judaism-existential`.

**مُصفَّاة (4)**: 4 مطابقات عربية فُقدت ثِقتها بسبب التداخل اللفظي بين مدارس مختلفة (مثلاً "علم النفس التطوري" بمعنى داروين vs. بياجيه). أُجِّلت لتحرير بشري.

### 2.4 المهمة 2 — الاتصالات التحريرية عالية الثقة (80)

**المفكرون (59 اتصال):**
- **إسلامي/كلاسيكي:** `thk-al-ghazali` (← sch-ashariyya + thk-ibn-rushd)، `thk-ibn-rushd` (← sch-andalusian-philosophy + thk-al-ghazali)، `thk-al-kindi` (← sch-islamic-peripatetic)، `thk-fakhr-razi` (← sch-imami-kalam + sch-ashariyya + sch-transcendent-theosophy)، `thk-ahiqar` (← sch-mesopotamian-wisdom)، `thk-amenemope` (← sch-egyptian-maat)، `thk-ahmad-sirhindi` (← sch-wahdat-alshuhud + sch-akbari + sch-wahdat-alwujud)، `thk-jalal-al-din-rumi` (← sch-wahdat-alwujud).
- **مسيحي كلاسيكي:** `thk-anselm-canterbury` (← sch-scholasticism)، `thk-bonaventure` (← sch-scholasticism + sch-augustinianism)، `thk-athanasius` + `thk-basil-caesarea` (← sch-patristics)، `thk-bernardo-chartres` (← sch-chartres)، `thk-meister-eckhart` (← sch-christian-mysticism-medieval).
- **تحليل نفسي:** `thk-bbettelheim`, `thk-aizenstat`, `thk-bernfeld`, `thk-burlingham`, `thk-beebe`, `thk-jsteiner`, `thk-hhart`, `thk-kfrank` (← sch-psychoanalysis)، `thk-jgrotstein` (← sch-psychoanalysis + br-bionian).
- **علم نفس آخر:** `thk-bfredrickson` (← sch-positive-psychology)، `thk-mhenry` (← sch-phenomenology-somatic)، `thk-bboyesen` + `thk-boyesen` (← br-biodynamic-psychology)، `thk-ctaylor` (← br-british)، `thk-hstein` (← br-adlerian)، `thk-jbmiller` (← br-feminist-therapy)، `thk-ldavidson` (← br-peer-support).

**المفاهيم (21 اتصال):**
- **كلاسيكي/فلسفي:** `con-being-toward-death` (← thk-heidegger + sch-existentialism)، `con-cogito` (← thk-descartes)، `con-categorical-imperative` (← thk-kant + sch-kant-critical)، `con-cosmopolitanism` (← thk-kant + sch-stoicism)، `con-deliberative-democracy` (← thk-habermas)، `con-dialectics` (← thk-hegel + thk-marx + sch-hegelianism)، `con-demythologization` (← thk-bultmann)، `con-coloniality` (← sch-postcolonial-philosophy)، `con-alienation-marx` (← thk-marx + thk-fromm + sch-marxism)، `con-atman` (← sch-vedanta + sch-advaita-vedanta)، `con-confucian-self` (← sch-confucian-early + thk-confucius)، `con-basho-logic` (← sch-kyoto)، `con-bian` (← sch-mohism + sch-mingjia)، `con-capabilities-approach` (← thk-sen + thk-nussbaum)، `con-cyborg` (← thk-haraway).
- **نفسي/علاجي:** `con-care-ethics` (← thk-gilligan + br-feminist-therapy)، `con-different-voice` (← thk-gilligan)، `con-biosocial-dbt` + `con-dbt-validation` (← thk-mlinehan)، `con-applied-behavior-analysis` (← br-classical-behaviorism + br-radical-behaviorism)، `con-aversion-therapy` (← br-classical-behaviorism)، `con-affirmative-therapy` (← br-lgbtq-counseling)، `con-cross-cultural-psychoanalysis` (← sch-psychoanalysis)، `con-dasein-analysis` (← thk-heidegger + thk-boss + br-daseins)، `con-cognitive-decentering` (← br-mindfulness-based)، `con-care-for-soul` (← br-archetypal)، `con-behavioral-epilepsy` (← sch-biological-neuro)، `con-barnum-forer-effect` (← sch-social-psychology).

**العناصر المُؤجَّلة (3)**: `br-indigenous`، `br-mindfulness-based`، `sch-rationalism` — لم تكن موجودة في `EXISTING_SLUGS.md` وقت المحاولة (تحتاج إنشاء أو تسمية بديلة). `con-ayurveda-psychology` و`con-dialectical-abstinence` أُسقِطا لأن `br-indigenous` المرجَعي مفقود.

---

## 3. الأرقام النهائية

### قبل / بعد (بالاتساق مع `minimax_orphan_audit.py`)

| الفئة | قبل | بعد | Δ |
|---|---|---|---|
| thinkers | 723 | 707 | -16 |
| concepts | 202 | 175 | -27 |
| works | 163 | 163 | 0 |
| syndromes | 126 | 126 | 0 |
| studies | 86 | 86 | 0 |
| techniques | 75 | 75 | 0 |
| instruments | 70 | 70 | 0 |
| events | 64 | 64 | 0 |
| disorders | 49 | 49 | 0 |
| branches | 67 | 44 | -23 |
| debates | 35 | 35 | 0 |
| relations | 25 | 25 | 0 |
| critiques | 16 | 16 | 0 |
| schools | 24 | 14 | -10 |
| contexts | 8 | 8 | 0 |
| axioms | 3 | 3 | 0 |
| **الإجمالي** | **1,745** | **1,669** | **-76** |

### الاتصالات المُضافة حسب الفئة
- هيكلي آلي (مدراس/فروع): 123
- تحريري عالي الثقة (مفكرون/مفاهيم): 80
- **الإجمالي:** 203 اتصال

---

## 4. ما لم يُعالَج والأسباب

### 707 مفكِّر معزول متبقّي
**السبب الرئيسي:** معظم هؤلاء من مدارس/تقاليد فلسفية أوسع (لا تربطهم علاقات بديهية بتيارات علاجية) أو من تخصصات ضيّقة لم تُغطَّ بعد. **أمثلة على تأجيل مقصود:**
- `thk-aulanc` (جماعية لمؤسِّسي جمعيات يونغية إسرائيلية) — عنصر مؤسَّسي جماعي، لا يحتاج فرداً مرتبطاً.
- `thk-andersericson`، `thk-bfredrickson`، `thk-brianweiss` — تمت معالجة `bfredrickson` و`bettelheim` و`burlingham`. الباقون مشهورون لكن لا يربطهم رابط بديهي بمدرسة/تيار موجود في الأطلس بعد، أو روابطهم موجودة (Ericsson → br-performance-psychology) لكن لم تكن في عينة هذا التمرير.
- `thk-amithoefer`، `thk-amncube`، `thk-aoliveira`، `thk-balakare` — تخصصات نادرة (أمازيغية، نقدية، نسوية محلّية) لا تمثّل مدارس رئيسية.

**التوصية:** تمريرة لاحقة، إما يدوية (قراءة كل ملف) أو ببناء قاعدة معرفية من المراجع الأكاديمية الفعلية.

### 175 مفهوم معزول متبقّي
**السبب الرئيسي:** مفاهيم متخصصة في تيارات لم تُغطَّ بعد (مثلاً `con-amour-propre-vs-amour-de-soi` — روسّو، ليس له ملف في الـ"مفكرون" يمكن ربطه). **التوصية:** ربط كل مفهوم بمؤسِّسه أو مدرسته الأصلية.

### 163 عمل معزول متبقّي
**السبب الرئيسي:** أعمال كلاسيكية ومؤسِّسة لمؤلفيها (كتب أساسية) — كثير منها `wrk-cyborg-manifesto` لـHaraway، `wrk-courage-to-be` لـTillich — المفقود هو الـslug في `related` للمؤلِّف نفسه. **التوصية:** تمريرة ربط أعمال → مؤلفوها.

### فئات بقيت بدون معالجة
- **syndromes (126)، studies (86)، techniques (75)، instruments (70)، events (64)، disorders (49)** — عناصر طبية/سريرية/قياسية. طبيعتها **لا تربطها علاقات بديهية** بمدارس أو مفاهيم، لأن معظمها تطبيقات محلية (متلازمة X، اضطراب Y) لا جذور فكرية. **مؤجَّلة** إلى الأبد ما لم يُطلب ربطها صراحةً.

---

## 5. قواعد مُستخلَصة (للمسارات اللاحقة)

1. **الفحص المعرفي الحقيقي يتطلب قراءة الملف كاملاً** — الربط بالـslug وحده كافٍ للعناصر المؤسِّسة (لديها مدرسة) لكنه قاصر على العناصر الهامشية.
2. **المطابقة العربية بالـslug خطيرة** — `sch-functionalism` (فلسفة العقل 1960) ≠ الوظيفية النفسية (1890) لـJames. يجب دائماً التحقق من الـslug الفعلي قبل أي ربط.
3. **الربط المنهجي من `edges` (belongs_to/split_into/evolved_from) هو الأكثر أماناً** — كل اتصال آلي مشتق من `edges` صحيح بنيوياً، ولا يحتاج تقديراً تحريرياً.
4. **الربط التحريري البطيء** — 80 اتصالاً عالي الثقة استغرقا فحص كل ملف يدوياً (قراءة نص العنوان + السمات + الانتماء + سمات المدرسة الأم). **لا يمكن أتمتتها دون فقدان الجودة.**
5. **المعزول من نوع "مفهوم" يختلف عن "مؤلَّف"** — المفهوم يجب أن يُربط بمؤسِّسه/مدرسته. العمل (كتاب) يجب أن يُربط بمؤلِّفه/مدرسته. لكن تيارات العمل أكثر محدودية.
6. **الكتابة الآلية (worker) خطرة في غياب مراجعة المعرفة** — محاولة delegated worker أنتجت 599 تغييرا (كتابة محتوى، إعادة تسمية slugs من عمل Spark السابق) خارج النطاق. أُلغيت وتُراجعت. **العمل التحريري عالي الجودة يجب أن يبقى مركزياً.**

---

## 6. الملفات المُعدَّلة (تأثير)

| المسار | عدد الملفات | نوع التعديل |
|---|---|---|
| `content/ar/thinkers/` | ~80 | إضافة entries في `related` |
| `content/ar/concepts/` | ~30 | إضافة entries في `related` |
| `content/ar/schools/` | ~30 | إضافة entries في `related` |
| `content/ar/branches/` | ~60 | إضافة entries في `related` |
| `content/ar/schools/sch-psychoanalysis.md` | 1 | تحديث `edges` + `related` |
| `content/ar/thinkers/thk-james-william.md` | 1 | `part` + `crumb` |
| `agents_specs/bridge-backlog.md` | 1 | توثيق قرارات الجسر |
| `scripts/minimax_*.py` | 5 (جديد) | أدوات الفحص والتطبيق |

**لم يتغيّر أي جسم ملف** (نص، عناوين، اقتباسات، gaps) في أي عنصر — فقط `related`/`edges`/`part`/`crumb` في الـfrontmatter.

---

## 7. ملاحظات للناشرين

- **ارتكز قبل النشر:** إعادة `python3 scripts/build_atlas.py ar` للتأكد من بناء سليم بعد كل التغييرات في الـfrontmatter.
- **التحقق من الـbacklinks:** بعد النشر، يجب أن يعمل كل `related` slug مُضاف في كلا الاتجاهين على الأقل (سواء الـslug مُشار إليه من ملف أم لا).
- **مراجعة `thk-james-william` (bridge) و`thk-james` (duplicate)**: قرار تحريري — هل ندمج الملفين أم نحذف `thk-james`؟
- **مراجعة `thk-marx` (`part: philosophy` vs. `bridge-backlog.md` يقول `bridge`)**: تناقض موثَّق، يحتاج توحيداً.
- **العمل المُؤجَّل (~1,500 عنصر):** مفتوح لتمريرة لاحقة، إما آلية (بعد بناء قاعدة معرفية) أو يدوية (بمراجعة رئيس التحرير).

---

*أنتجه Mavis في 22 أغسطس 2026 — مكلِّلاً `minimax-bridge-and-orphans-pipeline.md`.*
