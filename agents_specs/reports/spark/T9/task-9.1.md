# Task 9.1
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0 (بعد إصلاح 6 حالات ظهرت أثناء الكتابة)
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: 1/30 (تقنية واحدة فقط — tec-act-def-titchener-s-repetition — عندها دراسة مفردة موثقة؛ الباقي 29 لا دراسة معزولة موثقة لهم بمعزل عن حزمة ACT ككل، فسُجّل هذا في gaps بدل اختراع مصدر)

## أمر التحقق
python3 scripts/task.py verify spark 9.1
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 1 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- 29 من أصل 30 ملفاً (كل تقنيات ACT الفرعية): evidence_level = experimental أو probably-efficacious بشكل تحفظي — لا توجد دراسة (stu-) موثّقة في الأطلس تختبر التقنية الفرعية بمعزل عن حزمة ACT الكاملة؛ الأدلة العامة لـACT ككل غير موثقة كـslug مستقل، فلم تُستخدم كسند.
- tec-act-def-titchener-s-repetition.md: وُجدت دراسة حقيقية (Masuda, Hayes, Sackett & Twohig, 2004, Behaviour Research and Therapy) تختبر هذه التقنية بالتحديد → evidence_level = probably-efficacious مع قسم ## المصادر.
- tec-abm.md: evidence_level = controversial (تجارب معشاة حديثة فشلت في إظهار تفوق عن الضبط الوهمي)؛ حُذف رابط غير مبرر لـ tec-cbt-psychosis.
- tec-accelerated-resolution-therapy.md: تصحيح اسم المؤسِّسة من صيغة خاطئة إلى "لايني روزنويغ / Laney Rosenzweig"، وربط بتقنيات منافسة موثقة (EMDR، Flash Technique، Brainspotting).
- tec-act-def-labeling-thoughts.md: حُذف رابطان بلا أي سند نصي (dis-developmental-coordination، dis-specific-learning-disorder) واستُبدلا بـ dis-gad وdis-ptsd المذكورين فعلياً في المتن.
- tec-act-hexaflex.md: تصحيح edges — developed_by كان نصاً حراً "ستيفن هايز" بدل slug، وbelongs_to كان يشير لـ rel-act بدل sch-act الصحيح.
- tec-act-defusion-leaves-stream.md مقابل tec-act-def-leaves-on-a-stream.md: تقنيتان شبه متطابقتين بslug مختلف (ازدواج محتمل) — لم أُدمج أو أحذف لأن كل ملف كان مصرَّحاً به لعامل مختلف؛ سُجّل في gaps للمراجعة اليدوية اللاحقة.
- كل الروابط المضافة في related تحققت من EXISTING_SLUGS.md قبل الإضافة؛ لم يُخترع أي slug.

## متوقف عنده (لرئيس التحرير)
- ازدواج محتمل: tec-act-defusion-leaves-stream.md (TEC-0379) و tec-act-def-leaves-on-a-stream.md (TEC-0026) — نفس الاستعارة العلاجية (أوراق على النهر) بـslug مختلف. الأول أكمل بكثير. يحتاج قرار دمج/إحالة بشرياً.
- عدة مبتكرين مذكورين بالاسم في المتون بلا ملف thk- في الأطلس (Kevin Polk، Andrew Gloster، Gerald May، كولين ماكليود، مؤسِّسة ART) — لم يُربطوا، مُسجَّلون كفجوات بدل اختراع slug.

## الملفات
content/ar/techniques/tec-abm.md
content/ar/techniques/tec-accelerated-resolution-therapy.md
content/ar/techniques/tec-acceptance-based-bt.md
content/ar/techniques/tec-act-acc-creative-hopelessness.md
content/ar/techniques/tec-act-acc-dropping-the-struggle.md
content/ar/techniques/tec-act-acc-emotional-exposure.md
content/ar/techniques/tec-act-acc-expanding-awareness-making-room.md
content/ar/techniques/tec-act-acc-pain-vs-suffering.md
content/ar/techniques/tec-act-acc-radical-acceptance.md
content/ar/techniques/tec-act-acc-self-compassion-exercises.md
content/ar/techniques/tec-act-acc-willingness-vs-willfulness.md
content/ar/techniques/tec-act-ca-act-matrix.md
content/ar/techniques/tec-act-ca-behavioral-commitment-exercises.md
content/ar/techniques/tec-act-ca-if-then-planning.md
content/ar/techniques/tec-act-ca-self-rewarding.md
content/ar/techniques/tec-act-ca-smart-goals-in-act.md
content/ar/techniques/tec-act-ca-taking-the-first-step.md
content/ar/techniques/tec-act-ca-tiny-steps-approach.md
content/ar/techniques/tec-act-ca-willingness-to-fail-forward.md
content/ar/techniques/tec-act-def-carrying-a-card-with-your-thought.md
content/ar/techniques/tec-act-def-labeling-thoughts.md
content/ar/techniques/tec-act-def-leaves-on-a-stream.md
content/ar/techniques/tec-act-def-observing-self-talk.md
content/ar/techniques/tec-act-def-physicalizing-the-thought.md
content/ar/techniques/tec-act-def-singing-thoughts.md
content/ar/techniques/tec-act-def-thanking-your-mind.md
content/ar/techniques/tec-act-def-the-hands-as-thoughts-metaphor.md
content/ar/techniques/tec-act-def-titchener-s-repetition.md
content/ar/techniques/tec-act-defusion-leaves-stream.md
content/ar/techniques/tec-act-hexaflex.md
