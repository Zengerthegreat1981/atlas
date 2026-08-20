# -*- coding: utf-8 -*-
"""
Inspect all 122 draft files' unverified links completely.
"""

import os
import glob
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")

study_files = sorted(glob.glob(os.path.join(STUDIES_DIR, "*.md")))
instrument_files = sorted(glob.glob(os.path.join(INSTRUMENTS_DIR, "*.md")))
target_files = study_files + instrument_files

for fpath in target_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "## أفكار روابط لم تُتحقق" in content:
        section = content.split("## أفكار روابط لم تُتحقق")[1].strip()
        lines = [l.strip() for l in section.splitlines() if l.strip().startswith("- ")]
        print(f"File: {fname}")
        for l in lines:
            print(f"   {l}")
