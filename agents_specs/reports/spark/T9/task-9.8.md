# Task 9.8
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

ملاحظة تنفيذية: حصل انقطاع بمنتصف الدفعة بسبب حد جلسة API مؤقت — 4 ملفات (tec-dit، tec-drama-therapy، tec-eft-emotion-focused-empty-chair، tec-emdr-eight-phase-protocol) اتعدّلت جزئياً في المحاولة الأولى وتحققت من سلامتها، والباقي (26 ملفاً) اتعدّل في محاولة إعادة تشغيل كاملة. كل الـ30 نجحوا في preflight وverify في النهاية.

## الأرقام
جمل القائمة السوداء: 0 → 0 (اتصلح 2 حالة gaps ظهرت أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: تقريباً 0/30 → 9/30

## أمر التحقق
python3 scripts/task.py verify spark 9.8
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 9 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-facilitated-communication.md: **evidence_level = discredited** بوضوح — تجارب معشّاة محكّمة (Mostert 2001، Ganz et al. 2012) أثبتت أن الميسِّر هو من يوجّه الحركة لا الشخص المتوحد نفسه، رفضتها ASHA وAPA. أُصلح belongs_to الذي كان يشير خطأً لنفس slug الملف (حلقة ذاتية).
- tec-erp.md: evidence_level = well-established (APA Division 12 لعلاج الوسواس القهري)؛ صُححت title لـ tec-classical-behavior-therapy.
- tec-emdr.md: صُححت title لـ tec-brainspotting.
- tec-ego-state.md: صُححت title لـ thk-federn من "بول فيدرن" إلى "بول فيديرن"؛ صُححت النسبة إلى المؤسسَين الحقيقيين جون وهيلين واتكنز (بلا slug — طُلب في requests-spark.md).
- tec-fbt-arfid.md: صُححت title لـ tec-psychoeducational-family وtec-cbt-exp-exposure-hierarchy-building.
- tec-five-dimensions-therapeutic-relationship.md: صُححت title لـ thk-mbuber من "مارتن بوبر" إلى "مارتن بُبَر".
- tec-eft-couples.md: حُذف ادعاء رقمي غير موثق "70-75%" لم يكن مسنوداً بمرجع محدد.
- tec-dit.md: أُضيف ## المصادر (Lemma, Target & Fonagy 2011).
- tec-eft-emotion-focused-empty-chair.md وtec-empty-chair-dialogue-eft.md: تكرار محتمل مسجَّل في gaps صراحة بدون دمج (خارج نطاق المهمة).
- عدة أسماء مؤسسين حقيقيين بلا ملف thk- (سيرينا ويدر، فيكتور ماير، John & Helen Watkins، Lonnie Barbach): سُجّلوا في requests-spark.md أو gaps بدل الاختراع.
- كل الروابط تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- سيرينا ويدر (DIR/Floortime)، فيكتور ماير (ERP)، John & Helen Watkins (Ego State Therapy)، Lonnie Barbach (Directed Masturbation): بلا ملف thk- في الأطلس.
- تكرار محتمل: tec-eft-emotion-focused-empty-chair.md وtec-empty-chair-dialogue-eft.md يغطيان نفس التقنية تقريباً بمحتوى متداخل — يحتاج قرار دمج/فصل بشري.
- 4 ملفات اتعدّلت في محاولة أولى منقطعة قبل استكمال الدفعة — تحقق preflight/verify النهائي أكدهم سليمين، لكن يُفضَّل مراجعة بشرية إضافية لهم تحديداً: tec-dit.md، tec-drama-therapy.md، tec-eft-emotion-focused-empty-chair.md، tec-emdr-eight-phase-protocol.md.

## الملفات
content/ar/techniques/tec-dbt.md
content/ar/techniques/tec-ddp.md
content/ar/techniques/tec-dir-floortime.md
content/ar/techniques/tec-directed-masturbation.md
content/ar/techniques/tec-discernment-counseling.md
content/ar/techniques/tec-dit.md
content/ar/techniques/tec-drama-therapy.md
content/ar/techniques/tec-eft-couples-de-escalation.md
content/ar/techniques/tec-eft-couples.md
content/ar/techniques/tec-eft-emotion-focused-empty-chair.md
content/ar/techniques/tec-eft-individual.md
content/ar/techniques/tec-ego-state.md
content/ar/techniques/tec-eight-dimensions-of-relatedness.md
content/ar/techniques/tec-elman-hypnosis.md
content/ar/techniques/tec-emdr-bilateral-stimulation.md
content/ar/techniques/tec-emdr-eight-phase-protocol.md
content/ar/techniques/tec-emdr-rdi-resource-installation.md
content/ar/techniques/tec-emdr-resourcing.md
content/ar/techniques/tec-emdr.md
content/ar/techniques/tec-empty-chair-dialogue-eft.md
content/ar/techniques/tec-encounter-groups.md
content/ar/techniques/tec-ericksonian-hypnotherapy.md
content/ar/techniques/tec-erp.md
content/ar/techniques/tec-experiential-symbolic-family.md
content/ar/techniques/tec-facilitated-communication.md
content/ar/techniques/tec-fap.md
content/ar/techniques/tec-fbt-arfid.md
content/ar/techniques/tec-feldenkrais-method.md
content/ar/techniques/tec-filial-therapy.md
content/ar/techniques/tec-five-dimensions-therapeutic-relationship.md
