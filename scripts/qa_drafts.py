#!/usr/bin/env python3
"""
qa_drafts.py — بوابة جودة آلية لملفات المسودات الجديدة.
تفحص معيار الإنجاز السبعة في ATLAS_MASTER_PLAN.md §3.

الاستعمال:
    python3 scripts/qa_drafts.py                      # كل المسودات
    python3 scripts/qa_drafts.py thinkers             # مجلد واحد
    python3 scripts/qa_drafts.py thinkers thk-kraepelin
"""
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DRAFTS = os.path.join(ROOT, "content", "ar", "drafts")
INDEX = os.path.join(DRAFTS, "EXISTING_SLUGS.md")

BLACKLIST = [
    "لا يوجد اقتباس مباشر موثوق متاح",
    "يمثل هذا المفهوم لبنة تأسيسية",
    "يقدم هذا العمل أطروحة فلسفية فارقة",
    "يمثل هذا التيار الفرعي تحولاً جوهرياً",
    "يمثل هذا العمل علامة فارقة في مجاله",
    "شكل هذا الحدث منعطفاً حاسماً",
    "يقدم هذا الموقف رؤية نسقية تستند",
    "يتناول هذا النقد تفكيك المسلمات",
    "حظي هذا المفهوم بمراجعات وتطويرات واسعة",
    "ترك هذا الفرع بصمات عميقة",
    "انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية",
    "حيث يوفر أداة دقيقة لتفسير قضايا الوجود",
    "حظي الكتاب بدراسات وشروح وترجمات واسعة",
]

FILLER = {
    "wrk-men-are-from-mars", "wrk-12-rules-for-life", "wrk-design-everyday-things",
    "wrk-power-of-habit", "con-res-cogitans-res-extensa", "con-set-and-setting",
    "con-voluntarism-divine-will", "br-relational-cultural", "br-recovered-memory-movement",
    "dbt-mao-maoism-vs-deng-ism", "dbt-feminist-essentialism-vs-constructionism",
    "evt-egaz-moniz-nobel-lobotomy-1949", "evt-founding-of-al-azhar-970",
}
STAMP = {"sch-cognitive-behavioral", "sch-psychoanalysis", "sch-existential-therapy",
         "sch-humanistic", "sch-positive-psychology"}

GENERIC_GAPS = [
    "لم يُراجع من مصدر أولي بعد",
    "المصادر الأولية تحتاج مراجعة وتوثيقاً إضافياً",
    "توسيع شبكة العلاقات مع المدارس المجاورة قيد المتابعة التحريرية",
    "لا يوجد اقتباس مباشر موثوق",
]

SCAFFOLD = ["أفكار روابط لم تُتحقق", "ملاحظة معمارية", "مراجعة وكيل",
            "(النسخة المعدلة)", "enhanced version", "alternative version"]

MIN_BODY, MAX_BODY = 1200, 6000
SOFT_BODY = 1800


def known_slugs():
    if not os.path.exists(INDEX):
        return None
    txt = open(INDEX, encoding="utf-8").read()
    return set(re.findall(r'^- `([a-z0-9-]+)`', txt, re.M))


def slug_types():
    """slug -> النوع الحقيقي من ملف الهدف نفسه."""
    m = {}
    base = os.path.join(ROOT, "content", "ar")
    for d in os.listdir(base):
        p = os.path.join(base, d)
        if not os.path.isdir(p) or d == "_merged":
            continue
        for f in os.listdir(p):
            if not f.endswith(".md"):
                continue
            try:
                head = open(os.path.join(p, f), encoding="utf-8").read(900)
            except Exception:
                continue
            t = re.search(r'^type: "(.*)"', head, re.M)
            ti = re.search(r'^title: "(.*)"', head, re.M)
            if t:
                m[f[:-3]] = t.group(1)
            if ti:
                _TITLE_MAP[f[:-3]] = ti.group(1)
    # المسودات كمان
    dt = os.path.join(base, "drafts")
    for d in os.listdir(dt):
        p = os.path.join(dt, d)
        if not os.path.isdir(p):
            continue
        for f in os.listdir(p):
            if f.endswith(".md"):
                head = open(os.path.join(p, f), encoding="utf-8").read(900)
                t = re.search(r'^type: "(.*)"', head, re.M)
                ti = re.search(r'^title: "(.*)"', head, re.M)
                if t:
                    m.setdefault(f[:-3], t.group(1))
                if ti:
                    _TITLE_MAP.setdefault(f[:-3], ti.group(1))
    return m


_TITLE_MAP = {}
TYPES = None
TITLES = None


def check(path, slugs):
    name = os.path.basename(path)[:-3]
    t = open(path, encoding="utf-8").read()
    errs, warns = [], []

    if t.count("---") < 2:
        return ["لا يوجد frontmatter صالح"], []
    fm, body = t.split("---", 2)[1], t.split("---", 2)[2]

    def field(k):
        m = re.search(rf'^{k}: (.*)$', fm, re.M)
        return m.group(1).strip().strip('"') if m else None

    # --- 0. البنية ---
    if field("slug") != name:
        errs.append(f"slug ({field('slug')}) ≠ اسم الملف ({name})")
    for k in ("slug", "id", "type", "part", "level", "title", "en", "crumb", "gaps"):
        if field(k) is None and f"\n{k}:" not in fm:
            errs.append(f"حقل ناقص: {k}")
    if field("part") not in ("psychology", "philosophy", "bridge"):
        errs.append(f"part غير صالح: {field('part')}")
    if field("level") not in ("مبتدئ", "متوسط", "متقدم"):
        errs.append(f"level غير صالح: {field('level')}")

    # صيغة السطر الواحد بلا إزاحة
    for ln in fm.split("\n"):
        if re.match(r'^\s+- (id|rel):', ln):
            errs.append("سطر related/edges بإزاحة بادئة (يجب عمود صفر)")
            break
    # related متعدد الأسطر: بند قائمة يبدأ بـ id: ولا يتبعه title في نفس السطر
    if re.search(r'^-\s*id:\s*"[^"]*"\s*$', fm, re.M):
        errs.append("related مكتوب على أسطر متعددة — البنّاء سيُسقطه صامتاً")

    # --- 1. طول المتن ---
    b = body.strip()
    if len(b) < MIN_BODY:
        errs.append(f"المتن {len(b)} حرف — أقل من الحد الأدنى {MIN_BODY}")
    elif len(b) < SOFT_BODY:
        warns.append(f"المتن {len(b)} حرف — دون المستهدف {SOFT_BODY}")
    if len(b) > MAX_BODY:
        warns.append(f"المتن {len(b)} حرف — فوق السقف {MAX_BODY}")

    # --- 2. القائمة السوداء ---
    for p in BLACKLIST:
        if p in t:
            errs.append(f"عبارة من القائمة السوداء: «{p[:45]}»")

    # --- 3. المصادر ---
    if "## المصادر" not in body:
        errs.append("لا يوجد قسم ## المصادر")
    else:
        src = body.split("## المصادر")[1]
        n = len([l for l in src.split("\n") if l.strip().startswith("-")])
        if n < 2:
            errs.append(f"قسم المصادر فيه {n} مرجعاً فقط (الحد الأدنى 2)")

    # --- 4. الروابط ---
    ids = re.findall(r'^- id: "([^"]+)", title: "([^"]*)", type: "([^"]*)"', fm, re.M)
    rel_ids = [i[0] for i in ids]
    if not (4 <= len(rel_ids) <= 10):
        errs.append(f"عدد الروابط {len(rel_ids)} — المطلوب بين 4 و10")
    if len(rel_ids) != len(set(rel_ids)):
        errs.append("روابط مكرّرة داخل الملف")
    if name in rel_ids:
        errs.append("رابط ذاتي")
    if slugs is not None:
        for i in rel_ids:
            if i not in slugs:
                errs.append(f"رابط لعنصر غير موجود: {i}")
    if TYPES:
        for rid, _rt, declared in ids:
            real = TYPES.get(rid)
            if real and declared and real != declared:
                errs.append(f"نوع الرابط يخالف نوع الهدف: {rid} كُتب «{declared}» والصحيح «{real}»")
    if TITLES:
        for rid, rt, _d in ids:
            real = TITLES.get(rid)
            if real and rt and " ".join(real.split()) != " ".join(rt.split()):
                warns.append(f"عنوان الرابط يخالف عنوان الهدف: {rid}\n         كُتب:    «{rt}»\n         الصحيح: «{real}»")

    # --- 5. الحشو والثلاثية ---
    bad = set(rel_ids) & FILLER
    if bad:
        errs.append(f"روابط حشو ممنوعة: {', '.join(sorted(bad))}")
    if len([i for i in rel_ids[:3] if i in STAMP]) >= 2:
        errs.append("ثلاثية المدارس المطبوعة في رأس الروابط")

    # كل رابط مبرَّر في المتن؟
    def stems(word):
        """الكلمة وجذعها بعد نزع أداة التعريف والسوابق الشائعة."""
        out = {word}
        for pre in ("وال", "بال", "كال", "فال", "لل", "ال", "و", "ب", "ك", "ف", "ل"):
            if word.startswith(pre) and len(word) - len(pre) >= 3:
                out.add(word[len(pre):])
        return out

    for rid, rtitle, _ in ids:
        core = re.sub(r'\s*\(.*?\)\s*', '', rtitle).strip()
        toks = [w for w in re.split(r'[\s،:—-]+', core) if len(w) > 2]
        cands = set()
        for w in toks:
            cands |= {x for x in stems(w) if len(x) > 2}
        if toks and not any(c in body for c in cands):
            warns.append(f"رابط غير مذكور في المتن: {rid} ({core[:28]})")

    # --- 6. gaps ---
    gaps = re.findall(r'^\s+- "(.*)"\s*$', fm.split("gaps:")[-1], re.M) if "gaps:" in fm else []
    if not gaps:
        errs.append("gaps فارغة أو غير مقروءة")
    elif all(any(g_ in g for g_ in GENERIC_GAPS) for g in gaps):
        errs.append("كل مداخل gaps عامة — يجب تسمية الناقص بالضبط")

    # --- 7. السقّالات ---
    for s in SCAFFOLD:
        if s in t:
            errs.append(f"سقّالة تحريرية ظاهرة: «{s}»")

    # --- إضافي: H1 = title ---
    h1 = re.search(r'^# (.+)$', body, re.M)
    if not h1:
        errs.append("لا يوجد عنوان H1")
    elif h1.group(1).strip() != (field("title") or "").strip():
        warns.append(f"H1 «{h1.group(1)[:30]}» ≠ title «{(field('title') or '')[:30]}»")

    # --- إضافي: تناسق الجنس في العناوين ---
    fem = len(re.findall(r'^## (ما أعطته|موقعها من .*|أهم أعمالها)\s*$', body, re.M))
    masc = len(re.findall(r'^## (ما أعطاه|موقعه من .*|أهم أعماله)\s*$', body, re.M))
    if fem and masc:
        errs.append("خلط بين صيغ المذكر والمؤنث في عناوين الأقسام")

    return errs, warns


def main():
    global TYPES, TITLES
    slugs = known_slugs()
    TYPES = slug_types()
    TITLES = _TITLE_MAP
    if slugs is None:
        print("⚠️  EXISTING_SLUGS.md غير موجود — تخطّي فحص وجود الروابط\n")
    args = sys.argv[1:]
    folders = [args[0]] if args else [d for d in sorted(os.listdir(DRAFTS))
                                      if os.path.isdir(os.path.join(DRAFTS, d))]
    only = args[1] if len(args) > 1 else None

    tot = ok = 0
    failing = []
    for fold in folders:
        p = os.path.join(DRAFTS, fold)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if not f.endswith(".md"):
                continue
            if only and f[:-3] != only:
                continue
            tot += 1
            errs, warns = check(os.path.join(p, f), slugs)
            if errs:
                failing.append(f[:-3])
                print(f"❌ {fold}/{f[:-3]}")
                for e in errs:
                    print(f"     ✗ {e}")
                for w in warns:
                    print(f"     · {w}")
            else:
                ok += 1
                mark = "✅" if not warns else "🟡"
                print(f"{mark} {fold}/{f[:-3]}")
                for w in warns:
                    print(f"     · {w}")

    print(f"\n{'='*60}\nالإجمالي: {tot} · ناجح: {ok} · راسب: {tot-ok}")
    if failing:
        print("الراسبة: " + ", ".join(failing))
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
