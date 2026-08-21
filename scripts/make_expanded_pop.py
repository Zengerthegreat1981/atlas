# -*- coding: utf-8 -*-
import os

thinkers_data = [
    # Academic Thinkers
    {
        "slug": "thk-jonathan-haidt",
        "title": "جوناثان هايدت",
        "en": "Jonathan Haidt",
        "dates": "الولايات المتحدة · 1963–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1992,
        "active_end": "مستمر",
        "school": "علم النفس الأخلاقي والاجتماعي",
        "is_pop": False,
        "lede": "عالم نفس اجتماعي وأستاذ القيادة الأخلاقية بكلية شتيرن لإدارة الأعمال بجامعة نيويورك؛ رائد نظرية الأسس الأخلاقية (Moral Foundations Theory) وباحث تأثير وسائل التواصل على الصحة النفسية للشباب.",
        "works": ["The Happiness Hypothesis (2006)", "The Righteous Mind (2012)", "The Coddling of the American Mind (2018)", "The Anxious Generation (2024)"],
        "related": [
            {"id": "wrk-righteous-mind", "title": "العقل الصالح", "type": "عمل / كتاب"},
            {"id": "wrk-anxious-generation", "title": "الجيل القلق", "type": "عمل / كتاب"},
            {"id": "wrk-happiness-hypothesis", "title": "فرضية السعادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-daniel-gilbert",
        "title": "دانيال جيلبرت",
        "en": "Daniel Gilbert",
        "dates": "الولايات المتحدة · 1957–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي والمعرفي",
        "is_pop": False,
        "lede": "أستاذ علم النفس بجامعة هارفارد، اشتهر بأبحاثه الرائدة في 'التنبؤ العاطفي' (Affective Forecasting) وأخطاء الدماغ في تقدير السعادة المستقبلية والرضا الذاتي.",
        "works": ["Stumbling on Happiness (2006)", "Immune Neglect: A Source of Durability Bias in Affective Forecasting (1998)"],
        "related": [
            {"id": "wrk-stumbling-on-happiness", "title": "العثرات في طريق السعادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-dan-ariely",
        "title": "دان آرييلي",
        "en": "Dan Ariely",
        "dates": "إسرائيل / الولايات المتحدة · 1967–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 1998,
        "active_end": "مستمر",
        "school": "الاقتصاد السلوكي وعلم النفس المعرفي",
        "is_pop": False,
        "lede": "أستاذ علم النفس والاقتصاد السلوكي بجامعة ديوك، اشتهر بأبحاثه التجريبية حول اللامنطقية الممنهجة في السلوك البشري وسيكولوجيا الخداع الذاتي والأمانة.",
        "works": ["Predictably Irrational (2008)", "The Upside of Irrationality (2010)", "The (Honest) Truth About Dishonesty (2012)"],
        "related": [
            {"id": "wrk-predictably-irrational", "title": "اللامنطقية المتوقعة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-elaine-aron",
        "title": "إيلين آرون",
        "en": "Elaine N. Aron",
        "dates": "الولايات المتحدة · 1944–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1990,
        "active_end": "مستمر",
        "school": "علم النفس الإكلينيكي وحساسية المعالجة الحسية",
        "is_pop": False,
        "lede": "عالمة نفس إكلينيكي وباحثة رائدة، صاغت مفهوم 'حساسية المعالجة الحسية' (Sensory Processing Sensitivity) وعممت مصطلح 'الشخص عالي الحساسية' (Highly Sensitive Person - HSP) في الأوساط الأكاديمية والشعبية.",
        "works": ["The Highly Sensitive Person (1996)", "The Highly Sensitive Person in Love (2000)", "Sensory-processing sensitivity and its relation to introversion and emotionality (1997)"],
        "related": [
            {"id": "wrk-highly-sensitive-person", "title": "الشخص عالي الحساسية", "type": "عمل / كتاب"},
            {"id": "con-highly-sensitive-person", "title": "الشخص عالي الحساسية HSP", "type": "مفهوم"}
        ]
    },

    # Pop Psychology Thinkers (register: popular)
    {
        "slug": "thk-stephen-covey",
        "title": "ستيفن كوفي",
        "en": "Stephen R. Covey",
        "dates": "الولايات المتحدة · 1932–2012",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1970,
        "active_end": "2012",
        "school": "علم النفس الشعبي والقيادة الشخصية",
        "is_pop": True,
        "lede": "مؤلف واستشاري قيادي أمريكي، يُعد أحد أبرز رموز أدبيات الفاعلية الإنسانية والإدارة الذاتية في العالم عبر كتابه الأيقوني «العادات السبع للناس الأكثر فاعلية».",
        "works": ["The 7 Habits of Highly Effective People (1989)", "First Things First (1994)", "The 8th Habit (2004)"],
        "related": [
            {"id": "wrk-7-habits", "title": "العادات السبع للناس الأكثر فاعلية", "type": "عمل / كتاب"},
            {"id": "con-seven-habits", "title": "العادات السبع للفاعلية", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-robert-greene",
        "title": "روبرت غرين",
        "en": "Robert Greene",
        "dates": "الولايات المتحدة · 1959–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1998,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي وسيكولوجيا القوة",
        "is_pop": True,
        "lede": "كاتب ومؤلف أمريكي حققت كتبه مبيعات بالملايين، اشتهر بدراسة الجوانب المظلمة والاستراتيجية في النفس البشرية، والتأثير، والقيادة التاريخية عبر أعمال مثل «48 قانوناً للقوة» و«قوانين الطبيعة البشرية».",
        "works": ["The 48 Laws of Power (1998)", "The Art of Seduction (2001)", "Mastery (2012)", "The Laws of Human Nature (2018)"],
        "related": [
            {"id": "wrk-48-laws-of-power", "title": "48 قانوناً للقوة", "type": "عمل / كتاب"},
            {"id": "wrk-laws-of-human-nature", "title": "قوانين الطبيعة البشرية", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-eckhart-tolle",
        "title": "إيكهارت تول",
        "en": "Eckhart Tolle",
        "dates": "ألمانيا / كندا · 1948–",
        "country": "كندا",
        "language": "الإنجليزية / الألمانية",
        "active_start": 1997,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي واليقظة الروحية",
        "is_pop": True,
        "lede": "معلم روحي وكاتب كندي ألماني المولد، ساهم في تعميم مفاهيم اليقظة الذهنية، والتحرر من طغيان الأنا (Ego)، والعيش في اللحظة الحاضرة عبر كتابيه ذائعي الصيت «قوة الآن» و«أرض جديدة».",
        "works": ["The Power of Now (1997)", "Practicing the Power of Now (2001)", "A New Earth: Awakening to Your Life's Purpose (2005)"],
        "related": [
            {"id": "wrk-power-of-now", "title": "قوة الآن", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-gary-chapman",
        "title": "غاري تشابمان",
        "en": "Gary Chapman",
        "dates": "الولايات المتحدة · 1938–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والإرشاد الزواجي",
        "is_pop": True,
        "lede": "مستشار علاقات ومؤلف أمريكي، ابتكر نموذج «لغات الحب الخمس» الذي حقق انتشاراً جماهيرياً عالمياً وترجم لأكثر من 50 لغة وباع أكثر من 20 مليون نسخة.",
        "works": ["The 5 Love Languages (1992)", "The 5 Languages of Appreciation in the Workplace (2011)"],
        "related": [
            {"id": "wrk-5-love-languages", "title": "لغات الحب الخمس", "type": "عمل / كتاب"},
            {"id": "con-five-love-languages", "title": "لغات الحب الخمس", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-louise-hay",
        "title": "لويز هاي",
        "en": "Louise Hay",
        "dates": "الولايات المتحدة · 1926–2017",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1976,
        "active_end": "2017",
        "school": "علم النفس الشعبي والتأكيدات الإيجابية",
        "is_pop": True,
        "lede": "مؤلفة وناشرة أمريكية، رائدة حركة التفكير الإيجابي والشفاء الذاتي عبر التأكيدات (Affirmations)، ومؤسسة دار نشر Hay House؛ حقق كتابها «يمكنك شفاء حياتك» مبيعات تتجاوز 50 مليون نسخة.",
        "works": ["Heal Your Body (1976)", "You Can Heal Your Life (1984)", "The Power Is Within You (1991)"],
        "related": [
            {"id": "wrk-you-can-heal-your-life", "title": "يمكنك شفاء حياتك", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-john-bradshaw",
        "title": "جون برادشو",
        "en": "John Bradshaw",
        "dates": "الولايات المتحدة · 1933–2016",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "2016",
        "school": "علم النفس الشعبي وعلاج صدمات الأسرة",
        "is_pop": True,
        "lede": "معالج ومؤلف ومحاضر جماهيري أمريكي، كان له الفضل الأكبر في نشر وتعميم مفاهيم 'الطفل الداخلي الجريح' (Wounded Inner Child) و'الخزي السام' (Toxic Shame) في الثقافة الشعبية وعلاج الإدمان والاعتمادية.",
        "works": ["Bradshaw On: The Family (1988)", "Healing the Shame That Binds You (1988)", "Homecoming: Reclaiming and Championing Your Inner Child (1990)"],
        "related": [
            {"id": "wrk-homecoming-inner-child", "title": "العودة إلى الوطن: استعادة طفلك الداخلي", "type": "عمل / كتاب"},
            {"id": "con-inner-child-popular", "title": "الطفل الداخلي في علم النفس الشعبي", "type": "مفهوم"}
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
    lines.append(f"إسهامات رئيسية في مجال {item['school']}، ونشر مفاهيم وأطر سيكولوجية إنسانية مؤثرة عالمياً.")
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
        "slug": "wrk-feeling-good",
        "title": "الشعور بالرضا: العلاج الجديد للمزاج",
        "en": "Feeling Good: The New Mood Therapy",
        "dates": "1980 · ديفيد بيرنز",
        "language": "الإنجليزية",
        "active_start": 1980,
        "active_end": 1980,
        "school": "العلاج المعرفي السلوكي",
        "author_id": "thk-jburns",
        "author_title": "ديفيد بيرنز",
        "lede": "الكتاب الذي جعل العلاج المعرفي السلوكي (CBT) متاحاً لملايين القراء في العالم (أكثر من 5 ملايين نسخة)؛ يقدم أدوات منهجية لتحديد التشوهات المعرفية وتعديل الأفكار التلقائية السلبية وعلاج الاكتئاب الخفيف والمتوسط بالقراءة (Bibliotherapy).",
        "sections": [
            ("التشوهات المعرفية العشرة", "التفكير بطريقة الكل أو لا شيء، التعميم الزائد، الفلترة العقلية، قراءة الأفكار، التهويل والتصغير، والتفكير بـ 'ينبغي'."),
            ("الأثر الإكلينيكي للببليوثيرابي", "أثبتت دراسات مقارنة متعددة أن قراءة الكتاب كعلاج بالقراءة تُحدث تحسناً ملموساً يماثل جلسات العلاج النفسي المنفردة في حالات الاكتئاب غير المعقد.")
        ]
    },
    {
        "slug": "wrk-7-habits",
        "title": "العادات السبع للناس الأكثر فاعلية",
        "en": "The 7 Habits of Highly Effective People",
        "dates": "1989 · ستيفن كوفي",
        "language": "الإنجليزية",
        "active_start": 1989,
        "active_end": "1989",
        "school": "علم النفس الشعبي والقيادة الشخصية",
        "author_id": "thk-stephen-covey",
        "author_title": "ستيفن كوفي",
        "lede": "أحد أكثر كتب الإدارة الذاتية والقيادة الشخصية تأثيراً في التاريخ (أكثر من 40 مليون نسخة بـ 40 لغة)؛ يطرح إطاراً متكاملاً للتحول من التبعية إلى الاستقلال ثم إلى الاعتماد المتبادل عبر مبادئ وقيم جوهرية.",
        "sections": [
            ("العادات السبع", "1. كن مبادراً (Proactive). 2. ابدأ والنهاية في ذهنك. 3. ضع الأهم أولاً. 4. فكر بطريقة ربح-ربح. 5. اسعَ أولاً لتَفهم ثم لتُفهم. 6. التكاتف والتآزر (Synergy). 7. اشحذ المنشار (التجديد المستمر)."),
            ("أخلاق الشخصية مقابل أخلاق المظهر", "نقد كوفي لثقافة الحيل السطحية والتركيز على غرس الفضائل الأصيلة (النزاهة والعدالة).")
        ]
    },
    {
        "slug": "wrk-awaken-giant-within",
        "title": "أيقظ العملاق الذي بداخلك",
        "en": "Awaken the Giant Within",
        "dates": "1991 · توني روبنز",
        "language": "الإنجليزية",
        "active_start": 1991,
        "active_end": 1991,
        "school": "علم النفس الشعبي والتكيف العصبي الترابطي",
        "author_id": "thk-trobbins",
        "author_title": "توني روبنز",
        "lede": "عمل تأسيسي في حركة التحفيز وتطوير الأداء الشخصي؛ يقدم نظام 'التكيف العصبي الترابطي' (NAC) للتحكم الفوري في الانفعالات والحالة الجسدية والمعتقدات والقرارات المصيرية.",
        "sections": [
            ("قوة القرارات ومحرك الألم والمتعة", "كل سلوك إنساني مدفوع بالحاجة لتجنب الألم أو كسب المتعة؛ وتغيير السلوك يقتضي إعادة ربط الألم بالعادات القديمة والمتعة بالعادات الجديدة."),
            ("الأثر الجماهيري", "رسخ الكتاب حضور روبنز كأشهر مدرب حياة ومتحدث تحفيزي عالمي.")
        ]
    },
    {
        "slug": "wrk-48-laws-of-power",
        "title": "48 قانوناً للقوة",
        "en": "The 48 Laws of Power",
        "dates": "1998 · روبرت غرين",
        "language": "الإنجليزية",
        "active_start": 1998,
        "active_end": 1998,
        "school": "علم النفس الشعبي وسيكولوجيا القوة",
        "author_id": "thk-robert-greene",
        "author_title": "روبرت غرين",
        "lede": "كتاب واسع الانتشار ومثير للجدل (بيع منه ملايين النسخ)؛ يستخلص من 3000 عام من التاريخ الفلسفي والسياسي قواعد براغماتية صارمة لسيكولوجيا السلطة والتأثير والدفاع ضد الميكافيلية.",
        "sections": [
            ("القواعد الكلاسيكية للقوة", "لا تشرق أبداً أكثر من سيدك، اكتم نواياك، قل دائماً أقل مما يلزم، واكسب بالعمل لا بالحجة."),
            ("القراءة النقدية والأخلاقية", "يُنقد لتشجيعه المناورة والشك، بينما يدافع مؤلفه بأنه يقدم تحليلاً واقعياً لحماية الذات في بيئات العمل الصعبة.")
        ]
    },
    {
        "slug": "wrk-laws-of-human-nature",
        "title": "قوانين الطبيعة البشرية",
        "en": "The Laws of Human Nature",
        "dates": "2018 · روبرت غرين",
        "language": "الإنجليزية",
        "active_start": 2018,
        "active_end": 2018,
        "school": "علم النفس الشعبي والشخصية",
        "author_id": "thk-robert-greene",
        "author_title": "روبرت غرين",
        "lede": "كتاب موسوعي يستكشف الدوافع اللاواعية، والظل النفسي، والنرجسية، والعدوانية الكامنة وراء السلوك الإنساني، مقدماً دليلاً لتطوير الاستبصار الذاتي والذكاء الاجتماعي العاطفي.",
        "sections": [
            ("تفكيك الأوهام النفسية", "قانون اللاعقلانية، قانون النرجسية، قانون لعب الأدوار، وقانون قصر النظر العاطفي."),
            ("تطوير التعاطف والوعي بالظل", "مواجهة الجوانب المظلمة في الذات لتحويلها إلى طاقة إبداعية وتواصل ناضج.")
        ]
    },
    {
        "slug": "wrk-power-of-now",
        "title": "قوة الآن: دليل إلى التنوير الروحي",
        "en": "The Power of Now",
        "dates": "1997 · إيكهارت تول",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": 1997,
        "school": "علم النفس الشعبي واليقظة الروحية",
        "author_id": "thk-eckhart-tolle",
        "author_title": "إيكهارت تول",
        "lede": "ظاهرة روحية ونفسية عالمية تُرجمت لأكثر من 30 لغة وبيعت منها ملايين النسخ؛ يطرح أن معظم المعاناة النفسية والقلق تنبع من استغراق العقل في اجترار الماضي أو التوجس من المستقبل، وأن التحرر يكمن في الحضور التام في 'الآن'.",
        "sections": [
            ("تفكيك طغيان التفكير و'جسد الألم'", "التمييز بين 'الأنا الفكرية' وبين الوعي الشاهد، ومفهوم 'جسد الألم' (Pain-body) كطاقة انفعالية متراكمة تتغذى على المعاناة."),
            ("الأثر في ثقافة اليقظة المعاصرة", "أصبح مرجعاً أساسياً لحركات التأمل واليقظة الذهنية في الغرب.")
        ]
    },
    {
        "slug": "wrk-learned-optimism",
        "title": "التفاؤل المكتسب: كيف تغير عقلك وحياتك",
        "en": "Learned Optimism: How to Change Your Mind and Your Life",
        "dates": "1991 · مارتن سيليجمان",
        "language": "الإنجليزية",
        "active_start": 1991,
        "active_end": 1991,
        "school": "علم النفس الإيجابي",
        "author_id": "thk-mseligman",
        "author_title": "مارتن سيليجمان",
        "lede": "كتاب أكاديمي-شعبي رائد نقل فيه سيليجمان أبحاث 'العجز المتعلم' إلى 'التفاؤل المكتسب'؛ موضحاً أن التفاؤل ليس سذاجة بل مهارة معرفية يمكن تعلمها عبر تعديل أسلوب التفسير السببي للأحداث (Explanatory Style).",
        "sections": [
            ("الأبعاد الثلاثة لأسلوب التفسير (The 3 Ps)", "1. الدوام (Permanence): مؤقت مقابل دائم. 2. الشمول (Pervasiveness): محدد مقابل عام. 3. الشخصنة (Personalization): داخلي مقابل خارجي."),
            ("نموذج ABCDE لدحض الأفكار التشاؤمية", "تطبيق تقنيات العلاج المعرفي لتفنيد المعتقدات الكارثية واكتساب المرونة النفسية.")
        ]
    },
    {
        "slug": "wrk-righteous-mind",
        "title": "العقل الصالح: لماذا ينقسم الأخيار حول السياسة والدين",
        "en": "The Righteous Mind",
        "dates": "2012 · جوناثان هايدت",
        "language": "الإنجليزية",
        "active_start": 2012,
        "active_end": 2012,
        "school": "علم النفس الأخلاقي والاجتماعي",
        "author_id": "thk-jonathan-haidt",
        "author_title": "جوناثان هايدت",
        "lede": "عمل فكري وعلمي واسع الانتشار يستكشف جذور الانقسام الأيديولوجي والسياسي؛ مؤكداً أن الحدس الأخلاقي يأتي أولاً بينما يقوم التفكير العقلاني بالتبرير اللاحق (استعارة الفيل والراكب).",
        "sections": [
            ("الأسس الأخلاقية الستة", "الرعاية/الضرر، العدالة/الغش، الولاء/الخيانة، السلطة/التخريب، القداسة/الانحطاط، والحرية/القمع."),
            ("أثر الكتاب", "فتح آفاقاً جديدة في فهم الاستقطاب السياسي وعلم النفس الانتخابي.")
        ]
    },
    {
        "slug": "wrk-anxious-generation",
        "title": "الجيل القلق: كيف تؤدي إعادة برمجة الطفولة العظيمة إلى وباء المرض النفسي",
        "en": "The Anxious Generation",
        "dates": "2024 · جوناثان هايدت",
        "language": "الإنجليزية",
        "active_start": 2024,
        "active_end": 2024,
        "school": "علم النفس الاجتماعي والنمائي",
        "author_id": "thk-jonathan-haidt",
        "author_title": "جوناثان هايدت",
        "lede": "كتاب تصدر قوائم المبيعات العالمية فور صدوره؛ يوثق بالأدلة الإحصائية الارتفاع الحاد في معدلات القلق والاكتئاب وإيذاء النفس بين المراهقين بعد عام 2010 إثر الانتقال من 'الطفولة القائمة على اللعب' إلى 'الطفولة القائمة على الهواتف الذكية'.",
        "sections": [
            ("الأضرار الأربعة للهواتف الذكية", "الحرمان من النوم، التفتت الاجتماعي، الإدمان الرقمي، وتراجع الانتباه والتركيز."),
            ("الحلول الجماعية الإصلاحية", "حظر الهواتف في المدارس، تأخير امتلاك الهواتف الذكية حتى سن 14، واستعادة اللعب الحر المستقل.")
        ]
    },
    {
        "slug": "wrk-predictably-irrational",
        "title": "اللامنطقية المتوقعة: القوى الخفية التي تشكل قراراتنا",
        "en": "Predictably Irrational",
        "dates": "2008 · دان آرييلي",
        "language": "الإنجليزية",
        "active_start": 2008,
        "active_end": 2008,
        "school": "الاقتصاد السلوكي وعلم النفس المعرفي",
        "author_id": "thk-dan-ariely",
        "author_title": "دان آرييلي",
        "lede": "كتاب شهير يبرهن عبر تجارب سلوكية ممتعة أن أخطاء البشر في اتخاذ القرارات والإنفاق ليست عشوائية، بل متكررة وممنهجة وقابلة للتنبؤ العلمي الدقيق.",
        "sections": [
            ("مفاهيم اتخاذ القرار اليومية", "تأثير الصفر/المجاني، مقارنة الخيارات بالنسبية، فخ الإرساء السعري (Anchoring)، وصراع الأعراف الاجتماعية مع الأعراف المالية."),
            ("الأثر في السياسات العامة والتسويق", "إعادة هيكلة تصميم الخيارات التسعيرية والمصرفية لحماية المستهلكين.")
        ]
    },
    {
        "slug": "wrk-nudge",
        "title": "سقزة: تحسين القرارات المتعلقة بالصحة والثروة والسعادة",
        "en": "Nudge: Improving Decisions About Health, Wealth, and Happiness",
        "dates": "2008 · ريتشارد ثالر وكاس سنستين",
        "language": "الإنجليزية",
        "active_start": 2008,
        "active_end": 2008,
        "school": "الاقتصاد السلوكي والسياسات العامة",
        "author_id": "thk-rkthaler",
        "author_title": "ريتشارد هـ. ثالر",
        "lede": "الكتاب الذي غيّر تصميم السياسات العامة والحكومية عالمياً؛ يطرح مفهوم 'الأبوية التحررية' (Libertarian Paternalism) وهندسة الاختيار لتوجيه السلوك البشري نحو الأفضل دون إجبار أو منع.",
        "sections": [
            ("هندسة الاختيار والخيارات التلقائية (Default Options)", "استغلال ميل الإنسان للبقاء على الخيار التلقائي لزيادة معدلات التبرع بالأعضاء والادخار التقاعدي."),
            ("تأسيس وحدات السلوك الحكومية (Nudge Units)", "إنشاء فرق تطبيقية في بريطانيا والولايات المتحدة لإصلاح الخدمات العامة اعتماداً على علم النفس السلوكي.")
        ]
    },
    {
        "slug": "wrk-5-love-languages",
        "title": "لغات الحب الخمس: سر الحب الذي يدوم",
        "en": "The 5 Love Languages",
        "dates": "1992 · غاري تشابمان",
        "language": "الإنجليزية",
        "active_start": 1992,
        "active_end": 1992,
        "school": "علم النفس الشعبي والإرشاد الزواجي",
        "author_id": "thk-gary-chapman",
        "author_title": "غاري تشابمان",
        "lede": "أحد أشهر كتب العلاقات في العالم (أكثر من 20 مليون نسخة)؛ يطرح أن التعبير عن الحب وتلقيه يتم عبر خمس لغات أساسية يختلف تفضيلها من شريك لآخر.",
        "sections": [
            ("اللغات الخمس", "1. كلمات التشجيع والتوكيد. 2. تكريس الوقت وقضاء وقت نوعي. 3. تبادل الهدايا. 4. أعمال الخدمة والمساعدة. 5. التلامس الجسدي."),
            ("التطبيق الزواجي", "تعلم التحدث باللغة العاطفية الأساسية للشريك لملء 'خزان الحب' العاطفي وتجنب سوء الفهم المزمن.")
        ]
    },
    {
        "slug": "wrk-highly-sensitive-person",
        "title": "الشخص عالي الحساسية: كيف تزدهر عندما يغمرك العالم",
        "en": "The Highly Sensitive Person (HSP)",
        "dates": "1996 · إيلين آرون",
        "language": "الإنجليزية",
        "active_start": 1996,
        "active_end": 1996,
        "school": "علم النفس الإكلينيكي وحساسية المعالجة الحسية",
        "author_id": "thk-elaine-aron",
        "author_title": "إيلين آرون",
        "lede": "العمل التأسيسي الذي وثق سمة الحساسية العالية لدى 15-20% من البشر، مبيناً أنها سمة عصبية ونفسية فطرية وليست خللاً أو اضطراباً، وتتسم بعمق المعالجة والاستجابة الانفعالية القوية.",
        "sections": [
            ("معايير DOES للسمة", "1. عمق المعالجة (Depth of processing). 2. فرط الاستثارة الحسية (Overstimulation). 3. الاستجابة الانفعالية والتعاطف (Emotional reactivity). 4. حساسية المثيرات الدقيقة (Sensing the subtle)."),
            ("الأثر الإكلينيكي والتربوي", "تخفيف الوصم عن الأطفال والبالغين الحساسين وتقديم استراتيجيات للتعامل مع الإرهاق الحسي.")
        ]
    },
    {
        "slug": "wrk-you-can-heal-your-life",
        "title": "يمكنك شفاء حياتك",
        "en": "You Can Heal Your Life",
        "dates": "1984 · لويز هاي",
        "language": "الإنجليزية",
        "active_start": 1984,
        "active_end": 1984,
        "school": "علم النفس الشعبي والتأكيدات الإيجابية",
        "author_id": "thk-louise-hay",
        "author_title": "لويز هاي",
        "lede": "كتاب كلاسيكي في حركة المساعدة الذاتية الروحية بيع منه أكثر من 50 مليون نسخة؛ يربط بين الأنماط الفكرية السلبية والشعور بالذنب وبين الأعراض الجسدية، داعياً للشفاء عبر حب الذات والتسامح والتأكيدات اللفظية.",
        "sections": [
            ("الأطروحة المركزية", "استبدال الانتقاد الذاتي والاستياء بقبول الذات اللامشروط وتعديل المعتقدات الموروثة من الطفولة."),
            ("القراءة النقدية", "يُنقد علمياً بسبب ادعاءاته بمسؤولية المريض عن أمراضه العضوية الخطيرة، بينما يُقدّر لدوره في تعزيز العناية الذاتية الإيجابية.")
        ]
    },
    {
        "slug": "wrk-homecoming-inner-child",
        "title": "العودة إلى الوطن: استعادة طفلك الداخلي وحمايته",
        "en": "Homecoming: Reclaiming and Championing Your Inner Child",
        "dates": "1990 · جون برادشو",
        "language": "الإنجليزية",
        "active_start": 1990,
        "active_end": 1990,
        "school": "علم النفس الشعبي وعلاج صدمات الأسرة",
        "author_id": "thk-john-bradshaw",
        "author_title": "جون برادشو",
        "lede": "كتاب تصدر قوائم نيويورك تايمز للبِست سيلر وأطلق ثورة علاج 'الطفل الداخلي'؛ يقدم دليلاً تأهيلياً لشفاء جراح الطفولة، وتفكيك الخزي السام الموروث من الأسر غير الفعالة (Dysfunctional Families).",
        "sections": [
            ("مراحل النمو واستعادة الذات", "إعادة التربية الوالدية الذاتية (Self-Reparenting) للرضيع، والطفل الصغير، ومرحلة المدرسة، والمراهق الداخلي."),
            ("الأثر في الثقافة العلاجية", "تحول مصطلح 'الطفل الداخلي' إلى جزء أساسي من الثقافة النفسية الشعبية ومجموعات الدعم.")
        ]
    },
    {
        "slug": "wrk-getting-love-you-want",
        "title": "الحصول على الحب الذي تريده: دليل الأزواج",
        "en": "Getting the Love You Want",
        "dates": "1988 · هارفيل هندريكس",
        "language": "الإنجليزية",
        "active_start": 1988,
        "active_end": 1988,
        "school": "علاج العلاقات بإيماجو وعلم النفس الشعبي",
        "author_id": "thk-hhendrix",
        "author_title": "هارفي هندرِكس",
        "lede": "المرجع التأسيسي لعلاج العلاقات بإيماجو (Imago Relationship Therapy) بيع منه أكثر من 4 ملايين نسخة؛ يفسر كيف يختار الإنسان شريك حياته بناءً على صورة لاواعية (Imago) تعيد إنتاج جروح طفولته للبحث عن الشفاء.",
        "sections": [
            ("الدينامية اللاواعية للاختيار الزواجي", "صراع القوة بين الشريكين كفرصة غير واعية لإنهاء مهام الطفولة غير المكتملة."),
            ("حوار إيماجو الثلاثي (Imago Dialogue)", "المرآة (Mirroring)، التحقق من صحة المشاعر (Validation)، والتعاطف (Empathy).")
        ]
    },
    {
        "slug": "wrk-seven-principles-marriage",
        "title": "المبادئ السبعة لنجاح الزواج",
        "en": "The Seven Principles for Making Marriage Work",
        "dates": "1999 · جون غوتمان ونان سيلفر",
        "language": "الإنجليزية",
        "active_start": 1999,
        "active_end": 1999,
        "school": "علم النفس الإكلينيكي والعلاقات الأسرية",
        "author_id": "thk-jgottman",
        "author_title": "جون غوتمان",
        "lede": "كتاب بِست سيلر عالمي استند لأبحاث مختبر غوتمان للحب (Love Lab) على آلاف الأزواج؛ يقدم سبعة مبادئ تجريبية للحفاظ على استقرار الزواج والتنبؤ بمصير العلاقات بدقة تفوق 90%.",
        "sections": [
            ("فرسان الهلاك الأربعة (The Four Horsemen)", "النقد الهجومي، الازدراء (أخطرها)، الدفاعية، والمماطلة وجدار الصمت (Stonewalling)."),
            ("المبادئ السبعة للنجاح", "توسيع خرائط الحب، رعاية الإعجاب والتقدير، التوجه نحو الشريك بدلاً من الابتعاد، وقبول التأثير المتبادل.")
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

# Concepts Data
concepts_data = [
    {
        "slug": "con-five-love-languages",
        "title": "لغات الحب الخمس (الأطر التعبيرية في العلاقات)",
        "en": "The Five Love Languages",
        "school": "علم النفس الشعبي",
        "active_start": 1992,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-5-love-languages", "title": "لغات الحب الخمس", "type": "عمل / كتاب"},
            {"id": "thk-gary-chapman", "title": "غاري تشابمان", "type": "مفكر"}
        ],
        "gaps": [
            "الأبحاث السيكومترية الحديثة في تقييم موثوقية استبيان لغات الحب الخمس.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم وتصنيف نفسي شعبي صاغه غاري تشابمان عام 1992، يفترض أن الأفراد يفضلون طرقاً مميزة للتعبير عن المودة وتلقيها: كلمات التوكيد، تكريس الوقت، الهدايا، أعمال الخدمة، والتلامس الجسدي.",
        "sections": [
            ("الدينامية والتطبيق", "يساعد النموذج الشركاء على إدراك أن الاختلاف في لغة التعبير لا يعني غياب الحب، بل تباين في الشفرة العاطفية المستخدمة."),
            ("التقييم العلمي", "يحظى بانتشار تطبيقي هائل في الاستشارات الزوجية رغم كونه نموذجاً تصنيفياً مبسطاً.")
        ]
    },
    {
        "slug": "con-highly-sensitive-person",
        "title": "الشخص عالي الحساسية (حساسية المعالجة الحسية HSP)",
        "en": "Highly Sensitive Person (HSP) / Sensory Processing Sensitivity",
        "school": "علم النفس الإكلينيكي والشخصية",
        "active_start": 1996,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-highly-sensitive-person", "title": "الشخص عالي الحساسية", "type": "عمل / كتاب"},
            {"id": "thk-elaine-aron", "title": "إيلين آرون", "type": "مفكر"}
        ],
        "gaps": [
            "الربط بين سمة HSP والتصوير العصبي الوظيفي للوزة والقشرة الجزيرية.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "سمة مزاجية وعصبية فطرية تتسم بحساسية عالية للمؤثرات البيئية والحسية والاجتماعية، وعمق معالجة المعلومات في الجهاز العصبي المركزي، وتوجد لدى نحو 20% من البشر والحيوانات.",
        "sections": [
            ("الفارق عن الخجل والانطواء", "الحساسية العالية سمة معالجة حسية بيولوجية، وليست خجلاً (الخوف من التقييم الاجتماعي) ولا انطوائية بالضرورة (يوجد 30% من الحساسين انبساطيين)."),
            ("نقاط القوة والتحديات", "عمق التعاطف والحدس والتذوق الفني في مقابل سرعة الإرهاق في البيئات المزدحمة والصاخبة.")
        ]
    },
    {
        "slug": "con-inner-child-popular",
        "title": "الطفل الداخلي في علم النفس الشعبي والعلاجي",
        "en": "The Inner Child (Pop Psychology Movement)",
        "school": "علم النفس الشعبي",
        "active_start": 1985,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-homecoming-inner-child", "title": "العودة إلى الوطن: استعادة طفلك الداخلي", "type": "عمل / كتاب"},
            {"id": "thk-john-bradshaw", "title": "جون برادشو", "type": "مفكر"}
        ],
        "gaps": [
            "الجذور التاريخية للمفهوم لدى كارل يونغ (النمط البدئي للطفل) وإريك بيرن (حالة أنا الطفل).",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم نفسي واستعارة علاجية تمثل الجزء الطفولي الأصيل في الشخصية الذي يحمل الذكريات العاطفية المبكرة، والاحتياجات غير الملباة، والصدمات والجراح غير المعالجة، إلى جانب البراءة والإبداع والفضول الفطري.",
        "sections": [
            ("تقنيات إعادة التربية الوالدية الذاتية", "ممارسة الحوار مع الطفل الداخلي باليد غير المسيطرة، وتوفير الأمان والاحتواء العاطفي الذي افتقده الشخص في صغره."),
            ("الأثر الشعبي", "أصبح مفهوماً مركزياً في علاج الصدمات المعقدة ومجموعات التعافي من الإدمان.")
        ]
    },
    {
        "slug": "con-seven-habits",
        "title": "العادات السبع للفاعلية والنمو الشخصي",
        "en": "The Seven Habits Framework",
        "school": "علم النفس الشعبي والقيادة الشخصية",
        "active_start": 1989,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-7-habits", "title": "العادات السبع للناس الأكثر فاعلية", "type": "عمل / كتاب"},
            {"id": "thk-stephen-covey", "title": "ستيفن كوفي", "type": "مفكر"}
        ],
        "gaps": [
            "تطبيقات النموذج في القيادة المؤسسية والتعليمية.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "إطار ومصفوفة نمو نفسي وسلوكي صاغها ستيفن كوفي، تنظم نضج الفرد عبر مسار متدرج: من الاعتمادية (التبعية) إلى الاستقلال عبر 'الانتصار الشخصي'، ثم إلى الاعتماد المتبادل والتعاون الفعال عبر 'الانتصار العام'.",
        "sections": [
            ("المصفوفة والمبادئ", "ترتيب الأولويات وفق الأهمية لا العجلة (مصفوفة إدارة الوقت)، وبناء حساب البنك العاطفي في العلاقات."),
            ("الأثر العالمي", "يُعد الإطار الأكثر اعتماداً في برامج تدريب القيادات وتطوير المدارس والجامعات عالمياً.")
        ]
    },
    {
        "slug": "con-toxic-positivity",
        "title": "الإيجابية السامة (إنكار المشاعر الصعبة والإلزام بالتفاؤل)",
        "en": "Toxic Positivity",
        "school": "علم النفس الشعبي والمعاصر",
        "active_start": 2015,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-subtle-art", "title": "فن اللامبالاة", "type": "عمل / كتاب"},
            {"id": "thk-mark-manson", "title": "مارك مانسون", "type": "مفكر"},
            {"id": "thk-kristin-neff", "title": "كريستين نيف", "type": "مفكر"}
        ],
        "gaps": [
            "الأبحاث الإكلينيكية حول أثر كبت الانفعالات السلبية على التنشيط العصبي الذاتي.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم نفسي نقدي يصف الفرض القسري والمفرط لحالة التفاؤل والبهجة وتعميم مقولات 'كن إيجابياً فقط'، مما يؤدي إلى قمع وإنكار المشاعر الإنسانية الطبيعية الصعبة كالحزن والغضب والخوف وتوليد شعور مركب بالذنب لدى المتألم.",
        "sections": [
            ("الأضرار السريرية", "يؤدي إسكات المشاعر الصعبة إلى مضاعفة التوتر النفسي، وقطع جسور التعاطف الإنساني الحقيقي، وتعميق العزلة."),
            ("البديل الصحي", "الاعتراف والتحقق من صحة المشاعر (Emotional Validation) وتقبل الألم كجزء طبيعي من التجربة الإنسانية بالتوازي مع بناء الأمل الواقعي.")
        ]
    },
    {
        "slug": "con-gaslighting-popular",
        "title": "التلاعب بالعقول والتضليل النفسي في الثقافة الشعبية (Gaslighting)",
        "en": "Gaslighting (Popular Concept)",
        "school": "علم النفس الشعبي والعلاقات",
        "active_start": 1944,
        "active_end": "مستمر",
        "related": [
            {"id": "dis-narcissistic-personality", "title": "اضطراب الشخصية النرجسية", "type": "اضطراب/حالة إكلينيكية"},
            {"id": "syn-stockholm", "title": "متلازمة ستوكهولم", "type": "متلازمة"}
        ],
        "gaps": [
            "تطور المفهوم من مسرحية Gaslight (1938) إلى أدبيات العنف النفسي المعاصرة.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "شكل من أشكال التلاعب وسوء المعاملة النفسية والعاطفية الخبيثة، يسعى فيه المتلاعب إلى زرع بذور الشك في عقل الضحية حول صحة ذاكرتها وإدراكها للواقع وسلامة قواها العقلية، لفرض السيطرة والهيمنة التامة عليها.",
        "sections": [
            ("الأساليب والتكتيكات الكلاسيكية", "الإنكار الصريح لوقائع حدثت، اتهام الضحية بالجنون أو فرط الحساسية، والتحريف المتعمد للحوارات لإشعارها بأنها المخطئة."),
            ("التعافي واستعادة الواقع", "توثيق الوقائع كتابياً، وضع حدود نفسية صارمة، وبناء شبكة دعم خارجية موثوقة لكسر العزلة والارتباك الذهني.")
        ]
    }
]

out_dir_con = "content/ar/drafts/concepts"
os.makedirs(out_dir_con, exist_ok=True)

for item in concepts_data:
    lines = ["---"]
    lines.append(f'slug: "{item["slug"]}"')
    lines.append('id: "[DRAFT-UNKNOWN]"')
    lines.append('type: "مفهوم"')
    lines.append('register: "popular"')
    lines.append('part: "psychology"')
    lines.append('level: "متوسط"')
    lines.append(f'title: "{item["title"]}"')
    lines.append(f'en: "{item["en"]}"')
    lines.append(f'crumb: "{item["school"]} ← المفاهيم ← {item["title"].split(" (")[0]}"')
    lines.append(f'active_start: {item["active_start"]}')
    lines.append('active_end: "مستمر"' if item["active_end"] == "مستمر" else f'active_end: {item["active_end"]}')
    lines.append("edges:")
    lines.append(f'  - rel: "belongs_to", target: "{item["school"]}", target_type: "مدرسة"')
    lines.append("related:")
    for rel in item["related"]:
        lines.append(f'  - id: "{rel["id"]}", title: "{rel["title"]}", type: "{rel["type"]}"')
    lines.append("gaps:")
    for g in item["gaps"]:
        lines.append(f'  - "{g}"')
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

    filepath = os.path.join(out_dir_con, f"{item['slug']}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"Wrote {filepath}")

print("All expanded pop items written successfully.")
