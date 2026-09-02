# Task 3.20
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-ipavlov..thk-jayres (شامل بافلوف وإقبال وإيريغاراي ونيوتن وجيمس وياسبرز وجلال الدين الرومي).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 5 / 35 (thk-jakhan، thk-isaac-luria، thk-jalal-al-din-rumi، thk-jaspers، وواحد آخر ضمن التفاصيل)
- **أخطر اكتشاف: thk-istansky** — اسم شخص حقيقي (إروِن ستراونسكي، طبيب نمساوي 1877–1962، صاحب مفهوم "الرنح النفسي الداخلي" 1904) لكن السيرة المعتمدة بالكامل كانت مختلَقة (مفهوم "علاج السلطوية/التبعية" وروابط مفبركة بفيرينتزي وجاي هالي وكلوي مادانس — شخصيات من عصور مختلفة تماماً). أُعيدت كتابة السيرة بالكامل بوقائع حقيقية موثّقة. **نمط أخطر من الأسماء المختلَقة الصريحة لأنه يمر فحص "هل الشخص موجود؟" بينما المحتوى نفسه كذب.**
- **خلط هوية جسيم بين شخصين بفارق 3 قرون: thk-isaac-blind** — الملف المعتمد كان يخلط بين إسحاق الأعمى القبّالي (1160-1235م) وإسحاق بن سليمان الإسرائيلي الطبيب (855-955م). أُعيدت كتابة الملف ليخص إسحاق الأعمى فقط، متسقاً مع الـslug. **يحتاج ملفاً مستقلاً جديداً لإسحاق بن سليمان الإسرائيلي — محتواه قيّم ولا ينبغي فقدانه.**
- **حجران جديدان**: thk-isquella (لا أثر في سجلات IAAP أو الدليل التشيلي؛ جزء من عنقود لاتيني-يونغي مشبوه)، thk-jaliaga (الملف نفسه يعترف بعدم توثيق وجود الشخص).
- **خطأ هوية جوهري: thk-james-allen** — نُسب تأسيس حركة "الفكر الجديد" خطأً لـ"فيلبس بروكس" (أسقف أمريكي لا صلة له) بدل فينياس باركهرست كويمبي الحقيقي.
- **كشف زائف مُصحَّح: thk-jayearly** — مذكرة gaps سابقة زعمت "تعارض هوية" بين الـslug وحقل en، تبيّن أنه لا تعارض فعلياً — حُذفت الملاحظة الخاطئة.
- **رابط محجور رغم الحجر المسبق: thk-iprogoff** — رابط thk-jbrowne محجور فعلياً منذ 2026-08-26 لكنه كان لا يزال موجوداً في related.
- **نمط false positive في فحص الجنس (مستمر، الآن حالتان جديدتان)**: thk-jacobson (إديث جاكوبسون) وthk-janina-fisher — نفس مشكلة "المعالج"/"عالم" العامة تخدع الفحص الآلي.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: قليلة نسبياً هذه الدفعة (janet→thk-charcot، jayearly→sch-ifs المباشر). حالات كثيرة بلا slug مطابق (irolf [رولفينغ]، irubenfeld [جشطالت جسدي]، iprogoff [العلاج بالكتابة]، jay-shetty [علم نفس شعبي/يقظة]، jayres [التكامل الحسي]، jamiller [لاكانية]) أُفرغت مع تسجيل طلبات — تراكم واضح لفجوة "العلاج بالكتابة" (بروغوف، بينيبيكر، كاميرون).
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{ipavlov,iplayer,iprogoff,iqbal,irigaray,irolf,irubenfeld,isaac-blind,isaac-newton,isebastiani,ishvarakrishna,isquella,istansky,iyengar,jacobson,jaffe,jahoda,jalal-al-din-dawani,james-allen,james-clear,james,jamiller,janet,janina-fisher,jaustin,jay-shetty,jayatirtha,jayearly,jayres}.md
→ ✅ 28 ملف — مخالفة واحدة فقط (jacobson) مؤكَّدة false positive وتُركت كما هي.
5+ ملفات سليمة تماماً بلا مسودة (jakhan، isaac-luria، jalal-al-din-rumi، jaspers). thk-isquella وthk-jaliaga حُجرا بدل كتابة مسودة.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-istansky**: نمط "اسم حقيقي + سيرة مفبركة بالكامل" أخطر من الأسماء المختلَقة الصريحة — يستحق فحصاً موسّعاً لملفات مشابهة قد تحمل نفس النمط.
- **thk-isaac-blind**: يحتاج ملفاً جديداً مستقلاً لإسحاق بن سليمان الإسرائيلي (المحتوى المفصول عنه قيّم تاريخياً).
- **thk-isquella وthk-jaliaga**: حجران جديدان، جزء من عنقود لاتيني-يونغي أوسع مشبوه (مع thk-epaz المحجور سابقاً وthk-gdiaz وthk-gadamoli غير المفحوصين) — يستحق فحصاً شاملاً للعنقود كله.
- **طلب `br-writing-therapy`**: تراكم واضح (بروغوف الآن + طلبات سابقة).
- **thk-jacobson**: false positive إضافي في فحص الجنس (الآن 6 حالات موثقة عبر الدفعات) — يستحق تحسين الـheuristic.

## الملفات
content/ar/thinkers/thk-ipavlov.md
content/ar/thinkers/thk-iplayer.md
content/ar/thinkers/thk-iprogoff.md
content/ar/thinkers/thk-iqbal.md
content/ar/thinkers/thk-irigaray.md
content/ar/thinkers/thk-irolf.md
content/ar/thinkers/thk-irubenfeld.md
content/ar/thinkers/thk-isaac-blind.md
content/ar/thinkers/thk-isaac-luria.md
content/ar/thinkers/thk-isaac-newton.md
content/ar/thinkers/thk-isaacs.md
content/ar/thinkers/thk-isebastiani.md
content/ar/thinkers/thk-ishvarakrishna.md
content/ar/thinkers/thk-isquella.md
content/ar/thinkers/thk-istansky.md
content/ar/thinkers/thk-iyengar.md
content/ar/thinkers/thk-jacobson.md
content/ar/thinkers/thk-jaffe.md
content/ar/thinkers/thk-jahoda.md
content/ar/thinkers/thk-jakhan.md
content/ar/thinkers/thk-jalal-al-din-dawani.md
content/ar/thinkers/thk-jalal-al-din-rumi.md
content/ar/thinkers/thk-jaliaga.md
content/ar/thinkers/thk-james-allen.md
content/ar/thinkers/thk-james-clear.md
content/ar/thinkers/thk-james.md
content/ar/thinkers/thk-jamiller.md
content/ar/thinkers/thk-janet.md
content/ar/thinkers/thk-janina-fisher.md
content/ar/thinkers/thk-jaspers.md
content/ar/thinkers/thk-jaustin.md
content/ar/thinkers/thk-jay-shetty.md
content/ar/thinkers/thk-jayatirtha.md
content/ar/thinkers/thk-jayearly.md
content/ar/thinkers/thk-jayres.md
