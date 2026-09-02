# مراجعة الحجر — دفعة A (20 ملفاً)

الحالة: مكتمل
العملية: تصحيح مخالفات preflight_check.py الآلية على 20 ملف thk- مقترحة للمراجعة | الملفات: 20

## الأرقام
إجمالي المخالفات: قبل 109 → بعد 0

## تفصيل المخالفات المصححة حسب النوع

| النوع | العدد | الإجراء |
|---|---|---|
| `related: id` بيشاور لملف غير موجود | 65 | حُذف السطر من `related`، وسُجّلت ملاحظة في `gaps` تفسّر الحذف |
| `related: id/title` متضاربين (title لا يطابق عنوان الملف الحقيقي) | 11 | صُحّح الـtitle ليطابق عنوان الملف المستهدف الحقيقي (وفي حالة `thk-eknobe`/`thk-rick-doblin`/`thk-mmithoefer` استُبدل الـid نفسه بالـslug الصحيح غير المحجور) |
| `edges: target` نص حر مش slug حقيقي | 9 | 7 حالات استُبدلت بـslug مدرسة/تيار حقيقي موجود فعلاً (`br-clinical-hypnotherapy`, `br-psychiatric-vocational-rehab` ×2, `sch-yoga`, `sch-psychedelic-assisted-therapy`, `sch-developmental`)؛ حالتان (`thk-sothmer`, `thk-rlandy-md`) لا يوجد لهما slug مقابل فعلاً → `edges: []` وسُجّلتا في `agents_specs/missing-schools.md` |
| `gaps` بتؤكد حقيقة بدل ما تسمي فجوة | 12 | أُعيدت صياغتها لتسمية فجوة فعلية أو حُذفت (وأُبدلت بفجوات حقيقية عن الروابط المحذوفة) |
| سنة في المتن بعد `active_end` بلا إشارة "بعد وفاته/وفاتها" | 6 | 4 حالات أُضيفت لها عبارة "بعد وفاته/وفاتها" قبل السنة مباشرة؛ حالة `thk-nionescu` صُحح فيها `active_end` من 1930 إلى 1940 (خطأ فعلي يناقض `dates` والمتن نفسه) بالإضافة لإضافة الإشارات اللازمة لتواريخ أشخاص آخرين مذكورين في نفس الملف |

## قرارات اتخذتها
- `thk-mgold.md`: حذف روابط con-ips وdis-mental-illness (غير موجودين)، تصحيح target في edges.
- `thk-mtrevi.md`: حذف 3 روابط غير موجودة (thk-jhillman, thk-emevarez, ومفاهيم إيطالية).
- `thk-pritz.md`: تصحيح thk-sfreud → thk-freud، حذف 3 مفاهيم غير موجودة.
- `thk-snygg.md`: تصحيح thk-amaslow → thk-maslow، حذف مفهومين.
- `thk-snichols.md`: تصحيح thk-eknobe (title كان خطأ)، حذف thk-jknobe (مكرر لثيك-eknobe)، حذف 4 روابط أخرى.
- `thk-mahfouz.md`: حذف رابط thk-mrauf، إصلاح إشارة السنة 2006 بعد active_end=1995.
- `thk-tbarber.md`: تصحيح edges target إلى br-clinical-hypnotherapy، حذف 5 روابط غير موجودة.
- `thk-rryan.md`: تصحيح titles (csikszentmihalyi, crogers→rogers, amaslow→maslow)، حذف thk-frick و3 مفاهيم.
- `thk-rosenfeld.md`: تصحيح thk-mklein→thk-klein، thk-wbion→thk-bion، thk-hsegal→thk-segal، حذف مفهومين.
- `thk-spiegelberg.md`: تصحيح title هايدجر، merleau، sartre، حذف مفهومين، إصلاح إشارة سنة 1990.
- `thk-wanthony.md`: تصحيح edges target، تصحيح title سبولدنغ، حذف 4 مفاهيم.
- `thk-yogananda.md`: تصحيح edges target إلى sch-yoga، حذف 3 مفاهيم، إصلاح إشارة سنة 1985.
- `thk-tgreening.md`: حذف 3 روابط غير موجودة، تبسيط gaps.
- `thk-mithoefer.md`: تصحيح target وtitle دابلن، تصحيح edges target، حذف thk-rmap ومفهومين.
- `thk-nionescu.md`: حذف 4 روابط غير موجودة، تصحيح active_end (خطأ فعلي 1930→1940)، إصلاح إشارات سنوات متعددة.
- `thk-mmithoefer.md`: تصحيح thk-rick-doblin (محجور) → thk-rmdoblin، thk-kgrof→thk-sgrof، حذف con-emdr.
- `thk-sothmer.md`: edges→[]  (لا مدرسة مقابلة)، تصحيح title ستيرمان، حذف روابط ومفاهيم غير موجودة، تسجيل في missing-schools.md.
- `thk-rlandy-md.md`: edges→[]، تصحيح title زيركا مورينو، حذف thk-nagler و3 مفاهيم، تسجيل في missing-schools.md.
- `thk-rennie.md`: حذف روابط ومفاهيم غير موجودة، تبسيط gaps.
- `thk-tbrazelton.md`: تصحيح edges target إلى sch-developmental، تصحيح thk-ewinnicott→thk-winnicott، thk-jbowlby→thk-bowlby، حذف مفهومين.

## أمر التحقق
```
python3 scripts/build_slug_index.py
python3 scripts/preflight_check.py <الملفات العشرين>
```
→ `✅ 20 ملف — صفر مخالفات آلية.`

## الملفات
thk-mgold, thk-mtrevi, thk-pritz, thk-snygg, thk-snichols, thk-mahfouz, thk-tbarber, thk-rryan, thk-rosenfeld,
thk-spiegelberg, thk-wanthony, thk-yogananda, thk-tgreening, thk-mithoefer, thk-nionescu, thk-mmithoefer,
thk-sothmer, thk-rlandy-md, thk-rennie, thk-tbrazelton
