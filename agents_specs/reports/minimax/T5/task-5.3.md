# Task 5.3
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة | الملفات: 40

## الأرقام
مخالفات preflight: 3 → 0
belongs_to/developed_by/influenced_by/adjacent_to نصية حرة عولجت: 12
  - تحويل فعلي لـslug مدرسة/br موجودة: 5 — br-haskalah-jewish-enlightenment→sch-haskalah, br-islamic-positive-psychology→sch-positive-psychology, br-intersectional-feminist→sch-intersectionality, br-irfan-nazari-akbari→sch-akbari, br-kabbalah-lurianic-theosophy→sch-kabbalah-lurianic
  - developed_by/influenced_by محوّلة لـthk-slug: 6 — thk-fairbairn (br-independents)، thk-hdavanloo (br-istdp-core-techniques)، thk-jung (br-jungian)، thk-heidegger-equivalent (br-humanistic→br-daseins لـinfluenced_by)، thk-may+thk-bugental+thk-yalom (br-humanistic، فُصّل من سطر واحد بثلاث أسماء لثلاث علاقات منفصلة)
  - إصلاح slug خاطئ (typo/تطابق ناقص، مش نص حر لكنه غير موجود): 1 — br-ifs-clinical-applications: sch-internal-family-systems → sch-ifs
تصحيحات عناوين related متضاربة: ~15 حالة، أهمها اكتشاف **خلط هوية** في br-kleinian.md — id `thk-zsegal` (وهو فعلياً Zindel Segal، باحث CBT/mindfulness مختلف تماماً) كان مربوطاً بعنوان "حنا سيغال" المحللة النفسية الكلاينية؛ صُحح إلى id الصحيح `thk-segal`.

## أمر التحقق
`python3 scripts/task.py verify minimax 5.3` → قائمة سوداء متبقية: 21 (خارج نطاق Task 5) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك)
`python3 scripts/build_slug_index.py` → 6777 عنصر، 297 تعارض pre-existing (لم ألمسها، خارج نطاقي)

## قرارات اتخذتها
- br-kleinian.md: preflight ما كانش هيكشف خطأ الهوية (thk-zsegal له عنوان صحيح "حنا سيغال" مكتوب في نفس السياق، والتضارب مش في تطابق id/title بل في هوية الشخص الحقيقي وراء الـid) — الوكيل لقاها يدوياً بمراجعة محتوى ملف thk-zsegal.md ولقاه شخص تاني (Zindel Segal). ده أخطر من تضارب عنوان عادي، سجّلته هنا صراحة.
- br-humanistic.md: developed_by كان فيه اسم مركّب "ماي وبوجنتال ويالوم" لثلاثة أشخاص في target واحد — الوكيل الأصلي سابها عمداً لأنها خارج تعليماته (اسم واحد بس)، أنا فصلتها لثلاث سطور developed_by منفصلة بعد التحقق من وجود الثلاثة (thk-may, thk-bugental, thk-yalom).
- br-ifs-clinical-applications.md: `sch-internal-family-systems` كان slug شكله سليم لكنه مش موجود فعلياً — الملف الصحيح `sch-ifs`. اتصحح.
- باقي الملفات (~28): كانت بالفعل slugs صحيحة من مراحل سابقة (Phase 0)، اتفحصت وتأكد بس من صحتها بلا تعديل.

## متوقف عنده (لرئيس التحرير)
- الجمل القالبية (21) وغياب `## المصادر` (40/40) خارج نطاق Task 5.
- 297 تعارض slug في build_slug_index.py قديمة من قبل هذه الدفعة.
- **يستحق مراجعة بشرية إضافية:** br-kleinian.md — تأكد إن thk-zsegal فعلاً مش مستخدم غلط في ملفات تانية غير دي (ما فحصتش الأطلس كله بحثاً عن استخدامات تانية لنفس الـid الخاطئ).

## الملفات
content/ar/branches/br-german-idealism-schellingian.md
content/ar/branches/br-gestalt-berlin.md
content/ar/branches/br-gestalt-theoretical-psychotherapy.md
content/ar/branches/br-gestalt-therapy.md
content/ar/branches/br-glasser-reality-therapy.md
content/ar/branches/br-group-psychoanalysis.md
content/ar/branches/br-haskalah-jewish-enlightenment.md
content/ar/branches/br-hikmat-mutaaliya-isfahan.md
content/ar/branches/br-hikmat-mutaaliya-qom-contemporary.md
content/ar/branches/br-huayan-interpenetration.md
content/ar/branches/br-hullian-behaviorism.md
content/ar/branches/br-humanistic.md
content/ar/branches/br-ibadi-kalam-rustamid-oman.md
content/ar/branches/br-ibp.md
content/ar/branches/br-ifs-clinical-applications.md
content/ar/branches/br-ifs-protocol.md
content/ar/branches/br-imami-theology-hilla-philosophical.md
content/ar/branches/br-imami-theology-qom-baghdad.md
content/ar/branches/br-independents.md
content/ar/branches/br-integrative-psychoanalysis.md
content/ar/branches/br-interpersonal-neurobiology.md
content/ar/branches/br-intersectional-feminist.md
content/ar/branches/br-intersubjective-psychoanalysis.md
content/ar/branches/br-irfan-nazari-akbari.md
content/ar/branches/br-irfan-shuhudi-sirhindi.md
content/ar/branches/br-ishraq-classical.md
content/ar/branches/br-ishraq-commentators.md
content/ar/branches/br-islamic-positive-psychology.md
content/ar/branches/br-istdp-core-techniques.md
content/ar/branches/br-jainism-digambara-philosophy.md
content/ar/branches/br-jainism-shvetambara-philosophy.md
content/ar/branches/br-jewish-philosophy-rationalist-averroist.md
content/ar/branches/br-jungian.md
content/ar/branches/br-kabbalah-lurianic-theosophy.md
content/ar/branches/br-kleinian.md
content/ar/branches/br-korean-silhak-practical.md
content/ar/branches/br-kyoto-school-first-generation.md
content/ar/branches/br-lacanian.md
content/ar/branches/br-legalism-fajia-qin.md
content/ar/branches/br-leibnizian-wolffian-enlightenment.md
