# Task 9.5
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0 (اتصلح 3 حالات + 1 title mismatch ظهرت أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: تقريباً 0/30 → 9/30

## أمر التحقق
python3 scripts/task.py verify spark 9.5
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 9 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-cbt-mind-self-monitoring.md: حُذفت 16 رابط related غير ذي صلة (منسوخة من ملف آخر: اضطرابات جنسية، فصام، بيكا) واستُبدلت بـ dis-mdd/dis-gad/dis-binge-eating-disorder/dis-alcohol-use-disorder المبررة نصياً.
- tec-cbt-prob-crisis-survival-planning.md: صُححت title لـ tec-dbt-dt-stop.
- tec-child-parent-psychotherapy.md: صُححت title لـ thk-lieberman من "ألسي ليبرمان" إلى "أليسيا ليبرمان"؛ صُحح belongs_to من sch-humanistic إلى sch-psychoanalysis (أساس تحليلي حقيقي من عمل سيلما فرايبرغ).
- tec-cra.md: صُححت title لـ thk-nazrin من "نصرت أزرين" إلى "نَثَان هـ. أزّرين" (في related والمتن)؛ أُصلح edges.belongs_to من نص حر "الإدمان" إلى sch-behaviorism.
- tec-compassionate-mind-training.md: صُححت title لـ thk-pgilbert (كان "بول غيلبرت" خطأ) إلى "بول جيلبرت"؛ وصُححت title لـ dis-binge-eating-disorder أثناء المراجعة.
- tec-collaborative-language-systems.md: **إصلاح جوهري** — related كان يشير لثلاثة مفكرين غير مذكورين إطلاقاً في المتن (بيغي بن، تشارلز غيربر، كارمن ديلورو)، بينما المؤسسان الحقيقيان (هارلين أندرسون وهارولد غوليشيان) كانا بلا رابط — أُصلح بالكامل.
- tec-cognitive-hypnotherapy-silvester.md: **إصلاح جوهري** — edges.belongs_to كان يشير لنفس slug الملف (حلقة ذاتية) — أُصلح إلى br-clinical-hypnotherapy.
- tec-cognitive-reappraisal.md: **إصلاح تصنيف** — كان مصنفاً خطأً تحت sch-existential-therapy رغم أن مبتكره (Lazarus) ينتمي لـ sch-cognitive-behavioral حسب ملفه — صُحح crumb وbelongs_to.
- tec-classical-behavior-therapy.md: طُلب slug جديد لإدموند جاكوبسون (مخترع PMR الفعلي، منفصل عن thk-jacobson/thk-njacobson الموجودين).
- عدة طلبات slug جديدة أُضيفت لـ requests-spark.md: كانفر، هوم، لويس شوارتز، جورج دوران (SMART)، ستيفن كوفي (تحقق: غير موجود).
- كل الروابط المضافة تحققت من EXISTING_SLUGS.md أو بقراءة الملف فعلياً؛ تكرر رفض ربط slug بشخص مختلف الاسم مشابه في عدة ملفات (thk-lazarus/أرنولد وليس ريتشارد، thk-jacobson/إديث وليس إدموند، thk-mccullough/جيمس وليس مايكل).

## متوقف عنده (لرئيس التحرير)
- عدة مؤسسين حقيقيين بلا ملف thk- (إدموند جاكوبسون، فريدريك كانفر، لويد هوم، لويس شوارتز، جورج دوران) — مسجَّلون في requests-spark.md.
- tec-cbt-sud.md: المتن الأصلي نسب التقنية لأسماء تبدو ملفّقة/متضاربة (ماري جو روفيتو، كارل هانكس، بروس رادون) — استُبدلت بمصادر حقيقية موثقة (بيك 1993، كارول 1998) بدل الإبقاء على الادعاء المشكوك فيه.
- tec-ccbt.md: نسبة FearFighter وSilverCloud كانت خاطئة في المتن الأصلي — صُححت.

## الملفات
content/ar/techniques/tec-cbt-mind-self-monitoring.md
content/ar/techniques/tec-cbt-mind-values-clarification.md
content/ar/techniques/tec-cbt-prob-behavioral-contracting.md
content/ar/techniques/tec-cbt-prob-crisis-survival-planning.md
content/ar/techniques/tec-cbt-prob-prioritization-time-management.md
content/ar/techniques/tec-cbt-prob-smart-goal-setting.md
content/ar/techniques/tec-cbt-psychosis.md
content/ar/techniques/tec-cbt-sud.md
content/ar/techniques/tec-ccbt.md
content/ar/techniques/tec-cft.md
content/ar/techniques/tec-child-parent-psychotherapy.md
content/ar/techniques/tec-circle-of-security.md
content/ar/techniques/tec-classical-behavior-therapy.md
content/ar/techniques/tec-clinical-stress.md
content/ar/techniques/tec-cognitive-hypnotherapy-silvester.md
content/ar/techniques/tec-cognitive-hypnotherapy.md
content/ar/techniques/tec-cognitive-reappraisal.md
content/ar/techniques/tec-coherence-therapy.md
content/ar/techniques/tec-collaborative-language-systems.md
content/ar/techniques/tec-compassionate-mind-training.md
content/ar/techniques/tec-comprehensive-resource-model.md
content/ar/techniques/tec-contemplative-psychotherapy.md
content/ar/techniques/tec-contextual-family-therapy.md
content/ar/techniques/tec-contingency-management.md
content/ar/techniques/tec-cpt.md
content/ar/techniques/tec-cra.md
content/ar/techniques/tec-dance-movement-therapy.md
content/ar/techniques/tec-dbt-daily-daily-mindfulness-check-in.md
content/ar/techniques/tec-dbt-daily-dbt-coping-toolbox.md
content/ar/techniques/tec-dbt-daily-dbt-diary-card.md
