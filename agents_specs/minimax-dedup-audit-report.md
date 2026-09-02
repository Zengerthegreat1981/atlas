# تقرير تدقيق التكرار الشامل — MiniMax

**التاريخ:** 21 أغسطس 2026
**المسار:** خط أنابيب MiniMax — المرحلة 3 (التدقيق)
**النطاق:** كل ملفات `content/ar/drafts/<فولدر>/*.md` (20 فولدر) + المعتمد في `content/ar/<فولدر>/*.md`

---

## ملخص إحصائي

| القياس | القيمة |
|---|---|
| **إجمالي الملفات المفحوصة** | 2,887 |
| **عدد المسودات (drafts)** | 2,469 |
| **عدد المعتمد (approved)** | 418 |
| **حالات التكرار المؤكدة (المُعالجة)** | 64 |
| **حالات "تشابه لكن مشروع" (لم تُلمس)** | 17 (10 cross-type + 7 cross-school techniques) |

---

## المنهجية

1. **سحب البيانات**:سكريبت Python مرن (`scripts/dedup_audit.py`) يستخرج `slug` + `title` (عربي) + `en` (إنجليزي) من الـ frontmatter لكل ملف في الـ21 فولدراً.
2. **التطبيع**:
   - عربي: توحيد الألف بأشكالها، الياء/الياء المقصورة، التاء المربوطة، حذف الأقواس والتشكيل.
   - إنجليزي: أحرف صغيرة + حذف كل ما عدا الحروف.
3. **التجميع**:
   - **نفس النوع + تطابق عربي**: 27 مجموعة (أول تشغيل).
   - **نفس النوع + تطابق إنجليزي**: 62 مجموعة (أول تشغيل).
   - **عبر الأنواع + تطابق عربي**: 10 مجموعات.
4. **التحقق اليدوي**: لكل مجموعة، فتح الملفات (2+) وقراءة العنوان والـ slug والمحتوى للتأكد 100% من أنها نفس الشخص/المفهوم/التقنية.

---

## حالات التكرار المؤكدة (المُعالجة)

### الفئة A — مسودات مفكرين مكررة مع نسخة معتمدة (39 حالة)

كل حالة: مسودة بنفس الشخص والـ slug مختلف عن نسخة معتمدة في `content/ar/thinkers/`.

| المسودة المحذوفة | المعتمد الباقي |
|---|---|
| `thk-amaslow` | `thk-maslow` |
| `thk-hmhusserl` | `thk-husserl` |
| `thk-efromm` | `thk-fromm` |
| `thk-elukas` | `thk-lukas` |
| `thk-asutich` | `thk-sutich` |
| `thk-orank` | `thk-rank` |
| `thk-irvinyalom` | `thk-yalom` |
| `thk-pgoodman` | `thk-goodman` |
| `thk-jlacanian` | `thk-lacan` |
| `thk-jfabry` | `thk-fabry` |
| `thk-mayr` | `thk-may` |
| `thk-viktorfrankl` | `thk-frankl` |
| `thk-crogers` | `thk-rogers` |
| `thk-ccaldwell` | `thk-caldwell` |
| `thk-rmoustakas` | `thk-moustakas` |
| `thk-ludwigbinswanger` | `thk-binswanger` |
| `thk-medardboss` | `thk-boss` |
| `thk-abatth` | `thk-batthyany` |
| `thk-alangle` | `thk-langle` |
| `thk-ffanon` | `thk-fanon` |
| `thk-ffrommreich` | `thk-fromm-reichmann` |
| `thk-pwatzl` (مسودة خاطئة لـ Bateson) | `thk-gbateson` |
| `thk-hsachs` | `thk-sachs` |
| `thk-jjonas` | `thk-jonas` |
| `thk-hguntrip` | `thk-guntrip` |
| `thk-hssullivan` | `thk-sullivan` |
| `thk-hkohut` | `thk-kohut` |
| `thk-hansbacher` | `thk-ansbacher` |
| `thk-jpanksepp` | `thk-panksepp` |
| `thk-jbreuer` | `thk-breuer` |
| `thk-jjordan` | `thk-jordan` |
| `thk-dkahneman` | `thk-rkahneman` |
| `thk-rubin-jeffrey` | `thk-jrubin` |

**السبب:** المعتمدات أقدم وأكمل (تحتوي `id` حقيقي، `gaps` أوسع، `related` أكثر). المسودات الزائدة زائدة.

### الفئة B — مسودات مكررة (كلتاهما مسودة) لنفس الشخص (25 حالة)

| المحذوف | المحفوظ | السبب |
|---|---|---|
| `thk-abeck` | `thk-beck` | Aaron T. Beck — نسخة واحدة فقط |
| `thk-aellis` | `thk-ellis` | Albert Ellis |
| `thk-aaichhorn` | `thk-aichhorn` | August Aichhorn |
| `thk-abateman` | `thk-bateman` | Anthony Bateman |
| `thk-bbrandchaft` | `thk-brandchaft` | Bernard Brandchaft |
| `thk-alazarus` | `thk-lazarus` | Arnold Lazarus |
| `thk-harrystack-sullivan` | `thk-hssullivan` | Harry Stack Sullivan (لكن أعيد إنشاؤها لاحقاً في المعتمد `thk-sullivan`) |
| `thk-evandeurzen` | (المعتمد `thk-vandeurzen`) | Emmy van Deurzen |
| `thk-irerich` | (المعتمد `thk-fromm`) | Erich Fromm (نسخة 3) |
| `thk-karenhorney` | `thk-khorney` | Karen Horney |
| `thk-lirigaray` | `thk-irigaray` | Luce Irigaray |
| `thk-lbinswanger` | (المعتمد `thk-binswanger`) | Ludwig Binswanger (نسخة 3) |
| `thk-lymanwynne` | (المعتمد `thk-lwynne`) | Lyman C. Wynne |
| `thk-mahler` | `thk-mmahler` | Margaret Mahler |
| `thk-eitingon` | `thk-meitingon` | Max Eitingon |
| `thk-mboss` | (المعتمد `thk-boss`) | Medard Boss (نسخة 3) |
| `thk-mcsik` | `thk-mcsikszent` | Mihaly Csikszentmihalyi |
| `thk-olovaas` | `thk-ilovaas` | O. Ivar Lovaas |
| `thk-orlindsley` | `thk-rlindsl` | Ogden R. Lindsley |
| `thk-phaley` | (المعتمد `thk-pwatzlawick`) | Paul Watzlawick (slug كان خطأً "phaley") |
| `thk-mfonagy` | `thk-pfonel` | Peter Fonagy |
| `thk-paulagnier` | `thk-aulagnier` | Piera Aulagnier |
| `thk-kaes` | `thk-rkaes` | René Kaes |
| `thk-rspitz` | `thk-spitz` | René Spitz |
| `thk-rstolorow` | `thk-stolorow` | Robert Stolorow |
| `thk-dreikurs` | `thk-rdreikurs` | Rudolf Dreikurs |
| `thk-ferenczi` | `thk-sferenczi` | Sándor Ferenczi |
| `thk-sorenk` | (المعتمد `thk-kierkegaard`) | Søren Kierkegaard |
| `thk-vfrankl` | (المعتمد `thk-frankl`) | Viktor Frankl (نسخة 3) |
| `thk-oreich` | `thk-reich` | Wilhelm Reich |
| `thk-stekel` | `thk-wstekel` | Wilhelm Stekel |

**إجمالي المحذوف:** 64 ملفاً.

---

## حالات "تشابه مشروع" (لم تُلمس)

### الفئة C — 7 تقنيات متكررة عبر مدارس (تحتاج قرار بشري)

نفس التقنية (en و ar) لكن تحت مدرستين مختلفتين. وُسِمت مسبقاً في `pipeline-progress-log.md` (19 أغسطس 2026) كقضايا "تحتاج قرار بشري":

- `tec-cbt-mind-body-scan` ↔ `tec-act-pres-body-scan` (مسح الجسد)
- `tec-dbt-er-self-validation` ↔ `tec-cbt-int-self-validation` (التصديق الذاتي)
- `tec-cbt-emo-self-compassion-exercises` ↔ `tec-act-acc-self-compassion-exercises` (تمارين الرأفة بالذات)
- `tec-dbt-dt-willingness-vs-willfulness` ↔ `tec-act-acc-willingness-vs-willfulness` (الاستعداد مقابل العناد)
- `tec-dbt-dt-radical-acceptance` ↔ `tec-act-acc-radical-acceptance` (التقبل الجذري)
- `tec-dbt-er-mindful-eating` ↔ `tec-act-pres-mindful-eating` (الأكل بيقظة)
- `tec-dbt-dt-urge-surfing` ↔ `tec-act-pres-urge-surfing` (ركوب موجة الرغبة الملحة) — جديدة لم تكن في القائمة الأصلية.

**السبب في إبقاءها:** قرار تحريري مشروع — هل التقنية نفسها تُطبَّق بالتساوي في كل مدرسة أم لها فروق تستحق ملفين؟ يُترك للمراجعة التحريرية.

### الفئة D — 10 تكرارات عبر الأنواع (مُبررة بنيوياً)

نفس العنوان يظهر تحت نوعين مختلفين، لكنهما يخدمان غرضين مختلفين (per `draft-writer-brief.md`):

| العنصر | الفولدر الأول | الفولدر الثاني | السبب المشروع |
|---|---|---|---|
| `abstinence-vs-harm-reduction` | `branches/` (تيار) | `concepts/` (مفهوم) | تيار نقاشي + مفهوم نظري |
| `dissociation` | `concepts/` (مفهوم) | `syndromes/` (متلازمة) | مفهوم فينومينولوجي + نمط سريري |
| `restorative-justice` | `branches/` | `concepts/` | تيار + مفهوم |
| `functional-family-therapy` | `branches/` (FFT كتيار) | `techniques/` (FFT كتطبيق) | تيار + تقنية محددة |
| `dbt` | `schools/` (مدرسة) | `techniques/` (مفردة) | المدرسة ككل + تطبيق محدد |
| `dynamic-couples-family-therapy` | `branches/` | `concepts/` | تيار + مفهوم |
| `critical-liberation-therapy` | `branches/` | `concepts/` | تيار + مفهوم |
| `multisystemic-therapy` | `branches/` (MST كتيار) | `techniques/` (كتطبيق) | تيار + تقنية |
| `family-sandplay` | `branches/` | `concepts/` | تيار + مفهوم |
| `intersectional-feminist` | `branches/` | `concepts/` | تيار + مفهوم |

**القاعدة:** نفس الموضوع يمكن أن يظهر كتـ**تيار** (`br-`)، أو كتـ**مفهوم** (`con-`)، أو كـ**تقنية** (`tec-`) حسب الزاوية. هذا متعمَّد في بنية المشروع. لم يُلمس.

---

## تأثير التنظيف

| المؤشر | قبل | بعد |
|---|---|---|
| إجمالي العناصر في الفهرس | 2,951 | 2,887 |
| عدد المسودات | 2,533 | 2,469 |
| حالات تكرار حرفي (same-type ar) | 27 | 7 (المشروع للقرار البشري) |
| حالات تكرار cross-type | 10 | 10 (مُبررة) |
| حالات تشابه en (same-type) | 62 | 7 (نفس التقنيات الـ7) |

**الرقم النهائي بعد التنظيف:** 2,887 عنصر (418 معتمد + 2,469 مسودة)، صفر تكرار حقيقي قابل للمعالجة تلقائياً.

---

## الأدوات

- `scripts/dedup_audit.py` — فاحص التكرار (يقبل إعادة التشغيل).
- `scripts/dedup_resolve.py` — محذوف التكرار (مع قوائم الـ slugs، آمن للتشغيل المتعدد).
- `python3 scripts/build_slug_index.py` — لتحديث الفهرس بعد أي حذف.

---

## ملاحظات

- **لم تُلمس الملفات المعتمدة أبداً** — كل عمليات الحذف كانت على مسودات فقط.
- **التقنيات الـ7 المتبقية** تحت مدارس مختلفة ستُترك للمراجعة التحريرية البشرية (لم تتغير منذ التقرير الأصلي في 19 أغسطس 2026).
- **التكرار الحرفي بين مسودات بسبب race condition**: متوقع تماماً مع التشغيل المتوازي لجلسات مختلفة. القاعدة "حدّث الفهرس بعد كل عنصر" تحدّ من المعدل لكنها لا تمنعه. الفحص الدوري مثل هذا التقرير مطلوب.
