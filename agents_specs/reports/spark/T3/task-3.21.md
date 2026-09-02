# Task 3.21
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-jbanmen..thk-jgebser.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 1 / 35 (thk-jfreedman تقريباً سليم، أخطاء طفيفة فقط في الباقي)
- **أخطر اكتشاف: thk-jenny-odell** — تلفيق واسع في الملف المعتمد: تاريخ/مكان ميلاد خاطئ، مشروع فني مختلَق بالكامل ("مكتبة السكينة" بدل Bureau of Suspended Objects الحقيقي)، ادعاءات استشهاد تايلور سويفت ولورد وبيلي آيليش بها، وادعاء تأثيرها على Extinction Rebellion — جميعها مفبركة. أُعيد كتابة الملف بالكامل بمادة موثّقة فقط.
- **شخصية مشكوك فيها بقوة: thk-jcawley** — بحث مكثّف لم يجد أي أثر مستقل للشخص أو البرنامج المزعوم "PREPP" أو الورقة العلمية المنسوبة. **يستحق قراراً صريحاً من رئيس التحرير: حجر أم حذف نهائي.**
- **ازدواج مؤكد + اسم مختلَق مكتشف: thk-jeberenz ↔ thk-dolweus** — كلاهما لنفس الشخص (دان أولڤيوس)، لكن الأخطر أن thk-dolweus يسمّي هذا الملف باسم مختلَق تماماً "وولتر جيمس أَولِس". **يحتاج دمجاً وتصحيحاً عاجلين.**
- **تعارض هوية سابق مؤكَّد ومُطابَق**: thk-jflax وthk-jgebser (من مجموعتين مختلفتين) كلاهما أشار لتضارب هوية موجود مسبقاً في thk-jmitchell (المعتمد يصفها "جوليا ميتشِل" أمريكية، لكن مسودة مصححة موجودة فعلاً تحت نفس الslug تصفها بشكل صحيح "جوليت ميتشل" بريطانية) — **مسودة الحل جاهزة، تحتاج فقط ترقية.**
- **هوية شخص ثانٍ متنازع عليها**: thk-jbiko يربط thk-amncube، لكن preflight اكتشف أن النسخة المعتمدة والمسودة الموازية تصفان شخصين مختلفين تماماً بنفس الـslug — يحتاج قراراً منفصلاً.
- **نمط "gaps تدّعي حذف رابط لسه موجود" استمر بشدة**: thk-jbeck (denise davis)، thk-jcgibbs (krischer)، thk-jchamberlin (dfisher)، thk-jeffrey-zeig (4 روابط).
- **نمط false positive في فحص الجنس (حالة سابعة)**: thk-jbmiller (جين بيكر ميلر) — تُركت الصيغة المؤنثة الصحيحة عمداً.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً هذه الدفعة (jbanmen→sch-systemic-family، jbaylin→br-ddp، jbeck→sch-cbt، jbenjamin، jbiko→br-ubuntu-psychology، jbmiller→br-feminist-therapy، jboss→tec-tre، jburns→sch-cognitive-behavioral، jcameron→tec-writing-therapy، jcarlson→br-adlerian، jcgibbs→br-aggression-treatment، jchamberlin→br-peer-support، jcmcgrew→br-psychiatric-rehabilitation، jcolapinto، jdifede→br-vr-therapy، jean-baudrillard/jean-francois-lyotard→sch-postmodernism-philosophical، jfox→tec-poetry-therapy، jframo→tec-contextual-family-therapy، jferrer→sch-transpersonal). حالات بلا slug مطابق (jconstantino [DIR/Floortime]، jeberenz [علاج التنمر]، jeffrey-rediger [علم النفس الصحي]، jgebser [علم النفس التكاملي]، jenny-odell [نقد الإنتاجية]) أُفرغت مع تسجيل طلبات.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 30 ملفاً — النمط الأكثر شيوعاً هذه الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{jbanmen,jbaylin,jbeck,jbeebe,jbenjamin,jbiko,jbmiller,jboss,jburns,jcameron,jcarlson,jcawley,jcgibbs,jchamberlin,jcmcgrew,jcmilner,jcolapinto,jconstantino,jcurran,jdifede,jdollard,jean-baudrillard,jean-francois-lyotard,jeberenz,jeffrey-rediger,jeffrey-zeig,jenny-odell,jeong-yak-yong-dasan,jerry-fodor,jferrer,jflax,jfox,jframo,jfreedman,jgebser}.md
→ ✅ 34 ملف — مخالفة واحدة فقط (jbmiller) مؤكَّدة false positive وتُركت كما هي.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإصلاح تناقضات "gaps تدّعي حذف رابط لسه موجود".

## متوقف عنده (لرئيس التحرير)
- **thk-jenny-odell**: تلفيق واسع أُعيد كتابته بالكامل — أولوية عالية للمراجعة.
- **thk-jcawley**: احتمال تلفيق كامل (شخص + برنامج + مرجع) — يحتاج قرار حجر/حذف صريح.
- **thk-jeberenz ↔ thk-dolweus**: ازدواج مؤكد مع اسم مختلَق ("وولتر جيمس أوليس") — يحتاج دمجاً وتصحيحاً عاجلين.
- **thk-jmitchell**: مسودة تصحيح جاهزة (جوليت لا جوليا ميتشل) — يحتاج فقط ترقية.
- **thk-jbiko ↔ thk-amncube**: تعارض هوية بين النسخة المعتمدة والمسودة الموازية لشخصين مختلفين بنفس الslug — يحتاج قراراً منفصلاً.
- **thk-jbmiller**: false positive إضافي في فحص الجنس (الآن 7 حالات موثقة).

## الملفات
content/ar/thinkers/thk-jbanmen.md
content/ar/thinkers/thk-jbaylin.md
content/ar/thinkers/thk-jbeck.md
content/ar/thinkers/thk-jbeebe.md
content/ar/thinkers/thk-jbenjamin.md
content/ar/thinkers/thk-jbiko.md
content/ar/thinkers/thk-jbmiller.md
content/ar/thinkers/thk-jboss.md
content/ar/thinkers/thk-jburns.md
content/ar/thinkers/thk-jcameron.md
content/ar/thinkers/thk-jcarlson.md
content/ar/thinkers/thk-jcawley.md
content/ar/thinkers/thk-jcgibbs.md
content/ar/thinkers/thk-jchamberlin.md
content/ar/thinkers/thk-jcmcgrew.md
content/ar/thinkers/thk-jcmilner.md
content/ar/thinkers/thk-jcolapinto.md
content/ar/thinkers/thk-jconstantino.md
content/ar/thinkers/thk-jcurran.md
content/ar/thinkers/thk-jdifede.md
content/ar/thinkers/thk-jdollard.md
content/ar/thinkers/thk-jean-baudrillard.md
content/ar/thinkers/thk-jean-francois-lyotard.md
content/ar/thinkers/thk-jeberenz.md
content/ar/thinkers/thk-jeffrey-rediger.md
content/ar/thinkers/thk-jeffrey-zeig.md
content/ar/thinkers/thk-jenny-odell.md
content/ar/thinkers/thk-jeong-yak-yong-dasan.md
content/ar/thinkers/thk-jerry-fodor.md
content/ar/thinkers/thk-jferrer.md
content/ar/thinkers/thk-jflax.md
content/ar/thinkers/thk-jfox.md
content/ar/thinkers/thk-jframo.md
content/ar/thinkers/thk-jfreedman.md
content/ar/thinkers/thk-jgebser.md
