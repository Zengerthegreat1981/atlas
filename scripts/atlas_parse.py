#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_parse.py — المحلّل/المُصدِّر الموحّد لصيغة الأطلس الهجينة.

المشكلة: كل ملف فيه frontmatter شبه-YAML. الحقول العادية (slug, title, dates,
gaps...) صالحة YAML قياسي. لكن `related` و`edges` مكتوبتان بصيغة سطر واحد
مضغوطة (`- id: "x", title: "y", type: "z"`) وهي flow-mapping بدون أقواس {} —
مش صالحة كـ YAML، فـ yaml.safe_load بيفشل على كل ملف في الأطلس (0 من 6,618).

الحل هنا: لا نحوّل الصيغة (قرار DR منفصل مؤجَّل لمرحلة لاحقة). نقرأها بمحلّل
مخصص، ونصدّرها بنفس الصيغة بالظبط. أي سكربت في المشروع لازم يستعمل الوحدة دي
بدل ما يكتب regex خاص بيه — ده اللي كان بيسبب تراكم أخطاء التحليل (16 ملف
critiques انكسرت بمفتاح ملتصق، مثلاً).

الاستعمال:
    from atlas_parse import parse_file, dump_file, parse_frontmatter

    doc = parse_file("content/ar/thinkers/thk-freud.md")
    doc.related          # [{'id':..,'title':..,'type':..}, ...]
    doc.edges            # [{'rel':..,'target':..,'target_type':..}, ...]
    doc.fields           # dict لبقية الحقول العادية (YAML قياسي فعلاً)
    doc.body              # المتن بعد الـ frontmatter
    dump_file(doc, path)  # يكتبها تاني بنفس الصيغة

تشغيل مباشر (تشخيص):
    python3 scripts/atlas_parse.py content/ar/thinkers/thk-freud.md
    python3 scripts/atlas_parse.py --scan        # يفحص المستودع كله ويطبع
                                                   # أي سطر related/edges لا
                                                   # يطابق الصيغة المعروفة
"""
from __future__ import annotations
import os, re, sys, glob
from dataclasses import dataclass, field

try:
    import yaml
except ImportError:
    yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = os.path.join(ROOT, "content", "ar")
SKIP_DIRS = {"drafts", "_merged"}

# سطر related: - id: "...", title: "...", type: "..."
_REL_RE = re.compile(
    r'^\s*-\s*id:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
    r'title:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
    r'type:\s*"((?:[^"\\]|\\.)*)"\s*$'
)
# سطر edges: - rel: "...", target: "...", target_type: "..."
_EDGE_RE = re.compile(
    r'^\s*-\s*rel:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
    r'target:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
    r'target_type:\s*"((?:[^"\\]|\\.)*)"\s*$'
)
_EMPTY_LIST_RE = re.compile(r'^\s*\[\s*\]\s*$')
# عنصر gaps: - "..." (بإزاحة متسقة أو غير متسقة — 157 ملفاً فيهم تذبذب فعلي
# في المصدر، فبنطلعها كـ list of str بمحلّل متسامح بدل الاعتماد على YAML.)
_GAP_ITEM_RE = re.compile(r'^\s*-\s*"((?:[^"\\]|\\.)*)"\s*$')


def _unescape(s: str) -> str:
    return s.replace('\\"', '"').replace('\\\\', '\\')


def _escape(s: str) -> str:
    return s.replace('\\', '\\\\').replace('"', '\\"')


@dataclass
class AtlasDoc:
    path: str
    fields: dict = field(default_factory=dict)     # كل الحقول العادية (YAML صالح)
    related: list = field(default_factory=list)     # [{'id','title','type'}]
    edges: list = field(default_factory=list)        # [{'rel','target','target_type'}]
    related_malformed: list = field(default_factory=list)  # أسطر مش قادر يحللها
    edges_malformed: list = field(default_factory=list)
    gaps_malformed: list = field(default_factory=list)
    body: str = ""
    field_order: list = field(default_factory=list)  # ترتيب الحقول الأصلي لإعادة الكتابة


class AtlasParseError(Exception):
    pass


def _split_frontmatter(text: str, path: str = "") -> tuple[str, str]:
    if not text.startswith("---"):
        raise AtlasParseError(f"{path}: الملف لا يبدأ بـ frontmatter (---)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise AtlasParseError(f"{path}: frontmatter غير مغلق (--- ناقصة)")
    return parts[1], parts[2]


def _extract_block(fm: str, key: str) -> tuple[str | None, str]:
    """يشيل كتلة `key:\n- ...` من الـ frontmatter، يرجّع (الكتلة أو None، الباقي).

    الأسطر التابعة تبدأ بـ `-` سواء بإزاحة أو بدونها (الصيغة الفعلية في
    المستودع غالباً بدون إزاحة: `edges:\n- rel: "..."`)، أو تكون سطراً فاضياً
    داخل الكتلة، أو `[]`.
    """
    m = re.search(rf'(^|\n){key}:[ \t]*\n((?:[ \t]*(?:-.*|\[\s*\])\n|[ \t]*\n)*)', fm)
    if not m:
        m2 = re.search(rf'(^|\n){key}:[ \t]*(\[\s*\])?[ \t]*\n', fm)
        if m2 and m2.group(2) is not None:
            rest = fm[: m2.start()] + (m2.group(1) or "") + fm[m2.end():]
            return "", rest
        return None, fm
    block = m.group(2)
    rest = fm[: m.start()] + (m.group(1) or "") + fm[m.end():]
    return block, rest


def parse_frontmatter(fm: str, path: str = ""):
    """يرجّع (fields, related, edges, related_malformed, edges_malformed, gaps_malformed, field_order)."""
    related_block, fm2 = _extract_block(fm, "related")
    edges_block, fm2b = _extract_block(fm2, "edges")
    gaps_block, fm3 = _extract_block(fm2b, "gaps")

    related, related_bad = [], []
    if related_block:
        for line in related_block.splitlines():
            if not line.strip() or _EMPTY_LIST_RE.match(line):
                continue
            mm = _REL_RE.match(line)
            if mm:
                related.append({
                    "id": _unescape(mm.group(1)),
                    "title": _unescape(mm.group(2)),
                    "type": _unescape(mm.group(3)),
                })
            else:
                related_bad.append(line)

    edges, edges_bad = [], []
    if edges_block:
        for line in edges_block.splitlines():
            if not line.strip() or _EMPTY_LIST_RE.match(line):
                continue
            mm = _EDGE_RE.match(line)
            if mm:
                edges.append({
                    "rel": _unescape(mm.group(1)),
                    "target": _unescape(mm.group(2)),
                    "target_type": _unescape(mm.group(3)),
                })
            else:
                edges_bad.append(line)

    gaps, gaps_bad = [], []
    if gaps_block:
        for line in gaps_block.splitlines():
            if not line.strip() or _EMPTY_LIST_RE.match(line):
                continue
            mm = _GAP_ITEM_RE.match(line)
            if mm:
                gaps.append(_unescape(mm.group(1)))
            else:
                gaps_bad.append(line)

    # باقي الحقول: YAML قياسي فعلاً (title, slug, dates, part...)
    field_order = []
    for m in re.finditer(r'^(\w+):', fm3, re.M):
        if m.group(1) not in field_order:
            field_order.append(m.group(1))
    fields = {}
    if yaml is not None:
        try:
            loaded = yaml.safe_load(fm3) or {}
            if isinstance(loaded, dict):
                fields = loaded
        except Exception as e:
            raise AtlasParseError(f"{path}: باقي الحقول (بعد استخراج related/edges/gaps) لسه مش YAML صالح: {e}")
    else:
        raise AtlasParseError("PyYAML غير مثبَّت — pip install pyyaml")

    if gaps:
        fields["gaps"] = gaps

    return fields, related, edges, related_bad, edges_bad, gaps_bad, field_order


def parse_file(path: str) -> AtlasDoc:
    text = open(path, encoding="utf-8", errors="replace").read()
    fm, body = _split_frontmatter(text, path)
    fields, related, edges, rbad, ebad, gbad, order = parse_frontmatter(fm, path)
    return AtlasDoc(path=path, fields=fields, related=related, edges=edges,
                     related_malformed=rbad, edges_malformed=ebad, gaps_malformed=gbad,
                     body=body, field_order=order)


def _dump_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    return f'"{_escape(s)}"'


def dump_frontmatter(doc: AtlasDoc) -> str:
    """يعيد بناء الـ frontmatter بنفس ترتيب الحقول الأصلي وبنفس صيغة السطر الواحد."""
    lines = []
    emitted = set()
    for key in doc.field_order:
        if key in ("related", "edges", "gaps"):
            continue
        if key not in doc.fields or key in emitted:
            continue
        emitted.add(key)
        v = doc.fields[key]
        if isinstance(v, list):
            if not v:
                lines.append(f"{key}: []")
            elif all(isinstance(x, str) for x in v):
                lines.append(f"{key}:")
                for x in v:
                    lines.append(f'  - "{_escape(x)}"')
            else:
                lines.append(f"{key}: {yaml.safe_dump(v, allow_unicode=True, default_flow_style=True).strip()}")
        elif isinstance(v, dict):
            lines.append(f"{key}: {yaml.safe_dump(v, allow_unicode=True, default_flow_style=True).strip()}")
        else:
            lines.append(f"{key}: {_dump_scalar(v)}")

    # حقول موجودة في fields لكن مش في field_order (نادر، أمان إضافي)
    for key, v in doc.fields.items():
        if key in emitted or key in ("related", "edges", "gaps"):
            continue
        if isinstance(v, list) and all(isinstance(x, str) for x in v):
            lines.append(f"{key}:")
            for x in v:
                lines.append(f'  - "{_escape(x)}"')
        elif isinstance(v, (list, dict)):
            lines.append(f"{key}: {yaml.safe_dump(v, allow_unicode=True, default_flow_style=True).strip()}")
        else:
            lines.append(f"{key}: {_dump_scalar(v)}")

    # edges → related → gaps: الترتيب الفعلي في كل الملفات الملاحَظة
    if doc.edges or "edges" in doc.field_order:
        if doc.edges:
            lines.append("edges:")
            for e in doc.edges:
                lines.append(f'- rel: "{_escape(e["rel"])}", target: "{_escape(e["target"])}", target_type: "{_escape(e["target_type"])}"')
        else:
            lines.append("edges: []")

    if doc.related or "related" in doc.field_order:
        if doc.related:
            lines.append("related:")
            for r in doc.related:
                lines.append(f'- id: "{_escape(r["id"])}", title: "{_escape(r["title"])}", type: "{_escape(r["type"])}"')
        else:
            lines.append("related: []")

    gaps = doc.fields.get("gaps")
    if gaps:
        lines.append("gaps:")
        for g in gaps:
            lines.append(f'  - "{_escape(g)}"')

    return "\n".join(lines)


def dump_file(doc: AtlasDoc, path: str | None = None) -> None:
    fm = dump_frontmatter(doc)
    text = f"---\n{fm}\n---{doc.body}"
    with open(path or doc.path, "w", encoding="utf-8") as f:
        f.write(text)


def iter_atlas_files(base: str = AR, include_drafts: bool = False):
    skip = set() if include_drafts else SKIP_DIRS
    for d in sorted(os.listdir(base)):
        p = os.path.join(base, d)
        if not os.path.isdir(p) or d in skip:
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".md"):
                yield os.path.join(p, f)


def _scan():
    total = ok = 0
    bad_related = bad_edges = bad_gaps = parse_fail = 0
    fail_examples = []
    for path in iter_atlas_files():
        total += 1
        try:
            doc = parse_file(path)
            ok += 1
            if doc.related_malformed:
                bad_related += 1
            if doc.edges_malformed:
                bad_edges += 1
            if doc.gaps_malformed:
                bad_gaps += 1
        except AtlasParseError as e:
            parse_fail += 1
            if len(fail_examples) < 15:
                fail_examples.append(str(e))
    print(f"إجمالي: {total}")
    print(f"اتحلّل بنجاح بمحلّل الأطلس: {ok}")
    print(f"فشل التحليل تماماً: {parse_fail}")
    print(f"فيها سطر related مش قادر المحلّل يفهمه: {bad_related}")
    print(f"فيها سطر edges مش قادر المحلّل يفهمه: {bad_edges}")
    print(f"فيها سطر gaps مش قادر المحلّل يفهمه: {bad_gaps}")
    if fail_examples:
        print("\nأمثلة فشل:")
        for e in fail_examples:
            print(" -", e)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--scan":
        _scan()
    elif len(sys.argv) > 1:
        d = parse_file(sys.argv[1])
        print(f"الحقول: {len(d.fields)} | related: {len(d.related)} (مكسور: {len(d.related_malformed)}) | edges: {len(d.edges)} (مكسور: {len(d.edges_malformed)}) | gaps مكسورة: {len(d.gaps_malformed)}")
        for k in d.field_order:
            if k in d.fields:
                print(f"  {k}: {str(d.fields[k])[:80]}")
        if d.related_malformed:
            print("related مكسورة:")
            for l in d.related_malformed:
                print(" ", l)
        if d.edges_malformed:
            print("edges مكسورة:")
            for l in d.edges_malformed:
                print(" ", l)
    else:
        print(__doc__)
