# Task 3.16
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-gnaranjo..thk-gweber. **المحاولة الأولى فشلت جزئياً — الجهاز نام أثناء التنفيذ فأدى لفشل كل الـ7 subagents (5 بسبب "stalled" و2 بسبب "API error: computer went to sleep")؛ مجموعة D كانت قد أنجزت فعلياً كتابة 5 ملفاتها كاملة قبل التوقف فأُصلحت المخالفات المتبقية يدوياً (preflight)، وأُعيد تشغيل باقي الـ6 مجموعات من الصفر بنجاح.**

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 1 / 35 (thk-gotama-kanad)
- **اقتباس مفبرك مكتشف ومصحح: thk-gobind-singh** — الاقتباس الختامي كان لا يطابق أي مصدر ويتناقض مضمونياً مع سياقه — استُبدل باقتباس حقيقي موثّق من الزفرنامه بعد بحث خارجي (يُنصح بمراجعة بشرية إضافية قبل الترقية).
- **خطأ هوية جغرافي جوهري: thk-gongsun-long** — كان منسوباً لولاية تشي ومرتبطاً بأكاديمية جياتشي، والصحيح أنه من ولاية جاو (Zhao) وتابع للأمير پينغيوان — لا صلة موثقة بجياتشي إطلاقاً. تصحيح تاريخي جوهري لا مجرد صياغة.
- **ازدواج slug رابع مكتشف: thk-gotama-kanad ↔ thk-gotama-nyaya** — كلاهما يصف نفس الشخص التاريخي (مؤسس مدرسة النيايا) بتواريخ متضاربة.
- **وفاة حديثة غير مسجلة: thk-griffiths (رولاند غريفيثز)** — توفي فعلياً أكتوبر 2023، الملف كان يعرضه كحيّ.
- **خطأ نسبة جوهري: thk-gregory-rimini** — كتاب «الجُمل» كان منسوباً لـ"أمبروزيوس" خطأً، والصحيح لبطرس اللومباردي.
- **نمط تصنيف خاطئ بلا سبب نصي: thk-gschwartz** — كان مصنَّفاً تحت "العلاج بمساعدة الذكاء الاصطناعي" رغم أن عمله الفعلي بحوث وسائط روحية/علم نفس الطاقة، لا صلة فعلية — أُفرغت edges/related بالكامل. **نفس الخطأ موجود بالمثل في thk-jgrind (رابط عكسي).**
- **رابط محجور لسه موجود في الملف المعتمد: thk-gweber** — رابط `thk-jjoyce` محجور فعلياً في quarantine-spark.md لكن الملف المعتمد الحالي لا يزال يحمله — يستحق تصحيحاً فورياً عند الترقية.
- **أخطاء تواريخ**: thk-gsmith (تاريخ ميلاد كان `[DRAFT-UNKNOWN]`، صُحح ببحث خارجي إلى 1950)، thk-gnardone (نفس النمط، صُحح إلى 1958)، thk-goldfried (توضيح أنه لا يوجد دليل وفاة رغم فراغ الحقل)، thk-gordon (`active_end` كان يوهم بتوقف النشاط)، thk-greenberg (كان `active_end: 2015` رغم استمرار نشاطه فعلياً).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير (gnaranjo→sch-gestalt-therapy، gnardone→br-brief-strategic-therapy، gshepherd→br-case-management، gsmith→sch-kaupapa-maori، griffiths→sch-psychedelic-assisted-therapy، gretchen-rubin→sch-positive-psychology). حالات بلا slug مطابق (goldfried [تكامل العلاج]، goleman [علم نفس شعبي]، guy-winch [نفس]، gweber/gschwartz) أُفرغت مع تسجيل طلبات جديدة — تكرار إضافي لفجوة "علم النفس الشعبي" وفجوة "تشكيلات الأسرة" (تؤثر على 3 ملفات معتمدة أخرى: bhellinger، hbeaumont، jschneider).
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{gnaranjo,gnardone,gobind-singh,goldberg,goldfried,goldmann,goldstein,goleman,golwalkar,gongsun-long,goodman,gordon,gorgias,gotama-nyaya,govinda,gparis,graeber,graham-harman,greenberg-lisa,greenberg,gregory-rimini,grenier,gretchen-rubin,griffiths,gschwartz,gshepherd,gsmith,guattari,guggenbuhl,guntrip,guo-xiang,gurwitsch,guy-winch,gweber}.md
→ ✅ 34 ملف — صفر مخالفات آلية (thk-gotama-kanad سليم تماماً، بلا مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن (أو إضافة سبب موثّق حين كان ممكناً)، وإصلاح تعارضات id/title.

## متوقف عنده (لرئيس التحرير)
- **thk-gongsun-long**: تصحيح تاريخي جوهري (Zhao لا Qi) — يستحق مراجعة بشرية قبل الترقية.
- **thk-gotama-kanad ↔ thk-gotama-nyaya**: ازدواج مؤكد يحتاج دمجاً.
- **thk-gweber**: الملف المعتمد الحالي لا يزال يحمل رابطاً محجوراً (thk-jjoyce) — تصحيح فوري مطلوب.
- **thk-gschwartz ↔ thk-jgrind**: نمط تصنيف خاطئ متبادل (كلاهما يربط الآخر بالذكاء الاصطناعي بلا صلة فعلية) — يحتاج فحصاً منفصلاً.
- **thk-gobind-singh**: الاقتباس البديل يستحق مراجعة بشرية إضافية رغم التحقق الخارجي.
- **طلب `br-family-constellations`**: يؤثر على 3 ملفات معتمدة أخرى غير مشمولة بهذه الدفعة (bhellinger، hbeaumont، jschneider).
- **حادثة النوم**: توقف الجهاز أثناء الدفعة تسبب في فشل جماعي — تم التعافي كاملاً بلا فقد بيانات (مجموعة D أُنقذت يدوياً، الباقي أُعيد من الصفر).

## الملفات
content/ar/thinkers/thk-gnaranjo.md
content/ar/thinkers/thk-gnardone.md
content/ar/thinkers/thk-gobind-singh.md
content/ar/thinkers/thk-goldberg.md
content/ar/thinkers/thk-goldfried.md
content/ar/thinkers/thk-goldmann.md
content/ar/thinkers/thk-goldstein.md
content/ar/thinkers/thk-goleman.md
content/ar/thinkers/thk-golwalkar.md
content/ar/thinkers/thk-gongsun-long.md
content/ar/thinkers/thk-goodman.md
content/ar/thinkers/thk-gordon.md
content/ar/thinkers/thk-gorgias.md
content/ar/thinkers/thk-gotama-kanad.md
content/ar/thinkers/thk-gotama-nyaya.md
content/ar/thinkers/thk-govinda.md
content/ar/thinkers/thk-gparis.md
content/ar/thinkers/thk-graeber.md
content/ar/thinkers/thk-graham-harman.md
content/ar/thinkers/thk-greenberg-lisa.md
content/ar/thinkers/thk-greenberg.md
content/ar/thinkers/thk-gregory-rimini.md
content/ar/thinkers/thk-grenier.md
content/ar/thinkers/thk-gretchen-rubin.md
content/ar/thinkers/thk-griffiths.md
content/ar/thinkers/thk-gschwartz.md
content/ar/thinkers/thk-gshepherd.md
content/ar/thinkers/thk-gsmith.md
content/ar/thinkers/thk-guattari.md
content/ar/thinkers/thk-guggenbuhl.md
content/ar/thinkers/thk-guntrip.md
content/ar/thinkers/thk-guo-xiang.md
content/ar/thinkers/thk-gurwitsch.md
content/ar/thinkers/thk-guy-winch.md
content/ar/thinkers/thk-gweber.md
