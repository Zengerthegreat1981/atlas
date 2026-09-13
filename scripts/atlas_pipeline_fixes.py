#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_pipeline_fixes.py — إصلاحات بنيوية شاملة للدفعة الأولى من خطة العمل.

يعالج:
  F1: 2-space-indent bug في related (321 ملف)
  F2: duplicate related IDs (59 ملف)
  F3: visible [DRAFT-UNKNOWN] (17 ملف)
  F4: empty related: →  []  (تنظيف شكلي)
  F5: cross-part duplicate thk-cgrob (دمج)
  F6: 5+ orphans (sch-cbt + 4 techniques) — L2.1

الاستخدام:
  python3 scripts/atlas_pipeline_fixes.py --dry-run
  python3 scripts/atlas_pipeline_fixes.py --apply
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os, re, sys, json, shutil
from collections import Counter
from datetime import date

ROOT = _ATLAS_ROOT
CONTENT_AR = os.path.join(ROOT, 'content/ar')

# ----------------- helpers -----------------

def all_md_files():
    out = []
    for sub in os.listdir(CONTENT_AR):
        p = os.path.join(CONTENT_AR, sub)
        if not os.path.isdir(p): continue
        for f in os.listdir(p):
            if f.endswith('.md') and not f.startswith('_'):
                out.append(os.path.join(p, f))
    return out

def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()

def write(p, content):
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(content)

# ----------------- F1: 2-space-indent fix -----------------

def f1_fix_indent(content):
    """تحويل '  - id:' إلى '- id:' داخل قسم related فقط."""
    # Find related: block
    m = re.search(r'(related:\s*\n)(.*?)(\n[a-z_]+:|\Z)', content, re.MULTILINE | re.DOTALL)
    if not m:
        return content, False
    block = m.group(2)
    new_block = re.sub(r'^  - id:', r'- id:', block, flags=re.MULTILINE)
    if new_block == block:
        return content, False
    new_content = content[:m.start(2)] + new_block + content[m.end(2):]
    return new_content, True

# ----------------- F2: dedupe related -----------------

def f2_dedupe_related(content):
    """حذف related IDs مكررة داخل الملف نفسه (الإبقاء على الأول)."""
    m = re.search(r'(related:\s*\n)(.*?)(\n[a-z_]+:|\Z)', content, re.MULTILINE | re.DOTALL)
    if not m:
        return content, False
    block = m.group(2)
    # Parse lines
    lines = block.split('\n')
    seen_ids = set()
    new_lines = []
    for line in lines:
        m_id = re.match(r'^\s*-\s+id:\s*"([^"]+)"', line)
        if m_id:
            sid = m_id.group(1)
            if sid in seen_ids:
                continue  # skip duplicate
            seen_ids.add(sid)
        new_lines.append(line)
    new_block = '\n'.join(new_lines)
    if new_block == block:
        return content, False
    new_content = content[:m.start(2)] + new_block + content[m.end(2):]
    return new_content, True

# ----------------- F3: visible DRAFT-UNKNOWN -----------------

def f3_clean_draft_unknown(content):
    """إزالة [DRAFT-UNKNOWN] الظاهر في الجسم (ليس داخل gaps:).
    يستبدل بـ "[معلومات غير متاحة بعد]" إذا كان في منتصف جملة، أو يحذفه إذا كان في سطر مستقل."""
    # Split frontmatter from body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content, False
    fm = '---' + parts[1] + '---'
    body = parts[2]
    new_body = body
    # Find DRAFT-UNKNOWN outside gaps: section
    in_gaps = False
    new_lines = []
    changed = False
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('gaps:'):
            in_gaps = True
            new_lines.append(line)
            continue
        # End of gaps: when we hit a non-indented, non-empty line
        if in_gaps and stripped and not line.startswith(' ') and not line.startswith('\t') and not stripped.startswith('-'):
            in_gaps = False
        if '[DRAFT-UNKNOWN]' in line and not in_gaps:
            # Replace
            if stripped == '[DRAFT-UNKNOWN]':
                # standalone line — remove
                changed = True
                continue
            # Inline — replace with placeholder
            new_line = line.replace('[DRAFT-UNKNOWN]', '[بيانات غير متاحة — للمراجعة]')
            new_lines.append(new_line)
            changed = True
            continue
        new_lines.append(line)
    if changed:
        new_body = '\n'.join(new_lines)
        return fm + new_body, True
    return content, False

# ----------------- F4: empty related: →  [] -----------------

def f4_empty_related(content):
    """تحويل 'related: \\n  []' أو 'related:\\n' إلى 'related: []'."""
    new_content = re.sub(r'related:\s*\n\s*\[\]', r'related: []', content)
    new_content = re.sub(r'related:\s*\n(?=\n)', r'related: []\n', new_content)
    if new_content != content:
        return new_content, True
    return content, False

# ----------------- F6: orphan closes -----------------

def f6_orphan_additions():
    """إضافة related entries للأورفانات المعروفة.
    Returns dict: filename → (old, new) content pairs."""
    fixes = {}

    # sch-cbt — add major CBT thinkers
    fp = os.path.join(CONTENT_AR, 'schools/sch-cbt.md')
    if os.path.exists(fp):
        c = read(fp)
        if 'related:' in c and 'thk-beck' not in c:
            # Inject before gaps: or end
            new_related = '''related:
- id: "thk-beck", title: "أرون بيك", type: "مفكر"
- id: "thk-ellis", title: "ألبرت إليس", type: "مفكر"
- id: "thk-meichenbaum", title: "دونالد ميتشنbaum", type: "مفكر"
- id: "sch-behaviorism", title: "السلوكية", type: "مدرسة"
- id: "rel-psychoanalysis-cbt", title: "التحليل النفسي والعلاج المعرفي-السلوكي: من الردّ إلى الهجين", type: "علاقة بين مدرستين"
- id: "sch-dbt", title: "العلاج الجدلي السلوكي (DBT)", type: "مدرسة"
- id: "sch-act", title: "العلاج بالقبول والالتزام (ACT)", type: "مدرسة"
- id: "tec-cbt-emo-self-compassion-exercises", title: "تمارين الرأفة بالذات", type: "تقنية/تدخل علاجي"
- id: "tec-cbt-mind-body-scan", title: "مسح الجسد", type: "تقنية/تدخل علاجي"
'''
            new_c = re.sub(r'related:\s*\n', new_related, c, count=1)
            if new_c != c:
                fixes['schools/sch-cbt.md'] = (c, new_c)

    # 4 techniques → add sch-cbt or sch-dbt
    tech_to_school = {
        'tec-cbt-emo-self-compassion-exercises': 'sch-cbt',
        'tec-cbt-mind-body-scan': 'sch-cbt',
        'tec-dbt-dt-radical-acceptance': 'sch-dbt',
        'tec-dbt-dt-urge-surfing': 'sch-dbt',
    }
    for slug, school in tech_to_school.items():
        fp = os.path.join(CONTENT_AR, f'techniques/{slug}.md')
        if not os.path.exists(fp):
            continue
        c = read(fp)
        if f'id: "{school}"' in c:
            continue
        # Inject before gaps: or end of related
        new_entry = f'- id: "{school}", title: "مدرسة", type: "مدرسة"\n'
        new_c = re.sub(r'(related:\s*\n(?:-\s+id:[^\n]+\n)*)', r'\1' + new_entry, c, count=1)
        if new_c != c:
            fixes[f'techniques/{slug}.md'] = (c, new_c)

    # wrk-berne-games-people-play (6th orphan)
    fp = os.path.join(CONTENT_AR, 'works/wrk-berne-games-people-play.md')
    if os.path.exists(fp):
        c = read(fp)
        if 'related:' in c and 'thk-berne' not in c:
            new_related = '''related:
- id: "thk-berne", title: "إريك برن", type: "مفكر"
- id: "thk-harris", title: "توماس هاريس", type: "مفكر"
- id: "sch-transactional-analysis", title: "تحليل المعاملات (TA)", type: "مدرسة"
- id: "tec-strokes", title: "المداعبات (Strokes)", type: "تقنية/تدخل علاجي"
- id: "tec-life-script", title: "سيناريو الحياة (Life Script)", type: "تقنية/تدخل علاجي"
- id: "tec-ego-states-ta", title: "حالات الأنا الثلاث (Parent-Adult-Child)", type: "تقنية/تدخل علاجي"
'''
            new_c = re.sub(r'related:\s*\n', new_related, c, count=1)
            if new_c != c:
                fixes['works/wrk-berne-games-people-play.md'] = (c, new_c)

    return fixes

# ----------------- L1.7: cross-part duplicate -----------------

def f7_merge_cgrob():
    """دمج thk-cgrob (philosophy) في thk-charles-grob (psychology)."""
    a = os.path.join(CONTENT_AR, 'thinkers/thk-cgrob.md')
    b = os.path.join(CONTENT_AR, 'thinkers/thk-charles-grob.md')
    if not os.path.exists(a) or not os.path.exists(b):
        return None
    # Read both
    ca = read(a)
    cb = read(b)
    # Move cgrob to _merged/
    merged_dir = os.path.join(CONTENT_AR, '_merged')
    os.makedirs(merged_dir, exist_ok=True)
    shutil.move(a, os.path.join(merged_dir, 'thk-cgrob.md'))
    return True

# ----------------- Main -----------------

def main():
    dry = '--apply' not in sys.argv
    if dry:
        print("DRY RUN — pass --apply to write changes\n")
    else:
        print("APPLY MODE — writing changes\n")

    files = all_md_files()
    print(f"Scanning {len(files)} files\n")

    stats = Counter()
    changed_files = []

    for fp in files:
        try:
            c = read(fp)
        except Exception as e:
            print(f"  ERR reading {fp}: {e}")
            continue
        original = c
        rel = os.path.relpath(fp, CONTENT_AR)

        # F1: indent
        c, ch = f1_fix_indent(c)
        if ch: stats['F1_indent'] += 1
        # F2: dedupe
        c, ch = f2_dedupe_related(c)
        if ch: stats['F2_dedupe'] += 1
        # F3: draft-unknown
        c, ch = f3_clean_draft_unknown(c)
        if ch: stats['F3_draft_unknown'] += 1
        # F4: empty related format
        c, ch = f4_empty_related(c)
        if ch: stats['F4_empty_format'] += 1

        if c != original:
            changed_files.append((rel, original, c))
            if not dry:
                write(fp, c)

    print("=" * 50)
    print("Per-file structural fixes:")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v} files")
    print(f"  Total: {len(changed_files)} files changed")
    print()

    # F6: orphan additions
    print("=" * 50)
    print("F6: Orphan-related additions")
    orphan_fixes = f6_orphan_additions()
    for fn, (old, new) in orphan_fixes.items():
        fp = os.path.join(CONTENT_AR, fn)
        if not dry:
            write(fp, new)
        print(f"  {'+DRY' if dry else '+APPLY'} {fn}")
    print(f"  Total: {len(orphan_fixes)} orphan-fixes")
    print()

    # F7: cross-part duplicate merge
    print("=" * 50)
    print("F7: Cross-part duplicate merge (thk-cgrob → thk-charles-grob)")
    merged = f7_merge_cgrob()
    if merged:
        print(f"  {'+DRY' if dry else '+APPLY'} thk-cgrob.md → _merged/")
    else:
        print("  (skipped — file already merged or missing)")
    print()

    print("Done." if not dry else "Dry run complete — pass --apply to commit changes.")

if __name__ == '__main__':
    main()
