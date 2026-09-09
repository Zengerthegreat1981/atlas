"""
يصحّح ستَّ عقدٍ تُعلن نفسَها أباً لنفسِها في `belongs_to`.

`- rel: "belongs_to", target: "<slug العقدة نفسِها>"` حلقةٌ مغلقةٌ لا معنى لها،
ولا تُفيد القارئَ ولا الرسمَ البياني. وأصلُها — كما يظهر — **اختلاطٌ في البادئة**:
كُتب slug المفهوم (`con-`) في موضع slug التيّار (`br-`). وأوضحُ دليلٍ على ذلك أنّ
`con-aba-autism` يقابله `br-aba-autism` في الأطلس فعلاً، وكذلك
`con-id-psychotherapy` يقابله `br-psychotherapy-intellectual-disability`،
و`con-addiction-model-debate` يقابله `br-medical-model-addiction`.

    python3 scripts/fix_selfref_belongs_to.py            # فحص
    python3 scripts/fix_selfref_belongs_to.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FIX = {
 "con-aba-autism":              ("br-aba-autism", "التيّارُ المقابلُ موجودٌ بالاسم نفسِه — اختلاطُ بادئةٍ ظاهر"),
 "con-id-psychotherapy":        ("br-psychotherapy-intellectual-disability", "التيّارُ المقابلُ موجودٌ في الأطلس"),
 "con-addiction-model-debate":  ("br-medical-model-addiction", "التيّارُ المقابلُ موجودٌ في الأطلس"),
 "con-postcolonial-psychoanalysis": ("sch-psychoanalysis", "مقولةٌ في التحليل النفسي"),
 "con-political-psychoanalysis":    ("sch-psychoanalysis", "مقولةٌ في التحليل النفسي"),
 "con-community-psychology":        ("sch-liberation-psychology", "علمُ النفس المجتمعيُّ التحرُّريُّ من علم نفس التحرر"),
}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    bad = [t for t, _ in FIX.values() if t not in d]
    if bad: print("!! أهدافٌ غير موجودة:", bad); return
    n = 0
    for slug, (tgt, why) in FIX.items():
        if slug not in d: print("!! غير موجود:", slug); continue
        p = find_file(slug)
        t = open(p, encoding="utf-8").read()
        m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(slug) + r'".*$', t, re.M)
        if not m: print(f"   لا حلقةَ ذاتيةً في {slug}"); continue
        newline = f'- rel: "belongs_to", target: "{tgt}", target_type: "{d[tgt].get("type")}"'
        t2 = t[:m.start()] + newline + t[m.end():]
        note = ('  - "**صُحِّحت حلقةٌ ذاتية 2026-09-08:** كان `belongs_to` يشير إلى '
                f'`{slug}` — أي إلى الملفّ نفسِه، وهي حلقةٌ مغلقةٌ لا معنى لها، أصلُها '
                f'اختلاطُ بادئةٍ في الـslug. ونُقل إلى `{tgt}`: ' + why + '."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        n += 1
        print(f"{'APPLY' if apply else 'DRY'}  {slug:34} -> {tgt}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    print(f"\nصُحِّح: {n}")

if __name__ == "__main__":
    main()
