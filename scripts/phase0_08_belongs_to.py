#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0.8 — توحيد belongs_to: تحويل الأسماء العربية الحرة لـ slug حيثما توجد مدرسة
حقيقية بنفس العنوان بالضبط (بعد إزالة الاعتراض الإنجليزي بين قوسين وتطبيع
المسافات) — مطابقة **تامة فقط**، صفر تخمين أو مطابقة تقريبية، لتجنّب ربط
مفكر بمدرسة غلط.

الباقي (لا يقابله عنوان مدرسة تام) يُسجَّل في
`agents_specs/missing-schools-registry.md` مرتَّباً بعدد الأعضاء، ليستعمله
صاحب القسم 9 (إنشاء المدارس الغائبة) أو صاحب القسم 5 (توحيد بنيوي).
"""
import os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap


def norm(s):
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.strip("،, ")


def load_school_titles():
    out = {}
    base = os.path.join(ap.AR, "schools")
    for f in os.listdir(base):
        if not f.endswith(".md"):
            continue
        d = ap.parse_file(os.path.join(base, f))
        title = d.fields.get("title", "")
        if title:
            out[norm(title)] = f[:-3]
    return out


def main():
    apply = "--apply" in sys.argv
    norm_to_slug = load_school_titles()

    n_files = n_links = 0
    unmatched = collections.Counter()
    unmatched_sample_file = {}

    for path in ap.iter_atlas_files():
        try:
            d = ap.parse_file(path)
        except ap.AtlasParseError:
            continue
        changed = False
        for e in d.edges:
            if e["rel"] != "belongs_to":
                continue
            if re.match(r"^[a-z]+-", e["target"]):
                continue
            key = norm(e["target"])
            if key in norm_to_slug:
                slug = norm_to_slug[key]
                e["target"] = slug
                e["target_type"] = "مدرسة"
                changed = True
                n_links += 1
            else:
                unmatched[e["target"]] += 1
                unmatched_sample_file.setdefault(e["target"], os.path.relpath(path, ap.ROOT))
        if changed:
            n_files += 1
            if apply:
                ap.dump_file(d)

    print(f"{'تنفيذ' if apply else 'معاينة'} — ملفات اتحوَّلت: {n_files} | روابط اتحوَّلت لـ slug: {n_links}")
    print(f"أسماء لسه بلا مدرسة مطابقة تماماً: {len(unmatched)}")

    if apply:
        registry = os.path.join(ap.ROOT, "agents_specs", "missing-schools-registry.md")
        with open(registry, "w", encoding="utf-8") as f:
            f.write("# سجل المدارس الغائبة — بعد التحويل الآلي في 0.8\n\n")
            f.write(
                "أسماء عربية حرة في `belongs_to` لا يقابلها عنوان مدرسة تام في "
                "`content/ar/schools/`. الأعلى عدداً أولى بالإنشاء (القسم 9). "
                "أقل من 3 أعضاء = أسفل القائمة، راجع كل حالة قبل الإنشاء — بعضها "
                "قد يكون اسماً عاماً لا مدرسة حقيقية.\n\n"
            )
            f.write(f"**إجمالي:** {len(unmatched)} اسماً، منها بـ≥3 أعضاء: "
                     f"{sum(1 for v in unmatched.values() if v >= 3)}\n\n---\n\n")
            for name, cnt in sorted(unmatched.items(), key=lambda x: -x[1]):
                f.write(f"- **{cnt}** — {name}  _(مثال: {unmatched_sample_file[name]})_\n")
        print(f"السجل: agents_specs/missing-schools-registry.md")


if __name__ == "__main__":
    main()
