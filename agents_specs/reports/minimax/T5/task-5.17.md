# Task 5.17
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/) | الملفات: 40

## الأرقام
مخالفات preflight النهائية: 0 (كل الوكلاء شغّلوا preflight_check.py بأنفسهم لغاية "صفر مخالفات")
belongs_to/evolved_from/co_founded_by نصية حرة عولجت: ~20
  - تحويل فعلي لـslug موجود: 3 (sch-sikh-philosophy→sch-bhakti-movement، sch-sanlun/sch-sikolohiyang-pilipino وغيرها)
  - حُذف الرابط (فئة عامة/دائري/خطأ تصنيف): ~14
  - تسجيل مدارس/مظلات حقيقية بلا ملف: ~9 سطور جديدة (التقليد الشكّي اليوناني، الإصلاح البروتستانتي، الفلسفة الأخلاقية اليابانية، الشنتو كمظلة، روبرت هاربر REBT، الهوبزية)
تصحيحات هوية خطيرة (3 حالات جديدة):
  - **sch-quinean-naturalism.md:** `thk-goodman` هو فعلياً **بول غودمان** (مؤسس مشارك للجشطالت) مش **نيلسون غودمان** (فيلسوف تحليلي) — حُذف الرابط الخاطئ، أُبقي `thk-jgoodman` الصحيح.
  - **sch-scientific-realism.md:** ازدواج id لنفس الشخص (باس فان فراسن) بين `thk-bvanfraassen` و`thk-bas-van-fraassen` — أُبقي واحد وحُذف التكرار. كمان `gaps` كانت بتزعم غياب بوبر وفان فراسن رغم وجودهما فعلاً ومربوطين بالفعل — تناقض بين شك معلن وثقة ظاهرة (قاعدة 11)، حُذف.
  - **sch-social-ecology.md:** `gaps` كانت بتزعم غياب Murray Bookchin (thk-bookchin) رغم إن الملف موجود فعلاً ويشاور بـbelongs_to على sch-social-ecology نفسها — أُضيف الرابط الناقص وحُذف الـgap الخاطئ.
اكتشاف مهم (استعلام مباشر من التعليمات): **راجعت sch-social-contract.md بالتفصيل وتأكدت إنه مش مربوط بخطأ بـ"البنائية الاجتماعية" — الملف نظيف تماماً من الالتباس المكتشف سابقاً في rel-narrative-constructionist.md.**
تصحيحات تأريخية حقيقية (active_end): sch-rangaku.md (1862→1875)، sch-second-scholasticism.md (1750→1756)، sch-shakta-tantra.md (1800→"مستمر")، sch-shingaku.md (1885→1890).

## أمر التحقق
`python3 scripts/task.py verify minimax 5.17` → قائمة سوداء متبقية: **0** · سقّالة ظاهرة: 0 · `## المصادر`: 0/40
`python3 scripts/build_slug_index.py` → 6902 عنصر، 464 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- **3 خلطات هوية جديدة** (thk-goodman، ازدواج فان فراسن، thk-bookchin المفقود من related رغم وجوده) — أخطر من عناوين متضاربة عادية.
- **sch-social-contract.md:** تحقق مباشر بناءً على طلب صريح — الملف سليم، مفيش خلط مع social constructionism.
- ملاحظة تناسق: بعض الوكلاء سجّلوا "الفلسفة السياسية المعاصرة" كمظلة حقيقية (دفعة 5.12 و5.16) بينما وكلاء آخرون في هذه الدفعة (sch-radical-democracy، sch-rawlsianism) اعتبروها فئة عامة وحذفوها بلا تسجيل — عدم اتساق طفيف بين دفعات مختلفة، يستحق توحيد قرار لاحقاً (السطر الموجود في missing-schools.md يبقى صحيحاً لملفاته الأصلية).

## متوقف عنده (لرئيس التحرير)
- **sch-rebt.md:** احتمال خلط هوية `thk-dgreenberger` (دِنيز د. ديفيس) مقابل "دانيال ديفيد" الباحث المذكور فعلياً في المصادر — لم يُصحح (خارج يقين كافٍ)، يستحق فحص thinkers/.
- **sch-shingon.md:** المتن يستخدم مصطلح "Mandalorian Esotericism" (من Star Wars!) بدل مصطلح أكاديمي حقيقي — يحتاج تصحيح في Task 10 (تعميق).
- 9 مدارس/مظلات جديدة في missing-schools.md تنتظر Task 13.
- 464 تعارض slug قديمة، لم تُلمس.

## الملفات
content/ar/schools/sch-pyrrhonism.md
content/ar/schools/sch-pythagorean.md
content/ar/schools/sch-queer-theory.md
content/ar/schools/sch-quinean-naturalism.md
content/ar/schools/sch-radical-democracy.md
content/ar/schools/sch-rangaku.md
content/ar/schools/sch-rawlsianism.md
content/ar/schools/sch-realism-medieval.md
content/ar/schools/sch-rebt.md
content/ar/schools/sch-renaissance-humanism.md
content/ar/schools/sch-renaissance-naturalism.md
content/ar/schools/sch-renaissance-neoplatonism.md
content/ar/schools/sch-romanticism.md
content/ar/schools/sch-sage-philosophy.md
content/ar/schools/sch-sakya.md
content/ar/schools/sch-salafism-modern.md
content/ar/schools/sch-samkhya.md
content/ar/schools/sch-sanlun.md
content/ar/schools/sch-schelling.md
content/ar/schools/sch-scholasticism.md
content/ar/schools/sch-scientific-realism.md
content/ar/schools/sch-scotism.md
content/ar/schools/sch-scottish-common-sense.md
content/ar/schools/sch-second-scholasticism.md
content/ar/schools/sch-sensorimotor-psychotherapy.md
content/ar/schools/sch-seon.md
content/ar/schools/sch-shaiva-siddhanta.md
content/ar/schools/sch-shakta-tantra.md
content/ar/schools/sch-shingaku.md
content/ar/schools/sch-shingon.md
content/ar/schools/sch-shinto-philosophical.md
content/ar/schools/sch-shiraz.md
content/ar/schools/sch-shramana.md
content/ar/schools/sch-shuddhadvaita.md
content/ar/schools/sch-sikh-philosophy.md
content/ar/schools/sch-sikolohiyang-pilipino.md
content/ar/schools/sch-silhak.md
content/ar/schools/sch-social-contract.md
content/ar/schools/sch-social-darwinism.md
content/ar/schools/sch-social-ecology.md
