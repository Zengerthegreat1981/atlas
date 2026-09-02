# Task 17.1
الحالة: مكتمل جزئياً
العملية: طبقة ما بعد 2010 — 5 مفاهيم جديدة تمثّل كل عنقود من عناقيد Task 17 الستة (5 subagent متوازي) | الملفات: 5

## الأرقام
مسودات الأطلس الكلية: 208 → 214 (+6 صافي)

## أمر التحقق
`python3 scripts/preflight_check.py` على كل ملف → صفر مخالفات آلية (بعد إضافة جملة صريحة تشرح رابط con-set-and-setting بالاسم في con-psychedelic-renaissance.md، وهو كان الشرط اللي SPARK.md بينص عليه لاستخدام هذا الرابط تحديداً)
`python3 scripts/build_slug_index.py` → 6832 عنصر (6618 معتمد + 214 مسودة)

## قرارات اتخذتها
- كتبت مفهوماً واحداً ممثِّلاً من كل عنقود من عناقيد Task 17 الستة: آليات العلم المفتوح، الطب النفسي الحوسبي، نظرية الشبكة في علم النفس المرضي، نهضة المهلوسات، والرعاية المستنيرة بالصدمة — العنقود السادس (الصحة النفسية العالمية: mhGAP، نقل المهام، PM+، Friendship Bench) لسه مش مكتوب.
- ملفا "الطب النفسي الحوسبي" و"نظرية الشبكة" مُصمَّمان عمداً ليكملا (لا يكرّرا) ملفَي المفكرَين thk-friston وthk-borsboom المكتوبين في دفعة سابقة من نفس الجلسة (Task 13) — الأول عن سيرة الشخص، الثاني عن الحقل/الإطار النظري نفسه بوصفه مفهوماً مستقلاً.
- طول محتوى كل ملف (بدون frontmatter وقسم المصادر) بين 2,400-3,050 حرف — تحققت يدوياً من طول المتن الفعلي بعد ما لاحظت إن حجم الملف الكامل بالبايت لبعضها قريب من 6,000-7,500 بايت (ده شامل الـfrontmatter الطويل نسبياً لهذا النوع من الملفات، مش المتن نفسه اللي هو الخاضع لسقف 6,000 حرف).
- تجنبت اختراع thk-shay وthk-meyer (مؤلفَي مفهومي الإصابة الأخلاقية وضغط الأقلية) رغم أهميتهما — سُجِّلا في gaps كطلبات slug جديدة.

## متوقف عنده (لرئيس التحرير)
- عنقود "الصحة النفسية العالمية" (mhGAP، نقل المهام Task-Shifting، PM+، Friendship Bench، فجوة العلاج) لسه غير مكتوب.
- طلبات slugs جديدة تراكمت من عدة دفعات (thk-shay، thk-meyer، thk-hare، thk-bordin، thk-horvath، thk-putnam، thk-carlson-bernstein، thk-iwata، thk-cade، thk-sternbach، thk-lewy) — تستحق تجميعها في `agents_specs/requests-spark.md` رسمياً.

## الملفات
content/ar/drafts/spark/concepts/con-open-science-reform-psychology.md
content/ar/drafts/spark/concepts/con-computational-psychiatry.md
content/ar/drafts/spark/concepts/con-network-theory-psychopathology.md
content/ar/drafts/spark/concepts/con-psychedelic-renaissance.md
content/ar/drafts/spark/concepts/con-trauma-informed-care.md
