# -*- coding: utf-8 -*-
"""
Clean up any corrupted phantom strings in frontmatter related: blocks.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import subprocess

ROOT_DIR = _ATLAS_ROOT
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

NL = chr(10)

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
all_files = study_files + instrument_files

cleaned_count = 0
for fpath in all_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '  - "الـphantom slug' in content:
        lines = content.splitlines()
        new_lines = []
        for line in lines:
            if '  - "الـphantom slug' in line:
                cleaned_line = line.split('  - "الـphantom slug')[0].rstrip()
                new_lines.append(cleaned_line)
            else:
                new_lines.append(line)
        new_content = NL.join(new_lines).strip() + NL
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        cleaned_count += 1
        print("Cleaned: " + os.path.basename(fpath))

print("Total files cleaned: " + str(cleaned_count))

cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_slug_index.py")]
res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
print("build_slug_index: " + res.stdout.strip())
