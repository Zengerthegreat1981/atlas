"""
يبني index.html الكامل للأطلس من مصدرين، للغة واحدة في كل مرة (ar أو en):
  1. ملفات Markdown في content/<lang>/ (thinkers/, concepts/, debates/, ...) — دي مصدر
     الحقيقة الوحيد لـ DATA.nodes، وبتتغير باستمرار (كل تعديل من /atlas-review بيروح هنا).
     كل لغة نسخة مستقلة بنفس البنية وأسماء الملفات (نفس الـ slugs)، عشان لما content/en/
     تتترجم بالكامل يوم الأحد، تُبنى بنفس السكريبت من غير أي تعديل فيه.
  2. scripts/template/ — قالب الواجهة الأصلية (Atlas-Version-7.1.html) مقسّم لـ:
       - shell_prefix.html : كل حاجة قبل "const DATA=" (كل الـ <head>/CSS وبداية الصفحة)
       - shell_suffix.html : كل حاجة بعد قفل كائن DATA (كل الـ JS اللي بيرسم ويوصل الأزرار)
       - data_extras.json  : كل مفاتيح DATA ماعدا nodes (entries, layers, timeline,
         sources, edges, unknowns, dash, lede, bridge, people, pairs, groups,
         gnodes, glinks, gantt, threads) — دي بيانات عرض/تصفح ثابتة من الأصل، مش
         مشتقة من ملفات Markdown، فبتتنسخ زي ما هي بدون تعديل (حتى في نسخة en — لسه
         عربي حالياً، هتتترجم بشكل منفصل لاحقاً لو لزم).
  الناتج: shell_prefix + "const DATA=" + json.dumps({**extras, "nodes": built_nodes}) + shell_suffix
  يعني نفس الشكل والتنقل والـ CSS والـ JS بالظبط زي الأصل، بس المحتوى (nodes) طالع من
  ملفات الـ Markdown المُحدَّثة.

الاستخدام:
  python3 scripts/build_atlas.py          # يبني نسخة العربي (الافتراضي) → data.json + index.html
  python3 scripts/build_atlas.py ar       # نفس الشيء صراحةً
  python3 scripts/build_atlas.py en       # يبني نسخة الإنجليزي → data-en.json + index-en.html

ملاحظات على شكل ملفات الـ Markdown الفعلي (لازم يتوافق معاه الـ parser، مش العكس):
  - كل عنصر related أو edges بيتكتب في سطر واحد مفصول بفواصل، مش على تلات أسطر:
      - id: "thk-heidegger", title: "هايدجر", type: "مفكر"
      - rel: "belongs_to", target: "المدرسة الوجودية", target_type: "مدرسة"
  - المتن بعد الـ frontmatter بيبدأ بـ "# العنوان" ثم فقرة lede سايبة، ثم أقسام "## ...".
  - لو فيه قسم اسمه "جدول مقارن" ومحتواه Markdown table، بيتحوّل لحقل node.table
    (head + rows) بدل ما يتحط كقسم نصي عادي — عشان يتوافق مع شكل الأصل.
"""

import os
import re
import sys
import json

ATLAS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "template")
LANG = sys.argv[1] if len(sys.argv) > 1 else "ar"
if LANG not in ("ar", "en"):
    raise SystemExit(f"لغة غير معروفة: {LANG!r} — استخدم ar أو en")

BASE_DIR = os.path.join(ATLAS_ROOT, "content", LANG)
SUFFIX = "" if LANG == "ar" else "-en"
OUTPUT_JSON = os.path.join(ATLAS_ROOT, f"data{SUFFIX}.json")
OUTPUT_HTML = os.path.join(ATLAS_ROOT, f"index{SUFFIX}.html")

RELATED_ITEM_RE = re.compile(
    r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"'
)
EDGE_ITEM_RE = re.compile(
    r'-\s*rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"\s*,\s*target_type:\s*"([^"]*)"'
)
GAP_ITEM_RE = re.compile(r'^\s*-\s*"(.*)"\s*$')
SIMPLE_FIELD_RE = re.compile(r'^([a-zA-Z0-9_-]+):\s*"(.*)"\s*$')
NUMERIC_FIELD_RE = re.compile(r'^([a-zA-Z0-9_-]+):\s*(-?\d+)\s*$')
TABLE_SECTION_TITLES = {"جدول مقارن"}


def parse_frontmatter_block(raw_yaml):
    node = {}

    for line in raw_yaml.split("\n"):
        if line.startswith(" ") or line.startswith("\t"):
            continue  # سطر فرعي (جوه related/edges/gaps) — بيتعالج لوحده تحت
        line = line.strip()
        m = SIMPLE_FIELD_RE.match(line)
        if m:
            key, val = m.groups()
            if key not in ("related", "edges", "gaps"):
                node[key] = val
            continue
        # active_start/active_end ممكن يتكتبوا رقم صريح من غير علامات اقتباس (زي 1946)،
        # أو نص "مستمر" لو العنصر لسه نشط بلا تاريخ نهاية — النص بيتلقط فوق عادي، الرقم هنا بس.
        m = NUMERIC_FIELD_RE.match(line)
        if m:
            key, val = m.groups()
            if key not in ("related", "edges", "gaps"):
                node[key] = int(val)

    def block_between(start_key, stop_keys):
        if f"{start_key}:" not in raw_yaml:
            return ""
        chunk = raw_yaml.split(f"{start_key}:", 1)[1]
        for stop in stop_keys:
            chunk = chunk.split(f"\n{stop}:")[0]
        return chunk

    related_block = block_between("related", ["gaps", "edges"])
    node["related"] = [list(m.groups()) for m in RELATED_ITEM_RE.finditer(related_block)]

    edges_block = block_between("edges", ["related", "gaps"])
    node["edges"] = [list(m.groups()) for m in EDGE_ITEM_RE.finditer(edges_block)]

    gaps_block = block_between("gaps", ["related", "edges"])
    node["gaps"] = [m.group(1) for line in gaps_block.split("\n") for m in [GAP_ITEM_RE.match(line)] if m]

    return node


def parse_markdown_table(text):
    """يحوّل جدول Markdown (| a | b |\\n|---|---|\\n| x | y |) لـ {"head": [...], "rows": [[...]]}."""
    lines = [ln.strip() for ln in text.strip().split("\n") if ln.strip()]
    if len(lines) < 2:
        return None
    def split_row(ln):
        return [c.strip() for c in ln.strip("|").split("|")]
    head = split_row(lines[0])
    rows = [split_row(ln) for ln in lines[2:]]  # lines[1] هو خط الفاصل |---|---|
    return {"head": head, "rows": rows}


def parse_body(body):
    """يفصل: (lede, sections, table) من المتن اللي بعد الـ frontmatter."""
    body = body.strip()
    lines = body.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    remainder = "\n".join(lines).strip()

    parts = re.split(r'\n##\s+', "\n" + remainder)
    lede = parts[0].strip()
    sections = []
    table = None
    for chunk in parts[1:]:
        chunk = chunk.strip()
        if not chunk:
            continue
        first_line, _, rest = chunk.partition("\n")
        title = first_line.strip()
        rest = rest.strip()
        if title in TABLE_SECTION_TITLES:
            table = parse_markdown_table(rest)
        else:
            sections.append([title, rest])

    return lede, sections, table


def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not m:
        return None

    raw_yaml, body = m.groups()
    node = parse_frontmatter_block(raw_yaml)
    lede, sections, table = parse_body(body)
    node["lede"] = lede
    node["sections"] = sections
    if table:
        node["table"] = table
    return node


def build_nodes():
    nodes = {}
    if not os.path.isdir(BASE_DIR):
        raise SystemExit(f"مجلد المحتوى غير موجود: {BASE_DIR}")
    for root, dirs, files in os.walk(BASE_DIR):
        # drafts/ مسودات لسه ما اتراجعتش ولا اعتُمدت — ما تدخلش في البناء النهائي أبداً
        # (بيتم نقل الملف يدوياً من drafts/<folder>/ لـ <folder>/ بعد المراجعة، مش قبلها)
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "drafts"]
        for fname in files:
            if fname.endswith(".md"):
                path = os.path.join(root, fname)
                slug = os.path.splitext(fname)[0]
                node_data = parse_markdown(path)
                if node_data:
                    nodes[slug] = node_data
    return nodes


def build():
    nodes = build_nodes()
    placeholders = sum(1 for n in nodes.values() if "[EN TRANSLATION NEEDED]" in (n.get("title") or ""))

    with open(OUTPUT_JSON, "w", encoding="utf-8") as out:
        json.dump({"nodes": nodes}, out, ensure_ascii=False, indent=2)
    print(f"✅ [{LANG}] {os.path.basename(OUTPUT_JSON)}: {len(nodes)} عنصر"
          + (f" — ⚠️ {placeholders} لسه placeholder مش متَرجَم" if placeholders else ""))

    extras_path = os.path.join(TEMPLATE_DIR, "data_extras.json")
    prefix_path = os.path.join(TEMPLATE_DIR, "shell_prefix.html")
    suffix_path = os.path.join(TEMPLATE_DIR, "shell_suffix.html")
    if not (os.path.exists(extras_path) and os.path.exists(prefix_path) and os.path.exists(suffix_path)):
        print("⚠️  قالب الواجهة (scripts/template/) غير موجود — تم توليد data.json فقط، بدون index.html.")
        return nodes

    extras = json.load(open(extras_path, encoding="utf-8"))
    full_data = dict(extras)
    full_data["nodes"] = nodes

    prefix = open(prefix_path, encoding="utf-8").read()
    suffix = open(suffix_path, encoding="utf-8").read()
    data_js = json.dumps(full_data, ensure_ascii=False, separators=(",", ":"))

    html = prefix + "const DATA=" + data_js + suffix
    with open(OUTPUT_HTML, "w", encoding="utf-8") as out:
        out.write(html)
    print(f"✅ [{LANG}] {os.path.basename(OUTPUT_HTML)}: {len(html):,} حرف، {len(nodes)} عنصر مضمّن.")
    return nodes


if __name__ == "__main__":
    build()
