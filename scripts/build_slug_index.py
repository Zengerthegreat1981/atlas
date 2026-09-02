"""
يولّد content/ar/drafts/EXISTING_SLUGS.md — فهرس بكل الـ slugs والعناوين والأنواع
الموجودة فعلاً في الأطلس (المعتمد + المسودات معاً)، عشان النموذج اللي بيكتب المسودات يقدر
يتأكد قبل ما يضيف أي حاجة (ماتكررش، واربط related بـ id موجود فعلاً لا مخترَع).

**تصحيح 2026-08-19:** النسخة القديمة من السكريبت ده كانت بتفهرس المحتوى المعتمد (`content/ar/`)
بس — وده كان بيسيب فجوة خطيرة: أي مسودتين اتكتبوا في جلستين مختلفتين مش هيقدروا يعرفوا ببعض
(لأن EXISTING_SLUGS.md مكنش شايف أي حاجة جوه `drafts/` أصلاً)، وده السبب الحقيقي وراء 93 ملف
مكرَّر اتكتشفوا واتنضّفوا يدوياً (راجع agents_specs/FULL_REVIEW_REPORT.md وagents_specs/
RECONCILIATION_REPORT.md). دلوقتي الفهرس بيغطي الاتنين معاً، بعلامة توضح حالة كل عنصر.

شغّله بعد أي تعديل على content/ar/ أو content/ar/drafts/:
  python3 scripts/build_slug_index.py
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
from build_atlas import build_nodes, parse_markdown, ATLAS_ROOT  # noqa: E402

OUTPUT = os.path.join(ATLAS_ROOT, "content", "ar", "drafts", "EXISTING_SLUGS.md")
DRAFTS_ROOT = os.path.join(ATLAS_ROOT, "content", "ar", "drafts")

TYPE_ORDER = [
    "مفكر", "مفهوم", "عمل / كتاب", "جدل", "تيار", "مدرسة", "علاقة بين مدرستين",
    "سياق/تقليد", "أداة قياس", "اضطراب/حالة إكلينيكية", "تقنية/تدخل علاجي",
    "دراسة وبحث", "حدث تاريخي", "مصطلح لغوي متنازع عليه", "نقد خارجي موثَّق",
    "خبرة معيشة", "استعارة/مجاز مؤسِّس", "بديهية/مبدأ تأسيسي", "سؤال مولِّد",
    "حوار مع مدرسة مجاورة", "متلازمة", "نظام تصنيف", "دواء",
]
# ملاحظة 2026-08-27: "دواء" أُضيفت هنا — نوع عقدة جديد كلياً (drg-) أنشأته Spark في Task 16
# (أول 5 ملفات: drg-lithium وغيرها). أُضيفت فوراً بدل ما تُترك كـ"نوع غير مسجَّل" دائم، تطبيقاً
# لنفس الدرس المستفاد من حادثة "مدرسة" فوق.
# ملاحظة 2026-08-21: "مدرسة" كانت ناقصة من هنا — ده كان بيخفي كل ملفات schools/ (333 ملف وقت
# الاكتشاف) عن EXISTING_SLUGS.md تمامًا (مش حتى في قسم "أخرى" — التكرار بيتفلتر بصمت في build()،
# راجع تحت). اتصلح بعد ما MiniMax اكتشف المشكلة أثناء شغل contexts.


def build_draft_nodes():
    """بيمشي على content/ar/drafts/ بس (عكس build_nodes اللي بيتجاهلها عمداً للموقع الحي)."""
    nodes = {}
    if not os.path.isdir(DRAFTS_ROOT):
        return nodes
    for root, dirs, files in os.walk(DRAFTS_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in files:
            if fname.endswith(".md"):
                path = os.path.join(root, fname)
                slug = os.path.splitext(fname)[0]
                node_data = parse_markdown(path)
                if node_data:
                    nodes[slug] = node_data
    return nodes


def build():
    approved = build_nodes()
    drafts = build_draft_nodes()

    # لو نفس الـslug موجود في الاتنين (حالة نادرة، مثلاً بعد اعتماد مسودة بدون حذفها من drafts/)،
    # المعتمد بياخد الأولوية في العرض لكن الاتنين بيتسجّلوا في by_type عشان الفحص يمسك التعارض.
    by_type = {}
    conflicts = []
    for slug, n in approved.items():
        by_type.setdefault(n.get("type", "؟"), []).append((slug, n.get("title", ""), "✅ معتمد"))
    for slug, n in drafts.items():
        if slug in approved:
            conflicts.append(slug)
            continue
        by_type.setdefault(n.get("type", "؟"), []).append((slug, n.get("title", ""), "🕓 مسودة"))

    total = len(approved) + len(drafts) - len(conflicts)

    lines = [
        "# فهرس كل عناصر الأطلس الموجودة فعلاً (معتمد + مسودات معاً)",
        "",
        "**ملف مولَّد تلقائياً — لا تعدّله يدوياً.** يُعاد بناؤه بـ `python3 scripts/build_slug_index.py`.",
        "",
        f"الإجمالي: **{total}** عنصراً (**{len(approved)}** معتمد + **{len(drafts) - len(conflicts)}** مسودة).",
        "استخدم هذا الفهرس دايماً قبل ما تضيف أي عنصر جديد — لا تخترع slug ولا تفترض إنه غير موجود",
        "من غير ما تتأكد هنا فعلياً. **الفهرس ده بيغطي المسودات كمان، مش بس المحتوى المعتمد** —",
        "لازم تفحصه حتى لو بتكتب مسودة جديدة، عشان متكررش مسودة موجودة بالفعل من جلسة تانية.",
        "",
    ]
    if conflicts:
        lines.append(f"⚠️ **{len(conflicts)} slug موجود في المعتمد والمسودات معاً (يحتاج تنظيف):** " + ", ".join(conflicts))
        lines.append("")

    for t in TYPE_ORDER:
        items = sorted(by_type.get(t, []))
        lines.append(f"## {t} ({len(items)})")
        lines.append("")
        for slug, title, status in items:
            lines.append(f"- `{slug}` — {title} — {status}")
        lines.append("")

    # شبكة أمان: أي نوع مش مذكور في TYPE_ORDER (بادئة جديدة، أو خطأ إملائي في حقل type) يظهر هنا
    # بدل ما يختفي بصمت زي ما حصل مع "مدرسة" — لو الملف ده فضل فاضي فترة طويلة، ده دليل صحة كويس.
    unknown_types = sorted(set(by_type) - set(TYPE_ORDER))
    if unknown_types:
        lines.append("## ⚠️ أنواع غير مسجَّلة في TYPE_ORDER (يحتاج مراجعة عاجلة)")
        lines.append("")
        for t in unknown_types:
            items = sorted(by_type.get(t, []))
            lines.append(f"### {t} ({len(items)})")
            for slug, title, status in items:
                lines.append(f"- `{slug}` — {title} — {status}")
        lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ فهرس الـ slugs: {total} عنصر ({len(approved)} معتمد + {len(drafts) - len(conflicts)} مسودة) → {OUTPUT}")
    if conflicts:
        print(f"⚠️  {len(conflicts)} تعارض slug بين المعتمد والمسودات: {conflicts}")


if __name__ == "__main__":
    build()
