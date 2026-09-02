# Task 3.15
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-gaudapada..thk-gleonard.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-gcivitarese، thk-gilgamesh)
- **حجر صحي محتمل غير محسوم: thk-gdiaz** — جزء من عنقود ثلاثي (مع thk-epaz المحجور فعلاً وthk-gadamoli غير المفحوص) بلا أثر خارجي مستقل — تُرك "غامضاً" حسب الصلاحية (Task 2)، لكن يستحق حسماً.
- **نمط خطير مكتشف: روابط أُزيلت خطأً في مراجعات سابقة رغم كونها صحيحة فعلياً** — thk-gbond (thk-brapp/تشارلز راب) وthk-gcecchin (thk-boscolo/لويجي بوسكولو) كلاهما كان يحمل ملاحظة "أُزيل لعدم التحقق" رغم أن الشخصين معتمدان وحقيقيان تماماً — أُعيد الرابطان. **يستحق مراجعة رئيس التحرير لسبب هذا النمط في مراجعات سابقة.**
- **ازدواج slug مؤكد ثالث: thk-gendlin ↔ thk-egendlin** — نفس الشخص (يوجين جندلين) بملفين معتمدين معاً.
- **نسبة خاطئة مصححة**: thk-gendlin كان يُنسب له تقنيتان ليستا له فعلياً (`tec-four-existential-dimensions-healing` أقرب لفان ديورزن، و`tec-process-experiential-tasks` تقنية غرينبرغ/EFT) — حُذفتا.
- **محتوى مفبرك/تواريخ خاطئة: thk-george-herbert-mead** — عنوان كتاب مختلَق بالكامل ("Mind, Self and the Cosmos 1934")، تاريخ محاضرة خاطئ (1924→1926)، وصف خاطئ لملحق داخل كتاب كأنه كتاب مستقل، واسم شخص مشوَّه (Manfred→Manford Kuhn).
- **رابط بمعرّف خاطئ لشخص مختلف تماماً: thk-glasser** — رابط `thk-lieberman` كان بعنوان "أليسي ليبرمان" لكن الـslug الحقيقي لشخص آخر (أليسيا ف. ليبرمان، باحثة رضّع لا علاقة لها بغلاسر) — حُذف.
- **قرار حساس محتمل نظامي: thk-ggurdjieff/thk-glasser/thk-gferri** — نمط روابط `related` قوالبية متكررة عبر ملفات إنسانية متعددة بلا أي تحقق فعلي من العلاقة (thk-gferri وحده كان فيه 12 من 14 رابطاً بلا تبرير نصي) — يستحق فحصاً منهجياً شاملاً.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير (gbond→br-case-management، ghoffman→tec-circle-of-security، gbateson→tec-strategic-family-therapy، gdiamond→br-abft، georgeatwood→br-intersubjective-psychoanalysis، gferri→br-vegetotherapy-orgonomy، glasser→br-glasser-reality-therapy). حالات بلا slug مطابق (ggurdjieff [الطريق الرابع]، gbach/gleonard [حركة اللقاء]، gcecchin [ميلانو]، ge-moore [فلسفة كامبريدج التحليلية]، gengel [النموذج الحيوي-النفسي-الاجتماعي]، george-lakoff [اللسانيات المعرفية]، giorgio-agamben [الفلسفة الإيطالية المعاصرة]، gjohanson [هاكومي]، gcraig [TFT]) أُفرغت مع تسجيل طلبات جديدة.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.
- عدة ملفات كانت تفتقر لقسم `## المصادر` — أُضيفت مصادر أولية حقيقية (gaudapada، gbach، gcombs، gbond، gcecchin).
- **وفاة حديثة غير مسجلة: thk-gcraig (غاري كريغ، مؤسس EFT/التنصيل)** — توفي فعلياً يناير 2026، كان `active_end` يقول "مستمر".

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{gaudapada,gbach,gbateson,gbond,gcecchin,gcombs,gcraig,gdiamond,gdiaz,ge-hong,ge-moore,gebsattel,gendlin,gengel,george-herbert-mead,george-lakoff,georgeatwood,gferri,gfrege,ggurdjieff,ghiyath-al-din-dashtaki,ghoffman,giegerich,gilligan,giordano-bruno,giorgi,giorgio-agamben,gjohanson,gklerman,gladwell,glandreth,glasser,gleonard}.md
→ ✅ 33 ملف — صفر مخالفات آلية (thk-gcivitarese وthk-gilgamesh سليمان تماماً، بلا مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن (أو إضافة سبب موثّق حين كان ممكناً بدل الحذف)، وإصلاح تعارضات id/title.

## متوقف عنده (لرئيس التحرير)
- **thk-gdiaz**: عنقود غير موثّق (مع epaz المحجور وgadamoli غير المفحوص) — يستحق حسماً.
- **نمط "روابط حُذفت خطأً في مراجعات سابقة رغم صحتها"**: مكتشف في gbond وgcecchin — عكس نمط "gaps تدّعي حذف رابط لسه موجود" المعتاد؛ هنا الحذف نفسه كان الخطأ. يستحق تحقيقاً في سبب حدوثه بمراجعات سابقة.
- **thk-gendlin ↔ thk-egendlin**: ازدواج مؤكد يحتاج دمجاً.
- **thk-gferri**: 12 من 14 رابطاً حُذفت لعدم التبرير — هل هي شبكة SEOr حقيقية تحتاج توثيقاً نصياً، أم كانت نسخاً عشوائياً؟
- **thk-georgeatwood/thk-dorange/thk-lorange**: ارتباك بين slugين لاسم "أورانج" (دومينيك مقابل دونا) يحتاج حسماً على مستوى الملفات المصدر.
- **thk-gcraig**: وفاته (يناير 2026) يستحق تحققاً من ملفات أخرى قد تشير له كـ"نشط".
- **thk-giegerich**: تصنيف تحت `sch-psychoanalysis` (اتساقاً مع يونغ) أم `br-jungian` الأدق؟

## الملفات
content/ar/thinkers/thk-gaudapada.md
content/ar/thinkers/thk-gbach.md
content/ar/thinkers/thk-gbateson.md
content/ar/thinkers/thk-gbond.md
content/ar/thinkers/thk-gcecchin.md
content/ar/thinkers/thk-gcivitarese.md
content/ar/thinkers/thk-gcombs.md
content/ar/thinkers/thk-gcraig.md
content/ar/thinkers/thk-gdiamond.md
content/ar/thinkers/thk-gdiaz.md
content/ar/thinkers/thk-ge-hong.md
content/ar/thinkers/thk-ge-moore.md
content/ar/thinkers/thk-gebsattel.md
content/ar/thinkers/thk-gendlin.md
content/ar/thinkers/thk-gengel.md
content/ar/thinkers/thk-george-herbert-mead.md
content/ar/thinkers/thk-george-lakoff.md
content/ar/thinkers/thk-georgeatwood.md
content/ar/thinkers/thk-gferri.md
content/ar/thinkers/thk-gfrege.md
content/ar/thinkers/thk-ggurdjieff.md
content/ar/thinkers/thk-ghiyath-al-din-dashtaki.md
content/ar/thinkers/thk-ghoffman.md
content/ar/thinkers/thk-giegerich.md
content/ar/thinkers/thk-gilgamesh.md
content/ar/thinkers/thk-gilligan.md
content/ar/thinkers/thk-giordano-bruno.md
content/ar/thinkers/thk-giorgi.md
content/ar/thinkers/thk-giorgio-agamben.md
content/ar/thinkers/thk-gjohanson.md
content/ar/thinkers/thk-gklerman.md
content/ar/thinkers/thk-gladwell.md
content/ar/thinkers/thk-glandreth.md
content/ar/thinkers/thk-glasser.md
content/ar/thinkers/thk-gleonard.md
