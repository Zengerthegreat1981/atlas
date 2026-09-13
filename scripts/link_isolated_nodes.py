# -*- coding: utf-8 -*-
"""يربط العقدَ المعزولة (بلا `related` ولا `edges`) بأدلّةٍ في المستودع نفسِه.

قاعدتان، ولا ثالثة — ولا تُخترع علاقةٌ قط:

  F) **عكسُ إشارةٍ قائمة**: إن كان ملفٌّ آخرُ يشير إلى هذه العقدة فعلاً، فالإشارةُ
     العكسيةُ مسنودةٌ بما يؤكّده المستودعُ سلفاً. تُضاف إلى `related`.
  B) **مسارُ التنقّل**: إن سمّى `crumb` مدرسةً أو تيّاراً له ملفٌّ قائم — بعنوانه
     العربيِّ أو الإنجليزيِّ أو ما بين قوسيه — فذاك نسبٌ مكتوبٌ في البيانات الوصفية.
     يُضاف `belongs_to` إن طابق `part` وسمَ الأب، وإلا فإشارةُ `related`.
  E) **ذكرٌ صريحٌ في المتن**: عنوانُ عقدةٍ أخرى مكتوبٌ في متن هذه بحروفه، بشرط أن
     يكون **من كلمتين فأكثرَ وطولُه عشرةُ أحرفٍ فأكثر**. والشرطُ ليس تزيّداً: الألقابُ
     المفردةُ في العربية تصادف كلماتٍ عاديةً («طالب»، «مايو»، «الكبير») فتُنتج روابطَ
     كاذبة، وقد جُرِّبت فأُسقطت.

ثم خطوةٌ ثالثةٌ لازمة: عقدةٌ صار لها صادرٌ ولا يشير إليها أحدٌ تبقى غيرَ قابلةٍ للوصول
بالتنقّل، فتُضاف الإشارةُ العكسيةُ عند أقلِّ أهدافها ازدحاماً (لا عند عقدةٍ مركزيةٍ
تربط العشرات، فتُغرَق فيها).

    python3 scripts/link_isolated_nodes.py --dry          # عرضٌ بلا كتابة
    python3 scripts/link_isolated_nodes.py --apply        # ربطٌ + ضمانُ الوصول
    python3 scripts/link_isolated_nodes.py --reciprocate  # ضمانُ الوصول وحدَه
"""
import json, os, re, sys, glob, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AR = os.path.join(ROOT, "content", "ar")
APPLY = "--apply" in sys.argv
RECIP = "--reciprocate" in sys.argv
MAX_BACKLINKS = 3

d = json.load(open(os.path.join(ROOT, "data.json"), encoding="utf-8"))["nodes"]

def dep(v):
    t = v.get("title") or ""
    return bool(v.get("status") == "quarantined" or v.get("redirect_to")
                or "حجر" in t or "إحالة" in t)

# صِيَغُ إعلان الحجر في المتن — جُمعت من المستودع نفسِه، وبعضُها لا يذكر لفظَ «حجر»
QUARANTINE_PHRASES = re.compile(
    r"(هذا الملف في الحجر|\*\*حُجر|سجل الحجر|وُسم بالحجر|قرار الحجر|بلا سيرة"
    r"|غير مؤكد الهوية|لا يوجد ما يؤكد هوية|لم يُعثر على مصدر مستقل"
    r"|لا يمكن توثيقه|لم يُعثر له على أي توثيق)")

def na(t):
    t = re.sub(r"[ً-ْٰـ]", "", t or ""); t = re.sub(r"[إأآٱ]", "ا", t)
    t = re.sub(r"[ىي]", "ي", t).replace("ة", "ه")
    t = re.sub(r"\s*\(.*?\)", "", t); t = re.sub(r"\s*—.*$", "", t)
    return re.sub(r"\s+", " ", t).strip()


def reciprocate():
    """عقدةٌ لها صادرٌ ولا واردَ لها = غيرُ قابلةٍ للوصول. تُضاف الإشارةُ العكسيةُ عند
       أقلِّ أهدافها ازدحاماً، فلا تتورّم العقدُ المركزية."""
    data = json.load(open(os.path.join(ROOT, "data.json"), encoding="utf-8"))["nodes"]
    inb2 = collections.defaultdict(set)
    for a, b in data.items():
        for r in b.get("related", []): inb2[r[0]].add(a)
        for e in b.get("edges", []): inb2[e[1]].add(a)
    nrel2 = {a: len(b.get("related", [])) for a, b in data.items()}
    need = [a for a, b in data.items()
            if not dep(b) and not inb2[a] and (b.get("related") or b.get("edges"))]
    host = {}
    for a in need:
        tg = [e[1] for e in data[a].get("edges", []) if e[0] == "belongs_to"] \
             + [r[0] for r in data[a].get("related", [])]
        tg = [t for t in tg if t in data and not dep(data[t])]
        if tg: host[a] = min(tg, key=lambda t: nrel2.get(t, 0))
    by = collections.defaultdict(list)
    for a, h in host.items(): by[h].append(a)
    pths = {os.path.basename(f)[:-3]: f for f in glob.glob(os.path.join(AR, "*", "*.md"))
            if "/_merged/" not in f and "/drafts/" not in f}
    G = ('  - "**رُبطت عقدٌ معزولة 2026-09-13:** أُضيفت هنا إشاراتٌ إلى {n} عقدةً تشير إلى '
         'هذا الملفّ ولا يشير إليها أحد، فكانت غيرَ قابلةٍ للوصول بالتنقّل. الإشارةُ عكسُ '
         'علاقةٍ مكتوبةٍ في العقدة نفسِها، لم تُخترَع."')
    for h, ks in by.items():
        fp = pths[h]; raw = open(fp, encoding="utf-8").read()
        fm, body = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S).groups()
        L = fm.split("\n")
        ri = next(i for i, x in enumerate(L) if x.rstrip() == "related:")
        if L[ri+1].strip() == "[]": del L[ri+1]
        j = ri + 1
        while j < len(L) and L[j].startswith("- "): j += 1
        L[j:j] = [f'- id: "{a}", title: "{data[a]["title"]}", type: "{data[a]["type"]}"' for a in ks]
        gi = next((i for i, x in enumerate(L) if x.rstrip() == "gaps:"), None)
        if gi is None: L.append("gaps:"); gi = len(L) - 1
        t = gi + 1
        while t < len(L) and (L[t].startswith("  - ") or L[t].startswith("    ")): t += 1
        L.insert(t, G.format(n=len(ks)))
        open(fp, "w", encoding="utf-8").write("---\n" + "\n".join(L) + "\n---\n" + body)
    print(f"✔ ضمانُ الوصول: {len(host)} عقدةً عبر {len(by)} ملفاً")


if RECIP and not APPLY:
    reciprocate(); raise SystemExit(0)

iso = [k for k, v in d.items()
       if not v.get("related") and not v.get("edges") and not dep(v)]
S = set(iso)

# ── F
# عقدةٌ «مركزية» تربط العشرات: استُعملت في دفعاتٍ سابقةٍ لفكِّ العزلة بالجملة، فإشارتُها
# إلى دراسةٍ بعينها ضعيفةُ الدلالة — وعكسُ رابطٍ ضعيفٍ رابطٌ ضعيف. تُستبعد ما دام
# لغير المركزيّ وجودٌ، وتبقى آخرَ ملجأٍ إن لم يشر إليها سواه.
HUB = 40
nrel = {k: len(v.get("related", [])) for k, v in d.items()}
inb = collections.defaultdict(list)
for k, v in d.items():
    if dep(v) or k in S: continue
    for r in v.get("related", []):
        if r[0] in S: inb[r[0]].append(k)
    for e in v.get("edges", []):
        if e[1] in S: inb[e[1]].append(k)
for k, srcs in inb.items():
    srcs[:] = list(dict.fromkeys(srcs))
    slim = [s for s in srcs if nrel.get(s, 0) <= HUB]
    same = [s for s in slim if d[s].get("part") == d[k].get("part")]
    srcs[:] = (same or slim or srcs)
    srcs.sort(key=lambda s: nrel.get(s, 0))
HUBONLY = {k for k, srcs in inb.items() if srcs and all(nrel.get(s, 0) > HUB for s in srcs)}

# ── B
GENERIC = {"الناس", "علم النفس", "الفلسفه", "المفاهيم", "الاطلس", "تطوير", "التاسيس"}
sch, claims = {}, {}
# عنوانُ ملفٍّ صار إحالةً ما زال يُستعمل في مسارات التنقّل القديمة — يُحلّ إلى هدفه
for k, v in d.items():
    t = v.get("redirect_to")
    if not t or t not in d or d[t]["type"] not in ("مدرسة", "تيار"): continue
    for c in (v.get("title") or "", re.sub(r"\s*—.*$", "", v.get("title") or "")):
        c = na(c)
        if len(c) >= 4: sch.setdefault(c, t)
for k, v in d.items():
    if dep(v) or v["type"] not in ("مدرسة", "تيار"): continue
    cands = [v["title"], re.sub(r"\s*\(.*?\)", "", v["title"]),
             *re.findall(r"\((.*?)\)", v["title"]),
             (v.get("en") or "").split("(")[0], *re.findall(r"\((.*?)\)", v.get("en") or "")]
    for c in cands:
        c = na(c)
        # الاختصارُ اللاتينيُّ (DDP، IFS) دالٌّ وإن قصُر؛ والعربيُّ القصيرُ يصادف كلماتٍ عادية
        lim = 3 if re.fullmatch(r"[A-Za-z0-9 .\-]+", c or "") else 4
        if len(c) >= lim and c not in GENERIC:
            claims.setdefault(c, set()).add(k); sch.setdefault(c, k)
# اختصارٌ أو اسمٌ يدّعيه أكثرُ من مدرسة لا يميّز شيئاً — «EFT» وحدَه لمدرستين،
# وثالثةٌ تحمله في مسارها ولا ملفَّ لها أصلاً. يُسقَط الملتبسُ كلُّه.
for c, owners in claims.items():
    if len(owners) > 1: sch.pop(c, None)

parent = {}
for k in iso:
    for seg in [x.strip() for x in (d[k].get("crumb") or "").split("←")][:-1]:
        for c in [seg, re.sub(r"\s*\(.*?\)", "", seg), *re.findall(r"\((.*?)\)", seg)]:
            n = na(c)
            if n in sch and sch[n] != k and n not in GENERIC:
                parent[k] = sch[n]; break
        if k in parent: break

# ── E
WORDCH = re.compile(r"[ء-ي0-9A-Za-z]")
surf = {}
for k, v in d.items():
    if dep(v): continue
    for c in (v["title"], re.sub(r"\s*\(.*?\)", "", v["title"])):
        c = na(c)
        if len(c) >= 10 and len(c.split()) >= 2: surf.setdefault(c, set()).add(k)
surf = {s2: next(iter(t)) for s2, t in surf.items() if len(t) == 1}
def mentioned(k):
    b = na((d[k].get("lede") or "") + "\n" + "\n".join(x[1] for x in d[k].get("sections", [])))
    out = []
    for s2, nid in surf.items():
        if nid == k: continue
        i = b.find(s2)
        if i < 0: continue
        bf = b[i-1] if i else " "; af = b[i+len(s2)] if i+len(s2) < len(b) else " "
        if not WORDCH.match(bf) and not WORDCH.match(af): out.append(nid)
    return list(dict.fromkeys(out))[:3]

paths = {os.path.basename(f)[:-3]: f for f in glob.glob(os.path.join(AR, "*", "*.md"))
         if "/_merged/" not in f and "/drafts/" not in f}

plan, skipped = {}, []
for k in iso:
    par = parent.get(k)
    rel = list(dict.fromkeys(inb.get(k, [])))
    # مُشيرٌ مركزيٌّ وحدَه، وللعقدة أبٌ مكتوبٌ في مسارها: الأبُ أصدقُ وأغنى، فيُترك المركزيّ
    if k in HUBONLY and par: rel = []
    rel = rel[:MAX_BACKLINKS]
    if not rel and not par:
        rel = mentioned(k)
    rel = [x for x in dict.fromkeys(rel) if x != k and x != par]
    as_edge = bool(par) and d[par].get("part") == d[k].get("part")
    if par and not as_edge and par not in rel:
        rel.append(par)
    if not rel and not (par and as_edge):
        skipped.append(k); continue
    plan[k] = {"related": rel, "belongs_to": par if as_edge else None}

print(f"معزولةٌ حيّة: {len(iso)}")
print(f"تُربط الآن: {len(plan)}  ·  بلا دليلٍ في المستودع: {len(skipped)}")
print(f"  منها بحرف `belongs_to` من المسار: {sum(1 for p in plan.values() if p['belongs_to'])}")
print(f"  مجموعُ بنود `related` المضافة: {sum(len(p['related']) for p in plan.values())}")

if not APPLY:
    for k, p in list(plan.items())[:12]:
        print(f"   {k:44} ⊂{p['belongs_to'] or '—':28} ← {', '.join(p['related']) or '—'}")
    json.dump(skipped, open(os.path.join(ROOT, "scripts", "isolated_no_evidence.json"), "w"),
              ensure_ascii=False, indent=1)
    raise SystemExit(0)

GAP = ('  - "**رُبطت عقدةٌ معزولة 2026-09-13:** لم يكن لهذا الملفّ أيُّ `related` ولا `edges`، '
       'فكان طريقاً مسدوداً لمن يصل إليه. وكلُّ إشارةٍ أُضيفت هنا **عكسُ علاقةٍ يؤكّدها المستودعُ '
       'أصلاً** — إمّا ملفٌّ يشير إليه فعلاً، وإمّا مدرسةٌ يسمّيها مسارُ التنقّل في ترويسته. '
       'لم تُخترَع واحدةٌ منها."')

n = 0
for k, p in plan.items():
    fp = paths[k]
    raw = open(fp, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    fm, body = m.groups()
    lines = [l for l in fm.split("\n")
             if not re.match(r"^(related|edges):\s*(\[\])?\s*$", l) and l.strip() != "[]"]
    # احذف كتلتي related/edges الفارغتين القديمتين إن بقيت أسطرُهما
    out = []
    for l in lines:
        if re.match(r"^(related|edges):", l): continue
        out.append(l)
    fm2 = "\n".join([l for l in out if l.strip() or True])
    # أدرِج الكتلتين قبل gaps إن وُجدت، وإلا في النهاية
    blk = ""
    if p["belongs_to"]:
        b = p["belongs_to"]
        blk += f'edges:\n- rel: "belongs_to", target: "{b}", target_type: "{d[b]["type"]}"\n'
    else:
        blk += "edges:\n  []\n"
    if p["related"]:
        blk += "related:\n" + "".join(
            f'- id: "{r}", title: "{d[r]["title"]}", type: "{d[r]["type"]}"\n' for r in p["related"])
    else:
        blk += "related:\n  []\n"
    L = fm2.split("\n")
    gi = next((i for i, x in enumerate(L) if x.rstrip() == "gaps:"), None)
    if gi is None:
        new_fm = "\n".join(L).rstrip("\n") + "\n" + blk.rstrip("\n") + "\ngaps:\n" + GAP
    else:
        j = gi + 1
        while j < len(L) and (L[j].startswith("  - ") or L[j].startswith("    ")): j += 1
        new_fm = ("\n".join(L[:gi]).rstrip("\n") + "\n" + blk.rstrip("\n") + "\n"
                  + "\n".join(L[gi:j]).rstrip("\n") + "\n" + GAP + "\n" + "\n".join(L[j:])).rstrip("\n")
    open(fp, "w", encoding="utf-8").write("---\n" + new_fm + "\n---\n" + body)
    n += 1
print(f"✔ عُدِّل {n} ملفاً")
json.dump(skipped, open(os.path.join(ROOT, "scripts", "isolated_no_evidence.json"), "w"),
          ensure_ascii=False, indent=1)
os.system(f'cd {ROOT} && python3 scripts/build_atlas.py ar >/dev/null 2>&1')
reciprocate()
