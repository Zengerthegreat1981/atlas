# -*- coding: utf-8 -*-
import os

thinkers_data = [
    {
        "slug": "thk-marshall-rosenberg",
        "title": "مارشال روزنبرغ",
        "en": "Marshall Rosenberg",
        "dates": "الولايات المتحدة · 1934–2015",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1965,
        "active_end": "2015",
        "school": "علم النفس الإنساني والتواصل اللاعنفي",
        "is_pop": True,
        "lede": "عالم نفس إكلينيكي ومؤسس مركز التواصل غير العنيف (CNVC)؛ ابتكر عملية 'التواصل غير العنيف' (Nonviolent Communication - NVC) التي أحدثت تأثيراً عالمياً في فض النزاعات وبناء التعاطف الإنساني.",
        "works": ["Nonviolent Communication: A Language of Life (1999)", "Speak Peace in a World of Conflict (2005)"],
        "related": [
            {"id": "wrk-nonviolent-communication", "title": "التواصل غير العنيف", "type": "عمل / كتاب"},
            {"id": "con-nonviolent-communication", "title": "التواصل غير العنيف", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-amir-levine",
        "title": "أمير ليفين",
        "en": "Amir Levine",
        "dates": "إسرائيل / الولايات المتحدة · 1968–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 2000,
        "active_end": "مستمر",
        "school": "علم الأعصاب وسيكولوجيا التعلق البالغ",
        "is_pop": False,
        "lede": "طبيب نفسي وعالم أعصاب وأستاذ بجامعة كولومبيا؛ اشتهر بأبحاثه الرائدة في نقل نظرية التعلق لجون بولبي إلى سيكولوجيا العلاقات العاطفية بين البالغين عبر كتابه الشهير «المتعلقون».",
        "works": ["Attached: The New Science of Adult Attachment (2010)"],
        "related": [
            {"id": "wrk-attached", "title": "المتعلقون", "type": "عمل / كتاب"},
            {"id": "con-attachment-styles-popular", "title": "أنماط التعلق في العلاقات", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-rachel-heller",
        "title": "راشيل هيلر",
        "en": "Rachel S. F. Heller",
        "dates": "إسرائيل / الولايات المتحدة · 1972–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / العبرية",
        "active_start": 2005,
        "active_end": "مستمر",
        "school": "علم النفس الاجتماعي وعلاقات التعلق",
        "is_pop": True,
        "lede": "عالمة نفس اجتماعي ومؤلفة حاصلة على الماجستير من جامعة كولومبيا، شاركت في تأليف كتاب «المتعلقون» وساهمت في تبسيط استراتيجيات التعلق الآمن لجمهور القراء.",
        "works": ["Attached: The New Science of Adult Attachment (2010)"],
        "related": [
            {"id": "wrk-attached", "title": "المتعلقون", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-richard-schwartz",
        "title": "ريتشارد شوارتز",
        "en": "Richard C. Schwartz",
        "dates": "الولايات المتحدة · 1949–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1980,
        "active_end": "مستمر",
        "school": "علاج أنظمة الأسرة الداخلية (IFS)",
        "is_pop": False,
        "lede": "معالج أسري وأستاذ مساعد سابق بجامعة هارفارد للطب؛ مؤسس نموذج 'علاج أنظمة الأسرة الداخلية' (Internal Family Systems - IFS) الذي ينظر إلى النفس كعائلة متعددة الأجزاء تحكمها 'الذات الجوهرية'.",
        "works": ["Internal Family Systems Therapy (1995)", "No Bad Parts (2021)", "You Are the One You've Been Waiting For (2008)"],
        "related": [
            {"id": "wrk-no-bad-parts", "title": "لا توجد أجزاء سيئة", "type": "عمل / كتاب"},
            {"id": "con-internal-family-systems-popular", "title": "أنظمة الأسرة الداخلية", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-russ-harris",
        "title": "روس هاريس",
        "en": "Russ Harris",
        "dates": "المملكة المتحدة / أستراليا · 1966–",
        "country": "أستراليا",
        "language": "الإنجليزية",
        "active_start": 2000,
        "active_end": "مستمر",
        "school": "العلاج بالقبول والالتزام (ACT)",
        "is_pop": True,
        "lede": "طبيب ومعالج نفسي ومدرب دولي رائد في 'العلاج بالقبول والالتزام' (ACT)؛ حقق كتابه «فخ السعادة» انتشاراً عالمياً واسعاً ببيعه أكثر من مليون نسخة وترجمته لأكثر من 30 لغة.",
        "works": ["The Happiness Trap (2007)", "ACT Made Simple (2009)", "The Reality Slap (2011)"],
        "related": [
            {"id": "wrk-happiness-trap", "title": "فخ السعادة", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-peter-levine",
        "title": "بيتر ليفين",
        "en": "Peter A. Levine",
        "dates": "الولايات المتحدة · 1942–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1970,
        "active_end": "مستمر",
        "school": "العلاج الجسدي للصدمات (Somatic Experiencing)",
        "is_pop": False,
        "lede": "عالم فيزياء حيوية وطبيب نفسي؛ مؤسس أسلوب 'التجربة الجسدية' (Somatic Experiencing - SE) لعلاج الصدمات النفسية، معتمداً على مراقبة استجابة الحيوانات في البرية لإفراغ طاقة الصدمة الحركية.",
        "works": ["Waking the Tiger: Healing Trauma (1997)", "In an Unspoken Voice (2010)", "Trauma and Memory (2015)"],
        "related": [
            {"id": "wrk-waking-the-tiger", "title": "إيقاظ النمر", "type": "عمل / كتاب"},
            {"id": "con-somatic-experiencing-popular", "title": "التجربة الجسدية للصدمة", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-stephen-porges",
        "title": "ستيفن بورغيس",
        "en": "Stephen Porges",
        "dates": "الولايات المتحدة · 1945–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1970,
        "active_end": "مستمر",
        "school": "علم الأعصاب النفسي والفيزيولوجيا الحيوية",
        "is_pop": False,
        "lede": "أستاذ الطب النفسي وعلم الأعصاب بجامعة نورث كارولينا؛ مؤسس 'النظرية العصبية المبهمة' (Polyvagal Theory) التي أحدثت ثورة في فهم استجابة الجهاز العصبي الذاتي للأمان والتهديد والتواصل الاجتماعي.",
        "works": ["The Polyvagal Theory: Neurophysiological Foundations of Emotions (2011)", "The Pocket Guide to the Polyvagal Theory (2017)"],
        "related": [
            {"id": "wrk-polyvagal-theory-therapy", "title": "النظرية العصبية المبهمة في العلاج", "type": "عمل / كتاب"},
            {"id": "con-polyvagal-theory-popular", "title": "السلم العصبي المبهم", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-deb-dana",
        "title": "ديب دانا",
        "en": "Deb Dana",
        "dates": "الولايات المتحدة · 1956–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1995,
        "active_end": "مستمر",
        "school": "العلاج العصبي المبهم وتعديل الصدمات",
        "is_pop": True,
        "lede": "معالجة نفسية ومؤلفة ومحاضرة؛ كان لها الفضل الأكبر في ترجمة وتطبيق النظرية العصبية المبهمة لستيفن بورغيس إلى ممارسات سريرية وتمارين تنظيم ذاتي مبسطة للمعالجين والجمهور.",
        "works": ["The Polyvagal Theory in Therapy (2018)", "Anchored: How to Befriend Your Nervous System Using Polyvagal Theory (2021)"],
        "related": [
            {"id": "wrk-polyvagal-theory-therapy", "title": "النظرية العصبية المبهمة في العلاج", "type": "عمل / كتاب"},
            {"id": "con-polyvagal-theory-popular", "title": "السلم العصبي المبهم", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-nedra-tawwab",
        "title": "نيدرا غلوفر تواب",
        "en": "Nedra Glover Tawwab",
        "dates": "الولايات المتحدة · 1982–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2007,
        "active_end": "مستمر",
        "school": "علم النفس الشعبي والعلاقات الأسرية",
        "is_pop": True,
        "lede": "معالجة أسرية ومؤلفة أمريكية تصدرت كتبها قوائم نيويورك تايمز للبِست سيلر؛ اشتهرت بتبسيط مفاهيم وضع الحدود النفسية والتحرر من دراما العلاقات الأسرية السامة.",
        "works": ["Set Boundaries, Find Peace (2021)", "Drama Free: A Guide to Managing Unhealthy Family Relationships (2023)"],
        "related": [
            {"id": "wrk-set-boundaries-find-peace", "title": "ضع حدوداً، تجد سلاماً", "type": "عمل / كتاب"},
            {"id": "con-boundaries-psychological", "title": "الحدود النفسية والعاطفية", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-lindsay-gibson",
        "title": "ليندسي جيبسون",
        "en": "Lindsay C. Gibson",
        "dates": "الولايات المتحدة · 1952–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1985,
        "active_end": "مستمر",
        "school": "علم النفس الإكلينيكي وعلاج الصدمات التطورية",
        "is_pop": True,
        "lede": "عالمة نفس إكلينيكي ومؤلفة حققت كتبها انتشاراً عالمياً واسعاً ببيعه ملايين النسخ؛ اشتهرت بتأصيل مفهوم 'اللاتنضج العاطفي الوالدي' وكيفية تعافي الأبناء البالغين من الإهمال العاطفي غير المرئي.",
        "works": ["Adult Children of Emotionally Immature Parents (2015)", "Recovering from Emotionally Immature Parents (2019)", "Self-Care for Adult Children of Emotionally Immature Parents (2021)"],
        "related": [
            {"id": "wrk-emotionally-immature-parents", "title": "أبناء الآباء غير الناضجين عاطفياً", "type": "عمل / كتاب"},
            {"id": "con-emotional-immaturity-parents", "title": "اللاتنضج العاطفي الوالدي", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-susan-forward",
        "title": "سوزان فوروارد",
        "en": "Susan Forward",
        "dates": "الولايات المتحدة · 1938–2020",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "2020",
        "school": "علم النفس الشعبي والعلاج الأسري",
        "is_pop": True,
        "lede": "معالجة نفسية ومؤلفة رائدة تصدرت كتبها قوائم البِست سيلر لعقود؛ صاغت مفاهيم شعبية وسريرية كبرى مثل 'الآباء السامون' و'الابتزاز العاطفي' (Emotional Blackmail).",
        "works": ["Toxic Parents (1989)", "Emotional Blackmail (1997)", "Men Who Hate Women and the Women Who Love Them (1986)", "Mothers Who Can't Love (2013)"],
        "related": [
            {"id": "wrk-toxic-parents", "title": "الآباء السامون", "type": "عمل / كتاب"},
            {"id": "wrk-emotional-blackmail", "title": "الابتزاز العاطفي", "type": "عمل / كتاب"},
            {"id": "con-emotional-blackmail", "title": "الابتزاز العاطفي", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-kubler-ross",
        "title": "إليزابيث كوبلر-روس",
        "en": "Elisabeth Kübler-Ross",
        "dates": "سويسرا / الولايات المتحدة · 1926–2004",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية / الألمانية",
        "active_start": 1958,
        "active_end": "2004",
        "school": "الطب النفسي وسيكولوجيا الموت والحداد",
        "is_pop": False,
        "lede": "طبيبة نفسية سويسرية-أمريكية رائدة، أسست لحركة رعاية المحتضرين (Hospice Care) وصاغت نموذج 'مراحل الحزن الخمس' (DABDA) الشهير عالمياً في كتابها الكلاسيكي «عن الموت والاحتضار».",
        "works": ["On Death and Dying (1969)", "Questions and Answers on Death and Dying (1974)", "On Grief and Grieving (with David Kessler, 2005)"],
        "related": [
            {"id": "wrk-on-death-and-dying", "title": "عن الموت والاحتضار", "type": "عمل / كتاب"},
            {"id": "con-five-stages-of-grief", "title": "مراحل الحزن الخمس", "type": "مفهوم"}
        ]
    },
    {
        "slug": "thk-judson-brewer",
        "title": "جودسون بروير",
        "en": "Judson Brewer",
        "dates": "الولايات المتحدة · 1974–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 2005,
        "active_end": "مستمر",
        "school": "علم الأعصاب السريري وعلاج الإدمان والقلق",
        "is_pop": False,
        "lede": "طبيب نفسي وعالم أعصاب ومدير الأبحاث والابتكار بمركز اليقظة الذهنية بجامعة براون؛ اشتهر بأبحاثه حول دوائر العادات الدماغية وعلاج القلق والإدمان باليقظة الذهنية.",
        "works": ["The Craving Mind (2017)", "Unwinding Anxiety (2021)", "The Hunger Habit (2024)"],
        "related": [
            {"id": "wrk-unwinding-anxiety", "title": "تفكيك القلق", "type": "عمل / كتاب"}
        ]
    },
    {
        "slug": "thk-robert-bolton",
        "title": "روبرت بولتون",
        "en": "Robert Bolton",
        "dates": "الولايات المتحدة · 1935–",
        "country": "الولايات المتحدة",
        "language": "الإنجليزية",
        "active_start": 1975,
        "active_end": "2010",
        "school": "علم النفس الشعبي ومهارات التواصل",
        "is_pop": True,
        "lede": "عالم نفس ومؤلف واستشاري؛ حقق كتابه الكلاسيكي «مهارات التعامل مع الناس» انتشاراً هائلاً كدليل تدريبي شامل للاستماع النشط والتوكيدية وإدارة الصراعات البين-شخصية.",
        "works": ["People Skills: How to Assert Yourself, Listen to Others, and Resolve Conflicts (1979)", "Social Style/Management Style (1984)"],
        "related": [
            {"id": "wrk-people-skills", "title": "مهارات التعامل مع الناس", "type": "عمل / كتاب"}
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
    lines.append(f"إسهامات رئيسية في مجال {item['school']} ونشر المعرفة النفسية والعلاجية التطبيقية.")
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
        "slug": "wrk-nonviolent-communication",
        "title": "التواصل غير العنيف: لغة الحياة",
        "en": "Nonviolent Communication: A Language of Life",
        "dates": "1999 · مارشال روزنبرغ",
        "language": "الإنجليزية",
        "active_start": 1999,
        "active_end": 1999,
        "school": "علم النفس الإنساني والتواصل اللاعنفي",
        "author_id": "thk-marshall-rosenberg",
        "author_title": "مارشال روزنبرغ",
        "lede": "المرجع التأسيسي العالمي في التواصل التعاطفي وحل النزاعات (أكثر من 5 ملايين نسخة بـ 35 لغة)؛ يطرح نموذجاً من 4 خطوات للتعبير الصادق والاستماع التعاطفي بعيداً عن لغة الأحكام واللوم.",
        "sections": [
            ("عناصر التواصل الأربعة (OFNR)", "1. الملاحظة دون تقييم أو حكم (Observations). 2. التعبير عن المشاعر الحقيقية (Feelings). 3. تحديد الاحتياجات الإنسانية الجوهرية (Needs). 4. صياغة طلبات محددة وإيجابية وقابلة للتنفيذ (Requests)."),
            ("لغة الزرافة ولغة ابن آوى الرمزية", "استعارة 'ابن آوى' للغة اللوم والسيطرة واستعارة 'الزرافة' (صاحبة أكبر قلب) للغة التعاطف والتفهم.")
        ]
    },
    {
        "slug": "wrk-attached",
        "title": "المتعلقون: العلم الجديد للتعلق بالبالغين وكيف يساعدك في العثور على الحب والحفاظ عليه",
        "en": "Attached: The New Science of Adult Attachment",
        "dates": "2010 · أمير ليفين وراشيل هيلر",
        "language": "الإنجليزية",
        "active_start": 2010,
        "active_end": "2010",
        "school": "علم الأعصاب وسيكولوجيا التعلق البالغ",
        "author_id": "thk-amir-levine",
        "author_title": "أمير ليفين",
        "lede": "أشهر كتاب في سيكولوجيا العلاقات العاطفية في العقد الأخير (أكثر من 3 ملايين نسخة)؛ يطبق نظرية التعلق لشرح أسباب التنافر والانجذاب بين الشركاء عبر تصنيفهم إلى 3 أنماط أساسية: الآمن، القلق، والتجنبي.",
        "sections": [
            ("فخ القلق–التجنبي (The Anxious-Avoidant Trap)", "الدورة الهدامة التي ينجذب فيها الشخص القلق الباحث عن القرب للشخص التجنبي الباحث عن المسافة، مما يشعل صراعاً مزمناً."),
            ("مفارقة الاعتمادية (The Dependency Paradox)", "كلما كان الاعتماد المتبادل آمناً وموثوقاً بين الشريكين، كلما أصبح كل منهما أكثر استقلالاً وشجاعة في العالم الخارجي.")
        ]
    },
    {
        "slug": "wrk-no-bad-parts",
        "title": "لا توجد أجزاء سيئة: شفاء الصدمات واستعادة التكامل عبر أنظمة الأسرة الداخلية",
        "en": "No Bad Parts: Healing Trauma and Restoring Wholeness with the Internal Family Systems Model",
        "dates": "2021 · ريتشارد شوارتز",
        "language": "الإنجليزية",
        "active_start": 2021,
        "active_end": "2021",
        "school": "علاج أنظمة الأسرة الداخلية (IFS)",
        "author_id": "thk-richard-schwartz",
        "author_title": "ريتشارد شوارتز",
        "lede": "دليل علاجي ثوري موجه للجمهور نقل نموذج IFS من العيادات التخصصية إلى الثقافة العامة؛ يؤكد أنه لا توجد أجزاء شريرة داخل النفس، بل أجزاء مجروحة وحامية تبنت أدواراً متطرفة لحماية الإنسان من الألم.",
        "sections": [
            ("الأجزاء الثلاثة والذات الجوهرية (Self)", "المنفيون (Exiles - يحملون ألم الطفولة)، المديرون (Managers - يسيطرون استباقياً لمنع الألم)، رجال الإطفاء (Firefighters - يخدرون الألم بالسلوكيات الاندفاعية والإدمان)، والذات الحكيمة الشافية."),
            ("سمات الذات الثمانية (The 8 Cs)", "الهدوء (Calm)، والفضول (Curiosity)، والوضوح (Clarity)، والرحمة (Compassion)، والثقة (Confidence)، والشجاعة (Courage)، والإبداع (Creativity)، والتواصل (Connectedness).")
        ]
    },
    {
        "slug": "wrk-happiness-trap",
        "title": "فخ السعادة: كيف تتوقف عن الصراع وتبدأ في العيش",
        "en": "The Happiness Trap",
        "dates": "2007 · روس هاريس",
        "language": "الإنجليزية",
        "active_start": 2007,
        "active_end": "2007",
        "school": "العلاج بالقبول والالتزام (ACT)",
        "author_id": "thk-russ-harris",
        "author_title": "روس هاريس",
        "lede": "أحد أكثر كتب العلاج بالقبول والالتزام (ACT) مبيعاً في العالم؛ يوضح أن السعي القهري وراء السعادة وتجنب المشاعر الصعبة هو الفخ الحقيقي الذي يولد الاكتئاب، ويقدم أدوات لفك الاندماج المعرفي والعيش وفق القيم الأصيلة.",
        "sections": [
            ("فك الاندماج المعرفي (Cognitive Defusion)", "النظر إلى الأفكار السلبية كـ 'كلمات عابرة في الذهن' بدلاً من التعامل معها كحقائق ملزمة ومطلقة."),
            ("التقبل والالتزام بالقيم", "إفساح المجال للمشاعر غير المريحة دون خوض حرب معها، والتركيز على اتخاذ أفعال موجهة بالقيم الحياتية الجوهرية.")
        ]
    },
    {
        "slug": "wrk-waking-the-tiger",
        "title": "إيقاظ النمر: شفاء الصدمة",
        "en": "Waking the Tiger: Healing Trauma",
        "dates": "1997 · بيتر ليفين وآن فريدريك",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": "1997",
        "school": "العلاج الجسدي للصدمات (Somatic Experiencing)",
        "author_id": "thk-peter-levine",
        "author_title": "بيتر ليفين",
        "lede": "العمل التأسيسي الذي غيّر علم نفس الصدمات عالمياً؛ يوضح أن الصدمة النفسية تُخزن في الجسد والجهاز العصبي كطاقة بيولوجية محبوسة لم تكتمل دورة تفريغها، مقدماً دليلاً جسدياً لإعادة إطلاق هذه الطاقة والشفاء.",
        "sections": [
            ("ملاحظة الحيوانات في الطبيعة", "كيف تنجو الحيوانات من الصدمات اليومية والافتراس عبر الارتعاش والاهتزاز العضلي التلقائي لتفريغ طاقة الجهاز العصبي الذاتي."),
            ("المعايرة والتأرجح العلاجي (Titration & Pendulation)", "معالجة الصدمة عبر جرعات جسدية دقيقة والانتقال المتدرج بين الشعور بالأمان واستدعاء مشاعر الصدمة لتفريغها بسلام.")
        ]
    },
    {
        "slug": "wrk-polyvagal-theory-therapy",
        "title": "النظرية العصبية المبهمة في العلاج: إشراك إيقاع التنظيم الذاتي",
        "en": "The Polyvagal Theory in Therapy: Engaging the Rhythm of Regulation",
        "dates": "2018 · ديب دانا",
        "language": "الإنجليزية",
        "active_start": 2018,
        "active_end": "2018",
        "school": "العلاج العصبي المبهم وتعديل الصدمات",
        "author_id": "thk-deb-dana",
        "author_title": "ديب دانا",
        "lede": "كتاب رائد جعل النظرية العصبية المبهمة لستيفن بورغيس في متناول المعالجين والجمهور؛ يقدم خريطة عملية لفهم الجهاز العصبي الذاتي بوصفه سلماً يصعد ويهبط فيه الإنسان بين الأمان، والقتال/الهروب، والتجمد والانغلاق.",
        "sections": [
            ("درجات السلم العصبي المبهم الثلاث", "1. المبهم البطني (Ventral Vagal - الأمان والتواصل الاجتماعي). 2. الودي (Sympathetic - التعبئة والقتال/الهروب). 3. المبهم الظهري (Dorsal Vagal - التثبيط والتجمد والانهيار)."),
            ("الإدراك العصبي اللاواعي (Neuroception)", "كيف يستشعر الجهاز العصبي إشارات الخطر والأمان في البيئة دون وعي إدراكي مسبق.")
        ]
    },
    {
        "slug": "wrk-set-boundaries-find-peace",
        "title": "ضع حدوداً، تجد سلاماً: دليل لاستعادة ذاتك",
        "en": "Set Boundaries, Find Peace: A Guide to Reclaiming Yourself",
        "dates": "2021 · نيدرا غلوفر تواب",
        "language": "الإنجليزية",
        "active_start": 2021,
        "active_end": "2021",
        "school": "علم النفس الشعبي والعلاقات الأسرية",
        "author_id": "thk-nedra-tawwab",
        "author_title": "نيدرا غلوفر تواب",
        "lede": "كتاب تصدر قوائم نيويورك تايمز للبِست سيلر لشهور؛ يقدم دليلاً عملياً وصريحاً لوضع حدود واضحة وصحية في كافة مجالات الحياة (الأسرة، العمل، العلاقات العاطفية، والصداقات) دون ذنب.",
        "sections": [
            ("المستويات الثلاثة للحدود", "الحدود الرخوة (Porous - تسبب الاستنزاف)، الحدود الصلبة (Rigid - تسبب العزلة والجفاء)، والحدود الصحية (Healthy - توازن بين الأمان والتواصل)."),
            ("أنواع الحدود الستة", "الحدود الجسدية، الجنسية، الفكرية، العاطفية، المادية، والزمنية.")
        ]
    },
    {
        "slug": "wrk-emotionally-immature-parents",
        "title": "أبناء الآباء غير الناضجين عاطفياً: كيف تشفي جروح طفولتك وتستعيد استقلالك",
        "en": "Adult Children of Emotionally Immature Parents",
        "dates": "2015 · ليندسي جيبسون",
        "language": "الإنجليزية",
        "active_start": 2015,
        "active_end": "2015",
        "school": "علم النفس الإكلينيكي وعلاج الصدمات التطورية",
        "author_id": "thk-lindsay-gibson",
        "author_title": "ليندسي جيبسون",
        "lede": "ظاهرة نشر عالمية بيعت منها ملايين النسخ وتُرجمت لعشرات اللغات؛ تشرح المعاناة الصامتة للأبناء الذين نشأوا مع آباء نرجسيين أو متقلبين أو منغلقين عاطفياً وكيف أثر ذلك على وحدتهم العاطفية في الرشد.",
        "sections": [
            ("الأنماط الأربعة للآباء غير الناضجين", "الوالد الانفعالي (Emotional)، الوالد المندفع/المتسلط (Driven)، الوالد الرافض (Rejecting)، والوالد السلبي المتجاهل (Passive)."),
            ("أسلوب الشفاء عبر الوعي الموضوعي", "التوقف عن محاولة تغيير الوالدين والتحول إلى أسلوب 'التعامل القائم على النضج المعرفي' وحماية الذات العاطفية.")
        ]
    },
    {
        "slug": "wrk-toxic-parents",
        "title": "الآباء السامون: التغلب على إرثهم المؤلم واستعادة حياتك",
        "en": "Toxic Parents: Overcoming Their Hurtful Legacy and Reclaiming Your Life",
        "dates": "1989 · سوزان فوروارد وكريغ باك",
        "language": "الإنجليزية",
        "active_start": 1989,
        "active_end": "1989",
        "school": "علم النفس الشعبي والعلاج الأسري",
        "author_id": "thk-susan-forward",
        "author_title": "سوزان فوروارد",
        "lede": "الكتاب الكلاسيكي الذي صاغ ونشر مصطلح 'الآباء السامين' في الثقافة العالمية وظل متصدراً لقوائم نيويورك تايمز؛ يقدم خريطة لتحديد الإساءات الوالدية (اللفظية، الجسدية، الجنسية، والسيطرة) وكسر دائرة الشعور بالذنب.",
        "sections": [
            ("أصناف الآباء السامين", "الآباء المتحكمون، مدمنو الكحول، المعتدون لفظياً وجسدياً، والآباء غير المؤهلين الذين يحولون أبناءهم لآباء بدلاء (Parentification)."),
            ("المواجهة الشافية واستعادة المسؤولية", "إعادة تعريف المسؤولية والتأكيد على أن الطفل لم يكن سبباً في إساءة والديه.")
        ]
    },
    {
        "slug": "wrk-emotional-blackmail",
        "title": "الابتزاز العاطفي: عندما يستغل المحبون الخوف والالتزام والشعور بالذنب للسيطرة عليك",
        "en": "Emotional Blackmail: When the People in Your Life Use Fear, Obligation, and Guilt to Manipulate You",
        "dates": "1997 · سوزان فوروارد ودونا فريزر",
        "language": "الإنجليزية",
        "active_start": 1997,
        "active_end": "1997",
        "school": "علم النفس الشعبي والعلاقات",
        "author_id": "thk-susan-forward",
        "author_title": "سوزان فوروارد",
        "lede": "كتاب رائد صاغ مصطلح 'الابتزاز العاطفي' وثالوث الضباب (FOG: Fear, Obligation, Guilt)؛ يشرح كيف يتلاعب الشركاء وأفراد الأسرة بالمشاعر لفرض مطالبهم على حساب سلامة الطرف الآخر.",
        "sections": [
            ("ثالوث الضباب FOG والأنماط الأربعة للمبتزين", "المهددون الصريحون (Punishers)، المعاقبون للذات (Self-punishers)، الشهداء الضحايا (Martyrs)، والمغرون بالوعود الكاذبة (Tantalizers)."),
            ("استراتيجية SOS للمواجهة", "التوقف (Stop)، الملاحظة والمراقبة (Observe)، ووضع الاستراتيجية المناسبة (Strategize).")
        ]
    },
    {
        "slug": "wrk-on-death-and-dying",
        "title": "عن الموت والاحتضار: ما يجب أن يتعلمه الأطباء والممرضات ورجال الدين والأسر من المحتضرين",
        "en": "On Death and Dying",
        "dates": "1969 · إليزابيث كوبلر-روس",
        "language": "الإنجليزية",
        "active_start": 1969,
        "active_end": "1969",
        "school": "الطب النفسي وسيكولوجيا الموت والحداد",
        "author_id": "thk-kubler-ross",
        "author_title": "إليزابيث كوبلر-روس",
        "lede": "المرجع العالمي الكلاسيكي الذي كسر حاجز الصمت حول الموت والاحتضار؛ صاغت فيه كوبلر-روس نموذج 'مراحل الحزن الخمس' (DABDA) بعد مقابلات إكلينيكية مطولة مع مئات المرضى الميؤوس من شفائهم.",
        "sections": [
            ("مراحل الحزن الخمس (DABDA)", "1. الإنكار والعزلة (Denial). 2. الغضب (Anger). 3. المساومة (Bargaining). 4. الاكتئاب (Depression). 5. التقبل (Acceptance)."),
            ("الأثر الإنساني والإكلينيكي", "تأسيس معايير الرعاية التلطيفية والتعامل الرحيم مع المشاعر الصادقة للمحتضرين وذويهم.")
        ]
    },
    {
        "slug": "wrk-unwinding-anxiety",
        "title": "تفكيك القلق: تدريب الدماغ لكسر دوائر الخوف والوسواس والشهوة",
        "en": "Unwinding Anxiety: New Science Shows How to Break the Cycles of Worry and Fear to Heal Your Mind",
        "dates": "2021 · جودسون بروير",
        "language": "الإنجليزية",
        "active_start": 2021,
        "active_end": "2021",
        "school": "علم الأعصاب السريري وعلاج الإدمان والقلق",
        "author_id": "thk-judson-brewer",
        "author_title": "جودسون بروير",
        "lede": "كتاب تصدر قوائم نيويورك تايمز؛ يوضح استناداً لتصوير الدماغ بالرنين المغناطيسي أن القلق يعمل كـ 'عادة عصبية' تتغذى على دوائر المكافأة، مقدماً برنامجاً من 3 خطوات مبني على اليقظة الذهنية لتفكيكه.",
        "sections": [
            ("حلقة العادة الثلاثية للقلق", "المحفز (Trigger) -> السلوك وهو القلق والاجترار (Behavior) -> المكافأة المؤقتة وهي وهم السيطرة (Reward)."),
            ("تحديث نظام تقييم المكافأة بالدماغ (BBO)", "استخدام الفضول واليقظة اللطيفة كـ 'عرض أفضل وأكبر' (Bigger Better Offer) يستبدل القلق بالهدوء العصبي.")
        ]
    },
    {
        "slug": "wrk-people-skills",
        "title": "مهارات التعامل مع الناس: كيف تؤكد ذاتك وتستمع للآخرين وتحل النزاعات",
        "en": "People Skills",
        "dates": "1979 · روبرت بولتون",
        "language": "الإنجليزية",
        "active_start": 1979,
        "active_end": "1979",
        "school": "علم النفس الشعبي ومهارات التواصل",
        "author_id": "thk-robert-bolton",
        "author_title": "روبرت بولتون",
        "lede": "دليل كلاسيكي تدريبي شامل بيعت منه ملايين النسخ؛ يفكك مهارات التواصل الإنساني إلى ثلاث مجموعات كبرى: مهارات الاستماع الفعال، مهارات التوكيدية (Assertion)، ومهارات إدارة الصراع.",
        "sections": [
            ("عوائق التواصل الاثنا عشر (Communication Roadblocks)", "الأوامر، التهديد، الوعظ، النقد، السخرية، والتحليل النفسي غير المطلوب."),
            ("رسائل الأنا التوكيدية (Assertion Messages)", "الصيغة الثلاثية للتعبير الحازم غير العدواني: وصف السلوك بموضوعية + تأثيره الملموس + المشاعر الناتجة عنه.")
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
        "slug": "con-nonviolent-communication",
        "title": "التواصل غير العنيف (لغة التعاطف وفض النزاعات NVC)",
        "en": "Nonviolent Communication (NVC)",
        "school": "علم النفس الإنساني والتواصل",
        "active_start": 1999,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-nonviolent-communication", "title": "التواصل غير العنيف", "type": "عمل / كتاب"},
            {"id": "thk-marshall-rosenberg", "title": "مارشال روزنبرغ", "type": "مفكر"}
        ],
        "gaps": [
            "تطبيقات NVC في مناطق النزاعات الدولية والسجون والمدارس.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "منهجية تواصل وإطار سيكولوجي صاغه مارشال روزنبرغ يرتكز على افتراض أن العنف وسوء التفاهم ينبعان من لغة الأحكام واللوم، وأن التواصل البشري يزدهر عند التركيز على الملاحظة، والمشاعر، والاحتياجات الإنسانية المشتركة، والطلبات الإيجابية.",
        "sections": [
            ("المراحل الأربع لـ NVC", "1. الملاحظة الصرفة الخالية من الحكم. 2. التعبير عن المشاعر الصادقة. 3. ربط المشاعر بالاحتياجات الحيوية. 4. صياغة طلبات واضحة وقابلة للتنفيذ."),
            ("الأثر العلاجي والاجتماعي", "تحويل الحوارات المشحونة بالغضب إلى تفاهم عميق وإعادة بناء الروابط الأسرية والمهنية.")
        ]
    },
    {
        "slug": "con-attachment-styles-popular",
        "title": "أنماط التعلق في العلاقات المعاصرة (الآمن، القلق، التجنبي)",
        "en": "Adult Attachment Styles (Popular Concept)",
        "school": "علم النفس الإكلينيكي والعلاقات",
        "active_start": 2010,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-attached", "title": "المتعلقون", "type": "عمل / كتاب"},
            {"id": "thk-amir-levine", "title": "أمير ليفين", "type": "مفكر"}
        ],
        "gaps": [
            "تطور النظرية من بولبي وإينسورث إلى أبحاث هازان وشيفر وليفين على البالغين.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "إطار نفسي وعاطفي واسع الانتشار يفسر كيف يتصرف البالغون في العلاقات العاطفية بناءً على برمجة جهاز التعلق لديهم إلى أربعة أنماط: الآمن (Secure)، القلق المنشغل (Anxious)، التجنبي الرافض (Dismissive-Avoidant)، والخائف التجنبي (Fearful-Avoidant).",
        "sections": [
            ("خصائص الأنماط", "الآمن يشعر بالراحة مع الحميمية والاستقلال؛ القلق يبحث عن التأكيد الدائم ويخشى الهجر؛ والتجنبي يدافع عن استقلاليته بالابتعاد العاطفي."),
            ("التحول نحو التعلق الآمن المكتسب", "إمكانية تعديل نمط التعلق عبر الوعي الذاتي، اختيار شركاء آمنين، وتطوير مهارات التواصل المباشر.")
        ]
    },
    {
        "slug": "con-internal-family-systems-popular",
        "title": "أنظمة الأسرة الداخلية (تعددية النفس والذات الشافية IFS)",
        "en": "Internal Family Systems (IFS Concept)",
        "school": "علاج أنظمة الأسرة الداخلية (IFS)",
        "active_start": 1995,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-no-bad-parts", "title": "لا توجد أجزاء سيئة", "type": "عمل / كتاب"},
            {"id": "thk-richard-schwartz", "title": "ريتشارد شوارتز", "type": "مفكر"}
        ],
        "gaps": [
            "التطبيقات السريرية لـ IFS في علاج اضطراب كرب ما بعد الصدمة المعقد (C-PTSD).",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم ونموذج نفسي يعتبر أن العقل البشري ليس كتلة واحدة، بل نظام بيئي داخلي يتكون من عدة 'أجزاء' (Parts) تمتلك مشاعر ودوافع متباينة، وتديرها 'الذات الحكيمة' (The Self) التي لا يمكن تدميرها.",
        "sections": [
            ("الأدوار الثلاثة للأجزاء", "المنفيون (يحملون الصدمات والخزي)، المديرون (يتحكمون في البيئة استباقياً)، ورجال الإطفاء (يلجأون للإدمان والإلهاء لتخدير الألم الحاد)."),
            ("الشفاء الداخلي (Unburdening)", "مساعدة الذات على الاستماع للأجزاء المتطرفة برحمة وتفريغ أعباء الماضي لتستعيد أدوارها الإبداعية الفطرية.")
        ]
    },
    {
        "slug": "con-polyvagal-theory-popular",
        "title": "السلم العصبي المبهم والتنظيم الذاتي (Polyvagal Ladder)",
        "en": "Polyvagal Theory (Applied Concept)",
        "school": "علم الأعصاب والفيزيولوجيا الحيوية",
        "active_start": 2011,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-polyvagal-theory-therapy", "title": "النظرية العصبية المبهمة في العلاج", "type": "عمل / كتاب"},
            {"id": "thk-stephen-porges", "title": "ستيفن بورغيس", "type": "مفكر"},
            {"id": "thk-deb-dana", "title": "ديب دانا", "type": "مفكر"}
        ],
        "gaps": [
            "تطبيقات النظرية في تمارين التنفس وتنشيط العصب المبهم البطني.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم عصبي تطبيقي يصف كيف يستجيب الجهاز العصبي الذاتي لبيئته عبر 3 حالات فيزيولوجية متدرجة كالسلم: المبهم البطني (الأمان والتواصل الاجتماعي)، الودي (القتال أو الهروب)، والمبهم الظهري (التجمد والتخشب والانهيار).",
        "sections": [
            ("المشاركة الاجتماعية والتنظيم المشترك (Co-regulation)", "أهمية نظرات العين ونبرة الصوت والتنفس المشترك في إرسال إشارات أمان للجهاز العصبي للآخرين."),
            ("تمارين استعادة الأمان", "استخدام الزفير المطول والغناء والحركات اللطيفة لإعادة توجيه الجهاز العصبي نحو قمة السلم.")
        ]
    },
    {
        "slug": "con-boundaries-psychological",
        "title": "الحدود النفسية والعاطفية في العلاقات",
        "en": "Psychological Boundaries",
        "school": "علم النفس الإكلينيكي والعلاقات",
        "active_start": 1990,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-set-boundaries-find-peace", "title": "ضع حدوداً، تجد سلاماً", "type": "عمل / كتاب"},
            {"id": "thk-nedra-tawwab", "title": "نيدرا غلوفر تواب", "type": "مفكر"}
        ],
        "gaps": [
            "التمييز بين الحدود الصحية والانفصال التجنبي العازل.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم نفسي يصف الخطوط الفاصلة غير المرئية التي تحدد هوية الشخص، ومسؤولياته، ومساحته العاطفية والجسدية والزمنية، وما يسمح به وما يرفضه في تعامل الآخرين معه.",
        "sections": [
            ("مؤشرات انهيار الحدود", "الشعور المزمن بالإنهاك والاستياء، الخوف من قول 'لا'، وتحمل مسؤولية مشاعر وسلوكيات الآخرين."),
            ("تطبيق الحدود بالتوكيدية", "وضع الحدود كفعل حب للذات وللعلاقة يحميها من التآكل والغضب المكتوم.")
        ]
    },
    {
        "slug": "con-emotional-blackmail",
        "title": "الابتزاز العاطفي وثالوث الضباب (FOG: الخوف والالتزام والذنب)",
        "en": "Emotional Blackmail (FOG Framework)",
        "school": "علم النفس الشعبي والعلاقات",
        "active_start": 1997,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-emotional-blackmail", "title": "الابتزاز العاطفي", "type": "عمل / كتاب"},
            {"id": "thk-susan-forward", "title": "سوزان فوروارد", "type": "مفكر"}
        ],
        "gaps": [
            "ديناميات الابتزاز العاطفي في العلاقات النرجسية والاعتمادية.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "شكل قوي من أشكال التلاعب في العلاقات القريبة، يستخدم فيه المبتز 'ثالوث الضباب FOG' (الخوف Fear، الالتزام Obligation، والشعور بالذنب Guilt) لإجبار الضحية على الرضوخ لمطالبه على حساب راحتها وقيمها.",
        "sections": [
            ("مراحل الابتزاز الست", "المطلب، المقاومة، الضغط، التهديد، الرضوخ، وتكرار الحلقة كنمط ثابت."),
            ("كسر دائرة الابتزاز", "التدريب على تحمل الانزعاج المؤقت للطرف الآخر والتوقف عن تبرير القرارات الذاتية المشروعة.")
        ]
    },
    {
        "slug": "con-emotional-immaturity-parents",
        "title": "اللاتنضج العاطفي الوالدي والإهمال غير المرئي",
        "en": "Parental Emotional Immaturity",
        "school": "علم النفس الإنمائي والعائلي",
        "active_start": 2015,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-emotionally-immature-parents", "title": "أبناء الآباء غير الناضجين عاطفياً", "type": "عمل / كتاب"},
            {"id": "thk-lindsay-gibson", "title": "ليندسي جيبسون", "type": "مفكر"}
        ],
        "gaps": [
            "الأثر التراكمي للإهمال العاطفي في مرحلة الطفولة المبكرة (CEN).",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مفهوم نفسي إكلينيكي صاغته ليندسي جيبسون، يصف الآباء والأمهات الذين يفتقرون للعمق الانفعالي، والقدرة على التعاطف، وتحمل المسؤولية عن أخطائهم، مما يخلق بيئة أسرية تتمركز حول احتياجات الوالد وتفرض على الأبناء كبت مشاعرهم والتحول إلى 'بالغين مبكرين'.",
        "sections": [
            ("سمات الوالد غير الناضج عاطفياً", "السطحية الانفعالية، سرعة الغضب عند مواجهة الواقع، التمركز حول الذات، والعجز عن تقديم الاحتواء الوجداني الحقيقي."),
            ("تعافي الأبناء", "التخلص من دور المنقذ أو المصلح للوالدين وبناء علاقات متوازنة وناضجة في الرشد.")
        ]
    },
    {
        "slug": "con-five-stages-of-grief",
        "title": "مراحل الحزن الخمس (نموذج كوبلر–روس DABDA)",
        "en": "Five Stages of Grief (Kübler-Ross Model)",
        "school": "الطب النفسي وسيكولوجيا الحداد",
        "active_start": 1969,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-on-death-and-dying", "title": "عن الموت والاحتضار", "type": "عمل / كتاب"},
            {"id": "thk-kubler-ross", "title": "إليزابيث كوبلر-روس", "type": "مفكر"},
            {"id": "dis-prolonged-grief", "title": "اضطراب الحزن المطول", "type": "اضطراب/حالة إكلينيكية"}
        ],
        "gaps": [
            "التأكيد المعاصر على أن المراحل ليست خطية متسلسلة بل أمواجاً وجدانية متداخلة.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "النموذج الأكثر شهرة عالمياً في سيكولوجيا الفقد والحداد؛ يصف 5 استجابات عاطفية يمر بها الإنسان عند مواجهة الموت أو الفقدان الصادم: الإنكار (Denial)، الغضب (Anger)، المساومة (Bargaining)، الاكتئاب (Depression)، والتقبل (Acceptance).",
        "sections": [
            ("المراحل الخمس وطبيعتها الدينامية", "توضح الأبحاث الحديثة أن هذه المراحل لا تحدث بترتيب خطي صارم، بل يتقلب المفجوع بينها كأمواج وجدانية متداخلة."),
            ("إضافة المرحلة السادسة (المعنى)", "أضاف ديفيد كيسلر لاحقاً مرحلة 'إيجاد المعنى' كخطوة تتويجية للتعايش مع الفقد واستمرار الحياة.")
        ]
    },
    {
        "slug": "con-somatic-experiencing-popular",
        "title": "التجربة الجسدية وتفريغ شحنة الصدمة (Somatic Experiencing)",
        "en": "Somatic Experiencing (SE Concept)",
        "school": "العلاج الجسدي للصدمات",
        "active_start": 1997,
        "active_end": "مستمر",
        "related": [
            {"id": "wrk-waking-the-tiger", "title": "إيقاظ النمر", "type": "عمل / كتاب"},
            {"id": "thk-peter-levine", "title": "بيتر ليفين", "type": "مفكر"},
            {"id": "dis-ptsd", "title": "اضطراب الكرب التالي للصدمة", "type": "اضطراب/حالة إكلينيكية"}
        ],
        "gaps": [
            "تطبيقات الاستشعار الجسدي (Felt Sense) في علاج الألم العضلي والصدمات المعقدة.",
            "لا يوجد اقتباس مباشر موثوق متاح."
        ],
        "lede": "مقاربة علاجية ونفسية جسدية رائدة طورها بيتر ليفين لعلاج صدمات ما بعد الكرب (PTSD)؛ تركز على إعادة توجيه الانتباه نحو 'الحس المعاش في الجسد' (Felt Sense) لاستكمال الاستجابات الدفاعية الحركية المعطلة وتفريغ الطاقة العصبية المحبوسة.",
        "sections": [
            ("التفريغ الطبيعي للجهاز العصبي", "السماح للجسد بالارتجاف التلقائي، والتنفس العميق، وتغيير درجة الحرارة كعلامات حيوية على اكتمال دورة تفريغ الصدمة."),
            ("التحول من الحديث العقلي إلى الوعي الجسدي", "تجاوز العلاج بالكلام المجرد والوصول المباشر لمراكز الدماغ الحوفية عبر الإحساس الجسدي.")
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

print("Package 2 generated successfully.")
