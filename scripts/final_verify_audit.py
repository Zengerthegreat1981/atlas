# -*- coding: utf-8 -*-
"""
Final Verification Script for Cross-Link Audit
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import re

ROOT_DIR = _ATLAS_ROOT
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

valid_slugs = set()
for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "content/ar")):
    for f in files:
        if f.endswith(".md") and not f.startswith("EXISTING_SLUGS") and not f.startswith("PATCH_") and not f.startswith("MASTER_"):
            valid_slugs.add(f[:-3])

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
all_files = study_files + instrument_files

errors = []
related_thinkers_count = 0

for fpath in all_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check frontmatter
    if not content.startswith("---"):
        errors.append(f"{fname}: Missing frontmatter start")
        
    parts = content.split("---")
    if len(parts) < 3:
        errors.append(f"{fname}: Broken frontmatter")
        continue
        
    fm = parts[1]
    
    # Check related format
    if "related:" in fm:
        for line in fm.splitlines():
            if line.strip().startswith("- id:"):
                m = re.match(r'^\s*-\s*id:\s*\"([^\"]+)\",\s*title:\s*\"([^\"]+)\",\s*type:\s*\"([^\"]+)\"$', line)
                if not m:
                    errors.append(f"{fname}: Invalid related format -> {line}")
                else:
                    rel_id = m.group(1)
                    rel_type = m.group(3)
                    if rel_id not in valid_slugs:
                        errors.append(f"{fname}: Phantom slug in related -> {rel_id}")
                    if rel_type == "مفكر":
                        related_thinkers_count += 1

print(f"Total files checked: {len(all_files)}")
print(f"Total related thinker links in target files: {related_thinkers_count}")

if errors:
    print("Errors found:")
    for e in errors:
        print(" - " + e)
else:
    print("✅ 100% CLEAN: All files, frontmatters, single-line related links, and valid slugs verified successfully!")
