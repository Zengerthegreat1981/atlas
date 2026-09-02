# Task 8.5
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40 (40/40 التزموا بصيغة slug القصيرة من البداية)
باقي مجلد schools/ بلا ## المصادر: 250 → 210

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تجميع** (بعد تصحيحات صغيرة عملها الـsubagents أنفسهم لمخالفات preflight قديمة قبل التسليم — مش أنا)

## قرارات اتخذتها
- صحّحت بنفسي مخالفة دلالية واحدة بعد التسليم: `sch-hebrew-wisdom.md` كان فيه `cultural_origin: "islamic-arabic"` رغم إن الملف عن تقليد الحكمة العبرية القديمة (لا علاقة له بالعالم الإسلامي) — غيّرته لـ"greek" (أقرب قيمة متاحة في اتفاقية العالم القديم، نفس منطق sch-gnosticism/sch-hermeticism)، وسجّلت في `gaps` تحديداً إن الاتفاقية الحالية ناقصة slug مخصص لـ"الشرق الأدنى القديم/إسرائيل القديمة".
- الـsubagents أنفسهم صحّحوا عدداً كبيراً من مخالفات preflight قديمة قبل التسليم (نمط متكرر عبر الدفعة): تعارضات id/title (sch-fichte: كانط/شيلينغ، sch-german-idealism: نفس الاثنين، sch-gelug: مادهياماكا، sch-huayan: نفس الملف، sch-formal-phil-language: كريبكي، sch-functionalism: بوتنام، sch-gestalt-therapy: بيرلز/كوفكا، sch-imago: هندريكس، sch-hermeticism: نيوبلاتونزم، sch-humanistic: 3 عناوين + edge)، وحذف/استبدال edges بنص حر بدل slug حقيقي (أكثر من 15 حالة عبر الدفعة، منها استبدالات ناجحة لـslugs موجودة فعلاً: sch-systemic-family، sch-bhakti-movement، sch-egyptian-maat، br-self-actualization-maslow، sch-ismaili، thk-richard-schwartz).
- **sch-functionalism.md**: تأكدت الهوية فعلياً — الملف عن الوظيفية في فلسفة العقل (Putnam/Fodor/Block/Searle) مش الوظيفية النفسية الأمريكية (جيمس/ديوي) كما حذّر MINIMAX.md. لا لبس فعلي في هذا الملف تحديداً، لكن رُصد رابط `rel-pragmatism-functional-psychology` يستاهل مراجعة لاحقة للتأكد من دقة الربط بين المدرستين (خارج نطاق هذه الدفعة).
- **sch-humanistic.md**: تأكدت الهوية — علم النفس الإنساني (روجرز/ماسلو)، ليست فلسفة عامة.
- ملفات اكتفت بعدد مصادر أقل من 4 عمداً: `sch-faxiang.md`، `sch-huang-lao.md`، `sch-gandhianism.md`، `sch-hermeticism.md`، `sch-ethiopian-hataata.md` وغيرها — مادة أكاديمية محدودة، لا اختراع.
- توحيد عناوين أقسام مصادر قديمة مكرّرة المعنى بدل تكرارها: sch-imago (## أهم المرجعيات)، sch-ifs (## المرجع الأساسي)، sch-gestalt-therapy (## المرجع الموصى)، sch-humanistic (## المرجع الموصى).

## متوقف عنده (لرئيس التحرير)
- 3 طلبات slug جديدة اتسجلوا في `requests-minimax.md` (علم الكلام الإسلامي، تقاليد الحكمة الأفريقية، الفلسفات الآسيوية الحديثة) — أول واحد منهم مؤكد كأولوية في MINIMAX.md Task 13 فعلاً.

## الملفات
content/ar/schools/sch-experimental-philosophy.md
content/ar/schools/sch-faxiang.md
content/ar/schools/sch-feminism-black.md
content/ar/schools/sch-imago.md
content/ar/schools/sch-feminism-existential.md
content/ar/schools/sch-feminism-french-poststructural.md
content/ar/schools/sch-feminism-liberal.md
content/ar/schools/sch-feminism-marxist.md
content/ar/schools/sch-feminism-phenomenological.md
content/ar/schools/sch-feminism-postcolonial.md
content/ar/schools/sch-feminism-radical.md
content/ar/schools/sch-fichte.md
content/ar/schools/sch-formal-phil-language.md
content/ar/schools/sch-frankfurt-school.md
content/ar/schools/sch-functionalism.md
content/ar/schools/sch-gandhianism.md
content/ar/schools/sch-gelug.md
content/ar/schools/sch-german-idealism.md
content/ar/schools/sch-gestalt-therapy.md
content/ar/schools/sch-gnosticism.md
content/ar/schools/sch-hasidic.md
content/ar/schools/sch-haskalah.md
content/ar/schools/sch-haudenosaunee.md
content/ar/schools/sch-hebrew-wisdom.md
content/ar/schools/sch-hegel-left.md
content/ar/schools/sch-hegel-right.md
content/ar/schools/sch-hegelianism.md
content/ar/schools/sch-heraclitean.md
content/ar/schools/sch-hermeneutics-critical.md
content/ar/schools/sch-hermeneutics.md
content/ar/schools/sch-hermeticism.md
content/ar/schools/sch-hindutva.md
content/ar/schools/sch-huang-lao.md
content/ar/schools/sch-huayan.md
content/ar/schools/sch-humanistic.md
content/ar/schools/sch-humeanism.md
content/ar/schools/sch-ibadi-kalam.md
content/ar/schools/sch-ifa.md
content/ar/schools/sch-ifs.md
content/ar/schools/sch-ikhwan-safa.md
