import json, os, re, glob, collections
ROOT="/Users/mina/Desktop/Atlas"; S=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(f"{ROOT}/data.json"))["nodes"]; slugs=set(d)
files=[f for f in glob.glob(f"{ROOT}/content/ar/*/*.md") if "/drafts/" not in f and "/_merged/" not in f]
raw={os.path.basename(f)[:-3]:(f,open(f,encoding="utf-8").read()) for f in files}
def yr(v):
    try: return int(v)
    except: return None
def dump(name,rows):
    with open(f"{S}/{name}.txt","w") as fh:
        for r in rows: fh.write(("\t".join(map(str,r)) if isinstance(r,(list,tuple)) else str(r))+"\n")
    print(f"--- {name}: {len(rows)}")
# 1 duplicate titles full
tc=collections.defaultdict(list)
for s,n in d.items(): tc[(n.get("title") or "").strip()].append(s)
dupt=[(k,v) for k,v in tc.items() if len(v)>1]; dump("dup_titles",dupt); [print("  ",x) for x in dupt]
# 2/3 batch-stamped parents: belongs_to distribution for ctx/syn/dis/met/trm/dbt/que/evt/exp/stu/ins/crt
par={s:e[1] for s,n in d.items() for e in n.get("edges",[]) if e[0]=="belongs_to"}
for pref in ("ctx","syn","dis","evt","exp","stu","ins","crt","met","trm","dbt","que","axm","axi","wrk","con","tec"):
    c=collections.Counter(par.get(s,"∅") for s in d if s.startswith(pref+"-"))
    print(pref, c.most_common(6))
# suspicious: parent psychology school for a node whose active_start predates parent by >100y
sus=[(s,par[s],d[s].get("active_start"),d[par[s]].get("active_start")) for s in par if par[s] in slugs and yr(d[s].get("active_start")) is not None and yr(d[par[s]].get("active_start")) is not None and yr(d[s]["active_start"])<yr(d[par[s]]["active_start"])-100]
dump("anachronistic_belongs_to",sus)
# 6 unresolved textual edge targets
title2slug={(n.get("title") or "").strip():s for s,n in d.items()}
un=[(s,e[0],e[1]) for s,n in d.items() for e in n.get("edges",[]) if e[1] not in slugs]
dump("edge_text_targets",un); [print("  ",x) for x in un]
# 7 sources placeholder by dir
PH=("يفتقر هذا الملف","لا تتوفر مصادر","لم تُتَح","بلا مصادر")
ph=[]
for b,(f,t) in raw.items():
    m=re.search(r'## المصادر\n(.*?)(?=\n## |\Z)',t,re.S); src=m.group(1).strip() if m else ""
    if not m or len(src)<40 or any(p in src for p in PH): ph.append((f.split("/")[-2],b,d[b].get("part")))
dump("sources_placeholder",ph); print(collections.Counter(x[0] for x in ph)); print(collections.Counter(x[2] for x in ph))
# 8 short bodies by dir
sh=[]
for b,(f,t) in raw.items():
    body=t.split("\n---\n",1)[1] if "\n---\n" in t else t
    w=len(body.split())
    if w<120: sh.append((f.split("/")[-2],b,w,(d[b].get("title") or "")[:40]))
dump("short_bodies",sorted(sh,key=lambda x:x[2])); print(collections.Counter(x[0] for x in sh))
unver=[s for s,n in d.items() if "غير محقَّق" in (n.get("title") or "") or "غير محقق" in (n.get("title") or "")]
dump("unverified_titles",unver)
# 9 links to deprecated stubs
dep={s for s,n in d.items() if ("حجر" in (n.get("title") or "") and "انظر" in n["title"]) or "إحالة" in (n.get("title") or "")}
todep=[(s,r[0]) for s,n in d.items() for r in n.get("related",[]) if r[0] in dep]
dump("links_to_deprecated",todep); dump("deprecated_stubs",[(s,d[s]["title"],d[s].get("redirect_to","")) for s in dep])
# 10 URL sanity
badurl=[]
for b,(f,t) in raw.items():
    for m in re.findall(r'\]\(([^)]*)\)',t):
        if m.startswith("http"):
            if m.count("(")!=m.count(")") or " " in m: badurl.append((b,m))
    for m in re.findall(r'https?://[^\s)\]>]+',t):
        if m.count("(")>m.count(")"): pass
dump("bad_urls",badurl)
# bare url count & domains
dom=collections.Counter(re.sub(r'https?://([^/]+).*',r'\1',m) for b,(f,t) in raw.items() for m in re.findall(r'https?://[^\s)\]>"]+',t))
print("domains",dom.most_common(12))
# 11 part vs crumb
cp=[(s,n.get("part"),n.get("crumb")) for s,n in d.items() if n.get("part")=="philosophy" and (n.get("crumb") or "").split("←")[0].strip() in ("مدرسة التحليل النفسي","التحليل النفسي","علم النفس","المعرفية السلوكية","الإنسانية")]
dump("philosophy_part_psych_crumb",cp); print(collections.Counter(x[2].split("←")[0].strip() for x in cp))
cp2=[(s,n.get("part"),n.get("crumb")) for s,n in d.items() if n.get("part")=="psychology" and (n.get("crumb") or "").split("←")[0].strip() in ("الفلسفة","الفلسفة الوجودية","المفاهيم الفلسفية الكبرى","المكتبة الفلسفية","أعلام الفلسفة والفكر")]
dump("psychology_part_phil_crumb",cp2); print("psych part/phil crumb",len(cp2))
generic=[(s,n.get("part"),n.get("crumb")) for s,n in d.items() if (n.get("crumb") or "").split("←")[0].strip() in ("الناس","نقد")]
dump("generic_crumb_root",generic)
roots=collections.Counter((n.get("crumb") or "").split("←")[0].strip() for n in d.values()); print("distinct crumb roots",len(roots)); dump("crumb_roots",roots.most_common())
# 12 school-thinker date mismatch in related
mis=[]
for s,n in d.items():
    if not s.startswith(("sch-","br-")): continue
    a,b_=yr(n.get("active_start")),yr(n.get("active_end"))
    if a is None: continue
    for r in n.get("related",[]):
        if r[0].startswith("thk-") and r[0] in slugs:
            ta,tb=yr(d[r[0]].get("active_start")),yr(d[r[0]].get("active_end"))
            if ta is not None and b_ is not None and ta>b_+30: mis.append((s,r[0],f"school {a}-{b_}",f"thinker {ta}-{tb}"))
            if tb is not None and tb< a-100: mis.append((s,r[0],f"school {a}-{b_}",f"thinker {ta}-{tb}"))
dump("school_thinker_date_mismatch",mis)
# evolved_into/from anachronism
ev=[]
for s,n in d.items():
    for e in n.get("edges",[]):
        if e[1] in slugs and e[0] in ("evolved_into","evolved_from","superseded_by","split_into","absorbed_by"):
            a,p=yr(n.get("active_start")),yr(d[e[1]].get("active_start"))
            if a is None or p is None: continue
            if e[0] in("evolved_into","superseded_by","absorbed_by","split_into") and p<a-30: ev.append((s,e[0],e[1],a,p))
            if e[0]=="evolved_from" and p>a+30: ev.append((s,e[0],e[1],a,p))
dump("evolution_anachronism",ev)
# 13 empty schools
kids=collections.Counter(par.values())
emp=[(s,d[s].get("part"),len(d[s].get("related",[])),d[s]["title"][:40]) for s in d if s.startswith(("sch-","br-")) and kids[s]==0 and len(d[s].get("related",[]))<3]
dump("empty_schools",emp)
# 14-20 misc
dump("level_empty",[s for s,n in d.items() if not n.get("level")])
dump("level_odd",[(s,n.get("level")) for s,n in d.items() if n.get("level") not in ("متقدم","متوسط","مبتدئ")])
dump("odd_prefix_or_type",[(s,n.get("type")) for s,n in d.items() if not s.startswith(("thk-","con-","sch-","br-","tec-","wrk-","rel-","dbt-","que-","met-","trm-","ins-","stu-","evt-","exp-","crt-","dia-","syn-","dis-","ctx-","axm-","axi-")) or (s.startswith("con-") and n.get("type")!="مفهوم") or (s.startswith("wrk-") and n.get("type")!="عمل / كتاب")])
dump("sociology_part",[s for s,n in d.items() if n.get("part")=="sociology"])
dump("self_edge",[(s,e) for s,n in d.items() for e in n.get("edges",[]) if e[1]==s])
dump("thinkers_no_dates",[(s,d[s]["title"]) for s in d if s.startswith("thk-") and not str(d[s].get("dates","")).strip()])
dump("odd_keys",[(s,k) for s,n in d.items() for k in n if k in ("crumbs","redirect_to","status","verification_status")])
# duplicate headings / empty sections full
duph=[];emp2=[]
for b,(f,t) in raw.items():
    body=t.split("\n---\n",1)[1] if "\n---\n" in t else t
    secs=re.findall(r'^## (.+)$',body,re.M)
    if len(secs)!=len(set(secs)): duph.append((b,[x for x,c in collections.Counter(secs).items() if c>1]))
    parts=re.split(r'^## .+$',body,flags=re.M)
    for i,p in enumerate(parts[1:]):
        if len(p.strip())<15: emp2.append((b,secs[i] if i<len(secs) else "?")); break
dump("dup_headings",duph); dump("empty_sections",emp2)
# 26 frontmatter lines dropped by parser
drop=[]
for b,(f,t) in raw.items():
    m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
    if not m: continue
    for ln in m.group(1).split("\n"):
        if not ln.strip() or ln.startswith((" ","\t","- ")) or ln.strip() in ("related:","edges:","gaps:"): continue
        if not re.match(r'^[a-zA-Z0-9_-]+:\s*"(.*)"\s*$',ln) and not re.match(r'^[a-zA-Z0-9_-]+:\s*(-?\d+)\s*$',ln): drop.append((b,ln[:80]))
dump("frontmatter_dropped_lines",drop); print(collections.Counter(x[1].split(":")[0] for x in drop).most_common(10))
# 30 en field arabic
dump("en_field_arabic",[(s,n.get("en")) for s,n in d.items() if re.search(r'[؀-ۿ]',n.get("en") or "")])
# 32 crumb last != title
cl=[(s,n["title"][:40],(n.get("crumb") or "").split("←")[-1].strip()[:40]) for s,n in d.items() if (n.get("crumb") or "").split("←")[-1].strip()!=(n.get("title") or "").strip()]
print("crumb tail != title:",len(cl)); dump("crumb_tail_mismatch",cl)
# drafts collisions
drafts=[os.path.basename(f)[:-3] for f in glob.glob(f"{ROOT}/content/ar/drafts/*.md")]
print("drafts",len(drafts),"colliding with live:",len([x for x in drafts if x in slugs]))
draft_refs=[(s,r[0]) for s,n in d.items() for r in n.get("related",[]) if r[0] in set(drafts) and r[0] not in slugs]
print("live related -> draft slug:",len(draft_refs))
# gaps counts
g=collections.Counter(len(n.get("gaps",[])) for n in d.values()); print("gaps dist",sorted(g.items())[:12])
# related count zero
print("nodes w/ zero related:",len([s for s,n in d.items() if not n.get("related")]))
# nodes with zero edges and not thinker
print("nodes no edges:",collections.Counter(s.split("-")[0] for s,n in d.items() if not n.get("edges")))
