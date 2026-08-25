#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_health.py — كل مؤشرات §1 و§8 من الخطة، بأمر واحد.

هذا هو مقياس النجاح الوحيد للمشروع كله. يُشغَّل قبل وبعد كل سكربت في المرحلة
صفر، وقبل وبعد كل مراجعة لدفعة نماذج. أي انحراف عن المتوقع = رجوع خطوة واحدة.

الاستعمال:
    python3 scripts/atlas_health.py                 # تقرير كامل بالعربي
    python3 scripts/atlas_health.py --json           # نفس الأرقام كـ JSON
    python3 scripts/atlas_health.py --save <name>    # يحفظ لقطة في
                                                       # agents_specs/health-snapshots/
    python3 scripts/atlas_health.py --diff <name>    # يقارن بلقطة محفوظة
"""
from __future__ import annotations
import os, re, sys, json, statistics, collections, subprocess
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import atlas_parse as ap

SNAP_DIR = os.path.join(ROOT, "agents_specs", "health-snapshots")

STAMP = {"sch-cognitive-behavioral", "sch-psychoanalysis", "sch-existential-therapy",
         "sch-humanistic", "sch-positive-psychology"}
FILLER = {"wrk-men-are-from-mars", "wrk-12-rules-for-life", "wrk-design-everyday-things",
          "wrk-power-of-habit", "con-res-cogitans-res-extensa", "con-set-and-setting",
          "con-voluntarism-divine-will", "br-relational-cultural", "br-recovered-memory-movement",
          "dbt-mao-maoism-vs-deng-ism", "dbt-feminist-essentialism-vs-constructionism",
          "evt-egaz-moniz-nobel-lobotomy-1949", "evt-founding-of-al-azhar-970"}
BLACKLIST = [
    "لا يوجد اقتباس مباشر موثوق متاح", "يمثل هذا المفهوم لبنة تأسيسية",
    "حيث يوفر أداة دقيقة لتفسير قضايا الوجود", "شكل هذا المفهوم منطلقاً لحوارات ومقاربات نقدية متجددة",
    "يقدم هذا العمل أطروحة فلسفية فارقة", "حظي الكتاب بدراسات وشروح وترجمات واسعة",
    "حيث يقدم إطاراً تحليلياً لتفسير جوانب محددة", "حظي هذا المفهوم بمراجعات وتطويرات واسعة",
    "يمثل هذا التيار الفرعي تحولاً جوهرياً وتطويراً بنيوياً", "مسهماً في بلورة مفاهيمها وإشكالياتها الكبرى",
    "ترك هذا الفرع بصمات عميقة في تطور الفكر الفلسفي", "يمثل هذا العمل علامة فارقة في مجاله",
    "حيث صاغ مفهوماً جديداً أو قدم نسقاً برهانياً متميزاً", "يقدم هذا الموقف رؤية نسقية تستند إلى براهين",
    "يقدم الطرف المقابل قراءة نقدية بديلة تكشف الثغرات", "شكل هذا الحدث منعطفاً حاسماً",
    "أعاد هذا الحدث تشكيل خريطة الأفكار", "يتناول هذا النقد تفكيك المسلمات النظرية",
    "مبيناً التناقضات الداخلية أو القصور الإبستمولوجي", "أحدث هذا النقد تحولاً منهجياً كبيراً",
    "يربط هذا الملف بين المفهوم الفلسفي التأسيسي واستعارته", "يمثل هذا الملف جسراً معرفياً",
    "انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية",
]
NOQUOTE = "لا يوجد اقتباس مباشر موثوق متاح"
SCAFFOLD_MARKERS = ("أفكار روابط لم تُتحقق", "ملاحظة معمارية", "مراجعة وكيل")


def git_info():
    try:
        h = subprocess.run(["git", "log", "-1", "--format=%h %ci"], cwd=ROOT,
                            capture_output=True, text=True, timeout=10).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                                capture_output=True, text=True, timeout=30).stdout
        n_dirty = len([l for l in dirty.splitlines() if l.strip()])
        return h, n_dirty
    except Exception:
        return "—", 0


def scan():
    per_folder = collections.defaultdict(lambda: {"n": 0, "lens": [], "stamped": 0,
                                                     "filler": 0, "scaffold": 0, "noquote": 0,
                                                     "sources": 0, "blacklist": 0,
                                                     "bt_slug": 0, "bt_name": 0,
                                                     "low_links": 0})
    inbound = collections.Counter()
    bt_names = collections.Counter()
    parse_fail = 0

    for path in ap.iter_atlas_files():
        folder = os.path.basename(os.path.dirname(path))
        f = per_folder[folder]
        try:
            d = ap.parse_file(path)
        except ap.AtlasParseError:
            parse_fail += 1
            continue
        f["n"] += 1
        body = d.body.strip()
        f["lens"].append(len(body))
        # ملاحظة: «لا يوجد اقتباس موثوق» والجمل القالبية تُفحص على الملف كله
        # (متن + frontmatter) لأن أغلبها يعيش داخل `gaps:` لا المتن الظاهر —
        # وهي بالضبط الصياغة الجاهزة اللي المعيار عايز يقتلها من جذرها.
        # هذا يطابق منهجية الأرقام المرجعية في ATLAS_EXECUTION_PLAN.md §1.
        full_text = open(path, encoding="utf-8", errors="replace").read()
        rel_ids = [r["id"] for r in d.related]
        for rid in rel_ids:
            inbound[rid] += 1
        if len(rel_ids) >= 2 and len(set(rel_ids[:3]) & STAMP) >= 2:
            f["stamped"] += 1
        if set(rel_ids) & FILLER:
            f["filler"] += 1
        if any(m in full_text for m in SCAFFOLD_MARKERS):
            f["scaffold"] += 1
        if NOQUOTE in full_text:
            f["noquote"] += 1
        if "## المصادر" in d.body:
            f["sources"] += 1
        if any(b in full_text for b in BLACKLIST):
            f["blacklist"] += 1
        if len(rel_ids) < 3:
            f["low_links"] += 1
        for e in d.edges:
            if e["rel"] != "belongs_to":
                continue
            if re.match(r"^[a-z]+-", e["target"]):
                f["bt_slug"] += 1
            else:
                f["bt_name"] += 1
                bt_names[e["target"]] += 1

    schools_slugs = {os.path.splitext(f)[0] for f in os.listdir(os.path.join(ap.AR, "schools"))
                      if f.endswith(".md")} if os.path.isdir(os.path.join(ap.AR, "schools")) else set()
    missing_schools = [(v, k) for k, v in bt_names.items() if v >= 3 and k not in schools_slugs]

    return per_folder, inbound, bt_names, missing_schools, parse_fail


def build_report():
    per_folder, inbound, bt_names, missing_schools, parse_fail = scan()
    total = sum(f["n"] for f in per_folder.values())
    tot = collections.Counter()
    for f in per_folder.values():
        for k in ("stamped", "filler", "scaffold", "noquote", "sources", "blacklist",
                   "bt_slug", "bt_name", "low_links"):
            tot[k] += f[k]
    all_lens = [x for f in per_folder.values() for x in f["lens"]]
    u600 = sum(1 for x in all_lens if x < 600)
    u1200 = sum(1 for x in all_lens if x < 1200)
    ghash, dirty = git_info()

    return {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "git": ghash, "dirty": dirty,
        "total_files": total, "parse_fail": parse_fail,
        "u600": u600, "u1200": u1200,
        "stamped": tot["stamped"], "filler": tot["filler"], "scaffold": tot["scaffold"],
        "noquote": tot["noquote"], "sources": tot["sources"], "blacklist": tot["blacklist"],
        "bt_slug": tot["bt_slug"], "bt_name": tot["bt_name"],
        "low_links": tot["low_links"],
        "missing_schools_count": len(missing_schools),
        "top_missing_schools": sorted(missing_schools, reverse=True)[:15],
        "top_inbound": inbound.most_common(15),
        "per_folder": {
            d: {"n": f["n"], "median": int(statistics.median(f["lens"])) if f["lens"] else 0,
                "u1200": sum(1 for x in f["lens"] if x < 1200),
                "stamped": f["stamped"], "filler": f["filler"], "scaffold": f["scaffold"],
                "blacklist": f["blacklist"], "low_links": f["low_links"], "bt_name": f["bt_name"]}
            for d, f in sorted(per_folder.items())
        },
    }


def print_report(r):
    print(f"=== أطلس النفس البشرية — تقرير الصحة ===")
    print(f"{r['generated']}  ·  git {r['git']}  ·  {r['dirty']} تغيير غير محفوظ\n")
    print(f"إجمالي الملفات: {r['total_files']}" + (f"  (فشل تحليل: {r['parse_fail']})" if r['parse_fail'] else ""))
    print()
    rows = [
        ("متنها < 1,200 حرف", r["u1200"]),
        ("متنها < 600 حرف", r["u600"]),
        ("الروابط المطبوعة آلياً", r["stamped"]),
        ("روابط الحشو", r["filler"]),
        ("أقسام سقّالة ظاهرة", r["scaffold"]),
        ("«لا يوجد اقتباس موثوق»", r["noquote"]),
        ("فيها ## المصادر", r["sources"]),
        ("جمل القائمة السوداء", r["blacklist"]),
        ("belongs_to → slug", r["bt_slug"]),
        ("belongs_to → اسم عربي حر", r["bt_name"]),
        ("< 3 روابط واردة (related)", r["low_links"]),
        ("مدارس غائبة بـ≥3 أعضاء", r["missing_schools_count"]),
    ]
    w = max(len(x[0]) for x in rows)
    for label, val in rows:
        print(f"  {label:<{w}}  {val:>6,}")

    print(f"\nأعلى المدارس الغائبة (اسم عربي حر بلا ملف):")
    for v, k in r["top_missing_schools"]:
        print(f"  {v:>4}  {k}")

    print(f"\nأعلى العناصر بروابط واردة:")
    for k, v in r["top_inbound"]:
        print(f"  {v:>5}  {k}")

    print(f"\nبحسب المجلد:")
    print(f"  {'مجلد':<13}{'عدد':>6}{'وسيط':>7}{'<1200':>7}{'مطبوع':>7}{'حشو':>6}{'سقّالة':>7}{'قالب':>6}{'<3روابط':>8}{'bt_اسم':>7}")
    for d, f in r["per_folder"].items():
        print(f"  {d:<13}{f['n']:>6}{f['median']:>7}{f['u1200']:>7}{f['stamped']:>7}{f['filler']:>6}{f['scaffold']:>7}{f['blacklist']:>6}{f['low_links']:>8}{f['bt_name']:>7}")


def main():
    args = sys.argv[1:]
    r = build_report()

    if "--save" in args:
        name = args[args.index("--save") + 1]
        os.makedirs(SNAP_DIR, exist_ok=True)
        path = os.path.join(SNAP_DIR, f"{name}.json")
        json.dump(r, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"✅ اتحفظت اللقطة في {path}")
        return

    if "--diff" in args:
        name = args[args.index("--diff") + 1]
        path = os.path.join(SNAP_DIR, f"{name}.json")
        if not os.path.isfile(path):
            print(f"❌ مفيش لقطة اسمها {name} في {SNAP_DIR}")
            return
        old = json.load(open(path, encoding="utf-8"))
        keys = ["total_files", "u1200", "u600", "stamped", "filler", "scaffold",
                "noquote", "sources", "blacklist", "bt_slug", "bt_name",
                "low_links", "missing_schools_count"]
        print(f"=== الفرق منذ اللقطة «{name}» ({old['generated']}) ===\n")
        w = max(len(k) for k in keys)
        for k in keys:
            o, n = old.get(k, 0), r.get(k, 0)
            d = n - o
            sign = "+" if d > 0 else ""
            print(f"  {k:<{w}}  {o:>6,} → {n:>6,}   ({sign}{d:,})")
        return

    if "--json" in args:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return

    print_report(r)


if __name__ == "__main__":
    main()
