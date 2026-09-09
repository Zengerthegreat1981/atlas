import json, re, collections, unicodedata, os
ROOT="/Users/mina/Desktop/Atlas"; S=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(f"{ROOT}/data.json"))["nodes"]
def asc(s): return unicodedata.normalize("NFKD",s or "").encode("ascii","ignore").decode().lower()
mis=[]
for s,n in d.items():
    if not s.startswith("thk-"): continue
    en=asc(n.get("en")); 
    if not en or "unverified" in en or "founders" in en or "[" in (n.get("en") or ""): continue
    toks=[t for t in re.split(r'[^a-z]+',en) if len(t)>2 and t not in ("the","and","von","van","der","de","al","ibn","bin","abu","el","da","di","le","la","du","des")]
    if not toks: continue
    body=s[4:].replace("-","")
    if not any(t[:4] in body or body[-4:] in t for t in toks): mis.append((s,n.get("en"),n["title"][:30]))
print("=== thinker slug does not match en name:",len(mis)); [print("  ",x) for x in mis]
open(f"{S}/slug_name_mismatch.txt","w").write("\n".join("\t".join(x) for x in mis))
# fuzzy dup titles
def nt(t): return re.sub(r'\s+',' ',re.sub(r'\(.*?\)|—.*$|:.*$','',t or '')).strip()
g=collections.defaultdict(list)
for s,n in d.items(): g[(s.split("-")[0],nt(n.get("title")))].append(s)
fd=[(k[1],v) for k,v in g.items() if len(v)>1 and k[1]]
print("=== fuzzy dup titles (same prefix):",len(fd)); [print("  ",x) for x in fd]
