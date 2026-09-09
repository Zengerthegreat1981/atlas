"""
أدواتُ تعديلٍ آمنةٍ على frontmatter ملفات الأطلس.

المبدأ: **لا نُعيد كتابةَ الملفّ**، بل نُعدّل الأسطرَ المقصودةَ فقط ونُبقي كلَّ
ما عداها كما هو حرفاً بحرف — لأنّ الملفات فيها تشكيلٌ وعلاماتٌ وتعليقاتٌ لا
يحفظها أيُّ محوِّلٍ YAML عامّ.

    from atlas_edit import load, save, remove_edge, add_edge, set_field, add_gap

كلُّ دالّةٍ تأخذ نصَّ الملفّ وتُعيد نصاً جديداً (أو None إن لم يتغيّر شيء).
"""
import os, re, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AR = os.path.join(ROOT, "content", "ar")
SKIP = ("/drafts/", "/_merged/")

BLOCK_KEYS = ("edges", "related", "gaps")


def path_of(slug):
    hits = [p for p in glob.glob(os.path.join(AR, "*", slug + ".md"))
            if not any(s in p for s in SKIP)]
    if len(hits) != 1:
        raise FileNotFoundError(f"{slug}: {len(hits)} matches")
    return hits[0]


def load(slug):
    p = path_of(slug)
    with open(p, encoding="utf-8") as f:
        return p, f.read()


def save(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _split(text):
    """يفصل (frontmatter, بقية الملفّ) مع إبقاء المحدِّدات."""
    m = re.match(r'^(---\n)(.*?)(\n---\n)(.*)$', text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    return m.group(1), m.group(2), m.group(3), m.group(4)


def _block_lines(fm, key):
    """يُعيد (فهرسُ سطر المفتاح, أسطرُ البنود) للكتلة المطلوبة، أو (None, [])."""
    lines = fm.split("\n")
    for i, ln in enumerate(lines):
        if re.match(rf'^{key}:\s*(\[\])?\s*$', ln):
            j = i + 1
            items = []
            while j < len(lines) and (lines[j].startswith("- ") or lines[j].startswith("  - ")
                                      or lines[j].startswith("  ") and lines[j].strip()):
                items.append(j)
                j += 1
            return i, items
    return None, []


def remove_edge(text, rel=None, target=None):
    """يحذف كلَّ حرفٍ يطابق (rel, target). None = أيّ قيمة."""
    pre, fm, mid, body = _split(text)
    i, items = _block_lines(fm, "edges")
    if i is None:
        return None
    lines = fm.split("\n")
    drop = []
    for j in items:
        m = re.search(r'rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"', lines[j])
        if not m:
            continue
        if (rel is None or m.group(1) == rel) and (target is None or m.group(2) == target):
            drop.append(j)
    if not drop:
        return None
    kept = [j for j in items if j not in drop]
    new = lines[:i] + ([f"edges:"] + [lines[j] for j in kept] if kept else ["edges: []"]) \
        + lines[(items[-1] + 1 if items else i + 1):]
    return pre + "\n".join(new) + mid + body


def add_edge(text, rel, target, target_type):
    """يُضيف حرفاً في نهاية كتلة edges (ويُنشئها إن لم توجد)، بلا تكرار."""
    pre, fm, mid, body = _split(text)
    line = f'- rel: "{rel}", target: "{target}", target_type: "{target_type}"'
    if line in fm:
        return None
    lines = fm.split("\n")
    i, items = _block_lines(fm, "edges")
    if i is None:
        # تُوضع قبل related إن وُجدت، وإلا في النهاية
        r, _ = _block_lines(fm, "related")
        at = r if r is not None else len(lines)
        lines = lines[:at] + ["edges:", line] + lines[at:]
    elif items:
        lines = lines[:items[-1] + 1] + [line] + lines[items[-1] + 1:]
    else:
        lines[i] = "edges:"
        lines = lines[:i + 1] + [line] + lines[i + 1:]
    return pre + "\n".join(lines) + mid + body


def replace_edge_target(text, old, new, new_type=None):
    pre, fm, mid, body = _split(text)
    def sub(m):
        t = f'target_type: "{new_type}"' if new_type else m.group(3)
        return f'{m.group(1)}target: "{new}"{m.group(2)}{t}'
    pat = re.compile(r'(rel:\s*"[^"]*"\s*,\s*)target:\s*"' + re.escape(old) + r'"(\s*,\s*)(target_type:\s*"[^"]*")')
    fm2 = pat.sub(sub, fm)
    return None if fm2 == fm else pre + fm2 + mid + body


def replace_edge_rel(text, target, new_rel):
    pre, fm, mid, body = _split(text)
    pat = re.compile(r'rel:\s*"[^"]*"(\s*,\s*target:\s*"' + re.escape(target) + r'")')
    fm2 = pat.sub(lambda m: f'rel: "{new_rel}"{m.group(1)}', fm)
    return None if fm2 == fm else pre + fm2 + mid + body


def set_field(text, key, value, quote=True):
    """يُبدّل قيمةَ حقلٍ بسيط، أو يُضيفه بعد آخر حقلٍ بسيطٍ إن لم يوجد."""
    pre, fm, mid, body = _split(text)
    v = f'"{value}"' if quote else str(value)
    pat = re.compile(rf'^{re.escape(key)}:.*$', re.M)
    if pat.search(fm):
        fm2 = pat.sub(f'{key}: {v}', fm, count=1)
    else:
        lines = fm.split("\n")
        at = 0
        for i, ln in enumerate(lines):
            if re.match(r'^[a-zA-Z0-9_-]+:', ln) and ln.split(":")[0] not in BLOCK_KEYS:
                at = i + 1
            elif ln.split(":")[0] in BLOCK_KEYS:
                break
        fm2 = "\n".join(lines[:at] + [f'{key}: {v}'] + lines[at:])
    return None if fm2 == fm else pre + fm2 + mid + body


def rename_field(text, old, new):
    pre, fm, mid, body = _split(text)
    fm2 = re.sub(rf'^{re.escape(old)}:', f'{new}:', fm, count=1, flags=re.M)
    return None if fm2 == fm else pre + fm2 + mid + body


def add_gap(text, gap):
    """يُضيف بنداً في gaps (ويُنشئ الكتلةَ إن لم توجد)."""
    pre, fm, mid, body = _split(text)
    esc = gap.replace('"', "'")
    line = f'  - "{esc}"'
    if esc in fm:
        return None
    lines = fm.split("\n")
    i, items = _block_lines(fm, "gaps")
    if i is None:
        lines = lines + [f"gaps:", line] if lines[-1].strip() else lines[:-1] + ["gaps:", line]
    elif items:
        lines = lines[:items[-1] + 1] + [line] + lines[items[-1] + 1:]
    else:
        lines[i] = "gaps:"
        lines = lines[:i + 1] + [line] + lines[i + 1:]
    return pre + "\n".join(lines) + mid + body


def set_related(text, pairs):
    """يُعيد كتابةَ كتلة related بالكامل من [(id,title,type), ...]."""
    pre, fm, mid, body = _split(text)
    lines = fm.split("\n")
    i, items = _block_lines(fm, "related")
    new_items = [f'- id: "{a}", title: "{b}", type: "{c}"' for a, b, c in pairs]
    if i is None:
        g, _ = _block_lines(fm, "gaps")
        at = g if g is not None else len(lines)
        lines = lines[:at] + (["related:"] + new_items if new_items else ["related: []"]) + lines[at:]
    else:
        tail = items[-1] + 1 if items else i + 1
        lines = lines[:i] + (["related:"] + new_items if new_items else ["related: []"]) + lines[tail:]
    return pre + "\n".join(lines) + mid + body


def replace_related_item(text, old_id, new_id=None, new_title=None, new_type=None):
    pre, fm, mid, body = _split(text)
    pat = re.compile(r'-\s*id:\s*"' + re.escape(old_id) + r'"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')
    m = pat.search(fm)
    if not m:
        return None
    i = new_id or old_id
    t = new_title if new_title is not None else m.group(1)
    ty = new_type if new_type is not None else m.group(2)
    fm2 = fm[:m.start()] + f'- id: "{i}", title: "{t}", type: "{ty}"' + fm[m.end():]
    return None if fm2 == fm else pre + fm2 + mid + body


def remove_related_item(text, rid):
    pre, fm, mid, body = _split(text)
    lines = fm.split("\n")
    i, items = _block_lines(fm, "related")
    if i is None:
        return None
    keep = [j for j in items if not re.search(r'id:\s*"' + re.escape(rid) + r'"', lines[j])]
    if len(keep) == len(items):
        return None
    new = lines[:i] + (["related:"] + [lines[j] for j in keep] if keep else ["related: []"]) \
        + lines[items[-1] + 1:]
    return pre + "\n".join(new) + mid + body


def all_files():
    return sorted(p for p in glob.glob(os.path.join(AR, "*", "*.md"))
                  if not any(s in p for s in SKIP))
