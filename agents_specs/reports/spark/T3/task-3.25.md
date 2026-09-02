# Task 3.25
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-karl-reinhold..thk-kkambon (شامل كيركغارد وكيرنبيرغ وهورني وغودل).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 0 / 35 — كل ملف احتاج تصحيحاً واحداً على الأقل.
- **حجر صحي جديد: thk-kashan** — نفس الاسم غير الموثّق الذي سبق أن أكّد ملف thk-fvanderzee المحجور عدم وجوده (لا "مشروع فان دير زي"، لا slug "علم النفس الإيجابي الشرقي").
- **تصحيح هوية جذري: thk-kathylaurenceau** — الملف المعتمد وصف شخصية مؤنثة مختلَقة بالكامل ("كاثي لورنسو"، "نظرية التآكل التدريجي") بينما الباحث الحقيقي هو **جان-فيليب لورنسو (رجل)**، صاحب "النموذج التفاعلي للحميمية" الحقيقي. أُعيدت كتابة السيرة كاملة بجنس مذكر وأعمال حقيقية. **يستحق مراجعة أوسع لملفات مشابهة.**
- **تأكيد نمط التصنيف الخاطئ المتبادل: thk-kcolby ↔ thk-jgrind** — تأكَّد أن الرابط بين كولبي (PARRY) وجون غريندر (NLP) كان تصنيفاً مفبركاً متبادلاً بلا سند علمي، كما اشتُبه في دفعة سابقة.
- **خطأ زمني/تسلسل جسيم: thk-keizan** — الملف كان يزعم أن كييزان "سافر ليدرس على يد دوگِن" رغم أن دوگِن توفي قبل ميلاد كييزان بـ11 عاماً — أُعيدت كتابة تسلسل التلمذة الصحيح (كُوان إيغو وغيكاي).
- **قرار تصحيحي تاريخي جسيم: thk-khwaja-baqi-billah** — كان يُلقَّب "المُجدِّد الثالث" بترتيب يناقض التسلسل الزمني الفعلي (توفي قبل تلميذه السرهندي بعقدين). حُذف اللقب العددي غير الموثَّق.
- **هوية مشكوك فيها بقوة: thk-kimkwansung** — لا مصدر لباحث بهذا الاسم في أدبيات Hwabyung؛ الاسم الشائع فعلياً "Kwang-Iel Kim" مختلف. حُذفت كل الادعاءات الواثقة وأُبقي وصف عام فقط.
- **ملف يستحق مراجعة حجر إضافية: thk-kfeeney** — الملف نفسه يحمل "تحذير تحقّق" سابق (لا باحثة بهذا الاسم موثّقة في منشورات PREP أو جامعة دنفر) لم يُحسم بعد.
- **تصحيحات هوية/جنس/تسلسل أخرى**: thk-khorney (خطأ جنس نحوي "توفي"↔"توفيت"، part خاطئ، بلد ناقص، عنوان كتاب خاطئ)، thk-kbradway (تاريخ ميلاد صُحح من 1916 إلى 1910، كتاب وهمي "In Her Own Voice" استُبدل بأعمال حقيقية).
- **نمط false positive في فحص الجنس**: thk-kbradway (كاي برادواي) — تُركت الصيغة المؤنثة الصحيحة عمداً.
- **عنقود مشبوه إضافي**: thk-kelleycolleen مرتبطة بروابط محجورة فعلياً (thk-bruceperkins، thk-marisaberkouwer) — حُذفت، والملف نفسه يستحق تدقيقاً إضافياً لاحقاً.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً هذه الدفعة (kcrenshaw→br-intersectional-feminist، keizan→sch-zen-soto، kelley→br-vegetotherapy-orgonomy، kelleycolleen→sch-sensorimotor-psychotherapy، kelly-george→br-personal-construct-psychology، kaufmann→sch-existential-therapy، kcolby→br-ai-chatbot-therapy، kcooper→tec-circle-of-security، kimmerer→sch-indigenous-psychology، kimura→sch-existential-therapy، kkambon→sch-african-psychology، kierkegaard→sch-existential-therapy، kgergen→br-social-constructionism، kgolding→br-ddp). حالات كثيرة بلا slug مطابق (karsavin [فلسفة دينية روسية]، kastenbaum [Thanatology]، kholzkamp/kimkwansung [علم نفس نقدي/ثقافي]، ken-blanchard [قيادة ظرفية]، kets [تحليل نفسي تنظيمي]) أُفرغت مع تسجيل طلبات.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{karl-reinhold,karsavin,kast,kastenbaum,kathylaurenceau,kaufmann,kbradway,kcolby,kcooper,kcrenshaw,keen,keizan,kelley,kelleycolleen,kelly-george,ken-blanchard,kernberg,kets,kfeeney,kfrank,kgergen,kgodel,kgolding,kgwilson,khan,kholzkamp,khorney,khwaja-baqi-billah,kierkegaard,kimkwansung,kimmerer,kimura,king,kkambon}.md
→ ✅ 33 ملف — مخالفة واحدة فقط (kbradway) مؤكَّدة false positive وتُركت كما هي. thk-kashan حُجر بدل كتابة مسودة.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-kathylaurenceau**: تصحيح هوية جذري (جنس وشخص كاملين) — يستحق فحصاً موسّعاً لأنماط مشابهة.
- **thk-kcolby ↔ thk-jgrind**: تأكيد رسمي لنمط التصنيف المفبرك المتبادل.
- **thk-kimkwansung وthk-kfeeney**: هويتان مشكوك فيهما بقوة، تحتاجان قراراً حجر/تصحيح.
- **thk-kelleycolleen**: عنقود مشبوه من شخصيات مطوري العلاج الحسي-الحركي — يستحق تدقيقاً مستقلاً.
- **thk-keizan**: أعيدت كتابته بحذر شديد لكن يفتقر لمصادر أكاديمية مستقلة — قد يستحق نقلاً لتاسك تعميق مخصص.
- **طلبات تصنيف متراكمة**: علم النفس النقدي/الثقافي، Thanatology، القيادة الظرفية، فلسفة دينية روسية.

## الملفات
content/ar/thinkers/thk-karl-reinhold.md
content/ar/thinkers/thk-karsavin.md
content/ar/thinkers/thk-kashan.md
content/ar/thinkers/thk-kast.md
content/ar/thinkers/thk-kastenbaum.md
content/ar/thinkers/thk-kathylaurenceau.md
content/ar/thinkers/thk-kaufmann.md
content/ar/thinkers/thk-kbradway.md
content/ar/thinkers/thk-kcolby.md
content/ar/thinkers/thk-kcooper.md
content/ar/thinkers/thk-kcrenshaw.md
content/ar/thinkers/thk-keen.md
content/ar/thinkers/thk-keizan.md
content/ar/thinkers/thk-kelley.md
content/ar/thinkers/thk-kelleycolleen.md
content/ar/thinkers/thk-kelly-george.md
content/ar/thinkers/thk-ken-blanchard.md
content/ar/thinkers/thk-kernberg.md
content/ar/thinkers/thk-kets.md
content/ar/thinkers/thk-kfeeney.md
content/ar/thinkers/thk-kfrank.md
content/ar/thinkers/thk-kgergen.md
content/ar/thinkers/thk-kgodel.md
content/ar/thinkers/thk-kgolding.md
content/ar/thinkers/thk-kgwilson.md
content/ar/thinkers/thk-khan.md
content/ar/thinkers/thk-kholzkamp.md
content/ar/thinkers/thk-khorney.md
content/ar/thinkers/thk-khwaja-baqi-billah.md
content/ar/thinkers/thk-kierkegaard.md
content/ar/thinkers/thk-kimkwansung.md
content/ar/thinkers/thk-kimmerer.md
content/ar/thinkers/thk-kimura.md
content/ar/thinkers/thk-king.md
content/ar/thinkers/thk-kkambon.md
