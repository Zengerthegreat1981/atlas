# Task 3.17
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-habermas..thk-heysenck (شامل هابرماس وهيغل وهايدجر وهلمهولتز وهيراقليطس).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 5 / 35 (thk-hayyim-vital، thk-hanfeizi، thk-haraway، thk-hegel، thk-he-yan، thk-hermes-trismegistus — ملاحظة: 6 فعلياً، راجع القائمة أدناه)
- **سيرة مفبركة جزئياً مكتشفة: thk-helen-lakelly-hunt** — تعليم مختلَق بالكامل (سميث كوليدج/UT أوستن)، جملة عبثية عن "طفولة المُتعاطِف"، اسم جمعية خيرية خاطئ، عنوانا كتابين خاطئين، اقتباس غير موثّق. **قرار حساس جداً يحتاج مراجعة رئيس التحرير قبل أي ترقية.**
- **خطأ نسبة/تفبرك: thk-harriet-lerner** — انتساب مؤسسي خاطئ (معهد وهمي بدل عيادة مينينغر الحقيقية)، كتاب مفبرك بالكامل («The Courage to Be» — فعلياً كتاب بول تيليش، لا علاقة بليرنر)، عنوان كتاب آخر خاطئ.
- **خطأ نسبة في كتاب حقيقي: thk-haponte** — المؤلفة المشاركة الحقيقية لكتاب 2016 هي "كارني كيسيل" وليس "كارين ك. كارلسن" (اسم مختلف تماماً كان قد مرّ دون رصد).
- **أرقام مبالغ فيها/مفبركة: thk-harville-hendrix** — "90 دولة/11,000 معالج/200 ظهور تلفزيوني" صُححت إلى الأرقام الرسمية الموثقة (~50 دولة، ~2,000+ معالج، 17 ظهوراً في أوبرا وينفري).
- **تأكيد ازدواج معروف مسبقاً: thk-heidegger ↔ thk-heidegger-technology** — نفس الشخص (مارتن هايدجر) بملفين. كان مسجَّلاً بالفعل في gaps الملف الرئيسي كقرار نمذجة معلَّق — لم يُدمج، تُرك لرئيس التحرير.
- **وفاة حديثة غير مسجلة: thk-hdavanloo (حبيب دفانلو)** — توفي فعلياً نوفمبر 2023، الملف كان يذكر 2016 (مع شك داخلي بين 2016/2018).
- **رابط محجور آخر في نمط "تشكيلات الأسرة"**: thk-hbeaumont كان يربط `thk-jjoyce` المحجور فعلياً (شخصية غير موثقة تستخدم slug جيمس جويس) — حُذف. فجوة `edges` نفسها (تشكيلات الأسرة) تراكمت الآن عبر 4 ملفات (bhellinger، gweber، jjoyce، hbeaumont).
- **تناقض بنيوي داخلي مصحح: thk-hbernheim** — كان مصنَّفاً تحت "الماسمرية" بينما متن الملف نفسه يقول صراحة إن برنهايم رفضها — أُفرغت edges (اقتراح `sch-nancy-school`).
- **نمط تصنيف خاطئ نظامي (part: bridge)**: thk-helmholtz وملفات أخرى (fechner، bachelard، cassirer، calkins، fc-schiller) تشترك في نفس الخطأ — `edges.belongs_to` يشير لعنوان علاقة (rel-) بدل slug مدرسة — يستحق قراراً موحداً بدل إصلاح ملف بملف.
- **false positives مؤكدة في فحص الجنس**: thk-heimann وthk-helen-lakelly-hunt (كلاهما امرأتان مؤكدتان) — الفحص الآلي يحسب كلمات دور عامة ("المعالج") كمؤشرات ذكورية خطأً. تُركتا بصيغة مؤنثة صحيحة عمداً.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.
- عدة ملفات كانت تفتقر لقسم `## المصادر` — أُضيفت مصادر أولية حقيقية (habermas، hadi-sabzawari، hajime-tanabe، hakuin، halling).

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{habermas,hadi-sabzawari,hajime-tanabe,hakuin,halling,handerson,hannah,haponte,harriet-lerner,harris,hartmann,hartmannheinz,harville-hendrix,hassan-hanafi,hbarbaree,hbeaumont,hbernheim,hdavanloo,heimann,helen-lakelly-hunt,heller,hellmuth,helmholtz,henry-odera-oruka,heraclitus,heydt,heysenck}.md
→ ✅ 27 ملف — صفر مخالفات آلية حقيقية (مخالفتا الجنس في heimann/helen-lakelly-hunt مؤكَّدتان false positive وتُركتا كما هما).
6 ملفات سليمة بلا مسودة: thk-hayyim-vital، thk-hanfeizi، thk-haraway، thk-hegel، thk-he-yan، thk-hermes-trismegistus. thk-heidegger وthk-heidegger-technology رُوجعا بالكامل ولم تُكتشف فيهما أخطاء تدقيق (الازدواج بينهما مسجَّل مسبقاً في gaps، لم يُعدَّل).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإضافة مصادر أولية حقيقية حيث كانت غائبة.

## متوقف عنده (لرئيس التحرير)
- **thk-helen-lakelly-hunt**: سيرة مفبركة جزئياً بشكل ملموس — أولوية عالية جداً للمراجعة قبل الترقية.
- **thk-heidegger ↔ thk-heidegger-technology**: ازدواج مؤكد معلَّق منذ فترة — يحتاج حسماً (تحويل ملف التكنولوجيا لعقدة مفهوم بدل "مفكر"، أم دمج).
- **thk-hdavanloo**: تصحيح وفاته (2023 لا 2016) أولوية عالية.
- **نمط `part: "bridge"`**: خطأ تصنيف نظامي يمس 5+ ملفات (helmholtz، fechner، bachelard، cassirer، calkins، fc-schiller) — يستحق قراراً موحداً.
- **فجوة "تشكيلات الأسرة"**: الآن 4 ملفات معتمدة (bhellinger، gweber، jjoyce، hbeaumont) بحاجة slug واحد.
- **false positives الجنس**: heimann وhelen-lakelly-hunt — يستحق تحسين منطق preflight_check.py لتفادي عدّ الأسماء العامة كمؤشر جنس.

## الملفات
content/ar/thinkers/thk-habermas.md
content/ar/thinkers/thk-hadi-sabzawari.md
content/ar/thinkers/thk-hajime-tanabe.md
content/ar/thinkers/thk-hakuin.md
content/ar/thinkers/thk-halling.md
content/ar/thinkers/thk-handerson.md
content/ar/thinkers/thk-hanfeizi.md
content/ar/thinkers/thk-hannah.md
content/ar/thinkers/thk-haponte.md
content/ar/thinkers/thk-haraway.md
content/ar/thinkers/thk-harriet-lerner.md
content/ar/thinkers/thk-harris.md
content/ar/thinkers/thk-hartmann.md
content/ar/thinkers/thk-hartmannheinz.md
content/ar/thinkers/thk-harville-hendrix.md
content/ar/thinkers/thk-hassan-hanafi.md
content/ar/thinkers/thk-hayyim-vital.md
content/ar/thinkers/thk-hbarbaree.md
content/ar/thinkers/thk-hbeaumont.md
content/ar/thinkers/thk-hbernheim.md
content/ar/thinkers/thk-hdavanloo.md
content/ar/thinkers/thk-he-yan.md
content/ar/thinkers/thk-hegel.md
content/ar/thinkers/thk-heidegger-technology.md
content/ar/thinkers/thk-heidegger.md
content/ar/thinkers/thk-heimann.md
content/ar/thinkers/thk-helen-lakelly-hunt.md
content/ar/thinkers/thk-heller.md
content/ar/thinkers/thk-hellmuth.md
content/ar/thinkers/thk-helmholtz.md
content/ar/thinkers/thk-henry-odera-oruka.md
content/ar/thinkers/thk-heraclitus.md
content/ar/thinkers/thk-hermes-trismegistus.md
content/ar/thinkers/thk-heydt.md
content/ar/thinkers/thk-heysenck.md
