# Task 9.7
الحالة: مكتمل
المسار: minimax | العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط | الملفات: 30

## الأرقام
جمل القائمة السوداء: قبل ~15 ملفاً فيها بقايا/قوالب كاملة → بعد 0
YAML مكسور (frontmatter بلا `---` ختامي): 1 (con-cosmopolitanism-world-citizen) → أُصلح
edges بنص حر بدل slug/target صحيح: 1 (con-dasein-analysis: formulated_by كان اسماً حراً) → أُصلح لـthk-binswanger

## أمر التحقق
python3 scripts/task.py verify minimax 9.7
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 (المستهدف 0) | فيها ## المصادر: 0 / 30

## قرارات اتخذتها
- con-conversion-therapy-harm.md: حُذف thk-jnicolosi (غير مذكور)، أُضيف con-affirmative-therapy وbr-lgbtq-counseling.
- con-cosmopolitanism-world-citizen.md، con-cosmopolitanism.md: احتمال ازدواج مسجل في gaps الملفين. أُصلح YAML مكسور في الأول (frontmatter بلا `---` ختامي).
- con-counterpart-theory-lewis.md، con-creatio-ex-nihilo-theology.md: متنان قالبيان — أُعيدا كتابتهما (لويس/العوالم الممكنة، جدل الخلق من عدم).
- con-creative-block.md: لا تعديل جوهري بالروابط، حُذفت بقايا جملة سوداء من gaps.
- con-critical-liberation-therapy.md: صُحح slug مكسور (br-critical-liberation→br-critical-liberation-therapy).
- con-cross-cultural-meditation.md، con-cross-cultural-psychoanalysis.md: edges.belongs_to كان نصاً حراً/حلقة ذاتية — حُذف في كليهما.
- con-cultural-capital-bourdieu.md: متن بلا أي اسم مذكور ولا ملف thk-bourdieu فعلي — related تُرك فارغاً، edges.belongs_to نص حر حُذف.
- con-cultural-complex.md: أُبقي thk-singer، حُذف thk-samuels وthk-jhenderson (غير مذكورين).
- con-cultural-psychoanalysis.md: edges.belongs_to كان حلقة ذاتية — حُذف، أُعيد بناء related (فرويد، لاكان، يونغ، إريكسون، هورني).
- con-cultural-unconscious.md: صُحح عنوان thk-jung.
- con-culture-industry-adorno.md، con-cunning-of-reason-hegel.md: متنان قالبيان — أُعيدا كتابتهما (أدورنو/هوركهايمر، هيغل).
- con-cyborg.md: صُحح عنوان sch-posthumanism، أُضيف sch-transhumanism.
- con-dao-the-way-concept.md: متن عام حشو بالكامل — related تُرك فارغاً `[]`.
- con-dao.md: أُعيد بناء related (sch-daoism-philosophical، لاو تزو بعد تصحيح العنوان، تشوانغ تزو، برهمان، هايدغر)، حُذف con-wuwei (غير مذكور).
- con-das-man-the-they.md: متن شبه فارغ — related تُرك فارغاً، سُجّل مسار مستقبلي بـgaps.
- con-dasein-analysis.md: صُحح edges.formulated_by (كان اسماً حراً بدل slug)، أُضيف thk-heidegger وthk-husserl وthk-freud (مذكورون بالاسم).
- con-dasein-being-in-the-world.md: رابط واحد فقط (thk-heidegger) — بقية المتن حشو.
- con-dasein-being-there.md: صُحح عنوان thk-heidegger، أُضيف con-dasein-being-in-the-world.
- con-datsuzoku.md: edges.belongs_to نص حر — حُذف. حُذف thk-fukuzawa (غير مذكور)، أُضيف thk-nishida وcon-ataraxia.
- con-dbt-validation.md: أُضيف thk-rogers (مقارنة صريحة بالمتن).
- con-death-instinct.md: حُذف thk-jung (غير مذكور)، أُبقي thk-spielrein وthk-freud.
- con-death-of-god-nietzsche.md: متن قالبي بالكامل بلا ذكر نيتشه حتى — related تُرك فارغاً.
- con-death.md: أُعيد بناء related بثمانية روابط (هايدغر، يالوم، سارتر، فرانكل، بوس، تيليش، ياسبرز، sch-existential-therapy، con-meaning).
- con-decolonizing-pedagogy.md: أُضيف thk-pfreire وthk-imartinbaro (بعد تصحيح العنوان) وcon-conscientization-paulo-freire وcon-praxis.
- con-decolonizing-therapy.md: صُحح عنوان con-coloniality وthk-imartinbaro، أُضيف con-decolonizing-pedagogy.
- con-deconstruction-logocentrism.md: متن قالبي — أُعيد كتابته، رابط واحد فقط (sch-deconstruction)؛ لم يُضف thk-derrida لعدم ذكره بالمتن رغم كونه واضع المفهوم.

## متوقف عنده (لرئيس التحرير)
- con-cosmopolitanism-world-citizen.md وcon-cosmopolitanism.md: احتمال ازدواج — قرار دمج بشري.
- con-dao-the-way-concept.md وcon-dao.md: نفس الأمر.
- con-dasein-being-in-the-world.md وcon-dasein-being-there.md: نفس الأمر.
- con-das-man-the-they.md، con-death-of-god-nietzsche.md، con-cultural-capital-bourdieu.md: متون شبه فارغة من محتوى حقيقي — تحتاج تعميقاً فعلياً (Task 4/10) قبل إمكان بناء related كامل.
- con-cosmopolitanism-world-citizen.md: كان فيه YAML مكسور (frontmatter بلا `---` ختامي) — أُصلح، لكن يُنصح بفحص بقية الأطلس لملفات مشابهة بنفس الخلل.

## الملفات
content/ar/concepts/con-conversion-therapy-harm.md
content/ar/concepts/con-cosmopolitanism-world-citizen.md
content/ar/concepts/con-cosmopolitanism.md
content/ar/concepts/con-counterpart-theory-lewis.md
content/ar/concepts/con-creatio-ex-nihilo-theology.md
content/ar/concepts/con-creative-block.md
content/ar/concepts/con-critical-liberation-therapy.md
content/ar/concepts/con-cross-cultural-meditation.md
content/ar/concepts/con-cross-cultural-psychoanalysis.md
content/ar/concepts/con-cultural-capital-bourdieu.md
content/ar/concepts/con-cultural-complex.md
content/ar/concepts/con-cultural-psychoanalysis.md
content/ar/concepts/con-cultural-unconscious.md
content/ar/concepts/con-culture-industry-adorno.md
content/ar/concepts/con-cunning-of-reason-hegel.md
content/ar/concepts/con-cyborg.md
content/ar/concepts/con-dao-the-way-concept.md
content/ar/concepts/con-dao.md
content/ar/concepts/con-das-man-the-they.md
content/ar/concepts/con-dasein-analysis.md
content/ar/concepts/con-dasein-being-in-the-world.md
content/ar/concepts/con-dasein-being-there.md
content/ar/concepts/con-datsuzoku.md
content/ar/concepts/con-dbt-validation.md
content/ar/concepts/con-death-instinct.md
content/ar/concepts/con-death-of-god-nietzsche.md
content/ar/concepts/con-death.md
content/ar/concepts/con-decolonizing-pedagogy.md
content/ar/concepts/con-decolonizing-therapy.md
content/ar/concepts/con-deconstruction-logocentrism.md
