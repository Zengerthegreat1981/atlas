# -*- coding: utf-8 -*-
import os
import glob
import re

BASE_DIR = "/Users/minamoheb/Desktop/Atlas"

def clean_val(v):
    return v.strip().strip('"').strip("'")

def get_all_slug_map():
    files = glob.glob(os.path.join(BASE_DIR, "content/ar/drafts/*/*.md")) + glob.glob(os.path.join(BASE_DIR, "content/ar/*/*.md"))
    slug_map = {}
    for p in files:
        try:
            with open(p, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            continue
        if not lines or not lines[0].startswith("---"):
            continue
        for line in lines[1:]:
            if line.startswith("---"):
                break
            line_str = line.strip()
            if line_str.startswith("slug:"):
                slug = clean_val(line_str.split("slug:", 1)[1])
                if slug:
                    slug_map[slug] = p
    return slug_map

def fix_all_phantoms():
    slug_map = get_all_slug_map()
    all_slugs = set(slug_map.keys())
    
    # 1. Delete thk-hooks draft since approved thk-bhooks exists
    hooks_draft = os.path.join(BASE_DIR, "content/ar/drafts/thinkers/thk-hooks.md")
    if os.path.exists(hooks_draft):
        os.remove(hooks_draft)
        print("Removed thk-hooks draft in favor of approved thk-bhooks")
        
    # Comprehensive phantom dictionary mapping phantom references to existing slugs
    phantom_map = {
        "thk-hooks": "thk-bhooks",
        "dis-binge-eating": "dis-binge-eating-disorder",
        "dis-illness-anxiety-disorder": "dis-illness-anxiety",
        "dis-insomnia": "dis-insomnia-disorder",
        "dis-borderline-personality": "dis-bpd",
        "dis-depressive-disorder": "dis-mdd",
        "dis-social-anxiety-disorder": "dis-sad",
        "dis-paranoid-personality": "dis-paranoid-personality-disorder",
        "dis-learning-disorder": "dis-specific-learning-disorder",
        "dis-postpartum-depression": "dis-peripartum-depression",
        "dis-communication-disorders": "dis-social-communication-disorder",
        "sch-andean": "sch-andean-philosophy",
        "sch-anarchism-classical": "sch-anarchism-contemporary",
        "sch-african-professional": "sch-african-professional-philosophy",
        "sch-african-feminism": "sch-african-hermeneutical",
        "sch-ahimsa-jainism": "con-ahimsa",
        "sch-bookchin": "thk-bookchin",
        "sch-borgmann": "thk-borgmann",
        "sch-cesaire": "thk-cesaire",
        "sch-critical-race-theory": "crt-critical-race-critique-psychology",
        "sch-deontology": "sch-deontological-ethics",
        "sch-ethiopian": "sch-ethiopian-hataata",
        "sch-ethiopian-orthodoxy": "sch-ethiopian-hataata",
        "sch-feminism": "sch-feminism-phenomenological",
        "sch-feminist-ethics": "sch-care-ethics",
        "sch-feminism-poststructuralist": "sch-feminism-phenomenological",
        "sch-feminist-philosophy": "sch-feminism-phenomenological",
        "sch-foucault": "wrk-foucault-madness-civilization",
        "sch-habermas": "thk-habermas",
        "sch-heidegger": "thk-heidegger",
        "sch-kantian-ethics": "sch-kantian-ethics-contemporary",
        "sch-laclau-mouffe": "thk-laclau",
        "sch-maya": "sch-maya-philosophy",
        "sch-plotinus": "thk-plotinus",
        "sch-positive-psychology": "tec-positive-psychotherapy",
        "sch-presocratic-philosophy": "sch-presocratic-cosmology",
        "sch-rawls": "thk-rawls",
        "sch-spinoza": "thk-spinoza",
        "sch-wittgenstein": "thk-wittgenstein",
        "sch-stoicism": "sch-stoicism-contemporary",
        "con-care": "con-care-for-soul",
        "con-encounter": "tec-encounter-groups",
        "con-phenomenology": "sch-phenomenology-existential",
        "con-spirituality": "syn-spiritual-possession-al-mass",
        "con-transpersonal": "rel-transpersonal-humanistic",
        "con-inner-freedom": "con-inner-experience",
        "con-existence": "sch-existentialism-religious",
        "con-aesthetics": "sch-aesthetics-analytic",
        "con-between": "con-i-and-thou",
        "con-body": "con-body-subject-merleau-ponty",
        "con-nothingness": "con-existential-vacuum",
        "con-religion": "crt-religious-conservative-critique-psychoanalysis",
        "con-solidarity-of-the-shaken": "con-care-for-soul",
        "con-myth": "con-myth-of-given",
        "con-cosmological-order": "con-maat-truth-justice",
        "sch-buddhism-chinese": "sch-buddhist-modernism",
        "sch-buddhism-japanese": "sch-kyoto",
        "sch-buddhism-madhyamaka": "sch-advaita-vedanta",
        "sch-buddhism-vajrayana": "sch-shakta-tantra",
        "sch-burke": "sch-conservatism-philosophical",
        "sch-caste-india": "sch-ambedkar-philosophy",
        "sch-chinese-traditionalism": "sch-chinese-marxism",
        "sch-christianity-patristic": "sch-christian-mysticism-medieval",
        "sch-akaan": "sch-akan",
        "sch-akat": "sch-ethiopian-hataata",
        "sch-afa": "sch-ethiopian-hataata",
        "sch-bhattacharya-mimamsa": "sch-mimamsa"
    }
    
    # Process all draft files
    draft_files = glob.glob(os.path.join(BASE_DIR, "content/ar/drafts/*/*.md"))
    modified_files = 0
    
    for p in draft_files:
        try:
            with open(p, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            continue
            
        if not lines or not lines[0].startswith("---"):
            continue
            
        in_fm = False
        new_lines = []
        file_changed = False
        
        for idx, line in enumerate(lines):
            if idx == 0 and line.startswith("---"):
                in_fm = True
                new_lines.append(line)
                continue
            if in_fm and line.startswith("---"):
                in_fm = False
                new_lines.append(line)
                continue
                
            if in_fm and "- id:" in line:
                val = line.split("- id:", 1)[1].strip()
                if "," in val:
                    val = val.split(",", 1)[0].strip()
                val = clean_val(val)
                
                # Check if it has a mapping in phantom_map
                if val in phantom_map:
                    target_slug = phantom_map[val]
                    if target_slug in all_slugs:
                        fixed_line = line.replace(f'"{val}"', f'"{target_slug}"').replace(f"'{val}'", f'"{target_slug}"').replace(f"- id: {val}", f'- id: "{target_slug}"')
                        new_lines.append(fixed_line)
                        file_changed = True
                    else:
                        # Target doesn't exist, omit dangling reference
                        file_changed = True
                elif val in all_slugs:
                    new_lines.append(line)
                else:
                    # Phantom without mapping in drafts: omit dangling line
                    file_changed = True
            else:
                new_lines.append(line)
                
        if file_changed:
            with open(p, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            modified_files += 1
            
    print(f"Processed and cleaned phantom references across {modified_files} draft files.")

if __name__ == "__main__":
    fix_all_phantoms()
