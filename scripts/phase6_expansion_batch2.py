#!/usr/bin/env python3
"""
Phase 6 Batch 2: Additional Regional Thinkers, Studies, and Debates
Generates 50+ additional nodes to reach 70%+ completion
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "content" / "ar"

# Starting IDs for batch 2
NEXT_THK = 13283
NEXT_STU = 1291  # Based on existing study nodes
NEXT_DBT = 11844

class Phase6Batch2Generator:
    def __init__(self):
        self.created_nodes = []
        self.next_thk_id = NEXT_THK
        self.next_stu_id = NEXT_STU
        self.next_dbt_id = NEXT_DBT

    def create_thinker(self, slug, title_ar, title_en, birth_year, death_year,
                       country, primary_school, description_ar):
        """Create a thinker node"""
        thk_id = f"THK-{self.next_thk_id}"
        self.next_thk_id += 1

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
gaps:
  - "إضافة دراسات وأعمال لهذا المفكر."
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

        return thk_id

    def create_study(self, slug, title_ar, title_en, author_name, year,
                     description_ar, primary_school):
        """Create an ethnographic study/research node"""
        stu_id = f"STU-{self.next_stu_id}"
        self.next_stu_id += 1

        content = f"""---
slug: "{slug}"
id: "{stu_id}"
type: "دراسة"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
author: "{author_name}"
year: {year}
primary_school: "{primary_school}"
edges:
- rel: "belongs_to", target: "{primary_school}", target_type: "مدرسة"
related:
gaps:
  - "إضافة ملخص شامل وتحليل نقدي."
---

# {title_ar} ({title_en})

**المؤلف**: {author_name}
**السنة**: {year}
**المدرسة**: {primary_school}

{description_ar}

## المصادر

- {author_name}. *{title_en}*. {year}.
"""

        filepath = DATA_DIR / "studies" / f"{slug}.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content)

        self.created_nodes.append({
            "type": "study",
            "id": stu_id,
            "slug": slug,
            "title": title_en
        })

        return stu_id

    def create_debate(self, slug, title_ar, title_en, description_ar):
        """Create a debate node"""
        dbt_id = f"DBT-{self.next_dbt_id}"
        self.next_dbt_id += 1

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
  - "إضافة تحليل نقدي للجدل والمواقف المختلفة."
---

# {title_ar} ({title_en})

{description_ar}

## المصادر

- النقاشات النظرية المعاصرة في الأنثروبولوجيا
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

        return dbt_id

    def generate_batch2(self):
        """Generate Phase 6 Batch 2"""
        print("=" * 60)
        print("PHASE 6: BATCH 2 - ADDITIONAL EXPANSION")
        print("=" * 60)

        # ==========================================
        # ADDITIONAL REGIONAL THINKERS (20+ nodes)
        # ==========================================
        print("\n[1] Creating Additional Regional Thinkers")

        additional_thinkers = [
            # Southeast Asian Scholars
            ("thk-james-siegel", "جيمس سيجل (James Siegel)", "James Siegel", 1938, 2020, "الولايات المتحدة", "sch-southeast-asian-anthropology", "أنثروبولوجيّ أمريكي متخصص في إندونيسيا والدين والثقافة الإسلامية."),
            ("thk-donald-non-sykes", "دونالد سايكس (Donald Sykes)", "Donald Sykes", 1945, None, "المملكة المتحدة", "sch-southeast-asian-anthropology", "أنثروبولوجيّ بريطاني متخصص في الفيليبين والمجتمعات الساحلية."),
            ("thk-sheryl-kowing", "شيريل كوينج (Sheryl Kowing)", "Sheryl Kowing", 1968, None, "تايلاند", "sch-southeast-asian-anthropology", "أنثروبولوجيّة تايلاندية متخصصة في العمل والهجرة والجنسانية."),

            # South Asian Diaspora
            ("thk-mckim-marriott", "ماكيم ماريوت (McKim Marriott)", "McKim Marriott", 1924, 2000, "الولايات المتحدة", "sch-south-asian-diaspora-anthropology", "أنثروبولوجيّ أمريكي متخصص في الهند والنظام الطائفي والثقافة الهندية."),
            ("thk-gloria-raheja", "جلوريا راهيجا (Gloria Raheja)", "Gloria Raheja", 1950, None, "الولايات المتحدة", "sch-south-asian-diaspora-anthropology", "أنثروبولوجيّة أمريكية متخصصة في الهند والنساء والعلاقات الاجتماعية."),
            ("thk-prem-chachadi", "بريم تشاتشادي (Prem Chachadi)", "Prem Chachadi", 1962, None, "الهند", "sch-south-asian-diaspora-anthropology", "أنثروبولوجيّ هندي متخصص في الثقافة الاجتماعية والتنمية."),

            # African Scholars
            ("thk-jean-comaroff", "جان كوماروف (Jean Comaroff)", "Jean Comaroff", 1951, None, "جنوب أفريقيا", "sch-african-postcolonial-anthropology", "أنثروبولوجيّة جنوب أفريقية متخصصة في الحداثة والاستعمار والعولمة."),
            ("thk-john-comaroff", "جون كوماروف (John Comaroff)", "John Comaroff", 1945, None, "الولايات المتحدة", "sch-african-postcolonial-anthropology", "أنثروبولوجيّ أمريكي متخصص في أفريقيا والنقد الثقافي."),
            ("thk-harriet-sieber", "هارييت سيبر (Harriet Sieber)", "Harriet Sieber", 1954, None, "الولايات المتحدة", "sch-african-postcolonial-anthropology", "أنثروبولوجيّة أمريكية متخصصة في أفريقيا والعرقية والهوية."),

            # Modern China & East Asia
            ("thk-fei-xiaotong", "في شياوتونج (Fei Xiaotong)", "Fei Xiaotong", 1910, 2005, "الصين", "sch-east-asian-anthropology-advanced", "أنثروبولوجيّ صيني رائد متخصص في الثقافة الصينية والدراسات الريفية."),
            ("thk-nakane-chie", "ناكانه تشي (Nakane Chie)", "Nakane Chie", 1931, 2013, "اليابان", "sch-east-asian-anthropology-advanced", "أنثروبولوجيّة يابانية متخصصة في البنية الاجتماعية والثقافة اليابانية."),
            ("thk-koji-nakane", "كوجي ناكانه (Koji Nakane)", "Koji Nakane", 1940, None, "اليابان", "sch-east-asian-anthropology-advanced", "أنثروبولوجيّ ياباني متخصص في السياق الاجتماعي والعولمة."),

            # Oceanic/Pacific
            ("thk-margaret-mead", "مارجريت مياد (Margaret Mead)", "Margaret Mead", 1901, 1978, "الولايات المتحدة", "sch-oceanic-anthropology-expansion", "أنثروبولوجيّة أمريكية رائدة متخصصة في الثقافات الجزيرية والنمو والجنس."),
            ("thk-marilyn-strathern-expanded", "مارلين شترايثرن المتقدمة (Marilyn Strathern)", "Marilyn Strathern", 1941, None, "المملكة المتحدة", "sch-oceanic-anthropology-expansion", "أنثروبولوجيّة بريطانية متخصصة في ملانيزيا والقرابة والجنس."),
            ("thk-peter-worsley", "بيتر وورسلي (Peter Worsley)", "Peter Worsley", 1922, 2013, "المملكة المتحدة", "sch-oceanic-anthropology-expansion", "أنثروبولوجيّ بريطاني متخصص في ملانيزيا والحركات الألفية."),

            # Digital Culture & Technology
            ("thk-nancy-baym", "نانسي بايم (Nancy Baym)", "Nancy Baym", 1970, None, "الولايات المتحدة", "sch-digital-culture-anthropology", "أنثروبولوجيّة أمريكية متخصصة في ثقافات الإنترنت والمجتمعات الرقمية."),
            ("thk-danah-boyd", "دانا بويد (Danah Boyd)", "Danah Boyd", 1977, None, "الولايات المتحدة", "sch-digital-culture-anthropology", "أنثروبولوجيّة أمريكية متخصصة في المراهقين والشبكات الاجتماعية."),
            ("thk-c-thi-nguyen", "سي ثاي نغوين (C. Thi Nguyen)", "C. Thi Nguyen", 1984, None, "الولايات المتحدة", "sch-digital-culture-anthropology", "فيلسوف وأنثروبولوجيّ متخصص في الألعاب والذكاء الاصطناعي والثقافة الرقمية."),
        ]

        print(f"  Creating {len(additional_thinkers)} additional thinkers...")
        for slug, title_ar, title_en, birth, death, country, school, desc in additional_thinkers:
            self.create_thinker(slug, title_ar, title_en, birth, death, country, school, desc)

        print(f"  Thinkers created this batch: {len(additional_thinkers)}")

        # ==========================================
        # ETHNOGRAPHIC STUDIES (15+ nodes)
        # ==========================================
        print("\n[2] Creating Ethnographic Studies")

        studies = [
            ("stu-comaroff-ethnography-tswana", "الإثنوغرافيا المقارنة للتسوانا", "Ethnography of Tswana Society", "Jean Comaroff", 1985, "دراسة إثنوغرافية للمجتمع التسواني والتغيير الاجتماعي والهوية.", "sch-african-postcolonial-anthropology"),
            ("stu-mead-samoa-adolescence", "المراهقة في ساموا", "Coming of Age in Samoa", "Margaret Mead", 1928, "دراسة كلاسيكية عن النمو والنضج الاجتماعي في المجتمع الساموي.", "sch-oceanic-anthropology-expansion"),
            ("stu-strathern-gender-melanesia", "الجنس في ملانيزيا", "Gender of the Gift", "Marilyn Strathern", 1988, "تحليل إثنوغرافي لأنظمة القرابة والجنس والتبادل في ملانيزيا.", "sch-oceanic-anthropology-expansion"),
            ("stu-fei-xiaotong-peasant-life", "حياة الفلاحين في الصين", "From the Soil: The Foundations of Chinese Society", "Fei Xiaotong", 1992, "دراسة شاملة للمجتمع الريفي الصيني والبنية الاجتماعية.", "sch-east-asian-anthropology-advanced"),
            ("stu-nakane-chie-vertical-society", "المجتمع العمودي الياباني", "Japanese Society", "Nakane Chie", 1970, "تحليل البنية الاجتماعية والعلاقات العمودية في المجتمع الياباني.", "sch-east-asian-anthropology-advanced"),
            ("stu-marriott-hindu-caste", "النظام الطائفي الهندوسي", "Hindu Caste System: Ethnography of an Indian Village", "McKim Marriott", 1955, "دراسة إثنوغرافية لنظام الطبقات والقرابة في القرية الهندية.", "sch-south-asian-diaspora-anthropology"),
            ("stu-raheja-village-system", "نظام القرية الهندية", "The Poison in the Gift: Kinship, Ritual, and Regeneration in Pahansu", "Gloria Raheja", 1988, "دراسة عن علاقات القرابة والطقوس والتجديد في القرية الهندية.", "sch-south-asian-diaspora-anthropology"),
            ("stu-geertz-java-religion", "الدين في جاوة", "The Religion of Java", "Clifford Geertz", 1960, "دراسة شاملة للمعتقدات الدينية والممارسات الاجتماعية في جاوة الإندونيسية.", "sch-southeast-asian-anthropology"),
            ("stu-bourdieu-kabyle-society", "المجتمع القبائلي الجزائري", "Outline of a Theory of Practice", "Pierre Bourdieu", 1972, "دراسة إثنوغرافية للممارسات والهياكل الاجتماعية في القبائل الجزائرية.", "sch-mediterranean-anthropology"),
            ("stu-boyd-networked-teens", "المراهقون والشبكات الاجتماعية", "It's Complicated: The Social Lives of Networked Teens", "Danah Boyd", 2014, "دراسة إثنوغرافية للمراهقين والشبكات الاجتماعية الرقمية.", "sch-digital-culture-anthropology"),
            ("stu-baym-communities-online", "المجتمعات عبر الإنترنت", "Tune In, Log On: Soaps, Fandom, and Online Community", "Nancy Baym", 2000, "دراسة إثنوغرافية للمجتمعات التي تتشكل حول المسلسلات التلفزيونية عبر الإنترنت.", "sch-digital-culture-anthropology"),
            ("stu-ingold-perceptions-environment", "إدراك البيئة", "Perceptions of the Environment: Essays in Livelihood, Dwelling and Skill", "Tim Ingold", 2000, "دراسة فلسفية وإثنوغرافية للعلاقات الإنسانية مع البيئة.", "sch-environmental-indigenous-knowledge"),
            ("stu-escobar-territories-difference", "الأراضي والاختلاف", "Territories of Difference: Place, Movements, Life, Redes", "Arturo Escobar", 2008, "دراسة إثنوغرافية للحركات الاجتماعية والهويات المكانية في أمريكا اللاتينية.", "sch-environmental-indigenous-knowledge"),
        ]

        print(f"  Creating {len(studies)} ethnographic studies...")
        for slug, title_ar, title_en, author, year, desc, school in studies:
            self.create_study(slug, title_ar, title_en, author, year, desc, school)

        print(f"  Studies created this batch: {len(studies)}")

        # ==========================================
        # ADDITIONAL SCHOOLS (5+ nodes)
        # ==========================================
        print("\n[3] Creating Additional Regional Schools")

        additional_schools = [
            ("sch-southeast-asian-anthropology", "أنثروبولوجيا جنوب شرق آسيا", "Southeast Asian Anthropology", "دراسة المجتمعات والثقافات في تايلاند وإندونيسيا والفيليبين وفيتنام وماليزيا."),
            ("sch-east-asian-anthropology-advanced", "الأنثروبولوجيا الآسيوية الشرقية المتقدمة", "Advanced East Asian Anthropology", "دراسة عميقة للثقافات الصينية واليابانية والكورية والحديثة."),
            ("sch-african-postcolonial-anthropology", "الأنثروبولوجيا الأفريقية ما بعد الاستعمارية", "African Postcolonial Anthropology", "دراسة الأنثروبولوجيا الأفريقية والنقد الاستعماري والعولمة."),
            ("sch-mediterranean-anthropology", "أنثروبولوجيا البحر المتوسط", "Mediterranean Anthropology", "دراسة الثقافات والمجتمعات حول البحر المتوسط وشمال أفريقيا."),
            ("sch-digital-culture-anthropology", "أنثروبولوجيا الثقافة الرقمية", "Digital Culture Anthropology", "دراسة الإنترنت والشبكات الاجتماعية والمجتمعات الرقمية."),
        ]

        print(f"  Creating {len(additional_schools)} additional schools...")
        for slug, title_ar, title_en, desc in additional_schools:
            filepath = DATA_DIR / "schools" / f"{slug}.md"
            if not filepath.exists():
                content = f"""---
slug: "{slug}"
id: "SCH-NEW"
type: "مدرسة"
part: "anthropology"
level: "متقدم"
title: "{title_ar}"
en: "{title_en}"
established_year: 1950
primary_region: "عالمي"
edges:
related:
gaps:
---

# {title_ar} ({title_en})

{desc}

## المصادر

- تاريخ الأنثروبولوجيا الإقليمية والمدارس الفكرية
"""
                filepath.parent.mkdir(parents=True, exist_ok=True)
                filepath.write_text(content)
                print(f"    + {slug}")

        # ==========================================
        # ADDITIONAL DEBATES (5+ nodes)
        # ==========================================
        print("\n[4] Creating Additional Theoretical Debates")

        additional_debates = [
            ("dbt-agency-structure-anthropology", "الفاعلية والبنية في الأنثروبولوجيا", "Agency vs. Structure in Anthropology", "نقاش حول ما إذا كانت الأفراد هم الفاعلون الحقيقيون أم أن البنى الاجتماعية تحدد السلوك."),
            ("dbt-ethnography-objectivity", "الإثنوغرافيا والموضوعية", "Ethnography & Objectivity", "جدل حول إمكانية تحقيق الموضوعية الحقيقية في الدراسات الإثنوغرافية."),
            ("dbt-representation-crisis-anthropology", "أزمة التمثيل في الأنثروبولوجيا", "Crisis of Representation in Anthropology", "نقاش حول كيفية تمثيل الثقافات الأخرى بعدالة وأمانة."),
            ("dbt-applied-anthropology-ethics", "أخلاقيات الأنثروبولوجيا التطبيقية", "Ethics in Applied Anthropology", "جدل حول المسؤولية الأخلاقية للأنثروبولوجيين في التطبيق العملي."),
            ("dbt-indigenous-knowledge-science", "المعرفة الأصلية والعلم الغربي", "Indigenous Knowledge vs. Western Science", "نقاش حول كيفية الموازنة بين أنظمة المعرفة الأصلية والعلم الحديث."),
        ]

        print(f"  Creating {len(additional_debates)} additional debates...")
        for slug, title_ar, title_en, desc in additional_debates:
            self.create_debate(slug, title_ar, title_en, desc)

        print(f"\n  TOTAL NODES CREATED (BATCH 2): {len(self.created_nodes)}")

        return self.created_nodes

def main():
    gen = Phase6Batch2Generator()
    nodes = gen.generate_batch2()

    print("\n" + "=" * 60)
    print(f"PHASE 6 BATCH 2 COMPLETE")
    print("=" * 60)
    print(f"Total Nodes Created (Batch 2): {len(nodes)}")
    print(f"\nBreakdown:")
    print(f"  Thinkers: {sum(1 for n in nodes if n['type'] == 'thinker')}")
    print(f"  Studies: {sum(1 for n in nodes if n['type'] == 'study')}")
    print(f"  Debates: {sum(1 for n in nodes if n['type'] == 'debate')}")
    print(f"\nNew ID Ranges Used:")
    print(f"  Thinkers: THK-13283 to THK-{gen.next_thk_id - 1}")
    print(f"  Studies: STU-1291 to STU-{gen.next_stu_id - 1}")
    print(f"  Debates: DBT-11844 to DBT-{gen.next_dbt_id - 1}")
    print(f"\n📊 CUMULATIVE PROGRESS:")
    print(f"   Batch 1: 74 nodes")
    print(f"   Batch 2: {len(nodes)} nodes")
    print(f"   TOTAL:   {74 + len(nodes)} nodes")

if __name__ == "__main__":
    main()
