# Task 17.2
الحالة: مكتمل
العملية: كتابة الملفين الغائبين من الفجوة المحددة في task-17-gap-analysis.md | الملفات: 2

## الأرقام
مفاهيم Task 17 المغطاة: 5/6 → 6/6

## أمر التحقق
`python3 scripts/preflight_check.py con-hallucinogens-mental-health.md con-digital-mental-health.md`
→ ✅ 2 ملف — صفر مخالفات آلية (بعد تصحيح تطابق title في related مرة واحدة).
`python3 scripts/build_slug_index.py` → ✅ 6915 عنصر (6621 معتمد + 294 مسودة)، صفر ظهور للـslugين
الجديدين في قائمة التعارض.

## قرارات اتخذتها
- **con-hallucinogens-mental-health**: مفهوم عابر (الأياهواسكا، الجرعات الدقيقة، MEQ30، الأضرار
  والفضائح) مميّز عن `drg-esketamine.md` الذي يغطي الاستطباب الطبي الضيق فقط. ربطته بـ
  `drg-esketamine` و`stu-maps-mdma-phase3` و`stu-griffiths-psilocybin-cancer` الموجودين فعلاً.
  فجوة موثّقة: رقم دقيق لاستمرار أثر الأياهواسكا (الدراسات المتاحة رصدية صغيرة لا معشاة)، وتفاصيل
  فضيحة MAPS 2015 موثّقة صحفياً لا في ورقة محكّمة.
- **con-digital-mental-health**: التنميط الرقمي (Torous 2016) + التقييم اللحظي البيئي +
  معالجو LLM ومخاطرهم (Woebot 2017 كمثال موثّق) + التنبؤ الخوارزمي بالانتحار (REACH VET، McCarthy
  et al. 2015). `edges` تُركت فارغة (`[]`) بدل اختراع slug مدرسة غير موجود — نفس الوضع في
  `con-global-mental-health` الشقيق.
- كلا الملفين preflight نظيف، وصفر ظهور في قائمة تعارضات build_slug_index.

## متوقف عنده (لرئيس التحرير)
- لا شيء.

## الملفات
content/ar/drafts/spark/concepts/con-hallucinogens-mental-health.md
content/ar/drafts/spark/concepts/con-digital-mental-health.md
