# Task 14 — تحليل الفجوة (studies + instruments حديثة)

الحالة: مكتمل جزئياً (فحص فقط، لا كتابة في هذه الدفعة)
العملية: مقارنة قائمتي `std-` و`ins-` في SPARK.md Task 14 بالموجود فعلياً في
`content/ar/drafts/spark/studies/` و`content/ar/drafts/spark/instruments/` | الملفات: 0 جديدة

## `std-` — الموجود (10 ملفات)
stu-ace-study, stu-catie, stu-griffiths-psilocybin-cancer, stu-many-labs-2, stu-maps-mdma-phase3,
stu-minnesota-starvation, stu-mta, stu-robins-vietnam-heroin, stu-stard, stu-whitehall-studies

## `std-` — الفجوة الحقيقية (غير موجود)
- **Many Labs 1، 3، 4** — موجود فقط `many-labs-2`، والقائمة تطلب "Many Labs 1–4" صراحةً
- **فشل تكرار استنزاف الأنا (ego depletion)** — غير موجود كدراسة مستقلة
- **فشل تكرار وضعية القوة (power posing)** — غير موجود
- **بارك الجرذان (Rat Park — ألكسندر)** — غير موجود

## `ins-` — الموجود (10 ملفات)
ins-cat-q, ins-ctq, ins-des-ii, ins-maslach-burnout-inventory, ins-mini-neuropsychiatric,
ins-oq-45, ins-pcl-r, ins-rosenberg-self-esteem, ins-scl-90-r, ins-wai

## `ins-` — الفجوة الحقيقية (غير موجود)
- **مقياس الضغط المُدرَك (Perceived Stress Scale)**
- **استبيان ACE** (مختلف عن `stu-ace-study` — هذا مقياس الأداة نفسها لا الدراسة)
- **WHODAS 2.0**
- **CORE-OM**
- **RAADS-R** (CAT-Q موجود، RAADS-R غير موجود رغم أنهما مذكوران معاً في نفس البند)

## أمر التحقق
`find content/ar/drafts/spark/studies content/ar/drafts/spark/instruments -iname "*<اسم>*"` لكل بند،
مع بحث تكميلي لأسماء بديلة (ego-depletion, power-pos, rat-park, many-labs, stress, core-om, raads,
whodas) → صفر نتيجة لكل البنود المذكورة أعلاه كفجوة.

## قرارات اتخذتها
- Task 14 **ليس مكتملاً** — 8 بنود حقيقية غائبة (4 دراسات + 4 أدوات) من أصل ~24 بنداً في القائمة
  الأصلية. الموجود (10 دراسات + 10 أدوات = 20 ملفاً) يغطي الغالبية لكن ليس الكل.
- لم تُكتب أي ملفات في هذه الدفعة — الطلب كان تحديد الفجوة فقط قبل أي كتابة جديدة.

## متوقف عنده (لرئيس التحرير)
- لا شيء يستدعي قراراً — الفجوة واضحة وجاهزة للتنفيذ في دفعة subagents قادمة (8 ملفات).

## الملفات
لا ملفات جديدة — تقرير فجوة فقط.
