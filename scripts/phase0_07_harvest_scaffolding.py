#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0.7 — حصاد أقسام السقّالة الظاهرة `## أفكار روابط لم تُتحقق` ثم حذفها.

بيحصد **بس** القسم ده (501 ملفاً، صيغة موحّدة: قايمة نقطية بأسماء/كيانات).
مش بيلمس `## ملاحظة معمارية` ولا `## مراجعة وكيل` (30+12 ملفاً) — دول مش
سقّالة مرشحين، دول قرارات دمج/انتماء حقيقية بعضها لسه معلَّق (ازدواجات لم
تُحسم، أو محتوى اتحط في ملف غلط) وتحتاج قرار تحريري من صاحب المجلد (القسم 1
أو 2 — thinkers)، مش سكربت ميكانيكي. اتسجّلوا في تقرير منفصل بدل ما يتحذفوا.

الناتج:
  - agents_specs/pending-links-bank.md  (كل المرشحين، مصنّفين حسب الملف الأصل)
  - agents_specs/phase0-architectural-notes-flagged.md  (الـ42 ملف المعلَّقة)
  - حذف قسم "## أفكار روابط لم تُتحقق" من كل ملف حصلناه فقط
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap

SCAFFOLD_HEADING = "## أفكار روابط لم تُتحقق"
ARCH_HEADINGS = ("## ملاحظة معمارية", "## مراجعة وكيل")


def harvest_scaffold(body):
    """يرجّع (bullets:list[str], body_بدون_القسم)."""
    m = re.search(rf'\n?{re.escape(SCAFFOLD_HEADING)}\s*\n(.*?)(?=\n## |\Z)', body, re.S)
    if not m:
        return None, body
    bullets = [l.strip("- ").strip() for l in m.group(1).splitlines() if l.strip().startswith("-")]
    new_body = body[:m.start()] + body[m.end():]
    return bullets, new_body


def main():
    apply = "--apply" in sys.argv
    bank_entries = []      # (rel_path, [bullets])
    arch_flagged = []       # (rel_path, heading, snippet)
    n_harvested = 0

    for path in ap.iter_atlas_files():
        try:
            d = ap.parse_file(path)
        except ap.AtlasParseError:
            continue
        rel = os.path.relpath(path, ap.ROOT)

        if SCAFFOLD_HEADING in d.body:
            bullets, new_body = harvest_scaffold(d.body)
            if bullets is not None:
                bank_entries.append((rel, bullets))
                n_harvested += 1
                if apply:
                    d.body = new_body
                    ap.dump_file(d)

        for h in ARCH_HEADINGS:
            if h in d.body:
                idx = d.body.find(h)
                snippet = d.body[idx: idx + 300].replace("\n", " ")
                arch_flagged.append((rel, h, snippet))

    print(f"{'تنفيذ' if apply else 'معاينة'} — سقّالة أُحصدت وحُذفت: {n_harvested} ملفاً")
    print(f"ملاحظات معمارية معلَّقة (لم تُلمس): {len(arch_flagged)} ملفاً")

    if apply:
        bank_path = os.path.join(ap.ROOT, "agents_specs", "pending-links-bank.md")
        with open(bank_path, "w", encoding="utf-8") as f:
            f.write("# بنك الروابط المعلَّقة — حصاد المرحلة 0.7\n\n")
            f.write(
                "مرشحات روابط استُخرجت من أقسام `## أفكار روابط لم تُتحقق` قبل حذفها. "
                "لكل مرشح: هل يقابله ملف فعلي في `content/ar/drafts/EXISTING_SLUGS.md`؟\n"
                "- **موجود** → يُنقل لـ`related` في الملف الأصلي مع جملة تبرير في المتن.\n"
                "- **غير موجود** → يُسجَّل في طلبات القسم صاحب الملكية (القسم 9/10).\n\n"
                f"**إجمالي الملفات المحصودة:** {len(bank_entries)}\n\n---\n\n"
            )
            for rel, bullets in bank_entries:
                f.write(f"## {rel}\n\n")
                for b in bullets:
                    f.write(f"- [ ] {b}\n")
                f.write("\n")

        arch_path = os.path.join(ap.ROOT, "agents_specs", "phase0-architectural-notes-flagged.md")
        with open(arch_path, "w", encoding="utf-8") as f:
            f.write("# ملاحظات معمارية/مراجعة وكيل معلَّقة — لم تُلمس في المرحلة 0\n\n")
            f.write(
                "هذه ملفات فيها قسم `## ملاحظة معمارية` أو `## مراجعة وكيل` يحتوي "
                "**قرارات دمج/انتماء حقيقية**، بعضها ازدواجات لم تُحسم وبعضها محتوى "
                "في ملف غلط. تحتاج قرار تحريري من صاحب `thinkers/` (القسم 1 أو 2)، "
                "لا حذفاً آلياً.\n\n---\n\n"
            )
            for rel, h, snippet in arch_flagged:
                f.write(f"## {rel}\n\n`{h}`\n\n> {snippet}...\n\n")

        print(f"\nالبنك: agents_specs/pending-links-bank.md")
        print(f"المعلَّق: agents_specs/phase0-architectural-notes-flagged.md")


if __name__ == "__main__":
    main()
