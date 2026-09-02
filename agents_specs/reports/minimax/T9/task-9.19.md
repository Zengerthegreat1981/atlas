# Task 9.19
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط (10 subagents متوازية) | الملفات: 60

## الأرقام
جمل القائمة السوداء: بعد 0
سقّالة ظاهرة: بعد 0

## أمر التحقق
`python3 scripts/task.py verify minimax 9.19` → جمل قائمة سوداء: 0، سقّالة: 0
`python3 scripts/preflight_check.py <60 ملفاً>` → صفر مخالفات

## قرارات اتخذتها
- **ازدواجات مكتشفة (تراكمي 9 أزواج هذه الدفعة، منها 2 نُفيا فعلياً بعد تحقق):**
  - con-peak-experience.md ⟷ con-peak-experience-maslow.md — **ليس ازدواجاً**: عام مقابل تفصيل موسّع بإحالة صريحة.
  - con-political-liberalism.md ⟷ con-overlapping-consensus-rawls.md — **ازدواج حقيقي مؤكَّد نهائياً** (سُجّل R-010 الأصلي، بعد إعادة الترقيم).
  - con-polyvagal-theory.md ⟷ con-polyvagal-theory-popular.md ⟷ con-polyvagal-states.md — ثلاثي متداخل (أكاديمي/شعبي/سريري)، لم يُدمج.
  - con-primary-emotion.md ⟷ con-primary-adaptive-maladaptive-emotions.md — تداخل حقيقي (فئة فرعية مقابل تصنيف كامل).
  - con-psilocybin.md ⟷ con-psilocybin-depression.md — تداخل موضوعي (نفس تجارب Johns Hopkins/Imperial).
  - con-purusha.md ⟷ con-purusha-prakriti-dualism.md — **ليس ازدواجاً**: الأول معمّق، الثاني سقّالة عامة تحتاج تعميق (Task 10).
- **إصلاح تصادم ترقيم**: subagents مختلفة استخدمت "R-010" لطلبين مختلفين (con-political-liberalism وcon-secondary-emotion) بدون تنسيق بينها — أعدت ترقيم الثاني لـR-013 بعد التحقق.
- **طلبات slug جديدة:** R-012 (لا يوجد ملف لإرنست فيبر Weber ولا ستانلي ستيفنز Stevens — الأسماء المشابهة في الأطلس أشخاص مختلفون)، R-013 (con-secondary-emotion/con-emotion-regulation)، إضافة لطلبات مفردة (Helen Wambach، Ian Stevenson، Heidi Hartmann، Gersonides، Robert/Lynn Koegel — مطوّرا PRT).
- **ثلاث حالات ملفات كسر YAML مؤقت أثناء التحرير** اكتُشفت وأُصلحت ذاتياً بمعرفة نفس الـsubagent المسؤول (con-patriarchy.md، con-purusha-prakriti-dualism.md) — تحققت بنفسي من سلامتها النهائية عبر preflight.
- تضارب اسمي (thk-griffiths): مارك غريفيثز (إدمان قمار) مقابل رولاند غريفيثز (سيلوسيبين، جونز هوبكنز) — صُحح في con-psilocybin.md، وتُرك بلا ربط في con-psilocybin-depression.md عند الشك بدل التخمين.

## متوقف عنده (لرئيس التحرير)
- تراكم الازدواجات المسجّلة عبر Task 9 لحد الآن: **~20 زوجاً** — تستاهل مراجعة تحريرية مجمّعة بدل التعامل معها واحداً واحداً.
- طلبات slug: R-012، R-013، بالإضافة لأسماء مفردة متعددة أعلاه.

## الملفات
60 ملف — نطاق con-parrhesia-fearless-speech.md إلى con-purusha.md أبجدياً في content/ar/concepts/ (راجع state.json، claimed=9.19، للقائمة الكاملة).
