# Task 3.5
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد). تغطي فلاسفة تأسيسيين (بنثام، بيركلي، برجسون، برتراند راسل) وشخصيات إكلينيكية مؤسِّسة (إريك بيرن، بيون، بلويلر).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-bergson، thk-boethius)
- **أخطر ملف في الدفعة: thk-berne (إريك بيرن)** — 6+ أخطاء نسبة متراكمة: كتاب "I'm OK, You're OK" كان منسوباً له خطأً (فعلياً لتوماس هاريس)؛ أداة "OK Corral" نُسبت له رغم أنها طُوِّرت بعد وفاته (فرانكلين إرنست 1971)؛ "الجوع الخمسة" كانت تخلط نظريته بنظرية شوتز FIRO؛ لعبتان مختلفتان ("Rapo" و"NIGYYSOB") ملصقتان ببعض خطأً؛ اقتباس غير قابل للتوثيق حُذف نهائياً بدل تركه.
- **أخطاء هوية/جنس جسيمة في thk-bill-ohanlon**: `thk-jkim-berg` كان يشير لشخص باسم "جون كيم بيرغ" (ذكر) بينما الشخص الحقيقي إنسو كيم بيرغ (امرأة) — تعارض id/title وجنس معاً؛ عنوان فرعي "أهم أعمالها" كان بصيغة مؤنثة لشخص المفروض ذكر (بيل أوهانلون نفسه) — خلط داخلي بين الشخصين.
- **استحالات زمنية**: `thk-boethius-dacia` كانت تزعم أن ابن رشد (ت. 1198) اطّلع على أعماله (نشط 1270+) — فارق 70+ سنة، حُذفت الفقرة بالكامل.
- **أخطاء نسبة/تواريخ نشر**: `thk-bertrand-russell` (`active_end` كان يقطع 11 سنة من نشاطه)، `thk-bguerney` (`active_end: "مستمر"` رغم وفاته 2015)، `thk-bodunrin` (مسار أكاديمي كامل خاطئ + سنة وفاة مختلَقة).
- **تعارض عابر للتاسكات مكتشف بشكل نمطي**: **5 ملفات مختلفة** (`thk-bhellinger`, `thk-besselvanderkolk`, `thk-dfeinstein`, `thk-dchurch`, `thk-jdavid`, `thk-craig-henderson`) كانت لسه رابطة بأشخاص محجورين فعلياً في `quarantine-spark.md` من Task 2 (`thk-jjoyce`, `thk-albertellis-somatic`, `thk-cgarrett` ×2، `thk-aschultz`, `thk-brosen`) — بعضها كان `gaps` نفسها تدّعي زوراً أن الرابط "أُزيل" رغم بقائه فعلياً. **صُححت كل الحالات الـ6.** هذا نمط خطر (ادّعاء تنظيف بلا تنفيذ فعلي) يستحق فحصاً أوسع لاحقاً.
- محتوى مختلَق حُذف بالكامل: `thk-bob-proctor` (اسم مؤلف خاطئ، ادعاء نقد أكاديمي غير موثّق، قائمة "قوانين" مبالغ فيها)، `thk-bill-ohanlon` (كتاب بمؤلفة مختلقة، نسبة سنة مقلوبة).
- **مرشح لـTask 2 (هوية مشكوكة)**: `thk-bobbeck` — لا تواريخ ولا منشور واحد موثّق، الصلة بأي شخص حقيقي موثق (روبرت سي. بيك، فيزيائي) غير مؤكدة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{bentham,berkeley,bernardo-chartres,berne,bernfeld,bertrand-russell,besselvanderkolk,beutler,bfredrickson,bguerney,bhartrhari,bhellinger,bhooks,biko,bill-devall,bill-ohanlon,bion,bj-fogg,bjoseph,blanchot,blankenburg,blbettner,bleuler-jung-assoc,bleuler,bloch,boadella,bob-proctor,bobbeck,bodhidharma,bodunrin,boethius-dacia,bohanlon,bolen,dfeinstein,dchurch,jdavid,craig-henderson}.md
→ ✅ 37 ملف — صفر مخالفات آلية (يشمل الملفات الأربعة المصححة من دفعات سابقة: dfeinstein, dchurch, jdavid, craig-henderson).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي (أو حذفه مع تسجيل طلب في requests-spark.md عند غياب slug مناسب)، حذف روابط `related` بلا سبب مذكور بالمتن، وتصحيحات id/title متضاربة (`thk-gfrege`, `thk-mahoney`, `thk-gold`, `thk-mseligman`, `thk-hountondji`, `thk-wiredu`, `thk-fromm`, `thk-zsegal`/`thk-segal`).

## متوقف عنده (لرئيس التحرير)
- **نمط "ادّعاء تنظيف بلا تنفيذ"**: عدة ملفات كانت `gaps` تدّعي فيها أن رابطاً محجوراً "أُزيل" رغم بقائه فعلياً في `related`. صُححت الحالات المكتشفة (6) لكن يستحق فحصاً شاملاً آلياً عبر كل `drafts/spark/` (وربما `drafts/minimax/`) بدل الاعتماد على الاكتشاف العرضي دفعة بدفعة.
- **thk-bobbeck**: مرشح مباشر لتطبيق معيار Task 2 (موثّق/غير موجود/غامض).
- **thk-bohanlon ↔ thk-bill-ohanlon**: احتمال قوي جداً أنهما نفس الشخص (وليام هدسون أوهانلون) بملفين منفصلين. يحتاج قرار دمج.
- **thk-berne**: التصحيحات الستة معتمدة على معرفة عامة موثقة بأدبيات التحليل التفاعلي لا مصدر أولي داخل المشروع — يستحق مراجعة إضافية بمصدر ثانوي قبل الترقية.
- **thk-beutler**: لا يوجد slug لمدرسة "تكامل العلاج النفسي" (`sch-psychotherapy-integration` مقترح في requests-spark.md) — الملف بلا `belongs_to` حتى يُبتّ.
- **thk-bertrand-russell / thk-bguerney**: تصحيحات `active_end` معتمدة على استنتاج من نشاط عام موثق لا تأكيد مباشر — تستحق تحققاً إضافياً.
- **thk-bhellinger**: لا يوجد slug لمدرسة "تشكيلات الأسرة" (`sch-family-constellations` مقترح).

## الملفات
content/ar/thinkers/thk-bentham.md
content/ar/thinkers/thk-bergson.md
content/ar/thinkers/thk-berkeley.md
content/ar/thinkers/thk-bernardo-chartres.md
content/ar/thinkers/thk-berne.md
content/ar/thinkers/thk-bernfeld.md
content/ar/thinkers/thk-bertrand-russell.md
content/ar/thinkers/thk-besselvanderkolk.md
content/ar/thinkers/thk-beutler.md
content/ar/thinkers/thk-bfredrickson.md
content/ar/thinkers/thk-bguerney.md
content/ar/thinkers/thk-bhartrhari.md
content/ar/thinkers/thk-bhellinger.md
content/ar/thinkers/thk-bhooks.md
content/ar/thinkers/thk-biko.md
content/ar/thinkers/thk-bill-devall.md
content/ar/thinkers/thk-bill-ohanlon.md
content/ar/thinkers/thk-bion.md
content/ar/thinkers/thk-bj-fogg.md
content/ar/thinkers/thk-bjoseph.md
content/ar/thinkers/thk-blanchot.md
content/ar/thinkers/thk-blankenburg.md
content/ar/thinkers/thk-blbettner.md
content/ar/thinkers/thk-bleuler-jung-assoc.md
content/ar/thinkers/thk-bleuler.md
content/ar/thinkers/thk-bloch.md
content/ar/thinkers/thk-boadella.md
content/ar/thinkers/thk-bob-proctor.md
content/ar/thinkers/thk-bobbeck.md
content/ar/thinkers/thk-bodhidharma.md
content/ar/thinkers/thk-bodunrin.md
content/ar/thinkers/thk-boethius-dacia.md
content/ar/thinkers/thk-boethius.md
content/ar/thinkers/thk-bohanlon.md
content/ar/thinkers/thk-bolen.md
