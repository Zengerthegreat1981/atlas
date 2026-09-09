import json, os, re, glob, collections
ROOT="/Users/mina/Desktop/Atlas"; S=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(f"{ROOT}/data.json"))["nodes"]; slugs=set(d)
def norm(s): return re.sub(r'[^a-z0-9]+',' ',(s or "").lower()).strip()
# near-dup by en field within same prefix
by=collections.defaultdict(list)
for s,n in d.items():
    e=norm(n.get("en"))
    if e: by[(s.split("-")[0],e)].append(s)
dups=[(k,v) for k,v in by.items() if len(v)>1]
print("=== same-en duplicates within type:",len(dups)); [print("  ",k[1][:50],v) for k,v in sorted(dups)]
# cross-type same en (con vs wrk etc.) count only
cross=collections.defaultdict(set)
for s,n in d.items():
    e=norm(n.get("en"))
    if e: cross[e].add(s.split("-")[0])
# edge type mismatch breakdown
mm=collections.Counter()
for s,n in d.items():
    for e in n.get("edges",[]):
        if e[1] in slugs and e[2] and e[2]!=d[e[1]].get("type"): mm[(e[2],d[e[1]]["type"])]+=1
print("=== edge target_type mismatch pairs:"); [print("  ",k,v) for k,v in mm.most_common()]
# related stale: substantive vs cosmetic
sub=[]; cos=0
for s,n in d.items():
    for r in n.get("related",[]):
        if r[0] in slugs:
            a=r[1].strip(); b=(d[r[0]].get("title") or "").strip()
            if a==b: continue
            if re.sub(r'\s*\(.*?\)\s*','',a)==re.sub(r'\s*\(.*?\)\s*','',b) or a in b or b in a: cos+=1
            else: sub.append((s,r[0],a[:35],b[:35]))
print("=== related stale titles: cosmetic",cos,"substantive",len(sub)); [print("  ",x) for x in sub[:25]]
open(f"{S}/related_stale_substantive.txt","w").write("\n".join("\t".join(x) for x in sub))
# philosophy part w/ psychoanalysis crumb sample
ps=[(s,n["crumb"][:60]) for s,n in d.items() if n.get("part")=="philosophy" and (n.get("crumb") or "").startswith(("مدرسة التحليل النفسي","التحليل النفسي"))]
print("=== philosophy-part psychoanalysis-crumb sample:",len(ps)); [print("  ",x) for x in ps[:12]]
print("   prefixes:",collections.Counter(x[0].split("-")[0] for x in ps))
# thinkers short
tw=[(s,len(" ".join(x[1] for x in n.get("sections",[])).split())+len((n.get("lede") or "").split())) for s,n in d.items() if s.startswith("thk-")]
print("=== thinkers by body words: <50:",sum(1 for _,w in tw if w<50),"<80:",sum(1 for _,w in tw if w<80),"<120:",sum(1 for _,w in tw if w<120))
# non-thinker short bodies
sh=[l.split("\t") for l in open(f"{S}/short_bodies.txt")]
print("=== short non-thinker:"); [print("  ",x[0],x[1],x[2],x[3].strip()) for x in sh if x[0]!="thinkers"][:0]
for x in sh:
    if x[0]!="thinkers": print("  ",x[0],x[1],x[2],x[3].strip())
# empty schools rest
print("=== empty schools by part/prefix:",collections.Counter((l.split("\t")[1],l.split("\t")[0].split("-")[0]) for l in open(f"{S}/empty_schools.txt")))
# do parents link back to those empty br- children?
par={s:e[1] for s,n in d.items() for e in n.get("edges",[]) if e[0]=="belongs_to"}
nb=[]
for l in open(f"{S}/empty_schools.txt"):
    s=l.split("\t")[0]; p=par.get(s)
    if p and p in slugs and not any(r[0]==s for r in d[p]["related"]): nb.append((s,p))
print("=== empty br- whose parent does NOT link back:",len(nb)); [print("  ",x) for x in nb[:10]]
# inbound-only nodes (no outgoing related at all)
print("=== nodes with zero related, by prefix:",collections.Counter(s.split("-")[0] for s,n in d.items() if not n.get("related")))
# gaps: template-y gap strings repeated verbatim across many files
gc=collections.Counter(g for n in d.values() for g in n.get("gaps",[]))
print("=== most repeated verbatim gap strings:"); [print("  ",v,g[:90]) for g,v in gc.most_common(8)]
# repeated lede (template)
lc=collections.Counter((n.get("lede") or "")[:80] for n in d.values()); print("=== repeated lede prefixes:"); [print("  ",v,k) for k,v in lc.most_common(5) if v>2]
# sections titles frequency - sanity
sc=collections.Counter(x[0] for n in d.values() for x in n.get("sections",[])); print("=== top sections:",sc.most_common(12))
