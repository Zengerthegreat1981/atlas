# متتبّع حزم مدارس علم الاجتماع — موضع التوقّف/الاستئناف على مستوى المدرسة

> **لماذا هذا الملف:** `sociology-schools-backlog.md` اكتمل بالكامل (159/159 مدرسة) في 2026-09-14
> ولم يعد صالحاً لتتبّع التقدّم. هذا الملف يتتبّع المرحلة التالية من `SOCIOLOGY_MISSION_PROMPT.md`:
> لكل مدرسة من الـ159، بناء **حزمتها** — مفكروها (`thk-`)، مفاهيمها (`con-`)، أعمالها (`wrk-`)،
> دراساتها (`stu-`)، جدالاتها (`dbt-`) — حتى الوصول إلى هدف 1,200–1,500 عقدة حيّة بـ`part: "sociology"`.

## كيفية الاستخدام

- `- [ ]` = حزمة المدرسة لم تُبدأ بعد.
- `- [~]` = حزمة جزئية (بعض عناصرها مكتوب، وليس كلها).
- `- [x]` = حزمة مكتملة معقولاً (مفكروها الرئيسون + مفهوم واحد على الأقل + مصدر موثَّق لكل ملف)؛
  «مكتملة» هنا لا تعني «شاملة كل تفصيل» بل أن المدرسة لم تعد «هيكلاً عارياً» بلا محتوى داعم.
- عند كل بند، إن كان مفكّرو المدرسة موجودين مسبقاً في أقسام أخرى (`philosophy`/`psychology`/`bridge`)
  فالمطلوب هو **الربط عبر `related`** (كما جرى فعلاً في دفعات المدارس)، لا إنشاء ملف ثانٍ مكرَّر —
  راجع قائمة «الأصول الموجودة سلفاً» في `SOCIOLOGY_PART_PLAN.md` (القسم 0-B) قبل كتابة أي `thk-` جديد.
- بعد كل دفعة: `check_content_integrity.py` ثم `build_atlas.py` ثم `audit_atlas.py` (صفر إلزامي)،
  ثم تحديث هذا الملف (`[ ]`→`[~]`→`[x]`)، ثم الالتزام والدفع.

## ⚠️ ملاحظة تصحيحية مؤجَّلة — معجم `sociological_tradition`

القيم المستعملة فعلياً في الدفعات 1–8 لمدارس علم الاجتماع (`classical-foundational`,
`chicago-interactionist`, `structural-functionalist`, `exchange-rational-choice`, `conflict-critical`,
`post-structuralist`, `practice-theoretical`, `phenomenological-ethnomethodological`,
`decolonial-global-south`, `feminist`, `contemporary-globalization`, `specialized-subdiscipline`,
`systems-theoretical`, `organizational`, `arab-islamic-sociology`) **لا تطابق حرفياً** المعجم المغلق
المعتمد في DR-009 (`classical-positivist`, `marxian-conflict`, `weberian-interpretive`,
`structural-functionalist`, `symbolic-interactionist`, `phenomenological-ethnomethodological`,
`exchange-rational-choice`, `critical-theory`, `structuralist-poststructuralist`, `feminist-gender`,
`postcolonial-decolonial-global`, `arab-islamic-sociology`, `contemporary-synthetic`,
`applied-specialized`). لا فحصَ قاطعاً في `audit_atlas.py` يرصد هذا الانحراف حالياً (الحقل غير
مُتحقَّقٍ منه آلياً)، فلم يُوقِف أيَّ التزام، لكنه انحرافٌ حقيقي عن القرار المعماري المعتمد.
**القرار لهذه المرحلة:** الملفات الجديدة (حزم المفكرين/المفاهيم) تستعمل معجم DR-009 حرفياً من الآن
فصاعداً. تصحيح الـ136 ملف مدرسة القائمة مهمةٌ منفصلة مؤجَّلة (لا تُحل ضمن دفعات الحزم)، ويجب ألا
تُنسى: أضِفها كبند عمل صريح حين يُستكمل بناء الحزم ولا تُغلق هذا الملف قبل تنفيذها أو تسجيلها
رسمياً كتنازل معماري موثَّق.

## موضع التوقّف الحالي

**الدفعة 9 (2026-09-14):** بدأت حزم القسم 1. كُتبت 11 ملف مفكر جديد (`thk-durkheim`, `thk-simmel`,
`thk-sumner`, `thk-pareto`, `thk-mosca`, `thk-michels`, `thk-martineau`, `thk-veblen`, `thk-tonnies`,
`thk-tarde`, `thk-lebon`)، وأُصلحت خمسة أخطاء توثيق سابقة في ملفات مدارس زعمت خطأً غياب مفكرين
موجودين فعلاً في أقسامٍ أخرى (كونت، سبنسر، ماركس، فيبر، دوبوا) — أُضيف `related` صحيح لكلٍّ منها
مع تصحيح رجعي في `gaps`. **أوّل بندٍ للدفعة التالية:** إكمال حزمة القسم 1 (مفاهيم `con-` وأعمال
`wrk-` ودراسات `stu-` لكل مدرسة أُضيف لها مفكر — لم تُكتب بعد لأيٍّ منها)، ثم `sch-khaldunian-ilm-
al-umran` و`sch-booth-rowntree-social-survey` (لا مفكر مستقل لهما بعد ضمن هذه الدفعة).

**الدفعة 10 (2026-09-14):** أُكملت أول حلقة مفاهيم/أعمال للقسم 1 — 4 ملفات `con-` جديدة
(`con-anomie-durkheim`, `con-conspicuous-consumption`, `con-gemeinschaft-gesellschaft`,
`con-iron-law-of-oligarchy`) و2 ملف `wrk-` جديد (`wrk-suicide-durkheim`,
`wrk-theory-of-leisure-class-veblen`)، مع تحديث `related` في `thk-durkheim`, `thk-michels`,
`thk-tonnies`, `thk-veblen`، وفي مدرستي `sch-mertons-strain-theory` (ربط بـ`con-anomie-durkheim`
الأصلي) و`sch-bourdieu-distinction-cultural-reproduction` (ربط بـ`con-conspicuous-consumption`
كأصل تاريخي لتحليل بورديو). الفحوص الثلاثة كلها صفر. **ملاحظة تنسيق:** وكيلٌ ثانٍ يعمل بالتوازي
على الأقسام 5–8 من هذا الملف؛ هذه الجلسة تقتصر من الآن فصاعداً على **الأقسام 1–4 فقط**.
**أوّل بند للدفعة التالية:** بقية مفكري/مفاهيم/أعمال القسم 1 (دو بوا، مارتينو، تارد ولوبون،
سمنر — لم تُكتب لهم `con-`/`wrk-` بعد)، ثم `sch-khaldunian-ilm-al-umran` و
`sch-booth-rowntree-social-survey`، ثم الانتقال للقسم 2 (شيكاغو والتفاعلية الرمزية).

**الدفعة 11 (2026-09-14):** أُكملت حلقة ثانية من مفاهيم/أعمال القسم 1 — 4 ملفات `con-` جديدة
(`con-double-consciousness-dubois`, `con-folkways-mores-sumner`, `con-laws-of-imitation-tarde`,
`con-crowd-mind-lebon`) و1 ملف `wrk-` جديد (`wrk-philadelphia-negro-dubois`)، مع تحديث `related`
في `thk-web-dubois`, `thk-sumner`, `thk-tarde`, `thk-lebon`. لم يبقَ في القسم 1 مفهومٌ/عملٌ مستقلٌّ
لم يُكتب إلا لمارتينو (لا `con-`/`wrk-` مستقل بعد لترجمتها كونت أو منهجها في الملاحظة المقارنة —
مؤجَّل لأنه أقلّ مركزية من بقية المفاهيم). الفحوص الثلاثة صفر. **ملاحظة تعايش:** جرى العمل في نفس
شجرة العمل المشتركة مع الوكيل الثاني (الأقسام 5–8)؛ استُعمل `git add` بمسارات محدَّدة لا `-A` لتفادي
التقاط تعديلاته غير المُلتزمة (`sch-bourdieu-*`, `sch-foucauldian-*`) ضمن هذا الالتزام.
**أوّل بند للدفعة التالية:** `sch-khaldunian-ilm-al-umran` و`sch-booth-rowntree-social-survey`
(لا مفكر مستقل لهما بعد)، ثم الانتقال إلى القسم 2 (شيكاغو والتفاعلية الرمزية).

**الدفعة 12 (2026-09-14):** إكمال آخر بندي القسم 1. لـ`sch-khaldunian-ilm-al-umran` (كان موجوداً
سلفاً منذ الدفعة 1): أُضيف `con-asabiyyah-ibn-khaldun` (مفهوم العصبية مفصَّلاً) ورابطه في المدرسة
وفي `thk-ibn-khaldun`. لـ`sch-booth-rowntree-social-survey`: كُتب `thk-booth` و`thk-rowntree`
(كلاهما جديد) و`con-poverty-line-rowntree`، وأُسندا بـ`belongs_to` وربطا في المدرسة. **بذلك اكتمل
القسم 1 بأكمله معقولاً** إلا `sch-martineau-feminist-sociology` (يبقى `[~]`، لا `con-`/`wrk-`
مستقل بعد لمارتينو — أقل مركزية، مؤجَّل). الفحوص الثلاثة صفر. **ملاحظة معرِّفات مهمة:** واجهت هذه
الدفعة تصادمَي id فعليَّين مع ملفات غير مُلتزمة للوكيل الثاني (`CON-30xx`, `THK-63xx` تكرَّرت)؛ حُلَّا
برفع معرِّفات هذه الدفعة إلى نطاق أعلى (`THK-6390+`, `CON-3050+`) بدل نطاق `CON-3030s`/`THK-6380s`
الذي بات مزدحماً بعمل متزامن. **أي دفعة لاحقة يجب أن تتحقق من أعلى id مستعمل فعلياً في الشجرة قبل
التثبيت، لا الافتراض أن آخر id مُلتزم هو الأعلى**، لأن الشجرة مشتركة بين وكيلين الآن. كذلك: `Write`
على ملف مدرسة (`sch-khaldunian-ilm-al-umran`) بدل قراءته أولاً أدّى إلى الكتابة فوق نسخة موجودة
فعلاً (بمعرِّف وفحوى مختلفين) قبل أن يُلتقَط الخطأ بفحص السلامة ويُصحَّح — **درسٌ**: التحقق بـ`find`/`ls`
مباشرة قبل `Write` على أي مسار جديد الآن، لا الاعتماد على بحث سابق قد يكون فشل صامتاً.
**أوّل بند للدفعة التالية:** الانتقال إلى القسم 2 (شيكاغو والتفاعلية الرمزية) — أول بنوده:
`sch-chicago-urban-ecology`.

**الدفعة 13 (2026-09-14):** أول بند من القسم 2. كُتب `thk-robert-park` و`thk-ernest-burgess`
(بادئتا `thk-park`/`thk-burgess` مستعملتان سلفاً لمفكرين آخرين مختلفين تماماً، فاستُعملت صيغة
الاسم الكامل) و`con-concentric-zone-model-burgess`، وأُسندت جميعاً إلى `sch-chicago-urban-ecology`
(موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة
(فحص الشجرة الكاملة يُظهر عزلة `thk-ulrich-beck`، ملف غير مُلتزم لوكيل آخر، لم يُلمس هنا).
**أوّل بند للدفعة التالية:** `sch-wirthian-urbanism-ghetto` (سوسيولوجيا الحياة الحضرية والغيتو).

**الدفعة 14 (2026-09-14):** كُتب `thk-wirth` و`con-urbanism-as-way-of-life` وأُسندا إلى
`sch-wirthian-urbanism-ghetto` (موجودة سلفاً منذ الدفعة 2)، وأُضيفت روابطهما فيها. الفحوص
الثلاثة صفر. **⚠️ حادثةُ سباقٍ على الفهرس المشترك:** الالتزام الأول لهذه الدفعة (712f2f45) حمل
رسالتها لكنه التزم فعلياً ملفات وكيلٍ آخر بالخطإ (كانت مرحَّلةً في فهرس `git` المشترك بين الجلستين
في نفس شجرة العمل عند لحظة `commit`)، بينما ملفات هذه الدفعة الحقيقية بقيت غير مُلتزمة رغم `git add`
سابقٍ لها. صُحِّح ذلك بالتزامٍ ثانٍ (cbf880bb) يحمل الملفات الصحيحة، بعد التحقق من `git status`
مباشرة قبل `commit`. **درسٌ مُلزم لكل دفعة تالية: تحقّق من `git status --short` فوراً قبل كل
`git commit` مباشرة، لا الاكتفاء بـ`git add` سابق قد يُسبَق بعملية `add`/`commit` من الجلسة الأخرى.**
**أوّل بند للدفعة التالية:** `sch-thomas-znaniecki-life-history`.

**الدفعة 15 (2026-09-14):** كُتب `thk-wi-thomas`، `thk-znaniecki`، `con-thomas-theorem`، و
`stu-polish-peasant-thomas-znaniecki` (أول ملف `stu-` في قسم علم الاجتماع)، وأُسندت جميعاً إلى
`sch-thomas-znaniecki-life-history` (موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطها فيها. الفحوص
الثلاثة صفر. **أوّل بند للدفعة التالية:** `sch-whyte-participant-observation`.

**الدفعة 16 (2026-09-14):** كُتب `thk-wf-whyte` و`stu-street-corner-society-whyte`، وأُسندا إلى
`sch-whyte-participant-observation` (موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطهما فيها. الفحوص
الثلاثة صفر على نطاق ملفات هذه الدفعة (فحص الشجرة الكاملة يُظهر تصادمَي id وعزلاتٍ في ملفات غير
مُلتزمة لوكيل آخر — `thk-nick-srnicek`, `thk-deborah-lupton` وغيرها — لم تُلمس هنا). **أوّل بند
للدفعة التالية:** `sch-cooley-looking-glass-self`.

---

## 1. التأسيس الكلاسيكي، علم العمران والرواد الأوائل (Classical & Foundational Sociology)

- [x] `sch-khaldunian-ilm-al-umran` — علم العمران البشري الخلدوني (Ibn Khaldun's Ilm al-Umran)
- [~] `sch-comtean-positivism` — الوضعية السوسيولوجية الكلاسيكية (Comtean Positivism)
- [~] `sch-spencerian-evolutionism` — التطورية الاجتماعية والعضوية (Spencerian Social Evolutionism & Organicism)
- [~] `sch-marxist-classical-sociology` — المادية التاريخية السوسيولوجية ونظرية الصراع الطبقي (Marxist Classical Sociology)
- [~] `sch-durkheimian-structural-functionalism` — البنائية الوظيفية الدوركهايمية (Durkheimian Structural Functionalism)
- [ ] `sch-durkheimian-sociology-of-religion` — سوسيولوجيا الدين والطقوس الجمعية الدوركهايمية (Durkheimian Sociology of Religion)
- [~] `sch-weberian-interpretive-sociology` — السوسيولوجيا الفهمية والتفسيرية الفيبرية (Weberian Interpretive Sociology / Verstehen)
- [ ] `sch-weberian-rationalization-bureaucracy` — سوسيولوجيا العقلنة والبيروقراطية (Sociology of Rationalization & Bureaucracy)
- [ ] `sch-weberian-religion-capitalism` — سوسيولوجيا الأخلاق الرأسمالية والدين (Weberian Sociology of Religion & Capitalism)
- [~] `sch-simmelian-formal-sociology` — السوسيولوجيا الصورية والشبكات الدقيقة (Simmelian Formal Sociology)
- [ ] `sch-simmelian-money-metropolis` — سوسيولوجيا الثقافة الحضرية والمالية (Simmelian Sociology of Money & Metropolis)
- [x] `sch-sumnerian-evolutionary-sociology` — الداروينية الاجتماعية والأعراف المجتمعية (Sumnerian Evolutionary Sociology)
- [x] `sch-classical-elite-theory` — نظرية النخبة السوسيولوجية الكلاسيكية (Classical Elite Theory: Pareto, Mosca, Michels)
- [~] `sch-martineau-feminist-sociology` — التأسيس النسوي والمنهجي المبكر (Martineau's Foundational Feminist Sociology) — لا `con-`/`wrk-` مستقل بعد
- [x] `sch-du-boisian-sociology` — السوسيولوجيا النقدية للأعراق والازدواجية الوجدانية (Du Boisian Sociology)
- [x] `sch-veblenian-institutional-sociology` — سوسيولوجيا الاستهلاك والمؤسسية التطورية (Veblenian Institutional Sociology)
- [x] `sch-tonnies-gemeinschaft-gesellschaft` — ثنائية المجتمع المحلي والمجتمع التعاقدي (Tönnies' Gemeinschaft und Gesellschaft)
- [x] `sch-tarde-lebon-crowd-theory` — سيكولوجيا الجماهير والتقليد الاجتماعي (Tarde & Le Bon's Crowd & Imitation Theory)
- [x] `sch-booth-rowntree-social-survey` — حركة المسوح الاجتماعية والفقر البريطانية (Booth & Rowntree's Social Survey Movement)

## 2. مدرسة شيكاغو، التفاعلية الرمزية وسوسيولوجيا الحياة اليومية (Chicago School & Symbolic Interactionism)

- [x] `sch-chicago-urban-ecology` — مدرسة شيكاغو الإيكولوجية الحضرية الأولى (First Chicago School / Urban Ecology)
- [x] `sch-wirthian-urbanism-ghetto` — سوسيولوجيا الحياة الحضرية والغيتو (Wirthian Urbanism & Ghetto Studies)
- [x] `sch-thomas-znaniecki-life-history` — منهج دراسات تاريخ الحياة والتعريف بالموقف (Thomas & Znaniecki's Life History & Situational Sociology)
- [x] `sch-whyte-participant-observation` — سوسيولوجيا الملاحظة بالمشاركة والمجتمعات الهامشية (Whyte's Participant Observation Sociology)
- [ ] `sch-cooley-looking-glass-self` — نظرية الذات المنعكسة في المرآة والجماعات الأولية (Cooley's Looking-Glass Self Theory)
- [ ] `sch-mead-social-behaviorism` — الأسس البراغماتية للتفاعلية الرمزية (Mead's Social Behaviorism & Mind/Self/Society)
- [ ] `sch-blumerian-symbolic-interactionism` — التفاعلية الرمزية المنهجية (Blumerian Symbolic Interactionism)
- [ ] `sch-goffman-dramaturgical` — النظرية الدراماتورجية وإدارة الانطباع (Goffman's Dramaturgical Sociology)
- [ ] `sch-goffman-total-institutions` — سوسيولوجيا المؤسسات الشاملة والمصحات (Goffman's Total Institutions Sociology)
- [ ] `sch-goffman-stigma` — سوسيولوجيا الوصمة والهوية المشوهة (Goffman's Sociology of Stigma)
- [ ] `sch-goffman-frame-analysis` — تحليل الأطر والنظام التفاعلي اليومي (Goffman's Frame Analysis & Interaction Order)
- [ ] `sch-becker-labeling-theory` — نظرية الوصم والانحراف كمسار مهني (Becker's Labelling Theory of Deviance)
- [ ] `sch-lemert-primary-secondary-deviance` — سوسيولوجيا الانحراف البنائية (Lemert's Primary & Secondary Deviance)
- [ ] `sch-sutherland-differential-association` — نظرية الارتباط التفاضلي وجرائم الياقات البيضاء (Sutherland's Differential Association Theory)
- [ ] `sch-hochschild-emotional-labor` — سوسيولوجيا الانفعالات والعمل العاطفي (Hochschild's Sociology of Emotions & Emotional Labor)
- [ ] `sch-hochschild-care-work` — سوسيولوجيا سلاسل الرعاية العالمية والوردية الثانية (Hochschild's Care Work Sociology)
- [ ] `sch-goffmanian-interaction-rituals` — طقوس التفاعل اليومي وحفظ ماء الوجه (Goffmanian Interaction Rituals & Face-Work)
- [ ] `sch-grounded-theory-school` — مدرسة النظرية المجذرة السوسيولوجية (Grounded Theory School: Glaser & Strauss)
- [ ] `sch-drake-cayton-black-metropolis` — دراسات المتروبوليس الأسود والتفاوت العرقي (Drake & Cayton's Black Metropolis School)
- [ ] `sch-stryker-burke-structural-interactionism` — التفاعلية الرمزية البنائية ونظرية الهوية (Stryker & Burke's Structural Interactionism)

## 3. الوظيفية البنائية، نظرية الأنساق ونظرية التبادل (Structural Functionalism, Systems & Exchange Theory)

- [ ] `sch-parsonian-action-frame` — نظرية الفعل الاجتماعي والتركيب البارسونزي (Parsonian Action Frame of Reference)
- [ ] `sch-parsonian-structural-functionalism-agil` — الوظيفية البنائية الشاملة ونموذج AGIL (Parsonian Structural Functionalism)
- [ ] `sch-parsonian-pattern-variables` — متغيرات النمط ونظرية التحديث (Parsonian Pattern Variables & Modernization Theory)
- [ ] `sch-mertonian-middle-range` — وظيفية المدى المتوسط والتحليل البنائي (Mertonian Middle-Range Functionalism)
- [ ] `sch-mertons-strain-theory` — نظرية التوتر والأنومي (Merton's Strain Theory of Deviance)
- [ ] `sch-reference-group-relative-deprivation` — نظرية الجماعات المرجعية والحرمان النسبي (Reference Group & Relative Deprivation Theory)
- [ ] `sch-mertonian-sociology-of-science` — سوسيولوجيا العلم والمؤسسة الأكاديمية (Mertonian Sociology of Science / CUDOS)
- [ ] `sch-neofunctionalism` — الوظيفية الجديدة والتركيب ما بعد البارسونزي (Neofunctionalism: Alexander & Colomy)
- [ ] `sch-luhmannian-autopoietic-systems` — نظرية الأنساق الاجتماعية الأوتوبويتية (Luhmannian Autopoietic Social Systems Theory)
- [ ] `sch-luhmannian-communication-differentiation` — سوسيولوجيا التواصل والتمايز النسقي (Luhmannian Sociology of Communication & Differentiation)
- [ ] `sch-homans-behavioral-exchange` — نظرية التبادل الاجتماعي السلوكية (Homans' Behavioral Social Exchange Theory)
- [ ] `sch-blau-structural-exchange` — نظرية التبادل البنائي والتفاوت الطبقي (Blau's Structural Exchange Theory)
- [ ] `sch-coleman-rational-choice-sociology` — سوسيولوجيا الاختيار العقلاني ورأس المال الاجتماعي (Coleman's Rational Choice Sociology)
- [ ] `sch-analytical-sociology` — السوسيولوجيا التحليلية ونظرية الآليات الاجتماعية (Analytical Sociology: Elster & Hedström)
- [ ] `sch-network-exchange-theory` — نظرية التبادل الشبكي وعلاقات القوة-التبعية (Network Exchange Theory: Willer & Cook)
- [ ] `sch-new-institutionalism-organizational` — المؤسسية الجديدة في سوسيولوجيا التنظيمات (New Institutionalism in Organizational Sociology: DiMaggio & Powell)
- [ ] `sch-social-capital-civic` — سوسيولوجيا رأس المال الاجتماعي والشبكات المدنية (Putnam's Social Capital Theory)
- [ ] `sch-complex-organizations-gouldner-blau` — سوسيولوجيا التنظيمات والخلل البيروقراطي (Sociology of Complex Organizations: Gouldner & Blau)
- [ ] `sch-social-network-analysis-paradigm` — سوسيولوجيا الشبكات الاجتماعية وتحليل البنى (Social Network Analysis Paradigm: Wellman & Granovetter)
- [ ] `sch-cumulative-advantage-theory` — سوسيولوجيا المكانة والتمايز الطبقي التراكمي (Cumulative Advantage Theory / Matthew Effect)

## 4. نظرية الصراع، مدرسة فرانكفورت والماركسية النقدية (Conflict Theory & Critical Sociology)

- [ ] `sch-dahrendorfian-conflict-sociology` — سوسيولوجيا الصراع الليبرالية (Dahrendorfian Conflict Sociology)
- [ ] `sch-millsian-power-elite` — السوسيولوجيا الراديكالية ونقد نخبة القوة (Millsian Critical Sociology & The Power Elite)
- [ ] `sch-collins-micro-conflict` — سوسيولوجيا الصراع المجهرية وسلاسل طقوس التفاعل (Collins' Micro-Conflict Sociology)
- [ ] `sch-wallerstein-world-systems` — تحليل النظم العالمية والتقسيم الدولي للعمل (Wallerstein's World-Systems Analysis)
- [ ] `sch-latin-american-dependency-theory` — نظرية التبعية السوسيولوجية اللاتينية (Latin American Dependency Theory: Cardoso, Dos Santos)
- [ ] `sch-frankfurt-critical-sociology` — النظرية النقدية الأولى والتسليع الثقافي (Frankfurt School Critical Sociology: Horkheimer & Adorno)
- [ ] `sch-marcusean-one-dimensionality` — سوسيولوجيا المجتمع الصناعي أحادي البعد (Marcusean Critical Sociology of One-Dimensionality)
- [ ] `sch-habermasian-public-sphere` — سوسيولوجيا المجال العام والديمقراطية التداولية (Habermasian Public Sphere Sociology)
- [ ] `sch-habermasian-communicative-action` — نظرية الفعل التواصلي واستعمار عالم الحياة (Habermasian Theory of Communicative Action)
- [ ] `sch-althusserian-structural-marxism` — الماركسية البنيوية وأجهزة الدولة (Althusserian Structural Marxism)
- [ ] `sch-gramscian-cultural-hegemony` — الهيمنة الثقافية والكتلة التاريخية (Gramscian Cultural Hegemony & Historical Bloc)
- [ ] `sch-laclau-mouffe-discourse-hegemony` — ما بعد الماركسية والتحليل الخطابي للصراع (Laclau & Mouffe's Discourse & Hegemony Theory)
- [ ] `sch-miliband-poulantzas-state-theory` — سوسيولوجيا الدولة الرأسمالية (Miliband-Poulantzas State Theory)
- [ ] `sch-wright-analytical-marxist-class` — التحليل الطبقي والمواقع المتناقضة (Wright's Analytical Marxist Class Theory)
- [ ] `sch-lefebvrean-spatial-sociology` — سوسيولوجيا الفضاء والحق في المدينة (Lefebvrean Spatial Sociology)
- [ ] `sch-harvey-critical-urban-spatial` — الجغرافيا الماركسية والتراكم المكاني (Harvey's Critical Urban & Spatial Sociology)
- [ ] `sch-braverman-labor-process` — سوسيولوجيا عملية العمل ونزع المهارة (Braverman's Labor Process Theory)
- [ ] `sch-honneth-fraser-recognition-redistribution` — سوسيولوجيا الاعتراف والعدالة التوزيعية (Honneth & Fraser's Recognition & Redistribution Theory)
- [ ] `sch-skocpol-comparative-historical-revolutions` — علم الاجتماع التاريخي والمقارن للثورات (Skocpol's Comparative-Historical Sociology of Revolutions)
- [ ] `sch-tilly-tarrow-contentious-politics` — سوسيولوجيا الحركات الاجتماعية وعمليات التعبئة (Tilly & Tarrow's Contentious Politics & Social Movements)

## 5. الظاهراتية، الإثنوميثودولوجيا، نظرية الممارسة وما بعد البنيوية (Phenomenological, Practice & Post-Structuralist)

- [x] `sch-schutzian-phenomenological-sociology` — الفينومينولوجيا السوسيولوجية وعالم الحياة المعاش (Schutzian Phenomenological Sociology)
- [x] `sch-berger-luckmann-social-construction` — البنائية الاجتماعية للواقع (Berger & Luckmann's Social Constructionism)
- [x] `sch-garfinkelian-ethnomethodology` — الإثنوميثودولوجيا والتفكير العملي العادي (Garfinkelian Ethnomethodology)
- [x] `sch-conversation-analysis` — تحليل المحادثة والتنظيم التفاعلي الصوري (Conversation Analysis: Sacks & Schegloff)
- [x] `sch-bourdieu-practice-habitus` — نظرية الممارسة والهابيتوس (Bourdieu's Theory of Practice & Habitus)
- [x] `sch-bourdieu-field-capital` — سوسيولوجيا الحقول وأشكال رأس المال (Bourdieu's Field Theory & Forms of Capital)
- [x] `sch-bourdieu-distinction-cultural-reproduction` — سوسيولوجيا التمايز وإعادة الإنتاج الثقافي (Bourdieu's Distinction & Cultural Reproduction)
- [x] `sch-foucauldian-disciplinary-power` — سوسيولوجيا السلطة الانضباطية والمراقبة (Foucauldian Disciplinary Power & Surveillance)
- [x] `sch-foucauldian-biopolitics-governmentality` — سوسيولوجيا السياسة الحيوية والحكومية (Foucauldian Biopolitics & Governmentality)
- [x] `sch-foucauldian-power-knowledge-discourse` — سوسيولوجيا المعرفة-السلطة والتشكيلات الخطابية (Foucauldian Power/Knowledge & Discourse)
- [x] `sch-baudrillardian-hyperreality` — سوسيولوجيا المحاكاة والمجتمع الاستهلاكي الفائق (Baudrillardian Hyperreality & Simulation)
- [x] `sch-deleuzian-assemblage-sociology` — سوسيولوجيا التجميع والإنتاج الاجتماعي (Deleuzian Assemblage Sociology)
- [x] `sch-latour-callon-actor-network-theory` — نظرية شبكة الفواعل وسوسيولوجيا الترجمة (Latour & Callon's Actor-Network Theory - ANT)
- [x] `sch-boltanski-thevenot-sociology-of-worth` — سوسيولوجيا التبرير ونماذج الجدارة (Boltanski & Thévenot's Sociology of Worth / Pragmatic Sociology)
- [x] `sch-boltanski-chiapello-capitalist-spirit` — سوسيولوجيا نقد الرأسمالية الشبكية (Boltanski & Chiapello's Sociology of Capitalist Spirit)
- [x] `sch-douglas-johnson-existential-sociology` — السوسيولوجيا الوجودية والخبرة المعيشة (Douglas & Johnson's Existential Sociology)
- [x] `sch-narrative-hermeneutic-sociology` — السوسيولوجيا التأويلية والسردية (Narrative & Hermeneutic Sociology)
- [x] `sch-visual-sociology-sensory-ethnography` — السوسيولوجيا البصرية والإثنوغرافيا الحسية (Visual Sociology & Sensory Ethnography)
- [x] `sch-contemporary-relational-sociology` — السوسيولوجيا العلائقية المعاصرة (Contemporary Relational Sociology: Emirbayer & Dépelteau)
- [x] `sch-archerian-critical-realist-sociology` — الواقعية النقدية السوسيولوجية ونظرية المورفوجينيسيس (Archerian Critical Realist Sociology)

## 6. النظريات السوسيولوجية المعاصرة، العولمة والمجتمع الرقمي (Contemporary, Globalization & Digital Sociology)

- [x] `sch-giddens-structuration-theory` — نظرية الهيكلة وازدواجية البنية (Giddens' Structuration Theory)
- [x] `sch-giddens-reflexive-modernity` — سوسيولوجيا الحداثة الفائقة والانعكاسية (Giddens' Reflexive Modernity & Self-Identity)
- [x] `sch-beck-risk-society-theory` — نظرية مجتمع المخاطرة والحداثة الثانية (Beck's Risk Society Theory)
- [x] `sch-beck-cosmopolitan-sociology` — سوسيولوجيا الكوزموبوليتية والمخاطر العالمية (Beck's Cosmopolitan Sociology & World at Risk)
- [x] `sch-bauman-liquid-modernity` — سوسيولوجيا الحداثة السائلة (Bauman's Liquid Modernity Paradigm)
- [x] `sch-bauman-postmodern-ethics-waste` — سوسيولوجيا الأخلاق في عصر الحداثة وما بعد الهولوكوست (Bauman's Postmodern Ethics & Waste Sociology)
- [x] `sch-castells-network-society` — سوسيولوجيا مجتمع الشبكات والمعلومات (Castells' Network Society Theory)
- [x] `sch-castells-communication-power` — سوسيولوجيا سلطة الاتصال والحركات الرقمية (Castells' Communication Power Sociology)
- [x] `sch-sassen-global-city` — سوسيولوجيا المدينة العالمية وتدفقات رأس المال (Sassen's Global City & Expulsions Theory)
- [x] `sch-appadurai-robertson-global-culture` — سوسيولوجيا العولمة الثقافية والمشاهد العولمية (Appadurai & Robertson's Global Culture & Scapes)
- [ ] `sch-zuboff-surveillance-capitalism` — سوسيولوجيا رأسمالية المراقبة (Zuboff's Surveillance Capitalism Sociology)
- [ ] `sch-srnicek-platform-capitalism` — سوسيولوجيا رأسمالية المنصات واقتصاد العمل الحر (Srnicek's Platform Capitalism Sociology)
- [ ] `sch-lupton-digital-sociology` — السوسيولوجيا الرقمية وحكومية البيانات (Lupton's Digital Sociology & Metric Power)
- [ ] `sch-rosa-social-acceleration` — نظرية التسارع الاجتماعي وتغير الإيقاع الزمني (Rosa's Social Acceleration & Resonance Theory)
- [ ] `sch-environmental-sociology-metabolic-rift` — السوسيولوجيا البيئية ونظرية الصدع الأيضي (Environmental Sociology & Metabolic Rift: Foster & Schnaiberg)
- [ ] `sch-medicalization-biosociality` — سوسيولوجيا التطبيب والهندسة الحيوية الاجتماعية (Sociology of Medicalization & Biosociality: Conrad & Rose)
- [ ] `sch-scott-everyday-peasant-resistance` — سوسيولوجيا المقاومة اليومية والنصوص الخفية (Scott's Everyday Peasant Resistance Sociology)
- [ ] `sch-burawoy-public-sociology` — علم الاجتماع العام وأنماط الممارسة الأربعة (Burawoy's Public Sociology Paradigm)
- [ ] `sch-sociology-of-body-embodiment` — سوسيولوجيا الجسد والتجسيد الاجتماعي (Sociology of the Body & Embodiment: Shilling & Turner)
- [ ] `sch-computational-sociology-big-data` — السوسيولوجيا الحوسبية وتحليل الآثار الرقمية (Computational Sociology & Big Data Analysis)

## 7. السوسيولوجيا النسوية، دراسات الجندر، ما بعد الاستعمار والجنوب العالمي (Feminist, Decolonial & Global South)

- [ ] `sch-dorothy-smith-standpoint-theory` — نظرية الموقف النسوي في علم الاجتماع (Feminist Standpoint Theory: Dorothy Smith)
- [ ] `sch-dorothy-smith-institutional-ethnography` — الإثنوغرافيا المؤسسية (Institutional Ethnography: Dorothy Smith)
- [ ] `sch-hill-collins-black-feminist-sociology` — الفكر النسوي الأسود ومصفوفة الهيمنة (Black Feminist Sociology: Patricia Hill Collins)
- [ ] `sch-sociological-intersectionality` — النظرية التقاطعية السوسيولوجية (Sociological Intersectionality: Crenshaw & Collins)
- [ ] `sch-bell-hooks-critical-feminist-sociology` — النسوية النقدية ومناهضة النظام الأبوي الإمبريالي (bell hooks' Critical Feminist Sociology)
- [ ] `sch-butler-gender-performativity` — سوسيولوجيا الأداء الجندري وتفكيك الثنائية (Butler's Gender Performativity Sociology)
- [ ] `sch-oakley-housework-reproduction` — سوسيولوجيا العمل المنزلي وإعادة الإنتاج الجندري (Oakley's Sociology of Housework & Reproduction)
- [ ] `sch-fraser-social-reproduction-crisis-of-care` — سوسيولوجيا أزمة الرعاية والعدالة الرأسمالية (Fraser's Social Reproduction & Crisis of Care)
- [ ] `sch-quijano-coloniality-of-power` — سوسيولوجيا استعمارية السلطة والمركزية الأوروبية (Quijano's Coloniality of Power Sociology)
- [ ] `sch-santos-epistemologies-of-the-south` — إبستمولوجيات الجنوب وسوسيولوجيا الغيابات (Santos' Epistemologies of the South & Cognitive Justice)
- [ ] `sch-said-sociology-of-orientalism` — النقد السوسيولوجي للاستشراق والتمثيل الإمبريالي (Said's Sociology of Orientalism & Knowledge)
- [ ] `sch-fanonian-liberation-sociology` — علم الاجتماع التحرري ومناهضة الاستعمار (Fanonian Liberation Sociology & Sociogeny)
- [ ] `sch-alatas-captive-mind-sociology` — سوسيولوجيا العقل الأسير والتبعية الأكاديمية الآسيوية (Alatas' Captive Mind Sociology)
- [ ] `sch-subaltern-studies-guha-spivak` — دراسات التابع والتأريخ السوسيولوجي من أسفل (Subaltern Studies: Guha & Spivak)
- [ ] `sch-khaldunian-historical-sociology` — سوسيولوجيا العمران والتحول البدوي-الحضري الخلدونية (Khaldunian Historical Sociology)
- [ ] `sch-alwardi-iraqi-arab-sociology` — سوسيولوجيا الشخصية الازدواجية وصراع القيم العربي (Al-Wardi's Iraqi & Arab Sociology)
- [ ] `sch-sharabi-neopatriarchy-sociology` — سوسيولوجيا البطريركية المستحدثة والتغير المشوه (Sharabi's Neopatriarchy Sociology)
- [ ] `sch-contemporary-arab-sociology` — سوسيولوجيا المجتمع الفسيفسائي والاغتراب العربي (Barakat's Contemporary Arab Society Sociology)
- [ ] `sch-elsaadawi-arab-feminist-sociology` — السوسيولوجيا النسوية العربية ونقد الهيمنة البطريركية (El Saadawi's Arab Feminist Sociology)
- [ ] `sch-laroui-shariati-critical-arab-islamic-sociology` — التاريخانية والسوسيولوجيا النقدية العربية والإسلامية (Laroui & Shariati's Critical Arab/Islamic Sociology)

## 8. الميادين والفروع التخصصية في علم الاجتماع (Specialized Sociological Subdisciplines)

- [ ] `sch-sociology-of-scientific-knowledge` — سوسيولوجيا المعرفة والعلوم (Sociology of Knowledge & Scientific Knowledge - SSK)
- [ ] `sch-sociology-of-culture-lifestyles` — سوسيولوجيا الثقافة وأنماط الحياة (Sociology of Culture & Lifestyles)
- [ ] `sch-sociology-of-religion-post-secularism` — سوسيولوجيا الدين والتحولات العلمانية (Sociology of Religion & Post-Secularism)
- [ ] `sch-sociology-of-deviance-crime-justice` — سوسيولوجيا الانحراف والجريمة والعدالة الجنائية (Sociology of Deviance, Crime & Justice)
- [ ] `sch-medical-health-clinical-sociology` — السوسيولوجيا الطبية والصحية والسريرية (Medical, Health & Clinical Sociology)
- [ ] `sch-urban-sociology-spatial-planning` — السوسيولوجيا الحضرية وتخطيط المدن (Urban Sociology & Urban Spatial Planning)
- [ ] `sch-rural-agrarian-sociology` — السوسيولوجيا الريفية والمجتمعات الزراعية (Rural & Agrarian Sociology)
- [ ] `sch-environmental-sociology-sustainability` — السوسيولوجيا البيئية والتنمية المستدامة (Environmental Sociology & Sustainability)
- [ ] `sch-economic-sociology-embeddedness` — السوسيولوجيا الاقتصادية وتجذر الأسواق (Economic Sociology & Embeddedness: Polanyi & Granovetter)
- [ ] `sch-sociology-of-work-occupations` — سوسيولوجيا العمل والمهن والتصنيع (Sociology of Work, Occupations & Industrial Relations)
- [ ] `sch-political-sociology-state-citizenship` — السوسيولوجيا السياسية والدولة والمواطنة (Political Sociology, State & Citizenship)
- [ ] `sch-sociology-of-education-cultural-capital` — سوسيولوجيا التربية والتعليم وإعادة الإنتاج (Sociology of Education & Cultural Capital)
- [ ] `sch-sociology-of-family-gender-intimacy` — سوسيولوجيا الأسرة والنوع الاجتماعي والعلاقات الحميمية (Sociology of Family, Gender & Intimacy)
- [ ] `sch-sociology-of-migration-diaspora` — سوسيولوجيا الهجرة واللجوء والشتات (Sociology of Migration, Asylum & Diaspora)
- [ ] `sch-sociology-of-aging-life-course` — سوسيولوجيا الشيخوخة ودورة الحياة (Sociology of Aging & Life Course)
- [ ] `sch-sociology-of-youth-subcultures` — سوسيولوجيا الشباب والثقافات الفرعية (Sociology of Youth & Subcultures)
- [ ] `sch-sociology-of-art-literature-aesthetics` — سوسيولوجيا الفن والأدب والجماليات (Sociology of Art, Literature & Aesthetics)
- [ ] `sch-sociology-of-law-social-control` — سوسيولوجيا القانون والضبط الاجتماعي (Sociology of Law & Social Control)
- [ ] `sch-sociology-of-social-movements-collective-action` — سوسيولوجيا الحركات الاجتماعية والعمل الجماعي (Sociology of Social Movements & Collective Action)
- [ ] `sch-military-sociology-armed-conflict` — السوسيولوجيا العسكرية والنزاعات المسلحة (Military Sociology & Armed Conflict)
