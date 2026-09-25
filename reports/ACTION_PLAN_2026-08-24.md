# خطة عمل أطلس — توسيع البيانات والروابط
## تاريخ الإصدار: 2026-08-24 · الجلسة: mvs_5c3999563f704259be719b862e9a7299 · الحالة: جاهز للتدقيق

> **الغرض:** خطة تنفيذية مرحلية لتوسيع بيانات الأطلس وروابطه، مع تعريف صريح بالتبعيات بين المراحل، ومخرجات قابلة للتحقق آلياً.
> **المُسلِّم:** Mavis (root session) · **المُراجِع:** نموذج ذكاء اصطناعي آخر (مرحلة التدقيق).

---

# 1. الملخص التنفيذي (Executive Summary)

## 1.1 الوضع الحالي (verified at 2026-08-24 17:48)

| المؤشر | القيمة | المصدر |
|---|---|---|
| إجمالي الملفات المعتمدة | **6,435** | `ls content/ar/*/` |
| ملفات `thinkers/` المعتمدة | **2,188** | نفس |
| ملفات `schools/` المعتمدة | **369** | نفس |
| إجمالي المسودّات | **5** (فقط) | نفس |
| إجمالي العناصر في الفهرس | **6,478** | `EXISTING_SLUGS.md` |
| Orphan files | **5** | `python3 scripts/minimax_orphan_audit.py` |
| روابط معلّقة (unverified) | **0** | `python3 scripts/audit_unverified_links.py` |
| Slugs وهمية (phantoms) | **0** | `python3 scripts/spark_integrity_audit.py` |
| مكررات داخل القسم الواحد | **0** | نفس |
| مكررات cross-part | **1** | نفس (`thk-cgrob` ≡ `thk-charles-grob`) |
| Backlogs منجزة 100% | **10 من 10** | فحص يدوي |
| Thinkers لم تُقرأ بعد في التدقيق | **1,301** | `scripts/audit_unread_thinkers.txt` |
| Thinkers بـ `related` فارغ (boilerplate) | **184** | فحص regex |
| Thinkers بـ `[DRAFT-UNKNOWN]` ظاهر | **237** | `AUDIT_HANDOFF.md` §4 |
| أزواج دمج معلّقة | **48** | `scripts/thinker_merge_plan.json` |
| تعارضات slug/identity | **30** | `AUDIT_HANDOFF.md` §5 |
| `active_end: مستمر` لأموات | **182** | `AUDIT_HANDOFF.md` §4 |

## 1.2 الحكم التشغيلي

**البنية التحتية سليمة. المحتوى ناضج لكنه غير متجانس:**

- ✅ **0 روابط مكسورة، 0 slugs وهمية، 0 مكررات داخل القسم** — سلامة بنيوية شبه مثالية.
- ⚠️ **0.6% فقط من الـthinkers عندهم 21+ related، و65.6% عندهم 1-3 فقط** — كثافة الروابط هزيلَة رغم سلامة البنية.
- ⚠️ **بعض الأنواع معزولة فعلياً:** events (65.9% بلا related)، relations (55.1% بلا related)، dialogues (46.8% بلا related)، debates (38.5%)، works (37.8%)، concepts (35.4%) — هذه فجوة الروابط الأساسية.
- ⚠️ **التوزيع بين المدارس غير متكافئ:** 336 مدرسة عندها ≤2 مفكرين، بينما المدرسة الوجودية وحدها 299 مفكر — 60% من المدارس ممثَّلة بـ 1-2 شخص فقط.
- ⚠️ **1,301 ملف thinker لم يُقرأ بعد** في التدقيق — بمعدّل 4-6 أخطاء حقيقية لكل ملف، نتوقع ~6,500 خطأ محتوى متبقي.

## 1.3 الاستراتيجية في 3 جمل

1. **ثبّت أولاً، وسّع ثانياً، اربط ثالثاً، وثّق رابعاً.** لا إضافة بيانات فوق بنية قابلة للسقوط.
2. **التوسيع = رفع كثافة الروابط في الأنواع الضعيفة + رفع تمثيل المدارس الرفيعة قبل إضافة مفكرين جدد.** المدرسة ذات المفكر الواحد لا تحتاج مفكراً ثانياً بقدر ما تحتاج شبكة حول مفكرها الوحيد.
3. **كل خطوة قابلة للتحقق آلياً.** الـAuditor-model يحصل على سكريبت تحقق واحد لكل بند في الخطة.

## 1.4 الخريطة الاستراتيجية (5 طبقات، متسلسلة بالتبعية)

```
[Layer 0] التثبيت التشغيلي          ← idempotent، يجب في كل جلسة
    ↓
[Layer 1] جودة المحتوى (تدقيق)     ← يُغلق ~6,500 خطأ محتوى
    ↓
[Layer 2] كثافة الروابط             ← يُغلق 5 orphans + 184 empty related + ضعف 9 أنواع
    ↓
[Layer 3] توسيع التغطية             ← 336 مدرسة ضعيفة + فجوات الأنواع
    ↓
[Layer 4] ذكاء الشبكة + التوثيق     ← مصفوفة + تحليل + handoff
```

**التبعيات الحرجة (لماذا الترتيب هكذا):**
- L0 → L1: لا يمكن إعادة تدقيق الملفات قبل تطبيق إصلاحات الجلسة السابقة.
- L1 → L2: الملفات التي ستُدمج أو تُعاد تسميتها في L1 ستفسد أي `related` يُضاف في L2.
- L2 → L3: نحتاج رؤية نظيفة للروابط لنعرف أي المدارس ما زالت ضعيفة.
- L3 → L4: لا يمكن تحليل الشبكة قبل اكتمال البيانات.
- L4 → تسليم: بدون توثيق، الـAuditor لا يمكنه التحقق.

---

# 2. الحالة التفصيلية قبل البدء (Baseline)

## 2.1 كثافة الروابط حسب نوع الملف

| النوع | عدد الملفات | متوسط related | % بصفر related | % بـ 1-3 | % بـ 7+ |
|---|---|---|---|---|---|
| `dialogues` | 47 | 1.02 | **46.8%** | 51.1% | 0.0% |
| `axioms` | 48 | 1.75 | **39.6%** | 43.8% | 0.0% |
| `events` | 135 | **0.61** | **65.9%** ⚠️ | 31.9% | 0.7% |
| `relations` | 98 | 2.58 | 55.1% | 9.2% | 18.4% |
| `debates` | 161 | 1.91 | **38.5%** | 43.5% | 4.3% |
| `branches` | 234 | 2.19 | 37.2% | 39.7% | 7.3% |
| `concepts` | 893 | 2.01 | **35.4%** | 46.2% | 3.0% |
| `works` | 609 | 1.13 | **37.8%** | 56.8% | 0.3% |
| `critiques` | 99 | 2.97 | 40.4% | 27.3% | 16.2% |
| `thinkers` | 2,188 | 3.19 | 8.4% | 60.1% | 7.8% |
| `schools` | 369 | **19.50** | 0.0% | 33.9% | 21.4% ✅ |

**الاستنتاج:** `events`, `works`, `concepts`, `debates` هي الفجوات الأكبر في كثافة الروابط. `schools` و `disorders` و `critiques` كثافتها ممتازة.

## 2.2 توزيع المدارس

| حجم المدرسة (مفكرين) | عدد المدارس | النسبة |
|---|---|---|
| ≤ 2 مفكرين | **336** | **60%** |
| 3-5 | 153 | 27% |
| 6-10 | 64 | 11% |
| 11-20 | 4 | <1% |
| > 20 | 6 | 1% |

**أعلى 5:** الوجودية (299)، التحليل النفسي (226+81)، المعرفية-السلوكية (29)، السلوكية (28)، علم نفس الجسد (24).

**المشكلة:** الـ 336 مدرسة ضعيفة (≤2) هي حيث يوجد أكبر قدر من "الهواء" — ملف مدرسة + ملف مفكر واحد أو اثنين = شبكة مفقودة.

## 2.3 حالة الـ 5 orphans المتبقية

| Slug | النوع | العنوان |
|---|---|---|
| `sch-cbt` | schools | العلاج المعرفي السلوكي |
| `tec-cbt-emo-self-compassion-exercises` | techniques | تمارين الرأفة بالذات |
| `tec-cbt-mind-body-scan` | techniques | مسح الجسد |
| `tec-dbt-dt-radical-acceptance` | techniques | التقبل الجذري |
| `tec-dbt-dt-urge-surfing` | techniques | ركوب موجة الرغبة الملحة |

**ملاحظة:** هذه كلها CBT/DBT — مما يعني أن `sch-cbt` و `sch-dbt` (التي هي مدرسة كبيرة بـ 369 ملف approved) لا تُشير إلى تقنياتها، أو أن هذه التقنيات لا تُشير إلى المدرسة. مشكلة اتساق داخل المدرسة الواحدة.

## 2.4 ملف الـ 5 مسودات في `drafts/`

```
content/ar/drafts/thinkers/thk-rsterba.md.bak   # نسخة احتياطية، ليست مسودة حقيقية
```

**ملاحظة:** مجلد `drafts/thinkers/` به ملف واحد فقط، وهو نسخة احتياطية `.bak`. كل المسودات الفعلية التي يذكرها الـmemory هي في `content/ar/drafts/EXISTING_SLUGS.md` و `PATCH_SUGGESTIONS.md` — معظمها مدمج في المحتوى المعتمد.

---

# 3. الخطة التفصيلية — 5 طبقات، 18 مهمة، ~75 نشاطاً

> **رمز التبعية:** `[L0]` `[L1]` `[L2]` `[L3]` `[L4]` · `→` = "يفتح/يُغذِّي" · `⇄` = "تبادل ثنائي الاتجاه"
> **المخرج (Deliverable):** كل مهمة لها ملف/سكريبت/تقرير ملموس
> **معيار القبول (Acceptance):** أمر تحقق واحد على الأقل

---

## Layer 0 — التثبيت التشغيلي (يجب تنفيذه أولاً، كل جلسة)

### مهمة 0.1: تطبيق تراكمات التدقيق السابقة
**الوصف:** تشغيل `reapply_thinkers_audit.py` لتطبيق التصحيحات المُخزَّنة في `scripts/thinkers_audit_fixes.json`.
**التبعيات:** لا شيء (السكريبت idempotent بعد 2026-08-23).
**المخرج:** تأكيد أن 0 تصحيحات جديدة تم تطبيقها في التشغيلة الثانية.
**معيار القبول:**
```bash
python3 scripts/reapply_thinkers_audit.py --apply   # التطبيق
python3 scripts/reapply_thinkers_audit.py --apply   # التحقق (يجب: 0 تغيير)
```
**مخاطرة:** إذا أُعيد تخزين تصحيحات بين الجلستين، التطبيق يطبّقها. هذا هو المطلوب.

### مهمة 0.2: تحديث فهرس الـslugs
**الوصف:** إعادة بناء `EXISTING_SLUGS.md` ليعكس الحالة الراهنة.
**المخرج:** ملف `EXISTING_SLUGS.md` محدَّث.
**معيار القبول:**
```bash
python3 scripts/build_slug_index.py
wc -l content/ar/drafts/EXISTING_SLUGS.md   # يجب: ~6478-6500
```

### مهمة 0.3: فحص السلامة كـbaseline
**الوصف:** توثيق الأرقام الحالية في تقرير baseline (للمقارنة اللاحقة).
**المخرج:** `agents_specs/minimax-baseline-2026-08-24.md`.
**معيار القبول:** الملف يحوي أرقام الأقسام 2.1، 2.2، 2.3 أعلاه.

---

## Layer 1 — جودة المحتوى (تدقيق 1,301 ملف متبقي + إغلاق الفجوات النوعية)

### مهمة 1.1: استكمال تدقيق الـ 1,301 thinker المتبقي
**الوصف:** قراءة الملفات بالترتيب الأبجدي من `scripts/audit_unread_thinkers.txt`، تطبيق التصحيحات على دفعات ~28 ملفاً.
**التبعيات:** `→ L1.2, L1.3, L1.4, L1.5, L1.6` (الملفات هنا قد تحتوي على boilerplate، DRAFT-UNKNOWN، تاريخ مغلوط، تعارضات).
**المخرج:** `scripts/thinkers_audit_fixes.json` يضاف إليه ~6,500 تصحيح.
**معيار القبول:**
```bash
wc -l scripts/audit_unread_thinkers.txt   # يجب: 0
ls scripts/thinkers_audit_fixes.json | xargs wc -l   # زيادة ~6,500 سطر
```
**نشاط 1.1.1:** دفعات 1-7 (الـ 400 الأولى من القائمة) — تدقيق محتوى كامل (هوية، تواريخ، كتب، مدارس).
**نشاط 1.1.2:** دفعات 8-14 (الـ 400 التالية) — التركيز على ترجمات الأسماء الأجنبية والـ`en` slug.
**نشاط 1.1.3:** دفعات 15-20 (الـ 500 الأخيرة) — تنظيف boilerplate ونقل `DRAFT-UNKNOWN` الظاهر.

### مهمة 1.2: إغلاق الـ 184 ملف boilerplate (related فارغ + جسم قالب)
**الوصف:** اتخاذ قرار لكل ملف من `scripts/audit_boilerplate_shells.txt`:
- إما كتابة محتوى حقيقي (الأولوية للمفكرين المعروفين)
- وإما نقله إلى `drafts/` بنص واضح
- وإما وسمه كمدخل تعريفي مختصر

**التبعيات:** `→ L2.2` (إضافة `related` تتطلب وجود محتوى).
**المخرج:** `agents_specs/boilerplate-decisions.md` يحوي قرار كل ملف.
**معيار القبول:**
```bash
python3 -c "
import os, re
empty = 0
for f in os.listdir('content/ar/thinkers'):
    if not f.endswith('.md') or f.startswith('_'): continue
    c = open(f'content/ar/thinkers/{f}').read()
    if re.search(r'^related:\s*$', c, re.MULTILINE) and not re.search(r'^related:\s*\n\s*-\s+id:', c, re.MULTILINE):
        empty += 1
print(f'Empty related: {empty}')"   # يجب: 0
```

### مهمة 1.3: حل الـ 30 تعارض slug/identity
**الوصف:** كل حالة في `AUDIT_HANDOFF.md §5.3` لها خيار: (أ) إعادة تسمية الـslug، (ب) إضافة `gaps`، (ج) إعادة تسمية الـ`en` فقط.
**التبعيات:** أي إعادة تسمية slug تكسر كل الروابط الخارجية → يُنفَّذ بالتنسيق مع `L1.4` و `L2.1` (التحديث بعد).
**المخرج:** `scripts/slug_identity_decisions.json` يوثق كل قرار.
**معيار القبول:** الـAuditor يقرأ الملف ويتحقق أن لكل واحد من الـ30 اسم قرار موثَّق.

### مهمة 1.4: إعادة دمج الـ 48 زوج مكرر (مع 27 جديد)
**الوصف:** من `scripts/thinker_merge_plan.json` — نقل محتوى الـ`drop` إلى `keep`، نقل كل الـ`related`، ثم نقل `drop.md` إلى `_merged/`.
**التبعيات:** `⇄ L1.1` (الجلسات المتوازية قد تُعيد الدمج تلقائياً — يحتاج تنسيق).
**المخرج:** تقرير `agents_specs/merges-2026-08-24.md` يحوي: keep، drop، عدد related المنقول، السجلات المتأثرة.
**معيار القبول:**
```bash
python3 scripts/merge_thinker_duplicates.py --plan scripts/thinker_merge_plan.json
ls content/ar/_merged/ | wc -l   # يجب: ≥ 48
python3 scripts/audit_unverified_links.py   # يجب: 0
```

### مهمة 1.5: تنظيف 237 `[DRAFT-UNKNOWN]` ظاهر
**الوصف:** الملف إما يُكتب نصه الكامل، أو يُنقل إلى `drafts/` بنص واضح.
**التبعيات:** `→ L1.2` (نفس آلية البوilerplate).
**المخرج:** تقرير في `agents_specs/draft-unknown-resolved.md`.
**معيار القبول:**
```bash
grep -rl '\[DRAFT-UNKNOWN\]' content/ar/thinkers/   # يجب: 0 ملف
```

### مهمة 1.6: إصلاح 182 `active_end: مستمر` لأشخاص متوفين
**الوصف:** استبدال بقيمة تاريخ الوفاة الفعلي.
**المخرج:** `scripts/active_end_fixes.json` ثم `reapply`.
**معيار القبول:** السكريبت الجديد `scripts/check_active_end_dead.py` يعطي 0 نتيجة.

### مهمة 1.7: حل cross-part duplicate (1 حالة)
**الوصف:** `thk-cgrob` (philosophy) ≡ `thk-charles-grob` (psychology) — نفس الشخص، نفس `en`. الإجراء: حذف `thk-cgrob` ودمج `related` في `thk-charles-grob` (psychology هو الموضع الصحيح تبعاً لـPROJECT_PLAN §5.2).
**المخرج:** `thk-cgrob.md` منقول إلى `_merged/`.
**معيار القبول:**
```bash
ls content/ar/thinkers/thk-cgrob.md   # يجب: not found
python3 scripts/spark_integrity_audit.py   # يجب: 0 cross-part dupes
```

### مهمة 1.8: حل 3 EN-duplicate pairs
**الوصف:** `con-confucian-ren` ≡ `con-ren-humaneness-confucianism`، `con-land-ethic-leopold` ≡ `con-land-ethic`، `con-li-ritual-propriety` ≡ `con-li` — توحيد الـslug والـ`en` بعد موافقة رئيس التحرير.
**المخرج:** `agents_specs/en-dup-decisions.md` يوثق كل قرار.
**معيار القبول:**
```bash
python3 scripts/spark_integrity_audit.py   # يجب: 0 EN dupes
```

---

## Layer 2 — كثافة الروابط (إغلاق الـ5 orphans + رفع كثافة 9 أنواع ضعيفة)

### مهمة 2.1: إغلاق الـ 5 orphans المتبقية
**الوصف:**
- `sch-cbt` → يحتاج `related` يشير إلى 3 من كبار مفكريه (مثلاً `thk-beck`, `thk-ellis`).
- 4 تقنيات CBT/DBT → كل واحدة تحتاج `related: sch-cbt` أو `sch-dbt` حسب المدرسة.

**التبعيات:** `→ L2.5` (bidirectional update).
**المخرج:** الملف الخمسة محدَّث.
**معيار القبول:**
```bash
python3 scripts/minimax_orphan_audit.py   # يجب: "Total orphans: 0"
```

### مهمة 2.2: ملء `related` الفارغ في الـ184 thinker (L1.2)
**تبعيات:** `← L1.2` (يجب أن يكون المحتوى موجوداً).
**المخرج:** كل ملف له ≥ 3 related.
**معيار القبول:**
```bash
# السكريبت أدناه يُفترض إنشاؤه في L2.0
python3 scripts/check_empty_related.py   # يجب: 0
```

### مهمة 2.3: رفع كثافة 9 أنواع ضعيفة (الجدول في §2.1)
**الوصف:** الترتيب حسب الأولوية (النسبة الأعلى بصفر related أولاً):
1. `events` (65.9% بصفر) → هدف: <10%
2. `dialogues` (46.8%) → هدف: <10%
3. `axioms` (39.6%) → هدف: <10%
4. `debates` (38.5%) → هدف: <10%
5. `works` (37.8%) → هدف: <10%
6. `branches` (37.2%) → هدف: <10%
7. `concepts` (35.4%) → هدف: <15%
8. `critiques` (40.4%) → هدف: <20%
9. `relations` (55.1%) → هدف: <20%

**التبعيات:** `→ L2.5` (bidirectional).
**المخرج:** تقرير `agents_specs/connection-density-2026-08-24.md` يحوي الأرقام قبل/بعد لكل نوع.
**معيار القبول:** السكريبت `python3 scripts/connection_density_report.py --target events` يطبع الأرقام الجديدة.

### مهمة 2.4: إضافة cross-school relations (rel-*-*) للمدارس الرفيعة
**الوصف:** الـ98 ملف `relations/` الحالي يغطّي جزءاً من شبكة المدارس. نحتاج إضافة:
- علاقة بين كل مدرستين متجاورتين تاريخياً (مثلاً: CBT ↔ السلوكية، CBT ↔ الإنسانية، DBT ↔ CBT).
- أولوية للمدارس التي لها ≥ 5 مفكرين.

**التبعيات:** `→ L3.1` (يحتاج بيانات المدرسة مكتملة أولاً).
**المخرج:** +20 ملف `rel-*` جديد على الأقل.
**معيار القبول:**
```bash
ls content/ar/relations/ | wc -l   # يجب: ≥ 118
```

### مهمة 2.5: تحديث bidirectional cross-references
**الوصف:** بعد كل إضافة `related`، الطرف الآخر يجب أن يُحدَّث ليعكس الرابط العكسي.
**التبعيات:** `→ جميع مهام L2 و L3.4`.
**المخرج:** سكريبت `scripts/bidirectional_related_audit.py` يطبع 0 عدم تماثل.
**معيار القبول:**
```bash
python3 scripts/bidirectional_related_audit.py   # يجب: All symmetric
```

### مهمة 2.6: إعادة تشغيل passes إغلاق orphans (15 passes)
**الوصف:** بعد كل L2.x، شغّل `scripts/minimax_orphan_close_pass.py` لإغلاق أي orphans جديدة ناتجة عن الإضافات.
**المخرج:** تقرير في `agents_specs/orphan-passes-log.md`.
**معيار القبول:** 0 orphans في نهاية L2.

---

## Layer 3 — توسيع التغطية (البيانات الجديدة)

### مهمة 3.1: Gap analysis للمدارس الرفيعة (336 مدرسة بـ ≤2 مفكرين)
**الوصف:** لكل مدرسة ضعيفة، تحديد إن كانت:
- (أ) تستحق 5+ مفكرين إضافيين (الكتابة مطلوبة)
- (ب) تستحق البقاء بـ 1-2 مفكرين مع شبكة rich (توسيع related)
- (ج) تكرار لاسم آخر (يُحذف)

**التبعيات:** `→ L3.2, L3.3`.
**المخرج:** `agents_specs/school-gap-analysis-2026-08-24.md` يحوي قرار لكل واحدة من الـ336.
**معيار القبول:** الملف يغطي 336 صف (واحد لكل مدرسة ضعيفة).

### مهمة 3.2: توسيع schools الرفيعة (المجموعة "أ" من 3.1)
**الوصف:** لكل مدرسة مُحدَّدة في 3.1-أ، كتابة/نقل 3-5 مفكرين إضافيين.
**المخرج:** +200-300 thinker جديد (تقدير).
**معيار القبول:**
```bash
python3 -c "
from collections import defaultdict
import os, re
counts = defaultdict(int)
for f in os.listdir('content/ar/thinkers'):
    if not f.endswith('.md') or f.startswith('_'): continue
    c = open(f'content/ar/thinkers/{f}').read()
    m = re.search(r'edges:\s*\n((?:\s*-.*\n)+)', c)
    if m:
        mm = re.search(r'target:\s*\"([^\"]+)\"', m.group(1))
        if mm: counts[mm.group(1)] += 1
weak = sum(1 for v in counts.values() if v <= 2)
print(f'Schools with <=2 thinkers: {weak}')"   # يجب: < 100
```

### مهمة 3.3: توسيع شبكة الـschools الرفيعة (المجموعة "ب" من 3.1)
**التبعيات:** `→ L2.5`.
**المخرج:** كل مدرسة ضعيفة من المجموعة "ب" لها ≥ 5 related.
**معيار القبول:** السكريبت `check_weak_school_density.py` يطبع < 50 مدرسة بكثافة < 5.

### مهمة 3.4: توسيع قسم الجسر (Bridge)
**الوصف:** حالياً bridge = Marx فقط (`part: bridge`). أضف 5-10 أسماء جديدة تستوفي المعيار: "مفكر أثّر في مدرسة نفسية لكنه ليس معالج/باحث نفسي نفسه ولا فيلسوفاً نظامياً بحتاً."
**التبعيات:** `→ L2.5`.
**المخرج:** `agents_specs/bridge-additions-2026-08-24.md` يحوي القائمة المقترحة.
**معيار القبول:**
```bash
grep -l 'part: "bridge"' content/ar/thinkers/ | wc -l   # يجب: ≥ 5
```

### مهمة 3.5: توسيع 9 أنواع ضعيفة (L2.3)
**التبعيات:** `→ L2.3`.
**الوصف:** إضافة ملفات جديدة للأنواع التي ما زالت أرقامها منخفضة.
- `events`: من 135 → هدف 200+
- `debates`: من 161 → هدف 220+
- `works`: من 609 → هدف 750+
- `concepts`: من 893 → هدف 1100+
- `dialogues`, `axioms`, `relations`, `critiques`, `branches`: +20% لكل

**معيار القبول:** السكريبت `scripts/coverage_matrix.py` يطبع الأرقام الجديدة.

### مهمة 3.6: معالجة 5 ملفات placeholder
**التبعيات:** `→ L1.1` (تنبيه ضمن تدقيق).
**المخرج:** كل placeholder له إما محتوى أو نقل إلى `drafts/`.
**معيار القبول:**
```bash
grep -r '\[.*placeholder.*\]' content/ar/ --include='*.md' -l   # يجب: 0
```

---

## Layer 4 — ذكاء الشبكة + التوثيق النهائي

### مهمة 4.1: بناء مصفوفة cross-school (أي مدرسة تتشارك أي مفاهيم)
**التبعيات:** `→ L3` (يحتاج بيانات مكتملة).
**المخرج:** `data/cross_school_matrix.json` + `preview-atlas-cross-school.html`.
**معيار القبول:** المصفوفة تحوي ≥ 50 رابط (concepts مشتركة بين مدرستين أو أكثر).

### مهمة 4.2: تحديد الـhubs والـbridges في الشبكة
**التبعيات:** `→ L4.1`.
**المخرج:** `agents_specs/network-hubs-2026-08-24.md` يحوي أعلى 20 ملفاً من حيث degree centrality.
**معيار القبول:** التقرير قابل لإعادة التوليد عبر `python3 scripts/network_centrality.py`.

### مهمة 4.3: تحديث AUDIT_HANDOFF.md
**التبعيات:** `→ جميع L1, L2, L3`.
**المخرج:** `AUDIT_HANDOFF.md` بحالة 2026-08-25 (بعد التنفيذ).
**معيار القبول:** الأرقام الجديدة تطابق تقارير L1.7, L2.6, L3.2-3.5.

### مهمة 4.4: تحديث PROJECT_PLAN.md
**التبعيات:** `→ L3, L4.1`.
**المخرج:** `PROJECT_PLAN.md` بـ 6 مراحل بدلاً من 5.
**معيار القبول:** مرحلة جديدة "Layer 4: Network Intelligence" موثقة.

### مهمة 4.5: توليد backlog جديد للدورة التالية
**التبعيات:** `→ L3.1, L3.5, L4.1`.
**المخرج:** `agents_specs/cycle-2-backlog.md` يحوي 20-30 بند قابل للتنفيذ.
**معيار القبول:** الـbacklog يحوي بنوداً لكل من: density gaps، thin schools، uncovered events.

### مهمة 4.6: snapshot للـauditor
**التبعيات:** `→ جميع المهام السابقة`.
**المخرج:** `agents_specs/audit-snapshot-2026-08-25.md` يحوي:
- أوامر تحقق كاملة لكل بند في هذه الخطة
- الأرقام baseline والأرقام المتوقعة بعد التنفيذ
- قائمة بجميع السكريبتات/الملفات المُشار إليها

**معيار القبول:** الـAuditor-model يمكنه تشغيل الأوامر في الـsnapshot بدون الرجوع لملفات أخرى.

---

# 4. خريطة التبعيات (Dependency Graph)

```
L0.1 → L0.2 → L0.3
              ↓
L1.1 (تدقيق 1301) → L1.2 (boilerplate 184) → L2.2 (related فاضي)
        ↓                ↓                      ↓
L1.3 (slug/identity)  L1.4 (دمج 48)        L2.3 (كثافة 9 أنواع)
        ↓                ↓                      ↓
L1.5 (DRAFT-UNKNOWN)  L1.6 (active_end)    L2.4 (cross-school rel)
        ↓                ↓                      ↓
L1.7 (cross-part)     L1.8 (EN dupes)      L2.5 (bidirectional)
                                                ↓
                                            L2.6 (orphan passes)
                                                ↓
L3.1 (gap analysis) → L3.2 (توسيع مدارس)
       ↓              ↓
L3.3 (شبكة مدارس)  L3.4 (bridge)
       ↓
L3.5 (توسيع أنواع)  L3.6 (placeholders)
       ↓
L4.1 (مصفوفة) → L4.2 (hubs) → L4.3 (audit handoff)
       ↓                          ↓
L4.4 (project plan)         L4.5 (backlog جديد)
                                   ↓
                              L4.6 (snapshot للمدقق)
```

**Critical path:** L0 → L1.1 → L1.4 → L2.5 → L2.6 → L3.1 → L4.1 → L4.6

---

# 5. تقدير الجهد (Time estimate per task)

| الطبقة | المهمة | الجهد التقديري | العمال المقترحون |
|---|---|---|---|
| L0 | 0.1-0.3 | 15 دقيقة (سكربتات) | 1 (root) |
| L1 | 1.1 (1301 ملف) | 6-8 ساعات | 4 workers متوازيين × 28 ملف/دفعة |
| L1 | 1.2 (184 boilerplate) | 4-5 ساعات | 2 workers (قراءة + قرار) |
| L1 | 1.3 (30 slug) | 1 ساعة (مع قرار بشري) | 1 + human |
| L1 | 1.4 (48 merge) | 2 ساعة | 1 (idempotent) |
| L1 | 1.5-1.6 (DRAFT + active_end) | 1.5 ساعة | 1 |
| L1 | 1.7-1.8 (3 duplicates) | 30 دقيقة | 1 |
| L2 | 2.1 (5 orphans) | 15 دقيقة | 1 |
| L2 | 2.2-2.3 (كثافة) | 4-5 ساعات | 2 workers (related additions) |
| L2 | 2.4-2.5 (cross-school + bidi) | 3-4 ساعات | 1 |
| L2 | 2.6 (passes) | 1 ساعة (سكربتات) | 1 |
| L3 | 3.1 (gap analysis) | 2 ساعة (قراءة) | 1 + human review |
| L3 | 3.2 (schools رفيعة) | 8-12 ساعة | 4-6 workers متوازيين |
| L3 | 3.3-3.4 (شبكة + bridge) | 3 ساعات | 1-2 |
| L3 | 3.5 (توسيع أنواع) | 6-8 ساعات | 3-4 workers |
| L3 | 3.6 (placeholders) | 1 ساعة | 1 |
| L4 | 4.1-4.6 (ذكاء + توثيق) | 3-4 ساعات | 1 |
| **الإجمالي** | | **45-60 ساعة عمل موزعة** | 2-3 جلسات كاملة |

---

# 6. سجل المخاطر (Risk Register)

| # | المخاطرة | الاحتمال | التأثير | التخفيف |
|---|---|---|---|---|
| R1 | جلسات متوازية (Spark/MiniMax) تعيد الملفات بعد دمجها | عالٍ | متوسط | الـmerge idempotent + `reapply` في بداية كل جلسة |
| R2 | إعادة تسمية slug تكسر روابط خارجية | متوسط | عالٍ | L1.3 قبل L2.x (لا تضيف related قبل تثبيت الـslugs) |
| R3 | `[DRAFT-UNKNOWN]` يبقى ظاهر في الإنتاج | متوسط | منخفض | L1.5 + فحص يومي |
| R4 | Orphan count يتذبذب (5 → 0 → 5) بسبب جلسات أخرى | عالٍ | منخفض | L2.6 تشغيل دوري، ليس لمرة واحدة |
| R5 | كثافة related ترتفع شكلياً لكن بأسماء خاطئة | متوسط | عالٍ | فحص جودة: كل إضافة related يجب أن يُقرأ سياقه |
| R6 | خطة التوسع تكتب مفكرين بمواقع خاطئة (part/edges) | متوسط | متوسط | تطبيق `part:` validation script بعد كل دفعة |
| R7 | Auditor-model لا يجد ملف الخطة | منخفض | عالٍ | هذا الملف محفوظ في `ACTION_PLAN_2026-08-24.md` |
| R8 | المستخدم ينتقل لمشروع آخر قبل اكتمال L4 | متوسط | منخفض | L4.3-4.6 قابلة للتأجيل، L0-L2 يجب إكمالها |
| R9 | المدرسة الوجودية وحدها 299 مفكر — ضخامة تخلق تحيز في التوصيات | عالٍ | متوسط | L3.1 يضع cap: لا تُكتب مدرسة جديدة بأكثر من 50 مفكر في هذه الدورة |
| R10 | أخطاء تاريخية في الملفات تُكتشف بعد البناء | عالٍ | عالٍ | L1.1 قبل أي بناء — الـbuild لازم يمرّ على clean data |

---

# 7. دليل التحقق (Verification commands for the Auditor)

**التشغيل الكامل (من 0 إلى Verification):**

```bash
cd "$(git rev-parse --show-toplevel)"

# === Baseline verification ===
python3 scripts/reapply_thinkers_audit.py --apply       # L0.1
python3 scripts/build_slug_index.py                      # L0.2
python3 scripts/minimax_orphan_audit.py                  # L0.3 + L2.1
python3 scripts/audit_unverified_links.py                # L0.3
python3 scripts/spark_integrity_audit.py                 # L0.3
python3 scripts/final_verify_audit.py                    # L0.3

# === Layer 1 verification ===
wc -l scripts/audit_unread_thinkers.txt                  # L1.1: must be 0
ls scripts/audit_boilerplate_shells.txt 2>/dev/null      # L1.2: should not exist
grep -rl '\[DRAFT-UNKNOWN\]' content/ar/thinkers/         # L1.5: must be empty
python3 scripts/check_active_end_dead.py 2>/dev/null     # L1.6: must be 0
python3 scripts/spark_integrity_audit.py                 # L1.7-1.8: 0 dupes

# === Layer 2 verification ===
python3 scripts/connection_density_report.py --target events   # L2.3
python3 scripts/connection_density_report.py --target works    # L2.3
python3 scripts/bidirectional_related_audit.py                 # L2.5

# === Layer 3 verification ===
python3 scripts/coverage_matrix.py                            # L3.5
grep -l 'part: "bridge"' content/ar/thinkers/ | wc -l         # L3.4: ≥ 5
ls content/ar/relations/ | wc -l                              # L2.4: ≥ 118

# === Layer 4 verification ===
ls agents_specs/audit-snapshot-2026-08-25.md                  # L4.6: exists
ls agents_specs/network-hubs-2026-08-24.md                    # L4.2: exists
ls data/cross_school_matrix.json                             # L4.1: exists
```

**السكريبتات الجديدة المتوقعة (L4.6 يجب أن يُولِّدها):**
- `scripts/check_empty_related.py` (L2.2)
- `scripts/check_active_end_dead.py` (L1.6)
- `scripts/connection_density_report.py` (L2.3)
- `scripts/bidirectional_related_audit.py` (L2.5)
- `scripts/network_centrality.py` (L4.2)
- `scripts/coverage_matrix.py` (L3.5)

---

# 8. ما لا تشمله هذه الخطة (Out of scope)

لتوضيح النطاق للمراجع:

1. **الترجمة الإنجليزية** (`content/en/`) — مؤجلة كما في `PROJECT_PLAN.md §5.6`.
2. **المرحلة 5 من PROJECT_PLAN (الفلسفة الكاملة)** — مؤجلة لحين إغلاق علم النفس.
3. **بناء UI/UX** — `preview-atlas-visuals.html` خارج النطاق.
4. **ترحيل إلى قاعدة بيانات** — البنية الحالية markdown فقط.
5. **تحسينات SEO/meta** — خارج النطاق.

---

# 9. المخرج النهائي المتوقع (Expected final state if all layers complete)

| المؤشر | قبل | متوقع بعد |
|---|---|---|
| إجمالي الملفات المعتمدة | 6,435 | **~7,200** (+12%) |
| Thinkers | 2,188 | **~2,500** |
| Events | 135 | **~200** |
| Works | 609 | **~750** |
| Concepts | 893 | **~1,100** |
| مدارس بـ ≤2 مفكرين | 336 | **<100** |
| Orphans | 5 | **0** (مستقر) |
| Cross-part duplicates | 1 | **0** |
| EN duplicates | 3 | **0** |
| Thinkers مع `[DRAFT-UNKNOWN]` | 237 | **0** |
| Thinkers بـ `related` فارغ | 184 | **0** |
| متوسط related (events) | 0.61 | **>3** |
| متوسط related (works) | 1.13 | **>3** |
| متوسط related (concepts) | 2.01 | **>3** |
| `active_end: مستمر` لأموات | 182 | **0** |
| ملفات boilerplate | 184 | **0** |

---

# 10. الاعتمادات (Approvals needed from human)

عدد من القرارات تحتاج موافقة رئيس التحرير (لأنها ليست idempotent أو تكسر روابط):

| # | القرار | المهمة | الأثر |
|---|---|---|---|
| A1 | إعادة تسمية 30 slug (L1.3) | L1.3 | تكسر كل الروابط الخارجية لذلك الـslug |
| A2 | نقل 184 boilerplate إلى drafts (L1.2) | L1.2 | إزالة من الموقع |
| A3 | إضافة 200-300 thinker جديد (L3.2) | L3.2 | إضافة ضخمة للـindex |
| A4 | دمج 3 EN-duplicate pairs (L1.8) | L1.8 | إعادة تسمية slug في كل موضع |
| A5 | توسيع قسم bridge (L3.4) | L3.4 | إقرار القائمة المقترحة |

---

# 11. ملاحظات للـAuditor-model

1. **كل رقم في هذه الخطة قابل للتحقق** عبر الأوامر في §7.
2. **كل مهمة لها معيار قبول واحد على الأقل** يمكن للـAuditor تشغيله آلياً.
3. **خريطة التبعيات في §4** يجب أن تُحترم — لا تتخطى L1.x لتذهب إلى L2.x.
4. **التقرير النهائي** للمدقق يجب أن يشير إلى:
   - عدد المهام المُكتملة (من أصل 18)
   - عدد معايير القبول التي فشلت (من أصل ~25)
   - عدد الاعتمادات البشرية (من A1-A5) التي تم/أو رُفضت
   - أي انحراف عن خريطة التبعيات في §4

5. **Baseline snapshot** محفوظ في هذا الملف (§2) — يجب مقارنة كل رقم "بعد" بهذا الـbaseline.
6. **سجل المخاطر (§6)** يجب مراجعته: هل ظهرت مخاطر جديدة لم تكن متوقعة؟

---

*انتهت الخطة. جاهزة للتدقيق من نموذج ذكاء اصطناعي آخر.*
*الـAuditor-model يجب أن يبدأ من §7 (دليل التحقق).*
