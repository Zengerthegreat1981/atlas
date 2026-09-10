"""
المرحلة 3 — دمجُ العقد المكرَّرة.

القاعدةُ المتَّبعةُ هي قاعدةُ المستودع نفسُها (كما في
`merge_duplicate_relations.py`): **لا يُحذف ملفٌّ ولا يُعاد تسميةُ slug.** تُحفظ
النسخةُ الأصليةُ في `agents_specs/merge-archive-2026-09-10/`، ويصير الملفُّ
المدموجُ **إحالةً دائمة** تحفظ كلَّ رابطٍ واردٍ إليه — ثم تُعاد كتابةُ كلِّ
إشارةٍ واردةٍ في الأطلس لتشير إلى الباقي مباشرةً، فلا يمرُّ القارئُ بإحالةٍ إلا
إن جاء من خارج المستودع.

**اختيارُ الباقي:** الأغزرُ متناً. والسببُ أنّ الروابطَ الواردةَ كلَّها تُعاد
كتابتُها آلياً، فلا يترتّب على اختيار الـslug أيُّ كسرٍ — بينما فقدُ المتن
الأغزر لا يُستدرَك. وحيث كان الـslug الباقي مخالفاً لاسم صاحبه (`thk-ibrenner`
لتشارلز برينر مثلاً) سُجِّل ذلك فجوةً، ولم يُعَد التسميةُ عملاً بقاعدة المستودع.

**ما لم يُدمج، وهو أهمُّ من المدموج:** كشف الفحصُ الآليُّ 61 مجموعةً، وتسعَ
عشرةَ منها **ليست تكراراً** وكان دمجُها سيُفسد الأطلس:

  • `con-li` (禮، الطقسُ والأدب) و`con-li-principle-neoconfucian` (理، المبدأُ
    والنظامُ العقلاني) — **مفهومان صينيان مختلفان تماماً** يتصادفان في النقل
    اللاتيني «Li» وفي النقل العربي «اللي».
  • `con-jouissance` (اللذّةُ اللاكانيةُ المتجاوزةُ لمبدأ اللذة) و`con-pleasure`
    (اللذةُ بمعناها العامّ) — متضادّان في الاصطلاح لا مترادفان.
  • `con-anxiety` (قلقُ المدرسة الوجودية) و`con-anxiety-existential` (القلقُ
    المعرفيُّ العصبي) — والـslugs مضلّلةٌ هنا لأنّ الثاني هو **غيرُ** الوجودي،
    لكنّ العنوانَين يفرّقان، وإعادةُ التسمية ممنوعة.
  • `con-alienation` (الاغترابُ عامّةً) و`con-alienation-marxist-vs-existentialist`
    (مقارنةُ التقليدين) — عامٌّ ومقارَنة.
  • تسعةُ أزواجٍ من التقنيات بين CBT وDBT وACT (التقبّلُ الجذري، مسحُ الجسد،
    الأكلُ بيقظة…): التقنيةُ نفسُها تُدرَّس في كلِّ مدرسةٍ بصياغتها ووحدتها
    التدريبية الخاصّة، ومتونُها تختلف فعلاً وتنسب لكلٍّ أصلَه. فأُبقيت
    ورُبط كلُّ زوجٍ بشقيقه برابطٍ متبادلٍ يُبيّن الفرق — وهذا حكمٌ تحريريٌّ
    مُعلَنٌ لا إغفال.
"""
import os, re, sys, json, shutil, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

APPLY = "--apply" in sys.argv
DATE = "2026-09-10"
ARCH = os.path.join(E.ROOT, "agents_specs", f"merge-archive-{DATE}")

# ── المجموعاتُ المدموجة: (الملفّان) → مسوّغُ الدمج
MERGE = [
    (("thk-assagioli", "thk-robert-assagioli"), "ملفّان لروبرتو أساجيولي مؤسِّس التركيب النفسي (Psychosynthesis)."),
    (("thk-berne", "thk-eburne"), "ملفّان لإريك بيرن مؤسِّس تحليل المعاملات؛ والعنوانان متطابقان والتواريخُ نفسُها (1910–1970)."),
    (("thk-biko", "thk-jbiko"), "ملفّان لستيف بيكو، أحدُهما تحت الوجودية السوداء والآخرُ تحت علم نفس الأوبونتو."),
    (("thk-carnegie", "thk-dale-carnegie"), "ملفّان لديل كارنيجي."),
    (("thk-ibrenner", "thk-cbrenner"), "ملفّان لتشارلز برينر (Charles Brenner) بحقلِ `en` نفسِه."),
    (("thk-cmadanes", "thk-cloemadanes"), "ملفّان لكلوي مادانيس، أحدُهما تحت العلاج الأسري الاستراتيجي والآخرُ تحت علاج التبعية-السلطة."),
    (("thk-david-berceli", "thk-jboss"), "ملفّان لديفيد بيرسيلي واضعِ تمارين إطلاق الصدمة (TRE)؛ و`thk-jboss` **اسمُ slug لشخصٍ آخر** فمتنُه لبيرسيلي."),
    (("thk-jeberenz", "thk-dolweus"), "ملفّان لدان أولِس رائدِ بحوث التنمّر؛ و`thk-jeberenz` **اسمُ slug لشخصٍ آخر**."),
    (("thk-edith-stein", "thk-stein"), "ملفّان لإديث شتاين."),
    (("thk-paul-ekman", "thk-ekman"), "ملفّان لبول إيكمان."),
    (("thk-francine-shapiro", "thk-francesharville"), "ملفّان لفرانسين شابيرو واضعةِ EMDR — وعنوانُ أحدهما يقول صراحةً «ملف مكرّر»؛ و`thk-francesharville` **اسمُ slug لشخصٍ آخر**."),
    (("thk-roland-griffiths", "thk-griffiths"), "ملفّان لرولاند غريفيثز."),
    (("thk-harville-hendrix", "thk-hhendrix"), "ملفّان لهارفيل هندرِكس مؤسِّسِ علاج إيماغو."),
    (("thk-helen-lakelly-hunt", "thk-hlkelly"), "ملفّان لهيلين لاكيلي هانت المشاركةِ في تأسيس علاج إيماغو."),
    (("thk-ieyberg", "thk-seyberg"), "ملفّان لشيلا إيبِرغ واضعةِ PCIT."),
    (("thk-jluborsky", "thk-lluborsky"), "ملفّان لِلِستر لوبورسكي؛ و`thk-jluborsky` بحرفٍ أوّلَ خاطئ."),
    (("thk-mtrevi", "thk-jmertz"), "ملفّان لماريو تريفي — وفيهما **تاريخا وفاةٍ متناقضان** (2008 و2011)، وهو خلافٌ يُسجَّل فجوةً؛ و`thk-jmertz` **اسمُ slug لشخصٍ آخر**."),
    (("thk-leon-festinger", "thk-lfestinger"), "ملفّان لليون فستنغر صاحبِ التنافر المعرفي."),
    (("thk-lrice", "thk-rice"), "ملفّان للورا نورين رايس."),
    (("thk-msrosenberg", "thk-marshall-rosenberg"), "ملفّان لمارشال روزنبرغ واضعِ التواصل اللاعنفي."),
    (("thk-michael-yapko", "thk-michael-yapko-jr"), "ملفّان لمايكل يابكو؛ ولاحقةُ `-jr` لا سندَ لها."),
    (("thk-noam-chomsky", "thk-nchomsky"), "ملفّان لنعوم تشومسكي، أحدُهما تحت علم النفس المعرفي واللغوي والآخرُ تحت الفوضوية."),
    (("thk-plevine", "thk-peter-levine"), "ملفّان لبيتر ليفين واضعِ التجربة الجسدية."),
    (("thk-zoroaster", "thk-zarathushtra"), "ملفّان لزرادشت — وفيهما **تأريخان متباعدان** (1000 و1500 ق.م) يعكسان خلافاً حقيقياً في تأريخه، يُسجَّل فجوةً."),
    # أعمال
    (("wrk-milgram-obedience-authority", "wrk-obedience-to-authority"), "ملفّان لكتاب ميلغرام *Obedience to Authority* (1974)."),
    (("wrk-phenomenology-perception-merleau-ponty", "wrk-phenomenology-of-perception-merleau-ponty"), "ملفّان لـ*فينومينولوجيا الإدراك* لميرلوبونتي (1945)."),
    (("wrk-philosophy-mirror-nature", "wrk-rorty-philosophy-and-mirror-of-nature"), "ملفّان لـ*الفلسفة ومرآة الطبيعة* لرورتي (1979)."),
    (("wrk-self-compassion-neff", "wrk-self-compassion"), "ملفّان لكتاب كريستين نف *Self-Compassion* (2011)."),
    # مفاهيم وأدوات
    (("ins-hamilton-hdrs", "ins-ham-d"), "ملفّان لمقياس هاملتون للاكتئاب (HAM-D / HDRS)."),
    (("con-window-of-tolerance-detailed", "con-window-of-tolerance"), "ملفّان لنافذة التحمل، والثاني عنوانُه «مفصَّل» صراحةً — أي أنه وُلد نسخةً موسَّعةً لا مفهوماً آخر."),
    (("con-ataraxia-epicurean", "con-ataraxia"), "ملفّان للأتاراكسيا (السكينة)."),
    (("con-ahimsa", "con-ahimsa-non-violence"), "ملفّان لأهيمسا (اللاإيذاء)."),
    (("con-ubuntu", "con-ubuntu-african-humanism"), "ملفّان للأوبونتو."),
    (("con-dao", "con-dao-the-way-concept"), "ملفّان للداو (道)."),
    (("con-maat", "con-maat-ethics"), "ملفّان لماعت المصرية."),
    (("con-substance-accident", "con-substance-and-accident"), "ملفّان للجوهر والعرض؛ والـslugان يختلفان بحرف عطفٍ واحد."),
    (("con-will-to-live-schopenhauer", "con-blind-will-to-life"), "ملفّان لإرادة الحياة عند شوبنهاور."),
]

# ── أزواجٌ **لا تُدمج** ويُربط كلٌّ بشقيقه برابطٍ متبادلٍ مُعلَّل
CROSSLINK = [
    (("tec-act-acc-radical-acceptance", "tec-dbt-dt-radical-acceptance"),
     "التقنيةُ نفسُها بصياغتَي مدرستين: وحدةُ «التقبل» في ACT ووحدةُ «تحمل الضغوط» في DBT."),
    (("tec-act-acc-self-compassion-exercises", "tec-cbt-emo-self-compassion-exercises"),
     "تمارينُ الرأفة بالذات بصياغتَي ACT وCBT."),
    (("tec-act-acc-willingness-vs-willfulness", "tec-dbt-dt-willingness-vs-willfulness"),
     "الاستعدادُ مقابل العناد بصياغتَي ACT وDBT."),
    (("tec-act-pres-body-scan", "tec-cbt-mind-body-scan"), "مسحُ الجسد بصياغتَي ACT وCBT."),
    (("tec-act-pres-mindful-eating", "tec-dbt-er-mindful-eating"), "الأكلُ بيقظةٍ بصياغتَي ACT وDBT."),
    (("tec-act-pres-urge-surfing", "tec-dbt-dt-urge-surfing"), "ركوبُ موجة الرغبة بصياغتَي ACT وDBT."),
    (("tec-act-sac-perspective-taking", "tec-cbt-int-perspective-taking"), "تبنّي منظورٍ مختلفٍ بصياغتَي ACT وCBT."),
    (("tec-cbt-int-self-validation", "tec-dbt-er-self-validation"), "التصديقُ الذاتيُّ بصياغتَي CBT وDBT."),
    (("thk-heidegger", "thk-heidegger-technology"),
     "`thk-heidegger-technology` ملفٌّ موضوعيٌّ عن هايدجر **فيلسوفاً للتكنولوجيا** (محاضرة "
     "*Die Frage nach der Technik*، 1953) لا ملفَّ شخصٍ ثانٍ — فلم يُدمج. والأصوبُ أن يكون "
     "مفهوماً (`con-`) لا مفكّراً، وهذا مُسجَّلٌ فجوةً لا مُصلَحٌ هنا لأنّ إعادةَ التسمية ممنوعة."),
]


# ── الباقي مُثبَّتٌ يدوياً حيث كان الأغزرُ متناً يحمل **slug اسمِ شخصٍ آخر** أو
#    عنواناً مؤقّتاً. فالـslug الخاطئ عيبٌ دائمٌ يتناسل، أمّا المتنُ الأغزر فلا
#    يُفقد: يُنقَل إلى الباقي نقلاً كاملاً (transplant) ولا يُترك في الأرشيف.
SURVIVOR = {
    "thk-biko": "الـslug الصحيحُ لستيف بيكو، وإليه أكثرُ الروابط الواردة",
    "thk-cbrenner": "«C» لتشارلز برينر — و`thk-ibrenner` بحرفٍ أوّلَ لا يطابق اسمَه",
    "thk-dolweus": "الـslug الصحيحُ لدان أولِس — و`thk-jeberenz` **اسمُ slug لشخصٍ آخر**",
    "thk-seyberg": "«S» لشيلا إيبِرغ — و`thk-ieyberg` بحرفٍ أوّلَ لا يطابق اسمَها",
    "thk-lluborsky": "«L» لِلِستر لوبورسكي — و`thk-jluborsky` بحرفٍ أوّلَ لا يطابق اسمَه",
    "thk-mtrevi": "الـslug الصحيحُ لماريو تريفي — و`thk-jmertz` **اسمُ slug لشخصٍ آخر**",
    "con-window-of-tolerance": "الـslug النظيفُ للمفهوم، وإليه أكثرُ الروابط — و«مفصَّل» في عنوان الآخر أثرُ عملٍ لا تمييزُ مفهوم",
    "con-ataraxia": "الأتاراكسيا مفهومٌ هلنستيٌّ مشترَكٌ بين الأبيقورية والشكّية والرواقية، فالـslug العامُّ أصحُّ من المقصور على مدرسةٍ واحدة",
}


def words(n):
    return len((n.get("lede") or "").split()) + sum(len(x[1].split()) for x in n.get("sections", []))


def split_doc(text):
    m = re.match(r'^(---\n.*?\n---\n)(.*)$', text, re.S)
    return m.group(1), m.group(2)


def transplant(keep_path, drop_path, keep_title):
    """ينقل متنَ المدموج (الأغزر) إلى الباقي، مع تصحيح عنوان H1 إلى عنوان الباقي."""
    kfm, _ = split_doc(open(keep_path, encoding="utf-8").read())
    _, dbody = split_doc(open(drop_path, encoding="utf-8").read())
    dbody = re.sub(r'^#\s+.*$', f'# {keep_title}', dbody.lstrip("\n"), count=1, flags=re.M)
    open(keep_path, "w", encoding="utf-8").write(kfm + "\n" + dbody.rstrip("\n") + "\n")


def field(fm, k, default='""'):
    m = re.search(rf'^{k}:\s*(.*)$', fm, re.M)
    return m.group(1) if m else default


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    inb = collections.Counter()
    for s, n in d.items():
        for r in n.get("related", []):
            inb[r[0]] += 1
        for e in n.get("edges", []):
            inb[e[1]] += 1

    plan = []
    for pair, why in MERGE:
        a, b = pair
        assert a in d and b in d, pair
        pin = [x for x in pair if x in SURVIVOR]
        if pin:
            keep = pin[0]; drop = b if keep == a else a
            why = why + f" والباقي `{keep}` تثبيتاً يدوياً: {SURVIVOR[keep]}."
        else:
            keep, drop = (a, b) if words(d[a]) >= words(d[b]) else (b, a)
        plan.append((keep, drop, why))

    print(f"{'الباقي':46} {'المدموج':44} متن  واردة  نقلُ متن")
    for keep, drop, _ in plan:
        tp = "نعم" if words(d[drop]) > words(d[keep]) else "—"
        print(f"{keep:46} {drop:44} {words(d[keep]):4}/{words(d[drop]):<4} {inb[keep]:3}/{inb[drop]:<3} {tp}")
    print(f"\n{len(plan)} مجموعةً للدمج · {len(CROSSLINK)} زوجاً يُربط ولا يُدمج")
    if not APPLY:
        print("\n(معاينة — أضِف --apply للتنفيذ)")
        return

    os.makedirs(ARCH, exist_ok=True)
    # 1) إعادةُ كتابةِ كلِّ إشارةٍ واردةٍ في المستودع: المدموج → الباقي
    ren = {drop: keep for keep, drop, _ in plan}
    changed = 0
    for path in E.all_files():
        t0 = open(path, encoding="utf-8").read()
        t = t0
        me = os.path.basename(path)[:-3]
        for drop, keep in ren.items():
            if drop not in t or me == drop:
                continue
            kt = (d[keep].get("title") or "").replace('"', "'")
            # related
            t = re.sub(r'-\s*id:\s*"' + re.escape(drop) + r'"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"([^"]*)"',
                       lambda m: f'- id: "{keep}", title: "{kt}", type: "{d[keep]["type"]}"', t)
            # edges
            t = re.sub(r'(rel:\s*"[^"]*"\s*,\s*)target:\s*"' + re.escape(drop) + r'"(\s*,\s*)target_type:\s*"[^"]*"',
                       lambda m: f'{m.group(1)}target: "{keep}"{m.group(2)}target_type: "{d[keep]["type"]}"', t)
        if t != t0:
            open(path, "w", encoding="utf-8").write(t)
            changed += 1
    print(f"أُعيدت كتابةُ الإشارات في {changed} ملفاً")

    # 2) إزالةُ التكرارِ والإشارةِ الذاتية الناتجَين عن إعادة الكتابة
    fixed = 0
    for path in E.all_files():
        t0 = open(path, encoding="utf-8").read()
        me = os.path.basename(path)[:-3]
        m = re.search(r'^related:\n((?:- .*\n)*)', t0, re.M)
        if not m:
            continue
        seen, out = set(), []
        for ln in m.group(1).rstrip("\n").split("\n"):
            i = re.search(r'id:\s*"([^"]*)"', ln)
            if not i or i.group(1) == me or i.group(1) in seen:
                continue
            seen.add(i.group(1)); out.append(ln)
        new = "related:\n" + ("\n".join(out) + "\n" if out else "")
        if new != m.group(0):
            open(path, "w", encoding="utf-8").write(t0[:m.start()] + (new if out else "related: []\n") + t0[m.end():])
            fixed += 1
    print(f"أُزيل التكرارُ/الإشارةُ الذاتيةُ في {fixed} ملفاً")

    # 2.5) نقلُ المتن الأغزر إلى الباقي حيث كان الباقي مُثبَّتاً يدوياً
    moved = []
    for keep, drop, _ in plan:
        if words(d[drop]) <= words(d[keep]):
            continue
        kp, dp = E.path_of(keep), E.path_of(drop)
        transplant(kp, dp, d[keep].get("title") or "")
        _, t = E.load(keep)
        t = E.add_gap(t, f"**نُقل المتنُ من المكرَّر 2026-09-10:** دُمج `{drop}` في هذا الملفّ، "
                         f"وكان متنُه أغزرَ ({words(d[drop])} كلمة مقابل {words(d[keep])}) — فنُقل متنُه "
                         f"إلى هنا كاملاً بدل أن يُفقد، لأنّ الباقيَ اختير بصحّة الـslug لا بغزارة المتن. "
                         f"وعنوانُ المتن (`# …`) عُدِّل إلى عنوان هذا الملفّ. والنسخةُ الأصليةُ محفوظةٌ في الأرشيف.") or t
        E.save(kp, t); moved.append(f"{drop} → {keep}")
    print(f"نُقل المتنُ الأغزر في {len(moved)} حالة: {', '.join(moved) if moved else '—'}")

    # 3) تحويلُ المدموج إلى إحالةٍ دائمة
    for keep, drop, why in plan:
        p = E.path_of(drop)
        raw = open(p, encoding="utf-8").read()
        fm = raw.split("---")[1]
        old_title = re.search(r'^title:\s*"(.*?)"', fm, re.M).group(1)
        kt = d[keep].get("title") or ""
        crumb0 = (d[drop].get("crumb") or "").split("←")[0].strip() or "الأطلس"
        shutil.copy(p, os.path.join(ARCH, f"{drop}.md.archived.{DATE}"))
        new = f'''---
slug: "{drop}"
id: {field(fm,'id')}
type: {field(fm,'type')}
level: {field(fm,'level','"متوسط"')}
part: {field(fm,'part')}
title: "{old_title} — إحالة، انظر {keep}"
en: "Merged — see {keep}"
crumb: "{crumb0} ← [إحالة]"
active_start: null
active_end: null
redirect_to: "{keep}"
edges: []
related:
- id: "{keep}", title: "{kt.replace(chr(34), chr(39))}", type: "{d[keep]['type']}"
gaps:
  - "**دُمج {DATE}:** كان في الأطلس ملفّان لهذا المدخل. مسوّغُ الدمج: {why} والباقي `{keep}` لأنّ متنَه أغزر ({words(d[keep])} كلمة مقابل {words(d[drop])})."
  - "الـslug باقٍ ولم يُحذف عملاً بقاعدة المستودع في عدم إعادة التسمية، فكلُّ رابطٍ واردٍ من خارج المستودع يصل إلى هذه الإحالة. وكلُّ إشاراتِ الأطلس الداخليةِ أُعيدت كتابتُها إلى `{keep}` مباشرةً. النسخةُ الأصلية في `agents_specs/merge-archive-{DATE}/{drop}.md.archived.{DATE}`."
---

# {old_title} — إحالة

**دُمج هذا الملف.** المعالجةُ الكاملةُ في `{keep}` — «{kt}».

{why}

## المصادر

التوثيقُ البيبليوغرافيُّ في الملفِّ المُحال إليه `{keep}`، لا في هذه الإحالة.
'''
        open(p, "w", encoding="utf-8").write(new)
    print(f"حُوِّل {len(plan)} ملفاً إلى إحالةٍ دائمة (والأصولُ محفوظةٌ في {os.path.relpath(ARCH, E.ROOT)})")

    # 4) الروابطُ المتبادلةُ للأزواج التي لا تُدمج
    n = 0
    for (a, b), why in CROSSLINK:
        for x, y in ((a, b), (b, a)):
            p, t = E.load(x)
            cur = [tuple(r) for r in d[x]["related"]]
            if any(r[0] == y for r in cur):
                continue
            t2 = E.set_related(t, cur + [(y, (d[y].get("title") or "").replace('"', "'"), d[y]["type"])])
            if t2:
                t2 = E.add_gap(t2, f"**رُبط بشقيقه 2026-09-10:** لم يُدمج مع `{y}` — {why} فأُضيف رابطٌ متبادلٌ ليرى القارئُ الصياغةَ الأخرى.") or t2
                E.save(p, t2); n += 1
    print(f"أُضيف {n} رابطاً متبادلاً بين أزواجٍ لم تُدمج")


if __name__ == "__main__":
    main()
