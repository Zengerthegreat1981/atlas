# Task 5.6
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة | الملفات: 40

## الأرقام
مخالفات preflight: 14 → 0
belongs_to/developed_by نصية حرة عولجت: ~12
  - تحويل فعلي لـslug مدرسة موجودة: 4 — br-ubuntu-psychology→sch-ubuntu, br-tibetan-gelug→sch-gelug, br-tibetan-nyingma-dzogchen→sch-nyingma, rel-act-cbt-third-wave (سطرين: sch-act, sch-cognitive-behavioral)
  - developed_by/فصل أسماء مركّبة: 1 (br-spinelli-phenomenological→thk-spinelli)
  - حُذف الرابط (فئة عامة/بلا مدرسة حقيقية مطابقة): 5 — br-sex-therapy, br-single-session-therapy, br-theraplay + تسجيل مدارس غائبة حقيقية بلا ملف: br-sotp, br-teletherapy, br-therapeutic-risk-assessment, br-ultra-brief-psychotherapy, br-vr-therapy (edges حُذفت من الملفات، المدرسة مسجلة في missing-schools.md)
  - تصحيح تصنيف خاطئ (خطأ عملية سابقة): rel-addiction-cbt "الإدمان وتغيير السلوك" حُذف (فئة عامة/crumb، مش مدرسة)
missing-schools.md: تم توحيد الإدخالات المكررة (كانت 3 وكيلين سجّلوا "علم النفس الشرعي/الجنائي" و"التكنولوجيا والعلاج الرقمي" بسطور منفصلة) → دُمجت في 6 أسطر فريدة بعدد أعضاء دقيق.

## أمر التحقق
`python3 scripts/task.py verify minimax 5.6` → قائمة سوداء متبقية: 19 (خارج نطاق Task 5) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك)
`python3 scripts/build_slug_index.py` → 6788 عنصر، 299 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- وحّدت missing-schools.md: 3 وكلاء مختلفين سجّلوا نفس المدرستين ("علم النفس الشرعي/الجنائي" و"التكنولوجيا والعلاج الرقمي") بسطور مكررة منفصلة من ملفات مختلفة — دمجتها في سطر واحد لكل مدرسة بقائمة كل الملفات وعدد أعضاء صحيح.
- 5 ملفات (br-sotp, br-teletherapy, br-therapeutic-risk-assessment, br-ultra-brief-psychotherapy, br-vr-therapy) كان فيها belongs_to نصي حر لمدارس حقيقية مسجلة في missing-schools.md لكن preflight رفض بقاء النص الحر في الملف نفسه — حذفت سطر edges من كل ملف (المدرسة تفضل مسجلة في البنك لـTask 13).
- br-transactional-analysis.md: صححت خلط سهو في `related` — id `thk-gunnel-cederblad` كان مربوطاً بعنوان "جونيل سيدِربلاد" بينما عنوان الملف الفعلي "ماريان سيدِربلاد"؛ وid `thk-jacqueline-astington` كان "جاكلين أستنغتون" والفعلي "جانيت وايلد أستنغتون".
- br-ubuntu-psychology.md: صححت id `thk-bdanner` من عنوان "بيرنارد دانِفَر" إلى العنوان الفعلي "ديبورا دانر" — تضارب جنس واسم كامل، يستحق تنبيهاً.
- rel-advaita-vedanta-transpersonal.md وrel-advaita-vedanta-transpersonal-psychology.md: **ملاحظة ازدواج محتمل** — نفس الموضوع (أدفايتا فيدانتا وعلم النفس عبر الشخصي، نفس الشخصيات ويلبر/غروف/ماسلو) لكن المحتوى غير متطابق حرفياً؛ النسخة `-transpersonal.md` أعمق وموثقة أكتر، والتانية فيها جمل من القائمة السوداء. **لم أدمج ولا أعد تسمية** (برا صلاحيات هذا التاسك) — محتاج قرار كلود.

## متوقف عنده (لرئيس التحرير)
- **ازدواج محتمل:** rel-advaita-vedanta-transpersonal.md ↔ rel-advaita-vedanta-transpersonal-psychology.md — يستحق مراجعة ودمج محتمل (Task مستقبلي، مش Task 5).
- الجمل القالبية (19) وغياب `## المصادر` (40/40) خارج نطاق Task 5.
- 299 تعارض slug قديمة، لم تُلمس.
- 6 subagents فشلوا أول مرة بسبب session limit وأُعيد تشغيلهم بنجاح — كل الـ40 ملف اتغطوا فعلياً.

## الملفات
content/ar/branches/br-sex-therapy.md
content/ar/branches/br-sikolohiyang-pilipino.md
content/ar/branches/br-single-session-therapy.md
content/ar/branches/br-social-constructionism.md
content/ar/branches/br-social-learning-theory.md
content/ar/branches/br-sotp.md
content/ar/branches/br-spinelli-phenomenological.md
content/ar/branches/br-spinozism-monism.md
content/ar/branches/br-sport-psychology.md
content/ar/branches/br-stoicism-early.md
content/ar/branches/br-stoicism-late-roman.md
content/ar/branches/br-stoicism-middle.md
content/ar/branches/br-structural-family.md
content/ar/branches/br-teacch.md
content/ar/branches/br-teletherapy.md
content/ar/branches/br-therapeutic-risk-assessment.md
content/ar/branches/br-theraplay.md
content/ar/branches/br-tiantai-lotus-philosophy.md
content/ar/branches/br-tibetan-gelug.md
content/ar/branches/br-tibetan-nyingma-dzogchen.md
content/ar/branches/br-transactional-analysis.md
content/ar/branches/br-transpersonal-psychology.md
content/ar/branches/br-ubuntu-psychology.md
content/ar/branches/br-ultra-brief-psychotherapy.md
content/ar/branches/br-vaisheshika-classical.md
content/ar/branches/br-vegetotherapy-orgonomy.md
content/ar/branches/br-vishishtadvaita-classical.md
content/ar/branches/br-vr-therapy.md
content/ar/branches/br-yoga-classical-raja.md
content/ar/branches/br-yogacara-classical.md
content/ar/branches/br-young-hegelians-left.md
content/ar/branches/br-zaidi-kalam-hadawi.md
content/ar/branches/br-zen-rinzai.md
content/ar/branches/br-zen-soto-classical.md
content/ar/relations/rel-act-cbt-third-wave.md
content/ar/relations/rel-act.md
content/ar/relations/rel-addiction-cbt.md
content/ar/relations/rel-adorno-authoritarian-personality-f-scale.md
content/ar/relations/rel-advaita-vedanta-transpersonal-psychology.md
content/ar/relations/rel-advaita-vedanta-transpersonal.md
