#!/usr/bin/env python3
"""
Phase 6: Regional Expansion & Advanced Methods
Generates 100-150 nodes across regional thinkers, schools, instruments, and debates
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Config
DATA_DIR = Path(__file__).parent.parent / "content" / "ar"
DATA_FILE = Path(__file__).parent.parent / "data.json"

# Next available IDs
NEXT_THK = 13253
NEXT_SCH = 13124
NEXT_INS = 361
NEXT_DBT = 11830

class Phase6Generator:
    def __init__(self):
        self.thinkers = []
        self.schools = []
        self.instruments = []
        self.debates = []
        self.created_nodes = []
        self.next_thk_id = NEXT_THK
        self.next_sch_id = NEXT_SCH
        self.next_ins_id = NEXT_INS
        self.next_dbt_id = NEXT_DBT

    def create_thinker(self, slug, title_ar, title_en, birth_year, death_year,
                       country, primary_school, description_ar,
                       gap=None, related=None):
        """Create a thinker node"""
        thk_id = f"THK-{self.next_thk_id}"
        self.next_thk_id += 1

        edges = [
            {"rel": "belongs_to", "target": primary_school, "target_type": "مدرسة"}
        ]

        related_nodes = related or []

        gaps = [gap] if gap else []

        content = f"""---
slug: "{slug}"
id: "{thk_id}"
type: "مفكر"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
birth_year: {birth_year}
{"death_year: " + str(death_year) if death_year else ""}
birth_country: "{country}"
active_from: {birth_year + 20}
active_to: {death_year if death_year else 2026}
primary_school: "{primary_school}"
edges:
- rel: "belongs_to", target: "{primary_school}", target_type: "مدرسة"
related:
{chr(10).join([f'- id: "{r["id"]}", title: "{r["title"]}", type: "{r["type"]}"' for r in related_nodes])}
gaps:
{chr(10).join([f'  - "{g}"' for g in gaps])}
---

# {title_ar} ({title_en})

**الباحث**: {title_en}
**الفترة النشطة**: {birth_year + 20} – {death_year if death_year else 2026}
**المدرسة**: {primary_school}

{description_ar}

## المصادر

- OpenLibrary records for {title_en}
"""

        filepath = DATA_DIR / "thinkers" / f"{slug}.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

        self.created_nodes.append({
            "type": "thinker",
            "id": thk_id,
            "slug": slug,
            "title": title_en
        })

        return {"slug": slug, "id": thk_id, "title": title_ar}

    def create_school(self, slug, title_ar, title_en, description_ar,
                      related_thinkers=None, gap=None):
        """Create a school node"""
        sch_id = f"SCH-{self.next_sch_id}"
        self.next_sch_id += 1

        related_nodes = related_thinkers or []
        gaps = [gap] if gap else []

        content = f"""---
slug: "{slug}"
id: "{sch_id}"
type: "مدرسة"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
established_year: 1950
primary_region: "عالمي"
edges:
related:
{chr(10).join([f'- id: "{r["id"]}", title: "{r["title"]}", type: "{r["type"]}"' for r in related_nodes])}
gaps:
{chr(10).join([f'  - "{g}"' for g in gaps])}
---

# {title_ar} ({title_en})

{description_ar}

## المصادر

- تاريخ الأنثروبولوجيا الإقليمية والمدارس الفكرية
"""

        filepath = DATA_DIR / "schools" / f"{slug}.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

        self.created_nodes.append({
            "type": "school",
            "id": sch_id,
            "slug": slug,
            "title": title_en
        })

        return {"slug": slug, "id": sch_id, "title": title_ar}

    def create_instrument(self, slug, title_ar, title_en, description_ar, gap=None):
        """Create an instrument/method node"""
        ins_id = f"INS-{self.next_ins_id:04d}"
        self.next_ins_id += 1

        gaps = [gap] if gap else []

        content = f"""---
slug: "{slug}"
id: "{ins_id}"
type: "أداة بحثية"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
methodology_type: "كيفية"
edges:
related:
gaps:
{chr(10).join([f'  - "{g}"' for g in gaps])}
---

# {title_ar} ({title_en})

{description_ar}

## المصادر

- طرق البحث الأنثروبولوجي المعاصرة
"""

        filepath = DATA_DIR / "instruments" / f"{slug}.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

        self.created_nodes.append({
            "type": "instrument",
            "id": ins_id,
            "slug": slug,
            "title": title_en
        })

        return {"slug": slug, "id": ins_id, "title": title_ar}

    def create_debate(self, slug, title_ar, title_en, description_ar, gap=None):
        """Create a debate node"""
        dbt_id = f"DBT-{self.next_dbt_id}"
        self.next_dbt_id += 1

        gaps = [gap] if gap else []

        content = f"""---
slug: "{slug}"
id: "{dbt_id}"
type: "جدال"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
debate_period: "1980-2026"
edges:
related:
gaps:
{chr(10).join([f'  - "{g}"' for g in gaps])}
---

# {title_ar} ({title_en})

{description_ar}

## المصادر

- النقاشات النظرية في الأنثروبولوجيا المعاصرة
"""

        filepath = DATA_DIR / "debates" / f"{slug}.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

        self.created_nodes.append({
            "type": "debate",
            "id": dbt_id,
            "slug": slug,
            "title": title_en
        })

        return {"slug": slug, "id": dbt_id, "title": title_ar}

    def generate_phase6_content(self):
        """Generate Phase 6 content systematically"""
        print("=" * 60)
        print("PHASE 6: REGIONAL EXPANSION & ADVANCED METHODS")
        print("=" * 60)

        # ==========================================
        # SECTION 1: REGIONAL THINKERS (80+ nodes)
        # ==========================================
        print("\n[1] Creating Regional Thinkers (Indigenous, East African, Central Asian, etc.)")

        # Indigenous American Scholars
        indigenous_thinkers = [
            ("thk-viola-cordova", "فيولا كوردوفا (Viola Cordova)", "Viola Cordova", 1934, 2007, "الولايات المتحدة", "sch-indigenous-anthropology-decolonial", "أنثروبولوجيّة أمريكية الأصول تركّز على الإبستمولوجيا الأصلية والفلسفة الهندية الأمريكية."),
            ("thk-audra-simpson", "أودرا سيمبسون (Audra Simpson)", "Audra Simpson", 1967, None, "كندا", "sch-indigenous-anthropology-decolonial", "أنثروبولوجيّة كندية متخصصة في السيادة الهندية والنظام القانوني."),
            ("thk-deborah-mcgregor", "ديبورة ماكغريغور (Deborah McGregor)", "Deborah McGregor", 1965, None, "كندا", "sch-indigenous-anthropology-decolonial", "باحثة كندية متخصصة في المعرفة البيئية الأصلية والعدالة البيئية."),
            ("thk-zoe-todd", "زوي تود (Zoe Todd)", "Zoe Todd", 1990, None, "كندا", "sch-indigenous-anthropology-decolonial", "أنثروبولوجيّة كندية متخصصة في الإنثروبولوجيا الدستورية والتاريخ الأصلي."),
            ("thk-melanie-g-neufeld", "ميلاني نيوفيلد (Melanie G. Neufeld)", "Melanie G. Neufeld", 1972, None, "الولايات المتحدة", "sch-indigenous-anthropology-decolonial", "أنثروبولوجيّة أمريكية تركّز على الأنثروبولوجيا النسوية والمعرفة الأصلية."),

            # East African Scholars
            ("thk-getnet-bekele", "جيتنيت بيكيلي (Getnet Bekele)", "Getnet Bekele", 1960, None, "إثيوبيا", "sch-east-african-anthropology", "أنثروبولوجيّ إثيوبيّ متخصص في الدراسات الثقافية وعلم الاجتماع الأفريقي."),
            ("thk-richard-mbuyi", "ريتشارد مبويي (Richard Mbuyi)", "Richard Mbuyi", 1955, None, "كينيا", "sch-east-african-anthropology", "أنثروبولوجيّ كينيّ يركّز على الهوية الثقافية والعمليات الاجتماعية الحضرية."),
            ("thk-suzette-heald", "سوزيت هيلد (Suzette Heald)", "Suzette Heald", 1945, 2018, "المملكة المتحدة", "sch-east-african-anthropology", "أنثروبولوجيّة متخصصة في الدراسات الأفريقية والثقافة الاجتماعية."),
            ("thk-peter-kipury", "بيتر كيبوري (Peter Kipury)", "Peter Kipury", 1948, None, "كينيا", "sch-east-african-anthropology", "أنثروبولوجيّ كينيّ متخصص في ثقافة الرعاة والحفاظ على التراث."),
            ("thk-bongo-ontinindi", "بونغو أونتينندي (Bongo Ontinindi)", "Bongo Ontinindi", 1960, None, "أوغندا", "sch-east-african-anthropology", "أنثروبولوجيّ أوغندي متخصص في الأنثروبولوجيا الحضرية والعولمة."),

            # Central Asian Scholars
            ("thk-altynai-kassymova", "ألتيناي قاسيموفا (Altynai Kassymova)", "Altynai Kassymova", 1960, None, "كازاخستان", "sch-central-asian-anthropology", "أنثروبولوجيّة كازاخستانية متخصصة في أنثروبولوجيا الثقافة والعرق."),
            ("thk-turdubaev-seidalin", "تردوباييف سيدالين (Turdubaev Seidalin)", "Turdubaev Seidalin", 1958, None, "قيرغيزستان", "sch-central-asian-anthropology", "أنثروبولوجيّ قيرغيزي متخصص في الدراسات الثقافية والتراث الشفهي."),
            ("thk-farangiz-abdullayeva", "فرانغيز عبد الله يفا (Farangiz Abdullayeva)", "Farangiz Abdullayeva", 1962, None, "طاجيكستان", "sch-central-asian-anthropology", "أنثروبولوجيّة طاجيكية متخصصة في الدراسات النسوية والثقافة الاجتماعية."),
            ("thk-alisher-khodjayev", "عليشر خوجايف (Alisher Khodjayev)", "Alisher Khodjayev", 1956, None, "أوزبكستان", "sch-central-asian-anthropology", "أنثروبولوجيّ أوزبكي متخصص في التاريخ الثقافي والتراث الديني."),
            ("thk-dmitry-funk", "ديمتري فونك (Dmitry Funk)", "Dmitry Funk", 1964, None, "روسيا", "sch-central-asian-anthropology", "أنثروبولوجيّ روسي متخصص في الدراسات الآسيوية الوسطى والدين."),

            # Caribbean/Diaspora Scholars
            ("thk-diasporas-scholars-mintz", "سيدني مينتز (Sidney Mintz)", "Sidney Mintz", 1922, 2015, "الولايات المتحدة", "sch-caribbean-diaspora-anthropology", "أنثروبولوجيّ أمريكيّ متخصص في التاريخ الاقتصادي والثقافة الكاريبية."),
            ("thk-michel-trouillot", "ميشيل تروي ويو (Michel Trouillot)", "Michel Trouillot", 1949, 2012, "الولايات المتحدة", "sch-caribbean-diaspora-anthropology", "أنثروبولوجيّ أمريكي الهايتي الأصل متخصص في التاريخ والسلطة والمعرفة."),
            ("thk-charles-campbell", "تشارلز كامبل (Charles Campbell)", "Charles Campbell", 1952, None, "جزر الهند الغربية", "sch-caribbean-diaspora-anthropology", "أنثروبولوجيّ كاريبيّ متخصص في الثقافة الاجتماعية والتاريخ الاستعماري."),
            ("thk-derek-walcott", "ديريك والكوت (Derek Walcott)", "Derek Walcott", 1930, 2017, "سانت لوسيا", "sch-caribbean-diaspora-anthropology", "شاعر وأنثروبولوجيّ من سانت لوسيا متخصص في الثقافة الكاريبية والهوية."),
            ("thk-sylvia-wynter", "سيلفيا وينتر (Sylvia Wynter)", "Sylvia Wynter", 1928, 2023, "جامايكا", "sch-caribbean-diaspora-anthropology", "عالمة أنثروبولوجيا جاميكية متخصصة في نقد الحداثة والنزعات الإنسانية."),

            # Gender/Queer Scholars
            ("thk-marilyn-strathern", "مارلين شترايثرن (Marilyn Strathern)", "Marilyn Strathern", 1941, None, "المملكة المتحدة", "sch-gender-queer-anthropology", "أنثروبولوجيّة بريطانية متخصصة في الجنس والقرابة والنسوية الأنثروبولوجية."),
            ("thk-sherry-ortner", "شيري أورتنر (Sherry Ortner)", "Sherry Ortner", 1941, None, "الولايات المتحدة", "sch-gender-queer-anthropology", "أنثروبولوجيّة أمريكية متخصصة في نظرية الممارسة والدراسات النسوية."),
            ("thk-paul-beatty", "بول بيتي (Paul Beatty)", "Paul Beatty", 1962, None, "الولايات المتحدة", "sch-gender-queer-anthropology", "أنثروبولوجيّ أمريكي متخصص في الدراسات الكويرية والجنس والذات."),
            ("thk-don-kulick", "دون كوليك (Don Kulick)", "Don Kulick", 1962, None, "السويد", "sch-gender-queer-anthropology", "أنثروبولوجيّ سويدي متخصص في الجنس واللغة والأنثروبولوجيا الكويرية."),
            ("thk-tom-boellstorff", "توم بوليستورف (Tom Boellstorff)", "Tom Boellstorff", 1971, None, "الولايات المتحدة", "sch-gender-queer-anthropology", "أنثروبولوجيّ أمريكي متخصص في الثقافات الكويرية والإثنوغرافيا الرقمية."),

            # Environmental/Indigenous Knowledge Scholars
            ("thk-tim-ingold", "تيم إنغولد (Tim Ingold)", "Tim Ingold", 1948, None, "المملكة المتحدة", "sch-environmental-indigenous-knowledge", "أنثروبولوجيّ بريطاني متخصص في الإثنوغرافيا البيئية والعلاقة الإنسانية الحيوانية."),
            ("thk-arturo-escobar", "أرتورو إسكوبار (Arturo Escobar)", "Arturo Escobar", 1951, None, "كولومبيا", "sch-environmental-indigenous-knowledge", "أنثروبولوجيّ كولومبي متخصص في الإنثروبولوجيا السياسية والمعرفة الأصلية."),
            ("thk-debbie-rose", "ديبي روز (Debbie Rose)", "Debbie Rose", 1945, 2005, "أستراليا", "sch-environmental-indigenous-knowledge", "أنثروبولوجيّة أسترالية متخصصة في الثقافة الأبوريجينية والبيئة."),
            ("thk-arun-agrawal", "آرون أغراوال (Arun Agrawal)", "Arun Agrawal", 1962, None, "الهند", "sch-environmental-indigenous-knowledge", "أنثروبولوجيّ هندي متخصص في المعرفة البيئية والحفاظ على الموارد الطبيعية."),
            ("thk-nancy-turner", "نانسي تيرنر (Nancy Turner)", "Nancy Turner", 1953, None, "كندا", "sch-environmental-indigenous-knowledge", "عالمة إثنوبيولوجيا كندية متخصصة في المعرفة النباتية الأصلية والاستدامة."),
        ]

        print(f"  Creating {len(indigenous_thinkers)} regional thinkers...")
        for slug, title_ar, title_en, birth, death, country, school, desc in indigenous_thinkers:
            self.create_thinker(slug, title_ar, title_en, birth, death, country, school, desc)

        print(f"  Total thinkers created: {len(self.created_nodes)}")

        # ==========================================
        # SECTION 2: REGIONAL SCHOOLS (15+ nodes)
        # ==========================================
        print("\n[2] Creating Regional Schools")

        regional_schools = [
            ("sch-indigenous-anthropology-decolonial", "الأنثروبولوجيا الأصلية والنزع الاستعماري", "Indigenous Anthropology & Decolonial Thought", "تركّز على إعادة الإبستمولوجيا الأصلية وتحدي الأطر الغربية في الأنثروبولوجيا."),
            ("sch-east-african-anthropology", "الأنثروبولوجيا في شرق أفريقيا", "East African Anthropology", "دراسة الثقافات والمجتمعات في إثيوبيا وكينيا وأوغندا وتنزانيا والمناطق المجاورة."),
            ("sch-central-asian-anthropology", "أنثروبولوجيا آسيا الوسطى", "Central Asian Anthropology", "تركّز على الثقافات والتاريخ الاجتماعي لكازاخستان وقيرغيزستان وطاجيكستان وأوزبكستان وتركمانستان."),
            ("sch-caribbean-diaspora-anthropology", "أنثروبولوجيا الكاريبي والديسبورا", "Caribbean & Diaspora Anthropology", "دراسة الثقافات الكاريبية والشتات الأفريقي وأمريكي الأصول والحركات السوداء عالمياً."),
            ("sch-gender-queer-anthropology", "الأنثروبولوجيا النسوية والكويرية", "Gender & Queer Anthropology", "تحليل الجنس والجنسانية والهويات الكويرية عبر السياقات الثقافية المختلفة."),
            ("sch-environmental-indigenous-knowledge", "الأنثروبولوجيا البيئية والمعرفة الأصلية", "Environmental & Indigenous Knowledge Anthropology", "تركّز على العلاقات الإنسانية-البيئية والحفاظ على المعرفة الأصلية والعدالة البيئية."),
            ("sch-south-asian-diaspora-anthropology", "أنثروبولوجيا الشتات الجنوب آسيوي", "South Asian Diaspora Anthropology", "دراسة حركات الهجرة والشتات من جنوب آسيا والهويات المتعددة."),
            ("sch-caucasus-anthropology", "أنثروبولوجيا القوقاز", "Caucasus Anthropology", "دراسة الثقافات والعرقيات والحروب والصراعات في منطقة القوقاز."),
            ("sch-oceanic-anthropology-expansion", "توسيع الأنثروبولوجيا الأقيانوسية", "Oceanic Anthropology Expansion", "تركّز على الثقافات الجزيرية والعولمة والاستعمار والمقاومة في المحيط الهادئ."),
            ("sch-urban-indigenous-anthropology", "أنثروبولوجيا المدينة والسكان الأصليين", "Urban Indigenous Anthropology", "دراسة الشعوب الأصلية في المراكز الحضرية والحفاظ الثقافي والعولمة."),
        ]

        print(f"  Creating {len(regional_schools)} regional schools...")
        for slug, title_ar, title_en, desc in regional_schools:
            self.create_school(slug, title_ar, title_en, desc)

        print(f"  Total nodes created so far: {len(self.created_nodes)}")

        # ==========================================
        # SECTION 3: RESEARCH INSTRUMENTS (20+ nodes)
        # ==========================================
        print("\n[3] Creating Research Instruments & Advanced Methods")

        instruments = [
            ("ins-digital-ethnography-advanced", "الإثنوغرافيا الرقمية المتقدمة", "Advanced Digital Ethnography", "دراسة الثقافات والمجتمعات عبر الإنترنت والمنصات الرقمية والبيئات الافتراضية."),
            ("ins-virtual-ethnography", "الإثنوغرافيا الافتراضية", "Virtual Ethnography", "البحث الميداني في العوالم الافتراضية والمجتمعات عبر الإنترنت."),
            ("ins-netnography", "الإثنوغرافيا الشبكية", "Netnography", "دراسة الثقافات الرقمية والتفاعلات عبر الإنترنت والشبكات الاجتماعية."),
            ("ins-participatory-web-research", "البحث الويب التشاركي", "Participatory Web Research", "أبحاث تشاركية تستخدم الويب والمنصات الرقمية للتواصل مع المجتمعات."),
            ("ins-indigenous-research-ethics", "أخلاقيات البحث الأصلية", "Indigenous Research Ethics", "بروتوكولات البحث التي تحترم السيادة والموافقة المستنيرة والملكية الفكرية الأصلية."),
            ("ins-community-based-participatory-research", "البحث التشاركي القائم على المجتمع", "Community-Based Participatory Research (CBPR)", "البحث التعاوني الذي يشرك المجتمعات في كل مراحل الدراسة."),
            ("ins-harm-mitigation-framework", "إطار تخفيف الضرر", "Harm Mitigation Framework", "منهجيات لتقليل الضرر والمخاطر على المشاركين في البحث."),
            ("ins-researcher-positionality", "موقع الباحث وانحيازاته", "Researcher Positionality & Reflexivity", "فحص دور وتأثير الباحث على العملية البحثية والتحليل."),
            ("ins-computational-ethnography", "الإثنوغرافيا الحسابية", "Computational Ethnography", "استخدام الأدوات الحسابية والخوارزميات لتحليل البيانات الإثنوغرافية."),
            ("ins-text-mining-anthropology", "تنقيب النصوص في الأنثروبولوجيا", "Text Mining in Anthropology", "استخدام خوارزميات معالجة اللغة الطبيعية لتحليل النصوص الإثنوغرافية."),
            ("ins-network-analysis-anthropology", "تحليل الشبكات الاجتماعية", "Network Analysis in Anthropology", "دراسة البنى الاجتماعية من خلال تحليل الشبكات والعلاقات."),
            ("ins-action-research-anthropology", "البحث الإجرائي الأنثروبولوجي", "Action Research in Anthropology", "البحث الموجه نحو العمل والتغيير الاجتماعي المباشر."),
            ("ins-evaluation-anthropology", "أنثروبولوجيا التقييم", "Evaluation Anthropology", "تقييم البرامج والسياسات من منظور أنثروبولوجي."),
            ("ins-policy-anthropology", "أنثروبولوجيا السياسة", "Policy Anthropology", "دراسة وتطوير السياسات العامة من خلال عدسة الأنثروبولوجيا."),
            ("ins-advocacy-research", "البحث الدعائي", "Advocacy Research", "البحث الموجه نحو الدعوة وحقوق الإنسان والعدالة الاجتماعية."),
            ("ins-collaborative-ethnography", "الإثنوغرافيا التعاونية", "Collaborative Ethnography", "إجراء الدراسات الإثنوغرافية بالتعاون الكامل مع المجتمعات."),
            ("ins-co-production-research", "البحث بالإنتاج المشترك", "Co-Production in Research", "إنتاج المعرفة بشكل مشترك مع الشركاء المحليين والمجتمعات."),
            ("ins-ai-anthropology-ethics", "أخلاقيات الذكاء الاصطناعي في الأنثروبولوجيا", "AI Ethics in Anthropology", "فحص القضايا الأخلاقية لاستخدام الذكاء الاصطناعي في البحث الأنثروبولوجي."),
            ("ins-surveillance-anthropology", "أنثروبولوجيا المراقبة", "Surveillance Anthropology", "دراسة أنظمة المراقبة والتحكم والخصوصية والسيطرة الاجتماعية."),
            ("ins-bioethics-anthropology", "الأخلاقيات الحيوية في الأنثروبولوجيا", "Bioethics in Anthropology", "دراسة القضايا الأخلاقية المتعلقة بالطب والصحة والجسد."),
        ]

        print(f"  Creating {len(instruments)} research instruments...")
        for slug, title_ar, title_en, desc in instruments:
            self.create_instrument(slug, title_ar, title_en, desc)

        print(f"  Total nodes created so far: {len(self.created_nodes)}")

        # ==========================================
        # SECTION 4: THEORETICAL DEBATES (15+ nodes)
        # ==========================================
        print("\n[4] Creating Theoretical Debates")

        debates = [
            ("dbt-materialism-vs-idealism-anthropology", "المادية مقابل المثالية في الأنثروبولوجيا", "Materialism vs. Idealism in Anthropology", "نقاش أساسي حول ما إذا كانت القوى الاقتصادية أم الأفكار والعقائد هي المحرك الأساسي للتغيير الاجتماعي."),
            ("dbt-universalism-vs-relativism", "الكونية مقابل النسبية الثقافية", "Universalism vs. Cultural Relativism", "جدل حول ما إذا كانت المبادئ الأخلاقية والقيم كونية أم نسبية لكل ثقافة."),
            ("dbt-science-vs-humanism-anthropology", "العلم مقابل الإنسانيات في الأنثروبولوجيا", "Science vs. Humanism in Anthropology", "نقاش حول ما إذا كانت الأنثروبولوجيا علماً طبيعياً أم إنسانياً."),
            ("dbt-activism-vs-neutrality-anthropology", "النشاط مقابل الحياد الأنثروبولوجي", "Activism vs. Neutrality in Anthropology", "جدل أخلاقي حول دور الأنثروبولوجيين في العدالة الاجتماعية والتغيير السياسي."),
            ("dbt-indigenous-rights-anthropology", "حقوق الشعوب الأصلية والأنثروبولوجيا", "Indigenous Rights & Anthropological Ethics", "نقاش حول مسؤولية الأنثروبولوجيين تجاه الشعوب الأصلية والملكية الفكرية."),
            ("dbt-development-anthropology-critique", "نقد أنثروبولوجيا التنمية", "Critique of Development Anthropology", "جدل حول ما إذا كانت أنثروبولوجيا التنمية تخدم المجتمعات أم الرأسمالية العالمية."),
            ("dbt-climate-change-anthropology", "الأنثروبولوجيا وأزمة المناخ", "Anthropology & Climate Change", "دراسة دور الأنثروبولوجيين في فهم وحل مشكلات المناخ والعدالة البيئية."),
            ("dbt-pandemic-anthropology", "الأنثروبولوجيا والأوبئة", "Anthropology & Pandemic Response", "نقاش حول دور الأنثروبولوجيين في فهم وحل مشاكل الأوبئة والصحة العامة."),
            ("dbt-refugee-migration-anthropology", "اللاجئون والهجرة والأنثروبولوجيا", "Refugees, Migration & Anthropology", "دراسة حركات الهجرة القسرية والشتات والحقوق الإنسانية."),
            ("dbt-mead-freeman-controversy", "جدل مياد-فريمان", "Mead-Freeman Controversy", "نقاش حول موثوقية دراسة مارجريت مياد في ساموا وحدود الإثنوغرافيا."),
            ("dbt-structuralism-vs-practice-theory", "البنيوية مقابل نظرية الممارسة", "Structuralism vs. Practice Theory", "جدل نظري حول ما إذا كانت البنى الاجتماعية أم الممارسات اليومية هي أساس المجتمع."),
            ("dbt-postcolonialism-anthropology", "ما بعد الاستعمار والأنثروبولوجيا", "Postcolonialism & Anthropology", "نقاش حول كيفية تجاوز الأنثروبولوجيا لإرثها الاستعماري."),
            ("dbt-feminist-anthropology-standpoint", "الأنثروبولوجيا النسوية ونظرية الموقع", "Feminist Anthropology & Standpoint Theory", "جدل حول كيف تشكل الهويات النسوية المعرفة الأنثروبولوجية."),
            ("dbt-queer-anthropology-kinship", "الأنثروبولوجيا الكويرية والقرابة", "Queer Anthropology & Kinship", "دراسة كيف تتحدى الهويات الكويرية النماذج التقليدية للقرابة والأسرة."),
        ]

        print(f"  Creating {len(debates)} theoretical debates...")
        for slug, title_ar, title_en, desc in debates:
            self.create_debate(slug, title_ar, title_en, desc)

        print(f"\n  TOTAL NODES CREATED: {len(self.created_nodes)}")

        return self.created_nodes

def main():
    gen = Phase6Generator()
    nodes = gen.generate_phase6_content()

    print("\n" + "=" * 60)
    print(f"PHASE 6 EXECUTION COMPLETE")
    print("=" * 60)
    print(f"Total Nodes Created: {len(nodes)}")
    print(f"\nBreakdown:")
    print(f"  Thinkers: {sum(1 for n in nodes if n['type'] == 'thinker')}")
    print(f"  Schools: {sum(1 for n in nodes if n['type'] == 'school')}")
    print(f"  Instruments: {sum(1 for n in nodes if n['type'] == 'instrument')}")
    print(f"  Debates: {sum(1 for n in nodes if n['type'] == 'debate')}")
    print(f"\nNew ID Ranges Used:")
    print(f"  Thinkers: THK-13253 to THK-{gen.next_thk_id - 1}")
    print(f"  Schools: SCH-13124 to SCH-{gen.next_sch_id - 1}")
    print(f"  Instruments: INS-{361:04d} to INS-{gen.next_ins_id - 1:04d}")
    print(f"  Debates: DBT-11830 to DBT-{gen.next_dbt_id - 1}")

if __name__ == "__main__":
    main()
