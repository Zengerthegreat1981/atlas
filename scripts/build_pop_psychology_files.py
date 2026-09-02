# -*- coding: utf-8 -*-
import os

thinkers_data = [
    # Academic Thinkers (no register: popular on thinker)
    {
        "slug": "thk-kahneman",
        "title": "دانيال كانمان",
        "en": "Daniel Kahneman",
        "dates": "إسرائيل / الولايات المتحدة · 1934–2024",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 1969,
        "active_end": 2024,
        "school": "علم النفس المعرفي والاقتصاد السلوكي",
        "is_pop": False,
        "lede": "عالم نفس معرفي إسرائيلي-أمريكي، حائز على جائزة نوبل في العلوم الاقتصادية (2002)؛ يُعد رائد أبحاث اتخاذ القرار، واستدلالات التفكير والانحيازات المعرفية (Heuristics and Biases)، ونظرية الاحتمال مع عاموس تفيرسكي.",
        "works": ["Thinking, Fast and Slow (2011)", "Judgement under Uncertainty: Heuristics and Biases (1982)", "Prospect Theory: An Analysis of Decision under Risk (1979)"],
        "related": [
            {"id": "wrk-thinking-fast-slow", "title": "التفكير: السريع والبطيء", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-cialdini",
        "title": "روبرت تشالديني",
        "en": "Robert B. Cialdini",
        "dates": "الولايات المتحدة · 1945–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1970,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي التجريبي",
        "is_pop": False,
        "lede": "أستاذ علم النفس الفخري بجامعة ولاية أريزونا، يُعد المرجع الأكاديمي العالمي الأول في سيكولوجيا التأثير والإقناع والامتثال الاجتماعي التجريبي.",
        "works": ["Influence: The Psychology of Persuasion (1984)", "Pre-Suasion: A Revolutionary Way to Influence and Persuade (2016)"],
        "related": [
            {"id": "wrk-influence-persuasion", "title": "التأثير: علم نفس الإقناع", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-dweck",
        "title": "كارول دويك",
        "en": "Carol S. Dweck",
        "dates": "الولايات المتحدة · 1946–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "مستمر",
        "school": "علم النفس النمائي والشخصية",
        "is_pop": False,
        "lede": "أستاذة علم النفس بجامعة ستانفورد، رائدة الأبحاث التجريبية في الدافعية ونظرية العقلية (Mindset)، وصاحبة التمييز الكلاسيكي بين العقلية الثابتة وعقلية النمو.",
        "works": ["Mindset: The New Psychology of Success (2006)", "Self-theories: Their Role in Motivation, Personality, and Development (1999)"],
        "related": [
            {"id": "wrk-mindset", "title": "طريقة التفكير / العقلية", "type": "عمل / كتاب"},
            {"id": "stu-dweck-growth-mindset-praise", "title": "دراسة مولر ودويك حول عقلية النمو", "type": "دراسة وبحث"}
        ]
    },
    {
        "slug": "thk-duckworth",
        "title": "أنجيلا دَكوورث",
        "en": "Angela Duckworth",
        "dates": "الولايات المتحدة · 1970–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2005,
        "active_end": "مستمر",
        "school": "علم النفس الإيجابي والشخصية",
        "is_pop": False,
        "lede": "أستاذة علم النفس بجامعة بنسلفانيا، ومؤسسة مختبر الشخصية (Character Lab)؛ ركزت أبحاثها على دور الشغف والمثابرة طويلة الأمد (Grit) وضبط الذات في التنبؤ بالنجاح.",
        "works": ["Grit: The Power of Passion and Perseverance (2016)", "Grit: Perseverance and passion for long-term goals (Journal of Personality and Social Psychology, 2007)"],
        "related": [
            {"id": "wrk-grit-2016", "title": "المثابرة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-amy-cuddy",
        "title": "إيمي كادي",
        "en": "Amy Cuddy",
        "dates": "الولايات المتحدة · 1972–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2006,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي التجريبي",
        "is_pop": False,
        "lede": "عالمة نفس اجتماعي ومحاضرة سابقة في كلية هارفارد للأعمال، اشتهرت بأبحاث لغة الجسد ووضعيات القوة (Power Posing) وحضور الذات، واحتلت دراساتها موقعاً مركزياً في نقاشات أزمة التكرار في علم النفس.",
        "works": ["Presence: Bringing Your Boldest Self to Your Biggest Challenges (2015)", "Power Posing: Brief Nonverbal Displays Affect Neuroendocrine Levels and Risk Tolerance (Psychological Science, 2010)"],
        "related": [
            {"id": "wrk-presence-cuddy", "title": "الحضور", "type": "عمل / كتاب"},
            {"id": "dbt-psychology-replication-crisis", "title": "أزمة التكرار في علم النفس", "type": "جدل"}
        ]
    },
    {
        "slug": "thk-kristin-neff",
        "title": "كريستين نيف",
        "en": "Kristin Neff",
        "dates": "الولايات المتحدة · 1966–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2003,
        "active_end": "مستمر",
        "school": "علم النفس الإنمائي والمعرفي",
        "is_pop": False,
        "lede": "أستاذة مشاركة في علم النفس بجامعة تكساس في أوستن، رائدة الأبحاث الأكاديمية في الشفقة بالذات (Self-Compassion) ومطورة مقياس الشفقة بالذات المعياري وبرنامج Mindful Self-Compassion مع كريس غيرمر.",
        "works": ["Self-Compassion: The Proven Power of Being Kind to Yourself (2011)", "The Mindful Self-Compassion Workbook (2018)", "Self-Compassion: An Alternative Conceptualization of a Healthy Attitude Toward Oneself (2003)"],
        "related": [
            {"id": "wrk-self-compassion-neff", "title": "التعاطف مع الذات", "type": "عمل / كتاب"},
            {"id": "tec-cbt-emo-self-compassion-exercises", "title": "تمارين الرأفة بالذات", "type": "تقنية/تدخل علاجي"}
        ]
    },

    # Pop Psychology Authors (register: "popular")
    {
        "slug": "thk-carnegie",
        "title": "ديل كارنيجي",
        "en": "Dale Carnegie",
        "dates": "الولايات المتحدة · 1888–1955",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1912,
        "active_end": 1955,
        "school": "علم النفس الشعبي وتطوير الذات",
        "is_pop": True,
        "lede": "كاتب ومحاضر أمريكي، يُعد الأب الروحي لحركة المساعدة الذاتية (Self-Help) والتدريب على العلاقات الإنسانية والخطابة العامة في القرن العشرين.",
        "works": ["How to Win Friends and Influence People (1936)", "How to Stop Worrying and Start Living (1948)"],
        "related": [
            {"id": "wrk-how-to-win-friends", "title": "كيف تكسب الأصدقاء وتؤثر في الناس", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-thomas-harris",
        "title": "توماس أ. هاريس",
        "en": "Thomas A. Harris",
        "dates": "الولايات المتحدة · 1910–1995",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1950,
        "active_end": "1995",
        "school": "التحليل التفاعلي وعلم النفس الشعبي",
        "is_pop": True,
        "lede": "طبيب نفسي أمريكي وتلميذ لإريك بيرن، ساهم في نشر نظرية التحليل التفاعلي على نطاق جماهيري واسع عبر كتابه ذائع الصيت «أنا بخير، أنت بخير».",
        "works": ["I'm OK – You're OK (1967)", "Staying OK (1985)"],
        "related": [
            {"id": "wrk-im-ok-youre-ok", "title": "أنا بخير، أنت بخير", "type": "عمل / كتاب"},
            {"id": "thk-eburne", "title": "إريك بيرن", "type": "مفكر"}
        ]
    },
    {
        "slug": "thk-scott-peck",
        "title": "م. سكوت بيك",
        "en": "M. Scott Peck",
        "dates": "الولايات المتحدة · 1936–2005",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1978,
        "active_end": "2005",
        "school": "علم النفس الشعبي والروحي",
        "is_pop": True,
        "lede": "طبيب نفسي ومؤلف أمريكي، اشتهر بدمج الممارسة النفسية بالبعد الروحي والانضباط الأخلاقي في كتابه الشهير «الطريق الأقل ارتياداً».",
        "works": ["The Road Less Traveled (1978)", "People of the Lie (1983)"],
        "related": [
            {"id": "wrk-road-less-traveled", "title": "الطريق الأقل ارتياداً", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-goleman",
        "title": "دانيال غولمان",
        "en": "Daniel Goleman",
        "dates": "الولايات المتحدة · 1946–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1980,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والصحافة العلمية",
        "is_pop": True,
        "lede": "عالم نفس وصحفي علمي سابق في نيويورك تايمز، كان له الفضل الأكبر في تحويل مفهوم «الذكاء العاطفي» إلى ظاهرة عالمية في الإدارة والتربية والعلاقات.",
        "works": ["Emotional Intelligence (1995)", "Working with Emotional Intelligence (1998)", "Social Intelligence: The New Science of Human Relationships (2006)"],
        "related": [
            {"id": "wrk-emotional-intelligence", "title": "الذكاء العاطفي", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-john-gray",
        "title": "جون غراي",
        "en": "John Gray",
        "dates": "الولايات المتحدة · 1951–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1990,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والعلاقات الأسرية",
        "is_pop": True,
        "lede": "استشاري علاقات ومؤلف أمريكي، حققت كتبه حول الفروق النفسية بين الجنسين انتشاراً قياسياً، وخاصة مؤلفه «الرجال من المريخ والنساء من الزهرة».",
        "works": ["Men Are from Mars, Women Are from Venus (1992)", "Mars and Venus on a Date (1997)"],
        "related": [
            {"id": "wrk-men-are-from-mars", "title": "الرجال من المريخ والنساء من الزهرة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-gladwell",
        "title": "مالكولم غلادويل",
        "en": "Malcolm Gladwell",
        "dates": "المملكة المتحدة / كندا · 1963–",
        "country": "كندا",
        "language": "الإنجليزية",
        "active_start": 2000,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والصحافة الاستقصائية",
        "is_pop": True,
        "lede": "صحفي وكاتب كندي بارز في مجلة «نيويوركر»، اشتهر بتبسيط أبحاث علم النفس المعرفي والاجتماعي وسوسيولوجيا النجاح والسلوك الجمعي في سرديات روائية شيقة.",
        "works": ["The Tipping Point (2000)", "Blink: The Power of Thinking Without Thinking (2005)", "Outliers: The Story of Success (2008)"],
        "related": [
            {"id": "wrk-tipping-point", "title": "نقطة التحول", "type": "عمل / كتاب"},
            {"id": "wrk-blink", "title": "التفكير اللماح / ذكاء اللحظة", "type": "عمل / كتاب"},
            {"id": "wrk-outliers", "title": "المتميزون / المتفوقون", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-susan-cain",
        "title": "سوزان كين",
        "en": "Susan Cain",
        "dates": "الولايات المتحدة · 1968–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2012,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والشخصية",
        "is_pop": True,
        "lede": "كاتبة ومحاضرة أمريكية، أحدث كتابها «الهدوء» ثورة في النظرة المجتمعية للانطوائية، وتفكيك الانحياز الثقافي الغربي للنمط الانبساطي.",
        "works": ["Quiet: The Power of Introverts in a World That Can't Stop Talking (2012)", "Bittersweet: How Sorrow and Longing Make Us Whole (2022)"],
        "related": [
            {"id": "wrk-quiet-2012", "title": "الهدوء: قوة الانطوائيين", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-brene-brown",
        "title": "برينيه براون",
        "en": "Brené Brown",
        "dates": "الولايات المتحدة · 1965–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2002,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والعمل الاجتماعي",
        "is_pop": True,
        "lede": "أستاذة باحثة في جامعة هيوستن ومؤلفة كتب حققت مبيعات قياسية حول سيكولوجيا الهشاشة (Vulnerability)، والخجل، والتعاطف، والشجاعة العاطفية.",
        "works": ["The Gifts of Imperfection (2010)", "Daring Greatly (2012)", "Rising Strong (2015)"],
        "related": [
            {"id": "wrk-daring-greatly", "title": "الشجاعة العظيمة", "type": "عمل / كتاب"},
            {"id": "wrk-gifts-of-imperfection", "title": "هبات النقص", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-jordan-peterson",
        "title": "جوردان بيترسون",
        "en": "Jordan B. Peterson",
        "dates": "كندا · 1962–",
        "country": "كندا",
        "language": "الإنجليزية",
        "active_start": 1993,
        "active_end": "مستمر",
        "school": "علم النفس الإكلينيكي وعلم النفس الشعبي",
        "is_pop": True,
        "lede": "عالم نفس إكلينيكي وأستاذ فخري بجامعة تورنتو ومؤلف كندي، اشتهر بدمج علم النفس اليونغي، وعلم الأحياء التطوري، والمسؤولية الفردية في كتبه ومحاضراته الجماهيرية واسعة التأثير والجدل.",
        "works": ["Maps of Meaning: The Architecture of Belief (1999)", "12 Rules for Life: An Antidote to Chaos (2018)", "Beyond Order: 12 More Rules for Life (2021)"],
        "related": [
            {"id": "wrk-12-rules-for-life", "title": "12 قاعدة للحياة", "type": "عمل / كتاب"},
            {"id": "thk-jung", "title": "كارل غوستاف يونغ", "type": "مفكر"}
        ]
    },
    {
        "slug": "thk-mark-manson",
        "title": "مارك مانسون",
        "en": "Mark Manson",
        "dates": "الولايات المتحدة · 1984–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2011,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والتنمية الذاتية",
        "is_pop": True,
        "lede": "كاتب ومدون أمريكي، اشتهر بأسلوبه الصريح والناقد للإيجابية السامة والتنمية الذاتية التقليدية، مقدماً مقاربة وجودية واقعية للمرونة وتقبل الألم.",
        "works": ["The Subtle Art of Not Giving a F*ck (2016)", "Everything Is F*cked: A Book About Hope (2019)"],
        "related": [
            {"id": "wrk-subtle-art", "title": "فن اللامبالاة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-gretchen-rubin",
        "title": "غريتشين روبين",
        "en": "Gretchen Rubin",
        "dates": "الولايات المتحدة · 1965–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2009,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي وعلم نفس السعادة",
        "is_pop": True,
        "lede": "مؤلفة وباحثة أمريكية في سيكولوجيا العادات والسعادة الإنسانية والطبيعة البشرية، ومبتكرة نموذج الميول الأربعة (The Four Tendencies).",
        "works": ["The Happiness Project (2009)", "Better Than Before (2015)", "The Four Tendencies (2017)"],
        "related": [
            {"id": "wrk-happiness-project", "title": "مشروع السعادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-gabor-mate",
        "title": "غابور ماتيه",
        "en": "Gabor Maté",
        "dates": "كندا / المجر · 1944–",
        "country": "كندا",
        "language": "الإنجليزية",
        "active_start": 1999,
        "active_end": "مستمر",
        "school": "الطب النفسي الجسدي وعلاج الصدمات",
        "is_pop": True,
        "lede": "طبيب وكاتب كندي مجري الأصل، رائد في استكشاف الروابط بين الصدمات النفسية في الطفولة المبكرة، واضطرابات الإدمان، والأمراض الجسدية المزمنة والمناعية.",
        "works": ["In the Realm of Hungry Ghosts (2008)", "When the Body Says No (2003)", "The Myth of Normal: Trauma, Illness and Healing in a Toxic Culture (2022)"],
        "related": [
            {"id": "wrk-myth-of-normal", "title": "أسطورة الطبيعي", "type": "عمل / كتاب"},
            {"id": "wrk-realm-hungry-ghosts", "title": "في عالم الأشباح الجائعة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-james-clear",
        "title": "جيمس كلير",
        "en": "James Clear",
        "dates": "الولايات المتحدة · 1986–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2012,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي وسيكولوجيا العادات",
        "is_pop": True,
        "lede": "كاتب وباحث أمريكي في السلوك البشري واتخاذ القرار، حقق كتابه «العادات الذرية» صدارة مبيعات الكتب العالمية وتُرجم لعشرات اللغات.",
        "works": ["Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones (2018)"],
        "related": [
            {"id": "wrk-atomic-habits", "title": "العادات الذرية", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-charles-duhigg",
        "title": "تشارلز دوهيغ",
        "en": "Charles Duhigg",
        "dates": "الولايات المتحدة · 1974–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2006,
        "active_end": "مستمر",
        "school": "الصحافة العلمية وسيكولوجيا الإنتاجية",
        "is_pop": True,
        "lede": "صحفي استقصائي حائز على جائزة بوليتزر وكاتب في نيويورك تايمز ونيويوركر، اشتهر بتبسيط أبحاث علم الأعصاب والسلوك التنظيمي في كتبه ذائعة الصيت.",
        "works": ["The Power of Habit: Why We Do What We Do in Life and Business (2012)", "Smarter Faster Better (2016)", "Supercommunicators (2024)"],
        "related": [
            {"id": "wrk-power-of-habit", "title": "قوة العادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-dan-kiley",
        "title": "دان كايلي",
        "en": "Dan Kiley",
        "dates": "الولايات المتحدة · 1941–1996",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "1996",
        "school": "علم النفس الشعبي والإرشاد الأسري",
        "is_pop": True,
        "lede": "معالج نفسي ومؤلف أمريكي، اشتهر بصياغة وتعميم مفهوم «متلازمة بيتر بان» لوصف عجز الرجال النفسي والوجداني عن النضج وتحمل المسؤولية البالغة.",
        "works": ["The Peter Pan Syndrome: Men Who Have Never Grown Up (1983)", "The Wendy Dilemma (1984)"],
        "related": [
            {"id": "wrk-peter-pan-syndrome", "title": "متلازمة بيتر بان", "type": "عمل / كتاب"},
            {"id": "con-peter-pan-complex", "title": "متلازمة / عقدة بيتر بان", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-colette-dowling",
        "title": "كوليت داولينغ",
        "en": "Colette Dowling",
        "dates": "الولايات المتحدة · 1938–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "2010",
        "school": "علم النفس الشعبي والدراسات النسوية",
        "is_pop": True,
        "lede": "معالجة نفسية وكاتبة أمريكية، اشتهرت بصياغة مفهوم «عقدة سندريلا» الذي يصف الخوف اللاواعي لدى بعض النساء من الاستقلال والاعتماد الذاتي ورغبتهن الخفية في الخلاص الخارجي.",
        "works": ["The Cinderella Complex: Women's Hidden Fear of Independence (1981)", "Perfect Women (1988)", "You Mean I Don't Have to Feel This Way? (1991)"],
        "related": [
            {"id": "wrk-cinderella-complex", "title": "عقدة سندريلا", "type": "عمل / كتاب"},
            {"id": "con-cinderella-complex", "title": "عقدة سندريلا", "type": "مفهوم"}
        ]
    }
]

out_dir = "content/ar/drafts/thinkers"
os.makedirs(out_dir, exist_ok=True)

for item in thinkers_data:
    lines = ["---"]
    lines.append(f'slug: "{item["slug"]}"')
    lines.append('id: "[DRAFT-UNKNOWN]"')
    lines.append('type: "مفكر"')
    lines.append('part: "psychology"')
    if item["is_pop"]:
        lines.append('register: "popular"')
    lines.append('level: "متوسط"')
    lines.append(f'title: "{item["title"]}"')
    lines.append(f'en: "{item["en"]}"')
    lines.append(f'crumb: "{item["school"]} ← الناس ← {item["title"]}"')
    lines.append(f'dates: "{item["dates"]}"')
    lines.append(f'country: "{item["country"]}"')
    lines.append(f'language: "{item["language"]}"')
    lines.append(f'active_start: {item["active_start"]}')
    lines.append('active_end: "مستمر"' if item["active_end"] == "مستمر" else f'active_end: {item["active_end"]}')
    lines.append("edges:")
    lines.append(f'  - rel: "belongs_to", target: "{item["school"]}", target_type: "مدرسة"')
    lines.append("related:")
    for rel in item["related"]:
        lines.append(f'  - id: "{rel["id"]}", title: "{rel["title"]}", type: "{rel["type"]}"')
    lines.append("gaps:")
    lines.append('  - "بيانات السيرة الذاتية الدقيقة وتاريخ المنشورات تحتاج مراجعة بيبلوغرافية إضافية."')
    lines.append('  - "لا يوجد اقتباس مباشر موثوق متاح."')
    lines.append("---")
    lines.append("")
    lines.append(f'# {item["title"]}')
    lines.append("")
    lines.append(item["lede"])
    lines.append("")
    lines.append("## ما أعطاه")
    lines.append("")
    lines.append(f"إسهامات رئيسية في مجال {item['school']}، وصياغة وتعميم مفاهيم إنسانية وعلاجية وتطبيقية.")
    lines.append("")
    lines.append("## أهم أعماله")
    lines.append("")
    for w in item["works"]:
        lines.append(f"- *{w}*")
    lines.append("")
    lines.append("## اقتباسات مختارة")
    lines.append("")
    lines.append("لا يوجد اقتباس مباشر موثوق متاح.")
    lines.append("")

    filepath = os.path.join(out_dir, f"{item['slug']}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"Wrote {filepath}")

print("All thinkers written successfully.")
