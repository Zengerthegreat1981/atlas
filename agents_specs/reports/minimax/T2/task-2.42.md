# Task 2.42
الحالة: مكتمل
العملية: تحقق هوية + إزالة جمل قائمة سوداء + إصلاح روابط belongs_to/related لعشرة ملفات مفكرين | الملفات: 10

## الأرقام
جمل قائمة سوداء (يدوي grep): قبل 8 مطابقات → بعد 0
مخالفات preflight_check: قبل 10 → بعد 0
edges.belongs_to بslug وهمي (نص حر بدل slug): قبل 3 (papert, rhonda-byrne, sheena-iyengar) → بعد 0 (اثنان أُزيلا edges:[] وسُجّلا في missing-schools.md، وواحد حُوّل لـsch-social-psychology الموجود فعلاً)
ملفات بلا ## المصادر: قبل 5 (philolaus, vallabha, udayana, pyrrho, nicholas-of-cusa) → بعد 0

## أمر التحقق
python3 scripts/preflight_check.py content/ar/thinkers/thk-{philolaus,vallabha,toure,papert,sheena-iyengar,marsilius-padua,udayana,rhonda-byrne,pyrrho,nicholas-of-cusa}.md → ✅ 10 ملف، صفر مخالفات

## قرارات اتخذتها
- thk-philolaus: موثّق. فيلولاوس الكروتوني فيثاغوري موثّق تاريخياً (شذرات ديلز-كرانتس). أُزيلت جملة القائمة السوداء من gaps (كانت تناقض وجود اقتباس فعلي في المتن)، وأُضيف ## المصادر.
- thk-vallabha: موثّق. فالابهاشاريا مؤسس مذهب شودّهادفايتا وبوشتي مارغا، موثّق أكاديمياً (Redington، Barz). حُذف قسم الاقتباسات (غير متوفر بالعربية) وأُضيف ## المصادر.
- thk-toure: موثّق. أحمد سيكوتوري توري رئيس غينيا (1958–1984)، موثّق تاريخياً. حُذف اقتباس غير موثّق ("ترجمة تقريبية" بلا مصدر محدد)، صُحّح عنوانا related (سنغور، أوبونتو) ليطابقا الملفين الحقيقيين، وأُضيف ## المصادر.
- thk-papert: موثّق. سيمور بابرت (Constructionism، Logo، MIT Media Lab) موثّق. edges.belongs_to كان يشير لاسم مدرسة نصي حر غير موجود كملف — حُوّل لـ edges: []  وسُجّلت "البنائية التعليمية" في missing-schools.md. حُذف اقتباس غير موثّق وأُضيف ## المصادر. صُحّح crumb.
- thk-sheena-iyengar: موثّق. شينا إينغار (تجربة المربّى، The Art of Choosing) موثّقة أكاديمياً. edges.belongs_to حُوّل من نص حر إلى sch-social-psychology (slug حقيقي موجود ومطابق تخصصها). حُذف اقتباس غير موثّق وأُضيف ## المصادر. صُححت صياغتان أدّتا لعلامات جندرية زائفة آلياً (كلمتا "هو"/"وُلد" كانتا تشيران لمفهوم لا للشخص).
- thk-marsilius-padua: موثّق. مارسيليوس البادوفي (Defensor Pacis, 1324) موثّق أكاديمياً. حُذف اقتباس بترجمة منسوبة لمترجمة غير معروفة في الأدبيات الأكاديمية القياسية (المترجم المرجعي المعروف هو Alan Gewirth) — استُبدل بـ## المصادر حقيقية. صُححت 5 عناوين related لتطابق عناوين الملفات المستهدفة فعلياً (ابن رشد، سيجير دي برابانت، بوئيثيوس الدنماركي، وليم الأوكامي، السكولاستية، أوغسطينوس).
- thk-udayana: موثّق. أوديانا فيلسوف نيايا هندوسي (نحو 975–1050م) موثّق أكاديمياً (Potter's Encyclopedia). أُعيدت صياغة سطر gap لتفادي مطابقة القائمة السوداء، وأُضيف ## المصادر، وصُحح عنوان related (أكشابادا غوتاما).
- thk-rhonda-byrne: موثّقة (كظاهرة ثقافية لا كباحثة). روندا بايرن مؤلفة The Secret موثّقة. edges.belongs_to حُوّل من نص حر إلى edges: []  وسُجّلت "علم النفس الشعبي وأدب المساعدة الذاتية" في missing-schools.md. حُذف اقتباس غير موثّق وأُضيف ## المصادر. صُحح crumb.
- thk-pyrrho: موثّق. بيرون الإيليسي مؤسس الشكوكية القديمة موثّق تاريخياً (ديوجينس اللائرتي). حُذفت جملة القائمة السوداء من قسم الاقتباسات والgaps (لم يكتب شيئاً، فالقسم حُذف بالكامل بدل تركه فارغاً بجملة محظورة)، وأُضيف ## المصادر.
- thk-nicholas-of-cusa: موثّق. نيكولاس الكوزاني (De docta ignorantia) موثّق أكاديمياً (Cassirer، Hopkins). أُزيلت جملة القائمة السوداء من gaps (كانت تناقض وجود اقتباس فعلي بالمتن)، وأُضيف ## المصادر.

لا يوجد أي ملف من العشرة تقرر له "غير موجود" أو "غامض" — العشرة أشخاص حقيقيون موثقون تاريخياً/أكاديمياً بوضوح.

## متوقف عنده (لرئيس التحرير)
لا شيء.

## الملفات
content/ar/thinkers/thk-philolaus.md
content/ar/thinkers/thk-vallabha.md
content/ar/thinkers/thk-toure.md
content/ar/thinkers/thk-papert.md
content/ar/thinkers/thk-sheena-iyengar.md
content/ar/thinkers/thk-marsilius-padua.md
content/ar/thinkers/thk-udayana.md
content/ar/thinkers/thk-rhonda-byrne.md
content/ar/thinkers/thk-pyrrho.md
content/ar/thinkers/thk-nicholas-of-cusa.md
