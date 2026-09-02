# Task 3.8
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-ckorsgaard، thk-comte)
- **أخطر اكتشاف: thk-ctart (تشارلز تارت)** — الملف كان لسه يعامله كـ"حي" (`active_end: مستمر`) رغم أنه **توفي فعلياً في 5 مارس 2025** — صُحح.
- **thk-cwhitaker (كارل ويتاكر)**: هذا الـslug كان محذَّراً منه صراحة في SPARK.md كمثال تاريخي على "إعادة تدوير slug" ممنوعة — تحقق الـsubagent وأكد أن المحتوى فعلاً عن كارل ويتاكر الحقيقي (لا انتهاك)، لكن اكتشف خطأ اسم متعاون حقيقي: "توماس نابير" (غير موجود) بدل **أوغسطس نابير** (Augustus Napier)، المؤلف الحقيقي المشارك لـ*The Family Crucible*.
- **محتوى مختلَق/غير قابل للتحقق حُذف**: `thk-csocarides` (عنوان كتاب "Sexual Preference and the Law 1996" لم يظهر في أي فهرسة موثوقة)، `thk-cwebster` (عنوان عمل ثانٍ غير مؤكد)، `thk-cwhitaker` (كتاب "Nightmares..." 1992 غير موثّق).
- **استحالة زمنية**: `thk-condillac` كان يزعم أن تجربته (1754) أثّرت في "شيطان ديكارت" (1641 — أسبق بقرن).
- **أخطاء تواريخ ميلاد/وفاة**: `thk-csoler` (سنة ميلاد "غير مؤكد" → صُححت 1937 بمصدر BnF)، `thk-cioran` (`active_end` كان يقطع 14 سنة من نشاطه)، `thk-confucius` (`active_start` كان مقلوباً/متناقضاً مع `active_source: lifespan`).
- **أخطاء نسبة/تصنيف**: `thk-cmadanes` (`belongs_to` نص حر بلا slug، واحتمال ازدواج مع `thk-cloemadanes` الموثّقة في Task 2.3 — **قرار حساس**)، `thk-crsnyder` (روابط محجورة فعلياً لسه موجودة رغم ادعاء الحذف في gaps)، `thk-clhull` (رابط بلا سبب مذكور، أُصلح بإضافة السياق التاريخي بدل الحذف).
- **نمط `sch-popular-psychology` المتكرر**: هذه الدفعة أضافت طلبين إضافيين لنفس الـslug الناقص (thk-colette-dowling) — الآن 4 حالات متراكمة عبر الدفعات (thk-brene-brown، thk-carlos-castaneda، thk-charles-duhigg، thk-colette-dowling). **يُنصح بإنشاء الـslug دفعة واحدة بدل تكرار الطلب.**

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{cialdini,cindy-hazan,cioran,clarissa,clarkson,claude-levi-strauss,cleanthes,clhull,cmadanes,cmalchiodi,cmartell,cmouffe,colette-dowling,combs,condillac,condorcet,condrau,confucius,copleston,corbett,crates-thebes,crenshaw,crsnyder,csikszentmihalyi,csocarides,csoler,ctart,cthompson,ctrungpa,cwebster,cwhitaker,czeanah,dabrowski}.md
→ ✅ 33 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة، وتصحيح تعارضات id/title.

## متوقف عنده (لرئيس التحرير)
- **thk-ctart**: تصحيح وفاته (مارس 2025) أولوية عالية — الملف المعتمد الحالي يقدّمه كحيّ.
- **thk-cmadanes ↔ thk-cloemadanes**: احتمال ازدواج slug حقيقي لنفس الشخص (كلوي مادانيس) — الأول معتمد بالفعل، والثاني وُثِّق في Task 2.3. يحتاج قرار دمج.
- **thk-cwhitaker**: تأكيد أن الـslug ليس انتهاكاً (المحتوى فعلاً عن كارل ويتاكر) — يستحق تسجيلاً في SPARK.md لتحديث التحذير التاريخي بأن الملف الحالي سليم الهوية بعد التصحيح.
- **thk-crsnyder**: روابط محجورة (thk-james-gumpert, thk-kevin-sparger) كانت لسه موجودة رغم ادعاء gaps بإزالتها — نفس النمط النظامي المكتشف في دفعات سابقة (3.5، 3.6)، صُححت هنا لكن يؤكد الحاجة لفحص شامل آلي.
- **thk-csocarides / thk-cwebster / thk-cwhitaker**: عناوين أعمال غير قابلة للتحقق حُذفت — القرار مبني على عدم التوثيق لا إثبات الاختلاق، يستحق تأكيداً لو توفر مصدر مستقل.
- **طلب `sch-popular-psychology`**: تراكم 4 طلبات منفصلة لنفس الـslug الناقص عبر الدفعات — يستحق إنشاءً واحداً بدل التكرار.

## الملفات
content/ar/thinkers/thk-cialdini.md
content/ar/thinkers/thk-cindy-hazan.md
content/ar/thinkers/thk-cioran.md
content/ar/thinkers/thk-ckorsgaard.md
content/ar/thinkers/thk-clarissa.md
content/ar/thinkers/thk-clarkson.md
content/ar/thinkers/thk-claude-levi-strauss.md
content/ar/thinkers/thk-cleanthes.md
content/ar/thinkers/thk-clhull.md
content/ar/thinkers/thk-cmadanes.md
content/ar/thinkers/thk-cmalchiodi.md
content/ar/thinkers/thk-cmartell.md
content/ar/thinkers/thk-cmouffe.md
content/ar/thinkers/thk-colette-dowling.md
content/ar/thinkers/thk-combs.md
content/ar/thinkers/thk-comte.md
content/ar/thinkers/thk-condillac.md
content/ar/thinkers/thk-condorcet.md
content/ar/thinkers/thk-condrau.md
content/ar/thinkers/thk-confucius.md
content/ar/thinkers/thk-copleston.md
content/ar/thinkers/thk-corbett.md
content/ar/thinkers/thk-crates-thebes.md
content/ar/thinkers/thk-crenshaw.md
content/ar/thinkers/thk-crsnyder.md
content/ar/thinkers/thk-csikszentmihalyi.md
content/ar/thinkers/thk-csocarides.md
content/ar/thinkers/thk-csoler.md
content/ar/thinkers/thk-ctart.md
content/ar/thinkers/thk-cthompson.md
content/ar/thinkers/thk-ctrungpa.md
content/ar/thinkers/thk-cwebster.md
content/ar/thinkers/thk-cwhitaker.md
content/ar/thinkers/thk-czeanah.md
content/ar/thinkers/thk-dabrowski.md
