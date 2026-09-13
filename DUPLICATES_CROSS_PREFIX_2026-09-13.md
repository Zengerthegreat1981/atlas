# ازدواجُ العناوين عبر البادئات — أُغلق

**التاريخ:** 2026-09-13 · **الحالة:** مُنفَّذة
**المرجع:** `FIXES_2026-09-13.md` · **الأداة:** `scripts/merge_duplicate_pair.py`

كان فحصُ التكرار يقارن داخلَ البادئة الواحدة فقط، فلم يرَ قطُّ عقدتين تصفان الشيءَ نفسَه
تحت بادئتين مختلفتين. صار يقارن عبرَ البادئات، فظهرت المجموعاتُ أدناه وعولجت كلُّها.

## ما جرى

| | |
|---|---|
| ملفٌّ دُمج وصار إحالةً دائمة | **59** |
| ملفٌّ قانونيٌّ استقبل المتنَ المدموج | **58** |
| عناوينُ مُيِّزت بدل الدمج (كيانان مختلفان) | 14 |
| عناوينُ نُظِّفت من لاحقةِ نوعٍ لم تعد لازمة | 13 |

**طريقةُ الدمج** في كلِّ حالة:

1. تُحفَظ نسخةُ الملفِّ المُحال كما هي في `content/ar/_merged/` — لا يضيع شيء.
2. يُقرأ المتنان معاً، ويُنقل إلى القانونيِّ **ما انفرد به** الآخرُ من أقسامٍ ومعلومات.
3. `related` و`edges` اتحادٌ بلا تكرار، و`gaps` اتحادٌ، و**المعرِّفُ `id` لا يُمسّ** في أيٍّ منهما.
4. يصير المُحالُ إحالةً صريحةً بـ`redirect_to` وعنوانٍ يقول ذلك — فلا تنكسر الروابطُ القديمة.
5. تُعاد كلُّ إشارةٍ واردةٍ في الأطلس من المُحال إلى القانونيِّ آلياً.

## الجدول

| الملفُّ القانونيّ | ما دُمج فيه |
|---|---|
| `br-abstinence-vs-harm-reduction` — الامتناع الكامل مقابل الحد من الضرر | `con-abstinence-vs-harm-reduction` |
| `br-critical-liberation-therapy` — العلاج النقدي-التحرري | `con-critical-liberation-therapy` |
| `br-daseins` — التحليل الوجودي والدازاين | `con-dasein-analysis` |
| `br-ddp` — العلاج النفسي النمائي الثنائي (DDP) | `tec-ddp` |
| `br-discernment-counseling` — الإرشاد التمييزي (Discernment Counseling) | `con-discernment-counseling`، `tec-discernment-counseling` |
| `br-dynamic-couples-family-therapy` — العلاج الديناميكي للأزواج والأسرة | `con-dynamic-couple-family` |
| `br-family-sandplay` — علاج الأسر الرملية | `con-family-sandplay` |
| `br-fft` — العلاج الأسري الوظيفي (FFT) | `tec-functional-family-therapy` |
| `br-glasser-reality-therapy` — علاج الواقع ونظرية الاختيار (غلاسر) | `tec-reality-choice-therapy` |
| `br-intersectional-feminist` — علم النفس النسوي التقاطعي | `con-intersectional-feminism` |
| `br-mst` — العلاج متعدد الأنظمة (MST) | `tec-multisystemic-therapy` |
| `br-neurodiversity-affirming` — الإرشاد التأكيدي للتنوّع العصبي | `con-neurodiversity-affirming` |
| `br-neuropsychoanalysis` — التحليل النفسي العصبي | `con-neuropsychoanalysis` |
| `br-pcit` — العلاج بتفاعل الوالد-الطفل (PCIT) | `tec-pcit` |
| `br-psychoeducation` — التثقيف النفسي | `con-psychoeducation` |
| `br-restorative-justice` — العدالة التصالحية | `con-restorative-justice` |
| `br-sensory-integration` — التكامل الحسي | `con-sensory-integration` |
| `br-sex-therapy` — العلاج الجنسي | `tec-sex-therapy-overview` |
| `br-structural-family` — العلاج الأسري البنيوي (Structural Family Therapy) | `tec-structural-family-therapy` |
| `br-teacch` — TEACCH | `con-teacch` |
| `br-theraplay` — Theraplay (العلاج بالألعاب العلائقي) | `tec-theraplay` |
| `con-dialectics` — الجدلية (Dialektik) | `trm-dialectic-greek` |
| `con-dissociation` — الانفصال (Dissociation) | `syn-dissociation` |
| `con-free-association` — التداعي الحرّ (Free Association) | `trm-free-association` |
| `con-mindfulness` — اليقظة الذهنية (Mindfulness) | `trm-mindfulness` |
| `dbt-recovered-memory-validity` — جدل الذاكرة المُستعادة: حقيقية أم زائفة؟ | `con-recovered-memory-controversy` |
| `dis-hwabyung` — الهوابيونغ (Hwabyung) | `con-hwabyung-concept` |
| `dis-taijin-kyofusho` — تاي جين كيو فوشو (Taijin Kyofusho) | `con-taijin-kyofusho-concept` |
| `sch-aedp` — العلاج النفسي الديناميكي التعزيزي المتسارع (AEDP) | `tec-aedp` |
| `sch-care-ethics` — أخلاقيات الرعاية (Care Ethics) | `con-care-ethics` |
| `sch-cft` — العلاج المتمحور حول التعاطف (CFT) | `tec-cft` |
| `sch-contemplative-psychotherapy` — العلاج النفسي التأملي (ناروبا) | `tec-contemplative-psychotherapy` |
| `sch-dbt` — العلاج الجدلي السلوكي (DBT) | `tec-dbt` |
| `sch-deep-ecology` — الإيكولوجيا العميقة | `con-deep-ecology-naess` |
| `sch-deliberative-democracy` — الديمقراطية التداولية | `con-deliberative-democracy` |
| `sch-emdr` — إعادة المعالجة عبر حركات العين وتخفيف الأعراض (EMDR) | `tec-emdr` |
| `sch-gestalt-therapy` — علاج الجشطالت (Gestalt Therapy) | `br-gestalt-therapy` |
| `sch-haskalah` — هَسْكَلاة (التنوير اليهودي) | `br-haskalah-jewish-enlightenment` |
| `sch-imago` — العلاج بالـ Imago | `tec-imago-relationship-therapy` |
| `sch-ipt` — العلاج بين الأشخاص (IPT) | `tec-ipt` |
| `sch-istdp` — العلاج النفسي الديناميكي قصير المدى المكثف (ISTDP) | `tec-istdp` |
| `sch-marxism` — الماركسية الكلاسيكية | `br-classical-marxism` |
| `sch-mbct` — العلاج المعرفي القائم على اليقظة الذهنية (MBCT) | `tec-mbct` |
| `sch-motivational-interviewing` — المقابلة التحفيزية (Motivational Interviewing) | `tec-motivational-interviewing` |
| `sch-narrative-therapy` — العلاج السردي (Narrative Therapy) | `tec-narrative-therapy` |
| `sch-navya-nyaya` — نيايا الجديدة (نافيا-نيايا) | `br-navya-nyaya-new-logic` |
| `sch-positive-psychology` — علم النفس الإيجابي (Positive Psychology) | `br-positive-psychology` |
| `sch-positive-psychotherapy` — العلاج النفسي الإيجابي عند بسشكيان | `tec-positive-psychotherapy-peseschkian` |
| `sch-pragmatism-classical` — البراغماتية الكلاسيكية | `br-classical-pragmatism` |
| `sch-queer-theory` — النظرية الكويرية | `con-queer-theory` |
| `sch-rebt` — العلاج العقلاني الانفعالي السلوكي (REBT) | `tec-rebt` |
| `sch-solution-focused` — العلاج المختصر القائم على الحل (SFBT) | `tec-sfbt` |
| `sch-somatic-experiencing` — التجربة الجسدية (Somatic Experiencing) | `tec-somatic-experiencing` |
| `sch-tathagatagarbha` — تاثاغاتاغاربها (طبيعة البوذا) | `con-tathagatagarbha-buddha-nature` |
| `sch-transcendentalism` — التجاوزية الأمريكية | `br-american-transcendentalism` |
| `sch-zen-rinzai` — زن: رينزاي | `br-zen-rinzai` |
| `tec-behavioral-activation` — التنشيط السلوكي (BA) | `con-behavioral-activation` |
| `tec-cbt-cog-cognitive-restructuring` — إعادة الصياغة المعرفية | `con-cognitive-restructuring` |

---

## ما لم يُدمج — وهو الصواب

ستُّ مجموعاتٍ **ليست تكراراً** بل كيانان مختلفان يتقاسمان اسماً. الدمجُ فيها إتلافٌ لا توحيد،
فمُيِّزت العناوينُ بدل ذلك:

| المجموعة | لماذا تبقى منفصلة | ما فُعل |
|---|---|---|
| `wrk-annihilation-of-caste` / `con-annihilation-of-caste` | كتابُ أمبيدكار (1936) بسنته وناشرِه واستقبالِه ≠ المفهومُ الذي حمل اسمَه | لاحقةُ «— الكتاب»/«— المفهوم»، والاسمُ الإنجليزيُّ يحمل المؤلِّفَ والسنة |
| `wrk-7-habits` / `con-seven-habits` | كتابُ كوفي (1989) ≠ المفهومُ الإداريُّ المستقلّ | كما سبق |
| `wrk-behaviorism-watson` / `sch-behaviorism` | كتابُ واطسون (1925) ≠ المدرسةُ كلُّها | «السلوكية — كتاب جون واطسون (1925)» |
| `wrk-existential-psychotherapy` / `sch-existential-therapy` | كتابُ يالوم (1980) ≠ المدرسة | «… — كتاب فرانسين شابيرو/يالوم» في `en` |
| `rel-psychoanalysis` / `sch-psychoanalysis` | الأولى **علاقةٌ** بين الوجودية والتحليل النفسي (ما انفصلت عنه وما احتفظت به)، لا مدخلٌ عن التحليل النفسي | عنوانٌ يصف العلاقةَ صراحةً |
| `rel-humanistic` / `sch-humanistic` | كما سبق | كما سبق |

وكذلك **`sch-positive-psychotherapy` و`tec-positive-psychotherapy`**: تجانسٌ لفظيٌّ بين علاجين
لا صلةَ تاريخيةً بينهما — مدرسةُ **بسشكيان** الألمانية (1968) وبروتوكولُ **راشد وسليغمان**
الأمريكيُّ (2006). صار كلُّ عنوانٍ يحمل صاحبَه صراحةً.

## ما ظهر أثناء الدمج وعولج

- **`br-fft`**: تعارضٌ في إسناد التأسيس بين الملفّين («بارتون بارنز/شيكاغو» مقابل «بروس بارسونز/جامعة يوتا، 1973»). اعتُمدت الروايةُ المقرونةُ بمرجعٍ قابلٍ للتحقّق وسُجِّل التعارضُ في `gaps`.
- **`dis-taijin-kyofusho`**: جاء مع الدمج حرفُ `belongs_to → sch-cognitive-behavioral` — ومتلازمةٌ ثقافيةٌ يابانيةٌ لا تنتمي إلى مدرسةٍ أمريكية. أُسقط الختمُ القالبيّ.
- **`br-daseins` و`br-discernment-counseling`** وثلاثةُ مفكّرين تحتهما: `part` كان «philosophy» وأبوهم «psychology» — وُحِّد على وسم الأب.
- **ثلاثةُ ملفات** ظهر فيها عنوانا قسمٍ متداخلان بعد الدمج، فدُمج القسمان في واحد.

