# -*- coding: utf-8 -*-
"""
Search all thinkers in EXISTING_SLUGS.md
"""

import re

EXISTING_SLUGS_PATH = "content/ar/drafts/EXISTING_SLUGS.md"

all_thinkers = []
with open(EXISTING_SLUGS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        m = re.match(r'- `(thk-[^`]+)` — ([^—]+) —', line)
        if m:
            slug = m.group(1).strip()
            title = m.group(2).strip()
            all_thinkers.append((slug, title))

print(f"Total thinkers in EXISTING_SLUGS.md: {len(all_thinkers)}")

# Let's list some thinkers and see if there are matches for our authors
search_terms = [
    "بيك", "بياجيه", "ميلغرام", "زيمباردو", "بافلوف", "سكينر", "ثورندايك", "هارلو",
    "أينسورث", "فستنجر", "سليجمان", "سليغمان", "روزنهان", "لوفتوس", "سبيري", "غازانيغا",
    "بروكا", "إبنغهاوس", "بارتليت", "رافن", "وكسلر", "بينيه", "تيرمان", "رورشاخ",
    "موراي", "هاملتون", "غودمان", "فوا", "روتر", "ماكوفر", "كوستا", "ماكري",
    "كاتل", "آيزنك", "دينر", "ريف", "أرجايل", "بندر", "كونرز", "سبارو",
    "دول", "نصر الدين", "فولستين", "كولمان", "كلارك", "دويك", "لانغر", "باتسون",
    "دارلي", "لاتانيه", "تاجفيل", "شريف", "روس", "جونز", "روزنتال", "كريك",
    "تولفينغ", "ميلر", "سبيرلينج", "بيترسون", "ليبيت", "ميلنر", "هوبل", "فيزل",
    "واطسون", "جارسيا", "كامين", "ريسكورلا", "نيلسون", "بيكستون", "هيرون", "هيب",
    "روزنزفايج", "دياموند", "كيرتس", "لينبرغ", "ليلي", "فارينا", "لينك", "تيميرلين",
    "بيريندا", "كوستانزو", "شو", "إنهيلدر", "بيرنر", "فيمر", "بايارغيون", "ميلتزوف",
    "مور", "والترز", "باركي", "ماير", "هيروتو", "رودين", "هوفلينغ", "لورد",
    "ليبر", "هايمان", "بيكريل", "روديغر", "ماكديرموت", "جونسون", "وودكوك", "مايرز",
    "بريجز", "أشتون", "كابلان", "جورج", "شيفر", "بارثولوميو", "هوروفيتز", "سبانير",
    "أرمسدن", "غرينبيرغ", "إيمونز", "لارسن", "تيليغن", "هيلز", "تينانت", "كرونكي",
    "رادلوف", "ويذرز", "مارمار", "فايس", "ريتان", "يونغ", "سبيتزر", "أشنباخ", "آش", "باندورا", "بولبي"
]

found = {}
for term in search_terms:
    matches = [t for t in all_thinkers if term in t[1] or term in t[0]]
    if matches:
        found[term] = matches

print(f"Terms found in EXISTING_SLUGS: {len(found)} out of {len(search_terms)}")
for term, matches in found.items():
    print(f"Term '{term}': {matches}")
