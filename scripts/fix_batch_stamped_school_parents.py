"""
يصحّح `belongs_to` في مدارسَ وُسمت بأبٍ خاطئٍ من ختمٍ قالبيّ — ثلاثةُ عناقيد.

هذا نفسُ خللِ `fix_existential_belongs_to.py` في موضعٍ آخر: دفعةٌ آليةٌ ختمت
حقلَ الانتماء بأبٍ واحدٍ لكلِّ ما يُشبهه موضوعياً، فأنتجت أبوّةً كاذبة.

## 1) حلقةُ فيينا أباً لسبعةَ عشرَ مدرسة
`br-logical-positivism-vienna-circle` مُعلَنٌ أباً لـ**أخلاقيات الفضيلة
النيوأرسطية** و**الكانطية الأخلاقية المعاصرة** و**النفعية المعاصرة**
و**التعاقدية** و**فلسفة الرياضيات** و**البراغماتية الجديدة** — ولا واحدةٌ منها
من حلقة فيينا. والوضعيةُ المنطقية مذهبٌ في المعنى والتحقّق، لا مظلّةٌ لكلِّ
ما كُتب بالإنجليزية بعدها. وأطرفُ ما في العنقود أنّ **`sch-vienna-circle`
نفسَها** تُعلن `br-logical-positivism-vienna-circle` أباً لها — أي مدرسةٌ تنتمي
إلى تيّارٍ يحمل اسمَها؛ وهذه حالةُ **ازدواجٍ** بين ملفَّين لموضوعٍ واحد لا
حالةُ انتماء، فتُركت للدمج ولم تُلمس هنا.

## 2) الفلسفةُ المقارنةُ أباً لأحدَ عشرَ مدرسة — ومنها نفسُها
`sch-comparative-philosophy` مُعلَنٌ أباً لأخلاقيات الذكاء الاصطناعي وفلسفة
الإعاقة وما بعد الإنسانية… **و`sch-comparative-philosophy` نفسِها.** وعقدةٌ
تنتمي إلى نفسِها حلقةٌ مغلقةٌ لا معنى لها بحال.

## 3) علمُ النفس الأفريقيُّ أباً لثلاثةَ عشرَ مدرسةً **فلسفية**
`sch-african-psychology` — وهي مدرسةٌ في **علم النفس** — مُعلَنةٌ أباً للزنوجة
وعموم أفريقيا والأفروبيسيميزم والإثنوفلسفة وأوبونتو. وهذه مدارسُ **فلسفية**،
وانتماؤها إلى مدرسةٍ نفسيةٍ خطأٌ في المقولة. والمظلّةُ الصحيحة — «الفلسفة
الأفريقية» — **لا ملفَّ لها في الأطلس**، وقد سُجِّل غيابُها في
`agents_specs/missing-schools.md` من قبل.

## القاعدة
كلُّ هذه المدارس **مدارسُ نِدٍّ أو مظلّاتٌ مستقلّة**، فيُفرَّغ حقلُها ويُسجَّل
السبب — على اصطلاح المستودع ولا يُوضَع أبٌ تقريبيّ.

    python3 scripts/fix_batch_stamped_school_parents.py            # فحص
    python3 scripts/fix_batch_stamped_school_parents.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CLUSTERS = {
 "br-logical-positivism-vienna-circle": (
   "الوضعيةُ المنطقية مذهبٌ في المعنى والتحقّق، لا مظلّةٌ للفلسفة التحليلية كلِّها",
   {"sch-vienna-circle"}),      # يُستثنى: حالةُ ازدواجٍ تُترك للدمج
 "sch-comparative-philosophy": (
   "الفلسفةُ المقارنةُ منهجٌ ومجالٌ مستقلّ، لا مظلّةٌ للفلسفات التطبيقية المعاصرة",
   set()),
 "sch-african-psychology": (
   "مدرسةٌ في علم النفس لا تصلح أباً لمدارسَ فلسفية؛ والمظلّةُ الصحيحة «الفلسفة الأفريقية» لا ملفَّ لها في الأطلس",
   set()),
}

# نقلٌ بدل تفريغ، حيث يُوجد أبٌ صحيحٌ في الأطلس
REPOINT = {
  "sch-black-existentialism": ("sch-existentialism",
    "الوجوديةُ السوداء صيغةٌ من الوجودية لا فرعٌ من علم النفس الأفريقي"),
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
    total = 0; skipped = []
    for parent, (why, keep) in CLUSTERS.items():
        # **مدارسُ فقط.** العنقودُ الأفريقيُّ يحوي مفكِّرين (منديلا، وايد نوبلز،
        # كوبي كامبون، نعيم أكبر) وانتماؤهم إلى «علم النفس الأفريقي» **صحيح** —
        # فهم علماءُ نفسٍ أفريقيون. الخطأُ في المدارس الفلسفية المُدرَجة تحتها لا فيهم.
        kids = [s for s, n in d.items()
                if n.get("type") == "مدرسة"
                and any(e[0] == "belongs_to" and e[1] == parent for e in n.get("edges", []))]
        print(f"\n=== {parent} — {len(kids)} تُعلنه أباً ===")
        for s in sorted(kids):
            if s in keep:
                skipped.append(s); print(f"   تُرك (ازدواج): {s}"); continue
            selfref = (s == parent)
            rep = REPOINT.get(s)
            p = find_file(s)
            if not p: print("   !! not found", s); continue
            t = open(p, encoding="utf-8").read()
            m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(parent) + r'".*$', t, re.M)
            if not m: print(f"   !! شكلٌ غير متوقَّع: {s}"); continue
            if rep:
                newline = f'- rel: "belongs_to", target: "{rep[0]}", target_type: "{d[rep[0]].get("type")}"'
                t2 = t[:m.start()] + newline + t[m.end():]
                note = ('  - "**صُحِّح الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                        + f'`{parent}` ختماً قالبياً، ونُقل إلى `{rep[0]}` — ' + rep[1] + '."')
                t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
                total += 1
                print(f"   {'APPLY' if apply else 'DRY'}  {s:40}  -> {rep[0]}")
                if apply: open(p, "w", encoding="utf-8").write(t2)
                continue
            t2 = t[:m.start()] + t[m.end():]
            t2 = re.sub(r'\n\n+', '\n', t2)
            if not re.search(r'^edges:\n- rel:', t2, re.M):
                t2 = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t2, count=1, flags=re.M)
            note = ('  - "**فُرِّغ حقلُ الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    + f'`{parent}` ختماً قالبياً — '
                    + ('و**العقدةُ كانت تُعلن نفسَها أباً لنفسِها**، وهي حلقةٌ مغلقةٌ لا معنى لها. '
                       if selfref else '')
                    + why + '. وهذه مدرسةُ نِدٍّ أو مظلّةٌ مستقلّة، فبقي الحقلُ فارغاً؛ '
                    'ولم يُوضَع أبٌ تقريبيٌّ لأنّ أباً خاطئاً أسوأُ من غياب أب."')
            t2 = re.sub(r'^gaps:$', 'gaps:\n' + note, t2, count=1, flags=re.M)
            total += 1
            print(f"   {'APPLY' if apply else 'DRY'}  {s:40}{'  ← كان يُعلن نفسَه أباً' if selfref else ''}")
            if apply: open(p, "w", encoding="utf-8").write(t2)
    print(f"\nفُرِّغ: {total}   تُرك للدمج: {skipped}")

if __name__ == "__main__":
    main()
