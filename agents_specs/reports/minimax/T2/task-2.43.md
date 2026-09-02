# Task 2.43
الحالة: مكتمل
العملية: Task 2 — التحقق من وجود أصحاب 10 ملفات مفكّرين + حسم ازدواجين | الملفات: 10

## الأرقام
- موثّق (أُعيد كتابته/نُقّح): 8 ملفات (park-jiwon, patricia-churchland, robert-kegan, walter-benjamin, quentin-meillassoux, morteza-motahhari, peter-abelard, sminuchin)
- إحالة ازدواج (redirect): 2 ملفان (richard-thaler → rkthaler، meillassoux → quentin-meillassoux)
- غير موجود: 0
- غامض: 0
- جمل قائمة سوداء قبل: 8 (churchland×2 [gaps+quotes]، kegan×2، benjamin×2، thaler×1، quentin-meillassoux×2، motahhari×2، abelard×2) → بعد: 0
- `## المصادر` مضافة لملفات كانت بلا القسم: park-jiwon، churchland (كان فيه قسم فاضي/جملة سوداء فقط)، kegan، benjamin، quentin-meillassoux، motahhari، abelard، sminuchin = 8 ملفات
- `edges.belongs_to` بنص حر صُححت: churchland (حُذف → missing-schools.md)، kegan (حُذف → missing-schools.md)، sminuchin (developed → br-structural-family slug حقيقي)
- روابط `related` بعنوان متضارب صُححت: 6 (park-jiwon×2، kegan×1، sminuchin×4)
- مخالفة "سنة بعد active_end" صُححت: 1 (benjamin: 1982 نُشر بعد وفاته 1940)

## أمر التحقق
`python3 scripts/preflight_check.py <10 ملفات>` → ✅ 10 ملف — صفر مخالفات آلية (بعد تصحيح مخالفتين: تاريخ benjamin وedge حر في sminuchin)

## قرارات اتخذتها
- **thk-park-jiwon**: موثّق. شخص حقيقي (باك جي-وون/يونام، عالم سيلهاك كوري 1737–1805، جناح بوكهاك)، لكن المحتوى السابق كان مُختلَقاً بالكامل تقريباً (اسم صيني "تشو بيغنيو" غير موجود، عناوين كتب مشوّهة لا تطابق أعماله الحقيقية). أعدت كتابته بالكامل بأعماله الحقيقية الموثّقة (يولها إلجي 1780، هوجيل، هوسايونغ جون، يانغبان جون) بعد تحقق ويب مباشر (Wikipedia، LOC Authorities، Korea Times).
- **thk-patricia-churchland**: موثّق (فيلسوفة عصبية معروفة، بحث سابق كان جيداً بالفعل). حُذفت جملتا قائمة سوداء، حُذف edge حر (المادية الإقصائية) وسُجّل في missing-schools.md، أُضيف `## المصادر`.
- **thk-robert-kegan**: موثّق (أستاذ هارفارد معروف). نفس الإصلاحات: حذف edge حر (سُجّل في missing-schools.md)، حذف جملة سوداء، إضافة مصادر، تصحيح عنوان `related` متضارب.
- **thk-walter-benjamin**: موثّق. المحتوى كان جيداً وله اقتباسان موثّقان فعلياً (يناقضان جملة القائمة السوداء الموجودة في gaps في نفس الوقت — حُذفت الجملة المتناقضة). أُضيف `## المصادر` (كان غائباً)، وصُححت مخالفة السنة (1982 نشر بعد الوفاة 1940) بإضافة "بعد وفاته".
- **thk-richard-thaler ≡ thk-rkthaler**: ازدواج مؤكَّد لنفس الشخص (Richard H. Thaler). القرار: **thk-rkthaler هو المعتمد** لأن له روابط واردة حقيقية أكثر (`wrk-nudge` عبر `author_slug`، و`thk-kahneman`، و`thk-rkahneman` في `_merged`)، بينما `thk-richard-thaler` لا يملك سوى رابط وارد واحد حقيقي (`thk-arascovsky`). حُوّل `thk-richard-thaler` لإحالة صريحة على نمط `thk-mwhitehouse`.
- **thk-quentin-meillassoux ≡ thk-meillassoux**: ازدواج مؤكَّد لنفس الشخص (Quentin Meillassoux، فيلسوف فرنسي). القرار: **thk-quentin-meillassoux هو المعتمد** لأنه الملف الذي يربطه `sch-speculative-realism` نفسه برابط `related` حقيقي (بنية مدرسية)، بينما `thk-meillassoux` رابطه الوارد الوحيد من `thk-arascovsky`. أضفت `related` (هارمان، كانط، الواقعية المضاربة) و`## المصادر` لـ`thk-quentin-meillassoux`، وحُوّل `thk-meillassoux` لإحالة صريحة.
- **thk-morteza-motahhari**: موثّق (فيلسوف إيراني معروف، تلميذ الطباطبائي، اغتيل 1979). حُذفت جملة سوداء، أُضيف `## المصادر` (Encyclopaedia Iranica + SEP).
- **thk-peter-abelard**: موثّق (فيلسوف مدرسي معروف، له اقتباس موثّق فعلياً). حُذفت جملة سوداء متناقضة مع وجود الاقتباس الفعلي، أُضيف `## المصادر`.
- **thk-sminuchin**: تحقّقت أولاً من عدم وجود slug مزدوج لسلفادور مينوشين في `EXISTING_SLUGS.md` — لا يوجد ازدواج، `thk-sminuchin` هو الوحيد. الملف موثّق ومفصّل جيداً من دفعة سابقة، لكن ناقصه `## المصادر` (أضفتها) واقتباسان بلا مصدر محدد (حُذفا بعد بحث ويب لم يؤكدهما حرفياً)، وصُححت 4 روابط `related` بعنوان متضارب، وصُحح edge حر (developed → br-structural-family).

## متوقف عنده (لرئيس التحرير)
لا شيء.

## سجلّات جانبية
- `agents_specs/missing-schools.md`: أُضيف سطران — المادية الإقصائية (من thk-patricia-churchland)، وعلم النفس التنموي للبالغين والقيادة التكيفية (من thk-robert-kegan).
- ملاحظة: `content/ar/thinkers/thk-arascovsky.md` (خارج نطاق دفعتي) لا يزال يشير إلى `thk-richard-thaler` و`thk-meillassoux` (الملفين اللذين تحوّلا لإحالة) بدل الـslug المعتمد؛ يُنصح بتحديثه في دفعة لاحقة.

## الملفات
- content/ar/thinkers/thk-park-jiwon.md
- content/ar/thinkers/thk-patricia-churchland.md
- content/ar/thinkers/thk-robert-kegan.md
- content/ar/thinkers/thk-walter-benjamin.md
- content/ar/thinkers/thk-richard-thaler.md
- content/ar/thinkers/thk-quentin-meillassoux.md
- content/ar/thinkers/thk-meillassoux.md
- content/ar/thinkers/thk-morteza-motahhari.md
- content/ar/thinkers/thk-peter-abelard.md
- content/ar/thinkers/thk-sminuchin.md
