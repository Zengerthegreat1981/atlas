"""
مراجعةٌ شاملةٌ لأنساب `belongs_to` في الأطلس، وإصلاحُ ما ثبت خطؤه.

فُحصت **كلُّ** أنساب المدارس والتيّارات (279 إعلاناً، 129 أباً مميَّزاً) لا
عناقيدَ منتقاة. والنتيجةُ أنّ أكثرَ الشجرة **سليمٌ ومُحكَم** — التحليلُ النفسي
بسبعةٍ وعشرين تياراً، وفيدانتا والكونفوشية الجديدة والمدرسية والمثالية الألمانية
والرواقية والأفلاطونية المحدثة كلُّها منتظمة. والخللُ في مواضعَ معدودةٍ بعينها:

## أ) أبٌ مهجور: 45 عقدة
`sch-cbt` و`br-transpersonal-psychology` صارا **إحالتين** إلى بديلَيهما
المعتمدَين في دفعةٍ سابقة، **ولم تُنقَل الأنسابُ الواردةُ إليهما**. فبقي 43
ملفاً يُعلن أباً له ملفَّ إحالةٍ لا مدرسةً — طريقٌ مسدود. وهذا نقصٌ في دمجٍ
سابقٍ من عملي، لا خللٌ موروث.

## ب) حرفُ انتماءٍ مكرَّرٌ حرفياً: ملفّان
`sch-andalusian-philosophy` و`dbt-humanistic-vs-existential` يُعلن كلٌّ منهما
أباه **مرّتين** في `edges`.

## ج) أنسابٌ خاطئةٌ بعينها: 13
وأوضحُها ما يُكذِّبه **متنُ الملفِّ نفسِه**:
  · `sch-kierkegaardian` مُدرَجٌ تحت **الهيغلية اليسارية**، ولِيدُه يقول إنّ
    «قوامَه **نقدُ النظام الهيغلي**». وعنوانُ الملفِّ نفسُه يسمّيه «الوجودية
    المبكرة الدينية» — فأُسند إلى `sch-existentialism`.
  · `br-alchemical-psychology` مُدرَجٌ تحت **علم النفس الإنساني**، ولِيدُه يقول
    «**فرعٌ في علم النفس الأركيتيبي** عند هيلمان» — فأُسند إلى `br-archetypal`.
  · `br-gestalt-berlin` («علم النفس الجشطالتي — مدرسة برلين») مُدرَجٌ تحت **علاج
    الجشطالت**. وعلمُ النفس الجشطالتي (فيرتهايمر وكوهلر، 1912) سبق علاجَ
    الجشطالت (1951) وأسهم فيه، وليس فرعاً منه — والخلطُ بينهما معروف.
  · `sch-ishraqiyya` مُدرَجٌ تحت **المشائية**، ولِيدُه يقول إنه «**يقابل** الحكمةَ
    البحثية (المشائية)» — أي أنه خصمُها لا فرعُها.
  · `sch-wahdat-alwujud` (عرفانُ ابن عربي) مُدرَجٌ تحت المشائية، وموضعُه
    `sch-islamic-sufism`.

    python3 scripts/fix_belongs_to_parentage_audit.py            # فحص
    python3 scripts/fix_belongs_to_parentage_audit.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 1) أبٌ مهجور -> بديلُه المعتمد
DEPRECATED = {
    "sch-cbt": "sch-cognitive-behavioral",
    "br-transpersonal-psychology": "sch-transpersonal",
}
# 2) حرفٌ مكرَّر: يُحذف الزائد
DEDUPE = ["sch-andalusian-philosophy", "dbt-humanistic-vs-existential"]
# 3) نسبٌ خاطئ -> (البديل أو None للتفريغ، السبب)
REPARENT = {
 "sch-kierkegaardian":   ("sch-existentialism", "لِيدُه: «قوامه نقد النظام الهيغلي»؛ وعنوانُه يسمّيه «الوجودية المبكرة الدينية». وإدراجُه تحت الهيغلية اليسارية عكسُ الحقيقة"),
 "br-alchemical-psychology": ("br-archetypal", "لِيدُه: «فرعٌ في علم النفس الأركيتيبي عند هيلمان» — لا في علم النفس الإنساني"),
 "sch-wahdat-alwujud":   ("sch-islamic-sufism", "عرفانُ ابن عربي تصوُّفٌ إسلاميّ لا فلسفةٌ مشائية"),
 "br-african-centered-psychology": ("sch-african-psychology", "للأطلس مدرسةٌ لعلم النفس الأفريقي، وهي موضعُه لا «الإنساني»"),
 "br-liberation-psychology": ("sch-liberation-psychology", "للأطلس مدرسةٌ لعلم نفس التحرر، وهي موضعُه"),
 "br-decolonizing-therapy": ("sch-liberation-psychology", "نزعُ استعمار العلاج في نسَب علم نفس التحرر لا «الإنساني»"),
 "br-sikolohiyang-pilipino": ("sch-indigenous-psychology", "علمُ النفس الفلبيني الأصيل من علم نفس الشعوب الأصلية"),
 "br-gestalt-berlin":    (None, "علمُ النفس الجشطالتي (برلين 1912) سبق علاجَ الجشطالت (1951) وأسهم فيه، وليس فرعاً منه. ولا ملفَّ مدرسةٍ لعلم النفس الجشطالتي في الأطلس"),
 "sch-ishraqiyya":       (None, "لِيدُه: «يقابل الحكمةَ البحثية (المشائية)» — خصمُها لا فرعُها. ولا مظلّةَ «فلسفةٍ إسلامية» في الأطلس تُنسب إليها"),
 "br-discursive-psychology": (None, "بوتر وويذرل: «ما بعد الاتّجاهات والسلوك» — تيّارٌ نقديٌّ خطابيّ لا إنسانيّ. ولا ملفَّ لـ«علم النفس النقدي» في الأطلس"),
 "sch-anarchism":        (None, "الأناركيةُ الكلاسيكية (برودون وباكونين وكروبوتكين) ليست فرعاً من الهيغلية اليسارية؛ وشتيرنر وحده كان من هيغليي الشباب"),
}
# 4) أبٌ نصّيٌّ زائدٌ لا يُحلّ، مع وجود أبٍ سليمٍ بجانبه
DROP_FREETEXT_PARENT = {"sch-indigenous-psychology": "علم النفس عبر الثقافي"}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def add_gap(t, note):
    return re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    for v in list(DEPRECATED.values()) + [v for v, _ in REPARENT.values() if v]:
        if v not in d: print("!! هدفٌ غير موجود:", v); return
    stats = collections.Counter()

    # ── 1) أبٌ مهجور
    for old, new in DEPRECATED.items():
        kids = [s for s, n in d.items()
                if any(e[0] == "belongs_to" and e[1] == old for e in n.get("edges", []))]
        for s in kids:
            p = find_file(s); t = open(p, encoding="utf-8").read()
            m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(old) + r'".*$', t, re.M)
            if not m: continue
            t = t[:m.start()] + f'- rel: "belongs_to", target: "{new}", target_type: "{d[new].get("type")}"' + t[m.end():]
            t = add_gap(t, '  - "**نُقل الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                        f'`{old}` — وهو **ملفُّ إحالةٍ** لا مدرسة (صار إحالةً في دفعة دمجٍ '
                        f'سابقة ولم تُنقَل الأنسابُ الواردةُ إليه)، فنُقل إلى البديل المعتمد `{new}`."')
            stats[f"أبٌ مهجور -> {new}"] += 1
            print(f"{'APPLY' if apply else 'DRY'}  [مهجور] {s:44} {old} -> {new}")
            if apply: open(p, "w", encoding="utf-8").write(t)

    # ── 2) حرفٌ مكرَّر
    for s in DEDUPE:
        p = find_file(s); t = open(p, encoding="utf-8").read()
        seen = set(); out = []
        for line in t.split("\n"):
            m = re.match(r'^- rel: "belongs_to", target: "([^"]+)"', line)
            if m:
                if m.group(1) in seen: stats["حرفٌ مكرَّر حُذف"] += 1; continue
                seen.add(m.group(1))
            out.append(line)
        t2 = "\n".join(out)
        t2 = add_gap(t2, '  - "**حُذف حرفُ انتماءٍ مكرَّر 2026-09-08:** كان `edges` يحمل '
                     'البندَ `belongs_to` نفسَه مرّتين حرفياً."')
        print(f"{'APPLY' if apply else 'DRY'}  [مكرَّر] {s}")
        if apply: open(p, "w", encoding="utf-8").write(t2)

    # ── 3) نسبٌ خاطئ
    for s, (new, why) in REPARENT.items():
        if s not in d: print("!! غير موجود:", s); continue
        cur = [e[1] for e in d[s].get("edges", []) if e[0] == "belongs_to"]
        if not cur: print(f"   {s}: بلا أبٍ بالفعل — يُترك"); continue
        p = find_file(s); t = open(p, encoding="utf-8").read()
        m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(cur[0]) + r'".*$', t, re.M)
        if not m: print(f"   !! شكلٌ غير متوقَّع: {s}"); continue
        if new:
            t = t[:m.start()] + f'- rel: "belongs_to", target: "{new}", target_type: "{d[new].get("type")}"' + t[m.end():]
            note = ('  - "**صُحِّح الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    f'`{cur[0]}`، ونُقل إلى `{new}` — ' + why + '."')
            stats[f"نُقل -> {new}"] += 1
        else:
            t = t[:m.start()] + t[m.end():]
            t = re.sub(r'\n\n+', '\n', t)
            if not re.search(r'^edges:\n- rel:', t, re.M):
                t = re.sub(r'^edges:\s*\n(?=related:|gaps:)', 'edges: []\n', t, count=1, flags=re.M)
            note = ('  - "**فُرِّغ حقلُ الانتماء 2026-09-08:** كان `belongs_to` يشير إلى '
                    f'`{cur[0]}` وهو نسبٌ خاطئ — ' + why + '. فبقي الحقلُ فارغاً؛ '
                    'ولم يُوضَع أبٌ تقريبيٌّ لأنّ أباً خاطئاً أسوأُ من غياب أب."')
            stats["فُرِّغ (نسبٌ خاطئ)"] += 1
        t = add_gap(t, note)
        print(f"{'APPLY' if apply else 'DRY'}  [نسب]   {s:44} {cur[0]} -> {new or '(فُرِّغ)'}")
        if apply: open(p, "w", encoding="utf-8").write(t)

    # ── 4) أبٌ نصّيٌّ زائد
    for s, txt in DROP_FREETEXT_PARENT.items():
        p = find_file(s); t = open(p, encoding="utf-8").read()
        m = re.search(r'^- rel: "belongs_to", target: "' + re.escape(txt) + r'".*$', t, re.M)
        if not m: continue
        t = t[:m.start()] + t[m.end():]
        t = re.sub(r'\n\n+', '\n', t)
        t = add_gap(t, '  - "**حُذف أبٌ نصّيٌّ زائد 2026-09-08:** كان الملفُّ يُعلن أبوَين، '
                    f'أحدُهما نصٌّ حرٌّ «{txt}» لا يُحلّ إلى ملفّ، والآخرُ slug سليم — '
                    'فحُذف النصُّ الحرُّ وبقي السليم."')
        stats["أبٌ نصّيٌّ زائد حُذف"] += 1
        print(f"{'APPLY' if apply else 'DRY'}  [نصّي]  {s} — حُذف «{txt}»")
        if apply: open(p, "w", encoding="utf-8").write(t)

    print("\n" + "="*56)
    for k, v in stats.most_common(): print(f"   {v:4}  {k}")
    print(f"   الإجمالي: {sum(stats.values())}")

if __name__ == "__main__":
    main()
