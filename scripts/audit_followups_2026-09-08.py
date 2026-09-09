"""
بنودٌ صغيرةٌ رصدتها المراجعةُ الشاملة (`audit_atlas.py`) وأُغلقت.

1. **`con-epistemic-injustice-fricker-concept` و`thk-miranda-fricker` بلا أبٍ.**
   وفجوةُ المفهوم تقول «لا مدرسةَ أمّ في الأطلس تُنسب إليها… المفهومُ ينتمي إلى
   الإبستمولوجيا الاجتماعية». والملاحظةُ كانت دقيقةً وقتَ كتابتها في نفي
   `sch-virtue-ethics` و`sch-care-ethics`، لكنّ **`sch-epistemology`** («نظرية
   المعرفة») موجودةٌ في الأطلس وهي موضعُ الظلم المعرفيِّ بلا لبس. فأُسند الانتماءُ
   إليها وصُحِّحت الفجوة.

2. **`thk-cavasco` قسمُه `psychology`** وهو — بنصِّ لِيده — «عالم رياضيات وفيزيائي
   وفيلسوف… في التربية والإبستمولوجيا»، وأبوه `sch-epistemology` (قسمُه
   `philosophy`)، وأشقّاؤه كلُّهم `philosophy`. فوُحِّد.

    python3 scripts/audit_followups_2026-09-08.py            # فحص
    python3 scripts/audit_followups_2026-09-08.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PARENT = "sch-epistemology"
ATTACH = {
  "con-epistemic-injustice-fricker-concept": "الظلمُ المعرفيُّ مقولةٌ في الإبستمولوجيا الاجتماعية",
  "thk-miranda-fricker": "فريكر فيلسوفةٌ في الإبستمولوجيا الاجتماعية",
}
PART_FIX = {"thk-cavasco": ("psychology", "philosophy",
  "لِيدُه: «عالم رياضيات وفيزيائي وفيلسوف… في التربية والإبستمولوجيا»، وأبوه وأشقّاؤه كلُّهم `philosophy`")}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    for slug, why in ATTACH.items():
        if slug not in d: print("!! غير موجود:", slug); continue
        if any(e[0] == "belongs_to" for e in d[slug].get("edges", [])):
            print(f"   {slug}: له أبٌ بالفعل"); continue
        p = find_file(slug); t = open(p, encoding="utf-8").read()
        line = f'- rel: "belongs_to", target: "{PARENT}", target_type: "{d[PARENT].get("type")}"'
        if re.search(r'^edges: \[\]$', t, re.M):
            t = re.sub(r'^edges: \[\]$', 'edges:\n' + line, t, count=1, flags=re.M)
        elif re.search(r'^edges:\n', t, re.M):
            t = re.sub(r'^edges:\n', 'edges:\n' + line + '\n', t, count=1, flags=re.M)
        else:
            print(f"   !! لا حقلَ edges في {slug}"); continue
        # تصحيحُ الفجوة القديمة إن كانت تنفي وجودَ أبٍ
        t = re.sub(r'^(  - "\*\*لا مدرسةَ أمّ في الأطلس تُنسب إليها\*\*.*)$',
                   r'\1\n  - "**صُحِّحت الفجوةُ السابقة 2026-09-08:** كانت تنفي وجودَ مدرسةٍ أمّ، '
                   'وكان نفيُها دقيقاً في `sch-virtue-ethics` و`sch-care-ethics`، لكنّ '
                   '`sch-epistemology` («نظرية المعرفة») موجودةٌ في الأطلس وهي موضعُ '
                   'المفهوم — فأُسند الانتماءُ إليها."', t, count=1, flags=re.M)
        if 'صُحِّحت الفجوةُ السابقة 2026-09-08' not in t:
            t = re.sub(r'^gaps:$', 'gaps:\n  - "**أُسند الانتماء 2026-09-08:** كان الملفُّ بلا '
                       f'أبٍ، وأُسند إلى `{PARENT}` — {why}."', t, count=1, flags=re.M)
        print(f"{'APPLY' if apply else 'DRY'}  {slug:44} -> {PARENT}")
        if apply: open(p, "w", encoding="utf-8").write(t)
    for slug, (old, new, why) in PART_FIX.items():
        p = find_file(slug); t = open(p, encoding="utf-8").read()
        if not re.search(r'^part: "' + old + r'"$', t, re.M):
            print(f"   {slug}: قسمُه ليس {old}"); continue
        t = re.sub(r'^part: "' + old + r'"$', f'part: "{new}"', t, count=1, flags=re.M)
        t = re.sub(r'^gaps:$', 'gaps:\n  - "**وُحِّد حقل `part` 2026-09-08:** كان «' + old +
                   '» وصار «' + new + '» — ' + why + '."', t, count=1, flags=re.M)
        print(f"{'APPLY' if apply else 'DRY'}  {slug:44} part {old} -> {new}")
        if apply: open(p, "w", encoding="utf-8").write(t)

if __name__ == "__main__":
    main()
