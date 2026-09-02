# Task 5.1
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة | الملفات: 40

## الأرقام
مخالفات preflight: 28 → 0
belongs_to نصية حرة معالجة: 12 (من أصل 40 ملفاً فيها edges/belongs_to)
  - تحويل فعلي لـslug موجود: 0 (كل الأسماء الحرة اللي فُحصت لم تطابق مدرسة موجودة فعلياً بملف)
  - حُذف الرابط (لا مدرسة حقيقية مطابقة/فئة عامة): 6 — br-aba-autism, br-abft, br-abstinence-vs-harm-reduction, br-cb-sex-therapy, br-case-management (الرابط بس، الملف بقى بدون edges), + غيرها
  - سُجّل في missing-schools.md (مدرسة حقيقية بلا ملف): 5 — علم النفس الشرعي/الجنائي، التكنولوجيا والعلاج الرقمي، علم الأعصاب الوجداني، الدعم والتأهيل النفسي-الاجتماعي، العلاج القصير المستقل (Brief Therapy/Palo Alto)
belongs_to كانت بالفعل slug صحيح (خارج نطاق التاسك، اتأكد منها بس): ~20 ملفاً

## أمر التحقق
`python3 scripts/task.py verify minimax 5.1` → جمل قائمة سوداء متبقية: 14 (خارج نطاق Task 5 — دي مهمة Task 6/10/11 لكسر القالب، مش belongs_to) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك، مهمة Task 4/8)

## قرارات اتخذتها
- br-aba-autism.md, br-abft.md, br-abstinence-vs-harm-reduction.md, br-advanced-aba-prt-vb.md (بعد مراجعة تانية), br-cb-sex-therapy.md: الـtarget النصي كان فئة تصنيفية عامة (نفس نص الـcrumb، زي "العلاج المتخصص بالإعاقات"، "مدارس نادرة/متفرقة") مش مدرسة فكرية لها مؤسس ومنهج → حُذف edges بالكامل، مفيش سطر بديل.
- br-aggression-treatment.md, br-ai-chatbot-therapy.md, br-affective-neuroscience-informed.md, br-case-management.md, br-brief-strategic-therapy.md: الـtarget يمثل مدرسة/تيار حقيقي موثّق (علم نفس جنائي، تكنولوجيا العلاج الرقمي، علم الأعصاب الوجداني، دعم وتأهيل نفسي-اجتماعي، Brief/Strategic Therapy عائلة Palo Alto) بس بلا ملف مخصص في content/ar/schools/ → حُذف edges من الملف وسُجّلت المدرسة في agents_specs/missing-schools.md لـTask 13.
- br-adlerian.md, br-budapest-berlin.md: edges فيها developed_by بقيمة اسم حر بدل slug → حوّلتها لـthk-adler وthk-vandeurzen/thk-sferenczi (تحققت من وجود الملفات).
- preflight كشف تطابقات id/title متضاربة في related لملفات: br-adlerian, br-aedp-applied, br-alchemical-psychology, br-archetypal, br-asharism-late-philosophical, br-attachment-theory, br-british, br-budapest-berlin, br-case-management, br-child-psychoanalysis — صحّحت العنوان المكتوب ليطابق العنوان الحقيقي في الملف المستهدف (فتحت كل ملف وتأكدت).
- br-affective-neuroscience-informed.md: gaps كانت فيها سطر "لا تاريخ نهاية موثّق" رغم إن active_end موجود فعلاً ("مستمر") → حذفت السطر، سيبت الفجوة الحقيقية بس.

## متوقف عنده (لرئيس التحرير)
- تضارب بين وكيلين على نفس النص "العلاج المتخصص بالإعاقات" (ظهر في br-aba-autism وbr-advanced-aba-prt-vb): وكيل واحد اعتبره فئة عامة، التاني سجّله كمدرسة غائبة. حسمت لصالح "فئة عامة" (يطابق نص الـcrumb حرفياً، لا مؤسس أو منهج محدد) وشلت السطر المكرر من missing-schools.md.
- الجمل القالبية (14) والمصادر الناقصة (40/40 بلا ## المصادر) باقية — خارج نطاق Task 5، تنتظر Task 6/8/10.

## الملفات
content/ar/branches/br-aba-autism.md
content/ar/branches/br-abft.md
content/ar/branches/br-abstinence-vs-harm-reduction.md
content/ar/branches/br-adlerian.md
content/ar/branches/br-advaita-vedanta-classical.md
content/ar/branches/br-advanced-aba-prt-vb.md
content/ar/branches/br-aedp-applied.md
content/ar/branches/br-affective-neuroscience-informed.md
content/ar/branches/br-african-centered-psychology.md
content/ar/branches/br-aggression-treatment.md
content/ar/branches/br-ai-chatbot-therapy.md
content/ar/branches/br-alchemical-psychology.md
content/ar/branches/br-american-transcendentalism.md
content/ar/branches/br-antipsychiatry.md
content/ar/branches/br-archetypal.md
content/ar/branches/br-aristotelianism-early-peripatetic.md
content/ar/branches/br-aristotelianism-late-hellenistic.md
content/ar/branches/br-asharism-early.md
content/ar/branches/br-asharism-late-philosophical.md
content/ar/branches/br-attachment-theory.md
content/ar/branches/br-biodynamic-psychology.md
content/ar/branches/br-bioenergetic-analysis.md
content/ar/branches/br-bionian.md
content/ar/branches/br-bodynamic-analysis.md
content/ar/branches/br-bowen-systems.md
content/ar/branches/br-brief-strategic-therapy.md
content/ar/branches/br-british-empiricism-classical.md
content/ar/branches/br-british.md
content/ar/branches/br-budapest-berlin.md
content/ar/branches/br-buddhist-logic-pramana.md
content/ar/branches/br-cartesianism-orthodox.md
content/ar/branches/br-case-management.md
content/ar/branches/br-cb-sex-therapy.md
content/ar/branches/br-charvaka-lokayata-materialism.md
content/ar/branches/br-child-psychoanalysis.md
content/ar/branches/br-christian-patristics-greek.md
content/ar/branches/br-christian-patristics-latin.md
content/ar/branches/br-classical-behaviorism.md
content/ar/branches/br-classical-marxism.md
content/ar/branches/br-classical-pragmatism.md
