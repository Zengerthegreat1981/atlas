"""
يربط العقدَ المعزولة: كلُّ عقدةٍ لا يشير إليها أحدٌ لا يمكن الوصولُ إليها بالتنقّل.

**لماذا هذا خللٌ حقيقي:** واجهةُ الأطلس تُبني التنقّلَ من `related` و`edges`
**الصادرة** فقط (`shell_suffix.html`: بطاقاتُ الروابط، و`readNextFor`، وشرائح
`related`). ودالّةُ `relCountFor` تحسب الواردَ لكنها تُستعمل في **شارةِ عددٍ**
لا في تنقّل. فالعقدةُ المعزولة مكتوبةٌ ولا يبلغها القارئُ إلا ببحثٍ مباشر باسمها.

**قاعدةُ العمل: لا يُخترَع رابط.** كلُّ رابطٍ يُضاف هنا هو **عكسُ رابطٍ يؤكّده
المستودعُ أصلاً** — إمّا تأليفٌ مُصرَّحٌ به، أو انتماءٌ هرمي، أو رابطٌ صادرٌ من
المعزولة نفسِها يُجعَل ذا اتجاهين. وهذا احترازٌ من خلل الإقحام الذي عُولج في
`remove_spurious_related_links.py` و`remove_filler_authenticity_links.py`.

ترتيبُ اختيار الملفّ الذي سيستضيف الرابط (الأقوى تسويغاً أولاً):
  1. المؤلِّف المُصرَّح به (`author_slug` أو حرفُ تأليفٍ في `edges`)
  2. مفكِّرٌ يسمّيه slug المعزولة نفسُها (العَلَمُ الذي سُمّيت به)
  3. أبُ `belongs_to`
  4. أيُّ عقدةٍ يسمّيها الـslug
  5. مفكِّر من `related`
  6. بقيةُ أهداف `related`
ويُضاف مصدرٌ سابعٌ للمرشَّحين: **العَلَمُ الذي يسمّيه الـslug** ولو لم يكن مربوطاً
بعد — فملفُّ «صدور أصل الأنواع لداروين» كان لا يشير إلى `thk-darwin` أصلاً وإنما
إلى حدثين لا صلةَ لهما به. والـslug والعنوانُ كلاهما يسمّيان داروين، فالتسويغُ
من المستودع لا من عندي. وشروطُه ثلاثة، وكلُّها لازمة، ووُضعت بعد أن أنتجت الصيغةُ الأولى أخطاءً فاحشة:
  (أ) أن يكون اللقبُ **آخِرَ** كلمةٍ في حقل `en` بعد إسقاط ما بين قوسين — فحقل
      `en` يحمل أوصافاً بين قوسين («فيلسوف اللغة»، «مؤسس اليوغا») فكان الفهرسُ
      يلتقطها، فأُسند «فلسفة اللغة العادية» إلى **بهارتريهاري** و«الأشراق» إلى
      **باتانجالي**.
  (ب) أن تكون المطابقةُ **وحيدة** — فإن حمل اللقبَ أكثرُ من مفكِّرٍ أُسقِط، تحرُّزاً
      من فخّ اللقب المشترك (`stu-peterson-peterson` كان يُسند إلى **جوردان بيترسون**).
  (ج) **تأكيدٌ عبر الخطَّين**: أن يظهر جزءٌ من الاسم العربيِّ للمفكِّر في عنوان
      العقدة العربيِّ أيضاً. وهذا الشرطُ هو الذي يمنع أفحشَ الأخطاء: «أطروحات
      لوثر 1517» كانت تُسند إلى **مارتن لوثر كينغ**، و«الأليثيا» إلى **سوجورنر
      تروث** (لمطابقة truth)، و«خذ فاقرأ» عند أوغسطين إلى **إيكهارت تول**
      (لمطابقة tolle)، و«الآبائية اليونانية» إلى **كريستيان فولف**.
  (د) أن يكون اللقبُ **أوَّلَ** كلمةٍ في الـslug بعد بادئة النوع — فاصطلاحُ
      التسمية يضع العَلَمَ أوّلاً (`crt-hume-critique-of-miracles`). وبغير هذا
      الشرط كانت أسماءُ المدن تُقرأ ألقاباً: «إدانات باريس 1277» و«تأسيس جامعة
      باريس» و«انتفاضة مايو 1968 في باريس» أُسندت كلُّها إلى **جينيت باريس**،
      و«سقوط جدار برلين» إلى **فريد برلين**.
  (هـ) ألّا تكون العقدةُ المعزولةُ نفسُها مفكِّراً — فمفكِّرٌ لا يُستضاف عند
      مفكِّرٍ آخر بمصادفةٍ في الاسم: أُسند «أبو البركات البغدادي» إلى **حليم
      بركات**، و«أبو الحسن العامري» إلى **الأشعري**، و«جلال الدين الدواني» إلى
      **صادق جلال العظم**، و«وانغ فو تشي» إلى **وانغ بي**.
وفي الرتب الهرمية والتأليفية يُفضَّل الأقلُّ حمولةً (توزيعاً للعبء)، أمّا في
رتبة **التبادل** فيُفضَّل الأهدفُ **الأكثرُ مركزيةً** (الأعلى وروداً) — لأنّ
القارئ يتوقّع أن يجد ميشينباوم في صفحة بيك لا في صفحة زميلٍ مغمور؛ وجُرِّب
تفضيلُ الأقلِّ حمولةً فأسند ميشينباوم إلى «ستيفن هيغينز» وأسند «أصل الأنواع»
إلى «معيار يوروبسي 2001»، وهو إسنادٌ صحيحُ التسويغ رديءُ المنفعة.
وثمّة سقفٌ للإضافات في الملفّ الواحد — كي لا تتحوّل مدرسةٌ كبرى إلى جدارِ شرائح
(sch-psychoanalysis كان سيأخذ 109 روابط وحده).

**ما يُستثنى:** الملفاتُ المحجورة والإحالات (عنوانُها يحمل «حجر — انظر» أو
«إحالة»). عزلتُها مقصودة: هي مهجورةٌ تُشير إلى بديلها المعتمد، وربطُها يسوق
القارئَ إلى طريقٍ مسدود.

    python3 scripts/deorphan_links.py            # فحص
    python3 scripts/deorphan_links.py --apply
"""
import json, os, re, sys, collections, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAP = 12
AUTH_RELS = {"authored_by", "written_by", "developed_by", "formulated_by", "founded_by", "coined_by"}
STOP = {'and', 'the', 'of', 'vs', 'al'}

def safe_title(t):
    """يُبدِّل علامات التنصيص المزدوجة بعلامتي اقتباس عربيتين.

    محرِّكُ البناء يقرأ بند related بنمطٍ يتوقّف عند أوّل `"`، فالعنوانُ الذي يحمل
    `\"` داخله يُقطع فيُهمَل البندُ كلُّه بصمت — وهو الخللُ الذي يرصده
    `check_content_integrity.py`. وقع مرّةً مع عنوان «تحليل الدازاين … من
    \"الكينونة والزمن\" …» فأُضيف هذا التطهير.
    """
    t = (t or "").replace('\\"', '"')
    if '"' not in t: return t
    out = []; open_q = True
    for ch in t:
        if ch == '"':
            out.append('«' if open_q else '»'); open_q = not open_q
        else:
            out.append(ch)
    return ''.join(out)


def fold(s):
    s = (s or "")
    for a, b in [('œ','oe'), ('æ','ae'), ('ø','o'), ('ß','ss')]:
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()


def deprecated(n):
    t = n.get("title") or ""
    return ("حجر" in t and "انظر" in t) or ("إحالة" in t)

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p
    return None

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]

    inb = collections.defaultdict(set)  # يُستعمل للعزلة ولقياس المركزية
    for s, n in d.items():
        for r in n.get("related", []):
            if r[0] in d: inb[r[0]].add(s)
        for e in n.get("edges", []):
            if e[1] in d: inb[e[1]].add(s)

    orphans = [s for s in d if not inb[s] and not deprecated(d[s])]
    skipped = [s for s in d if not inb[s] and deprecated(d[s])]
    load = {s: len(d[s].get("related", [])) for s in d}
    added = collections.Counter()

    def toks(slug): return [t for t in slug.split("-")[1:] if len(t) > 3 and t not in STOP]

    # فهرسُ الألقاب: آخِرُ كلمةٍ في `en` بعد إسقاط ما بين قوسين، للعَلَم الوحيد فقط
    surname = collections.defaultdict(set)
    for k, v in d.items():
        if v.get("type") != "مفكر": continue
        en = re.sub(r'\(.*?\)', ' ', v.get("en") or '')
        parts = [t for t in re.split(r'[^a-z]+', fold(en)) if len(t) > 3
                 and t not in ('jr', 'sr', 'iii')]
        if parts: surname[parts[-1]].add(k)

    AR_D = re.compile(r'[\u064B-\u0652\u0670\u0640]')
    def arnorm(x):
        x = AR_D.sub('', x or '')
        for a, b in [('أ','ا'), ('إ','ا'), ('آ','ا'), ('ى','ي'), ('ة','ه')]:
            x = x.replace(a, b)
        return x

    def cross_script_ok(orphan_slug, thinker):
        """يشترط ظهورَ جزءٍ من اسم المفكِّر العربيِّ في عنوان العقدة العربيِّ."""
        ot = arnorm(d[orphan_slug].get("title"))
        for tok in arnorm(d[thinker].get("title")).replace('(', ' ').replace(')', ' ').split():
            if len(tok) >= 4 and tok in ot: return True
        return False

    def cands(s):
        n = d[s]; out = []; seen = set()
        def add(x, w):
            if x in d and x != s and not deprecated(d[x]) and x not in seen:
                seen.add(x); out.append((x, w))
        if n.get("author_slug"): add(n["author_slug"], "author")
        for e in n.get("edges", []):
            if e[0] in AUTH_RELS: add(e[1], "author")
        for e in n.get("edges", []):
            if e[0] == "belongs_to": add(e[1], "belongs_to")
        for e in n.get("edges", []): add(e[1], "edge")
        for r in n.get("related", []): add(r[0], "reciprocal")
        tk = toks(s)
        if tk and n.get("type") != "مفكر":
            who = surname.get(tk[0], set())
            if len(who) == 1:
                cand = next(iter(who))
                if cross_script_ok(s, cand): add(cand, "eponym")
        return out

    TYPE_PRI = {"مفكر": 0, "مدرسة": 1, "تيار": 2, "مفهوم": 3}

    def rank(s, cd):
        t, w = cd
        epo = any(tok in t for tok in toks(s))
        th = d[t].get("type") == "مفكر"
        if w == "author":      return (0, load[t], t)
        if w == "eponym":      return (1, load[t], t)
        if epo and th:         return (1, load[t], t)
        if w == "belongs_to":  return (2, load[t], t)
        if epo:                return (3, load[t], t)
        # تبادل: النوعُ الأصلحُ لاستضافة الرابط، ثم الأكثرُ مركزيةً (سالبُ الورود)
        return (4, TYPE_PRI.get(d[t].get("type"), 4), -len(inb[t]), t)

    plan = []; unplaced = []
    for s in sorted(orphans, key=lambda s: (len(cands(s)), s)):
        c = cands(s)
        if not c: unplaced.append(s); continue
        pool = [x for x in c if added[x[0]] < CAP] or c
        tgt, why = min(pool, key=lambda cd: rank(s, cd))
        plan.append((s, tgt, why)); load[tgt] += 1; added[tgt] += 1

    print(f"معزولة: {len(orphans)}   ستُربَط: {len(plan)}   بلا تسويغ: {len(unplaced)}"
          f"   مستثناة (محجورة/إحالة): {len(skipped)}")
    print("مصدرُ التسويغ:", dict(collections.Counter(w for _, _, w in plan)))
    after = sorted(load.values())
    print(f"طول related بعد: وسيط {after[len(after)//2]}، p90 {after[int(len(after)*.9)]}، أقصى {max(after)}")
    print("أكثرُ الملفات استضافةً:", [(t, c) for t, c in added.most_common(5)])

    if not apply:
        print("\n(فحصٌ فقط — أضف --apply للتنفيذ)")
        for s, t, w in plan[:20]:
            print(f"  [{w:11}] {s:44} -> {t}")
        return

    # group by host file
    byhost = collections.defaultdict(list)
    for s, t, w in plan: byhost[t].append((s, w))
    written = 0
    for host, items in byhost.items():
        p = find_file(host)
        if not p: print("!! not found", host); continue
        s = open(p, encoding="utf-8").read()
        m = re.search(r'^related:\n((?:- .*\n)*)', s, re.M)
        lines = []
        for slug, w in items:
            n = d[slug]
            if f'id: "{slug}"' in (m.group(1) if m else ""): continue
            lines.append(f'- id: "{slug}", title: "{safe_title(n.get("title"))}", '
                         f'type: "{n.get("type")}"\n')
        if not lines: continue
        if m:
            s = s[:m.end(1)] + "".join(lines) + s[m.end(1):]
        else:
            # no related block — insert before gaps: or before closing ---
            blk = "related:\n" + "".join(lines)
            if re.search(r'^gaps:$', s, re.M):
                s = re.sub(r'^gaps:$', blk + 'gaps:', s, count=1, flags=re.M)
            else:
                parts = s.split("---", 2)
                parts[1] = parts[1].rstrip("\n") + "\n" + blk
                s = "---".join(parts)
        note = ('  - "**رُبطت عقدٌ معزولة 2026-09-08:** أُضيفت هنا إشاراتٌ إلى '
                + str(len(lines)) + ' عقدةً كانت لا يشير إليها أيُّ ملفّ، فكانت غيرَ قابلةٍ '
                'للوصول بالتنقّل. وكلُّ إشارةٍ عكسُ علاقةٍ يؤكّدها المستودعُ أصلاً '
                '(تأليفٌ أو انتماءٌ أو رابطٌ صادرٌ منها)، لم تُخترَع واحدةٌ منها."')
        if re.search(r'^gaps:$', s, re.M):
            s = re.sub(r'^gaps:$', 'gaps:\n' + note, s, count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(s)
        written += 1
    print(f"\nعُدِّل {written} ملفاً مستضيفاً، وأُضيف {len(plan)} رابطاً.")
    print(f"بقيت {len(unplaced)} معزولةً بلا تسويغ — تُطبع للسجل:")
    for s in unplaced: print("   ", s, "|", (d[s].get("title") or "")[:56])

if __name__ == "__main__":
    main()
