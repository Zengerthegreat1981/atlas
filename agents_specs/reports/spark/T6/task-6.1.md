# Task 6.1 — أول دفعة تُصرَف لهذه المهمة إطلاقاً

**الحالة: مكتمل** · **التاريخ:** 2026-09-02 · **الملفات:** 30 (`works/` معتمد) · **commit:** `17b734a7`
**النتيجة الآلية:** صفر مخالفات preflight · 22 تعارض slug · صفر حذف · لا ملف فوق السقف

## لماذا فُتحت Task 6 الآن

Task 4 مُثبتة وتسير (ستّ دفعات)، وبقي لها نحو 37. لكن Task 6 **لم تُصرَف لها دفعة واحدة قط**،
و`works/` كانت في حال أسوأ ممّا كان عليه `thinkers/` في أي وقت:

| | قبل |
|---|---|
| ملفات `works/` | 609 |
| منها بـ`## المصادر` | **صفر (0%)** |
| وسيط الطول | 1,291 حرفاً |
| تحت إرشاد 1,800 | **429 من 609** |

وأسوأ ملفَّين في الدفعة: **«السوفسطائي» لأفلاطون بـ577 حرفاً**، و**«الخطابة» لأرسطو بـ673 حرفاً
وصفر عناوين أقسام**.

## الأرقام

| المؤشر | قبل | بعد |
|---|---|---|
| وسيط الطول | 1,643 | **4,693** |
| أقصر ملف | **577** | **3,689** |
| أطول ملف | 3,749 | 5,979 |
| `## المصادر` | **0/30** | **30/30** |
| `publication_year` معبّأ | 21/30 | 26/30 (و4 تُركت null عن قصد) |

## أمر التحقق

```
cat scratchpad/t6/b_6_1.txt | xargs python3 scripts/preflight_check.py
→ ✅ 30 ملف — صفر مخالفات آلية.
python3 scripts/build_slug_index.py → 22 تعارض slug (الثابت محفوظ)
```

## لماذا 30/30 هنا مقابل ~80% في Task 4

قاعدة المصادر مختلفة **وأسهل**: مصدر الكتاب هو **طبعته**. فالطبعة الأصلية تستوفي القاعدة 5
دائماً. وللنصوص القديمة وبلا مؤلِّف تحلّ **الطبعة النقدية** محلّها:

- بيرنت (OCT، 1900) للسوفسطائي · روس (1959) وكاسِل (1976) للخطابة
- **كوربان**، *Opera Metaphysica et Mystica* — للتلويحات (I، 1945) ولحكمة الإشراق (II، 1952)
- **كلود سلامة** (المعهد الفرنسي، دمشق، 1990) لتبصرة الأدلّة للنسفي
- **بولوتسكي وبوهليغ** (1940) و**فونك** (1999–2000) للكِفالايا المانوية
- **رينولدز** (OCT، 1977) لحواريات سينيكا

## الترجمات العربية: أُثبتت في اثنين من ثلاثين فقط

وهذا **النتيجة الصحيحة**، لا نقصاً. أخطر ما يمكن أن يُرتكب في هذه المهمة **ترجمة عربية مُختلَقة**،
فلم يُذكر مترجم ولا ناشر ولا سنة إلا حيث أمكن تثبيتها:

- **الداوديجينغ**: فراس السوّاح، *الطاو تي تشينغ*، دار علاء الدين (دمشق)، 1998 — مع تسجيل أنها
  عبر لغات وسيطة لا عن الصينية.
- **الخطابة**: تحقيق **عبد الرحمن بدوي** للترجمة العربية الوسيطة (القاهرة، 1959) — ووُصفت
  **بأنها وسيطة** لا حديثة.

وللأعمال **عربية الأصل** (التلويحات، حكمة الإشراق، تبصرة الأدلّة) يسقط السؤال أصلاً: المطلوب
طبعة لا ترجمة، وقيل ذلك صراحةً. وفيما عدا ذلك سُجِّل الغياب في `gaps` **بوصفه نتيجة بحث** لا حقيقة.

## تلفيق حُذف

| الملف | ما كان مكتوباً |
|---|---|
| `wrk-kephalaia` | طبعة منسوبة إلى **العالِم الخطأ والعقد الخطأ**: «ألبِري 1938» وهي **غاردنر 1995**؛ وألبِري 1938 هو كتاب المزامير. وبنية بستّة أقسام و«380 فصلاً» ومصطلح لاتيني مُختلق |
| `wrk-buddhas-brain` | طريقة **HEAL** منسوبة إلى كتاب 2009 وهي في *Hardwiring Happiness* (2013) |
| `wrk-erroneous-zones` | مادة REBT معروضة كأنها لداير — وهي **لإليس (1962)**، وهي بعينها الخصومة الموثَّقة حول الكتاب |
| `wrk-lewin-...` | تصنيف ثلاثي للنزاع ليس له؛ وأن *Getting to Yes* (1981) استند إليه — **وقد مات 1947**؛ و`active_end: 1981` مشتقّ من ذلك |
| `wrk-goffman-...` | **ابن خلدون** شريكاً في تأسيس التفاعلية الرمزية؛ وأن أوستن وغرايس «أعادا قراءة غوفمان» وأوستن مات 1960 |
| `wrk-gender-trouble` | مناظرة مع **ماكينون** في مجلّد 1992 — وهو مجلّد نيكولسون 1990 ولا يحوي شيئاً من ذلك |
| `wrk-tree-of-knowledge` | **فيرشور** مؤسِّساً للذكاء الاصطناعي الإنضامي؛ وتأثير في فاتسلافيك وساتير بلا سند |
| ثلاثة ملفات | أرقام مبيعات وترجمات مُختلقة: «35 مليون نسخة» · «30+ لغة» · «250+ لغة» |

## تصحيحات

- **`wrk-illuminations-walter-benjamin`**: ليس كتاباً كتبه بنيامين بل **مختارات إنجليزية 1968**
  اختارتها وقدّمت لها **حنة آرندت** وترجمها هاري زون. و1955 هو *Schriften* الألماني.
  غُيِّرت `publication_year` **مع تسجيل التعليل في `gaps`** لا بصمت.
- **`wrk-design-everyday-things`**: صدر 1988 باسم *The Psychology of Everyday Things*، وأُعيدت
  تسميته 1990، وطبعة موسَّعة 2013.
- **`wrk-goffman-...`**: أول ظهور من **مركز البحوث الاجتماعية بجامعة إدنبرة 1956** لا 1959.
- **`wrk-daodejing`**: `publication_year: -400` كان تخميناً فأُعيد إلى **null**.
- **`wrk-beck-cognitive-therapy-depression`**: نتيجة **NIMH TDCRP 1989** مذكورة على وجهها
  (العلاج المعرفي **لم** يتفوّق)، مع تنبيه أن الأطلس يعرضها مقلوبة في موضع آخر — وهو ما تشير
  إليه قائمة Task 7 في SPARK.md أصلاً. والكتاب **لأربعة مؤلِّفين** لا لبيك وحده.

## قرارات اتخذتها

- **فتح Task 6 قبل إكمال Task 4**: كلتاهما في البند نفسه من قائمة الأولويات، وTask 4 مُثبتة
  وتحتاج 37 دفعة، وTask 6 عند الصفر المطلق. الوصول بـ`works/` من 0% إلى شيء أنفع من دفعة سابعة.
- **مراقبة الأطوال أثناء عمل الوكلاء لا بعده** — لم يحتَج أي ملف تقليماً بعد التسليم هذه المرّة.

## متوقف عنده (لرئيس التحرير)

- **تعارض القاعدة 1** مع المهام 1–12: تقرير مستقلّ في `../REVISION/FINDING-rule1-vs-tasks-1-12.md`.
  أبلغ عنه وكيل توقّف قبل الكتابة، وهو محقّ.
- **`wrk-design-everyday-things`** `belongs_to: sch-cognitive-behavioral` وهو كتاب في علم النفس
  المعرفي/HCI لا CBT — ولا يوجد `sch-` معتمد لعلم النفس المعرفي (`sch-cognitive-psychology`
  في مسودات MiniMax فقط).
- **عنوان `wrk-beck-cognitive-therapy-depression`** يقول «لآرون بيك» لكتاب بأربعة مؤلِّفين —
  ولم يُغيَّر لأن ملفات أخرى تحمل العنوان حرفياً في `related`، فتغييره يحتاج دفعة تصحّح كل مُشير.
- **`publication_year` مُختلَقة ورثتها الملفات** (1185 للتلويحات، 60 لسينيكا) — تُركت وسُمّيت
  في `gaps` بوصفها تقديرات بلا سند.

## ملاحظات لموجزات 6.2 فصاعداً

جُمعت من الوكلاء العشرة كلهم في `task-6-brief-notes.md` — تسع نقاط، منها **اقتراح قِسته ورفضته**
(توسيع فحص السنوات في preflight: 100% إيجابيات كاذبة على 409 ملفات)، و**تصحيح لخطأ في صياغتي أنا**
عن «الصيغة القريبة» من القائمة السوداء.

## الملفات

```
content/ar/works/wrk-men-are-from-mars.md
content/ar/works/wrk-12-rules-for-life.md
content/ar/works/wrk-design-everyday-things.md
content/ar/works/wrk-power-of-habit.md
content/ar/works/wrk-daodejing.md
content/ar/works/wrk-kephalaia.md
content/ar/works/wrk-lewin-resolving-social-conflicts.md
content/ar/works/wrk-buddhas-brain.md
content/ar/works/wrk-erroneous-zones.md
content/ar/works/wrk-tabsirat-al-adilla-nasafi.md
content/ar/works/wrk-beck-cognitive-therapy-depression.md
content/ar/works/wrk-affective-neuroscience.md
content/ar/works/wrk-tractatus.md
content/ar/works/wrk-speculum-of-the-other-woman-irigaray.md
content/ar/works/wrk-learned-optimism.md
content/ar/works/wrk-rhetoric-aristotle.md
content/ar/works/wrk-theory-of-justice.md
content/ar/works/wrk-tiny-habits.md
content/ar/works/wrk-why-has-nobody-told-me.md
content/ar/works/wrk-sophist-plato.md
content/ar/works/wrk-gender-trouble.md
content/ar/works/wrk-goffman-presentation-self.md
content/ar/works/wrk-al-talwihat-suhrawardi.md
content/ar/works/wrk-on-tranquility-of-mind-seneca.md
content/ar/works/wrk-illuminations-walter-benjamin.md
content/ar/works/wrk-essence-of-christianity-feuerbach.md
content/ar/works/wrk-porges-polyvagal-theory.md
content/ar/works/wrk-hikmat-al-ishraq-suhrawardi.md
content/ar/works/wrk-flow-csikszentmihalyi.md
content/ar/works/wrk-tree-of-knowledge.md
```
