"""
المرحلة 5 — توحيدُ البيانات الوصفية.

تُشغَّل **بعد** المراحل 1–4 لا قبلها: لأنّ إعادةَ كتابة عناوين `related` من
`data.json` تُثبِّت ما تشير إليه الروابطُ فعلاً — فلو شُغِّلت قبل تصحيح
الأهداف الخاطئة لثبَّتت الخطأَ وأزالت الدليلَ عليه. (وهو بعينه ما كشف خطأَ
«زندل سيغال» في المرحلة 2: العنوانُ المكتوبُ كان يفضح أنّ الهدفَ شخصٌ آخر.)

الأعمال:

**(1) `part`.** 516 عقدةً تخالف أباها. والقاعدةُ ليست «الابنُ يتبع أباه»
مطلقاً، بل **الأغلبيةُ داخل الأسرة**: إن خالف الأبُ أكثرَ أبنائه وله ثلاثةٌ
منهم على الأقلّ، فالخطأُ في الأب فيُقلَب هو؛ وإلا فالأبناءُ. وأكبرُ عنقودٍ
هنا 196 ملفاً تحت التحليل النفسي موسومةً `philosophy` — والتحليلُ النفسيُّ
علمُ نفسٍ لا فلسفة.

**(2) عناوينُ وأنواعُ `related` و`target_type`.** تُعاد كتابتُها من
`data.json` — أي من الملفّ الهدف نفسِه. فالعنوانُ المكتوبُ في الرابط نسخةٌ
قديمةٌ تتقادم مع كلِّ تعديلٍ في الهدف.

**(3) `level`.** سبعةَ عشرَ فارغاً تُعبَّأ بمقياسِ كثافةِ المتن (وهو المعيارُ
المُعلَنُ في مهمّةٍ سابقة)، وثلاثةٌ بقيمةٍ خارج المعجم («أساسي» ← «مبتدئ»).

**(4) `crumb`.** جذرُ المسار كان منقسماً بين «مدرسة التحليل النفسي» (210) و
«التحليل النفسي» (234) — أي أنّ فهرسَ التصفّح يعرض الشيءَ نفسَه في موضعين.
وُحِّد على الصيغة الأكثر. و99 ملفاً جذرُ مسارها «الناس» بلا مدرسة، فأُضيفت
مدرستُها من شجرة الانتماء.

**(5) `en`.** أربعةَ عشرَ حقلاً فيه عربيةٌ أو فاصلةٌ عربية.

**(6) `active_start`.** 206 ملفاً بلا هذا الحقل وفي `dates` سنةٌ صريحةٌ
قابلةٌ للاستخراج — وبغيره تغيب العقدةُ عن الخطِّ الزمني.

**(7) عناوينُ أقسامٍ مكرَّرةٌ وأقسامٌ فارغة.** العنوانُ الفارغ يُوهم القارئَ
أنّ مضموناً حُجب.
"""
import os, sys, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

LEVELS = ("مبتدئ", "متوسط", "متقدم")
CRUMB_UNIFY = {
    "مدرسة التحليل النفسي": "التحليل النفسي",
    "مدرسة علم النفس الفردي": "علم النفس الفردي",
    "مدرسة التحليل النفسي وعلم النفس الإكلينيكي": "التحليل النفسي",
    "نقد": "النقد الخارجي",
}
EN_FIX = {
    "rel-humanistic-existential": "Humanistic and Existential Psychology: From Rogers and Maslow to Yalom",
    "rel-behavioral-activation-depression": "Behavioral Activation and Depression: From Lewinsohn to Jacobson",
    "rel-dbt-bpd": "DBT and Borderline Personality Disorder: The Birth of DBT in Linehan's Clinic",
    "rel-act-cbt-third-wave": "ACT and the Third Wave of CBT: From Controversy to Convergence",
}


def core_title(t):
    return re.sub(r'\s*\(.*?\)\s*$', '', re.sub(r'\s*—.*$', '', t or '')).strip()


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    c = collections.Counter()
    par = {s: e[1] for s, n in d.items() for e in n.get("edges", [])
           if e[0] == "belongs_to" and e[1] in d}
    kids = collections.defaultdict(list)
    for s, p in par.items():
        kids[p].append(s)

    # ── (1) part بالأغلبية داخل الأسرة
    flip_parent, set_child = {}, {}
    for p, ch in kids.items():
        if d[p].get("part") == "bridge":
            continue
        real = [x for x in ch if d[x].get("part") not in ("bridge", None)]
        if not real:
            continue
        cnt = collections.Counter(d[x]["part"] for x in real)
        maj, nmaj = cnt.most_common(1)[0]
        if maj != d[p].get("part") and len(real) >= 3 and nmaj / len(real) >= 0.75:
            flip_parent[p] = maj
        else:
            for x in real:
                if d[x]["part"] != d[p].get("part"):
                    set_child[x] = d[p]["part"]
    for s, v in flip_parent.items():
        p, t = E.load(s)
        t2 = E.set_field(t, "part", v)
        if not t2:
            continue
        t2 = E.add_gap(t2, f"**صُحِّح `part` 2026-09-10:** كان «{d[s].get('part')}» ويخالف "
                           f"{len([x for x in kids[s] if d[x].get('part') == v])} من أبنائه — "
                           f"فالخطأُ في الأب لا في الأبناء، وصُحِّح إلى «{v}» بأغلبية الأسرة.") or t2
        E.save(p, t2); c["part_parent"] += 1
    byval = collections.defaultdict(list)
    for s, v in set_child.items():
        byval[v].append(s)
    for s, v in set_child.items():
        p, t = E.load(s)
        t2 = E.set_field(t, "part", v)
        if not t2:
            continue
        t2 = E.add_gap(t2, f"**صُحِّح `part` 2026-09-10:** كان «{d[s].get('part')}» بينما أبوه "
                           f"`{par[s]}` موسومٌ «{v}» — فوُحِّد على وسم الأب. والوسمُ يحكم التصفيةَ "
                           f"والفهارسَ في الواجهة، فاختلافُه عن الأب يُخرج العقدةَ من فهرس قسمها.") or t2
        E.save(p, t2); c["part_child"] += 1

    # ── (3) level
    for s, n in d.items():
        lv = n.get("level")
        if lv in LEVELS:
            continue
        w = len((n.get("lede") or "").split()) + sum(len(x[1].split()) for x in n.get("sections", []))
        new = "متقدم" if w >= 800 else ("متوسط" if w >= 300 else "مبتدئ")
        p, t = E.load(s)
        t2 = E.set_field(t, "level", new)
        if not t2:
            continue
        was = f"«{lv}»" if lv else "فارغاً"
        t2 = E.add_gap(t2, f"**عُبِّئ `level` 2026-09-10:** كان {was} وهو خارجُ المعجم "
                           f"(مبتدئ/متوسط/متقدم). وقُدِّر بكثافة المتن ({w} كلمة) ← «{new}».") or t2
        E.save(p, t2); c["level"] += 1

    # ── (5) en
    for s, n in d.items():
        en = n.get("en") or ""
        if not re.search(r'[؀-ۿ]', en):
            continue
        new = EN_FIX.get(s) or en.replace("،", ",")
        if re.search(r'[؀-ۿ]', new):
            print("  ⚠️  ما زال فيه عربية:", s, new); continue
        p, t = E.load(s)
        t2 = E.set_field(t, "en", new)
        if t2:
            E.save(p, t2); c["en"] += 1

    # ── (6) active_start من dates
    for s, n in d.items():
        if "active_start" in n:
            continue
        dt = str(n.get("dates") or "")
        bc = "ق.م" in dt
        m = re.search(r'\b(\d{3,4})\b', dt)
        if not m:
            continue
        y = int(m.group(1))
        if not bc and not (1000 <= y <= 2030):
            continue
        val = -y if bc else y
        p, t = E.load(s)
        t2 = E.set_field(t, "active_start", val, quote=False)
        if not t2:
            continue
        t2 = E.add_gap(t2, f"**عُبِّئ `active_start` 2026-09-10:** كان الحقلُ غائباً فتغيب العقدةُ "
                           f"عن الخطِّ الزمنيّ، والسنةُ صريحةٌ في `dates` («{dt[:60]}») فاستُخرجت: {val}.") or t2
        E.save(p, t2); c["active_start"] += 1

    # ── (4) crumb
    for s, n in d.items():
        cr = (n.get("crumb") or "").strip()
        if not cr:
            continue
        parts = [x.strip() for x in cr.split("←")]
        new = list(parts)
        if new[0] in CRUMB_UNIFY:
            new[0] = CRUMB_UNIFY[new[0]]
        elif new[0] == "الناس":
            pt = core_title(d[par[s]].get("title")) if s in par else None
            if pt:
                new = [pt] + new
        if new == parts:
            continue
        p, t = E.load(s)
        t2 = E.set_field(t, "crumb", " ← ".join(new))
        if not t2:
            continue
        t2 = E.add_gap(t2, f"**وُحِّد مسارُ التنقّل 2026-09-10:** كان «{parts[0]}» وصار «{new[0]}» — "
                           f"لأنّ الجذرَ كان منقسماً بين صيغتين للشيء نفسِه، فيعرض فهرسُ التصفّح "
                           f"موضعين لموضعٍ واحد.") or t2
        E.save(p, t2); c["crumb"] += 1

    # ── (7) عناوينُ أقسامٍ مكرَّرةٌ وأقسامٌ فارغة
    for path in E.all_files():
        t0 = open(path, encoding="utf-8").read()
        m = re.match(r'^(---\n.*?\n---\n)(.*)$', t0, re.S)
        if not m:
            continue
        fm, body = m.group(1), m.group(2)
        blocks = re.split(r'^(##\s+.+)$', body, flags=re.M)
        head, rest = blocks[0], blocks[1:]
        out, seen, drop, ren = [], collections.Counter(), 0, 0
        for i in range(0, len(rest), 2):
            h, txt = rest[i], (rest[i + 1] if i + 1 < len(rest) else "")
            name = h[2:].strip()
            if len(txt.strip()) < 15:
                drop += 1
                continue
            seen[name] += 1
            if seen[name] > 1:
                h = f"## {name} ({seen[name]})"; ren += 1
            out.append(h + txt)
        if not drop and not ren:
            continue
        nb = head + "".join(out)
        note = []
        if drop:
            note.append(f"حُذف {drop} قسماً فارغاً (أقلَّ من 15 حرفاً) — والعنوانُ الفارغ يُوهم القارئَ أنّ مضموناً حُجب")
        if ren:
            note.append(f"مُيِّز {ren} عنوانَ قسمٍ مكرَّرٍ حرفياً بترقيمه")
        t = fm + nb
        t = E.add_gap(t, "**نُظِّفت الأقسام 2026-09-10:** " + "؛ و".join(note) + ".") or t
        open(path, "w", encoding="utf-8").write(t)
        c["sections"] += 1

    # ── (2) عناوينُ/أنواعُ related و target_type — آخِرُ خطوة
    d2 = d  # الأسماءُ لم تتغيّر في هذه الدفعة إلا في en/level/part
    for path in E.all_files():
        t0 = open(path, encoding="utf-8").read()
        t = t0

        def fix_rel(m):
            i = m.group(1)
            if i not in d2:
                return m.group(0)
            return f'- id: "{i}", title: "{(d2[i].get("title") or "").replace(chr(34), chr(39))}", type: "{d2[i]["type"]}"'

        def fix_edge(m):
            tg = m.group(2)
            if tg not in d2:
                return m.group(0)
            return f'{m.group(1)}target: "{tg}", target_type: "{d2[tg]["type"]}"'

        t = re.sub(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"[^"]*"', fix_rel, t)
        t = re.sub(r'(rel:\s*"[^"]*"\s*,\s*)target:\s*"([^"]*)"\s*,\s*target_type:\s*"[^"]*"', fix_edge, t)
        if t != t0:
            open(path, "w", encoding="utf-8").write(t); c["labels"] += 1

    print("النتيجة:", dict(c))


if __name__ == "__main__":
    main()
