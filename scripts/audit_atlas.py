"""
مراجعةٌ شاملةٌ للأطلس — تُعيد فحصَ كلِّ ما عُولج في جلسة 2026-09-07/08.

الغرض: التأكّدُ أنّ ما أُصلح **بقي مُصلَحاً**، وأنّ الإصلاحَ لم يُولّد خللاً
جديداً. تُشغَّل بعد أيِّ دفعة تعديل:

    python3 scripts/audit_atlas.py            # كامل
    python3 scripts/audit_atlas.py --brief    # الملخّص فقط

كلُّ فحصٍ يطبع سطراً واحداً: ✅ سليم أو ❌ مع العدد وأمثلة. والخروجُ بقيمةٍ غير
صفريةٍ إن وُجد خللٌ في فحصٍ **قاطع** (تُترك المعلوماتيةُ للقراءة لا للإفشال).
"""
import json, os, re, sys, glob, collections, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BRIEF = "--brief" in sys.argv
FAILURES = []

def load():
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        return json.load(f)["nodes"]

def ok(name, n=0, info=""):
    print(f"  ✅ {name}" + (f" — {info}" if info else ""))

def bad(name, n, examples=(), fatal=True, info=""):
    print(f"  {'❌' if fatal else '⚠️ '} {name}: {n}" + (f" — {info}" if info else ""))
    if not BRIEF:
        for e in list(examples)[:6]: print(f"        {e}")
    if fatal: FAILURES.append(name)

def deprecated(n):
    t = n.get("title") or ""
    return ("حجر" in t and "انظر" in t) or ("إحالة" in t)

def main():
    d = load()
    slugs = set(d)
    print(f"\n{'='*66}\nمراجعةُ الأطلس — {len(d)} عقدة\n{'='*66}")

    # ── 1. البنية الأساسية
    print("\n[1] البنية الأساسية")
    dang = [(s, r[0]) for s, n in d.items() for r in n.get("related", []) if r[0] not in slugs]
    bad("إحالاتُ related معلَّقة", len(dang), [f"{a} -> {b}" for a, b in dang]) if dang else ok("لا إحالاتِ related معلَّقة")
    selfr = [s for s, n in d.items() for r in n.get("related", []) if r[0] == s]
    bad("related يشير إلى الملفّ نفسِه", len(selfr), selfr) if selfr else ok("لا إشارةَ ذاتيةً في related")
    dup = [s for s, n in d.items()
           if len([r[0] for r in n.get("related", [])]) != len({r[0] for r in n.get("related", [])})]
    bad("بنودُ related مكرَّرة", len(dup), dup) if dup else ok("لا تكرارَ في related")
    nofile = [s for s, n in d.items() if not (n.get("title") or "").strip()]
    bad("بلا عنوان", len(nofile), nofile) if nofile else ok("كلُّ عقدةٍ لها عنوان")

    # ── 2. الوصول (العزلة)
    print("\n[2] الوصولُ بالتنقّل")
    inb = collections.defaultdict(set)
    for s, n in d.items():
        for r in n.get("related", []):
            if r[0] in slugs: inb[r[0]].add(s)
        for e in n.get("edges", []):
            if e[1] in slugs: inb[e[1]].add(s)
    orph = [s for s in d if not inb[s]]
    live = [s for s in orph if not deprecated(d[s])]
    pct = 100 * (len(d) - len(orph)) / len(d)
    ok("نسبةُ العقد التي يُشار إليها", info=f"{pct:.2f}%  (معزولة {len(orph)}، منها {len(orph)-len(live)} مهجورةٌ بقصد)")
    if pct < 97: bad("نسبةُ الوصول تراجعت", len(live), live)
    withnothing = [s for s in live if not d[s].get("related") and not d[s].get("edges")]
    ok("المعزولاتُ الحيّة كلُّها بلا بياناتٍ علائقية", info=f"{len(withnothing)}/{len(live)}") \
        if len(withnothing) == len(live) else bad("معزولةٌ تحمل بياناتٍ علائقيةً (كان يجب ربطُها)",
            len(live)-len(withnothing), [s for s in live if s not in withnothing])

    # ── 3. صحّةُ الانتماء
    print("\n[3] حقلُ belongs_to")
    par = {}
    for s, n in d.items():
        for e in n.get("edges", []):
            if e[0] == "belongs_to" and e[1] in slugs: par[s] = e[1]; break
    sr = [s for s, n in d.items() for e in n.get("edges", []) if e[0] == "belongs_to" and e[1] == s]
    bad("ينتمي إلى نفسِه", len(sr), sr) if sr else ok("لا انتماءَ ذاتيّ")
    def root(x):
        seen = set()
        while x in par:
            if x in seen: return None
            seen.add(x); x = par[x]
        return x
    cyc = [s for s in par if root(s) is None]
    bad("في حلقةِ انتماءٍ مغلقة", len(cyc), cyc) if cyc else ok("شجرةُ الانتماء لا حلقاتَ فيها",
        info=f"أقصى عمق {max((lambda f: [f(s) for s in par])(lambda s: (lambda c: c)(len([0 for _ in iter(int,1)])) if False else 0) or [0]) if False else max(sum(1 for _ in iter(lambda: None, 1)) if False else 0 for _ in [0])}")
    depth = 0
    for s in par:
        x, n2 = s, 0
        while x in par and n2 < 60: x = par[x]; n2 += 1
        depth = max(depth, n2)
    ok("أقصى عمقٍ لشجرة الانتماء", info=str(depth))
    dupedge = [s for s, n in d.items()
               if (lambda b: len(b) != len(set(b)))([e[1] for e in n.get("edges", []) if e[0] == "belongs_to"])]
    bad("حرفُ انتماءٍ مكرَّر", len(dupedge), dupedge) if dupedge else ok("لا تكرارَ في حرف الانتماء")
    depp = [(s, e[1]) for s, n in d.items() for e in n.get("edges", [])
            if e[0] == "belongs_to" and e[1] in slugs and deprecated(d[e[1]])]
    bad("أبٌ مهجور (إحالة/حجر)", len(depp), [f"{a} -> {b}" for a, b in depp]) if depp \
        else ok("لا أبَ مهجوراً")
    unres = collections.Counter(e[1] for n in d.values() for e in n.get("edges", [])
                               if e[0] == "belongs_to" and e[1] not in slugs
                               and e[1] not in {(v.get("title") or "").strip() for v in d.values()})
    if unres:
        bad("أبٌ نصّيٌّ لا يُحلّ إلى ملفّ", len(unres),
            [f"{k} ×{v}" for k, v in unres.most_common()],
            fatal=False, info="مدارسُ غائبةٌ عن الأطلس — تسجيلٌ لا خطأ")
    else:
        ok("كلُّ أبٍ يُحلّ إلى ملفٍّ قائم")
    phil = [s for s, p in par.items() if p == "sch-existential-therapy" and d[s].get("part") == "philosophy"]
    bad("مدخلٌ فلسفيٌّ داخل مدرسةِ العلاج الوجودي", len(phil), phil, fatal=False) if phil \
        else ok("لا مدخلَ فلسفيٍّ في مدرسة العلاج الوجودي")

    # ── 4. مسارُ التنقّل
    print("\n[4] مسارُ التنقّل (crumb)")
    ph = [s for s, n in d.items() if (n.get("crumb") or "").startswith("المدرسة الوجودية")]
    bad("وسمٌ قالبيٌّ «المدرسة الوجودية»", len(ph), ph) if ph else ok("لا وسمَ «المدرسة الوجودية» قالبياً")
    noc = [s for s, n in d.items() if not (n.get("crumb") or "").strip()]
    bad("بلا مسار تنقّل", len(noc), noc) if noc else ok("كلُّ عقدةٍ لها مسارُ تنقّل")
    empty1 = [s for s, n in d.items() if not (n.get("crumb") or "").split("←")[0].strip()]
    bad("جزءٌ أوّلُ فارغ", len(empty1), empty1) if empty1 else ok("لا جزءَ أوّلَ فارغاً")
    short = [s for s, n in d.items() if len((n.get("crumb") or "").split("←")) < 2]
    bad("مسارٌ بأقلَّ من جزأين", len(short), short) if short else ok("كلُّ مسارٍ جزآن على الأقلّ")
    gen = [s for s, n in d.items() if s.startswith("stu-") and (n.get("crumb") or "").startswith("علم النفس ←")]
    bad("دراسةٌ بوسمٍ عامّ «علم النفس»", len(gen), gen, fatal=False) if gen else ok("لا دراسةَ بوسمٍ عامّ")

    # ── 5. الروابطُ المُقحَمة
    print("\n[5] الروابطُ المُقحَمة حشواً")
    # أهدافٌ ثبت إقحامُها في دفعاتٍ قالبية. و`ALLOW` حكمٌ تحريريٌّ مُعلَن: صلةٌ
    # موضوعيةٌ قائمةٌ وإن لم يذكر المتنُ الكلمةَ الدالّة — تيّاراتٌ تقنيةٌ شقيقة.
    INJECTED = {
        "con-authenticity": (("أصالة", "أصيل", "authentic"), set()),
        "br-ml-personalized-therapy": (("تعلّم الآلة", "machine learning", "خوارزم",
                                        "الذكاء الاصطناعي", "تعلم الآلة"),
            {"br-digital-therapeutics", "br-teletherapy",
             "br-serious-games-therapy", "br-predictive-processing-informed"}),
        "br-sikolohiyang-pilipino": (("فلبين", "Sikolohiyang", "Filipino", "إنريكيز", "kapwa"), set()),
    }
    for target, (words, allow) in INJECTED.items():
        susp = []
        for s, n in d.items():
            if s == target or s in allow: continue
            if not any(r[0] == target for r in n.get("related", [])): continue
            body = (n.get("lede") or "") + " ".join(x[1] for x in n.get("sections", []))
            if not any(w in body for w in words): susp.append(s)
        bad(f"`{target}` بلا سندٍ في المتن", len(susp), susp) if susp \
            else ok(f"`{target}` كلُّ إشاراته مسوَّغة",
                    info=(f"{len(allow)} مُبقاةٌ بحكمٍ تحريريٍّ مُعلَن" if allow else ""))

    # ── 6. سلامةُ المتن
    print("\n[6] سلامةُ المتن")
    files = glob.glob(os.path.join(ROOT, "content", "ar", "*", "*.md"))
    pats = {"ماركداون مكسور `****`": r'\*\*\*\*',
            "وصلاتُ ويكي `[[`": r'\[\[',
            "علامةُ `DRAFT-UNKNOWN`": r'DRAFT-UNKNOWN',
            "مسارٌ نائبٌ بالمجلّد الإنجليزي": r'^crumb: "الأطلس ← (thinkers|concepts|schools|works)'}
    hits = {k: [] for k in pats}
    unbal = []; nosrc = []
    for f in files:
        if "/drafts/" in f or "/_merged/" in f: continue
        t = open(f, encoding="utf-8").read()
        b = os.path.basename(f)[:-3]
        for k, p in pats.items():
            if re.search(p, t, re.M): hits[k].append(b)
        if t.count("**") % 2: unbal.append(b)
        if "## المصادر" not in t: nosrc.append(b)
    for k, v in hits.items():
        bad(k, len(v), v) if v else ok(f"لا {k}")
    bad("`**` غيرُ متوازن", len(unbal), unbal) if unbal else ok("`**` متوازنٌ في كلِّ ملفّ")
    bad("بلا قسم «المصادر»", len(nosrc), nosrc, fatal=False) if nosrc else ok("كلُّ ملفٍّ فيه قسمُ المصادر")

    # ── 7. ما يقرأه البناءُ فعلاً
    print("\n[7] مطابقةُ الملفّ لما يقرأه البناء")
    RE_R = re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')
    drop = []
    for f in files:
        if "/drafts/" in f or "/_merged/" in f: continue
        t = open(f, encoding="utf-8").read()
        b = os.path.basename(f)[:-3]
        m = re.search(r'^related:\n((?:- .*\n)*)', t, re.M)
        if not m: continue
        written = len([l for l in m.group(1).split("\n") if l.startswith("- ")])
        parsed = len(RE_R.findall(m.group(1)))
        if written != parsed: drop.append(f"{b}: كُتب {written} قُرئ {parsed}")
    bad("بنودٌ يُهملها البناءُ بصمت", len(drop), drop) if drop else ok("كلُّ بندٍ مكتوبٍ يقرأه البناء")

    # ── 8. اتّساقُ part بين الأشقّاء
    print("\n[8] اتّساقُ `part` بين الأشقّاء")
    kids = collections.defaultdict(list)
    for s, p in par.items(): kids[p].append(s)
    odd = []
    for p, xs in kids.items():
        xs = [s for s in xs if d[s].get("part") != "bridge"]
        if len(xs) < 8: continue
        c = collections.Counter(d[s].get("part") for s in xs)
        if len(c) < 2: continue
        maj = c.most_common()[0]
        if maj[0] != d[p].get("part"): continue
        for part, cnt in c.most_common()[1:]:
            if cnt / len(xs) <= 0.20:
                odd += [f"{s} ({part} بين أشقّاء {maj[0]})" for s in xs if d[s].get("part") == part]
    bad("يخالف أشقّاءه في `part`", len(odd), odd, fatal=False) if odd \
        else ok("لا عنصرَ يخالف أشقّاءه شذوذاً في `part`")

    # ── 9. فجواتٌ متقادمة
    print("\n[9] فجواتٌ صارت كاذبة")
    # الكشفُ يشترط **التجاور**: عبارةُ الغياب ثم الـslug بعدها مباشرةً.
    # فالصياغةُ الأولى كانت ترصد أيَّ gap فيه عبارةُ غيابٍ و slug موجودٌ في أيِّ
    # موضع، فأعطت 24 نتيجةً أكثرُها كاذب: فجوةُ `wrk-measurement-intelligence`
    # تقول «تحقّقتُ من `thk-ssterman` وهو لشخص آخر تماماً» — تذكر الـslug **لتنفي**
    # المطابقة لا لتدّعي غيابَه. وكذلك تُستثنى الفجواتُ التي تحمل علامةَ إنجاز.
    NEAR = re.compile(r'(?:لا ملفَّ|لا ملف |بلا ملف|بلا ملفّ|بلا ملفٍّ|لا يوجد ملف)'
                      r'[^`]{0,40}`((?:thk|con|sch|br|tec|wrk|rel|dbt|que|met|trm|ins|stu'
                      r'|evt|exp|crt|dia|syn|dis|ctx|axm|axi)-[a-z0-9\-]+)`')
    # ملاحظة: «الموجودُ …» و«ليس أحدُهما موضعَه» صيغتا **نفيٍ** للمطابقة، لا ادّعاءَ
    # غياب: فجوةُ `con-epistemic-injustice-fricker-concept` تقول «الموجودُ
    # `sch-virtue-ethics` و`sch-care-ethics` وليس أحدُهما موضعَه» — أي أنها تعرف
    # أنهما موجودان وتنفي صلاحيتهما. فأُضيفتا إلى المستثنيات.
    DONE = ("سُدّت", "صُحِّح", "كُتب", "أُضيف", "نُقل", "فُرِّغ", "حُذف", "رُبطت",
            "تحقّقت", "لشخص آخر", "موجودٌ فعلاً", "دُمج", "الموجودُ", "موضعَه")
    stale = []
    for s, n in d.items():
        for g in n.get("gaps", []):
            if any(w in g for w in DONE): continue
            for mm in NEAR.findall(g):
                if mm in slugs:
                    stale.append(f"{s}: يدّعي غيابَ `{mm}` وهو موجود"); break
    bad("فجوةٌ تدّعي غيابَ ملفٍّ موجود", len(stale), stale, fatal=False) if stale \
        else ok("لا فجوةَ تدّعي غيابَ موجود")

    # ══════════════════════════════════════════════════════════════════
    # فحوصٌ أُضيفت 2026-09-10 بعد مراجعةٍ ختاميةٍ كشفت أخطاءً لم يكن أيٌّ
    # من الفحوص السابقة يراها: أنسابٌ مختومةٌ قالبياً، وحروفُ نسبٍ معكوسةٌ
    # زمنياً، و51 مجموعةً مكرَّرة، وslugs تحمل اسمَ شخصٍ آخر. وكلُّ فحصٍ
    # هنا يمنع رجوعَ خللٍ **وقع فعلاً** لا خللاً متوهَّماً.
    # ══════════════════════════════════════════════════════════════════
    import unicodedata as _ud

    def _redirect(s):
        n = d[s]
        return bool(n.get("redirect_to")) or n.get("status") == "quarantined" \
            or "إحالة" in (n.get("title") or "") or "حجر" in (n.get("title") or "")

    def _yr(v):
        try: return int(v)
        except (TypeError, ValueError): return None

    print("\n[10] سلامةُ الأضلاع كلِّها (لا `belongs_to` وحده)")
    alld = [(s, e[0], e[1]) for s, n in d.items() for e in n.get("edges", []) if e[1] not in slugs]
    bad("حرفٌ هدفُه ليس ملفاً قائماً", len(alld), [f"{a} —{b}→ {c}" for a, b, c in alld]) if alld \
        else ok("كلُّ حرفٍ في `edges` هدفُه ملفٌّ قائم")
    mm = [(s, e[1], e[2], d[e[1]]["type"]) for s, n in d.items() for e in n.get("edges", [])
          if e[1] in slugs and e[2] and e[2] != d[e[1]].get("type")]
    bad("`target_type` يخالف نوعَ الهدف", len(mm), [f"{a}→{b}: «{c}» ≠ «{e}»" for a, b, c, e in mm]) \
        if mm else ok("`target_type` مطابقٌ لنوع الهدف في كلِّ حرف")

    print("\n[11] حروفُ النسب التاريخي")
    LIN = {"evolved_into", "evolved_from", "superseded_by", "split_into", "absorbed_by"}
    nonsch = [(s, e[0], e[1]) for s, n in d.items() for e in n.get("edges", [])
              if e[0] in LIN and e[1] in slugs and not e[1].startswith(("sch-", "br-"))]
    ALLOW_NONSCH = {("sch-systemic-family", "split_into", "tec-structural-family-therapy"),
                    ("sch-systemic-family", "split_into", "tec-strategic-family-therapy"),
                    ("sch-behaviorism", "evolved_into", "con-applied-behavior-analysis")}
    nonsch = [x for x in nonsch if tuple(x) not in ALLOW_NONSCH]
    bad("حرفُ نسبٍ هدفُه ليس مدرسةً/تيّاراً", len(nonsch),
        [f"{a} —{b}→ {c}" for a, b, c in nonsch]) if nonsch \
        else ok("كلُّ حرفِ نسبٍ هدفُه مدرسةٌ أو تيّار", info=f"{len(ALLOW_NONSCH)} مُستثنىً بحكمٍ مُعلَن")
    ana = []
    for s, n in d.items():
        for e in n.get("edges", []):
            if e[0] not in LIN or e[1] not in slugs: continue
            a, p2 = _yr(n.get("active_start")), _yr(d[e[1]].get("active_start"))
            if a is None or p2 is None: continue
            if e[0] == "evolved_from" and p2 > a + 30: ana.append(f"{s}[{a}] ←{e[0]}— {e[1]}[{p2}]")
            elif e[0] != "evolved_from" and p2 < a - 30: ana.append(f"{s}[{a}] —{e[0]}→ {e[1]}[{p2}]")
    bad("حرفُ نسبٍ معكوسٌ زمنياً", len(ana), ana) if ana \
        else ok("لا حرفَ نسبٍ يجعل المتقدِّمَ ثمرةً للمتأخّر")

    print("\n[12] الأنسابُ المختومةُ قالبياً")
    CBTW = ("المعرفي السلوكي", "المعرفية السلوكية", "المعرفي-السلوكي", "CBT", "العلاج المعرفي")
    st = []
    for s, n in d.items():
        if s.split("-")[0] not in ("syn", "dis") : continue
        if not any(e[0] == "belongs_to" and e[1] == "sch-cognitive-behavioral" for e in n.get("edges", [])):
            continue
        st.append(s)
    bad("متلازمةٌ/اضطرابٌ ينتمي إلى CBT (ختمٌ قالبيّ)", len(st), st) if st \
        else ok("لا متلازمةَ مختومةً بالانتماء إلى CBT")
    # يكفي أن يطابق `part` **أحدَ** آبائه: عقدةٌ لها أبوان في قسمين مختلفين
    # (كأكابتشوك تحت الكونفوشية النفسية والكونفوشية الحديثة) تجمع القسمين
    # بطبعها، فلا يصحُّ إفشالُها على مخالفةِ أحدِهما.
    par2 = collections.defaultdict(list)
    for s, n in d.items():
        for e in n.get("edges", []):
            if e[0] == "belongs_to" and e[1] in slugs:
                par2[s].append(e[1])
    ppm = []
    for s, ps in par2.items():
        if d[s].get("part") in ("bridge", None):
            continue
        cand = [p for p in ps if d[p].get("part") not in ("bridge", None)]
        if cand and d[s]["part"] not in {d[p]["part"] for p in cand}:
            ppm.append(f"{s} ({d[s]['part']}) ⊂ " + " / ".join(f"{p} ({d[p].get('part')})" for p in cand))
    bad("`part` يخالف وسمَ الأب", len(ppm), ppm) if ppm \
        else ok("`part` مطابقٌ لوسم الأب في كلِّ العقد")

    print("\n[13] التكرار")
    def _na(t):
        t = re.sub(r'[ً-ْٰٖ-ٟ]', '', t or '')
        t = re.sub(r'[إأآٱ]', 'ا', t); t = re.sub(r'[ىي]', 'ي', t)
        t = t.replace('ة', 'ه').replace('ـ', '')
        t = re.sub(r'\s*\(.*?\)', '', t); t = re.sub(r'\s*—.*$', '', t)
        return re.sub(r'[^\w\s]', '', re.sub(r'\s+', ' ', t)).strip()
    def _ne(t):
        t = _ud.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
        return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', t)).strip()
    # أزواجٌ رُوجعت وتقرّر **عدمُ** دمجها بحكمٍ تحريريٍّ مُعلَن (المرحلة 3)
    ALLOW_DUP = {
        ("con-li", "con-li-principle-neoconfucian"), ("con-jouissance", "con-pleasure"),
        ("con-anxiety", "con-anxiety-existential"),
        ("con-alienation", "con-alienation-marxist-vs-existentialist"),
        ("thk-heidegger", "thk-heidegger-technology"),
        ("br-existential-humanistic-american", "br-humanistic"),
        ("thk-cwhitaker-pt", "thk-jjoyce"), ("thk-cwhitaker-pt", "thk-jroddy"),
        ("thk-jjoyce", "thk-jroddy"),
        # تقنياتٌ بعينها تُدرَّس في مدرستين بصياغتين وإسنادين مختلفين، ومُيِّزت
        # عناوينُها بلاحقة المدرسة — والمُطبِّعُ هنا يُسقط ما بين القوسين فتبدو
        # متطابقة. أُبقيت بقرارٍ مكتوبٍ في `p3_merge_duplicates.py`.
        ("tec-act-acc-radical-acceptance", "tec-dbt-dt-radical-acceptance"),
        ("tec-act-acc-self-compassion-exercises", "tec-cbt-emo-self-compassion-exercises"),
        ("tec-act-acc-willingness-vs-willfulness", "tec-dbt-dt-willingness-vs-willfulness"),
        ("tec-act-pres-body-scan", "tec-cbt-mind-body-scan"),
        ("tec-act-pres-mindful-eating", "tec-dbt-er-mindful-eating"),
        ("tec-act-pres-urge-surfing", "tec-dbt-dt-urge-surfing"),
        ("tec-act-sac-perspective-taking", "tec-cbt-int-perspective-taking"),
        ("tec-cbt-int-self-validation", "tec-dbt-er-self-validation"),
    }
    grp = collections.defaultdict(set)
    for s, n in d.items():
        if _redirect(s): continue
        pre = s.split("-")[0]
        a, e2 = _na(n.get("title")), _ne(n.get("en"))
        if a: grp[(pre, "ar", a)].add(s)
        if e2 and len(e2) > 3 and "unverified" not in e2 and "merged" not in e2:
            grp[(pre, "en", e2)].add(s)
    dups = set()
    for v in grp.values():
        v = sorted(v)
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if (v[i], v[j]) not in ALLOW_DUP: dups.add((v[i], v[j]))
    bad("عقدتان حيّتان بالعنوان/الاسم نفسِه", len(dups), [f"{a} = {b}" for a, b in sorted(dups)]) \
        if dups else ok("لا تكرارَ حيّاً غيرَ مُعلَن", info=f"{len(ALLOW_DUP)} زوجاً مُستثنىً بقرارٍ مكتوب")

    print("\n[14] الإحالاتُ والحجر")
    nort = [s for s in d if _redirect(s) and not d[s].get("redirect_to")
            and d[s].get("status") != "quarantined"]
    bad("إحالةٌ بلا `redirect_to` ولا وسمِ حجر", len(nort), nort) if nort \
        else ok("كلُّ إحالةٍ تحمل `redirect_to`، وكلُّ محجورٍ يحمل وسمَه")
    badt = [f"{s} → {d[s]['redirect_to']}" for s in d
            if d[s].get("redirect_to") and d[s]["redirect_to"] not in slugs]
    bad("`redirect_to` يشير إلى ملفٍّ غيرِ موجود", len(badt), badt) if badt \
        else ok("كلُّ `redirect_to` يُحلّ إلى ملفٍّ قائم")
    tord = [f"{s} → {r[0]}" for s, n in d.items() if not _redirect(s)
            for r in n.get("related", []) if r[0] in slugs and _redirect(r[0])]
    bad("رابطٌ حيٌّ ينتهي إلى إحالة/محجور", len(tord), tord, fatal=False) if tord \
        else ok("لا رابطَ حيٍّ ينتهي إلى إحالة")

    print("\n[15] البادئاتُ والحقولُ المُعجمية")
    PRE = ("thk", "con", "sch", "br", "tec", "wrk", "rel", "dbt", "que", "met", "trm",
           "ins", "stu", "evt", "exp", "crt", "dia", "syn", "dis", "ctx", "axm", "axi")
    op = [s for s in d if s.split("-")[0] not in PRE]
    bad("بادئةٌ خارجَ المعجم", len(op), op, fatal=False) if op else ok("كلُّ بادئةٍ من المعجم")
    lv = [f"{s}: «{d[s].get('level')}»" for s in d if d[s].get("level") not in ("مبتدئ", "متوسط", "متقدم")]
    bad("`level` خارجَ المعجم", len(lv), lv) if lv else ok("`level` من المعجم في كلِّ عقدة")
    pt = [f"{s}: «{d[s].get('part')}»" for s in d if d[s].get("part") not in ("philosophy", "psychology", "bridge")]
    bad("`part` خارجَ المعجم", len(pt), pt, fatal=False) if pt else ok("`part` من المعجم في كلِّ عقدة")
    ena = [s for s in d if re.search(r'[؀-ۿ]', d[s].get("en") or "")]
    bad("حقلُ `en` فيه عربية", len(ena), ena) if ena else ok("لا عربيةَ في حقل `en`")

    print("\n[16] مطابقةُ العنوان لِما تشير إليه الروابط")
    stale_t = [f"{s}→{r[0]}: «{r[1][:26]}» ≠ «{(d[r[0]].get('title') or '')[:26]}»"
               for s, n in d.items() for r in n.get("related", [])
               if r[0] in slugs and r[1].strip() != (d[r[0]].get("title") or "").strip()]
    bad("عنوانٌ في `related` يخالف عنوانَ الهدف", len(stale_t), stale_t) if stale_t \
        else ok("كلُّ عنوانٍ في `related` مطابقٌ لهدفه")
    stale_y = [f"{s}→{r[0]}" for s, n in d.items() for r in n.get("related", [])
               if r[0] in slugs and r[2] != d[r[0]].get("type")]
    bad("نوعٌ في `related` يخالف نوعَ الهدف", len(stale_y), stale_y) if stale_y \
        else ok("كلُّ نوعٍ في `related` مطابقٌ لهدفه")

    print("\n[17] قسمُ المصادر — المضمونُ لا العنوان")
    PH = ("يفتقر هذا الملف", "لا تتوفر مصادر", "لم تُتَح", "بلا مصادر",
          "لم تُستكمل بعد مراجعة المصادر")
    hollow = []
    for s, n in d.items():
        if _redirect(s): continue
        sec = [x[1] for x in n.get("sections", []) if x[0] == "المصادر"]
        txt = sec[0].strip() if sec else ""
        if not sec or len(txt) < 40 or any(p in txt for p in PH): hollow.append(s)
    bad("قسمُ مصادرٍ قالبيٌّ أو أقصرُ من 40 حرفاً", len(hollow), hollow, fatal=False,
        info="عملٌ تحريريٌّ مستمرّ — يُقاس ولا يُفشِل البناء") if hollow \
        else ok("كلُّ ملفٍّ حيٍّ فيه مصادرُ فعلية")

    print("\n[18] ما يقرأه القالبُ الثابت")
    exp = os.path.join(ROOT, "scripts", "template", "data_extras.json")
    if os.path.exists(exp):
        raw = open(exp, encoding="utf-8").read()
        ref = set(re.findall(r'"((?:' + "|".join(PRE) + r')-[a-z0-9\-]+)"', raw))
        miss = sorted(x for x in ref if x not in slugs)
        bad("`data_extras.json` يشير إلى ملفٍّ غيرِ موجود", len(miss), miss) if miss \
            else ok("كلُّ slug في `data_extras.json` يُحلّ إلى ملفٍّ قائم")
        rd = sorted(x for x in ref if x in slugs and _redirect(x))
        bad("`data_extras.json` يشير إلى إحالة/محجور", len(rd), rd, fatal=False) if rd \
            else ok("لا إشارةَ من القالب إلى إحالة")
    mdl = []
    for f in files:
        t = open(f, encoding="utf-8").read()
        if re.search(r'\]\([a-zA-Z0-9\-_]+\.md\)', t): mdl.append(os.path.basename(f)[:-3])
    bad("رابطُ ماركداون إلى ملفّ `.md` (لا يفسّره الأطلس)", len(mdl), mdl) if mdl \
        else ok("لا روابطَ ماركداون إلى ملفات")

    print("\n[19] سلامةُ الملفّ على القرص (خللٌ يُهمله البناءُ بصمت)")
    # أُضيف 2026-09-10 بعد أن كشفت المراجعةُ المستقلّةُ ثلاثةَ أصنافٍ من الخلل
    # **لا يشكو منها البناءُ ولا تظهر في data.json**: فجواتٌ مكتوبةٌ في الملفّ
    # وغيرُ مقروءةٍ (39 فجوةً استُرجعت)، ومفاتيحُ مكرَّرةٌ يقرأ البناءُ آخرَها
    # ويُهمل أوّلَها، وكتلٌ مكرَّرةٌ يقرأها البناءُ بالمصادفة.
    dupk, badgap, dupblk = [], [], []
    for f in files:
        b = os.path.basename(f)[:-3]
        raw = open(f, encoding="utf-8").read()
        m = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
        if not m: continue
        fm = m.group(1)
        lines = fm.split("\n")
        ks = [x.group(1) for l in lines if (x := re.match(r'^([a-zA-Z0-9_-]+):', l))]
        for k, c2 in collections.Counter(ks).items():
            if c2 > 1:
                (dupblk if k in ("related", "edges", "gaps") else dupk).append(f"{b}: {k} ×{c2}")
        try:
            gi = next(i for i, l in enumerate(lines) if re.match(r'^gaps:\s*$', l))
        except StopIteration:
            continue
        j = gi + 1
        while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("- ")):
            l = lines[j]
            if l.strip().startswith("- ") and not re.match(r'^\s*-\s*".*"\s*$', l):
                badgap.append(f"{b}: {l.strip()[:60]}")
            j += 1
    bad("مفتاحٌ مكرَّرٌ في frontmatter", len(dupk), dupk) if dupk \
        else ok("لا مفتاحَ مكرَّراً في أيِّ frontmatter")
    bad("كتلةٌ (`related`/`edges`/`gaps`) مُعلَنةٌ مرّتين", len(dupblk), dupblk) if dupblk \
        else ok("لا كتلةَ مُعلَنةً مرّتين")
    bad("بندُ `gaps` لا ينتهي بعلامة اقتباسٍ فيُهمله البناءُ بصمت", len(badgap), badgap) if badgap \
        else ok("كلُّ بنود `gaps` يقرأها البناء")

    # ── الخلاصة
    print(f"\n{'='*66}")
    if FAILURES:
        print(f"❌ فحوصٌ قاطعةٌ فاشلة: {len(FAILURES)}")
        for f in FAILURES: print(f"     - {f}")
        return 1
    print("✅ كلُّ الفحوص القاطعة سليمة.")
    print("   (البنودُ المعلَّمة ⚠️ تسجيلٌ لا خطأ: مدارسُ غائبة، ملفاتٌ بلا مصادر بقصد…)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
