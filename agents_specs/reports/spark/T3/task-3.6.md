# Task 3.6
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-bromberg، thk-bonaventure)
- **أخطر اكتشاف في الدفعة: thk-boscolo** — أسماء مؤسسي "مجموعة ميلانو" الأربعة كانت **مختلَقة بالكامل**: "سلفيانو برلين" و"مارتا برلين" (زوجان وهميان) و"فرانشيسكا تشيكين" بدل الأسماء الحقيقية الموثقة (مارا سلفيني بالاتزولي، جيانفرانكو تشيكين، جوليانا براتا) — صُححت الأربعة، وصُحح اسم شريك بوسكولو اللاحق من "برترام جيلينجن" (غير موجود) إلى باولو برتراندو الحقيقي.
- **أخطاء نسبة جسيمة أخرى**:
  - `thk-calkins`: عناوين إنجليزية مقرونة بعناوين عربية غير مطابقة إطلاقاً لكل أعمالها؛ وادعاء "تتلمذ هاري ستاك سوليفان عليها" — نسبة تأثير مختلَقة بالكامل لا مصدر لها، حُذفت.
  - `thk-brentano`: أربعة كتب لفِخنر وفونت وهلمهولتز ولوتسه كانت مرتبطة به في `related` وكأنها له — حُذفت جميعاً، أُبقي فقط عمله الحقيقي.
  - `thk-brapp`: نموذج ACT نُسب لتطويره مع باحثين آخرين، بينما المطورين الحقيقيين هما ليونارد شتاين وماري آن تِست — صُحح ليقتصر إسهامه على نموذج مواطن القوة الموثّق.
  - `thk-brene-brown`: باحثة وهمية "جون براون لويس" بدل هيلين بلوك لويس الحقيقية (المذكورة صح في فقرة أخرى من نفس الملف).
  - `thk-brian-aleman`: خلط هوية كامل بين براين ألمان وديف إلمان (شخص آخر له ملف مستقل وتقنية موثقة باسمه).
  - `thk-brianweiss`: ربط غير موثق بـ"إعادة الولادة" بدل استرجاع ذكريات الحياة السابقة الموثّق فعلاً.
- **تعارض عابر للتاسكات — نمط متكرر مؤكَّد الآن في 4 ملفات إضافية**: `thk-brianweiss` (3 أشخاص محجورين: `thk-connie-rae-anderson`, `thk-jim-ackerman`, `thk-katie-rae`)، `thk-bwilson` (تناقض gaps/related داخلي مشابه لنمط bhellinger من دفعة 3.5). **هذا يرفع إجمالي الاكتشافات لهذا النمط إلى 10+ ملفات عبر 3 دفعات متتالية (3.5، 3.6) — يستدعي فحصاً آلياً شاملاً بدل الاكتشاف العرضي.**
- تصحيحات تواريخ: `thk-buddha` (`active_start/end` كانا لا يطابقان `dates` ولا أي تأريخ مذكور فعلياً في الملف)، `thk-borgmann` (`active_end` كان يقطع 24 سنة من نشاطه).
- تكرارات محتملة موثّقة (بلا حذف): `thk-boyesen`/`thk-bboyesen`، `thk-bvanfraassen`/`thk-bas-van-fraassen`، `thk-bvdkolk`/`thk-besselvanderkolk`.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{bonaparte,bookchin,borgmann,boscolo,boss,bostrom,boszormenyi,bowlby,boyesen,bperry,brapp,brene-brown,brentano,breuer,brian-aleman,brianweiss,brihaspati,buddha,bugental,buhler,bultmann,burlingham,burton,butler,buytendijk,bvanfraassen,bvdkolk,bwiederhold,bwilson,cabral,caldwell,calkins,cambray}.md
→ ✅ 33 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء (الآن مغطاة آلياً في preflight_check.py المحدَّث)، تصحيح `edges.belongs_to` من نص حر لslug حقيقي، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة.

## متوقف عنده (لرئيس التحرير)
- **نمط "روابط محجورة لسه فعّالة" مؤكَّد الآن على نطاق واسع (10+ حالة عبر دفعتين متتاليتين)** — يستحق سكريبت فحص شامل يمسح كل `content/ar/drafts/spark/` و`content/ar/drafts/minimax/` بحثاً عن أي `related.id` يطابق slug في `quarantine-spark.md` أو `quarantine-minimax.md`، بدل انتظار اكتشاف كل subagent له بالصدفة.
- **thk-boscolo**: تصحيحات الأسماء (Selvini Palazzoli/Cecchin/Prata/Bertrando) مبنية على معرفة تاريخية عامة موثقة جيداً، لكن التواريخ (1932–2013) غير مؤكدة من مصدر أولي — يستحق أولوية عالية في المراجعة البشرية نظراً لحجم الاختلاق المكتشف.
- **thk-calkins**: حذف ادعاء "تتلمذ سوليفان عليها" — نوعية الخطأ (اختراع صلة تأثير بين شخصيتين حقيقيتين) أخطر من أخطاء الإسناد المعتادة، يستحق تنبيهاً خاصاً.
- **thk-bperry**: حُذف الشق الكندي من هويته (كندي-أمريكي → أمريكي فقط) لعدم توفر مصدر؛ لو ثبت لاحقاً ارتباط كندي حقيقي يحتاج تصحيحاً عكسياً.
- طلب `sch-popular-psychology` (من thk-brene-brown) يؤثر على عدة ملفات أخرى (thk-berne سابقاً، وربما napoleon-hill/bob-proctor) — يستحق معالجة جماعية بدل تكرار الطلب.

## الملفات
content/ar/thinkers/thk-bonaparte.md
content/ar/thinkers/thk-bonaventure.md
content/ar/thinkers/thk-bookchin.md
content/ar/thinkers/thk-borgmann.md
content/ar/thinkers/thk-boscolo.md
content/ar/thinkers/thk-boss.md
content/ar/thinkers/thk-bostrom.md
content/ar/thinkers/thk-boszormenyi.md
content/ar/thinkers/thk-bowlby.md
content/ar/thinkers/thk-boyesen.md
content/ar/thinkers/thk-bperry.md
content/ar/thinkers/thk-brapp.md
content/ar/thinkers/thk-brene-brown.md
content/ar/thinkers/thk-brentano.md
content/ar/thinkers/thk-breuer.md
content/ar/thinkers/thk-brian-aleman.md
content/ar/thinkers/thk-brianweiss.md
content/ar/thinkers/thk-brihaspati.md
content/ar/thinkers/thk-bromberg.md
content/ar/thinkers/thk-buddha.md
content/ar/thinkers/thk-bugental.md
content/ar/thinkers/thk-buhler.md
content/ar/thinkers/thk-bultmann.md
content/ar/thinkers/thk-burlingham.md
content/ar/thinkers/thk-burton.md
content/ar/thinkers/thk-butler.md
content/ar/thinkers/thk-buytendijk.md
content/ar/thinkers/thk-bvanfraassen.md
content/ar/thinkers/thk-bvdkolk.md
content/ar/thinkers/thk-bwiederhold.md
content/ar/thinkers/thk-bwilson.md
content/ar/thinkers/thk-cabral.md
content/ar/thinkers/thk-caldwell.md
content/ar/thinkers/thk-calkins.md
content/ar/thinkers/thk-cambray.md
