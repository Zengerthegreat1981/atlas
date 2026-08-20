#!/usr/bin/env python3
"""
patch script صارم لإضافة/تحديث active_start/active_end (وactive_source الاختياري) في frontmatter
ملفات معتمدة، معتمَد من المستخدم فقط لكل بند (Human-in-the-Loop) — نفس فلسفة apply_related_patch.py
بالظبط، بس للحقول دي بدل related.

بياخد ملف JSON فيه قائمة patches، كل واحد:
  {"file": "content/ar/thinkers/thk-nietzsche.md", "active_start": 1872, "active_end": 1888}
أو مع المصدر لو مشتق من dates بدل إنتاج موثّق:
  {"file": "content/ar/thinkers/thk-plotinus.md", "active_start": 204, "active_end": 270,
   "active_source": "lifespan"}
أو لعنصر "مستمر" (active_end نص، مش رقم):
  {"file": "content/ar/branches/br-humanistic.md", "active_start": 1950, "active_end": "مستمر"}

لكل patch:
  - يفتح الملف، يتأكد إن فيه frontmatter (يبدأ بـ ---).
  - لو active_start/active_end موجودين بالفعل في الملف، يتخطاه (idempotent) ويسجّله "skip" —
    محدّش يستبدل قيمة موجودة تلقائياً، لو محتاج تحديث لازم تشيل السطرين من الملف يدوياً الأول.
  - لو مش موجودين، يضيفهم كسطرين جداد فور سطر `dates:` لو موجود (نفس ترتيب القالب في
    draft-writer-brief.md)، وإلا فور آخر سطر بسيط في الـ frontmatter قبل `edges:`/`related:`/`gaps:`.
  - active_end ممكن يكون رقم أو نص "مستمر" — يتكتب بالصيغة المناسبة (رقم من غير علامات اقتباس،
    نص جوه علامات اقتباس).
  - active_source يتكتب بس لو موجود في الـ patch (مش إلزامي).
  - مايلمسش أي سطر تاني في الملف (المتن، الحقول التانية، related، edges، gaps، إلخ).

الاستخدام:
  python3 scripts/apply_active_period_patch.py patches.json [--dry-run]
"""

import json
import os
import re
import sys

ATLAS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FIELD_RE = re.compile(r'^(active_start|active_end|active_source):', re.MULTILINE)
DATES_LINE_RE = re.compile(r'^dates:.*$', re.MULTILINE)
FRONTMATTER_FIELD_RE = re.compile(r'^[A-Za-z_]+:', re.MULTILINE)


def fmt_value(v):
    """رقم يتكتب من غير علامات اقتباس، نص (زي "مستمر") يتكتب جواها."""
    if isinstance(v, int):
        return str(v)
    return f'"{v}"'


def apply_one(path, active_start, active_end, active_source=None, dry_run=False):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.startswith("---"):
        return "error", f"{path}: مفيش frontmatter (مايبدأش بـ ---)"

    end_fm = text.index("\n---", 3)
    frontmatter = text[: end_fm + 4]
    rest = text[end_fm + 4:]

    if FIELD_RE.search(frontmatter):
        return "skip", f"{path}: active_start/active_end/active_source موجودين بالفعل — شيلهم يدوياً لو محتاج تحديث"

    new_lines = [f"active_start: {fmt_value(active_start)}", f"active_end: {fmt_value(active_end)}"]
    if active_source:
        new_lines.append(f'active_source: "{active_source}"')

    lines = frontmatter.split("\n")

    # نحطهم فور سطر dates: لو موجود
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("dates:"):
            insert_at = i + 1
            break

    if insert_at is None:
        # مفيش dates: — نحطهم قبل أول حقل بلوك (edges:/related:/gaps:) أو قبل "---" القافلة
        for i, line in enumerate(lines):
            if line.strip() in ("edges:", "related:", "gaps:"):
                insert_at = i
                break
        if insert_at is None:
            insert_at = len(lines) - 1  # قبل "---" الأخيرة

    lines = lines[:insert_at] + new_lines + lines[insert_at:]
    new_frontmatter = "\n".join(lines)
    new_text = new_frontmatter + rest

    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)

    return "applied", f"{path}: + active_start={active_start}, active_end={active_end}" + (
        f", active_source={active_source}" if active_source else ""
    )


def main():
    if len(sys.argv) < 2:
        print("الاستخدام: python3 scripts/apply_active_period_patch.py patches.json [--dry-run]")
        sys.exit(1)

    patches_path = sys.argv[1]
    dry_run = "--dry-run" in sys.argv[2:]

    with open(patches_path, "r", encoding="utf-8") as f:
        patches = json.load(f)

    applied, skipped, errors = 0, 0, 0
    for p in patches:
        full_path = os.path.join(ATLAS_ROOT, p["file"])
        if not os.path.isfile(full_path):
            print(f"[ERROR] الملف مش موجود: {full_path}")
            errors += 1
            continue
        if "active_start" not in p or "active_end" not in p:
            print(f"[ERROR] {p['file']}: محتاج active_start و active_end")
            errors += 1
            continue
        status, msg = apply_one(
            full_path, p["active_start"], p["active_end"],
            p.get("active_source"), dry_run=dry_run,
        )
        prefix = {"applied": "[APPLIED]", "skip": "[SKIP]", "error": "[ERROR]"}[status]
        print(f"{prefix} {msg}")
        if status == "applied":
            applied += 1
        elif status == "skip":
            skipped += 1
        else:
            errors += 1

    print(f"\nالخلاصة: {applied} تمت إضافتها، {skipped} متخطاة (موجودة بالفعل)، {errors} أخطاء.")


if __name__ == "__main__":
    main()
