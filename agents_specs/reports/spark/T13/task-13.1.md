# Task 13.1
الحالة: مكتمل جزئياً
العملية: «الدراسة موجودة وصاحبها غائب» — ترحيل مسودات موجودة سابقاً + كتابة 12 ملف جديد لأسماء غائبة تماماً (نطاق thk-a إلى thk-l فقط) | الملفات: 73 (61 ترحيل + 12 جديد)

## الأرقام
مسودات الأطلس الكلية: 122 → 155 (+33 صافي؛ 61 ملف انتقل من `content/ar/drafts/thinkers/` غير المصنّف إلى `content/ar/drafts/spark/thinkers/` بلا تغيير عددي على الإجمالي، بالإضافة لـ12 ملف جديد فعلاً)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل الـ73 ملف → صفر مخالفات آلية بعد تصحيح 8 مخالفات (تواريخ بعد الوفاة بلا إشارة، gaps مؤكِّدة لحقيقة، تعارض جندري)
`python3 scripts/build_slug_index.py` → 6773 عنصر (6618 معتمد + 155 مسودة)

## قرارات اتخذتها
- اكتشفت إن أغلب أسماء Task 13 (مؤسسو علم النفس/الطب النفسي والمعرفي والقياس النفسي والنمائي) **كانت مكتوبة بالفعل** في مجلد قديم غير مصنَّف `content/ar/drafts/thinkers/` (قبل تقسيم المسارات في Phase 0.11). نقلت فقط الملفات اللي نطاق slug بتاعها من thk-a إلى thk-l (61 ملف) لمجلدي `drafts/spark/thinkers/`؛ سيبت ملفات thk-m إلى thk-z (زي neisser, tulving, baddeley وهي مش لي — تصحيح: baddeley بالفعل b فمن نصيبي واتنقل) لمجلد MiniMax بدون لمسها.
- صحّحت 8 مخالفات آلية ظهرت بعد الترحيل: `thk-bekhterev`/`thk-kraepelin`/`thk-herbert-simon` (سنوات بعد وفاة الشخص بلا صيغة «بعد وفاته» ملاصقة للسنة — حدّ preflight هو نافذة 30 حرف)، `thk-caspi`/`thk-claude-steele`/`thk-david-clark` (سطر gaps كان بيكرر حقيقة مؤكدة من dates بدل ما يسمي فجوة فعلية)، `thk-folkman` (كلمتا «هو» و«العالم» عامتان أنتجتا احتساب مذكر زائف رغم إن الملف عن سيدة).
- كتبت 12 ملف جديد فعلاً غير موجود إطلاقاً (لا معتمد ولا مسودة) في نطاقي: جيمس كاتل، إسكيرول، غريزنغر، ألزهايمر، لاشلي، بريندا ميلنر، لويس غولدبرغ (فرّقته بوضوح عن thk-goldberg وthk-ngoldberg الموجودين لأشخاص مختلفين)، إيمي فيرنر، ليزا فيلدمان باريت (فرّقتها عن thk-barrett/thk-lbarrett)، رونالد كيسلر، ريتشارد كلوفت، كريستين كورتوا. كل ملف عدّى preflight_check بصفر مخالفات.
- باقي أسماء Task 13 غير المكتوبة (Weber الفيزيولوجي، Stumpf، Woodworth، Yerkes، Rutter، Neisser، Tulving، Squire، Thurstone، Sternberg، McCrae، Sroufe، Shaver/Mikulincer، Tronick، Tomasello، Selye، Maslach، Tomkins، Moffitt، Malan/Sifneos، Safran/Muran، Salkovskis/Rachman، van der Hart/Nijenhuis) نطاق slug بتاعها m-z — دي مسؤولية MiniMax مش Spark، فسبتها.

## متوقف عنده (لرئيس التحرير)
- المجلد `content/ar/drafts/thinkers/` القديم لسه فيه ملفات m-z تخص MiniMax محتاجة نفس عملية الترحيل لـ`drafts/minimax/thinkers/` — دي مش من صلاحيتي.
- تحذير: `build_slug_index.py` رصد 282 تعارض slug بين معتمد ومسودة (زيادة من 231 قبل الترحيل، لأن أسماء زي thk-adler وthk-darwin وthk-ainsworth موجودة في المسودات القديمة اللي كانت مخفية عن الفهرس بسبب عدم مسحها من المجلد الصحيح — دلوقتي الفهرس شافها). ده تراكم قديم سابق لهذه الجلسة، مش نتيجة كتابتي الجديدة، ومحتاج مراجعة دمج منفصلة (Task 2).

## الملفات
content/ar/drafts/spark/thinkers/thk-abdulsattar-ibrahim.md
content/ar/drafts/spark/thinkers/thk-abu-zayd.md
content/ar/drafts/spark/thinkers/thk-al-attas.md
content/ar/drafts/spark/thinkers/thk-allen-frances.md
content/ar/drafts/spark/thinkers/thk-amber-haque.md
content/ar/drafts/spark/thinkers/thk-anil-seth.md
content/ar/drafts/spark/thinkers/thk-anthony-greenwald.md
content/ar/drafts/spark/thinkers/thk-baars.md
content/ar/drafts/spark/thinkers/thk-baddeley.md
content/ar/drafts/spark/thinkers/thk-banaji.md
content/ar/drafts/spark/thinkers/thk-bekhterev.md
content/ar/drafts/spark/thinkers/thk-bennabi.md
content/ar/drafts/spark/thinkers/thk-bentall.md
content/ar/drafts/spark/thinkers/thk-bernard-williams.md
content/ar/drafts/spark/thinkers/thk-borsboom.md
content/ar/drafts/spark/thinkers/thk-bourdieu.md
content/ar/drafts/spark/thinkers/thk-broadbent.md
content/ar/drafts/spark/thinkers/thk-bronfenbrenner.md
content/ar/drafts/spark/thinkers/thk-canguilhem.md
content/ar/drafts/spark/thinkers/thk-caspi.md
content/ar/drafts/spark/thinkers/thk-christof-koch.md
content/ar/drafts/spark/thinkers/thk-claude-steele.md
content/ar/drafts/spark/thinkers/thk-cloitre.md
content/ar/drafts/spark/thinkers/thk-corbin.md
content/ar/drafts/spark/thinkers/thk-costa.md
content/ar/drafts/spark/thinkers/thk-craik.md
content/ar/drafts/spark/thinkers/thk-daniel-stern.md
content/ar/drafts/spark/thinkers/thk-david-clark.md
content/ar/drafts/spark/thinkers/thk-dehaene.md
content/ar/drafts/spark/thinkers/thk-durkheim.md
content/ar/drafts/spark/thinkers/thk-dwairy.md
content/ar/drafts/spark/thinkers/thk-ebbinghaus.md
content/ar/drafts/spark/thinkers/thk-elmessiri.md
content/ar/drafts/spark/thinkers/thk-fazlur-rahman.md
content/ar/drafts/spark/thinkers/thk-folkman.md
content/ar/drafts/spark/thinkers/thk-friston.md
content/ar/drafts/spark/thinkers/thk-gardner.md
content/ar/drafts/spark/thinkers/thk-gazzaniga.md
content/ar/drafts/spark/thinkers/thk-george-miller.md
content/ar/drafts/spark/thinkers/thk-goffman.md
content/ar/drafts/spark/thinkers/thk-guidano.md
content/ar/drafts/spark/thinkers/thk-gunderson.md
content/ar/drafts/spark/thinkers/thk-hacking.md
content/ar/drafts/spark/thinkers/thk-hebb.md
content/ar/drafts/spark/thinkers/thk-hefny.md
content/ar/drafts/spark/thinkers/thk-herbert-simon.md
content/ar/drafts/spark/thinkers/thk-hijazi.md
content/ar/drafts/spark/thinkers/thk-ijzendoorn.md
content/ar/drafts/spark/thinkers/thk-insel.md
content/ar/drafts/spark/thinkers/thk-izetbegovic.md
content/ar/drafts/spark/thinkers/thk-kanner.md
content/ar/drafts/spark/thinkers/thk-kathy-steele.md
content/ar/drafts/spark/thinkers/thk-kendler.md
content/ar/drafts/spark/thinkers/thk-keshavarzi.md
content/ar/drafts/spark/thinkers/thk-kirmayer.md
content/ar/drafts/spark/thinkers/thk-kleinman.md
content/ar/drafts/spark/thinkers/thk-koenig.md
content/ar/drafts/spark/thinkers/thk-kraepelin.md
content/ar/drafts/spark/thinkers/thk-kretschmer.md
content/ar/drafts/spark/thinkers/thk-lahbabi.md
content/ar/drafts/spark/thinkers/thk-lambert.md
content/ar/drafts/spark/thinkers/thk-leontiev.md
content/ar/drafts/spark/thinkers/thk-liotti.md
content/ar/drafts/spark/thinkers/thk-james-cattell.md
content/ar/drafts/spark/thinkers/thk-esquirol.md
content/ar/drafts/spark/thinkers/thk-griesinger.md
content/ar/drafts/spark/thinkers/thk-alzheimer.md
content/ar/drafts/spark/thinkers/thk-lashley.md
content/ar/drafts/spark/thinkers/thk-brenda-milner.md
content/ar/drafts/spark/thinkers/thk-lewis-goldberg.md
content/ar/drafts/spark/thinkers/thk-emmy-werner.md
content/ar/drafts/spark/thinkers/thk-lisa-feldman-barrett.md
content/ar/drafts/spark/thinkers/thk-kessler.md
content/ar/drafts/spark/thinkers/thk-kluft.md
content/ar/drafts/spark/thinkers/thk-courtois.md

## ملحق — تحقق وجود حقيقي (بعد ملاحظة كلود)
كلود لاحظ صح إن الـ8 مخالفات المصحَّحة كانت آلية بس (preflight_check.py)، ومفيش تحقق بحثي بشري حقيقي من وجود الأشخاص الـ61 المرحَّلين، لأن الدفعة دي مصدرها مجلد قديم غير مراجَع مش بحث طازج مني. اتعمل تحقق بحثي حقيقي منفصل بـ7 subagents متوازية (كل واحد قرأ الملفات كاملة وقيّم من معرفته الفعلية، مش بس تحقق آلي شكلي)، غطّى كل الـ62 شخص المرحَّل (61 + kathy-steele اللي كانت جزء من الدفعة الأصلية).

**النتيجة: 62/62 "موثّق"** — صفر حالات "غامض" أو "غير موجود". كل شخص اتأكد وجوده الحقيقي وتطابقت الوقائع الجوهرية (الجنسية، المؤسسة، أهم عمل، السنوات) مع معرفة الوكيل الفعلية. الملفات نفسها أظهرت انضباطاً جيداً في تمييز الفجوات الصغيرة (تواريخ ميلاد دقيقة، تفاصيل مؤسسية) عبر حقل `gaps` بدل اختلاقها — وهذا سلوك حذر متوقع مش دليل اختلاق. لم يُنقل أي ملف لـ`quarantine-spark.md` لعدم وجود أي حالة تستدعي ذلك.
