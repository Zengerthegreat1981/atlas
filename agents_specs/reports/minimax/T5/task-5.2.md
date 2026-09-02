# Task 5.2
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة | الملفات: 40

## الأرقام
مخالفات preflight: 5 (بعد شغل الوكلاء) → 0 (بعد تصحيحي اليدوي)
belongs_to/developed_by نصية حرة عولجت: 15
  - تحويل فعلي لـslug مدرسة موجودة: 2 (br-critical-liberation-therapy → sch-liberation-psychology, br-fft → sch-systemic-family)
  - developed_by/influenced_by محوّلة لـthk-slug: 5 (thk-rwachtel، thk-lstevenhayes، thk-binswanger+thk-boss، thk-heidegger)
  - حُذف الرابط (فئة عامة/بلا مدرسة حقيقية مطابقة): 8 — br-conversion-therapy, br-digital-therapeutics, br-discernment-counseling, br-curanderismo, br-ddp, br-dynamic-couples-family-therapy, br-embodied-cognition-therapy, br-expressive-arts-therapy (جزئي), br-family-sandplay, br-clinical-hypnotherapy (سطرين)
  - سُجّل في missing-schools.md: 0 إضافات جديدة صافية في هذه الدفعة (حالة hypnotherapy اتسجلت من دفعة سابقة عبر وكيل واحد بس اتحذفت لاحقاً من الملف نفسه لعدم وجود ملف مدرسة)
تصحيحات عناوين related متضاربة (preflight §4): ~25 حالة عبر الدفعة (أسماء منقولة بشكل مختلف، ألقاب ناقصة)

## أمر التحقق
`python3 scripts/task.py verify minimax 5.2` → قائمة سوداء متبقية: 12 (خارج نطاق Task 5) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك)
`python3 scripts/build_slug_index.py` → 6760 عنصر، 265 تعارض pre-existing غير متعلق بهذه الدفعة (لم ألمسها)

## قرارات اتخذتها
- br-critical-liberation-therapy.md: "العدالة والمجتمع" ↔ تطابق حقيقي موثّق (Martín-Baró، Freire، Fanon) → sch-liberation-psychology.
- br-fft.md: "علاج الأطفال والوالدين" ↔ FFT هو علاج أسري نسقي فعلياً → sch-systemic-family.
- br-clinical-hypnotherapy.md: وكيل واحد سجّل "التنويم والهيبنوثيرابي" كمدرسة غائبة في missing-schools.md، لكن بعد المراجعة (preflight) قررت حذف الرابطين (belongs_to وevolved_into) من الملف نفسه لعدم وجود ملف مدرسة أو تيار Ericksonian مطابق فعلياً في الأطلس — السطر في missing-schools.md سيبته موجوداً لـTask 13 (المدرسة حقيقية، بس الملف الحالي ما ينفعش يفضل بنص حر).
- br-daseins.md: "هايدجر" → thk-heidegger (تحققت من وجود الملف)؛ "بينسوانغر وبوس" (من وكيل سابق) فُصلت لـthk-binswanger + thk-boss.
- br-embodied-cognition-therapy.md: gaps كانت فيها "لا تاريخ نهاية موثّق" رغم active_end="مستمر" موجود فعلاً → حذفت السطر (مخالفة تأكيد حقيقة بدل فجوة).
- br-critical-psychoanalysis.md: صححت عنوان thk-jbenjamin ليطابق التشكيل الفعلي "جيسيكا بِنْجامِين".
- باقي الحذوفات (8 ملفات): كل الأسماء الحرة طابقت نص الـcrumb حرفياً بلا مؤسس/منهج مستقل (فئات تصنيف عامة زي "مدارس نادرة/متفرقة"، "أطر غير غربية"، "العلاج الجماعي/التعبيري/الفني") — مش مدارس حقيقية، فاتحذف الرابط بدل تسجيلها.

## متوقف عنده (لرئيس التحرير)
- الجمل القالبية (12) وغياب `## المصادر` (40/40) خارج نطاق Task 5، تنتظر Task 6/8/10.
- 265 تعارض slug في build_slug_index.py قديمة من قبل هذه الدفعة، بلغتك بس ماعدلتهاش (خارج نطاقي).

## الملفات
content/ar/branches/br-classical-psychoanalysis.md
content/ar/branches/br-classical-utilitarianism-bentham-mill.md
content/ar/branches/br-clinical-hypnotherapy.md
content/ar/branches/br-confucianism-early-pre-qin.md
content/ar/branches/br-constructivist-cognitive.md
content/ar/branches/br-control-mastery.md
content/ar/branches/br-conversion-therapy.md
content/ar/branches/br-critical-liberation-therapy.md
content/ar/branches/br-critical-psychoanalysis.md
content/ar/branches/br-curanderismo.md
content/ar/branches/br-cyclical-psychodynamics.md
content/ar/branches/br-daoism-classical-lao-zhuang.md
content/ar/branches/br-daoism-xuanxue-neo-daoism.md
content/ar/branches/br-daseins.md
content/ar/branches/br-ddp.md
content/ar/branches/br-decolonizing-therapy.md
content/ar/branches/br-digital-therapeutics.md
content/ar/branches/br-discernment-counseling.md
content/ar/branches/br-discursive-psychology.md
content/ar/branches/br-dvaita-vedanta-classical.md
content/ar/branches/br-dynamic-couples-family-therapy.md
content/ar/branches/br-ego-psychology.md
content/ar/branches/br-embodied-cognition-therapy.md
content/ar/branches/br-embodied-relational-therapy.md
content/ar/branches/br-emdr-protocol.md
content/ar/branches/br-epicureanism-garden.md
content/ar/branches/br-epicureanism-roman.md
content/ar/branches/br-existential-humanistic-american.md
content/ar/branches/br-expressive-arts-therapy.md
content/ar/branches/br-falsafa-mashshaiyya-eastern.md
content/ar/branches/br-falsafa-mashshaiyya-western-andalusian.md
content/ar/branches/br-family-sandplay.md
content/ar/branches/br-feminist-therapy.md
content/ar/branches/br-fft.md
content/ar/branches/br-french-enlightenment-encyclopedists.md
content/ar/branches/br-french-psychoanalysis.md
content/ar/branches/br-functional-contextualism-rft.md
content/ar/branches/br-general-systems-cybernetics.md
content/ar/branches/br-german-idealism-fichtean.md
content/ar/branches/br-german-idealism-hegelian.md
