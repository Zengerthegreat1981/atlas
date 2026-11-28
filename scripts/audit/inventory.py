#!/usr/bin/env python3
"""Read-only baseline of the English corpus. One command reproduces every metric.

  python3 scripts/audit/inventory.py        # writes reports/audit/*.csv and summary.md
"""
import collections, csv, glob, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "reports", "audit")
N = lambda s: unicodedata.normalize("NFC", s).strip()
EDGE = re.compile(r'-\s*rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"\s*,\s*target_type:\s*"([^"]*)"')
REL = re.compile(r'-\s*id:\s*"?([^",\r\n]+)"?')
SLUGISH = re.compile(r"^[a-z]{2,6}-[\w-]+$")

CANDIDATES = """Mary Main|Cindy Hazan|Peter Salovey|John D. Mayer|Kirk Strosahl|Eric Kandel|Kurt Lewin|Paul Meehl|
Martín-Baró|van der Kolk|Allan Schore|Karl Friston|Edward Tronick|William James|Aaron Beck|George Kelly|Virginia Satir|
Peter Levine|Karen Horney|Ferenczi|Jerome Bruner|Ulric Neisser|Zimbardo|Joseph LeDoux|Francine Shapiro|Gottman|Fonagy|
Porges|Loftus|Charles Darwin|Wilhelm Reich|Stanislav Grof|Milton Erickson|von Franz|Sue Johnson|Alexander Lowen|Seneca|
George Berkeley|Lakatos|Feyerabend|Horkheimer|Marcuse|Lukács|Whitehead|Iris Murdoch|Philippa Foot|Anscombe|Simone Weil|
Adam Smith|Donald Davidson|Wilfrid Sellars|Cicero|Montaigne|Chomsky|Kripke|Erich Fromm|Levinas|Bernard Williams|
Paulo Freire|Maimonides|Hans Jonas|Parfit|Nussbaum|Charles Taylor|Churchland|Metzinger|Varela|Mounier|Dōgen|Balkhi|
Miskawayh|Ibn Bajja"""


def load(lang):
    pages = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "content", lang, "*", "*.md"))):
        if any(x in f for x in ("/._", "/drafts/", "/_merged/")) or f.endswith("README.md"):
            continue
        text = open(f, encoding="utf-8", errors="replace").read().replace("\r", "")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
        if not m:
            continue
        head, body = m.groups()
        field = lambda k: (re.search(r'^%s:[ \t]*"?(.*?)"?[ \t]*$' % k, head, re.M) or [None, ""])[1]
        blocks, cur = collections.defaultdict(list), None
        for line in head.split("\n"):
            k = re.match(r"^(\w+):", line)
            if k:
                cur = k[1]
            elif cur:
                blocks[cur].append(line)
        pages[N(os.path.basename(f)[:-3])] = dict(
            path=os.path.relpath(f, ROOT), folder=f.split(os.sep)[-2],
            **{k: field(k) for k in ("id", "type", "part", "title", "en", "crumb", "quality")},
            related=[N(x) for l in blocks["related"] for x in REL.findall(l)],
            edges=[e for l in blocks["edges"] for e in EDGE.findall(l)],
            sources=bool(re.search(r"^## .*(Source|Reference|Bibliograph)", body, re.M | re.I)),
            url="http" in body)
    return pages


def title_index(pages):
    idx = collections.defaultdict(set)
    for slug, p in pages.items():
        for k in ("title", "en"):
            if p[k]:
                idx[N(p[k]).casefold()].add(slug)
    return idx


def target_status(target, pages, idx):
    t = N(target)
    if t in pages:
        return "slug", t
    if SLUGISH.match(t):
        return "slug-broken", ""
    hit = idx.get(t.casefold(), set())
    if len(hit) == 1:
        return "name-exact", next(iter(hit))
    return ("name-ambiguous", "") if hit else ("name-unresolved", "")


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def main():
    os.makedirs(OUT, exist_ok=True)
    en = load("en")
    idx = title_index(en)
    by_id = {p["id"]: s for s, p in en.items() if p["id"]}
    inbound = collections.Counter(by_id.get(r, r) for s, p in en.items() for r in set(p["related"]))
    status, kinds, unresolved, rows = collections.Counter(), collections.Counter(), collections.defaultdict(set), []
    for s, p in en.items():
        for rel, tgt, _ in p["edges"]:
            st, _slug = target_status(tgt, en, idx)
            status[st] += 1
            kinds[rel] += 1
            if st != "slug" and st != "name-exact":
                unresolved[N(tgt)].add(s)
        rows.append([s, p["id"], p["folder"], p["part"], p["crumb"], p["title"], p["en"], inbound[s],
                     len(p["related"]), len(p["edges"]), int(p["sources"]), int(p["url"]), p["quality"]])
    write("inventory.csv", "slug id folder part crumb title en inbound related edges sources_section has_url quality".split(), rows)
    write("wanted-hubs.csv", ["target_name", "pages", "wanted_by"],
          sorted(([t, len(v), ";".join(sorted(v))] for t, v in unresolved.items()), key=lambda r: (-r[1], r[0])))

    # duplicates: same normalized name, or same slug once prefixes and initials are ignored
    groups = collections.defaultdict(set)
    for s, p in en.items():
        for k in ("title", "en"):
            if p[k]:
                words = [w for w in re.findall(r"\w+", p[k].casefold()) if len(w) > 1]  # drop initials
                groups[(p["folder"], " ".join(words))].add(s)
    dups = sorted({tuple(sorted(v)) for v in groups.values() if len(v) > 1})
    write("duplicate-names.csv", ["slugs"], [[";".join(d)] for d in dups])

    # part vs crumb root
    roots = collections.defaultdict(collections.Counter)
    for s, p in en.items():
        roots[p["part"]][re.split(r"\s*[›>·/←→|]\s*", p["crumb"])[0].strip()] += 1
    mism = []
    for s, p in en.items():
        root = re.split(r"\s*[›>·/←→|]\s*", p["crumb"])[0].strip()
        usual = roots[p["part"]].most_common(1)[0][0]
        if root != usual:
            mism.append([s, p["part"], root, usual])
    write("part-crumb-mismatch.csv", ["slug", "part", "crumb_root", "usual_root_for_part"], mism)

    people = {s: (p["title"] + " " + p["en"]).casefold() for s, p in en.items() if p["folder"] == "thinkers"}
    cand = []
    for name in (c.strip() for c in CANDIDATES.split("|")):
        words = name.casefold().replace(".", "").split()
        hit = [s for s, v in people.items()
               if all(re.search(r"\b%s\b" % re.escape(w), v.replace(".", "")) for w in words)]
        cand.append([name, "exists" if hit else "missing", ";".join(hit)])
    write("candidates.csv", ["name", "status", "slugs"], cand)

    # Arabic related links of shared pages that point at pages with no English version yet
    ar = load("ar")
    wanted = collections.defaultdict(set)
    for s in set(en) & set(ar):
        for r in ar[s]["related"]:
            if r in ar and r not in en:
                wanted[r].add(s)
    zero_in = {s for s in en if not inbound[s]}
    write("wanted-links.csv", ["target_slug", "wanted_by_count", "newly_connects_zero_inbound", "wanted_by"],
          sorted(([t, len(v), len(v & zero_in), ";".join(sorted(v))] for t, v in wanted.items()),
                 key=lambda r: (-r[1], r[0])))

    c = collections.Counter(p["part"] for p in en.values())
    lines = [
        "# English corpus baseline (generated by scripts/audit/inventory.py; do not edit)", "",
        f"- pages: {len(en)}",
        f"- zero related: {sum(not p['related'] for p in en.values())}",
        f"- zero inbound related: {len(zero_in)}",
        f"- zero edges: {sum(not p['edges'] for p in en.values())}",
        f"- sources section: {sum(p['sources'] for p in en.values())}; with a URL: {sum(p['url'] for p in en.values())}",
        f"- badged unverified: {sum('unverified' in p['quality'] for p in en.values())}; incomplete: {sum('incomplete' in p['quality'] for p in en.values())}",
        f"- edge targets: {dict(sorted(status.items()))}",
        f"- relation types: {len(kinds)} {dict(kinds.most_common())}",
        f"- duplicate-name groups: {len(dups)}; part/crumb mismatches: {len(mism)}",
        f"- candidates missing: {sum(r[1] == 'missing' for r in cand)} of {len(cand)}",
        f"- Arabic-only link targets wanted by English pages: {len(wanted)}",
        "- pages per part: " + ", ".join(f"{k} {v}" for k, v in c.most_common()),
    ]
    open(os.path.join(OUT, "summary.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
