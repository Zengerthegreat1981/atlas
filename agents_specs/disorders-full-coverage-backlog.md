# قائمة انتظار — التغطية الكاملة للاضطرابات الإكلينيكية (`dis-`)

**هذا خط أنابيب Spark (استكمال).** نفس آلية `schools-backlog.md` بالظبط (`[ ]`/`[~]`/`[x]`) —
بس هنا الـschema والتقسيم بالفعل جاهزين ومتفق عليهم في **`dis-scope-list.md`** (اقرأه كامل الأول،
ده مرجعك الوحيد لشكل الملف بالظبط — كود DSM-5-TR/ICD-11، حقل `classified_in`، القاعدة الخاصة
بربط `related` بالتقنيات والمتلازمات). الملف ده بس تتبّع التقدّم، مش تكرار للـschema.

**النطاق:** كل فئة تشخيصية رسمية معتمدة حالياً في DSM-5-TR أو ICD-11 (**مش** تصنيفات تاريخية
ملغاة — دي مستبعدة صراحة، راجع قسم "Deferred" في `dis-scope-list.md`).

## قبل أي حاجة
1. **`dis-scope-list.md` كامل** — الـschema، أكواد DSM/ICD، ترتيب البناء الموصى بيه.
2. `content/ar/drafts/EXISTING_SLUGS.md` — **حدّثه بعد كل اضطراب واحد، مش بس آخر الـTier.**
3. تأكد إن `classification-dsm-5-tr.md` و`classification-icd-11.md` موجودين فعلاً في
   `content/ar/drafts/disorders/` (لو مش موجودين، اعملهم الأول زي ما موضّح في `dis-scope-list.md`
   قبل أي اضطراب — كل الاضطرابات هتربط بيهم عبر `classified_in`).
4. `draft-writer-brief.md` §3 — بطاقة نوع "اضطراب/حالة إكلينيكية" — **راجع خصوصاً السقف الإكلينيكي**:
   كل ملف لازم يوضّح صراحة إنه وصف معرفي لا تشخيصي.

## الدورة الكاملة

### خطوة 0 — اختيار الاضطراب التالي
القائمة تحت مبنية بالفعل بترتيب Tier A → B → C (زي التوصية في `dis-scope-list.md`). أول `- [~]`
كمّله، وإلا أول `- [ ]` من فوق لتحت — **الأولوية لـTier A كاملة قبل B، وB كاملة قبل C**، حتى لو
حسيت C أسهل. غيّره لـ `- [~]` فوراً.

### خطوة 1 — البحث والتوثيق
ابحث عن الاضطراب: المعايير التشخيصية الفعلية (وصفياً، مش نسخ حرفي من الدليل)، العلاجات الموثّقة
(خصوصاً أي تقنية `tec-` موجودة بالفعل في الأطلس ليها صلة مباشرة — دي أهم روابط `related`)، أي
متلازمة `syn-` موجودة بالفعل ذات صلة (راجع القائمة في `dis-scope-list.md`: قلق حاد، هلع، أعراض
اكتئابية، غضب، خدر انفعالي، أرق، ألم مزمن، أفكار وسواسية، شهوة/رغبة قهرية، وحدة/عزلة، فرط يقظة،
انفصال).

### خطوة 2 — كتابة المسودة
اتبع الـschema في `dis-scope-list.md` **حرفياً** — الحقول، الأكواد، `classified_in` للتصنيفين،
`notes` field لأي فرق جوهري بين DSM-5-TR وICD-11 لنفس الاضطراب (قسم "Major Divergences" في
`dis-scope-list.md` فيه 10 حالات معروفة بالفعل). احفظها في `content/ar/drafts/disorders/<slug>.md`.

**قبل ما تحفظ:** تأكد إن `related` مربوط فعلياً بتقنيات/متلازمات موجودة (افحص `EXISTING_SLUGS.md`)،
مش بس مذكورة كنص.

### خطوة 3 — تحديث الفهرس (بعد كل اضطراب)
```
python3 scripts/build_slug_index.py
```

### خطوة 4 — قفل البند والتالي فوراً
غيّر `[~]` لـ `[x]` في القائمة تحت، سجّل سطر في `pipeline-progress-log.md`، ارجع خطوة 0 من غير
سؤال. استمر لحد ما Tier A وB يخلصوا بالكامل.

## قاعدة وقف صريحة لـTier C
**Tier C (60+ اضطراب، أدوية أساساً/علاقة غير مباشرة بمدارس العلاج النفسي) اختياري.** خلّص Tier A
وB الأول بالكامل (50 اضطراب) — دول الأولوية الحقيقية. لو خلصتهم وعندك وقت/مساحة، انتقل لـTier C
بنفس الانضباط (ملفات أرفع، `gaps` صريحة بالنقص، مش تلفيق عمق مش موجود).

---

## Tier A — أولوية عالية (23 اضطراب، ابدأ هنا)

### قلق (6)
- [x] Separation Anxiety Disorder — `dis-separation-anxiety`
- [x] Selective Mutism — `dis-selective-mutism`
- [x] Specific Phobia — `dis-specific-phobia`
- [x] Social Anxiety Disorder — `dis-social-anxiety-disorder`
- [x] Agoraphobia — `dis-agoraphobia`
- [x] Panic Disorder — `dis-panic-disorder` (✅ موجود بالفعل في `content/ar/disorders/` — تحقّق منه، ممكن يحتاج بس تحديث بالأكواد/`classified_in` الجديدة بدل إعادة كتابة كاملة)

### وسواس قهري وما يتصل به (3)
- [x] OCD — `dis-ocd`
- [x] Body Dysmorphic Disorder — `dis-body-dysmorphic-disorder`
- [x] Hoarding Disorder — `dis-hoarding-disorder`

### صدمة وضغط (2 — PTSD موجود بالفعل)
- [x] Acute Stress Disorder — `dis-acute-stress-disorder`
- [x] Adjustment Disorders — `dis-adjustment-disorders`

### اكتئابية (3 — MDD موجود بالفعل)
- [x] Persistent Depressive Disorder (Dysthymia) — `dis-persistent-depressive-disorder`
- [x] Premenstrual Dysphoric Disorder — `dis-premenstrual-dysphoric-disorder`
- [x] Disruptive Mood Dysregulation Disorder — `dis-disruptive-mood-dysregulation`

### ثنائي القطب (2)
- [x] Bipolar I Disorder — `dis-bipolar-i`
- [x] Bipolar II Disorder — `dis-bipolar-ii`

### أكل (3)
- [x] Anorexia Nervosa — `dis-anorexia-nervosa`
- [x] Bulimia Nervosa — `dis-bulimia-nervosa`
- [x] Binge-Eating Disorder — `dis-binge-eating-disorder`

### نوم (1)
- [x] Insomnia Disorder — `dis-insomnia-disorder`

### تعاطي مواد (1)
- [x] Alcohol Use Disorder — `dis-alcohol-use-disorder`

---

## Tier B — أولوية متوسطة (27 اضطراب)

- [x] Substance/Medication-Induced Anxiety Disorder — `dis-substance-induced-anxiety`
- [x] Anxiety Disorder Due to Another Medical Condition — `dis-anxiety-due-to-medical`
- [x] Trichotillomania — `dis-trichotillomania`
- [x] Excoriation Disorder — `dis-excoriation-disorder`
- [x] Reactive Attachment Disorder — `dis-reactive-attachment`
- [x] Prolonged Grief Disorder — `dis-prolonged-grief` (✅ موجود بالفعل — تحقّق/حدّث بالأكواد)
- [x] Cyclothymic Disorder — `dis-cyclothymia`
- [x] Substance/Medication-Induced Depressive/Bipolar Disorder — `dis-substance-induced-mood`
- [x] Depressive Disorder Due to Another Medical Condition — `dis-depressive-due-to-medical`
- [x] Dissociative Identity Disorder — `dis-dissociative-identity`
- [x] Dissociative Amnesia — `dis-dissociative-amnesia`
- [x] Depersonalization/Derealization Disorder — `dis-depersonalization-derealization`
- [x] Somatic Symptom Disorder — `dis-somatic-symptom-disorder`
- [x] Illness Anxiety Disorder — `dis-illness-anxiety`
- [x] Functional Neurological Symptom Disorder (Conversion) — `dis-functional-neurological-symptom`
- [x] Psychological Factors Affecting Other Medical Conditions — `dis-psychological-factors-medical`
- [x] Borderline Personality Disorder — `dis-borderline-personality`
- [x] Avoidant Personality Disorder — `dis-avoidant-personality`
- [x] Dependent Personality Disorder — `dis-dependent-personality`
- [x] Obsessive-Compulsive Personality Disorder — `dis-obsessive-compulsive-personality`
- [x] Narcissistic Personality Disorder — `dis-narcissistic-personality`
- [x] Antisocial Personality Disorder — `dis-antisocial-personality`
- [x] Schizoid Personality Disorder — `dis-schizoid-personality`
- [x] Schizotypal Personality Disorder — `dis-schizotypal-personality`
- [x] Intermittent Explosive Disorder — `dis-intermittent-explosive`
- [x] Kleptomania — `dis-kleptomania`
- [x] Pyromania — `dis-pyromania`

---

## Tier C — أولوية منخفضة/غير مباشرة (60+ اضطراب — اختياري، بعد A وB بالكامل)

### نمائي عصبي
- [x] Intellectual Disability — `dis-intellectual-disability`
- [x] Autism Spectrum Disorder — `dis-autism-spectrum`
- [x] ADHD — `dis-adhd`
- [x] Specific Learning Disorder — `dis-specific-learning-disorder`
- [x] Developmental Coordination Disorder — `dis-developmental-coordination`
- [x] Tic Disorders — `dis-tic-disorders`

### طيف الفصام
- [x] Schizophrenia — `dis-schizophrenia`
- [x] Schizoaffective Disorder — `dis-schizoaffective`
- [x] Delusional Disorder — `dis-delusional`
- [x] Brief Psychotic Disorder — `dis-brief-psychotic`
- [x] Schizophreniform Disorder — `dis-schizophreniform`

### عصبي معرفي
- [x] Major Neurocognitive Disorder (Dementia) — `dis-major-neurocognitive`
- [x] Mild Neurocognitive Disorder — `dis-mild-neurocognitive`
- [x] Delirium — `dis-delirium`

### تعاطي مواد محدد (8)
- [x] Cannabis Use Disorder — `dis-cannabis-use`
- [x] Stimulant Use Disorder — `dis-stimulant-use`
- [x] Opioid Use Disorder — `dis-opioid-use`
- [x] Sedative/Hypnotic/Anxiolytic Use Disorder — `dis-sedative-use`
- [x] Hallucinogen-Related Disorders — `dis-hallucinogen-use`
- [x] Inhalant Use Disorder — `dis-inhalant-use`
- [x] Tobacco Use Disorder — `dis-tobacco-use`
- [x] Gambling Disorder — `dis-gambling-disorder`

### نوم (أخرى)
- [x] Hypersomnolence Disorder — `dis-hypersomnolence`
- [x] Narcolepsy — `dis-narcolepsy`
- [x] Obstructive Sleep Apnea Hypopnea — `dis-breathing-related-sleep`
- [x] Nightmare Disorder — `dis-nightmare-disorder`

### وظيفة جنسية (7)
- [x] Delayed Ejaculation — `dis-delayed-ejaculation`
- [x] Erectile Disorder — `dis-erectile-disorder`
- [x] Female Orgasmic Disorder — `dis-female-orgasmic`
- [x] Female Sexual Interest/Arousal Disorder — `dis-female-sexual-interest-arousal`
- [x] Genito-Pelvic Pain/Penetration Disorder — `dis-genito-pelvic-pain`
- [x] Male Hypoactive Sexual Desire Disorder — `dis-male-hypoactive-sexual-desire`
- [x] Premature (Early) Ejaculation — `dis-premature-ejaculation`

### هوية جندرية
- [x] Gender Dysphoria — `dis-gender-dysphoria`

### سلوك تخريبي/اندفاعي
- [x] Oppositional Defiant Disorder — `dis-odd`
- [x] Conduct Disorder — `dis-conduct-disorder`

### باثوفيليا
- [x] Voyeuristic Disorder — `dis-voyeuristic`
- [x] Exhibitionistic Disorder — `dis-exhibitionistic`
- [x] Fetishistic Disorder — `dis-fetishistic`

### إخراج
- [x] Enuresis — `dis-enuresis`
- [x] Encopresis — `dis-encopresis`

### أكل (أخرى)
- [x] Pica — `dis-pica`
- [x] Rumination Disorder — `dis-rumination`
- [x] ARFID — `dis-arfid`

### أخرى
- [x] Factitious Disorder — `dis-factitious`
- [x] Catatonia — `dis-catatonia`
- [x] Medication-Induced Parkinsonism — `dis-parkinsonism-medication`
- [x] Other Specified Mental Disorder — `dis-other-specified-mental`
- [x] Unspecified Mental Disorder — `dis-unspecified-mental`
