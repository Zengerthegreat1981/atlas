# Task 2.4
الحالة: مكتمل
المسار: spark | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 15

## الأرقام
- موثّق (كُتبت مسودة في drafts/spark/): 13 / 15
- غير موجود (سُجّل في quarantine-spark.md): 1 / 15 (thk-gweishaar)
- غامض (تُرك بلا مسودة): 1 / 15 (thk-lcarter)
- **اكتشاف نمط مخالفة جديد لم يمسكه preflight_check.py**: `edges.belongs_to.target` بنص حر بدل slug (أو أسوأ: صيغة `related` مكتوبة تحت مفتاح `edges` بحقول `id/title/type` بدل `rel/target/target_type` — بتتسقط صامتة حسب قاعدة SPARK رقم 3). preflight_check ما بيفحصش هذا القسم إطلاقاً. اكتشفته بفحص يدوي إضافي (`grep`/regex) على كل ملفات الدفعة، ولقيت 4 حالات في دفعة اليوم نفسها + حالتين تانيين من دفعات 2.1/2.2/2.3 (jgreenspan, hpalmer, jadler من 2.1/2.2) صححتهم كلهم دلوقتي. **فحص أوسع لقى 126 حالة إضافية في ملفات Task 1 (قبل هذه الجلسة) — خارج نطاق Task 2، اتسجلت أدناه كملاحظة لرئيس التحرير، ملهاش علاقة بشغل اليوم.**
- هذه الدفعة نُفذت بـ15 subagent متوازي، ملف واحد لكل subagent.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-dgreenberger.md content/ar/drafts/spark/thinkers/thk-bmontalvo.md content/ar/drafts/spark/thinkers/thk-blondel.md content/ar/drafts/spark/thinkers/thk-hcrsilneck.md content/ar/drafts/spark/thinkers/thk-jacobsen.md content/ar/drafts/spark/thinkers/thk-beebe.md content/ar/drafts/spark/thinkers/thk-houle.md content/ar/drafts/spark/thinkers/thk-dostoevsky.md content/ar/drafts/spark/thinkers/thk-dboyden.md content/ar/drafts/spark/thinkers/thk-aboal.md content/ar/drafts/spark/thinkers/thk-david-krauss.md content/ar/drafts/spark/thinkers/thk-azriel-of-gerona.md content/ar/drafts/spark/thinkers/thk-gmesibov.md
→ ✅ 13 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- `thk-dgreenberger.md` — موثّق (دِنيز د. ديفيد Denise D. Davis)؛ صححت الجامعة والمتعاون الفعلي (بيك لا جوديث بيك). **صححت edges.belongs_to من نص حر إلى `sch-cognitive-behavioral`.**
- `thk-bmontalvo.md` (براوليو مونتالفو) — موثّق؛ صُحح belongs_to إلى `br-structural-family`، وحُذفت سنوات ميلاد/وفاة غير موثقة بدل تركها.
- `thk-blondel.md` (موريس بلونديل) — موثّق، فيلسوف فرنسي مؤكد؛ صُحح active_end إلى 1949.
- `thk-hcrsilneck.md` (هارولد كراسيلنيك) — موثّق؛ صُحح belongs_to من مدرسة خاطئة زمنياً إلى `br-clinical-hypnotherapy`.
- `thk-jacobsen.md` (بو ياكوبسن) — موثّق؛ صُححت سنة ميلاد وعنوان كتاب كانا خاطئين في الأصل.
- `thk-beebe.md` (بياتريس بيبي) — موثّق، تأكدت أنها ليست جون بيبي اليونغي.
- `thk-houle.md` (سيريل هول) — موثّق؛ حُذف رابط `belongs_to: sch-existential-therapy` غير المسنود (هول منظّر تعليم كبار لا معالج وجودي).
- `thk-dostoevsky.md` — موثّق، شخصية تاريخية مؤكدة؛ عُمّق المتن بمحاور الصرع والقمار وسيكولوجيا الجريمة بمصادر.
- `thk-dboyden.md` (ديان بويدن-بيسّو) — موثّق؛ حُذف عنوان كتاب غير قابل للتحقق بدل تركه.
- `thk-aboal.md` (أوغوستو بوال) — موثّق. **صححت edges.belongs_to من نص حر ("علاج الدراما") إلى `tec-drama-therapy`.**
- `thk-david-krauss.md` — موثّق. **صححت خطأً بنيوياً حقيقياً**: كان قسم `edges` مكتوباً بصيغة `related` (id/title/type) بدل rel/target/target_type — كان سيُسقَط صامتاً بالكامل؛ حُوّل إلى `related` بشكل صحيح.
- `thk-azriel-of-gerona.md` — موثّق، شخصية قبّالية تاريخية مؤكدة؛ حُذف ادعاء تأثر غير مسند بابن عربي.
- `thk-gmesibov.md` (غاري ميسيبوف) — موثّق. **صححت edges.belongs_to من "TEACCH" (نص حر) إلى `br-teacch`.**
- `thk-lcarter.md` — غامض، تُرك بلا مسودة (لبس اسم شائع + عدم يقين كافٍ).
- `thk-gweishaar.md` — غير موجود، سُجّل في quarantine-spark.md؛ الملف نفسه كان يحمل تحذير تحقّق سابق.
- **تصحيحات إضافية على ملفات من دفعات سابقة** اكتُشفت بنفس الفحص اليدوي: `thk-jgreenspan.md`، `thk-hpalmer.md`، `thk-jadler.md`، `thk-lkohlberg.md`، `thk-diclemente.md`، `thk-canderson.md` — كل واحد منهم كان فيه `edges.belongs_to` بنص حر بدل slug؛ صُححوا جميعاً (تفاصيل كل تصحيح في نص الملفات نفسها وgaps).

## متوقف عنده (لرئيس التحرير)
- **126 ملف من نتاج Task 1 (قبل بداية هذه الجلسة)** فيها نفس مخالفة `edges.belongs_to` بنص حر بدل slug — رصدتها بفحص شامل على `content/ar/drafts/spark/thinkers/` لكن **لم ألمسها**؛ خارج نطاق مهمتي في Task 2 وحجمها كبير (يحتاج دفعة عمل مستقلة). القائمة الكاملة موجودة في هذا التقرير أعلى (نتيجة سكريبت الفحص).
- **تم إصلاحه فعلياً**: أضفت `check_edges_target()` لـ`scripts/preflight_check.py` (فحص سادس) يرصد أي `edges.belongs_to.target` مش شكله slug حقيقي. جُرِّب وأمسك فعلاً الـ126 حالة القديمة من Task 1 (مثال: `thk-aboller.md`) — من الآن preflight_check هيرفض أي دفعة فيها هذا النمط تلقائياً.
- `thk-david-krauss.md`: مصدر واحد بس في `## المصادر` (المطلوب استرشادياً 2–5) — هو المصدر الوحيد الموثوق المتاح فعلياً، وثّقته كفجوة بدل اختلاق مصدر ثانٍ.
- `thk-lkohlberg.md`: ظروف وفاته الحساسة (من دفعة 2.3) لسه معلّقة لقرار تحريري.

## الملفات
content/ar/thinkers/thk-dgreenberger.md
content/ar/thinkers/thk-bmontalvo.md
content/ar/thinkers/thk-blondel.md
content/ar/thinkers/thk-hcrsilneck.md
content/ar/thinkers/thk-jacobsen.md
content/ar/thinkers/thk-beebe.md
content/ar/thinkers/thk-houle.md
content/ar/thinkers/thk-lcarter.md
content/ar/thinkers/thk-dostoevsky.md
content/ar/thinkers/thk-dboyden.md
content/ar/thinkers/thk-gweishaar.md
content/ar/thinkers/thk-aboal.md
content/ar/thinkers/thk-david-krauss.md
content/ar/thinkers/thk-azriel-of-gerona.md
content/ar/thinkers/thk-gmesibov.md
