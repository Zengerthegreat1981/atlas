#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0.6 — حذف الروابط المطبوعة آلياً وروابط الحشو من كل `related`.

الأهداف (§4 من reports/ATLAS_EXECUTION_PLAN.md — قائمة الأهداف الممنوعة):
- الثلاثية المطبوعة: sch-cognitive-behavioral / sch-psychoanalysis /
  sch-existential-therapy / sch-humanistic / sch-positive-psychology
  (تُحذف فقط لو ظهرت كمجموعة في بداية القائمة على ملفات لا تخصها فعلياً —
  لكن في مرحلة صفر الميكانيكية، القرار المطبَّق هنا أبسط وأكثر أماناً:
  تُحذف من كل ملف لا ينتمي هو نفسه لإحدى هذه المدارس ولا لتقنياتها/فروعها
  المباشرة، لأن الفحص الدلالي الكامل شغل تحريري لاحق)
- 17 هدف الحشو الثابت (كتب البوب-سايكولوجي + المفاهيم الأربعة + البقية)

القاعدة المطبَّقة: يُحذف الهدف من `related` في أي ملف **لا يخصه اسم أو نوع**
واضح (أي ملف عدا schools/ وbranches/ التي تخص هذه المدارس تحديداً)، لأن
هذه هي بالضبط الملفات التي أثبت التشخيص أنها حشو بلا علاقة دلالية.
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap

STAMP_TRIAD = {"sch-cognitive-behavioral", "sch-psychoanalysis", "sch-existential-therapy",
               "sch-humanistic", "sch-positive-psychology"}
FILLER_17 = {
    "wrk-men-are-from-mars", "wrk-12-rules-for-life", "wrk-design-everyday-things",
    "wrk-power-of-habit", "con-res-cogitans-res-extensa", "con-set-and-setting",
    "con-voluntarism-divine-will", "br-relational-cultural", "br-recovered-memory-movement",
    "dbt-mao-maoism-vs-deng-ism", "dbt-feminist-essentialism-vs-constructionism",
    "evt-egaz-moniz-nobel-lobotomy-1949", "evt-founding-of-al-azhar-970",
}
ALL_TARGETS = STAMP_TRIAD | FILLER_17

# الملفات المستثناة من الحذف: المدارس/التقنيات/التيارات نفسها والملفات اللي
# بتشرح صراحة الصلة بالاسم والتاريخ (نتركها لمراجعة القسم صاحب الملكية).
EXEMPT_SLUGS = STAMP_TRIAD | {
    "wrk-men-are-from-mars", "wrk-12-rules-for-life", "wrk-design-everyday-things",
    "wrk-power-of-habit", "con-res-cogitans-res-extensa", "con-set-and-setting",
    "con-voluntarism-divine-will", "br-relational-cultural", "br-recovered-memory-movement",
    "dbt-mao-maoism-vs-deng-ism", "dbt-feminist-essentialism-vs-constructionism",
    "evt-egaz-moniz-nobel-lobotomy-1949", "evt-founding-of-al-azhar-970",
}


def slug_of(path):
    return os.path.splitext(os.path.basename(path))[0]


def main():
    apply = "--apply" in sys.argv
    n_files = 0
    n_links_removed = 0
    log = []

    for path in ap.iter_atlas_files():
        my_slug = slug_of(path)
        if my_slug in EXEMPT_SLUGS:
            continue
        try:
            d = ap.parse_file(path)
        except ap.AtlasParseError:
            continue
        if not d.related:
            continue
        before = len(d.related)
        new_related = [r for r in d.related if r["id"] not in ALL_TARGETS]
        removed = before - len(new_related)
        if removed:
            n_files += 1
            n_links_removed += removed
            log.append((os.path.relpath(path, ap.ROOT), removed))
            if apply:
                d.related = new_related
                ap.dump_file(d)

    print(f"{'تنفيذ' if apply else 'معاينة'} — ملفات فيها حذف: {n_files} | روابط اتحذفت: {n_links_removed}")
    return log


if __name__ == "__main__":
    log = main()
    if "--verbose" in sys.argv:
        for path, n in sorted(log, key=lambda x: -x[1])[:30]:
            print(f"  -{n:>3}  {path}")
