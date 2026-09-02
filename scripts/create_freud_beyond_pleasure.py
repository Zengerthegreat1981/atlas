#!/usr/bin/env python3
"""
create_freud_beyond_pleasure.py
Creates canonical work node for Freud's 'Beyond the Pleasure Principle'.
"""

from atlas_content_generator import write_node

write_node("works", "wrk-freud-beyond-pleasure-principle",
    {"type": "عمل / كتاب", "part": "psychology", "level": "متقدم",
     "title": "ما وراء مبدأ اللذة",
     "en": "Beyond the Pleasure Principle by Sigmund Freud",
     "crumb": "التحليل النفسي ونظرية الغرائز ← أمهات الكتب ← ما وراء مبدأ اللذة"},
    "الكتاب النظري الثوري لسيغموند فرويد (1920) الذي أعاد فيه صياغة نظريته في الغرائز جذرياً؛ مقدماً لأول مرة مفهوم «غريزة الموت والهدام» (Todestrieb / Thanatos) ومفسراً ظاهرة قهر التكرار وأحلام صدمات الحروب.",
    [("تفكيك سيادة مبدأ اللذة المطلقة", "اكتشاف أن الجهاز النفسي لا يسعى فقط لخفض التوتر وجلب اللذة، بل تدفعه قوى قهرية لتكرار التجارب المؤلمة والصادمة في محاولة للسيطرة عليها."),
     ("ثنائية إيروس وثاناتوس", "صياغة الصراع الوجودي الأكبر بين «إيروس» (غريزة الحياة والحب والبناء) و«ثاناتوس» (غريزة الموت والتفكيك والعودة للجماد)."),
     ("الأثر في الطب النفسي وعلاج الصدمات", "أرسى الأساس لفهم اضطراب ما بعد الصدمة (PTSD) وسلوكيات إيذاء الذات القهرية.")],
    [("belongs_to", "sch-psychoanalysis", "مدرسة")],
    [("thk-freud", "سيغموند فرويد", "مفكر"), ("trm-todestrieb-death-drive", "غريزة الموت", "مصطلح")])

print("Created Freud's Beyond the Pleasure Principle work node.")
