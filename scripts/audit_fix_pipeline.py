# -*- coding: utf-8 -*-
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os
import glob
from collections import defaultdict

BASE_DIR = _ATLAS_ROOT

def clean_val(v):
    return v.strip().strip('"').strip("'")

def parse_all_slugs():
    files = glob.glob(os.path.join(BASE_DIR, "content/ar/drafts/*/*.md")) + glob.glob(os.path.join(BASE_DIR, "content/ar/*/*.md"))
    slug_map = {}
    for p in files:
        try:
            with open(p, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            continue
        if not lines or not lines[0].startswith("---"):
            continue
        for line in lines[1:]:
            if line.startswith("---"):
                break
            line_str = line.strip()
            if line_str.startswith("slug:"):
                slug = clean_val(line_str.split("slug:", 1)[1])
                if slug:
                    slug_map[slug] = p
    return slug_map

if __name__ == "__main__":
    slug_map = parse_all_slugs()
    print("Found total slugs: " + str(len(slug_map)))
