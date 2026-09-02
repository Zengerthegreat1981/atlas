# Task 2.24
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 10

## الأرقام
جمل القائمة السوداء: قبل ~ → بعد 0
ملفات فيها `## المصادر`: قبل 9/10 → بعد 10/10 (thk-mhoyt كان ناقصاً، أُضيف بعد تحقق ويب)

## أمر التحقق
`python3 scripts/task.py verify minimax 2.24` → جمل القائمة السوداء: 0 | سقّالة ظاهرة: 0 | فيها ## المصادر: 10/10
`python3 scripts/preflight_check.py <10 ملفات>` → ✅ صفر مخالفات آلية

## قرارات اتخذتها
جميع الملفات العشرة **موثّقة** — لا حجر، لا غموض.

- **thk-mhoyt (مايكل ف. هويت)**: نفسي إكلينيكي حقيقي، Kaiser Permanente، أحد مؤسسي Single-Session Therapy مع موشيه تالمون وروبرت روزنباوم. الملف كان بلا `## المصادر` رغم محتوى دقيق — تحقق رئيس التحرير عبر بحث ويب مباشر وأضاف القسم.
- **thk-rrudolf**: موثّق. أُضيفت مصادر.
- **thk-mwhitehouse (ماري ستاركس وايتهاوس) — ازدواج مؤكَّد ومُعالَج بشكل صحيح.** نفس الشخص الموثّق فعلاً على `thk-mary-whitehouse` (دفعة 2.7). الملف تحوّل بشكل صحيح لملف إحالة صريح (`related` يشاور على thk-mary-whitehouse، gaps تُقر بالازدواج، القاعدة 6 تمنع الحذف) بدل تكرار السيرة بمصادر منسوخة. لا حاجة لتدخل إضافي.
- **thk-twolff**: موثّق. أُضيفت مصادر.
- **thk-vramachandran (ف.س. رامتشاندران)**: عالم أعصاب شهير حقيقي، UCSD، صاحب أبحاث "المرايا العصبية" والأطراف الوهمية. أُضيفت مصادر.
- **thk-maryolson**: موثّقة. أُضيفت مصادر.
- **thk-vbuhrmann (فيرا بورمان)**: محللة يونغية جنوب أفريقية حقيقية. أُضيفت مصادر.
- **thk-rspitzer (روبرت سبيتزر)**: طبيب نفسي حقيقي، المهندس الرئيسي لـDSM-III. أُضيفت مصادر.
- **thk-sgreenspan (ستانلي غرينسبان)**: طبيب نفسي أطفال حقيقي، مؤسس نموذج DIR/Floortime (نفس المدرسة الغائبة المسجّلة سابقاً من ملف thk-mbauman في missing-schools.md — لا تكرار، مجرد ربط بنفس الفجوة البنيوية).
- **thk-widlocher (دانييل ويدلوشير)**: طبيب نفسي فرنسي حقيقي. أُضيفت مصادر.

## متوقف عنده (لرئيس التحرير)
- لا شيء. الدفعة مكتملة بالكامل: 10 توثيق، صفر حجر، صفر غامض.

## الملفات
content/ar/thinkers/thk-mhoyt.md
content/ar/thinkers/thk-rrudolf.md
content/ar/thinkers/thk-mwhitehouse.md
content/ar/thinkers/thk-twolff.md
content/ar/thinkers/thk-vramachandran.md
content/ar/thinkers/thk-maryolson.md
content/ar/thinkers/thk-vbuhrmann.md
content/ar/thinkers/thk-rspitzer.md
content/ar/thinkers/thk-sgreenspan.md
content/ar/thinkers/thk-widlocher.md
