# تصحيح دفعة 1.1–1.10 — أوامر لـSpark

**السياق:** مراجعة مستقلة لكل الـ250 ملف في `content/ar/drafts/spark/thinkers/` (تاسكات 1.1→1.10)
لقت نمط تلفيق/خلل ممنهج تحت غطاء اجتياز الفحص الشكلي (لا جملة قائمة سوداء، قسم مصادر موجود).
**قبل أي حاجة تانية، وقف تماماً عن ترقية أي ملف من الدفعة دي للمعتمد.** نفّذ الأوامر دي بالترتيب.

---

## أمر 0 — لا تكتب لغاية ما تخلص القراءة دي

اقرأ الملف ده كامل الأول. بعدين افتح كل ملف مذكور، افهم المشكلة، وصلحها حسب التصنيف تحت.
كل تصحيح = commit منطقي واحد. بعد كل مجموعة (أمر 1، أمر 2، ...) اكتب تقرير فرعي في
`agents_specs/reports/spark/T1/batch1-fix-<رقم الأمر>.md` بنفس قالب SPARK.md المعتاد.

---

## أمر 1 — إعادة تدوير الـslug (الأخطر، يكسر شبكة الأطلس) — 8 ملفات

الملفات دي الـslug فيها بيستدعي شخص مؤسِّس معروف، لكن المحتوى الفعلي عن شخص مختلف تماماً،
والملف نفسه معترف بده في `gaps`. ده يخالف القاعدة 4 في SPARK.md ("ممنوع اختراع slug") وقاعدة 6
("ممنوع حذف أو إعادة تسمية ملف. الازدواج → دمج + إحالة") — مش استبدال هوية كاملة.

| الملف | الـslug بيستدعي | المحتوى الفعلي عن |
|---|---|---|
| `thk-jjoyce.md` | جيمس جويس | "مارغريت بِي" (اسم عائلة "Be" مبتور/مشبوه) |
| `thk-cwhitaker-pt.md` | كارل ويتاكر | "جون مارش" (اسم عام غير قابل للتحقق) |
| `thk-jroddy.md` | (غير واضح) | "ج. لوك وود" — شخص حقيقي موثق لكن على slug غلط |
| `thk-hliddle-clin.md` | هوارد ليدل | "كريغ هندرسون" |
| `thk-lmorrnah.md` | مورّنا سيميونّا | "أبراهام كاوانيوآ" |
| `thk-jgould.md` | (غير واضح) | "جيمس ليبشيتز/James Lubin" — غير مؤكد الوجود أصلاً |
| `thk-hershman.md` | (غير واضح) | "دينا فاردي" |
| `thk-ebosnak.md` | يوحي بروبرت بوسناك | "مؤسسو رابطة معالجي ساندبلاي" (كيان جماعي) |

**لكل ملف من الثمانية:**
1. لو المحتوى الفعلي عن **شخص حقيقي موثّق** (زي `thk-jroddy` → ج. لوك وود): أنشئ له slug جديد صحيح
   في `content/ar/drafts/spark/thinkers/` (تأكد من `EXISTING_SLUGS.md` الأول)، انقل المحتوى إليه،
   واحذف نسخة الـslug القديم من `drafts/` — واكتب في `agents_specs/requests-spark.md` سطر يوضح:
   "الـslug `thk-xxx` القديم كان مخصص لشخص [اسمه لو معروف] ولسه بلا ملف — يحتاج كتابة لاحقة أو حجر
   صحي لو غير موجود".
2. لو المحتوى عن **شخص غير مؤكد الوجود** (زي `thk-jgould`، `thk-hershman`): **لا تكتب سيرة إطلاقاً**.
   طبّق Task 2 من SPARK.md حرفياً: سجّله في `agents_specs/quarantine-spark.md` بالسبب، أو لو غامض
   حقيقي سيبه بأقل حد ووصف الغموض فقط بلا سردية بيوغرافية.
3. `thk-ebosnak.md`: قرر — لو المقصود شخص فردي (روبرت بوسناك مثلاً) اكتب عنه هو، مش عن كيان جماعي
   باسم مختلف. الكيانات الجماعية (رابطات/جمعيات) مش `type: "مفكر"` أصلاً.

---

## أمر 2 — سيرة بلا أي مصدر يخص صاحبها (خرق مباشر لـ Task 2) — الملفات دي

النمط: مصادر الملف كلها لمؤسس المدرسة/المعلّم، وصفر مصدر بقلم أو عن الشخص موضوع الملف نفسه،
مع تفاصيل سردية محددة (منشورات، ورش، مقالات) بلا أي توثيق فعلي لها.

```
thk-jbissel, thk-cgerber2, thk-gillian-abbott, thk-jsimmermacher, thk-jbrowne, thk-epaz,
thk-ddiamond, thk-amncube, thk-katka-rubin, thk-aschultz, thk-jenna-brown, thk-andrew-schnack,
thk-jenniferschwab, thk-connie-rae-anderson, thk-bruceperkins, thk-daniellevision,
thk-eleanor-crisostomo, thk-alicorazon, thk-erikpearson, thk-julierawlins, thk-janicewilliams,
thk-ctuzio, thk-aoliveira, thk-jose-salgado, thk-david-reeve, thk-jacqueline-tortorella,
thk-james-berman, thk-gene-ennis, thk-deborah-kremer, thk-jim-ackerman, thk-kastrinidis,
thk-jarlena-white, thk-lars-johansson, thk-james-gumpert, thk-kurtz-sherman, thk-jbeker,
thk-brosen, thk-hnishida, thk-cel-bejjani, thk-ecolle, thk-katie-laperriere, thk-kruger-marielle,
thk-kevin-sparger, thk-jenny-osborn, thk-jlchner, thk-cgarrett, thk-katie-rae, thk-carolyn-dalglish,
thk-bill-matthews, thk-grose, thk-dparker, thk-jennifer-olding, thk-brianhug, thk-elin-rbaek,
thk-lavinia-shaw, thk-jacqueline-peart, thk-jose-arsenio, thk-deepak-ramsubeik
```

**لكل ملف من القائمة دي (~57 ملف): طبّق Task 2 من SPARK.md حرفياً — بحث فعلي عن مصدر أساسي
حقيقي، مش تخمين:**
- لقيت مصدر حقيقي بقلم/عن الشخص نفسه → أعد كتابة الملف بيه، احذف المصادر اللي مش بتاعته.
- ملقتش حاجة تثبت وجوده بعد بحث فعلي → سجّله في `agents_specs/quarantine-spark.md` بالسبب
  الدقيق (مثال: "لا يوجد أي منشور أو ذكر مستقل باسم X خارج وصف الملف نفسه").
- في شك حقيقي لكن الشخص مش مستحيل الوجود → سيبه غامضاً وسمّي الغموض بدقة في `gaps` بدل بناء
  سردية بيوغرافية كاملة.

**ممنوع الاعتماد على "المدرسة العلاجية اللي بينتمي لها موثقة" كبديل عن توثيق الشخص نفسه.**

---

## أمر 3 — أخطاء نسبة/هوية فعلية (تلفيق واضح، تصحيح فوري) — 6 ملفات

- **`thk-calbright.md`**: المصدر `Albright, A.C. (2011)` تبع مؤلفة مختلفة تماماً (Ann Cooper
  Albright، والكتاب فعلياً 2013) بينما الملف عن "Karen Albright". صحّح الاستشهاد أو احذفه، وتأكد
  من هوية الشخص الحقيقي قبل أي كتابة تانية.
- **`thk-dhanna.md`**: المصدر بتاع Michael J. Goldstein (UCLA، أبحاث Expressed Emotion) منسوب
  خطأ لـ"فرانك غولدشتاين". صحّح النسبة أو احذف المصدر لو مش بتاع الشخص فعلاً.
- **`thk-gunnel-cederblad.md`**: المصدر الفعلي لـMarianne Cederblad (دراسة Lundby) منسوب لـ"Gunnel
  Cederblad" — تأكد أي الاسمين هو الصح وصحّح الملف كله على أساسه.
- **`thk-jacqueline-astington.md`**: `title` = "جاكلين أستنغتون" لكن `en` = "Janet Wilde
  Astington" (الاسم الحقيقي للباحثة). صحّح العنوان العربي ليطابق.
- **`thk-lonan.md`**: الشخصية الحقيقية "لويجي أونيس" (Luigi Onnis) رجل، لكن الملف مكتوب بصيغ
  تأنيث بالكامل. تحقق من الجنس الصحيح وصحّح كل الصيغ.
- **`thk-kaarlokeranen.md`**: الاستشهاد `Seikkula, Alakare, & Keränen (2000)` — تحقق من وجود
  Keränen فعلاً كمؤلف مشارك في هذه الورقة تحديداً (الأدبيات المعروفة بتنسب دول لـSeikkula/Alakare/
  Aaltonen)، وصحّح أو احذف لو مش موجود.

---

## أمر 4 — روابط `related` بـ id/title متضاربَين (عطل نسخ-لصق متكرر)

`id="thk-sgreys"` بعنوان "دانيال هيوز" اتكرر **3 مرات منفصلة** — يوحي بنسخ من قالب معطوب:
`thk-apert.md`, `thk-brianhug.md`, `thk-bruceperkins.md`.

حالات مشابهة لازم تتصحح فرداً فرداً (افتح كل ملف، دوّر على الـid الصح اللي يطابق الاسم في
`EXISTING_SLUGS.md`، أو احذف الرابط لو مالوش أساس):
- `thk-dgray.md`: `id="thk-tstone"` عنوان "مارك ستون" — لا تطابق
- `thk-jacqueline-varner.md`: `id="thk-ogilvie"` عنوان "بروس أوكيف" (الصح النقل الصوتي "أوغيلفي")
- `thk-eduardo-duran.md`: `id="exp-david-duran-..."` بيسمي "David Duran" بدل "Eduardo Duran"
- `thk-jmitchell.md`: الرابط `thk-jflax` غير مذكور إطلاقاً في المتن — احذفه أو برّره في المتن
- `thk-gadamoli.md`: الرابط `thk-capriles` غير مذكور في المتن (فقط في المصادر) — احذفه أو برّره
- `thk-lovaas.md`: الرابط `thk-donbaer` غير مبرر في المتن — نفس الإجراء

---

## أمر 5 — إساءة استخدام حقل `gaps` (منتشرة — عشرات الملفات)

النمط: `gaps` بتعيد ذكر حقيقة مؤكدة موجودة أصلاً في المتن/`dates`، بدل تسمية نقص فعلي. القاعدة
في SPARK.md واضحة: "`gaps` تسمّي الناقص بالضبط." هذا مش نقص، ده تكرار.

**افحص كل ملف فيه `gaps` عبر الدفعة كلها (مش بس القايمة دي) وطبّق القاعدة دي:**
- لو المعلومة في `gaps` موجودة أصلاً في المتن أو الـfrontmatter → احذفها من `gaps` (هي مش فجوة).
- لو `gaps` بتحتوي معلومة **جديدة** غير مذكورة في المتن (زي `thk-cherylfairbairn`: لقب أستاذة +
  وسام) → انقلها للمتن، مش لحقل الفجوات.
- لو `gaps` صيغة قالبية عامة ("البيانات البيوغرافية الدقيقة تتطلب مراجعة من [جمعية]") بلا تسمية
  حقل محدد ناقص → أعد صياغتها لتسمي الحقل بالضبط (مثال: "تاريخ الميلاد غير مؤكد" مش "يتطلب مراجعة").

أمثلة موثقة بالفعل (مش حصرية — افحص كل الدفعة):
```
thk-john-makransky, thk-epictetus, thk-ahill, thk-acatania, thk-cavasco, thk-gold, thk-dmueser,
thk-ldesalvo, thk-lmiller, thk-eholt, thk-jbirnbrauer, thk-lequier, thk-bespaloff,
thk-cwebster-stratton, thk-chris-iveson, thk-cherylfairbairn, thk-atobart, thk-cschaefer,
thk-donaldatkinson, thk-bidwell, thk-kristin-buss, thk-flake, thk-econrad, thk-delman, thk-afaria,
thk-lroszak, thk-herskovitz, thk-andrew-barnes
```

---

## أمر 6 — مشاكل فردية إضافية (تصحيح مباشر)

- **`thk-jmertz.md`**: `type: "مفكر"` لكن المحتوى عن هيئة تحرير مجلة جماعية — أعد تصنيفه أو فكّكه
  لأفراد حقيقيين حسب طبيعة المحتوى الفعلي.
- **`thk-fkfu.md`**: تضارب الاسم الأوسط (K. مقابل H. Fu) بين عربي/إنجليزي/مصدر — وحّد الصحيح.
- **`thk-bala-jaison.md`**: عنوان/ناشر كتاب مختلفان بين "أهم المؤلفات" و"## المصادر" لنفس المرجع
  المفترض — تحقق من العنوان الصحيح ووحّده.
- **`thk-kmithoefer.md`**: تعارض بين العنوان "آن ميثوفر" والـslug — تحقق واصلح.
- **`thk-david-erceg.md`**: العنوان العربي يسقط جزء من `en: "David Erceg-Hurn"` — أكمله.
- **`thk-donaldatkinson.md`**: `active_end: 2010` بالفرونتماتر يتناقض مع المتن "من 1972 إلى 2006" —
  وحّد التاريخ الصحيح.
- **`thk-ahill.md`**: يوهم بتعاون بين أدريان هيل (توفي 1977) وكاثي مالكيودي (جيل لاحق زمنياً) —
  صحّح الصياغة لتفصل بين "ممهداً الطريق لـ" و"تعاون فعلي مع".
- **`thk-jim-ackerman.md`**: يعرض "إعادة الولادة" (Rebirthing) بلا أي تحذير رغم إنها مصنّفة
  `controversial`/`discredited` صراحة في SPARK.md (Task 9) — ضيف جملة توضيحية عن وضعها الجدلي.
- **`thk-kurbatov.md`**: مصنّف ضمن "مفكري علم النفس الوجودي" لكنه فعلياً ناقد أدبي روسي — راجع
  التصنيف وربطه بـ`sch-existential-therapy`، وأعد كتابة `gaps` لتسمي نقصاً فعلياً بدل إعادة سرد
  السيرة.
- **`thk-isap.md`**: أسماء "توماس إيرليش"، "أورسولا فيرتز"، "بول بروتشه" مذكورة بلا أي مصدر يدعمها
  — احذفها أو وثّقها.
- **`thk-alicorazon.md`**: فيه حرف كوري (هانغل) مقحم وسط كلمة عربية — عطل ترميز، صحّحه فوراً.
- **`thk-aboller.md`, `thk-amy-morgan.md`, `thk-dpierrakos.md`**: قسم "## ما قدمه/قدمته" بجمل عامة
  بلا اسم/سنة/رقم (يخالف معيار القبول #1) — إما املأها بمادة موثقة أو احذف الجمل العامة واكتب
  الناقص في `gaps`.

---

## بعد كل الأوامر

1. شغّل `python3 scripts/build_slug_index.py`.
2. اكتب تقرير ختامي واحد `agents_specs/reports/spark/T1/batch1-fix-summary.md`: كام ملف اتصحح،
   كام اتحوّل للحجر الصحي، كام slug جديد اتعمل.
3. **وقف وانتظر مراجعة كلود قبل الاستمرار لأي تاسك جديد من SPARK.md** — دي مش نقطة توقف كل 5،
   دي وقفة إلزامية لأن التصحيح ده بيمس القاعدة نفسها.
