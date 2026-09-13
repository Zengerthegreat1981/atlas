#!/usr/bin/env python3
"""
fix_all_slug_references.py
Maps referenced slugs in related: and edges: to canonical on-disk slugs across Atlas.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import re
from pathlib import Path

CONTENT_AR = Path(_ATLAS_ROOT + '/content/ar')

# Exact mapping from old/referenced slugs to canonical on-disk slugs
SLUG_REPLACEMENTS = {
    'thk-popper': 'thk-karl-popper',
    'thk-dchalmers': 'thk-david-chalmers',
    'thk-gassendi': 'thk-pierre-gassendi',
    'thk-galileo': 'thk-galileo-galilei',
    'thk-newton': 'thk-isaac-newton',
    'thk-adam-smith': 'thk-adam-smith',
    'thk-ffanon': 'thk-fanon',
    'thk-dussel': 'thk-enrique-dussel',
    'thk-petrarch': 'thk-petrarca',
    'thk-pico-della-mirandola': 'thk-pico',
    'thk-seligman': 'thk-mseligman',
    'thk-perls': 'thk-fperls',
    'thk-marcusaurelius': 'thk-marcus-aurelius',
    'thk-mboss': 'thk-boss',
    'thk-kandel': 'thk-ekandel',
    'thk-davanloo': 'thk-hdavanloo',
    'thk-porges': 'thk-stephen-porges',
    'thk-rschwartz': 'thk-richard-schwartz',
    'thk-sue-johnson': 'thk-sjohnson',
    'thk-paul-gilbert': 'thk-pgilbert',
    'thk-harville-hendrix': 'thk-hhendrix',
    'thk-michael-white': 'thk-mwhite',
    'thk-steve-de-shazer': 'thk-sdeshazer',
    'thk-jmark-williams': 'thk-mwilliams',
    'thk-malik-badri': 'thk-mbadri',
    'thk-yellow-horse-brave-heart': 'thk-mbraveheart',
    'thk-duran': 'thk-eduardo-duran',
    'thk-nobles': 'thk-wade-nobles',
    'thk-akbar': 'thk-wdowling',
    'thk-augustine-hippo': 'thk-augustine',
    'thk-einstein': 'thk-albert-einstein',
    'thk-girard': 'thk-rene-girard',
    'thk-tolstoy': 'thk-leo-tolstoy',
    'thk-tszasz': 'thk-szasz',
    'thk-iyalom': 'thk-yalom',
    'thk-linehan': 'thk-mlinehan',
    'thk-amos-tversky': 'thk-amos-tversky',
    'thk-david-buss': 'thk-david-buss',
    'thk-stephen-jay-gould': 'thk-stephen-jay-gould',
    'thk-andy-clark': 'thk-andy-clark',
    'thk-dawkins': 'thk-richard-dawkins',
    'thk-feynman': 'thk-richard-feynman',
    'thk-jyoung': 'thk-young-jeffrey',
    'thk-putnam': 'thk-hilary-putnam',
    'wrk-heidegger-being-and-time': 'wrk-being-and-time-heidegger',
    'thk-quine': 'thk-wquine',
    'thk-avicenna': 'thk-ibn-sina',
    'thk-rumi': 'thk-jalal-al-din-rumi',
    'thk-russell': 'thk-bertrand-russell',
    'thk-david-hume': 'thk-hume',
    'thk-john-locke': 'thk-locke',
    'thk-wbion': 'thk-bion',
    'thk-baudrillard': 'thk-jean-baudrillard',
    'thk-jsmill': 'thk-mill',
    'thk-carol-gilligan': 'thk-gilligan',
    'thk-nodding': 'thk-nel-noddings',
    'thk-erich-fromm': 'thk-fromm',
    'wrk-escape-from-freedom-fromm': 'wrk-fromm-escape-freedom',
    'wrk-open-society-popper': 'wrk-popper-open-society',
    'stu-milgram-obedience-authority': 'stu-milgram-obedience',
    'thk-wilber': 'thk-kwilber',
    'thk-john-dewey': 'thk-dewey',
    'thk-jankelevitch': 'thk-vladimir-jankelevitch',
    'thk-epicurus': 'thk-epicur',
    'thk-wittgenstein': 'thk-lwittgenstein',
    'wrk-beyond-the-pleasure-principle-freud': 'wrk-freud-beyond-pleasure-principle',
    'thk-paul-tillich': 'thk-tillich',
    'thk-frege': 'thk-gottlob-frege',
    'wrk-nietzsche-genealogy-of-morality': 'wrk-on-the-genealogy-of-morals-nietzsche',
    'trm-care-ethics-vs-justice-ethics': 'con-care-ethics',
    'stu-strange-situation-ainsworth': 'stu-ainsworth-strange-situation',
    'thk-jbowlby': 'thk-bowlby',
    'wrk-attachment-bowlby': 'wrk-attachment-loss-volume1',
    'thk-fshapiro': 'thk-francine-shapiro',
    'tec-emdr-standard-protocol': 'tec-emdr-eight-phase-protocol',
    'thk-aellis': 'thk-ellis',
    'con-depression-assessment': 'dis-major-depressive',
    'thk-kabat-zinn': 'thk-jkabat-zinn',
    'thk-edward-said': 'thk-said',
    'stu-asch-conformity-experiment': 'stu-asch-conformity',
    'wrk-foucault-discipline-and-punish': 'wrk-discipline-and-punish-foucault',
}

# Apply replacements across all markdown files in content/ar
updated_files = 0
for f in CONTENT_AR.rglob('*.md'):
    if 'drafts' in f.parts:
        continue
    txt = f.read_text(encoding='utf-8')
    orig_txt = txt
    for old_s, new_s in SLUG_REPLACEMENTS.items():
        txt = re.sub(rf'(id:\s*\"{re.escape(old_s)}\")', f'id: "{new_s}"', txt)
        txt = re.sub(rf'(target:\s*\"{re.escape(old_s)}\")', f'target: "{new_s}"', txt)
    
    if txt != orig_txt:
        f.write_text(txt, encoding='utf-8')
        updated_files += 1

print(f"Updated {updated_files} files with canonical slug mappings.")
