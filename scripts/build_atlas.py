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

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from atlas_frontmatter import parse_frontmatter as _parse_fm  # noqa: E402

PARSE_WARNINGS = []  # (path, lineno, text) — never dropped silently (audit P0-02)

ATLAS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "template")
_ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
STRICT = "--strict" in sys.argv[1:]
LANG = _ARGS[0] if _ARGS else "ar"
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


def parse_frontmatter_block(raw_yaml, path=""):
    """Tolerant reader (quoted/unquoted/multi-line/short related). See atlas_frontmatter.py."""
    node, warns = _parse_fm(raw_yaml, path)
    for ln, txt in warns:
        PARSE_WARNINGS.append((path, ln, txt))
    return node


def _legacy_parse_frontmatter_block(raw_yaml):
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
    node = parse_frontmatter_block(raw_yaml, file_path)
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
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "drafts" and d != "_merged"]
        for fname in files:
            if fname.endswith(".md") and not fname.startswith("._") and fname.upper() != "README.MD":
                path = os.path.join(root, fname)
                slug = os.path.splitext(fname)[0]
                node_data = parse_markdown(path)
                if node_data:
                    nodes[slug] = node_data
                else:
                    PARSE_WARNINGS.append((path, 0, "no frontmatter block: file skipped"))
    # short related items (`- id: x, type: y`) carry no title: resolve from the target node
    for node in nodes.values():
        for row in node.get("related", []):
            if not row[1]:
                tgt = nodes.get(row[0])
                row[1] = (tgt.get("title") or tgt.get("en") or row[0]) if tgt else row[0]
    return nodes


EN_TITLE = "Atlas of the Human Mind — Philosophy, Psychology and the Human Sciences"
EN_DESC = ("A structured reference atlas of thinkers, schools, concepts, studies and the connections "
           "between them across psychology, philosophy, sociology, anthropology and related disciplines.")


def localize_prefix_en(prefix):
    """Real EN locale for the document shell (audit P0-03): lang/dir/title/description.
    In-page UI strings still come from the template; they are tracked in reports/EN_STATUS.md."""
    prefix = prefix.replace('<html lang="ar" dir="rtl">', '<html lang="en" dir="ltr">', 1)
    # LTR fixes: skip link was parked at right:-9999px (horizontal overflow in LTR)
    prefix = prefix.replace("</style>" + chr(10) + "</head>", ".v2-skip{right:auto;left:-9999px}.v2-skip:focus{left:12px}" + chr(10) + "</style>" + chr(10) + "</head>", 1)
    head, sep, tail = prefix.partition("<body>")
    for a, b in EN_CHROME:
        tail = tail.replace(a, b)
    prefix = head + sep + tail
    prefix = re.sub(r"<title>.*?</title>", f"<title>{EN_TITLE}</title>", prefix, count=1, flags=re.S)
    prefix = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + EN_DESC + m.group(2), prefix, count=1)
    return prefix


EN_CHROME = [
    (">تجاوز إلى المحتوى<", ">Skip to content<"),
    (">أطلس النفس البشرية</div>", ">Atlas of the Human Mind</div>"),
    ('aria-label="ابحث في الأطلس"', 'aria-label="Search the atlas"'),
    ('placeholder="ابحث في الطبقات والعناصر والمعجم…  (Ctrl + K)"', 'placeholder="Search entries…  (Ctrl + K)"'),
    ('aria-label="نتائج البحث"', 'aria-label="Search results"'),
    ('title="يعيدك إلى آخر عنصر زرته، أو إلى صفحة الاختيار إن لم تزر شيئاً بعد">نقطة بداية<', 'title="Return to the last entry you visited, or to the home page">Start<'),
    (">رحلتي<b", ">My journey<b"),
    ('title="بدّل وضع القراءة بين البحثي الكامل والمبسّط"', 'title="Switch reading mode between full and simplified"'),
    (">وضع القراءة: بحثي<", ">Reading mode: full<"),
    ('aria-label="خيارات أخرى"', 'aria-label="More options"'),
    (">المدارس <span", ">Schools <span"),
    (">قالب المدرسة<", ">School template<"),
    (">تصفح حسب النوع<", ">Browse by type<"),
    (">تصفح حسب البلد<", ">Browse by country<"),
    (">تصفح حسب اللغة<", ">Browse by language<"),
    (">تصفح حسب الزمن<", ">Browse by time<"),
    (">أظهر ما ينقص<", ">Show what is missing<"),
    (">الوضع الليلي<", ">Dark mode<"),
    (">طباعة هذه الصفحة<", ">Print this page<"),
    (">انسخ رابط الصفحة الحالية<", ">Copy link to this page<"),
    (">مسح سجل القراءة<", ">Clear reading history<"),
    (">مسودة تحريرية معلَنة — أرقام الأدلة مُتحقَّق منها، والتواريخ والسِّيَر مرشّحة.<", ">Editorial draft — figures are checked; dates and biographies are provisional.<"),
    (">ما معنى هذا؟<", ">What does this mean?<"),
    ('aria-label="أغلق"', 'aria-label="Close"'),
]
EN_CHROME_SUFFIX = [
    ("'وضع القراءة: مبسّط' : 'وضع القراءة: بحثي'", "'Reading mode: simplified' : 'Reading mode: full'"),
]


UI_STRINGS_EN = os.path.join(TEMPLATE_DIR, "ui_strings_en.json")


TYPE_EN = {
    "دراسة": "Study", "عمل": "Work", "عمل / كتاب": "Work / Book", "تقنية/تدخل علاجي": "Technique / therapeutic intervention",
    "سياق/تقليد": "Context / tradition", "اضطراب/حالة إكلينيكية": "Disorder / clinical condition",
    "أداة قياس": "Measurement instrument", "علاقة بين مدرستين": "Relation between two schools",
    "دراسة وبحث": "Study and research", "بديهية/مبدأ تأسيسي": "Axiom / founding principle",
    "نقد خارجي موثَّق": "Documented external critique", "حوار مع مدرسة مجاورة": "Dialogue with a neighbouring school",
    "حدث تاريخي": "Historical event", "خبرة معيشة": "Lived experience", "استعارة/مجاز مؤسِّس": "Founding metaphor",
    "سؤال مولِّد": "Generative question", "مجال": "Field", "نظام تصنيف تشخيصي": "Diagnostic classification system", "مفكرون": "Thinkers", "مفكرة": "Thinker", "منهج": "Method", "فرع": "Branch", "حقل": "Field", "تدخّل": "Intervention", "متلازمة": "Syndrome", "مصطلح لغوي متنازع عليه": "Contested linguistic term",
}


def load_ui_strings():
    """ar-fragment -> en map (scripts/template/ui_strings_en.json), longest keys first."""
    m = json.load(open(UI_STRINGS_EN, encoding="utf-8")) if os.path.exists(UI_STRINGS_EN) else {}
    m = {**m, **{k: v for k, v in TYPE_EN.items() if k not in m}}
    return sorted(((k, v) for k, v in m.items() if k and v), key=lambda kv: -len(kv[0]))


def apply_ui_strings(text, pairs):
    for a, b in pairs:
        text = text.replace(a, b)
    return text


def localize_nodes_en(nodes, pairs):
    """Display labels that live in node data (type/level/relation types) use the same map as the shell,
    so comparisons like n.type==='X' stay consistent after both sides are translated."""
    mp = dict(pairs)
    tr = lambda v: mp.get(v, v) if isinstance(v, str) else v
    for n in nodes.values():
        for f in ("type", "level"):
            if f in n:
                n[f] = tr(n[f])
        for r in n.get("related", []):
            r[2] = tr(r[2])
        for e in n.get("edges", []):
            e[0] = e[0]  # relation keys stay internal
            e[2] = tr(e[2])
    return nodes


def localize_suffix_en(suffix):
    out = suffix
    # footer(): replace the whole function body with an English one
    out = re.sub(r"function footer\(\)\{return .*?</footer>';\}",
                 lambda m: "function footer(){return '<footer>Atlas of the Human Mind · editorial draft, not clinically or legally reviewed · not for diagnosis or advice.</footer>';}",
                 out, count=1, flags=re.S)
    for a, b in EN_CHROME_SUFFIX:
        out = out.replace(a, b)
    return out


def build():
    nodes = build_nodes()
    if PARSE_WARNINGS:
        print(f"⚠️  {len(PARSE_WARNINGS)} unreadable frontmatter line(s) — first 10:")
        for pth, ln, txt in PARSE_WARNINGS[:10]:
            print(f"   {os.path.relpath(pth, ATLAS_ROOT)}:{ln}: {txt[:80]}")
        if STRICT:
            raise SystemExit("--strict: refusing to build with silent data loss")
    placeholders = sum(1 for n in nodes.values() if any("[EN TRANSLATION NEEDED]" in str(v) for k, v in n.items() if k in ("title", "crumb", "en", "lede")))

    with open(OUTPUT_JSON, "w", encoding="utf-8") as out:
        json.dump({"nodes": nodes}, out, ensure_ascii=False, indent=2)
    print(f"✅ [{LANG}] {os.path.basename(OUTPUT_JSON)}: {len(nodes)} عنصر"
          + (f" — ⚠️ {placeholders} لسه placeholder مش متَرجَم" if placeholders else ""))

    extras_path = os.path.join(TEMPLATE_DIR, "data_extras.json")
    # النسخة الإنجليزية تستخدم data_extras-en.json إن وُجد، وإلا تسقط للعربي مع تحذير.
    if LANG == "en":
        en_extras_path = os.path.join(TEMPLATE_DIR, "data_extras-en.json")
        if os.path.exists(en_extras_path):
            extras_path = en_extras_path
        else:
            print("⚠️  data_extras-en.json غير موجود — ستُبنى الواجهة الإنجليزية ببيانات عرض عربية (data_extras.json).")
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

    if LANG == "en":
        import copy
        pairs = load_ui_strings()
        full_data["nodes"] = localize_nodes_en(copy.deepcopy(nodes), pairs)
        prefix = localize_prefix_en(prefix)
        suffix = localize_suffix_en(suffix)
        # the in-page home is the module home, not the legacy existential-school landing page
        suffix = suffix.replace("const HOME='sch-existential';", "const HOME='atlas-root';")
        prefix = prefix.replace("const HOME='sch-existential';", "const HOME='atlas-root';")
        if pairs:
            head, sep, tail = prefix.partition("<body>")
            prefix = head + sep + apply_ui_strings(tail, pairs)
            suffix = apply_ui_strings(suffix, pairs)
    data_js = json.dumps(full_data, ensure_ascii=False, separators=(",", ":"))

    html = prefix + "const DATA=" + data_js + suffix
    with open(OUTPUT_HTML, "w", encoding="utf-8") as out:
        out.write(html)
    print(f"✅ [{LANG}] {os.path.basename(OUTPUT_HTML)}: {len(html):,} حرف، {len(nodes)} عنصر مضمّن.")
    return nodes


if __name__ == "__main__":
    build()
