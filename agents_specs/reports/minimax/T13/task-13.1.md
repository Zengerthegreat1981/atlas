# Task 13.1 — المدارس الغائبة (دفعة 1)
الحالة: مكتمل | الملفات: 10

## العملية
إنشاء 10 ملفات مدرسة جديدة في `content/ar/drafts/minimax/schools/` من قائمة الأولويات المؤكدة في Task 13،
كل ملف عبر subagent مستقل بمادة موثقة وربط الأعضاء اليتامى الفعليين.

## الملفات
- sch-adlerian.md — علم النفس الفردي الأدلري (23 عضواً مربوطاً من 24)
- sch-critical-psychology.md — علم النفس النقدي (6 أعضاء)
- sch-islamic-kalam.md — علم الكلام الإسلامي (المظلة العامة، 7 فروع/أعضاء)
- sch-lacanian.md — اللاكانية (12 عضواً)
- sch-mst.md — العلاج متعدد الأنظمة MST (11 عضواً)
- sch-psychodrama.md — السيكودراما والسوسيومتري (7 أعضاء)
- sch-strategic-family.md — العلاج الأسري الاستراتيجي (9 أعضاء)
- sch-political-philosophy.md — الفلسفة السياسية المعاصرة (11 عضواً)
- sch-psychosocial-rehabilitation.md — التأهيل النفسي-الاجتماعي (12 عضواً)
- sch-art-therapy.md — العلاج بالفن (6 أعضاء)

## قرارات اتخذتها
- **sch-philosophy-of-science**: لم يُنشأ — الموضوع مغطى بالفعل في `content/ar/schools/sch-phil-science.md` (معتمد). تم تفادي تكرار.
- استُبعدت روابط لأعضاء محجورين أو مصادر غير موثقة (thk-spiper، thk-grose، thk-kets) بدل اختلاق ربط.

## متوقف عنده (لرئيس التحرير)
- **تعارض slug عابر للمسارين**: `thk-dgray` موجود بمحتوى مختلف تماماً في كل من
  `content/ar/thinkers/thk-dgray.md` (مسار MiniMax) و `content/ar/drafts/spark/thinkers/thk-dgray.md` (مسار Spark).
- **تعارض slug عابر للمسارين**: `thk-jgantt` نفس المشكلة — "جوزيف غانت" في `content/ar/thinkers/thk-jgantt.md`
  مقابل "سوزان ب. غانت" في `content/ar/drafts/spark/thinkers/thk-jgantt.md`.
  سُجّلا في `agents_specs/requests-minimax.md` لطلب حسم من رئيس التحرير (لا يمكن حسمهما ضمن Task 13).

## الملفات
content/ar/drafts/minimax/schools/{sch-adlerian,sch-critical-psychology,sch-islamic-kalam,sch-lacanian,sch-mst,sch-psychodrama,sch-strategic-family,sch-political-philosophy,sch-psychosocial-rehabilitation,sch-art-therapy}.md
