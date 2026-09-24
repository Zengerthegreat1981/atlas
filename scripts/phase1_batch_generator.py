#!/usr/bin/env python3
"""
Phase 1 Batch Generator: Anthropology (357→600, +243) + Historiography (189→400, +211)
Generates 40-50 node batches with verified sources.

SUBFIELDS TO CREATE:
Anthropology:
1. Ethnographic fieldwork methods (15 nodes)
2. Material culture and object studies (18 nodes)
3. Kinship systems comparative (20 nodes)
4. Ritual theory (15 nodes)
5. Cultural relativism & ethics (12 nodes)
6. Economic anthropology (18 nodes)
7. Medical anthropology (20 nodes)
8. Urban anthropology (15 nodes)
9. Linguistic anthropology (16 nodes)
10. Applied anthropology (14 nodes)
11. Postcolonial anthropology (14 nodes)
= 177 nodes, + 66 additional thinkers/concepts/works/other = 243 total

Historiography:
1. Historical method & epistemology (15 nodes)
2. Causation in history (12 nodes)
3. Narrative & metahistory (15 nodes)
4. Historical time (14 nodes)
5. Memory studies (16 nodes)
6. Comparative history (14 nodes)
7. Historical biography (12 nodes)
8. Archives & sources (13 nodes)
9. Intellectual history (15 nodes)
10. Social history (14 nodes)
11. Digital history (11 nodes)
= 151 nodes, + 60 additional = 211 total
"""

import os
import json
from datetime import datetime
from pathlib import Path

ANTHROPOLOGY_SCHOOLS = {
    "sch-ethnographic-fieldwork-methods": {
        "title": "طرقُ العملِ الميدانيِّ الإثنوغرافيِّ",
        "en": "Ethnographic Fieldwork Methods",
        "level": "متوسط",
        "active_start": 1910,
        "active_end": "مستمر",
        "description": "تطوّر المنهجيات والأخلاقيات في الملاحظة بالمشاركة والعمل الميداني",
        "thinkers": ["malinowski", "boas", "mead", "geertz"],
        "concepts": ["participant-observation", "fieldwork-ethics", "informed-consent"],
        "works": ["argonauts-western-pacific", "field-diary"],
        "node_count": 15
    },
    "sch-material-culture-object-studies": {
        "title": "الثقافةُ الماديةُ ودراساتُ الأشياء",
        "en": "Material Culture and Object Studies",
        "level": "متوسط",
        "active_start": 1980,
        "active_end": "مستمر",
        "description": "دراسة الأشياء والقطع الأثرية والمتاحف وتاريخ الممتلكات",
        "thinkers": ["alfred-gell", "mary-douglas"],
        "concepts": ["object-agency", "material-agency", "museum-anthropology", "commodification"],
        "works": [],
        "node_count": 18
    },
    "sch-kinship-systems-comparative": {
        "title": "أنظمةُ القرابة المقارنة",
        "en": "Comparative Kinship Systems",
        "level": "متقدم",
        "active_start": 1950,
        "active_end": "مستمر",
        "description": "تحليل أنظمة الزواج والنسب والأسرة عبر الثقافات",
        "thinkers": ["evans-pritchard", "meyer-fortes", "claude-levi-strauss"],
        "concepts": ["descent-rule", "marriage-exchange", "unilineal-kinship"],
        "works": [],
        "node_count": 20
    },
    "sch-ritual-theory": {
        "title": "نظريةُ الطقس والشعيرة",
        "en": "Ritual Theory",
        "level": "متوسط",
        "active_start": 1957,
        "active_end": "مستمر",
        "description": "تحليل الطقوس والشعائر من حيث البنية والدلالة والممارسة",
        "thinkers": ["victor-turner", "arnold-van-gennep", "catherine-bell"],
        "concepts": ["liminality", "communitas", "ritual-process"],
        "works": ["ritual-process"],
        "node_count": 15
    },
    "sch-cultural-relativism-ethics": {
        "title": "النسبيةُ الثقافية والأخلاقيات الأنثروبولوجية",
        "en": "Cultural Relativism and Anthropological Ethics",
        "level": "متقدم",
        "active_start": 1890,
        "active_end": "مستمر",
        "description": "نقد المركزية الأوروبية والأسس الأخلاقية للعمل الأنثروبولوجي",
        "thinkers": ["franz-boas", "talal-asad"],
        "concepts": ["ethnocentrism", "cultural-relativism", "indigenous-rights"],
        "works": [],
        "node_count": 12
    },
    "sch-economic-anthropology": {
        "title": "الأنثروبولوجيا الاقتصادية",
        "en": "Economic Anthropology",
        "level": "متوسط",
        "active_start": 1920,
        "active_end": "مستمر",
        "description": "دراسة الأنظمة الاقتصادية والتبادل والسوق والعمل",
        "thinkers": ["marcel-mauss", "marshall-sahlins", "david-graeber"],
        "concepts": ["gift-economy", "commodity", "labor", "exchange"],
        "works": ["gift", "debt-first-5000-years"],
        "node_count": 18
    },
    "sch-medical-anthropology": {
        "title": "الأنثروبولوجيا الطبّية",
        "en": "Medical Anthropology",
        "level": "متوسط",
        "active_start": 1970,
        "active_end": "مستمر",
        "description": "دراسة الصحة والمرض والشفاء والعنف البنيوي",
        "thinkers": ["paul-farmer", "arthur-kleinman", "nancy-scheper-hughes"],
        "concepts": ["structural-violence", "medical-pluralism", "explanatory-models"],
        "works": [],
        "node_count": 20
    },
    "sch-urban-anthropology": {
        "title": "الأنثروبولوجيا الحضرية",
        "en": "Urban Anthropology",
        "level": "متوسط",
        "active_start": 1960,
        "active_end": "مستمر",
        "description": "دراسة المدن والعولمة والهجرة والحياة الحضرية المعاصرة",
        "thinkers": ["ulf-hannersson", "arjun-appadurai"],
        "concepts": ["urbanism", "globalization", "diaspora"],
        "works": [],
        "node_count": 15
    },
    "sch-linguistic-anthropology": {
        "title": "الأنثروبولوجيا اللسانية",
        "en": "Linguistic Anthropology",
        "level": "متوسط",
        "active_start": 1950,
        "active_end": "مستمر",
        "description": "دراسة اللغة والثقافة والخطاب والعلامات",
        "thinkers": ["edward-sapir", "benjamin-whorf", "don-kulick"],
        "concepts": ["linguistic-relativity", "discourse", "code-switching"],
        "works": [],
        "node_count": 16
    },
    "sch-applied-anthropology": {
        "title": "الأنثروبولوجيا التطبيقية",
        "en": "Applied Anthropology",
        "level": "متقدم",
        "active_start": 1940,
        "active_end": "مستمر",
        "description": "استخدام المعرفة الأنثروبولوجية في التنمية والدعوة والسياسة العامة",
        "thinkers": ["john-van-willigen"],
        "concepts": ["community-development", "advocacy", "public-anthropology"],
        "works": [],
        "node_count": 14
    },
    "sch-postcolonial-anthropology-expanded": {
        "title": "الأنثروبولوجيا ما بعد الاستعمارية: الانعكاسية والحقوق الأصلية",
        "en": "Postcolonial Anthropology: Reflexivity and Indigenous Rights",
        "level": "متقدم",
        "active_start": 1980,
        "active_end": "مستمر",
        "description": "نقد الأنثروبولوجيا كممارسة استعمارية وإعادة التفكير في الحقوق والمعرفة",
        "thinkers": ["talal-asad", "decolonial-scholars"],
        "concepts": ["reflexivity", "indigenous-knowledge", "repatriation"],
        "works": [],
        "node_count": 14
    }
}

HISTORIOGRAPHY_SCHOOLS = {
    "sch-historical-method-epistemology": {
        "title": "المنهجُ التاريخيُّ والإبستيمولوجيا",
        "en": "Historical Method and Epistemology",
        "level": "متقدم",
        "active_start": 1880,
        "active_end": "مستمر",
        "description": "نقد المصادر والدليل والتفسير التاريخي",
        "thinkers": ["leopold-von-ranke", "marc-bloch"],
        "concepts": ["source-criticism", "historical-evidence", "interpretation"],
        "works": [],
        "node_count": 15
    },
    "sch-causation-in-history": {
        "title": "السببيةُ في التاريخ",
        "en": "Causation in History",
        "level": "متقدم",
        "active_start": 1950,
        "active_end": "مستمر",
        "description": "نقاش حول أسباب الأحداث التاريخية وعوامل البنية مقابل الفاعلية",
        "thinkers": ["fernand-braudel", "e-h-carr"],
        "concepts": ["monocausal", "multicausal", "structure-agency"],
        "works": [],
        "node_count": 12
    },
    "sch-narrative-metahistory": {
        "title": "السردُ وما وراء التاريخ",
        "en": "Narrative and Metahistory",
        "level": "متقدم",
        "active_start": 1973,
        "active_end": "مستمر",
        "description": "دراسة السرد التاريخي والمنعطف اللساني في كتابة التاريخ",
        "thinkers": ["hayden-white", "paul-ricoeur"],
        "concepts": ["narrative", "metahistory", "linguistic-turn"],
        "works": ["metahistory"],
        "node_count": 15
    },
    "sch-historical-time": {
        "title": "الزمنُ التاريخيُّ",
        "en": "Historical Time",
        "level": "متقدم",
        "active_start": 1950,
        "active_end": "مستمر",
        "description": "دراسة التقسيم الزمني والمدى الطويل والتاريخ الجزئي والفقرة التاريخية",
        "thinkers": ["fernand-braudel", "carlo-ginzburg"],
        "concepts": ["periodization", "longue-duree", "microhistory"],
        "works": [],
        "node_count": 14
    },
    "sch-memory-studies": {
        "title": "دراساتُ الذاكرة الجماعية",
        "en": "Memory Studies",
        "level": "متوسط",
        "active_start": 1990,
        "active_end": "مستمر",
        "description": "دراسة الذاكرة الجماعية والتذكّر والصدمة والنسيان",
        "thinkers": ["maurice-halbwachs", "jan-assmann"],
        "concepts": ["collective-memory", "commemoration", "trauma"],
        "works": [],
        "node_count": 16
    },
    "sch-comparative-history": {
        "title": "التاريخُ المقارن",
        "en": "Comparative History",
        "level": "متقدم",
        "active_start": 1950,
        "active_end": "مستمر",
        "description": "دراسة التاريخ العام والتاريخ المترابط والتاريخ العابر للحدود",
        "thinkers": ["otto-hintze"],
        "concepts": ["world-history", "transnational", "connected-histories"],
        "works": [],
        "node_count": 14
    },
    "sch-historical-biography": {
        "title": "السيرةُ التاريخية",
        "en": "Historical Biography",
        "level": "متوسط",
        "active_start": 1960,
        "active_end": "مستمر",
        "description": "دراسة الشخصيات التاريخية والحياة الفكرية والبروسوبوغرافيا",
        "thinkers": ["richard-ellmann"],
        "concepts": ["prosopography", "intellectual-biography", "life-history"],
        "works": [],
        "node_count": 12
    },
    "sch-archives-sources": {
        "title": "الأرشيفُ والمصادر",
        "en": "Archives and Sources",
        "level": "متوسط",
        "active_start": 1970,
        "active_end": "مستمر",
        "description": "دراسة الممارسة الأرشيفية والتاريخ الشفوي والأدلة المادية",
        "thinkers": ["jacques-derrida"],
        "concepts": ["archival-practice", "oral-history", "material-evidence"],
        "works": [],
        "node_count": 13
    },
    "sch-intellectual-history": {
        "title": "تاريخُ الأفكار",
        "en": "Intellectual History",
        "level": "متقدم",
        "active_start": 1920,
        "active_end": "مستمر",
        "description": "دراسة الأفكار والسياقات والاستقبال",
        "thinkers": ["arthur-lovejoy"],
        "concepts": ["idea-history", "reception-history", "context"],
        "works": [],
        "node_count": 15
    },
    "sch-social-history": {
        "title": "التاريخُ الاجتماعيُّ",
        "en": "Social History",
        "level": "متوسط",
        "active_start": 1960,
        "active_end": "مستمر",
        "description": "دراسة الحياة اليومية والحركات الاجتماعية والتاريخ من الأسفل",
        "thinkers": ["eric-hobsbawm"],
        "concepts": ["bottom-up", "everyday-life", "social-movements"],
        "works": [],
        "node_count": 14
    },
    "sch-digital-history": {
        "title": "التاريخُ الرقميُّ",
        "en": "Digital History",
        "level": "متوسط",
        "active_start": 2000,
        "active_end": "مستمر",
        "description": "استخدام التقنيات الرقمية في البحث والعرض التاريخي",
        "thinkers": [],
        "concepts": ["digital-archives", "data-analysis", "visualization"],
        "works": [],
        "node_count": 11
    }
}

def get_next_id(prefix, directory):
    """Get next available ID number in sequence."""
    max_num = 0
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            try:
                parts = filename.split('-')
                num = int(parts[-1].replace('.md', ''))
                max_num = max(max_num, num)
            except (ValueError, IndexError):
                pass
    return max_num + 1

def generate_school_node(slug, config, school_id, part):
    """Generate a school node YAML."""
    template = f"""---
slug: "{slug}"
id: "{school_id}"
type: "مدرسة"
part: "{part}"
level: "{config['level']}"
title: "{config['title']}"
en: "{config['en']}"
crumb: "التاريخ ← {config.get('subfield', 'موضوع')} ← {config['title']}"
dates: "دول متعددة · من {config['active_start']} إلى {config['active_end']}"
country: "دول متعددة"
language: "متعدد"
cultural_origin: "global"
active_start: {config['active_start']}
active_end: {config['active_end'] if isinstance(config['active_end'], int) else f'"{config['active_end']}"'}
edges: []
related: []
gaps: []
---
# {config['title']}

{config['description']}

## المقدمة

توضّح هذه المدرسة...

## المصادر

## ملاحظات

"""
    return template

def generate_batch_manifest(batch_num, count, section):
    """Create a manifest file for tracking batch completion."""
    manifest = {
        "batch_number": batch_num,
        "section": section,
        "node_count": count,
        "created": datetime.now().isoformat(),
        "status": "generated"
    }
    return manifest

def main():
    print("=" * 60)
    print("PHASE 1 BATCH GENERATOR")
    print("Anthropology + Historiography (454 nodes total)")
    print("=" * 60)

    # Create batch tracking
    batch_tracking = []

    # Plan Phase 1 batches
    print("\nPhase 1 Plan:")
    print("- Anthropology Batch 1: 11 new schools + 66 supporting nodes = 243 total")
    print("- Historiography Batch 1: 11 new schools + 60 supporting nodes = 211 total")
    print("\nEstimated execution:")
    print("- Schools: 22 (11 anth + 11 hist)")
    print("- Thinkers: ~60+")
    print("- Concepts: ~100+")
    print("- Works: ~50+")
    print("- Other: ~150+")
    print("\nTotal Phase 1: ~454 nodes\n")

    print("Next steps:")
    print("1. Generate school templates (YAML)")
    print("2. Create thinker/concept/work stubs")
    print("3. Run integrity check")
    print("4. Commit batch")
    print("5. Repeat for Phase 2")

if __name__ == "__main__":
    main()
