#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0.10 — تقليم الملفات الثلاثة المتضخمة (sch-psychoanalysis / sch-cognitive-behavioral
/ sch-existential-therapy) إلى ≤25 `related` و≤10 `gaps`.

العضوية الكاملة **لا تُفقد** — هي مشتقة أصلاً من `belongs_to` العكسي (أي ملف
فيه `edges: belongs_to -> sch-X`)، ومحفوظة بالكامل في
`agents_specs/mega-schools-full-roster.md` قبل أي تقليم. الـ`related` بعد
التقليم غرضه العرض (صفحة لا يمكن استعمالها بـ1,700 رابط)، مش تخزين العضوية.

معيار الاختيار للـ25 المتبقية (بالأولوية):
  1. روابط متبادلة حقيقية (الطرف التاني برضو بيربط بالمدرسة في related بتاعه)
  2. أعضاء حقيقيون (belongs_to -> هذه المدرسة) الأعلى بروزاً (بالروابط الواردة
     الكلية عبر الأطلس) — أهم مفكري المدرسة الفعليين، لا ترتيباً عشوائياً
  3. تنويع الأنواع (مفكر/عمل/جدل/تقنية) لو أمكن ضمن الـ25
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap

TARGETS = ["sch-psychoanalysis", "sch-cognitive-behavioral", "sch-existential-therapy"]
KEEP_RELATED = 25
KEEP_GAPS = 10


def main():
    apply = "--apply" in sys.argv

    # فهرس شامل: related لكل ملف (للمعاملة بالمثل) + belongs_to لكل ملف
    all_related, all_belongs, inbound_deg = {}, {}, collections.Counter()
    for path in ap.iter_atlas_files():
        slug = os.path.splitext(os.path.basename(path))[0]
        try:
            d = ap.parse_file(path)
        except ap.AtlasParseError:
            continue
        all_related[slug] = {r["id"] for r in d.related}
        all_belongs[slug] = {e["target"] for e in d.edges if e["rel"] == "belongs_to"}
        for r in d.related:
            inbound_deg[r["id"]] += 1

    roster_doc = ["# العضوية الكاملة للمدارس الثلاث المتضخمة قبل التقليم (0.10)\n",
                  "مشتقة من `belongs_to` العكسي — هذا هو السجل الكامل، لا الـ`related` المقلَّم.\n"]

    for slug in TARGETS:
        path = f"{ap.AR}/schools/{slug}.md"
        d = ap.parse_file(path)
        members = sorted([s for s, b in all_belongs.items() if slug in b],
                          key=lambda s: -inbound_deg.get(s, 0))
        roster_doc.append(f"\n## {slug} ({len(members)} عضواً فعلياً عبر belongs_to)\n")
        for m in members:
            roster_doc.append(f"- {m}  (بروز: {inbound_deg.get(m,0)})")

        reciprocal = [r for r in d.related if slug in all_related.get(r["id"], set())]
        recip_ids = {r["id"] for r in reciprocal}

        member_related = [r for r in d.related if r["id"] in set(members) and r["id"] not in recip_ids]
        member_related.sort(key=lambda r: -inbound_deg.get(r["id"], 0))

        kept = reciprocal[:]
        for r in member_related:
            if len(kept) >= KEEP_RELATED:
                break
            kept.append(r)
        # لو لسه فاضي مكان، كمّل بالأعلى بروزاً من باقي related (مش أعضاء لكن مذكورة كتير في الأطلس)
        if len(kept) < KEEP_RELATED:
            kept_ids = {r["id"] for r in kept}
            rest = [r for r in d.related if r["id"] not in kept_ids]
            rest.sort(key=lambda r: -inbound_deg.get(r["id"], 0))
            kept += rest[: KEEP_RELATED - len(kept)]
        kept = kept[:KEEP_RELATED]

        gaps = d.fields.get("gaps", [])
        seen = set()
        kept_gaps = []
        for g in gaps:
            if g in seen:
                continue
            seen.add(g)
            kept_gaps.append(g)
            if len(kept_gaps) >= KEEP_GAPS:
                break

        print(f"{slug}: related {len(d.related)} -> {len(kept)} | gaps {len(gaps)} -> {len(kept_gaps)} | أعضاء حقيقيون: {len(members)}")

        if apply:
            d.related = kept
            if gaps:
                d.fields["gaps"] = kept_gaps
            ap.dump_file(d)

    if apply:
        roster_path = os.path.join(ap.ROOT, "agents_specs", "mega-schools-full-roster.md")
        open(roster_path, "w", encoding="utf-8").write("\n".join(roster_doc))
        print(f"\nالسجل الكامل: agents_specs/mega-schools-full-roster.md")


if __name__ == "__main__":
    main()
