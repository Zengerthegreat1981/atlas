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
> - **الدفعة 3 (2026-09-14):** القسم 3 مكتملٌ بالكامل (19/19) — بارسونز (+فرعان: AGIL،
>   متغيرات النمط) وفرع الوظيفية الجديدة، ميرتون المدى المتوسط (+3 فروع: التوتر والأنومي،
>   الجماعة المرجعية، سوسيولوجيا العلم) وفرع رابع أُضيف لاحقاً (الميزة التراكمية/تأثير ماثيو)،
>   لومان (+فرع التواصل والتمايز)، هومانز (+فرعان: بلاو، التبادل الشبكي)، كولمان (+فرع
>   السوسيولوجيا التحليلية)، المؤسسية الجديدة التنظيمية، غولدنر وبلاو (التنظيمات المعقدة)،
>   تحليل الشبكات الاجتماعية. **تصحيح رجعي:** أُضيف `related` من `sch-social-capital-civic`
>   (دفعة 0) إلى `sch-coleman-rational-choice-sociology` الجديدة (لا `belongs_to`، فهما
>   صياغتان متنافستان متوازيتان لا علاقة أمّ-فرع).
> - **الدفعة 4 (2026-09-14):** القسم 4 مكتملٌ بالكامل (20/20) — دارندورف، ميلز (نخبة القوة)،
>   كولينز (الصراع المجهري)، فالرستين (+فرع تبعية أمريكا اللاتينية)، فرانكفورت السوسيولوجية
>   (+3 فروع: ماركوزه، هابرماس المجال العام وفرعه الفعل التواصلي، هونيث وفريزر الاعتراف)،
>   ألتوسير (+فرع ميليباند-بولانتزاس)، غرامشي (+فرع لاكلاو وموف)، رايت (التحليل الطبقي)،
>   لوفيفر (+فرع هارفي)، برافرمان، سكوتشبول (+فرع تيلي وتارو). ثلاثةُ مفكرين مشتركين مع
>   الفلسفة (ماركوزه، هابرماس، ألتوسير، غرامشي، لاكلاو، موف) رُبطوا عبر `related` فقط
>   لتباين `part`، لا `belongs_to`.
> - **الدفعة 5 (2026-09-14):** القسم 5 مكتملٌ بالكامل (19/19) — شوتز (+فرع بيرغر ولوكمان)،
>   غارفينكل (يسدّ فجوةً موثقة في دفعة 0: `sch-conversation-analysis` أُسندت إليه)، بورديو
>   (الممارسة/الهابيتوس، +فرعان: الحقول ورأس المال، والتمايز/إعادة الإنتاج — أول ملفات بورديو
>   في الأطلس رغم ذكره المتكرر في gaps سابقة)، فوكو (السلطة الانضباطية، +فرعان: السياسة
>   الحيوية، المعرفة-السلطة)، بودريار (+ربط متبادل مع دولوز)، دولوز، لاتور وكالون، بولتانسكي
>   وتيفنو (+فرع بولتانسكي وشيابيلو)، دوغلاس وجونسون الوجودية، السردية/التأويلية، البصرية/
>   الحسية، العلائقية المعاصرة، آرتشر الواقعية النقدية. 4 مفكرين مشتركين مع الفلسفة (شوتز،
>   فوكو، بودريار، دولوز) رُبطوا عبر `related` فقط.
> - **الدفعة 6 (2026-09-14):** القسم 6 مكتملٌ بالكامل (20/20) — غيدنز الهيكلة (+فرع الحداثة
>   الفائقة)، بيك مجتمع المخاطرة (+فرع الكوزموبوليتية؛ تنبيهٌ صريح: `thk-beck` القائم شخصٌ
>   آخر — آرون بيك مؤسس العلاج المعرفي السلوكي، لا أولريش بيك)، باومان الحداثة السائلة
>   (+فرع الأخلاق وما بعد الهولوكوست)، كاستلز مجتمع الشبكات (+فرع سلطة الاتصال)، ساسن
>   المدينة العالمية، أپادوراي وروبرتسون العولمة الثقافية، زوبوف رأسمالية المراقبة (+ربط
>   متبادل مع سرنيتشيك رأسمالية المنصات)، لوبتون السوسيولوجيا الرقمية، روزا التسارع
>   الاجتماعي، فوستر وشنايبرغ البيئية، كونراد وروز التطبيب، سكوت المقاومة اليومية، بوراوي
>   علم الاجتماع العام، شيلينغ وترنر الجسد، السوسيولوجيا الحوسبية. 3 مفكرين مشتركين مع
>   الفلسفة/النفس (غيدنز، باومان) رُبطوا عبر `related` فقط.
> - **الدفعة 7 (2026-09-14):** القسم 7 مكتملٌ بالكامل (19/19) — دوروثي سميث (+فرع الإثنوغرافيا
>   المؤسسية)، هيل كولينز (+فرع التقاطعية مع كرنشو)، بيل هوكس، بتلر الأداء الجندري، أوكلي
>   العمل المنزلي، فريزر أزمة الرعاية (مرتبطة بـsch-honneth-fraser من الدفعة 4 لنفس المفكرة)،
>   كويخانو استعمارية السلطة (+ربط متبادل مع سانتوس)، سانتوس إبستمولوجيات الجنوب، سعيد نقد
>   الاستشراق، فانون التحرري، ألاتاس العقل الأسير، دراسات التابع (غوها وسبيفاك) — الثلاثة
>   الأخيرة مربوطة ببعضها بعضاً (كتلة ما بعد استعمارية واحدة). **أُكملت حزمة `sch-contemporary-
>   arab-sociology` (فجوة موثقة من الدفعة 0):** أُضيفت 4 مدارس فرعية بـ`belongs_to` صحيح —
>   الوردي، شرابي، السعداوي، والعروي مع شريعتي — إضافة إلى `sch-khaldunian-historical-
>   sociology` فرعاً لـ`sch-khaldunian-ilm-al-umran` (دفعة 1). 6 مفكرين مشتركين مع الفلسفة
>   (كرنشو، كويخانو، سعيد، فانون، سبيفاك، العروي) رُبطوا عبر `related` فقط.
> - **الدفعة 8 (2026-09-14، الأخيرة):** القسم 8 مكتملٌ بالكامل (20/20) — سوسيولوجيا المعرفة
>   والعلوم (مانهايم وبلور)، الثقافة وأنماط الحياة (سويدلر وبيترسون)، الدين والعلمانية (بيرغر
>   وكازانوفا)، الانحراف والجريمة (هيرشي وكوهين)، الطب والصحة (بارسونز وفريدسون)، الحضرية
>   وتخطيط المدن (جين جاكوبس)، الريفية (غالبين ونيوبي)، البيئية والاستدامة (كاتون ودنلاب، مكمِّلة
>   لصدع فوستر الأيضي من الدفعة 6)، الاقتصادية والتجذر (بولاني وغرانوفيتر)، العمل والمهن
>   (هيوز)، السياسية والمواطنة (مارشال)، التربية ورأس المال الثقافي (برنشتاين، مكمِّلة لتمايز
>   بورديو من الدفعة 5)، الأسرة والحميمية (بارسونز/بيلز وغيدنز)، الهجرة والشتات (بورتيس
>   وسافران)، الشيخوخة ودورة الحياة (كامنغ وإلدر)، الشباب والثقافات الفرعية (هبديج)، الفن
>   والأدب (بيكر)، القانون والضبط (دونالد بلاك)، الحركات الاجتماعية (ماك آدم، مكمِّلة لتيلي
>   وتارو من الدفعة 4)، والعسكرية (يانوفيتز، آخر بند في القائمة بأكملها).
>
> **🎉 قائمة مدارس علم الاجتماع مكتملةٌ بالكامل: 159/159 (100%).** جميع الأقسام الثمانية
> منجزة. لا بندَ واحداً متبقياً غير مؤشَّرٍ بـ`[x]` في هذا الملف.
>
> **المرحلةُ التالية (خارج نطاق هذا الملف):** حسب `SOCIOLOGY_MISSION_PROMPT.md` القسم 4،
> الدفعات القادمة تنتقل من «الهيكل» (مدارس) إلى «الحزم» — لكل مدرسة من الـ159: مفكروها
> (`thk-`)، مفاهيمها (`con-`)، أعمالها (`wrk-`)، دراساتها (`stu-`)، جدالاتها (`dbt-`) وغيرها،
> وصولاً إلى الهدف الكلي 1,200–1,500 عقدة حيّة (الرصيد الحالي بعد هذه الدفعة: نحو 160 عقدة
> سوسيولوجية — 159 مدرسة + 3 مفكرين قدامى مُسنَدين إليها، بعيداً كثيراً عن الهدف). ثم الدفعة
> الأخيرة: جسور `part: "bridge"` إلى الفلسفة وعلم النفس (ماركس/الاغتراب، دوركهايم/الأنومي
> والانتحار، غوفمان/الوصمة والمؤسسات الشاملة، بورديو/الهابيتوس، فوكو المشترك). هذا الملف
> (`sociology-schools-backlog.md`) لم يعد «موضع التوقف» الأساسي لتتبع التقدّم بعد اكتماله؛
> الوكيل التالي يحتاج تتبعاً جديداً على مستوى المفكرين/المفاهيم لكل مدرسة (راجع
> `SOCIOLOGY_PART_PLAN.md` و`agents_specs/decision-records.md` لمعايير الحزم).

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

- [x] نظرية الفعل الاجتماعي والتركيب البارسونزي (Parsonian Action Frame of Reference) — `sch-parsonian-action-frame` (دفعة 3، 2026-09-14)
- [x] الوظيفية البنائية الشاملة ونموذج AGIL (Parsonian Structural Functionalism) — `sch-parsonian-structural-functionalism-agil` (دفعة 3، 2026-09-14)
- [x] متغيرات النمط ونظرية التحديث (Parsonian Pattern Variables & Modernization Theory) — `sch-parsonian-pattern-variables` (دفعة 3، 2026-09-14)
- [x] وظيفية المدى المتوسط والتحليل البنائي (Mertonian Middle-Range Functionalism) — `sch-mertonian-middle-range` (دفعة 3، 2026-09-14)
- [x] نظرية التوتر والأنومي (Merton's Strain Theory of Deviance) — `sch-mertons-strain-theory` (دفعة 3، 2026-09-14)
- [x] نظرية الجماعات المرجعية والحرمان النسبي (Reference Group & Relative Deprivation Theory) — `sch-reference-group-relative-deprivation` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا العلم والمؤسسة الأكاديمية (Mertonian Sociology of Science / CUDOS) — `sch-mertonian-sociology-of-science` (دفعة 3، 2026-09-14)
- [x] الوظيفية الجديدة والتركيب ما بعد البارسونزي (Neofunctionalism: Alexander & Colomy) — `sch-neofunctionalism` (دفعة 3، 2026-09-14)
- [x] نظرية الأنساق الاجتماعية الأوتوبويتية (Luhmannian Autopoietic Social Systems Theory) — `sch-luhmannian-autopoietic-systems` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا التواصل والتمايز النسقي (Luhmannian Sociology of Communication & Differentiation) — `sch-luhmannian-communication-differentiation` (دفعة 3، 2026-09-14)
- [x] نظرية التبادل الاجتماعي السلوكية (Homans' Behavioral Social Exchange Theory) — `sch-homans-behavioral-exchange` (دفعة 3، 2026-09-14)
- [x] نظرية التبادل البنائي والتفاوت الطبقي (Blau's Structural Exchange Theory) — `sch-blau-structural-exchange` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا الاختيار العقلاني ورأس المال الاجتماعي (Coleman's Rational Choice Sociology) — `sch-coleman-rational-choice-sociology` (دفعة 3، 2026-09-14)
- [x] السوسيولوجيا التحليلية ونظرية الآليات الاجتماعية (Analytical Sociology: Elster & Hedström) — `sch-analytical-sociology` (دفعة 3، 2026-09-14)
- [x] نظرية التبادل الشبكي وعلاقات القوة-التبعية (Network Exchange Theory: Willer & Cook) — `sch-network-exchange-theory` (دفعة 3، 2026-09-14)
- [x] المؤسسية الجديدة في سوسيولوجيا التنظيمات (New Institutionalism in Organizational Sociology: DiMaggio & Powell) — `sch-new-institutionalism-organizational` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا رأس المال الاجتماعي والشبكات المدنية (Putnam's Social Capital Theory) — `sch-social-capital-civic` (دفعة 0، 2026-09-14)
- [x] سوسيولوجيا التنظيمات والخلل البيروقراطي (Sociology of Complex Organizations: Gouldner & Blau) — `sch-complex-organizations-gouldner-blau` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا الشبكات الاجتماعية وتحليل البنى (Social Network Analysis Paradigm: Wellman & Granovetter) — `sch-social-network-analysis-paradigm` (دفعة 3، 2026-09-14)
- [x] سوسيولوجيا المكانة والتمايز الطبقي التراكمي (Cumulative Advantage Theory / Matthew Effect) — `sch-cumulative-advantage-theory` (دفعة 3، 2026-09-14)

---

## 4. نظرية الصراع، مدرسة فرانكفورت والماركسية النقدية (Conflict Theory & Critical Sociology)

- [x] سوسيولوجيا الصراع الليبرالية (Dahrendorfian Conflict Sociology) — `sch-dahrendorfian-conflict-sociology` (دفعة 4، 2026-09-14)
- [x] السوسيولوجيا الراديكالية ونقد نخبة القوة (Millsian Critical Sociology & The Power Elite) — `sch-millsian-power-elite` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا الصراع المجهرية وسلاسل طقوس التفاعل (Collins' Micro-Conflict Sociology) — `sch-collins-micro-conflict` (دفعة 4، 2026-09-14)
- [x] تحليل النظم العالمية والتقسيم الدولي للعمل (Wallerstein's World-Systems Analysis) — `sch-wallerstein-world-systems` (دفعة 4، 2026-09-14)
- [x] نظرية التبعية السوسيولوجية اللاتينية (Latin American Dependency Theory: Cardoso, Dos Santos) — `sch-latin-american-dependency-theory` (دفعة 4، 2026-09-14)
- [x] النظرية النقدية الأولى والتسليع الثقافي (Frankfurt School Critical Sociology: Horkheimer & Adorno) — `sch-frankfurt-critical-sociology` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا المجتمع الصناعي أحادي البعد (Marcusean Critical Sociology of One-Dimensionality) — `sch-marcusean-one-dimensionality` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا المجال العام والديمقراطية التداولية (Habermasian Public Sphere Sociology) — `sch-habermasian-public-sphere` (دفعة 4، 2026-09-14)
- [x] نظرية الفعل التواصلي واستعمار عالم الحياة (Habermasian Theory of Communicative Action) — `sch-habermasian-communicative-action` (دفعة 4، 2026-09-14)
- [x] الماركسية البنيوية وأجهزة الدولة (Althusserian Structural Marxism) — `sch-althusserian-structural-marxism` (دفعة 4، 2026-09-14)
- [x] الهيمنة الثقافية والكتلة التاريخية (Gramscian Cultural Hegemony & Historical Bloc) — `sch-gramscian-cultural-hegemony` (دفعة 4، 2026-09-14)
- [x] ما بعد الماركسية والتحليل الخطابي للصراع (Laclau & Mouffe's Discourse & Hegemony Theory) — `sch-laclau-mouffe-discourse-hegemony` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا الدولة الرأسمالية (Miliband-Poulantzas State Theory) — `sch-miliband-poulantzas-state-theory` (دفعة 4، 2026-09-14)
- [x] التحليل الطبقي والمواقع المتناقضة (Wright's Analytical Marxist Class Theory) — `sch-wright-analytical-marxist-class` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا الفضاء والحق في المدينة (Lefebvrean Spatial Sociology) — `sch-lefebvrean-spatial-sociology` (دفعة 4، 2026-09-14)
- [x] الجغرافيا الماركسية والتراكم المكاني (Harvey's Critical Urban & Spatial Sociology) — `sch-harvey-critical-urban-spatial` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا عملية العمل ونزع المهارة (Braverman's Labor Process Theory) — `sch-braverman-labor-process` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا الاعتراف والعدالة التوزيعية (Honneth & Fraser's Recognition & Redistribution Theory) — `sch-honneth-fraser-recognition-redistribution` (دفعة 4، 2026-09-14)
- [x] علم الاجتماع التاريخي والمقارن للثورات (Skocpol's Comparative-Historical Sociology of Revolutions) — `sch-skocpol-comparative-historical-revolutions` (دفعة 4، 2026-09-14)
- [x] سوسيولوجيا الحركات الاجتماعية وعمليات التعبئة (Tilly & Tarrow's Contentious Politics & Social Movements) — `sch-tilly-tarrow-contentious-politics` (دفعة 4، 2026-09-14)

---

## 5. الظاهراتية، الإثنوميثودولوجيا، نظرية الممارسة وما بعد البنيوية (Phenomenological, Practice & Post-Structuralist)

- [x] الفينومينولوجيا السوسيولوجية وعالم الحياة المعاش (Schutzian Phenomenological Sociology) — `sch-schutzian-phenomenological-sociology` (دفعة 5، 2026-09-14)
- [x] البنائية الاجتماعية للواقع (Berger & Luckmann's Social Constructionism) — `sch-berger-luckmann-social-construction` (دفعة 5، 2026-09-14)
- [x] الإثنوميثودولوجيا والتفكير العملي العادي (Garfinkelian Ethnomethodology) — `sch-garfinkelian-ethnomethodology` (دفعة 5، 2026-09-14)
- [x] تحليل المحادثة والتنظيم التفاعلي الصوري (Conversation Analysis: Sacks & Schegloff) — `sch-conversation-analysis` (دفعة 0، 2026-09-14)
- [x] نظرية الممارسة والهابيتوس (Bourdieu's Theory of Practice & Habitus) — `sch-bourdieu-practice-habitus` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا الحقول وأشكال رأس المال (Bourdieu's Field Theory & Forms of Capital) — `sch-bourdieu-field-capital` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا التمايز وإعادة الإنتاج الثقافي (Bourdieu's Distinction & Cultural Reproduction) — `sch-bourdieu-distinction-cultural-reproduction` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا السلطة الانضباطية والمراقبة (Foucauldian Disciplinary Power & Surveillance) — `sch-foucauldian-disciplinary-power` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا السياسة الحيوية والحكومية (Foucauldian Biopolitics & Governmentality) — `sch-foucauldian-biopolitics-governmentality` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا المعرفة-السلطة والتشكيلات الخطابية (Foucauldian Power/Knowledge & Discourse) — `sch-foucauldian-power-knowledge-discourse` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا المحاكاة والمجتمع الاستهلاكي الفائق (Baudrillardian Hyperreality & Simulation) — `sch-baudrillardian-hyperreality` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا التجميع والإنتاج الاجتماعي (Deleuzian Assemblage Sociology) — `sch-deleuzian-assemblage-sociology` (دفعة 5، 2026-09-14)
- [x] نظرية شبكة الفواعل وسوسيولوجيا الترجمة (Latour & Callon's Actor-Network Theory - ANT) — `sch-latour-callon-actor-network-theory` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا التبرير ونماذج الجدارة (Boltanski & Thévenot's Sociology of Worth / Pragmatic Sociology) — `sch-boltanski-thevenot-sociology-of-worth` (دفعة 5، 2026-09-14)
- [x] سوسيولوجيا نقد الرأسمالية الشبكية (Boltanski & Chiapello's Sociology of Capitalist Spirit) — `sch-boltanski-chiapello-capitalist-spirit` (دفعة 5، 2026-09-14)
- [x] السوسيولوجيا الوجودية والخبرة المعيشة (Douglas & Johnson's Existential Sociology) — `sch-douglas-johnson-existential-sociology` (دفعة 5، 2026-09-14)
- [x] السوسيولوجيا التأويلية والسردية (Narrative & Hermeneutic Sociology) — `sch-narrative-hermeneutic-sociology` (دفعة 5، 2026-09-14)
- [x] السوسيولوجيا البصرية والإثنوغرافيا الحسية (Visual Sociology & Sensory Ethnography) — `sch-visual-sociology-sensory-ethnography` (دفعة 5، 2026-09-14)
- [x] السوسيولوجيا العلائقية المعاصرة (Contemporary Relational Sociology: Emirbayer & Dépelteau) — `sch-contemporary-relational-sociology` (دفعة 5، 2026-09-14)
- [x] الواقعية النقدية السوسيولوجية ونظرية المورفوجينيسيس (Archerian Critical Realist Sociology) — `sch-archerian-critical-realist-sociology` (دفعة 5، 2026-09-14)

---

## 6. النظريات السوسيولوجية المعاصرة، العولمة والمجتمع الرقمي (Contemporary, Globalization & Digital Sociology)

- [x] نظرية الهيكلة وازدواجية البنية (Giddens' Structuration Theory) — `sch-giddens-structuration-theory` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا الحداثة الفائقة والانعكاسية (Giddens' Reflexive Modernity & Self-Identity) — `sch-giddens-reflexive-modernity` (دفعة 6، 2026-09-14)
- [x] نظرية مجتمع المخاطرة والحداثة الثانية (Beck's Risk Society Theory) — `sch-beck-risk-society-theory` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا الكوزموبوليتية والمخاطر العالمية (Beck's Cosmopolitan Sociology & World at Risk) — `sch-beck-cosmopolitan-sociology` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا الحداثة السائلة (Bauman's Liquid Modernity Paradigm) — `sch-bauman-liquid-modernity` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا الأخلاق في عصر الحداثة وما بعد الهولوكوست (Bauman's Postmodern Ethics & Waste Sociology) — `sch-bauman-postmodern-ethics-waste` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا مجتمع الشبكات والمعلومات (Castells' Network Society Theory) — `sch-castells-network-society` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا سلطة الاتصال والحركات الرقمية (Castells' Communication Power Sociology) — `sch-castells-communication-power` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا المدينة العالمية وتدفقات رأس المال (Sassen's Global City & Expulsions Theory) — `sch-sassen-global-city` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا العولمة الثقافية والمشاهد العولمية (Appadurai & Robertson's Global Culture & Scapes) — `sch-appadurai-robertson-global-culture` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا رأسمالية المراقبة (Zuboff's Surveillance Capitalism Sociology) — `sch-zuboff-surveillance-capitalism` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا رأسمالية المنصات واقتصاد العمل الحر (Srnicek's Platform Capitalism Sociology) — `sch-srnicek-platform-capitalism` (دفعة 6، 2026-09-14)
- [x] السوسيولوجيا الرقمية وحكومية البيانات (Lupton's Digital Sociology & Metric Power) — `sch-lupton-digital-sociology` (دفعة 6، 2026-09-14)
- [x] نظرية التسارع الاجتماعي وتغير الإيقاع الزمني (Rosa's Social Acceleration & Resonance Theory) — `sch-rosa-social-acceleration` (دفعة 6، 2026-09-14)
- [x] السوسيولوجيا البيئية ونظرية الصدع الأيضي (Environmental Sociology & Metabolic Rift: Foster & Schnaiberg) — `sch-environmental-sociology-metabolic-rift` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا التطبيب والهندسة الحيوية الاجتماعية (Sociology of Medicalization & Biosociality: Conrad & Rose) — `sch-medicalization-biosociality` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا المقاومة اليومية والنصوص الخفية (Scott's Everyday Peasant Resistance Sociology) — `sch-scott-everyday-peasant-resistance` (دفعة 6، 2026-09-14)
- [x] علم الاجتماع العام وأنماط الممارسة الأربعة (Burawoy's Public Sociology Paradigm) — `sch-burawoy-public-sociology` (دفعة 6، 2026-09-14)
- [x] سوسيولوجيا الجسد والتجسيد الاجتماعي (Sociology of the Body & Embodiment: Shilling & Turner) — `sch-sociology-of-body-embodiment` (دفعة 6، 2026-09-14)
- [x] السوسيولوجيا الحوسبية وتحليل الآثار الرقمية (Computational Sociology & Big Data Analysis) — `sch-computational-sociology-big-data` (دفعة 6، 2026-09-14)

---

## 7. السوسيولوجيا النسوية، دراسات الجندر، ما بعد الاستعمار والجنوب العالمي (Feminist, Decolonial & Global South)

- [x] نظرية الموقف النسوي في علم الاجتماع (Feminist Standpoint Theory: Dorothy Smith) — `sch-dorothy-smith-standpoint-theory` (دفعة 7، 2026-09-14)
- [x] الإثنوغرافيا المؤسسية (Institutional Ethnography: Dorothy Smith) — `sch-dorothy-smith-institutional-ethnography` (دفعة 7، 2026-09-14)
- [x] الفكر النسوي الأسود ومصفوفة الهيمنة (Black Feminist Sociology: Patricia Hill Collins) — `sch-hill-collins-black-feminist-sociology` (دفعة 7، 2026-09-14)
- [x] النظرية التقاطعية السوسيولوجية (Sociological Intersectionality: Crenshaw & Collins) — `sch-sociological-intersectionality` (دفعة 7، 2026-09-14)
- [x] النسوية النقدية ومناهضة النظام الأبوي الإمبريالي (bell hooks' Critical Feminist Sociology) — `sch-bell-hooks-critical-feminist-sociology` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا الأداء الجندري وتفكيك الثنائية (Butler's Gender Performativity Sociology) — `sch-butler-gender-performativity` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا العمل المنزلي وإعادة الإنتاج الجندري (Oakley's Sociology of Housework & Reproduction) — `sch-oakley-housework-reproduction` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا أزمة الرعاية والعدالة الرأسمالية (Fraser's Social Reproduction & Crisis of Care) — `sch-fraser-social-reproduction-crisis-of-care` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا استعمارية السلطة والمركزية الأوروبية (Quijano's Coloniality of Power Sociology) — `sch-quijano-coloniality-of-power` (دفعة 7، 2026-09-14)
- [x] إبستمولوجيات الجنوب وسوسيولوجيا الغيابات (Santos' Epistemologies of the South & Cognitive Justice) — `sch-santos-epistemologies-of-the-south` (دفعة 7، 2026-09-14)
- [x] النقد السوسيولوجي للاستشراق والتمثيل الإمبريالي (Said's Sociology of Orientalism & Knowledge) — `sch-said-sociology-of-orientalism` (دفعة 7، 2026-09-14)
- [x] علم الاجتماع التحرري ومناهضة الاستعمار (Fanonian Liberation Sociology & Sociogeny) — `sch-fanonian-liberation-sociology` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا العقل الأسير والتبعية الأكاديمية الآسيوية (Alatas' Captive Mind Sociology) — `sch-alatas-captive-mind-sociology` (دفعة 7، 2026-09-14)
- [x] دراسات التابع والتأريخ السوسيولوجي من أسفل (Subaltern Studies: Guha & Spivak) — `sch-subaltern-studies-guha-spivak` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا العمران والتحول البدوي-الحضري الخلدونية (Khaldunian Historical Sociology) — `sch-khaldunian-historical-sociology` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا الشخصية الازدواجية وصراع القيم العربي (Al-Wardi's Iraqi & Arab Sociology) — `sch-alwardi-iraqi-arab-sociology` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا البطريركية المستحدثة والتغير المشوه (Sharabi's Neopatriarchy Sociology) — `sch-sharabi-neopatriarchy-sociology` (دفعة 7، 2026-09-14)
- [x] سوسيولوجيا المجتمع الفسيفسائي والاغتراب العربي (Barakat's Contemporary Arab Society Sociology) — `sch-contemporary-arab-sociology` (دفعة 0، 2026-09-14)
- [x] السوسيولوجيا النسوية العربية ونقد الهيمنة البطريركية (El Saadawi's Arab Feminist Sociology) — `sch-elsaadawi-arab-feminist-sociology` (دفعة 7، 2026-09-14)
- [x] التاريخانية والسوسيولوجيا النقدية العربية والإسلامية (Laroui & Shariati's Critical Arab/Islamic Sociology) — `sch-laroui-shariati-critical-arab-islamic-sociology` (دفعة 7، 2026-09-14)

---

## 8. الميادين والفروع التخصصية في علم الاجتماع (Specialized Sociological Subdisciplines)

- [x] سوسيولوجيا المعرفة والعلوم (Sociology of Knowledge & Scientific Knowledge - SSK) — `sch-sociology-of-scientific-knowledge` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الثقافة وأنماط الحياة (Sociology of Culture & Lifestyles) — `sch-sociology-of-culture-lifestyles` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الدين والتحولات العلمانية (Sociology of Religion & Post-Secularism) — `sch-sociology-of-religion-post-secularism` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الانحراف والجريمة والعدالة الجنائية (Sociology of Deviance, Crime & Justice) — `sch-sociology-of-deviance-crime-justice` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا الطبية والصحية والسريرية (Medical, Health & Clinical Sociology) — `sch-medical-health-clinical-sociology` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا الحضرية وتخطيط المدن (Urban Sociology & Urban Spatial Planning) — `sch-urban-sociology-spatial-planning` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا الريفية والمجتمعات الزراعية (Rural & Agrarian Sociology) — `sch-rural-agrarian-sociology` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا البيئية والتنمية المستدامة (Environmental Sociology & Sustainability) — `sch-environmental-sociology-sustainability` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا الاقتصادية وتجذر الأسواق (Economic Sociology & Embeddedness: Polanyi & Granovetter) — `sch-economic-sociology-embeddedness` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا العمل والمهن والتصنيع (Sociology of Work, Occupations & Industrial Relations) — `sch-sociology-of-work-occupations` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا السياسية والدولة والمواطنة (Political Sociology, State & Citizenship) — `sch-political-sociology-state-citizenship` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا التربية والتعليم وإعادة الإنتاج (Sociology of Education & Cultural Capital) — `sch-sociology-of-education-cultural-capital` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الأسرة والنوع الاجتماعي والعلاقات الحميمية (Sociology of Family, Gender & Intimacy) — `sch-sociology-of-family-gender-intimacy` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الهجرة واللجوء والشتات (Sociology of Migration, Asylum & Diaspora) — `sch-sociology-of-migration-diaspora` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الشيخوخة ودورة الحياة (Sociology of Aging & Life Course) — `sch-sociology-of-aging-life-course` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الشباب والثقافات الفرعية (Sociology of Youth & Subcultures) — `sch-sociology-of-youth-subcultures` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الفن والأدب والجماليات (Sociology of Art, Literature & Aesthetics) — `sch-sociology-of-art-literature-aesthetics` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا القانون والضبط الاجتماعي (Sociology of Law & Social Control) — `sch-sociology-of-law-social-control` (دفعة 8، 2026-09-14)
- [x] سوسيولوجيا الحركات الاجتماعية والعمل الجماعي (Sociology of Social Movements & Collective Action) — `sch-sociology-of-social-movements-collective-action` (دفعة 8، 2026-09-14)
- [x] السوسيولوجيا العسكرية والنزاعات المسلحة (Military Sociology & Armed Conflict) — `sch-military-sociology-armed-conflict` (دفعة 8، 2026-09-14)
