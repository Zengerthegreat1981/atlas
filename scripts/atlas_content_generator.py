#!/usr/bin/env python3
"""
atlas_content_generator.py
Clean, robust generator module for Atlas content expansion nodes.
"""

import os
from pathlib import Path

ATLAS_ROOT = Path('/Users/minamoheb/Desktop/Atlas')
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'

def write_node(folder, slug, fm, lede, sections, edges=None, related=None, gaps=None):
    p = CONTENT_AR / folder / f"{slug}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    
    slug_val = slug
    type_val = fm.get("type", "مفهوم")
    part_val = fm.get("part", "philosophy")
    level_val = fm.get("level", "متوسط")
    title_val = fm.get("title", "")
    en_val = fm.get("en", "")
    crumb_val = fm.get("crumb", "")
    start_val = fm.get("active_start", "null")
    end_val = fm.get("active_end", '"مستمر"')
    
    lines = [
        "---",
        f'slug: "{slug_val}"',
        'id: "[DRAFT-UNKNOWN]"',
        f'type: "{type_val}"',
        f'part: "{part_val}"',
        f'level: "{level_val}"',
        f'title: "{title_val}"',
        f'en: "{en_val}"',
        f'crumb: "{crumb_val}"',
        f'active_start: {start_val}',
        f'active_end: {end_val}',
    ]
    lines.append("edges:")
    if edges:
        for rel, target, ttype in edges:
            lines.append(f'  - rel: "{rel}", target: "{target}", target_type: "{ttype}"')
    else:
        lines.append("  []")
    lines.append("related:")
    if related:
        for rid, rtitle, rtype in related:
            lines.append(f'  - id: "{rid}", title: "{rtitle}", type: "{rtype}"')
    else:
        lines.append("  []")
    lines.append("gaps:")
    if gaps:
        for g in gaps:
            lines.append(f'  - "{g}"')
    else:
        lines.append('  - "المصادر الأولية تحتاج مراجعة وتوثيقاً إضافياً."')
        lines.append('  - "توسيع شبكة العلاقات مع المدارس المجاورة قيد المتابعة التحريرية."')
    lines.append("---")
    
    body = [f"# {title_val}", "", lede.strip(), ""]
    for stitle, sbody in sections:
        body.append(f"## {stitle}\n\n{sbody.strip()}\n")
        
    p.write_text("\n".join(lines) + "\n\n" + "\n".join(body), encoding="utf-8")
    return p
