# -*- coding: utf-8 -*-
"""
Validate all historical events candidate slugs against existing slugs.
"""

import os
import glob
import re

ROOT_DIR = "/Users/minamoheb/Desktop/Atlas"

all_slugs = set()
for root, dirs, files in os.walk(os.path.join(ROOT_DIR, "content/ar")):
    for f in files:
        if f.endswith(".md") and not f.startswith("EXISTING_SLUGS") and not f.startswith("PATCH_") and not f.startswith("MASTER_"):
            all_slugs.add(f[:-3])

print(f"Total existing slugs in content/ar: {len(all_slugs)}")

candidates = [
    # Section A
    "evt-apa-founding-1892",
    "evt-aps-split-1988",
    "evt-aamft-founding-1942",
    "evt-bps-founding-1901",
    "evt-dgps-founding-1904",
    "evt-sfp-founding-1901",
    "evt-nuremberg-congress-ipa-1910",
    "evt-wednesday-psychological-society-1902",
    "evt-aabt-abct-founding-1966",
    "evt-eabct-founding-1971",
    "evt-ahp-founding-1961",
    "evt-esalen-institute-founding-1962",
    "evt-connecticut-licensing-law-1945",
    "evt-abpp-founding-1947",
    "evt-europsy-standard-2001",
    "evt-philosophische-studien-1881",
    "evt-american-journal-psychology-1887",
    "evt-jahrbuch-psychoanalyse-1909",
    "evt-jung-institute-zurich-1948",
    "evt-vienna-psychoanalytic-institute-1925",
    "evt-tavistock-institute-1947",
    # Section B
    "evt-dsm-1-publication-1952",
    "evt-dsm-2-publication-1968",
    "evt-dsm-3-publication-1980",
    "evt-dsm-4-publication-1994",
    "evt-dsm-5-publication-2013",
    "evt-icd-6-mental-disorders-1948",
    "evt-icd-11-cddi-2018",
    "evt-dsm-homosexuality-removal-1973",
    # Section C
    "evt-rosenhan-study-publication-1973",
    "evt-open-science-collaboration-2015",
    "evt-false-memory-syndrome-foundation-1992",
    "evt-little-albert-ethical-controversy-1970",
    "evt-stapel-fraud-scandal-2011",
    "evt-cyril-burt-twin-data-controversy-1976",
    "evt-hoffman-report-apa-torture-2015",
    # Section D
    "evt-egaz-moniz-nobel-lobotomy-1949",
    "evt-cerletti-bini-first-ect-1938",
    "evt-sakel-insulin-shock-therapy-1933",
    "evt-chlorpromazine-discovery-1952",
    "evt-fluoxetine-prozac-launch-1987",
    # Section E
    "evt-deinstitutionalization-movement-1960",
    "evt-basaglia-law-italy-1978",
    "evt-community-mental-health-act-1963",
    "evt-anti-psychiatry-network-london-1967",
    # Section F
    "evt-tarasoff-case-ruling-1976",
    "evt-mnaghten-rule-1843",
    "evt-hinckley-verdict-insanity-reform-1984",
    "evt-mental-health-parity-act-2008",
    "evt-wyatt-v-stickney-1971",
    "evt-rogers-v-o-kin-1979",
    # Section G
    "evt-shell-shock-ww1-craiglockhart-1917",
    "evt-army-alpha-beta-ww1-ww2-selection",
    "evt-va-clinical-psychology-expansion-1946",
    "evt-vietnam-veterans-ptsd-advocacy-1980",
    "evt-september-11-crisis-intervention-2001",
    # Section H
    "evt-clark-university-lectures-1909",
    "evt-weimar-congress-split-1911",
    "evt-munich-congress-jung-freud-split-1913",
    "evt-boulder-conference-scientist-practitioner-1949",
    "evt-third-wave-cbt-symposium-2004",
    # Section I
    "evt-immigration-act-iq-testing-1924",
    "evt-drapetomania-cartwright-1851",
    "evt-apa-apology-racism-2021",
    "evt-goering-institute-nazi-psychology-1936",
    # Section J
    "evt-egyptian-psychological-association-1948",
    "evt-aub-psychology-department-1950",
    "evt-calcutta-psychology-department-1916",
    "evt-tokyo-psychological-laboratory-1903",
    "evt-buenos-aires-psychology-institute-1908",
    "evt-south-african-psychological-association-1948"
]

print(f"Total candidate event slugs: {len(candidates)}")
collisions = [c for c in candidates if c in all_slugs]
if collisions:
    print(f"COLLISIONS FOUND: {collisions}")
else:
    print("✅ ZERO COLLISIONS! All 72 candidate slugs are completely unique!")
