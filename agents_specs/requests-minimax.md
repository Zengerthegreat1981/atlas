---
status: "نشط — قائمة طلبات بحث معلقة لـMiniMax"
created: "2026-08-26"
last_review: "2026-08-26"
owner: "MiniMax + رئيس التحرير (Mina)"
source: "agents_specs/quarantine-minimax.md — الأقسام التي تتطلب تحققاً خارجياً"
---

# MiniMax — طلبات البحث المعلقة

> **الغرض:** حالات في الحجر قررت MiniMax (و/أو Mina) أنها لا يمكن
> حلها بدون **بحث فعلي** (مكتبة، قواعد بيانات، Google Scholar، صفحة
> المؤلف، إلخ). MiniMax كـ coding agent ما عندوش وصول موثوق لأدوات
> البحث على الإنترنت، فما يحلش هذه الحالات من نفسه.
> كل سطر = سؤال بحثي محدد، ومن ينفّذه يضيف تاريخ النتيجة ويفرّغ الحجر.

---

## تنسيق السجل

| العمود | المعنى |
|---|---|
| **id** | رقم تسلسلي |
| **subject** | الاسم أو الـslug |
| **source** | رقم القسم في الحجر |
| **question** | السؤال البحثي |
| **status** | معلق / بحث جار / مُنحل |
| **result** | ما وجده البحث |
| **decided_at** | تاريخ الحل |

---

## الطلبات المعلقة

### R-014 — لا يوجد br- بعنوان مطابق لـ«العلاج المراعي للعرق والثقافة»

- **subject:** br-race-culturally-aware (لا يوجد — لا معتمد ولا مسودة)
- **source:** مهمة إصلاح روابط belongs_to/relates_to المكسورة (2026-09-02) — `con-race-culturally-aware-therapy.md` (CON-0700) يشير في `edges.belongs_to` إلى `br-race-culturally-aware`. بحث شامل في `branches/` و`schools/` و`drafts/minimax/` لم يجد ملفاً مطابقاً؛ `br-relational-cultural` موضوع مختلف (نظرية العلاقات الثقافية لجان بيكر ميلر) لا يصلح كإحالة.
- **question:** هل يستحق «العلاج المراعي للعرق والثقافة» (ديرالد وينغ سو، جانيت هيلمز، تسعينيات) تياراً مستقلاً؟ إن نعم، افتح slug صحيح (مقترح: `br-race-culturally-aware-therapy`) بمصادر حقيقية (Sue 2010، Helms 1990، Carter 2007، Williams et al. 2014 — كلها مذكورة بالفعل في متن con-race-culturally-aware-therapy.md).
- **status:** معلق
- **result:** — (تُرك الرابط المكسور موثّقاً في `gaps` بدل حذفه أو اختراع بديل، لحين حسم من رئيس التحرير)
- **decided_at:** —

---

### R-012 — لا يوجد ملف مفكر لإرنست هاينريش ويبر ولا لستانلي سميث ستيفنز في الأطلس

- **subject:** إرنست هاينريش ويبر (Ernst Heinrich Weber، قانون ويبر 1834)، ستانلي سميث ستيفنز (Stanley Smith Stevens، قانون الأس 1957)
- **source:** Task 9 (2026-09-01) — أثناء إعادة بناء `related` لملف `con-psychophysics-fechner.md`، الذي يستشهد بقانونيهما (Weber's Law وStevens' Power Law) بوصفهما ركيزتين أساسيتين لعلم النفس الفيزيائي. تحقق فعلي أظهر أن `thk-weber` موجود لكنه مخصص لماكس فيبر (عالم اجتماع)، و`thk-astevens` موجود لكنه مخصص لأنتوني ستيفنز (محلل يونغي)، ولا يوجد ملف مستقل لأي من العالِمين الفعليين.
- **question:** هل يستحق كل من إرنست هاينريش ويبر (فيزيولوجي ألماني، 1795–1878) وستانلي سميث ستيفنز (عالم نفس أمريكي، 1906–1973) ملفاً مستقلاً في الأطلس؟ إن كانت الإجابة نعم، افتح slug جديد صحيح غير محجوز (مقترح: `thk-eweber` أو `thk-ehweber` لويبر، و`thk-sstevens` أو `thk-ssstevens` لستيفنز) بمحتوى مبني على مصادر موثقة. لا تُعِد استخدام `thk-weber` أو `thk-astevens` لأنهما محجوزان فعلياً لشخصين آخرين.
- **status:** معلق
- **result:** — (لم يُربط `con-psychophysics-fechner.md` بأي slug مخترع لهما؛ سُجّلت الفجوة في `gaps` بدل اختراع slug)
- **decided_at:** —

---

### R-013 — لا يوجد `con-secondary-emotion` ولا `con-emotion-regulation` في الأطلس

- **subject:** con-secondary-emotion, con-emotion-regulation
- **source:** Task 9 (2026-09-01) — أثناء إعادة بناء `related` لملف `con-primary-emotion.md`، الذي كانت خانة `gaps` فيه تذكر صراحة "رابط مقترح لم يتحقق بعد: الانفعالات الثانوية (con-secondary-emotion)"، ووسم قسم "## ملاحظة معمارية" (تم حذفه لأنه سقّالة محظورة) بربط إضافي بـ`con-emotion-regulation` (تنظيم الانفعالات) كإطار علاجي أوسع.
- **question:** هل يستحق مفهوم "الانفعالات الثانوية" (Secondary Emotions) في EFT مدخلاً مستقلاً منفصلاً عن `con-primary-adaptive-maladaptive-emotions.md` (الذي يغطي التصنيف الرباعي كاملاً بما فيه الثانوية)؟ وهل يستحق "تنظيم الانفعالات" (Emotion Regulation) مدخل مفهوم عام مستقل عن `tec-stair-nt` (بروتوكول علاجي محدد)؟ إن كانت الإجابة نعم لأي منهما، افتح slug جديد صحيح (`con-secondary-emotion`، `con-emotion-regulation`) بمحتوى موثّق. لا تُخترع الـslug قبل التحقق.
- **status:** معلق
- **result:** — (لم يُربط `con-primary-emotion.md` بهذين الـslug؛ اكتُفي بالإشارة إلى `con-primary-adaptive-maladaptive-emotions.md` و`con-maladaptive-emotion.md` و`tec-stair-nt` الموجودة فعلياً)
- **decided_at:** —

---

### R-009 — لا يوجد ملف مفكر لأشعيا برلين (Isaiah Berlin) في الأطلس

- **subject:** thk-fberlin (يوجد بهذا الـslug، لكن محتواه الفعلي عن "فريد برلين" Fred Berlin، شخص مختلف تماماً — طبيب نفسي أمريكي معاصر، لا علاقة له بإسحاق/أشعيا برلين الفيلسوف)
- **source:** Task 9 (2026-09-01) — أثناء إعادة بناء `related` لملف `con-negative-liberty-berlin.md` (مفهوم أشعيا برلين للحرية السلبية، 1958) وملف `con-positive-liberty-berlin.md`، تبيّن عدم وجود أي ملف `thk-` موثّق لإسحاق/أشعيا برلين (Isaiah Berlin، 1909–1997) في `content/ar/thinkers/`.
- **question:** هل يستحق أشعيا برلين ملفاً مستقلاً في الأطلس (فيلسوف سياسي بريطاني-روسي، صاحب مقالة «مفهومان للحرية» 1958)؟ إن كانت الإجابة نعم، افتح slug جديد صحيح (مقترح: `thk-isaiah-berlin` أو `thk-iberlin`) بسيرة مبنية على مصادر حقيقية (Stanford Encyclopedia of Philosophy، Encyclopaedia Britannica). لا تُعِد استخدام `thk-fberlin` لهذا الغرض لأنه محجوز فعلياً لفريد برلين.
- **status:** معلق
- **result:** — (تعذّر ربط `con-negative-liberty-berlin.md` و`con-positive-liberty-berلin.md` بصاحب المفهوم؛ سُجّلت الفجوة في `gaps` بدل اختراع slug)
- **decided_at:** —

---

### R-010 — ازدواج مؤكَّد: con-political-liberalism ↔ con-overlapping-consensus-rawls

- **subject:** con-political-liberalism (عنوانه "الإجماع المتداخل") و con-overlapping-consensus-rawls (عنوانه "الإجماع التقاطعي والتعددية المعقولة")
- **source:** Task 9 (2026-09-01) — أثناء إعادة بناء `related` للملفين، قُرئ الملفان فعلياً بالكامل بعد ملاحظة سابقة من دفعة 9.18 اقترحت احتمال ازدواج.
- **question:** الملفان يعالجان نفس مفهوم رولز بنفس المصدر (Political Liberalism, 1993) بمحتوى شبه متطابق موضوعياً (نفس التعريف، نفس آلية "التقاطع لا الحياد"، نقد مشابه من ساندل/موف). **تأكيد نهائي: الازدواج حقيقي وليس وهمياً.** القرار المطلوب من رئيس التحرير: هل يُدمَج الملفان في ملف واحد بعد اختيار العنوان الأنسب (والتحويل من الآخر)، أم يُعاد تمييز نطاقهما (مثلاً: أحدهما عن "الإجماع المتداخل" كآلية عامة، والآخر عن "الليبرالية السياسية" كمشروع الكتاب ذاته)؟ لم يُدمَجا في هذه الدفعة بحسب تعليمات Task 9 (ممنوع الدمج، فقط تسجيل التأكيد).
- **status:** معلق
- **result:** تم ربط الملفين ببعضهما بعلاقة `related` صريحة (con-overlapping-consensus-rawls موجودة أصلاً في related الملف الآخر) ريثما يُحسم القرار المعماري.
- **decided_at:** —

---

### R-011 — لا يوجد ملف مفكر لتشارلز ميلز (Charles Mills) في الأطلس

- **subject:** thk-cmills أو ما يعادله (لا يوجد)
- **source:** Task 9 (2026-09-01) — أثناء إعادة بناء `related` لملف `con-political-liberalism.md`، ورد في قسم النقد "الناقد ما بعد الكولونيالي (Mills)" في سياق نقد الإجماع المتداخل الرولزي، لكن لا يوجد ملف `thk-` موثّق لتشارلز ميلز (Charles W. Mills، فيلسوف سياسي أمريكي، صاحب The Racial Contract 1997) في `content/ar/thinkers/`.
- **question:** هل يستحق تشارلز ميلز ملفاً مستقلاً في الأطلس بصفته أبرز ناقد ما بعد كولونيالي/عرقي لنظرية العقد الاجتماعي الرولزية؟ إن كانت الإجابة نعم، افتح slug جديد صحيح (مقترح: `thk-charles-mills`) بسيرة مبنية على مصادر حقيقية.
- **status:** معلق
- **result:** — (تعذّر ربط الإشارة إلى Mills في متن con-political-liberalism.md بصاحب مفهوم؛ تُركت كإشارة نصية فقط دون رابط)
- **decided_at:** —

---

### R-007 — slug جديد لروجر ت. أيمز (Roger T. Ames) — لا تُعِد استخدام thk-rwilliams

- **subject:** thk-rwilliams (محتوى كامل موثّق فعلياً لروجر ت. أيمز، فيلسوف أمريكي، منظّر الكونفوشية المعاصرة، مصادر حقيقية: Ames & Hall 1998/2001، Ames 2010/2011)
- **source:** Task 2.52 (2026-08-27) — علامة تحذير القاعدة 6: الـslug `rwilliams` لا يطابق اسم "Ames" إطلاقاً؛ الملف نفسه كان يحتوي ملاحظة معمارية داخلية تعترف بالخطأ ("الـslug الصحيح thk-rames") دون طلب فعلي.
- **question:** افتح slug جديد صحيح (مقترح: `thk-rames`) وانقل إليه المحتوى المؤرشف في `agents_specs/quarantine-minimax-archive/thk-rwilliams.md.archived.2026-08-27` (خارج نطاق حروف MiniMax إن كان a، وإلا فداخل نطاقي m→z ويمكن تنفيذه في مسار لاحق).
- **status:** مُنحل
- **result:** أُنشئ `thk-rames.md` بالسيرة الكاملة الموثّقة (مصادر: Ames & Hall 1998/2001، Ames 2010). `thk-rwilliams.md` حُوّل لإحالة دائمة تشير إلى `thk-rames`. preflight_check نظيف.
- **decided_at:** 2026-08-27

### R-008 — slug جديد لأكينسولا أكيووو (Akinsola A. Akiwowo) — لا تُعِد استخدام thk-rcabrera

- **subject:** thk-rcabrera (محتوى كامل موسّع لأكينسولا أكيووو، عالم اجتماع وأنثروبولوجي نيجيري 1926/1928–1990، نظرية «أجوبي أجوبي» 1976)
- **source:** Task 2.52 (2026-08-27)، امتداد لملاحظة سابقة من Task 2.39 حول رابط thk-okot-pbitek — علامة تحذير القاعدة 6: الـslug `rcabrera` لا يطابق اسم "Akiwowo" إطلاقاً؛ الملف كان يعترف في `gaps` بأن "ريتشارد كابريرا" غير موجود ثم ينشر سيرة أكيووو كاملة الشكل تحت نفس الـslug المضلل — وهو بالضبط ما تمنعه القاعدتان 6 و11.
- **question:** افتح slug جديد صحيح (مقترح: `thk-aakiwowo`) وانقل إليه المحتوى المؤرشف في `agents_specs/quarantine-minimax-archive/thk-rcabrera.md.archived.2026-08-27`، ثم أعد ربط الملفات الخمسة (thk-asante، thk-hountondji، thk-wiredu، thk-bodunrin، sch-african-psychology) بالـslug الجديد.
- **status:** معلق
- **result:** — (الملف الحي `thk-rcabrera.md` حُوّل لقالب حجر/إحالة؛ الروابط الخمسة الواردة إليه أُزيلت مؤقتاً)
- **decided_at:** —


### R-006 — slug جديد لتويين فالولا (Toyin Falola) — لا تُعِد استخدام thk-twolofor

- **subject:** thk-twolofor (محتوى مسودة سابقة استبدله بسيرة تويين فالولا Toyin Falola، مؤرخ نيجيري، مواليد 1953، أستاذ كرسي جوليا تافت في جامعة تكساس في أوستن)
- **source:** Task 2.51 (2026-08-27) — علامة تحذير القاعدة 6: الـslug `twolofor` لا يطابق اسم فالولا إطلاقاً ولا أي اسم حقيقي آخر معروف؛ المسودة السابقة اعترفت بالمشكلة في `gaps` ثم نشرت سيرة كاملة الشكل رغم ذلك، وهو بالضبط ما تمنعه القاعدة 6 والقاعدة 11.
- **question:** هل يستحق تويين فالولا ملفاً مستقلاً في الأطلس (مؤرخ لا عالم نفس، لكن عمله مرجع في نقد الاستيراد المعرفي لعلم النفس الأفريقي)؟ إن كانت الإجابة نعم، افتح slug جديد صحيح (مقترح: `thk-tfalola` أو `thk-toyin-falola`) بسيرة مبنية على مصادر حقيقية (Encyclopaedia Britannica، صفحته المؤسسية بجامعة تكساس في أوستن، إلخ). لا تُعِد استخدام `thk-twolofor` لهذا الغرض.
- **status:** مُنحل
- **result:** أُنشئ `thk-tfalola.md` بسيرة حقيقية موثّقة (Toyin Falola Network، UT Austin، Wikipedia). أُعيد ربط الملفات الثلاثة (`thk-asante.md`، `thk-hountondji.md`، `sch-african-psychology.md`) بالـslug الصحيح. `thk-twolofor.md` بقي إحالة/توضيح بلا سيرة (لا يزال هوية غير معروفة). preflight_check نظيف.
- **decided_at:** 2026-08-27

---

### R-003 — slug صحيح لكاملِش دي. باتيل / داجي (thk-sdesha لا يطابق الاسم)

- **subject:** thk-sdesha (محتواه الفعلي: Kamlesh D. Patel، المعروف بـ"داجي" Daaji، مواليد 28 سبتمبر 1956، الرئيس الرابع لبعثة شري رام تشاندرا ومرشد حركة Heartfulness)
- **source:** Task 2.40 (2026-08-27) — علامة تحذير القاعدة 6: الـslug `sdesha` لا يطابق اسم الشخص (Kamlesh/Patel/Daaji) بأي صورة.
- **question:** ما الـslug الصحيح؟ اقتراحان: `thk-kamlesh-patel` أو `thk-daaji`. تحقّق عبر ويكيبيديا الإنجليزية (Kamlesh Patel (Daaji)) وheartfulness.org قبل الإنشاء، والتزم بمعيار المصادر في القاعدة 5 (لا تُعِد استعمال ادّعاءات غير موثّقة من النسخة المحجورة مثل أرقام "5 مليون ممارس" أو تفاصيل دراسات fMRI دون تحقق).
- **status:** معلق
- **result:** — (الملف الحي `thk-sdesha.md` حُوّل مؤقتاً لقالب حجر بدل نشر سيرة تحت slug مضلل)
- **decided_at:** —

---

### R-002 — slug صحيح لتوماس كون (ازدواج thk-pkuhn / thk-thomas-kuhn)

- **subject:** thk-pkuhn (محتواه الفعلي: توماس كون Thomas Kuhn، 1922–1996)
- **source:** Task 2 (2026-08-27) — علامة تحذير القاعدة 6: الـslug `pkuhn` لا يطابق اسم الشخص المكتوب عنه المتن إطلاقاً، وهو ازدواج فعلي مع `thk-thomas-kuhn` (نفس الشخص، نفس التواريخ، مرتبط بروابط أكثر: 8 مقابل 4). `EXISTING_SLUGS.md` كان يسجّل `thk-pkuhn` كـ"معتمد ✅" رغم هذا التعارض — قرار سابق غير سليم.
- **question:** هل نعتمد `thk-thomas-kuhn` كالـslug النهائي لتوماس كون، ونحوّل `thk-pkuhn` لإحالة دائمة (`redirect_to`) بعد تحديث الروابط الواردة الأربعة إليه؟ (ملاحظة: يوجد أيضاً `thk-kuhn` = رولاند كون، و`thk-lkuhn` = ليندا كون — أسماء مختلفة حقيقية، لا تعارض معها.)
- **status:** مُنحل جزئياً — بقي طلب تنسيق واحد لـSpark
- **result:** `thk-thomas-kuhn` مؤكَّد كـslug نهائي (أُضيف له `## المصادر` كان ناقصاً). `thk-pkuhn.md` إحالة دائمة. صُحح الرابط الوارد في `sch-phil-science.md` (ضمن مجلداتي). **باقٍ:** `content/ar/works/wrk-kuhn-structure-revolutions.md` (ملف Spark) لسه بيشاور على `thk-pkuhn` في `author_slug` و`edges` — خارج نطاق كتابتي، يحتاج تصحيح من مسار Spark لـ`thk-thomas-kuhn`.
- **decided_at:** 2026-08-27 (جزئي)

---

### R-001 — هل Sandra Lindaman = Sandra Booth؟ (مجال Theraplay)

- **subject:** thk-sbooth
- **source:** القسم 3a (تعارض هوية)
- **question:** هل Sandra Lindaman (محتوى ملف thk-sbooth) هو نفس الشخص مثل Sandra Booth في Theraplay Institute؟ أو: هل الاسم الكامل الحقيقي هو "Sandra Lindaman Booth" أو "Sandra Booth Lindaman" (اسم مركّب)؟ أو: شخصان مختلفان؟ المصدر: الصفحة الرسمية لمعهد Theraplay، فهرس كتب Theraplay، Google Scholar لـ"S Lindaman Theraplay".
- **status:** معلق
- **result:** —
- **decided_at:** —

---

### R-002 — هل Marek Cieslak مفكر فنومينولوجي؟

- **subject:** thk-mcieslak (دفعة 1.1)
- **source:** القسم 1 (عاجل)
- **question:** ابحث عن Marek Cieslak في السياق الفنومينولوجي / علم النفس الظاهراتي / التحليل النفسي.هل هو عالم نفس بولندي معاصر؟ أم الاقتصادي / طبيب الأعصاب المعروف في أدب القمار؟ أم شخص آخر تماماً؟ المصدر: Google Scholar، PhilPapers، APA PsycNet، الجامعة البولندية.
- **status:** معلق
- **result:** —
- **decided_at:** —

---

### R-003 — هل Walter Boechat شخصية تحليلية يونغية فعلية؟

- **subject:** thk-wboechat
- **source:** القسم 1 (عاجل)
- **question:** ابحث عن Walter Boechat في التحليلية اللاتينية، خصوصاً AJB (Associação Junguiana do Brasil). هل هو رئيس AJB فعلاً؟ ما هي منشوراته / مساهماته الموثقة؟ المصدر: IAAP، AJB، C.G. Jung Institut Zürich-Küsnacht، Rivista di Psicologia Analitica.
- **status:** معلق
- **result:** —
- **decided_at:** —

---

### R-004 — حالة الملفات الـ227 ذات DRAFT-UNKNOWN: الفصل النهائي

- **subject:** ~227 ملف thk-* فيها DRAFT-UNKNOWN في frontmatter
- **source:** تحليل منهجي لـgrep
- **question:** بعد تطبيق الحجر على الملفات المعلومة، الـ227 الباقية تستحق **فصلاً منهجياً**:
  1. DRAFT-UNKNOWN + اعتراف بعدم التوثيق → الحجر (الأقسام 1-2).
  2. DRAFT-UNKNOWN + سيرة واثقة → عاجل (الأقسام 1 و3 و7).
  3. DRAFT-UNKNOWN فقط (في frontmatter) → قيد إنتاج، يُراجع في sub-task لاحق.

  **السؤال البحثي الرئيسي:** أي من الـ227 الباقية (بعد تطبيق الحجر) تندرج تحت (3) "قيد إنتاج" مقابل (1)+(2) "حجر أو عاجل"؟ تطلب مراجعة ملف-بملف أو grep أعمق.
- **status:** معلق
- **result:** —
- **decided_at:** —

---

### R-005 — روابط related مكسورة: تحقق مجمّع

- **subject:** ~10 ملفات ذات روابط مكسورة بعد إصلاحات القسم 5
- **source:** القسم 5 (روابط مكسورة) - حالات مؤجلة
- **question:** تحقق من الـid وtitle في كل related entry، إصلاح ما يمكن إصلاحه آلياً، تسجيل ما يحتاج بحثاً:

  1. **thk-theresaglasser:** id="thk-sgreys" title="دانيال هيوز" - هل sgreys = Daniel Hughes؟ تحقق في DDP Institute.
  2. **thk-margaretbodkin:** id="thk-eugenetaylor" title="يوجين تيلور" - هل هذا Eugene Taylor (Harvard, William James scholar)؟ تحقق.
  3. **thk-ppapp:** id="thk-bcarter" title="بيتي كارتر" - Betty Carter (المعالجة الأسرية)؟ id="thk-mwalter" title="مارجريت لورنسون فالتر" - هل Margaret Lorentzen Walter (المعالجة الأسرية)؟ id="thk-ackerman" title="ناثان أكيرمان" - Nathan Ackerman.
  4. **thk-tandersen:** id="thk-jseikkula" title="ياكو سيكولا" - هل jseikkula = Jaakko Seikkula (Open Dialogue)؟ id="thk-balakare" title="بيرجيتّا ألاكارِ" - من هي؟
  5. **thk-vjohnson:** id="thk-hkaplan" title="هيلين سنغر كابلان" - هل هذا Helen Singer Kaplan (sex therapy)؟ الـaudit قال Harvey Kaplan.
  6. **thk-maxwell-maltz:** id="thk-paulgthomas" title="بول جي. توماس" - من هو Paul G. Thomas في سياق Maltz/Psycho-Cybernetics؟ id="thk-charlesfaulkner" title="تشارلز فولكنر" - Charles Faulkner (NLP).
  7. **thk-rbenenzon:** id="thk-egaston" title="إ. ثوريت غاستون" - E. Thuret Gaston (music therapy)؟ id="thk-mpriestley" title="ماري بريسلي" - Mary Priestley (music therapy)؟ id="thk-sbruscia" title="كينيث بروسيا" - Kenneth Bruscia.
  8. **thk-petersmith:** id="thk-dolweus" title="دان أولِس" - Dan Olweus (bullying research)؟ id="thk-keinarsen" title="ستال إينارسِن" - Stål Einarsen (bullying)؟ id="thk-ssharp" title="سونيا شارب" - Sonia Sharp؟ id="thk-fvolkwein" title="فريد فولكwein" - Fred Volkwein.
  9. **thk-richard-dawkins:** الـaudit قال "ملاحظة: لا أرى تفسير" - تحقق ما إذا كان entry لابديل هو مقصود.
  10. **thk-sschoenwald:** id="thk-shenggeler" title="سكوت هِنغلَر" - Scott Henggeler (MST)، id="thk-cborduin" title="تشارلز بوردوين" - Charles Borduin (MST).

- **status:** معلق
- **result:** —
- **decided_at:** —

---

## ملاحظات

- أي سطر في الحجر يذكر "تحقق فعلي" أو "بحث" يجب أن يحال هنا.
- هذا الملف يُحدَّث كلما تم تنفيذ بحث أو إضافة سؤال.
- طلبات مُنجزة تنقل إلى `requests-minimax-archive/` بتأريخ الحل.

## تعارضات slug عابرة للمسارين (من Task 13.1، 2026-08-27)
- `thk-dgray`: محتوى مختلف تماماً بين `content/ar/thinkers/thk-dgray.md` (مسار MiniMax) و`content/ar/drafts/spark/thinkers/thk-dgray.md` (مسار Spark). يحتاج حسم رئيس التحرير.
- `thk-jgantt`: نفس المشكلة — "جوزيف غانت" (MiniMax) مقابل "سوزان ب. غانت" (Spark، في drafts/spark/thinkers/). يحتاج حسم رئيس التحرير.

## طلبات slug جديدة — من Task 13 (sch-philosophy-of-psychiatry، 2026-08-27)
- طلب slug جديد لـ**K.W.M. Fulford** (كي. دبليو. إم. فولفورد) — مؤسس حقل فلسفة الطب النفسي الأكاديمي، صاحب *Moral Theory and Medical Practice* (1989)، مؤسس مجلة PPP (1994). خارج نطاقي (`thk-` من a إلى l).
- طلب slug جديد لـ**Derek Bolton** (ديريك بولتون) — صاحب *What is Mental Disorder?* (2008). خارج نطاقي.
- طلب slug جديد لـ**Tim Thornton** (تيم ثورنتون) — صاحب *Essential Philosophy of Psychiatry* (2007). خارج نطاقي.

## طلب slug جديد — Task 13 (sch-second-order-cybernetics)
- **subject:** مفكران غائبان مطلوبان لتوثيق `sch-second-order-cybernetics` (السيبرنطيقا من الدرجة الثانية والأوتوبويزيس)
- **source:** Task 13، 2026-08-27
- **question:**
  1. **هاينز فون فورستر (Heinz von Foerster، 1911–2002)** — مؤسس مختبر السيبرنطيقا البيولوجية بجامعة إلينوي (1958–1975)، صاحب مفهوم "المراقب المشارك" وسيبرنطيقا الدرجة الثانية. يحتاج slug جديد (مقترح: `thk-heinz-von-foerster`).
  2. **هومبرتو ماتورانا (Humberto Maturana، 1928–2021)** — عالم أحياء تشيلي، مؤسس مفهوم الأوتوبويزيس مع فرانسيسكو فاريلا (*Autopoiesis and Cognition*، 1972). يحتاج slug جديد (مقترح: `thk-humberto-maturana` أو `thk-maturana`).
- **status:** معلق
- **result:** —
- **decided_at:** —

## طلب slug جديد — Task 2.14 (2026-08-27)
- **subject:** مدرسة "الممارسة الموجَّهة نحو التعافي" (Recovery-Oriented Practice) — لا يوجد لها ملف `sch-` في الأطلس، بينما `thk-patdeegan` (بات ديغان، مؤسسة حركة التعافي) و`thk-dan-fisher` و`thk-wwhite` مرتبطون بها فعلياً في المتن.
- **source:** Task 2.14، مراجعة thk-patdeegan.
- **question:** يُقترح slug جديد مثل `sch-recovery-oriented-practice` لإنشاء ملف مدرسة. حُذف `edges.belongs_to` النص الحر من `thk-patdeegan.md` مؤقتاً لحين الحسم.
- **status:** معلق
- **result:** —
- **decided_at:** —

## طلب slug جديد — Task 2.14 (2026-08-27، تكملة)
- **subject:** مدرسة "تقنيات الحرية الانفعالية" (Emotional Freedom Techniques / EFT-Tapping) — لا تخلط مع `sch-eft` الموجود (Emotionally Focused Therapy للأزواج، مدرسة مختلفة تماماً). `thk-peta-stapleton` باحثة أكاديمية في EFT-Tapping ولا يوجد لها مدرسة صحيحة تنتمي إليها حالياً.
- **source:** Task 2.14، مراجعة thk-peta-stapleton.
- **question:** يُقترح slug جديد مثل `sch-eft-tapping` أو `sch-emotional-freedom-techniques` لتفادي التعارض مع `sch-eft`. حُذف `edges.belongs_to` النص الحر من `thk-peta-stapleton.md` مؤقتاً لحين الحسم.
- **status:** معلق
- **result:** —
- **decided_at:** —

## طلبات من Task 14 (علم النفس العربي الحديث، 2026-08-27)
- `sch-` جديد مطلوب: "المدرسة التكاملية المصرية" أو "علم النفس المصري الحديث" (لربط thk-yusuf-murad وتلاميذه).
- `sch-` جديد مطلوب: "علم نفس الدين" (Psychology of Religion) — لربط thk-pargament بدل الربط الخاطئ المحذوف بـsch-islamic-psychology.
- `thk-` جديد مطلوب: مصطفى عبد الرازق (أستاذ عثمان أمين، مذكور بلا ملف).
- طلب لـSpark: تسجيل سياقات `ctx-` للواقع الإكلينيكي العربي (تقنين الأدوات بالعربية، صدمة الحرب والنزوح في سوريا/العراق/فلسطين/السودان، الشرف والعار في الصياغة الإكلينيكية، عزو الأعراض للجن، الأسرة العربية كنسق علاجي) — من Task 14 الأصلي، لم تُنشأ بعد لأنها خارج نطاق مجلدات MiniMax.

## طلبات لـSpark من Task 17 (أحداث evt- في أخلاقيات البحث، 2026-08-27)
لا عمود فقري لأخلاقيات البحث في الأطلس إطلاقاً — مطلوب من مسار Spark (مجلد events/ ضمن نطاقهم):
- فضح توسكيغي (Tuskegee Syphilis Study exposure, 1972)
- ويلوبروك (Willowbrook State School hepatitis experiments)
- أكتسيون T4 والطب النفسي النازي (Aktion T4)
- بينيل يفكّ قيود مرضى بيسيتر (Pinel at Bicêtre, 1793)
- مطرقة الساحرات (Malleus Maleficarum, 1487)
- بيان واطسون السلوكي (Watson's Behaviorist Manifesto, 1913)
- مقياس بينيه-سيمون (Binet-Simon Scale, 1905)
- تأسيس شبكة سماع الأصوات (Hearing Voices Network founding, 1987)
- لجنة لانسيت للصحة النفسية العالمية (Lancet Commission on Global Mental Health, 2018)

## طلب مراجعة يدوية — thk-jgantt (Task 2، 2026-08-27)

- **subject:** thk-jgantt (جوزيف غانت / Joseph Gantt، THK-1275) — ملف **معتمد**.
- **source:** `agents_specs/quarantine-minimax.md` القسم 9.
- **question/توصية:** بحث ويب فعلي لم يجد أي توثيق مستقل لوجود "Joseph Gantt" ككاتب
  كتاب "Trauma Be Not Proud" (2001) أو كشخصية معروفة في مجتمع السيكودراما
  (Psychodrama Network News إلخ). عنوان الكتاب يحاكي "Death Be Not Proud" الشهير،
  والملف يحتوي فعلاً على جملة قائمة سوداء ("لا يوجد اقتباس مباشر موثوق متاح").
  **التوصية: مراجعة رئيس التحرير يدوياً لـ`thk-jgantt` قبل أي بناء إضافي عليه**
  (عدم ربط ملفات جديدة بهذا الـslug حتى يُحسم — إما حذف، إما نقل لأرشيف الحجر،
  إما إبقاء بوسم صريح كسيرة غير موثقة).
- **status:** معلق
- **result:** —
- **decided_at:** —

## طلبات من eth-apa-ethics-code (Task 17، 2026-08-27)
- `sch-` جديد مطلوب: "الأخلاقيات المهنية الإكلينيكية" أو ما يعادله (لربط eth-apa-ethics-code وبقية مداخل eth- المستقبلية بـbelongs_to).
- `eth-` أو `con-` جديد مطلوب لاحقاً: واجب التحذير (Tarasoff) — لا يوجد حالياً مدخل مخصص له في الأطلس.
- `eth-` جديد مطلوب لاحقاً: مدونة نورمبرغ (1947) وإعلان هلسنكي (1964) — مذكوران في Task 17 كأولوية لكن لم يُنشآ بعد.

## طلب slug جديد — thk-hartshorne (من مراجعة thk-whitehead، 2026-08-27)
- **subject:** تشارلز هارتسشورن (Charles Hartshorne، 1897–2000)، أمريكي، طوّر لاهوت وايتهد
  إلى "اللاهوت العملياتي" (Process Theology) في *The Metaphysics of Whitehead* (1941)، ومذكور
  فعلاً في متن `sch-process-philosophy` تحت "المؤسِّس" و"الأعلام الإضافيون".
- **question/طلب:** لا يوجد ملف `thk-hartshorne` (أو ما يعادله) في `content/ar/thinkers/` ولا في
  `content/ar/drafts/minimax/thinkers/`. مطلوب slug جديد له لإتاحة ربطه من `thk-whitehead` مستقبلاً
  دون اختراع.
- **status:** معلق

## طلب slug جديد — thk-guymanaster (من حجر thk-rmanaster، Task 2.19، 2026-08-27)
- **subject:** غاي ج. ماناستر (Guy J. Manaster)، أمريكي، أستاذ بجامعة تكساس في أوستن، محرر
  *The Journal of Individual Psychology* (من 1976، وبالاشتراك مع جون كارلسون 1982–1995)،
  مؤلف مشارك مع رايموند كورسيني لـ*Individual Psychology: Theory and Practice*، ومحرر
  *Alfred Adler, As We Remember Him* (1977).
- **question/طلب:** الشخص موثّق فعلياً (بحث ويب 2026-08-27)، لكن لا يوجد له ملف بالاسم الصحيح.
  الـslug القائم `thk-rmanaster` كان يحمل سيرة مختلقة باسم "Rachael Manaster" وتم حجره. مطلوب
  slug جديد صحيح (`thk-guymanaster` مقترح) لكتابة سيرته الحقيقية عبر مسار عادي لاحقاً.
- **status:** معلق
- **result:** —
- **decided_at:** —

## تعارضات slug عابرة للمسارين (من Task 13.5، 2026-08-27)
- `thk-gunnel-cederblad`: محتوى مختلف بين `content/ar/thinkers/thk-gunnel-cederblad.md` (معتمد) و`content/ar/drafts/spark/thinkers/thk-gunnel-cederblad.md` (مسودة Spark) — أسماء مختلفة تحت نفس الـslug.
- `thk-jacqueline-astington`: نفس المشكلة — "جاكلين أستنغتون" (معتمد) مقابل "جانيت وايلد أستنغتون" (مسودة Spark).

## روابط مكسورة في ملفات معتمدة (من Task 13.6، 2026-08-27)
- `content/ar/thinkers/thk-pslade.md` و`thk-rlandy-md.md` (معتمدان) يحتويان روابط `related` إلى `con-role-theory`،
  `con-drama-therapy`، `con-child-drama` — الثلاثة غير موجودة فعلياً كملفات. تحتاج تصحيحاً (حذف الرابط أو إنشاء الملف).

## طلب slug جديد — thk-lsperry (من حجر thk-rsperry، Task 2.25، 2026-08-27)
- **subject:** لن سبيري (Len Sperry، MD/PhD)، أمريكي، أستاذ متفرغ بجامعة فلوريدا الأطلسية (FAU) وأستاذ
  إكلينيكي في الطب النفسي بكلية الطب في ويسكونسن، خريج برنامج شهادة العلاج النفسي بمعهد أدلر-شيكاغو
  (الآن Adler University). مؤلف لأكثر من 100 كتاب مهني منها *Psychopathology and Psychotherapy:
  DSM-5-TR Diagnosis, Case Conceptualization, and Treatment* و*Learning and Practicing Adlerian
  Therapy* و*Adlerian Couple Therapy* و*Adlerian Family Therapy*. موثّق ببحث ويب في 2026-08-27
  (AdlerPedia، صفحات جامعته، Routledge، Amazon).
- **question/طلب:** الـslug القائم `thk-rsperry` كان يحمل سيرة مختلقة باسم "Robert Sperry" بنفس
  الببليوغرافيا الأدلرية الحقيقية للن سبيري. تم حجر `thk-rsperry` (انظر `quarantine-minimax.md`
  القسم 3). مطلوب slug جديد صحيح (`thk-lsperry` مقترح) لكتابة سيرته الحقيقية عبر مسار عادي لاحقاً —
  يبدأ بحرف "l" وهو خارج نطاق حروف MiniMax (m→z)، فيحتاج مساراً منفصلاً (Spark أو كلود).
- **status:** معلق
- **result:** —
- **decided_at:** —

## طلب slug جديد — thk-dhughes (من حجر thk-sgreys، Task 2.25، 2026-08-27)
- **subject:** دانيال أ. هيوز (Daniel A. Hughes، PhD)، أمريكي، عالم نفس إكلينيكي، مؤسّس **العلاج
  التفاعلي النمائي الثنائي** (Dyadic Developmental Psychotherapy — DDP)، رئيس معهد DDPI (Dyadic
  Developmental Psychotherapy Institute)، مؤلف *Building the Bonds of Attachment* وغيره. موثّق
  ببحث ويب في 2026-08-27 (ddpnetwork.org، Wikipedia، موقعه الشخصي danielhughes.org).
- **question/طلب:** الـslug القائم `thk-sgreys` كان يحمل هذه السيرة الحقيقية والموثَّقة، لكن اسم
  الـslug ("sgreys") لا يمتّ لاسم "Daniel Hughes" بأي صلة — علامة تحذير صريحة بحسب القاعدة 6 في
  MINIMAX.md. تم حجر `thk-sgreys` (انظر `quarantine-minimax.md` القسم 3) رغم صحة المحتوى، لعدم
  مطابقة الـslug. مطلوب slug جديد صحيح (`thk-dhughes` مقترح) — يبدأ بحرف "d"، خارج نطاق حروف
  MiniMax (m→z)، يحتاج مساراً منفصلاً (Spark أو كلود) لنقل المحتوى الحقيقي (المحفوظ في
  `agents_specs/quarantine-minimax-archive/thk-sgreys.md.archived.2026-08-27`) إليه.
- **status:** معلق
- **result:** —
- **decided_at:** —

## تسجيل روابط محذوفة — Task 3 batch-5 (thk-r→s)، 2026-08-27
- **السياق:** أثناء التدقيق القرائي لدفعة batch-5 (39 ملفاً، thk-rpicard→thk-sspeer)، وُجد نمط
  ممنهج من روابط `related` تستخدم slugs مخترعة (بادئة حرف أول + لقب) لا تطابق أي ملف موجود فعلياً
  في الأطلس، رغم وجود الشخص الحقيقي بـslug مختلف تماماً أو عدم وجوده إطلاقاً.
- **صُحِّحت آلياً** (مطابقة اسم/لقب مؤكدة 1:1 مع ملف موجود): thk-mklein→thk-klein، thk-hsachs→thk-sachs،
  thk-sfreud→thk-freud، thk-jaseikkula→thk-jseikkula، thk-cmohanty→thk-mohanty، thk-nwiener→thk-norbert-wiener،
  thk-jdebeauvoir/thk-jbbutler/thk-jbutler→thk-beauvoir/thk-butler، thk-eharding→thk-meharding،
  thk-jbowlby→thk-bowlby، thk-helderlin→thk-holderlin، thk-ikant→thk-kant، thk-fschelling→thk-schelling،
  thk-jgoethe→thk-goethe، thk-rmay→thk-may، thk-mheidegger→thk-heidegger، thk-poseidonius→thk-posidonius،
  thk-marcusaurelius→thk-marcus-aurelius، thk-musonius→thk-musonius-rufus، thk-hbergson→thk-bergson،
  thk-jdewey→thk-dewey، thk-vfrankl→thk-frankl، thk-hannah-arendt→thk-arendt، thk-kblanchard→thk-ken-blanchard،
  thk-rgriffiths→thk-roland-griffiths، thk-jwatzlawick→thk-pwatzlawick، thk-jalal-rumi→thk-jalal-al-din-rumi،
  thk-mibn-arabi→thk-ibn-arabi، thk-thomas-kirsch→thk-tkirsch، thk-marygergen→thk-mgergen،
  thk-jkabatzinn→thk-jkabat-zinn (+ عدة concepts/تقنيات: con-evidence-based→con-evidence-based-practice،
  con-polyvagal→con-polyvagal-theory، con-existential-motivation→con-fundamental-existential-motivations،
  ins-some→ins-sources-of-meaning-some، tec-alexander→tec-alexander-technique).
- **حُذفت (لا يوجد ملف مطابق، ولا تطابق مؤكد):** thk-tlalev، thk-janderson، thk-fgeorge، thk-rashby
  (Ross Ashby)، thk-allende (سلفادور أليندي)، thk-rmgconrath، thk-bihbarker، thk-dkrigor، thk-phuges،
  thk-pcooper، thk-batter، thk-rhughes، thk-dhughes (طلب منفصل أعلاه لنفس الشخص عبر thk-sgreys)،
  thk-nero، thk-zeno-citium (زينون الكيتيومي، مؤسس الرواقية — **شخص مختلف عن** thk-zeno-elea
  الموجود في الأطلس؛ الأطلس يفتقر لملف مؤسس الرواقية الفعلي)، thk-dzahavi (دان زاهافي)، thk-jgrinder
  (جون غريندر)، thk-mdurie/thk-trore (السير ماسون دوري)، thk-pte-whaiti، thk-mihimere، thk-mshapiro،
  thk-ehauoli، thk-ihiwai، thk-mihaleole، thk-mnona، thk-alamerani، thk-mmontero (ماريثا مونتيرو)،
  thk-taos (معهد لا شخص)، thk-vshalamov (فارلام شالاموف)، thk-jsvetlana (سفيتلانا أليكسييفيتش)،
  thk-rkoch، thk-bhelliwell، thk-rharre (روم هارّيه)، thk-bross، thk-khayes (ستيفن هايز — يوجد
  thk-lstevenhayes لشخص مختلف الاسم الأول، لا تطابق مؤكد)، thk-rcsenge (بيتر سِنغي)، thk-jgoldstein
  (جوزيف غولدشتاين — **تنبيه:** thk-goldstein الموجود هو كورت غولدشتاين، شخص مختلف تماماً؛ لا يجوز
  الربط)، thk-sharon-beckman، thk-tnthich (ثيت نات هان)، thk-mwooffitt ("مارغريت ووفِت" — لا يوجد
  إلا thk-rwooffitt لروبن ووفيت، شخص مختلف)، وعدة concepts/instruments/branches مفقودة تماماً
  (con-vsm، con-cybernetics، con-sensory-processing، con-aba، con-ddp، con-discursive-psychology،
  con-brt، con-decisive-moment، con-rupture-repair، con-gender-identity، con-maori-health،
  con-critical-psychology، con-qualitative-research، con-power-knowledge، con-posture، dis-autism،
  dis-cancer، tec-taoist-cbt، br-metta-meditation، br-ims).
- **status:** معلق — يحتاج قراراً من رئيس التحرير: هل تُنشأ ملفات لهؤلاء المفكرين/المفاهيم الحقيقيين
  الغائبين (دوركهايم-مستوى الأهمية بعضهم: زينون الكيتيومي، فارلام شالاموف، سفيتلانا أليكسييفيتش،
  دان زاهافي، جون غريندر) أم تبقى الروابط محذوفة فقط.
- **decided_at:** —

## Task 9 — طلبات slug جديدة (concepts: con-fitrah-nafs-qalb-model)
- **wrk-** لكتاب "شرح عجائب القلب" (الكتاب 21 من *إحياء علوم الدين* لأبي حامد الغزالي، ت. 505هـ/1111م) —
  المصدر الأساسي لنموذج جسد–نفس–قلب–روح المستخدم في con-fitrah-nafs-qalb-model. غير موجود كملف wrk- مستقل
  (الموجود فقط: wrk-al-ghazali-munqidh، wrk-tahafut-al-falasifa-ghazali، wrk-al-iqtisad-fi-al-itiqad-ghazali،
  wrk-al-munqidh-min-al-dalal-ghazali، wrk-qawaid-al-aqaid-ghazali — لا أحد منها هو الإحياء).
- **con-tazkiyat-al-nafs** (تزكية النفس): مفهوم العملية العلاجية/التعبدية لترقية النفس عبر مراتبها الثلاث
  (أمّارة → لوّامة → مطمئنة)، مذكور ضمنياً في con-fitrah-nafs-qalb-model لكن بلا ملف مفهوم مستقل.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-fear)
- **thk-batja-mesquita** (Batja Mesquita، عالمة نفس ثقافية، مؤلفة *Between Us: How Cultures Create
  Emotions*، 2022): مذكورة بالاسم في متن con-fear («البعد الثقافي») كصاحبة الحجة القائلة إن اعتبار
  المشاعر ملكاً فردياً داخلياً افتراض ثقافي غربي (WEIRD). لا يوجد لها slug في الأطلس إطلاقاً (لا في
  content/ar ولا في drafts)، فتعذّر إضافة رابط `thk-` رغم أن الاسم موثّق في المتن.
- **ملاحظة ازدواج اسم (وليست طلب slug جديد، بل تنبيه لرئيس التحرير):** متن con-fear ينسب نظرية
  التقييم المعرفي للخوف/القلق إلى "لازاروس" ونظرية المشاعر المبنية إلى "ليزا فيلدمان باريت"، لكن
  الـslugs الحيّة `thk-lazarus` و`thk-barrett` في content/ar/thinkers/ تخصّان شخصين مختلفين تماماً
  (أرنولد لازاروس معالج سلوكي، وويليام باريت فيلسوف وجودي). المسودتان الصحيحتان
  (`content/ar/drafts/thinkers/thk-richard-lazarus.md` و`content/ar/drafts/spark/thinkers/thk-lisa-feldman-barrett.md`)
  موجودتان بالفعل لكن غير مُرقّاتين للمحتوى المعتمد؛ لم أربط بهما تجنباً لخلط id/title، وسجّلت
  الملاحظة في `gaps` داخل con-fear.md.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-four-principles-ogden)
- **wrk-subjects-of-analysis-ogden** (اقتراح slug فقط، غير منشأ): كتاب Thomas Ogden «Subjects of
  Analysis» (1994)، المصدر الأساسي لمفهوم المبادئ الأربعة للوظيفة الذهنية في con-four-principles-ogden.md.
  لا يوجد ملف wrk- له في الأطلس حالياً (لم يُنشأ، فقط طلب تسجيل).
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-fully-functioning-person)
- **wrk-on-becoming-a-person** (اقتراح slug فقط، غير منشأ): كتاب كارل روجرز *On Becoming a Person*
  (1961) — المصدر الأساسي المذكور صراحة في متن con-fully-functioning-person.md لمفهوم "الشخصية
  العاملة بكامل طاقتها"، وأيضاً *A Way of Being* (1980) حيث عرضه روجرز بصورته النهائية. لا يوجد
  ملف wrk- لأي من الكتابين في الأطلس حالياً (بحث شامل في content/ar/works و drafts لم يُظهر تطابقاً).
- **status:** معلق.

## Task 8 — طلبات slug جديدة (schools: sch-cbt / sch-cognitive-behavioral)
- **CBT القائم على العمليات (Process-Based CBT)**: مدرسة/تيار فرعي حديث (Hayes & Hofmann,
  Process-Based CBT، 2018) مذكور كـ split_into في كل من sch-cbt.md وsch-cognitive-behavioral.md
  لكن بلا ملف slug مستقل. الرابطان اتحذفا من edges لأن preflight_check يرفض target نصي حر (مش slug).
- **الموجة الثانية من الموجات المعرفية-السلوكية**: تصنيف تاريخي (belongs_to) بلا ملف slug مستقل
  (لا `sch-` ولا `br-`). اتحذف الرابط من edges لنفس السبب.
- **status:** معلق.

## Task 8 — طلبات slug جديدة (schools: umbrella مفقود)
- **الفلسفة السياسية المعاصرة**: umbrella مفقود ذُكرت edge إليه بنص حر في sch-conservatism-philosophical.md
  (حُذف الرابط). نفس الغياب مذكور في MINIMAX.md Task 13 كأولوية مؤكدة (11 عضواً يتيماً).
- **علم النفس عبر الثقافي (Cross-Cultural Psychology)**: umbrella مفقود ذُكرت edge إليه بنص حر في
  sch-confucian-psychology.md (حُذف الرابط). مذكور أيضاً في MINIMAX.md Task 13 ضمن فروع علم النفس
  الأكاديمي الغائبة كمدارس.
- **status:** معلق.

## Task 8 — طلبات slug جديدة (schools: umbrella مفقود، دفعة 8.5)
- **علم الكلام الإسلامي**: umbrella مفقود ⚠️ **تكرر 4 مرات مؤكدة عبر دفعات مختلفة** كـ target حر
  في edges (sch-ibadi-kalam، sch-imami-kalam، sch-maturidiyya، sch-mutazila) — كل مرة حُذف الرابط
  بدل اختراع slug. هذا التكرار المتعدد دليل قاطع على حاجة حقيقية لملف umbrella `sch-islamic-kalam`
  يجمع المدارس الكلامية الإسلامية الفرعية (معتزلة، أشعرية، ماتريدية، إمامية، إباضية) تحته.
  مذكور أيضاً في MINIMAX.md Task 13 كأولوية مؤكدة (ضمن قائمة المدارس المؤكدة الغائبة) — **هذا
  التكرار يرفعه لأولوية قصوى في Task 13**.
- **تقاليد الحكمة الأفريقية**: umbrella مفقود ذُكرت edge إليه بنص حر في sch-ifa.md (حُذف الرابط).
- **الفلسفات الآسيوية الحديثة**: umbrella مفقود ذُكرت edge إليه بنص حر في sch-hindutva.md (حُذف الرابط).
- **status:** معلق.

## Task 8 — طلبات slug جديدة (schools: umbrella مفقود، دفعة 8.6 — تكرار مؤكد)
- **الفلسفات اللاتينية (أمريكا اللاتينية)**: umbrella مفقود ظهر **مرتين** الآن كـ target حر في edges —
  مرة في sch-caribbean-philosophy.md (دفعة 8.3) ومرة في sch-indigenismo.md (دفعة 8.5)، وكلاهما حُذف
  الرابط. التكرار يشير لحاجة حقيقية لملف umbrella لتجميع مدارس أمريكا اللاتينية الفلسفية
  (sch-caribbean-philosophy، sch-indigenismo، sch-dependency-theory، sch-decolonial-latin، إلخ).
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-ghost-in-the-machine-ryle)
- **thk-gilbert-ryle** (Gilbert Ryle، 1900–1976، فيلسوف أكسفورد، صاحب *مفهوم العقل* 1949 وصائغ مصطلح
  "شبح في الآلة" وخطأ المقولة): لا يملك ملف thk- مستقل. الملف الوحيد باسم قريب `thk-ryle` يخص أنتوني
  رايل (Anthony Ryle)، معالج نفسي مختلف تماماً (مؤسس العلاج التحليلي المعرفي CAT)، فلم يُربط تجنباً
  لخلط id/title. سُجّلت الفجوة في gaps الملف بدل اختراع رابط.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-knowledge-argument-jackson)
- **thk-frank-jackson** (Frank Cameron Jackson، فيلسوف أسترالي، صاحب حجة المعرفة/تجربة ماري 1982):
  لا يملك ملف thk- مستقل. الملف الوحيد باسم قريب `thk-djackson` يخص دون جاكسون (Don D. Jackson)،
  معالج نفسي مختلف تماماً (مدرسة بالو ألتو)، فلم يُربط تجنباً لخلط id/title.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: latent-learning/law-of-attraction/law-of-effect/leap-of-faith/learned-helplessness/li-principle-neoconfucian، دفعة 9.1)
- **dis-mdd** (الاكتئاب): مذكور كرابط مُقترح لـ con-learned-helplessness.md — لا يوجد ملف بهذا
  الـslug تحت content/ar/disorders/ ولا غيره. حُذف الرابط، وسُجّلت الفجوة في gaps بدل اختراعه.
- **stu-peterson-seligman-explanatory-style** (دراسة أسلوب التفسير لبيترسون وسليجمان): مذكور كرابط
  مُقترح لنفس الملف — لا يوجد ملف studies بهذا الـslug. حُذف الرابط، وسُجّلت الفجوة في gaps.
- **ملاحظة تحقق مزدوجة (مش تكرار فعلي)**: con-li-principle-neoconfucian.md (المبدأ الكوني 理 عند
  تشو شي، النيوكونفوشية) وcon-li.md (اللي 禮 = الطقس/الأدب عند كونفوشيوس المبكر) يبدوان متطابقين
  بالعربية "اللي" لكنهما يوثقان رمزين صينيين مختلفين تماماً (理 مقابل 禮) بمعنيين مختلفين. تحقّقتُ
  فعلياً من محتوى الملفين ولم أدمجهما؛ تم ربطهما ببعض كـrelated concept مع توضيح الفرق في المتن.
  التوصية لدفعة con-li.md اللاحقة (Task 10 أو ما يعادلها): توضيح نفس الفرق من جهتها أيضاً.
- **status:** معلق.

## Task 9 — طلبات slug جديدة/ملاحظات (دفعة con-mafhum-wa-misdaq/con-makoto-naka-ima/con-maladaptive-emotion/con-mandate-of-heaven-legitimacy/con-mandate-of-heaven-tianming/con-marsha-acceptance-change)
- **sch-constructive-living** (Constructive Living، حركة David K. Reynolds اليابانية-الكندية):
  لا يوجد ملف مدرسة بهذا الاسم أو أي slug مكافئ تحت content/ar/schools/. الرابط الموجود سابقاً في
  edges لملف con-makoto-naka-ima.md كان نصاً حراً `"Constructive Living (اليابان/كندا)"` وليس slug
  حقيقياً؛ حُذف ولم يُستبدل، وسُجّلت الفجوة في gaps.
- **con-secondary-emotion** و**con-emotional-schematic-processing**: مذكوران في gaps الأصلية لملف
  con-maladaptive-emotion.md كروابط مقترحة — تحققتُ فعلياً ولا يوجد ملف بأي من الـslug المقترحين تحت
  content/ar/concepts/. لم يُضافا، وأُبقيت الملاحظة في gaps.
- **تصحيح slug خاطئ (ليس طلب جديد)**: ملف con-maladaptive-emotion.md كان يشير في edges/gaps إلى
  `thk-jsafran` (غير موجود). المفكر الفعلي هو **thk-ssafran** (جيريمي د. سافران، شريك غرينبرغ في صياغة
  التمييز 1987) — تم تصحيح edges وrelated ليشيرا إلى thk-ssafran.
- **ازدواج محقَّق فعلياً (وليس تخميناً)**: con-mandate-of-heaven-legitimacy.md (CON-1071، "الشرعية
  الأخلاقية للحكم") وcon-mandate-of-heaven-tianming.md (CON-1072، "الشرعية السياسية") يعالجان نفس
  مفهوم تفويض السماء الصيني (Tianming) بمحتوى شبه متطابق قبل هذه الدفعة (نفس الجمل المعيارية القالبية
  حرفياً). فُتح الملفان وقُرئا بالكامل؛ لم يُدمَجا بناءً على تعليمات المهمة، وبدلاً من ذلك رُبط كل
  منهما بالآخر كـrelated مع توضيح الفارق المقصود بينهما (بُعد أخلاقي مقابل بُعد سياسي-مؤسسي)، وسُجّلت
  ملاحظة الازدواج في gaps كل ملف. **التوصية**: قرار تحرير لاحق (دمج الملفين في ملف واحد بعنوان "تفويض
  السماء (Tianming)" شامل، أو تخصيص كل ملف فعلياً بمحتوى متمايز بوضوح بدل النسخ القالبي المتطابق).
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-moral-error-theory-mackie/con-moral-luck-nagel-williams/con-moral-particularism-dancy)
- **thk-mackie** (John Leslie Mackie، 1917-1981، صاحب نظرية الخطأ الأخلاقي في *Ethics: Inventing Right
  and Wrong*، 1977): لا يملك ملف thk- مستقل. سُجّلت الفجوة في gaps ملف con-moral-error-theory-mackie.md
  بدل اختراع رابط.
- **thk-bernard-williams** (Bernard Williams، 1929-2003، شارك ناغل في صياغة مفهوم الحظ الأخلاقي في ندوة
  1976): لا يملك ملف thk- مستقل. الملفات القريبة الاسم (thk-rlwilliams=روبرت لي ويليامز الثاني،
  thk-mwilliams=مارك ويليامز، thk-janicewilliams=جانيس ويليامز) تخص أشخاصاً مختلفين تماماً، فلم يُربط
  تجنباً لخلط id/title. سُجّلت الفجوة في gaps ملف con-moral-luck-nagel-williams.md.
- **thk-dancy** (Jonathan Dancy، صاحب *Ethics Without Principles*، 2004، أبرز منظّري التفصيلية
  الأخلاقية): لا يملك ملف thk- مستقل. سُجّلت الفجوة في gaps ملف con-moral-particularism-dancy.md.
- **ملاحظة إضافية**: ملفات con-moral-error-theory-mackie.md وcon-moral-luck-nagel-williams.md
  وcon-moral-particularism-dancy.md كان فيها edges.belongs_to بـtarget حر "الفلسفة الأخلاقية
  التحليلية" مش slug حقيقي — لا يوجد ملف sch- بهذا الاسم (المدارس الموجودة أضيق: sch-virtue-ethics،
  sch-kantian-ethics-contemporary، sch-care-ethics...). حُذف الرابط من الثلاثة بدل ترك نص حر أو اختراع
  slug. يُقترح لاحقاً إنشاء ملف مظلة sch-analytic-ethics أو ما يعادله لو تكرر الاحتياج.
- **ملاحظة ازدواج (تحقّق فعلي، مش دمج)**: con-monad.md وcon-monad-simple-substance.md يوثّقان نفس فكرة
  الموناد اللايبنتزية (نفس الشخص/نفس المدرسة sch-leibnizianism)، لكن con-monad.md مفصّل جداً (خصائص،
  أنواع، توافق مسبق، أثر فلسفي، نقد) بينما con-monad-simple-substance.md عام/مختصر جداً (قالب توليدي لم
  يُطوَّر بعد). لم يُدمَجا، وتم ربطهما ببعضهما كـrelated concept مع توضيح الفرق في متن كل منهما. التوصية
  لـTask 10: تعميق متن con-monad-simple-substance.md أو تقييم دمجه/حذفه كملف مكرر تماماً لاحقاً — القرار
  خارج نطاق Task 9.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-occasionalism-malebranche-concept/con-ockhams-razor-parsimony/con-ockhams-razor/con-oedipus-complex/con-omoluabi-yoruba-ethics/con-one-mind-two-aspects-wonhyo)
- **ملاحظة ازدواج (تحقّق فعلي، مش دمج)**: con-ockhams-razor.md وcon-ockhams-razor-parsimony.md يوثّقان نفس فكرة شفرة أوكام (Lex Parsimoniae) بنفس الشخص (thk-william-ockham) ونفس المدرسة (sch-ockhamism)، لكن con-ockhams-razor.md يقدّم الصياغة المنهجية العامة المختصرة («لا ينبغي مضاعفة الكيانات») بينما con-ockhams-razor-parsimony.md يركّز على البعد الأنطولوجي/الاقتصادي تحديداً. لم يُدمَجا، وتم ربطهما ببعضهما كـrelated مع توضيح الفرق نصياً في متن كل منهما. التوصية لـTask 10: تقييم دمجهما أو تعميق التمايز بينهما لاحقاً — القرار خارج نطاق Task 9.
- **thk- لصاحب مفهوم الأومولوابي**: لا يوجد ملف thk- مستقل لأي من فلاسفة اليوروبا المتخصصين في الأومولوابي (Sophie Oluwole، Segun Gbadegesin، J.O. Bewaji، Wande Abimbola). رُبط الملف بدلاً من ذلك بـsch-ethnophilosophy وthk-wiredu وthk-hountondji (ناقدَي الإثنوفلسفة الأفريقية) وcon-ubuntu/con-ubuntu-african-humanism كمفاهيم موازية. سُجّلت الفجوة في gaps بدل اختراع slug.
- **edges.belongs_to حر (مش slug) — con-omoluabi-yoruba-ethics.md**: كان target="الفلسفة الإثنية الأفريقية (Ethnophilosophy)" نص حر. تم تصحيحه إلى sch-ethnophilosophy (الملف موجود فعلياً ومطابق).
- **edges.belongs_to حر (مش slug) — con-one-mind-two-aspects-wonhyo.md**: كان target="البوذية الكورية (التقاليد التاريخية)" نص حر، ولا يوجد ملف sch- مطابق فعلياً للبوذية الكورية/بوذية سيلا التاريخية (sch-buddhism-early، sch-buddhist-modernism، sch-korean-neoconfucian كلها غير مطابقة موضوعياً). حُذف الرابط بدل اختراع slug أو ترك نص حر، وسُجّلت الفجوة في gaps.
- **thk-wonhyo**: لا يوجد ملف thk- مستقل لونهيو (Wonhyo، 617-686 م، راهب سيلا الكوري وصاحب المفهوم المباشر لـcon-one-mind-two-aspects-wonhyo.md) رغم كونه محورياً. سُجّلت الفجوة في gaps.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-mdma-ptsd/con-meaning/con-melammu/con-memory/con-mentalization/con-mere-exposure-effect، دفعة 9.2)
- **con-internal-healer** (المعالج الداخلي / Inner Healer): مذكور نصياً في con-mdma-ptsd.md ("تحديد
  المعالج الداخلي (Inner Healer)")، ولا يوجد ملف concepts بهذا الـslug. سُجّلت الفجوة في gaps بدل
  اختراعه.
- **con-psychedelic-assisted-therapy** (كمفهوم مستقل عن المدرسة): الموجود فعلاً هو sch-psychedelic-assisted-therapy
  فقط (مدرسة)، وقد رُبط. لا يوجد ملف concepts مستقل بهذا الاسم.
- **dbt-mdma-ptsd-trial**: لا يوجد ملف debates بهذا الـslug رغم أن con-mdma-ptsd.md يوثّق جدلاً علمياً
  حقيقياً (Lykins et al. 2020 ضد Mithoefer et al.) يستحق ملف جدل مستقل مستقبلاً.
- **thk-shulgin** (Alexander Shulgin، كيميائي اكتشف/أعاد اكتشاف MDMA الترفيهي والعلاجي 1970s): لا يملك
  ملف thk- في الأطلس رغم ذكره في con-mdma-ptsd.md.
- **thk-zajonc** (Robert Zajonc، صاحب مفهوم Mere Exposure Effect الأصلي 1968): موجود فقط كمسودة غير
  منشورة في content/ar/drafts/spark/thinkers/thk-zajonc.md، وليس ملف thk- معتمداً. يُنصح بترقيته
  ونشره لأنه صاحب المفهوم المباشر لـ con-mere-exposure-effect.md.
- **ملاحظة تحقق مزدوجة**: con-mere-exposure-effect.md وcon-exposure-habituation.md قد يبدوان متقاربين
  بالاسم العربي ("تعرض/تعريض") لكنهما مفهومان مختلفان تماماً (تأثير الألفة والانجذاب الاجتماعي مقابل
  التعود العلاجي السلوكي على القلق). تحقّقت فعلياً من محتوى الملفين ولم أربطهما، وسُجّلت الملاحظة في
  gaps لتفادي الخلط مستقبلاً.
- **ملاحظة تحقق con-melammu.md**: الرابط السابق con-autonomy-homonomy (مفهوم وجودي لأندراس أنجيال،
  1941-1965) كان في related دون أي أساس نصي فعلي — مفهوم مختلف كلياً (ميلمو رافدي، 3000 ق.م). حُذف
  بعد تحقق فعلي من المتن.
- **ملاحظة con-meaning.md**: حُذفت من related روابط stu-/ins-/br-/ctx- (نموذج صنع المعنى، LAP-R، SoMe،
  br-psychocoaching، ctx-stoicism) لأنها خارج فئات Task 9 المحددة (thk-/sch-/con-/wrk-/dbt-) ولا
  أساس نصي فعلي لها في متن الملف الحالي؛ الملفات نفسها صحيحة السلاج ويمكن ربطها لاحقاً إذا استُحدثت
  فقرة تخصها في Task 10.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-negative-theology-via-negativa/con-neidan/con-neo-freudian/con-neuroception-polyvagal/con-neuroception-safety-detection/con-neurodiversity-affirming)
- **thk-wang-chongyang** (Wang Chongyang، 1113-1170، مؤسس مدرسة الطاوية الكاملة Quanzhen التي تبنّت
  التاوية الداخلية كممارسة مركزية، مذكور نصياً في con-neidan.md): لا يملك ملف thk- مستقل (الملفات
  القريبة الاسم thk-wang-bi/thk-wang-fuzhi/thk-wang-yangming تخص مفكرين صينيين مختلفين تماماً).
  سُجّلت الفجوة في gaps بدل اختراع رابط.
- **Robinet** (الباحثة الفرنسية التي أعادت اكتشاف Neidan في الغرب بالقرن 20، مذكورة نصياً في
  con-neidan.md): لا يوجد ملف thk- لها في الأطلس.
- **thk-judy-singer** و**thk-harvey-blume** (صاغا مصطلح Neurodiversity أواخر التسعينيات، مذكوران نصياً
  في con-neurodiversity-affirming.md): لا يملكان ملفات thk- مستقلة. الملف الوحيد القريب بالاسم
  (thk-singer.md = توماس سينغر، محلل يونغي مختلف تماماً) لم يُربط تجنباً لخلط id/title.
- **ملاحظة ازدواج (تحقّق فعلي، مش دمج)**: con-neuroception-polyvagal.md وcon-neuroception-safety-detection.md
  يوثّقان فعلياً نفس فكرة بورجس الأساسية (النيوروسبشن/الاكتشاف اللاواعي للأمان ضمن النظرية العصبية
  المبهمية المتعددة)، لكن con-neuroception-safety-detection.md أعمق بكثير (قنوات الإدراك، جدول مقارنة،
  تطبيقات إكلينيكية، نقد LeDoux/Grossman/Crittenden، جذور فلسفية) بينما con-neuroception-polyvagal.md
  أقصر ويركّز على السلّم المبهمي الثلاثي. لم يُدمَجا، وتم ربطهما ببعضهما كـrelated concept مع توضيح
  الفرق في متن كل منهما (تماماً كسابقة con-monad/con-monad-simple-substance). كما لوحظ أن ملف
  con-neuroception-safety-detection.md كان يحتوي روابط لـthk-dsiegel/thk-plevine/thk-clarkson دون أي
  أساس نصي فعلي في المتن الأصلي؛ أُبقي على thk-dsiegel بعد إضافة جملة تبرير فعلية (نافذة التحمل)، بينما
  حُذف thk-plevine وthk-clarkson لعدم وجود أي صلة نصية أو محتوى فعلي يربطهما بالملف عند التحقق.
- **ملاحظة**: con-negative-theology-via-negativa.md وcon-negative-attributes.md (Via Negativa) يتقاطعان
  بشدة (نفس الفكرة اللاهوتية الفلسفية للنفي)، لكن الأول يركّز على التقليد الأفلاطوني المحدث/المسيحي
  (أفلوطين، ديونيسيوس المجهول) والثاني على التقليد اليهودي-الإسلامي الأندلسي (ابن ميمون، ابن عربي). تم
  ربطهما كـrelated concept دون دمج.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-nirvana-extinction/con-no-miracle-argument/con-noble-savage-rousseau/con-noema-and-noesis-husserl/con-nominalism-universals-concept/con-nonviolent-communication)
- **thk-rboyd** (Richmond Boyd، صاحب صياغة أكثر منهجية لحجة المعجزة، مذكور في متن con-no-miracle-argument.md): لا يزال غير موجود في الأطلس (لا معتمد ولا مسودة) — مسجّل مسبقاً في هذا الملف، أُعيد التأكيد بعد إعادة بناء related.
- **thk-ncartwright** (Nancy Cartwright، فيلسوفة العلم صاحبة "الحجة الأدائية" ضد حجة المعجزة، مذكورة في con-no-miracle-argument.md): الملف الموجود thk-dcartwright يوثّق شخصاً مختلفاً تماماً (Dorwin Cartwright، عالم نفس اجتماعي)، فلم يُربط تجنباً لخلط الهوية. يُنصح بإنشاء ملف مستقل لها.
- **ملاحظة إزالة**: con-autonomy-homonomy (مفهوم أنجيال الوجودي) كان مربوطاً سابقاً بـcon-no-miracle-argument.md دون أساس نصي فعلي — أُزيل بعد تحقق فعلي من المتن.
- **ملاحظة إصلاح edges**: con-nonviolent-communication.md كان فيه edges.belongs_to بـtarget حر "علم النفس الإنساني والتواصل" مش slug حقيقي — صُحّح إلى sch-humanistic (الملف الفعلي الموجود).
- **ملاحظة ازدواج مؤكَّدة**: thk-marshall-rosenberg ملف إحالة معلن لنفس شخص thk-msrosenberg (مارشال روزنبرغ، مؤسس NVC). استُخدم thk-msrosenberg فقط في related con-nonviolent-communication.md لتفادي تكرار نفس المفكر بسلاجين.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-neurofeedback/con-neuroplasticity-trauma/con-neuroplasticity/con-neuropsychoanalysis/con-neurosis-historical-framework/con-new-democracy)
- **thk-ssterman / thk-jlubar / thk-sothmer** (ماريو ستيرمان، جويل لوبار، سيغفريد أوتمر — رواد الأجيال
  الثلاثة للتغذية الراجعة العصبية المذكورون بالاسم في متن con-neurofeedback.md): لا يملكون ملفات thk-
  مستقلة في الأطلس (كانوا نُقلوا مسبقاً إلى المسودات — موثّق في gaps الملف قبل هذه الدفعة). لم تُخترع
  روابط لهم، الفجوة موجودة أصلاً في الملف.
- **thk-merzenich / thk-parihar** (مايكل ميرزينيش، فيجاي بارهار) و**con-hpa-axis / con-neurogenesis-adult
  / con-synaptic-pruning**: مذكورون بالفجوات مسبقاً في con-neuroplasticity.md قبل هذه الدفعة، تحقّقتُ
  فعلياً ولا يزال لا وجود لملفات thk-/con- بهذه الأسماء — أُبقيت الفجوات كما هي.
- **thk-hebb** (Donald Hebb، صاحب قاعدة هب المذكورة بالاسم في con-neuroplasticity.md): موجود فقط كمسودة
  غير منشورة في content/ar/drafts/spark/thinkers/thk-hebb.md، وليس ملف thk- معتمداً في content/ar/thinkers/.
  لم يُربط، ويُنصح بترقيته ونشره لأنه مرجع تأسيسي لمفهوم اللدونة العصبية.
- **thk-maguire** (Eleanor Maguire، دراسة سائقي التاكسي في لندن المذكورة بالاسم في con-neuroplasticity.md):
  لا يملك ملف thk- في الأطلس (لا منشور ولا مسودة). لم يُخترع رابط.
- **thk-lenin / thk-stalin** (فلاديمير لينين وجوزيف ستالين، مذكوران بالاسم في con-new-democracy.md ضمن
  مقارنة نظرية ماو بالمرحلة الديمقراطية عند لينين وبـ«الاشتراكية في بلد واحد» عند ستالين): لا يملكان ملف
  thk- مستقل في الأطلس. سُجّلت الفجوة في gaps الملف بدل اختراع الروابط.
- **ملاحظة تحقق ازدواج (con-neuroplasticity.md × con-neuroplasticity-trauma.md)**: تحقّقتُ فعلياً من
  محتوى الملفين — لا يوجد ازدواج فعلي. con-neuroplasticity.md هو المفهوم العام في علم النفس البيولوجي
  والعصبي (أنواع اللدونة، هب، ميرزينيش، ماغواير، تطبيقات عامة) بينما con-neuroplasticity-trauma.md
  تخصيص إكلينيكي ضيّق ضمن مدرسة العلاج السنسوريموتور لعلاج الصدمة تحديداً (فان دير كولك، ليفين، سيغل،
  EMDR). لم يُدمَجا، وتم ربطهما ببعضهما كمفهومين متكاملين (رابط con-neuroplasticity في related
  con-neuroplasticity-trauma.md، ورابط con-neuroplasticity-trauma في related con-neuroplasticity.md)
  مع توضيح الفرق في متن كل منهما وفي gaps الملف الإكلينيكي.
- **تصحيح مُلاحَظ أثناء التحقق**: عنوان con-trauma.md الفعلي هو "الصدمة النفسية في التحليلية" وليس
  "الصدمة" كما كان مكتوباً سابقاً في related الخاص بـcon-neuroplasticity-trauma.md — صُحِّح ليطابق
  عنوان الملف المستهدف حرفياً.
- **status:** معلق.

## Task 9 — طلب umbrella جديد (con-past-life-regression، دفعة parrhesia→peak-experience)
- **subject:** "حركات مثيرة للجدل" — كانت edges.belongs_to في con-past-life-regression.md تشير لهذا
  العنوان كنص حر (مدرسة/تيار)، بلا أي slug مطابق فعلياً (لا sch- ولا br- بهذا العنوان الحرفي في الأطلس).
- **source:** Task 9، 2026-09-01، مراجعة con-past-life-regression.md.
- **question:** هل تستحق "حركات مثيرة للجدل" ملف umbrella (`sch-` أو `br-`) يجمع ممارسات مثل
  استرجاع ذكريات الحياة السابقة، العلاج بالتحويل (conversion therapy)، العلاج الأولي (primal
  therapy)، وحركة الذاكرة المُستعادة؟ لاحظ وجود ملفات `br-` فرعية موثّقة فعلياً لهذه الحركات تحديداً
  (`br-recovered-memory-movement.md`، `br-conversion-therapy.md`، `br-primal-therapy.md`) دون
  umbrella يجمعها. حُذف الرابط الحر من con-past-life-regression.md بدل اختراع slug.
- **status:** معلق.
- **result:** —
- **decided_at:** —

## Task 9 — ملاحظة ازدواج مُتحقَّق منها (con-peak-experience.md × con-peak-experience-maslow.md)
- **subject:** con-peak-experience.md (مدخل عام مختصر، مبتدئ) وcon-peak-experience-maslow.md (تفصيل
  موسّع، متقدم) — كلاهما يوثّق مفهوم خبرة الذروة عند ماسلو.
- **source:** Task 9، 2026-09-01.
- **note:** تحقّقتُ فعلياً من محتوى الملفين: لا يوجد ازدواج يستوجب الحذف/الدمج — الفرق مقصود ومصرَّح
  به في متن con-peak-experience-maslow.md نفسه ("هذا الملفُّ يكمّل صفحة con-peak-experience العامّة
  بمزيد من التفصيل الفلسفي والإكلينيكي"). تم ربط الملفين ببعضهما في related مع توضيح العلاقة في
  gaps وفي قسم "الروابط والسياق" بدل الدمج، تماشياً مع تعليمات المهمة الصريحة بعدم الدمج.
- **status:** لا يحتاج قراراً إضافياً — إعلامي فقط.

## Task 9 — طلبات slug جديدة (concepts: con-political-psychoanalysis/con-polyvagal-states/con-polyvagal-theory-popular/con-polyvagal-theory/con-positive-existentialism/con-positive-liberty-berlin)
- **thk-isaiah-berlin** (أشعيا برلين، صاحب ثنائية الحرية الإيجابية/السلبية المذكورة بالاسم ضمنياً في con-positive-liberty-berlin.md وcon-negative-liberty-berlin.md): لا يملك ملف thk- في الأطلس (لا معتمد ولا مسودة) — الفجوة مسجّلة أصلاً في con-negative-liberty-berlin.md قبل هذه الدفعة، أُعيد تأكيدها في con-positive-liberty-berlin.md بعد التحقق الفعلي، ولم يُخترع رابط.
- **con-vagus-nerve** (العصب المُبهَم): مذكور بالاسم في متن con-polyvagal-theory.md، لا يوجد ملف بهذا slug في الأطلس حالياً. الفجوة كانت مسجّلة مسبقاً في الملف وأُبقيت.
- **ملاحظة ازدواج (تحقّق فعلي، مش دمج)**: con-polyvagal-theory.md وcon-polyvagal-theory-popular.md وcon-polyvagal-states.md الثلاثة يوثّقون فعلياً نفس نظرية بورجس العصبية المبهمية المتعددة لكن من زوايا متمايزة: con-polyvagal-theory.md هو الصياغة الأكاديمية الأصلية (متقدّم)، con-polyvagal-states.md تفصيل سريري للحالات الثلاث (متوسط)، con-polyvagal-theory-popular.md صياغة شعبية مبسّطة كـ"سلّم Polyvagal Ladder" عند ديب دانا (register: popular). لم تُدمَج، وتم ربط الثلاثة ببعضها كمفاهيم متكاملة مع توضيح الفرق صراحة في متن كل واحد منها.
- **تصحيح مُلاحَظ أثناء التحقق**: edges.belongs_to في con-polyvagal-theory-popular.md كان يشير إلى نص حر "علم الأعصاب والفيزيولوجيا الحيوية" وليس slug فعلي — صُحِّح إلى sch-polyvagal-informed-therapy (نفس مدرسة الملفين الشقيقين). كذلك أُزيل سطر related مكرر بنفس id (con-neuroception-polyvagal) في con-polyvagal-states.md، وصُحِّحت عناوين related غير المطابقة حرفياً لعناوين الملفات المستهدفة (con-polyvagal-theory-popular، con-window-of-tolerance، con-window-of-tolerance-detailed، con-neuroception-polyvagal، thk-dsiegel، thk-stephen-porges) في con-polyvagal-states.md وcon-polyvagal-theory.md.
- **status:** معلق.

## Task 9 — طلبات slug جديدة (concepts: con-private-language-argument/con-problem-of-induction/con-process-constructivism/con-prophetic-philosophy/con-prt-pivotal-response/con-psilocybin-depression)
- **con-problem-of-induction.md**: تحقّق فعلي كشف أن الفجوة القديمة "رابط مقترح لم يتحقق: كارل بوبر (thk-popper)" كانت خاطئة — الملف موجود فعلاً لكن بـslug مختلف (`thk-karl-popper`)، وكذلك `con-falsificationism-popper` موجود. رُبطا الاثنان بعد إضافة جملة تبرير في المتن. حُذف الرابط السابق `con-autonomy-homonomy` (مفهوم وجودي عن أنجيال لا علاقة له بمشكلة الاستقراء، بلا أي أساس نصي) — نفس نمط الروابط المخترعة المرصود سابقاً في ملفات أخرى.
- **con-prt-pivotal-response.md**: **thk-robert-koegel / thk-lynn-koegel** (روبرت ولين كوجل، مطوّرا PRT، مذكوران بالاسم صراحة في المتن): لا يملكان ملف thk- في الأطلس (تحقّق فعلي: بحث عن "koegel" في content/ar/thinkers لم يُظهر تطابقاً). الفجوة مسجّلة في gaps الملف. كما صُحِّح edges.belongs_to من "br-aba-advanced" (غير موجود) إلى "br-advanced-aba-prt-vb" (الملف الفعلي المطابق لعبارة "ABA المتقدم" في crumb). حُذف الرابط السابق `con-autonomy-homonomy` (بلا أساس نصي، نفس النمط المتكرر).
- **con-psilocybin-depression.md**: حُذف رابطا **thk-peter-bloom** (ملف مُحجَر فعلياً بسبب عدم توثيق أكاديمي رصين — راجع agents_specs/quarantine-minimax.md القسم 1) و**thk-rmdoblin** (ريك دوبلين، مؤسس MAPS المرتبط أساساً بالعلاج بمساعدة MDMA لا السيلوسيبين، ولا ذكر له في متن هذا الملف تحديداً). أُضيف بدلاً منهما **thk-rcarhart-harris** (مذكور بالاسم صراحة في المتن: "Carhart-Harris et al., 2021") و**con-psilocybin** (المفهوم الأعم للسيلوسيبين في العلاج النفسي) و**sch-psychedelic-assisted-therapy** (المدرسة، كانت موجودة فقط كـedges.relates_to). **ملاحظة عدم ربط**: لم يُربط أي ملف thk- لـ"Davis" (Davis et al., 2021) لعدم وجود ملف مطابق. كما لوحظ وجود ملفين منفصلين موثّقين بالكامل لشخصين مختلفين تماماً باسم "Roland Griffiths" (thk-griffiths وthk-roland-griffiths) — ازدواج محتمل يستحق مراجعة رئيس التحرير منفصلة، لم يُربط أي منهما بملف السيليكوبين تجنباً للخلط لعدم ورود اسمه صراحة في المتن.
- **con-prophetic-philosophy.md**: **thk-gersonides/thk-levi-ben-gershon** (ليفي بن جرسون/جيرسونيد) و**thk-kook** (الحاخام أبراهام إسحق كووك) مذكوران بالاسم في متن الأثر لكن لا يملكان ملف thk- في الأطلس — الفجوة مسجّلة. رُبط thk-judah-halevi وwrk-kuzari-judah-halevi وthk-maimonides وthk-al-ghazali وwrk-tahafut-al-falasifa-ghazali وthk-bonaventure وthk-mbuber، جميعها مذكورة بالاسم في المتن فعلياً.
- **con-private-language-argument.md**: الملف كان يحتوي متناً سقّالياً بالكامل (جمل قائمة سوداء عامة من preflight_check: "يمثل هذا المفهوم لبنة تأسيسية..."، "شكل هذا المفهوم منطلقاً لحوارات..."، وقسم "اقتباسات مختارة" يحوي "لا يوجد اقتباس مباشر موثوق متاح"). استُبدل بمتن حقيقي موجز (تعريف البرهان + مصدره في *بحوث فلسفية* 1953) لتبرير روابط thk-lwittgenstein وwrk-philosophical-investigations-wittgenstein وcon-language-games-late-wittgenstein وsch-ordinary-language، دون توسّع فلسفي إضافي (Task 10 منفصل).
- **con-process-constructivism.md**: صُحِّحت عناوين related غير المطابقة حرفياً لعناوين الملفات المستهدفة: con-felt-sense ("الإحساس الجسدي المُحسَّس (Felt Sense)" وليس "الإحساس الجسدي المحسَّس")، sch-humanistic ("علم النفس الإنساني (Humanistic Psychology)" وليس "الإنسانية"). أُضيف con-experiential-focusing (مبرَّر بمحور "التركيز" المذكور في المتن) وجملة تبرير قصيرة لعلاقة جندلين بروجرز.
- **preflight_check.py**: صفر مخالفات على الملفات الستة بعد التصحيحات (بما فيها حذف جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من gaps الأربعة ملفات التي كانت تحملها).
- **status:** معلق.

## Task 9 — طلب مراجعة edges (concepts: con-affirmative-therapy)
- **con-affirmative-therapy.md**: `edges.belongs_to` يشير إلى `br-affirmative-therapy` — الملف غير موجود فعلياً في الأطلس (تحقّق مباشر: لا ملف بهذا slug). خارج نطاق Task 9 (related فقط)، لم يُلمَس. يحتاج قرار رئيس التحرير: إنشاء الفرع أو تصحيح edges لهدف موجود.
- **status:** معلق.

## Task 9 — con-algorithmic-bias / con-alienation-entfremdung-marx / con-alienation-marx (2026-09-01)
- **con-algorithmic-bias.md**: **thk-kate-crawford** (كيت كروفورد، مذكورة بالاسم صراحة في المتن كمؤلفة *أطلس الذكاء الاصطناعي*) لا تملك ملف thk- في الأطلس (تحقّق: بحث عن "crawford" في content/ar/thinkers لم يُظهر تطابقاً — الملف الوحيد لهذا اللقب هو wrk-atlas-of-ai-crawford نفسه). الفجوة مسجّلة في gaps الملف، لم يُخترع slug.
- **con-alienation-entfremdung-marx.md** و**con-alienation-marx.md**: أُعيد بناء related من الصفر (Task 9)، بلا طلبات slug جديدة — كل الروابط المضافة (thk-marx, thk-hegel, thk-feuerbach, thk-fromm, thk-lukacs, thk-weber, thk-karl-popper, thk-foucault, thk-axel-honneth, thk-habermas, thk-yalom, thk-becker, con-commodity-fetishism, wrk-economic-philosophic-manuscripts-1844, wrk-capital-marx, sch-marxism) مطابقة لملفات موجودة فعلياً وموثّقة بالمتن.
- **ملاحظة ازدواج محتمل (خارج نطاق Task 9، لم تُلمس)**: con-alienation-entfremdung-marx.md وcon-alienation-marx.md يبدوان تكراراً لنفس المفهوم (اغتراب ماركس/Entfremdung) بعنوانين وslugين مختلفين — يحتاجان مراجعة رئيس التحرير لتقرير الدمج أو التمايز.
- **status:** معلق.

## Task 9 — con-al-yasar-al-islami-hanafi (2026-09-01)
- طُلب slug لعمل حسن حنفي "التراث والتجديد" (1980) — لا يوجد ملف wrk- له في content/ar. مذكور بالمتن كمشروع أوسع.
- طُلب slug لعمل حسن حنفي "مقدمة في علم الاستغراب" (1991) — لا يوجد ملف wrk- له في content/ar. مذكور بالمتن.

## Task 9 — con-analytic-neutrality (2026-09-01)
- **thk-arnold-modell** (أرنولد موديليف): مذكور بالاسم في المتن ("أرنولد موديليف (Arnold Modell): الحياد قد يُخفي خوف المحلّل من المواجهة") — لا يملك ملف thk- في الأطلس.
- **thk-dorothy-walsh** (دوروثي والش): مذكورة بالاسم في المتن — لا تملك ملف thk-. تحذير: يوجد `thk-rwalsh` بعنوان "روجر والش" وهو شخص مختلف تماماً؛ لم يُستخدم هذا الـslug تجنباً لخلط الهوية.
- **status:** معلق.

## Task 9 — con-boredom-existential (2026-09-01)
- طُلب slug wrk- لمحاضرات هايدجر *المفاهيم الأساسية للميتافيزيقا* (Die Grundbegriffe der Metaphysik، 1929-1930) — مذكورة بالاسم والسنة في متن con-boredom-existential.md (مصدر تمييز درجات الملل الثلاث)، لا يوجد ملف wrk- لها في content/ar/works.
- **con-border-thinking-mignolo.md**: لا طلب slug (thk-mignolo موجود فعلاً)، لكن المتن الحالي placeholder بالكامل ولا يذكر مينيولو بالاسم، فلم يُبنَ أي related — يحتاج Task 10 (كسر القالب) أولاً قبل إمكانية بناء related مبرر.
- **con-boundaries-psychological.md**: لا related — المتن لا يذكر أي مفكر/عمل/مدرسة بالاسم؛ الفجوة مسجّلة مسبقاً وصحيحة.
- **status:** معلق.

## Task 9 — con-bad-faith / con-bare-life-homo-sacer / con-barnum-forer-effect (2026-09-01)
- **con-bad-faith.md**: أُعيد بناء related من الصفر بجملة تبرير مضافة في المتن ("نقيض 'الأصالة'..."). رُبط thk-sartre وcon-freedom وcon-responsibility (موجودة مسبقاً وموثّقة بالمتن) وأُضيف con-authenticity (مبرَّر بالجملة الجديدة) وmet-sartre-cafe-waiter-bad-faith (مبرَّر بمثال النادل الموجود في المتن أصلاً) وsch-existential-therapy (عبر edges.belongs_to و"الممارسة الوجودية"). لا طلب slug جديد. **ملاحظتا ازدواج محتمل (خارج نطاق Task 9، لم تُلمسا)**: يوجد ملفان منفصلان لعمل *الوجود والعدم* (wrk-being-and-nothingness-sartre وwrk-sartre-being-and-nothingness) لم يُربط أي منهما تجنباً للالتباس؛ ويوجد ملف مصطلح منفصل (terms/trm-mauvaise-foi-bad-faith-sartre) يغطي نفس المفهوم بعنوان فرنسي — يحتاجان قرار رئيس التحرير للدمج.
- **con-bare-life-homo-sacer.md**: كان related فارغاً بالكامل لعدم ذكر أي اسم بالمتن. أُضيفت فقرة توثيقية قصيرة في المتن تسمّي جورجو أغامبين (Homo Sacer، 1995) وتربطه صراحة بمفهومي 'حالة الاستثناء' و'السلطة الحيوية' عند فوكو، ثم بُني related: thk-giorgio-agamben، thk-foucault، con-state-of-exception-agamben، con-biopolitics-and-biopower — جميعها ملفات موجودة فعلياً وموثّقة بالاسم في الفقرة المضافة. لا طلب slug جديد.
- **con-barnum-forer-effect.md**: أُضيفت كلمة "(Confirmation Bias)" لتسمية صريحة للانحياز الموصوف ضمنياً في المتن، وبُني related: con-self-serving-bias (مذكور صراحة أصلاً) وcon-confirmation-bias (بعد التسمية الصريحة). لم يُربط أي thk- لعدم وجود ملف لبيرترام فورير أو بي تي بارنوم في الأطلس (مسجّل في gaps مسبقاً). لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-categories-of-understanding-kant / con-catharsis-integration / con-cbt-mbt-mindfulness-3min-breathing-space (2026-09-01)
- **con-categories-of-understanding-kant.md**: كان related (thk-kant، sch-kant-critical) غير مبرَّر بالمتن إطلاقاً — المتن الأصلي (سطر واحد) لم يكن يذكر اسم كانط ولا نقد العقل الخالص، وكانت الفجوة تعترف بذلك صراحة (تناقض ثقة الشكل/شك المتن). أُعيد كتابة المتن ليسمّي كانط والسنة (1781) والعمل (*نقد العقل الخالص*) وما كان يعارضه (العقلانيون والتجريبيون)، فتبرَّر thk-kant وsch-kant-critical. أُضيف con-synthetic-a-priori-judgments (مبرَّر بجملة "تفترضها القضايا التركيبية القبلية شرطاً لإمكانها") وcon-transcendental-idealism-kant (مبرَّر بجملة "وهي في صلب المثالية الترنسندنتالية"). لا طلب slug جديد — كل الملفات المربوطة موجودة وعناوينها تطابق فعلياً.
- **con-catharsis-integration.md**: related كان مبنياً بالفعل بشكل صحيح من عمل سابق (thk-moreno وbr-psychodrama مبرَّران بجملة الافتتاح، thk-freud وsch-psychoanalysis مبرَّران بجدول المقارنة الفرويدي/المورينوي)، وكل العناوين تطابق الملفات المستهدفة فعلياً — لم يلزم أي تعديل.
- **con-cbt-mbt-mindfulness-3min-breathing-space.md**: related كان مبنياً بالفعل بشكل صحيح (sch-mbct وthk-zsegal مبرَّران بجملة الافتتاح، con-mindfulness وcon-cognitive-decentering وdis-mdd مبرَّرة بفقرات "الأثر العلاجي" و"الأبحاث")، وكل العناوين تطابق فعلياً — لم يلزم أي تعديل. طلب con-rumination المذكور في gaps كان مسجلاً مسبقاً ولم يُكرَّر هنا.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-cartesian-doubt-method / con-categorical-imperative-kant / con-categorical-imperative (2026-09-01)
- **con-cartesian-doubt-method.md**: related كان (thk-descartes، sch-cartesianism) غير مبرَّر بالمتن إطلاقاً — المتن سطر تعريف عام واحد لا يذكر ديكارت بالاسم ولا الكوجيتو ولا أي عمل. أُفرغ related بالكامل ([])، وتُركت الفجوة موصوفة بدقة (Task 10 مطلوب لتعميق المتن قبل أي إعادة بناء related). لا طلب slug جديد.
- **con-categorical-imperative-kant.md**: أُبقي thk-kant فقط (مبرَّر بجملة "في فلسفة كانط" الصريحة في أول سطر متن). أُزيل ذكر sch-kant-critical من related — اسم المدرسة الحرفي غير مذكور بالمتن رغم وجود edges.belongs_to لها. لا طلب slug جديد.
- **con-categorical-imperative.md**: أُبقي thk-kant وأُضيف كل من ذُكر بالاسم صراحة في المتن ولم يكن مربوطاً: thk-marx، thk-habermas، thk-jean-francois-lyotard (مطابق title "جان فرانسوا ليوتار")، thk-foucault — كلهم موجودون فعلاً في content/ar/thinkers وعناوينهم مطابقة. أُبقي أيضاً thk-rawls وthk-schopenhauer وthk-hegel وthk-nietzsche وthk-bentham وthk-mill (مبرَّرون أصلاً بالمتن). أُزيل sch-kant-critical من related لعدم ذكر اسمها الحرفي بالمتن (الوارد هو "الكانطية الجديدة"، مدرسة لاحقة مختلفة، لا يوجد لها ولا لأصحابها Marburg/Baden slug مطلوب هنا لأنها غير مسمّاة بأفراد).
  - **طلب slug جديد**: **F. H. Bradley** (فيلسوف هيغلي بريطاني، منتقد "الواجب المجرد" الكانطي، مذكور بالاسم في قسم "الأثر" بالمتن) — لا يوجد ملف thk- له في content/ar/thinkers. type مقترح: مفكر، part: philosophy.
  - **طلب slug جديد**: **T. H. Green** (توماس هيل جرين، فيلسوف هيغلي بريطاني، مذكور بالاسم بجانب برادلي في نفس الفقرة) — لا يوجد ملف thk- له في content/ar/thinkers. type مقترح: مفكر، part: philosophy.
- **ملاحظة تسجيل (لا دمج، خارج نطاق Task 9)**: con-categorical-imperative-kant.md وcon-categorical-imperative.md قد يكونا ازدواجاً — نفس العنوان الإنجليزي "Categorical Imperative"، نفس الموضوع، نفس السنة (1785)، نفس edges.belongs_to (sch-kant-critical). الملف الثاني أعمق وأوسع مصادرَ. سُجِّلت الملاحظة في gaps كلا الملفين سابقاً وهنا مجدداً لتنبيه رئيس التحرير؛ لم يُلمَس أي منهما بحذف أو دمج.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-brahman-nirguna-saguna / con-brahman / con-buddhist-compassion-karuna (2026-09-01)
- **con-brahman-nirguna-saguna.md**: المتن سطر واحد فقط، لا يذكر شانكارا ولا الفيشيشتادفايتا بالاسم (كما تسجّل gaps مسبقاً). أُعيد بناء related على أساس ما هو مذكور صراحة فقط: con-brahman (العنوان نفسه تمييز داخل البراهمان) وsch-vedanta ("الفيدانتا" مذكورة حرفياً بالمتن). لم يُربط sch-advaita-vedanta رغم وجوده في edges.belongs_to لأن اسم "أدفايتا" غير مذكور في متن الجسم نفسه. لا طلب slug جديد.
- **con-brahman.md**: أُعيد بناء related كاملاً من المتن الغني: أُبقي thk-shankara وcon-maya-vedanta وcon-brahman-nirguna-saguna (مذكورون صراحة). أُزيل sch-vedanta لأن كلمة "فيدانتا" غير مذكورة فعلياً في جسم المتن (فقط في crumb/dates بالـfrontmatter). أُضيف: sch-vishishtadvaita ("في الفيشيشتادفايتا")، thk-plotinus ("عند أفلوطين")، sch-daoism-philosophical ("في الداوية")، wrk-daodejing (اقتباس *Dao De Jing* الحرفي)، wrk-upanishads (اقتباسات Maitri/Chandogya/Brihadaranyaka Upanishad المتكررة). لا طلب slug جديد — كل الملفات موجودة وعناوينها تطابق فعلياً.
  - **ملاحظة ازدواج محتمل (خارج نطاق Task 9، لم يُدمج)**: يوجد ملفان لعمل داو ده جينغ (wrk-daodejing وwrk-daodejing-laozi) وملفان لمفهوم الداو (con-dao وcon-dao-the-way-concept) — لم يُربط سوى wrk-daodejing تجنباً للالتباس، يحتاجان قرار رئيس التحرير للدمج.
  - **ملاحظة الازدواج المطلوبة صراحة بالتاسك**: con-brahman-nirguna-saguna وcon-brahman قد يكونا تكراراً موضوعياً جزئياً (الأول تفصيل تحت مظلة الثاني) — لم يُدمجا، مسجَّل هنا فقط للمراجعة.
- **con-buddhist-compassion-karuna.md**: أُبقي con-cft-self-compassion وthk-pgilbert وwrk-gilbert-compassionate-mind وthk-ssalzberg (جميعهم مذكورون صراحة بالمتن: "علاج الفؤاد... بول جيلبرت 2009، 2014"، "شارون سالزبرغ... 1995"). لم يُربط sch-buddhist-psychology رغم edges.belongs_to لعدم ذكر "علم النفس البوذي" حرفياً في جسم المتن.
  - **طلب slug جديد**: **thk-dalai-lama** (الدالاي لاما) — مذكور بالاسم والعمل والسنة في المتن ("الدَّالَايْ لَامَا، 2001، *Ethics for the New Millennium*") — لا يوجد ملف thk- له في content/ar/thinkers.
  - **طلب slug جديد**: **thk-gazan** أو ما يعادله (Gazan) — مذكور بالاسم والسنة في المتن ("غَازَانْ، 2015: تطبيق كرونا في العلاقات بين الأمهات والأطفال") — لا يوجد ملف thk- ولا مصدر مقابل في الأطلس؛ الاسم غير واضح الهجاء الكامل (يحتاج تحقق بحثي قبل إنشاء الملف).
  - **طلب slug جديد**: **wrk-salzberg-lovingkindness** (أو ما يعادله) لكتاب شارون سالزبرغ *Lovingkindness* (1995) — مذكور بالاسم والسنة صراحة في المتن — لا يوجد ملف wrk- له في content/ar/works.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-coloniality-of-power-quijano / con-coloniality / con-commodity-fetishism (2026-09-01)
- **con-coloniality-of-power-quijano.md**: أُزيل thk-enrique-dussel (غير مذكور بالمتن إطلاقاً). أُضيف thk-anibal-quijano (صاحب المفهوم، مذكور صراحة: "عالم الاجتماع والمنظر البيروفي أنيبال كويخانو")، sch-decolonial-latin (edges.belongs_to، ومذكورة ضمنياً بالسياق البيروفي/اللاتيني)، con-coloniality (نفس الحقل المفاهيمي، تفصيل/تأصيل مشترك). لا طلب slug جديد.
  - **ملاحظة ازدواج (مطلوبة صراحة بالتاسك، لم تُدمج)**: con-coloniality-of-power-quijano.md وcon-coloniality-of-power-concept.md يغطيان نفس المفهوم بالضبط (استعمارية السلطة عند كويخانو، نفس العنوان الإنجليزي تقريباً "Coloniality of Power")، بمتنين مستقلين مختلفي الصياغة. سُجِّلت الملاحظة في gaps الملف الأول أيضاً. تحتاج قرار دمج من رئيس التحرير.
- **con-coloniality.md**: أُعيد بناء related كاملاً: thk-anibal-quijano وthk-mignolo (صاغا المفهوم، مذكوران بالاسم)، thk-said (مذكور بالاسم في مقارنة "ما بعد الكولونيالية")، sch-decolonial-philosophy (edges.belongs_to)، sch-postcolonial-philosophy (مذكورة حرفياً بالمتن)، con-coloniality-of-power-quijano (نفس صائغ المفهوم كويخانو، مفهوم شقيق). أُزيل con-decolonizing-therapy وcrt-medicalization-of-poverty (غير مذكورين بالمتن إطلاقاً).
  - **طلب slug جديد**: **لينين (Lenin)** — مذكور بالاسم في مقارنة صريحة ("يَختلف عن مفهوم الإمبريالية (Lenin)") — لا يوجد ملف thk- له في content/ar/thinkers. type مقترح: مفكر، part: philosophy.
  - **طلب slug جديد**: **هومي بابا (Homi Bhabha)** — مذكور بالاسم في مقارنة صريحة مع سعيد ("ما بعد الكولونيالية (Said، Bhabha)") — لا يوجد ملف thk- له في content/ar/thinkers. type مقترح: مفكر، part: philosophy.
- **con-commodity-fetishism.md**: related الموجود بالفعل (thk-marx، sch-marxism، wrk-capital-marx، con-alienation-marx) كله مبرَّر صراحة بالمتن (ماركس، رأس المال 1867، الماركسية الكلاسيكية، الاغتراب). لم يُعدَّل. لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-conscientization-paulo-freire / con-conscious-acts / con-contextualism-epistemic (2026-09-01)
- **con-conscientization-paulo-freire.md**: أُبقي thk-pfreire وthk-imartinbaro (مبرَّران صراحة بالمتن). أُضيف thk-eduardo-duran (مذكور بالاسم في فقرة "في علم النفس المناهض للاستعمار": "Eduardo Duran، Bonnie Duran") — الملف موجود وعنوانه "إدواردو دوران" مطابق. أُزيل wrk-freire-pedagogy-oppressed لأن عنوان العمل غير مذكور حرفياً في متن هذا الملف رغم كونه العمل المحوري لفريري — لا تبرير نصي مباشر.
  - **طلب slug جديد**: **Bonnie Duran** — مذكورة بالاسم بجانب إدواردو دوران في نفس الفقرة ("Eduardo Duran، Bonnie Duran") — لا يوجد ملف thk- لها في content/ar/thinkers. type مقترح: مفكرة، part: psychology.
- **con-conscious-acts.md**: أُبقي thk-brentano وthk-husserl وcon-intentionality-brentano وcon-phenomenology (مبرَّرون أصلاً بالمتن). أُضيف كل من ذُكر بالاسم صراحة في فقرات "الأثر الفلسفي والنفسي" و"الجدل المعاصر" ولم يكن مربوطاً: thk-john-searle (سيرل، *Intentionality* 1983)، thk-jerry-fodor (فودور، Language of Thought)، thk-rogers (كارل روجرز)، thk-aryle (جيلبرت ريل، "Ghost in the Machine")، thk-nussbaum (مارتا نوسباوم)، thk-freud (فرويد، فتح باب الأفعال اللاواعية) — كلهم موجودون فعلاً وعناوينهم مطابقة. لا طلب slug جديد.
- **con-contextualism-epistemic.md**: related كان مبنياً بالفعل بشكل صحيح — thk-dlewis مبرَّر صراحة بالمتن ("ديفيد لويس في مقالته Scorekeeping in a Language Game")، والعنوان مطابق فعلاً. لم يلزم أي تعديل. الفجوات المسجلة مسبقاً (belongs_to غير المبرَّر لـ br-logical-positivism-vienna-circle، وغياب DeRose/Cohen) خارج نطاق related ولم تُلمس.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-cultural-capital-bourdieu / con-cultural-complex / con-cultural-psychoanalysis (2026-09-01)
- **con-cultural-capital-bourdieu.md**: المتن سطر تعريف عام واحد فقط، لا يذكر بورديو ولا أي مفكر أو مدرسة أو عمل بالاسم إطلاقاً (رغم أن العنوان الإنجليزي "Cultural Capital Bourdieu" ينسب المفهوم إليه). تعذّر بناء أي related — لا يوجد اسم صريح بالمتن يبرر رابطاً واحداً. لم يُضَف related. الفجوات المسجلة سابقاً في الملف دقيقة وتغطي هذا بالضبط (لم تُعدَّل).
  - **طلب slug جديد**: **thk-bourdieu** (بيير بورديو، عالم الاجتماع الفرنسي، صاحب مفهوم رأس المال الثقافي والرمزي — *La Distinction*، 1979) — لا يوجد ملف thk- له في content/ar/thinkers رغم أن اسمه في en field لهذا الملف وملف trm-habitus-bourdieu (مذكور مسبقاً في MINIMAX.md). type مقترح: مفكر، part: philosophy.
- **con-cultural-complex.md**: related الموجود بالفعل (thk-singer، sch-psychoanalysis، con-complex) مبرَّر صراحة بالمتن (توماس سينغر مسمّى، "تطوير تحليلي معاصر" يمدد "العقدة النفسية"). لم يُعدَّل. صاموئيل كيمبر (Samuel Kimbles) مذكور بالاسم في المتن لكن لا ملف thk- له — مسجَّل في gaps الملف مسبقاً، لا طلب جديد (لم يُتحقق من الهجاء العربي الصحيح لاسمه).
- **con-cultural-psychoanalysis.md**: related الموجود بالفعل (thk-freud، thk-lacan، thk-jung، thk-erikson، thk-khorney، sch-psychoanalysis) كله مبرَّر صراحة بالمتن ("فرويد ولاكان"، "مشروع كارل يونغ"، "قراءة كارين هورني وإريك إريكسون"، "تيار في التحليل النفسي" أول سطر). لم يُعدَّل. تحقق من عدم وجود thk-zizek/thk-slavoj-zizek وthk-norman-holland/thk-nholland — كلاهما غائب فعلاً، مطابق لما هو مسجَّل في gaps الملف مسبقاً، لا طلب جديد (الأسماء بالعربي في المتن نفسه مشبوهة الدقة: "هاري ريتشاردسون (Harry Slochower)" و"مادلين لازاروس (Madeleine L. Lazenby)" لا تطابق الاسم الإنجليزي المرافق لها — مشكلة هوية خارج نطاق Task 9، تحتاج Task 3).
- **ملاحظة ازدواج محتمل (مطلوبة صراحة بالتاسك، لم تُدمج)**: con-cultural-complex.md وcon-cultural-unconscious.md (CON-0498) قد يكونا متكاملين/متداخلين موضوعياً — كلاهما "طبقة ثقافية وسيطة" في التحليل التحليلي اليونغي (اللاوعي الثقافي عند هندرسون 1962 مقابل المركّب الثقافي عند سينغر/كيمبر 2004)، لكنهما ملفان منفصلان بمفهومين مختلفين تاريخياً (الأول توسيع لـ"اللاوعي الجمعي" ليونغ، الثاني توسيع لـ"العقدة النفسية"). لم يُدمجا ولم يُربط أحدهما بالآخر لعدم ذكر أي منهما الآخر بالاسم في متنه؛ مسجَّلة هنا فقط لمراجعة رئيس التحرير.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-deliberative-democracy / con-demirge / con-demythologization (2026-09-01)
- **con-deliberative-democracy.md**: related الموجود بالفعل (thk-habermas، sch-deliberative-democracy، thk-cmouffe، thk-laclau، thk-spivak) كله مبرَّر صراحة بالمتن (هابرماس صاغه، نقد موف ولاكلاو الراديكالي، نقد سبيفاك ما بعد الكولونيالي). لم يُعدَّل. لا طلب slug جديد (بيسيت ويونغ مسجَّلان في gaps مسبقاً لعدم وجود ملف مطابق).
- **con-demirge.md**: related الموجود بالفعل (sch-gnosticism، thk-valentinus، con-gnosis، thk-plato، thk-plotinus، thk-athanasius، sch-manicheism) كله مبرَّر صراحة بالمتن (البعد الأفلاطوني/الغنوصي/الأفلوطيني/المانوي، ورفض إيريناوس وأثناسيوس). لم يُعدَّل. لا طلب slug جديد (إيريناوس مسجَّل في gaps مسبقاً).
- **con-demythologization.md**: related الموجود بالفعل (thk-bultmann، thk-heidegger، thk-barth، con-existence-existentialism) كله مبرَّر صراحة بالمتن (أنطولوجيا هايدجر، منهج بولتمان، جدل بارث). لم يُعدَّل. لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-derived-relational-responding / con-deus-sive-natura / con-devekut (2026-09-01)
- **con-derived-relational-responding.md**: related الموجود بالفعل (con-relational-frame-theory، sch-cognitive-behavioral، thk-lstevenhayes) كله مبرَّر: RFT مذكورة صراحة بالمتن، CBT هي edges.belongs_to، وهايز مذكور صراحة في "الأبحاث المُعاصرة" ("دراسات حديثة (Hayes، 2010s)"). لم يُعدَّل.
- **con-deus-sive-natura.md**: ملف مقتضب جداً (جملة تعريف واحدة فقط). related الموجود (thk-spinoza، sch-spinozism) مبرَّر بصفة "الأطروحة السبينوزية" و edges.belongs_to. لم يُعدَّل — لا اسم صريح إضافي بالمتن يبرر رابطاً جديداً.
- **con-devekut.md**: أُبقي كل الروابط الست الموجودة (كلها مبرَّرة بالمتن: بعل شيم طوف، شنور زلمن، مايستر إيكهارت، ابن عربي بالاسم، sch-hasidic بصفة "التصوف الحسيدي"). أُضيفت جملة توضيحية في المقدمة تربط الديفيقوت بالقبّالة اللوريانية (تسيمتسوم) لتبرير sch-kabbalah-lurianic الذي كان بلا جملة داعمة. أُضيف con-gelassenheit وcon-mindfulness (مذكوران صراحة بعنوانيهما الإنجليزيين في "الموضع الأوسع"، وعنوانا الملفين يطابقان). دوب ناخ من ميتريتش، الحلاج، وفيلنا غاون مذكورون بالاسم في المتن لكن بلا ملفات thk- — مسجَّلون في gaps، لا طلب slug جديد (لا يوجد اسم إنجليزي دقيق موثوق لهم في هذه الدفعة).
- **preflight_check.py**: راجع الأمر أدناه.
- **status:** معلق.

## Task 9 — con-deep-ecology-naess / con-deep-vs-shallow / con-deep-work (2026-09-01)
- **con-deep-ecology-naess.md**: أُعيد بناء related من الصفر. المتن كان يذكر أرني نايس فقط بالاسم؛ أُضيفت جملتان تبرران sch-deep-ecology (المدرسة التي أسسها) وwrk-ecology-community-lifestyle (كتابه *الإيكولوجيا والمجتمع ونمط الحياة*، حيث فصّل مبادئه)، وأُبقي con-deep-vs-shallow (مذكور ضمناً بتمييز "الإيكولوجيا الضحلة السطحية" المضاف). أُزيل sch-environmental-ethics من related (باقٍ في edges: belongs_to فقط) لعدم ذكره صراحة بالمتن.
- **con-deep-vs-shallow.md**: related الموجود بالفعل (sch-deep-ecology، thk-arne-naess، con-deep-ecology-naess) مبرَّر صراحة بالمتن ("نايس"، "الإيكولوجيا العميقة" مطابق حرفياً لعنوان sch-deep-ecology). أُضيف sch-ecofeminism لذكر "الـEcofeminism (الحركة البيئية النسوية)" صراحة بالمتن وعنوانه "النسوية البيئية (Ecofeminism)" مطابق.
  - **طلب slug جديد**: لا يوجد ملف sch- أو con- لـ"Gaianism" (فرضية غايا، جيمس لَفلوك James Lovelock) رغم ذكره صراحة بالمتن ("تَتقاطع مع الـGaianism… أقل تَكنولوجيا من Lovelock"). لم يُضَف رابط. type مقترح: مدرسة أو مفهوم، part: philosophy.
- **con-deep-work.md**: related الموجود بالفعل (thk-cal-newport، wrk-deep-work) صحيح مفهومياً لكن wrk-deep-work لم يكن مذكوراً صراحة بالمتن — أُضيفت جملة "صاغه كال نيوبورت في كتابه *العمل العميق: قواعد للنجاح المركز في عالم مشتت* (2016)" لتبريره صراحة. لا طلب slug جديد (عدم وجود sch- مطابق مسجَّل مسبقاً في gaps الملف).
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-drive-reduction / con-dukkha-suffering / con-dunbars-number (2026-09-01)
- **con-drive-reduction.md**: أُعيد بناء related من الصفر. أُضيف thk-ectolman (إدوارد تولمان، مذكور صراحة عبر "Tolman" في التراجع التاريخي، مع جملة موسّعة تسميه). أُبقيت الروابط الست الأخرى (thk-clhull، con-habit-strength، thk-nealmiller، thk-jdollard، thk-freud، thk-fskinner) كلها مبرَّرة صراحة بالمتن الأصلي (هال صاغها 1943، sHr، ميلر ودولارد وسّعاها، فرويد "التحليل النفسي"، سكينر "Positive Reinforcement"). أُضيفت جملة تبرر sch-cognitive-behavioral (كانت edges.belongs_to بلا جملة داعمة) تربط تقنيات التعزيز في CBT المعاصر بمبدأ خفض الدافع.
  - **طلب slug جديد**: كورت ليفين (Kurt Lewin، عالم نفس اجتماعي/جشطالتي، مؤسس نظرية المجال) مذكور صراحة بالمتن ("Expectancy-Value، Tolman، Lewin") بلا ملف thk- مطابق (بحثت بالعربي "ليفين" والإنجليزي "Lewin" في content/ar/thinkers، لا تطابق). type: مفكر، part: psychology.
  - **طلب slug جديد**: وولفرام شولتز (Wolfram Schultz، عالم أعصاب، باحث المكافأة الدوبامينية 1997) مذكور صراحة بالمتن ("بحث Schultz") بلا ملف thk- مطابق (thk-schulz الموجود هو بيتر شولتز، فيلسوف وجودي نمساوي معاصر — شخص مختلف تماماً). type: مفكر، part: psychology.
- **con-dukkha-suffering.md**: كان بلا related فعلي (جملة تعريف واحدة فقط، gaps تذكر صراحة "لا ذكر لأشخاص أو أعمال محددة بالاسم"). عُمِّق المتن بجملتين (المؤلف/المدرسة + موضع الدكها كحقيقة نبيلة أولى ناتجة عن الأنيكا/الأناتا ومنتهية بالسامسارا والنيرفانا) لتبرير روابط جديدة: thk-buddha، sch-buddhism-early، con-four-noble-truths-buddha، con-anikka-impermanence، con-anatta-non-self-concept، con-samsara، con-nirvana-extinction — كلها ملفات موجودة فعلاً وعناوينها مطابقة حرفياً للمذكور. لا طلب slug جديد.
- **con-dunbars-number.md**: أُبقي sch-social-psychology (الوحيد الموجود فعلياً في content/ar/schools لمجال المفهوم)، وأُضيفت جملة صريحة في المتن تربطه بعلم النفس الاجتماعي والتطوري معاً.
  - **طلب slug جديد**: روبن دانبار (Robin Dunbar) مذكور صراحة بالاسم بالمتن بلا ملف thk- مطابق (مسجَّل في gaps الملف الأصلي مسبقاً؛ يُعاد التسجيل هنا رسمياً). type: مفكر، part: psychology.
  - **طلب slug جديد**: مدرسة "علم النفس التطوري" (Evolutionary Psychology) مذكورة في crumb الأصلي كنص حر بلا slug مطابق في content/ar/schools (مسجَّلة في gaps مسبقاً؛ يُعاد التسجيل هنا رسمياً). type: مدرسة، part: psychology.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** مكتمل.

## Task 9 — con-enmeshment-disengagement.md
- طلب slug جديد من نوع `wrk-` لعمل سلفادور مينوشين *Families and Family Therapy* (1974، Harvard University Press) — مذكور في "## المرجع الأساسي" ولا يوجد ملف عمل موثّق له في works/.
- طلب slug جديد من نوع `wrk-` لعمل مينوشين وروزمان وبيكر *Psychosomatic Families* (1978، Harvard University Press) — نفس الملاحظة.

## Task 9 — con-enactivism-embodied-cognition / con-endurantism-vs-perdurantism / con-enmeshment-disengagement (2026-09-01)
- **con-enactivism-embodied-cognition.md**: related كان يحتوي رابطاً واحداً فقط (sch-phenomenology-somatic) وهو مبرَّر صراحة بالمتن ("يرتبط بذلك بتقليد الظاهراتية الجسدية"). لا يوجد ذكر صريح لأي thk-/con-/wrk- آخر (gaps الأصلي يؤكد غياب فاريلا وغيره بالاسم من المتن). لم يُعدَّل — بُقي كما هو بعد المراجعة.
- **con-endurantism-vs-perdurantism.md**: نفس الحالة — related يحتوي فقط sch-analytic-metaphysics، مبرَّر صراحة ("إشكالية مركزية في الميتافيزيقا التحليلية المعاصرة"). لا ذكر صريح لديفيد لويس أو غيره بالمتن. لم يُعدَّل.
- **con-enmeshment-disengagement.md**: related الموجود بالفعل (6 روابط: sch-systemic-family، br-structural-family، thk-sminuchin، con-family-structure، con-boundaries-psychological، con-differentiation-self) كلها مبرَّرة صراحة بالمتن (مينوشين مذكور مرتين، "العلاج الأسري البنيوي" في الجملة الافتتاحية، "البنية الأسرية الصحية"، "الحدود النفسية"، "التمايز الفردي/التمايز الفردي"). لم يتغيّر.
  - **طلب slug جديد**: `wrk-` لعمل مينوشين *Families and Family Therapy* (1974، Harvard University Press) — مذكور في "## المرجع الأساسي"، لا ملف works/ مطابق.
  - **طلب slug جديد**: `wrk-` لعمل مينوشين وروزمان وبيكر *Psychosomatic Families* (1978، Harvard University Press) — نفس الملاحظة، لا ملف works/ مطابق.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** مكتمل.

## Task 9 — con-exposure-hierarchy / con-expressivism-quasi-realism-blackburn / con-extended-mind-clark-chalmers (2026-09-01)
- **con-exposure-hierarchy.md**: أُعيد بناء related من الصفر. أُبقيت الروابط الخمسة الأصلية (thk-jwolpe، sch-cognitive-behavioral، thk-foa، tec-cbt-exp-exposure-hierarchy-building، con-exposure-habituation) — الأربعة الأولى مبرَّرة صراحة بالمتن الأصلي (وُلبّي 1958، فوا وكوزاك 1986، Habituation في الجدل الإكلينيكي)، وأُضيفت جملة صريحة تسمّي خطوات "البنية الإنشائية" بـ"بناء سلّم التعرض التدريجي" لتبرير tec-cbt-exp-exposure-hierarchy-building. أُضيف con-systematic-desensitization (مذكور صراحة "الحساسية المنهجية / Systematic Desensitization") وcon-reciprocal-inhibition (مذكور صراحة "مبدأ الاستجابة المضادة / Reciprocal Inhibition"). لا طلب slug جديد (Kozak/Bouton/Craske مسجَّلون في gaps الملف مسبقاً بلا ملف thk- مطابق).
- **con-expressivism-quasi-realism-blackburn.md**: المتن كان جملة تعريف واحدة بلا أي ذكر صريح لأشخاص أو مدارس أو جدل. عُمِّق بجملتين تسمّيان بلاكبيرن صراحة وتربطانه بـsch-analytic-metaphysics (belongs_to) وdbt-moral-realism-vs-moral-relativism، فأصبح related الموجود بالفعل (الاثنان) مبرَّراً صراحة بالمتن. لا طلب slug جديد (عدم وجود ملف مفكّر لسيمون بلاكبيرن مسجَّل في gaps الملف مسبقاً).
- **con-extended-mind-clark-chalmers.md**: المتن كان جملة تعريف واحدة بلا ذكر صريح لكلارك أو تشالمرز أو المدرسة أو الجدل رغم وجودهم في related. أُضيفت جملة تسمّي آندي كلارك وديفيد تشالمرز وسنة 1998 صراحة وتربط بـsch-phil-mind-analytic (belongs_to) وdbt-extended-mind-clark-chalmers، فأصبح related الموجود بالفعل (أربعة روابط) مبرَّراً صراحة بالمتن. لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-experiential-focusing / con-explanatory-gap-levine / con-exposure-habituation (2026-09-01)
- **con-experiential-focusing.md**: أُعيد بناء related من الصفر. أُبقيت الروابط الأربعة الأصلية (thk-gendlin، con-felt-sense، tec-focusing-oriented، wrk-focusing) بعد تصحيح عنوانين كانا مضطربين مع الملف الهدف فعلياً (con-felt-sense: "الإحساس الجسدي المُحسَّس (Felt Sense)"، tec-focusing-oriented: "العلاج الموجه بالتركيز والإحساس المعيش" بدل عنوانين منسوخين لا يطابقان الملفين الفعليين). أُضيف sch-humanistic (مدرسة جندلين) بجملة صريحة تسمّي جامعة شيكاغو وكارل روجرز، وجملة تربط wrk-focusing/tec-focusing-oriented بكتاب *Focusing-Oriented Psychotherapy* (1996). لا طلب slug جديد.
- **con-explanatory-gap-levine.md**: المتن كان جملتين بلا أي ذكر صريح لجوزيف ليفين أو الروابط الأربعة الموجودة أصلاً. أُضيفت جملة تسمّي ليفين وسنة 1983 صراحة وتربط المفهوم بـcon-hard-problem-of-consciousness وdbt-mind-body-dualism-vs-physicalism وcon-mind-body، فأصبحت الروابط الأربعة (عناوينها مطابقة فعلياً للملفات الهدف) مبرَّرة بالمتن. لم يُضَف قسم مصادر (لا مصدر موثّق متاح، والفجوة مسجَّلة أصلاً في gaps الملف).
  - **طلب slug جديد**: جوزيف ليفين (Joseph Levine)، فيلسوف عقل، صائغ مصطلح Explanatory Gap عام 1983 (*Materialism and Qualia: The Explanatory Gap*) — لا يوجد ملف thk- مطابق (ملفات thk-*levine* الموجودة كلها لأشخاص مختلفين تماماً: بيتر ليفين معالج الصدمة، أمير ليفين، إلخ). type: مفكر، part: philosophy.
- **con-exposure-habituation.md**: related الموجود بالفعل (tec-prolonged-exposure، tec-erp، thk-foa، dbt-memory-reconsolidation-vs-extinction) كلها مبرَّرة صراحة بالمتن الأصلي. أُضيف sch-cognitive-behavioral (مدرسة المفهوم) بجملة صريحة في الافتتاحية تسمّي CBT، وعُزِّز تبرير dbt-memory-reconsolidation-vs-extinction بجملة تربطه صراحة بخطوة الانقراض (Extinction). لا طلب slug جديد (Bouton مسجَّل في gaps الملف مسبقاً بلا ملف thk- مطابق).
- **preflight_check.py**: انظر التقرير أدناه.
- **status:** معلق.

## ⚠️ Task 9.30 — أولوية قصوى: تعارض ترميز Unicode محتمل + ازدواج فعلي
- **con-epoche-phenomenological-reduction.md** و **con-epoché-phenomenological-reduction.md** (الأخير بترميز NFD على القرص، e + combining accent U+0301): تم اكتشاف أن روابط أخرى كانت تشير للثاني بترميز NFC (é واحد U+00E9) فكانت تفشل preflight_check.py صامتة إلى أن ظهر الفحص الآلي المخالفة. صُحح الترميز في الروابط المُشيرة (لا تغيير في اسم الملف نفسه). **يحتاج قرار بشري عاجل**: هل الملفان محتوى مكرر فعلي (نفس مفهوم الإيبوخيه الهوسرلي بترميزين مختلفين للاسم بسبب bug تاريخي)، أم مفهومان متمايزان فعلاً؟ لو تكرار، يلزم دمج + redirect_to وليس مجرد ترك الملاحظة.
- con-epoche-suspension.md (بيرون الشكاك) موضوعه مختلف على الأرجح — أقل أولوية.
- **status:** عاجل — معلق.

## Task 9 — con-four-agreements / con-four-causes-aristotle / con-four-fundamentals-langle (2026-09-01)
- **con-four-agreements.md**: related الموجود بالفعل (wrk-four-agreements، thk-miguel-ruiz، sch-popular-psychology) مبرَّر صراحة بالكامل (كتاب رويز مذكور بعنوانه، رويز نفسه مذكور، وعلم النفس الشعبي في العنوان الرئيسي والمتن). لم يتغيّر.
- **con-four-causes-aristotle.md**: أُبقيت الروابط السبعة الأصلية (كلها مبرَّرة صراحة: أرسطو، Physica، الميتافيزيقا، المشائية، الهيلومورفية، الغائية، القوة والفعل). أُضيف thk-democritus (مذكور صراحة بالاسم "الذريين مثل ديمقريطس"). لا طلب slug جديد.
- **con-four-fundamentals-langle.md**: أُبقيت الروابط الخمسة الأصلية (لانغله، فرانكل، الوجودية العلاجية، dbt-langle-frankl، dbt-langle-frankl-meaning) كلها مبرَّرة صراحة بالمتن. أُضيف thk-rogers (مذكور صراحة بالاسم مرتين في قسم "في مقابل الشروط اللازمة والكافية لروجرز"). لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** مكتمل.

## Task 9 — con-externalizing-problem-reauthoring / con-fa-shu-shi-legalism / con-fa (2026-09-01)
- **con-externalizing-problem-reauthoring.md**: related الموجود بالفعل (6 روابط: sch-narrative-therapy، thk-mwhite، thk-depston، wrk-white-epston-narrative-means، con-unique-outcomes-sparkling، dbt-trauma-narrative-vs-medical-model) كلها مبرَّرة صراحة بالمتن (وايت وإبستون مذكوران بالاسم وكتابهما 1990، "الاستثناءات واللحظات المتألقة" مذكور بنص العبارة، والجدل السرد ضد الطبي مذكور صراحة). لم يتغيّر.
- **con-fa-shu-shi-legalism.md**: أُضيف thk-shang-yang (مذكور صراحة "أرساه شانغ يانغ" في قسم الفا). بقية الروابط الستة الأصلية مبرَّرة صراحة بالمتن (هان في تزو، كتابه، con-fa، con-shu، شين بو هاي مرتين). sch-legalism أُبقي كمدرسة بنيوية (belongs_to).
  - **طلب slug جديد**: `thk-` لشن داو (Shen Dao، القرن 4 ق.م)، صاحب فكرة «الشي» (السلطة المؤسسية) — مذكور صراحة مرتين في المتن ("السلطة المؤسسية عند شن داو" و"فكرة شن داو أن سلطة الحاكم مصدرها الموقع المؤسسي") لكن لا يوجد ملف thk-shen-dao. part: philosophy، type: مفكر.
- **con-fa.md**: أُضيف thk-xunzi (شون تزو، مذكور صراحة مرتين: "تلميذ الفيلسوف الكونفوشي شون تزو" و"موقف أستاذه شون تزو") وthk-mencius (منسيوس، مذكور صراحة "جدل الطبيعة البشرية ضد منسيوس"). بقية الروابط الثمانية الأصلية (sch-legalism، thk-shang-yang، thk-hanfeizi، wrk-hanfeizi، con-shu، con-fa-shu-shi-legalism، con-li، dbt-human-nature-debate) مبرَّرة صراحة بالمتن. لا طلب slug جديد إضافي.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** مكتمل.

## Task 9 — con-gender-performativity-concept / con-gender-performativity / con-general-will-rousseau (2026-09-01)
- **con-gender-performativity-concept.md**: أُعيد بناء related من الصفر. أُبقيت الروابط المبرَّرة صراحة بالمتن (thk-butler، wrk-gender-trouble، sch-queer-theory، con-queer-theory). أُضيف thk-jaustin (مذكور صراحة "نظرية أفعال الكلام عند جون أوستن") وthk-foucault (مذكور صراحة "تحليل ميشيل فوكو للخطاب والسلطة"). حُذف con-gender-performativity من related — علاقة الازدواج بينهما مسجَّلة بالفعل في gaps والملاحظة التحريرية بالمتن، لا كرابط related. لا طلب slug جديد.
- **con-gender-performativity.md**: أُعيد بناء related من الصفر. أُبقيت الروابط المبرَّرة صراحة (thk-butler، sch-feminism-french-poststructural، wrk-gender-trouble، sch-queer-theory، thk-foucault). أُضيف thk-jaustin (مذكور صراحة "Austin في فلسفة اللغة")، thk-derrida (مذكور صراحة في قسم "الأهمية النظرية": "أوستن، فوكو، دريدا")، thk-mackinnon وthk-firestone (كلاهما ناقدان مذكوران بالاسم في قسم "النقد"). حُذف con-gender-performativity-concept من related لنفس سبب الملف الأول. Halberstam مذكور بالنقد لكن لا يوجد ملف thk- مطابق — لم يُضَف (لا اختراع slug).
  - **ملاحظة ازدواج**: con-gender-performativity-concept.md وcon-gender-performativity.md يغطيان نفس مفهوم «الأداء الجندري عند بتلر» بصياغتين منفصلتين لم تُدمجا؛ كلاهما يحمل ملاحظة تحريرية صريحة بذلك في المتن وgaps. مسجَّل هنا فقط — يحتاج قرار بشري (دمج + redirect_to لا حذف).
- **con-general-will-rousseau.md**: أُعيد بناء related من الصفر. أُبقيت الروابط الأربعة المبرَّرة صراحة (thk-rousseau، sch-social-contract، wrk-the-social-contract-rousseau، con-amour-propre-vs-amour-de-soi). أُضيف thk-hobbes وthk-locke (مذكوران صراحة "إلى جانب هوبز ولوك... عن العقد الاجتماعي الليبرالي عند لوك"). لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-fundamental-attribution-error / con-fundamental-existential-motivations / con-fusion-horizons (2026-09-01)
- **con-fundamental-attribution-error.md**: أُبقيت الروابط الأربعة الأصلية (sch-social-psychology، con-self-serving-bias، stu-ross-fundamental-attribution-error، stu-heider-simmel-apparent-behavior) — كلها مبرَّرة صراحة بالمتن (لي روس 1977، هايدر وسيمل 1944، وقسم "علاقته بانحياز خدمة الذات" كامل). لم يتغيّر. لا يوجد ملف thk- للي روس، فريتز هايدر، إدوارد جونز، أو فيكتور هاريس — ملفات thk-jones وthk-harris الموجودة لأشخاص مختلفين تماماً (إرنست جونز محلل نفسي، أدريان هاريس)، فلم تُستخدم.
  - **طلب slug جديد**: `thk-` للي روس (Lee Ross)، عالم نفس اجتماعي، صائغ مصطلح Fundamental Attribution Error عام 1977 (*The Intuitive Psychologist and His Shortcomings*) — مذكور بالاسم مرتين في المتن. type: مفكر، part: psychology.
  - **طلب slug جديد**: `thk-` لفريتز هايدر (Fritz Heider)، صاحب تجربة الإدراك السببي مع ماريان سيمل 1944 — مذكور بالاسم في المتن وله بالفعل ملف stu- لكن لا ملف thk- مطابق. type: مفكر، part: psychology.
- **con-fundamental-existential-motivations.md**: الروابط الستة الأصلية (sch-existential-therapy، thk-schulz، thk-langle، thk-frankl، con-will-to-meaning، br-logotherapy) كلها مبرَّرة صراحة بالمتن (شولتز ولانغله صائغا النموذج، فرانكل والإرادة في المعنى، مدرسة GLE فرع من الوجودية العلاجية، العلاج بالمعنى). العناوين تطابق الملفات الهدف فعلياً. لم يتغيّر. لا طلب slug جديد.
- **con-fusion-horizons.md**: أُبقيت الروابط الثمانية الأصلية. اثنان منها (thk-ricoeur، con-dasein-being-there) لم يكونا مبرَّرين بالمتن الأصلي، فأُضيفت جملتان صريحتان: واحدة تربط الدازاين الهايدجري بفكرة الأفق عند غادامير، وأخرى تسمّي بول ريكور وهرمنيوطيقا السرد عنده مقارنة بغادامير. بقية الروابط (thk-gadamer، thk-heidegger، sch-hermeneutics، con-hermeneutics، con-hermeneutic-circle، con-fusion-of-horizons-gadamer) كانت مبرَّرة أصلاً. لا طلب slug جديد.
  - **ملاحظة ازدواج (مُسجَّلة أيضاً في gaps الملف نفسه)**: con-fusion-horizons.md وcon-fusion-of-horizons-gadamer.md (دفعة أخرى) يغطيان نفس مصطلح غادامير Horizontverschmelzung — الأول بامتداد نفسي/علاجي والثاني فلسفي بحت. لم يُدمجا بناءً على تعليمات المهمة (تسجيل فقط)، والرابط بينهما موثّق في كليهما. يحتاج قرار تحرير بشري لاحقاً (دمج أو تمييز أوضح في العنوانين).
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق.

## Task 9 — con-homeostasis (2026-09-01)
- **طلب slug جديد**: `thk-` لوالتر كانون (Walter Cannon)، عالِم الفيزيولوجيا الأمريكي، صائغ مصطلح Homeostasis عام 1926 — مذكور بالاسم في المتن. `thk-cannon` الموجود يخص بيتي كانون (Betty Cannon)، مفكرة وجودية معاصرة، شخص مختلف تماماً — لم يُستخدم. type: مفكر، part: psychology.

## Task 9 — con-hindsight-bias / con-hindutva / con-historical-materialism (2026-09-01)
- **con-hindsight-bias.md**: أُعيد بناء related من الصفر. أُبقيت الروابط الخمسة الأصلية (thk-kahneman، wrk-black-swan، thk-nassim-taleb، con-confirmation-bias، con-dunning-kruger-effect) — كلها مبرَّرة صراحة بالمتن. أُضيف thk-amos-tversky (مذكور صراحة "برنامج أبحاث الأحكام والحدس الذي طوّره مع آموس تفرسكي"). لا طلب slug جديد.
- **con-hindutva.md**: أُعيد بناء related من الصفر. أُبقيت sch-hindutva (belongs_to) وthk-savarkar (صائغ المفهوم، مذكور صراحة). أُضيف thk-shankara وthk-ramanuja (مذكوران صراحة بالاسم في قسم "الفرق عن مفاهيم مشابهة" — Shankara، Ramanuja). لم يُضَف رابط لنهرو (Nehru) ولا لموسوليني (Mussolini) رغم ذكرهما صراحة بالاسم — لا يوجد ملف thk- مطابق لأي منهما، فسُجّلا كطلب.
  - **طلب slug جديد**: `thk-` لجواهر لال نهرو (Jawaharlal Nehru)، أول رئيس وزراء للهند، ممثِّل القومية العلمانية المضادة للهندوتفا — مذكور صراحة بالاسم في المتن. type: مفكر، part: philosophy.
  - **طلب slug جديد**: `thk-` لبينيتو موسوليني (Benito Mussolini)، مذكور صراحة للمقارنة بين الهندوتفا والفاشية الأوروبية في تقديس الأمة والأرض. type: مفكر، part: philosophy.
- **con-historical-materialism.md**: أُعيد بناء related من الصفر. حُذف con-dialectics وcon-alienation-marx وcon-surplus-value-marx — الثلاثة غير مذكورين فعلياً في متن الملف الحالي (لا توجد جملة تبرّرهم). أُبقيت الروابط المبرَّرة صراحة (thk-marx، thk-engels، sch-marxism، thk-hegel، thk-lukacs، thk-antonio-gramsci، thk-weber، thk-karl-popper). أُضيف sch-frankfurt-school (مذكورة صراحة "مدرسة فرانكفورت")، thk-louis-althusser (ألتوسير، مذكور صراحة بقسم "الماركسيون اللاحقون")، thk-laclau (مذكور بالنص كـ"لاكروا" ضمن ثلاثي ما بعد الماركسية — تُعرَف بالاسم الصحيح إرنستو لاكلاو، الشريك المعتاد لموف في أدبيات ما بعد الماركسية)، thk-cmouffe (موف)، thk-badiou (بادييو)، thk-foucault وthk-derrida (مذكوران صراحة بقسم النقد: "ما بعد الحداثة: فوكو ودريدا نقدوا"). لم يُضَف رابط للينين ولا لروزا لوكسمبورغ ولا لكارل كورش رغم ذكرهم صراحة بالاسم — لا يوجد ملف thk- مطابق لأي منهم، فسُجّلوا كطلب.
  - **طلب slug جديد**: `thk-` لفلاديمير لينين (Lenin)، مذكور صراحة "اللينينية: لينين في «ما العمل؟» (1902) طبّقها في السياق الروسي". type: مفكر، part: philosophy.
  - **طلب slug جديد**: `thk-` لروزا لوكسمبورغ (Rosa Luxemburg)، مذكورة صراحة "الكسية (Luxemburg): قراءات ثورية". type: مفكرة، part: philosophy.
  - **طلب slug جديد**: `thk-` لكارل كورش (Karl Korsch)، مذكور صراحة ضمن "الماركسية الغربية: لوكاتش وكورش وغرامشي ومدرسة فرانكفورت". type: مفكر، part: philosophy.
- **preflight_check.py**: مخالفتان موجودتان مسبقاً وخارج نطاق هذه المهمة (تخص edges وgaps لا related) — con-hindsight-bias.md: edges target "علم النفس المعرفي والتجريبي" ليس slug حقيقياً؛ con-hindutva.md: سطر gaps يؤكد حقيقة بدل تسمية فجوة. لم تُلمَس (Task 9 = related فقط، القاعدة تمنع خلط المهام). con-historical-materialism.md: صفر مخالفات.
- **status:** معلق (بسبب طلبات slug جديدة + مخالفتا preflight خارج النطاق تحتاجان مهمة منفصلة).

## Task 9 — con-historical-trauma / con-ho-oponopono / con-homeostasis (2026-09-01)
- **con-historical-trauma.md**: أُعيد بناء related من الصفر. أُبقيت sch-indigenous-psychology وthk-mbraveheart وsch-liberation-psychology (مذكورة صراحة: "علم نفس التحرر (Martín-Baró)") وcon-intergenerational-historical-trauma (مقابلة في جدول "الفرق عن مفاهيم مشابهة") وcon-land-based-healing (مذكور صراحة "برامج الأرض» Land-Based Healing"). حُذف thk-jgone — موجود فقط كمسودة غير معتمدة في drafts/spark/thinkers/، ليس ملفاً منشوراً. طلب slug 'كارين ولترز' موجود مسبقاً في gaps الملف، أُبقي كما هو.
- **con-ho-oponopono.md**: أُعيد بناء related من الصفر. أُبقي thk-msimeona (مع تصحيح title المطابق فعلياً للملف الهدف: "مورّنا سيميونّا" بدل "مورانا سيميونا" غير المطابق). أُضيف thk-ihewlen (إِهالِيكالا هيو لين، مذكور بالاسم والتاريخ في المتن). حُذف con-autonomy-homonomy — لا جملة في المتن تبرر الصلة. حُذف أيضاً edges.belongs_to القديم ("الشفاء الهاوائي") لأنه نص حر وليس slug حقيقي — سجّلته preflight_check.py كمخالفة، ولا يوجد ملف sch- موثّق تحت هذا الاسم في الأطلس. حُذفت جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من gaps.
- **con-homeostasis.md**: أُعيد بناء related من الصفر. صُحح title لـaxm-homeostasis ("مبدأ الاستتباب (Homeostasis)" بدل "بديهية الاستتباب" غير المطابق) وsch-biological-neuro ("علم النفس البيولوجي والعصبي (Biological & Neuropsychology)" بدل الصيغة المبتورة). أُبقي con-drive-reduction وcon-adaptation (كلاهما مبرَّر صراحة بالمتن). حُذف thk-cannon — الـslug موجود فعلاً لكنه يخص بيتي كانون (Betty Cannon، مفكرة وجودية معاصرة)، شخص مختلف تماماً عن والتر كانون صائغ المصطلح 1926 المذكور في المتن.
  - **طلب slug جديد**: `thk-` لوالتر كانون (Walter Cannon) — مسجَّل أعلاه في نفس الملف.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة (بعد تصحيح مخالفة edges غير-slug وجملة القائمة السوداء في con-ho-oponopono.md).
- **status:** معلق.

## Task 9 — con-indra-net-huayan / con-inferiority-superiority-complex / con-inner-child-popular (2026-09-01)
- **con-indra-net-huayan.md**: أُعيد بناء related من الصفر. حُذف con-autonomy-homonomy (لا علاقة له بالمتن إطلاقاً، رابط حشو). أُبقي sch-huayan فقط (belongs_to مبرَّر، وأُضيفت جملة صريحة في المتن تسمّي المدرسة وFazang). حُذفت جملتا القائمة السوداء ("لا يوجد اقتباس مباشر موثوق متاح"، "حظي هذا المفهوم بمراجعات وتطويرات واسعة") من المتن وgaps واستُبدلتا بمحتوى فعلي.
  - **طلب slug جديد**: `thk-` لـFazang (643-712)، مبلور مدرسة هوايان الفلسفي — مذكور بالاسم مرتين في متن sch-huayan.md ومتن هذا الملف. type: مفكر، part: philosophy.
- **con-inferiority-superiority-complex.md**: أُعيد بناء related من الصفر. حُذف syn-impostor-syndrome وsyn-middle-child (غير مذكورين في المتن إطلاقاً). أُبقي thk-adler (مبرَّر بالاسم مرتين) وأُضيف wrk-adler-understanding-human-nature (كتاب 1927 مذكور الآن صراحة بالمتن بدل بقائه في gaps فقط). حُذف edges.belongs_to لأن هدفه "علم النفس الفردي (ألفرد أدلر)" نص حر بلا slug فعلي — سُجّل في gaps.
  - **طلب slug جديد**: `sch-` لمدرسة علم النفس الفردي الأدلرية (Individual Psychology) — مذكورة في crumb والعنوان لكن لا يوجد ملف schools/ مطابق (مؤكدة أيضاً في Task 13 كمدرسة أولوية مفقودة، 24 عضواً يتيماً). type: مدرسة، part: psychology.
- **con-inner-child-popular.md**: أُعيد بناء related من الصفر. أُبقي wrk-homecoming-inner-child (صُحح العنوان ليطابق الملف الهدف فعلياً: "...وحمايته") وthk-john-bradshaw. أُضيف thk-jung وcon-archetype (النمط البدئي للطفل) وthk-berne وtec-ego-state (حالة أنا الطفل) بعد نقل محتوى gaps القديم إلى فقرة متن صريحة جديدة "الجذور النظرية". حُذف edges.belongs_to الذي كان هدفه "علم النفس الشعبي" نصاً حراً، واستُبدل بـsch-popular-psychology (slug موجود فعلاً، تطابق تام). حُذفت جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من المتن.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة (بعد تصحيح edges غير الصالحة وحذف جمل القائمة السوداء، وهي أخطاء موجودة أصلاً في الملفات قبل هذه المهمة).
- **status:** مكتمل.

## ⚠️ Task 9.34 — أولوية عالية: عنقود con-imago مفتّت
- **con-imago.md**، **con-imago-childhood-wound.md**، **con-imago-fractured-self.md**، **con-imago-dialogue-process.md** + **tec-imago-dialogue-protocol.md**: خمسة ملفات تصف عملياً نفس البنية النظرية لهارفيل هندريكس (صورة الشريك اللاواعية / الجرح المتكرر / الذات المتشظية / حوار الإيماغو) من زوايا تسمية مختلفة بلا حدود مفاهيمية واضحة. يبدو تفتيتاً مصطنعاً أكثر من كونه مفاهيم متمايزة. يحتاج قرار دمج أو ترسيم حدود صريح.
- **status:** عاجل — معلق.

## Task 9 — con-intellectual-love-of-god / con-intentional-stance-dennett / con-intentionality-brentano (2026-09-01)
- **con-intellectual-love-of-god.md**: أُعيد فحص related. القائمة الموجودة (thk-spinoza، wrk-spinoza-ethics، con-sub-specie-aeternitatis، con-deus-sive-natura) مبرَّرة بالكامل بجمل صريحة في المتن أصلاً — لم يتغير شيء.
- **con-intentional-stance-dennett.md**: أُعيد بناء related. أُبقي thk-daniel-dennett وthk-john-searle وcon-functionalism-mind (كلها مبرَّرة صراحة بالمتن). أُضيف con-chinese-room-argument-searle لأن المتن يسمّي حجة "الغرفة الصينية" (1980) صراحة كنقد مباشر لسيرل، وكان هذا الرابط الأدق غائباً.
  - **طلب slug جديد**: `wrk-` لكتاب دانيال دينيت "الموقف القصدي" (The Intentional Stance، 1987) — مذكور بالاسم والتاريخ في المتن، لا يوجد ملف works/ مطابق حالياً.
- **con-intentionality-brentano.md**: أُعيد فحص related. القائمة الموجودة (8 عناصر: thk-brentano، thk-husserl، thk-daniel-dennett، thk-john-searle، thk-wsellars، con-phenomenology، con-qualia، con-conscious-acts) مبرَّرة بالكامل بجمل صريحة في المتن — لم يتغير شيء.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة، انظر الأمر أدناه.

### ⚠️ أولوية عالية — عنقود con-intentionality مكرر (لا يُدمج هنا، توثيق فقط)
ثلاثة ملفات شبه متطابقة الموضوع، لا حدود مفاهيمية واضحة بينها:
- `con-intentionality.md` (CON-0599, مبتدئ, الظاهراتية القارية)
- `con-intentionality-consciousness.md` (CON-1039, متقدم, "قصدية الوعي وهيكل التجربة")
- `con-intentionality-brentano.md` (CON-1300, متقدم, جسر فلسفة↔علم نفس, "القصدية عند برنتانو")
يحتاج قرار دمج أو ترسيم حدود صريح من رئيس التحرير — لم يُدمج أي منها في هذه المهمة تنفيذاً للتعليمات.

## Task 9 — con-ipt-problem-areas / con-ironic-process-theory / con-is-ought-problem-guillotine (2026-09-01)
- **con-ipt-problem-areas.md**: أُعيد بناء related من الصفر. أُبقي sch-ipt (belongs_to)، thk-gklerman، thk-mweissman (مؤسسا IPT، مذكوران صراحة في المقدمة)، con-five-stages-of-grief (مبرَّر صراحة: "يختلف IPT هنا عن مقاربة «مراحل الفجيعة الخمس» الكلاسيكية"). حُذف con-grief ("الحزن كمسار للتفريد") — لا جملة في المتن تبرّر هذا الرابط تحديداً (المتن يتكلم عن الفجيعة المعقّدة في IPT، إطار مختلف تماماً عن إطار con-grief). صُحح title لـdis-mdd من "الاكتئاب" (غير مطابق) إلى "اضطراب الاكتئاب الجسيم (MDD)" (العنوان الفعلي للملف الهدف). لا طلب slug جديد.
- **con-ironic-process-theory.md**: أُعيد بناء related من الصفر. أُبقي dis-ocd، dis-insomnia-disorder، sch-act، con-mindfulness، wrk-happiness-trap — كلها مبرَّرة صراحة في فقرة "التطبيقات في علاج الوسواس والأرق". أُضيف thk-russ-harris (مذكور بالاسم "شرحه راس هاريس بأسلوب شعبي في كتابه «فخ السعادة»" — الملف موجود بعنوان "روس هاريس"، نفس الشخص بتهجئة مختلفة).
  - **طلب slug جديد**: `thk-` لدانيال ويغنر (Daniel Wegner)، عالم النفس بجامعة هارفارد صائغ نظرية المعالجة الارتدادية عام 1987 وتجربة "الدب الأبيض" — مذكور صراحة بالاسم في متن الملف نفسه ولا يوجد ملف thk- مطابق له في الأطلس. type: مفكر، part: psychology.
- **con-is-ought-problem-guillotine.md**: أُعيد بناء related من الصفر. أُبقي thk-hume (belongs_to الفعلي وصائغ المفهوم) وsch-humeanism. أُضيف thk-ge-moore (مذكور صراحة بالاسم: "أعاد فلاسفة مثل جورج إدوارد مور صياغة الفكرة عبر «مغالطة الاستنتاج الطبيعي»"). لا طلب slug جديد.
- **preflight_check.py**: صفر مخالفات على الملفات الثلاثة.
- **status:** معلق (بسبب طلب slug جديد واحد لدانيال ويغنر).

## Task 9 — con-inner-experience / con-instrumental-reason-critique / con-integration-psychedelic (2026-09-01)
- **con-inner-experience.md**: أُعيد بناء related من الصفر. أُبقي thk-bataille (صاحب المفهوم)، thk-nietzsche، thk-sartre، thk-blanchot، con-ecstatic-moment (كلها مبرَّرة صراحة في المتن الأصلي). أُضيف sch-existential-therapy (belongs_to الفعلي)، thk-foucault وthk-derrida وthk-lacan (مذكورون صراحة في فقرة "الأثر": "ألهم فوكو... ودريدا... ولاكان وبلانشو")، thk-descartes وthk-kant وthk-dilthey (مذكورون صراحة كأطراف تعارض في فقرة "السياق الفلسفي")، con-death (مذكور صراحة ضمن ثلاثية "الألم، النشوة، الموت")، وwrk-madness-and-civilization-foucault (مطابق لـ"تاريخ الجنون" (1961) المذكور صراحة كأثر لباتاي على فوكو).
  - **طلب slug جديد**: `wrk-` للنص الأصلي لباتاي "L'Expérience intérieure" (1943) — هو العمل الذي صاغ المفهوم نفسه، مذكور بالاسم والتاريخ في `gaps` القديمة وفي `en:`، ولا يوجد ملف works/ مطابق.
  - **طلب slug جديد**: `con-` أو `wrk-` لمفهوم/كتاب "الجزء الملعون" (La Part maudite) لباتاي — مذكور صراحة بالاسم الفرنسي في فقرة "صلة بالنفقات اللامجدية" كمكمّل مباشر للخبرة الباطنية، ولا يوجد ملف مطابق.
  - **طلب slug جديد**: `wrk-` لمقالة سارتر "متصوف جديد" (Un nouveau mystique، 1943) — مذكورة بالاسم والتاريخ كنقد مباشر لكتاب باتاي، ولا يوجد ملف مطابق.
  - **طلب slug جديد**: `wrk-` لكتاب دريدا "الكتابة والاختلاف" (1967) — مذكور بالاسم والتاريخ في فقرة "الأثر"، ولا يوجد ملف works/ مطابق (بحثت عن `wrk-writing-and-difference-derrida` وما شابه، غير موجود).
- **con-instrumental-reason-critique.md**: أُعيد بناء related من الصفر. أُبقي thk-max-horkheimer وthk-adorno وthk-marcuse وwrk-dialectic-of-enlightenment-adorno-horkheimer وwrk-one-dimensional-man-marcuse (كلها مبرَّرة صراحة في المتن). أُضيف sch-frankfurt-school (belongs_to الفعلي، ومدرسة الثلاثة صراحة). لا طلب slug جديد لهذا الملف تحديداً (كتاب هوركهايمر "كسوف العقل"، Eclipse of Reason 1947، مذكور بالاسم لكن لا ملف works/ مطابق له في الأطلس — سُجّل أدناه كطلب منفصل لتفادي تكرار الفحص لاحقاً).
  - **طلب slug جديد**: `wrk-` لكتاب ماكس هوركهايمر "كسوف العقل" (Eclipse of Reason، 1947) — مذكور بالاسم والتاريخ في المتن بوصفه أول صياغة للنقد، ولا يوجد ملف works/ مطابق.
- **con-integration-psychedelic.md**: أُعيد بناء related من الصفر. أُبقي con-psychedelic-experience وtec-psychedelic-assisted-therapy (صُحح title إلى الاسم الفعلي "العلاج النفسي بمساعدة المواد السيكوديلية (PAP)")، con-psilocybin، rel-psychedelic-transpersonal (كلها مبرَّرة صراحة في المتن). أُضيف sch-psychedelic-assisted-therapy (belongs_to الفعلي)، con-mdma-ptsd (مذكور صراحة: "طُبّقت أساساً على مواد بعينها كالسيلوسيبين والـ MDMA")، وtec-holotropic-breathwork (مذكور صراحة: "استعارت بروتوكولات التكامل... أدوات من ممارسات التنفس الشامل (Holotropic Breathwork)"). لا طلب slug جديد لهذا الملف (معهد Chacruna وMAPS Integration ومدرسة Inner Trek مؤسسات وليست أشخاصاً أو مفاهيم مستقلة تستحق slug من نوع thk/con/wrk حسب معايير Task 9).
- **preflight_check.py**: نُفّذ على الملفات الثلاثة، انظر الأمر أدناه.
- **status:** معلق (بسبب أربعة طلبات slug جديدة: عمل باتاي الأصلي، "الجزء الملعون"، مقالة سارتر، كتاب دريدا، وكتاب هوركهايمر "كسوف العقل" — خمسة إجمالاً).

## Task 9 — con-jianai / con-jivanmukti-living-liberation / con-joining (2026-09-01)
- **con-jianai.md**: أُعيد بناء related من الصفر. أُبقي sch-mohism (belongs_to الفعلي)، thk-mozi (صاحب المفهوم)، thk-mencius (مذكور صراحة: "مِنسيوس سمّاه «الحبّ بلا أب»"). أُضيف sch-confucian-early (مذكورة صراحة كطرف الجدل: "الجدل الدائر بين الموهيين والكونفوشيّين"، وعنوان ملفها الفعلي "الكونفوشية المبكرة" يطابق الفترة الزمنية المقصودة). حُذف con-ren لأنه غير مذكور إطلاقاً في المتن الحالي (لا اسم ولا سياق يبرره حسب الشرط 4).
  - **ملاحظة تكرار (بدون دمج، حسب توجيه المهمة)**: `con-jianai.md` (هذا الملف) و`con-jian-ai-universal-love.md` (من دفعة سابقة) يبدوان تغطية لنفس المفهوم الصيني (جيان آي 兼愛) بعنوانين وslugين مختلفين. لم يتم الدمج بناءً على تعليمات المهمة — يُترك القرار لكلود.
- **con-jivanmukti-living-liberation.md**: كل الروابط الستة الموجودة أصلاً (sch-advaita-vedanta، thk-shankara، con-moksha-liberation، con-atman-brahman-vedanta، con-nirvana-extinction، dbt-advaita-vs-dvaita) مذكورة صراحة بالاسم في المتن الحالي وعناوينها مطابقة فعلياً لملفاتها المستهدفة — أُعيد كتابتها كما هي بعد التحقق من كل id/title مقابل الملف الفعلي (لا تغيير جوهري). لا طلب slug جديد.
- **con-joining.md**: أُعيد بناء related من الصفر. أُبقي sch-systemic-family (belongs_to الفعلي)، thk-sminuchin (صاحب المفهوم، مذكور بالاسم)، tec-structural-family-therapy (مذكور صراحة: "مفهوم محوري في العلاج الأسري البنيوي")، con-family-structure (مذكور صراحة: "يكشف بنية الأسرة... أين الحدود")، con-boundaries-psychological (مذكور صراحة عبر "الحدود العلاجية" و"تغيير الحدود" في فقرتي الآلية والانتقادات). حُذف con-subsystems وcon-enmeshment-disengagement لعدم ورود ما يبررهما بالاسم في المتن الحالي (الشرط 4). لم يُضَف رابط لـ"سلفيني" (مذكور بدون اسم أول في فقرة الأهمية السريرية: "الحياد العلاجي عند سلفيني") لأن يوجد ملفان محتملان (`thk-mselvini` لمارا سيلفيني-بالازولي و`thk-mtselvini` لماتيو سيلفيني) ولا يمكن حسم أيهما المقصود بثقة دون اختراع — لم يُطلب slug جديد لأن كلا الاثنين موجود فعلاً، والمشكلة غموض النص الأصلي لا نقص slug.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة، انظر الأمر أدناه.
- **status:** معلق (بسبب ملاحظة التكرار con-jianai / con-jian-ai-universal-love — تحتاج قرار كلود).

## ⚠️ Task 9.35 — أولوية عالية: عنقود con-intentionality الثلاثي
- con-intentionality.md (CON-0599) · con-intentionality-consciousness.md (CON-1039) · con-intentionality-brentano.md (CON-1300, part: bridge بخلاف الاثنين الآخرين part: philosophy). ثلاثتها عن نفس موضوع القصدية عند برنتانو/هوسرل بتداخل موضوعي قوي. مؤكد من 3 subagents مستقلين في نفس الدفعة. يحتاج قرار دمج أو ترسيم حدود.
- **status:** عاجل — معلق.

## Task 9 — con-li / con-liangzhi-innate-knowing / con-liangzhi (2026-09-01)
- **con-li.md**: أُعيد بناء related من الصفر. أُبقي sch-confucian-early (belongs_to الفعلي)، thk-confucius، wrk-lunyu (المحاورات/لون يو)، con-ren، con-zheng-ming، thk-xunzi (كلها مذكورة صراحة بالاسم في المتن الأصلي). أُضيف thk-wang-yangming (مذكور صراحة: "توتَّر مفهوم اللي بين تشو شي... ووانغ يانغ مينغ")، thk-zhu-xi (نفس الجملة، كان مفقوداً رغم ذكره صراحة)، thk-liang-shuming (مذكور صراحة: "استخدم ليانغ شو مينغ... كونفوشيوسية جديدة"). لم يُضَف رابط لـ"شيويه تشيانغ" المذكور بجوار ليانغ شو مينغ في نفس الجملة — لا يوجد ملف بعنوان مطابق (أقرب ملف موجود هو thk-xiong-shili بعنوان "شيونغ شي لي" وهو تهجئة مختلفة تماماً لا يمكن التأكد أنها نفس الشخص المقصود بثقة كافية لربطها بدون اختراع).
  - **طلب توضيح/slug**: تعريف هوية "شيويه تشيانغ" المذكور في con-li.md كمن استخدم إرث ليانغ شو مينغ لصياغة كونفوشيوسية جديدة — إما تصحيح الاسم في المتن ليطابق thk-xiong-shili الموجود فعلاً (لو كان المقصود شيونغ شي لي)، أو تسجيل thk- جديد لو شخص مختلف فعلاً.
- **con-liangzhi-innate-knowing.md**: أُعيد بناء related من الصفر بنفس الروابط الأربعة الأصلية (sch-xinxue belongs_to، thk-wang-yangming، con-liangzhi، con-zhixing-heyi) — كلها مذكورة صراحة في متن قصير جداً لا يذكر شيئاً إضافياً. **تكرار مؤكد سابقاً مع con-liangzhi.md** (كما ورد في gaps الملف نفسه) — لم يُدمج بناءً على توجيه المهمة، يُسجَّل هنا فقط.
- **con-liangzhi.md**: أُعيد بناء related من الصفر. أُبقي sch-xinxue (belongs_to الفعلي)، thk-wang-yangming، con-zhixing-heyi، con-li، thk-zhu-xi، sch-korean-neoconfucian (كلها مذكورة صراحة بالاسم). أُضيف thk-yi-i-yulgok (مذكور صراحة بالاسم الكامل "Yi I (Yulgok)" ونُسب صراحة لـ sch-korean-neoconfucian في نفس الجملة)، thk-mao-zedong (مذكور صراحة: "ماو تسي تونغ أعاد قراءة الحدس الأخلاقي")، sch-kogaku (مذكور صراحة: "نَقَلا أفكار الحدس الأخلاقي إلى Kogaku"). لم يُضَف رابط لـ"الضمير" المسيحي أو "العقل العملي" الكانطية أو "الأنا الأخلاقية" الفرويدية أو "الفطرة" الإسلامية — كلها مقارنات عامة بلا اسم علم أو عمل محدد قابل للربط بثقة (ملفا con-fitrah-* الموجودان لهما عناوين لا تطابق "الفطرة" وحدها).
  - **طلب slug جديد**: `thk-` لـ"Kumazawa Banzan" (كوماذاوا بانزان)، فيلسوف ياباني من القرن 17 نقل أفكار الحدس الأخلاقي إلى Kogaku — مذكور صراحة بالاسم، لا ملف مطابق.
  - **طلب slug جديد**: `thk-` لـ"Ito Jinsai" (إيتو جينساي)، فيلسوف ياباني من نفس الفقرة — مذكور صراحة بالاسم، لا ملف مطابق.
  - **طلب slug جديد**: `thk-` لـ"تشنغ تشونغ يينغ" (Cheng Chung-ying)، فيلسوف أخلاق أعاد قراءة الحدس الأخلاقي في إطار أخلاقيات الذكاء الاصطناعي في القرن 21 — مذكور صراحة بالاسم في نهاية المتن، لا ملف thk- مطابق (بحثت عن Cheng Chung-ying / Cheng Zhongying، غير موجود).
  - **طلب توضيح**: "حركة Nian" (انتفاضة الفلاحين 1851–1868) مذكورة صراحة كحدث تاريخي استخدم فيه مفهوم الحدس الأخلاقي — لا يوجد نوع ملف events/ ضمن صلاحيات هذا المسار الحالي يطابقها بثقة؛ تُسجَّل هنا للمراجعة فقط دون طلب slug فعلي.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة، انظر الأمر أدناه.
- **status:** معلق (بسبب طلبات slug جديدة لـ Kumazawa Banzan وIto Jinsai وCheng Chung-ying، وتوضيح هوية "شيويه تشيانغ"، وتكرار مؤكد con-liangzhi / con-liangzhi-innate-knowing بلا دمج).

## ⚠️ Task 9.37 — تصعيد عاجل: bug ترميز Unicode لسه بيمنع روابط جديدة
تأكيد ثالث (بعد 9.30 و9.35): ملف `con-epoché-phenomenological-reduction.md` اسمه على القرص مخزَّن بترميز NFD (e + combining accent)، والحل الجزئي في 9.30 (تصحيح ترميز id في الروابط الواردة القديمة) مش كافي — أي محاولة ربط **جديدة** لسه بتفشل/بتتجاهل الملف لأن preflight_check.py وأدوات أخرى بتقارن بالبايت. **الحل الوحيد الفعلي: rename الملف نفسه على القرص لترميز NFC القياسي** (`con-epoché-phenomenological-reduction.md` بترميز NFC بدل NFD)، مع تحديث كل الروابط الواردة بعدها.
- **status:** عاجل جداً — معلق، يحتاج تدخل رئيس التحرير مباشرة (rename + rebuild slug index).

## ✅ إغلاق: bug ترميز con-epoché (كان معلق منذ 9.30)
تم الحل الجذري بتاريخ 2026-09-01: أُعيد تسمية الملف فعلياً من NFD إلى NFC على القرص (`con-epoché-phenomenological-reduction.md`)، وصُححت حقول `id:` في كل من `con-epoche-phenomenological-reduction.md` و`con-epoche-suspension.md` لتطابق الترميز الجديد. `build_slug_index.py` و`preflight_check.py` نظيفان الآن على الملفات الثلاثة.
- **status:** مُغلق.

## Task 9 — con-myth-of-given / con-nafs-natiqa-rational-soul / con-name-of-father (2026-09-01)
- **con-myth-of-given.md**: أُعيد بناء related من الصفر. أُبقي thk-wsellars (صاحب المفهوم)، sch-critical-realism (belongs_to الفعلي)، thk-jmcdowell (مذكور صراحة: "ماكدوويل في «العقل والعالم» (1994) طوّر الموقف")، thk-rbrandom (مذكور صراحة: "براندوم في «بناء الفهم» (1994) أعاد بناء خرافة المعطيات"). أُضيف thk-donald-davidson (مذكور صراحة في قسم القيد: "الخلط بين خرافة المعطيات عند سيلارز ونقد البديهيات عند ديفيدسون"، وتحقق العنوان "دونالد ديفيدسون" مطابق فعلياً). لا توجد ملفات wrk- لـ"العقل والعالم" أو "بناء الفهم" أو مقال سيلارز الأصلي 1956 — لم تُطلب slug جديد لأنها أعمال ثانوية غير محورية للمفهوم نفسه، تُترك كملاحظة فقط.
- **con-nafs-natiqa-rational-soul.md**: تحقق كامل — كل الروابط السبعة الموجودة أصلاً (sch-islamic-peripatetic، thk-ibn-sina، thk-al-farabi، thk-aristotle، con-hylomorphism، con-tripartite-soul-plato، con-soul-psyche-classical) مذكورة صراحة بالاسم في المتن الحالي وعناوينها مطابقة فعلياً لملفاتها المستهدفة. أُعيد كتابتها كما هي (لا تغيير جوهري). لا طلب slug جديد.
- **con-name-of-father.md**: أُعيد بناء related من الصفر. أُبقي thk-lacan (صاحب المفهوم)، sch-psychoanalysis (belongs_to)، wrk-ecrits (مذكور صراحة كمصدر التجميع)، con-oedipus-complex (مذكور صراحة ومقارَن به مباشرة)، thk-jcmilner (مذكور صراحة). أُضيف thk-freud (مذكور صراحة عدة مرات: "عند فرويد عقد أوديب بيولوجي..."، والمفهوم يفسَّر كإعادة قراءة رمزية لعقدة أوديب الفرويدية)، thk-claude-levi-strauss (مذكور صراحة بالاسم: "حلقة وصل بين Lacan، Saussure، و Lévi-Strauss (البنيوية)"، والعنوان "كلود ليفي-ستراوس" مطابق فعلياً).
  - **طلب slug جديد**: `thk-` لـ Ferdinand de Saussier (فرديناند دو سوسير)، مذكور صراحة بالاسم في نفس الجملة أعلاه ("Saussure (اللغة)") كطرف في الأصول البنيوية للمفهوم — لا يوجد ملف thk- مستقل باسمه (موجود فقط كإشارة عابرة داخل ملفات مفكرين آخرين مثل thk-lacan وthk-roland-barthes وthk-noam-chomsky)، لم يُربط تجنباً لاختراع slug.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة، انظر الأمر أدناه.
- **status:** مغلق (طلب slug واحد معلق لـ Saussure، لا يمنع نشر الملفات الثلاثة).

## Task 9 — batch (concepts psychedelic/psychiatric-reform/psychoeducation)

- **con-psychedelic-experience.md**: أُعيد بناء related من الصفر. الروابط الخمسة الأصلية (sch-psychedelic-assisted-therapy، con-trauma، tec-psychedelic-assisted-therapy، con-psilocybin، rel-psychedelic-transpersonal) كل عناوينها مطابقة فعلياً لملفاتها المستهدفة، لكن أربعة منها لم يكن لها جملة تبرير صريحة في المتن — أُضيفت جمل تبرير لكل رابط (إعادة معالجة الصدمة، بروتوكول PAP، السيلوسيبين كأكثر مادة مبحوثة، والجذر التاريخي المشترك مع علم النفس عبر الشخصي عبر ستانيسلاف غروف) بلا اختراع حقائق جديدة.
  - **طلب slug جديد**: `thk-` لـ Humphry Osmond (همفري أوزموند، صاغ مصطلح Psychedelic في رسالة مفتوحة 1952) و`thk-` لـ Aldous Huxley (ألدوس هكسلي، متلقي الرسالة) — كلاهما مذكور بالاسم في متن الملف كصاحبَي الحدث المؤسِّس للمصطلح، ولا يوجد ملف مفكر مستقل لأي منهما. لم يُربطا تجنباً لاختراع slug.
- **con-psychiatric-reform.md**: راجعتُه بالكامل ولم أعدّل related — الروابط الستة كلها (thk-nisesilveira، sch-psychoanalysis، thk-jung، br-antipsychiatry، ctx-deinstitutionalization-psychiatric-reform، con-schizophrenia) مذكورة صراحة بالاسم في المتن مع جملة تبرير واضحة لكل واحد، وعناوينها مطابقة فعلياً لملفاتها المستهدفة. مطابق لمعيار Task 9 كما هو، لم يُكتب مسودة.
- **con-psychoeducation.md**: أُعيد بناء related — حُذف `con-autonomy-homonomy` (مفهوم أنجيال الوجودي 1941-1965) لعدم وجود أي ذكر له في المتن ولا صلة موضوعية فعلية بالتثقيف النفسي الإكلينيكي المعاصر (كان رابطاً غير مبرَّر موروثاً). الروابط الأربعة الباقية (br-psychoeducation، thk-jcawley، dis-bipolar-i، dis-schizophrenia) كلها مبرَّرة صراحة في المتن وعناوينها مطابقة. لا طلب slug جديد لهذا الملف.
- **preflight_check.py**: نُفّذ على الملفين المُعاد بناؤهما (con-psychedelic-experience، con-psychoeducation) في `content/ar/drafts/minimax/concepts/` + الملف المعتمد con-psychiatric-reform.md — صفر مخالفات آلية في الثلاثة.
- **status:** مغلق (طلبا slug معلّقان لأوزموند وهكسلي، لا يمنعان نشر الملفات الثلاثة).

## Task 9 — con-rigid-designators-kripke / con-risk-need-responsivity / con-rogers-person-centered-therapy (2026-09-01)
- **con-rigid-designators-kripke.md**: الروابط الأربعة الأصلية (thk-skripke، wrk-naming-and-necessity-kripke، con-possible-worlds-semantics-kripke، sch-analytic-metaphysics belongs_to، thk-hputnam) مبرَّرة صراحة في المتن. أُضيف con-sense-vs-reference (مفهوم مجاور/مضاد فعلي: كريبكي استبدل تمييز فريجه بين المعنى والمرجع بالتصميم الصارم — موثّق داخل con-sense-vs-reference.md نفسه). كُشف أيضاً أن الملف كان يحمل جملاً قالبية من القائمة السوداء ("يمثل هذا المفهوم لبنة تأسيسية..."، "شكل هذا المفهوم منطلقاً لحوارات...") وسطر gaps وهمي ("لا يوجد اقتباس مباشر موثوق متاح") — استُبدلت الفقرة بمحتوى فعلي (تاريخ الصياغة 1970/1972، الاعتراض على نظرية الوصف لفريجه ورَسل، مثال أرسطو، حجة الضرورة البَعدية) وحُذف سطر الاقتباس الوهمي. preflight_check كشف أيضاً عدم تطابق عنوان con-sense-vs-reference المكتوب مع عنوان الملف الحقيقي ("المعنى مقابل المحمول") — صُحح.
- **con-risk-need-responsivity.md**: الروابط الثلاثة (br-therapeutic-risk-assessment، con-relapse-prevention-sexual، con-restorative-justice) مبرَّرة صراحة وعناوينها مطابقة. حُذف سطر gaps الوهمي "لا يوجد اقتباس مباشر موثوق متاح" (قائمة سوداء)، ودُمج مضمونه في سطر gap الأول.
  - **طلب slug جديد**: `thk-` لـ James Bonta و`thk-` لـ Don Andrews (Public Safety Canada)، مؤسسا إطار RNR في التسعينيات، مذكوران بالاسم في المتن — لا ملف thk- مطابق لأي منهما.
- **con-rogers-person-centered-therapy.md**: الروابط التسعة كلها مذكورة بالاسم أو بمضمونها المباشر في المتن ومبرَّرة. preflight_check كشف عدم تطابق عنوان con-unconditional-positive-regard المكتوب ("UPR") مع عنوان الملف الحقيقي — صُحح.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة المعتمدة بعد التصحيحات — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق لـ Bonta وAndrews، لا يمنع نشر الملفات الثلاثة).

## Task 9 — con-shinrin-yoku / con-shu / con-shunyata-emptiness (2026-09-01)
- **con-shinrin-yoku.md**: `edges.belongs_to` كان يشاور على نص حر "العلاج البيئي/الطبيعي" مش slug — حُذف (المدرسة sch-ecotherapy غير موجودة، مسجّلة أصلاً في agents_specs/missing-schools.md). أُعيد بناء related: أُبقي thk-mlouv وtec-forest-therapy، أُضيف con-nature-deficit، وأُضيفت جملة صريحة في المتن تربط ريتشارد لوف ومتلازمة عجز الطبيعة بالممارسة (لم تكن مذكورة بالاسم من قبل رغم وجود الرابط). حُذفت جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من gaps. حُذف أيضاً ادّعاء غير معقول في المتن (هيئة المسح الجيولوجي الأمريكية USGS تدمج "وصف الغابات" في الرعاية الصحية — جهة جيولوجية لا صحية، خطأ نسبة واضح) واستُبدل بملاحظة gaps. أُضيف `## المصادر` (Miyazaki، Qing Li، Louv).
- **con-shu.md**: أُضيف sch-legalism وthk-hanfeizi (مذكور بالاسم فعلاً في المتن: "هان في تزو") إلى related. أُضيف `## المصادر` (Han Feizi الفصول 5/30، Creel 1970 المذكور أصلاً في المتن).
- **con-shunyata-emptiness.md**: أُضيف sch-madhyamaka لـrelated، وأُضيفت جملة صريحة في المتن تسمّي ناغارجونا ومدرسته. حُذفت جملة القائمة السوداء من gaps واستُبدلت بثلاث فجوات فعلية. أُضيف `## المصادر` (Mūlamadhyamakakārikā).
  - **ازدواج مُسجَّل لا حسم**: con-shunyata-emptiness.md شبه مطابق موضوعياً لـcon-shunyata.md (كلاهما عن نفس المفهوم البوذي، نفس المدرسة sch-madhyamaka، نفس المفكر thk-nagarjuna؛ con-shunyata أعمق وأكثر توثيقاً بمراتب). لم يُدمج — القرار متروك لرئيس التحرير.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق.

## Task 9.45 — دمج مؤكَّد ومطبَّق: con-sense-and-reference-frege → con-sense-vs-reference
تكرار مؤكَّد فعلياً (نفس تمييز فريجه Sinn/Bedeutung، الثاني أعمق وأشمل توثيقاً). طُبِّق الدمج مباشرة حسب القاعدة 6 في MINIMAX.md: con-sense-and-reference-frege.md تحوّل لإحالة `[حجر]`، والروابط الواردة (con-compositionality-principle-frege.md، syn-anomic-aphasia.md) صُححت لتشاور con-sense-vs-reference مباشرة.
- **status:** مُغلق (تم التنفيذ).

## Task 9.45 — تكرار جديد: con-sensorimotor-three-way-model / con-three-way-model-sensorimotor
الثاني نص مشوَّه بعلامات تشكيل/ترجمة آلية غريبة وبلا مصادر، ومربوط فعلياً بالمعتمد كـrelated من الطرفين. يحتاج قرار دمج/حجر.
- **status:** معلق.

## Task 9 — con-standpoint-epistemology / con-state-of-exception-agamben / con-status-anxiety-concept (2026-09-01)
- **con-standpoint-epistemology.md**: `related` كان يشاور thk-bhooks وthk-mohanty بلا أي ذكر لهما في المتن. استُبدلا بـthk-phcollins وthk-nussbaum وthk-butler وthk-spivak، الأربعة مذكورون بالاسم فعلاً في المتن (كولينز في التعريف، نوسباوم وبتلر وسبيفاك في قسم النقد). حُذفت جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من `gaps` واستُبدلت بفجوة فعلية (لا مراجعة من مصدر أولي لنصي Smith 1974 وHarding 1986).
- **con-state-of-exception-agamben.md**: إعادة كتابة كاملة — كان المتن قالبياً بالكامل (3 جمل من القائمة السوداء حرفياً)، بلا `related`، وبـ`edges.belongs_to` يشاور نصاً حراً "الفلسفة الإيطالية المعاصرة" وليس slug. حُذف الرابط (لا مدرسة بهذا slug موجودة) — **طلب slug جديد**: `sch-` لـ"الفلسفة الإيطالية المعاصرة" أو تصنيف أدق لأغامبين ضمن مدرسة قائمة، غير محسوم. أُعيد بناء المتن بمادة حقيقية موثقة (تعريف أغامبين 2003، علاقته بشميت وبالحياة العارية وبيوبوليتيك فوكو، نقد من الحقل القانوني)، وأُضيف `related` (thk-giorgio-agamben، con-bare-life-homo-sacer، con-biopolitics-and-biopower، thk-foucault) و`## المصادر` (Agamben 2003، Schmitt 1922).
- **con-status-anxiety-concept.md**: تصحيح تطابق id/title في `related` (عنوانا wrk-status-anxiety وsyn-duck-syndrome كانا مبتورين عن العنوان الحقيقي). أُضيفت في المتن جمل صريحة تسمّي آلان دو بوتون وكتابه ومتلازمة البطة بالاسم (لم تكن مذكورة إطلاقاً رغم وجود الروابط). حُذفت جملة القائمة السوداء من قسم "اقتباسات مختارة" واستُبدل القسم بفقرة "صورة معاصرة للمفهوم". حُذف `edges.belongs_to` (نص حر "الفلسفة النفسية التطبيقية" بلا slug مطابق) — **طلب slug جديد**: لا مدرسة موجودة لهذا التصنيف الشعبي/العلاجي، القرار متروك لرئيس التحرير إن كان يستحق مدرسة أصلاً. أُضيف `## المصادر` (De Botton 2004).
- **preflight_check.py**: نُفّذ على الملفات الثلاثة بعد التصحيحات — صفر مخالفات آلية.
- **status:** مغلق (طلبا slug معلقان لا يمنعان نشر الملفات الثلاثة).

- **thk-jaegwon-kim (طلب slug جديد)**: جايجوون كيم (Jaegwon Kim، 1934–2019)، فيلسوف كوري-أمريكي، صاحب التصنيفات الدقيقة للمواكبة الأنطولوجية (الضعيفة/القوية/العالمية) في مقاله Concepts of Supervenience (1984) وكتابه Supervenience and Mind (1993)، ومحرك رئيسي في نقاش الفيزيائية غير الاختزالية في فلسفة العقل. لا يوجد ملف باسمه في الأطلس (تحقق: thk-kimkwansung هو شخص مختلف "كيم كوان-سونغ" لا جايجوون كيم). طُلب أثناء تعديل con-supervenience-metaphysics.md.

## Task 9 — con-two-eyed-seeing / con-two-truths-doctrine-buddhist / con-tyranny-of-the-majority (2026-09-01)
- **con-two-eyed-seeing.md**: تحقّق فقط — الملف بالفعل موثّق جيداً (تعريف، مبررات، تطبيقات، مقارنة جدولية، مصادر ثلاثة)، وصفر مخالفات آلية أصلاً. لم يُعدَّل.
- **con-two-truths-doctrine-buddhist.md**: إعادة كتابة كاملة — كان قالبياً بالكامل (4 جمل من القائمة السوداء حرفياً في المتن وgaps)، بلا `related`. أُضيف `related` (thk-nagarjuna، sch-madhyamaka، sch-yogacara، con-shunyata-emptiness) وأُعيد بناء المتن: من صاغ العقيدة (ناغارجونا، مولاماديامكاكاريكا الفصل 24) وما كان يعارضه (الواقعية الأبهيدارمية والعدمية)، التعريف الدقيق للحقيقتين، تطورها عبر مدرستين (مادهياماكا سفاتانتريكا/برَسانغيكا، ويوغاكارا عبر الطبائع الثلاث)، الاستعمال التأملي، النقد (اتهام عدمية، قراءة سيديريتس الدلالية)، و`## المصادر` (Garfield 1995، Siderits & Katsura 2013). **طلب slug جديد**: `wrk-` لـ*مولاماديامكاكاريكا* غير موجود، مسجَّل في gaps.
- **con-tyranny-of-the-majority.md**: إعادة كتابة كاملة — نفس الأنماط القالبية (3 جمل قائمة سوداء). أُضيف `related` (thk-mill، thk-montesquieu، wrk-on-liberty-mill، sch-classical-liberalism-early، sch-deliberative-democracy) وأُعيد بناء المتن: من صاغ العبارة فعلياً (توكفيل 1835 لا ميل) وما كان يعارضه، الفرق الدقيق بين نسخة توكفيل الدستورية-المؤسسية ونسخة ميل الاجتماعية-الثقافية (1859)، الأصل عند مونتسكيو، الاستعمال في الديمقراطية التداولية، النقد (استبداد الأقلية المضاد، تناقض ميل الاستعماري). **طلب slug جديد**: لا يوجد `thk-tocqueville` في الأطلس رغم أنه صاحب العبارة الأصلية — مسجَّل في gaps. كذلك لا يوجد `wrk-` لـ*الديمقراطية في أمريكا*.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة بعد التصحيحات — صفر مخالفات آلية.
- **status:** مغلق (طلبا slug معلقان — thk-tocqueville وwrk- لكتابي مولاماديامكاكاريكا والديمقراطية في أمريكا — لا يمنعان نشر الملفات الثلاثة).

## ⚠️ Task 9.49 — أولوية عالية: عنقود ubuntu الثلاثي + طلب slug عاجل
- **con-ubuntu.md / con-ubuntu-african-humanism.md / con-ubuntu-relational-health.md**: ثلاثة ملفات تتقاطع في نفس التعريف الافتتاحي «أنا أكون لأننا نكون» — يحتاج قرار دمج/فصل.
- **thk-tocqueville**: أليكسيس دو توكفيل، صاحب عبارة "استبداد الأغلبية" (1835، *الديمقراطية في أمريكا*) — لا يملك ملف مفكر في الأطلس إطلاقاً رغم كونه أصل المصطلح المذكور في con-tyranny-of-the-majority.md. طلب عاجل.
- **status:** عاجل — معلق.

## Task 9 — con-yoga-therapy-concept / con-zeigarnik-effect / con-zeitgeist-spirit-of-the-age (2026-09-01)
- **con-yoga-therapy-concept.md**: `edges.belongs_to` كان يشاور نفس ملفه (`con-yoga-therapy-concept` كمدرسة!) — خطأ نسخ-لصق. صُحح إلى `sch-yoga` (موجود فعلاً). `related` كان يشاور thk-dchopra (ديباك شوبرا، غير مذكور في المتن إطلاقاً) وcon-autonomy-homonomy (بلا صلة مذكورة) — استُبدلا بـthk-iyengar، مذكور بالاسم في قسم المؤسسين فعلاً. حُذفت جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" من `gaps` واستُبدلت بفجوات فعلية (لا slug لـSatchidananda/Krishnamacharya/Desikachar، لا `## المصادر` موثقة).
- **con-zeigarnik-effect.md**: `edges.belongs_to` كان يشاور نصاً حراً "علم النفس الجشطالتي والمعرفي" وليس slug — حُذف (لا مدرسة بهذا الاسم موجودة؛ sch-gestalt-therapy مدرسة علاجية مختلفة تماماً). **طلب slug جديد**: مدرسة "علم النفس الجشطالتي التجريبي/البرليني" (فرتهايمر-كوفكا-كوهلر-ليفين) غائبة كلياً رغم أن تأثير زيغارنيك صيغ داخلها مباشرة — هذا يطابق فجوة موثقة في MINIMAX.md Task 13. كذلك **طلب slug**: thk-lewin (كورت ليفين، المشرف المباشر على تجربة زيغارنيك 1927) لا ملف له، وthk-zeigarnik موجودة فقط كمسودة minimax لم تُرقَّ بعد فلا يمكن الربط بها من ملف معتمد. صُححت عناوين `related` (wrk-getting-things-done وcon-getting-things-done-gtd كانا مبتورين عن العنوان الحقيقي). أُعيد بناء المتن: أضيف قسم "الأصل التجريبي (1927)" يسمّي زيغارنيك وليفين وبرلين وملاحظة النوادل بالتفصيل (كان غائباً كلياً من المتن رغم أنه أساس المفهوم)، وربط GTD بديفيد ألين بالاسم. حُذف قسم "اقتباسات مختارة" القائمة السوداء وأُضيف `## المصادر` (Zeigarnik 1927، Allen 2001).
- **con-zeitgeist-spirit-of-the-age.md**: إعادة كتابة كاملة — كان المتن قالبياً بالكامل (جملتان من القائمة السوداء حرفياً "يمثل هذا المفهوم لبنة تأسيسية..." و"حظي هذا المفهوم بمراجعات وتطويرات واسعة")، بلا `related` إطلاقاً. أُضيف `related` (thk-hegel، مذكور بالاسم في المتن). أُعيد بناء المتن: من صاغ المفهوم فلسفياً (هيغل، فينومينولوجيا الروح 1807) وما هو أصل المصطلح لغوياً قبله (هردر 1769)، وتطوره اللاحق خارج السياق الديالكتيكي الهيغلي الصارم. أُضيف `## المصادر` (Hegel 1807). **طلب slug جديد**: thk-herder (يوهان غوتفريد هردر) غير موجود رغم أنه صاحب الاستخدام الأول للمصطلح، مسجَّل في gaps.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة بعد التصحيحات — صفر مخالفات آلية.
- **status:** مغلق (طلبات slug معلقة — sch- للجشطالت التجريبي، thk-lewin، thk-herder — لا تمنع نشر الملفات الثلاثة).

## ⚠️ Task 11.1 — أولوية عالية: نمط مصادر ملفَّقة مكتشف
crt-commodification-critique.md كان فيه إسناد لمرجعين لا وجود لهما فعلياً ("Felix Marton 2014"، "Ronen Berg 2014" — لا أثر لهما في أدبيات نقد علم النفس الإيجابي). صُححا بأسماء المؤلفين الحقيقيين (Carl Cederström وAndré Spicer، كتاب *The Wellness Syndrome*). **هذا النمط يستحق فحصاً منهجياً أوسع عبر باقي ملفات critiques/ (276 ملف) — احتمال وجود مصادر ملفَّقة أخرى مشابهة من عمل سابق قبل هذا التتابع.**
- **status:** عاجل — معلق.

## Task 11 — debates/ (dbt-aurobindo-vs-vivekananda, dbt-boss-binswanger, dbt-brain-in-a-vat-skepticism) (2026-09-01)
- **dbt-brain-in-a-vat-skepticism.md**: إعادة كتابة كاملة — المتن كان قالبياً بالكامل (3 جمل من القائمة السوداء حرفياً: "لا يوجد اقتباس مباشر موثوق متاح"، "يقدم هذا الموقف رؤية نسقية تستند إلى براهين..."، "يقدم الطرف المقابل قراءة نقدية بديلة تكشف الثغرات..."). حُدد الطرفان الحقيقيان بالبحث: هيلاري بوتنام (*Reason, Truth and History*، 1981، حجة نظرية الإحالة السببية) وأنطوني بروكنر (نقده "Brains in a Vat"، *Journal of Philosophy* 83، 1986، وتطويره في *Mind* 101، 1991). `edges.belongs_to` كان يشاور `br-logical-positivism-vienna-circle` (خطأ مجال — بوتنام حجة تحليلية لاحقة على الوضعية المنطقية بعقود، لا علاقة نصية) — صُحح إلى `sch-phil-mind-analytic`. أُضيف `related` (thk-hputnam، thk-descartes، sch-academic-skepticism) و`## المصادر` (Putnam 1981، Brueckner 1986، Brueckner 1991). **طلب slug جديد**: thk- لأنطوني بروكنر (Anthony Brueckner) غير موجود رغم كونه الطرف الثاني الفعلي في هذا الجدل بالذات — مسجَّل في gaps الملف.
- **dbt-boss-binswanger.md**: تصحيحات — `related` كان بعناوين مبتورة لا تطابق عناوين الملفات المستهدفة (`br-daseins` بعنوان "التيار" بدل "التحليل الوجودي والدازاين"، الاسمان "بينسوانغر"/"بوس" بدل الاسمين الكاملين) — صُححت. `level` كانت فارغة — عُبّئت "متقدم". `active_start` كانت null رغم أن بداية تعاون بوس مع هايدجر (1947) موثّقة تاريخياً — عُبّئت. أُضيف تفصيل تاريخي للمتن (ندوات تسولّيكون 1959–1969) و`## المصادر` (Zollikon Seminars 2001، Boss 1971، Binswanger 1942) — كان الملف بلا مصادر إطلاقاً.
- **dbt-aurobindo-vs-vivekananda.md**: تصحيحات طفيفة — عناوين `related` لـsch-aurobindo وsch-neo-vedanta وthk-vivekananda كانت مبتورة عن العناوين الفعلية (بلا الأقواس التوضيحية) — صُححت. أُضيف `## المصادر` (Vivekananda، *Jnana Yoga* 1899؛ Aurobindo، *The Life Divine* 1914–1919/1939–1940) — كان الملف بلا مصادر.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة بعد التصحيحات — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق — thk-brueckner — لا يمنع نشر الملفات الثلاثة).

## Task 11 — crt-rorty-mirror-of-nature / crt-ryle-category-mistake-ghost-machine / crt-said-orientalism-epistemic-critique (2026-09-01)
- **crt-ryle-category-mistake-ghost-machine.md**: **طلب slug عاجل** — لا ملف مفكر لغيلبرت رايل (Gilbert Ryle، 1900–1976، مؤلف *The Concept of Mind* 1949) في الأطلس. الـslug الوحيد المتاح `thk-ryle` يشير إلى شخص مختلف تماماً هو أنتوني رايل (Anthony Ryle، مبتكر العلاج المعرفي التحليلي CAT) — تحقُّق أُنقذ به الملف من ربط خاطئ فادح. لم يُربط `related` بأي slug له.
- **crt-said-orientalism-epistemic-critique.md**: **طلب slug** — لا ملف مفكر لإرنست رينان ولا سلفستر دي ساسي (مستشرقان فرنسيان، مستهدَفان بالاسم في نقد سعيد) ولا لبرنارد لويس (المستشرق الذي ردّ مباشرة على سعيد في نيويورك ريفيو أوف بوكس 1982). كذلك ملاحظة تكرار: يوجد بالفعل `wrk-orientalism-said` و`wrk-orientalism-edward-said` لنفس كتاب سعيد — ازدواج لم يُحسم هنا (خارج نطاق التاسك)، إحالة لـTask 16.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلبات slug معلقة — thk-gilbert-ryle، thk-renan، thk-sacy، thk-bernard-lewis — لا تمنع نشر الملفات الثلاثة).

## Task 11 — dbt-mao-maoism-vs-deng-ism / dbt-mary-the-super-scientist-qualia / dbt-meaning-found (2026-09-01)
- **dbt-mao-maoism-vs-deng-ism.md**: `related` كان مليئاً بـ19 رابطاً عشوائياً بلا صلة بالمتن إطلاقاً (جدالات عن الإرادة الحرة، RDoC، الوراثة السلوكية...) — حُذفت كلها وأُبقي فقط sch-chinese-marxism وthk-mao-zedong (مبرَّران بالمتن). سُمّي الطرفان بالاسم الحقيقي: زانغ تشونتشياو (Zhang Chunqiao، صاحب "On Exercising All-Round Dictatorship over the Bourgeoisie" 1975) عن عصابة الأربعة، ودنغ شياو بينغ عن خطاب الجلسة الكاملة الثالثة (ديسمبر 1978). أُضيف `## المصادر`. **طلب slug جديد**: thk-deng-xiaoping غير موجود في الأطلس رغم كونه أحد طرفي هذا الجدل بالاسم مباشرة — الموجود فقط thk-deng-yuanhai (شخص مختلف تماماً).
- **dbt-mary-the-super-scientist-qualia.md**: إعادة كتابة كاملة — كان المتن قالبياً بالكامل (3 جمل من القائمة السوداء حرفياً: "لا يوجد اقتباس مباشر موثوق متاح"، "يقدم هذا الموقف رؤية نسقية تستند إلى براهين..."، "يقدم الطرف المقابل قراءة نقدية بديلة..."). حُدد الطرفان الحقيقيان: فرانك جاكسون (Epiphenomenal Qualia، 1982) ضد ديفيد لويس (What Experience Teaches، 1988) ودانيال دينيت (Consciousness Explained، 1991)، مع تسجيل تراجع جاكسون نفسه لاحقاً (Postscript on Qualia، 1998). أُضيف `## المصادر`. `related` بقي بلا روابط أشخاص لأن thk-djackson الموجود شخص مختلف تماماً (دون جاكسون، العلاج الأسري) لا فرانك جاكسون — **طلب slug جديد**: thk-frank-jackson غير موجود.
- **dbt-meaning-found.md**: `related` كان فيه عنوانان لا يطابقان الملفات المستهدفة فعلياً (br-logotherapy وthk-frankl بعناوين مبتورة) وربطان غير مبرَّرين بالمتن (thk-socrates وdbt-evidence) — صُححت العناوين وحُذف غير المبرَّر وأُضيف thk-yalom (مبرَّر بالمتن). حُدد الطرف الثاني بالاسم: إيرفين يالوم (Existential Psychotherapy، 1980، فصل Meaninglessness) بدل "التيار العلماني" المبهم. سُجّل تداخل محتمل مع dbt-langle-frankl / dbt-langle-frankl-meaning في `gaps` — تحقّق: الملفان يغطيان خلافاً مؤسسياً ضيقاً بين لانغله وفرانكل، بينما هذا الملف سؤال فلسفي أعم (فرانكل/يالوم) — لا تداخل فعلي، زاويتان مستقلتان. `level` كانت فارغة و`active_start` كان null رغم أن أول نص موثَّق (فرانكل 1959) معروف — عُبّئا.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلبا slug معلقان — thk-deng-xiaoping، thk-frank-jackson — لا يمنعان نشر الملفات الثلاثة).

## Task 11 — dbt-moral-foundations-pluralism / dbt-moral-realism-vs-moral-relativism / dbt-nature-nurture-behavioral-genetics-vs-constructionism (2026-09-01)
- **dbt-moral-foundations-pluralism.md**: إعادة كتابة كاملة — المتن كان قالبياً عاماً بلا اسم أو سنة فعلية للطرف الثاني (اكتُفي بذكر "العقلانية الكانطية والنفعية" دون تمثيل حقيقي). حُدد الطرفان الفعليان بالبحث: جوناثان هايدت وكريغ جوزيف (Intuitive Ethics، 2004؛ The New Synthesis in Moral Psychology، Science 2007؛ The Righteous Mind، 2012) ضد لورنس كولبرغ (Stage and Sequence، 1969) الذي انتقده هايدت صراحة في The Emotional Dog and Its Rational Tail (2001). استُبدل `related` (thk-kant غير المبرَّر مباشرة بالمتن) بـthk-lkohlberg الموجود فعلاً وموثّق الصلة بالمتن. أُضيف `## المصادر`. **طلب slug**: كريغ جوزيف (Craig Joseph)، شريك هايدت المؤسس لنظرية الأسس الأخلاقية، بلا ملف مفكر في الأطلس — مسجَّل في gaps الملف.
- **dbt-moral-realism-vs-moral-relativism.md**: إعادة كتابة كاملة — المتن كان قالبياً بالكامل (3 جمل من القائمة السوداء حرفياً: "لا يوجد اقتباس مباشر موثوق متاح"، "يقدم هذا الموقف رؤية نسقية تستند إلى براهين..."، "يقدم الطرف المقابل قراءة نقدية بديلة تكشف الثغرات..."). حُدد الطرفان الحقيقيان: غيلبرت هارمان (Moral Relativism Defended، 1975) ضد جوديث جارفيس طومسون — طرفا مناظرة منشورة معاً بعنوان Moral Relativism and Moral Objectivity (Blackwell، 1996) — مع إضافة ج. ل. ماكي (نظرية الخطأ، Ethics: Inventing Right and Wrong، 1977) وديريك بارفيت (On What Matters، 2011) كموقفين موازيين موثقين. أُضيف thk-dparfit إلى `related` (الوحيد الموجود فعلاً كملف مفكر) و`## المصادر`. **طلب slug**: غيلبرت هارمان (Gilbert Harman)، جوديث جارفيس طومسون (Judith Jarvis Thomson)، وج. ل. ماكي (J. L. Mackie) — لا ملفات مفكرين لهم في الأطلس رغم كونهم أطراف الجدل الفعليين بالاسم — مسجَّلون في gaps الملف.
- **dbt-nature-nurture-behavioral-genetics-vs-constructionism.md**: المتن كان بالفعل موثقاً بالاسم والسنة (بلومين، بوشار، غيرغن، فوكو، ميشيل...)، لكن `related` كان مليئاً بروابط غير مبررة بالمتن إطلاقاً (thk-bowlby، thk-erikson، thk-dewey، thk-james، thk-wundt، sch-behaviorism) — حُذفت واستُبدلت بروابط حقيقية موجودة فعلاً في الأطلس ومبررة بالمتن (thk-kgergen، thk-jshotter، thk-foucault، thk-stephen-jay-gould، thk-wmischel). صُحح خطأ هوية في المتن: "فرانك فراي (Frank Galton)" لا وجود له — الاسم الصحيح فرانسيس غالتون (Francis Galton)، وصُححت الفقرة. أُضيف `## المصادر`. **ملاحظة تحذيرية مهمة**: `thk-sbouchard` الموجود في الأطلس هو ستيفان بوشار (Stéphane Bouchard)، باحث كندي معاصر في العلاج بالواقع الافتراضي — **ليس** توماس بوشار (Thomas Bouchard) مؤلف دراسة توائم مينيسوتا المذكور في هذا الملف؛ لم يُربط بينهما تجنباً لخطأ هوية. **طلب slug**: روبرت بلومين (Robert Plomin)، توماس بوشار (Thomas Bouchard)، آوكه تيليغن (Auke Tellegen)، فرانسيس غالتون (Francis Galton) — لا ملفات مفكرين لهم في الأطلس رغم ذكرهم بالاسم في المتن — مسجَّلون في gaps الملف. **ملاحظة عنقود**: هذا الملف جزء من عنقود nature-nurture من 6 ملفات في هذه الدفعة؛ سُجّل التداخل المحتمل مع بقية العنقود في gaps دون دمج، بناءً على تعليمات المهمة.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلبات slug متعددة معلقة — thk-craig-joseph، thk-gilbert-harman، thk-judith-jarvis-thomson، thk-jl-mackie، thk-robert-plomin، thk-thomas-bouchard، thk-auke-tellegen، thk-francis-galton — لا تمنع نشر الملفات الثلاثة).

## دفعة عنقود nature-nurture (debates) — 2026-09-01

- **dbt-nature-nurture.md / dbt-nature-nurture-gene-environment-interaction.md / dbt-nature-nurture-cognitive-modules-vs-domain-general.md**: طلبات slug جديدة لمفكرين مذكورين بالاسم في المتن ولا ملف لهم في الأطلس:
  thk-noam-chomsky (Chomsky) · thk-steven-pinker (Pinker) · thk-leda-cosmides (Cosmides) · thk-john-tooby (Tooby) · thk-jerry-fodor (Fodor، *The Modularity of Mind*، 1983) · thk-david-rumelhart (Rumelhart) · thk-james-mcclelland (McClelland) · thk-elizabeth-spelke (Spelke) · thk-jeffrey-elman (Elman) · thk-annette-karmiloff-smith (Karmiloff-Smith) · thk-david-geary (Geary) · thk-michael-meaney (Meaney) · thk-moshe-szyf (Szyf) · thk-dean-buonomano (Buonomano).
  ملاحظة: thk-caspi وthk-moffitt موجودان فعلاً لكن فقط كمسودتين غير معتمدتين تحت `content/ar/drafts/spark/thinkers/` — لا يصلحان للربط حتى تُعتمدا.
- **status:** لا يمنع نشر الملفات الثلاثة — الروابط غير المبرَّرة إلى مفكرين آخرين حُذفت من `related` بدلاً من ذلك.

## Task 12 — axm-homeostasis / axm-insight-learning / axm-intentionality (2026-09-01)
- **axm-homeostasis.md**: `thk-cannon` الموجود في الأطلس هو **بيتي كانون** (Betty Cannon، معالجة وجودية أمريكية معاصرة) — شخص مختلف تماماً عن **والتر كانون** (Walter Cannon، 1871–1945، صائغ مصطلح Homeostasis في *The Wisdom of the Body*، 1932) صاحب هذه البديهية فعلياً. حُذف الرابط الخاطئ من `related` و`edges`، وأُبقي اسمه في المتن بلا رابط. **طلب slug جديد: `thk-walter-cannon`.**
- **axm-insight-learning.md / axm-intentionality.md**: لا طلبات slug جديدة — صُححت فقط عناوين `related` المتضاربة مع عناوين الملفات الفعلية (`thk-wkohler` = "فولفغانغ كولَر" لا "فولفجانج كولر"؛ `thk-brentano` = "فرانتس برنتانو" لا "فرانز برينتانو"؛ `thk-merleau-ponty` = "موريس مرلو-بونتي" لا "موريس ميرلو-بونتي")، وأُصلحت `edges.target` من نص حر (أسماء عربية ومدارس بلا slug) إلى slugs حقيقية (`sch-phenomenology`، `thk-brentano`، `br-gestalt-berlin`، `thk-wkohler`، `con-homeostasis`).
- أُضيف `## المصادر` (2–5 مراجع حقيقية) للملفات الثلاثة، وحُذفت روابط `related` غير المبرَّرة بالمتن (`axm-tabula-rasa`، `axm-intentionality` من الملفين الأولين — كانا مكررين في كل ملفات axm- بلا تبرير نصي).
- صُححت سنة صياغة Allostasis في `axm-homeostasis.md` من 2011 (غير دقيقة) إلى المرجع الصحيح: ستيرلنغ وآير 1988 (الصياغة الأصلية)، وستيرلنغ 2012 (التوسيع).
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق — `thk-walter-cannon` — لا يمنع نشر الملفات الثلاثة).

## Task 12 — dia-al-kindi-mu-tazila-creation / dia-al-razi-abu-hatim-prophecy / dia-arendt-jaspers-guilt-correspondence (2026-09-01)
- **dia-al-kindi-mu-tazila-creation.md**: أعيدت كتابة الملف — كان يصف "حواراً" عاماً بلا لحظة تقاطع موثَّقة (لا مكان ولا تاريخ ولا مشاركون بالاسم). أُعيد تأطيره حول التقاطع الفعلي الموثَّق: عمل الكندي في بيت الحكمة ببغداد أثناء المحنة المعتزلية (833–847) في بلاط المأمون والمعتصم. **طلب slug جديد**: أحمد بن أبي دؤاد (قاضي القضاة المعتزلي الذي أدار المحنة) والخليفة المأمون — لا ملف مفكر لهما في الأطلس رغم كونهما طرفي هذا التقاطع التاريخي بالاسم.
- **dia-al-razi-abu-hatim-prophecy.md**: أعيدت كتابة الملف بالكامل — كان قالبياً 100% (يحتوي جملة القائمة السوداء "انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية" حرفياً، و`related` بروابط عشوائية لحوارين لا علاقة لهما بالمناظرة — buber-rogers وrawls-habermas). المناظرة موثَّقة فعلياً: أبو بكر الرازي ضد أبي حاتم الرازي، الري، نحو 925–932م، مصدرها كتاب أبي حاتم "أعلام النبوة". **طلب slug جديد**: أبو حاتم أحمد بن حمدان الرازي (الداعي الإسماعيلي، ت. 934) — لا ملف مفكر له في الأطلس رغم كونه أحد طرفي المناظرة مباشرة بالاسم.
- **dia-arendt-jaspers-guilt-correspondence.md**: الملف كان موثقاً في جوهره (مراسلات آرندت-ياسبرز 1926–1969 حقيقية وموثقة) لكن بلا `## المصادر`، و`edges.belongs_to` كان يشاور sch-phenomenology غير الأدق — صُحح إلى sch-existentialism، وأُضيفت المصادر (Kohler & Saner 1992، Die Schuldfrage 1946، Eichmann in Jerusalem 1963)، وأُصلح gaps من صياغة عامة غير محددة إلى فجوة دقيقة (الاعتماد على الترجمة الإنجليزية لا الأصل الألماني).
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلبات slug معلقة — أحمد بن أبي دؤاد، الخليفة المأمون، أبو حاتم الرازي — لا تمنع نشر الملفات الثلاثة).

## Task 12 — dia-buddha-kassapa-asceticism / dia-carl-hovey-freud-interview / dia-chomsky-piaget-1975 (2026-09-01)
- **dia-buddha-kassapa-asceticism.md**: كان الملف موثقاً بالفعل بحدث حقيقي (سوتا Kassapasīhanāda، DN 8) لكن بلا `## المصادر` وبـ`gaps` غامضة — عُمّق المتن بتفاصيل السوتا الفعلية (كاسابا Acela Kassapa من الآجيفيكا، سيلا/سماذي/بانيا، دخوله السانغا وبلوغه الأرهت) وأُضيف قسم مصادر (Walshe 1995، Thanissaro Bhikkhu) و`gaps` محددة.
- **dia-carl-hovey-freud-interview.md**: **مشكلة هوية جوهرية** — الاسم/الـslug الأصلي "Carl Hovey" لا صلة موثقة له بفرويد بحثت عنها ولم أجدها؛ اللقاء الحقيقي الموثق هو مقابلة الصحفي جورج سيلفستر فيريك (George Sylvester Viereck) مع فرويد صيف 1926 في فيينا، المنشورة "Sigmund Freud Confronts the Sphinx" في *Glimpses of the Great* (1930). أُعيدت كتابة المتن بالكامل ليعكس هذا اللقاء الحقيقي بدل الاسم الخاطئ، مع الإبقاء على اسم الملف (slug) كما هو حسب القاعدة (ممنوع إعادة التسمية). حُذفت 3 روابط `related` غير مبررة بالمتن (dia-buber-rogers، dia-rawls-habermas، dia-lacan-heidegger). **طلب slug جديد**: thk-viereck (جورج سيلفستر فيريك) غير موجود في الأطلس.
- **dia-chomsky-piaget-1975.md**: إعادة كتابة كاملة — كان المتن قالبياً بالكامل مع جملتين من القائمة السوداء حرفياً ("انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية"، "لا يوجد اقتباس مباشر موثوق متاح"). المناظرة حقيقية وموثقة جيداً: أكتوبر 1975، دير روايومون، بتحرير ماسيمو بياتيلي-بالمريني، منشورة *Language and Learning* (Harvard UP، 1980). حُذف `related` غير المبرر (dia-buber-rogers، dia-rawls-habermas) واستُبدل بـthk-piaget وthk-nchomsky (مبرَّران بالمتن). أُضيف `## المصادر`. **ملاحظة ازدواج غير محسومة (خارج نطاق التاسك)**: يوجد ملفا مفكر منفصلان لنفس الشخص — thk-noam-chomsky.md وthk-nchomsky.md، كلاهما بعنوان "نعوم تشومسكي" — اخترت thk-nchomsky هنا للاتساق مع dia-foucault-chomsky-debate-1971.md الذي يستخدمه بالفعل؛ الدمج محال لـTask 16.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق — thk-viereck — لا يمنع نشر الملفات الثلاثة).

## Task 12 — dia-lacan-heidegger-1955 / dia-lacan-heidegger-anxiety-seminar / dia-leibniz-clarke-correspondence (2026-09-01)
- **dia-lacan-heidegger-1955.md**: أعيدت كتابة الملف بمصادر بحثية فعلية (رودينسكو، ريتشاردسون، lacanianworks.org) — صُححت التفاصيل: الزيارة كانت لاكان إلى فرايبورغ بصحبة جان بوفريه، ثم زيارة هايدجر المقابلة لضيعة لاكان بغيترانكور (لا "كوخ تودتناوبرغ" كما كان مكتوباً)، بمناسبة مؤتمر سيريزي-لا-سال 27 أغسطس-4 سبتمبر 1955. حُذف `related` غير المبرر (dia-buber-rogers، dia-rawls-habermas). لا طلب slug جديد — جان بوفريه ذُكر بالاسم في المتن لكن لم يُطلب له slug لعدم وضوح أهميته المستقلة كمفكر أطلسي.
- **dia-lacan-heidegger-anxiety-seminar.md**: عُمّق بتواريخ ومكان دقيقين (الجلسة الافتتاحية 14 نوفمبر 1962، مستشفى سانت آن، آخر سيمينار له في ذلك الموقع). صُححت مغالطة تاريخية: كانت تربط السيمينار (1962-1963) زمنياً بنشر سارتر لـ*الوجود والعدم* (1943 فعلياً، ليس نفس السنوات) — أُزيلت المقارنة الخاطئة واستُبدلت بمقارنة دقيقة بمصدر القلق الكيركيغاردي الذي استعاره هايدجر نفسه. حُذف `related` غير مبرر بالمتن (exp-derealization-depersonalization، con-alienation) لم يُذكرا في النص إطلاقاً.
- **تأكيد الازدواج**: الملفان يوثقان مناسبتين مختلفتين فعلياً — لقاء 1955 الشخصي/الترجمة النصية مقابل سيمينار 1962-1963 القرائي — لا تكرار حقيقي.
- **dia-leibniz-clarke-correspondence.md**: إعادة كتابة كاملة — كان الملف يحتوي جملتي القائمة السوداء حرفياً ("انعقد هذا الحوار في لحظة تاريخية وفكرية مفصلية"، "لا يوجد اقتباس مباشر موثوق متاح"). المراسلة موثقة بدقة (10 رسائل، 1715-1716، بوساطة الأميرة كارولين، انتهت بوفاة لايبنتز نوفمبر 1716). **طلب slug جديد: thk-samuel-clarke** (صمويل كلارك) — الطرف المراسِل المباشر للايبنتز طوال المراسلة، لا ملف مفكر له في الأطلس حالياً.
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق — thk-samuel-clarke — لا يمنع نشر الملفات الثلاثة).

## Task 12 — dia-jung-buber-1952 / dia-kahneman-gigerenzer-heuristics / dia-kuhn-popper-scientific-paradigms (2026-09-01)
- **dia-jung-buber-1952.md**: تحذير المهمة بأن الملفين الثاني والثالث "عن لاكان وهايدغر" لا ينطبق على المحتوى الفعلي — الملفات الثلاثة الموزَّعة كانت فعلياً عن يونغ-بوبر، كانمان-غيغرنزر، كون-بوبر؛ لا ذكر للاكان أو هايدغر في أي منها. أُعيدت كتابة الملف حول السجال الفعلي الموثَّق: رد يونغ على بوبر في مجلة Merkur (المجلد السادس، العدد 5، مايو 1952) بعد كتاب يونغ *جواب على أيوب* (1952) ونقد بوبر له في *كسوف الله* (1952). لا يوجد توثيق للقاء وجاهي فعلي بينهما — السجال بالكامل نصي/منشور، سُجِّل هذا في `gaps` بدل التغاضي عنه.
- **dia-kahneman-gigerenzer-heuristics.md**: أُعيد التأطير حول تبادل Psychological Review 1996 (كانمان وتفيرسكي مقابل غيغرنزر، المجلد 103، العدد 3). حُذف رابطا `related` غير المبرَّرين (dia-buber-rogers-dialogue-1957، dia-rawls-habermas-debate-1995 — نسخ-لصق من ملف آخر). **طلب slug جديد**: `thk-gerd-gigerenzer` غير موجود في الأطلس رغم كونه الطرف الثاني المباشر في هذا السجال بالاسم. صُحح عنوان `thk-kahneman` في related من "دانيال كانيمان" إلى "دانيال كانمان" (مطابقة لعنوان الملف الفعلي).
- **dia-kuhn-popper-scientific-paradigms.md**: عُمّق المتن بتفاصيل الحدث الفعلي: ندوة 13 يوليو 1965 ضمن المؤتمر الدولي لفلسفة العلم، كولدج بيدفورد، جامعة لندن (10–15 يوليو 1965)، برئاسة بوبر. صُحح خطأ: فايرابند لم يحضر فعلياً (كان مريضاً)، وحلّ محله جون واتكنز؛ أُضيف مسترمان وتولمين ولاكاتوش كمشاركين فعليين في النقاش. صُححت عناوين `related` المتضاربة (`thk-karl-popper` = "سير كارل بوبر" لا "كارل بوبر"؛ `thk-thomas-kuhn` = "توماس صامويل كوهن" لا "توماس كون").
- **preflight_check.py**: نُفّذ على الملفات الثلاثة — صفر مخالفات آلية.
- **status:** مغلق (طلب slug واحد معلق — `thk-gerd-gigerenzer` — لا يمنع نشر الملفات الثلاثة).

## Task 12 (2026-09-01) — طلب حسم ازدواج
- `que-mind-body-interaction` (QUE-0015) محجور، ازدواج مع `qst-mind-body-interaction-problem` (QUE-0129) الأعمق توثيقاً. القرار المرجّح: `redirect_to: "qst-mind-body-interaction-problem"` نهائياً بعد مراجعة بشرية.

## ✅ 2026-09-02 (الجلسة الثالثة) — حسم كامل لكل طلبات slug المعلَّقة أدناه
كل الأسماء المسجَّلة في الأقسام التالية (Task 16.4، 16.2، 13.13، 13.10، وكل الطلبات المبعثرة عبر تقارير Task 9/11/12) أُنشئت الآن كملفات مفكرين حقيقية في `content/ar/drafts/minimax/thinkers/`: جيمس بريد، جورج زيمل، كورت شنايدر، رودولف لابان، إرمغارد بارتينييف، سيلفيا باين، إيلا شارب، فولفغانغ باولي، غي ديبور، أنتوني بروكنر، فرانك جاكسون، كريغ جوزيف، غيلبرت هارمان، جوديث جارفيس طومسون، ج. ل. ماكي، جورج سيلفستر فيريك، غيرد غيغرنزر، كاتيا ليبراتي، فيديريكو ليس، هاري ترياندس، جون دبليو بيري، الحلاج، دنغ شياو بينغ، إرنست رينان، سلفستر دي ساسي، برنارد لويس، أحمد بن أبي دؤاد، الخليفة المأمون. راجع `agents_specs/reports/minimax/ISSUE-RESOLUTION-2026-09-02.md` للتفاصيل الكاملة.
**استثناء واحد اكتُشف أثناء التنفيذ**: جيلبرت رايل كان موجوداً بالفعل تحت slug `thk-aryle` (لم يُلاحَظ سابقاً) — لم يُنشأ ملف مكرر، وصُححت الفجوة الخاطئة في `crt-ryle-category-mistake-ghost-machine.md` بدلاً من ذلك.

## Task 16.4 (2026-09-02) — طلبات slug جديدة معلَّقة
- **غي ديبور (Guy Debord)** — لا ملف thk- له إطلاقاً (معتمد أو مسودة)، رغم أنه مؤلف wrk-society-of-spectacle-debord الجديد ومؤسس الأممية الموقفية.
- **دونالد هِب (Donald Hebb)** و**أولريك نايسر (Ulric Neisser)** — موجودان كمسودتين في مسار Spark فقط (`content/ar/drafts/spark/thinkers/`)، يحتاجان ترقية رسمية.

## Task 16.2 (2026-09-02) — طلبات slug جديدة معلَّقة (حوارات)
- **سيلفيا باين (Sylvia Payne)** و**إيلا شارب (Ella Sharpe)** — من dia-klein-anna-freud-controversial-discussions الجديد؛ باين ترأست جلسات النقاشات الخلافية 1941-1945 ولا ملف thk- لها.
- **فولفغانغ باولي (Wolfgang Pauli)** — من dia-jung-pauli الجديد؛ فيزيائي مركزي في العلاقة الموثقة (1932-1958)، لا ملف thk- له إطلاقاً في الأطلس.

## Task 13.13 (2026-09-02) — طلبات slug جديدة معلَّقة
- **رودولف لابان (Rudolf Laban)** و**إرمغارد بارتينييف (Irmgard Bartenieff)** — مؤسِّسا `sch-laban-movement-analysis.md` الجديد، لا ملف thk- لأي منهما رغم مركزيتهما.
- **جورج زيمل (Georg Simmel)** و**كورت شنايدر (Kurt Schneider)** — من دفعة 13.12، لا يزالان بلا slug.

## Task 13.10 (2026-09-02) — طلبات slug جديدة معلَّقة
- **جيمس بريد (James Braid)** — لا يوجد ملف `thk-` له رغم مركزيته التأسيسية (صاغ مصطلح hypnotism نفسه، أربعينيات القرن 19). مرتبط بـ`sch-hypnotherapy.md` الجديد عبر gaps فقط، لم يُخترع slug.
- **ريتشارد سوين (Richard Suinn) — قرار عدم إنشاء صحيح**: الموضوع (علم نفس الأداء الرياضي) موثَّق بالفعل كـ`br-sport-psychology.md` (تيار معتمد، BRN-0218) وليس كمدرسة مستقلة. التوصية: أضِف `thk-rsuinn` إلى `related` في `br-sport-psychology.md` (تم تطبيقه، راجع T13/task-13.10.md).

## sch-classical-sociology (2026-09-02) — طلب slug جديد معلَّق
- **جورج زيمل (Georg Simmel)** — لا يوجد ملف `thk-` له إطلاقاً في الأطلس (لا معتمد ولا مسودة) رغم كونه أحد ثلاثة مؤسسين لعلم الاجتماع الكلاسيكي (مع فيبر ودوركهايم)، مذكور بالاسم في متن `content/ar/drafts/minimax/schools/sch-classical-sociology.md`. طلب slug: `thk-simmel`.
- ملاحظة: `thk-durkheim` موجود كمسودة غير معتمدة في مسار Spark (`content/ar/drafts/spark/thinkers/thk-durkheim.md`، id مؤقت `[DRAFT-UNKNOWN]`) — لم يُربط في `related` احترازاً لأنه غير مُرقّى بعد؛ سُجِّل في `gaps` بدل الربط المباشر.

## dia-jung-pauli (2026-09-02) — طلب slug جديد معلَّق
- **فولفغانغ باولي (Wolfgang Pauli)** — لا يوجد ملف `thk-` له في الأطلس رغم كونه الطرف الثاني المباشر في `content/ar/drafts/minimax/dialogues/dia-jung-pauli.md` بالاسم، حائز نوبل 1945، وشخصية مركزية في تاريخ التحليل النفسي اليونغي (تحليله مع يونغ 1932، مصدر مادة *علم النفس والكيمياء*). طلب slug: `thk-wolfgang-pauli`.

## wrk-society-of-spectacle-debord (2026-09-02) — طلب slug جديد معلَّق
- **غي ديبور (Guy Debord)** — لا يوجد ملف `thk-` له في الأطلس (لا معتمد ولا مسودة) رغم كونه مؤلِّف *مجتمع الاستعراض* (1967) ومؤسِّس الأممية الموقفية (1957) بالاسم في `content/ar/drafts/minimax/works/wrk-society-of-spectacle-debord.md`. طلب slug: `thk-debord`.

## sch-map-metapsychoanalysis (2026-09-02) — طلبات slug جديدة معلَّقة
- **كاتيا ليبِراتي (Katia Liberati)** و**فيديريكو لايس (Federico Leiss)** — مؤسِّسا الفرع الإيطالي MAP (Metapsicoanalisi / Analisi del Difeso) من ISTDP، مذكوران بالاسم في `content/ar/drafts/minimax/schools/sch-map-metapsychoanalysis.md`. لا ملف `thk-` لأي منهما في الأطلس (لا معتمد ولا مسودة). طلب slug: `thk-kliberati` و`thk-fleiss` (بعد التحقق من عدم تعارضهما مع أي slug موجود).

## إصلاحات روابط مكسورة خارج نطاق كتابة MiniMax (2026-09-02)
هذه الملفات المرجعية تقع في مجلدات يملكها Spark (`experiences/`, `syndromes/`, `contexts/`, و`thinkers/` النطاق a–l) فلا يمكن لـMiniMax تعديلها مباشرة. الهدف الصحيح موثّق وموجود بالفعل — يحتاج فقط تصحيح سطر `edges.target` (وربما `target_type`) في الملف المصدر:
- `content/ar/experiences/exp-childhood-amnesia.md`: `sch-developmental-psychology` (غير موجود) → **`sch-developmental`** (title: "علم النفس النمائي (Developmental Psychology)"، ملف معتمد).
- `content/ar/contexts/ctx-french-salons-encyclopedie.md`: `sch-european-enlightenment` (غير موجود، target_type مدرسة) → **`sch-enlightenment`** (title: "فلسفة التنوير (كمظلة عامة)"، ملف معتمد؛ ملاحظة: `ctx-european-enlightenment` موجود أيضاً كسياق منفصل بنفس الموضوع تقريباً — إن كان القصد سياقياً لا مدرسياً فالهدف الأصح `ctx-european-enlightenment` مع `target_type: "سياق"`).
- `content/ar/thinkers/thk-leo-tolstoy.md`: `sch-existentialism-theistic` (غير موجود) → **`sch-existentialism-religious`** (title: "الوجودية الدينية/المسيحية (Christian Existentialism)"، ملف معتمد — يغطي الوجودية التوحيدية/المسيحية عموماً وتولستوي يقع ضمنها).
- `content/ar/syndromes/syn-eco-anxiety.md`: `sch-ecological-psychology` (غير موجود سابقاً) → الآن موجود كمسودة جديدة `content/ar/drafts/minimax/schools/sch-ecological-psychology.md` (بانتظار الترقية من كلود؛ بعد الترقية لن يحتاج الرابط تعديلاً).
- `content/ar/studies/stu-wertheimer-gestalt.md`: `sch-gestalt-psychology` (غير موجود سابقاً) → الآن موجود كملف إحالة مسودة `content/ar/drafts/minimax/schools/sch-gestalt-psychology.md` (`redirect_to: sch-gestalt-psychology-berlin`؛ بانتظار الترقية).

## دفعة روابط مكسورة 2026-09-02 — ملفات في مجال Spark (metaphors/works/experiences)، لا يحق لي تعديلها

- `content/ar/metaphors/met-psyche-as-palimpsest.md` يشاور على `sch-historical-psychology` (غير موجود).
  لا مدرسة حقيقية تطابق هذا الموضوع (استعارات تراكب الذاكرة عند دي كوينسي/فرويد/دريدا/فوكو) —
  الأقرب موضوعياً `sch-psychoanalysis` لكن العلاقة غير مباشرة بما يكفي لتبريرها في المتن كما هو.
  **التوصية لـSpark:** إما حذف السطر أو ربطه بمدرسة حقيقية يشرح المتن صلتها صراحة.
- `content/ar/metaphors/met-suhrawardi-light-shadow.md` يشاور على `sch-illuminationism` (غير موجود) بـ
  `belongs_to`. **التوصية لـSpark:** حوّله إلى `sch-ishraqiyya` (title: "الإشراقية") — نفس الموضوع
  بالضبط (شهرورديّ، الإشراقية)، وthk-suhrawardi وthk-al-shahrazuri يستخدمان هذا الslug فعلاً.
- `content/ar/works/wrk-adler-understanding-human-nature.md` يشاور على `sch-individual-psychology`
  (غير موجود) بـ`belongs_to`. **التوصية لـSpark:** حوّله إلى `sch-adlerian` (مسودة MiniMax، title:
  "علم النفس الفردي الأدلري") — هو نفس مفهوم "Individual Psychology" لأدلر بالضبط.
- `content/ar/experiences/exp-out-of-body-experience.md` يشاور على `sch-parapsychology` (غير موجود) بـ
  `relates_to`. **التوصية لـSpark:** حوّله إلى `con-parapsychology` (title: "ما وراء علم النفس والظواهر
  الخارقة")، `target_type: "مفهوم"`.
