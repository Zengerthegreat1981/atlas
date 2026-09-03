# Task 6.7 — ثلاثة ازدواجات استُقرّت، وأربع ترجمات عربية موثَّقة، وهُويّة كتاب مغلوطة كلّياً

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 (`works/`)
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **1,216** | **3,739** |
| أقصر ملف | 619 | 2,636 |
| ملفات بصفر عناوين أقسام | 3 | 0 |
| `## المصادر` | **0/30** | **30/30** |

## ثلاثة ازدواجات استُقرّ اتّجاهها بالتعميق

- **رولز**: `wrk-a-theory-of-justice-rawls` عُمِّق (3,491) — الطرف الآخر `wrk-theory-of-justice`
  (4,248) يبقى الأطول والمرشَّح الطبيعي.
- **نِف**: `wrk-self-compassion-neff` عُمِّق **بأمانة كاملة** (4,699) رغم معرفة الوكيل أنه
  سيبقى الطرف الأضعف أمام `wrk-self-compassion` (المعمَّق في 6.6) — وهذا التزامٌ بقاعدة
  «لا تختصر عمداً لأن ملفّك سيُحذف على الأرجح».
- **فوكو**: `wrk-foucault-madness-civilization` عُمِّق إلى **5,706 حرفاً**، فصار المرشَّح
  الواضح للبقاء أمام `wrk-madness-and-civilization-foucault` (742 حرفاً فقط).

## ازدواج رابع، غير مسجَّل، وجده وكيل

**المجموعة 38**: `wrk-phenomenology-of-perception-merleau-ponty` ⇄
`wrk-phenomenology-perception-merleau-ponty` — الفرق بينهما كلمة **"of"** واحدة في
الـslug الإنجليزي. تفصيله في `../REVISION/FINDING-duplicate-works-slugs.md`.

## ⛔ ملفّ يصف كتاباً غير كتابه الحقيقي كلّياً

**`wrk-wertz-five-ways-phenomenological-analysis`**: الملف الموروث بأكمله كان يصف
**خمس مدارس فينومينولوجية فرعية**. تحقّق الوكيل وقارن بملف الأطلس نفسه لمؤلِّفه
(`thk-wertz`)، فتبيّن أن الكتاب الحقيقي (Wertz, *Five Ways of Doing Qualitative
Analysis*، Guilford 2011) يقارن **خمس مناهج نوعية**، **واحد منها فقط فينومينولوجي**
(فيرتز نفسه)؛ الأربعة الباقية نظرية مؤسَّسة (شارماز)، تحليل خطاب (ماك مولين)، بحث
سردي (جوسلسون)، استقصاء حدسي (أندرسون). **صُحِّح المتن، وتُرك `title`/`slug`/`en`
كما هما** — تغييرهما خارج تفويض الوكيل وقد يكسر روابط واردة. يحتاج قرار تسمية.

## أربع ترجمات عربية مثبَتة بثلاثيّها (الفرع الأول) — أكبر حصيلة دفعة حتى الآن

| العمل | المترجم | الناشر | السنة |
|---|---|---|---|
| غولمان، الذكاء العاطفي | ليلى الجبالي | المجلس الوطني للثقافة والفنون والآداب (عالم المعرفة #262) | 2000 |
| ووكر، لماذا ننام | الحارث النبهان | دار التنوير | 2019 |
| ليمبكه، أمة الدوبامين | علياء العمري (مترجمة) | دار مدارك (ناشر) | **غير محسومة** — تعذّر التوفيق بين مصادر متضاربة (أحدها زعم 2019، مستحيل منطقياً لأن الأصل 2021) |

**الحالة الثالثة (ليمبكه) توضيحٌ مهمّ للفرعين 1 و4**: الوكيل ثبّت المترجم والناشر
بثقة لكنه **رفض إثبات سنة غير موثوقة**، فسجّل الاثنين في `gaps` فقط بدل كتابتهما
في المتن أو `## المصادر` بصفتهما ترجمة معتمدة كاملة. هذه حالة وسيطة صحيحة بين
«ثابتة بثلاثيّها» و«غير موجودة» لم يكن للموجز صيغة معتمدة لها من قبل.

## تلفيقات وأخطاء أخرى وُجدت وحُذفت

- **فرويد (سيكوباتولوجيا)**: مثال زلّة لسان («Milch» بدل «wollt») تعذّر التحقّق من
  انتمائه لهذا الكتاب — حُذف واستُبدل بالمثالين الموثَّقين فعلاً (نسيان اسم سينوريلي،
  ونسيان اقتباس «Aliquis»)؛ وسلاسل تأثير مختلقة («Nisbett & Wilson 1977»، «Levelt
  1989») حُذفت؛ وفجوة كاذبة «لا ملفّ لفرويد» — الملف موجود.
- **باندورا... لا، بيكون (Novum Organum)**: لم يكن للملف مؤلِّف ولا سياق تاريخي
  إطلاقاً قبل هذه الدفعة — بُني من الصفر.
- **غولمان**: `related` كان يحمل `thk-jacqueline-astington` بلا أي صلة موثَّقة بالكتاب
  ولا سبب في المتن — حُذف بدل اختلاق سبب له.
- **بوبر**: `active_end: "مستمر"` على ملفٍّ بلا `publication_year` أصلاً — صُحِّح إلى 1945.

## واقعة نشر جوهرية أُثبتت لأوّل مرّة

**فوكو، الجنون والحضارة**: الترجمة الإنجليزية 1965 **حذفت نحو ثلثي النصّ الفرنسي
الأصلي (1961)** — فقارئ الإنجليزية يقرأ نسخة مبتورة لا الكتاب كاملاً. أُضيفت الترجمة
الكاملة اللاحقة (2006، مورفي وخلفة) مصدراً.

## ما نجح لأنه امتنع

- **هيغل وبوبر**: صلتهما بعلم النفس أُقرّت **نحيفة عمداً** (فلسفة سياسية/قانونية)
  بدل اختلاق صلة.
- **جنيالوجيا الأخلاق**: العود الأبدي والسوبرمان **نُفيا صراحةً** عن هذا الملف
  (ينتميان لزرادشت، ملف آخر في الدفعة نفسها).
- **النجاة لابن سينا**: عومل عملاً مستقلّاً عن الشفاء (كما ثبت سابقاً)، لا ازدواجاً.

## معلَّق للمحرِّر

- تسمية `wrk-wertz-five-ways-phenomenological-analysis` (تصحيح العنوان أم نقل الـslug؟).
- المجموعة 38 (ميرلوبونتي) والازدواجات الثلاثة المستقرّة اتّجاهها.
- سنة ترجمة أمة الدوبامين (علياء العمري / دار مدارك) — المترجم والناشر ثابتان، السنة
  متنازَع عليها.
- تدقيق ناشر تحقيق النجاة: «دار الآفاق الجديدة» أم «دار الآفاق الحديثة»؟

## الملفات

```
content/ar/works/wrk-a-theory-of-justice-rawls.md
content/ar/works/wrk-al-kashf-an-manahij-al-adilla.md
content/ar/works/wrk-al-najat-avicenna.md
content/ar/works/wrk-aron-opium-of-intellectuals.md
content/ar/works/wrk-de-trinitate-augustine.md
content/ar/works/wrk-democracy-and-education-dewey.md
content/ar/works/wrk-dopamine-nation.md
content/ar/works/wrk-elements-philosophy-of-right-hegel.md
content/ar/works/wrk-emotional-intelligence.md
content/ar/works/wrk-foucault-madness-civilization.md
content/ar/works/wrk-huanglao-texts.md
content/ar/works/wrk-loves-executioner.md
content/ar/works/wrk-neuroscience-psychotherapy.md
content/ar/works/wrk-noise-kahneman.md
content/ar/works/wrk-novum-organum-bacon.md
content/ar/works/wrk-on-the-genealogy-of-morals-nietzsche.md
content/ar/works/wrk-ordinatio-duns-scotus.md
content/ar/works/wrk-phenomenology-of-perception-merleau-ponty.md
content/ar/works/wrk-popper-open-society.md
content/ar/works/wrk-pragmatism-william-james.md
content/ar/works/wrk-psychopathologie-alltagslebens.md
content/ar/works/wrk-realm-hungry-ghosts.md
content/ar/works/wrk-self-compassion-neff.md
content/ar/works/wrk-system-of-nature-holbach.md
content/ar/works/wrk-the-prince-machiavelli.md
content/ar/works/wrk-thus-spoke-zarathustra-nietzsche.md
content/ar/works/wrk-tipping-point.md
content/ar/works/wrk-two-dogmas.md
content/ar/works/wrk-wertz-five-ways-phenomenological-analysis.md
content/ar/works/wrk-why-we-sleep.md
```
