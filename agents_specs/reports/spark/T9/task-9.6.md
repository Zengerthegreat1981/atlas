# Task 9.6
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0 (اتصلح 6 حالات + 1 YAML مكسور ظهرت أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: 0/30 (كل الملفات مهارات DBT فرعية — لا دراسة معزولة عن حزمة DBT الكاملة موثقة لأي منها، فسُجّل هذا صراحة في gaps بدل اختراع مصدر)

## أمر التحقق
python3 scripts/task.py verify spark 9.6
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- الدفعة كلها تقنيات DBT فرعية — رُبطت جميعها بـ sch-dbt وthk-mlinehan (مارشا لينهان، 1993) وdis-borderline-personality (الاضطراب المستهدف الأصلي)، مع سبب مذكور بالمتن في كل ملف.
- evidence_level محافظ في كل الملفات (experimental أو probably-efficacious) — الدليل التجريبي موجود على مستوى حزمة DBT الكاملة (تجربة لينهان 1991)، وليس لكل مهارة فرعية معزولة؛ هذا مسجَّل بدقة في gaps بدل الادعاء بدليل مباشر.
- tec-dbt-dt-reality-acceptance.md: **إصلاح جوهري** — كان يربط خطأً بـ tec-act-acc-radical-acceptance (نسخة ACT) بدل tec-dbt-dt-radical-acceptance (نسخة DBT الصحيحة).
- tec-dbt-dt-self-soothe-with-the-five-senses.md: حُذف رابط dis-disruptive-mood-dysregulation غير المبرر نصياً واستُبدل بـ dis-ptsd المذكور فعلياً.
- tec-dbt-dt-rescue-thinking.md: لم أتمكن من تأكيد وجود "Rescue Thinking" كمهارة DBT رسمية بهذا الاسم في دليل لينهان — سُجِّل الشك صراحة في gaps بدل الجزم.
- تكرارات مفهومية بين مدرستين (DBT وACT) سُجِّلت في gaps بدون دمج حسب التعليمات: tec-dbt-dt-urge-surfing/tec-act-pres-urge-surfing، tec-dbt-dt-willingness-vs-willfulness/tec-act-acc-willingness-vs-willfulness (كلاهما يرجع لمصدر واحد: جيرالد ماي، بلا ملف مفكر في الأطلس).
- tec-dbt-er-please.md مقابل tec-dbt-er-abc-please.md: تحقق كامل من عدم التكرار — الأول يغطي العوامل الفسيولوجية الخمسة فقط، الثاني حزمة أوسع (بناء تجارب إيجابية + PLEASE كعنصر فرعي).
- كل الروابط تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- جيرالد ماي (May) مصدر تمييز willingness/willfulness في مدرستين (DBT وACT) — بلا ملف thk- في الأطلس.
- "Rescue Thinking" في tec-dbt-dt-rescue-thinking.md — غير مؤكد كمصطلح DBT رسمي، يحتاج تحقق بشري.
- عدة تكرارات مفهومية بين DBT وACT (urge surfing، willingness vs willfulness) — طبيعية (نفس التقنية تُستخدم في مدرستين) لكن تحتاج مراجعة تصنيفية.

## الملفات
content/ar/techniques/tec-dbt-daily-environmental-cues-for-skill-use.md
content/ar/techniques/tec-dbt-daily-skills-chaining-skill-stacking.md
content/ar/techniques/tec-dbt-daily-weekly-skills-review.md
content/ar/techniques/tec-dbt-dt-alternate-rebellion-adaptive-denial.md
content/ar/techniques/tec-dbt-dt-distract-with-accepts.md
content/ar/techniques/tec-dbt-dt-improve-the-moment.md
content/ar/techniques/tec-dbt-dt-practicing-imperfection.md
content/ar/techniques/tec-dbt-dt-pros-and-cons.md
content/ar/techniques/tec-dbt-dt-radical-acceptance.md
content/ar/techniques/tec-dbt-dt-reality-acceptance.md
content/ar/techniques/tec-dbt-dt-rescue-thinking.md
content/ar/techniques/tec-dbt-dt-self-soothe-with-the-five-senses.md
content/ar/techniques/tec-dbt-dt-stop.md
content/ar/techniques/tec-dbt-dt-tipp.md
content/ar/techniques/tec-dbt-dt-turning-the-mind.md
content/ar/techniques/tec-dbt-dt-urge-surfing.md
content/ar/techniques/tec-dbt-dt-willingness-vs-willfulness.md
content/ar/techniques/tec-dbt-er-abc-please.md
content/ar/techniques/tec-dbt-er-accumulating-positives-build-mastery.md
content/ar/techniques/tec-dbt-er-behavioral-chain-analysis.md
content/ar/techniques/tec-dbt-er-building-positive-experiences.md
content/ar/techniques/tec-dbt-er-check-the-facts.md
content/ar/techniques/tec-dbt-er-cope-ahead.md
content/ar/techniques/tec-dbt-er-dialectical-thinking.md
content/ar/techniques/tec-dbt-er-labeling-emotions.md
content/ar/techniques/tec-dbt-er-mindful-eating.md
content/ar/techniques/tec-dbt-er-model-for-describing-emotions.md
content/ar/techniques/tec-dbt-er-myths-about-emotions.md
content/ar/techniques/tec-dbt-er-opposite-action.md
content/ar/techniques/tec-dbt-er-please.md
