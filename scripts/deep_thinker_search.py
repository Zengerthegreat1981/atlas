# -*- coding: utf-8 -*-
"""
Inspect all thinkers in the repository (approved and drafts)
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import glob
import re

ROOT_DIR = _ATLAS_ROOT

thinker_files = glob.glob(os.path.join(ROOT_DIR, "content/ar/thinkers/*.md")) + \
                glob.glob(os.path.join(ROOT_DIR, "content/ar/drafts/thinkers/*.md"))

all_thinkers = {}
for tf in thinker_files:
    slug = os.path.basename(tf)[:-3]
    with open(tf, "r", encoding="utf-8") as f:
        content = f.read()
    title_m = re.search(r'title:\s*\"([^\"]+)\"', content)
    en_m = re.search(r'en:\s*\"([^\"]+)\"', content)
    title = title_m.group(1).strip() if title_m else ""
    en = en_m.group(1).strip() if en_m else ""
    all_thinkers[slug] = {
        "slug": slug,
        "title": title,
        "en": en,
        "file": tf
    }

print("Total thinkers loaded: " + str(len(all_thinkers)))

target_names = [
    ("ستانلي ميلغرام", "Stanley Milgram"),
    ("سولومون آش", "Solomon Asch"),
    ("فيليب زيمباردو", "Philip Zimbardo"),
    ("مظفر شريف", "Muzafer Sherif"),
    ("تشارلز هوفلينغ", "Charles Hofling"),
    ("ليون فستنجر", "Leon Festinger"),
    ("لي روس", "Lee Ross"),
    ("إدوارد إي. جونز", "Edward Jones"),
    ("روبرت روزنتال", "Robert Rosenthal"),
    ("هنري تاجفيل", "Henri Tajfel"),
    ("تشارلز لورد", "Charles Lord"),
    ("بيب لاتانيه", "Bibb Latane"),
    ("جون دارلي", "John Darley"),
    ("نورمان تريبليت", "Norman Triplett"),
    ("ماكس رينغلمان", "Max Ringelmann"),
    ("دانيال باتسون", "Daniel Batson"),
    ("إيفان بافلوف", "Ivan Pavlov"),
    ("جون ب. واطسون", "John Watson"),
    ("ب. ف. سكينر", "B. F. Skinner"),
    ("إدوارد ثورندايك", "Edward Thorndike"),
    ("جون جارسيا", "John Garcia"),
    ("روبرت ريسكورلا", "Robert Rescorla"),
    ("هاري هارلو", "Harry Harlow"),
    ("ماري أينسورث", "Mary Ainsworth"),
    ("جون بولبي", "John Bowlby"),
    ("ماري مين", "Mary Main"),
    ("مارشال كلاوس", "Marshall Klaus"),
    ("جان بياجيه", "Jean Piaget"),
    ("باربل إنهيلدر", "Barbel Inhelder"),
    ("جوزيف بيرنر", "Josef Perner"),
    ("رينيه بايارغيون", "Renee Baillargeon"),
    ("أديل دايموند", "Adele Diamond"),
    ("هيرمان إبنغهاوس", "Hermann Ebbinghaus"),
    ("فريدريك بارتليت", "Frederic Bartlett"),
    ("جورج سبيرلينج", "George Sperling"),
    ("جورج أ. ميلر", "George Miller"),
    ("لويد بيترسون", "Lloyd Peterson"),
    ("فيرغوس كريك", "Fergus Craik"),
    ("إندل تولفينغ", "Endel Tulving"),
    ("إليزابيث لوفتوس", "Elizabeth Loftus"),
    ("جاكلين بيكريل", "Jacqueline Pickrell"),
    ("هنري روديغر", "Henry Roediger"),
    ("مارسيا جونسون", "Marcia Johnson"),
    ("إيرا هايمان", "Ira Hyman"),
    ("روجر سبيري", "Roger Sperry"),
    ("مايكل غازانيغا", "Michael Gazzaniga"),
    ("بريندا ميلنر", "Brenda Milner"),
    ("ديفيد هوبل", "David Hubel"),
    ("بنجامين ليبيت", "Benjamin Libet"),
    ("بول بروكا", "Paul Broca"),
    ("ألبرت باندورا", "Albert Bandura"),
    ("أندرو ميلتزوف", "Andrew Meltzoff"),
    ("روس باركي", "Ross Parke"),
    ("مارتن سليجمان", "Martin Seligman"),
    ("ستيفن ماير", "Steven Maier"),
    ("دونالد هيروتو", "Donald Hiroto"),
    ("كريستوفر بيترسون", "Christopher Peterson"),
    ("إلين لانغر", "Ellen Langer"),
    ("كارول دويك", "Carol Dweck"),
    ("ديفيد روزنهان", "David Rosenhan"),
    ("أميريغو فارينا", "Amerigo Farina"),
    ("بروس لينك", "Bruce Link"),
    ("موريس تيميرلين", "Maurice Temerlin"),
    ("روث بيريندا", "Ruth Berenda"),
    ("فيليب كوستانزو", "Philip Costanzo"),
    ("جيمس كولمان", "James Coleman"),
    ("كينيث كلارك", "Kenneth Clark"),
    ("مامي فيبس كلارك", "Mamie Clark"),
    ("تشارلز نيلسون", "Charles Nelson"),
    ("وودبيرن هيرون", "Woodburn Heron"),
    ("دونالد هيب", "Donald Hebb"),
    ("مارك روزنزفايج", "Mark Rosenzweig"),
    ("ماريان دياموند", "Marian Diamond"),
    ("سوزان كيرتس", "Susan Curtiss"),
    ("إريك لينبرغ", "Eric Lenneberg"),
    ("جون سي. ليلي", "John Lilly"),
    ("ألفريد بينيه", "Alfred Binet"),
    ("لويس تيرمان", "Lewis Terman"),
    ("ديفيد وكسلر", "David Wechsler"),
    ("جون سي. رافن", "John Raven"),
    ("ريتشارد وودكوك", "Richard Woodcock"),
    ("ستارك هاثاواي", "Starke Hathaway"),
    ("بول كوستا", "Paul Costa"),
    ("روبرت ماكري", "Robert McCrae"),
    ("ريموند كاتل", "Raymond Cattell"),
    ("هانز آيزنك", "Hans Eysenck"),
    ("إيزابيل بريجز مايرز", "Isabel Myers"),
    ("كارل غوستاف يونغ", "Carl Jung"),
    ("كيبوم لي", "Kibeom Lee"),
    ("مايكل أشتون", "Michael Ashton"),
    ("هيرمان رورشاخ", "Hermann Rorschach"),
    ("جون إكسنر", "John Exner"),
    ("هنري موراي", "Henry Murray"),
    ("كريستيانا مورغان", "Christiana Morgan"),
    ("جون باك", "John Buck"),
    ("جوليان روتر", "Julian Rotter"),
    ("كارين ماكوفر", "Karen Machover"),
    ("آرون بيك", "Aaron Beck"),
    ("كورت كرونكي", "Kurt Kroenke"),
    ("روبرت سبيتزر", "Robert Spitzer"),
    ("ماكس هاملتون", "Max Hamilton"),
    ("لينور رادلوف", "Lenore Radloff"),
    ("واين غودمان", "Wayne Goodman"),
    ("فرانك ويذرز", "Frank Weathers"),
    ("إدنا فوا", "Edna Foa"),
    ("دانيال فايس", "Daniel Weiss"),
    ("ماردي هورويتز", "Mardi Horowitz"),
    ("لوريتا بندر", "Lauretta Bender"),
    ("رالف ريتان", "Ralph Reitan"),
    ("روبرت هيتون", "Robert Heaton"),
    ("جيه. ريدلي ستروب", "Ridley Stroop"),
    ("زياد نصر الدين", "Ziad Nasreddine"),
    ("مارشال فولستين", "Marshal Folstein"),
    ("توماس أشنباخ", "Thomas Achenbach"),
    ("إدغار دول", "Edgar Doll"),
    ("سارة سبارو", "Sara Sparrow"),
    ("سي. كيث كونرز", "Keith Conners"),
    ("وليام فرانكنبرغ", "William Frankenburg"),
    ("روبرت غودمان", "Robert Goodman"),
    ("كارول جورج", "Carol George"),
    ("فيليب شيفر", "Phillip Shaver"),
    ("كيم بارثولوميو", "Kim Bartholomew"),
    ("ليونارد هوروفيتز", "Leonard Horowitz"),
    ("غراهام سبانير", "Graham Spanier"),
    ("مارك غرينبيرغ", "Mark Greenberg"),
    ("إد دينر", "Ed Diener"),
    ("روبرت إيمونز", "Robert Emmons"),
    ("ديفيد واتسون", "David Watson"),
    ("مايكل أرجايل", "Michael Argyle"),
    ("كارول ريف", "Carol Ryff"),
    ("سارة ستيوارت-براون", "Sarah Stewart-Brown")
]

found_matches = []
for ar_name, en_name in target_names:
    matches = []
    en_last = en_name.split()[-1].lower() if en_name else ""
    ar_last = ar_name.split()[-1] if ar_name else ""
    for slug, t in all_thinkers.items():
        if (ar_name in t['title']) or (t['title'] and t['title'] in ar_name) or \
           (en_name.lower() in t['en'].lower()) or (t['en'] and t['en'].lower() in en_name.lower()):
            matches.append(t)
        elif en_last and len(en_last) > 3 and (slug == "thk-" + en_last or slug.endswith("-" + en_last)):
            matches.append(t)
    if matches:
        found_matches.append((ar_name, en_name, matches))

print("================ FOUND THINKER MATCHES (" + str(len(found_matches)) + ") ================")
for ar_name, en_name, matches in found_matches:
    for m in matches:
        print("Target: '" + ar_name + "' / '" + en_name + "' -> Slug: `" + m['slug'] + "` | Title: '" + m['title'] + "' | EN: '" + m['en'] + "'")
