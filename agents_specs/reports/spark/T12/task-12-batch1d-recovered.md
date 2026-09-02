# Task 12 — دفعة 1د (تقرير مستعاد)

الحالة: مكتمل | العملية: تعميق سياقات (contexts) | الملفات: 4

## سياق التقرير

هذا التقرير **مستعاد بأثر رجعي**، وليس نتاج دفعة جديدة. أثناء تحقيق حالة الـ~100 ملف
"claimed" في `state.json` بلا تقرير مكتوب، طابقت `git status`/`git diff` على قائمة الـ130
ملف المُدَّعاة في `contexts/experiences/metaphors` مقابل ما ذُكر فعلاً في تقارير
`T12/task-12-batch1a.md`، `1b.md`، `1c.md`. النتيجة: **8 ملفات إضافية معدَّلة فعلياً بلا
تقرير**، منها 4 تعديلات جوهرية (تعميق فعلي بمنهج T12) و4 تعديلات تافهة (تصحيح slug واحد
`dis-major-depressive`→`dis-mdd` و`dis-borderline-personality`→`dis-bpd` ناتجة عن دفعة دمج
مكررات Task 10، لا علاقة لها بالتعميق). هذا التقرير يغطي الـ4 الجوهرية فقط.

الملفان الآخران اللي كانا معدَّلين بنفس تصحيح الـslug التافه (`ctx-covid19-pandemic-global-lockdown`،
`ctx-dsm-evolution-biological-psychiatry`) **ما زالا فعلياً بلا تعميق حقيقي** رغم ظهورهما
claimed — أي متاحان لأخذهما ضمن باقي Task 12. كذلك `exp-susanna-kaysen-mclean-hospital` و
`exp-william-styron-darkness-visible` (معدَّلان بنفس تصحيح الـslug فقط، وغير مُدرَجين أصلاً
في claimed) — متاحان أيضاً.

## الأرقام

الملفات الأربعة المغطاة هنا:
1. `content/ar/contexts/ctx-counter-reformation-jesuit-education.md`
2. `content/ar/contexts/ctx-east-asian-neo-confucianism.md`
3. `content/ar/contexts/ctx-french-salons-encyclopedie.md`
4. `content/ar/contexts/ctx-industrial-revolution-manchester.md`

كل ملف: إضافة `## المصادر` (2–4 مراجع)، أسماء وتواريخ محددة تستبدل الجمل العامة، `gaps` دقيقة
غير قالبية بدل الصيغة الافتراضية.

## أمر التحقق

```
python3 scripts/preflight_check.py content/ar/contexts/ctx-counter-reformation-jesuit-education.md \
  content/ar/contexts/ctx-east-asian-neo-confucianism.md \
  content/ar/contexts/ctx-french-salons-encyclopedie.md \
  content/ar/contexts/ctx-industrial-revolution-manchester.md
```
→ عند الفحص الأول: مخالفة واحدة (`ctx-counter-reformation-jesuit-education`: عنوان رابط
`exp-descartes-stove-heated-room` غير مطابق للعنوان الحقيقي للملف — بقايا من قبل هذه الدفعة).
تم تصحيحه إلى العنوان الصحيح: "تجربة ديكارت في الغرفة المدفأة بألمانيا (1619): ميلاد المنهج
الحديث". بعد التصحيح: **✅ 4 ملف — صفر مخالفات آلية**.

## قرارات اتخذتها

- `ctx-counter-reformation-jesuit-education`: صححت `title` في رابط `exp-descartes-stove-heated-room`
  ليطابق عنوان الملف الفعلي (كان منسوخاً بصيغة مختصرة قديمة). أضفت `active_start/end` (1545–1648)
  وتواريخ دقيقة (Ratio Studiorum 1599، التحاق ديكارت بلافليش 1607–1615، ليلة الرؤى 10 نوفمبر 1619).
- `ctx-east-asian-neo-confucianism`: ميّزت تشو شي عن الأخوين تشنغ، وأضفت مصطلحات محددة
  (Ren/Yi/Li/Zhi/Xin) بدل ترجمة عامة، واستبدلت "اقتباسات مختارة" الفارغة بـ`## المصادر`.
- `ctx-french-salons-encyclopedie`: صححت عدد مجلدات الموسوعة (17 نصي + 11 لوحات، لا "28 مجلداً"
  كما في النص الأصلي) وأضفت أسماء دقيقة (دالمبير، تاريخ سحب الامتياز 1759).
- `ctx-industrial-revolution-manchester`: أضفت تواريخ عمل إنجلز في مانشستر (1842–1844) وتاريخ
  نشر كتابه (لايبزغ 1845) وربطها نصياً بالمخطوطات الاقتصادية والفلسفية لماركس (1844).

## متوقف عنده (لرئيس التحرير)

- لا شيء متوقف — الملفات الأربعة أُغلقت بالكامل.

## الملفات

content/ar/contexts/ctx-counter-reformation-jesuit-education.md
content/ar/contexts/ctx-east-asian-neo-confucianism.md
content/ar/contexts/ctx-french-salons-encyclopedie.md
content/ar/contexts/ctx-industrial-revolution-manchester.md
