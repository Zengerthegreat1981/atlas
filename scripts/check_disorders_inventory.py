# -*- coding: utf-8 -*-
"""
Detailed audit of all items in disorders-full-coverage-backlog.md
"""

import os
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
BACKLOG_PATH = os.path.join(ROOT_DIR, "agents_specs/disorders-full-coverage-backlog.md")
DISORDERS_DIR = os.path.join(ROOT_DIR, "content/ar/disorders")

app_files = set(os.listdir(DISORDERS_DIR))

with open(BACKLOG_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

present = []
missing = []

for line in lines:
    m = re.search(r'- \[( |~|x)\] (.*?) — `([^`]+)`', line)
    if m:
        status, name, slug = m.groups()
        fname = slug + ".md"
        # check if fname exists
        if fname in app_files:
            present.append((slug, name))
        else:
            # check alias (e.g. dis-borderline-personality -> dis-bpd.md)
            if slug == "dis-borderline-personality" and "dis-bpd.md" in app_files:
                present.append((slug, name + " (as dis-bpd.md)"))
            else:
                missing.append((slug, name))

print(f"Total present: {len(present)}")
print(f"Total missing: {len(missing)}")
for s, n in missing:
    print(f"Missing: {s} -> {n}")
