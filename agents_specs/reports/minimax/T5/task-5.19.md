# Task 5.19
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/، آخر دفعة أبجدياً — حرف Z) | الملفات: 9

## الأرقام
مخالفات preflight النهائية: 0
belongs_to نصية حرة عولجت: 2 (sch-zaydi-kalam→حُذف، مسجل مسبقاً في missing-schools.md ضمن "علم الكلام الإسلامي"؛ sch-zoroastrian-philosophy→حُذف "تقاليد الحكمة الإيرانية" كفئة عامة)
تصحيحات عناوين related متضاربة: ~6 (بما فيها تكرار مشكلة "مادهيامaka" المشوّهة في sch-zen-soto وsch-zen-rinzai)
لا خلطات هوية جديدة في هذه الدفعة الصغيرة.

## أمر التحقق
`python3 scripts/task.py verify minimax 5.19` → قائمة سوداء متبقية: **0** · سقّالة ظاهرة: 0
`python3 scripts/build_slug_index.py` → 6903 عنصر (نفس مستوى التعارضات السابق، لم تتغير)

## قرارات اتخذتها
- sch-zaydi-kalam.md: "علم الكلام الإسلامي" كانت مسجلة بالفعل في missing-schools.md من دفعة سابقة (7 أعضاء يتامى) — حذفت الرابط النصي الحر من الملف بدون تسجيل مكرر.
- sch-zoroastrian-philosophy.md: "تقاليد الحكمة الإيرانية" فئة عامة بلا ملف مطابق — حُذفت بلا تسجيل.

## هذه آخر دفعة أبجدياً من Task 5 (schools/ من A إلى Z)
تأكدت بفحص الملفات إن دي آخر ملفات schools/ (حرف Z). **Task 5 على schools/ يبدو مكتملاً أو قريباً من الاكتمال** — يستحق فحص من كلود لتأكيد عدم وجود دفعات متبقية قبل الانتقال لـTask 6.

## الملفات
content/ar/schools/sch-yinyang.md
content/ar/schools/sch-yoga.md
content/ar/schools/sch-yogacara.md
content/ar/schools/sch-zaydi-kalam.md
content/ar/schools/sch-zen-rinzai.md
content/ar/schools/sch-zen-soto.md
content/ar/schools/sch-zonghengjia.md
content/ar/schools/sch-zoroastrian-philosophy.md
content/ar/schools/sch-zurvanism.md
