# Task 16.3 — حسم ازدواج wrk- الثقيل (مذكور في تقرير 16.1)
الحالة: مكتمل | لا ملفات جديدة — 3 عمليات دمج + إصلاحات جانبية على 12 ملفاً

## السبب
تقرير 16.1 وثَّق ازدواجاً ثقيلاً لم يُحسم: «الوجود والعدم» لسارتر (×3 ملفات)، «بنية الثورات العلمية» لكون (×2)، «فينومينولوجيا الإدراك» لميرلوبونتي (×2). نُفِّذ الحسم شخصياً (بدون subagents) وفق قاعدة 6.

## الدمجات الثلاثة
1. **الوجود والعدم (سارتر)**: أُبقي `wrk-sartre-being-and-nothingness` (WRK-0794) كنسخة الأساس (الأكثر ربطاً فعلياً: استعارتا نادل المقهى وسكين الورق). حُوِّل `wrk-being-nothingness` وwrk-being-and-nothingness-sartre` لملفي إحالة. نُقل رابط con-freedom وthk-heidegger من النسخة المحجورة الأولى إلى المعتمدة (قيمة فعلية لم تُفقد). أُصلحت 4 ملفات مفكرين كانت تشير للنسخة المحجورة (thk-cannon، thk-badawi، thk-pareyson، thk-barnes) + ملف مفهوم واحد (con-being-for-itself-and-in-itself) + ملاحظة gap في con-bad-faith كانت تسأل عن الحسم — أُجيبت.
2. **بنية الثورات العلمية (كون)**: أُبقي `wrk-kuhn-structure-revolutions` (WRK-0366، 78 سطراً، أعمق بكثير) كنسخة الأساس. حُوِّل `wrk-the-structure-of-scientific-revolutions-kuhn` لملف إحالة. أُصلحت 3 ملفات كانت تشير للنسخة المحجورة (sch-kuhnianism، con-incommensurability-kuhn، con-paradigm-shift-kuhn).
3. **فينومينولوجيا الإدراك (ميرلوبونتي)**: أُبقي `wrk-phenomenology-perception-merleau-ponty` (WRK-0805، الأكثر ربطاً فعلياً: thk-husserl، thk-heidegger، con-lived-body، con-body-schema) كنسخة الأساس، بعد **إصلاح تشويه تنسيقي حاد فيه** (bold مفرط على كل كلمة تقريباً — أثر تنظيف/ترجمة آلية سابق) ونقل تحليلي الطرف الشبح والتجسيد المعرفي من النسخة الأخرى إليه لإثرائه. حُوِّل `wrk-merleau-ponty-phenomenology-perception` لملف إحالة. أُصلح ملف استعارة واحد (met-merleau-ponty-blind-man-cane) كان يشير للنسخة المحجورة.

## التحقق
- preflight على كل الملفات الـ15 المتأثرة (3 نسخ أساس + 3 محجورة + 9 ملفات مُصححة): صفر مخالفة حقيقية بعد إصلاحين إضافيين اكتُشفا أثناء الفحص (جملتا قائمة سوداء في thk-cannon وthk-badawi كانتا موجودتين مسبقاً قبل هذه الجلسة، حُذفتا).
- تنبيه واحد فحصته يدوياً وتبيَّن أنه إيجابية كاذبة من preflight_check.py نفسه: عَلَم على thk-barnes (هازل بارنز، امرأة) باعتبار عنوانين مؤنَّثين "خطأ" لأن الأداة رصدت "male_marker" واحداً في المتن — تحققتُ من السياق فعلياً: الكلمة المذكَّرة ("فيه") تعود لاسم مذكَّر ("نسقاً")، لا لبارنز نفسها. لا خطأ حقيقي، متن الملف كله يعامل بارنز بصيغة مؤنَّثة صحيحة.
- grep قائمة سوداء نهائي على كل الملفات: صفر تطابق.

## الملفات المعدَّلة (15)
- نسخ أساس (أُثريت): wrk-sartre-being-and-nothingness.md، wrk-kuhn-structure-revolutions.md (لم يُعدَّل محتوى)، wrk-phenomenology-perception-merleau-ponty.md (أُعيد صياغته بالكامل + إثراء)
- حُوِّلت لإحالة: wrk-being-nothingness.md، wrk-being-and-nothingness-sartre.md، wrk-the-structure-of-scientific-revolutions-kuhn.md، wrk-merleau-ponty-phenomenology-perception.md
- أُصلح رابط داخلي: thk-cannon.md، thk-badawi.md، thk-pareyson.md، thk-barnes.md، con-being-for-itself-and-in-itself.md، con-bad-faith.md، sch-kuhnianism.md، con-incommensurability-kuhn.md، con-paradigm-shift-kuhn.md، met-merleau-ponty-blind-man-cane.md
- إصلاح جانبي إضافي (بلاكليست، غير مرتبط بالدمج): thk-cannon.md، thk-badawi.md، thk-barnes.md

## متوقف عنده
- لا ازدواجات wrk- ثقيلة أخرى معروفة حالياً — التوصية: تشغيل فحص تكرار عناوين شامل عبر content/ar/works/ كخطوة وقائية دورية.
