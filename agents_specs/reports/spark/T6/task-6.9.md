# Task 6.9 — الدفعة الأكثف ازدواجاً: ثمانية من ثلاثين طرفٌ في زوج مسجَّل

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 (`works/`)
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **1,246** | **3,531** |
| أقصر ملف | 570 | 2,827 |
| ملفات بصفر عناوين أقسام | 6 | 0 |
| `## المصادر` | **0/30** | **30/30** |

## ثمانية ازدواجات في دفعة واحدة — رقمٌ قياسيّ

`wrk-republic-plato`، `wrk-al-ghazali-munqidh`، `wrk-the-myth-of-sisyphus-camus`،
`wrk-in-a-different-voice-gilligan`، `wrk-kuzari-judah-halevi`،
`wrk-maslow-motivation-and-personality`، `wrk-kant-critique-pure-reason`،
`wrk-mans-search` — **ثمانية من ثلاثين ملفاً** كانت أطراف أزواج مسجَّلة سلفاً.
عُمِّق كلٌّ منها باستقلالية تامّة، وتحقّقتُ بعد ورود الدفعة أن **كل الثمانية**
تحمل فجوة تسجّل الازدواج (بصياغات مختلفة: «للعمل ملف ثانٍ»، «يوجد ملف ثانٍ»)
— لا واحد منها أُغفل هذه المرّة، بخلاف ما حدث في 6.8.

## أهمّ ما وُجد: تلفيق اسمٍ مختلَق لاكتشاف مخطوطة

**`wrk-corpus-hermeticum`**: الملف الموروث كان يسمّي **«جورجيو فاستي»** راهباً
اكتشف المخطوطة في دير مقدوني وأحضرها إلى فلورنسا 1463 — **اسمٌ لا يمكن التحقّق
منه، ويبدو مختلَقاً بالكامل**. حُذف الاسم وأُبقي ما هو موثَّق فعلاً: وصول المخطوط
إلى فلورنسا نحو 1460 عبر راهبٍ كان يجمع مخطوطات لكوزيمو دي ميديتشي، ثم ترجمة
**فيتشينو** 1463، ثم طباعة تريفيزو 1471. وصُحِّح أيضاً **الإطار الذي يوهم بمؤلِّف
تاريخي حقيقي** — «هرمس المثلث» نسبة تقليدية لا شخص تاريخي، وأُضيفت واقعة **كازوبون
1614** (إثباته الفيلولوجي أن النصوص متأخّرة بكثير عمّا ادّعاه دعاة الحكمة
الفرعونية) بوصفها استقبالاً جوهرياً لا هامشاً.

## تلفيقات وأخطاء أخرى

- **التواصل اللاعنفي (روزنبرغ)**: «5 ملايين نسخة في 35 لغة» — رقمٌ بلا مصدر
  مستقلّ يربطه بهذا العنوان تحديداً، حُذف ونُقل إلى `gaps`.
- **بولبي (الفقدان)**: فجوة كاذبة «لا ملفّ مفكّر لبولبي» — الملف موجود، أُصلح الرابط.
- **ماسلو**: تصحيح الخلط الشائع — **الهرم المثلَّث الرسومي لم يظهر في نصّ ماسلو
  نفسه**؛ وصفه نصّياً بلا رسم، والهرم تبسيطٌ بصريّ صنعه آخرون لاحقاً.

## ملاحظة عملية: توثيق أفضل هذه المرّة

بعد حادثة 6.8 (وكيل نسي وضع فجوة الازدواج في ملفّ فوكو)، تحقّقتُ من الثمانية
كلّها **قبل الالتزام لا بعده** — ولم يلزم أيّ إصلاح يدويّ هذه المرّة.

## معلَّق للمحرِّر

- ثمانية قرارات دمج (انظر أعلاه)، أسهلها ماسلو وغيليغان (فارق حجم كبير).
- **اكتشاف جانبي**: `wrk-nonviolent-communication` يشير عبر `author_slug` إلى
  `thk-marshall-rosenberg` — وملفّ هذا الأخير نفسه يُقرّ بأنه **الطرف الخاسر**
  في ازدواج مفكّرين لصالح `thk-msrosenberg`. لم يُمَسّ (خارج نطاق الدفعة)، لكنه
  تناقض حيّ يستحقّ تصحيحاً واحداً.

## الملفات

```
content/ar/works/wrk-5-second-rule.md
content/ar/works/wrk-al-ghazali-munqidh.md
content/ar/works/wrk-al-mashair-mulla-sadra.md
content/ar/works/wrk-al-milal-wa-al-nihal-shahrastani.md
content/ar/works/wrk-analects-confucius.md
content/ar/works/wrk-barnes-an-existentialist-ethics.md
content/ar/works/wrk-contexts-of-being.md
content/ar/works/wrk-corpus-hermeticum.md
content/ar/works/wrk-eger-the-choice.md
content/ar/works/wrk-general-psychopathology.md
content/ar/works/wrk-how-to-do-things-with-words-austin.md
content/ar/works/wrk-in-a-different-voice-gilligan.md
content/ar/works/wrk-jung-psychological-types.md
content/ar/works/wrk-kant-critique-pure-reason.md
content/ar/works/wrk-kashf-al-murad-hilli.md
content/ar/works/wrk-kuzari-judah-halevi.md
content/ar/works/wrk-linehan-dbt-skills-manual.md
content/ar/works/wrk-loss-sadness-depression.md
content/ar/works/wrk-mans-search.md
content/ar/works/wrk-maslow-motivation-and-personality.md
content/ar/works/wrk-nonviolent-communication.md
content/ar/works/wrk-on-liberty-mill.md
content/ar/works/wrk-passions-of-the-soul-descartes.md
content/ar/works/wrk-republic-plato.md
content/ar/works/wrk-science-of-knowledge-fichte.md
content/ar/works/wrk-science-of-logic-hegel.md
content/ar/works/wrk-slow-productivity.md
content/ar/works/wrk-status-anxiety.md
content/ar/works/wrk-the-myth-of-sisyphus-camus.md
content/ar/works/wrk-unwinding-anxiety.md
```
