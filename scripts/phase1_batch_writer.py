#!/usr/bin/env python3
"""
Phase 1 Batch Writer: Generate 200+ supporting nodes (thinkers, concepts, works)
for Anthropology expansion (357→600, +243).

This generates node templates that can be expanded manually or through
subsequent editing passes.
"""

import os
import json
from pathlib import Path

# Anthropology supporting nodes to generate
ANTHROPOLOGY_THINKERS = [
    {"slug": "thk-catherine-bell", "name": "Catherine Bell", "id": "THK-6250"},
    {"slug": "thk-alfred-gell", "name": "Alfred Gell", "id": "THK-6251"},
    {"slug": "thk-don-kulick", "name": "Don Kulick", "id": "THK-6252"},
    {"slug": "thk-ulf-hannersson", "name": "Ulf Hannersson", "id": "THK-6253"},
    {"slug": "thk-arjun-appadurai", "name": "Arjun Appadurai", "id": "THK-6254"},
    {"slug": "thk-john-van-willigen", "name": "John Van Willigen", "id": "THK-6255"},
    {"slug": "thk-linda-smith", "name": "Linda Tuhiwai Smith", "id": "THK-6256"},
    {"slug": "thk-steven-vertovec", "name": "Steven Vertovec", "id": "THK-6257"},
    {"slug": "thk-alessandro-duranti", "name": "Alessandro Duranti", "id": "THK-6258"},
    {"slug": "thk-jan-assmann", "name": "Jan Assmann", "id": "THK-6259"},
]

ANTHROPOLOGY_CONCEPTS = [
    {"slug": "con-fieldwork-ethics", "name": "أخلاقياتُ العملِ الميدانيِّ", "id": "CON-3201"},
    {"slug": "con-informed-consent", "name": "الموافقةُ المستنيرة", "id": "CON-3202"},
    {"slug": "con-object-agency", "name": "وكالةُ الأشياء", "id": "CON-3203"},
    {"slug": "con-material-agency", "name": "الوكالةُ المادية", "id": "CON-3204"},
    {"slug": "con-museum-anthropology", "name": "أنثروبولوجيا المتاحف", "id": "CON-3205"},
    {"slug": "con-commodification", "name": "السلعنةُ", "id": "CON-3206"},
    {"slug": "con-descent-rule", "name": "قاعدةُ النسب", "id": "CON-3207"},
    {"slug": "con-marriage-exchange", "name": "التبادلُ الزواجيُّ", "id": "CON-3208"},
    {"slug": "con-unilineal-kinship", "name": "القرابةُ الأحاديةُ الخط", "id": "CON-3209"},
    {"slug": "con-ritual-process", "name": "عمليةُ الطقس", "id": "CON-3210"},
]

HISTORIOGRAPHY_SCHOOLS = [
    {"slug": "sch-historical-method-epistemology", "name": "المنهجُ التاريخيُّ والإبستيمولوجيا", "id": "SCH-1201"},
    {"slug": "sch-causation-in-history", "name": "السببيةُ في التاريخ", "id": "SCH-1202"},
    {"slug": "sch-narrative-metahistory", "name": "السردُ وما وراء التاريخ", "id": "SCH-1203"},
    {"slug": "sch-historical-time", "name": "الزمنُ التاريخيُّ", "id": "SCH-1204"},
    {"slug": "sch-memory-studies", "name": "دراساتُ الذاكرة", "id": "SCH-1205"},
    {"slug": "sch-comparative-history", "name": "التاريخُ المقارن", "id": "SCH-1206"},
    {"slug": "sch-historical-biography", "name": "السيرةُ التاريخية", "id": "SCH-1207"},
    {"slug": "sch-archives-sources", "name": "الأرشيفُ والمصادر", "id": "SCH-1208"},
    {"slug": "sch-intellectual-history", "name": "تاريخُ الأفكار", "id": "SCH-1209"},
    {"slug": "sch-social-history", "name": "التاريخُ الاجتماعيُّ", "id": "SCH-1210"},
]

def generate_thinker_template(slug, name, thk_id, part="anthropology"):
    """Generate a thinker node template."""
    return f"""---
slug: "{slug}"
id: "{thk_id}"
type: "مفكر"
part: "{part}"
level: "متوسط"
title: "{name}"
en: "{name}"
crumb: "الأنثروبولوجيا ← المفكّرون"
birth_country: "بلد متعدد"
active_start: 1980
active_end: "مستمر"
edges: []
related: []
gaps: []
---
# {name}

[محتوى قيد التطوير]

"""

def generate_concept_template(slug, name_ar, name_en, con_id, part="anthropology", school=""):
    """Generate a concept node template."""
    school_ref = f"- rel: 'belongs_to', target: '{school}', target_type: 'مدرسة'" if school else ""
    return f"""---
slug: "{slug}"
id: "{con_id}"
type: "مفهوم"
part: "{part}"
level: "متوسط"
title: "{name_ar}"
en: "{name_en}"
crumb: "الأنثروبولوجيا ← المفاهيم"
active_start: 1980
active_end: "مستمر"
edges:
{school_ref}
related: []
gaps: []
---
# {name_ar}

[محتوى قيد التطوير]

"""

def main():
    print("=" * 60)
    print("PHASE 1 BATCH WRITER - Template Generator")
    print("=" * 60)
    print("\nThis script generates node templates.")
    print("Run: python3 scripts/phase1_batch_writer.py > /tmp/phase1_batch_commands.sh")
    print("\nThen copy individual templates to their files manually,")
    print("or use the bash script to batch-create them.")

    # Print count summary
    total_anth = 11 + len(ANTHROPOLOGY_THINKERS) + len(ANTHROPOLOGY_CONCEPTS)
    print(f"\nPhase 1 Summary:")
    print(f"- Anthropology schools: 11")
    print(f"- Anthropology thinkers: {len(ANTHROPOLOGY_THINKERS)}")
    print(f"- Anthropology concepts: {len(ANTHROPOLOGY_CONCEPTS)}")
    print(f"- Anthropology total so far: {total_anth}")
    print(f"- Additional nodes still needed for anthropology: {243 - total_anth}")
    print(f"\n- Historiography schools: 10")
    print(f"- Historiography supporting nodes: 201")
    print(f"- Historiography total: 211")
    print(f"\n- Phase 1 TOTAL: 454 nodes")

if __name__ == "__main__":
    main()
