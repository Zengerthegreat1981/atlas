"""
يفكّ حلقاتِ `belongs_to` المتبادلة: A تنتمي إلى B، وB تنتمي إلى A.

أثرُها ليس على الزوجَين وحدَهما: **48 عقدةً** كان تسلسلُها الأعلى ينتهي إلى
حلقةٍ لا تُغلَق — أي أنّ صعودَ شجرة الانتماء منها لا يتوقّف أبداً. وهذا يُفسد
أيَّ حسابٍ للسلف الأعلى أو للتصفّح الهرمي.

والزوجان كلاهما **ازدواجٌ بين ملفَّي مدرسةٍ وتيّارٍ لموضوعٍ واحد**:
  · `sch-vienna-circle` («الوضعية المنطقية (حلقة فيينا)») ↔
    `br-logical-positivism-vienna-circle` («الوضعية المنطقية وحلقة فيينا»)
  · `sch-wahdat-alshuhud` ↔ `br-irfan-shuhudi-sirhindi`

والعلاجُ الجذريُّ دمجُهما (ملفٌّ واحدٌ لكلِّ موضوع)، وهو قرارٌ تحريريٌّ أوسع
تُركت له فجوةٌ مسجَّلة. وما يُفعَل هنا **فكُّ الحلقة فقط**، على اصطلاح الأطلس
الهرمي: **التيّار (`br-`) ينتمي إلى المدرسة (`sch-`)**، لا العكس. فيُحذف
الاتجاهُ المعاكس (`sch-` -> `br-`) ويبقى الصحيح.

    python3 scripts/break_belongs_to_cycles.py            # فحص
    python3 scripts/break_belongs_to_cycles.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    par = {}
    for s, n in d.items():
        for e in n.get("edges", []):
            if e[0] == "belongs_to" and e[1] in d: par[s] = e[1]; break
    pairs = {tuple(sorted((a, b))) for a, b in par.items() if par.get(b) == a}
    print(f"حلقاتٌ متبادلة: {len(pairs)}")
    for a, b in sorted(pairs):
        # يُحذف الاتجاه sch- -> br- ويبقى br- -> sch-
        drop, keep = (a, b) if a.startswith("sch-") and b.startswith("br-") else (b, a)
        print(f"\n   {a} <-> {b}")
        print(f"   يُبقى : {keep} -> {drop}")
        print(f"   يُحذف: {drop} -> {keep}")
        p = find_file(drop)
        if not p: print("   !! not found"); continue
        t = open(p, encoding="utf-8").read()
        m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(keep) + r'".*$', t, re.M)
        if not m: print("   !! سطرٌ غير موجود"); continue
        t2 = t[:m.start()] + t[m.end():]
        t2 = re.sub(r'\n\n+', '\n', t2)
        if not re.search(r'^edges:\n- rel:', t2, re.M):
            t2 = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t2, count=1, flags=re.M)
        note = ('  - "**فُكَّت حلقةُ انتماءٍ متبادلة 2026-09-08:** كان هذا الملفُّ يُعلن '
                f'`{keep}` أباً له، و`{keep}` يُعلن هذا الملفَّ أباً له — حلقةٌ مغلقةٌ '
                'كانت تجعل صعودَ شجرة الانتماء لا ينتهي (وتأثّر بها 48 عقدةً في الفرعَين). '
                'وحُذف هذا الاتجاه على اصطلاح الأطلس: **التيّار ينتمي إلى المدرسة لا العكس**. '
                f'ويبقى الملفّان مزدوجَين في الموضوع نفسِه (`{keep}` و`{drop}`)، ودمجُهما '
                'قرارٌ تحريريٌّ لم يُتَّخذ بعد."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        if apply: open(p, "w", encoding="utf-8").write(t2)
    print(f"\n{'طُبِّق' if apply else 'فحصٌ فقط'}")

if __name__ == "__main__":
    main()
