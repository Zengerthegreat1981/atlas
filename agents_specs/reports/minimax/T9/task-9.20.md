# Task 9.20
الحالة: مكتمل
العملية: concepts: مراجعة وتدقيق مركّز لـrelated على 3 ملفات محددة طُلبت صراحة (سبق أن مرّت ضمن 9.1) | الملفات: 3

## الأرقام
روابط related عبر الملفات الثلاثة: قبل 15 → بعد 17
روابط بلا جملة تبرير صريحة في المتن: قبل 2 → بعد 0
مخالفات preflight_check.py: 0 → 0

## أمر التحقق
python3 scripts/preflight_check.py content/ar/concepts/con-adaptation.md content/ar/concepts/con-addiction-model-debate.md content/ar/concepts/con-addiction.md
→ ✅ 3 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- con-adaptation.md: استبدلت con-schema (عنوان عام لا يطابق نقاش المتن المحدد ببياجيه) بـ con-piaget-schema ("المخطط (Schema) عند بياجيه") وعدّلت جملة المتن لتسميه صراحة. أبقيت axm-adaptation، thk-piaget، con-homeostasis، con-hedonic-treadmill، dis-adjustment-disorders (مبررة أصلاً بالمتن). أضفت dbt-evolutionary-psychology-adaptation-vs-spandrel مع جملة جديدة في فقرة "التكيف التطوري" تربط بديهية التكيف بجدل الحتمية التكيفية مقابل الأثر الجانبي (Spandrel).
- con-addiction-model-debate.md: أبقيت sch-motivational-interviewing، con-abstinence-vs-harm-reduction، con-rat-park، thk-mseligman (مبررة بالمتن). أضفت con-addiction مع جملة جديدة في قسم "موقعه" تميّز التفسير اليونغي الروحي عن النماذج الثلاثة الموصوفة في الملف.
- con-addiction.md: لم يتغيّر related — الأربعة الموجودون (thk-dieckmann، thk-mwoodman، thk-jung، br-medical-model-addiction) مذكورون بالاسم في المتن وعناوينهم تطابق الملفات المستهدفة فعلاً؛ لا حذف ولا إضافة.

## متوقف عنده (لرئيس التحرير)
- con-addiction-model-debate.md: edges.belongs_to لا يزال يشير إلى `con-addiction-model-debate` نفسه (حلقة ذاتية بـtarget_type "مدرسة" رغم أن الملف من نوع "مفهوم") — مُسجّلة سابقاً في تقرير 9.1، خارج نطاق related، تحتاج تصحيحاً بنيوياً منفصلاً (الأرجح أن تشير إلى مدرسة علاج فعلية أو تُحذف).
- ملاحظة تشغيلية: هذه الملفات الثلاثة كانت ضمن دفعة 9.1 السابقة أصلاً؛ أعيد بناء related عليها هنا تلبيةً لطلب صريح مطابق (نفس الملفات بالضبط)، فلا تكرار عمل يُحسب على العداد الإجمالي لـTask 9.

## الملفات
content/ar/concepts/con-adaptation.md
content/ar/concepts/con-addiction-model-debate.md
content/ar/concepts/con-addiction.md
