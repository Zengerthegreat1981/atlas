"""
يربط ما بقي من العقد المعزولة التي **لا تسويغَ آليّ لها** — بخريطةٍ محقَّقةٍ يدوياً.

هذه الملفاتُ كان `related` فيها يحمل حشوَ `con-authenticity` وحده، فلمّا حُذف
الحشوُ (انظر `remove_filler_authenticity_links.py`) بقيت بلا رابطٍ صادرٍ ولا
وارد. و`deorphan_links.py` لا يبلغها لأنه لا يخترع تسويغاً من عنده.

فالخريطةُ أدناه **حكمٌ تحريريٌّ مني**، لا مُشتقّةٌ من المستودع — ولذلك:
  · اقتُصر على حالاتٍ العلاقةُ فيها بيّنةٌ لا تحتاج مرجعاً: أدواتٌ من العائلة
    نفسِها (وكسلر)، أو أداةٌ تُضمَّن في بطاريةٍ (ستروب وربطُ المسارات في D-KEFS)،
    أو دراستان في الموضوع نفسِه (بيريندا وكوستانزو مع تجربة آش للامتثال).
  · وتُرك ما لا يُبتّ فيه بهذه السهولة معزولاً مع تسجيله، ولم يُلفَّق له رابط.
كلُّ هدفٍ في الخريطة مُتحقَّقٌ من وجوده وقتَ الكتابة.

    python3 scripts/link_curated_orphans.py            # فحص
    python3 scripts/link_curated_orphans.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# المعزولة -> الملفُّ الذي يستضيف الإشارة إليها (سببُ الاستضافة في التعليق)
CURATED = {
    # عائلة وكسلر وبطاريات القدرات
    "ins-wms":                      ("ins-wais", "من عائلة مقاييس وكسلر نفسِها"),
    "ins-woodcock-johnson":         ("ins-wisc", "بطاريةُ قدراتٍ معرفيةٍ تُقارَن بمقاييس وكسلر للأطفال"),
    # ستروب وربطُ المسارات مُضمَّنان في بطارية D-KEFS
    "ins-stroop-color-word":        ("ins-dkefs-executive", "اختبارُ ستروب أحدُ اختبارات بطارية D-KEFS"),
    "ins-trail-making-test":        ("ins-dkefs-executive", "ربطُ المسارات أحدُ اختبارات بطارية D-KEFS"),
    # جرد الشخصية
    "ins-cattell-16pf":             ("ins-eysenck-epq", "استبيانا سماتٍ عامليّان من التقليد نفسِه"),
    "ins-hexaco":                   ("ins-neo-pi-r", "هيكساكو توسيعٌ لنموذج العوامل الخمسة الذي يقيسه NEO-PI-R"),
    # الاختبارات الإسقاطية بالرسم
    "ins-draw-a-person":            ("ins-house-tree-person", "اختبارا رسمٍ إسقاطيّان من العائلة نفسِها"),
    "ins-house-tree-person":        ("ins-rorschach", "اختبارٌ إسقاطيٌّ يُدرَس مع بقع رورشاخ"),
    # الرفاه وجودة الحياة
    "ins-ryff-psychological-wellbeing": ("ins-warwick-edinburgh-wellbeing", "مقياسا رفاهٍ نفسيٍّ إيجابي"),
    "ins-warwick-edinburgh-wellbeing":  ("ins-whoqol-bref", "مقياسا رفاهٍ وجودةِ حياة"),
    # التعلّق
    "ins-inventory-parent-peer-attachment": ("ins-ecr", "قياسُ التعلّق بأداةِ تقريرٍ ذاتيّ"),
    # الذاكرة
    "stu-scoville-milner-patient-hm":        ("con-memory", "الدراسةُ المؤسِّسةُ لتمييز أنظمة الذاكرة"),
    "stu-sperling-iconic-memory":            ("con-memory", "تجاربُ الذاكرة الأيقونية"),
    "stu-peterson-peterson-short-term-memory": ("con-memory", "تلاشي الذاكرة قصيرة المدى"),
    "stu-roediger-mcdermott-drm":            ("con-memory", "نموذجُ DRM للذاكرة الزائفة"),
    "stu-hyman-false-childhood-memories":    ("thk-elizabeth-loftus", "من خطِّ أبحاث الذكريات المزروعة الذي تقوده لوفتوس"),
    # الامتثال
    "stu-berenda-children-conformity":       ("stu-asch-conformity", "إعادةُ إجراء نموذج آش على الأطفال"),
    "stu-costanzo-shaw-conformity-age":      ("stu-asch-conformity", "مسارُ الامتثال بالعمر في نموذج آش"),
    # الإيحاء والتشخيص
    "stu-temerlin-diagnostic-bias-suggestion": ("stu-rosenhan-on-being-sane", "أثرُ الإيحاء في الحكم التشخيصي"),
    # الانتباه والإدراك البصري
    "stu-hubel-wiesel-visual-cortex":        ("con-neuroplasticity", "الفترةُ الحَرِجةُ وتشكُّلُ القشرة البصرية بالخبرة"),
    "stu-rosenzweig-enriched-environment":   ("con-neuroplasticity", "أثرُ البيئة الغنية في بنية الدماغ"),
    # التحيّز
    "stu-lord-ross-polarization":            ("con-confirmation-bias", "استقطابُ المواقف بالمعالجة المتحيّزة للبيّنة"),
    # هذه لم يبلغها `deorphan_links.py` لأنّ العَلَمَ فيها ليس أوّلَ كلمةٍ في الـslug
    # (`evt-burning-of-giordano-bruno-1600`)، وشرطُ الموضع لازمٌ هناك لمنع قراءة
    # أسماء المدن ألقاباً. والنسبةُ هنا بيّنةٌ من عنوان الحدث نفسِه.
    "evt-burning-of-averroes-books-cordoba-1195": ("thk-ibn-rushd", "محنةُ ابن رشد وإحراقُ كتبه"),
    "evt-burning-of-giordano-bruno-1600":         ("thk-giordano-bruno", "إعدامُ برونو نفسِه"),
    "evt-encyclopedie-publication-diderot-1751":  ("thk-diderot", "موسوعةُ ديدرو التي حرّرها"),
    "evt-council-of-nicaea-325":                  ("sch-patristics", "مجمعٌ مسكونيٌّ في عصر الآباء"),
    "evt-council-of-chalcedon-451":               ("sch-patristics", "مجمعٌ مسكونيٌّ في عصر الآباء"),
    "evt-closing-of-athens-schools-justinian-529": ("sch-neoplatonism", "إغلاقُ الأكاديمية أنهى الأفلاطونيةَ المحدثةَ الأثينية"),
    "evt-condemnations-of-1270-1277-paris":        ("sch-scholasticism", "إداناتُ باريس حدثٌ مفصليٌّ في المدرسانية"),
    "evt-bandung-conference-1955-decolonial":      ("sch-decolonial-philosophy", "مؤتمرُ باندونغ من محطّات الفكر الديكولونيالي"),
    "evt-decolonization-wave-africa-1960":         ("sch-decolonial-philosophy", "موجةُ استقلالِ أفريقيا 1960"),
    "evt-first-african-philosophy-conference-1970": ("sch-african-professional-philosophy", "أوّلُ مؤتمرٍ للفلسفة الأفريقية المهنية"),
    "evt-expulsion-of-jews-and-muslims-spain-1492": ("sch-andalusian-philosophy", "نهايةُ الحضور الأندلسي"),

    # ——— مفكِّرون بمتنٍ معتبَرٍ وبلا أيِّ بيانات علائقية ———
    "thk-ibn-hazm":        ("sch-andalusian-philosophy", "من أعلام الأندلس"),
    "thk-arthur-collier":  ("thk-berkeley", "المثاليةُ الذاتيةُ الإنجليزية بموازاة باركلي"),
    "thk-chaim-perelman":  ("sch-scholasticism", "إحياءُ البلاغة والحجاج في تقليدٍ مدرسانيٍّ لاحق"),
}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p
    return None

def safe_title(t):
    t = (t or "").replace('\\"', '"')
    if '"' not in t: return t
    out = []; op = True
    for ch in t:
        if ch == '"': out.append('«' if op else '»'); op = not op
        else: out.append(ch)
    return ''.join(out)

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    byhost = collections.defaultdict(list)
    bad = 0
    for orphan, (host, why) in CURATED.items():
        if orphan not in d: print(f"!! المعزولة غير موجودة: {orphan}"); bad += 1; continue
        if host not in d:   print(f"!! المستضيف غير موجود: {host}"); bad += 1; continue
        byhost[host].append((orphan, why))
    print(f"خريطةٌ محقَّقة: {len(CURATED)} عقدة -> {len(byhost)} ملفاً مستضيفاً؛ أخطاءٌ في الخريطة: {bad}")
    for host, items in sorted(byhost.items()):
        for o, why in items:
            print(f"  {'APPLY' if apply else 'DRY'}  {o:44} -> {host:32} ({why})")
    if not apply: 
        print("\n(فحصٌ فقط — أضف --apply للتنفيذ)"); return
    for host, items in byhost.items():
        p = find_file(host)
        if not p: continue
        s = open(p, encoding="utf-8").read()
        m = re.search(r'^related:\n((?:- .*\n)*)', s, re.M)
        blk = m.group(1) if m else ""
        lines = [f'- id: "{o}", title: "{safe_title(d[o].get("title"))}", type: "{d[o].get("type")}"\n'
                 for o, _ in items if f'id: "{o}"' not in blk]
        if not lines: continue
        if m: s = s[:m.end(1)] + "".join(lines) + s[m.end(1):]
        else:
            b = "related:\n" + "".join(lines)
            s = re.sub(r'^gaps:$', b + 'gaps:', s, count=1, flags=re.M)
        note = ('  - "**رُبطت عقدٌ معزولة 2026-09-08 بخريطةٍ محقَّقةٍ يدوياً:** '
                + "، ".join(f'`{o}` ({w})' for o, w in items)
                + '. وهذه الملفاتُ كان `related` فيها حشوَ «الأصالة» وحده فحُذف، فبقيت بلا '
                  'رابطٍ وارد؛ ولم يكن في المستودع تسويغٌ آليٌّ لربطها، فرُبطت بحكمٍ تحريريٍّ '
                  'مقصورٍ على العلاقات البيّنة."')
        s = re.sub(r'^gaps:$', 'gaps:\n' + note, s, count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(s)
    print(f"\nعُدِّل {len(byhost)} ملفاً، وأُضيف {sum(len(v) for v in byhost.values())} رابطاً.")

if __name__ == "__main__":
    main()
