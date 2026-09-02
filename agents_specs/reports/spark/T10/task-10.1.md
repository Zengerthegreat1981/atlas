# Task 10.1
الحالة: مكتمل
المسار: spark | العملية: disorders+syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل + dsm5tr_code/icd11_code | الملفات: 30

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30
dsm5tr_code/icd11_code (أو null+سبب): موجودة سلفاً في أغلب الملفات (اتّبعنا الاتفاق القائم بدل dsm_code/icd_code الحرفي من نص المهمة)

## أمر التحقق
python3 scripts/task.py verify spark 10.1
→
=== تحقق Task 10.1 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **تسمية الحقول**: نص Task 10 يذكر حرفياً `dsm_code`/`icd_code`، لكن الاتفاق القائم فعلياً في ~96 ملف من `dis-` من قبل هو `dsm5tr_code`/`icd11_code`. اتّبعنا الاتفاق القائم للحفاظ على الاتساق عبر المشروع بدل اختراع تسمية حقل جديدة موازية. بعض الوكلاء الفرعيين أضافوا الحقلين معاً (تكراراً) — تم توحيدها لاحقاً بحذف dsm_code/icd_code والإبقاء على dsm5tr_code/icd11_code فقط (أو تحويلهما في dis-borderline-personality.md التي لم تكن تحمل الاسم القديم أصلاً).
- **classification-dsm-5-tr.md / classification-icd-11.md**: ملفا تصنيف عامّان (أنظمة تصنيف نفسها لا اضطراب فردي) — أُضيف لهما فقط "## السقف الإكلينيكي" (توضيح أنهما يوثقان بنية نظام تصنيف لا أداة تشخيص)، بلا "## العلاقة بالمفهوم الفلسفي المقابل" ولا dsm/icd code لأنهما غير منطبقين على ملف تصنيف نفسه.
- **dis-aspergers-disorder-historical.md**: تشخيص أُلغي من DSM-5 (دُمج في dis-autism-spectrum)؛ dsm5tr_code/icd11_code الحاليان = null مع سبب موثق في gaps، وأُضيف حقلا توضيح تاريخي منفصلان (dsm4_code_historical, icd10_code_historical) للكودين القديمين الفعليين دون خلطهما بكودات معتمدة حالياً.
- **dis-borderline-personality.md vs dis-bpd.md**: اكتُشف تكرار كامل — كلاهما يغطي اضطراب الشخصية الحدية بنفس الكود التشخيصي. طبقاً لقاعدة "لا حذف/دمج فعلي للملفات"، أُكمل كل ملف بنفس المعيار (السقف الإكلينيكي، العلاقة الفلسفية، الأكواد)، ووُثِّق في gaps كل ملف ملاحظة صريحة تسمّي الملف الآخر بدقة وتطلب قرار محرر بشري بشأن الدمج/التمييز. **هذه أهم نقطة تحتاج مراجعة محرر بشري في هذه الدفعة.**
- تصحيحات مخالفات preflight موجودة سلفاً عبر الدفعة (لم تنتج عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة لعناوين الملفات الفعلية، حذف كتل edges تشير لـ"classification-dsm-5-tr"/"classification-icd-11" (ليست slugs حقيقية بصيغة مقبولة)، وحذف جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من عدة ملفات.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم فلسفية حقيقية موجودة فعلاً بـ content/ar/concepts/ (مثال: con-addiction, con-mind-body, con-lived-body, con-attention, con-cartesian-doubt-method, con-blind-will-to-life, con-ataraxia, con-wu-wei-non-action, con-social-model-disability, con-the-look-of-the-other-sartre, con-responsibility, con-sadness, con-pleasure, con-maya-cosmic-illusion, con-neurodiversity-affirming, con-false-self-vs-true-self, con-fear, con-adaptation, con-attention, con-guilt، con-trauma) — لم يُخترع أي مفهوم.

## متوقف عنده (لرئيس التحرير)
- **dis-borderline-personality.md ↔ dis-bpd.md**: تكرار كامل موثّق ومُشار له صراحة في gaps كل ملف — يحتاج قرار محرر بشري: دمج أم تمييز نطاق (مثال مقترح من أحد الوكلاء: توجيه أحدهما نحو الرواية المعيشة/السردية والآخر نحو المعايير التشخيصية/التقنيات).
- **dis-aspergers-disorder-historical.md**: تشخيص تاريخي ملغى؛ الكود الحالي null بسبب موثق — قد يحتاج المحرر مراجعة ما إذا كان يجب دمج الملف كلياً مع dis-autism-spectrum.md بدلاً من إبقائه منفصلاً.

## الملفات
content/ar/disorders/classification-dsm-5-tr.md
content/ar/disorders/classification-icd-11.md
content/ar/disorders/dis-acute-stress-disorder.md
content/ar/disorders/dis-adhd.md
content/ar/disorders/dis-adjustment-disorders.md
content/ar/disorders/dis-agoraphobia.md
content/ar/disorders/dis-alcohol-use-disorder.md
content/ar/disorders/dis-anorexia-nervosa.md
content/ar/disorders/dis-antisocial-personality.md
content/ar/disorders/dis-anxiety-due-to-medical.md
content/ar/disorders/dis-arfid.md
content/ar/disorders/dis-aspergers-disorder-historical.md
content/ar/disorders/dis-autism-spectrum.md
content/ar/disorders/dis-avoidant-personality.md
content/ar/disorders/dis-binge-eating-disorder.md
content/ar/disorders/dis-bipolar-i.md
content/ar/disorders/dis-bipolar-ii.md
content/ar/disorders/dis-body-dysmorphic-disorder.md
content/ar/disorders/dis-borderline-personality.md
content/ar/disorders/dis-bpd.md
content/ar/disorders/dis-breathing-related-sleep.md
content/ar/disorders/dis-brief-psychotic.md
content/ar/disorders/dis-bulimia-nervosa.md
content/ar/disorders/dis-cannabis-use.md
content/ar/disorders/dis-catatonia.md
content/ar/disorders/dis-conduct-disorder.md
content/ar/disorders/dis-cyclothymia.md
content/ar/disorders/dis-delayed-ejaculation.md
content/ar/disorders/dis-delirium.md
content/ar/disorders/dis-delusional.md
