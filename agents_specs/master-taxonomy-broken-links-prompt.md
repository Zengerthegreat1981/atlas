# متابعة — إصلاح 27 رابط معلَّق من دفعة التحليل النفسي/اليونغية

انسخ من هنا للأسفل وابعته للنموذج اللي شغّل مهمة الـ Master Taxonomy.

---

فحصت كل ملفات `content/ar/drafts/` بعد آخر دفعة (328 ملف) بنفس الـ parser الحقيقي بتاع
`build_atlas.py`، ولقيت **27 رابط `related` معلَّق فعلياً** — بيشاوروا على IDs مش موجودة لا في
المحتوى المعتمد ولا في أي مسودة تانية. التقرير اللي بعتّه قال "0% روابط مكسورة"، وده مش دقيق.

## القايمة الكاملة (ملف المصدر → id المفقود، النوع المتوقع)

- `thk-dkalsched` → `con-trauma` (الصدمة النفسية)
- `thk-dtacey` → `con-post-christian` (ما بعد المسيحية)
- `thk-edinger` → `con-ego-self` (محور الأنا–الذات)
- `thk-ejung` → `con-anima-animus` (الأنيما والأنيموس)
- `thk-ejung` → `con-grail` (أسطورة الكأس المقدسة)
- `thk-fordham` → `con-primary-self` (الذات الأولية)
- `thk-giegerich` → `con-soul` (النفس)
- `thk-hillman` → `con-soul` (النفس)
- `thk-hsolomon` → `thk-kast` (فيرينا كاست — **مفكرة**، مش مفهوم)
- `thk-hsolomon` → `con-ethics` (الأخلاق في التحليلية)
- `thk-jaffe` → `con-parapsychology` (ما وراء علم النفس)
- `thk-jbeebe` → `con-psychological-type` (الأنماط النفسية)
- `thk-jhenderson` → `con-cultural-unconscious` (اللاوعي الثقافي)
- `thk-jhollis` → `con-midlife` (مرحلة منتصف العمر)
- `thk-mwoodman` → `con-feminine-principle` (المبدأ الأنثوي)
- `thk-neumann` → `con-great-mother` (الأم الكبرى/الأركيتيب)
- `thk-neumann` → `con-ego-self` (محور الأنا–الذات — نفس id المطلوب من edinger فوق، دمجهم في نفس الملف)
- `thk-nisesilveira` → `con-psychiatric-reform` (الإصلاح النفسي)
- `thk-rjohnson` → `thk-kunkel` (فريتز كونكل — **مفكر**، مش مفهوم)
- `thk-rstein` → `con-dream-interpretation` (تفسير الأحلام)
- `thk-samuels` → `con-political-psyche` (النفس السياسية)
- `thk-spielrein` → `con-death-instinct` (غريزة الموت)
- `thk-tkirsch` → `thk-jkirsch` (جيمس كيرش — **مفكر**، مش مفهوم)
- `thk-tkirsch` → `con-international-jungian` (التحليلية الدولية)
- `thk-tmoore` → `con-soul` (النفس — نفس id المطلوب من giegerich/hillman فوق، دمجهم في نفس الملف)
- `thk-twolff` → `con-anima-animus` (الأنيما والأنيموس — نفس id المطلوب من ejung فوق)
- `thk-vkast` → `con-grief` (الحزن)

## المطلوب

1. لكل id فريد في القايمة فوق (لاحظ `con-soul`، `con-anima-animus`، و`con-ego-self` كل واحد مطلوب من أكتر من ملف مصدر — يُكتب **مرة واحدة بس**، بيربط لكل المصادر اللي طلبته)، افتح كل ملفات المصدر اللي بتشاور عليه من `content/ar/drafts/thinkers/`، واكتب المسودة **حصراً** من المعلومات الموجودة فيهم (زي ما عملنا مع بلانكنبورغ وشنايدمان قبل كده — بلا اختراع من معرفة عامة).
2. النوع: المفاهيم (`con-`) تروح `content/ar/drafts/concepts/`، المفكرين (`thk-kast`, `thk-kunkel`, `thk-jkirsch`) يروحوا `content/ar/drafts/thinkers/` بنفس قالب البريف الكامل (مش مفهوم مختصر).
3. **Reverse engineering إلزامي**: بعد ما تكتب كل ملف، ارجع لكل ملف من ملفات المصدر (زي `thk-ejung.md`) وتأكد إن الـ id بقى صحيح فعلاً (يعني الملف الجديد موجود بنفس الاسم بالظبط).
4. لما تخلص، **افحص بنفسك فعلياً** (اقرأ كل ملف كتبته، تأكد من الصيغة، وابحث تاني عن أي `related` جديد كتبته يشاور على حاجة لسه مش موجودة) قبل ما تقول "خلصت" — المرة اللي فاتت التقرير كان فيه ادّعاء غير دقيق، فمرة دي وضّح بالتحديد إزاي اتأكدت (مش بس "تم الفحص").
5. رد في الآخر بقايمة أسماء الملفات الفعلية اللي كتبتها (مسارها الكامل)، وعدد أي روابط لسه معلَّقة لو فيه (0 المفروض).
