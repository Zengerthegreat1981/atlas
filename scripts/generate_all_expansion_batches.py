#!/usr/bin/env python3
"""
generate_all_expansion_batches.py
Generates the complete expansion batches for Atlas Content Expansion Plan:
  - Batch 1: The 5 Thin Categories (90 files: metaphors, questions, terms, experiences, contexts)
  - Batch 2: The 18 Sparse Therapy & Cultural Schools (60 files: concepts, techniques, works)
  - Batch 3: Landmark Dialogues (20 files in dialogues/)
  - Batch 4: Landmark Masterworks & Core Debates (40 files: works, debates)
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import sys
from pathlib import Path

ATLAS_ROOT = Path(_ATLAS_ROOT)
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'

def write_node(folder, slug, frontmatter_dict, lede, sections, edges=None, related=None, gaps=None):
    target_dir = CONTENT_AR / folder
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{slug}.md"
    
    fm_lines = [
        "---",
        f'slug: "{slug}"',
        f'id: "[DRAFT-UNKNOWN]"',
        f'type: "{frontmatter_dict.get("type", "مفهوم")}"',
        f'part: "{frontmatter_dict.get("part", "philosophy")}"',
        f'level: "{frontmatter_dict.get("level", "متوسط")}"',
        f'title: "{frontmatter_dict.get("title", "")}"',
        f'en: "{frontmatter_dict.get("en", "")}"',
        f'crumb: "{frontmatter_dict.get("crumb", "")}"',
        f'active_start: {frontmatter_dict.get("active_start", "null")}',
        'active_end: ' + str(frontmatter_dict.get("active_end", '"مستمر"')),
    ]
    
    fm_lines.append("edges:")
    if edges:
        for rel, target, ttype in edges:
            fm_lines.append(f'  - rel: "{rel}", target: "{target}", target_type: "{ttype}"')
    else:
        fm_lines.append("  []")
        
    fm_lines.append("related:")
    if related:
        for rid, rtitle, rtype in related:
            fm_lines.append(f'  - id: "{rid}", title: "{rtitle}", type: "{rtype}"')
    else:
        fm_lines.append("  []")
        
    fm_lines.append("gaps:")
    if gaps:
        for g in gaps:
            fm_lines.append(f'  - "{g}"')
    else:
        fm_lines.append('  - "المصادر الأولية تحتاج مراجعة وتوثيقاً إضافياً."')
        fm_lines.append('  - "توسيع شبكة العلاقات مع المدارس المجاورة قيد المتابعة التحريرية."')
        
    fm_lines.append("---")
    
    body_parts = [f"# {frontmatter_dict.get('title', '')}\n", lede.strip() + "\n"]
    for stitle, sbody in sections:
        body_parts.append(f"## {stitle}\n\n{sbody.strip()}\n")
        
    full_text = "\n".join(fm_lines) + "\n\n" + "\n".join(body_parts)
    target_file.write_text(full_text, encoding="utf-8")
    return slug

print("Generator helper defined.")
