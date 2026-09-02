# Task 10.2
الحالة: مكتمل
المسار: spark | العملية: disorders+syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل + dsm5tr_code/icd11_code | الملفات: 30

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30
dis-gad.md: نموذج ذهبي مكتمل مسبقاً — لم يُلمس، تحقّق فقط من اكتماله.

## أمر التحقق
python3 scripts/task.py verify spark 10.2
→
=== تحقق Task 10.2 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- تسمية الحقول: اتُّبع الاتفاق القائم dsm5tr_code/icd11_code (لا dsm_code/icd_code الحرفي في نص المهمة) للاتساق مع ~96 ملف سابق. لا تكرار حقول في هذه الدفعة.
- dis-depressive-personality-historical.md: فئة اقتُرحت في ملحق أبحاث DSM-IV فقط ولم تُعتمد رسمياً في أي دليل — dsm5tr_code/icd11_code = null مع سبب موثق في gaps.
- dis-gender-identity-disorder-historical.md: تصنيف تاريخي أُلغي واستُبدل بـdis-gender-dysphoria — وُثِّق الانتقال التاريخي بموضوعية معرفية بحتة.
- dis-hwabyung.md: متلازمة ثقافية كورية (culture-bound syndrome) — وُضّح طابعها الثقافي المحدد بدل معاملتها كفئة DSM/ICD عالمية مباشرة.
- dis-frotteuristic-disorder.md: dsm5tr_code أُضيف بثقة (302.89)، لكن icd11_code تُرك null مع سبب موثق في gaps (عدم ثقة كافية بالرقم الدقيق مقارنة بأكواد مشابهة غير متطابقة في ملفات المشروع الأخرى) — بدل تخمين كود.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم حقيقية موجودة فعلاً (أمثلة: con-autonomy-kantian, con-lived-body, con-mind-body, con-memory, con-narrative-identity-ricoeur, con-shame-guilt, con-dichotomy-of-control, con-blind-will-to-life, con-jouissance, con-false-self-vs-true-self, con-pleasure, con-commodity-fetishism, con-sadness, con-body-schema, con-golden-mean-virtue) — لا اختراع مفاهيم.
- تصحيحات preflight موجودة سلفاً عبر الدفعة (غير ناتجة عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة، حذف كتل edges تشير لـ"classification-dsm-5-tr"/"classification-icd-11" (ليست slugs صالحة الشكل)، وحذف/استبدال جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح".

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل. الفجوات المتبقية (أكواد null بسبب موثق) مسجّلة داخل gaps كل ملف.

## الملفات
content/ar/disorders/dis-dependent-personality.md
content/ar/disorders/dis-depersonalization-derealization.md
content/ar/disorders/dis-depressive-due-to-medical.md
content/ar/disorders/dis-depressive-personality-historical.md
content/ar/disorders/dis-developmental-coordination.md
content/ar/disorders/dis-disruptive-mood-dysregulation.md
content/ar/disorders/dis-dissociative-amnesia.md
content/ar/disorders/dis-dissociative-identity.md
content/ar/disorders/dis-encopresis.md
content/ar/disorders/dis-enuresis.md
content/ar/disorders/dis-erectile-disorder.md
content/ar/disorders/dis-excoriation-disorder.md
content/ar/disorders/dis-exhibitionistic.md
content/ar/disorders/dis-factitious.md
content/ar/disorders/dis-female-orgasmic.md
content/ar/disorders/dis-female-sexual-interest-arousal.md
content/ar/disorders/dis-fetishistic.md
content/ar/disorders/dis-frotteuristic-disorder.md
content/ar/disorders/dis-functional-neurological-symptom.md
content/ar/disorders/dis-gad.md
content/ar/disorders/dis-gambling-disorder.md
content/ar/disorders/dis-gender-dysphoria.md
content/ar/disorders/dis-gender-identity-disorder-historical.md
content/ar/disorders/dis-genito-pelvic-pain.md
content/ar/disorders/dis-hallucinogen-use.md
content/ar/disorders/dis-hoarding-disorder.md
content/ar/disorders/dis-hwabyung.md
content/ar/disorders/dis-hypersomnolence.md
content/ar/disorders/dis-illness-anxiety.md
content/ar/disorders/dis-inhalant-use.md
