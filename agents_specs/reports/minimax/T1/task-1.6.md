# Task 1.6

الحالة: مكتمل
العملية: تراث/دفعة كانت "مُطالَبة" (claimed) بدون تنفيذ — أُعيد تنفيذها بالكامل تحت إشراف مباشر
(subagents بدفعات 5 ملفات + `preflight_check.py` فوري لكل دفعة، مش دفعة 25 ثم تقرير) | الملفات: 25

## الأرقام
هوية موثّقة وأُصلحت بالكامل: 10/25 (منها 4 كانت أسماء/جنس/نسبة خاطئة اتصححت: thk-phackney →
Peggy Hackney، thk-marian-krcmar → تصحيح الاسم Marina، thk-tandreas → Tamara Andreas،
thk-tkellermann → Peter وليس Thomas Kellermann)
هوية غير موثّقة (حُوّلت لملف غامض + حجر): 15/25

## أمر التحقق
`python3 scripts/preflight_check.py <كل ملفات الدفعة>` → ✅ صفر مخالفات آلية على كل الدفعات الفرعية
(5 مجموعات × 5 ملفات)

## قرارات اتخذتها
- كل شخص ما قدرناش نوثّقه ببحث فعلي: اتحوّل الملف لـ"غامض" صريح (متن + gaps بيسموا بالظبط
  الناقص)، الروابط غير المبرَّرة اتشالت، وسُجّل في `quarantine-minimax.md`.
- كل تعارض هوية واضح (زي thk-phackney، thk-tandreas، thk-tkellermann): اتصحح في نفس الـslug
  (مش إعادة تسمية) لأن المرجع نفسه واحد، بس الاسم/التفاصيل غلط — مطابق لقاعدة 6.
- thk-marian-krcmar: الشخصة حقيقية (Marina Krcmar) لكن السيرة الأصلية كانت ملفَّقة بالكامل
  (مجال مختلف تماماً) — اتصححت، وتعارض الاسم (Marian/Marina) اتسجل في gaps كطلب تصحيح slug مستقبلي.

## متوقف عنده (لرئيس التحرير)
- thk-marian-krcmar: تصحيح slug محتمل (Marian → Marina) — يحتاج قرار رسمي قبل التنفيذ.

## تصحيح لاحق (رئيس التحرير، 2026-08-27)
سويب منهجي على كل دفعات minimax المكتملة كشف إن 5 ملفات من هذه الدفعة كانت لسه فيها جملة القائمة
السوداء "لا يوجد اقتباس مباشر موثوق متاح" — إما في `gaps` أو في قسم "## اقتباسات مختارة" في المتن
(نفس نمط bug اكتُشف في 2.16). preflight_check.py الوقتها ما كانش بيفحص محتوى `gaps`/المتن ضد
القائمة السوداء، فمرّت. الملفات المصححة: thk-vcarrera، thk-patrice-de-marco، thk-rviaro
(الأربعة "غامض")، thk-madeleine-sandberg (نفس النمط)، وthk-marian-krcmar (موثّقة، كانت الجملة في
`gaps` والمتن). التصحيح: حُذف قسم "## اقتباسات مختارة" بالكامل من الملفات الغامضة (بدل تركه بجملة
محظورة)، واستُبدلت جملة `gaps` بصياغة دقيقة تسمّي الشخص. بالمناسبة اتصلح كمان 4 مخالفات `edges`
كانت نص حر بدل slug حقيقي (اتشالت أو اتحوّلت لـbr-brief-strategic-therapy الموجود فعلاً لـrviaro).
`preflight_check.py` على الخمسة: ✅ صفر مخالفات بعد التصحيح.

## الملفات
thk-pguerin, thk-mary-guthrie, thk-phackney, thk-timothyclanton, thk-nsugiyama, thk-yhkim,
thk-rubin, thk-rpimenta, thk-nwatanabe, thk-tshibuya, thk-vcarrera, thk-patrice-de-marco,
thk-rviaro, thk-marian-krcmar, thk-madeleine-sandberg, thk-robert-cornelis, thk-syoung,
thk-tandreas, thk-tbrach, thk-tgillingham, thk-thomas-sells, thk-timothy-verduin,
thk-tkellermann, thk-utelfener, thk-yotsuka
