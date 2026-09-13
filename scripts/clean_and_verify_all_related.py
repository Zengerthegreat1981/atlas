# -*- coding: utf-8 -*-
"""
Validate and clean up all related: entries in all 122 study and instrument drafts.
Ensures every related entry has a valid existing slug, is formatted on a single line,
and removes any stray phantom comment lines.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import re
import subprocess

ROOT_DIR = _ATLAS_ROOT
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
EXISTING_SLUGS_PATH = os.path.join(ROOT_DIR, "content/ar/drafts/EXISTING_SLUGS.md")

NL = chr(10)

# Build valid slug set from all actual files in content/ar
valid_slugs = set()
for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "content/ar")):
    for f in files:
        if f.endswith(".md") and not f.startswith("EXISTING_SLUGS") and not f.startswith("PATCH_") and not f.startswith("MASTER_"):
            valid_slugs.add(f[:-3])

print("Total valid slugs in content/ar: " + str(len(valid_slugs)))

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
all_files = study_files + instrument_files

cleaned_files = 0

for fpath in all_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "---" not in content:
        continue
        
    parts = content.split("---")
    if len(parts) < 3:
        continue
        
    frontmatter = parts[1]
    body = "---".join(parts[2:])
    
    fm_lines = frontmatter.splitlines()
    new_fm_lines = []
    in_related = False
    valid_related_entries = []
    
    for line in fm_lines:
        if line.strip() == "related: []":
            new_fm_lines.append("related: []")
            continue
            
        if line.strip() == "related:":
            in_related = True
            continue
            
        if in_related:
            if line.strip().startswith("- id:"):
                # Parse entry
                m = re.match(r'\s*-\s*id:\s*\"([^\"]+)\",\s*title:\s*\"([^\"]+)\",\s*type:\s*\"([^\"]+)\"', line)
                if m:
                    rel_id = m.group(1).strip()
                    rel_title = m.group(2).strip()
                    rel_type = m.group(3).strip()
                    
                    if rel_id in valid_slugs:
                        valid_related_entries.append('  - id: "' + rel_id + '", title: "' + rel_title + '", type: "' + rel_type + '"')
                    else:
                        print("  [" + fname + "] Dropping invalid/phantom slug: " + rel_id)
            elif line.strip().startswith("gaps:") or line.strip().startswith("edges:") or (line.strip() and not line.startswith(" ") and not line.startswith("-")):
                # End of related block
                in_related = False
                # Append related block
                if valid_related_entries:
                    new_fm_lines.append("related:")
                    new_fm_lines.extend(valid_related_entries)
                else:
                    new_fm_lines.append("related: []")
                new_fm_lines.append(line)
            else:
                # Stray lines or comment lines in related, ignore
                continue
        else:
            new_fm_lines.append(line)
            
    if in_related: # if related was at end of frontmatter
        if valid_related_entries:
            new_fm_lines.append("related:")
            new_fm_lines.extend(valid_related_entries)
        else:
            new_fm_lines.append("related: []")

    new_frontmatter = NL.join(new_fm_lines)
    new_full_content = "---" + new_frontmatter + "---" + body
    
    if new_full_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_full_content)
        cleaned_files += 1
        print("Fixed frontmatter in: " + fname)

print("Total files with frontmatter fixed: " + str(cleaned_files))

# Rebuild index
cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_slug_index.py")]
res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
print("build_slug_index: " + res.stdout.strip())
