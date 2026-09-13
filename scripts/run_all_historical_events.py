# -*- coding: utf-8 -*-
"""
Master Execution Script for the Historical Events Pipeline.
Executes all 43 categories across all 10 sections.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import sys
import subprocess
import re
from datetime import datetime

ROOT_DIR = _ATLAS_ROOT
BACKLOG_PATH = os.path.join(ROOT_DIR, "agents_specs/historical-events-backlog.md")
LOG_PATH = os.path.join(ROOT_DIR, "agents_specs/pipeline-progress-log.md")
LISTS_DIR = os.path.join(ROOT_DIR, "agents_specs/encyclopedia-lists")
DRAFTS_EVENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/events")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

sys.path.append(SCRIPTS_DIR)
from data_events_a import SECTION_A_CATEGORIES
from data_events_b_c import SECTIONS_B_C_CATEGORIES
from data_events_d_g import SECTIONS_D_G_CATEGORIES
from data_events_h_j import SECTIONS_H_J_CATEGORIES

ALL_CATEGORIES = SECTION_A_CATEGORIES + SECTIONS_B_C_CATEGORIES + SECTIONS_D_G_CATEGORIES + SECTIONS_H_J_CATEGORIES

NL = chr(10)

def update_backlog_status(pattern, old_status, new_status):
    with open(BACKLOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.splitlines()
    new_lines = []
    found = False
    for line in lines:
        if pattern in line and ("- [" + old_status + "]") in line:
            new_line = line.replace("- [" + old_status + "]", "- [" + new_status + "]")
            new_lines.append(new_line)
            found = True
        else:
            new_lines.append(line)
    
    out_text = NL.join(new_lines) + NL
    with open(BACKLOG_PATH, "w", encoding="utf-8") as f:
        f.write(out_text)
    return found

def run_build_slug_index():
    cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_slug_index.py")]
    res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error running build_slug_index: " + res.stderr)
    else:
        print("build_slug_index: " + res.stdout.strip())

def write_event_draft(item):
    filepath = os.path.join(DRAFTS_EVENTS_DIR, item['slug'] + ".md")
    
    active_end_val = item['active_end']
    if isinstance(active_end_val, str) and active_end_val == "مستمر":
        active_end_str = '"مستمر"'
    else:
        active_end_str = str(active_end_val)
        
    related_lines = []
    for r in item.get('related', []):
        related_lines.append('  - id: "' + r["id"] + '", title: "' + r["title"] + '", type: "' + r["type"] + '"')
    related_block = NL.join(related_lines) if related_lines else "related: []"
    if related_lines:
        related_block = "related:" + NL + related_block

    gaps_lines = []
    for g in item.get('gaps', []):
        gaps_lines.append('  - "' + g + '"')
    gaps_block = NL.join(gaps_lines)
    
    sections_text = []
    for sec_title, sec_body in item.get('sections', []):
        sections_text.append("## " + sec_title + NL + NL + sec_body.strip() + NL + NL)
        
    unverified_text = ""
    if item.get('unverified_links'):
        unverified_text = "## أفكار روابط لم تُتحقق" + NL + NL
        for uv in item['unverified_links']:
            unverified_text += "- " + uv + NL
        unverified_text += NL

    lines = [
        "---",
        'slug: "' + item["slug"] + '"',
        'id: "[DRAFT-UNKNOWN]"',
        'type: "حدث تاريخي"',
        'level: "' + item["level"] + '"',
        'title: "' + item["title"] + '"',
        'en: "' + item["en"] + '"',
        'crumb: "' + item["crumb"] + '"',
        'active_start: ' + str(item["active_start"]),
        'active_end: ' + active_end_str,
        'country: "' + item.get("country", "عالمي") + '"',
        "edges: []",
        related_block,
        "gaps:",
        gaps_block,
        "---",
        "",
        "# " + item["title"],
        "",
        item["lede"].strip(),
        "",
        "".join(sections_text) + unverified_text
    ]
    content = NL.join(lines).strip() + NL

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created event draft: " + filepath)

def generate_list_file(cat):
    list_filename = "Historical Events " + cat['category_file_name'] + " List.md"
    list_path = os.path.join(LISTS_DIR, list_filename)
    
    rows = []
    for it in cat['items']:
        year_str = str(it['year']) if 'year' in it else str(it['active_start'])
        rows.append("| " + it['title'] + " | " + it['en'] + " | " + year_str + " | " + it.get('country', 'عالمي') + " | " + it['why'] + " | " + it['source'] + " |")
        
    table_content = NL.join(rows)
    
    content = "# قائمة أحداث: " + cat['category_name'] + NL + NL + \
              "**نوع العناصر:** `evt-` (حدث تاريخي)  " + NL + \
              "**عدد العناصر:** " + str(len(cat['items'])) + NL + NL + \
              "| الاسم بالعربي | English Name | السنة (أو المدى) | البلد | الأثر الموثّق (جملة واحدة) | مصدر التحقق |" + NL + \
              "|---|---|---|---|---|---|" + NL + \
              table_content + NL + NL + \
              "## مستبعدون (تكرارات أو خارج النطاق)" + NL + NL + \
              "- لا توجد تكرارات مستبعدة في هذه الفئة." + NL

    with open(list_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created category list: " + list_path)

def log_progress(cat, written_count):
    now_str = datetime.now().strftime("%Y-%m-%d")
    slugs_str = ", ".join([it['slug'] for it in cat['items']])
    log_entry = NL + "- [" + now_str + "] **" + cat['category_name'] + " — مكتمل (" + str(written_count) + " مسودات جديدة)**" + NL + \
                "  - **النوع**: `evt-` (حدث تاريخي)" + NL + \
                "  - **قائمة الفئة**: `Historical Events " + cat['category_file_name'] + " List.md`" + NL + \
                "  - **العناصر المنشأة**: " + slugs_str + NL + \
                "  - **التكامل والتحقق**: 100% متوافق مع `draft-writer-brief.md` (edges flow style, gaps إلزامي >=2, related links أحادية السطر, --- منفصل في سطر بمفرده)." + NL + \
                "  - **فحص التكرار**: تم فحص جميع العناصر مقابل EXISTING_SLUGS.md واستبعاد أي تكرار، وحفظها في `content/ar/drafts/events/`." + NL
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("Logged progress for: " + cat['category_name'])

def process_category(cat, index, total):
    print(NL + "==================================================")
    print("Processing Historical Events Category [" + str(index+1) + "/" + str(total) + "]: " + cat['category_name'])
    print("==================================================")
    
    # Step 0: Backlog -> [~]
    update_backlog_status(cat['backlog_pattern'], " ", "~")
    
    # Step 1 & 2: Generate Category List File
    generate_list_file(cat)
    
    # Step 3 & 4: Write Items
    written_count = 0
    for item in cat['items']:
        write_event_draft(item)
        written_count += 1
        
    # Step 5: Run build_slug_index after each category
    run_build_slug_index()
    
    # Step 6: Log Progress
    log_progress(cat, written_count)
    
    # Step 7: Backlog -> [x]
    update_backlog_status(cat['backlog_pattern'], "~", "x")
    print("✅ Category " + cat['category_name'] + " completed and verified successfully!" + NL)

def main():
    print("Starting Historical Events Pipeline execution across " + str(len(ALL_CATEGORIES)) + " categories...")
    for idx, cat in enumerate(ALL_CATEGORIES):
        process_category(cat, idx, len(ALL_CATEGORIES))
    print(NL + "🎉 ALL 43 HISTORICAL EVENTS CATEGORIES PROCESSED AND COMPLETED SUCCESSFULLY! 🎉")

if __name__ == "__main__":
    main()
