# تقرير فحص الأولويات — أطلس السياقات (2026-08-21)

> فحص شامل لحالة الأولويات اللي اتفقنا عليها في الجلسة السابقة، مع التحديثات اللي اتعملت.

## 1. ملخص تنفيذي

من آخر فحص للأنواع الـ 11، المشروع عمل **نقلة نوعية ضخمة** في أغلب الأنواع، لكن **الـ `contexts` (السياقات) هي الفجوة الوحيدة الحرجة** المتبقية. الحالة الحالية:

| النوع | العدد الكلي | الحالة | الإجراء |
|---|---|---|---|
| **thinkers** | 1,928 | متفوق | لا حاجة |
| **concepts** | 417 | متفوق | لا حاجة |
| **schools** | 330 | متفوق | لا حاجة |
| **techniques** | 340 | متفوق | لا حاجة |
| **studies** | 115 | متفوق | لا حاجة |
| **disorders** | 107 | متفوق | لا حاجة |
| **instruments** | 96 | متفوق | لا حاجة |
| **branches** | 129 | متفوق | لا حاجة |
| **debates** | 52 | متفوق | لا حاجة |
| **relations** | 32 | مقبول | لا حاجة |
| **contexts** | 8 (كانت) → **13 (الآن)** | كان ضعيف جداً — **تم التوسيع** | ✅ 5 ملفات جديدة |

## 2. ما تم إنجازه في الجلسة السابقة (تم التحقق)

### 2.1 الأولوية 1 (الأنواع الـ 5 الناقصة) — مُنجَز معظمها

من الـ 5 أنواع اللي كانت فيها عنصر واحد بس في الجلسة السابقة:

- ✅ **`ins-` (أدوات القياس)**: كان اقتراح PHQ-9, GAD-7, TAS-20. حالياً 96 ملف — تم تغطيتها كلها تقريباً (BDI-II, GAD-7, BAI, BPRS, etc.).
- ✅ **`dis-` (اضطرابات)**: كان اقتراح MDD, Panic, PTSD, BPD, OCD. حالياً 107 ملف — تم تغطيتها (MDD, dis-anxiety, dis-ptsd, dis-bpd, dis-ocd, إلخ).
- ✅ **`tec-` (تقنيات)**: كان اقتراح Socratic Dialogue, Logotherapy, MBCT, ACT defusion, Exposure, Empty Chair. حالياً 340 ملف — تم تغطيتها كلها وأكثر.
- ✅ **`stu-` (دراسات)**: كان اقتراح Terror Management, Becker 1979, Steger, Engel 1971, Jonas-Greenberg-Frey 2003. حالياً 115 ملف — تم تغطية Terror Management ودراسات كلاسيكية كثيرة.
- ⚠️ **`ctx-` (سياقات)**: كان اقتراح Husserl, Psychoanalysis, Stoicism, Buddhist, Hindu, Greek, Ibn Ata Allah, etc. — **كان فيه فقط 8 عناصر** (6 معتمد + 2 مسودة). **تمت إضافة 5 سياقات جديدة** في هذه الجلسة.

### 2.2 الأولوية 2 (فجوات الـ 6 الأصلية)

- **مفكرون (`thk-`)** — الأهم Morita, Boss, Binswanger, Leder, Gallagher. أضفت `thk-stoics` ضمنياً (لكن كـthk- واحدة مجمّعة). **لم يُضف أي من هؤلاء صراحةً** — لكن العدد (1,928) يجعل الفجوة غير حرجة.
- **مفاهيم (`con-`)** — كان اقتراح Authenticity, Bad Faith, The Absurd, Boredom, Emptiness, Loneliness vs Solitude, Being-toward-death, Alienation. **كلها موجودة كـمعتمدين**:
  - `con-authenticity.md` ✅
  - `con-bad-faith.md` ✅
  - `con-absurd.md` ✅
  - `con-being-toward-death.md` ✅
  - `con-existential-vacuum.md` ✅ (يغطي الفراغ)
  - `con-isolation.md` ✅ (يغطي العزلة)
  - `con-freedom.md` ✅
  - `con-responsibility.md` ✅
  - `con-thrownness.md` ✅
  - **مفقود فقط**: `con-boredom-existential` (الملل الوجودي) و `con-loneliness-solitude`.
- **جدل (`dbt-`)** — مقترحات التشخيص الوجودي مقابل DSM-5، الإرادة الحرة، المعنى مقابل العبث، الجسد، الشمولية. **معظمها متاح ضمن 52 ملف**، لكن التشخيص الوجودي تحديداً يستحق ملفاً مستقلاً.
- **تيارات (`br-`)** — British, Daseinsanalysis, Logotherapy, Morita. العدد 129 ملف يجعل الفجوة غير حرجة.
- **علاقة (`rel-`)** — 32 ملف، والمقترحات (Existentialism↔CBT, Existentialism↔Positive) متاحة ضمن `rel-cbt-*` و `rel-humanistic-*`.

## 3. السياقات الجديدة المُضافة في هذه الجلسة (5 ملفات)

كلها في `content/ar/drafts/contexts/` (تحتاج مراجعة `agent-4-draft-review.md` للنقل للمعتمد):

1. **`ctx-stoicism.md`** — الفلسفة الرواقية (philosophy)
   - يربط: sch-stoicism, sch-existentialism, thk-stoics, con-dichotomy-of-control, con-meaning, rel-stoicism-cbt
2. **`ctx-psychoanalytic-tradition.md`** — التقليد التحليلي النفسي (philosophy)
   - يربط: sch-psychoanalysis, sch-existentialism, thk-freud, thk-jung, thk-lacan
3. **`ctx-greek-philosophy-of-psyche.md`** — فلسفة النفس اليونانية (philosophy)
   - يربط: sch-academy-platonic, sch-aristotelianism, sch-atomism-greek, thk-plotinus
4. **`ctx-hindu-philosophical-traditions.md`** — التقاليد الفلسفية الهندية الكبرى (philosophy)
   - يربط: sch-advaita-vedanta, sch-dvaita-vedanta, sch-neo-vedanta, thk-patanjali, thk-shankara, thk-madhva, con-maya-vedanta, con-karma-philosophy
5. **`ctx-ibn-ata-allah.md`** — ابن عطاء الله السكندري والتصوف السلوكي (philosophy)
   - يربط: ctx-arabic-self, ctx-ghazali

## 4. شذوذ وفجوات مكتشفة أثناء العمل

### 4.1. شذوذ في EXISTING_SLUGS.md (مشكلة بنيوية)

**المشكلة**: ملف `content/ar/drafts/schools/` فيه **333 ملف `sch-*`** كلها `type: مدرسة`، لكن **مفيش قسم "مدرسة" في EXISTING_SLUGS.md** (سكريبت `build_slug_index.py` يستخدم `TYPE_ORDER` ثابت ما فيهوش "مدرسة").

**التأثير**: عند كتابة أي مسودة جديدة والإشارة لمدرسة في `related`، الفاحص مش هيشوف الـslug. ده كان سببي في 8 روابط مبدئية كادت تكون خاطئة قبل ما أكتشف.

**الحل الموصى به**: إضافة `"مدرسة"` لـ `TYPE_ORDER` في `scripts/build_slug_index.py` (موقع: السطر 30 تقريباً، بعد "علاقة بين مدرستين" وقبل "سياق/تقليد"). هذا إصلاح صغير لكنه يحرر 333 slug من الظل.

**حالياً**: في السياقات الجديدة، استخدمت الـschools في `edges` (مش `related`) لتفادي المشكلة.

### 4.2. فجوات المفاهيم الفلسفية-الدينية

اكتشفت 13 مفهوم محوري مذكور في السياقات الجديدة لكنه **غير موجود** كـ`con-` مستقل، وأضفتها في قسم `## أفكار روابط لم تُتحقق` في كل ملف:

- **التحليل النفسي**: con-unconscious, con-repression, con-transference, con-archetypes
- **الفلسفة اليونانية**: thk-plato, thk-aristotle, con-soul, con-virtue-ethics, con-passion-vs-reason
- **الفلسفة الهندية**: con-atman, con-brahman, con-moksha
- **التصوف الإسلامي**: thk-ibnataallah, con-trust-in-god-tawakkul, con-detachment-zuhd, con-presence-hudur, wrk-hikam-ibn-ata-allah
- **الرواقية**: con-amor-fati

**التوصية**: هذه الـ 17 slug هي المرحلة التالية الطبيعية — كل واحدة ممكن تتعمل كمسودة `con-` أو `thk-` في جولة كتابة لاحقة.

## 5. خلاصة — ما يحتاج فعل من المستخدم

| القرار | الخيار |
|---|---|
| المسودات الـ 5 الجديدة للسياقات | ✅ مراجعة من قِبل `agent-4-draft-review.md` ثم النقل للمعتمد |
| فجوة EXISTING_SLUGS.md (المدارس) | إضافة `"مدرسة"` لـ `TYPE_ORDER` في `build_slug_index.py` |
| الـ 17 slug الناقص في `## أفكار روابط لم تُتحقق` | أولوية متوسطة — يمكن معالجتها في جولة لاحقة |
| معارضة 9 slug بين المعتمد والمسودات | ⚠️ موجود من قبل (schopenhauer, emerson, schelling, kierkegaard, hegel, solomon, rousseau, nishida, nietzsche) — لم يُعالَج في هذه الجلسة |

## 6. الأرقام النهائية

- **عدد السياقات الكلي**: 13 (كانت 8، أُضيف 5)
- **عدد العناصر الكلي في الأطلس**: 4,155 (418 معتمد + 3,737 مسودة)
- **عدد السياقات المعتمدة**: 6 (المعتمدون في `content/ar/contexts/`)
- **عدد المسودات في contexts**: 7 (2 سابقين + 5 جداد)
- **المسودة الجاهزة للترقية الأعلى**: `ctx-stoicism` (أعلى كثافة ربط بين المعتمدين)
