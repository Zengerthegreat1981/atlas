"""
المرحلة 4-ب — إغلاقُ الطرق المسدودة، لا التبادلُ الشامل.

**مراجعةُ قرارٍ في الخطة.** كانت الخطةُ تقترح تبادلاً شاملاً: أن يُضاف كلُّ
ابنٍ في `belongs_to` إلى `related` أبيه (2,948 إضافة). والقياسُ الفعليُّ يُبطل
هذا: من 193 عقدةً معزولةً **تسعٌ فقط** لها أبٌ — أي أنّ التبادلَ الشاملَ
يُصلح تسعَ حالاتٍ ويُضيف 2,948 رابطاً، منها **404 روابطَ في صفحة التحليل
النفسي وحدها** و231 في CBT. والواجهةُ تعرض `related` رقائقَ تنقّلٍ متسلسلة،
فصفحةٌ بأربعمئة رقيقةٍ لا تُقرأ. فالتبادلُ الشاملُ **بلاءٌ لا دواء**، وتُرك
بقرارٍ مكتوب.

والمُصلَحُ هنا ما يُصلحه فعلاً:

  **(1) تسعُ عقدٍ معزولةٍ لها أبّ**: تُضاف إلى `related` أبيها فتصير قابلةً
      للوصول بالتنقّل — وهذا عكسُ علاقةٍ يؤكّدها المستودعُ أصلاً لا صلةٌ
      مُخترَعة.

  **(2) 117 مدرسةً/تيّاراً طريقاً مسدوداً**: من يهبط عليها لا يجد مخرجاً (أقلُّ
      من ثلاثة روابطَ ولا أعضاء). فتُربط بأبيها وبستّةٍ من أشقّائها على الأكثر
      — والأبُ والأشقّاءُ معلومون من شجرة الانتماء نفسِها، فلا اختراع.
"""
import os, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

MAX_SIB = 6


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    par = {s: e[1] for s, n in d.items() for e in n.get("edges", []) if e[0] == "belongs_to" and e[1] in d}
    kids = collections.defaultdict(list)
    for s, p in par.items():
        kids[p].append(s)
    inb = collections.Counter()
    for s, n in d.items():
        for r in n.get("related", []):
            inb[r[0]] += 1
        for e in n.get("edges", []):
            inb[e[1]] += 1

    def isred(s):
        n = d[s]
        return bool(n.get("redirect_to")) or n.get("status") == "quarantined" \
            or "إحالة" in (n.get("title") or "") or "حجر" in (n.get("title") or "")

    def item(s):
        return (s, (d[s].get("title") or "").replace('"', "'"), d[s]["type"])

    c = collections.Counter()

    # (1) معزولةٌ لها أبٌ → تُضاف إلى related أبيها
    iso = [s for s in d if not inb[s] and s in par and not isred(s)]
    byp = collections.defaultdict(list)
    for s in iso:
        byp[par[s]].append(s)
    for p, ch in byp.items():
        pp, t = E.load(p)
        cur = [tuple(r) for r in d[p]["related"]]
        new = [item(s) for s in ch if not any(r[0] == s for r in cur)]
        if not new:
            continue
        t2 = E.set_related(t, cur + new)
        if not t2:
            continue
        t2 = E.add_gap(t2, f"**رُبطت عقدٌ معزولة 2026-09-10:** أُضيفت إشارةٌ إلى "
                           f"{len(new)} عقدةً تُعلن الانتماءَ إلى هذا الملفّ في `belongs_to` "
                           f"ولا يشير إليها أيُّ ملفّ، فكانت غيرَ قابلةٍ للوصول بالتنقّل. "
                           f"وكلُّ إشارةٍ عكسُ علاقةٍ يؤكّدها المستودعُ أصلاً، لم تُخترَع واحدةٌ منها.") or t2
        E.save(pp, t2); c["iso"] += len(new)

    # (2) طرقٌ مسدودة → الأبُ والأشقّاء
    dead = [s for s in d if s.startswith(("sch-", "br-")) and len(d[s]["related"]) < 3
            and not kids[s] and not isred(s)]
    for s in dead:
        p = par.get(s)
        cur = [tuple(r) for r in d[s]["related"]]
        have = {r[0] for r in cur}
        add = []
        if p and p not in have and not isred(p):
            add.append(item(p))
            have.add(p)
        if p:
            sib = [x for x in sorted(kids[p], key=lambda y: -inb[y])
                   if x != s and x not in have and not isred(x)][:MAX_SIB]
            add += [item(x) for x in sib]
        if not add:
            c["dead_unfixable"] += 1
            continue
        pp, t = E.load(s)
        t2 = E.set_related(t, cur + add)
        if not t2:
            continue
        why = "أبوها" if p else ""
        t2 = E.add_gap(t2, f"**أُغلق طريقٌ مسدود 2026-09-10:** كان هذا الملفُّ بأقلَّ من ثلاثة "
                           f"روابطَ ولا أعضاءَ له، فمن يهبط عليه لا يجد مخرجاً. فأُضيف {len(add)} "
                           f"رابطاً إلى {why} وأشقّائه في شجرة الانتماء — وكلُّهم معلومون من الشجرة "
                           f"نفسِها، فلا صلةَ مُخترَعة.") or t2
        E.save(pp, t2); c["dead"] += 1

    print("النتيجة:", dict(c))
    print(f"(تُرك التبادلُ الشاملُ لـ2,948 رابطاً بقرارٍ مكتوب — انظر رأسَ هذا الملفّ)")


if __name__ == "__main__":
    main()
