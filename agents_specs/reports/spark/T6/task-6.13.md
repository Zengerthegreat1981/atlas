# Task 6.13 — القاعدة الجديدة صمدت، وفجوة هُويّة حقيقية: دانيال ستيرن بلا ملفّ

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 (`works/`)
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **1,310** | **3,520** |
| `## المصادر` | **0/30** | **30/30** |

## القاعدة الجديدة صمدت: صفر أخطاء نسبة بعد ثلاث دفعات متتالية أخطأت

بعد 6.10 و6.11 و6.12 (ثلاثة أخطاء نسبة متتالية في موجزاتي)، أُضيفت قاعدة صريحة:
**تحقّق من `author_slug` قبل كتابة أي ملاحظة عن مؤلِّف**. النتيجة في هذه الدفعة:
**صفر أخطاء نسبة**، وأكثر من ذلك — **وكيلٌ أمسك فخّاً قبل وقوعه**: كتاب نيشيدا
كان يخلو من `author_slug`، وفي الأطلس ملفّان متشابها الاسم (`thk-nishida`
كيتارو نيشيدا الفيلسوف الصحيح، و`thk-hnishida` هيرويوكي نيشيدا محلِّل نفسي
مختلف تماماً) — تحقّق الوكيل ولم يخلط بينهما.

## ⛔ فجوة هُويّة حقيقية: مؤلِّف كتاب مركزي بلا ملفّ، والاسم القريب شخصٌ آخر

**`wrk-interpersonal-world-infant`** يحمل `author_slug: thk-daniel-stern` —
وهذا slug **لا وجود له في الأطلس**. والاسم القريب الوحيد، `thk-dstern`، هو
**دونَل ب. سترن (Donnel B. Stern)، محلِّل نفسي علائقي معاصر — شخصٌ آخر تماماً**
عن **دانيال ن. ستيرن (1934-2012)**، طبيب النمو النفسي ومؤلِّف هذا الكتاب
(1985) الفعليّ. **امتنع الوكيل عن الربط** تجنّباً لخطإ نسبة فادح، وسجّل
الفجوة صراحةً بدل حلّها من عنده. هذا يتطلّب **إمّا إنشاء ملفّ مفكِّر جديد
لدانيال ن. ستيرن الحقيقي، أو تصحيح `author_slug` إن كان الاسم الصحيح مختلفاً**.

## تلفيقات أخرى وُجدت وحُذفت

- **Behave (سابولسكي)**: المتن القديم كان يعرض «أربعة عشر مستوى» بترتيب
  عشوائي لا يعكس أطروحة الكتاب الفعلية — **أُعيد بناؤه بالكامل** وفق الإطار
  الزمني المعكوس الصحيح (ثانية → دقائق → أشهر → عقود → قرون) بوصفه الأطروحة
  المنهجية نفسها لا سرداً اعتباطياً.
- **مفهوم التهكم (كيركغور)**: مشرف أطروحة مختلَق — **راسموس نيلسن** — وعلاقته
  الموثَّقة بكيركغور **لا تبدأ إلا في أواخر الأربعينيات**، أي بعد الدفاع
  بسنوات، فهي مستحيلة زمنياً. حُذف بلا استبدال بدل اختراع اسم آخر.
- **سادانا (طاغور)**: ادّعاء تأثير على سوزان سونتاغ وآلان باديو — بلا سند، حُذف.

## ستّة ازدواجات عُومِلت بالمعتاد، وواحد ثبت أنه **ليس** ازدواجاً

`wrk-nietzsche-thus-spoke-zarathustra`، `wrk-aristotle-nicomachean-ethics`،
`wrk-concept-anxiety`، `wrk-guide-for-perplexed`، `wrk-second-sex`،
`wrk-gender-trouble-butler` — عُمِّقت باستقلالية، بلا دمج. **و
`wrk-either-or-kierkegaard` تأكَّد أنه ليس ازدواجاً** مع *خوف ورعدة* رغم قرب
السنة (1843) — عملان متمايزان فعلاً، عومل كملف عادي.

## معلَّق للمحرِّر

- **إنشاء/تصحيح ملفّ دانيال ن. ستيرن** — فجوة هُويّة حقيقية لا خطأ نسبة.
- ستّة قرارات دمج (انظر أعلاه)، بالإضافة إلى `wrk-medicinische-psychologie`
  (لوتسه) الذي لا ملفّ مفكِّر له إطلاقاً في الأطلس.

## الملفات

```
content/ar/works/wrk-al-shawahid-al-rububiyya-sadra.md
content/ar/works/wrk-an-inquiry-into-the-good-nishida.md
content/ar/works/wrk-aristotle-nicomachean-ethics.md
content/ar/works/wrk-behave-sapolsky.md
content/ar/works/wrk-braiding-sweetgrass.md
content/ar/works/wrk-categories-aristotle.md
content/ar/works/wrk-cognitive-therapy-personality.md
content/ar/works/wrk-communist-manifesto-marx-engels.md
content/ar/works/wrk-concept-anxiety.md
content/ar/works/wrk-de-docta-ignorantia-cusa.md
content/ar/works/wrk-dialectic-sex.md
content/ar/works/wrk-either-or-kierkegaard.md
content/ar/works/wrk-enchiridion-epictetus.md
content/ar/works/wrk-fi-al-falsafa-al-ula-kindi.md
content/ar/works/wrk-gender-trouble-butler.md
content/ar/works/wrk-guide-for-perplexed.md
content/ar/works/wrk-hayakil-al-nur-suhrawardi.md
content/ar/works/wrk-hayy-ibn-yaqzan-tufayl.md
content/ar/works/wrk-ihsa-al-ulum-farabi.md
content/ar/works/wrk-interpersonal-world-infant.md
content/ar/works/wrk-kierkegaard-concept-of-irony.md
content/ar/works/wrk-medicinische-psychologie.md
content/ar/works/wrk-mind-and-brain.md
content/ar/works/wrk-nietzsche-thus-spoke-zarathustra.md
content/ar/works/wrk-politics-aristotle.md
content/ar/works/wrk-sadhana-tagore.md
content/ar/works/wrk-second-sex.md
content/ar/works/wrk-spirit-of-the-laws-montesquieu.md
content/ar/works/wrk-tahafut-al-falasifa-ghazali.md
content/ar/works/wrk-the-world-as-will-and-representation-schopenhauer.md
```
