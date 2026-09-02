#!/usr/bin/env python3
"""
patch script صارم لإضافة روابط related معتمَدة من المستخدم فقط (Human-in-the-Loop).

بياخد ملف JSON فيه قائمة patches، كل واحد: {file, id, title, type}.
لكل patch:
  - يفتح الملف، يدوّر على بلوك `related:` جوه الـ frontmatter (بين --- و ---).
  - لو الـ id موجود بالفعل في related، يتخطاه (idempotent) ويسجّله "skip".
  - لو مش موجود، يضيف سطر واحد بنفس الصيغة المستخدمة في كل الأطلس:
      - id: "<id>", title: "<title>", type: "<type>"
    في آخر بلوك related (أو ينشئ بلوك related جديد لو الملف مالوش related أصلاً).
  - مايلمسش أي سطر تاني في الملف (المتن، الحقول التانية، gaps، إلخ).

الاستخدام:
  python3 scripts/apply_related_patch.py patches.json [--dry-run]
"""

import json
import os
import re
import sys

ATLAS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RELATED_HEADER_RE = re.compile(r'^related:\s*$', re.MULTILINE)
RELATED_ITEM_RE = re.compile(r'^\s*-\s*id:\s*"([^"]*)"')
FRONTMATTER_FIELD_RE = re.compile(r'^[A-Za-z_]+:', re.MULTILINE)


def apply_one(path, target_id, target_title, target_type, dry_run=False):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.startswith("---"):
        return "error", f"{path}: مفيش frontmatter (مايبدأش بـ ---)"

    end_fm = text.index("\n---", 3)
    frontmatter = text[: end_fm + 4]
    rest = text[end_fm + 4 :]

    lines = frontmatter.split("\n")

    # هل related: موجود؟
    related_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "related:":
            related_idx = i
            break

    new_line = f'  - id: "{target_id}", title: "{target_title}", type: "{target_type}"'

    if related_idx is None:
        # مفيش related: أصلاً — نضيفه قبل أول حقل تاني بعد edges لو موجود، وإلا قبل "---" القافلة
        # نحطه قبل "gaps:" لو موجود، وإلا قبل "---" الأخيرة
        insert_at = None
        for i, line in enumerate(lines):
            if line.strip() == "gaps:":
                insert_at = i
                break
        if insert_at is None:
            # قبل آخر سطر (---)
            insert_at = len(lines) - 1
        new_block = ["related:", new_line]
        lines = lines[:insert_at] + new_block + lines[insert_at:]
    else:
        # related: موجود — نلاقي آخر سطر "- id:" تابع له
        j = related_idx + 1
        existing_ids = []
        while j < len(lines):
            m = RELATED_ITEM_RE.match(lines[j])
            if m:
                existing_ids.append(m.group(1))
                j += 1
                continue
            break
        if target_id in existing_ids:
            return "skip", f"{path}: {target_id} موجود بالفعل في related"
        # j دلوقتي أول سطر بعد آخر عنصر related
        lines = lines[:j] + [new_line] + lines[j:]

    new_frontmatter = "\n".join(lines)
    new_text = new_frontmatter + rest

    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)

    return "applied", f"{path}: + {target_id} ({target_title})"


def main():
    if len(sys.argv) < 2:
        print("الاستخدام: python3 scripts/apply_related_patch.py patches.json [--dry-run]")
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
        status, msg = apply_one(full_path, p["id"], p["title"], p["type"], dry_run=dry_run)
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
