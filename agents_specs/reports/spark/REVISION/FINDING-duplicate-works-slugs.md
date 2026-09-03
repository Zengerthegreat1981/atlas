# ازدواج في `works/`: انعكاس ترتيب الكلمات في الـslug

**التاريخ:** 2026-09-02 · **الحالة: ⛔ يحتاج قراراً — لم يُدمج شيء** · **26 مجموعة مفتوحة** (29 مؤكَّدة، 3 منها محلولة أصلاً)

## كيف ظهر

وكيل في الدفعة 6.2 أبلغ أن *نقد العقل الخالص* موجود في ملفَّين، ومثله *تأمّلات* ماركوس أوريليوس.
وكنتُ قد كتبتُ في تقرير ازدواج المفكّرين أن الفحص **غطّى `thk-` فقط** وأن الاصطلاحات نفسها قد
تكون كرّرت في `wrk-`. وقد كانت.

## السبب: نمط واحد نظيف

ليس هذا اصطلاحَين متوازيَين كما في المفكّرين، بل **انعكاس ترتيب**:

```
wrk-<العمل>-<المؤلِّف>   مقابل   wrk-<المؤلِّف>-<العمل>

wrk-critique-of-pure-reason-kant   ⇄   wrk-kant-critique-pure-reason
wrk-republic-plato                 ⇄   wrk-plato-republic
wrk-nicomachean-ethics             ⇄   wrk-aristotle-nicomachean-ethics
wrk-al-munqidh-min-al-dalal-ghazali ⇄  wrk-al-ghazali-munqidh
wrk-fasl-al-maqal-averroes         ⇄   wrk-ibn-rushd-fasl-al-maqal
```

## ولماذا هذه الحالات **أسهل** من ازدواج المفكّرين

في المفكّرين كان السؤال «هل هذا نفس الشخص؟» يحتاج حكماً بشرياً (ألفرد أدلر مقابل غيرهارد أدلر).
أمّا هنا فالتطابق **ميكانيكي ويقيني**: نفس العنوان، و**نفس `publication_year` في كل مجموعة
تقريباً** — 1781 لكانط، 1843 لكيركغور، 1966 لفوكو، 1108 للغزالي، 1179 لابن رشد، 180 لماركوس
أوريليوس، 1190 لابن ميمون. فلا مجال للشكّ في أنها أعمال واحدة.

## الجدول

| العمل | الملفات (سنة · حرف · روابط) |
|---|---|
| Being and Nothingness (L'Être et le Néant) b | `wrk-sartre-being-and-nothingness` (1943، 1684ح، 13ر) · `wrk-being-and-nothingness-sartre` (1943، 1193ح، 1ر) |
| Phenomenology of Perception - Merleau-Ponty | `wrk-phenomenology-perception-merleau-ponty` (؟، 2456ح، 7ر) · `wrk-phenomenology-of-perception-merleau-ponty` (؟، 662ح، 2ر) · `wrk-merleau-ponty-phenomenology-perception` (1945، 1413ح، 1ر) |
| Philosophy and the Mirror of Nature (1979) | `wrk-philosophy-mirror-nature` (؟، 1790ح، 6ر) · `wrk-rorty-philosophy-and-mirror-of-nature` (1979، 1791ح، 3ر) |
| Critique of Pure Reason (Kritik der reinen V | `wrk-critique-of-pure-reason-kant` (1781، 1150ح، 5ر) · `wrk-kant-critique-pure-reason` (1781، 1830ح، 4ر) |
| Self-Compassion: The Proven Power of Being K | `wrk-self-compassion-neff` (2011، 1431ح، 5ر) · `wrk-self-compassion` (؟، 1984ح، 2ر) |
| Republic Plato | `wrk-republic-plato` (-375، 766ح، 5ر) · `wrk-plato-republic` (؟، 1392ح، 2ر) |
| Thus Spoke Zarathustra Nietzsche | `wrk-thus-spoke-zarathustra-nietzsche` (1883، 692ح، 4ر) · `wrk-nietzsche-thus-spoke-zarathustra` (1883، 1485ح، 2ر) |
| Fear and Trembling by Søren Kierkegaard (Joh | `wrk-kierkegaard-fear-and-trembling` (1843، 1611ح، 4ر) · `wrk-fear-and-trembling-kierkegaard` (1843، 706ح، 3ر) |
| The Order of Things: An Archaeology of the H | `wrk-foucault-order-of-things` (1966، 1603ح، 3ر) · `wrk-the-order-of-things-foucault` (1966، 726ح، 1ر) |
| Deliverance from Error (Al-Munqidh min al-Da | `wrk-al-ghazali-munqidh` (1108، 1413ح، 3ر) · `wrk-al-munqidh-min-al-dalal-ghazali` (1108، 733ح، 1ر) |
| Nicomachean Ethics | `wrk-nicomachean-ethics` (-340، 1020ح، 3ر) · `wrk-aristotle-nicomachean-ethics` (-340، 1403ح، 2ر) |
| Obedience to Authority: An Experimental View | `wrk-obedience-to-authority` (1974، 1458ح، 3ر) · `wrk-milgram-obedience-authority` (1974، 3716ح، 1ر) |
| Studies on Hysteria by Josef Breuer and Sigm | `wrk-studies-hysteria-freud` (1895، 2673ح، 2ر) · `wrk-studien-hysterie` (؟، 2408ح، 1ر) |
| Das Ich und das Es | `wrk-ich-und-es` (1923، 3147ح، 2ر) · `wrk-ego-and-id-freud` (1923، 1999ح، 1ر) |
| Tractatus Theologico-Politicus by Baruch Spi | `wrk-spinoza-tractatus-theologico-politicus` (؟، 1384ح، 2ر) · `wrk-theologico-political-treatise-spinoza` (1670، 730ح، 1ر) |
| The Decisive Treatise (Fasl al-Maqal) by Ibn | `wrk-ibn-rushd-fasl-al-maqal` (1179، 1351ح، 2ر) · `wrk-fasl-al-maqal-averroes` (1179، 972ح، 1ر) |
| Meditations by Marcus Aurelius | `wrk-meditations-marcus-aurelius` (180، 1076ح، 2ر) · `wrk-marcus-aurelius-meditations` (180، 1413ح، 2ر) |
| Guide for the Perplexed (Maimonides, 1190) | `wrk-guide-for-perplexed` (1190، 2145ح، 2ر) · `wrk-guide-for-the-perplexed-maimonides` (1190، 1033ح، 1ر) |

## أبرز الحالات

- **مرلوبونتي، *فينومينولوجيا الإدراك*: ثلاثة ملفات** — `wrk-phenomenology-perception-merleau-ponty`
  (2,456 حرفاً، 7 روابط) و`wrk-phenomenology-of-perception-merleau-ponty` (662، رابطان)
  و`wrk-merleau-ponty-phenomenology-perception` (1,413، رابط). وصاحبه أيضاً مكرَّر في `thk-`.
- **سارتر، *الوجود والعدم*** — الفارق في الروابط حادّ: 13 مقابل 1، فالقرار هنا واضح.
- **ملغرام، *الطاعة للسلطة*** — والأطول (3,716 حرفاً) هو **الأقلّ ارتباطاً** (رابط واحد مقابل 3):
  نفس التعارض الذي عطّل 22 من مجموعات المفكّرين.
- **فرويد** له حالتان: *دراسات في الهستيريا* و*الأنا والهو* — وفي كلٍّ منهما أحد الملفَّين **مسودة**.

## المطلوب منك

**القرار نفسه المطلوب في تقرير المفكّرين، لكن التنفيذ أسهل:** يبقى واحد ويصير الآخر **إحالة**
(لا حذف — القاعدة 6)، ويُنقَل إليه المحتوى الموثَّق الزائد قبل الإحالة.

وأقترح قاعدة افتراضية: **يبقى الأكثر ارتباطاً**؛ فإن تعادلا (ماركوس أوريليوس 2 و2) يبقى الأطول.
والاستثناء الوحيد الذي يحتاج نظرك: **ملغرام**، حيث الأطول بفارق كبير هو الأقلّ ارتباطاً.

## ملاحظة على منهجي — الخطأ الخامس من نفس النوع

فحصي الأول لهذه المسألة أعطى **6 مجموعات و12 ملفاً**. والصحيح **18 و37**. السبب أنني طابقتُ
`en` **وجعلتُ `title` بديلاً احتياطياً فقط** (`norm(en) or norm(title)`) — فحين اختلف `en`
بزيادة «by Immanuel Kant» لم يُفحَص `title` أصلاً، **وهو متطابق حرفياً في الملفَّين**.
والصواب المطابقة على **أيٍّ من الحقلَين**.

وهذه **الخامسة** في هذه المراجعة من نفس النوع: قِستُ حقلاً واحداً أو تشابهاً لفظياً بدل ما يعنيه
السؤال فعلاً — بعد شكل الـslug بدل `en:` في المفكّرين (18→100→57)، وكل slug في ملف الحجْر بدل
عموده الأول (70→53)، والتطابق التامّ للعناوين بدل ما يرفضه preflight (1,119 «مخالفة» أغلبها
اختصارات مقبولة)، و«الصيغة القريبة» من القائمة السوداء (التي دفعت الوكلاء لحذف الفجوة الصحيحة).

## ⚠️ تصحيح: اثنتان من الثماني عشرة **محلولتان أصلاً**

أبلغ وكيل في الدفعة 6.3 أن `wrk-being-nothingness` يحمل في الـfrontmatter حقلاً لم أفحصه:

```
redirect_to: wrk-sartre-being-and-nothingness
```

أي أنه **كعب إحالة منجَز**، لا ازدواج مفتوح. فحصتُ الحقل في الأطلس كله: **13 ملفاً يحمله**
(4 `trm-` و4 `wrk-` و3 `sch-` وواحد `thk-` وواحد `que-`).

ومن مجموعاتي الثماني عشرة:

| | العدد |
|---|---|
| محلولة أصلاً بكعب `redirect_to` | **2** |
| **مفتوحة فعلاً** | **16** |

والمحلولتان: `wrk-being-and-nothingness-sartre` و`wrk-merleau-ponty-phenomenology-perception` —
**والثانية إحدى ملفات مرلوبونتي الثلاثة**، فتلك الحالة نصف محلولة لا كاملة.

### والفائدة العملية من الحالة المحلولة

الوكيل قارن نصفَي زوج سارتر بدقّة، فظهر أن الدمج **لا يُفقد إلا أربعة حقول وحدّاً واحداً** —
لكن ذلك الحدّ هو الأهمّ: **الملف الباقي (`wrk-sartre-being-and-nothingness`) لا يحمل حدّ
`written_by` إلى مؤلِّفه إطلاقاً**، ويربط سارتر عبر `related` فقط. فالكعب المُحال يحمل الحدّ
الصحيح والملف الباقي لا يحمله.

وهذا يعني أن **الإحالة وحدها لا تكفي**: الكعب قد يحمل بياناً بنيوياً يفتقده الباقي، فلا بدّ من
جرد الحقول قبل اعتبار الحالة مغلقة. وهو ما فعله الوكيل، وما ينبغي أن يُفعل في الستّة عشر الباقية.

### الدرس — للمرّة السابعة

لم أفحص حقل `redirect_to` قبل أن أعلن ثماني عشرة حالة مفتوحة. نفس النمط: **قياس بلا فحص ما هو
موجود أصلاً في البيانات.** والفحص كان سطراً واحداً.

## تصحيح ثانٍ للعدد: 18 → **26 مفتوحة** — وكيف ضُبِط

أبلغ وكيل في 6.3 عن زوج لكوهن لم يظهر في فحصي: `wrk-kuhn-structure-revolutions` و
`wrk-the-structure-of-scientific-revolutions-kuhn`. والسبب أن **اسم المؤلِّف مُلحَق في أحد
الشكلين، في `en` و`title` معاً** — فالمطابقة بالتساوي التامّ تفشل:

```
"The Structure of Scientific Revolutions"       → structurescientificrevolutions
"The Structure Of Scientific Revolutions Kuhn"  → structurescientificrevolutionskuhn
```

فأعدتُ الفحص **بالاحتواء** بدل التساوي: 32 مجموعة.

### لكن الاحتواء يُنتج إيجابيات كاذبة — وضُبِطت

| المجموعة الكاذبة | لماذا |
|---|---|
| `wrk-metaphysics-aristotle` / `wrk-physics-aristotle` | **«الطبيعة» جزء من «ما بعد الطبيعة» حرفياً** — وهما كتابان مختلفان لأرسطو |
| `wrk-metaphysics-of-morals-kant` (1797) / `wrk-groundwork-metaphysics-morals-kant` (1785) | *تأسيس ميتافيزيقا الأخلاق* غير *ميتافيزيقا الأخلاق* — **والسنتان تفضحانه** |
| `wrk-no-bad-parts` (2021) مع ملفَّي IFS (1995) | كتاب لاحق للمؤلِّف نفسه، لا نسخة أخرى |

**والمرشِّح هو `publication_year`**: الازدواج الحقيقي يحمل **نفس السنة** (كانط 1781، كيركغور
1843، فوكو 1966، الغزالي 1108، ابن رشد 1179، ماركوس أوريليوس 180، ابن ميمون 1190، ملغرام 1974،
فرانكل 1946، روجرز 1951، كريبكي 1980، سبينوزا 1677). واختلاف السنة يكشف عملَين مختلفَين.
وحالة أرسطو وحدها احتاجت رفضاً يدوياً لأن أحد ملفَّيها بلا سنة.

### الحصيلة المضبوطة

| | العدد |
|---|---|
| مجموعات بالاحتواء | 32 |
| مرفوضة (سنة مختلفة أو رفض يدوي) | 3 |
| **مؤكَّدة** | **29** |
| منها محلولة بكعب `redirect_to` | 3 |
| **مفتوحة فعلاً** | **26** |

### وممّا أضافه هذا التصحيح

مجموعات لم تكن في الثمانية عشر أصلاً، ومنها مهمّة:

- **Tractatus Logico-Philosophicus by Ludwig Wit** — `wrk-tractatus-logico-philosophicus-wittgenstein` (؟، 1073ح، 3ر) · `wrk-tractatus` (1921، 4800ح، 3ر)
- **Motivation and Personality by Abraham H. Mas** — `wrk-maslow-motivation-and-personality` (1954، 1628ح، 5ر) · `wrk-motivation-personality` (1954، 5272ح، 2ر)
- **Ethics, Demonstrated in Geometrical Order by** — `wrk-spinoza-ethics` (1677، 4725ح، 5ر) · `wrk-ethics-spinoza` (1677، 1112ح، 2ر)
- **Ideas Pertaining To Pure Phenomenology Husse** — `wrk-ideas-pertaining-to-pure-phenomenology-husserl` (1913، 806ح، 3ر) · `wrk-ideen-i` (1913، 4245ح، 2ر)
- **Naming And Necessity Kripke** — `wrk-naming-and-necessity-kripke` (1980، 771ح، 3ر) · `wrk-naming-necessity` (1980، 1935ح، 3ر)
- **Summa Theologiae by Thomas Aquinas** — `wrk-summa-theologiae-aquinas` (؟، 869ح، 7ر) · `wrk-summa-theologiae` (؟، 2195ح، 3ر)
- **Waking the Tiger: Healing Trauma** — `wrk-waking-the-tiger` (؟، 1268ح، 5ر) · `wrk-levine-waking-the-tiger` (1997، 1655ح، 3ر)
- **…trotzdem Ja zum Leben sagen · Man's Search ** — `wrk-mans-search` (1946، 1874ح، 3ر) · `wrk-frankl-mans-search-for-meaning` (1946، 1669ح، 3ر)
- **Client-Centered Therapy: Its Current Practic** — `wrk-rogers-client-centered-1951` (1951، 3902ح، 4ر) · `wrk-rogers-client-centered-therapy` (1951، 1617ح، 3ر)
- **An Inquiry Into The Good Nishida** — `wrk-an-inquiry-into-the-good-nishida` (؟، 644ح، 5ر) · `wrk-inquiry-into-good` (1911، 1765ح، 2ر)
- **Anarchy, State, and Utopia** — `wrk-anarchy-state-utopia` (1974، 2332ح، 3ر) · `wrk-anarchy-state-and-utopia-nozick` (1974، 731ح، 2ر)

## ⚠️ ونمط ظهر مرّتين: الملفّ الأقلّ ارتباطاً يحمل ما يفتقده الباقي

فحص وكيلان نصفَي زوجَين بالحقول، فظهر الشيء نفسه في كليهما:

- **سارتر**: الملف الباقي `wrk-sartre-being-and-nothingness` (13 رابطاً) **لا يحمل حدّ
  `written_by` إلى سارتر إطلاقاً**، ويربطه عبر `related` فقط — والكعب المُحال يحمل الحدّ الصحيح.
- **سبينوزا**: الملف الأقلّ ارتباطاً (رابط واحد) يحمل `author` و`author_slug` و`publication_year`
  و`original_language`، **وكلها غائبة عن الملف ذي الرابطَين**.

**فقاعدة «يبقى الأكثر ارتباطاً» غير كافية وحدها.** كل دمج يحتاج **جرد حقول** قبله، وإلا ضاع
بيان بنيوي موجود في الطرف المُحال. وهذا ما ينبغي أن يسبق أي تنفيذ للستّة والعشرين.

## ما لم يُفحَص بعد

`stu-` و`ins-` و`tec-` و`dis-` — نفس الانعكاس قد يكون كرّر فيها، ولم أفحصها.

---

## إضافة 2026-09-02 — المجموعة 27، وجدها وكيل في دفعة 6.4

| الملف | الطول | روابط واردة | `redirect_to` |
|---|---|---|---|
| `wrk-emdr-1995` | 4,930 | **4** | لا |
| `wrk-shapiro-emdr-principles` | 4,998 | 2 | لا |

الحقل `en:` **متطابق حرفياً** في الملفَّين:
*Eye Movement Desensitization and Reprocessing: Basic Principles, Protocols, and Procedures*
وكذلك `publication_year: 1995` و`author_slug: thk-francine-shapiro`. فهو **كتاب واحد في ملفَّين**،
وليس انعكاس `wrk-<عمل>-<مؤلف>` ⇄ `wrk-<مؤلف>-<عمل>` بل تسميتان مختلفتان تماماً — وهو **نمط
ثالث** يُضاف إلى النمطَين المعروفَين، ولا يلتقطه بحث الانعكاس.

⚠️ **كلا الملفَّين عُمِّق الآن**: `wrk-shapiro-emdr-principles` في هذه الدفعة (1,410 → 4,998)،
و`wrk-emdr-1995` كان معمَّقاً سلفاً. فالدمج صار **دمج محتوى حقيقي لا ترقية كعب**، وهو
أثقل من كل المجموعات السابقة.

وفي `wrk-emdr-1995` ثلاث مسائل مستقلّة عن الدمج:
- يسمّي طبعة **2018 «الطبعة الثانية»** وهي **الثالثة** (الثانية 2001).
- «أكثر من 100,000 ممارس معتمد في 90 دولة» — **رقم توزيع بلا سند**، من صنف §5.
- فجوة «لا يوجد اقتباس مباشر موثوق **من الكتاب نفسه** في هذه المسودة» — ليست جملة القائمة
  السوداء الحرفية، لكنها من صنفها.

## إضافة — المجموعة 28: نقد العقل الخالص (وجدها وكيل في 6.4)

`wrk-critique-of-pure-reason-kant` ⇄ `wrk-kant-critique-pure-reason` — **نمط الانعكاس المعروف**،
و`publication_year: 1781` في الاثنين. والوكيل **لم يربط أياً منهما** من ملف *التأسيس* الذي كان
يعمل عليه، تفادياً لترسيخ التكرار بربط ثالث — وهذا هو التصرّف الصحيح ويُعمَّم:
**لا تُضِف روابط واردة إلى طرفٍ في مجموعة ازدواج مفتوحة قبل حسمها.**

## إضافة — المجموعة 29: مدينة الله (وجدها وكيل في 6.4)

`wrk-city-of-god-augustine` ⇄ `wrk-city-of-god` — نفس العمل بعنوانين مختلفين.
وهذا **نمط رابع**: لا انعكاس، ولا تسميتان متباعدتان، بل **الاسم نفسه بلاحقة المؤلّف وبدونها**.

### حصيلة الأنماط الأربعة بعد 6.4
1. انعكاس `wrk-<عمل>-<مؤلف>` ⇄ `wrk-<مؤلف>-<عمل>` — الأكثر، ويلتقطه البحث الآلي.
2. لاحقة المؤلّف موجودة/غائبة (`wrk-city-of-god`) — يلتقطه بحث الاحتواء.
3. تسميتان لا تشترك فيهما كلمة (`wrk-emdr-1995` ⇄ `wrk-shapiro-emdr-principles`) — **لا يلتقطه
   إلا مطابقة حقل `en:` أو `publication_year`+`author_slug`**، وهو النمط الذي كنتُ أُغفله.
4. slug يسمّي **موضوعاً** والمحتوى كتاب (`wrk-listening-projective-identification` = «الانتباه
   والتأويل» لبيون) — **لا يلتقطه أيّ بحث آلي**، ولا يُكتشف إلا بقراءة الملف.

## إضافة — المجموعة 30 و31 (وجدهما وكيلان في 6.4)

- **30:** `wrk-plato-republic` ⇄ `wrk-republic-plato` — نمط الانعكاس، ووجده وكيلان مستقلّان.
- **31:** `wrk-naming-necessity` ⇄ `wrk-naming-and-necessity-kripke` — النمط الثاني (لاحقة المؤلّف).

⚠️ وفي `wrk-naming-necessity` **خطأان لا يقدر عليهما وكيل من خارج نطاقه**:
يعرض **«الأرض التوأم» بوصفها لكريبكي** — وهي **لبوتنام 1975** — ويجعل **الواقعية
الموداليّة عند ديفيد لويس** حصيلةً لـ*التسمية والضرورة*. فالملفّ المكرَّر ليس نسخة زائدة
فحسب، بل **يحمل تلفيقاً لا يحمله الطرف الآخر** — وهذه حجّة إضافية لأن الدمج ليس
اختياراً تجميلياً.

## إضافة — المجموعة 32: بعد الفضيلة (وجدها وكيل في 6.4)

`wrk-after-virtue` ⇄ `wrk-after-virtue-macintyre` — النمط الثاني (لاحقة المؤلّف)،
بنفس `author_slug` و`publication_year: 1981` و`belongs_to: sch-virtue-ethics`،
ومعرِّفَين مختلفين `WRK-0224` و`WRK-0504`. والثاني كعب من 727 حرفاً و`en:` مولَّد
آلياً من الـslug (`"After Virtue Macintyre"`).

⚠️ **والمعمَّق في هذه الدفعة هو `wrk-after-virtue` (5,995 حرفاً)** — فالكعب صار
**أصغر بثمانية أضعاف**، وهذه أسهل مجموعة في القائمة كلها: الاتّجاه لا لبس فيه.

---

# خلاصة الازدواج في `works/` بعد 6.4

**32 مجموعة مفتوحة.** والقياس تطوّر ستّ مرّات (6 → 18 → 26 → 27 → 29 → 32) لأن كل
نمطٍ جديد كان يحتاج بحثاً مختلفاً. والأنماط أربعة، ولا يلتقط البحث الآلي إلا الأوّلَين:

| النمط | مثال | كيف يُكتشف |
|---|---|---|
| 1. انعكاس `wrk-<عمل>-<مؤلف>` | `wrk-plato-republic` ⇄ `wrk-republic-plato` | بحث آلي |
| 2. لاحقة المؤلّف موجودة/غائبة | `wrk-after-virtue(-macintyre)` | بحث احتواء |
| 3. **تسميتان بلا كلمة مشتركة** | `wrk-emdr-1995` ⇄ `wrk-shapiro-emdr-principles` | **مطابقة `en:` فقط** |
| 4. **slug يسمّي موضوعاً والمحتوى كتاب** | `wrk-listening-projective-identification` = «الانتباه والتأويل» لبيون | **قراءة الملف فقط** |

**وقاعدة الدمج ليست «أبقِ الأكثر ارتباطاً»** — فالطرف الأقلّ ارتباطاً يحمل مراراً حقولاً
يفقدها الأكثر (`wrk-sartre-being-and-nothingness` بـ13 رابطاً **بلا حافة `written_by`**
إلى سارتر، وكعبُه يحملها). **كل دمج يحتاج جرداً حقلاً بحقل.** ويُضاف إليه أن الطرف المكرَّر
قد يحمل **تلفيقاً لا يحمله الآخر**: `wrk-naming-necessity` ينسب **«الأرض التوأم» إلى كريبكي**
وهي **لبوتنام 1975**.

## إضافة — المجموعة 33: الخلاصة اللاهوتية (وجدها وكيل في 6.5)

`wrk-summa-theologiae` (2,195 حرفاً، **11 رابطاً وارداً**) ⇄ `wrk-summa-theologiae-aquinas`
(869 حرفاً، **8 روابط واردة**) — النمط الثاني.

⚠️ **وهذه أثقل مجموعة في القائمة من جهة الروابط**: الطرف الأصغر ليس كعباً مهملاً بل
**يُشار إليه من ثمانية ملفات**. فالدمج يستلزم إعادة توجيه ثمانية روابط، لا حذف كعب.
وهذا يكسر الحدس القائل إن حجم الملف يدلّ على مركزيّته.

**وأثرٌ جانبيّ للازدواج المفتوح رصده الوكيل بنفسه:** لأنّ للعمل ملفَّين، **امتنع عن ربطه
أصلاً** من ملفٍّ ثالث وذكره نصّاً بلا رابط. أي أنّ الازدواج المفتوح **يُنقص الروابط
الصحيحة** ما دام مفتوحاً — وهذه كلفة مستمرّة لا ساكنة.

## ملحق: ازدواج في `thinkers/` ظهر من دفعات Task 6

هذه ليست من نطاق هذا التقرير (`works/`) وتُضاف إلى `duplicate-thinker-slugs-2026-09-02.md`:

| المجموعة | الملفّان | الأطوال |
|---|---|---|
| توما الأكويني | `thk-aquinas` ⇄ `thk-thomas-aquinas` | 2,491 / 4,731 |
| بول إيكمان | `thk-ekman` ⇄ `thk-paul-ekman` | 3,260 / 4,393 |
| أوروبيندو | `thk-aurobindo` ⇄ `thk-sri-aurobindo` | — |
| دانيال سيغل | `thk-dsiegel` ⇄ `thk-daniel-siegel` | **والثاني لا وجود له أصلاً** |

وثلاثتها الأولى في **أرض Spark** (`thk-a`, `thk-e`, `thk-d`) فهي قابلة للتنفيذ بإذنٍ واحد.

---

# القياس السابع، والكشّاف الصحيح — 36 مجموعة، 73 ملفاً

**التاريخ:** 2026-09-02 · بلاغُ وكيل في 6.5 عن **أربعة ملفات لعملَين** (البوليفاجال) لم يكن
أيٌّ منها في هذه القائمة، فأعدتُ بناء الكشّاف.

## ما كان خطأ في كشّافاتي السابقة

كنتُ أطابق **حقل `en:`** أو أبحث عن **انعكاس الـslug**. وكلاهما يفشل في الحالة الشائعة:
ملفّان لعملٍ واحد بحقلَي `en:` مختلفَين وبأسماء slug غير متعاكسة (`wrk-being-time` مقابل
`wrk-being-and-time-heidegger`).

**والكشّاف الصحيح: `author_slug` + `publication_year`.** فهما يُعرّفان العمل تعريفاً شبه
تامّ: مؤلِّفٌ واحد نشر عملاً واحداً في سنةٍ واحدة.

## ⚠️ لكنه كشّاف مرشَّحين لا كشّاف ازدواج

هذا التمييز هو بيت القصيد، وقد كدتُ أُغفله للمرّة التاسعة. الكشّاف يُخرج **46 دلواً**،
وفيها **مؤلِّفون نشروا عملَين مختلفَين في السنة نفسها**، أو أعمالاً تحمل **سنةً تقديرية
واحدة**:

| الدلو | ليس ازدواجاً لأنّ |
|---|---|
| روسو / 1762 | *العقد الاجتماعي* و*إميل* **صدرا في السنة نفسها فعلاً** |
| كيركغور / 1843 | *إمّا/أو* و*خوف ورعدة* **عملان مختلفان** في السنة نفسها |
| أرسطو / −340، −350، −335 | سنواتٌ **تقديرية** جُمعت تحتها أعمال متمايزة (الأخلاق، السماء، الشعر، الخطابة) |
| ابن سينا / 1027 | *الشفاء* و**النجاة** عملان — والنجاة مختصَرٌ عنه لكنها **كتاب مستقلّ** |
| الغزالي / 1095 · الرازي / 1210 · السهروردي / 1186 · ابن رشد / 1179 | أعمال متمايزة بسنةٍ واحدة |
| أفلاطون / −399 | *الدفاع* و*أقريطون* عملان |

فبعد تصفية الدلاء بشرط **تطابق العنوان أيضاً**، ثمّ استبعاد ثلاث حالات نجت من التصفية
بسبب اسم المؤلّف داخل الـslug: **38 زوجاً مؤكَّداً** تنتظم في **36 مجموعة** (35 مجموعة من
ملفَّين، وواحدة من ثلاثة هي سارتر) تشمل **73 ملفاً**. و**14 من المجموعات جديدة** لم تكن
في أيّ قياس سابق.

## الأزواج الأربعة عشر الجديدة

| العمل | الأطول (مرشَّح البقاء) | الأقصر |
|---|---|---|
| الجنس الآخر — بوفوار 1949 | `wrk-second-sex` (2,337) | `wrk-the-second-sex-beauvoir` (732) |
| قلق الجنوسة — بتلر 1990 | `wrk-gender-trouble` (4,813) | `wrk-gender-trouble-butler` (710) |
| أسطورة سيزيف — كامو 1942 | `wrk-myth-sisyphus` (1,819) | `wrk-the-myth-of-sisyphus-camus` (912) |
| النظرية المتعدّدة المبهمة في العلاج — دانا 2018 | `wrk-polyvagal-theory-therapy` (5,998) | `wrk-dana-polyvagal-therapy` (1,487) |
| تأمّلات في الفلسفة الأولى — ديكارت 1641 | `wrk-descartes-meditations` (1,513) | `wrk-meditations-on-first-philosophy-descartes` (730) |
| الجنون والحضارة — فوكو 1961 | `wrk-foucault-madness-civilization` (3,727) | `wrk-madness-and-civilization-foucault` (742) |
| بصوت مختلف — غيليغان 1982 | `wrk-different-voice` (1,840) | `wrk-in-a-different-voice-gilligan` (750) |
| هان فيتزي — نحو 240 ق.م | `wrk-hanfeizi` (2,784) | `wrk-han-feizi-text` (705) |
| الوجود والزمان — هايدغر 1927 | `wrk-being-and-time-heidegger` (4,829) | `wrk-being-time` (2,015) |
| ينبوع الحياة — ابن جبيرول 1050 | `wrk-fons-vitae` (2,290) | `wrk-fons-vitae-ibn-gabirol` (745) |
| الخزري — يهودا هليفي 1140 | `wrk-kuzari` (2,200) | `wrk-kuzari-judah-halevi` (730) |
| مفهوم القلق — كيركغور 1844 | `wrk-concept-anxiety` (1,893) | `wrk-concept-of-anxiety-kierkegaard` (687) |
| نظرية في العدالة — رولز 1971 | `wrk-theory-of-justice` (4,248) | `wrk-a-theory-of-justice-rawls` (914) |
| أنظمة الأسرة الداخلية — شوارتز 1995 | `wrk-internal-family-systems-1995` (5,154) | `wrk-schwartz-internal-family-systems` (1,603) |
## سارتر: ثلاثة ملفات لعمل واحد

`wrk-being-nothingness` (2,279، **كعب إحالة**) · `wrk-sartre-being-and-nothingness` (1,684) ·
`wrk-being-and-nothingness-sartre` (1,193، **كعب إحالة**). أي **كعبا إحالة وملفٌّ حقيقي** —
والملفّ الحقيقي هو الأوسط، وهو **الذي لا يحمل حافة `written_by` إلى سارتر** بينما يحملها
كعبُه. وهذه أوضح شاهد على أن **حجم الملف وعدد روابطه لا يدلّان على أيّهما الأصحّ حقلاً بحقل**.

## الخلاصة المحدَّثة

| | |
|---|---|
| مجموعات مؤكَّدة | **36** (73 ملفاً) |
| منها ما فيه كعب إحالة (`redirect_to`) محسوم جزئياً | 4 |
| أزواج طرفاها **معمَّقان** فالدمج دمجُ محتوى | `wrk-emdr-1995`/`wrk-shapiro-emdr-principles` · `wrk-tractatus`/`…-wittgenstein` |
| أسهل الأزواج (فارق ثمانية أضعاف أو أكثر) | بتلر · رولز · هايدغر · فوكو 1961 · دانا · ابن جبيرول · هليفي · ماكنتاير |

**والقاعدة تبقى:** لا يُدمَج زوجٌ قبل **جردٍ حقلاً بحقل** — فالطرف الأقصر يحمل مراراً
حقولاً يفقدها الأطول، وقد يحمل تلفيقاً لا يحمله الآخر.

## إضافة — المجموعة 37: الذات المتعاطفة (وجدها وكيل في 6.6)

`wrk-self-compassion` ⇄ `wrk-self-compassion-neff` — نفس العنوان الإنجليزي حرفياً
(*Self-Compassion: The Proven Power of Being Kind to Yourself*)، نفس المؤلّفة (نِف)،
نفس السنة (2011). النمط الثاني (لاحقة المؤلّف). **لم يلتقطه كشّاف `author_slug`+`publication_year`
في الجولة السابقة** — يستحقّ فحصاً لماذا (على الأرجح أحد الملفَّين بلا `author_slug` مُعبَّأ).

## إضافة — المجموعة 38: فينومينولوجيا الإدراك (وجدها وكيل في 6.7)

`wrk-phenomenology-of-perception-merleau-ponty` ⇄ `wrk-phenomenology-perception-merleau-ponty`
— الفرق بينهما كلمة **"of"** واحدة فقط في الـslug الإنجليزي. نفس الكتاب، صياغة مختلفة.
النمط الثاني (تنويع طفيف في الـslug لا لاحقة مؤلّف). الطرف المعمَّق في 6.7 هو `...-of-...`
(4,692 حرفاً).
