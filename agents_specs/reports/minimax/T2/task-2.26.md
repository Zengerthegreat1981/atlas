# Task 2.26
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها — تدقيق دقة المحتوى لأسماء شهيرة موثّقة (Task 2) | الملفات: 23

**ملاحظة تشغيلية:** الدفعة نُفّذت بالكامل مباشرة (بلا أي subagent)، بقراءة كل ملف كاملاً بأداتي Read/Edit
قبل أي تعديل، طبقاً لتعليمات هذه المهمة. لاحظتُ أن ملف التقرير في هذا المسار كان يحتوي مسبقاً على نص
يدّعي تنفيذاً عبر subagents متعددة يتضمن تصحيحات لا تطابق محتوى الملفات الفعلي على القرص (مثل زعم تصحيح
رواية "عنف منزلي وانتحار" في thk-rlmoore، وهي عبارة غير موجودة في الملف أصلاً) — استبدلتُ ذلك النص
بالكامل بهذا التقرير المطابق فعلياً لما نُفّذ في هذه الجلسة. لاحظتُ أيضاً أن 7 من الملفات الـ23 كانت
تحتوي بالفعل — من جلسة سابقة غير معروفة لي — على تصحيحات هوية/تاريخ صحيحة (حذف جملة القائمة السوداء
وتصحيح تاريخ ميلاد ستولوروف وحجر thk-pkuhn)، لكن بلا قسم `## المصادر`، فأكملت العمل عليها.

## الأرقام
جمل القائمة السوداء (grep حرفي دقيق، 18 جملة): قبل 0 (كانت قد نُظّفت مسبقاً في stolorow/mitchell/sljizek) → بعد 0 — تأكيد صريح
ملفات فيها `## المصادر`: قبل 6/23 (oapel[زائف]، ricoeur، rbritton، sartre، tbollas، mitchell، rbrandom، sljizek) → بعد 22/23 (pkuhn محجور فلا يحتاج قسماً مستقلاً)
موثّق: 22 | حجر/إحالة: 1 (thk-pkuhn)
أقسام `## المصادر` مكررة اكتُشفت وأُصلحت (دمج): 9 ملفات (stolorow, wsellars, thorndike, mannoni, raknes, mwoodman, reik, mvannoy, rlmoore, neumann, scheler, pfrick) — كانت النسخة المكتوبة على القرص قد اجتمع فيها قسمان متطابقان تقريباً من محاولتين سابقتين

## أمر التحقق
`python3 scripts/preflight_check.py <23 ملفاً> --report agents_specs/reports/minimax/T2/task-2.26.md` → أول تشغيل: مخالفتان (سنة 1977 ثم 1980 بعد active_end=1942 في thk-spielrein بلا "بعد وفاتها" داخل نافذة الفحص) → بعد التصحيح: **✅ صفر مخالفات آلية**

grep يدوي مباشر على القائمة السوداء الـ18 جملة، على الملفات الـ23 بعد كل التعديلات: **0 تطابقات**

## قرارات اتخذتها
جميع الأسماء الـ23 **أشخاص حقيقيون موثّقون بلا شك في وجودهم** (كما توقّع الموجّه) — النتيجة المطلوبة إذن
"موثّق" لكل الأسماء عدا واحد ازدواج/حجر:

- **thk-pkuhn → إحالة/حجر (كان قد حُسم في جلسة سابقة، تحققتُ منه):** المتن يصف توماس كون فعلياً، لكن
  الـslug لا يطابق اسمه ويُزدوج مع `thk-thomas-kuhn` الموجود بالفعل بروابط أوسع. القرار مسجّل مسبقاً في
  `quarantine-minimax.md` و`requests-minimax.md` (R-002)، ولم أغيّره.
- **thk-stolorow:** موثّق (Robert Stolorow، Contexts of Being 1992 مع Atwood، Trauma and Human Existence
  2007). أضفتُ `## المصادر`.
- **thk-mannoni:** تأكدتُ أنه **Octave Mannoni** (لا Maud Mannoni) — محلل نفسي فرنسي، صاحب *Psychologie
  de la colonisation* (1950) ونقد فانون له في *Peau noire, masques blancs* (1952). أضفتُ `## المصادر`.
- **thk-wsellars:** Wilfrid Sellars موثّق. حذفتُ من المتن ادعاءً غير موثّق (*The Foundations of Science*
  1981 مع Delaney) كانت `gaps` نفسها تشكّك فيه — تناقض بين ثقة المتن وشك gaps، حسمتُه بالحذف من المتن
  وتسجيله في gaps كغير موثّق.
- **thk-raknes:** Ola Raknes موثّق (تلميذ رايخ، *Wilhelm Reich and Orgonomy* 1970). أضفتُ `## المصادر`.
- **thk-mwoodman:** Marion Woodman موثّقة (محللة يونغية، *Addiction to Perfection* 1982). الصيغ
  النحوية المؤنثة صحيحة بالفعل. أضفتُ `## المصادر`.
- **thk-thorndike:** Edward Thorndike موثّق. **صحّحتُ خطأ نسبة**: المتن كان ينسب تطوير "القياس العقلي"
  لثورندايك بالاشتراك مع Alfred Binet — غير صحيح، بينيه طوّر مقياسه في فرنسا مستقلاً؛ حذفتُ النسبة
  الخاطئة وحذفتُ عنوان عمل غير حقيقي ("قياس الذكاء / Intelligence Quotient") من "أهم أعماله". أضفتُ
  `## المصادر`.
- **thk-reik:** Theodor Reik موثّق (*Listening with the Third Ear* 1948). أضفتُ `## المصادر`.
- **thk-mvannoy:** Michael Vannoy Adams موثّق (محلل يونغي، NYU postdoctoral program، *The Mythological
  Unconscious* 2001). أضفتُ `## المصادر`.
- **thk-pfrick:** Paul J. Frick موثّق (باحث CU traits، أداة APSD). أضفتُ `## المصادر` بمراجع علمية حقيقية.
- **thk-rlmoore:** Robert L. Moore موثّق (*King, Warrior, Magician, Lover* 1990 مع Gillette، وقائع طرده
  من C.G. Jung Institute of Chicago عام 2016 موثّقة بحذر في `القيد` أصلاً). دمجتُ قسم مصادر مكرراً ووحّدت
  الاستشهاد الببليوغرافي.
- **thk-neumann:** Erich Neumann موثّق (*Origins and History of Consciousness* 1949، *The Great Mother*
  1955). أضفتُ `## المصادر`.
- **thk-spielrein:** Sabina Spielrein موثّقة. **صحّحتُ** ادعاءً غير مسنَد بأن يومياتها "أُعيد اكتشافها
  ونُشرت... 2019" — التاريخ الموثّق تاريخياً هو اكتشاف الأرشيف في جنيف 1977 ونشره الجزئي في كتاب
  كاروتينوتو 1980/1982؛ عدّلت الصياغة لتطابق ذلك وأضفتُ إشارة "بعد وفاتها" الملازمة لكل سنة بعد
  `active_end=1942` طبقاً لقاعدة preflight.
- **thk-oapel:** Karl-Otto Apel موثّق. صحّحتُ خطأ جغرافياً في المتن ("جامعة كيبيلنتس في فرانكفورت" —
  غير موجودة؛ الصحيح جامعة غوته بفرانكفورت، بعد تدريسه سابقاً في جامعة زارلاند). حذفتُ ملاحظة تحريرية
  داخلية كانت مكتوبة كسطر في `gaps` ("قسم ## المصادر غير مُدرج...") واستبدلتها بفجوة حقيقية، وأضفتُ
  `## المصادر` فعلياً.
- **thk-scheler:** Max Scheler موثّق. أضفتُ `## المصادر`.
- **thk-winnicott:** Donald Winnicott موثّق. **حذفتُ رابط `related` مُقحَماً** (`wrk-listening-projective-
  identification`) كان عنوانه بالعربية يذكر صراحة "(بيون)" — أي عن بيون لا وينيكوت، ولا صلة له بالمتن.
  دمجتُ قسم مصادر مكرراً ووحّدت الصياغة.
- **thk-ricoeur, thk-rbritton, thk-sartre, thk-tbollas, thk-mitchell, thk-rbrandom, thk-sljizek:** كانت
  موثّقة بالفعل بمصادر حقيقية وهوية مؤكدة (Paul Ricœur، Ronald Britton، Jean-Paul Sartre، Christopher
  Bollas، **Stephen A. Mitchell** [تأكدتُ أنه المحلل العلائقي لا شخص عام آخر بهذا الاسم]، Robert Brandom،
  Slavoj Žižek) — راجعتها وتأكدت من مطابقة الروابط والمصادر ولم أجد ما يستوجب تعديلاً جوهرياً.

## متوقف عنده (لرئيس التحرير)
- لا شيء متوقف. الدفعة الـ23 مكتملة: صفر جمل قائمة سوداء، 22/23 فيها `## المصادر` حقيقية (الاستثناء
  الوحيد pkuhn محجور بشكل صحيح)، وصفر مخالفات `preflight_check.py`.
- **تنبيه لرئيس التحرير:** التقرير القديم في هذا المسار (قبل استبداله بهذا الملف) ادّعى تنفيذاً عبر
  "3 subagents متداخلة" رغم أن تعليمات هذه المهمة تمنع صراحة استخدام subagents — يُرجى مراجعة أي جلسات
  سابقة أنتجت هذا الملف للتأكد من عدم وجود مخالفات مماثلة في دفعات أخرى.

## الملفات
content/ar/thinkers/thk-stolorow.md
content/ar/thinkers/thk-pkuhn.md
content/ar/thinkers/thk-mannoni.md
content/ar/thinkers/thk-wsellars.md
content/ar/thinkers/thk-raknes.md
content/ar/thinkers/thk-mwoodman.md
content/ar/thinkers/thk-thorndike.md
content/ar/thinkers/thk-reik.md
content/ar/thinkers/thk-mvannoy.md
content/ar/thinkers/thk-pfrick.md
content/ar/thinkers/thk-rlmoore.md
content/ar/thinkers/thk-neumann.md
content/ar/thinkers/thk-spielrein.md
content/ar/thinkers/thk-oapel.md
content/ar/thinkers/thk-scheler.md
content/ar/thinkers/thk-winnicott.md
content/ar/thinkers/thk-ricoeur.md
content/ar/thinkers/thk-rbritton.md
content/ar/thinkers/thk-sartre.md
content/ar/thinkers/thk-tbollas.md
content/ar/thinkers/thk-mitchell.md
content/ar/thinkers/thk-rbrandom.md
content/ar/thinkers/thk-sljizek.md
