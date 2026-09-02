# Task 2.46
الحالة: مكتمل
العملية: تحقق وجود + إزالة جمل القائمة السوداء + تصحيح edges/related/تواريخ لعشرة مفكرين (thk-m→z) | الملفات: 10

## الأرقام
جمل قائمة سوداء (حرفية في المتن/gaps): قبل 10 (واحدة في كل ملف من العشرة) → بعد 0
edges.belongs_to بنص حر بدل slug: قبل 2 (thk-richard-davidson، thk-mark-manson) → بعد 0 (edges: [] + تسجيل في missing-schools.md)
edges.belongs_to بslug خاطئ منسوخ من نص حر: قبل 1 (thk-roy-baumeister) → بعد 1 صحيح (sch-social-psychology)
related بعنوان مضطرب لا يطابق الملف المستهدف: قبل 5 (thk-pyrrho، sch-mbct، wrk-subtle-art، thk-nagarjuna، thk-mohammed-abed-al-jabri) → بعد 0 (2 صُححت العناوين، 1 حُذف بلا مبرر في المتن — sch-mbct من thk-richard-davidson)
related بلا مبرر مذكور في المتن: قبل 1 (thk-richard-bernstein في thk-richard-davidson — التباس اسم مع Richard J. Davidson، لا صلة فعلية) → بعد 0 (حُذف)
أخطاء وقائعية/منطقية فادحة أُصلحت: 1 (thk-richard-davidson كان يقول إنه "تعاون مع Richard J. Davidson نفسه، لا تداخل" — جملة عبثية حُذفت، وحُذف كتاب غير موثّق "Mindfulness Is Better Than Chocolate" وادعاء تاريخ تأسيسي غير مؤكد 1992)
سنوات بعد active_end بلا إشارة "بعد وفاته": قبل 2 (thk-machiavelli: 1532، 1970) → بعد 0
ملفات بلا "## المصادر": قبل 10 → بعد 10 (أُضيف قسم 2–3 مراجع حقيقية عن الشخص نفسه لكل ملف)

## أمر التحقق
`python3 scripts/preflight_check.py <الملفات العشرة>` → ✅ 10 ملف — صفر مخالفات آلية (exit 0)
grep يدوي على جمل القائمة السوداء الـ17 كاملة عبر الملفات العشرة → 0 تطابق

## قرارات اتخذتها
- thk-qadi-abd-al-jabbar: **موثّق**. متكلم معتزلي حقيقي موثّق (935/936–1025م)، شيخ المعتزلة البهشمية، صاحب «المغني». حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ (لا يوجد اقتباس منسوب موثّق)، أُضيف `## المصادر` (Schmidtke، Hourani، Frank)، وأُضيفت جملة تبرير رابط `br-mutazila-basra` في المتن (انتماء البهشمية لمدرسة البصرة الكلامية).
- thk-sextus-empiricus: **موثّق**. فيلسوف شكوكي هيلينستي حقيقي، الملف كان جيداً أصلاً وفيه اقتباس حقيقي موثّق. حُذفت جملة قائمة سوداء زائدة من gaps (كانت متناقضة مع وجود اقتباس حقيقي في المتن)، صُحّح عنوان `thk-pyrrho` في related من "بيرون" إلى "بيرون الإليسي" ليطابق عنوان الملف المستهدف فعلياً، أُضيف `## المصادر`.
- thk-max-horkheimer: **موثّق**. مؤسس مدرسة فرانكفورت، شخصية تاريخية مؤكدة تماماً. حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ، أُضيف `## المصادر` (Wiggershaus، هوركهايمر نفسه، SEP).
- thk-richard-davidson: **موثّق** (تحققت من الازدواج أولاً في EXISTING_SLUGS.md — لا يوجد slug آخر له، متمايز تماماً عن thk-donald-davidson وthk-ldavidson). عالم أعصاب معاصر حقيقي، أستاذ في ويسكونسن-ماديسون ومؤسس Center for Healthy Minds. أخطاء وُجدت وأُصلحت: (1) `edges.belongs_to` كان نصاً حراً غير slug — حُوّل لـ`edges: []` وسُجّلت مدرسة "علم الأعصاب الإيجابي/علم أعصاب التأمل" الغائبة في missing-schools.md، (2) رابط `thk-richard-bernstein` في related بلا أي مبرر في المتن ولا صلة حقيقية (فيلسوف أمريكي مختلف تماماً) — حُذف، (3) رابط `sch-mbct` بلا مبرر كافٍ في المتن (عمله عن MBSR لا MBCT تحديداً) — حُذف، (4) جملة عبثية في المتن تزعم تعاونه مع "Richard J. Davidson نفسه، لا تداخل" — حُذفت وأُصلحت الصياغة، (5) كتاب غير موثّق "Mindfulness Is Better Than Chocolate" حُذف من أهم الأعمال، (6) تاريخ تأسيس غير مؤكد (1992) لمركز Healthy Minds حُذف واستُبدل بوصف عام غير مؤرَّخ. أُضيف `## المصادر`.
- thk-mark-manson: **موثّق**. كاتب تنمية ذاتية معاصر حقيقي وموثّق إعلامياً. حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ، `edges.belongs_to` كان نصاً حراً — حُوّل لـ`edges: []` وسُجّلت مدرسة "علم النفس الشعبي والتنمية الذاتية" الغائبة في missing-schools.md، صُحّح عنوان `wrk-subtle-art` في related ليطابق العنوان الكامل الفعلي للملف، أُضيف `## المصادر`.
- thk-machiavelli: **موثّق**. شخصية تاريخية مؤكدة تماماً. حُذفت جملة القائمة السوداء الزائدة من gaps (الملف فيه اقتباسان حقيقيان موثّقان أصلاً)، أُضيفت إشارة "بعد وفاته" قبل ذكر سنتي 1532 (نشر الأمير) و1970 (مقياس Mach-IV) لأن active_end=1527، أُضيفت جملة تبرير رابط `thk-hobbes` في المتن (تأثر هوبز بواقعيته السياسية)، أُضيف `## المصادر`.
- thk-vasubandhu: **موثّق**. فيلسوف بوذي هندي حقيقي (يوغاكارا، ق.4-5م). حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ، صُحّح عنوانا `sch-yogacara` و`thk-nagarjuna` في related ليطابقا عنواني الملفين المستهدفين فعلياً، أُضيف `## المصادر` (Frauwallner، Anacker، SEP).
- thk-mohammed-arkoun: **موثّق**. مفكر إسلامي جزائري-فرنسي حقيقي وبارز (تحققت من EXISTING_SLUGS.md — slug واحد فقط، لا ازدواج). حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ، صُحّح عنوان `thk-mohammed-abed-al-jabri` في related من "الجابري" إلى "محمد عابد الجابري" ليطابق عنوان الملف الفعلي، أُضيف `## المصادر` (Lee، أركون نفسه مترجَماً، Günther).
- thk-roy-baumeister: **موثّق**. عالم نفس اجتماعي حقيقي معروف عالمياً. حُذفت جملة القائمة السوداء من gaps والمتن، حُذف قسم اقتباسات فارغ، `edges.belongs_to` كان نصاً حراً — حُوّل إلى slug حقيقي موجود فعلاً كملف: `sch-social-psychology`، صُحّح عنوان `wrk-willpower-baumeister` في related ليطابق العنوان الكامل الفعلي للملف، أُضيف `## المصادر` (باوميستر وتيرني، الدراسة الأصلية 1998، دراسة التكرار Hagger 2016 المذكورة في المتن أصلاً).
- thk-porphyry: **موثّق**. فيلسوف أفلاطوني محدث حقيقي، تلميذ أفلوطين. حُذفت جملة القائمة السوداء الزائدة من gaps (الملف فيه اقتباس حقيقي موثّق أصلاً)، أُضيف `## المصادر` (Smith، SEP، ترجمة الإيساغوجي).

## متوقف عنده (لرئيس التحرير)
- لا يوجد.

## الملفات
content/ar/thinkers/thk-qadi-abd-al-jabbar.md
content/ar/thinkers/thk-sextus-empiricus.md
content/ar/thinkers/thk-max-horkheimer.md
content/ar/thinkers/thk-richard-davidson.md
content/ar/thinkers/thk-mark-manson.md
content/ar/thinkers/thk-machiavelli.md
content/ar/thinkers/thk-vasubandhu.md
content/ar/thinkers/thk-mohammed-arkoun.md
content/ar/thinkers/thk-roy-baumeister.md
content/ar/thinkers/thk-porphyry.md
