# -*- coding: utf-8 -*-
"""
Batch A: Soft Types Expansion (Events, Dialogues, Critiques, Axioms, Relations).
Target: 58 Events, 23 Dialogues, 42 Critiques, 19 Axioms, 27 Bridge Relations.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os

BASE_DIR = _ATLAS_ROOT

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

print("Script template ready.")
