# Task 2.5
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 5

## الأرقام
جمل القائمة السوداء: قبل 4 → بعد 0
سقّالة ظاهرة: قبل 0 → بعد 0
ملفات فيها ## المصادر: قبل 0/5 → بعد 5/5
موثّق (أعيدت كتابته): 4 (thk-tstone, thk-ssolomon, thk-tteo, thk-ramsden)
حُجر: 1 (thk-rollins)
غامض: 0

## أمر التحقق
python3 scripts/task.py verify minimax 2.5  →  جمل القائمة السوداء: 0 | سقّالة ظاهرة: 0 | فيها ## المصادر: 5/5
python3 scripts/preflight_check.py <5 ملفات>  →  ✅ صفر مخالفات آلية

## قرارات اتخذتها
- thk-tstone (مارك ستون): **موثّق**. شخص حقيقي — بروفوست/نائب رئيس جامعة أدلر، دبلوم في علم النفس الأدلري، مؤلف *Adler Speaks* و*Life-Lies and Self-Deception* (مؤكَّد عبر Goodreads وAbeBooks). حُذف ادّعاء كتاب "تدخلات أدلرية لـ DSM-5" غير الموجود في أي مصدر، وحُذفت روابط related غير مبرَّرة في المتن (thk-rsperry، thk-dgray) لأن لا صلة موثقة. أُضيفت gap توضّح أن الربط بين هذا الشخص وبين "Mark H. Stone" المؤلف المشارك لكتاب *Best Test Design* (قياس راش مع بنجامين رايت) **غير مؤكَّد** رغم تطابق الاسم — لتفادي دمج هويتين مختلفتين محتملتين.
- thk-ssolomon (شيلدون سولومون): **موثّق**. شخص حقيقي موثَّق بكثافة — أستاذ في كلية سكيدمور، أحد مؤسسي Terror Management Theory مع غرينبرغ وبيسزينسكي، مبني على أطروحة إرنست بيكر. أعيد كتابة المتن بمصادر (ويكيبيديا، الكتاب المشترك *The Worm at the Core* 2015، مقابلة PsychAlive)، وحُذف رابط `exp-derealization-depersonalization` لعدم وجود تبرير له في المتن.
- thk-rollins (Stephen Rollins): **غير موجود**. بحث ويب مباشر عن "Stephen Rollins" + MAPS/CIIS لم يُظهر أي وجود له كمدرب في العلاج بالمساعدة النفسية؛ الشخص الوحيد المطابق اسمياً (Steven Rollins) مدرب تنويم مغناطيسي عسكري متقاعد بلا صلة. المتن الأصلي كان صياغة قالبية بعلامات اقتباس مفرطة بلا أي واقعة موثَّقة — نمط نموذجي لملف مختلَق. النسخة الأصلية أُرشفت في `agents_specs/quarantine-minimax-archive/thk-rollins.md.archived.2026-08-27`، والملف الحالي استُبدل بقالب حجر موحّد يحيل إلى `quarantine-minimax.md` (سطر جديد في القسم 2).
- thk-tteo (توماس تِئو): **موثّق**. شخص حقيقي — أستاذ في جامعة يورك، برنامج الدراسات التاريخية والنظرية والنقدية لعلم النفس، حائز جائزة ثيودور ساربين من APA. صُحِّحت عناوين كتبه: العنوانان الأصليان "Psychology Misapplied" (2018) و"Critique in Psychology" (2014) غير موجودين في أي فهرس — استُبدلا بالعنوانين الصحيحين الموثَّقين: *The Critique of Psychology: From Kant to Postcolonial Theory* (2005) و*A Critical History and Philosophy of Psychology* (2018). حُذف قسم "اقتباسات مختارة" الذي كان يحتوي جملة القائمة السوداء حرفياً.
- thk-ramsden (رينيه رامسدن): **موثّق**. شخص حقيقي — محلّلة يونغية في كيب تاون، عضو مؤسِّس ورئيسة سابقة لـSAAJA، موثَّقة عبر موقع SAAJA ودراسة *Encountering the Other: Jungian Analysts and Traditional Healers in South Africa* (2024) التي توثّق مشاركتها في حوار المعالجين اليونغيين والتقليديين منذ 2016. حُذف رابط `thk-jdavid` (جوردان ديفيد) لعدم وجود ما يثبت صلة موثقة به، وسُجِّل ذلك صراحة في gaps بدل حذفه صامتاً.

## متوقف عنده (لرئيس التحرير)
- thk-tstone: يحتاج تأكيداً بشرياً/بحثاً إضافياً هل "مارك ستون الأدلري" (بروفوست جامعة أدلر) و"مارك إچ. ستون" (مؤلف Best Test Design مع بنجامين رايت في قياس راش) شخص واحد أم شخصان مختلفان بنفس الاسم — لم أُدرج أياً من ادّعاءات الرابط بينهما لعدم التأكد.

## الملفات
content/ar/thinkers/thk-tstone.md
content/ar/thinkers/thk-ssolomon.md
content/ar/thinkers/thk-rollins.md
content/ar/thinkers/thk-tteo.md
content/ar/thinkers/thk-ramsden.md
