# -*- coding: utf-8 -*-
"""مراجعةٌ ختاميةٌ مستقلّةٌ — تُفحَص من الصفر، ولا تعتمد على أيِّ سكربتٍ سابق."""
import json,os,re,glob,collections,unicodedata
ROOT="/Users/mina/Desktop/Atlas"
FAIL=[]; WARN=[]
def bad(t,n,ex=(),fatal=True):
    (FAIL if fatal else WARN).append(t)
    print(f"  {'❌' if fatal else '⚠️ '} {t}: {n}")
    for e in list(ex)[:5]: print(f"        {e}")
def ok(t,info=""): print(f"  ✅ {t}"+(f" — {info}" if info else ""))

files=[f for f in glob.glob(f"{ROOT}/content/ar/*/*.md") if "/drafts/" not in f and "/_merged/" not in f]
d=json.load(open(f"{ROOT}/data.json"))["nodes"]; slugs=set(d)
print(f"\n{'='*70}\nمراجعةٌ ختاميةٌ مستقلّة — {len(files)} ملفاً · {len(d)} عقدة\n{'='*70}")

# ═══ 1. سلامةُ الملفات نفسِها (هل أعطبت التعديلاتُ شيئاً؟)
print("\n[أ] سلامةُ الملفات على القرص")
nofm=[];badq=[];emptybody=[];badgap=[];dupkey=[]
for f in files:
    b=os.path.basename(f)[:-3]; t=open(f,encoding="utf-8").read()
    m=re.match(r'^---\n(.*?)\n---\n(.*)$',t,re.S)
    if not m: nofm.append(b); continue
    fm,body=m.group(1),m.group(2)
    if not body.strip() or not re.search(r'^#\s+\S',body,re.M): emptybody.append(b)
    keys=[l.split(":")[0] for l in fm.split("\n") if re.match(r'^[a-zA-Z0-9_-]+:',l)]
    dd=[k for k,v in collections.Counter(keys).items() if v>1]
    if dd: dupkey.append(f"{b}: {dd}")
    for l in fm.split("\n"):
        mm=re.match(r'^([a-zA-Z0-9_-]+):\s*"(.*)"\s*$',l)
        if mm and mm.group(2).count('"')%2: badq.append(f"{b}:{mm.group(1)}")
    g=re.search(r'^gaps:\n((?:\s+- .*\n)*)',fm+"\n",re.M)
    if g:
        for l in g.group(1).split("\n"):
            if l.strip() and not re.match(r'^\s+- ".*"\s*$',l): badgap.append(f"{b}: {l[:60]}")
bad("بلا frontmatter",len(nofm),nofm) if nofm else ok("كلُّ ملفٍّ له frontmatter سليم")
bad("متنٌ فارغٌ أو بلا عنوان H1",len(emptybody),emptybody) if emptybody else ok("كلُّ ملفٍّ له متنٌ وعنوانُ H1")
bad("مفتاحٌ مكرَّرٌ في frontmatter",len(dupkey),dupkey) if dupkey else ok("لا مفتاحَ مكرَّراً في أيِّ frontmatter")
bad("علاماتُ اقتباسٍ غيرُ متوازنةٍ في حقل",len(badq),badq) if badq else ok("علاماتُ الاقتباس متوازنةٌ في كلِّ حقل")
bad("بندُ gaps مكسورُ الصياغة (يُهمله البناءُ بصمت)",len(badgap),badgap) if badgap else ok("كلُّ بنود gaps سليمةُ الصياغة")
gc=sum(len(n.get("gaps",[])) for n in d.values())
ok("مجموعُ الفجوات المقروءة",info=str(gc))

# ═══ 2. ما يقرأه البناءُ = ما هو مكتوب
print("\n[ب] مطابقةُ الملفّ لما يقرأه البناء")
RE_R=re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')
RE_E=re.compile(r'-\s*rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"\s*,\s*target_type:\s*"([^"]*)"')
drop=[]; missing=[]
for f in files:
    b=os.path.basename(f)[:-3]; t=open(f,encoding="utf-8").read()
    if b not in d: missing.append(b); continue
    for key,rx,fld in (("related",RE_R,"related"),("edges",RE_E,"edges")):
        m=re.search(rf'^{key}:\s*\n((?:[ \t]*(?:-|\#).*\n)*)',t,re.M)
        if not m: continue
        w=len([l for l in m.group(1).split("\n") if l.strip().startswith("- ")]); p=len(rx.findall(m.group(1)))
        if w!=p: drop.append(f"{b}.{key}: كُتب {w} قُرئ {p}")
        if p!=len(d[b].get(fld,[])): drop.append(f"{b}.{key}: قُرئ {p} وفي data.json {len(d[b].get(fld,[]))}")
bad("ملفٌّ ليس في data.json",len(missing),missing) if missing else ok("كلُّ ملفٍّ في data.json")
extra=[s for s in d if s not in {os.path.basename(f)[:-3] for f in files}]
bad("عقدةٌ بلا ملفّ",len(extra),extra) if extra else ok("كلُّ عقدةٍ لها ملفّ")
bad("بنودٌ يُهملها البناءُ بصمت",len(drop),drop) if drop else ok("كلُّ بندٍ مكتوبٍ يقرأه البناء")
sl=[b for f in files if (b:=os.path.basename(f)[:-3]) and (m:=re.search(r'^slug:\s*"([^"]*)"',open(f,encoding='utf-8').read(),re.M)) and m.group(1)!=b]
bad("slug يخالف اسمَ الملفّ",len(sl),sl) if sl else ok("كلُّ slug يطابق اسمَ ملفّه")

# ═══ 3. الرسمُ البياني
print("\n[ج] سلامةُ الرسم البياني")
dr=[f"{s}→{r[0]}" for s,n in d.items() for r in n.get("related",[]) if r[0] not in slugs]
de=[f"{s}—{e[0]}→{e[1]}" for s,n in d.items() for e in n.get("edges",[]) if e[1] not in slugs]
bad("رابطُ related معلَّق",len(dr),dr) if dr else ok("كلُّ related يُحلّ")
bad("حرفُ edges معلَّق",len(de),de) if de else ok("كلُّ edges يُحلّ")
sf=[s for s,n in d.items() if any(r[0]==s for r in n.get("related",[])) or any(e[1]==s for e in n.get("edges",[]))]
bad("إشارةٌ ذاتية",len(sf),sf) if sf else ok("لا إشارةَ ذاتية")
du=[s for s,n in d.items() if len([r[0] for r in n.get("related",[])])!=len({r[0] for r in n.get("related",[])})]
bad("related مكرَّر",len(du),du) if du else ok("لا تكرارَ في related")
ids=collections.Counter(n.get("id") for n in d.values())
bad("id مكرَّر",len([1 for v in ids.values() if v>1]),[k for k,v in ids.items() if v>1]) if any(v>1 for v in ids.values()) else ok("كلُّ id فريد")
# حلقات
par={s:e[1] for s,n in d.items() for e in n.get("edges",[]) if e[0]=="belongs_to" and e[1] in slugs}
cyc=[]
for s in par:
    seen=set(); x=s
    while x in par:
        if x in seen: cyc.append(s); break
        seen.add(x); x=par[x]
bad("حلقةُ انتماء",len(cyc),cyc) if cyc else ok("شجرةُ الانتماء بلا حلقات")

# ═══ 4. المنطقُ التاريخي
print("\n[د] المنطقُ التاريخيُّ والنسب")
def yr(v):
    try: return int(v)
    except: return None
LIN={"evolved_into","evolved_from","superseded_by","split_into","absorbed_by"}
ana=[]
for s,n in d.items():
    for e in n.get("edges",[]):
        if e[0] not in LIN or e[1] not in slugs: continue
        a,p=yr(n.get("active_start")),yr(d[e[1]].get("active_start"))
        if a is None or p is None: continue
        if e[0]=="evolved_from" and p>a+30: ana.append(f"{s}[{a}]←{e[0]}—{e[1]}[{p}]")
        elif e[0]!="evolved_from" and p<a-30: ana.append(f"{s}[{a}]—{e[0]}→{e[1]}[{p}]")
bad("نسبٌ معكوسٌ زمنياً",len(ana),ana) if ana else ok("لا نسبَ معكوساً زمنياً")
tm=[f"{s}(ت{yr(d[s].get('active_end'))}) ⊂ {p}(بدأت {yr(d[p].get('active_start'))})" for s,p in par.items()
    if s.startswith("thk-") and yr(d[s].get("active_end")) is not None and yr(d[p].get("active_start")) is not None
    and yr(d[s]["active_end"])<yr(d[p]["active_start"])-30]
bad("مفكّرٌ انقضى نشاطُه قبل تأسيس مدرستِه",len(tm),tm) if tm else ok("لا مفكّرَ سابقاً لمدرستِه")
st=[s for s,n in d.items() if s.split("-")[0] in ("syn","dis") and any(e[0]=="belongs_to" and e[1]=="sch-cognitive-behavioral" for e in n.get("edges",[]))]
bad("متلازمةٌ منتميةٌ إلى CBT",len(st),st) if st else ok("لا نسبَ مختوماً قالبياً")

# ═══ 5. التكرار
print("\n[هـ] التكرار")
def na(t):
    t=re.sub(r'[ً-ْٰ]','',t or '')
    t=re.sub(r'[إأآٱ]','ا',t); t=re.sub(r'[ىي]','ي',t); t=t.replace('ة','ه').replace('ـ','')
    t=re.sub(r'\s*\(.*?\)','',t); t=re.sub(r'\s*—.*$','',t)
    return re.sub(r'[^\w\s]','',re.sub(r'\s+',' ',t)).strip()
def redirect(s):
    n=d[s]; return bool(n.get("redirect_to")) or n.get("status")=="quarantined" or "إحالة" in (n.get("title") or "") or "حجر" in (n.get("title") or "")
ALLOW={("con-li","con-li-principle-neoconfucian"),("con-jouissance","con-pleasure"),("con-anxiety","con-anxiety-existential"),
("con-alienation","con-alienation-marxist-vs-existentialist"),("thk-heidegger","thk-heidegger-technology"),
("br-existential-humanistic-american","br-humanistic"),("thk-cwhitaker-pt","thk-jjoyce"),("thk-cwhitaker-pt","thk-jroddy"),("thk-jjoyce","thk-jroddy"),
("tec-act-acc-radical-acceptance","tec-dbt-dt-radical-acceptance"),("tec-act-acc-self-compassion-exercises","tec-cbt-emo-self-compassion-exercises"),
("tec-act-acc-willingness-vs-willfulness","tec-dbt-dt-willingness-vs-willfulness"),("tec-act-pres-body-scan","tec-cbt-mind-body-scan"),
("tec-act-pres-mindful-eating","tec-dbt-er-mindful-eating"),("tec-act-pres-urge-surfing","tec-dbt-dt-urge-surfing"),
("tec-act-sac-perspective-taking","tec-cbt-int-perspective-taking"),("tec-cbt-int-self-validation","tec-dbt-er-self-validation")}
g=collections.defaultdict(set)
for s,n in d.items():
    if redirect(s): continue
    a=na(n.get("title"))
    if a: g[(s.split("-")[0],a)].add(s)
dups=set()
for v in g.values():
    v=sorted(v)
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            if (v[i],v[j]) not in ALLOW: dups.add((v[i],v[j]))
bad("تكرارٌ حيٌّ غيرُ مُعلَن",len(dups),[f"{a} = {b}" for a,b in sorted(dups)]) if dups else ok("لا تكرارَ حيٍّ غيرَ مُعلَن")

# ═══ 6. الإحالات
print("\n[و] الإحالاتُ والحجر")
nr=[s for s in d if redirect(s) and not d[s].get("redirect_to") and d[s].get("status")!="quarantined"]
bad("إحالةٌ بلا redirect_to ولا وسمِ حجر",len(nr),nr) if nr else ok("كلُّ إحالةٍ موسومةٌ ومحلولة")
br=[f"{s}→{d[s]['redirect_to']}" for s in d if d[s].get("redirect_to") and d[s]["redirect_to"] not in slugs]
bad("redirect_to معلَّق",len(br),br) if br else ok("كلُّ redirect_to يُحلّ")
ch=[f"{s}→{d[s]['redirect_to']}" for s in d if d[s].get("redirect_to") and d[s]["redirect_to"] in slugs and redirect(d[s]["redirect_to"])]
bad("إحالةٌ إلى إحالة (سلسلة)",len(ch),ch,fatal=False) if ch else ok("لا إحالةَ إلى إحالة")

# ═══ 7. الحقول
print("\n[ز] الحقولُ المُعجمية")
for fld,vals in (("level",("مبتدئ","متوسط","متقدم")),("part",("philosophy","psychology","bridge"))):
    b=[f"{s}:«{d[s].get(fld)}»" for s in d if d[s].get(fld) not in vals]
    bad(f"`{fld}` خارجَ المعجم",len(b),b,fatal=(fld=="level")) if b else ok(f"`{fld}` من المعجم")
ena=[s for s in d if re.search(r'[؀-ۿ]',d[s].get("en") or "")]
bad("`en` فيه عربية",len(ena),ena) if ena else ok("لا عربيةَ في `en`")
noc=[s for s in d if not (d[s].get("crumb") or "").strip() or len((d[s].get("crumb") or "").split("←"))<2]
bad("مسارُ تنقّلٍ ناقص",len(noc),noc) if noc else ok("كلُّ مسارٍ جزآن على الأقلّ")
mt=[f"{s}→{r[0]}" for s,n in d.items() for r in n.get("related",[]) if r[0] in slugs and (r[1].strip()!=(d[r[0]].get("title") or "").strip() or r[2]!=d[r[0]].get("type"))]
bad("عنوان/نوعٌ في related يخالف الهدف",len(mt),mt) if mt else ok("كلُّ عناوين وأنواع related مطابقة")
te=[f"{s}→{e[1]}" for s,n in d.items() for e in n.get("edges",[]) if e[1] in slugs and e[2] and e[2]!=d[e[1]].get("type")]
bad("target_type يخالف الهدف",len(te),te) if te else ok("كلُّ target_type مطابق")

# ═══ 8. المتن
print("\n[ح] سلامةُ المتن")
pats={"ماركداون مكسور ****":r'\*\*\*\*',"وصلات ويكي [[":r'\[\[',"DRAFT-UNKNOWN":r'DRAFT-UNKNOWN',
      "رابط ماركداون إلى .md":r'\]\([a-zA-Z0-9\-_]+\.md\)',"مسار نائب إنجليزي":r'^crumb: "الأطلس ← (thinkers|concepts|schools|works)',
      "TODO/FIXME":r'\b(TODO|FIXME|XXX|TBD)\b',"نائب [لم يُراجع]":r'\[لم يُراجع\]|\[بيانات غير متاحة\]'}
hits={k:[] for k in pats}; unbal=[]
for f in files:
    t=open(f,encoding="utf-8").read(); b=os.path.basename(f)[:-3]
    body=t.split("\n---\n",1)[1] if "\n---\n" in t else t
    for k,p in pats.items():
        tgt = body if k in ("نائب [لم يُراجع]","TODO/FIXME") else t
        if re.search(p,tgt,re.M): hits[k].append(b)
    if t.count("**")%2: unbal.append(b)
for k,v in hits.items():
    bad(k,len(v),v) if v else ok(f"لا {k}")
bad("`**` غيرُ متوازن",len(unbal),unbal) if unbal else ok("`**` متوازن")
url=[]
for f in files:
    t=open(f,encoding="utf-8").read(); b=os.path.basename(f)[:-3]
    for m in re.findall(r'https?://[^\s)\]<>"]+',t):
        if " " in m or m.endswith(("(",",")): url.append(f"{b}: {m[:50]}")
bad("رابطٌ خارجيٌّ مشوَّه",len(url),url,fatal=False) if url else ok("كلُّ الروابط الخارجية سليمةُ الصياغة")

# ═══ 9. القالب
print("\n[ط] القالبُ الثابت")
ex=f"{ROOT}/scripts/template/data_extras.json"
raw=open(ex,encoding="utf-8").read()
PRE="thk|con|sch|br|tec|wrk|rel|dbt|que|met|trm|ins|stu|evt|exp|crt|dia|syn|dis|ctx|axm|axi"
ref=set(re.findall(rf'"(({PRE})-[a-z0-9\-]+)"',raw))
ref={r[0] for r in ref}
ms=sorted(x for x in ref if x not in slugs)
bad("القالبُ يشير إلى ملفٍّ غيرِ موجود",len(ms),ms) if ms else ok("كلُّ slug في القالب يُحلّ")
rd=sorted(x for x in ref if x in slugs and redirect(x))
bad("القالبُ يشير إلى إحالة",len(rd),rd,fatal=False) if rd else ok("لا إشارةَ من القالب إلى إحالة")
html=open(f"{ROOT}/index.html",encoding="utf-8").read(300000)
ok("عنوانُ الصفحة",info=re.search(r'<title>(.*?)</title>',html).group(1))
if "يضم حالياً" in html: bad("عنوانُ الصفحةِ ما زال قديماً",1)

# ═══ 10. الوصول
print("\n[ي] الوصولُ بالتنقّل")
inb=collections.defaultdict(set)
for s,n in d.items():
    for r in n.get("related",[]):
        if r[0] in slugs: inb[r[0]].add(s)
    for e in n.get("edges",[]):
        if e[1] in slugs: inb[e[1]].add(s)
iso=[s for s in d if not inb[s]]
live=[s for s in iso if not redirect(s)]
withdata=[s for s in live if d[s].get("related") or d[s].get("edges")]
pct=100*(len(d)-len(iso))/len(d)
ok("نسبةُ العقد المُشار إليها",info=f"{pct:.2f}% (معزولة {len(iso)}، منها {len(iso)-len(live)} إحالةٌ/محجور)")
bad("معزولةٌ حيّةٌ تحمل بياناتٍ علائقية",len(withdata),withdata) if withdata else ok("المعزولاتُ الحيّةُ كلُّها بلا بياناتٍ علائقية")
kids=collections.defaultdict(list)
for s,p in par.items(): kids[p].append(s)
dead=[s for s in d if s.startswith(("sch-","br-")) and len(d[s]["related"])<3 and not kids[s] and not redirect(s)]
bad("مدرسة/تيّارٌ طريقٌ مسدود",len(dead),dead,fatal=False) if dead else ok("لا مدرسةَ طريقاً مسدوداً")

# ═══ الخلاصة
print(f"\n{'='*70}")
print(f"فحوصٌ قاطعةٌ فاشلة: {len(FAIL)}")
for x in FAIL: print(f"   ❌ {x}")
print(f"تسجيلاتٌ (لا تُفشِل): {len(WARN)}")
for x in WARN: print(f"   ⚠️  {x}")
print("="*70)
