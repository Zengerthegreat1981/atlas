"""
يربط أعلامَ الطب النفسي الظاهراتي بمدرستهم الجديدة `sch-phenomenological-psychiatry`.

هؤلاء الأربعةَ عشرَ كان `belongs_to` فيهم مختوماً آلياً على «الوجودية العلاجية»
(مدرسةٌ علاجيةٌ إكلينيكية)، فلمّا صُحِّح بقي فارغاً لعدم وجود ملفٍّ لحقلهم — وقد
أُنشئ الآن، فيُعاد الانتماءُ إلى موضعه الصحيح.

    python3 scripts/attach_phenomenological_psychiatry_members.py            # فحص
    python3 scripts/attach_phenomenological_psychiatry_members.py --apply
"""
import json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCHOOL = "sch-phenomenological-psychiatry"
MEMBERS = ["thk-bally", "thk-binswanger", "thk-blankenburg", "thk-buytendijk", "thk-ey",
           "thk-fuchs", "thk-gebsattel", "thk-minkowski", "thk-plugge", "thk-sass",
           "thk-stanghellini", "thk-tatossian", "thk-vandenberg", "thk-weizsacker"]

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    if SCHOOL not in d: print("!! المدرسة غير موجودة:", SCHOOL); return
    n = 0
    for slug in MEMBERS:
        if slug not in d: print("!! غير موجود:", slug); continue
        if any(e[0] == "belongs_to" for e in d[slug].get("edges", [])):
            print(f"   {slug}: له انتماءٌ بالفعل — يُترك"); continue
        p = find_file(slug)
        t = open(p, encoding="utf-8").read()
        line = f'- rel: "belongs_to", target: "{SCHOOL}", target_type: "مدرسة"\n'
        if re.search(r'^edges: \[\]$', t, re.M):
            t2 = re.sub(r'^edges: \[\]$', 'edges:\n' + line.rstrip("\n"), t, count=1, flags=re.M)
        elif re.search(r'^edges:\n', t, re.M):
            t2 = re.sub(r'^edges:\n', 'edges:\n' + line, t, count=1, flags=re.M)
        else:
            print(f"   !! لا حقلَ edges في {slug}"); continue
        note = ('  - "**أُعيد الانتماء 2026-09-08:** كان `belongs_to` مختوماً آلياً على '
                '«الوجودية العلاجية» فصُحِّح وبقي فارغاً لعدم وجود مدرسةٍ لهذا الحقل؛ '
                f'وقد أُنشئ ملفُّ `{SCHOOL}` فأُسند الانتماءُ إليه."')
        t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
        n += 1
        print(f"{'APPLY' if apply else 'DRY'}  {slug}")
        if apply: open(p, "w", encoding="utf-8").write(t2)
    print(f"\nرُبط: {n}")

if __name__ == "__main__":
    main()
