import sys, os, glob, re, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def title_of(path):
    t = open(path, encoding="utf-8", errors="replace").read(1500)
    m = re.search(r'^en:\s*["\']?(.*?)["\']?\s*$', t, re.M) or re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', t, re.M)
    return (m.group(1) if m else "")[:70]
def index(lang):
    return {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, "content", lang, "*", "*.md"))}
def render(mod, label):
    P = importlib.import_module(mod + "_scope")
    en, ar = index("en"), index("ar")
    out = [f"# {label} — closed v1 scope (EN)", "",
           "Decision record for audit P0.5. Entries marked **EN** exist in English; **from AR** were translated from the",
           "Arabic asset with the same slug/id (fact-checked, corrections in `reports/scope/corrections.txt`); **new** were authored.",
           "Anything not listed is out of v1 and belongs in the next-release backlog.", ""]
    tot = 0
    for g, s in P.SCOPE.items():
        out += [f"## {g}", "", "| slug | title | status |", "|---|---|---|"]
        for sl in s.split():
            tot += 1
            st = "EN" if sl in en else "MISSING"
            out.append(f"| {sl} | {title_of(en[sl]) if sl in en else title_of(ar[sl]) if sl in ar else ''} | {st} |")
        out.append("")
    out += ["## new-authored", "", "| slug | title | status |", "|---|---|---|"]
    for sl, v in P.NEW.items():
        tot += 1; out.append(f"| {sl} | {v[1]} | {'EN' if sl in en else 'MISSING'} |")
    out.append(f"\nTotal scope entries: {tot}")
    os.makedirs(os.path.join(ROOT, "reports", "scope"), exist_ok=True)
    open(os.path.join(ROOT, "reports", "scope", f"{mod}-scope.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(mod, tot)
if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
