# Task 6.12 — ثلاثة أخطاء نسبة في موجزي أنا، ثلاثتها اكتُشفت وصُحِّحت

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 (`works/`)
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **1,613** | **3,659** |
| `## المصادر` | **0/30** | **30/30** |

## ⛔ نمط جديد وخطير: ثلاثة أخطاء نسبة في موجزي، على التوالي

هذه الدفعة **الثالثة على التوالي** (بعد 6.11) التي يكتشف فيها وكيلٌ أنّ ملاحظتي
الخاصّة بشارده **تنسب الكتاب لمؤلِّف خاطئ** — واعتمدتُ في كتابتها على الذاكرة
لا على فحص الملف:

| الملف | نسبتُه أنا خطأً إلى | والصحيح | كيف اكتُشف |
|---|---|---|---|
| `wrk-object-relations-1983` | أوتو كيرنبرغ (1976) | **غرينبرغ وميتشل (1983)** | `author_slug` في الملف نفسه |
| `wrk-grundlagen-psychischen-entwicklung` | هاينز فيرنر | **كورت كوفكا** | ملف مفكِّر `thk-kkoffka.md` موجود بنفس العنوان الألماني |

وفي كلتا الحالتين **رفض الوكيل تطبيق ملاحظاتي**، ورجع إلى بيانات الملف الفعلية،
وكتب المحتوى الصحيح، وسجّل التعارض صراحةً بدل الامتثال الصامت. **هذا هو
السلوك الصحيح تماماً** — لكنّ تكرار الخطأ ثلاث مرّات متتالية معناه أن طريقة
كتابتي للموجزات (نسبة الكتب من الذاكرة) **غير موثوقة بما يكفي**، وقد أُضيفت
قاعدة صريحة: **فحص `author_slug` قبل كتابة أي ملاحظة عن مؤلِّف**.

## تلفيقات أخرى وُجدت وحُذفت

- **المجتمع العلاجي (جونز)**: قائمة أنيقة الشكل بعنوان **«المبادئ العشرة
  لجونز»** بلا أي إسناد — تعذّر التحقّق منها في الأدبيات فحُذفت، واستُبدلت
  بإطار **رابابورت الرباعي الموثَّق فعلاً** (الديمقراطية، التساهل، الجماعية،
  مواجهة الواقع، من *Community as Doctor*، 1960) مع تسمية رابابورت بوصفه
  صاحب هذا التصنيف التحليلي اللاحق لا جونز نفسه.
- **إريكسون (طفولة وجماعة)**: القبيلة «Sioux» تُرجمت خطأً إلى **«الساميون»**
  (خلط لفظي واضح بلا صلة بالسياق) — صُحِّحت إلى «سو (Sioux)».
- **لاكان (الكتابات)**: خطأ بنيويّ — حافة `authored_by` كانت تشير **إلى الكتاب
  نفسه** بدل `thk-lacan`. صُحِّحت.
- **أرقام مبيعات محذوفة**: أنا بخير أنت بخير، السايكوسبرنتيكس، التأثير،
  الإنسان يبحث عن المعنى — أربعة أرقام غير مسنَدة نُقلت من المتن إلى `gaps`.

## ازدواج مُحلَّل: `wrk-plato-republic` أخيراً يحمل حقوله

الملف الذي فلَتَ من كشّافين آليَّين متتاليَين (لأنه كان **بلا `author_slug`
ولا `publication_year` إطلاقاً**) عُبِّئت حقوله أخيراً هذه الدفعة، ممّا يُغلق
السبب الجذري لسقوطه من القياس الآلي مرّتين.

## أربعة أزواج ازدواج عُومِلت بالمعتاد

`wrk-plato-republic`، `wrk-kuzari`، `wrk-city-of-god`، `wrk-frankl-mans-
search-for-meaning` — كلّها عُمِّقت باستقلالية، بلا دمج ولا ربط، مع تسجيل
كلٍّ في `gaps`.

## معلَّق للمحرِّر

- إن كان هناك ملفّ عمل منفصل مخصَّص لكتاب هاينز فيرنر (Comparative Psychology
  of Mental Development) — لم يُعثَر عليه، فقد تكون **فجوة تغطية حقيقية**
  لا مجرّد خطإ إسناد.
- تناقض سنة الترجمة الإنجليزية الأولى لكتاب كوفكا (1924 مقابل 1928) بين
  ملفَّي العمل والمفكِّر.

## الملفات

```
content/ar/works/wrk-al-isharat-wa-al-tanbihat.md
content/ar/works/wrk-bowlby-separation.md
content/ar/works/wrk-city-of-god.md
content/ar/works/wrk-critique-of-practical-reason-kant.md
content/ar/works/wrk-daodejing-laozi.md
content/ar/works/wrk-ecrits.md
content/ar/works/wrk-emile-on-education-rousseau.md
content/ar/works/wrk-encyclopedia-philosophical-sciences-hegel.md
content/ar/works/wrk-erikson-childhood-society.md
content/ar/works/wrk-evolving-self.md
content/ar/works/wrk-fosha-transforming-power-affect.md
content/ar/works/wrk-four-hour-workweek.md
content/ar/works/wrk-frankl-mans-search-for-meaning.md
content/ar/works/wrk-grundlagen-psychischen-entwicklung.md
content/ar/works/wrk-guide-for-the-perplexed-maimonides.md
content/ar/works/wrk-holy-family-marx-engels.md
content/ar/works/wrk-im-ok-youre-ok.md
content/ar/works/wrk-influence-persuasion.md
content/ar/works/wrk-kuzari.md
content/ar/works/wrk-mindful-way-through-depression.md
content/ar/works/wrk-nudge.md
content/ar/works/wrk-object-relations-1983.md
content/ar/works/wrk-outline-psychology-titchener.md
content/ar/works/wrk-plato-republic.md
content/ar/works/wrk-psycho-cybernetics.md
content/ar/works/wrk-seligman-helplessness.md
content/ar/works/wrk-system-of-transcendental-idealism-schelling.md
content/ar/works/wrk-therapeutic-community.md
content/ar/works/wrk-twilight-of-the-idols-nietzsche.md
content/ar/works/wrk-vocabulaire-psychanalyse.md
```
