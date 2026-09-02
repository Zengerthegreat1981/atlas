# -*- coding: utf-8 -*-
"""
إعادة تطبيق تصحيحات تدقيق ملفات المفكرين (idempotent — يمكن تشغيله أكثر من مرة بأمان).

سبب وجوده: الشغل بيتم بالتوازي مع جلسات تانية بتكتب في نفس المجلد، وحصل إن تعديلات
اتلغت لما رجعت الملفات لآخر commit. السكريبت ده بيعيد تطبيق كل التصحيحات الميكانيكية
والنصية اللي اتعملت في التدقيق، فلو حصل revert تاني، شغّله تاني.

    python3 scripts/reapply_thinkers_audit.py            # فحص فقط (dry-run)
    python3 scripts/reapply_thinkers_audit.py --apply    # تطبيق فعلي
"""
import os, re, sys, glob, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AR   = os.path.join(ROOT, "content", "ar")
THK  = os.path.join(AR, "thinkers")
APPLY = "--apply" in sys.argv
changed = {}

def read(p):  return open(p, encoding="utf-8").read()
def write(p, t):
    if APPLY: open(p, "w", encoding="utf-8").write(t)

def note(fn, what):
    changed.setdefault(os.path.basename(fn), []).append(what)

# ---------------------------------------------------------------- canonical titles
TITLE = {}
for fn in glob.glob(os.path.join(AR, "*", "*.md")):
    if os.sep + "drafts" + os.sep in fn: continue
    m = re.search(r'^title: "(.*)"', read(fn), re.M)
    if m: TITLE[os.path.basename(fn)[:-3]] = m.group(1)

SLUGRE = r'(?:thk|sch|br|tec|con|wrk|dis|evt|ins|stu|rel|dbt|que|axm|crt|ctx)-[a-z0-9-]+'

# ---------------------------------------------------------------- mechanical passes
def pass_mechanical(fn, t):
    fm, sep, body = t.partition("\n---\n")
    if not sep: return t
    o_fm, o_body = fm, body

    # 1) raw slugs leaking into user-visible crumb / belongs_to targets
    def _crumb(m):
        s = m.group(1)
        return f'crumb: "{TITLE[s]}' if s in TITLE else m.group(0)
    fm = re.sub(r'^crumb: "(' + SLUGRE + r')', _crumb, fm, flags=re.M)
    def _target(m):
        s = m.group(1)
        return f'target: "{TITLE[s]}"' if s in TITLE else m.group(0)
    fm = re.sub(r'target: "(' + SLUGRE + r')"', _target, fm)

    # 2) date-field wording
    def _dates(m):
        v = m.group(1)
        v = v.replace("القرن العشرون", "القرن العشرين").replace("الواحد والعشرون", "الواحد والعشرين")
        if v.endswith("· present"): v = v[:-len("present")] + "معاصر"
        v = v.replace("–present", "–")
        return 'dates: "%s"' % v
    fm = re.sub(r'^dates: "([^"]*)"', _dates, fm, flags=re.M)

    # 3) null active_end silently dropped by the build parser
    fm = re.sub(r'^active_end: null\s*$', 'active_end: "مستمر"', fm, flags=re.M)

    # 3b) a bare duplicate `related:` line directly above the real one (parser keeps only
    #     the first block, silently dropping every link that follows)
    fm = re.sub(r'^related:\s*\nrelated:', 'related:', fm, flags=re.M)

    # 4) empty-list syntax -> house style
    fm = re.sub(r'^(related|edges|gaps): \[\]\s*$', r'\1:', fm, flags=re.M)

    # 5) hamza on تُوفِّي
    body = body.replace("تَوفِّي", "تُوفِّي").replace("تَوفّي", "تُوفّي")
    body = re.sub(r'(?<![ء-ي])توفِّي(?![ء-ي])', 'تُوفِّي', body)

    # 5b) spurious tatweel (ـ) wedged inside Arabic words — breaks names like
    #     هـال (Hull) / البوينـي (Bowen) / ريكـلين (Riklin) for search and screen readers
    prev = None
    while prev != fm:
        prev = fm; fm = re.sub(r'([ء-ي])ـ([ء-ي])', r'\1\2', fm)
    prev = None
    while prev != body:
        prev = body; body = re.sub(r'([ء-ي])ـ([ء-ي])', r'\1\2', body)

    # 5c) MST mistranslated as «العلاج متعدد الأجهزة» (multi-*device* therapy);
    #     the canonical branch title is «العلاج متعدد الأنظمة (MST)»
    fm = fm.replace("العلاج متعدد الأجهزة", "العلاج متعدد الأنظمة")
    body = body.replace("العلاج متعدد الأجهزة", "العلاج متعدد الأنظمة")
    body = body.replace("متعدد الأجهزة", "متعدد الأنظمة")
    # a school name accidentally doubled as "الاسم (الاسم)" by an earlier slug substitution
    fm = re.sub(r'^(crumb: "[^"\n]*?) \((?:ال)?([^()"\n]{4,40})\)(?= ←)',
                lambda m: m.group(1) if m.group(2).replace("ال","") in m.group(1) else m.group(0),
                fm, flags=re.M)

    # 5d) «كُثِّف بأنه…» — the verb means "was condensed"; every occurrence in the corpus
    #     is being used for "was criticised / was read as"
    body = body.replace("«كُثِّف» بوصفه", "قُرِئ بوصفه")
    body = re.sub(r'كُثِّفت?\s+أحياناً\s+بوصفه?ا?', 'قُرِئ أحياناً بوصفه', body)
    body = body.replace("كُثِّفت بأنها", "نُقِدت بأنها").replace("كُثِّفت بوصفها", "قُرِئت بوصفها")
    body = body.replace("كُثِّف بأنه", "نُقِد بأنه").replace("كُثِّف بوصفه", "قُرِئ بوصفه")

    # 6) Latin decade forms in Arabic prose
    DEC = {"00":"العقد الأول","10":"العقد الثاني","20":"العشرينيات","30":"الثلاثينيات",
           "40":"الأربعينيات","50":"الخمسينيات","60":"الستينيات","70":"السبعينيات",
           "80":"الثمانينيات","90":"التسعينيات"}
    CENT= {"15":"القرن السادس عشر","16":"القرن السابع عشر","17":"القرن الثامن عشر",
           "18":"القرن التاسع عشر","19":"القرن العشرين","20":"القرن الحادي والعشرين"}
    def _dec(m):
        y = m.group(1); c, d = y[:2], y[2:4]
        return f"{DEC[d]} من {CENT[c]}" if (c in CENT and d in DEC) else m.group(0)
    body = re.sub(r'(?<![A-Za-z0-9])(1[5-9]\d0|20[0-2]0)s(?![A-Za-z0-9])', _dec, body)

    if fm != o_fm:     note(fn, "frontmatter")
    if body != o_body: note(fn, "body")
    return fm + sep + body

# ---------------------------------------------------------------- gendered headings
FEM_LEDE = re.compile(r'^(?:عالِ?مة|عالمة|محلّ?لة|محلِّلة|مفكّ?رة|فيلسوفة|طبيبة|معالِ?جة|باحثة|'
                      r'أستاذة|ناقدة|كاتبة|مربّ?ية|أخصائية|اختصاصية|مدرّ?بة|مؤسِّ?سة|منظّ?رة|'
                      r'أنثروبولوجية|راهبة|شاعرة|ممرّ?ضة|مترجمة|سوسيولوجية|راقصة|ناشطة|طبيبة نفسية|'
                      r'أكاديمية|ممارِ?سة|مستشارة|محاضِ?رة|مُ?علِّ?مة|طالبة|قسّ?يسة|'
                      r'مربية|معلمة|مدربة|منظرة|مؤسسة|محللة|عالمة|رائدة|طبيبة أطفال|'
                      r'عالِ?مة نفس|مُحلّ?لة|منظِّ?مة|مؤرِّ?خة|مُربّ?ية|قابلة|فنانة|مصمِّ?مة)\b')
FEM_SUBS = [(r'^## ما أعطاه$','## ما أعطته'), (r'^## موقعه من التيار$','## موقعها من التيار'),
            (r'^## موقعه من هذا الأطلس$','## موقعها من هذا الأطلس'),
            (r'^## موقعه في الأطلس$','## موقعها في الأطلس'),
            (r'^## موقعه من الأطلس$','## موقعها من الأطلس'),
            (r'^## أهم أعماله$','## أهم أعمالها'), (r'^## أثره$','## أثرها'),
            (r'^## موقعه من المدرسة$','## موقعها من المدرسة'),
            (r'^## موقعه من هذه المدرسة$','## موقعها من هذه المدرسة'),
            (r'^## لماذا يُذكر هنا$','## لماذا تُذكر هنا'),
            (r'^## موقعه من الحقل$','## موقعها من الحقل'),
            (r'^## أعماله$','## أعمالها'), (r'^## أثره في الحقل$','## أثرها في الحقل'),
            (r'^## موقعه من التيارات الأخرى$','## موقعها من التيارات الأخرى'),
            (r'^## موقعه من التيارات$','## موقعها من التيارات'),
            (r'^## لماذا يُذكر هنا$','## لماذا تُذكر هنا'),
            (r'^## موقعه في الحقل$','## موقعها في الحقل')]
MALE_OVERRIDE = {"thk-csocarides","thk-jaustin","thk-lwittgenstein","thk-pfeyerabend",
                 "thk-pfreire","thk-greenberg-lisa"}
MASC_LEDE = re.compile(r'^(?:عالِ?م|محلّ?ل|محلِّل|مفكّ?ر|فيلسوف|طبيب|معالِ?ج|باحث|أستاذ|'
                       r'ناقد|كاتب|مربّ?ي|أخصائي|اختصاصي|مدرّ?ب|مؤسِّ?س|منظّ?ر|راهب|شاعر|'
                       r'مترجم|ناشط|مؤرِّ?خ|قسّ?يس|حاخام|أكاديمي|ممارِ?س|مستشار|فنان|موسيقي|مخرج)(?![ةه])')

# صيغ عنوان "ما أعطى" المكسورة نحوياً: 112 حالة عبر المجلد. الصيغة الصحيحة
# بتتحدّد من جنس الشخص كما يظهر في أول سطر بعد العنوان.
BROKEN_FEM = ["## ما أعطتها", "## ما أعطاها", "## ما أعطتاه", "## ما أعطاتها", "## ما أعطاته"]

# ------------------------------------------------ تنظيف مدخلات related المكررة داخل الملف
# ------------------------------------------------ آثار توليد مسرَّبة إلى النصّ الظاهر
# ------------------------------------------------ جنس صيغة الميلاد في حقل dates
def pass_dates_gender(fn, t):
    m = re.search(r'^# .*\n\n(.*)$', t, re.M)
    if not m: return t
    lede = m.group(1).lstrip('*_ ')
    o = t
    if FEM_LEDE.match(lede):
        t = re.sub(r'^(dates: ".*?)وُلد(?!ت)', r'\1وُلدت', t, flags=re.M)
        t = re.sub(r'^(dates: ".*?)مولود(?!ة)', r'\1مولودة', t, flags=re.M)
    elif MASC_LEDE.match(lede):
        t = re.sub(r'^(dates: ".*?)وُلدت', r'\1وُلد', t, flags=re.M)
        t = re.sub(r'^(dates: ".*?)مولودة', r'\1مولود', t, flags=re.M)
    if t != o: note(fn, "جنس صيغة الميلاد")
    return t

def pass_strip_artifacts(fn, t):
    o = t
    # أقواس فارغة خلّفها مولّد النصّ: "... والإداري ()."
    t = re.sub(r'\s*\(\s*\)', '', t)
    # مسافات متراكمة داخل السطر
    t = re.sub(r'(?<=\S)[ \t]{3,}(?=\S)', ' ', t)
    if t != o: note(fn, "أثر توليد")
    return t

def pass_dedupe_related(fn, t):
    o = t; seen = set(); out = []
    for line in t.split("\n"):
        m = re.match(r'\s*- id: "([^"]+)"', line)
        if m:
            if m.group(1) in seen: continue
            seen.add(m.group(1))
        out.append(line)
    t = "\n".join(out)
    if t != o: note(fn, "related مكرر")
    return t

# ------------------------------------------------ علامات تحرير مسرَّبة إلى عناوين ظاهرة
def pass_strip_edit_markers(fn, t):
    o = t
    t = re.sub(r'^(title: ".*?)\s*[–\-—]?\s*\((?:ال)?مُ?حسَّ?ن\)("?)$', r'\1\2', t, flags=re.M)
    t = re.sub(r'^(title: ".*?)\s*[–\-—]\s*(?:ال)?مُ?حسَّ?ن(")$', r'\1\2', t, flags=re.M)
    if t != o: note(fn, "علامة تحرير في العنوان")
    return t

def pass_heading_form(fn, t):
    o = t
    for bad in BROKEN_FEM:
        t = re.sub(r'^' + re.escape(bad) + r'$', '## ما أعطته', t, flags=re.M)
    t = re.sub(r'^## ما أعطه$', '## ما أعطاه', t, flags=re.M)
    if re.search(r'^## ما أعطت$', t, re.M):
        m = re.search(r'^# .*\n\n(.*)$', t, re.M)
        lede = m.group(1).lstrip('*_ ') if m else ''
        if FEM_LEDE.match(lede):
            t = re.sub(r'^## ما أعطت$', '## ما أعطته', t, flags=re.M)
        elif MASC_LEDE.match(lede):
            t = re.sub(r'^## ما أعطت$', '## ما أعطاه', t, flags=re.M)
        else:
            note(fn, "عنوان «ما أعطت» جنسه غير محسوم")
    if t != o: note(fn, "صيغة العنوان")
    return t

def pass_gender(fn, t):
    if os.path.basename(fn)[:-3] in MALE_OVERRIDE: return t
    m = re.search(r'^# .*\n\n(.*)$', t, re.M)
    if not m or not FEM_LEDE.match(m.group(1).lstrip('*_ ')): return t
    o = t
    for pat, rep in FEM_SUBS: t = re.sub(pat, rep, t, flags=re.M)
    if t != o: note(fn, "gendered headings")
    return t

# ---------------------------------------------------------------- targeted text fixes
TEXT_FIXES = json.load(open(os.path.join(os.path.dirname(__file__), "thinkers_audit_fixes.json"),
                            encoding="utf-8"))

# ---------------------------------------------------------------- school reclassification
SCHOOL = {
 **{s: "السلوكية (Behaviorism)" for s in [
   "thk-ipavlov","thk-thorndike","thk-jwatson","thk-clhull","thk-kspence","thk-ectolman",
   "thk-cferster","thk-fkeller","thk-rherrnstein","thk-mc-jones","thk-jwolpe","thk-heysenck",
   "thk-ilovaas","thk-nazrin","thk-sbijou","thk-mwolf","thk-trisley","thk-rfoxx",
   "thk-bjhopkins","thk-jbirnbrauer","thk-hjguilhardi","thk-m-amatos","thk-nsugiyama",
   "thk-rkerbauy","thk-tmoriyama","thk-acatania","thk-abandura","thk-jrotter","thk-wmischel",
   "thk-fskinner"]},
 "thk-dmeichenbaum": "المعرفية السلوكية",
 "thk-kgwilson": "العلاج بالقبول والالتزام (ACT)",
}
def pass_school(fn, t):
    slug = os.path.basename(fn)[:-3]
    if slug not in SCHOOL: return t
    o = t; school = SCHOOL[slug]
    t = re.sub(r'^(crumb: ")مدرسة التحليل النفسي(?= ←)', r'\1' + school, t, flags=re.M)
    t = re.sub(r'^(\s*- rel: "belongs_to", target: ")مدرسة التحليل النفسي(", target_type: "مدرسة")',
               r'\1' + school + r'\2', t, flags=re.M)
    if t != o: note(fn, "school reclassified")
    return t

# ---------------------------------------------------------------- active-period repairs
CAP = {"thk-angyal":1960,"thk-basaglia":1980,"thk-ellison":1994,"thk-fink":1975,"thk-flusser":1991,
 "thk-fondane":1944,"thk-fperls":1970,"thk-goldmann":1970,"thk-merleau-ponty":1961,"thk-muruwwa":1987,
 "thk-pareyson":1991,"thk-schutz":1959,"thk-stein":1942,"thk-tatossian":1995,"thk-zubiri":1983,
 "thk-arendt":1975,"thk-kafka":1924,"thk-pascal":1662,"thk-rousseau":1778,"thk-wright":1960}
LIFESPAN = {"thk-hammarskjold":(1905,1961),"thk-lequier":(1814,1862),"thk-lperls":(1905,1990),
 "thk-sullivan":(1892,1949),"thk-todes":(1924,1994),"thk-trub":(1889,1949),"thk-weil":(1909,1943)}
def pass_active(fn, t):
    slug = os.path.basename(fn)[:-3]; o = t
    if slug in CAP:
        m = re.search(r'^active_end: (\d+)$', t, re.M)
        if m and int(m.group(1)) > CAP[slug]:
            t = re.sub(r'^active_end: \d+$', f'active_end: {CAP[slug]}', t, flags=re.M)
    if slug in LIFESPAN and 'active_source:' not in t:
        b, d = LIFESPAN[slug]
        t = re.sub(r'^active_start: \d+$', f'active_start: {b}', t, flags=re.M)
        t = re.sub(r'^active_end: \d+$', f'active_end: {d}\nactive_source: "lifespan"', t, flags=re.M)
    if t != o: note(fn, "active period")
    return t

# ------------------------------------------------ active_end "مستمر" لأشخاص متوفَّين
# 182 ملفاً كانت بتقول إن فترة نشاط الشخص "مستمرة" بينما حقل dates في نفس الملف
# بيذكر سنة وفاته. سنة الوفاة بتتقرا من الملف نفسه، فالتصحيح ذاتي التحقق.
# قائمة يدوية للملفات اللي مالهاش حقل dates أصلاً (متوفّون معروفون).
DECEASED_NO_DATES = {
 "thk-albert-einstein": (1905, 1955), "thk-amos-tversky": (1969, 1996),
 "thk-galileo-galilei": (1589, 1642),  "thk-isaac-newton": (1665, 1727),
 "thk-leo-tolstoy": (1852, 1910),      "thk-rene-girard": (1961, 2015),
 "thk-richard-feynman": (1942, 1988),  "thk-stephen-jay-gould": (1965, 2002),
 "thk-vladimir-jankelevitch": (1933, 1985), "thk-nel-noddings": (1984, 2022),
}
_YRANGE = re.compile(r'(\d{3,4})\s*[–\-—]\s*(\d{3,4})')

def pass_active_end_deceased(fn, t):
    slug = os.path.basename(fn)[:-3]; o = t
    if not re.search(r'^active_end: "مستمر"$', t, re.M): return t
    death = start = None
    m_d = re.search(r'^dates: "(.*)"$', t, re.M)
    if m_d:
        m = _YRANGE.search(m_d.group(1))
        if m:
            b, d = int(m.group(1)), int(m.group(2))
            if b < d <= b + 110: death = d
    elif slug in DECEASED_NO_DATES:
        start, death = DECEASED_NO_DATES[slug]
    if death is None: return t
    t = re.sub(r'^active_end: "مستمر"$', f'active_end: {death}', t, flags=re.M)
    if start is not None:
        t = re.sub(r'^active_start: (null|"?\[DRAFT-UNKNOWN\]"?)$',
                   f'active_start: {start}', t, flags=re.M)
    if t != o: note(fn, "active_end للمتوفَّى")
    return t

# ---------------------------------------------------------------- related `type` repair
# مدخلات related كتير مكتوب فيها type: "مفكر" وهي بتشاور على تيار/مفهوم/تقنية،
# فبتتعرض في الشبكة كأنها أشخاص. النوع الصحيح بيتقرا من ملف الهدف نفسه.
NODETYPE = {}
for _fn in glob.glob(os.path.join(AR, "*", "*.md")):
    if os.sep + "drafts" + os.sep in _fn: continue
    _m = re.search(r'^type: "(.*)"', read(_fn), re.M)
    if _m: NODETYPE[os.path.basename(_fn)[:-3]] = _m.group(1)

def pass_related_type(fn, t):
    def _fix(m):
        tid, title, typ = m.group(1), m.group(2), m.group(3)
        real = NODETYPE.get(tid)
        if real and real != typ and not tid.startswith("thk-"):
            note(fn, "related type")
            return f'- id: "{tid}", title: "{title}", type: "{real}"'
        return m.group(0)
    return re.sub(r'- id: "([^"]+)", title: "([^"]*)", type: "([^"]*)"', _fix, t)

# ---------------------------------------------------------------- legacy slug remaps
# روابط قديمة بتشاور على slugs مش موجودة؛ البديل الصحيح موجود فعلاً بالاسم ده.
# دي بتتصلّح في كل المجلدات مش المفكرين بس، لأن نفس الروابط المكسورة موجودة في
# disorders/ و techniques/ و concepts/ كمان.
LEGACY = {
 "sch-cbt": "sch-cognitive-behavioral",
 "tec-cbt-emo-self-compassion-exercises": "tec-act-acc-self-compassion-exercises",
 "tec-dbt-dt-radical-acceptance": "tec-act-acc-radical-acceptance",
 "tec-cbt-mind-body-scan": "tec-act-pres-body-scan",
 "tec-dbt-dt-urge-surfing": "tec-act-pres-urge-surfing",
}
def fix_legacy_refs():
    n = 0
    # MST rendered «العلاج متعدد الأجهزة» (multi-*device*) outside thinkers/ too
    for fn in glob.glob(os.path.join(AR, "*", "*.md")) + glob.glob(os.path.join(AR, "drafts", "*", "*.md")):
        t2 = read(fn)
        n2 = t2.replace("متعدد الأجهزة", "متعدد الأنظمة")
        if n2 != t2: write(fn, n2); n += 1
    for fn in glob.glob(os.path.join(AR, "*", "*.md")) + glob.glob(os.path.join(AR, "drafts", "*", "*.md")):
        t = read(fn); o = t
        for old, new in LEGACY.items():
            if f'"{old}"' not in t: continue
            if new not in TITLE: continue
            t = re.sub(r'- id: "%s", title: "[^"]*", type: "([^"]*)"' % re.escape(old),
                       lambda m: f'- id: "{new}", title: "{TITLE[new]}", type: "{m.group(1)}"', t)
        if t != o:
            write(fn, t); n += 1
    return n

# ---------------------------------------------------------------- روابط مدارس مطبوعة آلياً
# 211 ملفاً تحمل نفس الثلاثة/الخمسة روابط المدرسية في رأس `related` بالترتيب نفسه —
# أثر توليد لا تنسيب. الحالات القاطعة هي المفكرون قبل 1850: لوقيبوس وميليسوس وهيباتيا
# وأسانغا مربوطون بـ«العلاج المعرفي السلوكي» و«التحليل النفسي»، وهي مدارس نشأت بعدهم
# بقرون أو بألفَي عام. تُحذف عنهم وحدهم؛ أما المعاصرون فيحتاجون قراراً تحريرياً.
STAMPED_SCHOOLS = ["sch-existential-therapy", "sch-humanistic", "sch-positive-psychology",
                   "sch-cognitive-behavioral", "sch-psychoanalysis"]
# الرواقيون والأبيقوريون استثناء: صلتهم بالعلاج المعرفي السلوكي موثَّقة ومقصودة.
STAMPED_KEEP = {"thk-epictetus", "thk-epicur", "thk-marcus-aurelius", "thk-seneca",
                "thk-stoics", "thk-zeno-citium", "thk-chrysippus"}
_QM = re.compile(r'^dates: "(.*)"', re.M)
def _death_year(fm):
    m = _QM.search(fm)
    if not m: return None
    s = m.group(1)
    if "ق.م" in s or "ق. م" in s: return -1
    ys = [int(x) for x in re.findall(r'\b(\d{3,4})\b', s)]
    return max(ys) if ys else None

def fix_stamped_school_links():
    n = 0
    for fn in sorted(glob.glob(os.path.join(THK, "thk-*.md"))):
        slug = os.path.basename(fn)[:-3]
        if slug in STAMPED_KEEP: continue
        t2 = o2 = read(fn)
        fm = t2.split("\n---\n")[0]
        present = [g for g in STAMPED_SCHOOLS if '- id: "%s"' % g in fm]
        if len(present) < 3: continue
        d = _death_year(fm)
        if d is None or d >= 1850: continue      # المعاصرون: قرار تحريري لا آلي
        # لا تُحذف مدرسةٌ هي مدرسة المفكّر نفسه
        own = re.search(r'belongs_to", target: "([^"]+)"', fm)
        own_t = own.group(1) if own else ""
        for g in present:
            m2 = re.search(r'^- id: "%s", title: "([^"]*)", type: "[^"]*"\n' % re.escape(g), t2, re.M)
            if not m2: continue
            if m2.group(1) and m2.group(1) in own_t: continue
            t2 = t2.replace(m2.group(0), "", 1)
        if t2 != o2:
            write(fn, t2); n += 1
    return n

# ---------------------------------------------------------------- corpus-wide name repairs
# أسماء أعلام تُرجمت بدل أن تُنقل صوتياً، فصارت كلمة عربية بلا معنى في موضعها.
# تُصلَّح في كل المجلدات لأن الاسم الخاطئ منتشر في related وفي المتن معاً.
GLOBAL_NAMES = {
 "ماري رئيس": "ماري مين",          # Mary Main — «Main» تُرجمت «رئيس»
 "الغشتالت": "الجشطالت",           # صيغة أقلّية (21) مقابل الصيغة السائدة (304)
 "علاج الغشتالت": "علاج الجشطالت",
}
# «Main» ظهرت أيضاً وحدها بلا الاسم الأول في ملفات التعلّق، فتُصلَّح فيها بحدود دقيقة
# (لا تُمَسّ «الرئيس/رئيسة/رئيسي» ولا «رئيس» مضافةً إلى مؤسسة).
MAIN_SCOPE = ["thinkers/thk-marymain.md", "thinkers/thk-fonagy.md",
              "branches/br-attachment-theory.md", "thinkers/thk-bowlby.md",
              "concepts/con-secure-attachment.md", "debates/dbt-attachment-stability.md"]
_MAIN_RE = re.compile(r'(?<![ء-ي])(و?)رئيس(?![ةي\u064b-\u0652ء-ي])')
def fix_main_bare():
    n = 0
    for rel in MAIN_SCOPE:
        p2 = os.path.join(AR, rel)
        if not os.path.exists(p2): continue
        t2 = o2 = read(p2)
        t2 = _MAIN_RE.sub(lambda m: m.group(1) + "مين", t2)
        if t2 != o2: write(p2, t2); n += 1
    return n

def fix_global_names():
    n = 0
    for fn in glob.glob(os.path.join(AR, "*", "*.md")) + glob.glob(os.path.join(AR, "drafts", "*", "*.md")):
        t2 = o2 = read(fn)
        for bad, good in GLOBAL_NAMES.items():
            t2 = t2.replace(bad, good)
        if t2 != o2: write(fn, t2); n += 1
    return n

# ---------------------------------------------------------------- cross-folder text fixes
# نفس فكرة thinkers_audit_fixes.json لكن لبقية المجلدات (concepts/ works/ critiques/ …).
# المفتاح: "المجلد/اسم-الملف.md".
_AFP = os.path.join(os.path.dirname(__file__), "atlas_audit_fixes.json")
ATLAS_FIXES = json.load(open(_AFP, encoding="utf-8")) if os.path.exists(_AFP) else {}
def fix_other_folders():
    n = 0
    for rel, subs in ATLAS_FIXES.items():
        p2 = os.path.join(AR, rel)
        if not os.path.exists(p2): continue
        t2 = o2 = read(p2)
        for a, b in subs:
            if not a or a == b: continue
            if a in b and b in t2: continue
            if a in t2: t2 = t2.replace(a, b, 1)
        if t2 != o2: write(p2, t2); n += 1
    return n

# ---------------------------------------------------------------- concept node-type repair
# عشرة ملفات في concepts/ مكتوب فيها type: "مفكر" فبتتعرض في الشبكة كأنها أشخاص.
CONCEPTS_MISTYPED = ["con-nature-deficit","con-complex-ptsd","con-integration-psychedelic",
 "con-harm-reduction","con-neurofeedback","con-shinrin-yoku","con-dissociation",
 "con-neuroplasticity-trauma","con-twelve-steps","con-psychedelic-experience"]
def fix_concept_types():
    n = 0
    for s in CONCEPTS_MISTYPED:
        p2 = os.path.join(AR, "concepts", s + ".md")
        if not os.path.exists(p2): continue
        t2 = read(p2)
        n2 = re.sub(r'^type: "مفكر"$', 'type: "مفهوم"', t2, flags=re.M)
        if n2 != t2: write(p2, n2); n += 1
    return n

# ---------------------------------------------------------------- run
for fn in sorted(glob.glob(os.path.join(THK, "thk-*.md"))):
    base = os.path.basename(fn)
    t = orig = read(fn)
    t = pass_mechanical(fn, t)
    t = pass_school(fn, t)
    t = pass_active(fn, t)
    t = pass_active_end_deceased(fn, t)
    t = pass_related_type(fn, t)
    t = pass_heading_form(fn, t)
    t = pass_strip_artifacts(fn, t)
    t = pass_dates_gender(fn, t)
    t = pass_dedupe_related(fn, t)
    t = pass_strip_edit_markers(fn, t)
    for a, b in TEXT_FIXES.get(base, []):
        # skip no-ops, and skip pairs already applied where the target is a
        # prefix/substring of its own replacement ("ما أعطت" -> "ما أعطته"):
        # re-running those would append the suffix again on every pass.
        if not a or a == b: continue
        if a in b and b in t: continue
        if a in t: t = t.replace(a, b, 1); note(fn, "text fix")
    # gender pass runs LAST: some text fixes change the lede's gender, and the
    # heading agreement must follow the corrected lede, not the original one.
    t = pass_gender(fn, t)
    if t != orig: write(fn, t)

n_stamped = fix_stamped_school_links()
if n_stamped: print(f"stamped school links removed from {n_stamped} pre-modern thinkers")
n_names = fix_global_names() + fix_main_bare()
if n_names: print(f"corpus-wide name repairs in {n_names} files")
n_other = fix_other_folders()
if n_other: print(f"cross-folder text fixes applied in {n_other} files")
n_ct = fix_concept_types()
if n_ct: print(f"concept node-types repaired in {n_ct} files")
n_legacy = fix_legacy_refs()
if n_legacy: print(f"legacy slug refs repaired in {n_legacy} files")
print(("APPLIED" if APPLY else "DRY RUN") + f" — {len(changed)} thinker files need/received changes")
for f in sorted(changed):
    print(f"  {f:34s} {', '.join(sorted(set(changed[f])))}")
if not APPLY:
    print("\nrun again with --apply to write the changes")
