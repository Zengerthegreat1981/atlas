#!/usr/bin/env python3
"""
Validate anthropology depth expansion nodes for quality standards.
Checks: word count, sources, structure, cross-references, citations.
"""

import os
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

def count_words(text):
    """Count words in a text string (excluding markdown)."""
    # Remove markdown syntax
    text = re.sub(r'[#*`\[\]()]', '', text)
    # Split and count
    return len(text.split())

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    lines = content.split('\n')
    if not lines[0].startswith('---'):
        return None, content

    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].startswith('---'):
            fm_end = i
            break

    if fm_end is None:
        return None, content

    fm_text = '\n'.join(lines[1:fm_end])
    body = '\n'.join(lines[fm_end+1:])

    # Parse simple YAML
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"\'')
            fm[key] = val

    return fm, body

def validate_node(filepath):
    """Validate a single node file."""
    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': f"Cannot read file: {e}"}

    # Extract frontmatter and body
    fm, body = extract_frontmatter(content)

    if not fm:
        errors.append("Missing YAML frontmatter")
    else:
        # Check required fields
        required = ['slug', 'id', 'type', 'part', 'level', 'title', 'en']
        for field in required:
            if field not in fm:
                errors.append(f"Missing required field: {field}")

        # Check part
        if fm.get('part') != 'anthropology':
            errors.append(f"part field is '{fm.get('part')}', should be 'anthropology'")

    # Count words in body (skip frontmatter)
    body_text = body.split('\n', 1)[1] if '\n' in body else body
    wordcount = count_words(body_text)

    if wordcount < 1200:
        errors.append(f"Content too short: {wordcount} words (need 1,200+)")
    elif wordcount > 1600:
        warnings.append(f"Content may be too long: {wordcount} words (target 1,200-1,600)")

    # Check sections (should have ## headers)
    sections = body.count('\n## ')
    if sections < 5:
        warnings.append(f"Only {sections} major sections (target 5-8)")
    elif sections > 8:
        warnings.append(f"Has {sections} major sections (target 5-8, but acceptable)")

    # Check for sources section
    if 'source' not in body.lower() and 'reference' not in body.lower() and 'bibliography' not in body.lower():
        warnings.append("No apparent sources section")

    # Count reference-like patterns
    source_patterns = [
        r'\[\d+\]',  # Numbered references
        r'\(.*?19\d\d\)',  # Year patterns
        r'\(.*?20\d\d\)',
        r'\*\*[A-Z].*?\(.*?\)',  # Bold names with parens
    ]
    ref_count = 0
    for pattern in source_patterns:
        ref_count += len(re.findall(pattern, body))

    if ref_count < 3:
        warnings.append(f"May have insufficient sources (found {ref_count} source indicators, need 3-5)")

    # Check for related/edges
    if 'related:' in body or 'edges:' in body:
        # Good sign they have cross-references
        pass
    else:
        warnings.append("No clear edges/related cross-references found")

    # Check for ethnographic examples
    ethnographic_keywords = ['ethnograph', 'fieldwork', 'observed', 'studied', 'research', 'example', 'case']
    ethnographic_score = sum(1 for keyword in ethnographic_keywords if keyword in body.lower())
    if ethnographic_score < 3:
        warnings.append("Limited ethnographic examples apparent")

    return {
        'filepath': str(filepath),
        'filename': os.path.basename(filepath),
        'wordcount': wordcount,
        'sections': sections,
        'ref_count': ref_count,
        'errors': errors,
        'warnings': warnings,
        'status': 'PASS' if not errors else 'FAIL'
    }

def validate_directory(dirpath, pattern='*anthropology*.md'):
    """Validate all anthropology nodes in a directory."""
    results = defaultdict(list)

    path = Path(dirpath)
    files = sorted(path.glob(pattern)) + sorted(path.glob('con-*.md')) + sorted(path.glob('thk-*.md'))

    # Filter to only part: anthropology
    anthropology_files = []
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                if 'part: "anthropology"' in fh.read():
                    anthropology_files.append(f)
        except:
            pass

    total = len(anthropology_files)
    passed = 0

    for filepath in anthropology_files:
        result = validate_node(filepath)
        results[result['status']].append(result)
        if result['status'] == 'PASS':
            passed += 1

    return {
        'total_files': total,
        'passed': passed,
        'failed': total - passed,
        'pass_rate': f"{100*passed/total if total > 0 else 0:.1f}%",
        'results': dict(results)
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Validate anthropology depth nodes')
    parser.add_argument('--dir', default='/Users/mina/Desktop/Atlas/content/ar', help='Content directory')
    parser.add_argument('--type', default='all', help='Node type to validate: all, concepts, thinkers, studies, works')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Map type to directory pattern
    type_dirs = {
        'all': ['concepts', 'thinkers', 'studies', 'works', 'schools'],
        'concepts': ['concepts'],
        'thinkers': ['thinkers'],
        'studies': ['studies'],
        'works': ['works'],
        'schools': ['schools'],
    }

    total_results = {
        'total_files': 0,
        'passed': 0,
        'failed': 0,
        'by_type': {}
    }

    for node_type in type_dirs.get(args.type, []):
        dirpath = os.path.join(args.dir, node_type)
        if not os.path.exists(dirpath):
            print(f"Skipping {node_type} (directory not found)")
            continue

        print(f"\nValidating {node_type}...")
        results = validate_directory(dirpath)

        total_results['total_files'] += results['total_files']
        total_results['passed'] += results['passed']
        total_results['failed'] += results['failed']
        total_results['by_type'][node_type] = results

        print(f"  {results['passed']}/{results['total_files']} passed ({results['pass_rate']})")

        if args.verbose and results['results'].get('FAIL'):
            for fail in results['results']['FAIL'][:3]:
                print(f"\n  FAIL: {fail['filename']}")
                for error in fail['errors']:
                    print(f"    ERROR: {error}")
                for warning in fail['warnings'][:2]:
                    print(f"    WARNING: {warning}")

    # Summary
    print("\n" + "="*60)
    print(f"TOTAL: {total_results['passed']}/{total_results['total_files']} nodes passed")
    print(f"Pass rate: {100*total_results['passed']/total_results['total_files'] if total_results['total_files'] > 0 else 0:.1f}%")

    if total_results['failed'] > 0:
        print(f"\n⚠️  {total_results['failed']} nodes failed validation")
        sys.exit(1)
    else:
        print("\n✓ All nodes passed validation")
        sys.exit(0)

if __name__ == '__main__':
    main()
