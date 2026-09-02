# Task 3.10
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-dlewis، thk-dmarivoet)
- **مرشح مباشر لـTask 2: thk-dkirkland** — تضارب هوية غير قابل للحل بثقة: `title` = "دانيال كيركلاند" لكن `en` = "Don Hanlon Johnson" (شخصان حقيقيان مختلفان)، والمتن يصف مؤسسي "العلاج العلائقي المجسد" الحقيقيين (نِك توتون وإم إدموندسون) بلا علاقة بأي من الاسمين. **لم تُكتب مسودة — تُرك بلا تعديل حسب القاعدة 10.**
- **سبب وفاة خاطئ حساس: thk-drapaport (ديفيد رابابورت)** — الملف كان يذكر "انتحار" بينما المصادر تؤكد وفاته بنوبة قلبية في مركز أوستن ريغز. صُحح. كذلك جنسيته كانت "النمسا" خطأً (وُلد في بودابست، المجر)، والمبادئ الميتاسيكولوجية الثلاثة المذكورة لا تطابق الخمسة الحقيقية (رابابورت-غيل).
- **محتوى مختلَق حُذف**: `thk-dparfit` (كتاب "The Metaphysics of Creation 2013" وشخص "تيرنس أوكونيل" غير موجودين)، `thk-drew-leder` (كتاب *Phantoms in the Brain* منسوب له خطأً — هو لرامشاندران وبلايكسلي)، `thk-djackson` (عمل "The Eternal Triangle" غير قابل للتحقق).
- **أخطاء هوية/جنسية أخرى**: `thk-dorange` (الاسم العربي "دومينيك" لا يطابق الإنجليزي "Donna")، `thk-country` لـ`thk-donald-davidson` كانت "بيركلي" (مدينة لا دولة).
- **روابط محجورة فعلياً كانت لسه موجودة**: `thk-dgbarrera` (thk-rcasals محجور في quarantine-minimax.md)، `thk-dreynolds` (thk-rreibo وthk-tisoma محجوران).
- **احتمال تغيير هوية slug غير مُسجَّل (خارج نطاقي، نطاق MiniMax)**: `thk-dtutu` كانت رابطة بـ`thk-amncube` و`thk-bdanner` بعناوين لا تطابق محتوى تلك الملفات حالياً (بدت مسودة سابقة غيّرت هويتهما لشخصيتين مختلفتين تماماً بلا تسجيل في quarantine-minimax.md). حُذف الرابطان مؤقتاً؛ **يستحق تنبيه فريق MiniMax مباشرة.**
- عدة تصحيحات `edges.belongs_to` من نص حر لslug حقيقي، وحالة واحدة (thk-dong-zhongshu) بلا slug مطابق فسُجّلت في `missing-schools.md` بدل الاختراع.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{dfisher,dgbarrera,dgrand,dharmakirti,diderot,dieckmann,dignaga,dilthey,diogenes-sinope,djackson,dkalsched,dmeichenbaum,dmiller,dogen,donald-davidson,donbaer,dong-zhongshu,dorange,downing,dparfit,dpooleheller,drapaport,drew-leder,dreyfus,dreynolds,dsaleeby,dscharff,dsharp,dsiegel,dstern,dtacey,dtutu}.md
→ ✅ 32 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء (وُجدت في 4+ ملفات من هذه الدفعة وحدها)، تصحيح `edges.belongs_to`، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة، وإضافة أقسام `## المصادر` غائبة (thk-dsharp، thk-dsiegel، thk-dstern، thk-dtacey، thk-dtutu).

## متوقف عنده (لرئيس التحرير)
- **thk-dkirkland**: يحتاج تطبيق معيار Task 2 كامل — تضارب هوية جوهري.
- **thk-dtutu ↔ thk-amncube/thk-bdanner**: احتمال تغيير هوية slug في نطاق MiniMax بلا تسجيل — يستحق تنبيهاً مباشراً لفريق MiniMax للتحقق (هل التغيير شرعي أم يحتاج تسجيل الشخصيتين الأصليتين في quarantine-minimax.md؟).
- **thk-drapaport**: تصحيح سبب الوفاة (انتحار → نوبة قلبية) حساس ويستحق أولوية عالية في المراجعة قبل الترقية.
- **thk-dgbarrera**: تعارض تاريخي مشبوه (تحليل عند لويجي تسويا في ميلانو 1970 رغم أن تسويا كان عمره 27 فقط آنذاك) — لم يُحذف، سُجّل في gaps لعدم اليقين التام.
- **thk-dong-zhongshu**: لا slug لمدرسة "الكونفوشية الهانية" — نفس فجوة سبق تسجيلها لـthk-yang-xiong من MiniMax.

## الملفات
content/ar/thinkers/thk-dfisher.md
content/ar/thinkers/thk-dgbarrera.md
content/ar/thinkers/thk-dgrand.md
content/ar/thinkers/thk-dharmakirti.md
content/ar/thinkers/thk-diderot.md
content/ar/thinkers/thk-dieckmann.md
content/ar/thinkers/thk-dignaga.md
content/ar/thinkers/thk-dilthey.md
content/ar/thinkers/thk-diogenes-sinope.md
content/ar/thinkers/thk-djackson.md
content/ar/thinkers/thk-dkalsched.md
content/ar/thinkers/thk-dkirkland.md
content/ar/thinkers/thk-dlewis.md
content/ar/thinkers/thk-dmarivoet.md
content/ar/thinkers/thk-dmeichenbaum.md
content/ar/thinkers/thk-dmiller.md
content/ar/thinkers/thk-dogen.md
content/ar/thinkers/thk-donald-davidson.md
content/ar/thinkers/thk-donbaer.md
content/ar/thinkers/thk-dong-zhongshu.md
content/ar/thinkers/thk-dorange.md
content/ar/thinkers/thk-downing.md
content/ar/thinkers/thk-dparfit.md
content/ar/thinkers/thk-dpooleheller.md
content/ar/thinkers/thk-drapaport.md
content/ar/thinkers/thk-drew-leder.md
content/ar/thinkers/thk-dreyfus.md
content/ar/thinkers/thk-dreynolds.md
content/ar/thinkers/thk-dsaleeby.md
content/ar/thinkers/thk-dscharff.md
content/ar/thinkers/thk-dsharp.md
content/ar/thinkers/thk-dsiegel.md
content/ar/thinkers/thk-dstern.md
content/ar/thinkers/thk-dtacey.md
content/ar/thinkers/thk-dtutu.md
