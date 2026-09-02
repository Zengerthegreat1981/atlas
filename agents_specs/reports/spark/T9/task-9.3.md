# Task 9.3
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0 (اتصلح 3 حالات ظهرت أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: تقريباً 0/30 → 12/30

## أمر التحقق
python3 scripts/task.py verify spark 9.3
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 12 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-authentic-movement.md: صُحح title لـ thk-jung من "كارل يونغ" إلى "كارل غوستاف يونغ"؛ أُضيفت المبتكرة الحقيقية thk-mwhitehouse (ماري ستاركس وايتهاوس، وليس المذيعة البريطانية المشابهة الاسم) وthk-jadler.
- tec-beck-cognitive-therapy.md: evidence_level = well-established (عشرات RCTs موثقة للاكتئاب أحادي القطب وفق معايير APA)، ربط بـ thk-beck وwrk-beck-cognitive-therapy-depression.
- tec-bedwetting-alarm.md: أُصلح edges.belongs_to من نص حر "العلاج السلوكي" إلى sch-behaviorism؛ صُححت title لـ tec-cbt-prob-behavioral-contracting وtec-psychoeducational-family لتطابق العناوين الحقيقية.
- tec-behavioral-medicine.md: صُححت title لـ con-behavioral-medicine؛ حُذفت 6 روابط dis- غير مبررة نصياً (اضطرابات جنسية، Pica، Rumination) واستُبدلت بـ dis-insomnia-disorder المذكور فعلياً.
- tec-biofeedback.md: حُذف ادعاء غير موثق (نسبة تأسيس مركز بيوفيدباك لـ"إليزابيث لومباردي") واستُبدل بتاريخ حقيقي (ميلر 1969، الزوجان جرين، تأسيس AAPB 1969)؛ أُصلح country/language من [DRAFT-UNKNOWN].
- tec-brainspotting.md: تحقق من الملاحظة الأصلية عن title tec-emdr — تبيّن أنه كان صحيحاً بالفعل، لا إصلاح لازم.
- tec-buddhist-informed-psychotherapy.md: صُححت title لـ tec-mbsr ("القائم على" كانت ناقصة)؛ أُضيف ## المصادر (لم يكن موجوداً) بمرجع حقيقي (Fromm/Suzuki/De Martino 1960).
- tec-cbt-cog-thought-defusion.md: صُححت title لـ tec-act-def-labeling-thoughts من "وسم الأفكار (ACT)" إلى "تسمية الأفكار".
- tec-cbt-cog-cognitive-restructuring.md: صُححت 3 عناوين related (thk-beck، con-cognitive-distortion، con-automatic-thought)؛ حُذفت 11 رابط dis- غير مبرر نصياً.
- tec-cbt-cog-socratic-questioning.md: صُحح خطأ إملائي في المتن "آلانت بيك" → "آرون بيك".
- tec-cbt-cog-decisional-balance-sheet.md: صُححت title لـ thk-diclemente من "كارل دي كليمنتي" إلى "كارلو دي كليمنتي" (مطابقةً للعنوان في drafts/spark/thinkers).
- عدة ملفات (habit-reversal، pleasant-activity-scheduling، graded-task، cbasp، cbct-couples إلخ): evidence_level محافظ حيثما لا توجد دراسة `stu-` مستقلة معزولة عن الحزمة العلاجية الأوسع؛ سُجّل هذا كسبب مسمّى في gaps بدل اختراع رابط أو دراسة.
- كل الروابط المضافة تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- R.G. Nunn (شريك آزرين)، Lewinsohn، صمويل كروذرز (bibliotherapy)، نيل إ. ميلر والزوجان جرين (biofeedback)، Frank Dattilio (cbct-couples)، دومينيلي وطومسون (AOP): مبتكرون مذكورون بالاسم بلا ملف thk- في الأطلس. طُلب Dattilio في requests-spark.md.
- عدة دراسات حقيقية مذكورة بالاسم (Azrin & Nunn 1973، Jacobson et al. 1996، Baucom Sayers & Sher 1990) بلا ملف stu- مستقل في الأطلس — الأدلة موجودة نصياً لكن بلا رابط قابل للتحقق آلياً.
- tec-cbt-cog-behavioral-experiments.md وtec-cbt-beh-behavioral-experiments.md: تشابه بالاسم لكن تأكد أنهما غير مكررين (زاويتان مختلفتان: معرفي مقابل سلوكي) — موثق في متن كل منهما.

## الملفات
content/ar/techniques/tec-anti-oppressive-practice.md
content/ar/techniques/tec-authentic-movement.md
content/ar/techniques/tec-beck-cognitive-therapy.md
content/ar/techniques/tec-bedwetting-alarm.md
content/ar/techniques/tec-behavioral-activation.md
content/ar/techniques/tec-behavioral-medicine.md
content/ar/techniques/tec-bibliotherapy.md
content/ar/techniques/tec-biofeedback.md
content/ar/techniques/tec-bowen-family-systems.md
content/ar/techniques/tec-brainspotting.md
content/ar/techniques/tec-buddhist-informed-psychotherapy.md
content/ar/techniques/tec-cat.md
content/ar/techniques/tec-cbasp.md
content/ar/techniques/tec-cbct-couples.md
content/ar/techniques/tec-cbt-beh-behavioral-experiments.md
content/ar/techniques/tec-cbt-beh-behavioral-rehearsal.md
content/ar/techniques/tec-cbt-beh-delayed-response-strategy.md
content/ar/techniques/tec-cbt-beh-graded-task-assignment.md
content/ar/techniques/tec-cbt-beh-habit-reversal-training.md
content/ar/techniques/tec-cbt-beh-pleasant-activity-scheduling.md
content/ar/techniques/tec-cbt-beh-role-playing.md
content/ar/techniques/tec-cbt-cog-behavioral-experiments.md
content/ar/techniques/tec-cbt-cog-challenging-cognitive-distortions.md
content/ar/techniques/tec-cbt-cog-cognitive-reframing.md
content/ar/techniques/tec-cbt-cog-cognitive-restructuring.md
content/ar/techniques/tec-cbt-cog-decisional-balance-sheet.md
content/ar/techniques/tec-cbt-cog-downward-arrow-technique.md
content/ar/techniques/tec-cbt-cog-identifying-core-beliefs-schemas.md
content/ar/techniques/tec-cbt-cog-socratic-questioning.md
content/ar/techniques/tec-cbt-cog-thought-defusion.md
