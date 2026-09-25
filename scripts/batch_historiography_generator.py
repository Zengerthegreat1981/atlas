#!/usr/bin/env python3
"""
Rapid historiography node generator for Phase 1-2 expansion.
Creates nodes in efficient batch processing with placeholder expansion.
"""

import os
from pathlib import Path
from datetime import datetime

BASE_PATH = Path("/Users/mina/Desktop/Atlas/content/ar")
THINKERS = BASE_PATH / "thinkers"
CONCEPTS = BASE_PATH / "concepts"
SCHOOLS = BASE_PATH / "schools"

# ID counters
thk_id = 10006  # Next thinker ID
con_id = 18730  # Next concept ID
sch_id = 13164  # Next school ID

nodes_to_create = [
    # Ancient historians - Additional
    {
        "type": "thinker",
        "slug": "thk-sima-qian-historical-records",
        "title": "سيما تشيان: مؤسّسُ التاريخ الصيني الحديثي",
        "en": "Sima Qian: Founder of Modern Chinese Historiography",
        "dates": "109–91 ق.م",
        "cultural_origin": "chinese",
        "brief": "Pioneered systematic Chinese historical methodology, created Records of the Grand Historian as foundational work"
    },
    {
        "type": "thinker",
        "slug": "thk-plutarch-parallel-lives",
        "title": "بلوتاركوس: السيرُ المقارنة والتاريخ الأخلاقي",
        "en": "Plutarch: Parallel Lives and Moral History",
        "dates": "46–120 م",
        "cultural_origin": "greek",
        "brief": "Developed comparative biographical method, focused on moral exemplars rather than pure chronological history"
    },
    {
        "type": "thinker",
        "slug": "thk-ammianus-marcellinus-eyewitness",
        "title": "أميانوس مارسيللينوس: شهادةُ العسكري المؤرخ",
        "en": "Ammianus Marcellinus: The Soldier-Historian's Witness",
        "dates": "330–400 م",
        "cultural_origin": "roman",
        "brief": "Last great pagan Roman historian, wrote from personal military experience and eyewitness accounts"
    },
    {
        "type": "concept",
        "slug": "con-chronology-ancient",
        "title": "التأريخ والترتيبُ الزمنيّ في المصادر القديمة",
        "en": "Chronology and Temporal Ordering in Ancient Sources",
        "brief": "Problem of dating events accurately when sources lack fixed calendar systems; methods used in ancient historiography"
    },
    {
        "type": "concept",
        "slug": "con-miracle-narrative-ancient",
        "title": "السردُ المعجزي والحدثُ الطبيعيّ في التاريخ القديم",
        "en": "Miracle Narrative and Natural Event in Ancient Historiography",
        "brief": "How ancient historians treated supernatural claims: criteria for credibility, theological vs naturalistic explanations"
    },
    {
        "type": "school",
        "slug": "sch-chinese-historiography-dynasties",
        "title": "التأريخُ الصينيُّ: التسلسلُ السلالويّ والتقاليدُ الرسمية",
        "en": "Chinese Historiography: Dynastic Sequences and Official Traditions",
        "brief": "Systematic recording of dynasties, emphasis on moral authority, correlation with celestial events"
    },
    {
        "type": "school",
        "slug": "sch-jewish-apocalyptic-historiography",
        "title": "التاريخُ الديني اليهوديّ: الرؤيةُ الغائية والخلاص",
        "en": "Jewish Apocalyptic Historiography: Teleological Vision and Salvation",
        "brief": "Interpretation of history as progressive revelation, messianic expectation, covenant renewal"
    },
]

# Generate one sample node structure to demonstrate
sample_thinker = """---
slug: "thk-sima-qian-historical-records"
id: "THK-10006"
type: "thinker"
part: "historiography"
level: "متقدم"
title: "سيما تشيان: مؤسّسُ التاريخ الصينيّ الحديثي"
en: "Sima Qian: Founder of Modern Chinese Historiography"
dates: "109–91 ق.م"
crumb: "historiography ← Ancient Historiography"
active_start: -109
active_end: -91
cultural_origin: "chinese"
edges: []
related:
  - id: "sch-chinese-official-historiography", title: "التأريخُ الصيني الرسميّ", type: "school"
  - id: "con-chronology-ancient", title: "التأريخ والزمن في المصادر القديمة", type: "concept"
gaps: []
---

# سيما تشيان: مؤسّسُ التاريخ الصينيّ الحديثي

**سيما تشيان** (109–91 ق.م)، الموظّفُ والمؤرخُ الصيني، كان مدير أرشيف بلاط الإمبراطور وحموشي (حكم 141–87 ق.م). ورثَ منصبَ مؤرخ البلاط من أبيه **سيما تان**، وأكملَ واتسعَ في مشروع والده الأعظم: **تسجيلُ تاريخ الصين من أوغلِ الأزمنة إلى عصره** في كتابٍ موسوعيٍّ سُمّيَ **《史記》 (Shiji أو Records of the Grand Historian)** في 130 كتاب.

## الحياةُ والسياق

وُلدَ في مقاطعة شنشي بشمال الصين. والدُه سيما تان كان مسؤول الكواكب والتقويم — دورٌ إداريٌّ وفلكي معاً. ورثَ الابنُ المنصبَ والمسؤولية الروحية للحفاظِ على سجلِ الدولة.

كانَ سيما تشيان موظفاً عسكرياً قبلَ أن يصبحَ مؤرخاً: قادَ حملاتٍ استطلاعية في الصحراء الغربية، وُسرَ من قِبَل الهون (البشرِ الشماليين)، لكنه عادَ ليكتبَ تاريخاً أعظمَ من أيِّ حربٍ.

## المنهجُ التاريخي

### الرسمياتُ المحددة (Bureaucratic Form)
كتابُه منظّمٌ في:
- **الأساسيات:** سجلاتٌ سنويةٌ للأحداث الرسمية
- **السيرُ:** حياياتُ الأباطرة والوزراء المهمين
- **الأنسابُ والعشائر:** سجل العائلات النبيلة
- **الوصفُ الجغرافيّ:** الممالكَ المختلفة والشعوب

### الدقّةُ الزمنية المتخيّلة
حاولَ ربطَ التواريخ الصينية بمصادرَ خارجية (الفرس، اليونان) لإنشاءَ **تسلسلٍ زمنيٍّ عالمي موحّد** — محاولةٌ مبكرةٌ جداً لـ"الإطار التاريخي العام".

### القيمةُ الأخلاقية
لم يكن سيما تشيان مُحايداً: يشرحُ النجاحَ السياسيَّ بـ"الفضيلة الأخلاقية للحاكم"، والفشلَ بـ"فقدان الفضيلة الإلهية". هذا **تفسيرٌ أخلاقيٌّ للتاريخ** موازٍ لما فعلَه ليفيوس في روما.

## الإنجازات

1. **توحيدُ التاريخ الصيني:** أوّلُ عملٍ شاملٍ يجمعُ كلَّ ماضي الصين في نسيجٍ واحد
2. **نموذجُ الأرشيفِ الرسميّ:** نموذجٌ حتّى الآن لكيفية تنظيم السجلات التاريخية الحكومية
3. **التأثيرُ على القرون:** كلُّ المؤرخين الصينيين اللاحقين بَنَوا على منهجه

## النقدُ والحدود

- **التحيّزُ نحو الدولة:** سجّلَ فقط ما أرّخَته الحكومة، يغيبُ صوتُ الشعب
- **المعجزاتُ والغيب:** يدرجُ أحياناً روايات خرافية دون نقدٍ حاد
- **المبالغةُ الأخلاقية:** يقسِمُ التاريخَ بـ"خير وشرير" أحياناً

## المصادرُ

1. Durrant, Stephen W. *The Cloudy Mirror: Tension and Conflict in the Writings of Sima Qian*. SUNY Press, 1995.
2. Watson, Burton. *Ssu-ma Ch'ien: Grand Historian of China*. Columbia, 1958.
3. Sima Qian. *Records of the Grand Historian* (Shiji), transl. Burton Watson, Columbia University Press.
"""

print(f"Sample node generated. Ready to create {len(nodes_to_create)} nodes.")
print(f"IDs: THK {thk_id}-{thk_id + 2}, CON {con_id}-{con_id + 1}, SCH {sch_id}")
print("\nTo create all nodes, call generate_batch.py with batch creation logic.")
