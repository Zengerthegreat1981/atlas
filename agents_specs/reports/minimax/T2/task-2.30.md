# Task 2.30
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 27

## الأرقام
جمل القائمة السوداء المتبقية: قبل 21 (ملفاً فيه واحدة على الأقل) → بعد 0
ملفات بلا `## المصادر`: قبل 16 → بعد 0
`edges` بـtarget نص حر بدل slug حقيقي: قبل 6 → بعد 0 (تحوّلت لـ`edges: []` وسُجّلت 3 مدارس فعلية غائبة في missing-schools.md)
`related` بعنوان (`title`) متضارب مع عنوان الملف المستهدف: قبل 8 روابط في 7 ملفات → بعد 0
gaps بتؤكد حقيقة بدل ما تسمي فجوة: قبل 2 → بعد 0
سنة في المتن بعد `active_end` بلا "بعد وفاته/وفاتها": قبل 2 (moreno، nozick) → بعد 0
ملفات محجورة: 1 (thk-wbennett)
ملفات أُعيد كتابتها بمصادر حقيقية بعد تصحيح ادعاءات مختلقة: 2 (thk-mpbargreen، thk-ovogt)

## أمر التحقق
python3 scripts/task.py verify minimax 2.30
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 (المستهدف 0) | فيها ## المصادر: 27 / 27

## قرارات اتخذتها
- thk-wbennett (وين بينيت): **حجر.** لا دليل مستقل (بحث ويب مباشر) على وجود شخص بهذا الاسم أو نسبة برنامج KIP-SST إليه. حقلا `country`/`dates` كانا أصلاً `[DRAFT-UNKNOWN]` رغم متن واثق الشكل — تناقض القاعدة 11. نُقلت النسخة الأصلية لـ`quarantine-minimax-archive/thk-wbennett.md.archived.2026-08-27`، استُبدل الملف الحي بقالب حجر موحّد، وسُجّل في `quarantine-minimax.md` القسم 9.
- thk-mpbargreen (ماري بيندر غرين): **موثّقة — أُعيد كتابتها.** بحث ويب أكّد وجودها الحقيقي (LCSW-R, CGP، MPG Consulting، AntiRacist Alliance)، لكن الكتاب المزعوم *A Woman's Recovery from the Trauma of War* (1985) والنظريات المسمّاة ("نظرية الموقع الاجتماعي" إلخ) غير موجودة في أي مصدر — استُبدلت بأعمالها الحقيقية الموثّقة (*Strategies for Deconstructing Racism in the Health and Human Services*، *Creative Mentorship and Career-Building Strategies*). `edges` تحوّل لـ`[]` (لا مدرسة مستقلة موثّقة باسمها) وأُضيف `## المصادر`.
- thk-ovogt (أوسكار فوغت): **موثّق — صُحّح.** شخصية حقيقية (عالم أعصاب ألماني 1870-1959)، لكن مصطلح "Vogt'sche Zustand" وربطه الوثيق بـ"التنويم الذاتي كإطار علاجي" غير موجودين في المصادر؛ الموثّق فعلياً هو رسالته 1897 في التجريب النفسي لحالات التنويم قبل تحوّله الكامل لبحث الدماغ. صُحّح عنوان عمله 1897، حُذف edges غير الموجود، وأُضيف `## المصادر` (PubMed).
- 15 ملفاً (nealmiller، sen، meichenbaum، rothbaum، sandel، rogers، young-jeffrey، pateman، mbalint، macintyre، singer، suzuki، mohanty، nozick، yalom‑جزئياً) — **موثّقون بالفعل، شخصيات حقيقية معروفة.** التصحيح اقتصر على: حذف جملة القائمة السوداء من `gaps` (استُبدلت بوصف دقيق للفجوة الفعلية)، إضافة `## المصادر`، تصحيح `related.title` غير المطابق، وإضافة "بعد وفاته" حيث لزم.
- thk-maturidi، thk-sadreddin-konevi، thk-shakespeare (توم شكسبير)، thk-nietzsche، thk-peter-singer، thk-vandeurzen: **موثّقون فعلاً بالفعل** (تراث عربي-إسلامي كلاسيكي أو فلاسفة/مفكرون معاصرون مشهورون) — لم يوجد فيهم جملة قائمة سوداء في المتن، أُضيف `## المصادر` حيث كان ناقصاً، وصُححت روابط `related` متضاربة العنوان في maturidi وvandeurzen وyalom.
- thk-moreno (يعقوب مورينو)، thk-npeseschkian (نصرت بيسشكيان)، thk-rmarvin (روبرت مارفن): **موثّقون فعلاً، مؤسسو مدارس علاجية حقيقية (سيكودراما، العلاج الإيجابي عبر-الثقافي، دائرة الأمان) لا ملف `sch-` مستقل لها في الأطلس.** حُذف `edges` (نص حر بدل slug) وسُجّلت المدارس الثلاث في `missing-schools.md` كأولويات Task 13. صُححت أيضاً سنة نشر بعد الوفاة (moreno: 1985) وrelated.title (rmarvin: كِنت هوفمان لا غلين هوفمان).
- thk-pateman، thk-mohanty: preflight أظهر تحذير جنس نحوي كاذب (false positive) — الكلمة المفعّلة كانت "هو" تشير لكلمة "العقد" (مذكر نحوياً، مش الشخص) في pateman، و"عالم" داخل "العالم الثالث" في mohanty. كلتاهما امرأتان موثّقتان (بيتمان مولودة 1940، موهانتي مولودة 1955) والعناوين الأصلية `## أهم أعمالها`/`## موقعها من التيار` كانت **صحيحة أصلاً**. أُعيدت صياغة الجملتين المسبِّبتين (بلا تغيير في المعنى) لتفادي المطابقة الآلية الخاطئة مع الحفاظ على صيغة العناوين المؤنثة الصحيحة.

## متوقف عنده (لرئيس التحرير)
- لا يوجد. كل الـ27 ملفاً حُسم قرارها (موثّق/محجور)، ولا ملف "غامض" في هذه الدفعة (كل الأسماء إما تحقق وجودها فعلياً أو ثبت غيابها).

## الملفات
content/ar/thinkers/thk-nealmiller.md
content/ar/thinkers/thk-sen.md
content/ar/thinkers/thk-mpbargreen.md
content/ar/thinkers/thk-meichenbaum.md
content/ar/thinkers/thk-wbennett.md
content/ar/thinkers/thk-rogers.md
content/ar/thinkers/thk-ovogt.md
content/ar/thinkers/thk-rothbaum.md
content/ar/thinkers/thk-sandel.md
content/ar/thinkers/thk-maturidi.md
content/ar/thinkers/thk-npeseschkian.md
content/ar/thinkers/thk-moreno.md
content/ar/thinkers/thk-young-jeffrey.md
content/ar/thinkers/thk-pateman.md
content/ar/thinkers/thk-rmarvin.md
content/ar/thinkers/thk-yalom.md
content/ar/thinkers/thk-peter-singer.md
content/ar/thinkers/thk-mbalint.md
content/ar/thinkers/thk-macintyre.md
content/ar/thinkers/thk-singer.md
content/ar/thinkers/thk-sadreddin-konevi.md
content/ar/thinkers/thk-vandeurzen.md
content/ar/thinkers/thk-shakespeare.md
content/ar/thinkers/thk-nietzsche.md
content/ar/thinkers/thk-suzuki.md
content/ar/thinkers/thk-mohanty.md
content/ar/thinkers/thk-nozick.md
