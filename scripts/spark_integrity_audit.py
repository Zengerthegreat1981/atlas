# -*- coding: utf-8 -*-
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os
import re
from collections import defaultdict

BASE_DIR = _ATLAS_ROOT
DRAFTS_BASE = os.path.join(BASE_DIR, "content/ar/drafts")
APPROVED_BASE = os.path.join(BASE_DIR, "content/ar")

TYPE_DIRS = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]

def normalize_arabic(s):
    if not s: return ""
    s = s.strip()
    s = re.sub(r'[\u064B-\u065F\u0670]', '', s)
    s = re.sub(r'[إأآا]', 'ا', s)
    s = re.sub(r'[يى]', 'ي', s)
    s = re.sub(r'ة', 'ه', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

def normalize_english(s):
    if not s: return ""
    s = s.strip().lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def parse_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        return None
        
    if not lines or not lines[0].startswith("---"):
        return None
        
    fm_lines = []
    for line in lines[1:]:
        if line.startswith("---"):
            break
        fm_lines.append(line)
        
    rec = {
        'path': path,
        'slug': '',
        'title_ar': '',
        'title_en': '',
        'part': '',
        'type': '',
        'related_ids': []
    }
    
    for line in fm_lines:
        line_str = line.strip()
        if line_str.startswith("slug:"):
            val = line_str.split("slug:", 1)[1].strip().strip('"\'')
            rec['slug'] = val
        elif line_str.startswith("title:"):
            val = line_str.split("title:", 1)[1].strip().strip('"\'')
            rec['title_ar'] = val
        elif line_str.startswith("en:"):
            val = line_str.split("en:", 1)[1].strip().strip('"\'')
            rec['title_en'] = val
        elif line_str.startswith("part:"):
            val = line_str.split("part:", 1)[1].strip().strip('"\'')
            rec['part'] = val
        elif line_str.startswith("type:"):
            val = line_str.split("type:", 1)[1].strip().strip('"\'')
            rec['type'] = val
        elif "- id:" in line_str:
            val = line_str.split("- id:", 1)[1].strip()
            if "," in val:
                val = val.split(",", 1)[0].strip()
            val = val.strip('"\'')
            if val:
                rec['related_ids'].append(val)
                
    return rec

def gather_all_files():
    all_files = []
    for tdir in TYPE_DIRS:
        draft_dir = os.path.join(DRAFTS_BASE, tdir)
        approved_dir = os.path.join(APPROVED_BASE, tdir)
        for base, status in [(draft_dir, 'draft'), (approved_dir, 'approved')]:
            if not os.path.isdir(base):
                continue
            for fn in os.listdir(base):
                if not fn.endswith('.md'):
                    continue
                path = os.path.join(base, fn)
                rec = parse_file(path)
                if rec and rec['slug']:
                    rec['type_dir'] = tdir
                    rec['status'] = status
                    all_files.append(rec)
    return all_files

def run_audit():
    files = gather_all_files()
    print("Total files parsed: " + str(len(files)))
    
    all_slugs_set = set(f['slug'] for f in files if f['slug'])
    print("Total unique defined slugs: " + str(len(all_slugs_set)))
    
    # --- TASK 1: Philosophy dedup audit ---
    phil_files = [f for f in files if f.get('part') == 'philosophy']
    print("Total philosophy files (part: 'philosophy'): " + str(len(phil_files)))
    
    same_type_ar = defaultdict(list)
    for f in phil_files:
        if f.get('title_ar'):
            key = (f['type_dir'], normalize_arabic(f['title_ar']))
            same_type_ar[key].append(f)
    same_type_ar_dupes = {k: v for k, v in same_type_ar.items() if len(v) >= 2}
    
    same_type_en = defaultdict(list)
    for f in phil_files:
        if f.get('title_en'):
            key = (f['type_dir'], normalize_english(f['title_en']))
            same_type_en[key].append(f)
    same_type_en_dupes = {k: v for k, v in same_type_en.items() if len(v) >= 2}
    
    cross_part_by_name = defaultdict(list)
    for f in files:
        if f.get('title_ar'):
            key = (f['type_dir'], normalize_arabic(f['title_ar']))
            cross_part_by_name[key].append(f)
    cross_part_dupes = {}
    for k, v in cross_part_by_name.items():
        if len(v) >= 2:
            parts = set(f.get('part', '') for f in v)
            if 'philosophy' in parts and len(parts) >= 2:
                cross_part_dupes[k] = v
                
    print(chr(10) + "="*50)
    print("TASK 1: PHILOSOPHY DEDUP RESULTS")
    print("="*50)
    print("1. Same-type (ar) potential duplicates in Philosophy: " + str(len(same_type_ar_dupes)) + " groups")
    for k, group in same_type_ar_dupes.items():
        print("  [AR DUP GROUP] Type: " + str(k[0]) + " | Title: '" + str(k[1]) + "'")
        for g in group:
            print("    - [" + g['status'] + "] slug=" + g['slug'] + " | en='" + g['title_en'] + "' | " + os.path.basename(g['path']))
            
    print(chr(10) + "2. Same-type (en) potential duplicates in Philosophy: " + str(len(same_type_en_dupes)) + " groups")
    for k, group in same_type_en_dupes.items():
        print("  [EN DUP GROUP] Type: " + str(k[0]) + " | En: '" + str(k[1]) + "'")
        for g in group:
            print("    - [" + g['status'] + "] slug=" + g['slug'] + " | ar='" + g['title_ar'] + "' | " + os.path.basename(g['path']))
            
    print(chr(10) + "3. Cross-part potential duplicates (Philosophy vs Psychology/Other): " + str(len(cross_part_dupes)) + " groups")
    for k, group in cross_part_dupes.items():
        print("  [CROSS-PART GROUP] Type: " + str(k[0]) + " | Title: '" + str(k[1]) + "'")
        for g in group:
            print("    - [" + g['status'] + "] slug=" + g['slug'] + " | part='" + g.get('part','') + "' | en='" + g['title_en'] + "' | " + os.path.basename(g['path']))
            
    # --- TASK 2: Phantom slugs audit across entire Atlas ---
    phantom_related = defaultdict(list)
    total_related_count = 0
    valid_related_count = 0
    
    for f in files:
        for rel_id in f['related_ids']:
            total_related_count += 1
            if rel_id in all_slugs_set:
                valid_related_count += 1
            else:
                phantom_related[rel_id].append(f['path'])
                
    print(chr(10) + "="*50)
    print("TASK 2: PHANTOM SLUGS RESULTS")
    print("="*50)
    print("Total related links checked: " + str(total_related_count))
    print("Valid related links: " + str(valid_related_count))
    print("Unique phantom related IDs: " + str(len(phantom_related)))
    
    print(chr(10) + "List of Phantom IDs and potential matches:")
    for ph, src_list in sorted(phantom_related.items()):
        close_matches = [s for s in all_slugs_set if ph in s or s in ph or (len(ph) > 5 and len(s) > 5 and ph[4:10] == s[4:10])]
        print("  PHANTOM: '" + ph + "' (in " + str(len(src_list)) + " files: " + os.path.basename(src_list[0]) + ") -> matches: " + str(close_matches[:3]))

if __name__ == '__main__':
    run_audit()
