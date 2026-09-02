# Task 8.6
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40 (40/40 التزموا بصيغة slug القصيرة من البداية)
باقي مجلد schools/ بلا ## المصادر: 210 → 170

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تجميع** (تصحيحات صغيرة عملها الـsubagents أنفسهم قبل التسليم)

## قرارات اتخذتها
- تراث يهودي/إسلامي مختلط جغرافياً: `sch-judaism-andalusian.md` وsch-kabbalah-lurianic.md`/`sch-kabbalah.md`/`sch-karaite.md` أُعطيت `cultural_origin: "islamic-arabic"` بناءً على سياق النشأة الجغرافي-السياسي الفعلي (الأندلس تحت الحكم الإسلامي، صفد العثمانية، بابل الإسلامية) لا الهوية الدينية — قرار متّسق مع كونها نشأت فعلياً داخل حضارة إسلامية-عربية، بخلاف `sch-judaism-hellenistic` (يوناني) و`sch-judaism-existential`/`sch-judaism-reform` (أوروبي حديث).
- توحيد/دمج عناوين أقسام مصادر قديمة مكررة المعنى بدل تكرارها: sch-ipt (## المطبوعات التأسيسية الرئيسية)، sch-islamic-psychology (## المرجع الأساسي)، sch-istdp (دمج قسمين متداخلين لواحد بلا تكرار).
- ملفات فيها قسم "## المؤلفات المرجعية" (نصوص أولية للمدرسة نفسها) تُرك بجانب "## المصادر" الجديد (مراجع أكاديمية ثانوية) لأنهما مختلفا المضمون فعلاً: sch-isfahan، sch-ismaili، sch-latin-averroism.
- الـsubagents صحّحوا بأنفسهم مخالفات preflight قديمة قبل التسليم: 3 تعارضات id/title (sch-indigenous-psychology: اسمين، sch-islamic-psychology: أبو ريا)، حذف 3 edges بنص حر بلا slug بديل موجود (sch-imami-kalam→"علم الكلام الإسلامي" تكرار من الدفعة الماضية، sch-indigenismo→"الفلسفات اللاتينية" **[جديد، مسجّل]**، sch-indigenous-philosophy-contemporary→"فلسفات السكان الأصليين")، وإعادة صياغة جملة قائمة سوداء واحدة في gaps.
- **تكرار مهم رُصد**: "الفلسفات اللاتينية" ظهرت كـtarget حر مفقود **مرتين** الآن (دفعة 8.3 وهذه الدفعة) — سُجّلت كطلب slug بأولوية أعلى بسبب التكرار (مؤشر حقيقي لحاجة umbrella).
- مشكلة تقنية بسيطة تم حلها: sch-latin-averroism.md رفض أداة Edit المطابقة النصية على السطر الأخير (فرق ترميز غير ظاهر) — الـsubagent استخدم append بدل الاستبدال، تحققت بنفسي إن النتيجة سليمة بلا تكرار أو تلف.
- ملفات اكتفت بعدد مصادر أقل من 4 عمداً: `sch-kaupapa-maori.md`، `sch-indigenismo.md`، `sch-lebensphilosophie.md` (3 لكل) — مادة محدودة، لا اختراع.

## متوقف عنده (لرئيس التحرير)
- طلب slug جديد بأولوية أعلى (تكرار مرتين): "الفلسفات اللاتينية" — umbrella لمدارس أمريكا اللاتينية.

## الملفات
content/ar/schools/sch-imami-kalam.md
content/ar/schools/sch-indigenismo.md
content/ar/schools/sch-indigenous-philosophy-contemporary.md
content/ar/schools/sch-lebensphilosophie.md
content/ar/schools/sch-indigenous-psychology.md
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
