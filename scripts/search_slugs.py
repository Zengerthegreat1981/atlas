# -*- coding: utf-8 -*-
"""
Search for specific thinkers in EXISTING_SLUGS.md
"""

import re

EXISTING_SLUGS_PATH = "content/ar/drafts/EXISTING_SLUGS.md"

queries = [
    "spearman", "سبيرمان",
    "watson", "واتسون", "واطسون",
    "binet", "بينيه",
    "piaget", "بياجيه",
    "milgram", "ميلغرام",
    "zimbardo", "زيمباردو",
    "harlow", "هارلو",
    "ainsworth", "أينسورث", "اينسورث",
    "loftus", "لوفتوس",
    "sperry", "سبيري",
    "gazzaniga", "غازانيغا", "غازانيجا",
    "broca", "بروكا",
    "cattell", "كاتل",
    "eysenck", "آيزنك", "ايزنك",
    "rorschach", "رورشاخ",
    "rotter", "روتر",
    "wechsler", "وكسلر",
    "hamilton", "هاملتون",
    "bender", "بندر",
    "diener", "دينر",
    "ryff", "ريف",
    "sherif", "شريف",
    "coleman", "كولمان",
    "clark", "كلارك",
    "dweck", "دويك",
    "rosenhan", "روزنهان",
    "reitan", "ريتان",
    "hebb", "هيب",
    "curtiss", "كيرتس",
    "lenneberg", "لينبرغ",
    "lilly", "ليلي",
    "farina", "فارينا",
    "link", "لينك",
    "temerlin", "تيميرلين",
    "berenda", "بيريندا",
    "costanzo", "كوستانزو",
    "inhelder", "إنهيلدر", "انهيلدر",
    "perner", "بيرنر",
    "wimmer", "فيمر",
    "baillargeon", "بايارغيون",
    "meltzoff", "ميلتزوف",
    "parke", "باركي",
    "maier", "ماير",
    "hiroto", "هيروتو",
    "hofling", "هوفلينغ",
    "lord", "لورد",
    "hyman", "هايمان",
    "pickrell", "بيكريل",
    "roediger", "روديغر",
    "mcdermott", "ماكديرموت",
    "woodcock", "وودكوك",
    "myers", "مايرز",
    "briggs", "بريجز",
    "ashton", "أشتون", "اشتون",
    "shaver", "شيفر",
    "bartholomew", "بارثولوميو",
    "horowitz", "هوروفيتز",
    "spanier", "سبانير",
    "greenberg", "غرينبيرغ", "غرينبرغ",
    "argyle", "أرجايل", "ارجايل",
    "kroenke", "كرونكي",
    "radloff", "رادلوف",
    "weathers", "ويذرز"
]

all_entries = []
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        m = re.match(r'- `([^`]+)` — ([^—]+) —', line)
        if m:
            all_entries.append((m.group(1).strip(), m.group(2).strip()))

print(f"Total entries in EXISTING_SLUGS.md: {len(all_entries)}")

for q in queries:
    matches = []
    for slug, title in all_entries:
        if q.lower() in slug.lower() or q in title:
            matches.append((slug, title))
    if matches:
        print(f"Match for '{q}': {matches}")
