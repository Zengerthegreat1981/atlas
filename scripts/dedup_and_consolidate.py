#!/usr/bin/env python3
"""
dedup_and_consolidate.py
Performs complete deduplication and reference reconciliation across all categories in Atlas.
  - Merges duplicate thinkers, concepts, works, and techniques
  - Redirects all incoming/outgoing pointers to the canonical slug
  - Cleans up deprecated files
  - Rebuilds indexes, matrices, and live production build
"""

import os
import re
import sys
import json
from pathlib import Path
from collections import defaultdict

ATLAS_ROOT = Path('/Users/minamoheb/Desktop/Atlas')
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'

RELATED_ITEM_RE = re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')

DUPLICATE_PAIRS = [
    # Thinkers
    ('thk-michael-sandel', 'thk-sandel'),
    ('thk-dellis', 'thk-ellis'),
    ('thk-charles-sanders-peirce', 'thk-peirce'),
    ('thk-peter-levine', 'thk-plevine'),
    ('thk-saul-kripke', 'thk-skripke'),
    ('thk-john-dewey', 'thk-dewey'),
    ('thk-al-maturidi', 'thk-maturidi'),
    ('thk-hannah-arendt', 'thk-arendt'),
    ('thk-mcsikszentmihalyi', 'thk-csikszentmihalyi'),
    ('thk-thomas-nagel', 'thk-nagel'),
    ('thk-jean-paul-sartre', 'thk-sartre'),
    ('thk-edmund-husserl', 'thk-husserl'),
    ('thk-paul-ricoeur', 'thk-ricoeur'),
    ('thk-hans-georg-gadamer', 'thk-gadamer'),
    ('thk-deb-dana', 'thk-dana'),
    ('thk-jurgen-habermas', 'thk-habermas'),
    ('thk-brussell', 'thk-bertrand-russell'),
    ('thk-ludwig-wittgenstein', 'thk-lwittgenstein'),
    ('thk-albert-camus', 'thk-camus'),
    ('thk-emmanuel-levinas', 'thk-levinas'),
    ('thk-alain-badiou', 'thk-badiou'),
    ('thk-jacques-lacan', 'thk-lacan'),
    ('thk-fakhr-al-din-al-razi', 'thk-fakhr-razi'),
    ('thk-abu-al-hasan-al-ashari', 'thk-ashari'),
    ('thk-walter-mignolo', 'thk-mignolo'),
    ('thk-shapiro', 'thk-francine-shapiro'),
    ('thk-simone-de-beauvoir', 'thk-beauvoir'),
    ('thk-jamal-al-din-al-afghani', 'thk-afghani'),
    ('thk-gilles-deleuze', 'thk-deleuze'),
    ('thk-judith-butler', 'thk-butler'),
    ('thk-kitaro-nishida', 'thk-nishida'),
    ('thk-charles-taylor', 'thk-charlestaylor'),
    ('thk-michel-foucault', 'thk-foucault'),
    ('thk-slavoj-zizek', 'thk-sljizek'),
    ('thk-w-v-o-quine', 'thk-wquine'),
    ('thk-william-of-ockham', 'thk-william-ockham'),
    ('thk-wilfrid-sellars', 'thk-wsellars'),
    ('thk-leopold-senghor', 'thk-senghor'),
    ('thk-adamasio', 'thk-damasio'),
    ('thk-keiji-nishitani', 'thk-nishitani'),
    ('thk-herbert-spencer', 'thk-spencer'),
    ('thk-john-rawls', 'thk-rawls'),
    ('thk-carol-gilligan', 'thk-gilligan'),
    ('thk-henry-david-thoreau', 'thk-thoreau'),
    ('thk-abu-bakr-al-razi', 'thk-al-razi-abu-bakr'),
    ('thk-john-stuart-mill', 'thk-mill'),
    ('thk-zaki-naguib-mahmoud', 'thk-zmahmoud'),
    ('thk-martin-buber', 'thk-buber'),
    ('thk-pogden-hakomi', 'thk-pogden'),
    ('thk-alasdair-macintyre', 'thk-macintyre'),
    ('thk-smilgram', 'thk-stanley-milgram'),
    ('thk-rudolf-carnap', 'thk-rcarnap'),
    ('thk-sadiq-jalal-al-azm', 'thk-alazm'),
    ('thk-robert-nozick', 'thk-nozick'),
    ('thk-achille-mbembe', 'thk-mbembe'),
    ('thk-jacques-derrida', 'thk-derrida'),
    ('thk-pzimbardo', 'thk-philip-zimbardo'),
    ('thk-herbert-marcuse', 'thk-marcuse'),
    ('thk-hayes-steven', 'thk-lstevenhayes'),
    ('thk-dfosha', 'thk-fosha'),
    ('thk-rlaing', 'thk-laing'),
    ('thk-vtausk', 'thk-tausk'),
    ('thk-psinger', 'thk-peter-singer'),
    ('thk-ilovaas', 'thk-lovaas'),
    ('thk-masondurie', 'thk-trore'),
    
    # Works
    ('wrk-emotional-intelligence-1995', 'wrk-emotional-intelligence'),
    
    # Concepts
    ('con-hard-problem-of-consciousness-chalmers', 'con-hard-problem-of-consciousness'),
    ('con-flow-csikszentmihalyi', 'con-flow'),
    ('con-miswak-attachment-styles', 'con-secure-attachment'),
]

def find_file(slug):
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'drafts']
        for f in files:
            if f == f'{slug}.md':
                return Path(root) / f
    return None

def merge_and_dedup():
    print('========================================')
    print('DEDUPLICATION & CANONICAL NORMALIZATION')
    print('========================================')
    
    redirect_map = {}
    merged_count = 0
    
    for dep_slug, can_slug in DUPLICATE_PAIRS:
        p_dep = find_file(dep_slug)
        p_can = find_file(can_slug)
        
        if p_dep and p_can:
            redirect_map[dep_slug] = can_slug
            txt_dep = p_dep.read_text(encoding='utf-8')
            txt_can = p_can.read_text(encoding='utf-8')
            
            if len(txt_dep) > len(txt_can):
                base_txt = txt_dep
                other_txt = txt_can
                base_txt = re.sub(r'^slug:\s*"[^"]*"', f'slug: "{can_slug}"', base_txt, flags=re.M)
            else:
                base_txt = txt_can
                other_txt = txt_dep
                
            m_other_rel = re.findall(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"', other_txt)
            for rid, rtitle, rtype in m_other_rel:
                if rid != dep_slug and rid != can_slug and rid not in base_txt:
                    rel_line = f'  - id: "{rid}", title: "{rtitle}", type: "{rtype}"'
                    if 'related:\n' in base_txt:
                        base_txt = base_txt.replace('related:\n', f'related:\n{rel_line}\n', 1)
                    elif 'related:  []' in base_txt:
                        base_txt = base_txt.replace('related:  []', f'related:\n{rel_line}', 1)
                        
            p_can.write_text(base_txt, encoding='utf-8')
            p_dep.unlink()
            merged_count += 1
            print(f'Merged {dep_slug} -> {can_slug} (kept {p_can.name})')
        elif p_dep and not p_can:
            redirect_map[dep_slug] = can_slug
            p_target = p_dep.parent / f'{can_slug}.md'
            txt = p_dep.read_text(encoding='utf-8')
            txt = re.sub(r'^slug:\s*"[^"]*"', f'slug: "{can_slug}"', txt, flags=re.M)
            p_target.write_text(txt, encoding='utf-8')
            p_dep.unlink()
            merged_count += 1
            print(f'Renamed {dep_slug} -> {can_slug}')
            
    print(f'\nTotal duplicate entities consolidated: {merged_count}')
    
    print('\nUpdating all references across the atlas...')
    updated_files = 0
    
    all_files = []
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'drafts']
        for f in files:
            if f.endswith('.md') and f != 'EXISTING_SLUGS.md':
                all_files.append(Path(root) / f)
                
    for p in all_files:
        txt = p.read_text(encoding='utf-8')
        orig_txt = txt
        for dep_slug, can_slug in redirect_map.items():
            if dep_slug in txt:
                txt = re.sub(r'id:\s*"' + re.escape(dep_slug) + r'"', f'id: "{can_slug}"', txt)
                txt = re.sub(r'target:\s*"' + re.escape(dep_slug) + r'"', f'target: "{can_slug}"', txt)
                
        if txt != orig_txt:
            p.write_text(txt, encoding='utf-8')
            updated_files += 1
            
    print(f'Reference reconciliation complete: {updated_files} files updated with canonical slugs.')

def rebuild_all():
    print('\n========================================')
    print('REBUILDING SLUG INDEX, MATRICES & ATLAS')
    print('========================================')
    
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_slug_index.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_coverage_matrix.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_philosophy_matrix.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_atlas.py ar')
    
    data_json = ATLAS_ROOT / 'data.json'
    index_html = ATLAS_ROOT / 'index.html'
    
    with open(data_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    nodes_count = len(data.get('nodes', {}))
    html_size = index_html.stat().st_size
    
    print(f'\nFinal Production Release Status:')
    print(f'  Unique Canonical Nodes: {nodes_count:,}')
    print(f'  index.html size: {html_size:,} bytes ({html_size / (1024*1024):.2f} MB)')

def main():
    merge_and_dedup()
    rebuild_all()

if __name__ == '__main__':
    main()
