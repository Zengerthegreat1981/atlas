# Task 3.27
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-lacan..thk-lhecker (شامل لاكان ولايبنتز وليفيناس ولانغر).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 1 / 35 (thk-laozi)
- **حجر صحي جديد: thk-lbarrett** — الملف كان ينسب لشخص مختلَق ("لورنس بارِت") تأليف كتاب "The Homosexual Matrix" (1996) في إطار معادٍ للمثلية؛ الكتاب الحقيقي مؤلفه C.A. Tripp (1975)، وهو عمل مؤيّد لا معادٍ، ولا صلة له بحركة Exodus International المزعومة.
- **ازدواج مؤكَّد ثانٍ: thk-leon-festinger ↔ thk-lfestinger** — نفس الشخص (ليون فستنغر) بملفين، أحدهما (leon-festinger) أضعف ويحمل أخطاء إضافية (نص روسي مشوَّه، اسم خاطئ "إلز إليس" بدل "ألبرت إليس"، ادعاء تأسيس غير موثّق).
- **خطأ نسبة جسيم مع اسم مؤلف مشارك مفبرك بالكامل: thk-ldavidson** — كتاب "Mental Health, Social Mirror" (2007) كان منسوباً له مع مؤلف مشارك مختلَق "N. Killion"؛ المؤلفون الحقيقيون Avison وMcLeod وPescosolido.
- **خطأ نسبة وتاريخ جسيم: thk-lebovici** — كتابه الأساسي كان منسوباً خطأً لميشيل فان (thk-fain) بتاريخ 1964؛ الشريك الحقيقي سيرج ستوليرو، والكتاب صدر 1983.
- **خطأ هوية/تأسيس جسيم: thk-leighmccullers** — كان يُنسب لها خطأً تأسيس AEDP (المؤسِّسة الحقيقية ديانا فوشا)؛ الشخصية الحقيقية مؤسِّسة نموذج منفصل تماماً (Affect Phobia Therapy). كذلك تواريخها ومؤسستها كانتا خاطئتين بالكامل.
- **خطأ هوية/جنس: thk-lgreenberg** — رابط "روبرت رايس" (ذكر) كان يجب أن يكون لورا إن. رايس (أنثى، المؤلفة المشاركة الفعلية)؛ ادعاء غير موثَّق بزواج غرينبرغ من سوزان جونسون؛ فقرة مؤثرين مختلَقة بالكامل (أسماء غير معروفة في أدبيات EFT) حُذفت.
- **هوية مشكوك فيها بقوة (مؤكَّدة سابقاً): thk-lhecker** — لا توثيق لباحث بهذا الاسم في أدبيات IPT؛ اسم جون ماركويتز كان مكتوباً خطأً "جيمس".
- **محتوى مختلَق حُذف**: thk-laplanche (علاقة مزعومة مع "جون ستولورتن" غير موجود)، thk-lazarsfeld (ادعاء أسبقية مفهوم "الجندر كأداء اجتماعي" بعقدين قبل بتلر)، thk-laron (كتاب "نحو العلائقي الإسلامي" غير موثّق)، thk-lewis-mumford (تأثير مباشر مختلَق على غوفمان وهايدجر عبر كتاب بعنوان غير موجود).
- **وفاة حديثة غير مسجلة: thk-lchodorow** — توفيت فعلياً 14 أكتوبر 2025، الملف كان يذكرها "مستمر".
- **قسمان مكرَّران بعنوان "## القيد" اكتُشفا ودُمجا**: thk-langer، thk-laclau، thk-lainentralgo (خلل بنيوي متكرر).
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{lacan,lachmann,laclau,lagache,lainentralgo,laing,langdridge,langer,langle,laplanche,laron,lazarsfeld,lazarus,lbertalanffy,lbrown,lchodorow,ldavidson,lebovici,leibniz,leifer,leighmccullers,leijssen,leon-festinger,leopold,leopoldo-zea,leucippus,levenson,levinas,lewis-mumford,lfestinger,lfinlay,lgreenberg,lhecker}.md
→ ✅ 33 ملف — صفر مخالفات آلية. thk-laozi سليم تماماً بلا مسودة، thk-lbarrett حُجر.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، ودمج أقسام "القيد" المكرَّرة.

## متوقف عنده (لرئيس التحرير)
- **thk-lbarrett**: يستحق حذفاً نهائياً — انتحال هوية كتاب وشخص حقيقيين.
- **thk-leon-festinger ↔ thk-lfestinger**: ازدواج مؤكد يحتاج دمجاً.
- **thk-ldavidson وthk-lebovici**: أخطاء نسبة مع أسماء مؤلفين مشاركين مفبركة بالكامل — نمط يستحق فحصاً موسّعاً.
- **thk-leighmccullers**: خطأ تأسيس جسيم (AEDP) مع تصنيف مؤقت (sch-psychoanalysis) بانتظار slug صحيح.
- **thk-lhecker**: يستحق حجراً إن لم يوجد توثيق إضافي.
- **thk-lchodorow**: تصحيح وفاتها (أكتوبر 2025) أولوية عالية.
- **طلبات تصنيف متعددة**: ما بعد الماركسية (لاكلاو)، فلسفة الرمز والجماليات (لانغر)، Affect Phobia Therapy (leighmccullers)، ستوليرو (lebovici).

## الملفات
content/ar/thinkers/thk-lacan.md
content/ar/thinkers/thk-lachmann.md
content/ar/thinkers/thk-laclau.md
content/ar/thinkers/thk-lagache.md
content/ar/thinkers/thk-lainentralgo.md
content/ar/thinkers/thk-laing.md
content/ar/thinkers/thk-langdridge.md
content/ar/thinkers/thk-langer.md
content/ar/thinkers/thk-langle.md
content/ar/thinkers/thk-laozi.md
content/ar/thinkers/thk-laplanche.md
content/ar/thinkers/thk-laron.md
content/ar/thinkers/thk-lazarsfeld.md
content/ar/thinkers/thk-lazarus.md
content/ar/thinkers/thk-lbarrett.md
content/ar/thinkers/thk-lbertalanffy.md
content/ar/thinkers/thk-lbrown.md
content/ar/thinkers/thk-lchodorow.md
content/ar/thinkers/thk-ldavidson.md
content/ar/thinkers/thk-lebovici.md
content/ar/thinkers/thk-leibniz.md
content/ar/thinkers/thk-leifer.md
content/ar/thinkers/thk-leighmccullers.md
content/ar/thinkers/thk-leijssen.md
content/ar/thinkers/thk-leon-festinger.md
content/ar/thinkers/thk-leopold.md
content/ar/thinkers/thk-leopoldo-zea.md
content/ar/thinkers/thk-leucippus.md
content/ar/thinkers/thk-levenson.md
content/ar/thinkers/thk-levinas.md
content/ar/thinkers/thk-lewis-mumford.md
content/ar/thinkers/thk-lfestinger.md
content/ar/thinkers/thk-lfinlay.md
content/ar/thinkers/thk-lgreenberg.md
content/ar/thinkers/thk-lhecker.md
