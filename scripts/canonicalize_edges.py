import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os
import re
import json

base = _ATLAS_ROOT + "/content/ar"
slug_set = set()
slug_to_title = {}
title_to_slug = {}
en_to_slug = {}

for root, dirs, files in os.walk(base):
    if "drafts" in root or "_merged" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            slug = f[:-3]
            slug_set.add(slug)
            with open(os.path.join(root, f), "r", encoding="utf-8") as fp:
                txt = fp.read()
            m_title = re.search(r"^title:\s*\"([^\"]*)\"", txt, re.M)
            m_en = re.search(r"^en:\s*\"([^\"]*)\"", txt, re.M)
            if m_title:
                t = m_title.group(1).strip()
                slug_to_title[slug] = t
                title_to_slug[t.lower()] = slug
                clean_t = re.sub(r"\(.*?\)", "", t).strip().lower()
                if clean_t:
                    title_to_slug[clean_t] = slug
                for part in re.split(r"[/–—\-]", clean_t):
                    p = part.strip()
                    if len(p) > 3 and p not in title_to_slug:
                        title_to_slug[p] = slug
            if m_en:
                e = m_en.group(1).strip()
                en_to_slug[e.lower()] = slug
                clean_e = re.sub(r"\(.*?\)", "", e).strip().lower()
                if clean_e:
                    en_to_slug[clean_e] = slug
                for part in re.split(r"[/–—\-]", clean_e):
                    p = part.strip()
                    if len(p) > 3 and p not in en_to_slug:
                        en_to_slug[p] = slug

DOMAIN_MAPPINGS = {
    "المدرسة الوجودية": "sch-existential-therapy",
    "العلاج الوجودي": "sch-existential-therapy",
    "الوجودية": "sch-existentialism",
    "مدرسة التحليل النفسي": "sch-psychoanalysis",
    "التحليل النفسي": "sch-psychoanalysis",
    "التحليل النفسي (Psychoanalysis)": "sch-psychoanalysis",
    "المعرفية السلوكية": "sch-cognitive-behavioral",
    "العلاج المعرفي السلوكي": "sch-cognitive-behavioral",
    "العلاج المعرفي السلوكي (CBT)": "sch-cognitive-behavioral",
    "السلوكية": "sch-behaviorism",
    "المدرسة السلوكية": "sch-behaviorism",
    "السلوكية (Behaviorism)": "sch-behaviorism",
    "الإنسانية": "sch-humanistic",
    "علم النفس الإنساني": "sch-humanistic",
    "علم النفس الإنساني (Humanistic Psychology)": "sch-humanistic",
    "العلاج الجدلي السلوكي (DBT)": "sch-dbt",
    "العلاج الجدلي السلوكي": "sch-dbt",
    "العلاج بالقبول والالتزام (ACT)": "sch-act",
    "العلاج بالقبول والالتزام": "sch-act",
    "المشائية / الأرسطية": "sch-aristotelianism",
    "المشائية": "sch-aristotelianism",
    "الأرسطية": "sch-aristotelianism",
    "ما بعد البنيوية": "sch-post-structuralism",
    "البنيوية": "sch-structuralism",
    "الجسر (فلسفة ↔ علم نفس)": "rel-phenomenology-existential-therapy",
    "النَّسَقية والأسرية": "sch-systemic-family",
    "العلاج الأسري والنظامي": "sch-systemic-family",
    "العلاج الأسري": "sch-systemic-family",
    "الفكر الإسلامي النقدي المعاصر (نقد التراث والاستشراق)": "sch-contemporary-islamic-critique",
    "علم النفس المعرفي": "sch-cognitive-psychology",
    "الموجة الثالثة": "sch-third-wave-cbt",
    "علم نفس الجسد": "sch-somatic-psychology",
    "الفلسفة المشائية الإسلامية (كمظلة عامة)": "sch-islamic-peripatetic",
    "الفلسفة المشائية الإسلامية": "sch-islamic-peripatetic",
    "الرواقية (القديمة/الوسطى/الرومانية)": "sch-stoicism",
    "الرواقية": "sch-stoicism",
    "فلسفة العقل التحليلية (كمظلة: سلوكية، وظيفية، هوية، مادية إقصائية)": "sch-philosophy-of-mind",
    "فلسفة العقل": "sch-philosophy-of-mind",
    "الأفلاطونية المحدثة (النيوأفلاطونية)": "sch-neoplatonism",
    "الأفلاطونية المحدثة": "sch-neoplatonism",
    "sch-rationalism": "sch-continental-rationalism",
    "sch-clinical-psychology": "sch-cognitive-behavioral",
    "sch-buddhism": "sch-buddhism-early",
    "علم النفس الفردي": "sch-adlerian",
    "فلسفة العلم (كمظلة: البوبرية، الكوهنية، اللاكاتوشية، الفاير أباندية)": "sch-philosophy-of-science",
    "فلسفة العلم": "sch-philosophy-of-science",
    "الكانطية النقدية": "sch-kantianism",
    "الماركسية الكلاسيكية": "sch-classical-marxism",
    "الكونفوشية المبكرة": "sch-confucianism-early",
    "النيتشوية": "sch-nietzscheanism",
    "الميتافيزيقا التحليلية المعاصرة": "sch-analytic-metaphysics",
    "الأكاديمية الأفلاطونية (القديمة/الوسطى/الجديدة الشكية)": "sch-platonism-academy",
    "النظرية النقدية / مدرسة فرانكفورت": "sch-frankfurt-school",
    "النظرية النقدية": "sch-frankfurt-school",
    "الاضطرابات والمتلازمات الإكلينيكية": "sch-cognitive-behavioral",
    "الفلسفة التحليلية (القرن 20–21)": "sch-analytic-philosophy",
    "الفلسفة التحليلية": "sch-analytic-philosophy"
}

def resolve(target):
    t_clean = target.strip()
    if t_clean in slug_set:
        return t_clean
    if t_clean in DOMAIN_MAPPINGS and DOMAIN_MAPPINGS[t_clean] in slug_set:
        return DOMAIN_MAPPINGS[t_clean]
    t_lower = t_clean.lower()
    if t_lower in DOMAIN_MAPPINGS and DOMAIN_MAPPINGS[t_lower] in slug_set:
        return DOMAIN_MAPPINGS[t_lower]
    if t_lower in title_to_slug and title_to_slug[t_lower] in slug_set:
        return title_to_slug[t_lower]
    if t_lower in en_to_slug and en_to_slug[t_lower] in slug_set:
        return en_to_slug[t_lower]
    t_nop = re.sub(r"\(.*?\)", "", t_clean).strip().lower()
    if t_nop in DOMAIN_MAPPINGS and DOMAIN_MAPPINGS[t_nop] in slug_set:
        return DOMAIN_MAPPINGS[t_nop]
    if t_nop in title_to_slug and title_to_slug[t_nop] in slug_set:
        return title_to_slug[t_nop]
    if t_nop in en_to_slug and en_to_slug[t_nop] in slug_set:
        return en_to_slug[t_nop]
    for prefix in ["مدرسة ", "تيار ", "العلاج ", "الفلسفة ", "علم النفس "]:
        if t_nop.startswith(prefix):
            sub_t = t_nop[len(prefix):].strip()
            if sub_t in title_to_slug and title_to_slug[sub_t] in slug_set:
                return title_to_slug[sub_t]
            if sub_t in DOMAIN_MAPPINGS and DOMAIN_MAPPINGS[sub_t] in slug_set:
                return DOMAIN_MAPPINGS[sub_t]
    return None

EDGE_ITEM_RE = re.compile(r"(-\s*rel:\s*\"[^\"]*\"\s*,\s*target:\s*\")([^\"]*)(\"\s*,\s*target_type:\s*\"[^\"]*\")")

files_changed = 0
edges_replaced = 0

for root, dirs, files in os.walk(base):
    if "drafts" in root or "_merged" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                txt = fp.read()
            if not txt.startswith("---"):
                continue
            parts = txt.split("---", 2)
            if len(parts) < 3:
                continue
            raw_yaml = parts[1]
            body = parts[2]
            
            changes_in_file = [0]
            def repl_edge(match):
                prefix, target, suffix = match.group(1), match.group(2), match.group(3)
                r = resolve(target)
                if r and r != target:
                    changes_in_file[0] += 1
                    return f"{prefix}{r}{suffix}"
                return match.group(0)
                
            new_yaml = EDGE_ITEM_RE.sub(repl_edge, raw_yaml)
            if changes_in_file[0] > 0:
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(f"---{new_yaml}---{body}")
                files_changed += 1
                edges_replaced += changes_in_file[0]

print(f"Edge Canonicalization Applied: {edges_replaced} edge targets canonicalized across {files_changed} files.")
