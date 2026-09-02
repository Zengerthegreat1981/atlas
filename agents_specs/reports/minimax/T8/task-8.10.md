# Task 8.10 (آخر دفعة)
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 49

## الأرقام
## المصادر موجود: قبل 0/49 → بعد 49/49
cultural_origin موجود: قبل 0/49 → بعد 49/49
**باقي مجلد schools/ بلا ## المصادر: 50 → 0 (فقط sch-cbt.md المُدمج/المُحال، متوقع بالتصميم)**
**Task 8 مكتمل بالكامل: 370/370 ملف**

## أمر التحقق
`python3 scripts/preflight_check.py <49 ملفاً>` → **صفر مخالفات من أول تجميع**
`grep -L "## المصادر" content/ar/schools/*.md` → `sch-cbt.md` فقط (متوقع، ملف إحالة)
`grep -L "cultural_origin" content/ar/schools/*.md` → صفر نتائج

## قرارات اتخذتها
- **اكتشاف هوية مهم مؤكَّد**: `sch-structuralism.md` تأكدت هويته الفعلية — البنيوية اللغوية/الأنثروبولوجية-الفلسفية (سوسير، ليفي-شتراوس، بارت، ألتوسير)، **وليست** الوظيفية النفسية أو البنيوية النفسية عند فونت-تيتشنر. هذا يؤكد بالضبط تحذير MINIMAX.md Task 13 ("البنيوية فونت–تيتشنر، متمايزة عن sch-structuralism الحالي"). سجّلت هذا صراحة في `gaps` الملف نفسه ليكون واضحاً لأي شات يشتغل على Task 13 لاحقاً: البنيوية النفسية الأصلية محتاجة ملف جديد مستقل، مش تعديل لهذا الملف.
- الـsubagents صحّحوا مخالفات preflight قديمة كثيفة في هذه الدفعة (أعلى معدل لحد الآن): 15+ edges بنص حر محذوفة/مستبدلة، 10+ تعارضات id/title، 8+ عبارات قائمة سوداء في gaps.
- توحيد/فصل أقسام مصادر: sch-social-psychology (## المرجع الموصى)، sch-solution-focused وsch-somatic-experiencing (فصل النصوص الأولية "الأعمال/المطبوعات التأسيسية" عن المراجع الثانوية الجديدة)، sch-transpersonal (## المرجع الموصى)، sch-systemic-family (## المرجع الموصى، 9 مراجع).
- ملفات اكتفت بمصدرين-ثلاثة عمداً: `sch-yinyang.md`/`sch-yoga.md`/`sch-yogacara.md`/`sch-zaydi-kalam.md`/`sch-zen-rinzai.md` (3 لكل)، `sch-zurvanism.md` (3) — مادة أكاديمية محدودة، لا اختراع.

## متوقف عنده (لرئيس التحرير)
- **البنيوية النفسية (فونت-تيتشنر) لسه محتاجة ملف مستقل جديد في Task 13** — sch-structuralism الحالي موثّق بدقة الآن لكنه يغطي موضوعاً مختلفاً تماماً.

## الملفات
content/ar/schools/sch-social-darwinism.md
content/ar/schools/sch-social-ecology.md
content/ar/schools/sch-social-psychology.md
content/ar/schools/sch-solution-focused.md
content/ar/schools/sch-somatic-experiencing.md
content/ar/schools/sch-sophistry.md
content/ar/schools/sch-speculative-realism.md
content/ar/schools/sch-spinozism.md
content/ar/schools/sch-stoicism.md
content/ar/schools/sch-structuralism.md
content/ar/schools/sch-systemic-family.md
content/ar/schools/sch-tagore-philosophy.md
content/ar/schools/sch-tathagatagarbha.md
content/ar/schools/sch-tendai-japan.md
content/ar/schools/sch-theravada.md
content/ar/schools/sch-thomism.md
content/ar/schools/sch-tiantai.md
content/ar/schools/sch-transcendent-theosophy.md
content/ar/schools/sch-transcendentalism.md
content/ar/schools/sch-transfeminism.md
content/ar/schools/sch-transhumanism.md
content/ar/schools/sch-transpersonal.md
content/ar/schools/sch-truc-lam.md
content/ar/schools/sch-upanishadic.md
content/ar/schools/sch-utilitarianism-contemporary.md
content/ar/schools/sch-utilitarianism.md
content/ar/schools/sch-vaisheshika.md
content/ar/schools/sch-vajrayana.md
content/ar/schools/sch-vedanta.md
content/ar/schools/sch-vedic.md
content/ar/schools/sch-victorines.md
content/ar/schools/sch-vienna-circle.md
content/ar/schools/sch-vietnamese-triple.md
content/ar/schools/sch-virtue-ethics.md
content/ar/schools/sch-vishishtadvaita.md
content/ar/schools/sch-wahdat-alshuhud.md
content/ar/schools/sch-wahdat-alwujud.md
content/ar/schools/sch-western-marxism.md
content/ar/schools/sch-xinxue.md
content/ar/schools/sch-xuanxue.md
content/ar/schools/sch-yinyang.md
content/ar/schools/sch-yoga.md
content/ar/schools/sch-yogacara.md
content/ar/schools/sch-zaydi-kalam.md
content/ar/schools/sch-zen-rinzai.md
content/ar/schools/sch-zen-soto.md
content/ar/schools/sch-zonghengjia.md
content/ar/schools/sch-zoroastrian-philosophy.md
content/ar/schools/sch-zurvanism.md
