# Task 2.2
الحالة: مكتمل
المسار: spark | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 15

## الأرقام
- موثّق (كُتبت مسودة في drafts/spark/): 12 / 15
- غير موجود (سُجّل في quarantine-spark.md، الملف الأصلي لم يُمسّ): 2 / 15
- غامض (تُرك الملف الأصلي كما هو، بلا مسودة): 1 / 15
- **إصلاح فعلي في `scripts/preflight_check.py`**: السكريبت كان يفحص السنوات داخل حقل `dates` الخام في الـfrontmatter وداخل `## المصادر` (طبعات/مراجع حديثة) كأنها أحداث سيرة، فيولّد إنذارات كاذبة متكررة. أضفت `_prose_body_only()` لقصر الفحص على المتن النثري الفعلي فقط. (بعد الإصلاح: 3 من 4 إنذارات وهمية اختفت في هذه الدفعة وحدها — berdyaev, glover, lvdpost).
- **باگ أدخلته أنا بنفس الإصلاح واكتُشف بالمراجعة**: نافذة السياق (`window`) كانت تُقتطع من `raw_text` الأصلي بإزاحة محسوبة على `prose` المقتطَع، فتُنتج سياقاً مغلوطاً. صُحح فوراً (`window = prose[...]` بدل `raw_text[...]`) وأُعيد التحقق.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-jadler.md content/ar/drafts/spark/thinkers/thk-bakewell.md content/ar/drafts/spark/thinkers/thk-binswanger.md content/ar/drafts/spark/thinkers/thk-dbecker.md content/ar/drafts/spark/thinkers/thk-berdyaev.md content/ar/drafts/spark/thinkers/thk-glover.md content/ar/drafts/spark/thinkers/thk-hpalmer.md content/ar/drafts/spark/thinkers/thk-lvdpost.md content/ar/drafts/spark/thinkers/thk-alam.md content/ar/drafts/spark/thinkers/thk-cooper.md content/ar/drafts/spark/thinkers/thk-hammarskjold.md content/ar/drafts/spark/thinkers/thk-busch.md
→ 3 مخالفات متبقية، كلها في thk-bakewell.md وthk-dbecker.md، وكلها false positive في فحص الجنس النحوي (الكلمة "مفكر" مطابقة داخل `type:` أو كصفة لأشخاص آخرين مذكورين في المتن — سارتر وهايدجر وغيرهما — لا للشخصة نفسها؛ متن الملفين فعلياً مؤنث صحيح بالكامل: "أعادت"، "طوّرت"، "نشرت"، "أسهمت"...). تحققت يدوياً بفحص كل تطابق.

## قرارات اتخذتها
- `thk-jadler.md` (جانيت أدلر) — موثّق، مؤسِّسة مفهوم "الشاهد" في الحركة الأصيلة.
- `thk-bakewell.md` (سارة بيكويل) — موثّق، مؤرخة فلسفية بريطانية معروفة (*At the Existentialist Café*).
- `thk-binswanger.md` (لودفيغ بينسوانغر) — موثّق مع تصحيح: أُضيفت إشارة "طبعة صدرت بعد وفاته عام 1992" لمراسلاته مع فرويد، وحُذف رابط `thk-bischler` المحجور من related.
- `thk-dbecker.md` (ديبورا بيكر) — موثّق، لكن صححت `edges.belongs_to` الذي كان يستهدف نصاً حراً ("التأهيل النفسي-الاجتماعي") بدل الـslug الموجود فعلاً `br-psychiatric-rehabilitation` (نفس المدرسة مذكورة صح في `related` بالفعل — كان مجرد سهو في `edges`). صححت أيضاً `part` من "philosophy" إلى "psychology".
- `thk-berdyaev.md` (نيكولاي بيردييف) — موثّق، فيلسوف وجودي مسيحي روسي مؤكد تماماً.
- `thk-glover.md` (إدوارد غلوفر) — موثّق، محلل نفسي بريطاني، خصم كلاين في المناقشات الخلافية.
- `thk-hpalmer.md` (هاري بالمر) — موثّق، مؤسس دورات Avatar؛ صُحح خطأ هوية كان يربطه بـ Landmark Forum خطأً في الملف الأصلي.
- `thk-lvdpost.md` (لورنز فان دير بوست) — موثّق، مع إضافة قيد صريح عن تفنيد سيرته الذاتية المعلنة في سيرة J.D.F. Jones النقدية (2001)، وحذف رابطين related غير قابلين للتحقق.
- `thk-alam.md` (محمود أمين العالم) — موثّق، مفكر ماركسي مصري؛ حُذف ادعاء غير مؤكد عن استضافته سارتر وبوفوار شخصياً وسُجّل في gaps بدل تركه كحقيقة.
- `thk-cooper.md` (ميك كوبر) — موثّق، أستاذ حالي بجامعة روهامبتون.
- `thk-hammarskjold.md` (داغ همرشولد) — موثّق، مع تصحيح رابط related من "مارتن بوبر" إلى العنوان المطابق فعلياً لـ `thk-mbuber` ("مارتن بُبَر").
- `thk-busch.md` (توماس بوش) — موثّق، أستاذ فلسفة بجامعة فيلانوفا.
- `thk-adelaserna.md` — غامض، تُرك كما هو، لا مسودة.
- `thk-albertellis-somatic.md`, `thk-bischler.md` — غير موجود، سُجّلا في quarantine-spark.md. الأول استخدام محظور لـslug ألبرت إليس المؤسس لكتابة سيرة شخص آخر (قاعدة 6).

## متوقف عنده (لرئيس التحرير)
- `thk-lvdpost.md`: القيد الجديد (فضح مبالغات فان دير بوست في سيرته) مادة حساسة تستحق مراجعة قبل الترقية.
- `thk-adelaserna.md`: يحتاج تحقق بحث خارجي فعلي (خارج معرفة النموذج الداخلية) قبل حسم القرار بين موثّق/غير موجود.
- `thk-albertellis-somatic.md`: يُنصح بفحص هل أي ملف تاني يشير لهذا الـslug في `related` قبل حسم مصيره النهائي.

## الملفات
content/ar/thinkers/thk-jadler.md
content/ar/thinkers/thk-bakewell.md
content/ar/thinkers/thk-binswanger.md
content/ar/thinkers/thk-bischler.md
content/ar/thinkers/thk-dbecker.md
content/ar/thinkers/thk-adelaserna.md
content/ar/thinkers/thk-berdyaev.md
content/ar/thinkers/thk-glover.md
content/ar/thinkers/thk-hpalmer.md
content/ar/thinkers/thk-albertellis-somatic.md
content/ar/thinkers/thk-lvdpost.md
content/ar/thinkers/thk-busch.md
content/ar/thinkers/thk-alam.md
content/ar/thinkers/thk-cooper.md
content/ar/thinkers/thk-hammarskjold.md
