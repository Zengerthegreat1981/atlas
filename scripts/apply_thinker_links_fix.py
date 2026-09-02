# -*- coding: utf-8 -*-
"""
Apply thinker links fix to studies and instruments drafts.
Moves confirmed thinkers from 'أفكار روابط لم تُتحقق' to 'related:' in frontmatter.
"""

import os
import re
import subprocess
from datetime import datetime

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")
LOG_PATH = os.path.join(ROOT_DIR, "agents_specs/pipeline-progress-log.md")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

NL = chr(10)

CONFIRMED_MATCHES = [
    {
        "file": "stu-asch-conformity.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"سولومون آش",
        "slug": "thk-sasch",
        "title": "سولومون آش",
        "type": "مفكر"
    },
    {
        "file": "stu-bandura-bobo-doll.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"ألبرت باندورا",
        "slug": "thk-abandura",
        "title": "ألبرت باندورا",
        "type": "مفكر"
    },
    {
        "file": "stu-bowlby-forty-four-thieves.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"جون بولبي",
        "slug": "thk-bowlby",
        "title": "جون بولبي",
        "type": "مفكر"
    },
    {
        "file": "stu-festinger-cognitive-dissonance.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"ليون فستنجر",
        "slug": "thk-lfestinger",
        "title": "ليون فِستِنغر",
        "type": "مفكر"
    },
    {
        "file": "stu-lilly-sensory-deprivation-tank.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"جون سي\. ليلي",
        "slug": "thk-jlilly",
        "title": "جون لِلي",
        "type": "مفكر"
    },
    {
        "file": "stu-pavlov-classical-conditioning.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"إيفان بافلوف",
        "slug": "thk-ipavlov",
        "title": "إيفان بافلوف",
        "type": "مفكر"
    },
    {
        "file": "stu-peterson-seligman-explanatory-style.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"كريستوفر بيترسون",
        "slug": "thk-cpeterson",
        "title": "كريستوفر بيترسون",
        "type": "مفكر"
    },
    {
        "file": "stu-seligman-maier-learned-helplessness.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"مارتن سليجمان",
        "slug": "thk-mseligman",
        "title": "مارتن سليغمان",
        "type": "مفكر"
    },
    {
        "file": "stu-skinner-operant-conditioning.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"ب\. ف\. سكينر",
        "slug": "thk-fskinner",
        "title": "بوريس فريدريك سكينر",
        "type": "مفكر"
    },
    {
        "file": "stu-thorndike-puzzle-box.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"إدوارد ثورندايك",
        "slug": "thk-thorndike",
        "title": "إدوارد ثورنديك",
        "type": "مفكر"
    },
    {
        "file": "stu-watson-little-albert.md",
        "folder": STUDIES_DIR,
        "unverified_pattern": r"جون ب\. واطسون",
        "slug": "thk-jwatson",
        "title": "جون ب. واتسون",
        "type": "مفكر"
    },
    {
        "file": "ins-bdi-ii.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"آرون بيك",
        "slug": "thk-beck",
        "title": "آرون تيموثي بيك",
        "type": "مفكر"
    },
    {
        "file": "ins-cbcl.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"توماس أشنباخ",
        "slug": "thk-tachenbach",
        "title": "توماس أشنباخ",
        "type": "مفكر"
    },
    {
        "file": "ins-mbti.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"كارل غوستاف يونغ",
        "slug": "thk-jung",
        "title": "كارل غوستاف يونغ",
        "type": "مفكر"
    },
    {
        "file": "ins-oci-r.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"إدنا فوا",
        "slug": "thk-foa",
        "title": "إدنا ب. فوا",
        "type": "مفكر"
    },
    {
        "file": "ins-phq-9.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"روبرت سبيتزر",
        "slug": "thk-rspitzer",
        "title": "روبرت سبيتزر",
        "type": "مفكر"
    },
    {
        "file": "ins-swls.md",
        "folder": INSTRUMENTS_DIR,
        "unverified_pattern": r"روبرت إيمونز",
        "slug": "thk-emmons",
        "title": "روبرت إيمونز",
        "type": "مفكر"
    }
]

def update_file(match_info):
    fpath = os.path.join(match_info["folder"], match_info["file"])
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_related_line = '  - id: "' + match_info["slug"] + '", title: "' + match_info["title"] + '", type: "' + match_info["type"] + '"'
    
    if "related: []" in content:
        content = content.replace("related: []", "related:" + NL + new_related_line)
    elif "related:" in content:
        if match_info["slug"] not in content:
            content = content.replace("related:" + NL, "related:" + NL + new_related_line + NL)
            
    lines = content.splitlines()
    new_lines = []
    in_unverified_section = False
    
    for line in lines:
        if line.strip() == "## أفكار روابط لم تُتحقق":
            in_unverified_section = True
            new_lines.append(line)
            continue
            
        if in_unverified_section:
            if re.search(match_info["unverified_pattern"], line):
                print("  Removed from unverified in " + match_info["file"] + ": " + line.strip())
                continue
            elif line.strip().startswith("- "):
                new_lines.append(line)
            elif line.strip().startswith("## "):
                in_unverified_section = False
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    final_lines = []
    skip_header = False
    for i, line in enumerate(new_lines):
        if line.strip() == "## أفكار روابط لم تُتحقق":
            has_items = False
            for j in range(i+1, len(new_lines)):
                if new_lines[j].strip().startswith("## "):
                    break
                if new_lines[j].strip().startswith("- "):
                    has_items = True
                    break
            if not has_items:
                skip_header = True
                continue
        if skip_header:
            if line.strip().startswith("## ") and line.strip() != "## أفكار روابط لم تُتحقق":
                skip_header = False
                final_lines.append(line)
            elif line.strip() == "":
                continue
            else:
                continue
        else:
            final_lines.append(line)

    new_content = NL.join(final_lines).strip() + NL
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated file: " + match_info["file"])

def main():
    print("Starting Thinker Links Fix across " + str(len(CONFIRMED_MATCHES)) + " confirmed matches...")
    touched_files = set()
    for m in CONFIRMED_MATCHES:
        update_file(m)
        touched_files.add(m["file"])

    print(NL + "Total files corrected: " + str(len(touched_files)))
    print("Total thinker links transferred: " + str(len(CONFIRMED_MATCHES)))

    print(NL + "Running build_slug_index.py...")
    cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_slug_index.py")]
    res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error rebuilding index: " + res.stderr)
    else:
        print(res.stdout.strip())

    now_str = datetime.now().strftime("%Y-%m-%d")
    log_entry = NL + "- [" + now_str + "] **تصحيح روابط المفكرين في مسودات الدراسات وأدوات القياس (Cross-Link Audit)**" + NL + \
                "  - **السياق**: فحص جميع الأسماء المذكورة في أقسام 'أفكار روابط لم تُتحقق' بالـ 120 مسودة مقابل `EXISTING_SLUGS.md`." + NL + \
                "  - **النتائج**: تم نقل **" + str(len(CONFIRMED_MATCHES)) + " رابط مفكر مؤكد** عبر **" + str(len(touched_files)) + " ملفاً** من قسم الروابط غير المتحققة إلى قسم `related` في الـ frontmatter بصيغة السطر الواحد." + NL + \
                "  - **الملفات والروابط المنقولة**:" + NL
    for m in CONFIRMED_MATCHES:
        log_entry += "    - `" + m["file"] + "` ➔ `id: \"" + m["slug"] + "\", title: \"" + m["title"] + "\", type: \"مفكر\"`" + NL
    log_entry += "  - **التحقق والتنظيف**: تحديث `EXISTING_SLUGS.md` تلقائياً، والاحتفاظ بالأسماء غير الموجودة في الفهرس (مثل إيزابيل مايرز، كورت كرونكي) في قسم الأفكار المقترحة." + NL

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("Logged progress to " + LOG_PATH)

if __name__ == "__main__":
    main()
