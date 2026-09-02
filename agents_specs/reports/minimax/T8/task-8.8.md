# Task 8.8
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40
باقي مجلد schools/ بلا ## المصادر: 130 → 90

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تجميع**

## قرارات اتخذتها
- قلّصت مصادر `sch-philosophy-of-technology.md` من 6 لـ5 (المعيار 2-5).
- تصنيف حدّي حُسم بحذر مع توثيق في `gaps` بدل قرار واثق زائف: `sch-postcolonial-philosophy.md` (حركة متعددة الأصول فعلياً — هندية عند سبيفاك/بابا، عربية عند سعيد، أفريقية-كاريبية عند فانون/مبيمبي — اختير "south-asian" كأصل التأسيس الأكاديمي مع تسجيل الحاجة لمراجعة أدق لاحقاً)، `sch-post-kyoto.md` (سجّل gap يوضح إن عدة أسماء في المسودة الأصلية — تانيغوتشي تيتسوزو، ساساكي كاتسونوري وغيرهم — غير مؤكدة كمصادر حقيقية، بلا اختراع أو حذف تعسفي خارج نطاق المهمة).
- الـsubagents صحّحوا بأنفسهم مخالفات preflight قديمة: حذف 4+ edges بنص حر (sch-neoplatonism: "أفلاطونية"/"الإسلام"، sch-neopragmatism، sch-new-materialism: "النسوية")، تصحيح تطابق title واحد (sch-new-materialism: sch-ooo)، إعادة صياغة عبارات قائمة سوداء متعددة، وتصحيح تعارض id/title واحد (sch-positive-psychology: شيلا إيبِرغ).
- توحيد/إعادة تسمية أقسام مصادر موجودة مسبقاً: sch-polyvagal-informed-therapy (## المطبوعات التأسيسية الرئيسية)، sch-positive-psychology (## المرجع الموصى)، sch-psychedelic-assisted-therapy (## المرجع الموصى للقراءة المُعمَّقة).
- ملفات فيها قسم "## المؤلفات المرجعية" (نصوص أولية) تُركت بجانب "## المصادر" الجديد كقرار صحيح: sch-patristics، sch-ockhamism/sch-occasionalism (ذُكرت بالمجموعة).
- ملف واحد اكتفى بمصدرين عمداً: `sch-process-philosophy.md` — فقط المصدران الموثقان فعلياً في المتن (وايتهيد وهارتشورن)، لا اختراع.

## متوقف عنده (لرئيس التحرير)
- لا طلبات slug جديدة هذه الدفعة (لم يظهر umbrella متكرر جديد).

## الملفات
content/ar/schools/sch-neoplatonism.md
content/ar/schools/sch-neopragmatism.md
content/ar/schools/sch-new-materialism.md
content/ar/schools/sch-psychedelic-assisted-therapy.md
content/ar/schools/sch-new-realism.md
content/ar/schools/sch-newconfucianism-modern.md
content/ar/schools/sch-nichiren.md
content/ar/schools/sch-nietzscheanism.md
content/ar/schools/sch-nongjia.md
content/ar/schools/sch-north-american-indigenous.md
content/ar/schools/sch-nyaya.md
content/ar/schools/sch-nyingma.md
content/ar/schools/sch-occasionalism.md
content/ar/schools/sch-ockhamism.md
content/ar/schools/sch-ooo.md
content/ar/schools/sch-ordinary-language.md
content/ar/schools/sch-pan-africanism.md
content/ar/schools/sch-pancasila.md
content/ar/schools/sch-patristics.md
content/ar/schools/sch-pessimism.md
content/ar/schools/sch-phenomenology-existential.md
content/ar/schools/sch-phenomenology-hermeneutic.md
content/ar/schools/sch-phenomenology-somatic.md
content/ar/schools/sch-phenomenology.md
content/ar/schools/sch-phil-mathematics.md
content/ar/schools/sch-phil-mind-analytic.md
content/ar/schools/sch-phil-science.md
content/ar/schools/sch-philosophy-of-disability.md
content/ar/schools/sch-philosophy-of-technology.md
content/ar/schools/sch-political-islam.md
content/ar/schools/sch-polyvagal-informed-therapy.md
content/ar/schools/sch-positive-psychology.md
content/ar/schools/sch-positivism-latin.md
content/ar/schools/sch-post-kyoto.md
content/ar/schools/sch-post-structuralism.md
content/ar/schools/sch-postcolonial-philosophy.md
content/ar/schools/sch-posthumanism.md
content/ar/schools/sch-postmodernism-philosophical.md
content/ar/schools/sch-pragmatism-classical.md
content/ar/schools/sch-process-philosophy.md
