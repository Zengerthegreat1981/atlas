# Task 13.3 — المدارس الغائبة (دفعة 3)
الحالة: مكتمل | الملفات: 9

## الملفات
- sch-integrative-eclectic — التكاملية/الانتقائية في العلاج النفسي
- sch-existential-phenomenology-therapy — الظاهراتية الفلسفية والعلاج الوجودي (هوسرل→هايدغر→بينسوانغر/بوس)
- sch-ecotherapy — العلاج البيئي/الطبيعي
- sch-addiction-psychology — علم نفس الإدمان
- sch-modern-philosophy — الفلسفة الحديثة (ديكارت إلى كانط)
- sch-discursive-psychology — علم النفس الخطابي (بوتر وويذرل)
- sch-reparative-therapy — العلاج بالتحويل (نيكولوسي/NARTH، متمايز عن br-conversion-therapy)
- sch-contemplative-psychotherapy — العلاج النفسي التأملي (جامعة ناروبا)
- sch-sensory-integration — التكامل الحسي (آيريس)

## الأرقام
preflight_check.py على كل مجلد schools/ (29 ملفاً، دفعات 1-3 معاً): صفر مخالفات بعد إصلاح مخالفة واحدة
اكتُشفت عند التجميع (جملة قائمة سوداء متبقية في gaps بملف sch-psychosocial-rehabilitation من الدفعة 1 — صُححت).

## قرارات اتخذتها
- **sch-existential-phenomenology-therapy**: استُبعد `thk-bachelard` من الروابط رغم إدراجه في missing-schools-registry
  لأن متن ملفه الفعلي (فلسفة العلم الفرنسية) لا صلة له بالتحليل الوجودي — ربط `belongs_to` في ملفه نفسه غير مبرَّر،
  سُجّل كطلب تصحيح.
- **sch-integrative-eclectic**: صُححت عنوانان متضاربان في related (thk-diclemente، thk-gold) اكتُشفا أثناء preflight.
- **sch-reparative-therapy**: مُيِّز بوضوح عن `br-conversion-therapy` الموجود؛ التزم بالتوثيق العلمي المُجمَع عليه
  (تقرير APA 2009، تراجع سبيتزر 2012) دون حكم أخلاقي مباشر في المتن.
- **sch-sensory-integration** و**sch-ecotherapy**: استُبعدت روابط لمفكرين بلا ملفات فعلية (إدوارد ويلسون، آرني ناس
  الموجود فقط في `content/ar/_merged/` كموقع قديم غير نشط) — سُجّلت كفجوات.

## متوقف عنده (لرئيس التحرير)
- طلب تصحيح `thk-bachelard.md` (ربط belongs_to خاطئ بالتحليل الوجودي في متنه/edges).

## الملفات
content/ar/drafts/minimax/schools/{sch-integrative-eclectic,sch-existential-phenomenology-therapy,sch-ecotherapy,sch-addiction-psychology,sch-modern-philosophy,sch-discursive-psychology,sch-reparative-therapy,sch-contemplative-psychotherapy,sch-sensory-integration}.md
