# Task 8.7
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40 (40/40 التزموا بصيغة slug القصيرة من البداية)
باقي مجلد schools/ بلا ## المصادر: 170 → 130

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تجميع**

## قرارات اتخذتها
- **إصلاح جانبي مهم اكتشفته بنفسي**: `sch-middle-platonism.md` كان فيه edge ذاتي عبثي (`evolved_into → sch-middle-platonism` نفسه) لم يرصده preflight (مفيش قاعدة تفحص self-loop) — حذفته، الرابط الصحيح الوحيد لهذا الحقل (`evolved_into → sch-neoplatonism`) بقي سليماً.
- **⚠️ اكتشاف مهم: "علم الكلام الإسلامي" umbrella مفقود تكرر 4 مرات مؤكدة** عبر دفعات مختلفة (sch-ibadi-kalam دفعة 8.5، sch-imami-kalam دفعة 8.6، sch-maturidiyya وsch-mutazila هذه الدفعة) — رفعت أولويته في `requests-minimax.md` صراحة لأنه دليل قاطع على حاجة حقيقية، ومتّسق مع MINIMAX.md Task 13.
- الـsubagents صحّحوا بأنفسهم عدداً كبيراً من مخالفات preflight قديمة قبل التسليم: حذف/استبدال 12+ edges بنص حر (منها استبدالات ناجحة لـslugs حقيقية موجودة فعلاً: sch-xinxue، thk-wmiller/thk-rollnick، thk-mwhite/thk-depston)، تصحيح تعارضات id/title متعددة (sch-navayana: مادهياماكا، sch-neohinduism: 4 عناوين)، وإعادة صياغة/حذف عبارات القائمة السوداء في gaps (10+ حالة).
- دمج أقسام مصادر متكررة أو مختلطة بدل التكرار: sch-leibnizianism (فرّق بين نصوص أولية "## المؤلفات المرجعية" ومصادر ثانوية "## المصادر" الجديد، قرار صحيح لأنهما مختلفا المضمون)، sch-mbct (## المطبوعات التأسيسية الرئيسية)، sch-mingjia (فصل "## الإرث" عن "## المصادر" الجديد)، sch-narrative-therapy (دمج قسمين متداخلين)، sch-motivational-interviewing (دمج قسمين متداخلين، 10 مراجع فريدة بعد حذف التكرار).
- ملفات اكتفت بعدد مصادر أقل من 4 عمداً: `sch-legalism.md`، `sch-leibnizianism.md`، `sch-liberation-philosophy.md`، `sch-neokantian.md`، `sch-mahasanghika.md` (3 لكل) — مادة أكاديمية محدودة، لا اختراع.

## متوقف عنده (لرئيس التحرير)
- طلب slug "علم الكلام الإسلامي" اترفع لأولوية قصوى في `requests-minimax.md` بعد التكرار الرابع المؤكد — يستاهل الأولوية القصوى فعلياً في بداية Task 13.

## الملفات
content/ar/schools/sch-legalism.md
content/ar/schools/sch-leibnizianism.md
content/ar/schools/sch-liberation-philosophy.md
content/ar/schools/sch-neokantian.md
content/ar/schools/sch-liberation-psychology.md
content/ar/schools/sch-libertarianism.md
content/ar/schools/sch-lixue.md
content/ar/schools/sch-lockeanism.md
content/ar/schools/sch-logical-atomism.md
content/ar/schools/sch-madhyamaka.md
content/ar/schools/sch-mahasanghika.md
content/ar/schools/sch-manicheism.md
content/ar/schools/sch-marxism-humanist.md
content/ar/schools/sch-marxism-structuralist.md
content/ar/schools/sch-marxism.md
content/ar/schools/sch-maturidiyya.md
content/ar/schools/sch-maya-philosophy.md
content/ar/schools/sch-mazdakism.md
content/ar/schools/sch-mbct.md
content/ar/schools/sch-megarian.md
content/ar/schools/sch-mesopotamian-wisdom.md
content/ar/schools/sch-mestizaje.md
content/ar/schools/sch-middle-platonism.md
content/ar/schools/sch-milesian.md
content/ar/schools/sch-military-chinese.md
content/ar/schools/sch-mimamsa.md
content/ar/schools/sch-mingjia.md
content/ar/schools/sch-mitogaku.md
content/ar/schools/sch-mohism.md
content/ar/schools/sch-motivational-interviewing.md
content/ar/schools/sch-mutazila.md
content/ar/schools/sch-nahua-aztec.md
content/ar/schools/sch-narrative-therapy.md
content/ar/schools/sch-nationalism-philosophical.md
content/ar/schools/sch-navayana.md
content/ar/schools/sch-navya-nyaya.md
content/ar/schools/sch-negritude.md
content/ar/schools/sch-neo-vedanta.md
content/ar/schools/sch-neoconfucianism.md
content/ar/schools/sch-neohinduism.md
