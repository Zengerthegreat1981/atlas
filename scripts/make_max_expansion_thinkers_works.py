# -*- coding: utf-8 -*-
import os

thinkers_data = [
    {
        "slug": "thk-adam-grant",
        "title": "آدم غرانت",
        "en": "Adam Grant",
        "dates": "الولايات المتحدة · 1981–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2007,
        "active_end": "مستمر",
        "school": "علم النفس التنظيمي والدافعية",
        "is_pop": False,
        "lede": "أستاذ علم النفس التنظيمي بجامعة بنسلفانيا (كلية وارتون) ومؤلف تصدرت كتبه قوائم نيويورك تايمز؛ ركزت أبحاثه على سيكولوجيا العطاء المؤسسي، وإعادة التفكير والمرونة الإدراكية في كتب مثل «الأخذ والعطاء» و«فكر مجدداً».",
        "works": ["Give and Take (2013)", "Originals (2016)", "Think Again: The Power of Knowing What You Don't Know (2021)", "Hidden Potential (2023)"],
        "related": [
            {"id": "wrk-think-again", "title": "فكر مرة أخرى", "type": "عمل / كتاب"},
            {"id": "wrk-give-and-take", "title": "الأخذ والعطاء", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-tali-sharot",
        "title": "تالي شاروت",
        "en": "Tali Sharot",
        "dates": "إسرائيل / المملكة المتحدة · 1975–",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 2005,
        "active_end": "مستمر",
        "school": "علم الأعصاب الإدراكي والانفعالي",
        "is_pop": False,
        "lede": "أستاذة علم الأعصاب الإدراكي بكلية لندن الجامعية (UCL) ومديرة مختبر الدماغ العاطفي؛ رائدة أبحاث 'انحياز التفاؤل الفطري' (The Optimism Bias) وسيكولوجيا التأثير وتغيير المعتقدات.",
        "works": ["The Optimism Bias (2011)", "The Influential Mind (2017)", "Look Again: The Power of Noticing What Was Always There (2024)"],
        "related": [
            {"id": "wrk-optimism-bias", "title": "انحياز التفاؤل", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-uri-gneezy",
        "title": "أوري غنيزي",
        "en": "Uri Gneezy",
        "dates": "إسرائيل / الولايات المتحدة · 1967–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 1997,
        "active_end": "مستمر",
        "school": "الاقتصاد السلوكي والدافعية التجريبية",
        "is_pop": False,
        "lede": "أستاذ الاقتصاد السلوكي بجامعة كاليفورنيا في سان دييغو (UCSD)؛ اشتهر بتجاربه الميدانية الرائدة حول الآثار العكسية للحوافز والغرامات المالية وسيكولوجيا التسعير في كتابه «المحور الخفي».",
        "works": ["The Why Axis: Hidden Motives and the Undiscovered Economics of Everyday Life (with John List, 2013)", "Mixed Signals (2023)"],
        "related": [
            {"id": "wrk-predictably-irrational", "title": "اللامنطقية المتوقعة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-john-cacioppo",
        "title": "جون كاسيوبو",
        "en": "John Cacioppo",
        "dates": "الولايات المتحدة · 1951–2018",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": 2018,
        "school": "علم الأعصاب الاجتماعي وسيكولوجيا الوحدة",
        "is_pop": False,
        "lede": "عالم نفس رائد ومؤسس مشارك لمجال 'علم الأعصاب الاجتماعي' (Social Neuroscience) وأستاذ متميز بجامعة شيكاغو؛ كشفت أبحاثه الرائدة في كتابه «الوحدة» عن الأثر الفسيولوجي والمناعي المدمر للعزلة الاجتماعية غير الطوعية.",
        "works": ["Loneliness: Human Nature and the Need for Social Connection (2008)", "Social Neuroscience: People Thinking about Thinking People (2005)"],
        "related": [
            {"id": "wrk-loneliness-cacioppo", "title": "الوحدة: الطبيعة البشرية", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-roy-baumeister",
        "title": "روي باوميستر",
        "en": "Roy Baumeister",
        "dates": "الولايات المتحدة · 1953–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1978,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي والتنظيم الذاتي",
        "is_pop": False,
        "lede": "أحد أكثر علماء النفس استشهاداً في العالم وأستاذ بجامعة كوينزلاند؛ اشتهر بصياغة نظرية 'استنزاف الأنا' (Ego Depletion) وأبحاث التحكم الذاتي وقوة الإرادة والإشباع المؤجل في كتابه «قوة الإرادة».",
        "works": ["Willpower: Rediscovering the Greatest Human Strength (2011)", "The Cultural Animal (2005)", "Evil: Inside Human Violence and Cruelty (1997)"],
        "related": [
            {"id": "wrk-willpower-baumeister", "title": "قوة الإرادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-george-lakoff",
        "title": "جورج لاكوف",
        "en": "George Lakoff",
        "dates": "الولايات المتحدة · 1941–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1968,
        "active_end": "مستمر",
        "school": "اللسانيات المعرفية وعلم النفس السياسي",
        "is_pop": False,
        "lede": "أستاذ فخري للعلوم اللغوية والإدراكية بجامعة كاليفورنيا في بيركلي؛ رائد نظرية 'الاستعارة المعرفية المجسدة' وصاحب الأثر الهائل في صياغة مفهوم 'التأطير اللغوي' في كتابه «لا تفكر في فيل».",
        "works": ["Metaphors We Live By (with Mark Johnson, 1980)", "Don't Think of an Elephant! (2004)", "Moral Politics (1996)"],
        "related": [
            {"id": "wrk-dont-think-of-an-elephant", "title": "لا تفكر في فيل", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-robert-kegan",
        "title": "روبرت كيغان",
        "en": "Robert Kegan",
        "dates": "الولايات المتحدة · 1946–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "مستمر",
        "school": "علم النفس التنموي للبالغين والقيادة التكيفية",
        "is_pop": False,
        "lede": "أستاذ علم النفس التنموي الفخري بجامعة هارفارد؛ صاغ نظرية 'المراحل الخمس لتطور الوعي في الرشد' وابتكر مع ليزا ليهي أداة 'المناعة النفسية ضد التغيير' لتفكيك الالتزامات الخفية المعيقة للتطور.",
        "works": ["The Evolving Self (1982)", "In Over Our Heads (1994)", "Immunity to Change (with Lisa Lahey, 2009)", "An Everyone Culture (2016)"],
        "related": [
            {"id": "wrk-immunity-to-change", "title": "المناعة ضد التغيير", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-sheena-iyengar",
        "title": "شينا إينغار",
        "en": "Sheena Iyengar",
        "dates": "كندا / الولايات المتحدة · 1969–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي واتخاذ القرار",
        "is_pop": False,
        "lede": "أستاذة متميزة في كلية الأعمال بجامعة كولومبيا؛ قائدة 'تجربة المربى' التاريخية التي أثبتت شلل الخيارات وفرط البدائل، ومؤلفة كتاب «فن الاختيار».",
        "works": ["The Art of Choosing (2010)", "Think Bigger (2023)"],
        "related": [
            {"id": "wrk-art-of-choosing", "title": "فن الاختيار", "type": "عمل / كتاب"},
            {"id": "con-paradox-of-choice", "title": "مفارقة الاختيار وشلل القرار", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-bj-fogg",
        "title": "بي جيه فوغ",
        "en": "B.J. Fogg",
        "dates": "الولايات المتحدة · 1963–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1998,
        "active_end": "مستمر",
        "school": "تصميم السلوك والتقنية الإقناعية",
        "is_pop": False,
        "lede": "مؤسس ومدير مختبر تصميم السلوك بجامعة ستانفورد؛ ابتكر 'نموذج فوغ السلوكي' (B=MAP) ومنهجية 'العادات الصغيرة' التي تخرج منها كبار رواد تصميم المنتجات والتطبيقات في وادي السيليكون.",
        "works": ["Persuasive Technology (2003)", "Tiny Habits: The Small Changes That Change Everything (2019)"],
        "related": [
            {"id": "wrk-tiny-habits", "title": "العادات الصغيرة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-guy-winch",
        "title": "غاي وينش",
        "en": "Guy Winch",
        "dates": "الولايات المتحدة · 1962–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1995,
        "active_end": "مستمر",
        "school": "علم النفس الإكلينيكي والنظافة العاطفية",
        "is_pop": True,
        "lede": "طبيب نفسي إكلينيكي ومتحدث TED شهير ومؤلف؛ اشتهر بالدعوة لممارسة 'النظافة العاطفية اليومية' وتقديم بروتوكولات عملية لعلاج الجروح النفسية كالرفض والشعور بالذنب والفقد في كتابه «الإسعافات الأولية العاطفية».",
        "works": ["Emotional First Aid (2013)", "How to Fix a Broken Heart (2018)", "The Squeaky Wheel (2011)"],
        "related": [
            {"id": "wrk-emotional-first-aid", "title": "الإسعافات الأولية العاطفية", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-alain-de-botton",
        "title": "آلان دو بوتون",
        "en": "Alain de Botton",
        "dates": "سويسرا / المملكة المتحدة · 1969–",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية / الفرنسية",
        "active_start": 1993,
        "active_end": "مستمر",
        "school": "الفلسفة النفسية التطبيقية ومدرسة الحياة",
        "is_pop": True,
        "lede": "فيلسوف وكاتب بريطاني-سويسري ومؤسس منظمة 'مدرسة الحياة' (The School of Life)؛ اشتهر بتبسيط الفلسفة وعلم النفس لمساعدة الإنسان المعاصر على فهم الحب، العمل، وقلق المكانة الاجتماعية.",
        "works": ["Status Anxiety (2004)", "The Course of Love (2016)", "Essays in Love (1993)", "The Consolations of Philosophy (2000)"],
        "related": [
            {"id": "wrk-status-anxiety", "title": "قلق السعي إلى المكانة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-jay-shetty",
        "title": "جاي شيتي",
        "en": "Jay Shetty",
        "dates": "المملكة المتحدة · 1987–",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية",
        "active_start": 2016,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي واليقظة الذهنية",
        "is_pop": True,
        "lede": "راهب فيدي سابق ومدرب ومؤلف بريطاني؛ حقق كتابه «فكر كراهب» صدارة المبيعات العالمية بملايين النسخ عبر ترجمة الحكمة الرهبانية القديمة إلى ممارسات يومية للسلام الداخلي والهدف.",
        "works": ["Think Like a Monk (2020)", "8 Rules of Love (2023)"],
        "related": [
            {"id": "wrk-think-like-a-monk", "title": "فكر كراهب", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-dan-millman",
        "title": "دان ميلمان",
        "en": "Dan Millman",
        "dates": "الولايات المتحدة · 1946–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1980,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي وسيكولوجيا الأداء والوعي",
        "is_pop": True,
        "lede": "بطل جمباز عالمي سابق وأستاذ تربية بدنية ومؤلف؛ حققت روايته شبه الذاتية «طريق المحارب السلمي» انتشاراً ملهماً بالملايين حول دمج تدريب الجسد باليقظة الروحية والعيش في الحاضر.",
        "works": ["Way of the Peaceful Warrior (1980)", "The Life You Were Born to Live (1995)", "No Ordinary Moments (1992)"],
        "related": [
            {"id": "wrk-way-of-the-peaceful-warrior", "title": "طريق المحارب السلمي", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-rhonda-byrne",
        "title": "روندا بايرن",
        "en": "Rhonda Byrne",
        "dates": "أستراليا · 1951–",
        "country": "أستراليا",
        "language": "الإنجليزية",
        "active_start": 2006,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي وقانون الجذب",
        "is_pop": True,
        "lede": "منتجة ومؤلفة أسترالية؛ أحدث كتابها وفيلمها الوثائقي «السر» (The Secret) ظاهرة عالمية ساحقة ببيعه أكثر من 30 مليون نسخة حول نشر مفهوم 'قانون الجذب' (Law of Attraction).",
        "works": ["The Secret (2006)", "The Power (2010)", "The Magic (2012)", "The Greatest Secret (2020)"],
        "related": [
            {"id": "wrk-the-secret", "title": "السر: قانون الجذب", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-mitch-albom",
        "title": "ميتش ألبوم",
        "en": "Mitch Albom",
        "dates": "الولايات المتحدة · 1958–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": "مستمر",
        "school": "السرديات النفسية والإنسانية",
        "is_pop": True,
        "lede": "صحفي وكاتب وروائي أمريكي؛ حقق كتابه «ثلاثاءات مع موري» مبيعات استثنائية تتجاوز 18 مليون نسخة وظل في قائمة نيويورك تايمز لأكثر من أربع سنوات، مقدماً دروساً وجودية في معنى الحياة ومواجهة الموت.",
        "works": ["Tuesdays with Morrie (1997)", "The Five People You Meet in Heaven (2003)", "For One More Day (2006)"],
        "related": [
            {"id": "wrk-tuesdays-with-morrie", "title": "ثلاثاءات مع موري", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-oliver-burkeman",
        "title": "أوليفر بوركمان",
        "en": "Oliver Burkeman",
        "dates": "المملكة المتحدة · 1975–",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية",
        "active_start": 2010,
        "active_end": "مستمر",
        "school": "الفلسفة النفسية ونقد الإنتاجية السامة",
        "is_pop": True,
        "lede": "كاتب وصحفي بريطاني سابق في الغارديان؛ اشتهر بكتابه الرائد «أربعة آلاف أسبوع» الذي يفكك هوس الإنتاجية المعاصرة ويدعو لتقبل محدودية العمر البشري والفناء كمدخل وحيد للحرية والسلام الداخلي.",
        "works": ["The Antidote: Happiness for People Who Can't Stand Positive Thinking (2012)", "Four Thousand Weeks: Time Management for Mortals (2021)", "Meditations for Mortals (2024)"],
        "related": [
            {"id": "wrk-four-thousand-weeks", "title": "أربعة آلاف أسبوع", "type": "عمل / كتاب"}
        ]
    }
]

out_dir_thk = "content/ar/drafts/thinkers"
os.makedirs(out_dir_thk, exist_ok=True)

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
    lines.append('  - "بيانات السيرة الذاتية وتاريخ المنشورات تحتاج مراجعة بيبلوغرافية إضافية."')
    lines.append('  - "لا يوجد اقتباس مباشر موثوق متاح."')
    lines.append("---")
    lines.append("")
    lines.append(f'# {item["title"]}')
    lines.append("")
    lines.append(item["lede"])
    lines.append("")
    lines.append("## ما أعطاه")
    lines.append("")
    lines.append(f"إسهامات نوعية ومؤثرة في مجال {item['school']} وإثراء المكتبة السيكولوجية العالمية.")
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

    filepath = os.path.join(out_dir_thk, f"{item['slug']}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"Wrote {filepath}")

# Works Data
works_data = [
    {
        "slug": "wrk-think-again",
        "title": "فكر مرة أخرى: قوة معرفة ما لا تعرفه",
        "en": "Think Again: The Power of Knowing What You Don't Know",
        "dates": "2021 · آدم غرانت",
        "language": "الإنجليزية",
        "active_start": 2021,
        "active_end": "2021",
        "school": "علم النفس التنظيمي والدافعية",
        "author_id": "thk-adam-grant",
        "author_title": "آدم غرانت",
        "lede": "كتاب تصدر قوائم نيويورك تايمز للبِست سيلر؛ يدعو لتبني 'عقلية العالم' كبديل عن عقليات الواعظ والمدعي العام والسياسي، مقدماً أدوات لإعادة النظر في القناعات والتخلص من الجمود الفكري.",
        "sections": [
            ("العقليات الثلاث المعيقة مقابل عقلية العالم", "الواعظ (يدافع عن أفكاره بقداسة)، المدعي العام (يهاجم آراء الآخرين)، والسياسي (يسعى للاستحسان)؛ بينما العالم يبحث عن الحقيقة ويعتبر الخطأ فرصة للتعلم."),
            ("متعة اكتشاف الخطأ", "تحرير الثقة بالنفس من الارتباط بالأفكار المؤقتة وجعلها مرتبطة بالقيم والقدرة على التعلم المستمر.")
        ]
    },
    {
        "slug": "wrk-give-and-take",
        "title": "الأخذ والعطاء: نهج ثوري للنجاح",
        "en": "Give and Take: A Revolutionary Approach to Success",
        "dates": "2013 · آدم غرانت",
        "language": "الإنجليزية",
        "active_start": 2013,
        "active_end": "2013",
        "school": "علم النفس التنظيمي والدافعية",
        "author_id": "thk-adam-grant",
        "author_title": "آدم غرانت",
        "lede": "دراسة سيكولوجية تنظيمية كبرى تقسم البشر في بيئات العمل إلى 3 أنماط تفاعلية: الآخذون (Takers)، المقايضون (Matchers)، والمعطاؤون (Givers)، وتثبت أن المعطائين الأذكياء هم من يتصدرون قمة النجاح المستدام عالمياً.",
        "sections": [
            ("المعطاء الساذج مقابل المعطاء الاستراتيجي", "الفرق بين العطاء غير المشروط الذي يقود للاحتراق الوظيفي، وبين العطاء الواعي الذي يبني شبكات ثقة قوية دون السماح بالاستغلال."),
            ("تأثير بيئات العطاء على إنتاجية المؤسسات", "كيف ترفع ثقافة العطاء والتعاون من أرباح وإبداع المؤسسات مقارنة ببيئات التنافس الأناني.")
        ]
    },
    {
        "slug": "wrk-the-secret",
        "title": "السر: قانون الجذب",
        "en": "The Secret",
        "dates": "2006 · روندا بايرن",
        "language": "الإنجليزية",
        "active_start": 2006,
        "active_end": "2006",
        "school": "علم النفس الشعبي وقانون الجذب",
        "author_id": "thk-rhonda-byrne",
        "author_title": "روندا بايرن",
        "lede": "الظاهرة التجارية الكبرى في القرن الحادي والعشرين (أكثر من 30 مليون نسخة بـ 50 لغة)؛ تطرح أن أفكار الإنسان ومشاعره تمتلك ترددات كهرومغناطيسية تجذب تلقائياً الأحداث المماثلة لها في الواقع (الشبيه يجذب شبيهه).",
        "sections": [
            ("الخطوات الثلاث للاستجابة", "اطلب (Ask)، آمن (Believe)، واستقبل المشاعر وكأن الهدف تحقق بالفعل (Receive)."),
            ("النقد السيكولوجي والعلمي", "التحذير من لوم الضحايا وتسطيح أسباب الفقر والمرض، مع الإقرار بأثر التفاؤل والتركيز الذهني الإيجابي في توجيه الانتباه نحو الفرص.")
        ]
    },
    {
        "slug": "wrk-think-like-a-monk",
        "title": "فكر كراهب: درب عقلك على السلام والهدف كل يوم",
        "en": "Think Like a Monk",
        "dates": "2020 · جاي شيتي",
        "language": "الإنجليزية",
        "active_start": 2020,
        "active_end": "2020",
        "school": "علم النفس الشعبي واليقظة الذهنية",
        "author_id": "thk-jay-shetty",
        "author_title": "جاي شيتي",
        "lede": "كتاب تصدر قوائم المبيعات العالمية؛ يدمج الحكمة الفيدية الرهبانية بالأبحاث النفسية المعاصرة لمساعدة القارئ على التخلص من السموم الفكرية والمقارنات الاجتماعية وتحديد الغرض الحياتي (Dharma).",
        "sections": [
            ("الأركان الثلاثة", "1. التخلي (Let Go): تصفية الضوضاء السلبية والآراء الموروثة. 2. النمو (Grow): إعادة توجيه الانتباه والامتنان. 3. العطاء (Give): خدمة الآخرين كقمة التحقق الروحي."),
            ("روتين الصباح وإدارة الأنا", "تمارين التنفس الواعي وتفكيك انتفاخ الأنا النرجسي.")
        ]
    },
    {
        "slug": "wrk-tuesdays-with-morrie",
        "title": "ثلاثاءات مع موري: رجل عجوز وشاب ودرس الحياة الأعظم",
        "en": "Tuesdays with Morrie",
        "dates": "1997 · ميتش ألبوم",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": "1997",
        "school": "السرديات النفسية والإنسانية",
        "author_id": "thk-mitch-albom",
        "author_title": "ميتش ألبوم",
        "lede": "مذكرات إنسانية وسيكولوجية خالدة (أكثر من 18 مليون نسخة)؛ توثق لقاءات أسبوعية كل يوم ثلاثاء بين صحفي شاب وأستاذه الجامعي العجوز موري شوارتز وهو يحتضر بمرض التصلب الجانبي الضموري (ALS)، متعلماً أسرار العاطفة ومسامحة الذات والعيش بوعي.",
        "sections": [
            ("دروس موري في الثقافة والحب والفناء", "'بمجرد أن تتعلم كيف تموت، ستتعلم كيف تعيش'؛ وضرورة رفض الثقافة الاستهلاكية التي تخدع الناس بأولويات زائفة."),
            ("الأثر الوجداني والعلاجي", "إلهام حركة عالمية لإعادة تقييم العلاقات الأسرية ومواجهة حتمية الفقد بالحب الصادق.")
        ]
    },
    {
        "slug": "wrk-status-anxiety",
        "title": "قلق السعي إلى المكانة: الشعور بالدونية والبحث عن التقدير",
        "en": "Status Anxiety",
        "dates": "2004 · آلان دو بوتون",
        "language": "الإنجليزية",
        "active_start": 2004,
        "active_end": "2004",
        "school": "الفلسفة النفسية التطبيقية ومدرسة الحياة",
        "author_id": "thk-alain-de-botton",
        "author_title": "آلان دو بوتون",
        "lede": "تحليل سيكولوجي وثقافي عميق للقلق الخفي المؤلم الذي يصيب الإنسان المعاصر من خوفه من الفشل في تلبية معايير النجاح المفروضة مجتمعياً وتجريده من التقدير والاحترام، كاشفاً جذوره في الجدارة الزائفة وسوق العمل.",
        "sections": [
            ("أسباب قلق المكانة الخمسة", "انعدام الحب، الغرور والمباهاة، التطلع والمقارنة بالأقران، وهم الجدارة، والاعتمادية على تقلبات الاقتصاد."),
            ("الحلول الخمسة الشافية", "الفلسفة، الفن، السياسة، الديانة، والموت وتأمل عظمة الطبيعة لتحجيم التفاهات اليومية.")
        ]
    },
    {
        "slug": "wrk-emotional-first-aid",
        "title": "الإسعافات الأولية العاطفية: علاج الفشل والرفض والشعور بالذنب وجروح الحياة اليومية",
        "en": "Emotional First Aid",
        "dates": "2013 · غاي وينش",
        "language": "الإنجليزية",
        "active_start": 2013,
        "active_end": "2013",
        "school": "علم النفس الإكلينيكي والنظافة العاطفية",
        "author_id": "thk-guy-winch",
        "author_title": "غاي وينش",
        "lede": "دليل علاجي وعملي يقارن بين الإسعافات الجسدية للجروح والإسعافات النفسية اللازمة للجروح العاطفية اليومية (الرفض، الوحدة، الفقد، الشعور بالذنب، الاجترار، الفشل، وتدني احترام الذات)، مقدماً بروتوكولات سلوكية فورية.",
        "sections": [
            ("علاج ألم الرفض والاجترار", "وقف نزيف التدمير الذاتي بالتعاطف مع الذات وإعادة بناء الكفاءة الشخصية."),
            ("النظافة العاطفية الوقائية", "التدريب على تنظيف الجروح النفسية الصغيرة قبل أن تتفاقم إلى اكتئاب وقلق سريري.")
        ]
    },
    {
        "slug": "wrk-willpower-baumeister",
        "title": "قوة الإرادة: إعادة اكتشاف أعظم طاقة بشرية",
        "en": "Willpower: Rediscovering the Greatest Human Strength",
        "dates": "2011 · روي باوميستر وجون تيرني",
        "language": "الإنجليزية",
        "active_start": 2011,
        "active_end": "2011",
        "school": "علم النفس الاجتماعي والتنظيم الذاتي",
        "author_id": "thk-roy-baumeister",
        "author_title": "روي باوميستر",
        "lede": "كتاب رائد يلخص عقوداً من أبحاث علم النفس التجريبي لإثبات أن قوة الإرادة ليست فضيلة مجردة بل 'طاقة بيولوجية محدودة كالعضلة' تستنزف بالجهد وتتغذى على الجلوكوز، مقدماً استراتيجيات علمية لإدارتها.",
        "sections": [
            ("آلية استنزاف الإرادة (Ego Depletion)", "كيف يؤدي اتخاذ قرارات متكررة أو مقاومة إغراءات في الصباح إلى انهيار ضبط النفس في المساء."),
            ("الحفاظ على الطاقة عبر الأتمتة والعادات", "تقليل الاعتماد على الإرادة اللحظية عبر هندسة البيئة وبناء عادات وروتينات تلقائية.")
        ]
    },
    {
        "slug": "wrk-optimism-bias",
        "title": "انحياز التفاؤل: جولة في الدماغ المبرمج إيجابياً",
        "en": "The Optimism Bias: A Tour of the Irrationally Positive Brain",
        "dates": "2011 · تالي شاروت",
        "language": "الإنجليزية",
        "active_start": 2011,
        "active_end": "2011",
        "school": "علم الأعصاب الإدراكي والانفعالي",
        "author_id": "thk-tali-sharot",
        "author_title": "تالي شاروت",
        "lede": "كتاب يستعرض أبحاث تصوير الدماغ بالرنين المغناطيسي لإثبات أن 80% من البشر مبرمجون عصبياً بـ 'انحياز التفاؤل' التلقائي (المبالغة في تقدير احتمالية الأحداث الإيجابية والتقليل من احتمالية الكوارث كالطلاق أو المرض).",
        "sections": [
            ("الفائدة التطورية للوهم الإيجابي", "كيف يحمي انحياز التفاؤل الإنسان من القلق الشال ويدفعه للاستكشاف والمبادرة والإنجاز."),
            ("موازنة المخاطر", "كيفية التمتع بالتفاؤل مع اتخاذ تدابير واقعية للحماية من المخاطر المحتملة.")
        ]
    },
    {
        "slug": "wrk-dont-think-of-an-elephant",
        "title": "لا تفكر في فيل: الأطر اللغوية والمعرفية في السياسة والفكر",
        "en": "Don't Think of an Elephant!",
        "dates": "2004 · جورج لاكوف",
        "language": "الإنجليزية",
        "active_start": 2004,
        "active_end": "2004",
        "school": "اللسانيات المعرفية وعلم النفس السياسي",
        "author_id": "thk-george-lakoff",
        "author_title": "جورج لاكوف",
        "lede": "الكتاب التأسيسي في سيكولوجيا 'التأطير المعرفي واللغوي' (Framing)؛ يشرح كيف تحدد الكلمات والأطر الاستعارية اللاواعية طريقة فهم وتصويت وتفكير الجماهير، وأن تكرار لغة الخصم حتى لنفيها يعزز إطاره الذهني في أدمغة السامعين.",
        "sections": [
            ("استعارة 'الأب الصارم' و'الوالد الراعي'", "النماذج الأخلاقية اللاواعية التي تشكل الفكر المحافظ والليبرالي."),
            ("قواعد صياغة الأطر المستقلة", "بناء لغة إيجابية تعبر عن قيمك الخاصة بدلاً من الرد الدائم داخل أطر المنافسين.")
        ]
    },
    {
        "slug": "wrk-loneliness-cacioppo",
        "title": "الوحدة: الطبيعة البشرية والحاجة للترابط الاجتماعي",
        "en": "Loneliness: Human Nature and the Need for Social Connection",
        "dates": "2008 · جون كاسيوبو وويليام باتريك",
        "language": "الإنجليزية",
        "active_start": 2008,
        "active_end": "2008",
        "school": "علم الأعصاب الاجتماعي وسيكولوجيا الوحدة",
        "author_id": "thk-john-cacioppo",
        "author_title": "جون كاسيوبو",
        "lede": "مرجع علمي وعصبي رائد يثبت أن الشعور بالوحدة ليس عيباً شخصياً بل 'إشارة تحذير بيولوجية كالجوع والعطش' تنبه الدماغ لضرورة حماية الذات والترابط، مبيناً أثرها المدمر على ارتفاع ضغط الدم والالتهابات وتراجع المناعة.",
        "sections": [
            ("فرط الاستثارة والبارانويا الاجتماعية", "كيف تجعل الوحدة الدماغ يفسر الإشارات الاجتماعية العادية كتهديدات عدائية."),
            ("إعادة الاتصال والتنظيم الذاتي", "خطوات الخروج من فخ العزلة عبر بناء علاقات قائمة على الثقة والتعاطف المتبادل.")
        ]
    },
    {
        "slug": "wrk-art-of-choosing",
        "title": "فن الاختيار: سيكولوجيا القرارات اليومية والمصيرية",
        "en": "The Art of Choosing",
        "dates": "2010 · شينا إينغار",
        "language": "الإنجليزية",
        "active_start": 2010,
        "active_end": "2010",
        "school": "علم النفس الاجتماعي واتخاذ القرار",
        "author_id": "thk-sheena-iyengar",
        "author_title": "شينا إينغار",
        "lede": "كتاب يستكشف سيكولوجيا الاختيار الإنساني وتأثيراته الثقافية والبيولوجية؛ يوضح كيف يتشكل الاختيار عبر التوقعات، ولماذا تؤدي كثرة البدائل لشلل التفكير، وكيف تتفاوت رغبة التحكم بين الثقافات الفردية والجماعية.",
        "sections": [
            ("تجربة المربى الشهيرة (24 خياراً مقابل 6 خيارات)", "جذب العرض الأكبر متفرجين أكثر لكن العرض الأقل حقق مبيعات أعلى بعشرة أضعاف."),
            ("تطوير مهارات التصفية والاختيار الحكيم", "استراتيجيات الحد من عبء القرار وتصنيف الأولويات.")
        ]
    },
    {
        "slug": "wrk-immunity-to-change",
        "title": "المناعة ضد التغيير: كيف نتغلب على الحواجز اللاواعية لتحقيق أهدافنا",
        "en": "Immunity to Change",
        "dates": "2009 · روبرت كيغان وليزا ليهي",
        "language": "الإنجليزية",
        "active_start": 2009,
        "active_end": "2009",
        "school": "علم النفس التنموي للبالغين والقيادة التكيفية",
        "author_id": "thk-robert-kegan",
        "author_title": "روبرت كيغان",
        "lede": "دليل تطبيقي رائد يكشف عن 'جهاز المناعة النفسي اللاواعي' الذي يمنع الأفراد والقادة من تحقيق التغييرات المنشودة، مقدماً خريطة من 4 أعمدة لكشف 'الالتزامات الخفية المتنافسة' والافتراضات الكبرى المقيدة.",
        "sections": [
            ("خريطة المناعة ضد التغيير (X-Ray Tool)", "1. الهدف الالتزامي. 2. السلوكيات المعاكسة للهدف. 3. الالتزامات المتنافسة الخفية (المخاوف غير المعلنة). 4. الافتراضات الكبرى غير المفحوصة."),
            ("التطور المعرفي للرشد", "الانتقال من العقل التابع اجتماعياً إلى العقل المستقل الموجه ذاتياً.")
        ]
    },
    {
        "slug": "wrk-way-of-the-peaceful-warrior",
        "title": "طريق المحارب السلمي: كتاب يغير الحياة",
        "en": "Way of the Peaceful Warrior",
        "dates": "1980 · دان ميلمان",
        "language": "الإنجليزية",
        "active_start": 1980,
        "active_end": "1980",
        "school": "علم النفس الشعبي وسيكولوجيا الأداء والوعي",
        "author_id": "thk-dan-millman",
        "author_title": "دان ميلمان",
        "lede": "رواية رمزية وفلسفية نفسية واسعة الانتشار؛ تحكي قصة رياضي شاب مغرور يلتقي بمرشد روحي غامض يدعى 'سقراط' يعلمه كيفية تفريغ العقل من الأوهام والتركيز الكامل على 'اللحظة الحاضرة هنا والآن'.",
        "sections": [
            ("المبادئ الثلاثة للمحارب السلمي", "المفارقة (الحياة لغز لا يحل بالعقل فقط)، الفكاهة (التواضع والضحك على الذات)، والتغيير المستمر."),
            ("الأثر في سيكولوجيا الرياضة والحياة", "تحرير الطاقة الإبداعية عبر الحضور الكامل وإلغاء القلق من النتيجة.")
        ]
    },
    {
        "slug": "wrk-alchemist",
        "title": "الخيميائي: رحلة البحث عن الأسطورة الشخصية",
        "en": "The Alchemist",
        "dates": "1988 · باولو كويلو",
        "language": "البرتغالية / الإنجليزية",
        "active_start": 1988,
        "active_end": "1988",
        "school": "السرديات النفسية والرمزية الوجودية",
        "author_id": "thk-coelho-paulo",
        "author_title": "باولو كويلو",
        "lede": "الرواية الرمزية النفسية الأكثر ترجمة ومبيعاً في العصر الحديث (أكثر من 150 مليون نسخة)؛ تروي رحلة الراعي الأندلسي سانتياغو نحو أهرامات مصر بحثاً عن كنزه، مستعرضة مفاهيم 'الأسطورة الشخصية'، والإشارات الكونية، والتحول الداخلي.",
        "sections": [
            ("مفهوم 'الأسطورة الشخصية' (Personal Legend)", "المسار الحقيقي الذي وُلد الإنسان لتحقيقه في الحياة، والتحديات النفسية التي تحاول ثنيه عنه."),
            ("الأثر في التنمية الذاتية المعاصرة", "تحولت الرواية لأيقونة عالمية للشجاعة الوجودية والاستماع لصوت القلب.")
        ]
    },
    {
        "slug": "wrk-tiny-habits",
        "title": "العادات الصغيرة: التغييرات الصغيرة التي تغير كل شيء",
        "en": "Tiny Habits: The Small Changes That Change Everything",
        "dates": "2019 · بي جيه فوغ",
        "language": "الإنجليزية",
        "active_start": 2019,
        "active_end": "2019",
        "school": "تصميم السلوك والتقنية الإقناعية",
        "author_id": "thk-bj-fogg",
        "author_title": "بي جيه فوغ",
        "lede": "كتاب تطبيقي رائد لمدير مختبر ستانفورد للسلوك؛ يوضح أن التغيير الدائم لا يعتمد على التحفيز المتقلب بل على تصغير السلوك لدرجة متناهية الصغر وربطه بعادات يومية ثابتة والاحتفال الفوري به.",
        "sections": [
            ("صيغة العادة الصغيرة (ABC)", "المرساة (Anchor - عادة ثابتة) + السلوك الصغير (Tiny Behavior) + الاحتفال الفوري (Celebration لإفراز الدوبامين)."),
            ("نموذج B=MAP", "السلوك يحدث فقط عند توافر الدافع (Motivation)، والقدرة (Ability)، والمحفز (Prompt) في نفس اللحظة.")
        ]
    },
    {
        "slug": "wrk-scarcity-mullainathan",
        "title": "الندرة: لماذا يعني القليل جداً الكثير جداً",
        "en": "Scarcity: Why Having Too Little Means So Much",
        "dates": "2013 · سيندهيل مولايناثان وإلديل شافير",
        "language": "الإنجليزية",
        "active_start": 2013,
        "active_end": "2013",
        "school": "الاقتصاد السلوكي والعلوم المعرفية",
        "author_id": "thk-mullainathan-sendhil",
        "author_title": "سيندهيل مولايناثان",
        "author_id2": "thk-shafir-eldar",
        "author_title2": "إلديل شافير",
        "lede": "دراسة سلوكية رائدة تثبت أن تجربة 'الندرة' (سواء في المال، أو الوقت، أو السعرات الحرارية) تستحوذ قسراً على 'النطاق الترددي المعرفي' للدماغ (Mental Bandwidth)، مما يقلل معدل الذكاء السائل ويقود لقرارات اندفاعية قصيرة المدى.",
        "sections": [
            ("ضريبة النطاق الترددي المعرفي (Bandwidth Tax)", "يفقد الإنسان ما يعادل 13 إلى 14 نقطة من حاصل ذكائه الفعلي عندما يكون عقله محاصراً بقلق مالي أو ضيق وقت ساحق."),
            ("كسر فخاخ الندرة", "توفير هوامش أمان (Slack) في الميزانيات والجداول الزمنية لاستعادة السيطرة المعرفية.")
        ]
    },
    {
        "slug": "wrk-four-thousand-weeks",
        "title": "أربعة آلاف أسبوع: إدارة الوقت للفانين",
        "en": "Four Thousand Weeks: Time Management for Mortals",
        "dates": "2021 · أوليفر بوركمان",
        "language": "الإنجليزية",
        "active_start": 2021,
        "active_end": "2021",
        "school": "الفلسفة النفسية ونقد الإنتاجية السامة",
        "author_id": "thk-oliver-burkeman",
        "author_title": "أوليفر بوركمان",
        "lede": "كتاب فكري وعلاجي تصدر قوائم نيويورك تايمز؛ يذكر بأن متوسط عمر الإنسان يبلغ حوالي 4000 أسبوع فقط، مبرهناً أن محاولات 'إنجاز كل شيء' عبث مستحيل، وأن السلام الحقيقي يكمن في تقبل فنائنا واختيار ما نهمله بوعي وشجاعة.",
        "sections": [
            ("فخ الكفاءة والإنتاجية اللانهائية", "كلما زادت كفاءتك وسرعتك في الرد على الإيميلات، كلما تدفقت عليك إيميلات أكثر؛ فالحل ليس زيادة السرعة بل اختيار ما يستحق وقتك المحدود."),
            ("بهجة التخلي عن السيطرة المطلقة", "الاعتراف بأننا لا نملك الوقت بل نحن الوقت نفسه، والتركيز على الحضور الكامل في المهام الحالية.")
        ]
    }
]

out_dir_wrk = "content/ar/drafts/works"
os.makedirs(out_dir_wrk, exist_ok=True)

for item in works_data:
    lines = ["---"]
    lines.append(f'slug: "{item["slug"]}"')
    lines.append('id: "[DRAFT-UNKNOWN]"')
    lines.append('type: "عمل / كتاب"')
    lines.append('register: "popular"')
    lines.append('part: "psychology"')
    lines.append('level: "متوسط"')
    lines.append(f'title: "{item["title"]}"')
    lines.append(f'en: "{item["en"]}"')
    lines.append(f'crumb: "{item["school"]} ← الأعمال ← {item["title"].split(":")[0]}"')
    lines.append(f'dates: "{item["dates"]}"')
    lines.append(f'language: "{item["language"]}"')
    lines.append(f'active_start: {item["active_start"]}')
    lines.append(f'active_end: {item["active_end"]}')
    lines.append("edges:")
    lines.append(f'  - rel: "belongs_to", target: "{item["school"]}", target_type: "مدرسة"')
    lines.append(f'  - rel: "written_by", target: "{item["author_title"]}", target_type: "مفكر"')
    lines.append("related:")
    lines.append(f'  - id: "{item["author_id"]}", title: "{item["author_title"]}", type: "مفكر"')
    lines.append("gaps:")
    lines.append('  - "بيانات الطبعة وأرقام الصفحات الدقيقة تحتاج مراجعة بيبلوغرافية إضافية."')
    lines.append('  - "لا يوجد اقتباس مباشر موثوق متاح."')
    lines.append("---")
    lines.append("")
    lines.append(f'# {item["title"]}')
    lines.append("")
    lines.append(item["lede"])
    lines.append("")
    for heading, text in item["sections"]:
        lines.append(f'## {heading}')
        lines.append("")
        lines.append(text)
        lines.append("")
    lines.append("## اقتباسات مختارة")
    lines.append("")
    lines.append("لا يوجد اقتباس مباشر موثوق متاح.")
    lines.append("")

    filepath = os.path.join(out_dir_wrk, f"{item['slug']}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"Wrote {filepath}")

print("Max expansion thinkers and works generated successfully.")
