# Task 9.16
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط (10 subagents متوازية) | الملفات: 55

## الأرقام
جمل القائمة السوداء: بعد 0
سقّالة ظاهرة: قبل 1 (con-maladaptive-emotion.md: "## ملاحظة معمارية") → صحّحته بنفسي (أعدت تسمية العنوان لـ"## الروابط والسياق" بلا حذف محتوى) → بعد 0

## أمر التحقق
`python3 scripts/task.py verify minimax 9.16` → جمل قائمة سوداء: 0، سقّالة: 0 (بعد تصحيحي)
`python3 scripts/preflight_check.py <55 ملفاً>` → صفر مخالفات

## قرارات اتخذتها
- **ازدواجات مكتشفة (سُجّلت بدل الدمج، خارج نطاق Task 9):**
  - con-jianai.md ⟷ con-jian-ai-universal-love.md (نفس مفهوم موزي "الحب الشامل")
  - con-karma-and-samsara.md ⟷ con-karma-philosophy.md (نفس مفهوم الكارما، الأول قالبي والثاني مطوَّر)
  - con-intersectional-feminism.md ⟷ con-intersectionality.md (تقاطع حقيقي، أجزاء مختلفة philosophy/psychology)
  - con-maat.md ⟷ con-maat-ethics.md (مفهوم ماعت المصري)
- **طلبات slug جديدة مسجَّلة في requests-minimax.md:** thk-frank-jackson (فيلسوف حجة المعرفة، لا يخلط مع thk-djackson).
- صحّحت بنفسي مخالفة سقّالة واحدة (con-maladaptive-emotion.md) بعد التسليم.
- الـsubagents صحّحوا عدداً كبيراً من مخالفات preflight قديمة قبل التسليم: عناوين related غير مطابقة (con-loneliness-solitude، con-modern-conflict، con-moi-peau، وغيرها)، edges بنص حر بدل slug (10+ حالة)، وجمل قائمة سوداء في المتن/gaps.
- ملفات اكتفت بعدد روابط أقل من 4 عمداً حين المادة النصية لا تسمّي مفكرين/مدارس إضافية (con-intergenerational-historical-trauma: رابطان فقط).

## متوقف عنده (لرئيس التحرير)
- 4 أزواج ازدواج محتملة مسجّلة أعلاه تستاهل قرار دمج/فصل تحريري.
- طلب slug: thk-frank-jackson.

## الملفات
55 ملف — راجع agents_specs/reports/minimax/state.json (claimed=9.16) للقائمة الكاملة، أو نطاق con-intentionality-consciousness.md إلى con-li-principle-neoconfucian.md أبجدياً في content/ar/concepts/.
