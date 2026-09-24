#!/usr/bin/env python3
"""
Fix duplicate and conflicting IDs from Phase 6 batch creation
"""

import re
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "content" / "ar"

# Map of existing thinkers to exclude from batch 2
existing_thinkers = {
    "thk-margaret-mead": "THK-6522",
    "thk-marilyn-strathern-expanded": "THK-12756",  # Different slug for strathern (expanded)
    "thk-sherry-ortner": "THK-12755",
    "thk-don-kulick": "THK-12769",
    "thk-tim-ingold": "THK-12759",
    "thk-tom-boellstorff": "THK-9011",
    "thk-fei-xiaotong": "THK-12763",
    "thk-jean-comaroff": "THK-13116",  # Already in Phase 5
    "thk-charles-campbell": "THK-12803",
    "thk-arturo-escobar": "THK-8934",
    "thk-peter-worsley": "THK-11820",
}

def fix_school_ids():
    """Fix school IDs from SCH-NEW to proper IDs"""
    next_id = 13134
    schools = {
        "sch-southeast-asian-anthropology": f"SCH-{next_id}",
        "sch-east-asian-anthropology-advanced": f"SCH-{next_id + 1}",
        "sch-mediterranean-anthropology": f"SCH-{next_id + 2}",
        "sch-digital-culture-anthropology": f"SCH-{next_id + 3}",
    }

    print("Fixing school IDs...")
    for slug, new_id in schools.items():
        filepath = DATA_DIR / "schools" / f"{slug}.md"
        if filepath.exists():
            content = filepath.read_text()
            content = content.replace('id: "SCH-NEW"', f'id: "{new_id}"')
            filepath.write_text(content)
            print(f"  {slug}: → {new_id}")

    return next_id + 4

def remove_duplicate_thinkers():
    """Remove thinker files that conflict with existing entries"""
    print("\nRemoving duplicate/conflicting thinker entries...")

    thinkers_to_remove = [
        "thk-margaret-mead.md",
        "thk-marilyn-strathern-expanded.md",
        "thk-sherry-ortner.md",
        "thk-don-kulick.md",
        "thk-tim-ingold.md",
        "thk-tom-boellstorff.md",
        "thk-fei-xiaotong.md",
        "thk-jean-comaroff.md",
        "thk-john-comaroff.md",  # Related to jean
        "thk-charles-campbell.md",
        "thk-arturo-escobar.md",
        "thk-peter-worsley.md",
    ]

    for filename in thinkers_to_remove:
        filepath = DATA_DIR / "thinkers" / filename
        if filepath.exists():
            filepath.unlink()
            print(f"  Removed: {filename}")

def fix_study_ids():
    """Fix study IDs to avoid duplicates"""
    # Studies seem to have conflicts in the STU series
    # Let me check for the stu- files created by batch 2
    study_files = list((DATA_DIR / "studies").glob("stu-*.md"))

    # Find studies created by batch 2 (based on recent content)
    batch2_studies = [
        "stu-comaroff-ethnography-tswana.md",
        "stu-mead-samoa-adolescence.md",
        "stu-strathern-gender-melanesia.md",
        "stu-fei-xiaotong-peasant-life.md",
        "stu-nakane-chie-vertical-society.md",
        "stu-marriott-hindu-caste.md",
        "stu-raheja-village-system.md",
        "stu-geertz-java-religion.md",
        "stu-bourdieu-kabyle-society.md",
        "stu-boyd-networked-teens.md",
        "stu-baym-communities-online.md",
        "stu-ingold-perceptions-environment.md",
        "stu-escobar-territories-difference.md",
    ]

    # Find the next available STU ID
    existing_stu_ids = []
    for f in study_files:
        content = f.read_text()
        match = re.search(r'id: "STU-(\d+)"', content)
        if match:
            existing_stu_ids.append(int(match.group(1)))

    if existing_stu_ids:
        next_stu = max(existing_stu_ids) + 1
    else:
        next_stu = 1304

    print(f"\nFixing study IDs (starting from STU-{next_stu})...")

    for i, study_filename in enumerate(batch2_studies):
        filepath = DATA_DIR / "studies" / study_filename
        if filepath.exists():
            new_id = f"STU-{next_stu + i}"
            content = filepath.read_text()
            content = re.sub(r'id: "STU-\d+"', f'id: "{new_id}"', content)
            filepath.write_text(content)
            print(f"  {study_filename}: → {new_id}")

def fix_instrument_ids():
    """Fix instrument IDs if there are duplicates"""
    print("\nChecking instrument IDs...")

    ins_files = list((DATA_DIR / "instruments").glob("ins-*.md"))
    existing_ids = []

    for f in ins_files:
        content = f.read_text()
        match = re.search(r'id: "INS-(\d+)"', content)
        if match:
            existing_ids.append(int(match.group(1)))

    # Check for duplicates
    if len(existing_ids) != len(set(existing_ids)):
        print("  Found duplicate instrument IDs!")
    else:
        print(f"  ✓ No duplicate instrument IDs (total: {len(existing_ids)})")

def main():
    print("=" * 60)
    print("FIXING PHASE 6 ID CONFLICTS")
    print("=" * 60)

    fix_school_ids()
    remove_duplicate_thinkers()
    fix_study_ids()
    fix_instrument_ids()

    print("\n" + "=" * 60)
    print("ID FIXES COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
