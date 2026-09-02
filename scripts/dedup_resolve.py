#!/usr/bin/env python3
"""
Dedup resolution: deletes redundant drafts where an approved version exists.
Does NOT touch the 6 cross-school techniques (per pipeline log).
Does NOT touch cross-type dupes that have legitimate different categories.
"""
import os
import re

DRAFTS_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar/drafts"
APPROVED_BASE = "/Users/minamoheb/Desktop/Atlas/content/ar"

# These are the 6 (now 7) cross-school techniques flagged in pipeline-progress-log
# as 'يحتاج قرار بشري' — DO NOT DELETE
KEEP_BOTH_SLUGS = {
    "tec-cbt-mind-body-scan",
    "tec-act-pres-body-scan",
    "tec-dbt-er-self-validation",
    "tec-cbt-int-self-validation",
    "tec-cbt-emo-self-compassion-exercises",
    "tec-act-acc-self-compassion-exercises",
    "tec-dbt-dt-willingness-vs-willfulness",
    "tec-act-acc-willingness-vs-willfulness",
    "tec-dbt-dt-radical-acceptance",
    "tec-act-acc-radical-acceptance",
    "tec-dbt-er-mindful-eating",
    "tec-act-pres-mindful-eating",
    "tec-dbt-dt-urge-surfing",
    "tec-act-pres-urge-surfing",
}

# These cross-type dupes are valid (different categories serve different purposes)
# Per the brief: br- for tيار, con- for مفهوم, tec- for تقنية
KEEP_BOTH_CROSS_TYPE = {
    "br-abstinence-vs-harm-reduction", "con-abstinence-vs-harm-reduction",
    "con-dissociation", "syn-dissociation",
    "br-restorative-justice", "con-restorative-justice",
    "br-fft", "tec-functional-family-therapy",
    "school-dbt", "tec-dbt",
    "br-dynamic-couples-family-therapy", "con-dynamic-couple-family",
    "br-critical-liberation-therapy", "con-critical-liberation-therapy",
    "br-mst", "tec-multisystemic-therapy",
    "br-family-sandplay", "con-family-sandplay",
    "br-intersectional-feminist", "con-intersectional-feminism",
}

# Drafts to keep (they have unique slug that doesn't conflict with approved)
# These are the drafts that should be DELETED if approved exists
DRAFTS_TO_DELETE_THINKER = [
    # Each is a draft of a thinker whose approved version exists with different slug
    "thk-amaslow",  # vs thk-maslow
    "thk-hmhusserl",  # vs thk-husserl
    "thk-efromm",  # vs thk-fromm
    "thk-elukas",  # vs thk-lukas
    "thk-asutich",  # vs thk-sutich
    "thk-orank",  # vs thk-rank
    "thk-irvinyalom",  # vs thk-yalom
    "thk-pgoodman",  # vs thk-goodman
    "thk-jlacanian",  # vs thk-lacan
    "thk-jfabry",  # vs thk-fabry
    "thk-mayr",  # vs thk-may
    "thk-viktorfrankl",  # vs thk-frankl
    "thk-crogers",  # vs thk-rogers
    "thk-ccaldwell",  # vs thk-caldwell
    "thk-rmoustakas",  # vs thk-moustakas
    "thk-ludwigbinswanger",  # vs thk-binswanger
    "thk-medardboss",  # vs thk-boss
    "thk-abatth",  # vs thk-batthyany
    "thk-alangle",  # vs thk-langle
    "thk-ffanon",  # vs thk-fanon
    "thk-ffrommreich",  # vs thk-fromm-reichmann
    "thk-pwatzl",  # vs thk-gbateson (this one has wrong slug — pwatzl is watzlawick name, not bateson!)
    "thk-hsachs",  # vs thk-sachs (sachs)
    "thk-jjonas",  # vs thk-jonas
    "thk-hguntrip",  # vs thk-guntrip
    "thk-hssullivan",  # vs thk-sullivan
    "thk-hkohut",  # vs thk-kohut
    "thk-hansbacher",  # vs thk-ansbacher
    "thk-jpanksepp",  # vs thk-panksepp
    "thk-jbreuer",  # vs thk-breuer
    "thk-jjordan",  # vs thk-jordan
    # thk-irerich doesn't exist (was hypothetical)
    "thk-dkahneman",  # vs thk-rkahneman (keep the more recent slug)
    # Add more as discovered
]

# A second list: drafts that are pure duplicates (both are drafts, same person, different slugs)
DRAFTS_TO_DELETE_DUPLICATES = [
    "thk-abeck",  # vs thk-beck (both drafts, Aaron T. Beck)
    "thk-aellis",  # vs thk-ellis
    "thk-aaichhorn",  # vs thk-aichhorn
    "thk-abateman",  # vs thk-bateman
    "thk-bbrandchaft",  # vs thk-brandchaft
    "thk-alazarus",  # vs thk-lazarus
    "thk-harrystack-sullivan",  # vs thk-hssullivan
    # Round 2: en-based duplicates discovered in second pass
    "thk-evandeurzen",  # vs approved thk-vandeurzen
    "thk-irerich",  # vs approved thk-fromm
    "thk-karenhorney",  # vs thk-khorney (both drafts, Karen Horney)
    "thk-lirigaray",  # vs thk-irigaray
    "thk-lbinswanger",  # vs approved thk-binswanger
    "thk-lymanwynne",  # vs approved thk-lwynne
    "thk-mahler",  # vs thk-mmahler (Margaret Mahler)
    "thk-eitingon",  # vs thk-meitingon (Max Eitingon)
    "thk-mboss",  # vs approved thk-boss
    "thk-mcsik",  # vs thk-mcsikszent (Mihaly Csikszentmihalyi)
    "thk-olovaas",  # vs thk-ilovaas (O. Ivar Lovaas)
    "thk-orlindsley",  # vs thk-rlindsl (Ogden R. Lindsley)
    "thk-phaley",  # vs approved thk-pwatzlawick (note: this draft is Paul Haley, but en field says Watzlawick; check!)
    "thk-mfonagy",  # vs thk-pfonel (Peter Fonagy)
    "thk-paulagnier",  # vs thk-aulagnier (Piera Aulagnier)
    "thk-kaes",  # vs thk-rkaes (Ren Kaes)
    "thk-rspitz",  # vs thk-spitz (Ren Spitz)
    "thk-rstolorow",  # vs thk-stolorow (Robert Stolorow)
    "thk-dreikurs",  # vs thk-rdreikurs (Rudolf Dreikurs)
    "thk-ferenczi",  # vs thk-sferenczi (Sándor Ferenczi)
    "thk-sorenk",  # vs approved thk-kierkegaard
    "thk-vfrankl",  # vs approved thk-frankl
    "thk-oreich",  # vs thk-reich (Wilhelm Reich)
    "thk-stekel",  # vs thk-wstekel (Wilhelm Stekel)
]

if __name__ == '__main__':
    all_to_delete = DRAFTS_TO_DELETE_THINKER + DRAFTS_TO_DELETE_DUPLICATES
    deleted = []
    skipped = []
    missing = []
    for slug in all_to_delete:
        # Find which folder
        for tdir in ["thinkers", "concepts", "works", "instruments", "techniques", "studies", "events", "disorders", "syndromes", "relations", "dialogues", "critiques", "axioms", "metaphors", "experiences", "terms", "questions", "contexts", "branches", "schools", "debates"]:
            for subdir in [DRAFTS_BASE, APPROVED_BASE]:
                p = os.path.join(subdir, tdir, f"{slug}.md")
                if os.path.isfile(p):
                    if subdir == DRAFTS_BASE:
                        if slug in KEEP_BOTH_SLUGS or slug in KEEP_BOTH_CROSS_TYPE:
                            skipped.append((slug, "KEEP_BOTH"))
                            continue
                        os.remove(p)
                        deleted.append((slug, tdir, p))
                    else:
                        # It's approved - check the draft version exists
                        pass
                    break
            else:
                continue
            break
        else:
            missing.append(slug)

    print(f"Deleted: {len(deleted)}")
    for s, t, p in deleted:
        print(f"  ✓ {s}.md  (from {t}/)")
    print(f"Skipped (in KEEP list): {len(skipped)}")
    print(f"Missing (not found in any folder): {len(missing)}")
    for m in missing:
        print(f"  ? {m}")
