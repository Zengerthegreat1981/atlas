# -*- coding: utf-8 -*-
import os, glob
from collections import defaultdict

BASE_DIR = "/Users/minamoheb/Desktop/Atlas"

drafts = glob.glob(os.path.join(BASE_DIR, "content/ar/drafts/*/*.md"))
approved = glob.glob(os.path.join(BASE_DIR, "content/ar/*/*.md"))

def get_fm(p):
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]
    res = {"path": p}
    for line in fm.splitlines():
        line = line.strip()
        for k in ["slug", "title", "en", "part", "type"]:
            if line.startswith(k + ":"):
                res[k] = line.split(k + ":", 1)[1].strip().strip('"\'')
    return res

all_items = [get_fm(p) for p in drafts + approved if get_fm(p).get("slug")]

for cat in ["schools", "branches", "concepts", "works", "thinkers", "terms", "critiques", "debates", "dialogues", "questions"]:
    items = [x for x in all_items if f"/{cat}/" in x.get("path","")]
    by_en = defaultdict(list)
    for it in items:
        en = it.get("en", "").lower().strip()
        if en:
            by_en[en].append(it)
    dupes_en = {k: v for k, v in by_en.items() if len(v) > 1}
    if dupes_en:
        print("=== DUPES EN in " + cat + " (" + str(len(dupes_en)) + ") ===")
        for k, v in dupes_en.items():
            slugs = [x.get("slug","") + (" [approved]" if "/drafts/" not in x.get("path","") else " [draft]") for x in v]
            print("  EN: '" + k + "' -> " + str(slugs))

    by_ar = defaultdict(list)
    for it in items:
        ar = it.get("title", "").strip()
        if ar:
            by_ar[ar].append(it)
    dupes_ar = {k: v for k, v in by_ar.items() if len(v) > 1}
    if dupes_ar:
        print("=== DUPES AR in " + cat + " (" + str(len(dupes_ar)) + ") ===")
        for k, v in dupes_ar.items():
            slugs = [x.get("slug","") + (" [approved]" if "/drafts/" not in x.get("path","") else " [draft]") for x in v]
            print("  AR: '" + k + "' -> " + str(slugs))
