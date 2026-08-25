#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
task.py — واجهة التاسكات لـ Spark و MiniMax.

الهدف: النموذج ماياخدش قايمة ملفات من غير ما يقراها، وماياخدش تاسك جديد
لغاية ما يقفل اللي قبله بتقرير. الأمر ده هو اللي بيخلي ملف SPARK.md/MINIMAX.md
صغيراً — النموذج بيقرا التاسك (وصفه العام) من ملفه، وبياخد قايمة الملفات
الفعلية من هنا وقت التنفيذ، مش من الملف.

الاستعمال:
    python3 scripts/task.py get    <spark|minimax> <رقم التاسك>          [حجم الدفعة]
    python3 scripts/task.py verify <spark|minimax> <رقم.دفعة>
    python3 scripts/task.py report <spark|minimax> <رقم.دفعة>
    python3 scripts/task.py status <spark|minimax>
    python3 scripts/task.py checkpoint <spark|minimax>     # كلود فقط، بعد المراجعة

قاعدة الوقوف: كل 5 دفعات (get) بدون checkpoint، الأمر get بيرفض ويطلب مراجعة.
"""
from __future__ import annotations
import os, re, sys, json, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_parse as ap
import atlas_health as ah

ROOT = ap.ROOT
AR = ap.AR
REPORTS = os.path.join(ROOT, "agents_specs", "reports")
CHECKPOINT_EVERY = 5

# ---------------------------------------------------------------------------
# خرائط الملكية والعمليات — نفس الترتيب والعناوين الموجودة في
# agents_specs/SPARK.md و agents_specs/MINIMAX.md بالحرف.
# mode:
#   "thinkers"  → folder=thinkers، filtered بنطاق أول حرف بعد thk-
#   "folder"    → مجلد أو أكتر، بالترتيب الأبجدي
#   "creative"  → مرحلة الإنشاء، مفيش قايمة ملفات معتمدة يُشتغل عليها،
#                 التاسك نفسه (الموضوعات) موجود في SPARK.md/MINIMAX.md
SORT_BY_LEN_ASC = "len_asc"   # الأقصر أولاً (مؤشر: يحتاج تعميق/فحص أولوية)

MANIFEST = {
    "spark": {
        1: {"mode": "thinkers", "range": ("a", "l"), "sort": SORT_BY_LEN_ASC, "batch": 25,
            "op": "التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر",
            "verify": "prose"},
        2: {"mode": "thinkers", "range": ("a", "l"), "sort": SORT_BY_LEN_ASC, "batch": 15,
            "op": "الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة",
            "verify": "prose"},
        3: {"mode": "thinkers", "range": ("a", "l"), "sort": "alpha", "batch": 35,
            "op": "التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج",
            "verify": "prose"},
        4: {"mode": "thinkers", "range": ("a", "l"), "sort": SORT_BY_LEN_ASC, "batch": 30,
            "op": "التعميق والمصادر لملفات تحت المعيار",
            "verify": "prose"},
        5: {"mode": "folder", "folders": ["works"], "sort": "alpha", "batch": 40,
            "op": "works: إضافة author / author_slug / publication_year / original_language",
            "verify": "schema:author"},
        6: {"mode": "folder", "folders": ["works"], "sort": SORT_BY_LEN_ASC, "batch": 30,
            "op": "works: التعميق (الأطروحة، الاستقبال، الترجمات) + المصادر",
            "verify": "prose"},
        7: {"mode": "folder", "folders": ["studies"], "sort": "alpha", "batch": 30,
            "op": "studies: study_year/design/sample_size/main_finding/replication_status + المتن",
            "verify": "schema:study_year"},
        8: {"mode": "folder", "folders": ["instruments"], "sort": "alpha", "batch": 30,
            "op": "instruments: items_count/target_population/reliability/evidence_level",
            "verify": "schema:evidence_level"},
        9: {"mode": "folder", "folders": ["techniques"], "sort": "alpha", "batch": 30,
            "op": "techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level",
            "verify": "schema:evidence_level"},
        10: {"mode": "folder", "folders": ["disorders", "syndromes"], "sort": "alpha", "batch": 30,
             "op": "disorders+syndromes: السقف الإكلينيكي + dsm_code/icd_code",
             "verify": "prose"},
        11: {"mode": "folder", "folders": ["events"], "sort": "alpha", "batch": 30,
             "op": "events: event_date/event_place + الحاضرون بالاسم",
             "verify": "schema:event_date"},
        12: {"mode": "folder", "folders": ["contexts", "experiences", "metaphors"], "sort": "alpha", "batch": 30,
             "op": "contexts/experiences/metaphors: تصنيف الصوت السردي + التعميق",
             "verify": "prose"},
        13: {"mode": "creative", "op": "الدراسة موجودة وصاحبها غائب (مؤسسو العلم/الطب النفسي)"},
        14: {"mode": "creative", "op": "دراسات وأدوات حديثة (Many Labs, STAR*D, DES, PCL-R...)"},
        15: {"mode": "creative", "op": "تقنيات واضطرابات غائبة (ABA, تخطيط السلامة, البارانويدي...)"},
        16: {"mode": "creative", "op": "النوع الجديد drg- (أدوية)"},
        17: {"mode": "creative", "op": "طبقة ما بعد 2010 (العلم المفتوح، الحوسبي، الشبكي...)"},
    },
    "minimax": {
        1: {"mode": "thinkers", "range": ("m", "z"), "sort": SORT_BY_LEN_ASC, "batch": 25,
            "op": "التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر",
            "verify": "prose"},
        2: {"mode": "thinkers", "range": ("m", "z"), "sort": SORT_BY_LEN_ASC, "batch": 15,
            "op": "الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة",
            "verify": "prose"},
        3: {"mode": "thinkers", "range": ("m", "z"), "sort": "alpha", "batch": 35,
            "op": "التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج",
            "verify": "prose"},
        4: {"mode": "thinkers", "range": ("m", "z"), "sort": SORT_BY_LEN_ASC, "batch": 30,
            "op": "التعميق والمصادر لملفات تحت المعيار",
            "verify": "prose"},
        5: {"mode": "folder", "folders": ["schools", "branches", "relations"], "sort": "alpha", "batch": 40,
            "op": "belongs_to: تحويل الأسماء العربية لـ slugs + بنك المدارس الغائبة",
            "verify": "belongs_to"},
        6: {"mode": "folder", "folders": ["branches"], "sort": SORT_BY_LEN_ASC, "batch": 30,
            "op": "branches: كسر القالب + evolved_into/absorbed_by/split_into",
            "verify": "prose"},
        7: {"mode": "folder", "folders": ["relations"], "sort": SORT_BY_LEN_ASC, "batch": 30,
            "op": "relations: تسمية المفكرين والأعمال بالاسم + part: bridge",
            "verify": "prose"},
        8: {"mode": "folder", "folders": ["schools"], "sort": "alpha", "batch": 30,
            "op": "schools: ## المصادر + cultural_origin + حسم الازدواجات",
            "verify": "prose"},
        9: {"mode": "folder", "folders": ["concepts"], "sort": "alpha", "batch": 30,
            "op": "concepts: إعادة بناء related من الصفر مع تبرير كل رابط",
            "verify": "prose"},
        10: {"mode": "folder", "folders": ["concepts"], "sort": SORT_BY_LEN_ASC, "batch": 30,
             "op": "concepts: كسر القالب + التعميق + الفصل الإلزامي فلسفي/إكلينيكي",
             "verify": "prose"},
        11: {"mode": "folder", "folders": ["debates", "critiques"], "sort": "alpha", "batch": 30,
             "op": "debates+critiques: تسمية الطرفين/الناقد بالاسم والنص والسنة",
             "verify": "prose"},
        12: {"mode": "folder", "folders": ["dialogues", "questions", "terms", "axioms"], "sort": "alpha", "batch": 30,
             "op": "dialogues/questions/terms/axioms: تصنيف + تعميق + مصادر",
             "verify": "prose"},
        13: {"mode": "creative", "op": "المدارس الغائبة (~147 مدرسة، من بنك 5.x)"},
        14: {"mode": "creative", "op": "علم النفس العربي الحديث (يوسف مراد، سويف...)"},
        15: {"mode": "creative", "op": "الفلاسفة والمفكرون الغائبون (دوركهايم، بورديو...)"},
        16: {"mode": "creative", "op": "أعمال وحوارات غائبة + حسم ازدواجات الكتب"},
        17: {"mode": "creative", "op": "النوع الجديد eth- (وثائق أخلاقية/قانونية معيارية)"},
    },
}


def _state_path(track):
    d = os.path.join(REPORTS, track)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "state.json")


def _load_state(track):
    p = _state_path(track)
    if os.path.isfile(p):
        return json.load(open(p, encoding="utf-8"))
    return {"claimed": {}, "next_sub": {}, "since_checkpoint": 0}


def _save_state(track, st):
    json.dump(st, open(_state_path(track), "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def _thinker_first_letter(slug):
    return slug[4:5].lower() if slug.startswith("thk-") else ""


def _candidates(track, major):
    spec = MANIFEST[track][major]
    files = []
    if spec["mode"] == "thinkers":
        lo, hi = spec["range"]
        base = os.path.join(AR, "thinkers")
        for f in os.listdir(base):
            if not f.endswith(".md"):
                continue
            slug = f[:-3]
            c = _thinker_first_letter(slug)
            if lo <= c <= hi:
                files.append(os.path.join(base, f))
    elif spec["mode"] == "folder":
        for folder in spec["folders"]:
            base = os.path.join(AR, folder)
            if not os.path.isdir(base):
                continue
            for f in os.listdir(base):
                if f.endswith(".md"):
                    files.append(os.path.join(base, f))
    else:
        return []

    if spec.get("sort") == SORT_BY_LEN_ASC:
        def keyfn(p):
            try:
                d = ap.parse_file(p)
                return len(d.body.strip())
            except ap.AtlasParseError:
                return 0
        files.sort(key=keyfn)
    else:
        files.sort()
    return files


def cmd_get(track, major, batch_override=None):
    major = int(major)
    spec = MANIFEST[track][major]
    st = _load_state(track)

    if st["since_checkpoint"] >= CHECKPOINT_EVERY:
        print(f"⛔ وقفت. اتعملتلك {st['since_checkpoint']} دفعة من غير مراجعة.")
        print("استنى رئيس التحرير يراجع ويشغّل: python3 scripts/task.py checkpoint " + track)
        return

    if spec["mode"] == "creative":
        n = st["next_sub"].get(str(major), 0) + 1
        st["next_sub"][str(major)] = n
        st["since_checkpoint"] += 1
        _save_state(track, st)
        print(f"# Task {major}.{n}  ·  {track}  ·  مرحلة الإنشاء (drafts/{track}/)")
        print(f"العملية: {spec['op']}")
        print(f"التفاصيل الكاملة في agents_specs/{ 'SPARK.md' if track=='spark' else 'MINIMAX.md' } — Task {major}.")
        print("اكتب في content/ar/drafts/" + track + "/<النوع>/ فقط. دوّر في EXISTING_SLUGS.md قبل أي slug جديد.")
        print(f"\nبعد ما تخلص: python3 scripts/task.py report {track} {major}.{n}")
        return

    claimed = set(st["claimed"].keys())
    cands = [p for p in _candidates(track, major) if p not in claimed]
    batch_size = batch_override or spec["batch"]
    batch = cands[:batch_size]

    if not batch:
        print(f"مفيش ملفات جديدة في Task {major} — كل ملفاته اتاخدت قبل كده. راجع الفهرس:")
        print(f"  agents_specs/reports/{track}/INDEX.md")
        return

    n = st["next_sub"].get(str(major), 0) + 1
    st["next_sub"][str(major)] = n
    for p in batch:
        st["claimed"][p] = f"{major}.{n}"
    st["since_checkpoint"] += 1
    _save_state(track, st)

    sub_id = f"{major}.{n}"
    print(f"# Task {sub_id}  ·  {track}  ·  {len(batch)} ملفاً")
    print(f"العملية: {spec['op']}\n")
    print("الملفات:")
    for p in batch:
        print(" ", os.path.relpath(p, ROOT))
    print(f"\nأمر التحقق بعد الانتهاء:")
    print(f"  python3 scripts/task.py verify {track} {sub_id}")
    print(f"\nبعد التحقق، اكتب التقرير:")
    print(f"  python3 scripts/task.py report {track} {sub_id}")


def _files_for_subtask(track, sub_id):
    st = _load_state(track)
    return [p for p, sid in st["claimed"].items() if sid == sub_id]


def cmd_verify(track, sub_id):
    major = int(sub_id.split(".")[0])
    spec = MANIFEST[track][major]
    files = _files_for_subtask(track, sub_id)
    if not files:
        print(f"مفيش ملفات مسجَّلة لـ {sub_id}. اتأكد إنك عملت get الأول.")
        return

    kind = spec.get("verify", "prose")
    print(f"=== تحقق Task {sub_id} ({len(files)} ملفاً) ===\n")

    bl_hits = scaffold_hits = source_ok = 0
    schema_ok = 0
    schema_field = kind.split(":")[1] if ":" in kind else None
    for p in files:
        if not os.path.isfile(p):
            continue
        full = open(p, encoding="utf-8", errors="replace").read()
        if any(b in full for b in ah.BLACKLIST):
            bl_hits += 1
        if any(m in full for m in ah.SCAFFOLD_MARKERS):
            scaffold_hits += 1
        if "## المصادر" in full:
            source_ok += 1
        if schema_field and re.search(rf'^{schema_field}:', full, re.M):
            schema_ok += 1

    print(f"جمل القائمة السوداء متبقية: {bl_hits} (المستهدف 0)")
    print(f"سقّالة ظاهرة متبقية: {scaffold_hits} (المستهدف 0)")
    print(f"فيها ## المصادر: {source_ok} / {len(files)}")
    if schema_field:
        print(f"فيها الحقل {schema_field}: {schema_ok} / {len(files)}")
    print(f"\n(لو ده تنظيف من drafts/: تأكد يدوياً من القائمة السوداء §5 والمعيار §4 —")
    print(f" التحقق الآلي هنا مؤشر أولي، مش بديل عن قراءتك للملفات.)")


def cmd_report(track, sub_id):
    major = int(sub_id.split(".")[0])
    spec = MANIFEST[track][major]
    files = _files_for_subtask(track, sub_id)
    d = os.path.join(REPORTS, track, f"T{major}")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"task-{sub_id}.md")

    rel_files = [os.path.relpath(p, ROOT) for p in files] if files else ["(مرحلة إنشاء — لا قائمة ملفات ثابتة)"]

    tpl = f"""# Task {sub_id}
الحالة: <مكتمل | مكتمل جزئياً | متوقف>
المسار: {track} | العملية: {spec['op']} | الملفات: {len(files) if files else 'غير مقيّد'}

## الأرقام
<مؤشر>: قبل X → بعد Y

## أمر التحقق
python3 scripts/task.py verify {track} {sub_id}
→ <الصق الناتج هنا>

## قرارات اتخذتها
- <ملف>: <القرار والسبب>

## متوقف عنده (لرئيس التحرير)
- <ملف>: <المشكلة>

## الملفات
{chr(10).join(rel_files)}
"""
    if not os.path.isfile(path):
        open(path, "w", encoding="utf-8").write(tpl)
        print(f"✅ اتكتب القالب في {os.path.relpath(path, ROOT)} — املاه واحفظه.")
    else:
        print(f"⚠️  {os.path.relpath(path, ROOT)} موجود بالفعل. عدّله يدوياً لو محتاج تحديث.")

    idx = os.path.join(REPORTS, track, "INDEX.md")
    print(f"\nلما تخلص ملء القالب، ضيف سطر في {os.path.relpath(idx, ROOT)}:")
    print(f"| {sub_id} | ✅ | <التاريخ> | {spec['op'][:40]} | {len(files) if files else '—'} ملفاً |")


def cmd_status(track):
    st = _load_state(track)
    print(f"=== حالة {track} ===")
    print(f"دفعات مُتاحة منذ آخر مراجعة: {st['since_checkpoint']} / {CHECKPOINT_EVERY}")
    for major in sorted(MANIFEST[track], key=int):
        n = st["next_sub"].get(str(major), 0)
        spec = MANIFEST[track][major]
        claimed_n = sum(1 for sid in st["claimed"].values() if sid.startswith(f"{major}."))
        print(f"  Task {major}: {n} دفعة صدرت ({claimed_n} ملفاً) — {spec['op'][:50]}")


def cmd_checkpoint(track):
    st = _load_state(track)
    st["since_checkpoint"] = 0
    _save_state(track, st)
    print(f"✅ اتصفّرت عدّاد المراجعة لـ {track}. يقدر ياخد 5 دفعات جداد.")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        return
    cmd = args[0]
    track = args[1]
    if track not in MANIFEST and cmd != "checkpoint":
        print(f"❌ مسار غير معروف: {track} (spark أو minimax فقط)")
        return

    if cmd == "get":
        major = args[2]
        batch = int(args[3]) if len(args) > 3 else None
        cmd_get(track, major, batch)
    elif cmd == "verify":
        cmd_verify(track, args[2])
    elif cmd == "report":
        cmd_report(track, args[2])
    elif cmd == "status":
        cmd_status(track)
    elif cmd == "checkpoint":
        cmd_checkpoint(track)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
