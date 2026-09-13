# -*- coding: utf-8 -*-
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os, glob
from collections import defaultdict

BASE_DIR = _ATLAS_ROOT

files = glob.glob(os.path.join(BASE_DIR, "content/ar/drafts/*/*.md")) + glob.glob(os.path.join(BASE_DIR, "content/ar/*/*.md"))

slug_to_file = {}
for p in files:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    fm = parts[1]
    for line in fm.splitlines():
        line = line.strip()
        if line.startswith("slug:"):
            slug = line.split("slug:", 1)[1].strip().strip('"\'')
            if slug:
                slug_to_file[slug] = p

all_slugs = set(slug_to_file.keys())
print("Total valid slugs: " + str(len(all_slugs)))

phantoms = defaultdict(list)
for p in files:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    fm = parts[1]
    for line in fm.splitlines():
        line = line.strip()
        if "- id:" in line:
            val = line.split("- id:", 1)[1].strip()
            if "," in val:
                val = val.split(",", 1)[0].strip()
            val = val.strip('"\'')
            if val and val not in all_slugs:
                phantoms[val].append(p)

print("Total unique phantoms: " + str(len(phantoms)))

prefix_counts = defaultdict(int)
for ph in phantoms:
    prefix = ph.split("-")[0] if "-" in ph else "no-prefix"
    prefix_counts[prefix] += 1

for pre, cnt in sorted(prefix_counts.items(), key=lambda x: x[1], reverse=True):
    print("Prefix " + pre + ": " + str(cnt) + " phantoms")

# Let us find exact typo matches
with open("/tmp/phantoms_classified.txt", "w", encoding="utf-8") as out:
    for ph, src_list in sorted(phantoms.items()):
        prefix = ph.split("-")[0] if "-" in ph else ""
        cands = [s for s in all_slugs if (prefix and s.startswith(prefix) and (ph in s or s in ph or ph[4:] == s[4:] or ph.replace("-","") == s.replace("-","")))]
        out.write("PHANTOM: " + ph + " (in " + str(len(src_list)) + " files)\n")
        out.write("  Sources: " + ", ".join([os.path.basename(s) for s in src_list]) + "\n")
        out.write("  Candidates: " + str(cands) + "\n\n")

print("Classified phantoms written to /tmp/phantoms_classified.txt")
