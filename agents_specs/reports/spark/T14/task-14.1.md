# Task 14.1
الحالة: مكتمل جزئياً
العملية: دراسات وأدوات حديثة (std-/ins-) — كتابة 5 دراسات + 5 أدوات قياس جديدة كلياً (10 subagent متوازي) | الملفات: 10

## الأرقام
مسودات الأطلس الكلية: 155 → 170 (+15؛ رقم أعلى من 10 لأن Task 13.1 وTask 14.1 نُفِّذا في نفس الجلسة والفهرس اتحدّث مرة واحدة آخر الاتنين)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل الـ10 ملفات → مخالفة واحدة فقط (title مكتوب "بوردن" بدل "بورديـن" في related بملف ins-wai) صُحِّحت فوراً → صفر مخالفات آلية
`python3 scripts/build_slug_index.py` → 6788 عنصر (6618 معتمد + 170 مسودة)

## قرارات اتخذتها
- اخترت 5 دراسات و5 أدوات من العناصر **المؤكَّدة صراحة في نص Task 14** (STAR*D، CATIE، MTA، دراسة ACE، DES/DES-II، PCL-R، روزنبرغ لتقدير الذات، جرد ماسلاخ، WAI) + دراسة روبنز عن هيروين فيتنام (مذكورة أيضاً في نص التاسك) بدل Whitehall لأن `syn-whitehall` موجود بالفعل كمتلازمة منفصلة وده كان هيسبب التباس نطاق.
- كل ملف اتكتب بحقول Task 7/8 المطلوبة (`study_year`/`design`/`sample_size`/`main_finding`/`replication_status` للدراسات، و`items_count`/`target_population`/`reliability`/`validity_note`/`evidence_level` للأدوات).
- التزمت الأدوات كلها بذكر "لا يوجد تقنين عربي موثّق" صراحة في `gaps` بدل اختراع تقنين وهمي — مفيش أداة من الخمسة لها تقنين عربي رسمي موثّق فعلياً.
- 3 subagents (ins-rosenberg, ins-maslach-burnout-inventory, ins-wai) أصابهم خطأ API بسبب حد استخدام الجلسة، لكن الملفات كانت اتكتبت فعلياً قبل الانقطاع — تحققت يدوياً من الثلاثة بـpreflight_check وعدّوا الفحص (بعد تصحيح مخالفة واحدة في ins-wai).
- تجنبت اختراع slugs لأدوية/أشخاص غير موجودين (زي thk-hare، thk-bordin، thk-horvath، thk-felitti، thk-anda) وسجلتهم في gaps كل ملف على حدة.

## متوقف عنده (لرئيس التحرير)
- باقي عناصر Task 14 غير مكتوبة بعد (Many Labs 1-4، فشل تكرار استنزاف الأنا ووضعية القوة، وايتهول I/II، تجربة مينيسوتا للتجويع، بارك الجرذان، تجارب غريفيثس للسيلوسيبين، MAPS المرحلة الثالثة من جانب الدراسات؛ SCL-90-R، CTQ، استبيان ACE، MINI، WHODAS 2.0، OQ-45، CORE-OM، CAT-Q، RAADS-R من جانب الأدوات) — محتاجة دفعة/دفعات تانية.

## الملفات
content/ar/drafts/spark/studies/stu-stard.md
content/ar/drafts/spark/studies/stu-catie.md
content/ar/drafts/spark/studies/stu-mta.md
content/ar/drafts/spark/studies/stu-ace-study.md
content/ar/drafts/spark/studies/stu-robins-vietnam-heroin.md
content/ar/drafts/spark/instruments/ins-des-ii.md
content/ar/drafts/spark/instruments/ins-pcl-r.md
content/ar/drafts/spark/instruments/ins-rosenberg-self-esteem.md
content/ar/drafts/spark/instruments/ins-maslach-burnout-inventory.md
content/ar/drafts/spark/instruments/ins-wai.md
