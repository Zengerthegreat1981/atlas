# Task 2.1
الحالة: مكتمل
المسار: spark | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 15

## الأرقام
- موثّق (كُتبت مسودة في drafts/spark/): 8 / 15
- غير موجود (سُجّل في quarantine-spark.md، الملف الأصلي لم يُمسّ): 5 / 15
- غامض (تُرك الملف الأصلي كما هو، بلا مسودة): 2 / 15
- مخالفات preflight بعد الكتابة الأولى: 5 → بعد التصحيح اليدوي: 4 (كلها false positive موثّقة، انظر تحت)

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-lmyers.md content/ar/drafts/spark/thinkers/thk-dimen.md content/ar/drafts/spark/thinkers/thk-janethelms.md content/ar/drafts/spark/thinkers/thk-hoeller.md content/ar/drafts/spark/thinkers/thk-fakhoury.md content/ar/drafts/spark/thinkers/thk-ecraig.md content/ar/drafts/spark/thinkers/thk-jgreenspan.md content/ar/drafts/spark/thinkers/thk-batthyany.md
→ 4 مخالفات متبقية، كلها في thk-lmyers.md وthk-janethelms.md، تحققت منها يدوياً وهي false positive: الفحص الآلي عدّ كلمة `type: "مفكر"` في الـfrontmatter وكلمة "هو" العائدة على *كتاب* (مش على الشخص) كـ"مؤشرات ذكورة"، بينما متن الملفين فعلياً كله بصيغة مؤنثة صحيحة (عالمة، أستاذة، طوّرت، شرحت، عملت...). لم أُغيّر عناوين الأقسام لأن تغييرها للمذكر كان سيكون هو الخطأ الفعلي.

## قرارات اتخذتها
- `thk-lmyers.md` (ليندا جيمس مايرز) — موثّق. حذفت قسم «اقتباسات مختارة» لأنه كان يحمل جملة القائمة السوداء الحرفية «لا يوجد اقتباس مباشر موثوق متاح» (كتبها الـsubagent سهواً كمحتوى بدل حذف القسم بالكامل حسب معيار القبول §3).
- `thk-janethelms.md` (جانيت هيلمز) — نفس تصحيح قسم الاقتباسات. كما حذفت رابط `edges.belongs_to` الذي كان يستهدف نصاً حراً غير موجود كـslug ("الاستشارات متعددة الثقافات" بدل `sch-xxx`)؛ لا يوجد slug مدرسة معتمد لهذا الحقل في الأطلس حالياً، فحذفت الرابط بدل اختراع slug وسجّلت السبب في `gaps` بدل الادعاء.
- `thk-fakhoury.md` (حنا الفاخوري) — صححت `active_end` من 2000 إلى 2011 لمطابقة سنة الوفاة الموثّقة في `dates` (1914–2011)؛ القيمة السابقة (2000) كانت تولّد تحذيراً كاذباً في preflight عن سنة 2011 المذكورة بعد نهاية النشاط.
- `thk-dimen.md` (موريل ديمن) — موثّق، محللة نفسية وأنثروبولوجية أمريكية (1942–2016)، محررة مؤسِّسة لمجلة Studies in Gender and Sexuality.
- `thk-hoeller.md` (كيث هولر) — موثّق، محرر عددين موثقين عن هايدجر وسارتر وعلم النفس.
- `thk-ecraig.md` (إريك كريك) — موثّق، لكن عنوان عمله في الملف الأصلي المعتمد كان مختلفاً عن العنوان الموثّق فعلياً (راجع "متوقف عنده" تحت).
- `thk-jgreenspan.md` (جايك غرينسبان) — موثّق، صححت اسم شريكه (تيم بليكر لا "بليسي" كما في الأصل) وحذفت ادعاءً غير موثّق عن منهجية "تعديل الإيقاع".
- `thk-batthyany.md` (ألكسندر باتياني) — موثّق، مدير معهد فيكتور فرانكل بفيينا ومحرر أعماله الكاملة.
- `thk-jlchirinos.md`, `thk-klemann.md`, `thk-aklinger.md`, `thk-aulanc.md`, `thk-jnakamura.md` — غير موجود، سُجّلوا في `agents_specs/quarantine-spark.md` بالسبب. الملفات الأصلية المعتمدة لم تُمسّ في أي حالة.
- `thk-ashoham.md`, `thk-alexandra-farkas.md` — غامض، تُركا كما هما تماماً، بلا مسودة، والسبب مسجّل في `gaps`/التقرير فقط.

## متوقف عنده (لرئيس التحرير)
- `thk-ecraig.md`: الملف الأصلي المعتمد (`content/ar/thinkers/thk-ecraig.md`) ينسب لإريك كريك عملاً بعنوان "Daseinsanalysis and the Phenomenological Approach to Dreams" (1988)، لكن العمل الموثّق فعلياً هو تحريره لعدد خاص من The Humanistic Psychologist بعنوان "Psychotherapy for Freedom: The Daseinsanalytic Way in Psychology and Psychoanalysis" (1988). المسودة استخدمت العنوان الموثّق ونبّهت لهذا في `gaps`، لكن تصحيح الملف الأصلي المعتمد قرار لرئيس التحرير وحده.
- `thk-klemann.md` و`thk-aklinger.md`: ملفان معتمدان حالياً في الشجرة الرئيسية يوصى بسحبهما أو نقلهما فعلياً — الملف الأصلي لكل منهما كان يحمل بالفعل تحذير تحقّق داخلي يفيد بعدم وجود دليل مستقل على وجود الشخص. تُركا بلا تعديل لأن قاعدة "ممنوع تعديل ملف معتمد" لا تسمح لي بسحبهما.
- `thk-aulanc.md` و`thk-jnakamura.md`: ليسا ملفي شخص بل placeholder جماعي غير مفكك لعدة أفراد/مؤسسات، يعترفان صراحة في متنهما بذلك. يحتاجان قراراً تحريرياً بالتفكيك أو الحذف، خارج صلاحية Spark.
- `thk-alexandra-farkas.md`: صُنِّف "غامض" لا "غير موجود" لأنه قد يكون معالجاً حقيقياً في مجتمع Sensorimotor Psychotherapy المتخصص وغير معروف من مصادري العامة، وليس ادعاءً مفضوحاً كالحالات الأخرى — يستحق تحققاً بشرياً إضافياً قبل حجره.

## الملفات
content/ar/thinkers/thk-lmyers.md
content/ar/thinkers/thk-dimen.md
content/ar/thinkers/thk-jnakamura.md
content/ar/thinkers/thk-janethelms.md
content/ar/thinkers/thk-alexandra-farkas.md
content/ar/thinkers/thk-hoeller.md
content/ar/thinkers/thk-jlchirinos.md
content/ar/thinkers/thk-fakhoury.md
content/ar/thinkers/thk-ecraig.md
content/ar/thinkers/thk-ashoham.md
content/ar/thinkers/thk-jgreenspan.md
content/ar/thinkers/thk-klemann.md
content/ar/thinkers/thk-aklinger.md
content/ar/thinkers/thk-batthyany.md
content/ar/thinkers/thk-aulanc.md
