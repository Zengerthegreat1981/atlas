# Task 3.7
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-cesaire، thk-charvaka)
- **أخطاء هوية/جنسية جسيمة**: `thk-carlos-castaneda` كان يزعم أصلاً "برازيلياً" له بينما هو بيروفي موثّق (لا سند لادعاء البرازيل إطلاقاً).
- **محتوى مختلَق بالكامل حُذف**:
  - `thk-cdouglas`: كتاب كامل "The E.T.A. Hoffmann–Jung Connection (2008)" لا وجود له، ووصفها كـ"محررة سابقة لمجلة" غير مؤكد — أُعيد بناء سيرتها من الصفر بأعمالها الحقيقية فقط.
  - `thk-charles-swenson`: قصة كاملة عن انتقاله للبرازيل وتطوير "DBT-BR" وكتاب 2020 — لا أثر لها في أي مصدر، حُذفت بالكامل واستُبدلت بسيرة موثقة (هارفارد→ييل→كورنيل→UMass، شريك تأسيس ISITDBT مع لينهان 1996).
  - `thk-cheikh-anta-diop`: استشهادات دقيقة الشكل («Emmanuel Anati 1968»، «David Brewer 1991») غير قابلة للتحقق تحمل ملامح اختلاق مصادر — حُذفت.
- **استحالات زمنية مكتشفة**: `thk-cheng-yi` (زعم تلمذة تشو هسي المباشرة عليه رغم أن تشو هسي وُلد بعد وفاته بـ23 عاماً).
- **أخطاء نسبة موثّقة بأدلة داخلية**: `thk-carta` (عنوان كتاب "2026" مختلَق زمنياً)، `thk-caruso` (اسم مؤسسة خاطئ، تواريخ نشاط خاطئة)، `thk-ccowan` (برنامج "Bringing Baby Home" نُسب له خطأً، والصحيح لعائلة غوتمان)، `thk-charles-glisson` (نُسب كمطوّر MST بينما هو مطوّر نموذج ARC المرتبط بها)، `thk-charlesfaulkner` (خلط كامل بين إطاري Psycho-Cybernetics وNLP، ورابط لشخص محجور في quarantine-minimax.md).
- **تصحيحات تواريخ**: `thk-camus` (يقطع 9 سنوات من نشاطه)، `thk-cannon`، `thk-charcot` (كان يعكس فقط سنتي محاضرة أخيرة بدل مسيرته الكاملة 1862-1893)، `thk-christian-wolff` (3 سنوات بعد وفاته بلا توضيح).
- **شبكة روابط مفرطة بلا تبرير**: `thk-camus` كان فيه 16 من 20 رابطاً بلا أي ذكر في المتن — حُذفت جميعاً.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{cameier,camus,cannon,capriles,carlos-castaneda,carnegie,carta,caruso,cassirer,castillejo,cbrenner,ccastoriadis,ccowan,cdouglas,cferster,cfischer,cgrof,chaim-perelman,chandrakirti,charcot,charles-duhigg,charles-glisson,charles-grob,charles-swenson,charlesfaulkner,charlestaylor,cheikh-anta-diop,cheng-hao,cheng-yi,chodorow,christian-wolff,chrysippus,ci-lewis}.md
→ ✅ 33 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي، حذف روابط `related` بلا سبب مذكور بالمتن.

## متوقف عنده (لرئيس التحرير)
- **thk-cdouglas / thk-charles-swenson**: أكبر تصحيحين في الدفعة (حذف محتوى مختلَق بالكامل واستبداله بسيرة موثقة من الصفر) — يستحقان أولوية عالية في المراجعة البشرية.
- **thk-carlos-castaneda**: خطأ "بيرو مقابل البرازيل" كان سيمر لولا التدقيق بترتيب الهوية أولاً.
- **thk-charlesfaulkner**: تحويل تصنيفه الكامل من Psycho-Cybernetics إلى NLP قرار جوهري (crumb وedges.belongs_to) مبني على أدلة داخل الأطلس نفسه (وجود thk-rbandler/thk-rdilts وحجر thk-maxwell-maltz في quarantine-minimax.md) — يستحق تأكيداً قبل الترقية.
- **thk-charcot**: `edges.belongs_to → sch-existential-therapy` يتناقض مع قسم «القيد» في المتن نفسه الذي ينفي عضويته — تُرك كما هو مع توثيق التناقض، قرار مفتوح.
- **thk-chaim-perelman**: لا يوجد slug لـ"نظرية الحجاج" (`sch-argumentation-theory` مقترح) — الملف بلا `belongs_to` حتى يُبتّ.
- **thk-cheikh-anta-diop**: حذف استشهادات نقدية (Anati/Brewer/Rutgers) أفقر القسم النقدي — لو فيه مصدر يوثقها يمكن إعادتها بدقة.

## الملفات
content/ar/thinkers/thk-cameier.md
content/ar/thinkers/thk-camus.md
content/ar/thinkers/thk-cannon.md
content/ar/thinkers/thk-capriles.md
content/ar/thinkers/thk-carlos-castaneda.md
content/ar/thinkers/thk-carnegie.md
content/ar/thinkers/thk-carta.md
content/ar/thinkers/thk-caruso.md
content/ar/thinkers/thk-cassirer.md
content/ar/thinkers/thk-castillejo.md
content/ar/thinkers/thk-cbrenner.md
content/ar/thinkers/thk-ccastoriadis.md
content/ar/thinkers/thk-ccowan.md
content/ar/thinkers/thk-cdouglas.md
content/ar/thinkers/thk-cesaire.md
content/ar/thinkers/thk-cferster.md
content/ar/thinkers/thk-cfischer.md
content/ar/thinkers/thk-cgrof.md
content/ar/thinkers/thk-chaim-perelman.md
content/ar/thinkers/thk-chandrakirti.md
content/ar/thinkers/thk-charcot.md
content/ar/thinkers/thk-charles-duhigg.md
content/ar/thinkers/thk-charles-glisson.md
content/ar/thinkers/thk-charles-grob.md
content/ar/thinkers/thk-charles-swenson.md
content/ar/thinkers/thk-charlesfaulkner.md
content/ar/thinkers/thk-charlestaylor.md
content/ar/thinkers/thk-charvaka.md
content/ar/thinkers/thk-cheikh-anta-diop.md
content/ar/thinkers/thk-cheng-hao.md
content/ar/thinkers/thk-cheng-yi.md
content/ar/thinkers/thk-chodorow.md
content/ar/thinkers/thk-christian-wolff.md
content/ar/thinkers/thk-chrysippus.md
content/ar/thinkers/thk-ci-lewis.md
