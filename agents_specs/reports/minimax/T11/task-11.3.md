# Task 11.3
الحالة: مكتمل
العملية: debates+critiques: تسمية الطرفين/الناقد بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.3): صفر مخالفات آلية (30/30 ملف)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء الـ18 على الملفات الـ30): صفر تطابق

## ⚠️ مصادر ملفَّقة/خاطئة — حصاد ضخم في هذه الدفعة (أكثر من 15 حالة)
النمط المكتشف في 11.1/11.2 (استشهادات لا وجود لها) تأكد وتوسّع بشدة في هذه الدفعة. كل الحالات التالية اتصلحت بمصادر حقيقية تحقّقنا منها بحثياً، أو حُذفت وسُجِّلت في `gaps` لو مفيش بديل مؤكد:

- **crt-popper-critique-psychoanalysis**: مرجعان ملفَّقان بالكامل — "Malan 2001, *The Collapse of a Fact?*" و"James Edwards" (narcissism/falsifiability) — لا وجود لهما في أي فهرس أكاديمي. حُذفا.
- **crt-neurodiversity-aba-critique**: "Katherine Maygate" و"Joseph Talia" أشخاص غير موجودين (حُذفا)؛ "Morgen Runswick-Cole" اسم خطأ (الصحيح: Katherine Runswick-Cole)؛ خلط خطير بين جودي سينغر (صاغت neurodiversity) وبيتر سينغر (Practical Ethics)؛ Nick Walker's *Neurocosmopolitanism* (2014) كان مذكوراً ككتاب وهو فعلياً سلسلة مقالات مدونة — الكتاب الحقيقي *Neuroqueer Heresies* (2021).
- **crt-medicalization-of-poverty**: *Anatomy of an Epidemic* (2010) نُسب خطأً لـ"تشارلز ويتاكر" (thk-cwhitaker = Carl Whitaker، معالج أسري) بينما المؤلف الحقيقي هو Robert Whitaker (صحفي) — لا ملف thk- له في الأطلس، سُجِّل في gaps.
- **crt-postmodern-critique**: "Cabaniss & Mermigos (2017)" (الصحيح Cabanas & Illouz)؛ "Nightingale (2017)" غير موجود؛ *Individualisme et holisme* (1986) نُسب لـRaymond Boudon وحده (فعلياً بتحرير Birnbaum & Leca)؛ Bueter (2015) بمضمون غير مطابق لبحثها الفعلي.
- **crt-postcolonial-critique-cbt/dsm/psychoanalysis**: عشرات الأسماء المُختلَقة بالكامل ("Chantal Zerdoun"، "Victor Kholodkov"، "Suman Sinha"، وغيرها) حُذفت بالكامل واستُبدلت بمصادر حقيقية موثَّقة (Fanon، Kleinman، Said، Nandy، Hartnack، Maldonado-Torres، Martín-Baró).
- **crt-religious-conservative-critique-psychoanalysis**: "Alan Jones, *Letting Go of God* (1994)" (كتاب غير موجود)، "Adams (1970), *The Sexual Wilderness*" (خطأ نسب — الكتاب فعلياً لـVance Packard)، "Herbert Cox (1995)" (غير موجود)، بالإضافة لأسماء غامضة بلا مصدر.
- **crt-replication-crisis**: "Brian/Bryan Schimmack" (الصحيح Ulrich Schimmack)؛ "Koladich, Lilienfeld & Lodi-Smith (2017)" مُختلَق (الصحيح: Lilienfeld & Waldman 2017).
- **crt-research-ethics-historical**: "Melissa McCullough 2009"، "Darlene 2014"، "Susan Milius 2002" (بلا لقب/مصدر حقيقي) — حُذفت الثلاثة.
- **crt-hysteria-history**: إحصائيتان غير موثقتين برقم دقيق (70%/75%) استُبدلتا بصياغة عامة مدعومة، وتصحيح اسم مجلة Tasca et al. 2012.

**هذا يرفع إجمالي المصادر الملفَّقة/الخاطئة المكتشفة والمصحَّحة في Task 11 (11.1+11.2+11.3) إلى ما يزيد عن 20 حالة موثَّقة — النمط مؤكَّد كمشكلة منهجية عبر critiques/، ويستحق تدقيقاً شاملاً منفصلاً عن التنقية التسلسلية الحالية.**

## قرارات محتوى بارزة
- ثلاثية بوبر (crt-popper-critique-of-historicism / -psychoanalysis / -falsifiability-psychoanalysis): تأكيد أنها ثلاثة مواضيع متمايزة فعلياً (تاريخانية سياسية vs خريطة نقد واسعة vs تركيز على حجة القابلية للتفنيد تحديداً) — لم تُدمج، وأُضيف رابط تبادلي بين الأخيرين.
- ثلاثية ما-بعد-كولونيالية (crt-postcolonial-critique-cbt/dsm/psychoanalysis): تأكيد استهداف كل ملف موضوعاً مختلفاً فعلياً.
- crt-marx-theses-on-feuerbach: كان قالبياً بالكامل — أُعيد بالكامل حول محتوى فعلي (دفتر بروكسل 1845، نشر إنجلز 1888، الأطروحات 1/3/6/7/11).
- ملاحظة جانبية غير مُنفَّذة (خارج نطاق Task 11): ازدواج محتمل wrk-after-virtue / wrk-after-virtue-macintyre (يخص Task 16).

صفر slugs مخترعة (باستثناء تصحيح المصادر أعلاه بأسماء حقيقية موثَّقة بحثياً؛ الأسماء غير القابلة للتحقق حُذفت وسُجِّلت في gaps بدل استبدالها بتخمين).

## متوقف عنده (لرئيس التحرير)
- **⚠️ عاجل — النمط أصبح واسع النطاق**: أكثر من 20 استشهاد ملفَّق/خاطئ مؤكَّد عبر 90 ملفاً فقط من critiques/ (11.1+11.2+11.3) — يستدعي تدقيقاً منهجياً شاملاً لباقي critiques/ (186 ملفاً متبقياً) بمعيار تحقق بحثي إلزامي لكل استشهاد، وليس فقط preflight الآلي.
- crt-medicalization-of-poverty: Robert Whitaker (مؤلف *Anatomy of an Epidemic*) بلا ملف thk- في الأطلس.
- wrk-after-virtue / wrk-after-virtue-macintyre: ازدواج محتمل (Task 16).

## الملفات
crt-hysteria-history, crt-irigaray-critique-of-specular-reason, crt-kant-critique-of-metaphysics, crt-kierkegaard-critique-of-hegelian-system, crt-laroui-critique-of-traditionalist-eclecticism, crt-lyotard-critique-of-grand-narratives, crt-macintyre-after-virtue, crt-marcuse-critique-of-consumerism, crt-marx-critique-of-capitalist-alienation, crt-marx-theses-on-feuerbach, crt-marxist-critique-psychology, crt-medicalization-of-poverty, crt-nagarjuna-critique-of-svabhava, crt-neurodiversity-aba-critique, crt-neuroscience-critique-classic-theories, crt-nietzsche-critique-of-christian-morality, crt-nozick-critique-of-patterned-justice, crt-pascal-critique-of-cartesian-rationalism, crt-popper-critique-of-historicism, crt-popper-critique-psychoanalysis, crt-popper-falsifiability-psychoanalysis, crt-postcolonial-critique-cbt, crt-postcolonial-critique-dsm, crt-postcolonial-critique-psychoanalysis, crt-postmodern-critique, crt-quijano-critique-of-colonial-matrix, crt-quine-two-dogmas, crt-religious-conservative-critique-psychoanalysis, crt-replication-crisis, crt-research-ethics-historical
