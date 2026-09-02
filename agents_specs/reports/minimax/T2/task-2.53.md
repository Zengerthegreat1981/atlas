# Task 2.53 — آخر دفعة في Task 2
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها | الملفات: 1

## الأرقام
هذه آخر دفعة متبقية في طابور Task 2 — `python3 scripts/task.py get minimax 2 10` رجّع بعدها
"مفيش ملفات جديدة في Task 2 — كل ملفاته اتاخدت قبل كده."

## قرارات اتخذتها
- **thk-marymain (ماري مين)**: موثّقة. عالمة نفس تطوّرية أمريكية حقيقية، بيركلي، مطوّرة مقابلة
  التعلق في البلوغ (AAI) مع Erik Hesse واكتشاف نمط التعلق غير المنظَّم (Type D) مع Solomon —
  محتوى دقيق ومفصّل أصلاً. صُححت: `edges.developed` كان نصاً حراً "نظرية التعلق (Attachment
  Theory)" → حُوّل لـslug حقيقي مطابق تماماً `br-attachment-theory`. حُذفت جملة القائمة السوداء
  المكرَّرة (في `gaps` وفي قسم "اقتباسات مختارة")، أُضيف `## المصادر` بمراجع حقيقية.

## أمر التحقق
`python3 scripts/preflight_check.py content/ar/thinkers/thk-marymain.md` → ✅ صفر مخالفات آلية

## ملخص Task 2 كاملاً
Task 2 خلصت بالكامل: **53 دفعة، ~799 ملف** فُحصت من "الملفات المشكوك في وجود أصحابها" عبر
thk-m إلى thk-z. النتيجة التراكمية تقريباً:
- الأغلبية الساحقة (~93%) موثّقة فعلياً بمصادر حقيقية بعد تصحيحات دقة (تواريخ، نسبة أعمال، هوية).
- عشرات الملفات اتحجرت لعدم وجود دليل مستقل على وجود الشخص، أو لأن الـslug ما بيطابقش اسم صاحب
  المحتوى الفعلي إطلاقاً (قاعدة 6) — كل حالة مسجّلة في `agents_specs/quarantine-minimax.md`.
- ~8 حالات ازدواج حقيقية اتحسمت (نفس الشخص بslugين) بإحالة صريحة بدل تكرار السيرة، من ضمنها:
  thk-mwhitehouse/thk-mary-whitehouse، thk-rick-doblin/thk-rmdoblin، thk-richard-thaler/thk-rkthaler،
  thk-meillassoux/thk-quentin-meillassoux، thk-plevine/thk-peter-levine،
  thk-msrosenberg/thk-marshall-rosenberg، thk-mgrof/thk-sgrof، thk-pkuhn/thk-thomas-kuhn.
- سويب منهجي منفصل لقى ولحّم bug فني (preflight_check.py القديم ما كانش بيفحص القائمة السوداء
  جوه gaps/المتن) أثّر على 40+ ملف عبر دفعات سابقة — كلها اتصححت.
- عشرات المدارس/التيارات الغائبة اتسجلت في `agents_specs/missing-schools.md` لـTask 13.

## الملفات
content/ar/thinkers/thk-marymain.md
