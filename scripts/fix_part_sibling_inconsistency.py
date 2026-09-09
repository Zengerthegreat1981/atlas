"""
يوحّد حقل `part` حيث يخالف عنصرٌ **أشقّاءه** تحت الأب نفسِه.

## ما هو `part`، وما ليس
`part` ليس حقلاً معروضاً للقارئ — فحصتُ `scripts/template/`، ولا يستعمله الواجهةُ
في أيِّ موضع (الثمانيةُ مواضعُ التي تحمل الكلمة كلُّها متغيّراتُ تقسيمِ نصوصٍ
لا صلةَ لها بالحقل). وهو حقلٌ تنظيميٌّ يقسم الأطلسَ أقساماً للإصدار — بدليل
`agents_specs/PHILOSOPHY_PART_PLAN.md` و`SOCIOLOGY_PART_PLAN.md`. وتوزيعُه في
المستودع متوازن: 3309 فلسفة، 3177 علم نفس، 161 جسراً، 3 اجتماع.

**ولهذا لم تُعَد كتابةُ الحقل على 543 ملفاً** ممّا يخالف قسمَ مدرسته: الحقلُ
دلالتُه قرارُ إصدارٍ لا تصنيفُ حقلٍ معرفيّ، وإعادةُ تفسيره من عندي تغييرٌ واسعٌ
في حقلٍ لا أعرف مرادَه كلَّه ولا أثرَ له في العرض. **ما يُعالَج هنا أضيقُ وأوثق**:
عنصرٌ يخالف أشقّاءه المباشرين مخالفةً شاذّةً — وهو تعارضٌ داخليٌّ في المجموعة
نفسِها أيّاً كان مرادُ الحقل.

## شروطٌ ثلاثة، وكلُّها لازمة
1. للأب **ثمانيةُ أبناءٍ** على الأقلّ (حتى تكون «الأغلبية» ذاتَ معنى).
2. المخالفون **20٪ أو أقلّ** من الأبناء.
3. **أغلبيةُ الأشقّاء تطابق قسمَ الأب** — وهذا الشرطُ يمنع نشرَ الخطأ: في
   `br-nlp-systemic` (تيّارٌ علاجيٌّ قسمُه `psychology`) أغلبيةُ الأبناء
   `philosophy`، فالأغلبيةُ نفسُها مشكوكة، فيُترك الفرعُ كلُّه.

## و`bridge` يُستثنى استثناءً تامّاً
كلُّ عقدةٍ من نوع «علاقة بين مدرستين» (`rel-`) قسمُها `bridge` — وهو **صحيحٌ
بالتصميم**: العلاقةُ بين التحليل النفسي وCBT تجسر قسمَين ولا تنتمي إلى أحدهما.
وكان الفحصُ الأولُ يرصدها خطأً (23 عقدة)، فاستُثنيت.

## وما لا يُعالَج
`sch-psychoanalysis` أبناؤه 238 `psychology` مقابل 205 `philosophy` — انقسامٌ
بالنصف لا أغلبيةٌ وشواذّ. فهو **قرارٌ تحريريٌّ غيرُ محسوم** على مستوى المستودع
(سُجِّل في تقرير 2026-09-07)، ولا يُحسَم بقاعدةٍ آلية.

    python3 scripts/fix_part_sibling_inconsistency.py            # فحص
    python3 scripts/fix_part_sibling_inconsistency.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MIN_SIBS = 8
MAX_MINORITY = 0.20

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    kids = collections.defaultdict(list)
    for s, n in d.items():
        for e in n.get("edges", []):
            if e[0] == "belongs_to" and e[1] in d: kids[e[1]].append(s)
    plan = []; skipped = []
    for p, xs in sorted(kids.items()):
        # bridge مستثنًى بالتصميم
        xs = [s for s in xs if d[s].get("part") != "bridge"]
        if len(xs) < MIN_SIBS: continue
        c = collections.Counter(d[s].get("part") for s in xs)
        if len(c) < 2: continue
        maj = c.most_common()[0]
        if maj[0] != d[p].get("part"):
            skipped.append((p, dict(c), d[p].get("part"))); continue
        for part, cnt in c.most_common()[1:]:
            if cnt / len(xs) > MAX_MINORITY: continue
            for s in xs:
                if d[s].get("part") == part: plan.append((s, part, maj[0], p))
    print(f"عناصرُ تخالف أشقّاءها: {len(plan)}")
    if skipped:
        print(f"\nفروعٌ تُركت لأنّ أغلبيةَ أبنائها تخالف قسمَ الأب (الأغلبيةُ نفسُها مشكوكة):")
        for p, c, pp in skipped: print(f"   {p:34} أب={pp:11} أبناء={c}")
    print()
    for s, old, new, p in plan:
        print(f"{'APPLY' if apply else 'DRY'}  {d[s].get('type')[:5]:6} {s:44} {old} -> {new}   (أشقّاء {p})")
        if not apply: continue
        fp = find_file(s)
        t = open(fp, encoding="utf-8").read()
        if not re.search(r'^part: ".*"$', t, re.M): print("   !! لا حقلَ part"); continue
        t = re.sub(r'^part: ".*"$', f'part: "{new}"', t, count=1, flags=re.M)
        note = ('  - "**وُحِّد حقل `part` 2026-09-08:** كان «' + old + '» وصار «' + new + '» '
                f'اتّساقاً مع أشقّائه تحت `{p}` (وأغلبيتُهم «{new}» وهو قسمُ الأب نفسِه). '
                'والحقلُ تنظيميٌّ لا يُعرَض للقارئ، والتصحيحُ لتعارضٍ داخليٍّ في المجموعة."')
        t = re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)
        open(fp, "w", encoding="utf-8").write(t)
    print(f"\nالإجمالي: {len(plan)}")

if __name__ == "__main__":
    main()
