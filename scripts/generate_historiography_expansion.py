#!/usr/bin/env python3
"""
Generate historiography expansion nodes (300-400 total).
Batch 1: Ancient historiography (50 nodes)
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# Base configuration
CONTENT_AR_PATH = Path("/Users/mina/Desktop/Atlas/content/ar")
THINKERS_PATH = CONTENT_AR_PATH / "thinkers"
SCHOOLS_PATH = CONTENT_AR_PATH / "schools"
CONCEPTS_PATH = CONTENT_AR_PATH / "concepts"

# ID counter - starting from 13200 (after existing 13102)
ID_COUNTER = 13200

def get_next_id(prefix: str) -> str:
    """Generate next ID."""
    global ID_COUNTER
    ID_COUNTER += 1
    return f"{prefix.upper()}-{ID_COUNTER}"

# PHASE 1: Ancient Historiography Nodes (50 nodes)
ANCIENT_HISTORIANS = [
    {
        "slug": "thk-herodotus",
        "title": "هيرودوت (Herodotus)",
        "en": "Herodotus",
        "dates": "484–425 ق.م",
        "type": "thinker",
        "content": """# هيرودوت — مؤسّسُ التاريخ الحديثي

**هيرودوت** (484–425 ق.م) من هاليكارناسوس، يلقّب بـ**«أبي التاريخ»** — أوّل مؤرخ يسعى إلى التحقّق من الروايات عبر الاستقصاء الميداني والمقابلات، لا الاعتماد على الأساطير الشعرية وحدها.

## حياته والسياق

- وُلد في ساحل آسيا الصغرى اليونانية في نهاية حروب اليونان والفرس (480–479 ق.م)
- سافر عبر العالم المعروف يومها: مصر، ليبيا، الشام، بابل، بحر الخزر
- ألّف **التاريخ** (Historiai، 9 كتب) وهي الروايةُ المتسلسلة الأولى للحروب الفارسية
- عاش في أثينا مع بركليس، ثم في ثوري (مستعمرة أثينية)

## المنهج

### الاستقصاءُ الميداني (Historiē/Inquiry)
- لم يعتمد على الأساطير الهوميروسية بل على **شهادات العيان** والتحريات المباشرة
- سؤالُ السكان المحليين والكهنة والتجار عن أحداثٍ شهدوها أو عرفوها
- مثالٌ: قصّتُه عن بناء الجسور على نهر الدانوب — سألَ المحاربين والهندسيين مباشرة

### فحصُ الروايات المتضاربة
- لا يرفع نسبة إذا تعارضت الروايات، بل يسجّل كلاهما ويترك للقارئ الحكم
- «أنا مُجرّدُ ناقلٍ، لا حاكمٍ» — موقفُ تحفّظيٍّ متقدّمٌ على عصره

### الجغرافياُ والإثنوغرافيا كمصادر
- وصفُ الأراضي والأمم بتفصيلٍ يسعى إلى الدقّة (وإن أخطأ أحياناً)
- فهمُ الماضي عبر فهم الجغرافيا والثقافات المحليّة

## الإنجازات والنقد

### الإيجابياتُ
- تأسيسُ فكرة **نقد المصادر الشفاهية** ومقارنتها
- رفعُ التاريخ من الفن الحكائي إلى سعيٍ منهجيٍّ للحقيقة
- حفظُ شهادات عن حروب فارسية لولاه لضاعت

### النقدُ التاريخيّ اللاحق
- حشوُ الأخبار الخرافية والغريبة من غير تمييزٍ دقيق (حيواناتٌ ضخمة، معاجزُ)
- إعادةُ سردٍ غير نقديةٍ لقصصٍ شعبيةٍ تسمّعها من الكهنة
- اتّهاماتٌ (منذ اليونان نفسها) بالاختلاق والتحيّز الأثيني

## المصادرُ

1. Marincola, John. *Authority and Tradition in Ancient Historiography*. Cambridge, 2007.
2. Gould, John P. *Herodotus*. St. Martin's Press, 1989.
3. Lateiner, Donald. *Sardonic Smile: Nonverbal Behavior in Homeric Epic*. U Michigan Press, 1995.
4. Dewald, Carolyn, & Marincola, John (eds.). *The Cambridge Companion to Herodotus*. Cambridge, 2006.

## الروابط

- Related: `sch-greco-roman-historiography`
- Related: `sch-oral-history-modern-method`
- Related: `con-witness-testimony-antiquity`
- Related: `con-source-criticism-origins`
"""
    }
]

def create_thinker_node(data: Dict) -> str:
    """Create a thinker node in markdown format."""
    node_id = get_next_id("THK")

    frontmatter = f"""---
slug: "{data['slug']}"
id: "{node_id}"
type: "thinker"
part: "historiography"
level: "متقدم"
title: "{data['title']}"
en: "{data['en']}"
dates: "{data['dates']}"
crumb: "historiography"
active_start: null
active_end: null
cultural_origin: null
edges: []
related: []
gaps: []
---

"""

    return frontmatter + data['content']

def save_node(filename: str, content: str, directory: Path) -> Path:
    """Save node to file."""
    directory.mkdir(parents=True, exist_ok=True)
    filepath = directory / f"{filename}.md"
    filepath.write_text(content, encoding='utf-8')
    return filepath

# Generate first thinker node
if __name__ == "__main__":
    for thinker in ANCIENT_HISTORIANS:
        content = create_thinker_node(thinker)
        filepath = save_node(thinker['slug'], content, THINKERS_PATH)
        print(f"✓ Created: {filepath}")
