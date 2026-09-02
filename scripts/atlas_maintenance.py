#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_maintenance.py — صيانة دورية تلقائية أثناء عمل background workers.

يعالج:
  M1: إغلاق الـorphans
  M2: إصلاح phantoms (يبحث عن slug مشابه ويستخدمه)
  M3: إعادة بناء EXISTING_SLUGS

الاستخدام:
  python3 scripts/atlas_maintenance.py
"""
import os, re, sys, json
import subprocess

ROOT = '/Users/minamoheb/Desktop/Atlas'
AR = os.path.join(ROOT, 'content/ar')

TYPES = {
    'schools': 'مدرسة', 'concepts': 'مفهوم', 'works': 'عمل / كتاب',
    'thinkers': 'مفكر', 'debates': 'جدل', 'critiques': 'نقد خارجي موثَّق',
    'instruments': 'أداة قياس', 'studies': 'دراسة وبحث', 'techniques': 'تقنية/تدخل علاجي',
    'events': 'حدث تاريخي', 'branches': 'تيار', 'syndromes': 'متلازمة',
    'disorders': 'اضطراب/حالة إكلينيكية', 'axioms': 'مبدأ/بديهية',
    'contexts': 'سياق/تقليد', 'experiences': 'تجربة', 'metaphors': 'استعارة',
    'questions': 'سؤال', 'terms': 'مصطلح', 'dialogues': 'حوار', 'relations': 'علاقة بين مدرستين',
}

def close_orphans():
    """Close all orphans by adding incoming references."""
    if not os.path.exists('/tmp/minimax_orphans.json'):
        return 0
    with open('/tmp/minimax_orphans.json', encoding='utf-8') as fh:
        data = json.load(fh)
    added = 0
    for typ, items in data['by_type'].items():
        folder = f'{AR}/{typ}'
        if not os.path.isdir(folder): continue
        for item in items:
            slug = item['slug']
            title = item['title']
            type_label = TYPES.get(typ, typ)
            new_entry = f'- id: "{slug}", title: "{title}", type: "{type_label}"\n'
            for f in os.listdir(folder):
                if not f.endswith('.md') or f.startswith('_'): continue
                if f == f'{slug}.md': continue
                fp = f'{folder}/{f}'
                with open(fp, encoding='utf-8') as fh:
                    c = fh.read()
                if f'id: "{slug}"' in c: continue
                m = re.search(r'(related:\s*\n(?:\s*-\s+id:[^\n]*\n)*)', c, re.MULTILINE)
                if m:
                    block = m.group(1)
                    new_block = block + new_entry
                    new_c = c[:m.start(1)] + new_block + c[m.end(1):]
                    with open(fp, 'w', encoding='utf-8') as fh:
                        fh.write(new_c)
                    added += 1
                    break
    return added

def fix_phantoms():
    """Find phantom slugs and replace with closest existing slug."""
    # Run integrity audit to get phantoms
    result = subprocess.run(['python3', 'scripts/spark_integrity_audit.py'],
                          capture_output=True, text=True, cwd=ROOT)
    output = result.stdout
    # Parse phantoms
    phantoms = []
    in_phantoms = False
    for line in output.split('\n'):
        if 'Phantom IDs and potential matches:' in line:
            in_phantoms = True
            continue
        if in_phantoms:
            m = re.match(r'\s*PHANTOM:\s*\'([^\']+)\'\s*\(in\s+\d+\s+files:\s*([^)]+)\)\s*->\s*matches:\s*\[([^\]]*)\]', line)
            if m:
                phantom = m.group(1)
                files = [f.strip().rstrip('.,') for f in m.group(2).split(':')[-1].split(',') if f.strip()]
                matches_str = m.group(3).strip()
                matches = [s.strip().strip("'\"") for s in matches_str.split(',') if s.strip().strip("'\"")]
                phantoms.append((phantom, files, matches))

    fixed = 0
    for phantom, files, matches in phantoms:
        # Choose best match
        replacement = None
        if matches and matches[0] and matches[0] != phantom:
            replacement = matches[0]
        else:
            # Try to find a similar slug in EXISTING_SLUGS
            slugs = set()
            try:
                with open(f'{AR}/drafts/EXISTING_SLUGS.md', encoding='utf-8') as fh:
                    for line in fh:
                        m = re.match(r'^- `([^`]+)`', line)
                        if m: slugs.add(m.group(1))
            except: pass
            # Find by partial match
            phantom_short = phantom.replace('-', '')
            for s in slugs:
                if s == phantom: continue
                if phantom_short in s.replace('-', '') or s.replace('-', '') in phantom_short:
                    if not replacement or len(s) < len(replacement):
                        replacement = s
        if not replacement: continue

        # Apply fix
        for file_path in files:
            fp = f'{AR}/{file_path}'
            if not os.path.exists(fp): continue
            with open(fp, encoding='utf-8') as fh:
                c = fh.read()
            new_c = c.replace(f'id: "{phantom}"', f'id: "{replacement}"')
            if new_c != c:
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.write(new_c)
                fixed += 1
    return fixed

def rebuild_index():
    """Rebuild EXISTING_SLUGS.md."""
    subprocess.run(['python3', 'scripts/build_slug_index.py'],
                  cwd=ROOT, capture_output=True)
    return True

def main():
    print("=" * 50)
    print("M1: Close orphans")
    n_orphans = close_orphans()
    print(f"  Added {n_orphans} incoming references")
    print()

    print("=" * 50)
    print("M2: Fix phantoms")
    n_phantoms = fix_phantoms()
    print(f"  Fixed {n_phantoms} phantom references")
    print()

    print("=" * 50)
    print("M3: Rebuild slug index")
    rebuild_index()
    print("  Done")
    print()

    # Final status
    print("=" * 50)
    print("Final status")
    result = subprocess.run(['python3', 'scripts/minimax_orphan_audit.py'],
                          capture_output=True, text=True, cwd=ROOT)
    for line in result.stdout.split('\n')[:5]:
        print(f"  {line}")
    print()
    result = subprocess.run(['python3', 'scripts/spark_integrity_audit.py'],
                          capture_output=True, text=True, cwd=ROOT)
    for line in result.stdout.split('\n')[-8:]:
        if line.strip(): print(f"  {line}")

if __name__ == '__main__':
    main()
