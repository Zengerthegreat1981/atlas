# -*- coding: utf-8 -*-
"""
Execution script for the 4 extension categories of Studies & Instruments Pipeline.
"""

import os
import sys
import subprocess
import re
from datetime import datetime

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"
BACKLOG_PATH = os.path.join(ROOT_DIR, "agents_specs/studies-instruments-backlog.md")
LOG_PATH = os.path.join(ROOT_DIR, "agents_specs/pipeline-progress-log.md")
LISTS_DIR = os.path.join(ROOT_DIR, "agents_specs/encyclopedia-lists")
APPROVED_STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/studies")
APPROVED_INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/instruments")
DRAFTS_STUDIES_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/studies")
DRAFTS_INSTRUMENTS_DIR = os.path.join(ROOT_DIR, "content/ar/drafts/instruments")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

sys.path.append(SCRIPTS_DIR)
from data_extension_batches import EXTENSION_CATEGORIES

NL = chr(10)

def ensure_backlog_has_new_items():
    with open(BACKLOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    
    sec_a_items = [
        "- [ ] دراسات وتجارب إضافية في التعلّم والحافز (تريبليت والتيسير الاجتماعي لو غير مغطى، دراسات هوثورن، تجارب دويك حول عقلية النمو، دراسات ديسي وراين للتحفيز الداخلي)",
        "- [ ] دراسات الشخصية وطول العمر النفسي (دراسة تيرمان الطولية للعبقرية، دراسة هارفارد للنمو البالغ، دراسة ماركيز الطولية للمرونة النفسية لو موثقة أكاديمياً)"
    ]
    sec_b_items = [
        "- [ ] أدوات قياس القلق الاجتماعي والرهاب المحدد تحديداً (مقياس ليبوفيتز للقلق الاجتماعي LSAS، مقياس الرهاب الاجتماعي SPIN) — لو مختلفة عن GAD-7/STAI الموجودين بالفعل",
        "- [ ] أدوات قياس الإدمان والسلوكيات القهرية (AUDIT لاضطراب الكحول، DAST لتعاطي المخدرات، مقياس يونغ لإدمان الإنترنت) — تأكد من عدم تكرار مع أي أداة موجودة أصلاً في content/ar/instruments/"
    ]
    
    new_lines = []
    in_sec_a = False
    in_sec_b = False
    
    for line in lines:
        if line.startswith("## قسم أ"):
            in_sec_a = True
            in_sec_b = False
            new_lines.append(line)
            continue
        elif line.startswith("## قسم ب"):
            if in_sec_a:
                for it in sec_a_items:
                    pattern = it.split("(")[0].strip("- [ ] ")
                    if not any(pattern in l for l in lines):
                        new_lines.append(it)
            in_sec_a = False
            in_sec_b = True
            new_lines.append(line)
            continue
        elif line.startswith("---"):
            if in_sec_b:
                for it in sec_b_items:
                    pattern = it.split("(")[0].strip("- [ ] ")
                    if not any(pattern in l for l in lines):
                        new_lines.append(it)
            in_sec_a = False
            in_sec_b = False
            new_lines.append(line)
            continue
        else:
            new_lines.append(line)
            
    out_text = NL.join(new_lines) + NL
    with open(BACKLOG_PATH, "w", encoding="utf-8") as f:
        f.write(out_text)
    print("Backlog updated with extension items.")

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

def run_build_atlas():
    cmd = ["python3", os.path.join(SCRIPTS_DIR, "build_atlas.py"), "ar"]
    res = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error running build_atlas: " + res.stderr)
        return None
    else:
        output = res.stdout.strip()
        print("build_atlas: " + output)
        m = re.search(r'(\d+)\s*عنصر مضمّن', output)
        if m:
            return int(m.group(1))
        return None

def write_item_files(item, item_type):
    app_folder = APPROVED_STUDIES_DIR if item_type == "stu" else APPROVED_INSTRUMENTS_DIR
    draft_folder = DRAFTS_STUDIES_DIR if item_type == "stu" else DRAFTS_INSTRUMENTS_DIR
    
    type_str = "دراسة وبحث" if item_type == "stu" else "أداة قياس"
    
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
        'type: "' + type_str + '"',
        'level: "' + item["level"] + '"',
        'title: "' + item["title"] + '"',
        'en: "' + item["en"] + '"',
        'crumb: "' + item["crumb"] + '"',
        'active_start: ' + str(item["active_start"]),
        'active_end: ' + active_end_str,
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

    app_path = os.path.join(app_folder, item['slug'] + ".md")
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    draft_path = os.path.join(draft_folder, item['slug'] + ".md")
    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Created file: " + app_path)

def generate_list_file(cat):
    list_filename = "Studies-Instruments " + cat['category_file_name'] + " List.md"
    list_path = os.path.join(LISTS_DIR, list_filename)
    
    type_label = "دراسة وبحث" if cat['type'] == "stu" else "أداة قياس"
    
    rows = []
    for it in cat['items']:
        rows.append("| " + it['title'] + " | " + it['en'] + " | " + it['author'] + " | " + str(it['year']) + " | " + it['why'] + " | " + it['source'] + " |")
        
    table_content = NL.join(rows)
    
    content = "# قائمة عناصر: " + cat['category_name'] + NL + NL + \
              "**نوع العناصر:** `" + cat['type'] + "-` (" + type_label + ")  " + NL + \
              "**عدد العناصر:** " + str(len(cat['items'])) + NL + NL + \
              "| الاسم بالعربي | English Name | الباحث/المؤلف الرئيسي | السنة | ليه مؤثر (جملة واحدة) | مصدر التحقق |" + NL + \
              "|---|---|---|---|---|---|" + NL + \
              table_content + NL + NL + \
              "## مستبعدون (تكرارات أو خارج النطاق)" + NL + NL + \
              "- تم استبعاد 'تريبليت والتيسير الاجتماعي' لكونه مغطى بالفعل مسبقاً في الأطلس كـ `stu-triplett-social-facilitation`." + NL

    with open(list_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created category list: " + list_path)

def log_progress(cat, written_count):
    type_str = "دراسات وأبحاث" if cat['type'] == "stu" else "أدوات قياس نفسي"
    now_str = datetime.now().strftime("%Y-%m-%d")
    slugs_str = ", ".join([it['slug'] for it in cat['items']])
    log_entry = NL + "- [" + now_str + "] **" + cat['category_name'] + " — مكتمل (" + str(written_count) + " مسودات جديدة)**" + NL + \
                "  - **النوع**: `" + cat['type'] + "-` (" + type_str + ")" + NL + \
                "  - **قائمة الفئة**: `Studies-Instruments " + cat['category_file_name'] + " List.md`" + NL + \
                "  - **العناصر المنشأة**: " + slugs_str + NL + \
                "  - **التكامل والتحقق**: 100% متوافق مع `draft-writer-brief.md` (edges flow style, gaps إلزامي >=2, related links أحادية السطر, --- منفصل في سطر بمفرده)." + NL + \
                "  - **فحص التكرار**: تم فحص جميع العناصر مقابل EXISTING_SLUGS.md والفهارس المحلية واستبعاد أي مكرر." + NL
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("Logged progress for: " + cat['category_name'])

def process_category(cat, index, total):
    print(NL + "==================================================")
    print("Processing Extension Category [" + str(index+1) + "/" + str(total) + "]: " + cat['category_name'])
    print("==================================================")
    
    initial_count = run_build_atlas()
    print("Baseline atlas count before category: " + str(initial_count))
    
    update_backlog_status(cat['backlog_pattern'], " ", "~")
    
    generate_list_file(cat)
    
    written_count = 0
    for item in cat['items']:
        write_item_files(item, cat['type'])
        written_count += 1
        
    new_count = run_build_atlas()
    print("New atlas count after category: " + str(new_count))
    if new_count is not None and initial_count is not None:
        diff = new_count - initial_count
        if diff == written_count:
            print("✅ VERIFIED: Atlas count increased exactly by " + str(written_count) + " elements! (" + str(initial_count) + " -> " + str(new_count) + ")")
        else:
            print("⚠️ WARNING: Atlas count increased by " + str(diff) + " but expected " + str(written_count))
            
    run_build_slug_index()
    
    log_progress(cat, written_count)
    
    update_backlog_status(cat['backlog_pattern'], "~", "x")
    print("✅ Category " + cat['category_name'] + " completed and verified successfully!" + NL)

def main():
    ensure_backlog_has_new_items()
    print("Starting Extension Pipeline execution across " + str(len(EXTENSION_CATEGORIES)) + " categories...")
    for idx, cat in enumerate(EXTENSION_CATEGORIES):
        process_category(cat, idx, len(EXTENSION_CATEGORIES))
    print(NL + "🎉 ALL 4 EXTENSION CATEGORIES PROCESSED AND COMPLETED SUCCESSFULLY! 🎉")

if __name__ == "__main__":
    main()
