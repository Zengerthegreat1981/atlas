# Task 9.2
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0 (اتصلح سطر واحد اتشاف أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: 0/30 → 3/30 (aedp، tec-alexander-technique، tec-animal-assisted-therapy — الوحيدة اللي عندها مصدر حقيقي موثّق معزول عن الحزمة)

## أمر التحقق
python3 scripts/task.py verify spark 9.2
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 3 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- معظم تقنيات ACT الفرعية (pres-/sac-/val-): evidence_level = experimental أو probably-efficacious/traditional تحفظياً — لا دراسة معزولة عن حزمة ACT ككل موثقة لكل تقنية بمفردها.
- tec-act-pres-mindful-breathing.md: حُذفت 4 روابط dis- غير مبررة نصياً (نسخ-لصق واضح: developmental-coordination، nightmare-disorder، specific-learning-disorder، tic-disorders) واستُبدلت بروابط مبررة فعلياً في المتن.
- tec-act-pres-body-scan.md: ربط بـ thk-jkabat-zinn (مبتكر مسح الجسد ضمن MBSR)، probably-efficacious بسند ميتا-تحليلات MBSR.
- tec-act-pres-urge-surfing.md: ربط بـ thk-amarlatt (ألان مارلات، مبتكرها 1985) وtec-mbrp، مع ذكر دراسة Bowen et al. 2014 (JAMA Psychiatry) بلا أرقام مختلقة.
- tec-act-sac-safe-place.md: حُذفت روابط غير مبررة (مسح الجسد/تنفس بيقظة/PMR) واستُبدلت بروابط مبررة نصياً + تصحيح title "تِيب" → "تيب (TIPP)" ليطابق العنوان الحقيقي.
- tec-aedp.md: تصحيح belongs_to من sch-psychoanalysis (خطأ) إلى sch-aedp الصحيح؛ حذف مرجع مختلق (LeDoux 2009) واستبداله بمصدرين حقيقيين (Fosha 2000، Fosha/Siegel/Solomon 2009).
- tec-aedp-emotion-to-emotion-processing.md: تصحيح title رابطين (con-aedp-emotion، con-aedp-transformance) كانا مختصرين وغير مطابقين للعنوان الحقيقي للملف المستهدف.
- tec-aedp-transformational-affects.md: حذف مصطلح "Vis Medicatrix Naturae" غير الموثق واستبداله بمصطلح فوشا الموثق "Transformance".
- tec-aedp-undoing-aloneness.md: حذف اقتباس منسوب لفوشا غير قابل للتحقق من نصه الإنجليزي الدقيق.
- جميع ملفات AEDP: evidence_level = experimental بسند دراسة Iwakabe et al. 2020 (Psychotherapy) — دراسة فعالية طبيعية بلا مجموعة ضابطة، وليست RCT.
- tec-animal-assisted-therapy.md: أصلح edges.target حر "العلاج البيئي/الطبيعي" → استُبدل بـ sch-humanistic (أقرب slug حقيقي موثق)، مع تسجيل غياب slug مخصص للعلاج البيئي في gaps. طُلب slug جديد لـ Boris Levinson في requests-spark.md.
- tec-alexander-technique.md: ربط بمؤسسها thk-falexander (موجود أصلاً) ومنافسها thk-mfeldenkrais، مع دراسة حقيقية (Little et al. 2008, BMJ, ATEAM trial).
- tec-affirmative-therapy.md: ربط بـ br-conversion-therapy كتقنية متضادة (لا منافسة) مع تسويغ نصي واضح للتباين.
- كل الروابط المضافة تحققت من EXISTING_SLUGS.md قبل الإضافة؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- thk-boris-levinson (مؤسس العلاج بمساعدة الحيوان): لا يوجد له ملف مفكر — طُلب في requests-spark.md.
- لا يوجد slug مدرسة مخصص لـ"العلاج البيئي/الطبيعي" (ecotherapy) — استُخدم sch-humanistic كأقرب بديل موثق مؤقتاً؛ يحتاج قرار لاحق هل يُنشأ slug مستقل.
- Kevin Polk، Andrew Gloster، Gerald May، Boris Levinson: مبتكرون مذكورون بالاسم بلا ملف thk- في الأطلس.

## الملفات
content/ar/techniques/tec-act-pres-anchoring-in-the-five-senses.md
content/ar/techniques/tec-act-pres-body-scan.md
content/ar/techniques/tec-act-pres-mindful-breathing.md
content/ar/techniques/tec-act-pres-mindful-eating.md
content/ar/techniques/tec-act-pres-noticing-without-judgment.md
content/ar/techniques/tec-act-pres-observing-the-present.md
content/ar/techniques/tec-act-pres-urge-surfing.md
content/ar/techniques/tec-act-sac-noticing-who-is-noticing.md
content/ar/techniques/tec-act-sac-perspective-taking.md
content/ar/techniques/tec-act-sac-safe-place.md
content/ar/techniques/tec-act-sac-the-chessboard-metaphor.md
content/ar/techniques/tec-act-sac-the-house-of-self-exercise.md
content/ar/techniques/tec-act-sac-the-observer-self-meditation.md
content/ar/techniques/tec-act-sac-the-sky-and-weather-metaphor.md
content/ar/techniques/tec-act-val-bullseye-exercise.md
content/ar/techniques/tec-act-val-life-compass.md
content/ar/techniques/tec-act-val-personal-mission-statement.md
content/ar/techniques/tec-act-val-values-based-decision-making.md
content/ar/techniques/tec-act-val-values-clarification-worksheet.md
content/ar/techniques/tec-act-val-values-vs-goals-distinction.md
content/ar/techniques/tec-act-val-write-your-own-eulogy.md
content/ar/techniques/tec-aedp-emotion-to-emotion-processing.md
content/ar/techniques/tec-aedp-metatherapeutic-processing.md
content/ar/techniques/tec-aedp-relational-reflectiveness.md
content/ar/techniques/tec-aedp-transformational-affects.md
content/ar/techniques/tec-aedp-undoing-aloneness.md
content/ar/techniques/tec-aedp.md
content/ar/techniques/tec-affirmative-therapy.md
content/ar/techniques/tec-alexander-technique.md
content/ar/techniques/tec-animal-assisted-therapy.md
