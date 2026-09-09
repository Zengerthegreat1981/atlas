import json, os, re, glob, collections, sys
ROOT="/Users/mina/Desktop/Atlas"
d=json.load(open(f"{ROOT}/data.json"))["nodes"]
slugs=set(d)
files=[f for f in glob.glob(f"{ROOT}/content/ar/*/*.md") if "/drafts/" not in f and "/_merged/" not in f]
def fm(t):
    m=re.match(r'^---\n(.*?)\n---\n(.*)$',t,re.S); return (m.group(1),m.group(2)) if m else (None,t)
raw={}
for f in files:
    t=open(f,encoding="utf-8").read(); raw[os.path.basename(f)[:-3]]=(f,t)
print("files",len(files),"nodes",len(d))
# A. filename vs slug field vs node key
bad_slug=[]; nofm=[]
for b,(f,t) in raw.items():
    y,body=fm(t)
    if y is None: nofm.append(b); continue
    m=re.search(r'^slug:\s*"([^"]*)"',y,re.M)
    if not m or m.group(1)!=b: bad_slug.append((b,m.group(1) if m else None))
print("A1 no frontmatter:",len(nofm),nofm[:5])
print("A2 slug!=filename:",len(bad_slug),bad_slug[:10])
missing_in_data=[b for b in raw if b not in d]; extra=[s for s in d if s not in raw]
print("A3 file not in data.json:",len(missing_in_data),missing_in_data[:5]); print("A4 node w/o file:",len(extra),extra[:5])
# B. type vs directory; prefix vs directory
dirtype=collections.defaultdict(collections.Counter); prefix_dir=collections.defaultdict(collections.Counter)
for b,(f,t) in raw.items():
    dr=f.split("/")[-2]; dirtype[dr][d.get(b,{}).get("type")]+=1; prefix_dir[dr][b.split("-")[0]]+=1
for dr in sorted(dirtype): print("B",dr,dict(dirtype[dr]),"| prefixes",dict(prefix_dir[dr]))
# C. required fields
REQ=["slug","id","type","title","crumb","part","level","en"]
miss=collections.Counter(); missex=collections.defaultdict(list)
for s,n in d.items():
    for k in REQ:
        if not str(n.get(k,"")).strip(): miss[k]+=1; missex[k].append(s)
print("C missing fields:",dict(miss)); 
for k in missex: print("   ",k,missex[k][:8])
print("C part values:",collections.Counter(n.get("part") for n in d.values()))
print("C level values:",collections.Counter(n.get("level") for n in d.values()))
# duplicate ids
idc=collections.Counter(n.get("id") for n in d.values()); print("C dup ids:",[(k,v) for k,v in idc.items() if v>1][:10], "count",sum(1 for v in idc.values() if v>1))
tc=collections.Counter((n.get("title") or "").strip() for n in d.values()); dupt=[(k,v) for k,v in tc.items() if v>1]
print("C dup titles:",len(dupt),dupt[:15])
# D. edges integrity
edge_dang=[]; edge_type_mis=[]; rel_kinds=collections.Counter(); self_edge=[]
for s,n in d.items():
    for e in n.get("edges",[]):
        rel_kinds[e[0]]+=1
        if e[1]==s: self_edge.append(s)
        if e[1] not in slugs:
            # resolves by title?
            edge_dang.append((s,e[0],e[1]))
        elif e[2] and d[e[1]].get("type") and e[2]!=d[e[1]]["type"]:
            edge_type_mis.append((s,e[1],e[2],d[e[1]]["type"]))
print("D rel kinds:",dict(rel_kinds))
title2slug={ (n.get("title") or "").strip():s for s,n in d.items()}
unres=[x for x in edge_dang if x[2] not in title2slug]; bytitle=[x for x in edge_dang if x[2] in title2slug]
print("D edge target not a slug:",len(edge_dang)," of which resolve by title:",len(bytitle)," unresolved:",len(unres)); print("   ",unres[:10]); print("   by-title sample",bytitle[:5])
print("D edge target_type mismatch:",len(edge_type_mis),edge_type_mis[:8]); print("D self edges",len(self_edge))
# E. related title/type staleness
rt=[]; rty=[]
for s,n in d.items():
    for r in n.get("related",[]):
        if r[0] in slugs:
            if r[1].strip()!=(d[r[0]].get("title") or "").strip(): rt.append((s,r[0],r[1][:30],(d[r[0]].get("title") or "")[:30]))
            if r[2]!=d[r[0]].get("type"): rty.append((s,r[0],r[2],d[r[0]].get("type")))
print("E related stale title:",len(rt),rt[:6]); print("E related stale type:",len(rty),rty[:6])
# F. body: placeholder sources, short body, inline links
ph=[]; short=[]; inl=[]; en_left=[]; todo=[]; emptysec=[]; duph=[]
PH=("يفتقر هذا الملف","لا تتوفر مصادر","لم تُتَح","لم يُتحقّق","بلا مصادر")
for b,(f,t) in raw.items():
    y,body=fm(t)
    if y is None: continue
    m=re.search(r'## المصادر\n(.*?)(?=\n## |\Z)',body,re.S)
    src=m.group(1).strip() if m else ""
    if not m or len(src)<40 or any(p in src for p in PH): ph.append(b)
    words=len(re.sub(r'\s+',' ',body).split())
    if words<120: short.append((b,words))
    for mm in re.findall(r'\]\(([^)]+)\)',body): inl.append((b,mm))
    if re.search(r'\b(TODO|TBD|XXX|FIXME|lorem)\b',t): todo.append(b)
    secs=re.findall(r'^## (.+)$',body,re.M)
    if len(secs)!=len(set(secs)): duph.append(b)
    for part in re.split(r'^## .+$',body,flags=re.M)[1:]:
        if len(part.strip())<15: emptysec.append(b); break
print("F sources placeholder/none:",len(ph)); 
print("F short bodies (<120w):",len(short),sorted(short,key=lambda x:x[1])[:10])
print("F inline md links:",len(inl),inl[:5]); print("F TODO marks:",len(todo),todo[:5]); print("F dup headings:",len(duph),duph[:5]); print("F empty sections:",len(emptysec),emptysec[:8])
# G. anachronism: belongs_to / evolved_into child older than parent
def yr(v):
    try: return int(v)
    except: return None
ana=[]
for s,n in d.items():
    a=yr(n.get("active_start"))
    for e in n.get("edges",[]):
        if e[1] in slugs:
            p=yr(d[e[1]].get("active_start"))
            if e[0]=="evolved_into" and a is not None and p is not None and p< a-50: ana.append((s,e[0],e[1],a,p))
            if e[0]=="belongs_to" and a is not None and p is not None and a< p-100: ana.append((s,e[0],e[1],a,p))
print("G anachronistic edges:",len(ana)); [print("   ",x) for x in ana[:30]]
# H. schools/branches with no members and no related
kids=collections.Counter(e[1] for n in d.values() for e in n.get("edges",[]) if e[0]=="belongs_to")
empty_sch=[s for s in d if s.startswith(("sch-","br-")) and kids[s]==0 and len(d[s].get("related",[]))<3]
print("H schools/branches w/ no members & <3 related:",len(empty_sch),empty_sch[:15])
# I. crumb inconsistency: crumb first token vs part
cp=collections.Counter((n.get("part"),(n.get("crumb") or "").split("←")[0].strip()) for n in d.values())
print("I part vs crumb-root:"); [print("   ",k,v) for k,v in cp.most_common(40)]
# J. en field non-latin / title contains 'حجر'
deprecated=[s for s,n in d.items() if ("حجر" in (n.get("title") or "") and "انظر" in n["title"]) or "إحالة" in (n.get("title") or "")]
print("J deprecated stubs:",len(deprecated),deprecated[:10])
# K. thinkers: birth/death fields
tk=[s for s in d if s.startswith("thk-")]
nodates=[s for s in tk if not any(str(d[s].get(k,"")).strip() for k in ("dates","active_start","born","birth"))]
print("K thinkers:",len(tk),"no dates:",len(nodates),nodates[:8])
keys=collections.Counter(k for s in tk for k in d[s])
print("K thinker keys:",dict(keys))
