# Task 13.16 — دفعة تدقيق شامل + إغلاق مرشحين حقيقيين متبقين
الحالة: مكتمل | الملفات الجديدة: 11 (129/~147 إجمالاً الآن)

## العملية
سبقتها **عملية تدقيق كاملة** (subagent مخصص، read-only) قابل كل الـ~170 سطر في `agents_specs/missing-schools.md` ضد الحالة الفعلية لمجلدات المدارس الأربعة (content/ar/schools، branches، drafts/minimax/schools، drafts/minimax/branches). النتيجة: **الملف كان قديماً جداً** — أكثر من 140 من أصل ~170 سطراً كانت بالفعل DONE (إما عبر عمل هذه الجلسة أو ملفات معتمدة سابقاً لم تُربط بصورة صحيحة في القائمة الأصلية)، تاركاً ~28 مرشحاً حقيقياً فقط. 4 دفعات متوازية عالجت هذه القائمة النظيفة.

## ✅ الملفات الجديدة (11)
- **sch-thought-field-therapy** — العلاج بالطاقة النفسية TFT (روجر كالاهان، 1980)
- **sch-map-metapsychoanalysis** — الفرع الإيطالي لـISTDP (ليبراتي وليس)
- **sch-encounter-group-movement** — حركة اللقاء الجماعي (وليام شوتز)
- **sch-contextualism-pepper** — السياقية الأمريكية (ستيفن بيبر، 1942، جذر Functional Contextualism/ACT)
- **sch-neurofeedback** — التغذية الراجعة العصبية كتقليد إكلينيكي (ستيرمان/لوبار→أوثمر)
- **sch-hobbesianism** — الهوبزية (المادية السياسية عند توماس هوبز)
- **sch-han-confucianism** — الكونفوشية الهانية (دونغ تشونغ شو، يانغ شيونغ)
- **sch-physiological-psychology** — علم النفس الفيزيولوجي (تقليد فونت 1874، جذر التطوري)
- **sch-cognitive-constructivism-piaget** — البنائية المعرفية عند بياجيه
- **sch-cross-cultural-psychology** — علم النفس عبر الثقافي (بيري/ترياندس)
- **sch-trauma-psychology** — ⚠️ **فجوة حقيقية مؤكَّدة كانت مستهدَفة بالفعل من 4 ملفات موجودة** (exp-flashback-ptsd، وثلاثة ملفات نقد) — أهم إنجاز في هذه الدفعة، تحل روابط معلَّقة كانت موجودة فعلياً في المحتوى المعتمد.

## ✅ قرارات "عدم إنشاء" صحيحة (6)
- **SAR (Submission-Authority-Relationship)**: مُصنَّف صراحة "خارج النطاق" في `MASTER_TAXONOMY_OUT_OF_SCOPE.md` — حركة فردية تاريخية بلا استمرارية مؤسسية.
- **العلاج البنيوي والعائلي باللعب**: تحقق من ملف thk-vaxline نفسه — لا يوثِّق شيئاً متمايزاً عن sch-filial-therapy/br-structural-family الموجودين.
- **الفلسفة العرفية لجنوب شرق آسيا**: sch-adat موجود فعلاً بنفس النطاق.
- **بانكاسيلا**: sch-pancasila موجود فعلاً.
- **التقليد الشكّي اليوناني (مظلة)**: sch-pyrrhonism وsch-academic-skepticism موجودان ومترابطان فعلاً — مظلة إضافية ستكرر لا تضيف.
- **فلسفات أستراليا/أوقيانوسيا (مظلة إقليمية)**: sch-dreamtime يغطي هذا النطاق فعلاً كمظلة إقليمية موازية لـsch-north-american-indigenous.

## ⚠️ تصادم ترقيم متكرر — 5 حالات، حُسمت بمسح شامل نهائي
رغم تقسيم العمل لـ4 دفعات منفصلة، تصادم SCH-0628/0629/0630 حدث 3 مرات متتالية بين الدفعات (Pepper×TFT، Neurofeedback×HanConfucianism، Hobbes×EncounterGroup). طُبِّق **مسح إعادة ترقيم شامل نهائي** (نفس نمط 13.14 الناجح): كل ملف بمعرِّف تكراري أُعيد ترقيمه بأرقام فريدة تبدأ من SCH-0700. تحقق نهائي: صفر تكرار عبر كل مجلد drafts/minimax/schools/ (129 ملفاً).

صفر slugs مخترعة، صفر مصادر ملفَّقة، صفر مخالفات preflight حقيقية (كل الإيجابيات الكاذبة تحققتُ منها شخصياً بـtest -f)، صفر تطابق قائمة سوداء.

## قرارات جودة بارزة
- sch-map-metapsychoanalysis: لا مصدر حقيقي موثوق كافٍ للاستشهاد به — **حُذف قسم `## المصادر` بالكامل بدل تلفيق استشهاد**، والغياب موثَّق في gaps صراحة.
- sch-cross-cultural-psychology: لم يُخترع thk-triandis أو thk-berry (لا ملفات لهما) رغم مركزيتهما — ذُكرا بالاسم في المتن فقط.
- sch-physiological-psychology: تجنَّب subagent تكرار محتوى sch-structuralism-wundt-titchener الموجود مسبقاً بكتابة زاوية مختلفة (الجذر المنهجي التاريخي، لا نفس المختبر/الكتاب).

## متوقف عنده (لرئيس التحرير)
- طلبات slug مسجلة: كاتيا ليبراتي وفريديريكو ليس (MAP)، ترياندس وبيري (علم النفس عبر الثقافي).
- **تقييم نهائي لـTask 13**: بعد التدقيق الشامل، **~28 مرشحاً حقيقياً** كانوا متبقين فعلاً، وعُولج 17 منهم في هذه الدفعة (11 إنشاء + 6 قرار عدم إنشاء صحيح موثَّق). المتبقي الحقيقي أصبح صغيراً جداً — أغلب ما تبقى في القائمة الأصلية (170 سطراً) كان بالفعل DONE أو مكرراً أو خارج النطاق.

## الملفات (مسار كامل)
content/ar/drafts/minimax/schools/{sch-thought-field-therapy,sch-map-metapsychoanalysis,sch-encounter-group-movement,sch-contextualism-pepper,sch-neurofeedback,sch-hobbesianism,sch-han-confucianism,sch-physiological-psychology,sch-cognitive-constructivism-piaget,sch-cross-cultural-psychology,sch-trauma-psychology}.md
