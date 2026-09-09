"""
يدمج زوجَين من الملفات المزدوجة: مدرسةٌ وتيّارٌ يغطّيان الموضوعَ نفسَه.

الزوجان ظهرا حين فُكَّت حلقاتُ `belongs_to` المتبادلة (`break_belongs_to_cycles.py`):
كلٌّ منهما كان يُعلن الآخرَ أباً له — وهي علامةٌ على الازدواج لا على الانتماء.

| المزدوج | كلمات | أقسام | أبناء | إشاراتٌ واردة | القرار |
|---|---|---|---|---|---|
| `sch-vienna-circle` | 292 | 5 | 10 | **14** | **المعتمد** |
| `br-logical-positivism-vienna-circle` | 228 | 4 | 9 | **0** | إحالة |
| `sch-wahdat-alshuhud` | 497 | 7 | 4 | **7** | **المعتمد** |
| `br-irfan-shuhudi-sirhindi` | 191 | 4 | 1 | **0** | إحالة |

وحقلُ `en` في زوج فيينا **متطابقٌ حرفياً** في الملفَّين
(«Logical Positivism (Vienna Circle)») — وهو أقطعُ دليلٍ على الازدواج.
والمعتمدُ في كلٍّ هو الأغزرُ متناً والأكثرُ إشاراتٍ واردةً إليه.

المعالجةُ على اصطلاح المستودع في الدمج:
  · لا يُحذف ملفٌّ ولا يُعاد تسميةُ slug (الروابطُ الواردةُ تُصان).
  · يبقى المزدوجُ في موضعه ويصير **إحالة**: عنوانُه يُلحَق بـ«— إحالة، انظر …»،
    و`edges: []`، و`related` بندٌ واحدٌ إلى المعتمد، والقرارُ في `gaps`.
  · **تُنقَل أنسابُ أبنائه** إلى المعتمد كي لا يبقى أبٌ مهجورٌ (وهو الخللُ الذي
    وقع في دمجٍ سابقٍ مع `sch-cbt` فبقي 43 ملفاً يُعلن إحالةً أباً له).
  · تُؤرشَف النسخةُ الأصلية في `agents_specs/merge-archive-2026-09-08/`.

    python3 scripts/merge_duplicate_school_current_pairs.py            # فحص
    python3 scripts/merge_duplicate_school_current_pairs.py --apply
"""
import json, os, re, sys, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ARCHIVE = os.path.join(ROOT, "agents_specs", "merge-archive-2026-09-08")

PAIRS = [
  ("br-logical-positivism-vienna-circle", "sch-vienna-circle",
   "حقلُ `en` متطابقٌ حرفياً في الملفَّين، والمعتمدُ أغزرُ متناً (292 مقابل 228 كلمة) "
   "وإليه 14 إشارةً واردةً مقابل صفر"),
  ("br-irfan-shuhudi-sirhindi", "sch-wahdat-alshuhud",
   "كلاهما في وحدة الشهود عند أحمد السرهندي، والمعتمدُ أغزرُ متناً (497 مقابل 191 كلمة) "
   "وإليه 7 إشاراتٍ واردةٍ مقابل صفر"),
]

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    if apply: os.makedirs(ARCHIVE, exist_ok=True)
    for dup, keep, why in PAIRS:
        if dup not in d or keep not in d: print("!! غير موجود:", dup, keep); continue
        print(f"\n=== {dup}  ->  إحالة إلى  {keep} ===")
        # 1) نقلُ أنساب الأبناء
        kids = [s for s, n in d.items()
                if any(e[0] == "belongs_to" and e[1] == dup for e in n.get("edges", []))]
        print(f"   أبناءٌ ستُنقل أنسابُهم: {len(kids)}")
        for s in kids:
            p = find_file(s)
            if not p: continue
            t = open(p, encoding="utf-8").read()
            m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(dup) + r'".*$', t, re.M)
            if not m: continue
            t = t[:m.start()] + f'- rel: "belongs_to", target: "{keep}", target_type: "{d[keep].get("type")}"' + t[m.end():]
            note = ('  - "**نُقل الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    f'`{dup}`، وقد صار ذلك الملفُّ **إحالةً** إلى `{keep}` بعد دمج '
                    'ملفَّين مزدوجَين، فنُقل الانتماءُ إلى المعتمد."')
            t = re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)
            print(f"     {'APPLY' if apply else 'DRY'}  {s}")
            if apply: open(p, "w", encoding="utf-8").write(t)
        # 2) تحويلُ المزدوج إلى إحالة
        p = find_file(dup)
        t = open(p, encoding="utf-8").read()
        if apply: shutil.copy2(p, os.path.join(ARCHIVE, os.path.basename(p)))
        title = d[dup].get("title") or ""
        if "إحالة" not in title:
            t = re.sub(r'^title: ".*"$', f'title: "{title} — إحالة، انظر {keep}"', t, count=1, flags=re.M)
        t = re.sub(r'^edges:\n(- rel:.*\n)+', 'edges: []\n', t, count=1, flags=re.M)
        t = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t, count=1, flags=re.M)
        rel = f'related:\n- id: "{keep}", title: "{d[keep].get("title")}", type: "{d[keep].get("type")}"\n'
        t = re.sub(r'^related:\n(- .*\n)*', rel, t, count=1, flags=re.M)
        note = ('  - "**دُمج هذا الملفُّ 2026-09-08 وصار إحالة:** كان مزدوجاً مع '
                f'`{keep}` — ' + why + '. ولم يُحذف الملفُّ ولا أُعيدت تسميةُ الـslug '
                'صوناً للروابط الواردة، ونُقلت أنسابُ أبنائه إلى المعتمد. والأصلُ في '
                '`agents_specs/merge-archive-2026-09-08/`."')
        t = re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)
        print(f"   {'APPLY' if apply else 'DRY'}  تحويلُ {dup} إلى إحالة")
        if apply: open(p, "w", encoding="utf-8").write(t)

if __name__ == "__main__":
    main()
