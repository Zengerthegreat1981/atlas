# Task 5.8
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (relations/) | الملفات: 40

## الأرقام
مخالفات preflight: 6 → 0
belongs_to/connects نصية حرة عولجت: ~10
  - تحويل فعلي لـslug موجود: 3 — rel-mbct-cbt (سطرين: sch-mbct, sch-cbt)، rel-gestalt-existential (سطرين فارغين اتصلحوا لـsch-gestalt-therapy/sch-existentialism)، rel-humanistic-existential (سطر فارغ اتصلح لـsch-existentialism)
  - حُذف الرابط (فئة عامة/بلا مدرسة حقيقية): 3 — rel-integrative-cbt-common-factors, rel-integrative-humanistic-common-factors, rel-integrative-psychoanalysis-common-factors ("التكاملية/الانتقائية" ليست حركة تكامل العلاج النفسي — sch-eclecticism موجود لكنه عن الانتقائية الهلنستية القديمة، لا علاقة)
  - تسجيل مدرسة حقيقية بلا ملف: 4 — الطب النفسي المضاد، اضطرابات التفكك وتبدد الشخصية، حركة تكامل العلاج النفسي، البنائية الاجتماعية (Gergen)
إصلاح ملفات معطوبة (target/title فارغة تماماً — سقّالة مكسورة): rel-narrative-constructionist.md، rel-neuropsychoanalysis.md، rel-ipmb-evidence-based.md، rel-mbt-mentalization.md، rel-humanistic-existential.md
**اكتشاف خلط هوية:** rel-narrative-constructionist.md كان مربوطاً بـ`sch-social-contract` (فلسفة سياسية/العقد الاجتماعي) بينما المقصود فعلياً "البنائية الاجتماعية" (Social Constructionism/Gergen) — مفهوم مختلف تماماً بالاسم متشابه فقط. حُذف الرابط الخاطئ وسُجّلت المدرسة الصحيحة في missing-schools.md.
تصحيحات عناوين related متضاربة: ~10 حالات (Beck، Fanon، Mesmer، إلخ)

## أمر التحقق
`python3 scripts/task.py verify minimax 5.8` → قائمة سوداء متبقية: 30 (خارج نطاق Task 5) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك)
`python3 scripts/build_slug_index.py` → 6807 عنصر، 332 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- **rel-narrative-constructionist.md:** خلط هوية بين `sch-social-contract` (فلسفة سياسية) و"البنائية الاجتماعية" (نظرية جيرجن النفسية) — اسمان متشابهان لفظياً بالعربي بس مختلفان تماماً في المعنى. حذفت الرابط الخاطئ، سجّلت المدرسة الصحيحة الناقصة في missing-schools.md.
- **rel-integrative-*-common-factors.md (3 ملفات):** "التكاملية/الانتقائية" ليست حركة تكامل العلاج النفسي المعاصرة (Psychotherapy Integration/Common Factors) — الملف الوحيد المتاح `sch-eclecticism` عن الانتقائية الهلنستية-الرومانية القديمة، لا علاقة. حذفت belongs_to من الثلاثة، أبقيت relates_to الصحيحة، سجّلت المدرسة الحقيقية في missing-schools.md بعدد أعضاء 3.
- 3 ملفات كانت معطوبة بشكل كبير (crumb مكسور، en=ar، target/title فارغة تماماً): rel-ipmb-evidence-based.md، rel-mbt-mentalization.md — هذي أعطال أعمق من نطاق Task 5 (تحويل نص حر)، صححت بس الـedges/related اللي قدرت أوثّقها بثقة، وسيبت باقي الأعطال (title/en/crumb) لتاسك تنظيف تاني.
- rel-hume-bundle-self-dissociation.md: `sch-dissociative` slug شكله سليم لكن الملف مش موجود فعلاً — سُجّل في missing-schools.md بدل الحذف لأنه مش نص حر حرفياً.

## متوقف عنده (لرئيس التحرير)
- **ملفات معطوبة تحتاج تاسك منفصل:** rel-ipmb-evidence-based.md وrel-mbt-mentalization.md (title/en/crumb فارغة أو مكررة، أعمق من Task 5).
- خلط هوية rel-narrative-constructionist.md مسجل هنا — يستحق فحص هل نفس الخطأ (`sch-social-contract` بدل social constructionism) موجود في ملفات تانية.
- الجمل القالبية (30) وغياب `## المصادر` (40/40) خارج نطاق Task 5.
- 332 تعارض slug قديمة، لم تُلمس.

## الملفات
content/ar/relations/rel-foucault-madness-anti-stigma-campaigns.md
content/ar/relations/rel-foucault-narrative-therapy-externalization.md
content/ar/relations/rel-frankfurt-school-critical-psychiatry.md
content/ar/relations/rel-frankl-will-to-meaning-logotherapy-resilience.md
content/ar/relations/rel-gestalt-existential.md
content/ar/relations/rel-gilligan-care-ethics-relational-therapy.md
content/ar/relations/rel-habermas-ideal-speech-family-therapy.md
content/ar/relations/rel-hegel-alienation-false-self-winnicott.md
content/ar/relations/rel-hegelianism-psychoanalysis.md
content/ar/relations/rel-heidegger-authenticity-existential-guilt.md
content/ar/relations/rel-heraclitus-dialectical-behavior-therapy.md
content/ar/relations/rel-humanistic-existential-gestalt.md
content/ar/relations/rel-humanistic-existential.md
content/ar/relations/rel-humanistic-positive.md
content/ar/relations/rel-humanistic.md
content/ar/relations/rel-hume-bundle-self-dissociation.md
content/ar/relations/rel-husserl-bracketing-phenomenological-interview.md
content/ar/relations/rel-husserlian-phenomenology-gestalt-therapy.md
content/ar/relations/rel-hypnosis-psychoanalysis.md
content/ar/relations/rel-integrative-cbt-common-factors.md
content/ar/relations/rel-integrative-humanistic-common-factors.md
content/ar/relations/rel-integrative-psychoanalysis-common-factors.md
content/ar/relations/rel-ipmb-evidence-based.md
content/ar/relations/rel-james-stream-of-thought-free-association.md
content/ar/relations/rel-kant-apperception-central-executive.md
content/ar/relations/rel-kant-cognitive-schemas.md
content/ar/relations/rel-kantian-epistemology-cbt-schemas.md
content/ar/relations/rel-kierkegaard-angst-generalized-anxiety.md
content/ar/relations/rel-kierkegaardianism-nietzscheanism-existential-therapy.md
content/ar/relations/rel-levinas-ethics-of-other-therapeutic-alliance.md
content/ar/relations/rel-locke-association-of-ideas-conditioning.md
content/ar/relations/rel-marxism-critical-psychology.md
content/ar/relations/rel-marxist-alienation-occupational-burnout.md
content/ar/relations/rel-mbct-cbt.md
content/ar/relations/rel-mbt-mentalization.md
content/ar/relations/rel-merleau-ponty-body-schema-body-dysmorphia.md
content/ar/relations/rel-merleau-ponty-embodiment-somatic-experiencing.md
content/ar/relations/rel-narrative-constructionist.md
content/ar/relations/rel-neuropsychoanalysis.md
content/ar/relations/rel-nietzsche-sublimation-freudian-defense.md
