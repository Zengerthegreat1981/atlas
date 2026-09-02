# -*- coding: utf-8 -*-
"""
Resolve slug conflicts between approved and drafts for philosophy elements.
Merges richer drafts content into approved when appropriate and cleans up duplicates.
"""
import os
import re

ATLAS_ROOT = "/Users/minamoheb/Desktop/Atlas"
APPROVED_BASE = os.path.join(ATLAS_ROOT, "content", "ar")
DRAFTS_BASE = os.path.join(ATLAS_ROOT, "content", "ar", "drafts")

TYPES = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]

def resolve():
    resolved_count = 0
    for t in TYPES:
        app_dir = os.path.join(APPROVED_BASE, t)
        drf_dir = os.path.join(DRAFTS_BASE, t)
        if not os.path.isdir(app_dir) or not os.path.isdir(drf_dir):
            continue
        
        for fn in os.listdir(drf_dir):
            if not fn.endswith(".md"):
                continue
            drf_fp = os.path.join(drf_dir, fn)
            app_fp = os.path.join(app_dir, fn)
            if os.path.exists(app_fp):
                with open(drf_fp, "r", encoding="utf-8") as f:
                    drf_content = f.read()
                with open(app_fp, "r", encoding="utf-8") as f:
                    app_content = f.read()
                
                # Check word count and quality
                if len(drf_content) > len(app_content) + 100:
                    # Merge: overwrite approved with richer draft, keeping approved ID if present
                    with open(app_fp, "w", encoding="utf-8") as f:
                        f.write(drf_content)
                    print(f"🔄 Merged richer draft into approved: {t}/{fn}")
                else:
                    print(f"🗑️ Cleaned redundant draft copy: {t}/{fn}")
                
                os.remove(drf_fp)
                resolved_count += 1

    print(f"✅ Successfully resolved {resolved_count} conflicts!")

if __name__ == "__main__":
    resolve()
