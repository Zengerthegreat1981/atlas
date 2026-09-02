# Task 5.16
الحالة: مكتمل جزئياً (مخالفة واحدة false-positive من عيب سكريبت، مش من المحتوى) | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/) | الملفات: 40

## الأرقام
مخالفات preflight الحقيقية: 0 (كل الوكلاء شغّلوا preflight_check.py بأنفسهم)
مخالفة preflight ظاهرة واحدة (false-positive): sch-positive-psychology.md — id "thk-groselli" title المكتوب "غيلي روزيليني" ضد "عنوان الملف الحقيقي" اللي طلعه السكريبت "غيل روزيليني". **السبب: تعارض slug حقيقي بين `content/ar/thinkers/thk-groselli.md` (المعتمد، title: "غيلي روزيليني") و`content/ar/drafts/spark/thinkers/thk-groselli.md` (مسودة Spark، title: "غيل روزيليني") — preflight_check.py بيلاقي نسخة drafts الأول بترتيب os.walk ويقارن بيها غلط.** الملف المستهدف الفعلي (content/ar المعتمد) عنوانه فعلاً "غيلي روزيليني" ومطابق تماماً لما كتبته في sch-positive-psychology.md — **المحتوى صحيح، السكريبت هو اللي بيشاور غلط.** لم ألمس ملف thk-groselli ولا السكريبت (خارج نطاقي، وthk-* من a-l ملك Spark).
belongs_to/evolved_from/founded_by/revived_by نصية حرة عولجت: ~18
  - تحويل فعلي لـslug موجود: 6
  - حُذف الرابط (فئة عامة/دائري/خطأ تصنيف): ~8
  - تسجيل مدارس/مظلات حقيقية بلا ملف: ~16 سطراً جديداً (أبرزها: 4 مدارس فلسفية للرياضيات فرعية بمؤسسين موثقين، 3 مدارس فلسفة العقل التحليلية، 4 مدارس فلسفة العلم، 4 تيارات علم النفس الإيجابي الفرعية، الفلسفة اليابانية المعاصرة)
تصحيحات هوية خطيرة (5 حالات في دفعة واحدة):
  - **sch-phil-science.md:** `thk-kuhn` هو فعلياً **رولاند كون** (طبيب نفسي سويسري) مش **توماس كون** (فيلسوف العلم) — حُذف الرابط الخاطئ، أُبقي `thk-pkuhn` الصحيح.
  - **sch-pessimism.md:** `thk-hartmann` هو **نيكولاي هارتمان** مش **إدوارد فون هارتمان** (صاحب "فلسفة اللاواعي" المذكور في المتن) — حُذف، وُثّق في gaps (يحتاج طلب slug جديد).
  - **sch-positive-psychology.md:** `thk-dsaleeby` كان بعنوان "دونالد سالييبي" لكن الملف الفعلي **دينس ساليبي (Dennis Saleeby)** — صُحح العنوان في related والمتن.
  - **sch-process-philosophy.md:** `thk-campbell-purton` رابط لشخص مختلف تماماً (موضوعه Focusing عند جنداين، لا علاقة بفلسفة العملية) — حُذف.
  - **sch-nyaya.md (ملاحظة، مش تصحيح):** احتمال خلط بين `thk-gotama-nyaya` و`thk-gotama-kanad` (مؤسسا نيايا وفايشيشيكا) — id/title متطابقان حالياً فمرّ من preflight، لكن يستحق مراجعة بشرية.
تصحيح كسر بنيوي: sch-psychedelic-assisted-therapy.md كانت founded_by/revived_by قوائم أسماء مدمجة في سطر واحد (صيغة مكسورة) — أُصلحت لـslugs مفردة صحيحة.

## أمر التحقق
`python3 scripts/task.py verify minimax 5.16` → قائمة سوداء متبقية: **0** · سقّالة ظاهرة: 0 · `## المصادر`: 0/40
`python3 scripts/build_slug_index.py` → 6901 عنصر، 438 تعارض pre-existing (منها thk-groselli المذكور أعلاه)

## قرارات اتخذتها
- **thk-groselli false-positive:** تحققت يدوياً بفتح الملفين — المحتوى صحيح، المشكلة في السكريبت (بيختار drafts/spark بدل content/ar المعتمد بسبب ترتيب os.walk). لم أعدّل، وثّقت هنا بدل الإبلاغ الخاطئ إن التاسك فشل.
- 5 حالات خلط هوية (thk-kuhn، thk-hartmann، thk-dsaleeby، thk-campbell-purton، واحتمال thk-gotama-nyaya) — أخطر من عناوين متضاربة عادية، وثّقتهم بالتفصيل.
- sch-personalism.md وsch-personalism-contemporary.md: راجعتهم فعلياً رغم إشارة MINIMAX.md لتطابق حرفي محتمل — **مش متطابقين**، محتوى مختلف فعلياً بفترتين زمنيتين مختلفتين (المبكرة حتى 1949 مقابل المعاصرة بعد 1937) — يستحق تنبيه Task 8 إن الادعاء الأصلي قديم/غير دقيق.

## متوقف عنده (لرئيس التحرير)
- **preflight_check.py bug:** يختار نسخة drafts/spark بدل content/ar المعتمد عند تعارض slug — يحتاج إصلاح في `resolve_path_for_slug` (تفضيل content/ar الأساسي) أو حذف تعارضات المسودات.
- **5 خلطات هوية مكتشفة** (تفاصيل فوق) — بعضها يحتاج طلب slug جديد (إدوارد فون هارتمان)، بعضها يحتاج مراجعة أوسع للأطلس.
- **sch-personalism / sch-personalism-contemporary:** ليسا مكررين فعلياً خلافاً لما ذكره MINIMAX.md — يستحق تحديث الإشارة في Task 8.
- 16 مدرسة/مظلة جديدة في missing-schools.md تنتظر Task 13.
- 438 تعارض slug قديمة (منها thk-groselli المفصّل أعلاه)، لم تُلمس معظمها.

## الملفات
content/ar/schools/sch-newconfucianism-modern.md
content/ar/schools/sch-nichiren.md
content/ar/schools/sch-nietzscheanism.md
content/ar/schools/sch-nongjia.md
content/ar/schools/sch-north-american-indigenous.md
content/ar/schools/sch-nyaya.md
content/ar/schools/sch-nyingma.md
content/ar/schools/sch-occasionalism.md
content/ar/schools/sch-ockhamism.md
content/ar/schools/sch-ooo.md
content/ar/schools/sch-ordinary-language.md
content/ar/schools/sch-pan-africanism.md
content/ar/schools/sch-pancasila.md
content/ar/schools/sch-patristics.md
content/ar/schools/sch-personalism-contemporary.md
content/ar/schools/sch-personalism.md
content/ar/schools/sch-pessimism.md
content/ar/schools/sch-phenomenology-existential.md
content/ar/schools/sch-phenomenology-hermeneutic.md
content/ar/schools/sch-phenomenology-somatic.md
content/ar/schools/sch-phenomenology.md
content/ar/schools/sch-phil-mathematics.md
content/ar/schools/sch-phil-mind-analytic.md
content/ar/schools/sch-phil-science.md
content/ar/schools/sch-philosophy-of-disability.md
content/ar/schools/sch-philosophy-of-technology.md
content/ar/schools/sch-political-islam.md
content/ar/schools/sch-polyvagal-informed-therapy.md
content/ar/schools/sch-positive-psychology.md
content/ar/schools/sch-positivism-latin.md
content/ar/schools/sch-post-kyoto.md
content/ar/schools/sch-post-structuralism.md
content/ar/schools/sch-postcolonial-philosophy.md
content/ar/schools/sch-posthumanism.md
content/ar/schools/sch-postmodernism-philosophical.md
content/ar/schools/sch-pragmatism-classical.md
content/ar/schools/sch-process-philosophy.md
content/ar/schools/sch-psychedelic-assisted-therapy.md
content/ar/schools/sch-psychoanalysis.md
content/ar/schools/sch-pure-land.md
