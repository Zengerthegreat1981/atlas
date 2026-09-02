#!/usr/bin/env python3
"""Apply school connection actions."""
import json
import re
import sys


def apply_action(action, dry_run=True):
    """Add target to source's related section."""
    source_slug = action['source']
    target_slug = action['target']
    target_title = action['target_title']
    source_path = action['source_path']
    source_related = action['source_related']
    source_type = action['source_type']

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if target_slug in source_related:
        return False, "already linked"

    # Find the type of the target
    target_type = source_type  # default; will be overridden by lookup

    m_rel = re.search(r'(related:\s*\n)((?:[ \t]*-\s*id:.*\n?)+)', content)
    if m_rel:
        rel_start = m_rel.start(1)
        rel_text = m_rel.group(2)
        new_entry = f'  - id: "{target_slug}", title: "{target_title}", type: "{target_type}"\n'
        new_rel_text = rel_text + new_entry
        new_content = content[:rel_start] + 'related:\n' + new_rel_text + content[m_rel.end():]
    else:
        m_gaps = re.search(r'(gaps:\s*\n)', content)
        if m_gaps:
            insert_pos = m_gaps.start(1)
            new_block = f"related:\n  - id: \"{target_slug}\", title: \"{target_title}\", type: \"{target_type}\"\n\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
        else:
            m_end = re.search(r'\n---\s*\n', content)
            if not m_end:
                return False, "no end of frontmatter"
            insert_pos = m_end.start()
            new_block = f"\nrelated:\n  - id: \"{target_slug}\", title: \"{target_title}\", type: \"{target_type}\"\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]

    if not dry_run:
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return True, "added"


def main(dry_run=False):
    with open('/tmp/minimax_school_actions_safe.json', 'r') as f:
        actions = json.load(f)

    print(f"Applying {len(actions)} school actions (dry_run={dry_run})")
    success = 0
    skipped = 0
    errors = 0
    for a in actions:
        ok, msg = apply_action(a, dry_run=dry_run)
        if ok:
            success += 1
        elif "already" in msg:
            skipped += 1
        else:
            errors += 1
            print(f"  ERROR: {a['source']} -> {a['target']}: {msg}")

    print(f"\n=== Results ===")
    print(f"  Success: {success}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")


if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    main(dry_run=dry)
