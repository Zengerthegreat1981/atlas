import sys, os, re, glob, json
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
mod = sys.argv[1]
PATHS = json.load(open(os.path.join(os.path.dirname(__file__), mod + "_paths.json"), encoding="utf-8"))
nodes = {}
for p in glob.glob(os.path.join(ROOT, "content", "en", "*", "*.md")):
    t = open(p, encoding="utf-8").read(2500)
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', t, re.M); ty = re.search(r'^type:\s*["\']?(.*?)["\']?\s*$', t, re.M)
    nodes[os.path.basename(p)[:-3]] = (m.group(1) if m else "", ty.group(1) if ty else "")
root = PATHS["root"]; rp = os.path.join(ROOT, "content", "en", PATHS["root_folder"], root + ".md")
t = open(rp, encoding="utf-8", newline="").read(); nl = "\r\n" if "\r\n" in t[:300] else "\n"
m = re.match(r"^(---\s*\r?\n)(.*?)(\r?\n---\s*\r?\n)(.*)$", t, re.S); fm, body = m.group(2), m.group(4)
rel = []; seen = set()
secs = [nl + "## Reading Paths" + nl]
for title, slugs in PATHS["paths"]:
    ok = [s for s in slugs if s in nodes]
    if not ok: continue
    secs.append(nl + f"### {title}" + nl)
    for i, s in enumerate(ok, 1):
        secs.append(f"{i}. {nodes[s][0]}" + nl)
        if s not in seen:
            seen.add(s); rel.append(f'  - id: "{s}", title: "{nodes[s][0]}", type: "{nodes[s][1]}"')
fm = re.sub(r"^related:.*?(?=^\w|\Z)", "", fm, flags=re.M | re.S).rstrip() + nl + "related:" + nl + nl.join(rel) + nl
body = re.sub(r"\n## Reading Path.*?(?=\n## |\Z)", "", body, flags=re.S)
if re.search(r"^## Sources", body, re.M):
    body = re.sub(r"^(## Sources)", "".join(secs).strip() + nl + nl + r"\1", body, count=1, flags=re.M)
else: body = body.rstrip() + nl + "".join(secs)
open(rp, "w", encoding="utf-8", newline="").write(m.group(1) + fm.rstrip() + m.group(3) + body)
print(len(rel), "linked from", root)
