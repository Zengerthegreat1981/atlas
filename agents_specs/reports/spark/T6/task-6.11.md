# Task 6.11 — كعبٌ محلول تُرك بلا لمس، وكتابان سابقان نُسب محتواهما لتطبيقهما اللاحق

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 مسحوبة، **29 معمَّقة + 1 كعب إحالة محلول**
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **1,384** | **3,722** |
| `## المصادر` | **0/29** | **29/29** (الكعب مستثنًى بحق) |

## أوّل حالة: كعبُ إحالة منجَز يُسحَب في دفعة تعميق

**`wrk-being-and-nothingness-sartre`** كان يحمل `redirect_to:
wrk-sartre-being-and-nothingness` — أي أنه **حالة منجَزة سلفاً**، لا مسودة تحتاج
تعميقاً. أُبلغ الوكيل بذلك قبل التنفيذ، وتحقّقتُ بعد ورود الدفعة أن الملف **لم
يُمَسّ إطلاقاً** (1,193 حرفاً، بلا تغيير). وهذا أوّل درس عملي في هذه الجلسة على
أن **draft ≠ الملف الذي سُحب** — أحياناً يكون الملف المسحوب نفسه إنجازاً سابقاً
يجب تركه كما هو، لا مادّة للعمل.

## نمط «الكتاب اللاحق يطبِّق مفاهيم الكتاب السابق» — مثالان جديدان

- **بيرن، ألعاب الناس (1964)**: حالات الأنا الثلاث (الوالد/الراشد/الطفل) ونظرية
  التبادلات **من كتابه السابق** *Transactional Analysis in Psychotherapy*
  (1961) — هذا الكتاب **يطبِّقها** على تصنيف «الألعاب»، لا يقدّمها لأوّل مرّة.
- **وينيكوت، اللعب والواقع (1971)**: **«الموضوع الانتقالي» من مقالته الأسبق
  (1953)** — هذا الكتاب يوسِّعه إلى «الفضاء الانتقالي» و«اللعب» أساساً للإبداع
  والثقافة عموماً.

وهذا يجعل النمط **ثمانياً على الأقلّ** عبر دفعات Task 6 (بينكر/سكينر/بيك سابقاً،
والآن بيرن ووينيكوت) — وهو النمط الأخطر والأكثر تكراراً في هذه المراجعة كلّها.

## أزواج ازدواج: أحدهما بكلا طرفيه في الدفعة نفسها، وثالثٌ مُهمَل من الموجز

- **ماركوس أوريليوس**: `wrk-meditations-marcus-aurelius` و
  `wrk-marcus-aurelius-meditations` **كلاهما مسحوبان في 6.11 نفسها** — عُمِّق
  كلٌّ باستقلالية، بصياغتَين مختلفتَين فعلاً كما طُلب.
- `wrk-being-time` (مقابل الأطول `wrk-being-and-time-heidegger`) و`wrk-fons-vitae`
  (مقابل `wrk-fons-vitae-ibn-gabirol`) — طرفا زوجَين مسجَّلين، عُومِلا كالمعتاد.
- ⚠️ **`wrk-spinoza-tractatus-theologico-politicus`** — طرفٌ في زوج **كان مسجَّلاً
  فعلاً في الجدول الأصلي الأوّل**، لكنّه **سقط من موجز 6.11** (خطأ في إعدادي أنا
  لا في عمل الوكيل). وجده الوكيل بنفسه (الطرف الآخر `wrk-theologico-political-
  treatise-spinoza` يحمل الازدواج مسجَّلاً فيه هو) وعمّق ملفّه كما ينبغي.

## تلفيقات وأخطاء حُذفت

- **العادات الذرية (كلير)**: رقما مبيعات متضاربان (15 مليون في ملفّ، 20 مليوناً
  في ملفّ مرتبط) — لم يُصالَح بينهما بتخمين رقم وسط، بل **حُذفا كلاهما** وسُجِّل
  التضارب في `gaps`.
- **ابنِ الحياة التي تريدها (بروكس)**: رقم «600,000 نسخة» وادّعاء استخدام من
  «مؤسّسة بيل وميلندا غيتس» — بلا سند، حُذفا.
- **وينيكوت**: ادّعاء تأثير على ريكور وليفيناس بلا مصدر أوّلي — حُذف من المتن
  ونُقل إلى `gaps`.

## خطأ في موجزي أنا، اكتشفه وكيلٌ ولم يُنفِّذه

نسبتُ في تعليماتي كتاب *Beiträge zur Sinneswahrnehmung* (1862) إلى **فخنر**.
والحقيقة — كما أثبتها `author_slug` في الملف نفسه — أنه **لِفونت**، لا فخنر.
**امتنع الوكيل عن تغيير المؤلِّف اتّكالاً على تعليماتي**، ورجع إلى بيانات
الملف الفعلية، وسجّل التعارض في `gaps` طالباً قراراً بدل الحسم بنفسه. هذا
بالضبط السلوك المطلوب من وكيلٍ حين يتعارض موجزٌ خارجي مع بيانات موثَّقة داخل
الملف نفسه.

## معلَّق للمحرِّر

- ثلاثة قرارات دمج (ماركوس أوريليوس، الوجود والزمان، ينبوع الحياة) بالإضافة
  لسبينوزا (الرسالة اللاهوتية السياسية).
- **تحقّق من مؤلِّف `wrk-beitrage-sinneswahrnehmung`**: فخنر أم فونت؟ الملف نفسه
  يقول فونت.

## الملفات

```
content/ar/works/wrk-a-thousand-plateaus-deleuze-guattari.md
content/ar/works/wrk-annihilation-of-caste.md
content/ar/works/wrk-atomic-habits.md
content/ar/works/wrk-attachment-loss-volume1.md
content/ar/works/wrk-barth-romerbrief.md
content/ar/works/wrk-beck-cognitive-therapy.md
content/ar/works/wrk-being-and-nothingness-sartre.md
content/ar/works/wrk-being-time.md
content/ar/works/wrk-beitrage-sinneswahrnehmung.md
content/ar/works/wrk-berne-games-people-play.md
content/ar/works/wrk-build-life-you-want.md
content/ar/works/wrk-deep-work.md
content/ar/works/wrk-factizitaet-geltung.md
content/ar/works/wrk-fons-vitae.md
content/ar/works/wrk-inquiry-into-human-mind-reid.md
content/ar/works/wrk-kitab-al-tawhid-maturidi.md
content/ar/works/wrk-marcus-aurelius-meditations.md
content/ar/works/wrk-meditations-marcus-aurelius.md
content/ar/works/wrk-monadology-leibniz.md
content/ar/works/wrk-origin-of-species-darwin.md
content/ar/works/wrk-presence-cuddy.md
content/ar/works/wrk-proslogion-anselm.md
content/ar/works/wrk-samkhya-karika-ishvarakrishna.md
content/ar/works/wrk-shobogenzo-dogen.md
content/ar/works/wrk-spinoza-tractatus-theologico-politicus.md
content/ar/works/wrk-tahdhib-al-akhlaq-miskawayh.md
content/ar/works/wrk-tawalii-al-anwar-baydawi.md
content/ar/works/wrk-what-we-owe.md
content/ar/works/wrk-winnicott-playing-reality.md
content/ar/works/wrk-word-and-object-quine.md
```
