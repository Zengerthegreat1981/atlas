# -*- coding: utf-8 -*-
import os

thinkers_data = [
    # Classic Pop & Self-Help Pioneers
    {
        "slug": "thk-napoleon-hill",
        "title": "نابليون هيل",
        "en": "Napoleon Hill",
        "dates": "الولايات المتحدة · 1883–1970",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1908,
        "active_end": "1970",
        "school": "علم النفس الشعبي وسيكولوجيا النجاح",
        "is_pop": True,
        "lede": "كاتب ومؤلف أمريكي رائد، يُعد أحد الآباء المؤسسين لأدبيات النجاح الشخصي الحديثة؛ أجرى مقابلات مع أكثر من 500 من كبار رواد الأعمال والعلماء لصياغة 'فلسفة الإنجاز' في كتابه الخالد «فكر وازدد ثراءً».",
        "works": ["The Law of Success (1928)", "Think and Grow Rich (1937)", "Outwitting the Devil (1938)"],
        "related": [
            {"id": "wrk-think-and-grow-rich", "title": "فكر وازدد ثراءً", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-maxwell-maltz",
        "title": "ماكسويل مالتز",
        "en": "Maxwell Maltz",
        "dates": "الولايات المتحدة · 1899–1975",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1940,
        "active_end": "1975",
        "school": "السيكوسبرنتيكس وسيكولوجيا الصورة الذاتية",
        "is_pop": True,
        "lede": "جراح تجميل ومؤلف أمريكي؛ لاحظ أن الجراحة التجميلية لا تغير مشاعر الدونية لدى المرضى إلا إذا تغيرت 'الصورة الذاتية الداخلية'، فصاغ علم 'السايكوسبرنتيكس' (التحكم النفسي الآلي) الذي أحدث نقلة في التنمية الذاتية.",
        "works": ["Psycho-Cybernetics (1960)", "The Magic Power of Self-Image Psychology (1964)"],
        "related": [
            {"id": "wrk-psycho-cybernetics", "title": "السايكوسبرنتيكس", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-norman-vincent-peale",
        "title": "نورمان فنسنت بيل",
        "en": "Norman Vincent Peale",
        "dates": "الولايات المتحدة · 1898–1993",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1932,
        "active_end": "1993",
        "school": "علم النفس الشعبي والتفكير الإيجابي",
        "is_pop": True,
        "lede": "رجل دين ومؤلف أمريكي، كان له الفضل الأكبر في نشر مفهوم 'التفكير الإيجابي' عالمياً عبر كتابه ذائع الصيت «قوة التفكير الإيجابي» الذي جمع بين المبادئ الإيمانية وعلم النفس العملي.",
        "works": ["The Power of Positive Thinking (1952)", "A Guide to Confident Living (1948)"],
        "related": [
            {"id": "wrk-power-of-positive-thinking", "title": "قوة التفكير الإيجابي", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-joseph-murphy",
        "title": "جوزيف ميرفي",
        "en": "Joseph Murphy",
        "dates": "أيرلندا / الولايات المتحدة · 1898–1981",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1940,
        "active_end": "1981",
        "school": "علم النفس الشعبي وسيكولوجيا العقل الباطن",
        "is_pop": True,
        "lede": "مؤلف وباحث ومحاضر أيرلندي-أمريكي؛ حقق كتابه «قوة عقلك الباطن» انتشاراً عالمياً غير مسبوق بتجاوزه 10 ملايين نسخة، مبيناً كيفية إعادة برمجة اللاوعي بالتأكيدات الإيجابية والتخيل الموجه.",
        "works": ["The Power of Your Subconscious Mind (1963)", "The Miracle of Mind Dynamics (1964)"],
        "related": [
            {"id": "wrk-power-of-subconscious-mind", "title": "قوة عقلك الباطن", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-david-schwartz",
        "title": "ديفيد ج. شوارتز",
        "en": "David J. Schwartz",
        "dates": "الولايات المتحدة · 1927–1987",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1955,
        "active_end": "1987",
        "school": "علم النفس الشعبي والتحفيز القيادي",
        "is_pop": True,
        "lede": "أستاذ تسويق بجامعة ولاية جورجيا ومؤلف تحفيزي رائد؛ اشتهر بكتابه الكلاسيكي «سحر التفكير بصورة أكبر» الذي يقدم دليلاً عملياً للتغلب على الخوف والتردد وتوسيع آفاق الطموح.",
        "works": ["The Magic of Thinking Big (1959)", "The Magic of Getting What You Want (1983)"],
        "related": [
            {"id": "wrk-magic-of-thinking-big", "title": "سحر التفكير بصورة أكبر", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-wayne-dyer",
        "title": "واين داير",
        "en": "Wayne W. Dyer",
        "dates": "الولايات المتحدة · 1940–2015",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1976,
        "active_end": "2015",
        "school": "علم النفس الإرشادي والتنمية الذاتية",
        "is_pop": True,
        "lede": "عالم نفس إرشادي ومؤلف ومحاضر دولي بارز؛ حقق كتابه الأول «مناطق أخطائك» مبيعات قياسية تتجاوز 35 مليون نسخة، مقدماً دليلاً علاجياً معرفياً لتفكيك الشعور بالذنب والقلق من أحكام الآخرين.",
        "works": ["Your Erroneous Zones (1976)", "Pulling Your Own Strings (1978)", "The Power of Intention (2004)"],
        "related": [
            {"id": "wrk-erroneous-zones", "title": "مناطق أخطائك", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-allen-carr",
        "title": "ألين كار",
        "en": "Allen Carr",
        "dates": "المملكة المتحدة · 1934–2006",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "2006",
        "school": "علم النفس الشعبي وإعادة الهيكلة المعرفية للإدمان",
        "is_pop": True,
        "lede": "مؤلف ومحاسب بريطاني سابق؛ أحدث ثورة عالمية في علاج الإدمان السلوكي عبر منهجيته 'Easyway' التي تعتمد على إعادة الهيكلة المعرفية الصرفة وإزالة غسيل المخ النفسي بدلاً من الاعتماد على قوة الإرادة العاجزة.",
        "works": ["The Easy Way to Stop Smoking (1985)", "The Easy Way to Control Alcohol (2001)"],
        "related": [
            {"id": "wrk-easy-way-stop-smoking", "title": "الطريقة السهلة للإقلاع عن التدخين", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-benedict-carey",
        "title": "بينيديكت كاري",
        "en": "Benedict Carey",
        "dates": "الولايات المتحدة · 1960–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2000,
        "active_end": "مستمر",
        "school": "الصحافة العلمية وسيكولوجيا التعلم",
        "is_pop": True,
        "lede": "صحفي علمي بارز في نيويورك تايمز؛ اشتهر بتبسيط أبحاث علم النفس المعرفي للتعلم والذاكرة وتفكيك أساطير الحفظ التقليدي في كتابه «كيف نتعلم».",
        "works": ["How We Learn: The Surprising Truth About When, Where, and Why It Happens (2014)"],
        "related": [
            {"id": "wrk-how-we-learn", "title": "كيف نتعلم", "type": "عمل / كتاب"}
        ]
    },

    # Academic Behavioral & Social Scientists
    {
        "slug": "thk-robert-sapolsky",
        "title": "روبرت سابولسكي",
        "en": "Robert Sapolsky",
        "dates": "الولايات المتحدة · 1957–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "مستمر",
        "school": "علم الأحياء العصبي والغدد الصماء وسيكولوجيا التوتر",
        "is_pop": False,
        "lede": "أستاذ علم الأحياء وعلم الأعصاب وجراحة الأعصاب بجامعة ستانفورد، وزميل أبحاث الرئيسيات؛ المرجع العالمي الأول في دراسة الآثار البيولوجية والعصبية للتوتر المزمن، وسلوك العدوان والتعاطف في كتابه الموسوعي «تصرف».",
        "works": ["Why Zebras Don't Get Ulcers (1994)", "A Primate's Memoir (2001)", "Behave: The Biology of Humans at Our Best and Worst (2017)", "Determined: A Science of Life without Free Will (2023)"],
        "related": [
            {"id": "wrk-why-zebras-dont-get-ulcers", "title": "لماذا لا تصاب الحمر الوحشية بالقرحة", "type": "عمل / كتاب"},
            {"id": "wrk-behave-sapolsky", "title": "تصرّف: بيولوجيا الإنسان", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-barry-schwartz",
        "title": "باري شوارتز",
        "en": "Barry Schwartz",
        "dates": "الولايات المتحدة · 1946–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي والاقتصاد السلوكي",
        "is_pop": False,
        "lede": "أستاذ علم النفس الفخري بكلية سوارثمور؛ اشتهر بصياغة ونشر أطروحة 'مفارقة الاختيار' (The Paradox of Choice) التي تبرهن أن كثرة الخيارات في المجتمعات الحديثة تؤدي للشلل النفسي وتراجع الرضا الذاتي.",
        "works": ["The Paradox of Choice: Why More Is Less (2004)", "Practical Wisdom (2010)", "Why We Work (2015)"],
        "related": [
            {"id": "wrk-paradox-of-choice", "title": "مفارقة الاختيار", "type": "عمل / كتاب"},
            {"id": "con-paradox-of-choice", "title": "مفارقة الاختيار وشلل القرار", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-elizabeth-loftus",
        "title": "إليزابيث لوفتوس",
        "en": "Elizabeth F. Loftus",
        "dates": "الولايات المتحدة · 1944–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1973,
        "active_end": "مستمر",
        "school": "علم النفس المعرفي وسيكولوجيا الذاكرة الجنائية",
        "is_pop": False,
        "lede": "أستاذة متميزة في علم النفس المعرفي والقانون بجامعة كاليفورنيا في إيرفاين؛ رائدة أبحاث مرونة الذاكرة البشرية وقابليتها للتعديل، ومكتشفة 'تأثير التضليل' (Misinformation Effect) وتكوين الذكريات الزائفة.",
        "works": ["Eyewitness Testimony (1979)", "The Myth of Repressed Memory (1994)"],
        "related": [
            {"id": "wrk-eyewitness-testimony", "title": "شهادة شهود العيان", "type": "عمل / كتاب"},
            {"id": "con-misinformation-effect-loftus", "title": "تأثير التضليل والذاكرة الزائفة", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-philip-zimbardo",
        "title": "فيليب زيمباردو",
        "en": "Philip Zimbardo",
        "dates": "الولايات المتحدة · 1933–2024",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1960,
        "active_end": 2024,
        "school": "علم النفس الاجتماعي التجريبي",
        "is_pop": False,
        "lede": "عالم نفس اجتماعي وأستاذ فخري بجامعة ستانفورد ورئيس الجمعية الأمريكية لعلم النفس (APA) سابقاً؛ قائد 'تجربة سجن ستانفورد' الشهيرة (1971) ومؤلف كتاب «تأثير لوسيفر» حول سيكولوجيا الشر المؤسسي والبطولة اليومية.",
        "works": ["The Lucifer Effect: Understanding How Good People Turn Evil (2007)", "The Time Paradox (2008)", "Shyness: What It Is, What to Do About It (1977)"],
        "related": [
            {"id": "wrk-lucifer-effect", "title": "تأثير لوسيفر", "type": "عمل / كتاب"},
            {"id": "con-lucifer-effect", "title": "تأثير لوسيفر والشر المؤسسي", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-stanley-milgram",
        "title": "ستانلي ميلغرام",
        "en": "Stanley Milgram",
        "dates": "الولايات المتحدة · 1933–1984",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1960,
        "active_end": "1984",
        "school": "علم النفس الاجتماعي التجريبي",
        "is_pop": False,
        "lede": "عالم نفس اجتماعي بارز بجامعة ييل وجامعة سيتي بنيويورك؛ صمم 'تجربة ميلغرام للانصياع' التاريخية (1961) وتجربة 'العالم الصغير' (الدرجات الست للتباعد)، ومؤلف كتاب «الانصياع للسلطة».",
        "works": ["Obedience to Authority: An Experimental View (1974)", "The Individual in a Social World (1977)"],
        "related": [
            {"id": "wrk-obedience-to-authority", "title": "الانصياع للسلطة", "type": "عمل / كتاب"},
            {"id": "con-agentic-state-milgram", "title": "الحالة الوكالية والانصياع للسلطة", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-zygmunt-bauman",
        "title": "زيجمونت باومان",
        "en": "Zygmunt Bauman",
        "dates": "بولندا / المملكة المتحدة · 1925–2017",
        "country": "المملكة المتحدة",
        "language": "الإنجليزية / البولندية",
        "active_start": 1960,
        "active_end": "2017",
        "school": "علم الاجتماع النفسي ونظرية السيولة",
        "is_pop": False,
        "lede": "عالم اجتماع ومفكر أوروبي بارز؛ صاغ نظرية 'الحداثة السائلة' (Liquid Modernity) واستكشف في كتابه «الحب السائل» هشاشة الروابط الإنسانية والعاطفية وتحول العلاقات إلى سلع استهلاكية سريعة الاستبدال.",
        "works": ["Liquid Modernity (2000)", "Liquid Love: On the Frailty of Human Bonds (2003)", "Liquid Fear (2006)"],
        "related": [
            {"id": "wrk-liquid-love", "title": "الحب السائل", "type": "عمل / كتاب"}
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
    lines.append(f"إسهامات محورية في مجال {item['school']} ونشر الأطر السيكولوجية والبحثية المؤثرة عالمياً.")
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
        "slug": "wrk-think-and-grow-rich",
        "title": "فكر وازدد ثراءً: فلسفة الإنجاز الكلاسيكية",
        "en": "Think and Grow Rich",
        "dates": "1937 · نابليون هيل",
        "language": "الإنجليزية",
        "active_start": 1937,
        "active_end": "1937",
        "school": "علم النفس الشعبي وسيكولوجيا النجاح",
        "author_id": "thk-napoleon-hill",
        "author_title": "نابليون هيل",
        "lede": "أحد أشهر الكتب في تاريخ النشر العالمي (أكثر من 100 مليون نسخة)؛ يستخلص 13 خطوة نحو الإنجاز ترتكز على الرغبة الحارقة، والإيمان، والتوجيه الذاتي للاوعي، والعقل المدبر (Mastermind).",
        "sections": [
            ("المبادئ الكلاسيكية الثلاثة عشر", "الرغبة المحددة، الإيمان بالنفس، الإيحاء الذاتي، المعرفة المتخصصة، التخيل، التخطيط المنظم، اتخاذ القرار الحاسم، والمثابرة."),
            ("الأثر في ثقافة التنمية الذاتية", "شكل الإطار المرجعي لكافة برامج التدريب والتحفيز وتطوير الأداء الشخصي في القرن العشرين.")
        ]
    },
    {
        "slug": "wrk-psycho-cybernetics",
        "title": "السايكوسبرنتيكس: التحكم النفسي الآلي والصورة الذاتية",
        "en": "Psycho-Cybernetics",
        "dates": "1960 · ماكسويل مالتز",
        "language": "الإنجليزية",
        "active_start": 1960,
        "active_end": "1960",
        "school": "السيكوسبرنتيكس وسيكولوجيا الصورة الذاتية",
        "author_id": "thk-maxwell-maltz",
        "author_title": "ماكسويل مالتز",
        "lede": "عمل كلاسيكي رائد بيع منه أكثر من 30 مليون نسخة؛ يطرح أن عقل الإنسان يمتلك 'آلية توجيه آلية' (Servo-Mechanism) تشبه الطيار الآلي، وتعمل دائماً على تحقيق ما ترسمه 'الصورة الذاتية' (Self-Image) الداخلية.",
        "sections": [
            ("قوة الصورة الذاتية", "لا يمكن للإنسان أن يتجاوز في واقعه حدود ما يعتقده عن نفسه في صورته الذاتية الداخلية؛ وتعديل الصورة الذاتية بالخيال هو المفتاح الحقيقي لتغيير السلوك."),
            ("البروفة الذهنية والتخيل المسرحي", "استخدام التخيل الإيجابي اليومي لتغذية العقل الباطن بذكريات نجاح بديلة ومحو ذكريات الفشل.")
        ]
    },
    {
        "slug": "wrk-power-of-positive-thinking",
        "title": "قوة التفكير الإيجابي",
        "en": "The Power of Positive Thinking",
        "dates": "1952 · نورمان فنسنت بيل",
        "language": "الإنجليزية",
        "active_start": 1952,
        "active_end": "1952",
        "school": "علم النفس الشعبي والتفكير الإيجابي",
        "author_id": "thk-norman-vincent-peale",
        "author_title": "نورمان فنسنت بيل",
        "lede": "كتاب تاريخي غير مسبوق ظل في قائمة نيويورك تايمز لأكثر من عامين؛ يدمج بين المبادئ الروحية والإرشاد النفسي العملي للقضاء على القلق المزمن وتوليد الثقة بالنفس والطاقة المتجددة.",
        "sections": [
            ("الأطروحة والممارسات اليومية", "تفريغ العقل من الأفكار الكارثية، ممارسة الحديث الإيجابي مع الذات، وتجديد النشاط الروحي والجسدي عبر الهدوء الذهني."),
            ("القراءة النقدية", "نُقد لتبسيطه الشديد لأسباب المعاناة الحقيقية، بينما يُقدّر كحجر أساس لثقافة التفاؤل والتحفيز الذاتي المعاصرة.")
        ]
    },
    {
        "slug": "wrk-power-of-subconscious-mind",
        "title": "قوة عقلك الباطن",
        "en": "The Power of Your Subconscious Mind",
        "dates": "1963 · جوزيف ميرفي",
        "language": "الإنجليزية",
        "active_start": 1963,
        "active_end": "1963",
        "school": "علم النفس الشعبي وسيكولوجيا العقل الباطن",
        "author_id": "thk-joseph-murphy",
        "author_title": "جوزيف ميرفي",
        "lede": "أحد أكثر كتب التنمية الذاتية الكلاسيكية انتشاراً في العالم؛ يوضح كيف يتلقى العقل الباطن أفكار العقل الواعي كأوامر قاطعة ويقوم بتنفيذها تلقائياً، مقدماً تقنيات للتأمل والتأكيد الإيجابي قبل النوم.",
        "sections": [
            ("قانون الاعتقاد والاستجابة اللاشعورية", "العقل الباطن لا يجادل بل ينفذ ما يزرعه فيه العقل الواعي من أفكار ومشاعر يقينية."),
            ("تقنيات التخيل قبل النوم", "استغلال مرحلة استرخاء الدماغ قبل النوم لتغذية اللاوعي بمشاعر الشفاء والوفرة والسلام.")
        ]
    },
    {
        "slug": "wrk-magic-of-thinking-big",
        "title": "سحر التفكير بصورة أكبر",
        "en": "The Magic of Thinking Big",
        "dates": "1959 · ديفيد ج. شوارتز",
        "language": "الإنجليزية",
        "active_start": 1959,
        "active_end": "1959",
        "school": "علم النفس الشعبي والتحفيز القيادي",
        "author_id": "thk-david-schwartz",
        "author_title": "ديفيد ج. شوارتز",
        "lede": "كتاب تحفيزي كلاسيكي بيع منه أكثر من 6 ملايين نسخة؛ يبرهن أن حجم النجاح والمال والرضا الذي يحققه الإنسان يحدده حصراً 'حجم تفكيره وتوقعاته' لا حجم ذكائه الفطري أو خلفيته العائلية.",
        "sections": [
            ("علاج 'مرض الأعذار' (Excusitis)", "القضاء على أعذار الصحة، الذكاء، العمر، والحظ السيئ، واستبدالها بالفعل والمبادرة."),
            ("بناء الثقة وهزيمة الخوف بالعمل", "التأكيد على أن الفعل والحركة هما الترياق الوحيد لهزيمة القلق والتردد.")
        ]
    },
    {
        "slug": "wrk-erroneous-zones",
        "title": "مناطق أخطائك: تحرر من السلوكيات الهدامة وعش بسعادة",
        "en": "Your Erroneous Zones",
        "dates": "1976 · واين داير",
        "language": "الإنجليزية",
        "active_start": 1976,
        "active_end": "1976",
        "school": "علم النفس الإرشادي والتنمية الذاتية",
        "author_id": "thk-wayne-dyer",
        "author_title": "واين داير",
        "lede": "أحد أكثر الكتب مبيعاً في التاريخ (أكثر من 35 مليون نسخة)؛ يقدم دليلاً مستنداً للعلاج العقلاني الانفعالي (REBT) لتفكيك 'المناطق الخاطئة' في التفكير كالشعور بالذنب، القلق، البحث عن الاستحسان، والتسويف.",
        "sections": [
            ("العاطفتان الأكثر عقماً: الذنب والقلق", "الذنب يركز على ماضٍ لا يمكن تغييره، والقلق يركز على مستقبل لا نملكه، وكلاهما يشل اللحظة الحاضرة."),
            ("التحرر من إدمان استحسان الآخرين", "تطوير مرجعية تقييم داخلية مستقلة لا تتأثر بمدح أو ذم المحيطين.")
        ]
    },
    {
        "slug": "wrk-easy-way-stop-smoking",
        "title": "الطريقة السهلة للإقلاع عن التدخين: إعادة البرمجة المعرفية للإدمان",
        "en": "The Easy Way to Stop Smoking",
        "dates": "1985 · ألين كار",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "1985",
        "school": "علم النفس الشعبي وإعادة الهيكلة المعرفية للإدمان",
        "author_id": "thk-allen-carr",
        "author_title": "ألين كار",
        "lede": "المرجع الأكثر نجاحاً عالمياً في علاج التدخين (أكثر من 13 مليون نسخة)؛ يفكك الوهم النفسي بأن السجائر تمنح متعة أو استرخاء، ويثبت أنها تخلق فقط التوتر الذي تدعي علاجه، مما يتيح الإقلاع الفوري دون أعراض حرمان مؤلمة.",
        "sections": [
            ("فخ الوحش الصغير والوحش الكبير", "التمييز بين الإدمان الكيميائي البسيط للنيكوتين (الوحش الصغير) وبين غسيل المخ النفسي والاعتقادي (الوحش الكبير)."),
            ("الإقلاع بالاستبصار لا بقوة الإرادة", "التوقف عن الشعور بالتضحية أو الحرمان والاحتفاء بالتحرر الفوري من العبودية النفسية.")
        ]
    },
    {
        "slug": "wrk-why-zebras-dont-get-ulcers",
        "title": "لماذا لا تصاب الحمر الوحشية بالقرحة: سيكولوجيا وبيولوجيا التوتر",
        "en": "Why Zebras Don't Get Ulcers",
        "dates": "1994 · روبرت سابولسكي",
        "language": "الإنجليزية",
        "active_start": 1994,
        "active_end": "1994",
        "school": "علم الأحياء العصبي وسيكولوجيا التوتر",
        "author_id": "thk-robert-sapolsky",
        "author_title": "روبرت سابولسكي",
        "lede": "تحفة علمية كلاسيكية في علم الأعصاب السلوكي؛ تشرح بأسلوب ساخر وعميق كيف طُورت استجابة التوتر البيولوجية للطوارئ الحادة (كالهروب من أسد لبضع دقائق)، بينما يفعلها البشر الحديثون نفسياً لشهور بسبب الرهن العقاري والوظيفة مما يدمر مناعتهم وأجسادهم.",
        "sections": [
            ("التكلفة الجسدية للتوتر المزمن", "كيف يؤدي استمرار الكورتيزول إلى تثبيط المناعة، قرحة المعدة، السكري، ضمور الذاكرة في الحصين، وانهيار الرغبة الجنسية."),
            ("المرونة النفسية والتحكم التكيفي", "استراتيجيات تفريغ التوتر عبر النشاط البدني، الدعم الاجتماعي الحقيقي، وإعادة التقييم المعرفي للتهديدات.")
        ]
    },
    {
        "slug": "wrk-paradox-of-choice",
        "title": "مفارقة الاختيار: لماذا يعني المزيد القليل",
        "en": "The Paradox of Choice: Why More Is Less",
        "dates": "2004 · باري شوارتز",
        "language": "الإنجليزية",
        "active_start": 2004,
        "active_end": "2004",
        "school": "علم النفس الاجتماعي والاقتصاد السلوكي",
        "author_id": "thk-barry-schwartz",
        "author_title": "باري شوارتز",
        "lede": "كتاب شهير يفكك العقيدة الغربية القائلة بأن زيادة الخيارات تعني بالضرورة زيادة الحرية والسعادة؛ مبيناً أن فرط الخيارات يولد شللاً في القرار، ورفعاً غير واقعي للتوقعات، ولوم الذات والندم المزمن.",
        "sections": [
            ("المعظمون (Maximizers) مقابل القانعون (Satisficers)", "المعظم يسعى دائماً للخيار الأفضل المطلق فيصاب بالندم والإنهاك؛ بينما القانع يحدد معايير مقبولة ويكتفي بما يفي بها فيحقق الرضا والسعادة."),
            ("علاج شلل الخيارات", "تقليص الخيارات طواعية وتبني استراتيجية 'جيد بما فيه الكفاية' في القرارات اليومية.")
        ]
    },
    {
        "slug": "wrk-eyewitness-testimony",
        "title": "شهادة شهود العيان وسيكولوجيا الذاكرة الزائفة",
        "en": "Eyewitness Testimony",
        "dates": "1979 · إليزابيث لوفتوس",
        "language": "الإنجليزية",
        "active_start": 1979,
        "active_end": "1979",
        "school": "علم النفس المعرفي وسيكولوجيا الذاكرة الجنائية",
        "author_id": "thk-elizabeth-loftus",
        "author_title": "إليزابيث لوفتوس",
        "lede": "العمل التأسيسي الذي غيّر المنظومة القضائية الجنائية عالمياً؛ أثبتت فيه لوفتوس عبر تجارب محكمة أن الذاكرة البشرية ليست شريط فيديو يسجل الواقع، بل عملية إعادة بناء إبداعية هشة تتأثر بالتضليل والأسئلة الإيحائية وتدمج معلومات كاذبة دون وعي.",
        "sections": [
            ("تأثير صياغة الأسئلة على الذاكرة", "كيف غيرت كلمة 'تحطمت' مقابل 'اصطدمت' تقدير سرعة السيارات في أذهان الشهود وجعلتهم يرون زجاجاً مكسوراً لم يكن موجوداً أصلاً."),
            ("الإصلاحات في التحقيق الجنائي", "وضع بروتوكولات صارمة لاستجواب الشهود وعرض المشتبه بهم لمنع إدانة الأبرياء.")
        ]
    },
    {
        "slug": "wrk-lucifer-effect",
        "title": "تأثير لوسيفر: كيف يتحول الأخيار إلى أشرار",
        "en": "The Lucifer Effect: Understanding How Good People Turn Evil",
        "dates": "2007 · فيليب زيمباردو",
        "language": "الإنجليزية",
        "active_start": 2007,
        "active_end": "2007",
        "school": "علم النفس الاجتماعي التجريبي",
        "author_id": "thk-philip-zimbardo",
        "author_title": "فيليب زيمباردو",
        "lede": "تحليل سيكولوجي شامل وموثق يربط بين تجربة سجن ستانفورد (1971) وبين انتهاكات سجن أبو غريب؛ يوضح كيف تحول البيئات المؤسسية والقوة غير المقيدة والتجريد من الإنسانية أفراداً أسوياء وأخياراً إلى ممارسي تعذيب ساديين.",
        "sections": [
            ("قوة الموقف والنظام مقابل التفاحة الفاسدة", "التأكيد على أن الشر ليس مجرد خلل فردي بل نتاج 'براميل فاسدة' تصنعها الأنظمة والقوانين الظالمة."),
            ("تنشئة البطولة اليومية (Everyday Heroism)", "تدريب الأفراد والشباب على الشجاعة الأخلاقية ومقاومة الضغط الجمعي والانصياع الأعمى للسلطة.")
        ]
    },
    {
        "slug": "wrk-obedience-to-authority",
        "title": "الانصياع للسلطة: نظرة تجريبية",
        "en": "Obedience to Authority: An Experimental View",
        "dates": "1974 · ستانلي ميلغرام",
        "language": "الإنجليزية",
        "active_start": 1974,
        "active_end": "1974",
        "school": "علم النفس الاجتماعي التجريبي",
        "author_id": "thk-stanley-milgram",
        "author_title": "ستانلي ميلغرام",
        "lede": "الكتاب الذي وثق تفاصيل أكثر التجارب إثارة للجدل في تاريخ علم النفس؛ حيث وافق 65% من المشاركين الأسوياء على صعق شخص بريء بصدمات كهربائية مميتة تصل إلى 450 فولت لمجرد تلقيهم أوامر هادئة من باحث يرتدي معطفاً مخبرياً.",
        "sections": [
            ("مفهوم 'الحالة الوكالية' (The Agentic State)", "تحول الفرد من كائن مستقل أخلاقياً إلى 'وكيل منفذ' يرى نفسه غير مسؤول عن عواقب أفعاله طالما ينفذ أوامر سلطة شرعية."),
            ("الأهمية الفلسفية والتاريخية", "تقديم تفسير علمي تجريبي لمحاكمات نورمبرغ وجرائم الإبادة الجماعية تحت شعار 'كنت أنفذ الأوامر فقط'.")
        ]
    },
    {
        "slug": "wrk-how-we-learn",
        "title": "كيف نتعلم: الحقيقة المدهشة عن وقت ومكان وكيفية حدوث التعلم",
        "en": "How We Learn",
        "dates": "2014 · بينيديكت كاري",
        "language": "الإنجليزية",
        "active_start": 2014,
        "active_end": "2014",
        "school": "الصحافة العلمية وسيكولوجيا التعلم",
        "author_id": "thk-benedict-carey",
        "author_title": "بينيديكت كاري",
        "lede": "كتاب يفكك الأساليب التقليدية العقيمة للحفظ والمذاكرة، مستعرضاً نتائج علوم الإدراك المعاصرة حول فوائد النسيان المتباعد، وتغيير بيئة الدراسة، والاختبار الذاتي، والنوم في تثبيت المهارات والمعارف.",
        "sections": [
            ("نظرية النسيان التكيفي المتباعد (Spaced Repetition)", "كيف يقوي النسيان المؤقت مسارات استرجاع المعلومات عند إعادة دراستها."),
            ("تأثير الاختبار والمزج بين المواد (Interleaving)", "تفوق الاختبار الذاتي المستمر على مجرد إعادة القراءة السلبية للكتب.")
        ]
    },
    {
        "slug": "wrk-liquid-love",
        "title": "الحب السائل: عن هشاشة الروابط الإنسانية",
        "en": "Liquid Love: On the Frailty of Human Bonds",
        "dates": "2003 · زيجمونت باومان",
        "language": "الإنجليزية",
        "active_start": 2003,
        "active_end": "2003",
        "school": "علم الاجتماع النفسي ونظرية السيولة",
        "author_id": "thk-zygmunt-bauman",
        "author_title": "زيجمونت باومان",
        "lede": "تحليل سوسيولوجي ونفسي عميق لواقع العلاقات العاطفية في العصر الرقمي الاستهلاكي؛ يوضح كيف تحولت الروابط الإنسانية إلى عقود سريعة ومؤقتة تشبه السلع الاستهلاكية، حيث يخشى الأفراد الالتزام العميق ويبحثون عن 'اتصالات شبكية' قابلة للفصل بنقرة زر.",
        "sections": [
            ("مفارقة الرغبة في الأمان والخوف من القيود", "صراع الفرد المعاصر بين حاجته للحميمية وبين خوفه من أن تقيد العلاقات حريته الفردية في سوق الخيارات المفتوح."),
            ("من العلاقات الصلبة إلى العلاقات السائلة", "تآكل مفاهيم التضحية والوفاء لصالح مبدأ المنفعة الفورية والجاهزية الدائمة للاستبدال.")
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

print("Unit 2 classics generated successfully.")
