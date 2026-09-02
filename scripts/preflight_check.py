"""
فحص آلي (grep/regex — مش ذكاء) يشتغل على أي دفعة ملفات **قبل** ما MiniMax أو Spark
يكتب تقرير sub-task. الهدف: يمسك آلياً الأنماط اللي ظهرت بكثافة في تدقيق MiniMax
بتاريخ 2026-08-26 (راجع agents_specs/audit-findings-minimax-t1-t2.md وagents_specs/
quarantine-minimax.md) — مش عشان يستبدل المراجعة البشرية، عشان يمسك الأنماط الميكانيكية
البسيطة قبل ما توصل لمراجعة بشرية أصلاً، لأن القواعد المكتوبة في MINIMAX.md/SPARK.md
بتتنسى تحت حجم الشغل، والسكريبت مبينساش.

بيفحص 5 حاجات بس (كل واحدة منها نمط أخطاء حقيقي ظهر في التدقيق، مش تخمين):

1. روابط `related` بid وtitle متضاربين — بيفتح الملف اللي الـid بيشاور عليه فعلياً
   ويقارن العنوان المكتوب معاه بعنوان الملف الحقيقي (قاعدة MINIMAX/SPARK 6 وشرط القبول 4).
2. صيغة `related`/`edges` مكسورة (`title="..."` بعلامة = بدل `title: "..."`، أو صيغة
   متعددة الأسطر) — بتتسقط صامتة من غير الفحص ده (قاعدة 3).
3. عنوان قسم بجنس نحوي غلط (`## أهم أعمالها` لرجل ظاهر من صيغ الفعل في المتن، والعكس)
   (قاعدة 12).
4. سطر `gaps` بيؤكد حقيقة بدل ما يسمي فجوة ("...موثّق" / "...موثّقة" / "...موثّقتان" في
   آخر السطر) (شرط القبول 5).
5. سنة مذكورة في المتن أكبر من `active_end` المعلن في الـfrontmatter، من غير أي إشارة
   "بعد وفاته/بعد وفاتها" في نفس الجملة (قاعدة 5/شرط القبول الجديد).

الاستخدام:
  python3 scripts/preflight_check.py content/ar/thinkers/thk-foo.md content/ar/thinkers/thk-bar.md
  python3 scripts/preflight_check.py --report agents_specs/reports/minimax/T1/task-1.15.md
  python3 scripts/preflight_check.py --glob "content/ar/thinkers/thk-[m-z]*.md"

بيرجع exit code != 0 لو لقى أي مخالفة — استخدمه كـgate قبل ما تكتب تقرير الـsub-task،
مش بعده.
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
_real_argv = sys.argv
sys.argv = [sys.argv[0], "ar"]  # build_atlas.py بيقرأ sys.argv[1] كلغة وقت الـimport نفسه
from build_atlas import ATLAS_ROOT, parse_markdown  # noqa: E402
sys.argv = _real_argv

CONTENT_AR = os.path.join(ATLAS_ROOT, "content", "ar")

FEMININE_HEADERS = {
    "## أهم أعمالها": "## أهم أعماله",
    "## علاقتها بالمفاهيم والمدارس": "## علاقته بالمفاهيم والمدارس",
    "## موقعها من التيار": "## موقعه من التيار",
    "## شُبَكُها العلمية": "## شُبَكُه العلمية",
}
# شواهد نحوية بسيطة على جنس الشخص من نفس المتن — مش قاموس أسماء، مجرد صيغ فعل/ضمير شائعة
MALE_MARKERS = [r"\bهو\b", r"وُلد\b", r"توفي\b", r"عالم\b", r"مفكر\b", r"معالج\b", r"طبيب\b"]
FEMALE_MARKERS = [r"\bهي\b", r"وُلدت\b", r"توفيت\b", r"عالمة\b", r"مفكرة\b", r"معالجة\b", r"طبيبة\b"]

# القائمة السوداء الحرفية من MINIMAX.md وSPARK.md (نسخة مجمّعة، بلا تكرار) — preflight الأصلي
# ما كانش بيفحصها، وده سبب تكرار نفس الغلطة (جملة القائمة السوداء جوه gaps أو "## اقتباسات
# مختارة") في أكتر من دفعة مستقلة (2.16 minimax، وبطاقة 1.6 لاحقاً) قبل ما حد يمسكها يدوياً.
BLACKLIST_SENTENCES = [
    "لا يوجد اقتباس مباشر موثوق متاح",
    "يمثل هذا المفهوم لبنة تأسيسية",
    "حيث يوفر أداة دقيقة لتفسير قضايا الوجود والمعرفة",
    "شكل هذا المفهوم منطلقاً لحوارات ومقاربات نقدية متجددة",
    "حيث يقدم إطاراً تحليلياً لتفسير جوانب محددة",
    "حظي هذا المفهوم بمراجعات وتطويرات واسعة",
    "يمثل هذا التيار الفرعي تحولاً جوهرياً وتطويراً بنيوياً",
    "مسهماً في بلورة مفاهيمها وإشكالياتها الكبرى",
    "ترك هذا الفرع بصمات عميقة في تطور الفكر الفلسفي",
    "يقدم هذا الموقف رؤية نسقية تستند إلى براهين",
    "يقدم الطرف المقابل قراءة نقدية بديلة تكشف الثغرات",
    "يتناول هذا النقد تفكيك المسلمات النظرية",
    "مبيناً التناقضات الداخلية أو القصور الإبستمولوجي",
    "أحدث هذا النقد تحولاً منهجياً كبيراً",
    "يربط هذا الملف بين المفهوم الفلسفي التأسيسي واستعارته",
    "يمثل هذا الملف جسراً معرفياً",
    "انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية",
    "يقدم هذا العمل أطروحة فلسفية فارقة",
    "حظي الكتاب بدراسات وشروح وترجمات واسعة",
    "يمثل هذا العمل علامة فارقة في مجاله",
    "حيث صاغ مفهوماً جديداً أو قدم نسقاً برهانياً متميزاً",
    "شكل هذا الحدث منعطفاً حاسماً",
    "أعاد هذا الحدث تشكيل خريطة الأفكار",
]

CONFIRMED_GAP_SUFFIX_RE = re.compile(r"(موثّق|موثّقة|موثّقتان|موثّقون)\s*[\.\!]?\s*$")
BROKEN_RELATED_EQ_RE = re.compile(r'(?:id|title|type)\s*=\s*"')
YEAR_RE = re.compile(r"(?<!\d)(1[5-9]\d{2}|20\d{2})(?!\d)")
# يقبل «بعد وفاته/وفاتها» و«بعد وفاة <اسم>». الصيغة الأخيرة ضرورية: عندما يكون العمل لمؤلف
# آخر (أثر بعد الوفاة)، فإن «بعد وفاته» يعود نحوياً إلى أقرب مذكور — أي إلى المؤلف الحيّ لا إلى
# صاحب الملف — فتصير الجملة خاطئة. تسمية المتوفَّى صراحةً هي الصياغة الصحيحة، فيجب ألا يرفضها
# الفحص. (رُصد في thk-heidegger-technology بتاريخ 2026-09-02.)
POSTHUMOUS_HINT_RE = re.compile(r"بعد\s+وفا(?:ت|ة)")
# سنة داخل طابع زمني كامل بصيغة YYYY-MM-DD ليست سنة بيوغرافية: في هذا المشروع تُكتب السنوات
# البيوغرافية مجرّدة («عام 1949»)، أما الصيغة الكاملة فهي دائماً طابع إداري — تاريخ حجْر أو
# تدقيق، أو جزء من مسار أرشيف مثل
# `agents_specs/quarantine-minimax-archive/thk-x.md.archived.2026-08-26`.
# رُصد هذا في thk-jlubar (2026-09-02): الفحص أبلغ عن «2026» وهي طابع «حُجر 2026-08-26»
# ونفس الطابع داخل أربعة مسارات أرشيف — وأي إعادة صياغة كانت ستكسر المسارات نفسها.
_DATESTAMP_RE = re.compile(r"(?<!\d)(1[5-9]\d{2}|20\d{2})-\d{2}-\d{2}(?!\d)")


def _datestamp_spans(prose):
    return [(m.start(), m.end()) for m in _DATESTAMP_RE.finditer(prose)]


def resolve_path_for_slug(slug):
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "drafts"]
        fname = slug + ".md"
        if fname in files:
            return os.path.join(root, fname)
    return None


# تطبيع عربي خفيف قبل مقارنة العناوين: تشكيل، صور الألف والياء والتاء المربوطة، التطويل،
# والشروح بين قوسين وعلامات الترقيم. الغرض: أن يتوقّف الفحص عن الإبلاغ عن فروق **إملائية**
# بين عنوان مكتوب وعنوان حقيقي لنفس الكيان (مثل «نِكولاس» مقابل «نيكولاس»، أو شرح بين قوسين
# بلغة مختلفة) — وهي 81% من ضجيج هذا الفحص حسب تحليل 2026-09-02
# (agents_specs/reports/spark/REVISION/title-mismatch-analysis-2026-09-02.md).
# ما يبقى مُبلَّغاً عنه هو الاختلاف الحقيقي في الاسم، وهو وحده ما تقصده القاعدة 6.
_HARAKAT_RE = re.compile(r"[\u064B-\u0652\u0670]")
_PARENS_RE = re.compile(r"\([^)]*\)")
_PUNCT_RE = re.compile(r"[«»\"'\[\]،,\.\:\;\-\u2013\u2014\u2026/]")


def normalize_title(s):
    s = _HARAKAT_RE.sub("", s or "")
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"), ("ى", "ي"), ("ة", "ه"), ("ـ", "")):
        s = s.replace(a, b)
    s = _PARENS_RE.sub(" ", s)
    s = _PUNCT_RE.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def titles_conflict(written, real):
    """True فقط لو العنوانان مختلفان فعلاً بعد التطبيع — لا مجرد اختصار أو فرق إملائي."""
    w, r = (written or "").strip(), (real or "").strip()
    if not r or w == r or w in r or r in w:
        return False
    nw, nr = normalize_title(w), normalize_title(r)
    if not nw or not nr:
        return False
    return not (nw == nr or nw in nr or nr in nw)


def check_related_mismatch(node, file_path, issues):
    for rel_id, rel_title, _rel_type in node.get("related", []):
        target_path = resolve_path_for_slug(rel_id)
        if target_path is None:
            issues.append(f"related: id \"{rel_id}\" مش بيشاور لأي ملف موجود (title المكتوب: \"{rel_title}\")")
            continue
        target = parse_markdown(target_path)
        if not target:
            continue
        real_title = (target.get("title") or "").strip()
        if titles_conflict(rel_title, real_title):
            issues.append(
                f"related: id \"{rel_id}\" title المكتوب \"{rel_title}\" != عنوان الملف الحقيقي \"{real_title}\""
            )


def check_broken_yaml(raw_text, issues):
    for i, line in enumerate(raw_text.split("\n"), start=1):
        if BROKEN_RELATED_EQ_RE.search(line):
            issues.append(f"سطر {i}: صيغة YAML مكسورة (= بدل :) — \"{line.strip()}\"")


_ALL_SLUGS_CACHE = None


def _slug_exists_anywhere(slug):
    """هل للslug ملف فعلي؟ يشمل `drafts/` عن قصد: الربط بـslug في المسودات اعتماد بانتظار
    الترقية (106 حالة قائمة في المعتمد)، لا خطأ. المرفوض هو الاسم الذي لا ملف له إطلاقاً."""
    global _ALL_SLUGS_CACHE
    if _ALL_SLUGS_CACHE is None:
        _ALL_SLUGS_CACHE = set()
        for root, dirs, files in os.walk(CONTENT_AR):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for fn in files:
                if fn.endswith(".md"):
                    _ALL_SLUGS_CACHE.add(fn[:-3])
    return slug in _ALL_SLUGS_CACHE


EDGES_TARGET_RE = re.compile(r'target:\s*"([^"]+)"')
SLUG_SHAPE_RE = re.compile(r'^[a-z]{2,5}-[a-z0-9-]+$')


def check_edges_target(raw_text, issues):
    """edges.belongs_to.target لازم يكون slug حقيقي (con-x/sch-x/br-x/tec-x...) مش نص حر —
    نص حر إما يتسقط صامتاً (لو edges اتكتبت غلط بصيغة related) أو يفشل يشاور لملف حقيقي."""
    m = re.search(r'^edges:\n((?:- .*\n?)*)', raw_text, re.M)
    if not m:
        return
    for line in m.group(1).strip().split("\n"):
        tm = EDGES_TARGET_RE.search(line)
        if not tm:
            continue
        target = tm.group(1)
        if not SLUG_SHAPE_RE.match(target):
            issues.append(f'edges: target "{target}" مش شكله slug حقيقي (زي sch-x أو br-x) — يُحذف الرابط أو يُستبدل بslug موجود فعلاً، ما يُتركش نصاً حراً')
        elif not _slug_exists_anywhere(target):
            # فحص الوجود، لا الشكل فقط. قبل 2026-09-02 كان الفحص يتحقق من **شكل** الهدف وحده،
            # فيمرّ أي slug مكتوب صحيحاً لكن لا ملف له — رابط معلَّق صامت. القياس وقتها: 37 إشارة
            # إلى 26 slug غير موجود، وأكثرها أخطاء كتابة قريبة من slug حقيقي (br-aba مقابل
            # br-aba-autism، sch-developmental-psychology مقابل sch-developmental، br-feldenkrais
            # مقابل sch-feldenkrais). المسودات مقبولة كهدف: 106 ملفاً معتمداً يشاور على slugs في
            # المسودات بانتظار الترقية، وهو اصطلاح قائم لا خطأ.
            issues.append(f'edges: target "{target}" شكله slug صحيح لكن لا يوجد ملف بهذا الاسم في content/ar (رابط معلَّق) — صحّح الاسم أو احذف الرابط')


def check_gender_headers(raw_text, node, issues):
    # استبعاد الـfrontmatter: `type: "مفكر"` تصنيف ثابت مش وصف جندري، وبيلخبط العدّ
    # في كل ملف (شوهد متكرراً في مراجعات Task 2 دفعة 2.2 و2.3).
    body = _prose_body_only(raw_text)
    male_hits = sum(len(re.findall(p, body)) for p in MALE_MARKERS)
    female_hits = sum(len(re.findall(p, body)) for p in FEMALE_MARKERS)
    if male_hits == female_hits:
        return  # مش واضح كفاية، سيبه للمراجعة البشرية
    likely_male = male_hits > female_hits
    for fem_header, male_header in FEMININE_HEADERS.items():
        if fem_header in body and likely_male:
            issues.append(f'عنوان "{fem_header}" مؤنث لكن باقي المتن بصيغة مذكر (male_markers={male_hits}, female_markers={female_hits}) — المفروض "{male_header}"')


def check_gaps_confirming(node, issues):
    for gap in node.get("gaps", []):
        if CONFIRMED_GAP_SUFFIX_RE.search(gap.strip()):
            issues.append(f'gaps: سطر بيؤكد حقيقة بدل ما يسمي فجوة — "{gap}"')


def check_blacklist_sentences(raw_text, node, issues):
    for sentence in BLACKLIST_SENTENCES:
        if sentence in raw_text:
            issues.append(f'جملة من القائمة السوداء موجودة حرفياً في الملف (متن أو gaps): "{sentence}"')
    for gap in node.get("gaps", []):
        for sentence in BLACKLIST_SENTENCES:
            if sentence in gap:
                issues.append(f'gaps: جملة قائمة سوداء داخل gaps تحديداً — "{gap}"')
                break


def _prose_body_only(raw_text):
    """يشيل الـfrontmatter (بين --- و---) وقسم ## المصادر — عشان الفحص ما يلخبطش
    سنة نشر طبعة حديثة أو حقل dates البنيوي بحدث في حياة الشخص فعلاً."""
    parts = raw_text.split("---", 2)
    body = parts[2] if len(parts) >= 3 else raw_text
    body = re.split(r"^##\s*المصادر\s*$", body, maxsplit=1, flags=re.M)[0]
    return body


def check_dates_vs_body(node, raw_text, issues):
    # الفحص ده معناه فعلياً "بعد وفاة الشخص" — مالوش معنى لمؤسسة/حدث/قانون (زي إعادة تسمية
    # مجلة، أو تصديق معاهدة بعد سنين). لاحظه Spark أثناء Task 11 (events/) — كان بيطلب صيغة
    # "بعد وفاته" لكيانات مش أشخاص أصلاً. اتصلح 2026-08-27.
    if node.get("type") != "مفكر":
        return
    active_end = node.get("active_end")
    if not isinstance(active_end, int):
        return
    if active_end < 1500:
        # شخصيات قديمة/وسيطة — أي سنة حديثة في المتن غالباً تاريخ نشر مصدر أكاديمي حديث
        # (زي "طبعة 1903") مش حدث في حياة الشخص، فالفحص ده مش مفيد هنا.
        return
    prose = _prose_body_only(raw_text)
    _stamps = _datestamp_spans(prose)
    for m in YEAR_RE.finditer(prose):
        year = int(m.group(1))
        if year <= active_end:
            continue
        if any(s <= m.start() < e for s, e in _stamps):
            continue
        window = prose[max(0, m.start() - 30):m.start()]
        if POSTHUMOUS_HINT_RE.search(window):
            continue
        issues.append(f"سنة {year} مذكورة في المتن بعد active_end={active_end} من غير إشارة لِـ«بعد وفاته/وفاتها»")
        break  # سنة واحدة كفاية كإشارة، مش عايزين نغرق التقرير


def check_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    node = parse_markdown(file_path)
    issues = []
    if node is None:
        return [f"تعذّر تفسير الـfrontmatter (YAML مكسور بالكامل؟)"]
    check_related_mismatch(node, file_path, issues)
    check_broken_yaml(raw_text, issues)
    check_edges_target(raw_text, issues)
    check_gender_headers(raw_text, node, issues)
    check_gaps_confirming(node, issues)
    check_blacklist_sentences(raw_text, node, issues)
    check_dates_vs_body(node, raw_text, issues)
    return issues


def files_from_report(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        text = f.read()
    section = text.split("## الملفات", 1)
    if len(section) < 2:
        return []
    lines = section[1].strip().split("\n")
    return [ln.strip() for ln in lines if ln.strip().endswith(".md")]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="مسارات ملفات مباشرة")
    parser.add_argument("--report", help="مسار تقرير sub-task فيه قسم ## الملفات")
    parser.add_argument("--glob", help="نمط glob (بين علامتي تنصيص)")
    args = parser.parse_args()

    targets = list(args.files)
    if args.report:
        targets += files_from_report(args.report)
    if args.glob:
        targets += glob.glob(args.glob)

    if not targets:
        print("محتاج ملفات: مسارات مباشرة، أو --report تقرير sub-task، أو --glob نمط.")
        sys.exit(2)

    total_issues = 0
    for rel_path in targets:
        abs_path = rel_path if os.path.isabs(rel_path) else os.path.join(ATLAS_ROOT, rel_path)
        if not os.path.exists(abs_path):
            print(f"⚠️  {rel_path}: الملف مش موجود")
            continue
        issues = check_file(abs_path)
        if issues:
            total_issues += len(issues)
            print(f"\n❌ {rel_path}")
            for issue in issues:
                print(f"   - {issue}")

    print(f"\n{'='*60}")
    if total_issues:
        print(f"إجمالي المخالفات: {total_issues} — لا تكتب تقرير الـsub-task قبل ما تصلّحها.")
        sys.exit(1)
    print(f"✅ {len(targets)} ملف — صفر مخالفات آلية. (ده مش بديل عن المراجعة البشرية.)")
    sys.exit(0)


if __name__ == "__main__":
    main()
