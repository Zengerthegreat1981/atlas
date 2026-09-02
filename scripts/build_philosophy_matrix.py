import os
import json
import re
from collections import defaultdict
from datetime import datetime

ATLAS_ROOT = "/Users/minamoheb/Desktop/Atlas"
APPROVED_BASE = os.path.join(ATLAS_ROOT, "content", "ar")
DRAFTS_BASE = os.path.join(ATLAS_ROOT, "content", "ar", "drafts")

TYPES = [
    "axioms", "branches", "concepts", "contexts", "critiques",
    "debates", "dialogues", "disorders", "events", "experiences",
    "instruments", "metaphors", "questions", "relations", "schools",
    "studies", "syndromes", "techniques", "terms", "thinkers", "works"
]

def parse_frontmatter(content):
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    fm = parts[1]
    rec = {
        "slug": "",
        "title": "",
        "type": "",
        "part": "",
        "philosophical_tradition": "",
        "historical_era": "",
        "cultural_origin": "",
        "belongs_to": [],
        "related": [],
        "gaps_count": 0,
    }
    for line in fm.splitlines():
        line_str = line.strip()
        for k in ["slug", "title", "type", "part", "philosophical_tradition", "historical_era", "cultural_origin"]:
            if line_str.startswith(k + ":"):
                val = line_str.split(":", 1)[1].strip().strip('"\'')
                rec[k] = val
        if "rel: \"belongs_to\"" in line_str or "rel: 'belongs_to'" in line_str:
            match = re.search(r"target:\s*[\"']([^\"']+)[\"']", line_str)
            if match:
                rec["belongs_to"].append(match.group(1))
        if line_str.startswith("- id:"):
            match = re.search(r"id:\s*[\"']([^\"']+)[\"']", line_str)
            if match:
                rec["related"].append(match.group(1))

    return rec

def get_all_philosophy_schools():
    schools = {}
    for base in [APPROVED_BASE, DRAFTS_BASE]:
        sp = os.path.join(base, "schools")
        if not os.path.isdir(sp):
            continue
        for fn in os.listdir(sp):
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(sp, fn)
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            rec = parse_frontmatter(content)
            if rec and (rec["part"] == "philosophy" or fn.startswith("sch-")):
                slug = rec["slug"] or os.path.splitext(fn)[0]
                schools[slug] = {
                    "title": rec["title"] or slug,
                    "path": fp,
                    "is_draft": "drafts" in fp,
                    "tradition": rec["philosophical_tradition"],
                    "era": rec["historical_era"],
                    "origin": rec["cultural_origin"]
                }
    return schools

def build_matrix():
    schools = get_all_philosophy_schools()
    school_name_to_slug = {}
    for slug, info in schools.items():
        school_name_to_slug[info["title"]] = slug
        clean = re.sub(r"\s*\(.*?\)\s*", "", info["title"]).strip()
        if clean != info["title"]:
            school_name_to_slug[clean] = slug
        school_name_to_slug[slug] = slug

    totals_approved = defaultdict(int)
    totals_drafts = defaultdict(int)
    totals_phil_approved = defaultdict(int)
    totals_phil_drafts = defaultdict(int)
    matrix = {slug: defaultdict(int) for slug in schools}
    unattached_phil = defaultdict(int)

    for base, is_draft in [(APPROVED_BASE, False), (DRAFTS_BASE, True)]:
        for t in TYPES:
            dir_path = os.path.join(base, t)
            if not os.path.isdir(dir_path):
                continue
            for fn in os.listdir(dir_path):
                if not fn.endswith(".md"):
                    continue
                fp = os.path.join(dir_path, fn)
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                rec = parse_frontmatter(content)
                if not rec:
                    continue

                if is_draft:
                    totals_drafts[t] += 1
                else:
                    totals_approved[t] += 1

                is_phil = (rec["part"] in ["philosophy", "bridge"])
                attached_schools = []
                for target in rec["belongs_to"]:
                    if target in school_name_to_slug:
                        attached_schools.append(school_name_to_slug[target])

                if is_phil or attached_schools:
                    if is_draft:
                        totals_phil_drafts[t] += 1
                    else:
                        totals_phil_approved[t] += 1

                    if attached_schools:
                        for s in attached_schools:
                            matrix[s][t] += 1
                    else:
                        unattached_phil[t] += 1

    by_school_totals = {slug: sum(counts.values()) for slug, counts in matrix.items()}

    return {
        "generated_at": datetime.now().isoformat(),
        "total_schools_count": len(schools),
        "schools": {s: info["title"] for s, info in schools.items()},
        "totals_approved": dict(totals_approved),
        "totals_drafts": dict(totals_drafts),
        "totals_phil_approved": dict(totals_phil_approved),
        "totals_phil_drafts": dict(totals_phil_drafts),
        "unattached_philosophy": dict(unattached_phil),
        "matrix": {k: dict(v) for k, v in matrix.items()},
        "by_school_totals": by_school_totals,
    }

def generate_report(data):
    md_lines = [
        "# مصفوفة تغطية قسم الفلسفة — تقرير خط الأساس (Baseline)",
        "",
        f"**تاريخ التوليد:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "**السكربت:** `scripts/build_philosophy_matrix.py`",
        "**المخرج الرقمي:** `data/philosophy_matrix.json`",
        "",
        "---",
        "",
        "## 1. الإحصاء العام لمحتوى الفلسفة الحالي",
        "",
        "| نوع المحتوى | معتمد (`content/ar/`) | مسودة (`drafts/`) | إجمالي الفلسفة الحالي | المستهدف بالخطة |",
        "|---|---|---|---|---|",
    ]

    plan_targets = {
        "schools": 330, "thinkers": 650, "concepts": 550, "works": 350,
        "debates": 85, "branches": 160, "critiques": 45, "axioms": 25,
        "dialogues": 25, "events": 60, "contexts": 25, "relations": 35
    }

    for t in sorted(plan_targets.keys()):
        app = data["totals_phil_approved"].get(t, 0)
        drf = data["totals_phil_drafts"].get(t, 0)
        tot = app + drf
        target = plan_targets.get(t, "-")
        md_lines.append(f"| {t} | {app} | {drf} | **{tot}** | **{target}** |")

    md_lines.extend([
        "", "---", "",
        "## 2. حالة تعميق المدارس الفلسفية الـ 330",
        "",
        f"- إجمالي المدارس المسجلة: **{data['total_schools_count']}** مدرسة وتيار.",
        f"- مدارس ذات كثافة محتوى (مرتبط بها مفكرون وأعمال ومفاهيم): **{sum(1 for cnt in data['by_school_totals'].values() if cnt >= 5)}** مدرسة.",
        f"- مدارس هياكل أولية بحاجة لتعميق فوري: **{sum(1 for cnt in data['by_school_totals'].values() if cnt < 5)}** مدرسة.",
        "", "---", "",
        "## 3. التوجيه التنفيذي للمراحل 1 - 7",
        "",
        "1. **المرحلة 1:** تعميق الفلسفة القديمة واليونانية والمشائية الإسلامية وعلم الكلام والسكولاستية.",
        "2. **المرحلة 2:** تعميق الفلسفة الهندية والبوذية والصينية ومدرسة كيوتو.",
        "3. **المرحلة 3:** تعميق الحداثة الأوروبية، العقلانية، التجريبية، الكانطية، المثالية، وفلاسفة القرن 19.",
        "4. **المرحلة 4:** تعميق قطبي التحليلية والقارية وفلسفة العقل والظاهراتية والنظرية النقدية.",
        "5. **المرحلة 5:** تعميق الفلسفة الأفريقية، التحرير، الديكولونيالية، النهضة والفكر العربي المعاصر، والنسوية.",
        "6. **المرحلة 6:** بناء أمهات الكتب، الجدالات، البديهيات، والمناظرات والأحداث الفلسفية.",
        "7. **المرحلة 7:** إحكام الجسر، التدقيق الهيكلي الكامل، والترقية والنشر.",
    ])
    return chr(10).join(md_lines)

if __name__ == "__main__":
    data = build_matrix()
    out_json = os.path.join(ATLAS_ROOT, "data", "philosophy_matrix.json")
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ كتب ملف JSON: {out_json}")

    report_md = generate_report(data)
    out_report = os.path.join(ATLAS_ROOT, "agents_specs", "philosophy-coverage-matrix-2026-08-22.md")
    with open(out_report, "w", encoding="utf-8") as f:
        f.write(report_md)
    print(f"✅ كتب تقرير المصفوفة: {out_report}")
