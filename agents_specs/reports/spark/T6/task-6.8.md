# Task 6.8 — المتن الكلاسيكي (صيني، يوناني، إسلامي، سنسكريتي)، وثلاثة ازدواجات ذاتية التسوية

**الحالة: مكتمل** · **التاريخ:** 2026-09-03 · **الملفات:** 30 (`works/`)
**النتيجة الآلية:** صفر مخالفات · 22 تعارض slug (ثابت) · صفر حذف · لا ملف فوق السقف · صفر `"مستمر"`

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | **978** | **3,810** |
| أقصر ملف | 617 | 2,789 |
| `## المصادر` | **0/30** | **30/30** |

## ثلاثة ازدواجات: كِلا طرفَيها في الدفعة نفسها

نمط جديد لم يحدث من قبل — بدل أن يعالَج طرفٌ واحد من الزوج ويبقى الآخر بحاله، **سُحب
الطرفان معاً** في نفس السحب العشوائي وعُمِّقا باستقلالية عن بعضهما، بلا تنسيق بين وكيلَيهما:

| الزوج | الطرف الأول | الطرف الثاني | ملاحظة |
|---|---|---|---|
| هان فاي تسي | `wrk-hanfeizi` (5,415) | `wrk-han-feizi-text` (3,767) | الاتجاه واضح |
| مرآة الطبيعة | `wrk-rorty-...` (3,740) | `wrk-philosophy-mirror-nature` (**4,967**) | ⚠️ **الاتجاه انعكس** عمّا كان قبل الدفعة |
| خوف ورعدة | `wrk-kierkegaard-fear-and-trembling` (2,455) | `wrk-fear-and-trembling-kierkegaard` (3,713) | **تقرير مستقلّ ثالث** لنفس الزوج، يؤكّده |

⚠️ **زوج «مرآة الطبيعة» يحتاج نظرة متجدّدة**: قبل هذه الدفعة كان `wrk-philosophy-mirror-
nature` (1,790) أقصر من `wrk-rorty-...` (1,791) بحرفٍ واحد فقط، فتعميق مستقلّ لكليهما
قلب الترتيب — الملف الذي كان يُفترض أنه «الكعب» صار الآن الأطول.

## تصحيح لملفّي — أُغفل الازدواج، فأُصلح بعد ورود الدفعة

**`wrk-the-order-of-things-foucault`** طرفٌ في ازدواج مسجَّل مقابل `wrk-foucault-order-
of-things`، ولم يُبلَّغ الوكيل المكلَّف به بهذا (خطأ في موجزي أنا، لا في عمل الوكيل).
أُضيفت فجوة التسجيل يدوياً بعد ورود الدفعة، قبل الالتزام.

## نمط متكرّر: ثلاثة وكلاء لم يجدوا ملفّ الازدواج رغم وجوده

**للمرّة الثالثة** في هذه الجلسة (بعد 6.7 مرّتين) أبلغ وكيلٌ أنه «لم يجد»
`REVISION/FINDING-duplicate-works-slugs.md` رغم أنه موجود فعلاً (36+ ك.ب.). **لا ضرر
وقع** — الوكلاء امتنعوا عن الدمج بحكم تعليمات الموجز المباشرة بصرف النظر عن الملف —
لكنها ظاهرة بحث تستحقّ تسجيلاً.

## تلفيقات وأخطاء أخرى وُجدت وحُذفت

- **فيخنر**: فجوة كاذبة «لا ملفّ لفخنر» — الملف موجود.
- **رورتي**: نقدٌ منسوب إلى «Dennett 1998» تعذّر التحقّق منه — حُذف واستُبدل بنقّاد
  موثَّقين فعلاً (بوتنام، هابرماس، بيرنشتاين، وماكداول الذي أقرّ صراحة بتأثّره).
- **أفلوطين**: `publication_year: 270` كان **سنة الوفاة** لا نشرٍ — نُقل إلى `null`
  مع مدى التأليف والتحرير الفعلي (253–301م تقريباً).
- **إبكتيتوس**: كاد يُنسَب إليه ترجمة عربية هي في الحقيقة لـ*المختصر* (Enchiridion)،
  عمل آخر أقصر لآريان نفسه — اكتُشف الفرق وسُجِّل صراحةً قبل الخطأ لا بعده.
- **لويز هاي**: رقم «50 مليون نسخة» نُقل من متن ملفّ العمل إلى `gaps` بدل إثباته —
  **فأنشأ تناقضاً ثالثاً عابراً للمسارَين** مع `thk-louise-hay` (أرض MiniMax)، حيث
  الرقم نفسه ما زال في المتن. سُلِّم لهم.

## ترجمات عربية موثَّقة جديدة (الفرع الأول)

| العمل | المترجم | الناشر | السنة |
|---|---|---|---|
| كيركغور، خوف ورعدة | فؤاد كامل | دار الثقافة للنشر والتوزيع | 1983 |
| كويلو، الخيميائي | بهاء طاهر | دار الهلال | — |
| أفلوطين، التاسوعات | فريد جبر | مكتبة لبنان ناشرون | 1997 |

**والحالة الثالثة (أفلوطين) دقيقة**: مُيِّزت صراحةً عن قناة نقل منفصلة تماماً —
«أثولوجيا أرسطو» المنحولة (نقلها ابن ناعمة الحمصي، نقّحها الكندي، حقّقها بدوي في
*أفلوطين عند العرب*) — وهي ليست ترجمة للتاسوعات نفسها.

## ما نجح لأنه امتنع

- **ابن باجة**: تعذّر تثبيت طبعة نقدية موثوقة، فأُبقي قسم المصادر سطراً واحداً بدل
  اختلاق محقِّق. وسنة 1130 (موروثة) أُبقيت مع تسجيل الشكّ في `gaps` بدل استبدالها
  بتخمين آخر.
- **عبد الجبار**: نصّ توثيقي جوهري أُضيف — النصّ كما وصلنا **تقرير تلميذه مانكديم
  لمجالسه لا تأليفه المباشر** — يوازي حالة باسكال (نصّ لم يكتبه صاحبه بيده).
- **بينكر وليبنتز**: قُرنا بحذرٍ صريح («وجها نزاع ممتدّ لا اتصال تاريخي مباشر»)
  عبر ثلاثة قرون على مسألة الفطرية/الصفحة البيضاء، بلا ادّعاء اتصال وهميّ.

## معلَّق للمحرِّر

- زوج «مرآة الطبيعة» بعد انعكاس الطول.
- ثلاثية «خوف ورعدة» (تأكيد ثالث مستقلّ).
- التناقض الثالث لرقم توزيع عابر للمسارَين (لويز هاي).
- تدقيق ناشر تحقيق شرح الأصول الخمسة وسنة نشره.

## الملفات

```
content/ar/works/wrk-alchemist.md
content/ar/works/wrk-anti-duhring-engels.md
content/ar/works/wrk-anti-oedipus-deleuze-guattari.md
content/ar/works/wrk-blank-slate.md
content/ar/works/wrk-cinderella-complex.md
content/ar/works/wrk-concluding-unscientific-postscript-kierkegaard.md
content/ar/works/wrk-discourses-epictetus.md
content/ar/works/wrk-elemente-psychophysik.md
content/ar/works/wrk-emotional-blackmail.md
content/ar/works/wrk-enneads-plotinus.md
content/ar/works/wrk-fear-and-trembling-kierkegaard.md
content/ar/works/wrk-formation-of-arab-reason-jabri.md
content/ar/works/wrk-han-feizi-text.md
content/ar/works/wrk-hanfeizi.md
content/ar/works/wrk-letters-concerning-english-nation-voltaire.md
content/ar/works/wrk-manzuma-hikma-sabzawari.md
content/ar/works/wrk-morena-who-shall-survive.md
content/ar/works/wrk-myth-of-normal.md
content/ar/works/wrk-new-essays-on-human-understanding-leibniz.md
content/ar/works/wrk-outlines-of-pyrrhonism-sextus.md
content/ar/works/wrk-philosophy-mirror-nature.md
content/ar/works/wrk-road-less-traveled.md
content/ar/works/wrk-rorty-philosophy-and-mirror-of-nature.md
content/ar/works/wrk-scarcity-mullainathan.md
content/ar/works/wrk-sharh-usul-al-khamsa-abd-al-jabbar.md
content/ar/works/wrk-tadbir-al-mutawahhid-bajja.md
content/ar/works/wrk-the-order-of-things-foucault.md
content/ar/works/wrk-time-and-free-will-bergson.md
content/ar/works/wrk-vimsatika-vijnaptimatrata-vasubandhu.md
content/ar/works/wrk-you-can-heal-your-life.md
```
