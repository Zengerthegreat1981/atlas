# خطة قسم علم النفس — الحالة الفعلية المقيسة (Measured Status)

هذا الملف هو **الخطة التفصيلية لقسم علم النفس بالكامل** (القسم الأول من الثلاثة في [PROJECT_PLAN.md](PROJECT_PLAN.md)).

> **تحديث 2 سبتمبر 2026 — إعادة معايرة كاملة.**
> النسخة السابقة من هذا الملف كانت بتاريخ 17 أغسطس، وكانت تعرض معظم القسم كـ ⬜ (غير موجود).
> **هذا لم يكن صحيحاً**: القسم كُتب فعلياً في الدفعات التالية لذلك التاريخ. كل صف في هذا الملف
> الآن **مقيس مباشرةً** من `content/ar/` (عدّ ملفات + تحقّق من الـslug والعنوان)، لا مُخمَّن.
> القاعدة المستعملة: `grep -l '^part: "psychology"'` عبر كل الأنواع.

---

## 0. الأرقام المقيسة (2 سبتمبر 2026)

**إجمالي عناصر قسم علم النفس المعتمدة: 3526 ملفاً** (`part: "psychology"` في `content/ar/`).

| النوع | إجمالي الملفات | منها علم نفس |
|---|---|---|
| `thinkers/` | 2297 | **1078** |
| `techniques/` | 380 | **380** (كله) |
| `concepts/` | 908 | **335** |
| `works/` | 609 | **236** |
| `syndromes/` | 195 | **195** (كله) |
| `studies/` | 121 | **121** (كله) |
| `disorders/` | 113 | **113** (كله) |
| `instruments/` | 103 | **103** (كله) |
| `branches/` | 234 | **113** |
| `events/` | 149 | **77** |
| `debates/` | 176 | **75** |
| `terms/` | 126 | **54** |
| `metaphors/` | 144 | **54** |
| `critiques/` | 100 | **53** |
| `schools/` | 379 | **43** |
| `experiences/` | 124 | **37** |
| `relations/` | 126 | **24** |
| `axioms/` | 50 | **22** |
| `contexts/` | 118 | **18** |
| `questions/` | 129 | **9** |
| `dialogues/` | 49 | **5** |

**الخلاصة:** القسم **مكتمل تغطيةً** في كل الأنواع الكثيفة. ما بقي ليس كتابة محتوى جديد
بحجم كبير، بل **تدقيق وربط وسدّ فجوات محدَّدة** — التفاصيل في القسم 15.

---

## 1. المدارس (`schools/`) — 43 مدرسة نفسية معتمدة

| المدرسة | الملف | حالة |
|---|---|---|
| الوجودية / العلاج الوجودي | `sch-existentialism`, `sch-existential-therapy` | ✅ 266 مفكراً مرتبطاً |
| التحليل النفسي الفرويدي | `sch-psychoanalysis` | ✅ 291 مفكراً مرتبطاً |
| التحليلية اليونغية | `sch-analytical-psychology` | ✅ الملف موجود — **لكن 3 مفكرين مرتبطين فقط** (فجوة ربط، القسم 15.4) |
| الفردية الأدلرية | `br-adlerian` | ✅ كفرع، 11 مفكراً — القرار المعماري (فرع لا مدرسة) **مُنفَّذ** |
| السلوكية | `sch-behaviorism` | ✅ 27 مفكراً |
| المعرفية / CBT | `sch-cbt`, `sch-cognitive-behavioral` | ✅ 41 + 3 مفكراً — **ملفان لنفس المدرسة، مرشّح دمج** |
| الجشطالتية | `sch-gestalt-therapy` | ✅ 10 مفكرين |
| الإنسانية | `sch-humanistic` | ✅ 20 مفكراً |
| النظامية / الأسرية | `sch-systemic-family` | ✅ 22 مفكراً |
| النمائية / التطورية (نمو) | `sch-developmental` | ✅ 16 مفكراً |
| **علم النفس التطوري (Evolutionary Psychology)** | — | ⬜ **الفجوة الوحيدة في المدارس**: موجود كمسودة فقط في `drafts/minimax/schools/sch-evolutionary-psychology.md`، لم يُعتمد |
| الاجتماعية | `sch-social-psychology` | ✅ 13 مفكراً |
| البيولوجية / العصبية | `sch-biological-neuro` | ✅ 8 مفكرين |
| الإيجابية | `sch-positive-psychology` | ✅ 9 مفكرين |
| عبر الشخصية | `sch-transpersonal` | ✅ 12 مفكراً |
| العلاقة بالموضوع | `sch-object-relations` | ✅ الملف موجود — **صفر مفكر مرتبط** (فجوة ربط، القسم 15.4) |
| ACT | `sch-act` | ✅ + `rel-act`, `rel-act-cbt-third-wave` |
| علم النفس البوذي / الأفريقي / AEDP … | `sch-buddhist-psychology`, `sch-african-psychology`, `sch-aedp` | ✅ توسّع خارج الخطة الأصلية |

---

## 2. المفكرون (`thinkers/`) — 1078 ملفاً

كل الأسماء التي كانت مسجَّلة كـ «أولوية قصوى غائبة» في النسخة السابقة **موجودة الآن**:

| المدرسة | التحقّق |
|---|---|
| تحليل نفسي | ✅ `thk-freud`, `thk-afreud` (أنّا), `thk-adler`, `thk-rank`, `thk-sferenczi`, `thk-khorney`, `thk-klein` (ميلاني), `thk-winnicott`, `thk-lacan`, `thk-kohut`, `thk-kernberg` |
| تحليلية | ✅ `thk-jung`, `thk-bleuler-jung-assoc` |
| سلوكية | ✅ `thk-ipavlov`, `thk-fskinner`, `thk-abandura`, `thk-jwolpe` + واطسون وثورندايك (مغطّيان في `studies/`) |
| معرفية / CBT | ✅ `thk-beck`, `thk-ellis`, `thk-piaget`, `thk-mlinehan`, `thk-lstevenhayes` |
| جشطالت | ✅ `thk-mwertheimer`, `thk-wkohler`, `thk-kkoffka`, `thk-klew` (كورت ليفين), `thk-fperls` |
| إنسانية | ✅ `thk-rogers`, `thk-nrogers`, `thk-maslow`, `thk-bugental`, `thk-vsatir` |
| نظامية | ✅ `thk-gbateson`, `thk-sminuchin`, `thk-mbowen`, `thk-vsatir` |
| نمائية | ✅ `thk-piaget`, `thk-erikson`, `thk-bowlby`, `thk-ainsworth`, `thk-vygotsky` |
| اجتماعية | ✅ `thk-stanley-milgram`, `thk-philip-zimbardo`, `thk-klew`, فستنغر |
| بيولوجية/عصبية | ✅ `thk-damasio`, `thk-jledoux` — ⬜ **دونالد هيب: الاسم الوحيد الغائب فعلياً** (موجود كاستعارة `met-hebb-neurons-fire-together` بلا ملف مفكر) |
| إيجابية | ✅ `thk-mseligman`, `thk-csikszentmihalyi` |
| عبر الشخصية | ✅ `thk-kwilber`, `thk-mgrof` |

> **تنبيه:** الملف موجود ≠ الملف صحيح. **781 ملف مفكر لم يُقرأ بعد** بمعدّل 4–6 أخطاء حقيقية
> للملف الواحد. هذا هو العمل المتبقّي الأكبر — القسم 15.1.

---

## 3. المفاهيم (`concepts/`) — 335 مفهوماً نفسياً

موجود: `con-unconscious`, `con-cultural-unconscious`, `con-interpersonal-unconscious`, `con-archetype`,
`con-archetypes`, `con-oedipus-complex`, `con-transference`, `con-inferiority-superiority-complex`, `con-classical-conditioning`,
`con-operant-conditioning`, `con-cognitive-distortion`, `con-schema`, `con-cognitive-restructuring`,
`con-unconditional-positive-regard`, `con-self-actualization` (+ `br-self-actualization-maslow`),
`con-triangulation`, `con-attachment-styles`, `con-secure-attachment`, `con-cognitive-dissonance`, `con-neuroplasticity`,
`con-flow`, `con-mindfulness`, `con-mind-body`.

**فجوات مفاهيمية مؤكَّدة (⬜ حقيقية — بحث بالـslug والعنوان العربي معاً):**

| المفهوم | المدرسة |
|---|---|
| آليات الدفاع النفسي (كمفهوم جامع) | تحليل نفسي |
| الأنا / الهو / الأنا الأعلى (البنية الثلاثية) | تحليل نفسي |
| اللاوعي الجمعي (منفصلاً عن `con-archetype`) | تحليلية |
| الانطواء / الانبساط | تحليلية |
| التعميم والتمييز السلوكي | سلوكية |
| الشكل والأرضية (Figure/Ground) | جشطالت |
| الاكتمال / قوانين الجشطالت (Closure, Prägnanz) | جشطالت |
| نظرية العقل (Theory of Mind) | نمائية |
| الرفاه النفسي (Well-being / Eudaimonia) | إيجابية |

*(إعادة التقييم المعرفي غير ناقصة — موجودة كتقنية `tec-cognitive-reappraisal`؛ المطلوب ربط لا إنشاء.)*

---

## 4. الأعمال (`works/`) — 236 عملاً نفسياً

موجود: `wrk-freud-interpretation-of-dreams`, `wrk-freud-beyond-pleasure-principle`,
`wrk-jung-psychological-types`, `wrk-adler-understanding-human-nature`, `wrk-behaviorism-watson`,
`wrk-skinner-behavior-organisms`, `wrk-beck-cognitive-therapy`, `wrk-beck-cognitive-therapy-depression`,
`wrk-reason-emotion-psychotherapy-ellis`, `wrk-rogers-client-centered-therapy` (+ نسختان),
`wrk-maslow-motivation-and-personality`, `wrk-erikson-childhood-society`, `wrk-bowlby-maternal-care`,
`wrk-bowlby-separation`, `wrk-horney-neurotic-personality`, `wrk-horney-inner-conflicts`,
`wrk-winnicott-playing-reality`, `wrk-seligman-helplessness`, `wrk-frankl-mans-search-for-meaning`.

**فجوات مؤكَّدة:**

| العمل | المؤلف |
|---|---|
| الأنا وآليات الدفاع | أنّا فرويد |
| مبادئ علم نفس الجشطالت | كوفكا |
| ما وراء الحرية والكرامة | سكينر |
| خطوات نحو إيكولوجيا العقل | باتيسون |
| أي عمل مستقل لبياجيه | بياجيه |
| صيرورة الإنسان (On Becoming a Person) | روجرز — الموجود هو `client-centered` لا هذا |
| التدفق (Flow) | تشيكسنتميهاي |

---

## 5. الجدالات والحوارات (`debates/` 75، `dialogues/` 5)

| البند | حالة |
|---|---|
| فرويد ضد يونغ | ✅ `dia-freud-jung-libido-split` + `evt-munich-congress-jung-freud-split-1913` |
| اللاوعي (طبيعته) | ✅ `dbt-unconscious` |
| الطبيعة ضد التنشئة | ✅ **5 ملفات** (`dbt-nature-nurture*`) — تغطية أعمق من المطلوب |
| الحرية ضد الحتمية | ✅ 4 ملفات (`dbt-free-will*`, `dbt-existential-freedom-vs-structuralist-determinism`) |
| القبول ضد التغيير المعرفي | ✅ `dbt-acceptance-vs-cognitive-change` |
| العملي-التجريبي ضد CBT | ✅ `dbt-process-experiential-vs-cbt` |
| استقرار التعلق | ✅ `dbt-attachment-stability` |
| قابلية التفنيد | ✅ `dbt-verification-vs-falsification` |
| **فرويد ضد أدلر** (الجنسي ضد إرادة القوة) | ⬜ فجوة |
| **السلوكية ضد التحليل النفسي** (واطسون/فرويد) | ⬜ فجوة |
| **نقد تشومسكي لسكينر** (الصندوق الأسود) | ⬜ فجوة — تشومسكي موجود (`thk-nchomsky`) والحوار مع بياجيه موجود، لكن جدل سكينر لا |

---

## 6. الاضطرابات (`disorders/`) — ✅ **113 ملفاً، مكتمل**

التغطية الآن **كاملة عبر DSM-5-TR وICD-11** بما فيها ملفّا التصنيف نفسيهما
(`classification-dsm-5-tr`, `classification-icd-11`)، وكل الفئات التي كانت ⬜:
المزاجية (`mdd`, `major-depressive`, `bipolar-i/ii`, `cyclothymia`, `persistent-depressive`)،
الشخصية (العشرة كلها + ثلاثة تاريخية)، الذهانية (`schizophrenia`, `schizoaffective`, `schizophreniform`,
`brief-psychotic`, `delusional`)، الأكل (`anorexia`, `bulimia`, `binge-eating`, `arfid`, `pica`)،
الوسواس والطيف (`ocd`, `body-dysmorphic`, `hoarding`, `trichotillomania`, `excoriation`)،
النمو العصبي (`autism-spectrum`, `adhd`, `intellectual-disability`, `specific-learning`)،
الارتباط (`reactive-attachment`)، الصدمة (`ptsd`, `acute-stress`, `adjustment`)،
بالإضافة إلى الاضطرابات الثقافية (`hwabyung`, `taijin-kyofusho`) والجنسية والنومية والإدمانية.

---

## 7. المتلازمات (`syndromes/`) — ✅ **195 ملفاً، مكتمل**

كل ما كان ⬜ موجود: `syn-stockholm`, `syn-burnout`, `syn-caregiver-burnout`, `syn-impostor`
(+ `syn-impostor-syndrome`، مرشّح دمج)، `syn-paris`, `syn-compassion-fatigue`, `syn-survivor-guilt-syndrome`.

---

## 8. أدوات القياس (`instruments/`) — ✅ **103 أدوات، مكتمل**

كل ما كان ⬜ موجود: `ins-gad7`, `ins-bdi-ii`, `ins-mmpi`, `ins-neo-pi-r` (الخماسي),
`ins-pcl-5`, `ins-rorschach`, `ins-tat`, `ins-penn-state-worry`, `ins-lot-r-life-orientation-test`, `ins-static-99`.
**العمل المتبقّي عليها تدقيقي لا إنشائي** — القسم 15.3.

---

## 9. التقنيات (`techniques/`) — ✅ **380 ملفاً، كله علم نفس**

تغطية كثيفة جداً بعائلات مرقّمة: `tec-cbt-*` (تعرّض، معرفي، يقظة)، `tec-dbt-*`، `tec-act-*`
(hexaflex، مصفوفة، استعارات)، `tec-eft-*`، `tec-cognitive-reappraisal`, `tec-prolonged-exposure`,
`tec-person-centered-core-conditions`, `tec-empty-chair-dialogue-eft`, `tec-cbt-cog-cognitive-reframing`.

**فجوتان مؤكَّدتان:**

| التقنية | المدرسة |
|---|---|
| التداعي الحر (Free Association) | تحليل نفسي — **لا يوجد أي ملف** |
| تحليل الأحلام كتقنية علاجية | تحليل نفسي — العمل موجود، التقنية لا |
| إزالة التحسس المنهجي (Systematic Desensitization) | سلوكية — التعرّض التدريجي مغطّى بعائلة `tec-cbt-exp-*`، لكن تقنية وولب باسمها غائبة |

---

## 10. الفروع (`branches/`) — 113 فرعاً نفسياً

✅ `sch-object-relations`, `br-ego-psychology`, `br-lacanian`, `br-adlerian`,
`br-self-actualization-maslow`, `br-transactional-analysis`, `sch-act`.
DBT مغطّى عبر `rel-dbt-bpd`, `rel-heraclitus-dialectical-behavior-therapy`, وعائلة `tec-dbt-*`
— ⬜ **لكن لا ملف فرع/مدرسة مستقلاً لـ DBT نفسه**.

---

## 11. الأحداث (`events/`) — ✅ **77 حدثاً، مكتمل**

كل ما كان ⬜ موجود: `evt-clark-university-lectures-1909`, `evt-munich-congress-jung-freud-split-1913`,
`evt-ahp-founding-1961`, `evt-yale-hull-neo-behaviorism-1935`, `evt-jahrbuch-psychoanalyse-1909`,
`evt-iaap-jungian-1955`, `evt-jung-institute-zurich-1948`، **وسلسلة DSM كاملة**
(1952 / 1968 / 1980 / 1994 / 2013 + `evt-dsm-homosexuality-removal-1973`).

---

## 12. النقد الخارجي (`critiques/`) — ✅ **53 ملفاً، مكتمل**

`crt-popper-critique-psychoanalysis`, `crt-popper-falsifiability-psychoanalysis`,
`crt-replication-crisis`, `crt-anti-psychiatry-critique`, `crt-foucault-critique-of-asylum`,
`crt-deleuze-guattari-critique-of-psychoanalysis`, `crt-feminist-critique-psychoanalysis`,
`crt-feminist-critique-behaviorism`, `crt-postcolonial-critique-psychoanalysis`,
`crt-religious-conservative-critique-psychoanalysis`.
**نقد تشومسكي لسكينر** هو الغائب (مذكور في القسم 5).

---

## 13. المصطلحات (`terms/`) — ✅ **54 مصطلحاً، مكتمل**

`trm-trieb-instinct-drive`, `trm-verdrangung-repression`, `trm-repression`,
`trm-todestrieb-death-drive`, `trm-angst-translation`.

---

## 14. الدراسات (`studies/`) — ✅ **121 دراسة، كله علم نفس**

`stu-milgram-obedience`, `stu-stanford-prison`, `stu-watson-little-albert`,
`stu-harlow-rhesus-monkeys`, `stu-ainsworth-strange-situation`, `stu-bowlby-forty-four-thieves`,
`stu-pavlov-classical-conditioning`, `stu-thorndike-puzzle-box`, `stu-bandura-vicarious-reinforcement`,
`stu-wertheimer-gestalt`, `stu-kohler-insight-chimpanzees`, `stu-festinger-cognitive-dissonance`,
`stu-lewin-leadership-climates`, `stu-peterson-seligman-explanatory-style`, `stu-terror-management-theory`.

---

## 15. ما بقي فعلاً — قائمة العمل الحقيقية

بترتيب الحجم والأثر. **هذا هو الجزء العملي من الملف؛ ما قبله جرد تحقّق.**

### 15.1 تدقيق قراءة ملفات المفكّرين — المهمّة الأكبر
- **781 ملفاً لم يُقرأ**، القائمة في `scripts/audit_unread_thinkers.txt`.
- معدّل الأخطاء **4–6 لكل ملف**، ولا يكشفها أي فحص آلي: هويّة خاطئة لصاحب الملف،
  موقف نظري معكوس، عمل منسوب لغير صاحبه، مصطلح مقلوب المعنى، تواريخ مستحيلة.
- 2351 تصحيحاً مسجَّلاً في 795 ملفاً حتى الآن. الإجراء والأدوات في [NEXT_SESSION.md](NEXT_SESSION.md).
- **قاعدة إلزامية:** `python3 scripts/reapply_thinkers_audit.py --apply` في بداية كل جلسة وبعد كل دفعة
  (المستودع يُكتب فيه بالتوازي وتُستبدل الملفات بنسخ أقدم).

### 15.2 قرار معلّق ينتظر تدخّلك — حجْر 264 ملفاً
- 264 ملف مفكر غير قابل للتحقّق (نص نائب ظاهر، أو قسم أعمال بلا عنوان كتاب واحد،
  أو الـslug يسمّي شخصاً و`en` يسمّي آخر).
- السكريبت جاهز ومُختبَر (`scripts/quarantine_unverified_thinkers.py --apply`) لكنه
  **نُفِّذ مرّتين وأُعيد مرّتين** من جلسات متوازية.
- `[DRAFT-UNKNOWN]` ظاهر حالياً في **221 ملفاً معتمداً** + 10 ملفات خارج `thinkers/`
  (في `concepts/` و`techniques/`) وكلها تُعرض على الموقع.
- **لا يتقدّم هذا البند بلا قرارك** (إيقاف الجلسات المتوازية / عزل على غرار `_merged/` / تنبيه ظاهر).

### 15.3 الخطة الرابعة (DSM والسيكومتريا) — 0 من ~15 مهمة
كل المراحل الخمس في [PLAN_4_DSM_AND_PSYCHOMETRICS.md](agents_specs/PLAN_4_DSM_AND_PSYCHOMETRICS.md) مفتوحة:
مسح مسار تطور DSM، ربط الـ103 أداة باضطراباتها ومطوّريها، تدقيق الصدق والثبات،
ربط الـ121 دراسة بالمفاهيم التأسيسية وبأزمة التكرار، ثم إعادة البناء ومحضر الإنجاز.
**هذه هي خطة التنفيذ الفعلية للأنواع المكتملة عددياً في الأقسام 6 و8 و14 أعلاه.**

### 15.4 فجوات ربط (الملف موجود، الشبكة حوله فارغة)
- `sch-object-relations`: **صفر مفكر مرتبط** — كلاين ووينيكوت وفيرن وكوهت موجودون كملفات وغير مربوطين.
- `sch-analytical-psychology`: **3 مفكرين فقط** لمدرسة يونغ كاملة.
- `sch-biological-neuro` (8)، `sch-positive-psychology` (9)، `sch-gestalt-therapy` (10)،
  `sch-social-psychology` (13) — كثافة منخفضة نسبةً لـ 291 في التحليل النفسي و266 في الوجودية.
- `rel-*`: 24 علاقة نفسية فقط. القاعدة المقرَّرة (كل مدرسة نفسية جديدة تحتاج `rel-` واحداً على
  الأقل يقارنها بالوجودية) **غير مطبَّقة على معظم المدارس الـ43**.

### 15.5 فجوات محتوى محدَّدة (قابلة للإنجاز في دفعة واحدة)
- **مدرسة:** علم النفس التطوري — اعتماد المسودة `drafts/minimax/schools/sch-evolutionary-psychology.md`.
- **مفكر:** دونالد هيب (الاسم الوحيد الغائب من كل قوائم هذا الملف).
- **9 مفاهيم:** القسم 3.
- **7 أعمال:** القسم 4.
- **3 جدالات:** فرويد/أدلر، السلوكية/التحليل النفسي، تشومسكي/سكينر (القسمان 5 و12).
- **3 تقنيات:** التداعي الحر، تحليل الأحلام، إزالة التحسس المنهجي (القسم 9).
- **1 فرع:** DBT كملف مستقل (القسم 10).

### 15.6 صيانة
- **مرشّحو دمج:** `sch-cbt` / `sch-cognitive-behavioral`، و`syn-impostor` / `syn-impostor-syndrome`.
  شغّل `python3 scripts/merge_thinker_duplicates.py` (فحص فقط) بعد كل نموّ — دُمج 48 حتى الآن في `_merged/`.
- **3 ملفات بلا أي قسم:** `thk-isap`, `thk-jmertz`, `thk-ebosnak` — وهي **جمعيات لا أشخاص**
  وتحتاج قراراً: تُكتب كمؤسسات، أم تُنقل، أم تُحذف من نوع «مفكر».
- **الأنواع الرقيقة** (`questions/` 9، `dialogues/` 5، `contexts/` 18، `axioms/` 22): تبقى رقيقة
  بقرار مقصود — تُكتب عند الحاجة أثناء كتابة نوع آخر، لا بقوائم استباقية.

---

*آخر تحديث: 2 سبتمبر 2026 — إعادة معايرة كاملة مقابل `content/ar/`. كل رقم في هذا الملف مقيس
لا موروث؛ راجع القسم 6 في [NEXT_SESSION.md](NEXT_SESSION.md) لقائمة الأرقام الموروثة المضخَّمة.*
