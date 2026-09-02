# Task 1.1
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- قائمة سوداء متبقية: قبل 25 → بعد 0
- سقّالة ظاهرة: قبل 17 → بعد 0
- ملفات بـ`## المصادر`: قبل 0 → بعد 25
- متوسط طول الملف: قبل ≈ 350 حرف → بعد ≈ 4,500 حرف
- شبكات `related` قابلة للاستخدام: قبل 0–3 روابط ضعيفة → بعد 4–8 روابط مبررة في المتن
- ملفات placeholder معلَّمة: 1 (`thk-mcieslak` — شخصية غير موثّقة في علم النفس الظاهراتي)

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.1
=== تحقق Task 1.1 (25 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها

- **thk-mcieslak (ماريك تشيسلاك)**: الشخصية المُسجَّلة كظاهراتي لا وجود لها في أي قاعدة بيانات أكاديمية (Web of Science / PhilPapers / APA PsycInfo حتى آب 2026). الأشخاص المعروفون بهذا الاسم (اقتصادي في بوزنان، طبيب أعصاب في تورون، معالج إدمان في وارسو) ليسوا ظاهراتيين. أبقى الملف placeholder، وأوسِّع `gaps` بتفاصيل التحقق، وأقترح على رئيس التحرير الحجر في `quarantine-minimax.md` أو دمج الاسم الصحيح. **لم أخترع سيرة.**

- **thk-rhassan (رفة حسن)**: وُلدت 1943 في لاهور، PhD Durham 1968 عن إقبال، Louisville 1976–2009. صحّحتُ الأخطاء في الـfrontmatter (كانت "active_start: 1980" → 1972). أضفتُ شبكة مع إقبال والمودودي وسعدية شيخ وعادل نجّام.

- **thk-sshaikh (سعدية شيخ)**: PhD Temple 2004، UCT. أضفتُ شبكة ابن عربي والرومي ورفه حسن. كتاب «Sufi Narratives» فاز بجائزة UCT 2015 ورُشّح لجائزة AAR 2013 (معلومة غير منشورة عربياً).

- **thk-ymohamed (ياسين محمد)**: وُلد 1954 في جوهانسبرغ، PhD Frankfurt 1986. صحّحتُ الأخطاء في `crumb` (كان "علم النفس الإيجابي الإسلامي" من غير اسم). أضفتُ شبكة الراغب الأصفهاني وعبد الخالق وابن تيمية.

- **thk-pgasser (بيتر غَسَر)**: وثّقتُ تجربتي BAG (10 LSD و7 MDMA) وتجربة 1988–1993 (171 مريضاً). حذفتُ خطأ "MDMA Mithoefer" واستبدلته بالروابط الصحيحة (Gasser، Oehen، Widmer، Doblin).

- **thk-wmasters (وليام ماسترز)**: صحّحتُ العلاقة مع فرجينيا جونسون (متزوجا 1971–1992، ليست شريكة عمل فقط).

- **thk-primo-levi (بريمو ليفي)**: نقلتُه من `philosophy` ضعيف إلى `philosophy` مع شبكة حقيقية: فيزل، لاكان، فرانكل، أرندت. وثّقتُ مفهوم «المنطقة الرمادية» في «الغارقون والناجون» (1986).

- **thk-sgallagher (شون غالاغر)**: ميّزت بين «صورة الجسد» و«مخطط الجسد» و«الوعي الأداتي» (Ownership/Agency). أضفتُ شبكة ميرلو-بونتي، فاريلا، روش، برغسون، زاهافي.

- **thk-wjanzarik (فيرنر يانتساريك)**: صحّحتُ الترجمة من "شولتز-هينكه" إلى «مدرسة هايدلبرغ». وثّقتُ علاقته بشنايدر وياسبرز ونيتشه.

- **thk-rcarson (راشيل كارسون)**: أضفتُ شبكة أرنه نيس وألدو ليوبولد ولوف. أوضحتُ أنها ليست معالجة نفسية بل مؤسسة الوعي البيئي الذي مهّد لعلم البيئة النفسية.

## متوقف عنده (لرئيس التحرير)

- **thk-mcieslak**: يحتاج قراراً من رئيس التحرير:
  - (أ) الحجر في `quarantine-minimax.md` لأن الشخصية المُسجَّلة غير موثَّقة في الظاهراتية.
  - (ب) تصحيح الاسم إلى شخصية موثقة إذا كان هناك خطأ إملائي.
  - أنا أرجّح (أ) لأن المعرف المرتبط (Clark Moustakas, Max van Manen) كلهم ظاهراتيون، والشخص المفترض لا يظهر في أي قاعدة بيانات ظاهراتية.

- **thk-nkhanna (نيخيل خانا)**: معلومات محدودة. يجب التحقق من:
  - جامعته الدقيقة.
  - منشوراته في المجلات المحكّمة (لا يزال معظم عمله في شكل ندوات ومقالات شعبية).
  - إن كان «مركز التدريب في بنغالور» مؤسسة حقيقية أم منصة تدريب.

- **25 تعارض slug بين المعتمد والمسودات** (تحذير `build_slug_index.py`): 25 slug له نسختان (معتمدة + مسودة). أستخدم بعضها في `related` (مثل `thk-amithoefer`, `thk-fpeseschkian`). هذا تحذير موجود مسبقاً ولا أُسبّبه، لكن يستحق التنبيه لرئيس التحرير.

## الملفات
content/ar/thinkers/thk-mcieslak.md
content/ar/thinkers/thk-rcarson.md
content/ar/thinkers/thk-rhassan.md
content/ar/thinkers/thk-mpolster.md
content/ar/thinkers/thk-slima.md
content/ar/thinkers/thk-tpichot.md
content/ar/thinkers/thk-ppapp.md
content/ar/thinkers/thk-pgasser.md
content/ar/thinkers/thk-ymohamed.md
content/ar/thinkers/thk-mcierpka.md
content/ar/thinkers/thk-wmasters.md
content/ar/thinkers/thk-parkjongik.md
content/ar/thinkers/thk-smcnamee.md
content/ar/thinkers/thk-wjanzarik.md
content/ar/thinkers/thk-mrand.md
content/ar/thinkers/thk-ydolan.md
content/ar/thinkers/thk-tstromsted.md
content/ar/thinkers/thk-pbooth.md
content/ar/thinkers/thk-sshaikh.md
content/ar/thinkers/thk-primo-levi.md
content/ar/thinkers/thk-rbenenzon.md
content/ar/thinkers/thk-petersmith.md
content/ar/thinkers/thk-sgallagher.md
content/ar/thinkers/thk-pnordoff.md
content/ar/thinkers/thk-nkhanna.md
