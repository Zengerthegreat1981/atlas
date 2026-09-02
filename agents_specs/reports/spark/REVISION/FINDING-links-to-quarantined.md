# Spark — روابط حيّة إلى مدخلات محجورة

**التاريخ:** 2026-09-02 · **الحالة: ⛔ يحتاج قراراً — لم يُزَل رابط واحد**

## المشكلة

`agents_specs/quarantine-spark.md` يسجّل **87 slug** لأشخاص لم يثبت وجودهم أو لم تُتَح لهم
مصادر مستقلّة. لكن الحجْر سجلٌّ لا فعل: **الروابط إليهم لا تزال قائمة في الأطلس المنشور.**

| | العدد |
|---|---|
| مدخلات محجورة لا تزال مُشاراً إليها من ملفات **معتمدة** | **53** |
| إجمالي الروابط الحيّة إليها | **86** |

أي أن الرسم البياني للأطلس **يُثبت علاقات فكرية بأشخاص قرّر المشروع نفسه أنه لا يستطيع توثيقهم**.
وأصرحها: `content/ar/thinkers/thk-sartre.md` يشير إلى `thk-delahorbe` — وقد تأكّد في الدفعة 4.5
أنه غير موثَّق أصلاً (لا منشور ولا دليل ولا مدخل في أي معجم تراجم).

> ولا يرى preflight شيئاً من هذا: الـid موجود وله ملف، والعنوان مطابق. فالفحص الآلي يتحقّق من
> **اتّساق الرابط** لا من **جدارة هدفه**.

## القسمة التي تحدّد القرار

### (أ) 27 رابطاً: الملف نفسه يقول إنه أزاله — ولم يُزَل

في هذه الحالات تحمل `gaps` في الملف الرابط سطراً يقول صراحةً إن الرابط **أُزيل** عند نقل مدخل
غير متحقَّق منه إلى المسودات. والرابط **لا يزال في `related` على القرص**.

| الملف الرابط | الرابط الذي يقول إنه أزاله |
|---|---|
| `thk-jcgibbs` | `thk-krischer` |
| `thk-dan-fisher` | `thk-kurtz-sherman` |
| `thk-dan-fisher` | `thk-gene-ennis` |
| `thk-dfeinstein` | `thk-cgarrett` |
| `thk-cborduin` | `thk-jgould` |
| `thk-gferri` | `thk-dpierrakos` |
| `thk-batkinson` | `thk-ecolle` |
| `thk-hliddle-clin` | `thk-brosen` |
| `thk-agoldstein` | `thk-krischer` |
| `thk-john-braithwaite` | `thk-jacqueline-peart` |
| `thk-john-braithwaite` | `thk-erikpearson` |
| `thk-hbeaumont` | `thk-jjoyce` |
| `thk-gweber` | `thk-jjoyce` |
| `thk-rcallahan` | `thk-cgarrett` |
| `thk-jpennebaker` | `thk-jbrowne` |
| `thk-emilecoue` | `thk-jose-salgado` |
| `thk-ereichelt` | `thk-cwhitaker-pt` |
| `thk-trore` | `thk-janicewilliams` |
| `thk-gmesibov` | `thk-cwhitaker-pt` |
| `thk-alemma` | `thk-gillian-abbott` |
| `thk-jbaylin` | `thk-apert` |
| `thk-crsnyder` | `thk-kevin-sparger` |
| `thk-crsnyder` | `thk-james-gumpert` |
| `thk-lorr` | `thk-connie-rae-anderson` |
| `thk-lorr` | `thk-jim-ackerman` |
| `thk-lorr` | `thk-katie-rae` |
| `thk-ovogt` | `thk-jose-salgado` |

**وهذه ليست قراراً جديداً**: القرار مُتّخذ ومُدوَّن، والناقص تنفيذه. وهي المرّة السادسة التي
يظهر فيها نمط **«مسجَّل ولم يُنفَّذ»** في هذه المراجعة — وأوضحها `thk-lorr` الذي تقول فجواته
إنه أزال ثلاثة روابط، وثلاثتها قائمة، **وهي روابطه الوحيدة**.

### (ب) 59 رابطاً: إزالتها قرار جديد

لا يوجد في الملف الرابط ما يقول إنه أزال شيئاً. ومنها **31** في `thinkers/` a–l (أرض
Spark) و**28** خارجها — في `schools/` و`branches/` و`concepts/` وملفات مفكّرين m–z،
**وهي أرض MiniMax**، فأي سويب منّي يعبر حدود المسار.

أمثلة من (ب):

- `content/ar/thinkers/thk-rdreikurs.md` → `thk-gweishaar`
- `content/ar/thinkers/thk-navarro.md` → `thk-dpierrakos`
- `content/ar/thinkers/thk-nkhanna.md` → `thk-fvanderzee`
- `content/ar/thinkers/thk-shamdasani.md` → `thk-jbissel`
- `content/ar/thinkers/thk-ngoldberg.md` → `thk-jbrowne`
- `content/ar/thinkers/thk-schultz-hencke.md` → `thk-hhuber`
- `content/ar/thinkers/thk-msimeona.md` → `thk-jramiro`
- `content/ar/thinkers/thk-novaco.md` → `thk-krischer`
- `content/ar/thinkers/thk-trudi-schoop.md` → `thk-daniellevision`
- `content/ar/thinkers/thk-ogilvie.md` → `thk-amy-morgan`
- `content/ar/thinkers/thk-ogilvie.md` → `thk-david-reeve`
- `content/ar/thinkers/thk-wwhite.md` → `thk-kurtz-sherman`

## المطلوب منك

**1.** الفئة (أ) — **27 رابطاً**: أُنفِّذ ما تقوله الملفات عن نفسها؟ أراه الأقرب
إلى الصواب لأنه لا يُنشئ قراراً بل يُتمّ قراراً مكتوباً. وسأدوّن في كل ملف أن الإزالة نُفِّذت
فعلاً هذه المرّة، بدل الاكتفاء بادّعائها.

**2.** الفئة (ب) الخاصة بـSpark — **31 رابطاً**: أُزيلها ويُدوَّن السبب في `gaps`؟
أو تُترك حتى يُحسَم مصير المحجورين أنفسهم (توثيق أم سحب)؟

**3.** الفئة (ب) خارج Spark — **28 رابطاً**: هذه ليست لي. تُحال إلى MiniMax أم
تُترك؟

## ملاحظة على المنهج

قِستُ هذا أول مرّة فخرج **70 مدخلاً و358 رابطاً** — وكان خطأً: كنتُ ألتقط كل slug مذكور في أي
مكان في ملف الحجْر، فدخلت في العدّ أسماءٌ **حقيقية** مذكورة في عمود *السبب* لا في عمود المحجور:
مارشا لينهان (97 رابطاً) وآرون بيك (70) وجون كابات-زين وبينسفانغر وكارل ويتاكر. الرقم الصحيح
جاء من قراءة **العمود الأول من الجدول** وحده.

وهو نفس درس التكرار: **اقرأ الحقل المقصود، لا ما يشبهه في النصّ.**
