import json, os, re, glob, collections
ROOT="/Users/mina/Desktop/Atlas"; S=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(f"{ROOT}/data.json"))["nodes"]; slugs=set(d)
def isredir(n):
    t=(n.get("title") or ""); c=(n.get("crumb") or ""); l=(n.get("lede") or "")
    return bool(n.get("redirect_to")) or "إحالة" in t or "حجر" in t or "(إحالة)" in c or l.startswith(("إحالة","هذا الملف إحالة","انظر"))
redir={s for s,n in d.items() if isredir(n)}
print("redirect-like nodes total:",len(redir)," of which title-marked:",len([s for s in redir if "إحالة" in d[s]["title"] or "حجر" in d[s]["title"]]))
print("redirect-like NOT title-marked:",[s for s in redir if not("إحالة" in d[s]["title"] or "حجر" in d[s]["title"])])
# dup pairs classification
def norm(s): return re.sub(r'[^a-z0-9]+',' ',(s or "").lower()).strip()
by=collections.defaultdict(list)
for s,n in d.items():
    e=norm(n.get("en"))
    if e: by[(s.split("-")[0],e)].append(s)
tc=collections.defaultdict(list)
for s,n in d.items(): tc[(n.get("title") or "").strip()].append(s)
pairs=set()
for v in list(by.values())+list(tc.values()):
    if len(v)>1: pairs.add(tuple(sorted(v)))
both=[];one=[]
for p in sorted(pairs):
    r=[s for s in p if s in redir]
    (one if r else both).append((p,r))
print("=== dup groups:",len(pairs),"with a redirect member:",len(one),"BOTH substantive:",len(both))
for p,r in both: print("   BOTH:",p,[ (d[s].get("crumb") or "")[:30] for s in p])
open(f"{S}/dup_groups.txt","w").write("\n".join(f"{'REDIR' if r else 'BOTH'}\t{p}\t{r}" for p,r in one+both))
# syn stamped
syn=[s for s in d if s.startswith("syn-")]
cbt=[s for s in syn if any(e[0]=="belongs_to" and e[1]=="sch-cognitive-behavioral" for e in d[s]["edges"])]
print("=== syn total",len(syn),"belongs_to CBT",len(cbt),"CBT related lists any syn:",sum(1 for r in d["sch-cognitive-behavioral"]["related"] if r[0].startswith("syn-")))
print("   syn crumb roots:",collections.Counter((d[s].get("crumb") or "").split("←")[0].strip() for s in cbt).most_common(3))
print("   syn CBT sample with mention of CBT in body:",sum(1 for s in cbt if "المعرفي السلوكي" in json.dumps(d[s]["sections"],ensure_ascii=False)),"/",len(cbt))
# part vs parent part
par={s:e[1] for s,n in d.items() for e in n.get("edges",[]) if e[0]=="belongs_to" and e[1] in slugs}
pp=[(s,d[s].get("part"),par[s],d[par[s]].get("part")) for s in par if d[s].get("part")!="bridge" and d[par[s]].get("part")!="bridge" and d[s].get("part")!=d[par[s]].get("part")]
print("=== part != parent part:",len(pp),collections.Counter((x[1],x[3]) for x in pp))
print("   by parent:",collections.Counter(x[2] for x in pp).most_common(10))
open(f"{S}/part_vs_parent.txt","w").write("\n".join("\t".join(x) for x in pp))
# crumb root pairs 'مدرسة X' vs 'X'
roots=collections.Counter((n.get("crumb") or "").split("←")[0].strip() for n in d.values())
pr=[(r,roots[r],roots[r[len("مدرسة "):]]) for r in roots if r.startswith("مدرسة ") and r[len("مدرسة "):] in roots]
print("=== crumb roots duplicated with/without «مدرسة»:",pr)
# reciprocity: belongs_to child not in parent's related
nr=[(s,par[s]) for s in par if not any(r[0]==s for r in d[par[s]]["related"])]
print("=== belongs_to children not listed in parent related:",len(nr),"of",len(par)," by child prefix:",collections.Counter(s.split("-")[0] for s,_ in nr).most_common(8))
# active_start null but dates has year
ns=[s for s,n in d.items() if "active_start" not in n]
print("=== nodes w/o active_start:",len(ns),collections.Counter(s.split("-")[0] for s in ns).most_common(8))
rec=[s for s in ns if re.search(r'\b1[5-9]\d\d\b|\b20[0-2]\d\b',str(d[s].get("dates","")))]
print("   of which `dates` has a parseable year:",len(rec))
# gaps repeated / lede repeated
gc=collections.Counter(g for n in d.values() for g in n.get("gaps",[]))
print("=== most repeated verbatim gaps:"); [print("  ",v,g[:100]) for g,v in gc.most_common(6)]
lc=collections.Counter((n.get("lede") or "")[:70] for n in d.values()); print("=== repeated lede:",[(v,k) for k,v in lc.most_common(4) if v>2])
# en folder
en=[os.path.basename(f)[:-3] for f in glob.glob(f"{ROOT}/content/en/*/*.md")]
print("=== en files",len(en),"not in ar:",[x for x in en if x not in slugs][:10])
# semantic school edge dump
rows=[]
for s,n in d.items():
    if not s.startswith(("sch-","br-")): continue
    for e in n.get("edges",[]):
        if e[0] in ("evolved_into","evolved_from","superseded_by","split_into","absorbed_by","belongs_to"):
            t=d.get(e[1],{}).get("title",e[1])
            rows.append(f"{n.get('part')}\t{s} [{n.get('active_start')}–{n.get('active_end')}]\t{e[0]}\t{e[1]} ({t[:40]}) [{d.get(e[1],{}).get('active_start')}]")
open(f"{S}/school_edges.txt","w").write("\n".join(sorted(rows))); print("school edges dumped",len(rows))
# thinker belongs_to mismatched with school dates (thinker died before school started)
def yr(v):
    try: return int(v)
    except: return None
tm=[]
for s,p in par.items():
    if not s.startswith("thk-"): continue
    te,ps=yr(d[s].get("active_end")),yr(d[p].get("active_start"))
    if te is not None and ps is not None and te<ps-30: tm.append((s,d[s]["title"][:25],f"{d[s].get('active_start')}–{te}",p,f"from {ps}"))
print("=== thinkers whose activity ended >30y before their school began:",len(tm)); [print("  ",x) for x in tm]
