# Task 2.25
الحالة: مكتمل
العملية: تحقّق وجود (Task 2) على 22 ملف مفكر — موثّق / غير موجود (حجر) / غامض | الملفات: 22

## الأرقام
جمل القائمة السوداء متبقية: قبل 18 (تقريباً، موزّعة على gaps ونصوص "اقتباسات مختارة") → بعد 0
ملفات فيها ## المصادر: قبل 9/22 → بعد 22/22
ملفات مُحجَّرة (تعارض slug/هوية): قبل 0 → بعد 2 (thk-rsperry، thk-sgreys)
edges.belongs_to بنص حر بدل slug حقيقي: قبل 7 → بعد 0 (صُحِّحت لـslugs حقيقية أو حُذفت + سُجّلت في missing-schools.md)

## أمر التحقق
`python3 scripts/task.py verify minimax 2.25` → جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 | فيها ## المصادر: 22 / 22
`python3 scripts/preflight_check.py <22 ملف>` → ✅ 22 ملف — صفر مخالفات آلية (exit code 0)

## قرارات اتخذتها
- **thk-vschroeter** (Vincentia Schroeter): موثّق. حذفت جملة القائمة السوداء من gaps، أضفت `## المصادر`.
- **thk-wmischel** (Walter Mischel): موثّق (تجربة المارشميلو، CAPS معروفان أكاديمياً). حذفت جملة القائمة السوداء، أضفت `## المصادر`. تحققت من مطابقة كل روابط `related` (axm-delayed-gratification، stu-mischel-marshmallow-test، thk-abandura، thk-jrotter).
- **thk-rsperry**: **حُجر** — الاسم "روبرت سبيري" (Robert Sperry) غير موجود كمؤلف أدلري. بحث ويب (2026-08-27) أثبت أن الببليوغرافيا الفعلية المذكورة في الملف (Adlerian Psychopathology، Adlerian Couples and Family Counseling، إلخ) هي لـ**لن سبيري (Len Sperry)**، طبيب نفسي حقيقي وأستاذ متفرغ FAU. لم أعِد تسمية المحتوى تحت هذا الـslug لأن الحرف الأول "r" لا يطابق "Len" (l) إطلاقاً (تحذير القاعدة 6 صراحة). نقلت النسخة الأصلية لـ archive، حوّلت الملف الحي لقالب حجر موحّد، وسجّلت طلب slug جديد `thk-lsperry` في requests-minimax.md.
- **thk-mmeade** (Michael Meade): موثّق (راوي قصص ومحلل يونغي أمريكي حقيقي، مؤسس Mosaic Multicultural Foundation). حذفت جملة القائمة السوداء من gaps.
- **thk-marcuse** (Herbert Marcuse): موثّق سلفاً بمصادر واقتباس حقيقي؛ لا تعديل جوهري لازم، تحققت من مطابقة `related` (thk-heidegger، con-alienation، con-freedom، thk-adorno) — كلها مطابقة.
- **thk-rdreikurs** (Rudolf Dreikurs): موثّق. صحّحت `edges.belongs_to` من نص حر "علم النفس الفردي الأدلري" إلى slug حقيقي `br-adlerian`. أزلت رابط `thk-rmanaster` من `related` لأن الملف المستهدف حُجر في هذه الدفعة (رايتشل ماناستر غير موثّقة). أزلت أيضاً رابط `thk-dgray` — الـslug له نسختان متعارضتا العنوان بين المعتمد (مارتن ديك) ومسودة Spark (مارتن غراي)، ضمن الـ464 تعارض slug الموثّقة في EXISTING_SLUGS.md.
- **thk-stoics** (الرواقيون): تيار فلسفي جماعي (سينيكا، إبيكتيتوس، ماركوس أوريليوس) لا شخص فرد — سجّلت هذا في `gaps` كملاحظة تصنيفية تحتاج قراراً لاحقاً (تقسيم لملفات أفراد + مدرسة، أم إبقاء كملخص جماعي)، ولم أعالجه كسيرة فردية. أضفت `## المصادر`. تحققت من مطابقة كل روابط `related`.
- **thk-rjohnson** (Robert A. Johnson): موثّق (محلل يونغي أمريكي حقيقي، مؤلف "He/She/We/Inner Work"). حذفت جملة القائمة السوداء، أضفت `## المصادر`.
- **thk-prochaska** (James O. Prochaska): موثّق (النموذج العابر للنظريات، TTM، معروف أكاديمياً مع كارل دي كليمنتي). حذفت جملة القائمة السوداء. حذفت `edges.belongs_to` لأن "التكاملية/الانتقائية" (بالمعنى العلاجي المعاصر) لا يقابلها slug حقيقي (sch-eclecticism الموجود عن الانتقائية الهلنستية-الرومانية القديمة فقط) — سجّلتها في missing-schools.md. نظّفت `gaps` من إدخالات متناقضة كانت تدّعي إزالة روابط (boscolo، hohagen، إلخ) بينما الملفات موجودة فعلياً بslugs صحيحة الآن. لم أُبقِ رابط `thk-diclemente` رغم أنه شريك التأسيس الفعلي — الـslug له نسختان متعارضتا العنوان بين المعتمد (كارل دي كليمنتي) ومسودة Spark (كارلو دي كليمنتي)، ضمن الـ464 تعارض slug الموثّقة في EXISTING_SLUGS.md؛ سجّلت هذا في gaps.
- **thk-mendelssohn** (Moses Mendelssohn): موثّق سلفاً بمصادر كافية؛ تحققت من مطابقة `related` (sch-haskalah، sch-judaism-reform) — مطابقة.
- **thk-weizsacker** (Viktor von Weizsäcker): موثّق. حذفت جملة القائمة السوداء من gaps.
- **thk-msolms** (Mark Solms): موثّق (مؤسس علم النفس العصبي التحليلي). حذفت جملة القائمة السوداء. صحّحت `edges.belongs_to` الثاني من نص حر "علم النفس العصبي التحليلي" إلى slug حقيقي `br-neuropsychoanalysis`.
- **thk-rkurtz** (Ron Kurtz، مؤسس Hakomi): موثّق. حذفت جملة القائمة السوداء من gaps **وأيضاً من متن قسم "## اقتباسات مختارة"** الذي كان يحمل الجملة السوداء ذاتها كنص — حذفت القسم بالكامل بدل استبداله بجملة بديلة. حذفت `edges.belongs_to` لأن "هاكومي (Hakomi)" لا يقابلها ملف مدرسة/تيار حقيقي في الأطلس — سجّلتها في missing-schools.md.
- **thk-mweissman** (Myrna Weissman): موثّقة (مؤسِّسة مشاركة لـIPT). حذفت جملة القائمة السوداء من gaps وحذفت قسم "اقتباسات مختارة" الذي كان يحمل نفس الجملة كمتن.
- **thk-novaco** (Raymond W. Novaco): موثّق. حذفت جملة القائمة السوداء من gaps.
- **thk-tgrisso** (Thomas Grisso): موثّق (MacCAT-T معروفة أكاديمياً). حذفت جملة القائمة السوداء. صحّحت `edges.belongs_to` من نص حر "تقييم المخاطر العلاجي" إلى slug حقيقي `br-therapeutic-risk-assessment`.
- **thk-wong** (Paul T. P. Wong): موثّق (علم النفس الوجودي الإيجابي، الموجة الثانية). حذفت جملة القائمة السوداء من gaps.
- **thk-mazdak** (مزدك): موثّق تاريخياً (مصلح ساساني، قُتل ~528م حسب الطبري وتاريخ إيران الساساني). أضفت `## المصادر` (الطبري، Cambridge History of Iran، Crone 1991).
- **thk-ogilvie** (Bruce C. Ogilvie): موثّق (أحد آباء علم نفس الرياضة الأمريكي). صحّحت `edges.belongs_to` من نص حر "علم نفس الرياضة" إلى slug حقيقي `br-sport-psychology`. حذفت رابطاً غير ذي صلة (`exp-derealization-depersonalization`) من `related` — لا علاقة له بمتن الملف. أضفت `## المصادر`.
- **thk-weisstub** (Eli Weisstub): موثّق (محلل يونغي، رئيس سابق لـISAP). صحّحت `edges.belongs_to` من نص حر "علم النفس التحليلي اليونغي" إلى slug حقيقي `br-jungian`. حذفت جملة القائمة السوداء من gaps وقسم الاقتباسات، أضيفت `## المصادر`.
- **thk-sgreys**: **حُجر** — المحتوى صحيح جوهرياً (دانيال أ. هيوز، مؤسس DDP، موثّق أكاديمياً بالكامل عبر بحث ويب 2026-08-27)، لكن الـslug "sgreys" لا يمتّ لاسمه بأي صلة إطلاقاً — علامة التحذير الصريحة في القاعدة 6. نقلت النسخة الأصلية لـ archive، حوّلت الملف الحي لقالب حجر، وسجّلت طلب slug جديد `thk-dhughes` في requests-minimax.md.
- **thk-rlewis** (Robert A. Lewis، Bioenergetics): موثّق. حذفت جملة القائمة السوداء من gaps، أضفت `## المصادر`.

## متوقف عنده (لرئيس التحرير)
- **thk-stoics**: قرار تصنيفي مطلوب — هل يُبقى كملف جماعي "الرواقيون" (كما هو حالياً)، أم يُقسَّم لملفات أفراد (thk-seneca، thk-epictetus، thk-marcus-aurelius) + ملف مدرسة sch-stoicism مستقل؟ تركته دون تفكيك لأن هذا خارج نطاق Task 2 (تحقق وجود)، لكن سجّلت الملاحظة في gaps.
- **thk-rsperry / thk-sgreys**: طلبا slug جديد (`thk-lsperry`، `thk-dhughes`) يبدآن بحرفين خارج نطاق MiniMax (m→z) — يحتاجان مساراً منفصلاً (Spark أو كلود) لكتابة السيرتين الحقيقيتين لاحقاً. المحتوى الأصلي محفوظ كاملاً في archive.
- **missing-schools.md**: أُضيفت 3 مدارس/تيارات غائبة من هذه الدفعة (هاكومي، التكاملية/الانتقائية المعاصرة، وتأكيد موجود سلفاً لعلم نفس الأداء الرياضي) — تحتاج Task 13 لكتابتها.

## الملفات
content/ar/thinkers/thk-vschroeter.md
content/ar/thinkers/thk-wmischel.md
content/ar/thinkers/thk-rsperry.md
content/ar/thinkers/thk-mmeade.md
content/ar/thinkers/thk-marcuse.md
content/ar/thinkers/thk-rdreikurs.md
content/ar/thinkers/thk-stoics.md
content/ar/thinkers/thk-rjohnson.md
content/ar/thinkers/thk-prochaska.md
content/ar/thinkers/thk-mendelssohn.md
content/ar/thinkers/thk-weizsacker.md
content/ar/thinkers/thk-msolms.md
content/ar/thinkers/thk-rkurtz.md
content/ar/thinkers/thk-mweissman.md
content/ar/thinkers/thk-novaco.md
content/ar/thinkers/thk-tgrisso.md
content/ar/thinkers/thk-wong.md
content/ar/thinkers/thk-mazdak.md
content/ar/thinkers/thk-ogilvie.md
content/ar/thinkers/thk-weisstub.md
content/ar/thinkers/thk-sgreys.md
content/ar/thinkers/thk-rlewis.md
