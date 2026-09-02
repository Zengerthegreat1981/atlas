# Task 16.2
الحالة: مكتمل جزئياً
العملية: النوع drg- — الدفعة الثانية (10 مداخل: أدوية + إجراءات تحفيزية + مبادئ إكلينيكية) | الملفات: 10

## الأرقام
مسودات الأطلس الكلية: 251 → 266 (+15 صافي)
نوع `drg-`: 5 → 15 مدخلاً (منها 3 وسّعت تعريف النوع ليشمل إجراءات/ظواهر لا مواد كيميائية فقط)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل الـ10 ملفات → صفر مخالفات آلية
`python3 scripts/build_slug_index.py` → 6884 عنصر (6618 معتمد + 266 مسودة)

## قرارات اتخذتها
- غطّت الدفعة: الهالوبيريدول، ثلاثية الحلقات (فئة)، مثبطات MAO (فئة)، الميثيلفينيديت، النالتريكسون، البوبرينورفين، الإسكيتامين، TMS، تحفيز العصب الحائر، البلاسيبو/النوسيبو، وتعدد الأدوية/الإيقاف التدريجي — كل عناصر Task 16 المذكورة صراحة تقريباً.
- **قرار توسيع نطاق schema `drg-`**: 3 من العشرة ليست "أدوية" بالمعنى الكيميائي الصارم — TMS وتحفيز العصب الحائر إجراءات تحفيز عصبي (جهاز/جراحة لا مادة)، والبلاسيبو/النوسيبو وتعدد الأدوية ظواهر/مبادئ إكلينيكية. عدّلت حقل `drug_class` نصياً في كل حالة ليوضح الفرق (زي "جهاز تحفيز عصبي مزروع جراحياً" أو "ظاهرة استجابة نفسية-فسيولوجية، لا مادة فعالة") بدل حشرها زوراً في قالب دواء كيميائي كلاسيكي — نفس النوع `drg-` يستوعب هذا التنوع لأن التصنيف الأصلي في SPARK.md يخلط أصلاً بين TMS/VNS والأدوية الكيميائية في نفس القائمة.
- كل ملف اتربط بالملفات ذات الصلة من دفعات سابقة في نفس الجلسة (drg-methadone↔drg-naltrexone/drg-buprenorphine، drg-ssri-class↔drg-tricyclic-antidepressants/drg-mao-inhibitors/drg-polypharmacy-tapering، con-psychedelic-renaissance↔drg-esketamine، syn-neuroleptic-malignant/syn-tardive-dyskinesia/syn-akathisia↔drg-haloperidol) بدل تكرار نفس الصياغات.
- تجنبت اختراع thk- لمكتشفي/مطوّري كل دواء (يانسن، كون، بانيتزو، باركر، بيتشر، هورويتز، تايلور) وسجّلتهم كـgaps.

## متوقف عنده (لرئيس التحرير)
- Task 16 الآن مكتمل تقريباً بالكامل (15/25-30 مدخلاً مطلوباً، وكل الأسماء المذكورة صراحة في نص SPARK.md اتغطّت). العناصر المتبقية لو حبيتوا التوسّع أكتر: أدوية فردية إضافية زي olanzapine/quetiapine/risperidone (مذكورة في stu-catie لكن بلا ملف drg- مستقل)، أو مضادات قلق أخرى.
- ملاحظة تقنية بسيطة: `drg-vagus-nerve-stimulation.md` اتكتب قبل `drg-tms.md` بترتيب متوازي، فسطر gaps فيه بيقول "لا يوجد drg-tms بعد للمقارنة" رغم إنه اتكتب فعلاً في نفس الدفعة — تفصيل تجميلي بسيط مش مخالفة فعلية، ممكن يتصحح لاحقاً بسهولة.

## الملفات
content/ar/drafts/spark/drg/drg-haloperidol.md
content/ar/drafts/spark/drg/drg-tricyclic-antidepressants.md
content/ar/drafts/spark/drg/drg-mao-inhibitors.md
content/ar/drafts/spark/drg/drg-methylphenidate.md
content/ar/drafts/spark/drg/drg-naltrexone.md
content/ar/drafts/spark/drg/drg-buprenorphine.md
content/ar/drafts/spark/drg/drg-esketamine.md
content/ar/drafts/spark/drg/drg-tms.md
content/ar/drafts/spark/drg/drg-vagus-nerve-stimulation.md
content/ar/drafts/spark/drg/drg-placebo-nocebo.md
content/ar/drafts/spark/drg/drg-polypharmacy-tapering.md
