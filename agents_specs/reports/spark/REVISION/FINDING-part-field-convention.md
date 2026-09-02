# Spark — حقل `part` يناقض `belongs_to` في 473 ملفاً

**التاريخ:** 2026-09-02 · **الحالة: ⛔ سؤال اصطلاح على مستوى المشروع كلّه — لم يُنفَّذ شيء**

## كيف ظهر

في كل دفعة من Task 4 أبلغ وكيل أو أكثر أن `part: "philosophy"` يبدو خطأً على مدخل إكلينيكي:
`thk-cwebster-stratton`، `thk-bbundy`، `thk-gschwartz`، `thk-evmunns`، `thk-carta`، `thk-jdifede`.
وكنتُ أعرضها عليك كإصلاحات صغيرة آمنة. **وهذا كان توصيفاً خاطئاً منّي.**

فحصتُ النطاق كاملاً فظهر أنها ليست حالات مفردة بل **نمط في 473 ملفاً**.

## القياس الحاسم: النِّسبة نفسها في المسارَين

| النطاق | الملفات | `part: philosophy` | ومنها `belongs_to` إكلينيكي | النسبة |
|---|---|---|---|---|
| **Spark** (a–l) | 1,293 | 673 | **283** | **21%** |
| **MiniMax** (m–z) | 1,007 | 528 | **190** | **18%** |

مسارَان مستقلّان تماماً، ونفس النسبة تقريباً. وهذا يعني أن الأمر **إمّا اصطلاح مقصود** (كل من
يُدرَس في تاريخ الأفكار يُقيَّد في مجلّد الفلسفة) **أو خطأ نَسَقيّ أقدم من المسارَين**. وفي
الحالتين ليس عطباً في Spark ولا قراراً لي.

و**`SPARK.md` لا يذكر حقل `part` إطلاقاً** — فلا مواصفة عندي أحكم بها.

## أكبر المجموعات

| `belongs_to` | العدد |
|---|---|
| `sch-existential-therapy` | 174 |
| `sch-psychoanalysis` | 157 |
| `sch-somatic-experiencing` | 15 |
| `sch-systemic-family` | 12 |
| `br-discernment-counseling` | 7 |
| `sch-phil-mind-analytic` | 6 |
| `sch-gestalt-therapy` | 6 |
| `sch-narrative-therapy` | 6 |
| `br-expressive-arts-therapy` | 5 |
| `sch-humanistic` | 5 |
| `sch-analytical-psychology` | 4 |
| `br-lacanian` | 4 |
| `br-recovery-oriented` | 4 |
| `tec-poetry-therapy` | 4 |

الـ174 تحت `sch-existential-therapy` **مشمولة أصلاً** بالقرار المنفصل في
`FINDING-existential-therapy-misclassification.md`. فيبقى نحو **299** خارجها.

## لماذا هذا مهمّ فعلاً

الـ157 تحت `sch-psychoanalysis` تضمّ أسماءً لا يُتصوَّر أنها في مجلّد الفلسفة:

- `thk-afreud` — **Anna Freud** (Spark)
- `thk-agreen` — **André Green** (Spark)
- `thk-aichhorn` — **August Aichhorn** (Spark)
- `thk-aulagnier` — **Piera Aulagnier** (Spark)
- `thk-bbettelheim` — **Bruno Bettelheim** (Spark)
- `thk-beebe` — **Beatrice Beebe** (Spark)
- `thk-bleuler` — **Eugen Bleuler** (Spark)
- `thk-bonaparte` — **Marie Bonaparte** (Spark)
- `thk-burlingham` — **Dorothy Burlingham** (Spark)
- `thk-jgreenberg` — **Jay R. Greenberg** (Spark)

**أنَّا فرويد** في مجلّد الفلسفة مثالٌ كافٍ: هي مؤسِّسة سيكولوجيا الأنا وتحليل الأطفال، ولا
قراءة معقولة تجعلها فيلسوفة. وبروينو بيتلهايم ويوجين بلويلر وماري بونابرت مثلها.

## اعتراف بعدم اتساق منّي

في الدفعة 4.4 صحّح وكيل `thk-jdifede` من `philosophy` إلى `psychology`، **وأنا commit-تُه**
(`a77c3759`). كان ذلك تغييراً لحالة واحدة من نمطٍ في 473 ملفاً قبل أن يُحسَم الاصطلاح.
ولم أعمّمه ولن أعمّمه قبل قرارك — لكنه قائم الآن، وأُبلغك به لا لأخفيه.

## المطلوب منك — سؤال واحد

**ما معنى `part` بالضبط؟**

1. **مجلّد النشر** (الفلسفة/علم النفس/الاجتماع) — فحينها الـ473 خطأ يحتاج تصحيحاً منهجياً،
   والأرجح أنه قابل للأتمتة من `belongs_to` مع مراجعة بشرية للحالات الحدّية (وهي حقيقية:
   بديو ولاكان وريكور يشتغلون على التحليل النفسي *فلسفياً*).
2. **الأصل المعرفي للمدخل** — فحينها كثير منها صحيح، والخطأ في توقّعي أنا، ولا عمل مطلوب.
3. شيء ثالث تقصده ولا أعرفه.

ولا أقترح تنفيذ أيٍّ منها الآن: النطاق يعبر المسارَين، فأي سويب منّي يمسّ أرض MiniMax.
