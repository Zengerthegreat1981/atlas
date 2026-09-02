# Task 8.3
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get` — نفس فخّ Task 8.2) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40 (بصيغة slug قصيرة موحّدة من البداية هالمرة، توجيه صريح للـsubagents)
باقي مجلد schools/ بلا ## المصادر: 330 → 290

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → 7 مخالفة (كلها قديمة سابقة على هذه الدفعة، في sch-behaviorism.md) → صُحّحت يدوياً → **صفر مخالفات**

## قرارات اتخذتها
- **sch-behaviorism.md** (24+ مفكر يتيم مرتبط بيه): صحّحت 5 تعارضات id/title (thk-jwatson، thk-fskinner، br-purposive-behaviorism، br-hullian-behaviorism، br-neobehaviorism) واستبدلت edge بنص حر ("السلوكية الراديكالية (Skinner)" → `br-radical-behaviorism` الموجود فعلاً، "علم النفس الغائي (Tolman)" → `br-purposive-behaviorism` الموجود فعلاً بدل تكراره). حوّلت العنوان القديم "## المرجع الموصى" لـ"## المصادر" وأضفت مرجعين (بافلوف 1927، ثورندايك 1911).
- **sch-biological-neuro.md**: كان فيه قسمان متطابقان حرفياً "## المرجع الأساسي" و"## المصادر" (الـsubagent أضاف الثاني بمحتوى مطابق للأول سهواً) — حذفت "## المرجع الأساسي" المكرر وسِبت "## المصادر" فقط.
- **sch-buddhist-psychology.md**: كان already فيه مصادر حقيقية تحت عنوان "## المرجع الأساسي" غير المعيار المتّبع — أعدت تسمية العنوان لـ"## المصادر" بلا تغيير المحتوى (الـsubagent قرر بحق عدم تكرار مصادر موجودة أصلاً).
- طبّعت `cultural_origin` لملف واحد خرج عن الاتفاقية ("british" → "anglo-american") — الباقي (39 ملف) التزم بصيغة slug القصيرة من البداية بفضل توجيه صريح في تعليمات الدفعة دي (تحسّن عن دفعة 8.2 اللي احتاجت تطبيع 24 قيمة بعديّاً).
- **sch-bhakti-movement.md**، **sch-care-ethics.md**، **sch-caribbean-philosophy.md**: subagents حذفوا edges بنص حر بلا slug بديل موجود (بدل الاستبدال) — قرار صحيح موثّق في `gaps` كل ملف (رابط لـsch-sufism وsch-feminist-ethics غير موجودين بعد في الأطلس).
- ملفات اكتفت بعدد مصادر أقل من 4 عمداً: `sch-bhedabheda.md` (2)، `sch-arielismo.md`/`sch-caribbean-philosophy.md`/`sch-arab-renaissance.md`/`sch-bon.md`/`sch-bowen-ferrer-vivir.md`/`sch-brahmo-samaj.md`/`sch-british-empiricism.md`/`sch-chan.md`/`sch-chartres.md`/`sch-buddhism-early.md`/`sch-buddhist-modernism.md`/`sch-charvaka.md`/`sch-chinese-liberalism-modern.md`/`sch-chinese-marxism.md`/`sch-civic-republicanism.md` (3 لكل) — مادة أكاديمية موثوقة محدودة لمدارس صغيرة/نادرة، لا اختراع.
- ملف واحد (`sch-black-existentialism.md` وغيره) لم يحتج تسجيل gaps إضافية — مصادره كافية ومباشرة.

## متوقف عنده (لرئيس التحرير)
- لا شيء جديد (نفس الملاحظة السابقة عن ازدواج thk-leighmccullers بين content/ar وdrafts/spark لسه قايمة، خارج نطاقي).

## الملفات
content/ar/schools/sch-apophatic.md
content/ar/schools/sch-arab-renaissance.md
content/ar/schools/sch-arielismo.md
content/ar/schools/sch-aristotelianism.md
content/ar/schools/sch-arya-samaj.md
content/ar/schools/sch-ashariyya.md
content/ar/schools/sch-athariyya.md
content/ar/schools/sch-atomism-greek.md
content/ar/schools/sch-augustinianism.md
content/ar/schools/sch-aurobindo.md
content/ar/schools/sch-behaviorism.md
content/ar/schools/sch-berkeleianism.md
content/ar/schools/sch-bhakti-movement.md
content/ar/schools/sch-bhedabheda.md
content/ar/schools/sch-biological-neuro.md
content/ar/schools/sch-black-existentialism.md
content/ar/schools/sch-bon.md
content/ar/schools/sch-bowen-ferrer-vivir.md
content/ar/schools/sch-brahmo-samaj.md
content/ar/schools/sch-british-empiricism.md
content/ar/schools/sch-british-idealism.md
content/ar/schools/sch-buddhism-early.md
content/ar/schools/sch-buddhist-modernism.md
content/ar/schools/sch-buddhist-psychology.md
content/ar/schools/sch-byzantine.md
content/ar/schools/sch-care-ethics.md
content/ar/schools/sch-caribbean-philosophy.md
content/ar/schools/sch-cartesianism.md
content/ar/schools/sch-cft.md
content/ar/schools/sch-chan.md
content/ar/schools/sch-chartres.md
content/ar/schools/sch-comtian-positivism.md
content/ar/schools/sch-charvaka.md
content/ar/schools/sch-chinese-liberalism-modern.md
content/ar/schools/sch-chinese-marxism.md
content/ar/schools/sch-christian-mysticism-medieval.md
content/ar/schools/sch-civic-republicanism.md
content/ar/schools/sch-classical-liberalism-early.md
content/ar/schools/sch-communitarianism.md
content/ar/schools/sch-comparative-philosophy.md
