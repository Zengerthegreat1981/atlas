#!/usr/bin/env python3
import os
import re
import json
from collections import defaultdict

ATLAS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT_AR = os.path.join(ATLAS_ROOT, "content", "ar")
DRAFTS_AR = os.path.join(CONTENT_AR, "drafts")
DATA_DIR = os.path.join(ATLAS_ROOT, "data")
OUTPUT_JSON = os.path.join(DATA_DIR, "sociology_matrix.json")
OUTPUT_MD = os.path.join(ATLAS_ROOT, "agents_specs", "sociology-coverage-matrix.md")

BACKLOG_PATH = os.path.join(ATLAS_ROOT, "agents_specs", "sociology-schools-backlog.md")

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    raw = parts[1]
    data = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        sm = re.match(r'^([a-zA-Z0-9_-]+):\s*"(.*)"\s*$', line)
        if sm:
            k, v = sm.groups()
            data[k] = v
            continue
        nm = re.match(r'^([a-zA-Z0-9_-]+):\s*(-?\d+)\s*$', line)
        if nm:
            k, v = nm.groups()
            data[k] = int(v)
    return data

def extract_backlog_schools():
    if not os.path.exists(BACKLOG_PATH):
        return []
    schools = []
    with open(BACKLOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^-\s*\[([ x~])\]\s*(.*)$", line.strip())
            if m:
                status, name = m.groups()
                schools.append({
                    "name": name,
                    "status": "completed" if status == "x" else ("in_progress" if status == "~" else "pending")
                })
    return schools

def analyze_sociology_content():
    stats = {
        "type_counts": defaultdict(int),
        "tradition_counts": defaultdict(int),
        "paradigm_counts": defaultdict(int),
        "total_approved_nodes": 0,
        "total_draft_nodes": 0,
    }

    for base_path, is_draft in [(CONTENT_AR, False), (DRAFTS_AR, True)]:
        if not os.path.exists(base_path):
            continue
        for root, dirs, files in os.walk(base_path):
            if not is_draft and ("drafts" in root.split(os.sep) or "_merged" in root.split(os.sep)):
                continue
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        text = f.read()
                    fm = parse_frontmatter(text)
                    part = fm.get("part", "")
                    
                    is_socio = part == "sociology"
                    if is_socio:
                        if is_draft:
                            stats["total_draft_nodes"] += 1
                        else:
                            stats["total_approved_nodes"] += 1
                        
                        node_type = fm.get("type", "غير محدد")
                        stats["type_counts"][node_type] += 1
                        
                        tradition = fm.get("sociological_tradition", "عام / غير مصنف")
                        stats["tradition_counts"][tradition] += 1
                        
                        paradigm = fm.get("sociological_paradigm", "غير محدد")
                        stats["paradigm_counts"][paradigm] += 1
                except Exception:
                    pass

    return stats

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    backlog_schools = extract_backlog_schools()
    stats = analyze_sociology_content()

    matrix_data = {
        "summary": {
            "total_backlog_items": len(backlog_schools),
            "completed_backlog_items": sum(1 for s in backlog_schools if s["status"] == "completed"),
            "in_progress_backlog_items": sum(1 for s in backlog_schools if s["status"] == "in_progress"),
            "pending_backlog_items": sum(1 for s in backlog_schools if s["status"] == "pending"),
            "approved_sociology_nodes": stats["total_approved_nodes"],
            "draft_sociology_nodes": stats["total_draft_nodes"],
            "total_sociology_nodes": stats["total_approved_nodes"] + stats["total_draft_nodes"]
        },
        "type_breakdown": dict(stats["type_counts"]),
        "tradition_breakdown": dict(stats["tradition_counts"]),
        "paradigm_breakdown": dict(stats["paradigm_counts"]),
        "backlog": backlog_schools
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(matrix_data, f, ensure_ascii=False, indent=2)

    NL = chr(10)
    lines = []
    lines.append("# تقرير مصفوفة تغطية قسم علم الاجتماع (Sociology Coverage Matrix)")
    lines.append("**التاريخ:** 2026-08-25  ")
    lines.append("**الحالة:** تأسيس خط الأساس لقسم علم الاجتماع بالأطلس")
    lines.append("")
    lines.append("## 1. الملخص الإحصائي العام")
    lines.append("- **إجمالي بنود قائمة الانتظار (Backlog):** " + str(matrix_data["summary"]["total_backlog_items"]) + " مدرسة وتياراً")
    lines.append("- **المكتمل المعتمد:** " + str(matrix_data["summary"]["completed_backlog_items"]))
    lines.append("- **قيد المسودة:** " + str(matrix_data["summary"]["in_progress_backlog_items"]))
    lines.append("- **المتبقي للتنفيذ:** " + str(matrix_data["summary"]["pending_backlog_items"]))
    lines.append("- **إجمالي عقد علم الاجتماع الحالية في الأطلس:** " + str(matrix_data["summary"]["total_sociology_nodes"]) + " (" + str(matrix_data["summary"]["approved_sociology_nodes"]) + " معتمد + " + str(matrix_data["summary"]["draft_sociology_nodes"]) + " مسودة)")
    lines.append("")
    lines.append("## 2. توزيع المحتوى حسب النوع")
    lines.append("| نوع المحتوى | العدد الحالي |")
    lines.append("|---|---|")
    for ntype, count in sorted(stats["type_counts"].items(), key=lambda x: -x[1]):
        lines.append("| " + str(ntype) + " | " + str(count) + " |")
    
    lines.append("")
    lines.append("## 3. توزيع التقاليد السوسيولوجية")
    lines.append("| التقليد السوسيولوجي | العدد |")
    lines.append("|---|---|")
    for trad, count in sorted(stats["tradition_counts"].items(), key=lambda x: -x[1]):
        lines.append("| " + str(trad) + " | " + str(count) + " |")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(NL.join(lines) + NL)

    print("SUCCESS: Generated matrix and report.")

if __name__ == "__main__":
    main()
