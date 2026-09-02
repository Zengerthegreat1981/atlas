# Task 2.44
الحالة: مكتمل
العملية: تحقق وجود + إصلاح انتهاكات القائمة السوداء وروابط related/edges غير صحيحة | الملفات: 10

## الأرقام
مخالفات القائمة السوداء: قبل 8 → بعد 0
مخالفات preflight_check: قبل 1 (title مضاد في thk-sun-bin) → بعد 0
edges بslug وهمي (نص عربي حر بدل slug حقيقي): قبل 3 (thk-tali-sharot, thk-uri-gneezy, thk-vsatir) → بعد 0
related بtitle متضارب مع الملف المستهدف: قبل 3 (thk-thomas-more/thk-erasmus، thk-tali-sharot/wrk-optimism-bias، thk-sun-bin/con-just-war...) → بعد 0
related بلا سبب في المتن: قبل 1 (thk-uri-gneezy/wrk-predictably-irrational) → بعد 0 (حُذف)

## أمر التحقق
`python3 scripts/preflight_check.py <الملفات العشرة>` → ✅ 10 ملف — صفر مخالفات آلية
grep يدوي على الـ17 جملة من القائمة السوداء على الملفات العشرة → 0 تطابق

## قرارات اتخذتها
- thk-thomas-more.md: **موثّق**. توماس مور (1478–1535) شخصية حقيقية موثقة جيداً (يوتوبيا 1516). حذفت جملة القائمة السوداء من gaps (كانت متناقضة مع وجود اقتباس حقيقي في المتن)، وصححت title الرابط لـthk-erasmus من "إيراسموس" إلى العنوان الفعلي "دسيديريوس إراسموس".
- thk-ummasvati.md: **موثّق**. أشاريا أومسفاتي (الجاينية، ق2–3م) موثق. حذفت جملة القائمة السوداء من gaps (المتن فيه اقتباس حقيقي فعلاً) واستبدلتها بفجوة حقيقية عن خلاف التأريخ.
- thk-tali-sharot.md: **موثّق**. تالي شاروت باحثة معاصرة حقيقية موثقة (UCL). حذفت قسم الاقتباسات بالكامل (كان يحتوي فقط جملة القائمة السوداء)، وصححت title الرابط wrk-optimism-bias، وحذفت edges.belongs_to الذي كان نصاً عربياً حراً بدل slug (لا يوجد ملف مدرسة "علم الأعصاب الإدراكي والانفعالي") وسجّلته في missing-schools.md.
- thk-thomas-reid.md: **موثّق**. توماس ريد (1710–1796) مؤسس مدرسة الحس المشترك الاسكتلندية، موثق جيداً وedges.belongs_to (sch-scottish-common-sense) صحيح. حذفت قسم الاقتباسات (جملة قائمة سوداء فقط) وصححت gaps.
- thk-wasil-ibn-ata.md: **موثّق**. واصل بن عطاء مؤسس المعتزلة، موثق جيداً. حذفت قسم الاقتباسات، وحذفت من gaps سطرين كانا متكررين/عفا عليهما الزمن (أحدهما يطلب slug "sch-mutazilism" رغم أن sch-mutazila الصحيح موجود بالفعل في edges، والآخر يكرر حقيقة موجودة أصلاً في المتن).
- thk-uri-gneezy.md: **موثّق**. أوري غنيزي باحث اقتصاد سلوكي معاصر حقيقي وموثق (UCSD). حذفت قسم الاقتباسات، وحذفت edges.belongs_to (نص حر بدل slug، سُجّل في missing-schools.md)، وحذفت related.wrk-predictably-irrational لأن الكتاب (لدان أريلي) غير مذكور في المتن أصلاً ولا صلة موثقة بينه وبين غنيزي — انتهاك معيار القبول رقم 4.
- thk-vsatir.md: **موثّق** (تحقق مسبق من عدم الازدواج — لا يوجد slug تانٍ لفرجينيا ساتير في EXISTING_SLUGS.md غير thk-vsatir، فقط thk-vyasatirtha لشخص آخر تماماً). صححت title الرابط met-freud-iceberg (كان "استعارة الجبل الجليدي" والعنوان الفعلي "الجبل الجليدي: استعارة الوعي واللاوعي التحليلي")، وصححت diacritics thk-rbandler، وحذفت edges.developed→br-humanistic-family لأن الملف غير موجود فعلاً (سُجّل في missing-schools.md، والفجوة كانت موثقة أصلاً في gaps).
- thk-malebranche.md: **موثّق**. نيكولا مالبرانش (1638–1715) رائد الأوكازيونالية، موثق جيداً وedges صحيح. حذفت قسم الاقتباسات وصححت gaps.
- thk-sun-bin.md: **موثّق**. سون بن قائد عسكري صيني تاريخي (نص مكتشف 1972). لا مخالفات قائمة سوداء حرفية، لكن preflight_check رصد تضارب title في related (con-just-war-theory-jus-ad-bellum) فصححته ليطابق عنوان الملف الفعلي. عدّلت صياغة gap عن الاقتباس لتكون أدق (النص المكتشف لم يُترجم كاملاً) بدل صياغة قريبة من القائمة السوداء.
- thk-proclus.md: **موثّق**. بروكلس (412–485م) آخر كبار الأفلاطونية المحدثة، موثق جيداً وedges (sch-neoplatonism) وrelated (thk-plotinus) صحيحان. حذفت قسم الاقتباسات وصححت gaps (كانت الفجوة القديمة تكرر حقيقة موجودة أصلاً في المتن عن Liber de Causis).

جميع الملفات العشرة أشخاص حقيقيون موثقون بمصادر أساسية معروفة (لا حالات "غير موجود" ولا "غامض" ولا ازدواج فعلي في هذه الدفعة) — لم يُحتَج لتسجيل أي منها في quarantine-minimax.md.

## متوقف عنده (لرئيس التحرير)
لا يوجد.

## الملفات
- content/ar/thinkers/thk-thomas-more.md
- content/ar/thinkers/thk-ummasvati.md
- content/ar/thinkers/thk-tali-sharot.md
- content/ar/thinkers/thk-thomas-reid.md
- content/ar/thinkers/thk-wasil-ibn-ata.md
- content/ar/thinkers/thk-uri-gneezy.md
- content/ar/thinkers/thk-vsatir.md
- content/ar/thinkers/thk-malebranche.md
- content/ar/thinkers/thk-sun-bin.md
- content/ar/thinkers/thk-proclus.md
