# Task 9.17
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط (10 subagents متوازية) | الملفات: 60

## الأرقام
جمل القائمة السوداء: بعد 0
سقّالة ظاهرة: قبل 1 (con-land-based-healing.md: "## ملاحظة معمارية") → صحّحته بنفسي (أعدت تسمية العنوان لـ"## الروابط والسياق" بلا حذف محتوى) → بعد 0

## أمر التحقق
`python3 scripts/task.py verify minimax 9.17` → جمل قائمة سوداء: 0، سقّالة: 0 (بعد تصحيحي)
`python3 scripts/preflight_check.py <60 ملفاً>` → صفر مخالفات

## قرارات اتخذتها
- **ازدواجات مكتشفة (سُجّلت بدل الدمج):**
  - con-liangzhi.md ⟷ con-liangzhi-innate-knowing.md (نفس مفهوم 良知 الصيني، الثاني نسخة مختصرة)
  - con-lifeworld.md ⟷ con-lifeworld-lebenswelt.md (نفس مفهوم Lebenswelt عند هوسرل)
  - con-mandate-of-heaven-legitimacy.md ⟷ con-mandate-of-heaven-tianming.md (نفس مفهوم تفويض السماء الصيني)
  - con-maya-cosmic-illusion.md ⟷ con-maya-vedanta.md (نفس مفهوم مايا الهندوسي)
  - con-monad.md ⟷ con-monad-simple-substance.md (مونادة لايبنتز، الأول مطوَّر جداً)
- **طلبات slug جديدة مسجَّلة في requests-minimax.md:** thk-mackie (جون ماكي)، thk-bernard-williams، thk-dancy، thk-zajonc (كل واحد مفكر حقيقي بلا ملف مستقل — الأسماء المشابهة في الأطلس أشخاص مختلفون فعلاً)، thk-shulgin وdbt-mdma-ptsd-trial وcon-internal-healer (دفعة 9.2).
- صحّحت بنفسي مخالفة سقّالة واحدة (con-land-based-healing.md) بعد التسليم.
- الـsubagents صحّحوا مخالفات preflight قديمة كثيفة: عناوين related غير مطابقة (10+)، edges بنص حر بدل slug (8+، منها استبدالات ناجحة بـslugs حقيقية مثل sch-korean-neoconfucian، sch-shinto-philosophical)، تصحيح thk-jgone (كان مسجَّلاً خطأً كـ"غير موجود" في gaps قديمة بينما هو موجود فعلاً).
- con-mind-body.md وcon-mindfulness.md وصلا لـ10 روابط (السقف الإرشادي) نظراً لثراء المادة الموثقة الفعلية.

## متوقف عنده (لرئيس التحرير)
- 5 أزواج ازدواج محتملة مسجّلة أعلاه تستاهل قرار دمج/فصل تحريري (المجموع التراكمي من 9.16+9.17: 9 أزواج).
- 5 طلبات slug جديدة (thk-mackie، thk-bernard-williams، thk-dancy، thk-zajonc، thk-shulgin).

## الملفات
60 ملف — راجع agents_specs/reports/minimax/state.json (claimed=9.17) للقائمة الكاملة، أو نطاق con-li.md إلى con-myth-of-given.md أبجدياً في content/ar/concepts/.
