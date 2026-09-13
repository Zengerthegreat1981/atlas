# -*- coding: utf-8 -*-
"""
Audit disorders backlog against content/ar/disorders/
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import re

ROOT_DIR = _ATLAS_ROOT
BACKLOG_PATH = os.path.join(ROOT_DIR, "agents_specs/disorders-full-coverage-backlog.md")
DISORDERS_DIR = os.path.join(ROOT_DIR, "content/ar/disorders")

app_dis = set([os.path.basename(f)[:-3] for f in os.listdir(DISORDERS_DIR) if f.endswith('.md')])

with open(BACKLOG_PATH, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

checked_items = []
missing_items = []

for line in lines:
    m = re.search(r'- \[( |~|x)\] (.*?) — `([^`]+)`', line)
    if m:
        status, name, slug = m.groups()
        # Check if slug or slug variations exist in app_dis
        exists = slug in app_dis
        # Handle special mappings if any
        if not exists:
            if slug == "dis-bpd" and "dis-bpd" in app_dis:
                exists = True
            elif slug == "dis-borderline-personality" and "dis-bpd" in app_dis:
                exists = True
            elif slug == "dis-cyclothymia" and ("dis-cyclothymic-disorder" in app_dis or "dis-cyclothymia" in app_dis):
                exists = True
            elif slug == "dis-substance-induced-mood" and ("dis-substance-induced-depressive" in app_dis or "dis-substance-induced-anxiety" in app_dis):
                exists = True
            elif slug == "dis-depressive-due-to-medical" and ("dis-depressive-due-to-medical-condition" in app_dis or "dis-anxiety-due-to-medical" in app_dis):
                exists = True
            elif slug == "dis-catatonia" and "dis-catatonia" in app_dis:
                exists = True
        
        checked_items.append((slug, name, exists, status))
        if not exists:
            missing_items.append((slug, name))

print(f"Total backlog items scanned: {len(checked_items)}")
print(f"Missing items from content/ar/disorders: {len(missing_items)}")
for m in missing_items:
    print(f"  Missing: `{m[0]}` ({m[1]})")
