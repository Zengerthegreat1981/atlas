# -*- coding: utf-8 -*-
"""
Generate comprehensive Philosophy Branches (br-).
"""
import os

BASE_DIR = "/Users/minamoheb/Desktop/Atlas"

def write_draft(subfolder, slug, frontmatter_dict, body_text):
    out_dir = os.path.join(BASE_DIR, "content", "ar", "drafts", subfolder)
    os.makedirs(out_dir, exist_ok=True)
    lines = ["---"]
    lines.append(f'slug: "{slug}"')
    lines.append('id: "[DRAFT-UNKNOWN]"')
    for k, v in frontmatter_dict.items():
        if k in ["slug", "id"]:
            continue
        if isinstance(v, list):
            if k == "edges":
                lines.append("edges:")
                for edge in v:
                    lines.append(f'  - rel: "{edge.get("rel","belongs_to")}", target: "{edge.get("target","")}", target_type: "{edge.get("target_type","مدرسة")}"')
            elif k == "related":
                lines.append("related:")
                for rel in v:
                    lines.append(f'  - id: "{rel.get("id","")}", title: "{rel.get("title","")}", type: "{rel.get("type","")}"')
            elif k == "gaps":
                lines.append("gaps:")
                for g in v:
                    lines.append(f'  - "{g}"')
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f'  - "{item}"')
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f'{k}: "{v}"')
    lines.append("---")
    lines.append("")
    lines.append(body_text.strip())
    lines.append("")
    
    filepath = os.path.join(out_dir, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"✅ Generated: {subfolder}/{slug}.md")

branches_data = [
    # 1. Classical Hellenistic & Roman
    {
        "slug": "br-stoicism-early",
        "title": "الرواقية القديمة — المدرسة الرواقية",
        "en": "Early Stoicism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الهيلينستية ← الرواقية ← الرواقية القديمة",
        "active_start": -300,
        "active_end": -200,
        "country": "أثينا (اليونان القديمة)",
        "school": "الرواقية (القديمة/الوسطى/الرومانية)",
        "related": [{"id": "thk-zeno-citium", "title": "زينون الرواقي", "type": "مفكر"}],
        "gaps": ["تأسيس الرواق المرسوم (Stoa Poikile) وصياغة الفيزياء والمنطق الرواقي مع خريسيبوس.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المرحلة التأسيسية للمدرسة الرواقية في أثينا على يد زينون الرواقي، وكليانثس، وخريسيبوس؛ ركزت على بناء المنظومة الفلسفية الشاملة المكونة من ثلاثة أجزاء متكاملة: المنطق ونظرية المعرفة، الفيزياء واللوغوس المادي الكوني، والأخلاق القائمة على التوافق مع الطبيعة."
    },
    {
        "slug": "br-stoicism-late-roman",
        "title": "الرواقية الرومانية المتأخرة — المدرسة الرواقية",
        "en": "Late Roman Stoicism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الهيلينستية والرومانية ← الرواقية ← الرواقية الرومانية",
        "active_start": 50,
        "active_end": 180,
        "country": "الإمبراطورية الرومانية",
        "school": "الرواقية (القديمة/الوسطى/الرومانية)",
        "related": [{"id": "thk-epictetus", "title": "إبكتيتوس", "type": "مفكر"}, {"id": "thk-marcus-aurelius", "title": "ماركوس أوريليوس", "type": "مفكر"}, {"id": "thk-seneca", "title": "سينيكا", "type": "مفكر"}],
        "gaps": ["التحول الكامل نحو الأخلاق التطبيقية والتدريبات النفسية والروحية اليومية في مواجهة تقلبات الإمبراطورية.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المرحلة الأكثر نضجاً وتأثيراً في تاريخ الرواقية؛ تحولت فيها الفلسفة من التنظير المنطقي والفيزيائي إلى 'طب عملي للنفس' والإرشاد السلوكي الأخلاقي مع سينيكا وإبكتيتوس وماركوس أوريليوس، وهي المرحلة التي استلهم منها العلاج المعرفي السلوكي الحديث مبادئه الأساسية."
    },
    {
        "slug": "br-neoplatonism-roman",
        "title": "الأفلاطونية المحدثة الرومانية — الأفلاطونية المحدثة",
        "en": "Roman Neo-Platonism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الرومانية ← الأفلاطونية المحدثة ← الأفلاطونية المحدثة الرومانية",
        "active_start": 244,
        "active_end": 305,
        "country": "روما",
        "school": "الأفلاطونية المحدثة (النيوأفلاطونية)",
        "related": [{"id": "thk-plotinus", "title": "أفلوطين", "type": "مفكر"}, {"id": "thk-porphyry", "title": "فرفوريوس", "type": "مفكر"}],
        "gaps": ["صياغة التاسوعات ونظرية الفيض الثلاثي (الواحد، العقل، النفس).", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "التيار التأسيسي للأفلاطونية المحدثة الذي أطلقه أفلوطين ودونه فرفوريوس في روما؛ تميز بالنزعة العقلية التأملية الصارمة والصعود الصوفي نحو الواحد عبر التجريد والتأمل دون اللجوء إلى طقوس الثيورجيا السحرية."
    },
    # 2. Islamic Kalam & Falsafa
    {
        "slug": "br-mutazila-basra",
        "title": "مدرسة البصرة الكلامية — المعتزلة",
        "en": "Basra School of Mu'tazilism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "علم الكلام الإسلامي ← المعتزلة ← مدرسة البصرة",
        "active_start": 725,
        "active_end": 1050,
        "country": "العراق (البصرة)",
        "school": "المعتزلة",
        "related": [{"id": "thk-wasil-ibn-ata", "title": "واصل بن عطاء", "type": "مفكر"}, {"id": "thk-qadi-abd-al-jabbar", "title": "القاضي عبد الجبار", "type": "مفكر"}],
        "gaps": ["نظرية الجوهر الفرد ونفي الجزء الذي لا يتجزأ عند النظام وتأسيس الأصول الخمسة.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المدرسة الأم والأكثر أصالة في الفكر الاعتزالي؛ تميزت بالصرامة المنطقية واللغوية والتحليل الدقيق للأصول الخمسة، وخرج منها كبار المنظرين كواصل، وعمرو بن عبيد، وأبي الهذيل العلاف، والنظام، وأبي علي الجبائي، وأبي هاشم الجبائي (البهشمية)."
    },
    {
        "slug": "br-mutazila-baghdad",
        "title": "مدرسة بغداد الكلامية — المعتزلة",
        "en": "Baghdad School of Mu'tazilism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "علم الكلام الإسلامي ← المعتزلة ← مدرسة بغداد",
        "active_start": 800,
        "active_end": 950,
        "country": "الدولة العباسية (بغداد)",
        "school": "المعتزلة",
        "related": [{"id": "sch-mutazilism", "title": "المعتزلة", "type": "مدرسة"}],
        "gaps": ["تأثير بشر بن المعتمر ونظرية التوليد وميل مدرسة بغداد إلى تفضيل الإمام علي في الإمامة.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "الفرع البغدادي للمعتزلة الذي أسسه بشر بن المعتمر؛ تميز بالانخراط السياسي في البلاط العباسي والتقارب مع بعض الرؤى الإمامية والزيدية في مسألة الإمامة، وتطوير نظرية 'التوليد' في الأفعال الطبيعية والإنسانية."
    },
    {
        "slug": "br-asharism-late-philosophical",
        "title": "الأشعرية المتأخرة الفلسفية — الأشعرية",
        "en": "Late Philosophical Ash'arism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "علم الكلام الإسلامي ← الأشعرية ← الأشعرية المتأخرة الفلسفية",
        "active_start": 1085,
        "active_end": 1500,
        "country": "العالم الإسلامي",
        "school": "الأشعرية",
        "related": [{"id": "thk-al-ghazali", "title": "أبو حامد الغزالي", "type": "مفكر"}, {"id": "sch-asharism", "title": "الأشعرية", "type": "مدرسة"}],
        "gaps": ["مزج علم الكلام بالمنطق الأرسطي والميتافيزيقا السيناوية مع الغزالي وفخر الدين الرازي والآمدي والإيجي.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المرحلة الناضجة لعلم الكلام الأشعري التي بدأت مع إمام الحرمين الجويني وأبي حامد الغزالي وبلغت ذروتها مع فخر الدين الرازي وسعد الدين التفتازاني؛ تميزت بإدماج كامل للمنطق الصوري الأرسطي والمباحث الوجودية للفلسفة المشائية في صلب كتب العقائد (المواقف والمقاصد)."
    },
    {
        "slug": "br-falsafa-mashshaiyya-western-andalusian",
        "title": "المشائية الأندلسية والمغربية — الفلسفة المشائية الإسلامية",
        "en": "Andalusian Peripatetic Philosophy",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الإسلامية ← الفلسفة الأندلسية ← المشائية الأندلسية",
        "active_start": 1100,
        "active_end": 1200,
        "country": "الأندلس والمغرب",
        "school": "الفلسفة المشائية الإسلامية (كمظلة عامة)",
        "related": [{"id": "thk-ibn-rushd", "title": "ابن رشد", "type": "مفكر"}, {"id": "thk-ibn-tufayl", "title": "ابن طفيل", "type": "مفكر"}],
        "gaps": ["تطهير أرسطو من تأويلات ابن سينا والفيضية النيوأفلاطونية والعودة إلى المشائية الخالصة.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المدرسة الفلسفية العقلانية التي ازدهرت في الأندلس والمغرب مع ابن باجة وابن طفيل وابن رشد؛ تميزت بالنزعة البرهانية النقدية الصارمة، ورفض الخلط بين الفلسفة والتصوف، والدفاع عن العلية الطبيعية ومطابقة البرهان العقلي للوحي الشرعي."
    },
    # 3. Indic & Buddhist Branches
    {
        "slug": "br-advaita-vedanta-classical",
        "title": "الأدفايتا فيدانتا الكلاسيكية — الفيدانتا",
        "en": "Classical Advaita Vedanta",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الهندية ← الفيدانتا ← أدفايتا فيدانتا",
        "active_start": 750,
        "active_end": 1300,
        "country": "الهند",
        "school": "أدفايتا فيدانتا",
        "related": [{"id": "thk-shankara", "title": "شانكارا", "type": "مفكر"}, {"id": "con-atman-brahman-vedanta", "title": "الأتمان والبراهمان", "type": "مفهوم"}],
        "gaps": ["مدرستا الشرح بعد شانكارا: مدرسة بهاماتي (Vachaspati Mishra) ومدرسة فيفارانا (Prakashatman).", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "التيار الفلسفي اللا-اثناني الأكبر في الهند؛ يؤكد على الوحدة المطلقة للوعي (البراهمان) وزيف التعدد والانفصال الحسي الناشئ عن المايا والجهل المركب (Avidya)."
    },
    {
        "slug": "br-zen-soto-classical",
        "title": "زن سوتو الكلاسيكي — البوذية اليابانية",
        "en": "Classical Soto Zen",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة البوذية ← زن ← زن سوتو",
        "active_start": 1227,
        "active_end": 1700,
        "country": "اليابان",
        "school": "زن: سوتو",
        "related": [{"id": "thk-dogen", "title": "دوغن", "type": "مفكر"}],
        "gaps": ["ممارسة الشيكانتازا (فقط الجلوس) ونفي الغائية النفعية من التأمل في نصوص إيهي دوغن.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "المدرسة البوذية التأملية التي أسسها دوغن في معبد إيهيجي؛ تركز على التأمل الصامت الهادئ دون استخدام ألغاز الكوان، وتعتبر أن الطبيعة الأصلية للبوذا متحققة في كل لحظة وفي كل كائن حي."
    },
    # 4. Modern European Branches
    {
        "slug": "br-british-empiricism-classical",
        "title": "التجريبية البريطانية الكلاسيكية — التجريبية",
        "en": "Classical British Empiricism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الحديثة ← التجريبية البريطانية ← التجريبية الكلاسيكية",
        "active_start": 1690,
        "active_end": 1776,
        "country": "المملكة المتحدة",
        "school": "التجريبية البريطانية (كمظلة)",
        "related": [{"id": "thk-locke", "title": "جون لوك", "type": "مفكر"}, {"id": "thk-hume", "title": "ديفيد هيوم", "type": "مفكر"}],
        "gaps": ["الثالوث التجريبي (لوك، بيركلي، هيوم) وتدرج الشك من نفي الأفكار الفطرية إلى الشك في المادة ثم الشك في السببية والذات.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "التيار الفلسفي المؤسس لنظرية المعرفة الحديثة في بريطانيا؛ أرسى أولوية الحواس والتجربة المعاشة في تشكيل الفكر، وألهم الثورة العلمية ونشأة العلوم الإنسانية وعلم النفس التجريبي والسلوكي."
    },
    {
        "slug": "br-german-idealism-hegelian",
        "title": "المثالية الهيغلية المطلقة — المثالية الألمانية",
        "en": "Hegelian Absolute Idealism",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة الألمانية ← المثالية الألمانية ← المثالية الهيغلية المطلقة",
        "active_start": 1807,
        "active_end": 1840,
        "country": "ألمانيا",
        "school": "الهيغلية",
        "related": [{"id": "thk-hegel", "title": "هيغل", "type": "مفكر"}, {"id": "con-master-slave-dialectic-hegel", "title": "جدلية السيد والعبد", "type": "مفهوم"}],
        "gaps": ["انقسام المدرسة بعد وفاة هيغل إلى الهيغلية اليمينية المحافظة والهيغلية اليسارية الثورية.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "ذروة النسق المثالي الديالكتيكي في أوروبا؛ يرى أن الواقع كله تجسيد وصيرورة تاريخية للعقل والروح المطلق (Geist)، مفسراً الفن، والدين، والفلسفة، والدولة كحلقات ارتقاء للحرية والوعي الإنساني."
    },
    {
        "slug": "br-logical-positivism-vienna-circle",
        "title": "الوضعية المنطقية وحلقة فيينا — الفلسفة التحليلية",
        "en": "Logical Positivism (Vienna Circle)",
        "part": "philosophy",
        "level": "متقدم",
        "crumb": "الفلسفة التحليلية ← الوضعية المنطقية ← حلقة فيينا",
        "active_start": 1922,
        "active_end": 1938,
        "country": "النمسا وألمانيا",
        "school": "الوضعية المنطقية (حلقة فيينا)",
        "related": [{"id": "thk-ludwig-wittgenstein", "title": "فيتغنشتاين", "type": "مفكر"}, {"id": "thk-karl-popper", "title": "كارل بوبر", "type": "مفكر"}],
        "gaps": ["مبدأ التحقق التجريبي (Verificationism) وحل حلقة فيينا عقب ضم النمسا 1938 وهجرة أعضائها إلى أمريكا.", "لا يوجد اقتباس مباشر موثوق متاح."],
        "lede": "الحركة الفلسفية والمنطقية الجذرية التي قادها موريتز شليك ورودولف كارناب في فيينا؛ سعت إلى توحيد العلوم ونفي كل القضايا الميتافيزيقية واللاهوتية واعتبارها 'عديمة المعنى إبستمولوجياً' لأنها غير قابلة للتحقق الحسي التجريبي."
    }
]

for item in branches_data:
    write_draft("branches", item["slug"], {
        "type": "تيار",
        "part": item["part"],
        "level": item["level"],
        "title": item["title"],
        "en": item["en"],
        "crumb": item["crumb"],
        "country": item["country"],
        "active_start": item["active_start"],
        "active_end": item["active_end"],
        "edges": [{"rel": "belongs_to", "target": item["school"], "target_type": "مدرسة"}],
        "related": item["related"],
        "gaps": item["gaps"]
    }, f"""# {item["title"]}

{item["lede"]}

## المعالم والخصائص الفكرية

يمثل هذا التيار محطة فارقة وتطوراً بنيوياً داخل المدرسة الأم، أسهم في صياغة مفاهيمها وأدواتها التحليلية وتطبيقاتها المعرفية.

## الأثر والامتداد التاريخي

ترك هذا التيار بصمات عميقة في تطور الفلسفة والعلوم الإنسانية والمدارس الفكرية المعاصرة.

## اقتباسات مختارة

لا يوجد اقتباس مباشر موثوق متاح.""")

print("Generated Philosophy Branches Successfully!")
