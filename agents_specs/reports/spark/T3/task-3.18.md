# Task 3.18
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-hghoffman..thk-hu-shi.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-hputnam، thk-holmes-rolston)
- **حجر صحي جديد ×2**: `thk-hhart` (الملف نفسه يعترف بعدم وجود منظّر بهذا الاسم؛ على الأرجح تحريف لهنري بينسكِر — شخص مختلف)، و`thk-hkoprulu` (لا أثر خارجي لعالم نفس تركي بهذا الاسم، وادعاء تأسيسي خاطئ لـIAIP).
- **فبركة محتوى واسعة مكتشفة: thk-hohagen** — الاسم الكامل خاطئ (فريدريش↔فريتز)، ومفهوم "العلاج البرنامجاتي" وشراكة "بيليندا بوسل" و"نموذج لوبيك" — جميعها غير قابلة للتحقق إطلاقاً رغم بحث خارجي مباشر. أُعيد كتابة الملف بمادة حقيقية بديلة (دراسة 1994، عيادة الوسواس القهري، مشاركة EVIDENT). **يستحق مراجعة رئيس التحرير — حجم الحذف يتجاوز التدقيق القرائي العادي.**
- **خطأ تواريخ جوهري: thk-hstein (هنري ت. ستاين)** — الملف يذكره كحيّ ("مستمر") بينما توفي فعلياً 2024.
- **ازدواج slug خامس مؤكَّد: thk-hlkelly ↔ thk-helen-lakelly-hunt** — نفس الشخص (هيلين لاكيلي هانت) تحت slugين، أحدهما (helen-lakelly-hunt) موثّق حديثاً في 3.17 بفبركة مكتشفة. **يحتاج دمجاً عاجلاً.**
- **رابط عكسي بمعرّف خاطئ**: thk-hmarkman كان يربط "جوليا غوتمان" بينما الاسم الحقيقي "جولي شوارتز غوتمان".
- **خطأ نسبة كتاب**: thk-hjguilhardi كان يربط شخصين محجورين فعلياً (thk-m-amatos وthk-rkerbauy) حسب quarantine-minimax.md.
- **تصنيف بنيوي خاطئ مصحح**: thk-hresneck (كانت مصنَّفة تحت Somatic Experiencing بينما الملف نفسه يؤكد انتماءها للتحليل الطاقي/IIBA — صُححت لـbr-bioenergetic-analysis)، thk-hschlesinger (كانت "تنويم تحليلي" رغم أن gaps تنفي هذا وتؤكد أنه محلل كلاسيكي — أسماء "جيدو" و"ماندر روس" غير قابلة للتحقق حُذفت كمفبركة محتملة).
- **رابط محجور لا يزال ظاهراً رغم اعتراف الملف بحذفه**: thk-hliddle (thk-brosen محجور فعلياً)، thk-hsteadman (عكس النمط: gaps تدّعي حذف رابط صحيح فعلياً — أُعيد).
- **نمط false positive في فحص الجنس مستمر**: thk-hsolomon (هستر سولومون، رئيسة IAAP سابقاً) — نفس مشكلة heimann/helen-lakelly-hunt في 3.17، تُركت الصيغة المؤنثة الصحيحة.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير (hghoffman→br-vr-therapy، hhendrix→4 تصحيحات، hkaplan→br-sex-therapy، hmosak→br-adlerian، hmurray→sch-humanistic، hobbes→sch-social-contract، hohagen→sch-cbt، hstrupp→br-cyclical-psychodynamics، hsteadman→br-therapeutic-risk-assessment). حالات بلا slug مطابق (hgoolishian [نفس فجوة handerson]، hkwiatkowska [علاج بالفن]، hliddle [MDFT]، hmarkman [بلا edges نهائياً]، hstein [أدلرية مخصصة]) أُفرغت مع تسجيل طلبات.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.
- عدة ملفات كانت تفتقر لقسم `## المصادر` — أُضيفت مصادر حقيقية (hohagen، holderlin، holzhey، hountondji، hstrupp، hu-shi، hsteadman).

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{hghoffman,hgoolishian,hhendrix,hierocles-stoic,hillman,hipparchia,hippias,hjguilhardi,hkaplan,hkawai,hkwiatkowska,hliddle,hmarkman,hmosak,hmurray,hobbes,hoffman,hohagen,holderlin,holzhey,hountondji,hresneck,hsampson,hschlesinger,hsolomon,hspotnitz,hsteadman,hstein,hstrupp,hu-shi}.md
→ ✅ 29 ملف — مخالفتان فقط في hsolomon مؤكَّدتان false positive (تُركت الصيغة المؤنثة الصحيحة عمداً).
2 ملفان سليمان تماماً بلا مسودة: thk-hputnam، thk-holmes-rolston. thk-hhart وthk-hkoprulu حُجرا بدل كتابة مسودة. thk-hlkelly لم تُكتب له مسودة تفادياً لتكريس الازدواج مع helen-lakelly-hunt.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-hohagen**: فبركة محتوى واسعة أُعيد كتابتها بالكامل تقريباً — يستحق مراجعة بشرية شاملة قبل الترقية.
- **thk-hlkelly ↔ thk-helen-lakelly-hunt**: ازدواج مؤكد يحتاج دمجاً عاجلاً (النسخة الأحدث تحمل فبركة مكتشفة يجب تطبيقها بعد الدمج).
- **thk-hstein**: تصحيح وفاته (2024) أولوية عالية؛ وتصنيفه الأدلري معلَّق مؤقتاً على `sch-psychoanalysis` بانتظار slug مخصص (حتى thk-adler نفسه يفتقره).
- **thk-hhart وthk-hkoprulu**: حجران جديدان — يستحقان تسجيل ملف بديل بslug جديد (بينسكِر لحالة الأولى) بدل إعادة تدوير الslug.
- **thk-hsolomon**: false positive إضافي في فحص preflight_check.py للجنس — نمط متكرر عبر عدة دفعات، يستحق تحسين الـheuristic.

## الملفات
content/ar/thinkers/thk-hghoffman.md
content/ar/thinkers/thk-hgoolishian.md
content/ar/thinkers/thk-hhart.md
content/ar/thinkers/thk-hhendrix.md
content/ar/thinkers/thk-hierocles-stoic.md
content/ar/thinkers/thk-hillman.md
content/ar/thinkers/thk-hipparchia.md
content/ar/thinkers/thk-hippias.md
content/ar/thinkers/thk-hjguilhardi.md
content/ar/thinkers/thk-hkaplan.md
content/ar/thinkers/thk-hkawai.md
content/ar/thinkers/thk-hkoprulu.md
content/ar/thinkers/thk-hkwiatkowska.md
content/ar/thinkers/thk-hliddle.md
content/ar/thinkers/thk-hlkelly.md
content/ar/thinkers/thk-hmarkman.md
content/ar/thinkers/thk-hmosak.md
content/ar/thinkers/thk-hmurray.md
content/ar/thinkers/thk-hobbes.md
content/ar/thinkers/thk-hoffman.md
content/ar/thinkers/thk-hohagen.md
content/ar/thinkers/thk-holderlin.md
content/ar/thinkers/thk-holmes-rolston.md
content/ar/thinkers/thk-holzhey.md
content/ar/thinkers/thk-hountondji.md
content/ar/thinkers/thk-hputnam.md
content/ar/thinkers/thk-hresneck.md
content/ar/thinkers/thk-hsampson.md
content/ar/thinkers/thk-hschlesinger.md
content/ar/thinkers/thk-hsolomon.md
content/ar/thinkers/thk-hspotnitz.md
content/ar/thinkers/thk-hsteadman.md
content/ar/thinkers/thk-hstein.md
content/ar/thinkers/thk-hstrupp.md
content/ar/thinkers/thk-hu-shi.md
