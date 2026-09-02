# Task 9.18
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط (10 subagents متوازية) | الملفات: 60

## الأرقام
جمل القائمة السوداء: بعد 0
سقّالة ظاهرة: بعد 0

## أمر التحقق
`python3 scripts/task.py verify minimax 9.18` → جمل قائمة سوداء: 0، سقّالة: 0
`python3 scripts/preflight_check.py <60 ملفاً>` → صفر مخالفات

## قرارات اتخذتها
- **أكبر عدد ازدواجات مكتشفة في دفعة واحدة لحد الآن (9 أزواج)، كلها سُجّلت بلا دمج:**
  - con-narrative-identity.md ⟷ con-narrative-identity-ricoeur.md
  - con-natural-law.md ⟷ con-natural-law-aquinas-concept.md
  - con-neuroception-polyvagal.md ⟷ con-neuroception-safety-detection.md
  - con-neuroplasticity.md ⟷ con-neuroplasticity-trauma.md (تحقق فعلي: **ليس ازدواجاً حقيقياً**، تخصص إكلينيكي ضيق داخل مدرسة مختلفة)
  - con-occasionalism-ashari.md ⟷ con-occasionalism-kalam-atomic.md (تحقق فعلي: **ليس ازدواجاً**، نظرية الكسب مقابل تجدد خلق الأعراض)
  - con-kasb-acquisition-ashari.md ⟷ con-occasionalism-ashari.md (ازدواج حقيقي مكتشف أثناء التحقق، خارج نطاق التكليف الأصلي)
  - con-overlapping-consensus-rawls.md ⟷ con-political-liberalism.md
  - con-panopticon-surveillance.md ⟷ con-panopticism-surveillance-society.md
  - con-ockhams-razor.md ⟷ con-ockhams-razor-parsimony.md
- **طلبات slug جديدة مسجَّلة في requests-minimax.md:** R-009 (thk-isaiah-berlin، لا يخلط مع thk-fberlin/Fred Berlin)، thk-rboyd، thk-ncartwright، thk-wang-chongyang، thk-judy-singer، thk-harvey-blume، Oluwole/Gbadegesin/Bewaji (فلاسفة الأومولوابي)، thk-wonhyo (فيلسوف بوذي كوري مهم بلا ملف).
- استخدام `thk-thomas-kuhn` (الـslug المعتمد نهائياً حسب R-002) بدل `thk-pkuhn` المُحال في con-paradigm-shift-kuhn.md، تطبيقاً لقرار سابق موثّق.
- الـsubagents صحّحوا مخالفات preflight قديمة كثيفة: عناوين related غير مطابقة (10+، منها thk-lacan، thk-jung مرتين، thk-suhrawardi)، edges بنص حر بدل slug (8+، منها sch-deep-ecology، sch-ethnophilosophy، sch-humanistic، sch-popular-psychology ×2).
- con-neuroception-safety-detection.md وصل لسقف 10 روابط نظراً لثراء المادة الموثقة.

## متوقف عنده (لرئيس التحرير)
- 9 أزواج ازدواج محتملة (منها 7 حقيقية مؤكدة و2 مؤكد أنهما ليسا ازدواجاً) تستاهل قرار دمج/فصل تحريري — المجموع التراكمي من كل دفعات Task 9 لحد الآن: 18 زوجاً.
- 8 طلبات slug جديدة (أعلاه).

## الملفات
60 ملف — نطاق con-nafs-natiqa-rational-soul.md إلى con-parkinsons-law.md أبجدياً في content/ar/concepts/ (راجع state.json، claimed=9.18، للقائمة الكاملة).
