> **موضعُ التوقّف/الاستئناف (2026-09-14):**
> - **الدفعة 0:** تضييق شرط `build_sociology_matrix.py` إلى `part == "sociology"`، وسدّ يُتم
>   العقد الثلاث القديمة (`sch-contemporary-arab-sociology`، `sch-social-capital-civic`،
>   `sch-conversation-analysis`).
> - **الدفعة 1:** القسم 1 مكتملٌ بالكامل (19/19) — كونت، سبنسر، ماركس، دوركهايم (+فرع)،
>   فيبر (+فرعان)، ابن خلدون، زيمل (+فرع)، سمنر، نظرية النخبة، مارتينو، دوبوا، فيبلن،
>   تونيس، تارد ولوبون، بوث وراونتري.
> - **الدفعة 2 (2026-09-14):** القسم 2 مكتملٌ بالكامل (20/20) — شيكاغو الإيكولوجية (+3 فروع:
>   ورث، توماس/زنانييكي، وايت)، كولي، ميد (+فرعان: بلومر، ستريكر/بيرك)، غوفمان الدراماتورجية
>   (+4 فروع: المؤسسات الشاملة، الوصمة، تحليل الأطر، طقوس التفاعل)، بيكر، ليمرت، ساذرلاند،
>   هوكشيلد (+فرع الرعاية العالمية)، النظرية المجذرة، دريك وكايتون (المتروبوليس الأسود).
> - **قاعدة معمارية ثابتة عبر كل الدفعات:** كل مدرسة أمّ (لا مدرسة أب لها في المستودع) تُترك
>   `belongs_to` فيها فارغاً صراحة مع توثيق السبب في `gaps`، لا يُختلق أبٌ. حيث وُجد مفكرٌ بنفس
>   الاسم في قسمٍ آخر (فلسفة/نفس) بـ`part` مختلف، الربط يكون عبر `related` فقط لا `belongs_to`
>   (يشترط تطابق `part`، فحصٌ قاطعٌ [12] في `audit_atlas.py`). كل عزلةٍ ظهرت بعد كل جزء (مدرسة
>   فرعية بلا إشارة واردة) أُصلحت بإضافة `related` حقيقي من الأمّ أو من مدرسةٍ شقيقة، لا بعلاقة
>   مختلَقة. `audit_atlas.py` عاد إلى صفرٍ بعد كل جزءٍ من كل دفعة دون استثناء.
> **الدفعةُ التالية (3):** القسم 3 — الوظيفية البنائية ونظرية الأنساق والتبادل — أوّل بندٍ
> غيرِ مؤشَّرٍ بـ`[x]` تحت العنوان `## 3.`.

# قائمة المدارس والنظريات السوسيولوجية الشاملة — قائمة انتظار (Backlog) لتغطية علم الاجتماع في أطلس

هذا الملف هو **مصدر الحقيقة المرجعي الوحيد** لتتبّع التقدّم في تغطية مدارس/تيارات/بارادايمات **علم الاجتماع (Sociology)** عالمياً،
من التأسيسات الكلاسيكية وحتى أحدث النظريات المعاصرة والسوسيولوجيا الرقمية — موازٍ لملفي `schools-backlog.md` (علم النفس)
و `philosophy-schools-backlog.md` (الفلسفة). تم تجميعه بدمج وتنسيق كبرى المرجعيات الأكاديمية السوسيولوجية العالمية
(الجمعية السوسيولوجية الدولية ISA، الجمعية الأمريكية ASA، المدارس الأوروبية، العربية، والجنوب العالمي).

## كيفية الاستخدام (لأي وكيل أو باحث):
- كل سطر `- [ ]` = مدرسة / تيار / بارادايم سوسيولوجي مستهدف كملف `schools/` (`sch-`).
- كل سطر `- [x]` = مكتمل ومعتمد في الأطلس.
- كل سطر `- [~]` = قيد العمل والمسودة في `content/ar/drafts/`.
- جميع المسودات الناتجة تحمل الوسم المعياري: `part: "sociology"`.
- كل مدرسة/تيار يكتب له ملف تمثيلي في `schools/` أو `branches/` مع حزمته المترابطة (مفكرون `thk-`، مفاهيم `con-`، أعمال `wrk-`، دراسات `stu-`، أدوات `ins-`، تقنيات `tec-`، جدالات `dbt-`).

---

## 1. التأسيس الكلاسيكي، علم العمران والرواد الأوائل (Classical & Foundational Sociology)

- [x] علم العمران البشري الخلدوني (Ibn Khaldun's Ilm al-Umran) — `sch-khaldunian-ilm-al-umran` (دفعة 1، 2026-09-14)
- [x] الوضعية السوسيولوجية الكلاسيكية (Comtean Positivism) — `sch-comtean-positivism` (دفعة 1، 2026-09-14)
- [x] التطورية الاجتماعية والعضوية (Spencerian Social Evolutionism & Organicism) — `sch-spencerian-evolutionism` (دفعة 1، 2026-09-14)
- [x] المادية التاريخية السوسيولوجية ونظرية الصراع الطبقي (Marxist Classical Sociology) — `sch-marxist-classical-sociology` (دفعة 1، 2026-09-14)
- [x] البنائية الوظيفية الدوركهايمية (Durkheimian Structural Functionalism) — `sch-durkheimian-structural-functionalism` (دفعة 1، 2026-09-14)
- [x] سوسيولوجيا الدين والطقوس الجمعية الدوركهايمية (Durkheimian Sociology of Religion) — `sch-durkheimian-sociology-of-religion` (دفعة 1، 2026-09-14)
- [x] السوسيولوجيا الفهمية والتفسيرية الفيبرية (Weberian Interpretive Sociology / Verstehen) — `sch-weberian-interpretive-sociology` (دفعة 1، 2026-09-14)
- [x] سوسيولوجيا العقلنة والبيروقراطية (Sociology of Rationalization & Bureaucracy) — `sch-weberian-rationalization-bureaucracy` (دفعة 1، 2026-09-14)
- [x] سوسيولوجيا الأخلاق الرأسمالية والدين (Weberian Sociology of Religion & Capitalism) — `sch-weberian-religion-capitalism` (دفعة 1، 2026-09-14)
- [x] السوسيولوجيا الصورية والشبكات الدقيقة (Simmelian Formal Sociology) — `sch-simmelian-formal-sociology` (دفعة 1، 2026-09-14)
- [x] سوسيولوجيا الثقافة الحضرية والمالية (Simmelian Sociology of Money & Metropolis) — `sch-simmelian-money-metropolis` (دفعة 1، 2026-09-14)
- [x] الداروينية الاجتماعية والأعراف المجتمعية (Sumnerian Evolutionary Sociology) — `sch-sumnerian-evolutionary-sociology` (دفعة 1، 2026-09-14)
- [x] نظرية النخبة السوسيولوجية الكلاسيكية (Classical Elite Theory: Pareto, Mosca, Michels) — `sch-classical-elite-theory` (دفعة 1، 2026-09-14)
- [x] التأسيس النسوي والمنهجي المبكر (Martineau's Foundational Feminist Sociology) — `sch-martineau-feminist-sociology` (دفعة 1، 2026-09-14)
- [x] السوسيولوجيا النقدية للأعراق والازدواجية الوجدانية (Du Boisian Sociology) — `sch-du-boisian-sociology` (دفعة 1، 2026-09-14)
- [x] سوسيولوجيا الاستهلاك والمؤسسية التطورية (Veblenian Institutional Sociology) — `sch-veblenian-institutional-sociology` (دفعة 1، 2026-09-14)
- [x] ثنائية المجتمع المحلي والمجتمع التعاقدي (Tönnies' Gemeinschaft und Gesellschaft) — `sch-tonnies-gemeinschaft-gesellschaft` (دفعة 1، 2026-09-14)
- [x] سيكولوجيا الجماهير والتقليد الاجتماعي (Tarde & Le Bon's Crowd & Imitation Theory) — `sch-tarde-lebon-crowd-theory` (دفعة 1، 2026-09-14)
- [x] حركة المسوح الاجتماعية والفقر البريطانية (Booth & Rowntree's Social Survey Movement) — `sch-booth-rowntree-social-survey` (دفعة 1، 2026-09-14)

---

## 2. مدرسة شيكاغو، التفاعلية الرمزية وسوسيولوجيا الحياة اليومية (Chicago School & Symbolic Interactionism)

- [x] مدرسة شيكاغو الإيكولوجية الحضرية الأولى (First Chicago School / Urban Ecology) — `sch-chicago-urban-ecology` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا الحياة الحضرية والغيتو (Wirthian Urbanism & Ghetto Studies) — `sch-wirthian-urbanism-ghetto` (دفعة 2، 2026-09-14)
- [x] منهج دراسات تاريخ الحياة والتعريف بالموقف (Thomas & Znaniecki's Life History & Situational Sociology) — `sch-thomas-znaniecki-life-history` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا الملاحظة بالمشاركة والمجتمعات الهامشية (Whyte's Participant Observation Sociology) — `sch-whyte-participant-observation` (دفعة 2، 2026-09-14)
- [x] نظرية الذات المنعكسة في المرآة والجماعات الأولية (Cooley's Looking-Glass Self Theory) — `sch-cooley-looking-glass-self` (دفعة 2، 2026-09-14)
- [x] الأسس البراغماتية للتفاعلية الرمزية (Mead's Social Behaviorism & Mind/Self/Society) — `sch-mead-social-behaviorism` (دفعة 2، 2026-09-14)
- [x] التفاعلية الرمزية المنهجية (Blumerian Symbolic Interactionism) — `sch-blumerian-symbolic-interactionism` (دفعة 2، 2026-09-14)
- [x] النظرية الدراماتورجية وإدارة الانطباع (Goffman's Dramaturgical Sociology) — `sch-goffman-dramaturgical` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا المؤسسات الشاملة والمصحات (Goffman's Total Institutions Sociology) — `sch-goffman-total-institutions` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا الوصمة والهوية المشوهة (Goffman's Sociology of Stigma) — `sch-goffman-stigma` (دفعة 2، 2026-09-14)
- [x] تحليل الأطر والنظام التفاعلي اليومي (Goffman's Frame Analysis & Interaction Order) — `sch-goffman-frame-analysis` (دفعة 2، 2026-09-14)
- [x] نظرية الوصم والانحراف كمسار مهني (Becker's Labelling Theory of Deviance) — `sch-becker-labeling-theory` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا الانحراف البنائية (Lemert's Primary & Secondary Deviance) — `sch-lemert-primary-secondary-deviance` (دفعة 2، 2026-09-14)
- [x] نظرية الارتباط التفاضلي وجرائم الياقات البيضاء (Sutherland's Differential Association Theory) — `sch-sutherland-differential-association` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا الانفعالات والعمل العاطفي (Hochschild's Sociology of Emotions & Emotional Labor) — `sch-hochschild-emotional-labor` (دفعة 2، 2026-09-14)
- [x] سوسيولوجيا سلاسل الرعاية العالمية والوردية الثانية (Hochschild's Care Work Sociology) — `sch-hochschild-care-work` (دفعة 2، 2026-09-14)
- [x] طقوس التفاعل اليومي وحفظ ماء الوجه (Goffmanian Interaction Rituals & Face-Work) — `sch-goffmanian-interaction-rituals` (دفعة 2، 2026-09-14)
- [x] مدرسة النظرية المجذرة السوسيولوجية (Grounded Theory School: Glaser & Strauss) — `sch-grounded-theory-school` (دفعة 2، 2026-09-14)
- [x] دراسات المتروبوليس الأسود والتفاوت العرقي (Drake & Cayton's Black Metropolis School) — `sch-drake-cayton-black-metropolis` (دفعة 2، 2026-09-14)
- [x] التفاعلية الرمزية البنائية ونظرية الهوية (Stryker & Burke's Structural Interactionism) — `sch-stryker-burke-structural-interactionism` (دفعة 2، 2026-09-14)

---

## 3. الوظيفية البنائية، نظرية الأنساق ونظرية التبادل (Structural Functionalism, Systems & Exchange Theory)

- [ ] نظرية الفعل الاجتماعي والتركيب البارسونزي (Parsonian Action Frame of Reference)
- [ ] الوظيفية البنائية الشاملة ونموذج AGIL (Parsonian Structural Functionalism)
- [ ] متغيرات النمط ونظرية التحديث (Parsonian Pattern Variables & Modernization Theory)
- [ ] وظيفية المدى المتوسط والتحليل البنائي (Mertonian Middle-Range Functionalism)
- [ ] نظرية التوتر والأنومي (Merton's Strain Theory of Deviance)
- [ ] نظرية الجماعات المرجعية والحرمان النسبي (Reference Group & Relative Deprivation Theory)
- [ ] سوسيولوجيا العلم والمؤسسة الأكاديمية (Mertonian Sociology of Science / CUDOS)
- [ ] الوظيفية الجديدة والتركيب ما بعد البارسونزي (Neofunctionalism: Alexander & Colomy)
- [ ] نظرية الأنساق الاجتماعية الأوتوبويتية (Luhmannian Autopoietic Social Systems Theory)
- [ ] سوسيولوجيا التواصل والتمايز النسقي (Luhmannian Sociology of Communication & Differentiation)
- [ ] نظرية التبادل الاجتماعي السلوكية (Homans' Behavioral Social Exchange Theory)
- [ ] نظرية التبادل البنائي والتفاوت الطبقي (Blau's Structural Exchange Theory)
- [ ] سوسيولوجيا الاختيار العقلاني ورأس المال الاجتماعي (Coleman's Rational Choice Sociology)
- [ ] السوسيولوجيا التحليلية ونظرية الآليات الاجتماعية (Analytical Sociology: Elster & Hedström)
- [ ] نظرية التبادل الشبكي وعلاقات القوة-التبعية (Network Exchange Theory: Willer & Cook)
- [ ] المؤسسية الجديدة في سوسيولوجيا التنظيمات (New Institutionalism in Organizational Sociology: DiMaggio & Powell)
- [x] سوسيولوجيا رأس المال الاجتماعي والشبكات المدنية (Putnam's Social Capital Theory) — `sch-social-capital-civic` (دفعة 0، 2026-09-14)
- [ ] سوسيولوجيا التنظيمات والخلل البيروقراطي (Sociology of Complex Organizations: Gouldner & Blau)
- [ ] سوسيولوجيا الشبكات الاجتماعية وتحليل البنى (Social Network Analysis Paradigm: Wellman & Granovetter)
- [ ] سوسيولوجيا المكانة والتمايز الطبقي التراكمي (Cumulative Advantage Theory / Matthew Effect)

---

## 4. نظرية الصراع، مدرسة فرانكفورت والماركسية النقدية (Conflict Theory & Critical Sociology)

- [ ] سوسيولوجيا الصراع الليبرالية (Dahrendorfian Conflict Sociology)
- [ ] السوسيولوجيا الراديكالية ونقد نخبة القوة (Millsian Critical Sociology & The Power Elite)
- [ ] سوسيولوجيا الصراع المجهرية وسلاسل طقوس التفاعل (Collins' Micro-Conflict Sociology)
- [ ] تحليل النظم العالمية والتقسيم الدولي للعمل (Wallerstein's World-Systems Analysis)
- [ ] نظرية التبعية السوسيولوجية اللاتينية (Latin American Dependency Theory: Cardoso, Dos Santos)
- [ ] النظرية النقدية الأولى والتسليع الثقافي (Frankfurt School Critical Sociology: Horkheimer & Adorno)
- [ ] سوسيولوجيا المجتمع الصناعي أحادي البعد (Marcusean Critical Sociology of One-Dimensionality)
- [ ] سوسيولوجيا المجال العام والديمقراطية التداولية (Habermasian Public Sphere Sociology)
- [ ] نظرية الفعل التواصلي واستعمار عالم الحياة (Habermasian Theory of Communicative Action)
- [ ] الماركسية البنيوية وأجهزة الدولة (Althusserian Structural Marxism)
- [ ] الهيمنة الثقافية والكتلة التاريخية (Gramscian Cultural Hegemony & Historical Bloc)
- [ ] ما بعد الماركسية والتحليل الخطابي للصراع (Laclau & Mouffe's Discourse & Hegemony Theory)
- [ ] سوسيولوجيا الدولة الرأسمالية (Miliband-Poulantzas State Theory)
- [ ] التحليل الطبقي والمواقع المتناقضة (Wright's Analytical Marxist Class Theory)
- [ ] سوسيولوجيا الفضاء والحق في المدينة (Lefebvrean Spatial Sociology)
- [ ] الجغرافيا الماركسية والتراكم المكاني (Harvey's Critical Urban & Spatial Sociology)
- [ ] سوسيولوجيا عملية العمل ونزع المهارة (Braverman's Labor Process Theory)
- [ ] سوسيولوجيا الاعتراف والعدالة التوزيعية (Honneth & Fraser's Recognition & Redistribution Theory)
- [ ] علم الاجتماع التاريخي والمقارن للثورات (Skocpol's Comparative-Historical Sociology of Revolutions)
- [ ] سوسيولوجيا الحركات الاجتماعية وعمليات التعبئة (Tilly & Tarrow's Contentious Politics & Social Movements)

---

## 5. الظاهراتية، الإثنوميثودولوجيا، نظرية الممارسة وما بعد البنيوية (Phenomenological, Practice & Post-Structuralist)

- [ ] الفينومينولوجيا السوسيولوجية وعالم الحياة المعاش (Schutzian Phenomenological Sociology)
- [ ] البنائية الاجتماعية للواقع (Berger & Luckmann's Social Constructionism)
- [ ] الإثنوميثودولوجيا والتفكير العملي العادي (Garfinkelian Ethnomethodology)
- [x] تحليل المحادثة والتنظيم التفاعلي الصوري (Conversation Analysis: Sacks & Schegloff) — `sch-conversation-analysis` (دفعة 0، 2026-09-14)
- [ ] نظرية الممارسة والهابيتوس (Bourdieu's Theory of Practice & Habitus)
- [ ] سوسيولوجيا الحقول وأشكال رأس المال (Bourdieu's Field Theory & Forms of Capital)
- [ ] سوسيولوجيا التمايز وإعادة الإنتاج الثقافي (Bourdieu's Distinction & Cultural Reproduction)
- [ ] سوسيولوجيا السلطة الانضباطية والمراقبة (Foucauldian Disciplinary Power & Surveillance)
- [ ] سوسيولوجيا السياسة الحيوية والحكومية (Foucauldian Biopolitics & Governmentality)
- [ ] سوسيولوجيا المعرفة-السلطة والتشكيلات الخطابية (Foucauldian Power/Knowledge & Discourse)
- [ ] سوسيولوجيا المحاكاة والمجتمع الاستهلاكي الفائق (Baudrillardian Hyperreality & Simulation)
- [ ] سوسيولوجيا التجميع والإنتاج الاجتماعي (Deleuzian Assemblage Sociology)
- [ ] نظرية شبكة الفواعل وسوسيولوجيا الترجمة (Latour & Callon's Actor-Network Theory - ANT)
- [ ] سوسيولوجيا التبرير ونماذج الجدارة (Boltanski & Thévenot's Sociology of Worth / Pragmatic Sociology)
- [ ] سوسيولوجيا نقد الرأسمالية الشبكية (Boltanski & Chiapello's Sociology of Capitalist Spirit)
- [ ] السوسيولوجيا الوجودية والخبرة المعيشة (Douglas & Johnson's Existential Sociology)
- [ ] السوسيولوجيا التأويلية والسردية (Narrative & Hermeneutic Sociology)
- [ ] السوسيولوجيا البصرية والإثنوغرافيا الحسية (Visual Sociology & Sensory Ethnography)
- [ ] السوسيولوجيا العلائقية المعاصرة (Contemporary Relational Sociology: Emirbayer & Dépelteau)
- [ ] الواقعية النقدية السوسيولوجية ونظرية المورفوجينيسيس (Archerian Critical Realist Sociology)

---

## 6. النظريات السوسيولوجية المعاصرة، العولمة والمجتمع الرقمي (Contemporary, Globalization & Digital Sociology)

- [ ] نظرية الهيكلة وازدواجية البنية (Giddens' Structuration Theory)
- [ ] سوسيولوجيا الحداثة الفائقة والانعكاسية (Giddens' Reflexive Modernity & Self-Identity)
- [ ] نظرية مجتمع المخاطرة والحداثة الثانية (Beck's Risk Society Theory)
- [ ] سوسيولوجيا الكوزموبوليتية والمخاطر العالمية (Beck's Cosmopolitan Sociology & World at Risk)
- [ ] سوسيولوجيا الحداثة السائلة (Bauman's Liquid Modernity Paradigm)
- [ ] سوسيولوجيا الأخلاق في عصر الحداثة وما بعد الهولوكوست (Bauman's Postmodern Ethics & Waste Sociology)
- [ ] سوسيولوجيا مجتمع الشبكات والمعلومات (Castells' Network Society Theory)
- [ ] سوسيولوجيا سلطة الاتصال والحركات الرقمية (Castells' Communication Power Sociology)
- [ ] سوسيولوجيا المدينة العالمية وتدفقات رأس المال (Sassen's Global City & Expulsions Theory)
- [ ] سوسيولوجيا العولمة الثقافية والمشاهد العولمية (Appadurai & Robertson's Global Culture & Scapes)
- [ ] سوسيولوجيا رأسمالية المراقبة (Zuboff's Surveillance Capitalism Sociology)
- [ ] سوسيولوجيا رأسمالية المنصات واقتصاد العمل الحر (Srnicek's Platform Capitalism Sociology)
- [ ] السوسيولوجيا الرقمية وحكومية البيانات (Lupton's Digital Sociology & Metric Power)
- [ ] نظرية التسارع الاجتماعي وتغير الإيقاع الزمني (Rosa's Social Acceleration & Resonance Theory)
- [ ] السوسيولوجيا البيئية ونظرية الصدع الأيضي (Environmental Sociology & Metabolic Rift: Foster & Schnaiberg)
- [ ] سوسيولوجيا التطبيب والهندسة الحيوية الاجتماعية (Sociology of Medicalization & Biosociality: Conrad & Rose)
- [ ] سوسيولوجيا المقاومة اليومية والنصوص الخفية (Scott's Everyday Peasant Resistance Sociology)
- [ ] علم الاجتماع العام وأنماط الممارسة الأربعة (Burawoy's Public Sociology Paradigm)
- [ ] سوسيولوجيا الجسد والتجسيد الاجتماعي (Sociology of the Body & Embodiment: Shilling & Turner)
- [ ] السوسيولوجيا الحوسبية وتحليل الآثار الرقمية (Computational Sociology & Big Data Analysis)

---

## 7. السوسيولوجيا النسوية، دراسات الجندر، ما بعد الاستعمار والجنوب العالمي (Feminist, Decolonial & Global South)

- [ ] نظرية الموقف النسوي في علم الاجتماع (Feminist Standpoint Theory: Dorothy Smith)
- [ ] الإثنوغرافيا المؤسسية (Institutional Ethnography: Dorothy Smith)
- [ ] الفكر النسوي الأسود ومصفوفة الهيمنة (Black Feminist Sociology: Patricia Hill Collins)
- [ ] النظرية التقاطعية السوسيولوجية (Sociological Intersectionality: Crenshaw & Collins)
- [ ] النسوية النقدية ومناهضة النظام الأبوي الإمبريالي (bell hooks' Critical Feminist Sociology)
- [ ] سوسيولوجيا الأداء الجندري وتفكيك الثنائية (Butler's Gender Performativity Sociology)
- [ ] سوسيولوجيا العمل المنزلي وإعادة الإنتاج الجندري (Oakley's Sociology of Housework & Reproduction)
- [ ] سوسيولوجيا أزمة الرعاية والعدالة الرأسمالية (Fraser's Social Reproduction & Crisis of Care)
- [ ] سوسيولوجيا استعمارية السلطة والمركزية الأوروبية (Quijano's Coloniality of Power Sociology)
- [ ] إبستمولوجيات الجنوب وسوسيولوجيا الغيابات (Santos' Epistemologies of the South & Cognitive Justice)
- [ ] النقد السوسيولوجي للاستشراق والتمثيل الإمبريالي (Said's Sociology of Orientalism & Knowledge)
- [ ] علم الاجتماع التحرري ومناهضة الاستعمار (Fanonian Liberation Sociology & Sociogeny)
- [ ] سوسيولوجيا العقل الأسير والتبعية الأكاديمية الآسيوية (Alatas' Captive Mind Sociology)
- [ ] دراسات التابع والتأريخ السوسيولوجي من أسفل (Subaltern Studies: Guha & Spivak)
- [ ] سوسيولوجيا العمران والتحول البدوي-الحضري الخلدونية (Khaldunian Historical Sociology)
- [ ] سوسيولوجيا الشخصية الازدواجية وصراع القيم العربي (Al-Wardi's Iraqi & Arab Sociology)
- [ ] سوسيولوجيا البطريركية المستحدثة والتغير المشوه (Sharabi's Neopatriarchy Sociology)
- [x] سوسيولوجيا المجتمع الفسيفسائي والاغتراب العربي (Barakat's Contemporary Arab Society Sociology) — `sch-contemporary-arab-sociology` (دفعة 0، 2026-09-14)
- [ ] السوسيولوجيا النسوية العربية ونقد الهيمنة البطريركية (El Saadawi's Arab Feminist Sociology)
- [ ] التاريخانية والسوسيولوجيا النقدية العربية والإسلامية (Laroui & Shariati's Critical Arab/Islamic Sociology)

---

## 8. الميادين والفروع التخصصية في علم الاجتماع (Specialized Sociological Subdisciplines)

- [ ] سوسيولوجيا المعرفة والعلوم (Sociology of Knowledge & Scientific Knowledge - SSK)
- [ ] سوسيولوجيا الثقافة وأنماط الحياة (Sociology of Culture & Lifestyles)
- [ ] سوسيولوجيا الدين والتحولات العلمانية (Sociology of Religion & Post-Secularism)
- [ ] سوسيولوجيا الانحراف والجريمة والعدالة الجنائية (Sociology of Deviance, Crime & Justice)
- [ ] السوسيولوجيا الطبية والصحية والسريرية (Medical, Health & Clinical Sociology)
- [ ] السوسيولوجيا الحضرية وتخطيط المدن (Urban Sociology & Urban Spatial Planning)
- [ ] السوسيولوجيا الريفية والمجتمعات الزراعية (Rural & Agrarian Sociology)
- [ ] السوسيولوجيا البيئية والتنمية المستدامة (Environmental Sociology & Sustainability)
- [ ] السوسيولوجيا الاقتصادية وتجذر الأسواق (Economic Sociology & Embeddedness: Polanyi & Granovetter)
- [ ] سوسيولوجيا العمل والمهن والتصنيع (Sociology of Work, Occupations & Industrial Relations)
- [ ] السوسيولوجيا السياسية والدولة والمواطنة (Political Sociology, State & Citizenship)
- [ ] سوسيولوجيا التربية والتعليم وإعادة الإنتاج (Sociology of Education & Cultural Capital)
- [ ] سوسيولوجيا الأسرة والنوع الاجتماعي والعلاقات الحميمية (Sociology of Family, Gender & Intimacy)
- [ ] سوسيولوجيا الهجرة واللجوء والشتات (Sociology of Migration, Asylum & Diaspora)
- [ ] سوسيولوجيا الشيخوخة ودورة الحياة (Sociology of Aging & Life Course)
- [ ] سوسيولوجيا الشباب والثقافات الفرعية (Sociology of Youth & Subcultures)
- [ ] سوسيولوجيا الفن والأدب والجماليات (Sociology of Art, Literature & Aesthetics)
- [ ] سوسيولوجيا القانون والضبط الاجتماعي (Sociology of Law & Social Control)
- [ ] سوسيولوجيا الحركات الاجتماعية والعمل الجماعي (Sociology of Social Movements & Collective Action)
- [ ] السوسيولوجيا العسكرية والنزاعات المسلحة (Military Sociology & Armed Conflict)
