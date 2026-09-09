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
