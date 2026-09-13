#!/usr/bin/env python3
"""
Apply orphan-connection actions to files.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import json
import sys
import os

APPROVED_BASE = _ATLAS_ROOT + "/content/ar"


def apply_action(action, dry_run=True):
    """Apply a single action: add orphan_slug to referrer's related section."""
    orphan_slug = action['orphan_slug']
    referrer_path = action['referrer_path']
    orphan_title = action['orphan_title']

    with open(referrer_path, 'r', encoding='utf-8') as f:
        content = f.read()

    import re

    # Get referrer's type
    m_type = re.search(r'^type:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    referrer_type = m_type.group(1).strip() if m_type else 'مفكر'

    # Find related block
    m_rel = re.search(r'(related:\s*\n)((?:[ \t]*-\s*id:.*\n?)+)', content)
    if not m_rel:
        # No related section — create one before gaps or end of frontmatter
        m_gaps = re.search(r'(gaps:\s*\n)', content)
        if m_gaps:
            insert_pos = m_gaps.start(1)
            new_block = f"related:\n  - id: \"{orphan_slug}\", title: \"{orphan_title}\", type: \"{referrer_type}\"\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
        else:
            # Add at end of frontmatter
            m_end = re.search(r'\n---\s*\n', content)
            if not m_end:
                return False, "no end of frontmatter found"
            insert_pos = m_end.start()
            new_block = f"\nrelated:\n  - id: \"{orphan_slug}\", title: \"{orphan_title}\", type: \"{referrer_type}\"\n"
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
    else:
        rel_start = m_rel.start(1)
        rel_text = m_rel.group(2)
        # Check if already there
        if f'"{orphan_slug}"' in rel_text:
            return False, "already in related"
        new_entry = f'  - id: "{orphan_slug}", title: "{orphan_title}", type: "{referrer_type}"\n'
        new_rel_text = rel_text + new_entry
        new_content = content[:rel_start] + 'related:\n' + new_rel_text + content[m_rel.end():]

    if not dry_run:
        with open(referrer_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return True, "added"


def main(dry_run=False):
    with open('/tmp/minimax_orphan_actions.json', 'r') as f:
        actions = json.load(f)

    print(f"Applying {len(actions)} actions (dry_run={dry_run})")
    success = 0
    skipped = 0
    errors = 0
    error_details = []

    for a in actions:
        ok, msg = apply_action(a, dry_run=dry_run)
        if ok:
            success += 1
        else:
            if msg == "already in related":
                skipped += 1
            else:
                errors += 1
                error_details.append((a['orphan_slug'], a['referrer_slug'], msg))

    print(f"\n=== Results ===")
    print(f"  Success: {success}")
    print(f"  Skipped (already linked): {skipped}")
    print(f"  Errors: {errors}")
    if errors > 0:
        print(f"\n=== Error details ===")
        for orphan, referrer, msg in error_details[:10]:
            print(f"  {referrer} → {orphan}: {msg}")


if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    main(dry_run=dry)
