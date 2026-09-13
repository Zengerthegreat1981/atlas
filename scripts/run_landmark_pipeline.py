#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Landmark Studies and Instruments Pipeline Execution Script
Executes all 23 categories in studies-instruments-backlog.md
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import sys
import subprocess
from datetime import datetime

ROOT_DIR = _ATLAS_ROOT
BACKLOG_PATH = os.path.join(ROOT_DIR, "agents_specs/studies-instruments-backlog.md")
LOG_PATH = os.path.join(ROOT_DIR, "agents_specs/pipeline-progress-log.md")
LISTS_DIR = os.path.join(ROOT_DIR, "agents_specs/encyclopedia-lists")
DRAFTS_STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
DRAFTS_INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

os.makedirs(LISTS_DIR, exist_ok=True)
os.makedirs(DRAFTS_STUDIES_DIR, exist_ok=True)
os.makedirs(DRAFTS_INSTRUMENTS_DIR, exist_ok=True)

def run_build_slug_index():
    cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_slug_index.py")]
    res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running build_slug_index: {res.stderr}")
    else:
        print("build_slug_index ran successfully.")

print("Directories verified.")
