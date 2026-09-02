# Task 9.4
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: تقريباً 0/30 → 3/30
YAML مكسور اتصلح: 3 ملفات (نقص سطر --- إغلاق)

## أمر التحقق
python3 scripts/task.py verify spark 9.4
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 3 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-cbt-cognitive-restructuring.md: **ازدواج مكتشف** مع tec-cbt-cog-cognitive-restructuring.md (عُدِّل في دفعة 9.3) — نفس التقنية بslug مختلف. لم يُدمج، سُجِّل في gaps.
- tec-cbt-emo-distress-tolerance-techniques.md: صُححت title لـ tec-dbt-dt-tipp، وصُحح خطأ إملائي في المتن "ليوينان" → "لينهان".
- tec-cbt-exp-in-vivo-exposure-with-response-prevention.md: صُححت title لـ tec-erp؛ استُبدل رابط dis-selective-mutism غير المبرر بـ dis-ocd.
- tec-cbt-mind-body-scan.md: **تكرار YAML فادح** (نفس الروابط الثلاثة مكررة ~10 مرات) — نُظّف الملف بالكامل.
- tec-cbt-mind-mindfulness-meditation.md: صُححت title لـ tec-mbsr؛ حُذف رابط syn-phantom-limb غير المبرر إطلاقاً.
- tec-cbt-mind-journaling-for-self-reflection.md: صُححت title لـ tec-writing-therapy.
- تصحيح اسم مبتكر: gratitude-practices — لم يُربط thk-mccullough لأنه شخص مختلف (جيمس ماكولوغ مؤسس CBASP وليس مايكل إي. ماكولوغ زميل إيمونز).
- boundary-setting-techniques: لم يُربط thk-deutsch (هيلين دويتش، محللة نفسية مختلفة) رغم وجود slug مشابه؛ مورتون دويتش الحقيقي بلا ملف.
- emotion-focused-coping: لم يُربط thk-lazarus لأنه أرنولد لازاروس شخص مختلف عن ريتشارد لازاروس/سوزان فولكمان (له مسودات غير مراجعة فقط).
- PMR: لم يُربط thk-jacobson (إديث جاكوبسون، محللة نفسية مختلفة عن إدموند جاكوبسون مخترع PMR) — طُلب slug جديد.
- طلبات slug جديدة أُضيفت لـ requests-spark.md: thk-edmund-jacobson، thk-borkovec، thk-spielman، thk-tgordon، thk-stampfl، thk-meyer-victor.
- كل الروابط المضافة تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع، ولا هوية مغلوطة (تكرر رفض ربط slug مشابه الاسم لشخص مختلف في 4 حالات).

## متوقف عنده (لرئيس التحرير)
- ازدواج محتمل: tec-cbt-cognitive-restructuring.md مقابل tec-cbt-cog-cognitive-restructuring.md — يحتاج قرار دمج/إحالة بشرياً.
- عدة أسماء مؤسسين حقيقيين مذكورين بالاسم بلا ملف thk- في الأطلس (مورتون دويتش، إدموند جاكوبسون، بوركوفيك، سبيلمان، توماس غوردون، ستامبفل، فيكتور ماير، روبرت سيلمان، غارفينكل/كريتشلي) — مسجَّلون في requests-spark.md أو gaps بدل الاختراع أو سوء الاستخدام.
- dis-selective-mutism: العنوان الفعلي فيه خطأ مطبعي (مسافة زائدة) — لوحظ من إحدى الوكلاء، خارج نطاق Task 9 (يخص disorders/).

## الملفات
content/ar/techniques/tec-cbt-cognitive-restructuring.md
content/ar/techniques/tec-cbt-emo-anger-management-techniques.md
content/ar/techniques/tec-cbt-emo-box-breathing.md
content/ar/techniques/tec-cbt-emo-coping-statements.md
content/ar/techniques/tec-cbt-emo-deep-breathing-techniques.md
content/ar/techniques/tec-cbt-emo-distress-tolerance-techniques.md
content/ar/techniques/tec-cbt-emo-emotion-focused-coping.md
content/ar/techniques/tec-cbt-emo-gratitude-practices.md
content/ar/techniques/tec-cbt-emo-interoceptive-awareness-training.md
content/ar/techniques/tec-cbt-emo-progressive-muscle-relaxation.md
content/ar/techniques/tec-cbt-emo-self-compassion-exercises.md
content/ar/techniques/tec-cbt-exp-exposure-hierarchy-building.md
content/ar/techniques/tec-cbt-exp-flooding.md
content/ar/techniques/tec-cbt-exp-in-vivo-exposure-with-response-prevention.md
content/ar/techniques/tec-cbt-exp-interoceptive-exposure.md
content/ar/techniques/tec-cbt-exp-worry-exposure.md
content/ar/techniques/tec-cbt-insomnia.md
content/ar/techniques/tec-cbt-int-active-listening-skills.md
content/ar/techniques/tec-cbt-int-assertiveness-training.md
content/ar/techniques/tec-cbt-int-boundary-setting-techniques.md
content/ar/techniques/tec-cbt-int-communication-skills-training.md
content/ar/techniques/tec-cbt-int-conflict-resolution-training.md
content/ar/techniques/tec-cbt-int-giving-and-receiving-feedback.md
content/ar/techniques/tec-cbt-int-perspective-taking.md
content/ar/techniques/tec-cbt-int-self-validation.md
content/ar/techniques/tec-cbt-mind-body-scan.md
content/ar/techniques/tec-cbt-mind-cbt-thought-log-thought-record.md
content/ar/techniques/tec-cbt-mind-grounding-techniques.md
content/ar/techniques/tec-cbt-mind-journaling-for-self-reflection.md
content/ar/techniques/tec-cbt-mind-mindfulness-meditation.md
