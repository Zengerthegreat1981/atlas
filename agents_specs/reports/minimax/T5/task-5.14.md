# Task 5.14
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/) | الملفات: 40

## الأرقام
مخالفات preflight: 0 (كل الوكلاء شغّلوا preflight_check.py بأنفسهم قبل التسليم — أول دفعة تخلص بدون جولة تصحيح إضافية مني)
belongs_to/evolved_from/founded_by نصية حرة عولجت: ~15
  - تحويل فعلي لـslug موجود: 7 — sch-kogaku→sch-neoconfucianism، sch-kabbalah→sch-hebrew-wisdom، sch-karaite→sch-hebrew-wisdom، sch-judaism-andalusian→sch-islamic-peripatetic، sch-judaism-existential→sch-phenomenology
  - حُذف الرابط (فئة عامة/دائري/خطأ تصنيف جغرافي): sch-interculturalidad، sch-kaupapa-maori ("تقليد أمريكي أصلي" لشعب بولينيزي — خطأ تصنيف جغرافي فعلي)، sch-kokugaku (دائري: كوكوغاكو هي حرفياً "الدراسات الوطنية")
  - **إصلاحان يدويان إضافيان بعد التسليم:** sch-islamic-peripatetic.md كانت belongs_to تشاور على نفسها (self-loop)، وsch-islamic-psychology.md كانت belongs_to تشاور على slug غير موجود (sch-islamic-psychology-tradition) — preflight ما كانش هيمسكهم لأن الصيغة شكلها slug صحيح. حذفتهم يدوياً.
  - تسجيل مدارس/مظلات حقيقية بلا ملف: ~10 سطور جديدة (فرع MAP الإيطالي لـISTDP، الباطنية الإسلامية، علم النفس النقدي، الفكر الإسلامي الحديث [دمج]، النسوية الفلسفية [دمج]، التقاليد الشايفية)
تصحيحات هوية خطيرة:
  - **sch-kantian-ethics-contemporary.md:** id `thk-sullivan` مربوط باسم "روجر سوليفان" (فيلسوف كانطي) لكن الملف الفعلي وراءه **هاري ستاك سوليفان** (طبيب نفسي). حُذف الرابط، ووُثّق في gaps.
  - **thk-mweissman.md:** اسمها الحقيقي "ميرنا وايسمان" لكن الملف مكتوب "ميري وايسمان" — خطأ في الملف نفسه (خارج نطاق schools/، أُبلغ فقط).
  - **thk-hajime-tanabe / thk-tanabe-hajime:** ملفان منفصلان لنفس الشخص (تانابي هاجيمي، مدرسة كيوتو) — تكرار هوية كامل، خارج نطاق schools/ (في thinkers/)، أُبلغ فقط.
تصحيحات تأريخ حقيقية (مش مجرد صياغة): sch-latin-averroism.md (active_end 1530→1603، يتناقض مع محتواه نفسه) وsch-leibnizianism.md (active_end 1780→1831، محتواه يوثق لايبنزية هيغلية حتى وفاة هيغل).

## أمر التحقق
`python3 scripts/task.py verify minimax 5.14` → قائمة سوداء متبقية: **0** · سقّالة ظاهرة: 0 · `## المصادر`: 0/40
`python3 scripts/build_slug_index.py` → 6892 عنصر، 428 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- **sch-islamic-peripatetic.md وsch-islamic-psychology.md:** بعد تسليم الوكلاء preflight نظيف، لاحظت بمراجعتي إن عندهم belongs_to بصيغة slug شكلياً صحيحة لكن فاسدة منطقياً (ذاتية أو لملف غير موجود) — preflight ما بيفحصش صحة الوجود لصيغ sch-x. حذفتهم يدوياً.
- **sch-latin-averroism.md وsch-leibnizianism.md:** صححت active_end فعلياً (مش مجرد صياغة "بعد وفاته") لأن المحتوى نفسه يوثق نشاطاً بعد التاريخ المعلن — تصحيح تأريخي حقيقي.
- **sch-kaupapa-maori.md:** "تقليد أمريكي أصلي" خطأ تصنيف جغرافي فعلي (الماوري شعب بولينيزي من نيوزيلندا) — حُذف بدل التسجيل كمدرسة غائبة.

## متوقف عنده (لرئيس التحرير)
- **sch-ismaili.md:** belongs_to → sch-islamic-peripatetic (المشائية) غريب دلالياً — الإسماعيلية باطنية/أفلاطونية محدثة أساساً، مش مشائية. صيغة slug صحيحة فماعديتهاش (خارج يقيني الكافي للحذف بلا تأكيد).
- **خلط هوية thk-sullivan** (روجر سوليفان الكانطي ↔ هاري ستاك سوليفان الطبيب النفسي) في sch-kantian-ethics-contemporary.md.
- **خطأ اسم thk-mweissman.md** (ميري بدل ميرنا وايسمان) — يحتاج تصحيح في thinkers/.
- **تكرار هوية thk-hajime-tanabe / thk-tanabe-hajime** — ملفان لنفس الشخص، يحتاج دمج في thinkers/.
- الجمل القالبية والمصادر خارج نطاق Task 5.
- 428 تعارض slug قديمة، لم تُلمس.

## الملفات
content/ar/schools/sch-intercultural-philosophy.md
content/ar/schools/sch-interculturalidad.md
content/ar/schools/sch-intersectionality.md
content/ar/schools/sch-ipt.md
content/ar/schools/sch-isfahan.md
content/ar/schools/sch-ishraqiyya.md
content/ar/schools/sch-islamic-critical-thought.md
content/ar/schools/sch-islamic-feminism.md
content/ar/schools/sch-islamic-peripatetic.md
content/ar/schools/sch-islamic-psychology.md
content/ar/schools/sch-islamic-reform.md
content/ar/schools/sch-ismaili.md
content/ar/schools/sch-istdp.md
content/ar/schools/sch-jainism.md
content/ar/schools/sch-jodo-shinshu.md
content/ar/schools/sch-jonang.md
content/ar/schools/sch-judaism-andalusian.md
content/ar/schools/sch-judaism-existential.md
content/ar/schools/sch-judaism-hellenistic.md
content/ar/schools/sch-judaism-reform.md
content/ar/schools/sch-kabbalah-lurianic.md
content/ar/schools/sch-kabbalah.md
content/ar/schools/sch-kagyu.md
content/ar/schools/sch-kant-critical.md
content/ar/schools/sch-kantian-ethics-contemporary.md
content/ar/schools/sch-kaozheng.md
content/ar/schools/sch-karaite.md
content/ar/schools/sch-kashmir-shaivism.md
content/ar/schools/sch-kaupapa-maori.md
content/ar/schools/sch-kierkegaardian.md
content/ar/schools/sch-kogaku.md
content/ar/schools/sch-kokugaku.md
content/ar/schools/sch-korean-neoconfucian.md
content/ar/schools/sch-kyoto.md
content/ar/schools/sch-latin-averroism.md
content/ar/schools/sch-lebensphilosophie.md
content/ar/schools/sch-legalism.md
content/ar/schools/sch-leibnizianism.md
content/ar/schools/sch-liberation-philosophy.md
content/ar/schools/sch-liberation-psychology.md
