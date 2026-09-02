# Task 13.5 — المدارس الغائبة (دفعة 5)
الحالة: مكتمل | الملفات: 10

## الملفات
- sch-milan-systemic — العلاج الأسري الميلاني
- sch-transactional-analysis — تحليل المعاملات (TA)
- sch-nlp — البرمجة اللغوية العصبية
- sch-teacch — TEACCH
- sch-dance-movement-therapy — العلاج بالحركة والرقص
- sch-dit — العلاج الديناميكي البيني القصير
- sch-multicultural-counseling — الاستشارات متعددة الثقافات
- sch-restorative-justice — العدالة التصالحية
- sch-feldenkrais — طريقة فيلدنكرايس
- sch-naikan-therapy — علاج نايكان

## الأرقام
preflight_check.py على مجلدي schools/+thinkers/ التراكميين (83 ملفاً): صفر مخالفات، بعد إعادة ترقيم شاملة أخرى.

## نمط مهم اكتُشف في هذه الدفعة: تصفية الأسماء المختلَقة تلقائياً
ثلاثة من العشرة وكلاء استخدموا `agents_specs/missing-thinkers-final-resolution.md` (ملف تسوية من عمل سابق)
لفحص أعضاء "اليتامى" المقترحين **قبل** الربط، واستبعدوا بنجاح:
- **sch-restorative-justice**: استبعد 4 من 6 أسماء مقترحة (مصنّفة LIKELY_FABRICATED في ملف التسوية).
- **sch-dit**: استبعد `thk-mary-guthrie` (محجور، هوية غير مؤكدة).
- **sch-feldenkrais**: استبعد 4 من 6 أسماء مقترحة (LIKELY_FABRICATED).
هذا يعني أن الاعتماد الأعمى على `missing-schools-registry.md` وحده (بدون تقاطعه مع ملفات التسوية/الحجر)
كان سيُدخل أسماء مختلقة في الشبكة — **يُوصى بأن تتحقق كل الدفعات القادمة من هذا الملف أيضاً بشكل روتيني.**

## متوقف عنده (لرئيس التحرير)
- **تعارضا slug عابران للمسارين جديدان**: `thk-gunnel-cederblad` و`thk-jacqueline-astington` — أسماء مختلفة
  تماماً بين النسخة المعتمدة والنسخة في drafts/spark، سُجّلا في `agents_specs/requests-minimax.md`.
- Task 13: 49 ملفاً منجزاً عبر 5 دفعات من أصل ~147 مدرسة مقدَّرة أصلاً.

## الملفات
content/ar/drafts/minimax/schools/{sch-milan-systemic,sch-transactional-analysis,sch-nlp,sch-teacch,sch-dance-movement-therapy,sch-dit,sch-multicultural-counseling,sch-restorative-justice,sch-feldenkrais,sch-naikan-therapy}.md
