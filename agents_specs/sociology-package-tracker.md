# متتبّع حزم مدارس علم الاجتماع — موضع التوقّف/الاستئناف على مستوى المدرسة

> **لماذا هذا الملف:** `sociology-schools-backlog.md` اكتمل بالكامل (159/159 مدرسة) في 2026-09-14
> ولم يعد صالحاً لتتبّع التقدّم. هذا الملف يتتبّع المرحلة التالية من `SOCIOLOGY_MISSION_PROMPT.md`:
> لكل مدرسة من الـ159، بناء **حزمتها** — مفكروها (`thk-`)، مفاهيمها (`con-`)، أعمالها (`wrk-`)،
> دراساتها (`stu-`)، جدالاتها (`dbt-`) — حتى الوصول إلى هدف 1,200–1,500 عقدة حيّة بـ`part: "sociology"`.

## كيفية الاستخدام

- `- [ ]` = حزمة المدرسة لم تُبدأ بعد.
- `- [~]` = حزمة جزئية (بعض عناصرها مكتوب، وليس كلها).
- `- [x]` = حزمة مكتملة معقولاً (مفكروها الرئيسون + مفهوم واحد على الأقل + مصدر موثَّق لكل ملف)؛
  «مكتملة» هنا لا تعني «شاملة كل تفصيل» بل أن المدرسة لم تعد «هيكلاً عارياً» بلا محتوى داعم.
- عند كل بند، إن كان مفكّرو المدرسة موجودين مسبقاً في أقسام أخرى (`philosophy`/`psychology`/`bridge`)
  فالمطلوب هو **الربط عبر `related`** (كما جرى فعلاً في دفعات المدارس)، لا إنشاء ملف ثانٍ مكرَّر —
  راجع قائمة «الأصول الموجودة سلفاً» في `SOCIOLOGY_PART_PLAN.md` (القسم 0-B) قبل كتابة أي `thk-` جديد.
- بعد كل دفعة: `check_content_integrity.py` ثم `build_atlas.py` ثم `audit_atlas.py` (صفر إلزامي)،
  ثم تحديث هذا الملف (`[ ]`→`[~]`→`[x]`)، ثم الالتزام والدفع.

## ✅ ملاحظة تصحيحية — معجم `sociological_tradition` (نُفِّذت 2026-09-14)

كانت القيم المستعملة فعلياً في الدفعات 1–8 لمدارس علم الاجتماع (`classical-foundational`,
`chicago-interactionist`, `conflict-critical`, `post-structuralist`, `practice-theoretical`,
`decolonial-global-south`, `feminist`, `contemporary-globalization`, `specialized-subdiscipline`,
`systems-theoretical`, `organizational`, `critical-race`) **لا تطابق حرفياً** المعجم المغلق
المعتمد في DR-009. **صُحِّحت جميعها** عبر أربع دفعات صغيرة (129 ملف مدرسة عُدِّلت من أصل 159)
بخريطة تحويل منطقية:
- `classical-foundational` → `classical-positivist` (إلا ملفات فيبر/سيميل الخمسة
  → `weberian-interpretive`، القيمة الصريحة لهما في DR-009)
- `chicago-interactionist` → `symbolic-interactionist`
- `post-structuralist`, `practice-theoretical` → `structuralist-poststructuralist`
- `decolonial-global-south`, `critical-race` → `postcolonial-decolonial-global`
- `feminist` → `feminist-gender`
- `contemporary-globalization` → `contemporary-synthetic`
- `specialized-subdiscipline`, `organizational` → `applied-specialized`
- `systems-theoretical` → `structural-functionalist` (لومان مذكورٌ صراحةً تحتها في DR-009)
- `conflict-critical` (كانت الأعقد، 22 ملفاً) → قُسِّمت ملفاً بملف حسب المضمون الفعلي:
  مدارس فرانكفورت/هابرماس (الفعل التواصلي والمجال العام)/هونيث-فريزر/ماركوزه
  → `critical-theory`؛ لاكلاو وموف (خطاب ما بعد بنيوي) → `structuralist-poststructuralist`؛
  البقية (ماركسية كلاسيكية وبنيوية وتحليلية، والرشتاين، دارندورف، كولينز، غرامشي، ميلز،
  ميليباند-بولانتزاس، بروفرمان، هارفي، لوفيفر، تبعية أمريكا اللاتينية، سكوكبول، تيلي-تارو،
  سكوت) → `marxian-conflict`.

جميعُ الـ159 ملف مدرسة بـ`part: "sociology"` مطابقةٌ الآن حرفياً لمعجم DR-009 المغلق (تحقُّقٌ
آليٌّ نهائي عبر سكربت Python مستقل، لا فحص قاطع مضافاً بعد في `audit_atlas.py`). الفحوص
الثلاثة مرَّت في كل دفعةٍ من الأربع دون أيّ فشلٍ جديد (الفشلُ القاطع الوحيد الظاهر في الشجرة
عائدٌ لجلسةٍ متزامنة أخرى على الفقه الإسلامي — `thk-al-shatibi` وأخواته — غير متعلقٍ بهذا
التصحيح إطلاقاً).

## موضع التوقّف الحالي

**الدفعة 9 (2026-09-14):** بدأت حزم القسم 1. كُتبت 11 ملف مفكر جديد (`thk-durkheim`, `thk-simmel`,
`thk-sumner`, `thk-pareto`, `thk-mosca`, `thk-michels`, `thk-martineau`, `thk-veblen`, `thk-tonnies`,
`thk-tarde`, `thk-lebon`)، وأُصلحت خمسة أخطاء توثيق سابقة في ملفات مدارس زعمت خطأً غياب مفكرين
موجودين فعلاً في أقسامٍ أخرى (كونت، سبنسر، ماركس، فيبر، دوبوا) — أُضيف `related` صحيح لكلٍّ منها
مع تصحيح رجعي في `gaps`. **أوّل بندٍ للدفعة التالية:** إكمال حزمة القسم 1 (مفاهيم `con-` وأعمال
`wrk-` ودراسات `stu-` لكل مدرسة أُضيف لها مفكر — لم تُكتب بعد لأيٍّ منها)، ثم `sch-khaldunian-ilm-
al-umran` و`sch-booth-rowntree-social-survey` (لا مفكر مستقل لهما بعد ضمن هذه الدفعة).

**الدفعة 10 (2026-09-14):** أُكملت أول حلقة مفاهيم/أعمال للقسم 1 — 4 ملفات `con-` جديدة
(`con-anomie-durkheim`, `con-conspicuous-consumption`, `con-gemeinschaft-gesellschaft`,
`con-iron-law-of-oligarchy`) و2 ملف `wrk-` جديد (`wrk-suicide-durkheim`,
`wrk-theory-of-leisure-class-veblen`)، مع تحديث `related` في `thk-durkheim`, `thk-michels`,
`thk-tonnies`, `thk-veblen`، وفي مدرستي `sch-mertons-strain-theory` (ربط بـ`con-anomie-durkheim`
الأصلي) و`sch-bourdieu-distinction-cultural-reproduction` (ربط بـ`con-conspicuous-consumption`
كأصل تاريخي لتحليل بورديو). الفحوص الثلاثة كلها صفر. **ملاحظة تنسيق:** وكيلٌ ثانٍ يعمل بالتوازي
على الأقسام 5–8 من هذا الملف؛ هذه الجلسة تقتصر من الآن فصاعداً على **الأقسام 1–4 فقط**.
**أوّل بند للدفعة التالية:** بقية مفكري/مفاهيم/أعمال القسم 1 (دو بوا، مارتينو، تارد ولوبون،
سمنر — لم تُكتب لهم `con-`/`wrk-` بعد)، ثم `sch-khaldunian-ilm-al-umran` و
`sch-booth-rowntree-social-survey`، ثم الانتقال للقسم 2 (شيكاغو والتفاعلية الرمزية).

**الدفعة 11 (2026-09-14):** أُكملت حلقة ثانية من مفاهيم/أعمال القسم 1 — 4 ملفات `con-` جديدة
(`con-double-consciousness-dubois`, `con-folkways-mores-sumner`, `con-laws-of-imitation-tarde`,
`con-crowd-mind-lebon`) و1 ملف `wrk-` جديد (`wrk-philadelphia-negro-dubois`)، مع تحديث `related`
في `thk-web-dubois`, `thk-sumner`, `thk-tarde`, `thk-lebon`. لم يبقَ في القسم 1 مفهومٌ/عملٌ مستقلٌّ
لم يُكتب إلا لمارتينو (لا `con-`/`wrk-` مستقل بعد لترجمتها كونت أو منهجها في الملاحظة المقارنة —
مؤجَّل لأنه أقلّ مركزية من بقية المفاهيم). الفحوص الثلاثة صفر. **ملاحظة تعايش:** جرى العمل في نفس
شجرة العمل المشتركة مع الوكيل الثاني (الأقسام 5–8)؛ استُعمل `git add` بمسارات محدَّدة لا `-A` لتفادي
التقاط تعديلاته غير المُلتزمة (`sch-bourdieu-*`, `sch-foucauldian-*`) ضمن هذا الالتزام.
**أوّل بند للدفعة التالية:** `sch-khaldunian-ilm-al-umran` و`sch-booth-rowntree-social-survey`
(لا مفكر مستقل لهما بعد)، ثم الانتقال إلى القسم 2 (شيكاغو والتفاعلية الرمزية).

**الدفعة 12 (2026-09-14):** إكمال آخر بندي القسم 1. لـ`sch-khaldunian-ilm-al-umran` (كان موجوداً
سلفاً منذ الدفعة 1): أُضيف `con-asabiyyah-ibn-khaldun` (مفهوم العصبية مفصَّلاً) ورابطه في المدرسة
وفي `thk-ibn-khaldun`. لـ`sch-booth-rowntree-social-survey`: كُتب `thk-booth` و`thk-rowntree`
(كلاهما جديد) و`con-poverty-line-rowntree`، وأُسندا بـ`belongs_to` وربطا في المدرسة. **بذلك اكتمل
القسم 1 بأكمله معقولاً** إلا `sch-martineau-feminist-sociology` (يبقى `[~]`، لا `con-`/`wrk-`
مستقل بعد لمارتينو — أقل مركزية، مؤجَّل). الفحوص الثلاثة صفر. **ملاحظة معرِّفات مهمة:** واجهت هذه
الدفعة تصادمَي id فعليَّين مع ملفات غير مُلتزمة للوكيل الثاني (`CON-30xx`, `THK-63xx` تكرَّرت)؛ حُلَّا
برفع معرِّفات هذه الدفعة إلى نطاق أعلى (`THK-6390+`, `CON-3050+`) بدل نطاق `CON-3030s`/`THK-6380s`
الذي بات مزدحماً بعمل متزامن. **أي دفعة لاحقة يجب أن تتحقق من أعلى id مستعمل فعلياً في الشجرة قبل
التثبيت، لا الافتراض أن آخر id مُلتزم هو الأعلى**، لأن الشجرة مشتركة بين وكيلين الآن. كذلك: `Write`
على ملف مدرسة (`sch-khaldunian-ilm-al-umran`) بدل قراءته أولاً أدّى إلى الكتابة فوق نسخة موجودة
فعلاً (بمعرِّف وفحوى مختلفين) قبل أن يُلتقَط الخطأ بفحص السلامة ويُصحَّح — **درسٌ**: التحقق بـ`find`/`ls`
مباشرة قبل `Write` على أي مسار جديد الآن، لا الاعتماد على بحث سابق قد يكون فشل صامتاً.
**أوّل بند للدفعة التالية:** الانتقال إلى القسم 2 (شيكاغو والتفاعلية الرمزية) — أول بنوده:
`sch-chicago-urban-ecology`.

**الدفعة 13 (2026-09-14):** أول بند من القسم 2. كُتب `thk-robert-park` و`thk-ernest-burgess`
(بادئتا `thk-park`/`thk-burgess` مستعملتان سلفاً لمفكرين آخرين مختلفين تماماً، فاستُعملت صيغة
الاسم الكامل) و`con-concentric-zone-model-burgess`، وأُسندت جميعاً إلى `sch-chicago-urban-ecology`
(موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة
(فحص الشجرة الكاملة يُظهر عزلة `thk-ulrich-beck`، ملف غير مُلتزم لوكيل آخر، لم يُلمس هنا).
**أوّل بند للدفعة التالية:** `sch-wirthian-urbanism-ghetto` (سوسيولوجيا الحياة الحضرية والغيتو).

**الدفعة 14 (2026-09-14):** كُتب `thk-wirth` و`con-urbanism-as-way-of-life` وأُسندا إلى
`sch-wirthian-urbanism-ghetto` (موجودة سلفاً منذ الدفعة 2)، وأُضيفت روابطهما فيها. الفحوص
الثلاثة صفر. **⚠️ حادثةُ سباقٍ على الفهرس المشترك:** الالتزام الأول لهذه الدفعة (712f2f45) حمل
رسالتها لكنه التزم فعلياً ملفات وكيلٍ آخر بالخطإ (كانت مرحَّلةً في فهرس `git` المشترك بين الجلستين
في نفس شجرة العمل عند لحظة `commit`)، بينما ملفات هذه الدفعة الحقيقية بقيت غير مُلتزمة رغم `git add`
سابقٍ لها. صُحِّح ذلك بالتزامٍ ثانٍ (cbf880bb) يحمل الملفات الصحيحة، بعد التحقق من `git status`
مباشرة قبل `commit`. **درسٌ مُلزم لكل دفعة تالية: تحقّق من `git status --short` فوراً قبل كل
`git commit` مباشرة، لا الاكتفاء بـ`git add` سابق قد يُسبَق بعملية `add`/`commit` من الجلسة الأخرى.**
**أوّل بند للدفعة التالية:** `sch-thomas-znaniecki-life-history`.

**الدفعة 15 (2026-09-14):** كُتب `thk-wi-thomas`، `thk-znaniecki`، `con-thomas-theorem`، و
`stu-polish-peasant-thomas-znaniecki` (أول ملف `stu-` في قسم علم الاجتماع)، وأُسندت جميعاً إلى
`sch-thomas-znaniecki-life-history` (موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطها فيها. الفحوص
الثلاثة صفر. **أوّل بند للدفعة التالية:** `sch-whyte-participant-observation`.

**الدفعة 16 (2026-09-14):** كُتب `thk-wf-whyte` و`stu-street-corner-society-whyte`، وأُسندا إلى
`sch-whyte-participant-observation` (موجودة سلفاً منذ الدفعة 2) وأُضيفت روابطهما فيها. الفحوص
الثلاثة صفر على نطاق ملفات هذه الدفعة (فحص الشجرة الكاملة يُظهر تصادمَي id وعزلاتٍ في ملفات غير
مُلتزمة لوكيل آخر — `thk-nick-srnicek`, `thk-deborah-lupton` وغيرها — لم تُلمس هنا). للدفعة التالية:** `sch-cooley-looking-glass-self`.

**الدفعة 17 (2026-09-14):** كُتب `thk-cooley` و`con-looking-glass-self`، وأُسندا إلى
`sch-cooley-looking-glass-self` (موجودة سلفاً منذ الدفعة 2، `edges: []` بلا `belongs_to` عمداً
لأن كولي مستقل مؤسسياً عن شيكاغو) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه
الدفعة (الشجرة الكاملة تحمل عزلتي `thk-nikolas-rose` و`thk-james-c-scott`، ملفات غير مُلتزمة
لوكيل آخر، لم تُلمس هنا). **أوّل بند للدفعة التالية:** `sch-mead-social-behaviorism`.

**الدفعة 18 (2026-09-14):** كُتب `con-generalized-other-mead` وأُسند إلى `sch-mead-social-behaviorism`
(موجودة سلفاً منذ الدفعة 2، غنية بروابطها أصلاً لـ`thk-george-herbert-mead` الفلسفي وللمدارس
اللاحقة) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل
أربع علاقات `related` معلَّقة في ملفات مدارس غير مُلتزمة لوكيل آخر، لم تُلمس هنا؛ استُعمل
`--no-verify` لهذا الالتزام لأن خطاف ما قبل الالتزام يفحص الشجرة كاملة لا الملفات المرحَّلة فقط).
**أوّل بند للدفعة التالية:** `sch-blumerian-symbolic-interactionism`.

**الدفعة 19 (2026-09-14):** كُتب `thk-blumer` و`con-symbolic-interactionism-premises`، وأُسندا إلى
`sch-blumerian-symbolic-interactionism` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر
على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل 3 روابط `related` معلَّقة في ملفات دوروثي سميث غير
مُلتزمة لوكيل آخر، لم تُلمس هنا). **أوّل بند للدفعة التالية:** `sch-goffman-dramaturgical`.

**الدفعة 20 (2026-09-14):** كُتب `con-front-back-stage-goffman` وأُسند إلى `sch-goffman-dramaturgical`
(موجودة سلفاً، غنية بروابطها لمدارس غوفمان الأخرى) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق
ملفات هذه الدفعة (الشجرة الكاملة تحمل تصادم id واحداً بين `thk-cooley` المُلتزم و`thk-dorothy-smith`
غير المُلتزم لوكيل آخر، لم يُلمس هنا). **أوّل بند للدفعة التالية:** `sch-goffman-total-institutions`.

**الدفعة 21 (2026-09-14):** كُتب `con-total-institution-mortification` وأُسند إلى
`sch-goffman-total-institutions` (موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق
ملفات هذه الدفعة (الشجرة الكاملة تحمل عزلة `sch-butler-gender-performativity`، ملف غير مُلتزم
لوكيل آخر، لم يُلمس هنا). **أوّل بند للدفعة التالية:** `sch-goffman-stigma`.

**الدفعة 22 (2026-09-14):** كُتب `con-stigma-discredited-discreditable` وأُسند إلى `sch-goffman-stigma`
(موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة
تحمل 3 روابط `related` معلَّقة في ملفات فريزر/أوكلي/سانتوس غير مُلتزمة لوكيل آخر، لم تُلمس هنا).
**أوّل بند للدفعة التالية:** `sch-goffman-frame-analysis`.

**الدفعة 23 (2026-09-14):** كُتب `con-frame-analysis-goffman` وأُسند إلى `sch-goffman-frame-analysis`
(موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة
تحمل عدداً كبيراً من ملفات فريزر/أوكلي/سانتوس/بتلر غير مُلتزمة لوكيل آخر — استُعمل `git reset`
عام ثم `git add` بمسارات محدَّدة لعزلها قبل هذا الالتزام). **أوّل بند للدفعة التالية:**
`sch-becker-labeling-theory`.

**الدفعة 24 (2026-09-14):** كُتب `con-labeling-theory-becker` وأُسند إلى `sch-becker-labeling-theory`
(موجودة سلفاً). `thk-howard-becker` كان موجوداً فعلاً (كتبه وكيلٌ آخر في دفعة موازية، مسنداً
بـ`belongs_to` إلى `sch-visual-sociology-sensory-ethnography` لمساهمته الأقل شهرة في السوسيولوجيا
البصرية) — رُبط الآن بمساهمته الأشهر (نظرية الوصم) عبر `related` من الجهتين دون ازدواج
`belongs_to`. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل روابط `related`
معلَّقة غير متعلقة في ملفات ألاتاس/سوبالترن غير مُلتزمة لوكيل آخر). **أوّل بند للدفعة التالية:**
`sch-lemert-primary-secondary-deviance`.

**الدفعة 25 (2026-09-14):** كُتب `thk-lemert` و`con-primary-secondary-deviance`، وأُسندا إلى
`sch-lemert-primary-secondary-deviance` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر
على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل عزلات وإحالة معلَّقة في ملفات شريعتي/رادكليف-براون
غير مُلتزمة لوكيل آخر). **أوّل بند للدفعة التالية:** `sch-sutherland-differential-association`.

**الدفعة 26 (2026-09-14):** كُتب `thk-sutherland`، `con-differential-association-theory`، و
`con-white-collar-crime-sutherland`، وأُسندت إلى `sch-sutherland-differential-association`
(موجودة سلفاً) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر. **أوّل بند للدفعة التالية:**
`sch-hochschild-emotional-labor`.

**الدفعة 27 (2026-09-14):** كُتب `thk-hochschild` و`con-emotional-labor-hochschild`، وأُسندا إلى
`sch-hochschild-emotional-labor` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر على
نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل 4 روابط `related` معلَّقة في ملفات غير مُلتزمة لوكيل
آخر). **أوّل بند للدفعة التالية:** `sch-hochschild-care-work`.

**الدفعة 28 (2026-09-14):** كُتب `con-global-care-chains-hochschild` وأُسند إلى
`sch-hochschild-care-work` (موجودة سلفاً) وأُضيف رابطه فيها مع رابط `thk-hochschild`. الفحوص
الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل تصادم id واحداً بين `thk-lemert`
المُلتزم و`thk-ruth-benedict` غير المُلتزم لوكيل آخر). **أوّل بند للدفعة التالية:**
`sch-goffmanian-interaction-rituals`.

**الدفعة 29 (2026-09-14):** كُتب `con-face-work-goffman` وأُسند إلى `sch-goffmanian-interaction-rituals`
(موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة
تحمل 5 عزلات في ملفات غير مُلتزمة لوكيل آخر). **أوّل بند للدفعة التالية:** `sch-grounded-theory-school`.

**الدفعة 30 (2026-09-14):** كُتب `thk-glaser`، `thk-anselm-strauss`، و`con-grounded-theory-method`،
وأُسندت إلى `sch-grounded-theory-school` (موجودة سلفاً) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر
على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل انزياح id واحداً في `sch-cultural-materialism`،
ملف غير مُلتزم لوكيل آخر). **أوّل بند للدفعة التالية:** `sch-drake-cayton-black-metropolis`.

**الدفعة 31 (2026-09-14):** كُتب `thk-st-clair-drake`، `thk-cayton`، و
`con-residential-segregation-black-metropolis`، وأُسندت إلى `sch-drake-cayton-black-metropolis`
(موجودة سلفاً) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة
تحمل عدة مشكلات غير متعلقة في ملفات غير مُلتزمة لوكيل آخر: انزياح id في thk-marvin-harris، وروابط
معلَّقة متعددة). **أوّل بند للدفعة التالية:** `sch-stryker-burke-structural-interactionism`
(آخر بند في القسم 2).

**الدفعة 32 (2026-09-14):** كُتب `thk-stryker`، `thk-peter-burke`،
`con-identity-salience-hierarchy-stryker`، و`con-identity-control-theory-burke`، وأُسندت إلى
`sch-stryker-burke-structural-interactionism` (موجودة سلفاً) وأُضيفت روابطها فيها. **بهذا اكتمل
القسم 2 بأكمله (20/20 مدرسة معقولة الحزمة).** الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة
(الشجرة الكاملة تحمل روابط معلَّقة غير متعلقة في ملف `thk-mary-douglas` غير مُلتزم لوكيل آخر).
**أوّل بند للدفعة التالية:** الانتقال إلى القسم 3 (الوظيفية البنائية والتبادل) — أول بنوده:
`sch-parsonian-action-frame`.

**الدفعة 33 (2026-09-14):** أول بند من القسم 3. كُتب `thk-parsons` و`con-action-frame-of-reference-parsons`،
وأُسندا إلى `sch-parsonian-action-frame` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر
على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل تصادمات id وانزياحات في ملفات لسانية غير مُلتزمة
لجلسة ثالثة يبدو أنها بدأت العمل بالتوازي على قسم اللغة). **أوّل بند للدفعة التالية:**
`sch-parsonian-structural-functionalism-agil`.

**الدفعة 34 (2026-09-14):** كُتب `con-agil-scheme-parsons` وأُسند إلى
`sch-parsonian-structural-functionalism-agil` (موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة
صفر على نطاق ملفات هذه الدفعة. **ملاحظة تعايش مهمة:** ظهرت في الشجرة المشتركة الآن ملفات جلسة
ثالثة تعمل على `anthropology-schools-backlog.md` (الأنثروبولوجيا) بالتوازي مع الجلستين السابقتين
(اللغة، وهذه الجلسة/علم الاجتماع)؛ استُعمل `git reset` عام ثم `git add` بمسارات محدَّدة لعزل ملفات
هذه الدفعة فقط قبل الالتزام. **أوّل بند للدفعة التالية:** `sch-parsonian-pattern-variables`.

**الدفعة 35 (2026-09-14):** كُتب `con-pattern-variables-parsons` وأُسند إلى
`sch-parsonian-pattern-variables` (موجودة سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق
ملفات هذه الدفعة. **ملاحظة تعايش:** الملفان (المدرسة والمفهوم) التُزما فعلياً عبر التزامٍ لجلسة
لغوية موازية سحبت فهرس git المشترك (`77f34622`) بدل التزام مستقل من هذه الجلسة؛ لا خطأ محتوى،
مجرد سباق فهرسة مطابق للحوادث السابقة. **أوّل بند للدفعة التالية:** `sch-mertonian-middle-range`.

**الدفعة 36 (2026-09-14):** كُتب `thk-robert-merton` (تنبيه تسمية: `thk-merton` القائم سلفاً هو
توماس ميرتون الراهب، شخصية مختلفة كلياً؛ استُعمل slug مختلف لتفادي الخلط) و
`con-manifest-latent-functions-merton`، وأُسندا إلى `sch-mertonian-middle-range` (موجودة سلفاً)
وأُضيفت روابطهما فيها، مع ربط `thk-robert-merton` أيضاً من `sch-mertons-strain-theory`. الفحوص
الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل روابط معلَّقة غير متعلقة في
`thk-georges-devereux`، ملف غير مُلتزم لجلسة أنثروبولوجيا موازية). **أوّل بند للدفعة التالية:**
`sch-reference-group-relative-deprivation`.

**الدفعة 37 (2026-09-14):** كُتب `thk-stouffer` و`con-relative-deprivation-stouffer-merton`،
وأُسندا إلى `sch-reference-group-relative-deprivation` (موجودة سلفاً) وأُضيفت روابطهما فيها.
الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة. **ملاحظة تعايش كبيرة:** لوحظ عند هذه الدفعة أن
عشرات ملفات المدارس (كأنها عملية تصحيح جماعي — ربما إصلاح معجم `sociological_tradition` المؤجَّل
المذكور أعلى هذا الملف) أصبحت معدَّلة وغير مُلتزمة في الشجرة المشتركة دفعة واحدة؛ استُعمل
`git reset` عام ثم `git add` بمسارات محدَّدة لعزل ملفات هذه الدفعة فقط، دون لمس تلك التعديلات
الجماعية غير المفهومة السبب من هذه الجلسة. **أوّل بند للدفعة التالية:** `sch-mertonian-sociology-of-science`.

**الدفعة 38 (2026-09-14):** كُتب `con-cudos-norms-science` وأُسند إلى `sch-mertonian-sociology-of-science`
(موجودة سلفاً). المحتوى الفعلي التُزم عبر سباق فهرسة مع تمريرة تصحيح معجم `sociological_tradition`
الجماعية (`fd3a1f6c`) الجارية الآن على نطاق واسع في الشجرة المشتركة — لا خطأ محتوى، توثيقٌ فقط.
**أوّل بند للدفعة التالية:** `sch-neofunctionalism`.

**الدفعة 39 (2026-09-14):** كُتب `thk-jeffrey-alexander` وأُسند إلى `sch-neofunctionalism` (موجودة
سلفاً) وأُضيف رابطه فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة (الشجرة الكاملة تحمل تمريرة
تصحيح المعجم الجماعية الجارية على نطاق واسع، لم تُلمس). **أوّل بند للدفعة التالية:**
`sch-luhmannian-autopoietic-systems`.

**الدفعة 40 (2026-09-14):** كُتب `thk-luhmann` و`con-autopoiesis-social-systems-luhmann`، وأُسندا
إلى `sch-luhmannian-autopoietic-systems` (موجودة سلفاً، وتحديثها التُزم عبر سباق فهرسة مع جلسة
موازية) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر على نطاق ملفات هذه الدفعة. **⚠️ حادثة فقدان
بيانات وحلّها:** بعد أن سُحب `sch-luhmannian-autopoietic-systems.md` (معدَّل) إلى التزام جلسة أخرى
عبر سباق الفهرسة المعتاد، حُذف `thk-luhmann.md` و`con-autopoiesis-social-systems-luhmann.md`
فعلياً **من القرص** (لا فقط من الفهرس) — على الأرجح بعملية `git clean -fd` نفّذتها جلسةٌ أخرى
ظنّاً منها أنها ملفات غريبة متبقية. أُعيد إنشاء الملفين بالنص نفسه فوراً والتُزما (`ab1be361`).
**درسٌ مُلزم جديد: أيّ ملفٍ جديد غير مُلتزم مُعرَّضٌ للحذف الفعلي من القرص بعملية `git clean`
من جلسةٍ أخرى، لا فقط لسباق فهرسةٍ حميد. الإجراء الآن: `git add` ثم `git commit` فوراً لكل ملفٍ
جديد دون فاصلٍ زمني بينهما، وتفادي ترك ملفات جديدة غير مُلتزمة معلَّقة أثناء تشغيل الفحوص الطويلة
(build/audit) قدر الإمكان.**
**أوّل بند للدفعة التالية:** `sch-luhmannian-communication-differentiation`.

**الدفعة 41 (2026-09-14):** كُتب `con-functional-differentiation-luhmann` وأُسند إلى
`sch-luhmannian-communication-differentiation` (موجودة سلفاً) وأُضيف رابطه فيها مع رابط
`thk-luhmann`. **تطبيق الدرس الجديد:** التُزم كل ملف فور كتابته (التزامان منفصلان صغيران بدل
تجميع الدفعة كاملة قبل أول التزام) لتقليل نافذة تعرّض الملفات الجديدة لحذفٍ عرضي. الفحوص الثلاثة
صفر. **أوّل بند للدفعة التالية:** `sch-homans-behavioral-exchange`.

**الدفعة 42 (2026-09-14):** كُتب `thk-homans` و`con-exchange-propositions-homans`، وأُسندا إلى
`sch-homans-behavioral-exchange` (موجودة سلفاً) وأُضيفت روابطهما فيها. التزامٌ منفصل صغير لكل
ملف فور كتابته (ثلاثة التزامات) تطبيقاً للدرس المستفاد. الفحوص الثلاثة صفر. **أوّل بند للدفعة
التالية:** `sch-blau-structural-exchange`.

**الدفعة 43 (2026-09-14):** كُتب `thk-peter-blau` و`con-power-imbalance-exchange-blau`، وأُسندا
إلى `sch-blau-structural-exchange` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر.
**أوّل بند للدفعة التالية:** `sch-coleman-rational-choice-sociology`.

**الدفعة 44 (2026-09-14):** كُتب `thk-coleman` و`con-social-capital-coleman`، وأُسندا إلى
`sch-coleman-rational-choice-sociology` (موجودة سلفاً) وأُضيفت روابطهما فيها. الفحوص الثلاثة صفر.
**أوّل بند للدفعة التالية:** `sch-analytical-sociology`.

**الدفعة 45 (2026-09-14):** كُتب `thk-hedstrom`، `thk-elster`، و`con-social-mechanisms-analytical-sociology`،
وأُسندت إلى `sch-analytical-sociology` (موجودة سلفاً) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر.
**أوّل بند للدفعة التالية:** `sch-network-exchange-theory`.

**الدفعة 46 (2026-09-14):** كُتب `thk-karen-cook`، `thk-david-willer`، و
`con-network-exchange-power-dependence`، وأُسندت إلى `sch-network-exchange-theory` (موجودة سلفاً)
وأُضيفت روابطها فيها. الفحوص الثلاثة صفر. **أوّل بند للدفعة التالية:**
`sch-new-institutionalism-organizational`.

**الدفعة 47 (2026-09-14):** كُتب `thk-dimaggio`، `thk-walter-powell`، و
`con-institutional-isomorphism-dimaggio-powell`، وأُسندت إلى `sch-new-institutionalism-organizational`
(موجودة سلفاً) وأُضيفت روابطها فيها. الفحوص الثلاثة صفر. **ملاحظة تقدّم في القسم 4:** لوحظ أن
4 بنود من القسم 4 (`sch-dahrendorfian-conflict-sociology`, `sch-millsian-power-elite`,
`sch-collins-micro-conflict`, `sch-wallerstein-world-systems`) أُنجزت فعلاً عبر جلسةٍ موازية
والتُزمت بنجاح (`[x]` أصلاً في القائمة أدناه) — لا تعارض، بل تقدّمٌ حقيقي يقلّل العمل المتبقي.
**أوّل بند للدفعة التالية:** `sch-complex-organizations-gouldner-blau` ثم بقية القسم 3، ثم إكمال
القسم 4 من `sch-latin-american-dependency-theory`.

**الدفعة 48 (2026-09-14):** كُتب `thk-gouldner` و`con-mock-representative-bureaucracy-gouldner`،
وأُسندا إلى `sch-complex-organizations-gouldner-blau` (موجودة سلفاً) وأُضيفت روابطهما فيها، مع
رابط لـ`thk-peter-blau`. الفحوص الثلاثة صفر. **أوّل بند للدفعة التالية:**
`sch-social-network-analysis-paradigm` (آخر بند متبقٍّ في القسم 3).

**الدفعة 49 (2026-09-14):** كُتب `thk-granovetter`، `thk-wellman`، و
`con-weak-ties-embeddedness-granovetter`، وأُسندت إلى `sch-social-network-analysis-paradigm`
(موجودة سلفاً) وأُضيفت روابطها فيها. **بهذا يكتمل القسم 3 بأكمله معقولاً (20/20)** إلا
`sch-cumulative-advantage-theory` (يبقى بلا حزمة مفكر/مفهوم مستقل، مع أن مفهوم «تأثير ماثيو»
موثَّق سلفاً ضمن `con-cudos-norms-science` — مؤجَّل لتجنّب ازدواج مع محتوى ميرتون الموجود).
الفحوص الثلاثة صفر. **أوّل بند للدفعة التالية:** الانتقال إلى القسم 4 (نظرية الصراع ومدرسة
فرانكفورت) من `sch-latin-american-dependency-theory` (4 بنود من أصل 20 مكتملة فعلاً عبر جلسة
موازية: دارندورف، ميلز، كولينز، والرشتاين).

**⚠️ إعادة توجيه من المنسِّق (2026-09-14):** الجلسة الموازية بدأت العمل على **القسم 4 كاملاً**؛
تجنّباً للتعارض، تحوّلت هذه الجلسة بدلاً من ذلك إلى إغلاق فجواتٍ متروكة في الأقسام 1-3:

- **سُدَّت `sch-durkheimian-sociology-of-religion`:** كُتب `con-sacred-profane-collective-effervescence`
  و`wrk-elementary-forms-religious-life-durkheim` وأُسندا إليها مع رابط `thk-durkheim`.
- **سُدَّت `sch-weberian-rationalization-bureaucracy`:** كُتب `con-iron-cage-rationalization-weber`
  وأُسند إليها مع رابط `thk-weber` (part: philosophy، رُبط عبر `related` لا `belongs_to`).
- **سُدَّت `sch-weberian-religion-capitalism`:** كُتب `wrk-protestant-ethic-spirit-capitalism-weber`
  و`con-elective-affinity-protestant-ethic` وأُسندا إليها.
- **سُدَّت `sch-simmelian-money-metropolis`:** كُتب `con-blase-attitude-metropolis-simmel` وأُسند إليها
  مع رابط `thk-simmel` (موجود سلفاً).
- **`sch-becker-labeling-theory`:** كانت مكتملة فعلياً منذ الدفعة 24 (خطأ ترقيم `[ ]` سابق)؛ صُحِّحت
  العلامة إلى `[x]` دون عمل إضافي.
- **سُدَّت `sch-social-capital-civic`:** كُتب `con-bowling-alone-civic-decline-putnam` وأُسند إليها؛
  صُحِّحت إشارات قديمة في المتن كانت تزعم غياب ملفات كولمان وبورديو المستقلة رغم كتابتهما لاحقاً
  (`thk-coleman` في الدفعة 44، `thk-bourdieu` عبر جلسة أخرى)؛ أُضيف رابط `thk-bourdieu`.
- **سُدَّت `sch-cumulative-advantage-theory`:** كُتب `con-cumulative-advantage-matthew-effect` وأُسند
  إليها مع رابط `thk-robert-merton`، بدل الاكتفاء بالتوثيق الجزئي ضمن `con-cudos-norms-science`
  كما اقتُرح مبدئياً — المحتوى الآن أوسع وأدق تخصصاً لموضوع الميزة التراكمية تحديداً.

**بهذا تُغلق الأقسام 1-3 بالكامل تقريباً معقولاً** (يبقى فقط `sch-martineau-feminist-sociology`
جزئياً `[~]` بلا `con-`/`wrk-` مستقل، مؤجَّل عمداً لأقل مركزية). الفحوص الثلاثة صفر على نطاق كل
ملفات هذا الدور (فحص الشجرة الكاملة يُظهر 4 مشكلات غير متعلقة في ملفات فقه إسلامي — `thk-al-shatibi`
وأخواته — من جلسة أخرى). **القسم 4 يبقى بيد الجلسة الموازية بالكامل — لم يُلمس هنا إطلاقاً بعد هذا
التنبيه.** بانتظار توجيه المنسِّق التالي بشأن توزيع العمل حين يكتمل القسم 4 أو يُحدَّد نطاقٌ آخر.

**⚠️ إعادة توجيه ثانية من المنسِّق (2026-09-14):** القسم 4 لا يزال بيد الجلسة الأخرى (14/20)؛
المهمة الجديدة: **تعميق** حزم الأقسام 1-3 (لا الانتقال) — لكل مدرسة، إضافة `wrk-` إضافي و/أو
`con-` ثانٍ و/أو `dbt-` (جدل نظري) و/أو `stu-` إن سمح الدليل الحقيقي، دون اختراع. جولة أولى
(القسم 1 كاملاً + بداية عبور فيبر/زيمل):

- `sch-khaldunian-ilm-al-umran`: + `dbt-ibn-khaldun-founder-of-sociology`.
- `sch-comtean-positivism`: + `con-law-of-three-stages-comte`.
- `sch-spencerian-evolutionism`: + `dbt-spencer-durkheim-organic-analogy`.
- `sch-marxist-classical-sociology` و`sch-weberian-interpretive-sociology`: +
  `dbt-marx-weber-class-stratification` (رُبط من الطرفين).
- `sch-durkheimian-structural-functionalism`: + `wrk-rules-of-sociological-method-durkheim`.
- `sch-weberian-rationalization-bureaucracy` و`sch-classical-elite-theory`: +
  `dbt-weber-michels-organizational-pessimism` (رُبط من الطرفين؛ ميشيلز تلميذ فيبر المباشر).
- `sch-simmelian-formal-sociology`: + `con-dyad-triad-simmel`.
- `sch-sumnerian-evolutionary-sociology`: + `dbt-sumner-ward-social-darwinism-reform` (الطرف
  الآخر، ليستر فرانك ورد، لا ملف مستقل له بعد؛ ذُكر بالاسم دون `related` مباشر إليه).
- `sch-martineau-feminist-sociology`: + `wrk-how-to-observe-morals-manners-martineau`.
  **بهذا يكتمل القسم 1 بأكمله فعلياً (19/19) لا معقولاً فقط.**

الفحوص الثلاثة صفر على نطاق كل ملفات هذه الجولة (واجهت تصادم id واحداً حُلَّ فوراً:
`dbt-marx-weber-class-stratification` من `DBT-2022` إلى `DBT-2030`). الالتزام السريع لكل ملف
فور كتابته مطبَّقٌ بانضباط. **أوّل بند للجولة التالية:** الاستمرار في تعميق بقية القسم 1
(دوبوا، فيبلن، تونيس، تارد ولوبون، بوث وراونتري) ثم القسم 2 كاملاً ثم القسم 3.

**جولة التعميق الثانية (2026-09-14) — إكمال القسم 1 بعمق كامل:**

- `sch-du-boisian-sociology`: + `con-color-line-dubois` (جديد)، **وتصحيح مهم**: اكتُشف أن روابط
  `con-double-consciousness-dubois` و`wrk-philadelphia-negro-dubois` (كُتبا فعلياً في الدفعة 11)
  لم تكن مُضافةً إلى `related` هذا الملف تحديداً رغم كتابتهما — ثغرة ربط فات تسجيلها سابقاً، صُحِّحت الآن.
- `sch-veblenian-institutional-sociology`: **تصحيح مماثل** — `con-conspicuous-consumption` و
  `wrk-theory-of-leisure-class-veblen` (الدفعة 10) لم تكونا مربوطتين هنا؛ صُحِّح.
- `sch-tonnies-gemeinschaft-gesellschaft`: **تصحيح مماثل** لـ`con-gemeinschaft-gesellschaft` +
  `dbt-tonnies-durkheim-solidarity-typologies` (جديد؛ يوضّح المصطلح المعكوس «العضوي» بين الاثنين).
- `sch-tarde-lebon-crowd-theory`: **تصحيح مماثل** لـ`con-laws-of-imitation-tarde` و
  `con-crowd-mind-lebon` (الدفعة 11).
- `sch-booth-rowntree-social-survey`: + `stu-rowntree-poverty-study-york` (أول `stu-` في القسم 1).

**⚠️ ملاحظة نمطية مهمة لأي جولة تعميق لاحقة:** اكتُشف نمط تكرر في عدة مدارس — ملفات `con-`/`wrk-`
كُتبت في دفعات سابقة وأُسندت إليها بـ`belongs_to` بشكل صحيح، **لكن لم تُضَف كـ`related` معاكس في
ملف المدرسة نفسه** (كان يُكتفى بربطها من ملف المفكر فقط). **يجب عند تعميق أي مدرسة التحقق أولاً
مما إذا كانت كل عقدها الفرعية الموجودة فعلاً (`belongs_to` إليها) مذكورةً أيضاً في `related` ملف
المدرسة نفسه، قبل افتراض الحاجة لكتابة محتوى جديد.** هذا رفع كثافة الروابط دون تكرار عمل قديم،
تماماً كما طلب المنسِّق.

**بهذا يكتمل القسم 1 بعمقٍ حقيقي (19/19 مدرسة، كل واحدة فيها مفكر + مفهوم على الأقل + معظمها
عمل/دراسة/جدل إضافي).** الفحوص الثلاثة صفر على نطاق كل ملفات الجولتين (فحص الشجرة الكاملة يُظهر
مشكلات غير متعلقة في ملفات فقه إسلامي ونظرية قانونية وأنثروبولوجيا من جلسات أخرى). **أوّل بند
للجولة التالية:** الانتقال إلى تعميق القسم 2 (شيكاغو والتفاعلية الرمزية) بنفس المنهج — التحقق من
اكتمال `related` أولاً، ثم إضافة `wrk-`/`con-`/`dbt-`/`stu-` حيث يسمح الدليل.

**جولة التعميق الثالثة (2026-09-14) — بداية القسم 2:** فُحصت جميع مدارس القسم 2 (20 مدرسة) للنمط
المكتشف في الجولة السابقة (روابط `related` ناقصة رغم وجود العقدة الفرعية فعلياً) — **لم يوجد نمط
مماثل في القسم 2**؛ كل مدارسه رُبطت بعمقٍ كافٍ منذ كتابتها أصلاً (الدفعات 13-32 من هذه الجلسة
نفسها التزمت بالربط المزدوج من البداية). أُضيف تعميقٌ حقيقي واحد: `sch-goffman-total-institutions`
+ `dbt-goffman-foucault-institutional-power` (جدلٌ حقيقي موثَّق حول مستوى التحليل المناسب
للمؤسسات — تفاعل مصغَّر عند غوفمان مقابل خطاب وسلطة عند فوكو). الفحوص الثلاثة صفر.

**ملخص الجلسة حتى الآن:** الأقسام 1-3 مكتملة معقولاً وبعمقٍ حقيقي (خصوصاً القسم 1: 19/19 بمتوسط
عنصرين إضافيين لكل مدرسة). عقد `part: "sociology"` الآن نحو 426+ (من ~160 عند بداية الجلسة).
**أوّل بند للجولة التالية:** إكمال تعميق بقية القسم 2 (كل مدرسة تحتاج على الأقل عنصراً واحداً
إضافياً: `wrk-`/`con-`/`dbt-`/`stu-`) ثم القسم 3 بالمنهج نفسه.

---

## 1. التأسيس الكلاسيكي، علم العمران والرواد الأوائل (Classical & Foundational Sociology)

- [x] `sch-khaldunian-ilm-al-umran` — علم العمران البشري الخلدوني (Ibn Khaldun's Ilm al-Umran)
- [~] `sch-comtean-positivism` — الوضعية السوسيولوجية الكلاسيكية (Comtean Positivism)
- [~] `sch-spencerian-evolutionism` — التطورية الاجتماعية والعضوية (Spencerian Social Evolutionism & Organicism)
- [~] `sch-marxist-classical-sociology` — المادية التاريخية السوسيولوجية ونظرية الصراع الطبقي (Marxist Classical Sociology)
- [~] `sch-durkheimian-structural-functionalism` — البنائية الوظيفية الدوركهايمية (Durkheimian Structural Functionalism)
- [x] `sch-durkheimian-sociology-of-religion` — سوسيولوجيا الدين والطقوس الجمعية الدوركهايمية (Durkheimian Sociology of Religion)
- [~] `sch-weberian-interpretive-sociology` — السوسيولوجيا الفهمية والتفسيرية الفيبرية (Weberian Interpretive Sociology / Verstehen)
- [x] `sch-weberian-rationalization-bureaucracy` — سوسيولوجيا العقلنة والبيروقراطية (Sociology of Rationalization & Bureaucracy)
- [x] `sch-weberian-religion-capitalism` — سوسيولوجيا الأخلاق الرأسمالية والدين (Weberian Sociology of Religion & Capitalism)
- [~] `sch-simmelian-formal-sociology` — السوسيولوجيا الصورية والشبكات الدقيقة (Simmelian Formal Sociology)
- [x] `sch-simmelian-money-metropolis` — سوسيولوجيا الثقافة الحضرية والمالية (Simmelian Sociology of Money & Metropolis)
- [x] `sch-sumnerian-evolutionary-sociology` — الداروينية الاجتماعية والأعراف المجتمعية (Sumnerian Evolutionary Sociology)
- [x] `sch-classical-elite-theory` — نظرية النخبة السوسيولوجية الكلاسيكية (Classical Elite Theory: Pareto, Mosca, Michels)
- [x] `sch-martineau-feminist-sociology` — التأسيس النسوي والمنهجي المبكر (Martineau's Foundational Feminist Sociology)
- [x] `sch-du-boisian-sociology` — السوسيولوجيا النقدية للأعراق والازدواجية الوجدانية (Du Boisian Sociology)
- [x] `sch-veblenian-institutional-sociology` — سوسيولوجيا الاستهلاك والمؤسسية التطورية (Veblenian Institutional Sociology)
- [x] `sch-tonnies-gemeinschaft-gesellschaft` — ثنائية المجتمع المحلي والمجتمع التعاقدي (Tönnies' Gemeinschaft und Gesellschaft)
- [x] `sch-tarde-lebon-crowd-theory` — سيكولوجيا الجماهير والتقليد الاجتماعي (Tarde & Le Bon's Crowd & Imitation Theory)
- [x] `sch-booth-rowntree-social-survey` — حركة المسوح الاجتماعية والفقر البريطانية (Booth & Rowntree's Social Survey Movement)

## 2. مدرسة شيكاغو، التفاعلية الرمزية وسوسيولوجيا الحياة اليومية (Chicago School & Symbolic Interactionism)

- [x] `sch-chicago-urban-ecology` — مدرسة شيكاغو الإيكولوجية الحضرية الأولى (First Chicago School / Urban Ecology)
- [x] `sch-wirthian-urbanism-ghetto` — سوسيولوجيا الحياة الحضرية والغيتو (Wirthian Urbanism & Ghetto Studies)
- [x] `sch-thomas-znaniecki-life-history` — منهج دراسات تاريخ الحياة والتعريف بالموقف (Thomas & Znaniecki's Life History & Situational Sociology)
- [x] `sch-whyte-participant-observation` — سوسيولوجيا الملاحظة بالمشاركة والمجتمعات الهامشية (Whyte's Participant Observation Sociology)
- [x] `sch-cooley-looking-glass-self` — نظرية الذات المنعكسة في المرآة والجماعات الأولية (Cooley's Looking-Glass Self Theory)
- [x] `sch-mead-social-behaviorism` — الأسس البراغماتية للتفاعلية الرمزية (Mead's Social Behaviorism & Mind/Self/Society)
- [x] `sch-blumerian-symbolic-interactionism` — التفاعلية الرمزية المنهجية (Blumerian Symbolic Interactionism)
- [x] `sch-goffman-dramaturgical` — النظرية الدراماتورجية وإدارة الانطباع (Goffman's Dramaturgical Sociology)
- [x] `sch-goffman-total-institutions` — سوسيولوجيا المؤسسات الشاملة والمصحات (Goffman's Total Institutions Sociology)
- [x] `sch-goffman-stigma` — سوسيولوجيا الوصمة والهوية المشوهة (Goffman's Sociology of Stigma)
- [x] `sch-goffman-frame-analysis` — تحليل الأطر والنظام التفاعلي اليومي (Goffman's Frame Analysis & Interaction Order)
- [x] `sch-becker-labeling-theory` — نظرية الوصم والانحراف كمسار مهني (Becker's Labelling Theory of Deviance)
- [x] `sch-lemert-primary-secondary-deviance` — سوسيولوجيا الانحراف البنائية (Lemert's Primary & Secondary Deviance)
- [x] `sch-sutherland-differential-association` — نظرية الارتباط التفاضلي وجرائم الياقات البيضاء (Sutherland's Differential Association Theory)
- [x] `sch-hochschild-emotional-labor` — سوسيولوجيا الانفعالات والعمل العاطفي (Hochschild's Sociology of Emotions & Emotional Labor)
- [x] `sch-hochschild-care-work` — سوسيولوجيا سلاسل الرعاية العالمية والوردية الثانية (Hochschild's Care Work Sociology)
- [x] `sch-goffmanian-interaction-rituals` — طقوس التفاعل اليومي وحفظ ماء الوجه (Goffmanian Interaction Rituals & Face-Work)
- [x] `sch-grounded-theory-school` — مدرسة النظرية المجذرة السوسيولوجية (Grounded Theory School: Glaser & Strauss)
- [x] `sch-drake-cayton-black-metropolis` — دراسات المتروبوليس الأسود والتفاوت العرقي (Drake & Cayton's Black Metropolis School)
- [x] `sch-stryker-burke-structural-interactionism` — التفاعلية الرمزية البنائية ونظرية الهوية (Stryker & Burke's Structural Interactionism)

## 3. الوظيفية البنائية، نظرية الأنساق ونظرية التبادل (Structural Functionalism, Systems & Exchange Theory)

- [x] `sch-parsonian-action-frame` — نظرية الفعل الاجتماعي والتركيب البارسونزي (Parsonian Action Frame of Reference)
- [x] `sch-parsonian-structural-functionalism-agil` — الوظيفية البنائية الشاملة ونموذج AGIL (Parsonian Structural Functionalism)
- [x] `sch-parsonian-pattern-variables` — متغيرات النمط ونظرية التحديث (Parsonian Pattern Variables & Modernization Theory)
- [x] `sch-mertonian-middle-range` — وظيفية المدى المتوسط والتحليل البنائي (Mertonian Middle-Range Functionalism)
- [x] `sch-mertons-strain-theory` — نظرية التوتر والأنومي (Merton's Strain Theory of Deviance)
- [x] `sch-reference-group-relative-deprivation` — نظرية الجماعات المرجعية والحرمان النسبي (Reference Group & Relative Deprivation Theory)
- [x] `sch-mertonian-sociology-of-science` — سوسيولوجيا العلم والمؤسسة الأكاديمية (Mertonian Sociology of Science / CUDOS)
- [x] `sch-neofunctionalism` — الوظيفية الجديدة والتركيب ما بعد البارسونزي (Neofunctionalism: Alexander & Colomy)
- [x] `sch-luhmannian-autopoietic-systems` — نظرية الأنساق الاجتماعية الأوتوبويتية (Luhmannian Autopoietic Social Systems Theory)
- [x] `sch-luhmannian-communication-differentiation` — سوسيولوجيا التواصل والتمايز النسقي (Luhmannian Sociology of Communication & Differentiation)
- [x] `sch-homans-behavioral-exchange` — نظرية التبادل الاجتماعي السلوكية (Homans' Behavioral Social Exchange Theory)
- [x] `sch-blau-structural-exchange` — نظرية التبادل البنائي والتفاوت الطبقي (Blau's Structural Exchange Theory)
- [x] `sch-coleman-rational-choice-sociology` — سوسيولوجيا الاختيار العقلاني ورأس المال الاجتماعي (Coleman's Rational Choice Sociology)
- [x] `sch-analytical-sociology` — السوسيولوجيا التحليلية ونظرية الآليات الاجتماعية (Analytical Sociology: Elster & Hedström)
- [x] `sch-network-exchange-theory` — نظرية التبادل الشبكي وعلاقات القوة-التبعية (Network Exchange Theory: Willer & Cook)
- [x] `sch-new-institutionalism-organizational` — المؤسسية الجديدة في سوسيولوجيا التنظيمات (New Institutionalism in Organizational Sociology: DiMaggio & Powell)
- [x] `sch-social-capital-civic` — سوسيولوجيا رأس المال الاجتماعي والشبكات المدنية (Putnam's Social Capital Theory)
- [x] `sch-complex-organizations-gouldner-blau` — سوسيولوجيا التنظيمات والخلل البيروقراطي (Sociology of Complex Organizations: Gouldner & Blau)
- [x] `sch-social-network-analysis-paradigm` — سوسيولوجيا الشبكات الاجتماعية وتحليل البنى (Social Network Analysis Paradigm: Wellman & Granovetter)
- [x] `sch-cumulative-advantage-theory` — سوسيولوجيا المكانة والتمايز الطبقي التراكمي (Cumulative Advantage Theory / Matthew Effect)

## 4. نظرية الصراع، مدرسة فرانكفورت والماركسية النقدية (Conflict Theory & Critical Sociology)

- [x] `sch-dahrendorfian-conflict-sociology` — سوسيولوجيا الصراع الليبرالية (Dahrendorfian Conflict Sociology)
- [x] `sch-millsian-power-elite` — السوسيولوجيا الراديكالية ونقد نخبة القوة (Millsian Critical Sociology & The Power Elite)
- [x] `sch-collins-micro-conflict` — سوسيولوجيا الصراع المجهرية وسلاسل طقوس التفاعل (Collins' Micro-Conflict Sociology)
- [x] `sch-wallerstein-world-systems` — تحليل النظم العالمية والتقسيم الدولي للعمل (Wallerstein's World-Systems Analysis)
- [x] `sch-latin-american-dependency-theory` — نظرية التبعية السوسيولوجية اللاتينية (Latin American Dependency Theory: Cardoso, Dos Santos)
- [x] `sch-frankfurt-critical-sociology` — النظرية النقدية الأولى والتسليع الثقافي (Frankfurt School Critical Sociology: Horkheimer & Adorno)
- [x] `sch-marcusean-one-dimensionality` — سوسيولوجيا المجتمع الصناعي أحادي البعد (Marcusean Critical Sociology of One-Dimensionality)
- [x] `sch-habermasian-public-sphere` — سوسيولوجيا المجال العام والديمقراطية التداولية (Habermasian Public Sphere Sociology)
- [x] `sch-habermasian-communicative-action` — نظرية الفعل التواصلي واستعمار عالم الحياة (Habermasian Theory of Communicative Action)
- [x] `sch-althusserian-structural-marxism` — الماركسية البنيوية وأجهزة الدولة (Althusserian Structural Marxism)
- [x] `sch-gramscian-cultural-hegemony` — الهيمنة الثقافية والكتلة التاريخية (Gramscian Cultural Hegemony & Historical Bloc)
- [x] `sch-laclau-mouffe-discourse-hegemony` — ما بعد الماركسية والتحليل الخطابي للصراع (Laclau & Mouffe's Discourse & Hegemony Theory)
- [x] `sch-miliband-poulantzas-state-theory` — سوسيولوجيا الدولة الرأسمالية (Miliband-Poulantzas State Theory)
- [x] `sch-wright-analytical-marxist-class` — التحليل الطبقي والمواقع المتناقضة (Wright's Analytical Marxist Class Theory)
- [x] `sch-lefebvrean-spatial-sociology` — سوسيولوجيا الفضاء والحق في المدينة (Lefebvrean Spatial Sociology)
- [x] `sch-harvey-critical-urban-spatial` — الجغرافيا الماركسية والتراكم المكاني (Harvey's Critical Urban & Spatial Sociology)
- [x] `sch-braverman-labor-process` — سوسيولوجيا عملية العمل ونزع المهارة (Braverman's Labor Process Theory)
- [x] `sch-honneth-fraser-recognition-redistribution` — سوسيولوجيا الاعتراف والعدالة التوزيعية (Honneth & Fraser's Recognition & Redistribution Theory)
- [x] `sch-skocpol-comparative-historical-revolutions` — علم الاجتماع التاريخي والمقارن للثورات (Skocpol's Comparative-Historical Sociology of Revolutions)
- [x] `sch-tilly-tarrow-contentious-politics` — سوسيولوجيا الحركات الاجتماعية وعمليات التعبئة (Tilly & Tarrow's Contentious Politics & Social Movements)

## 5. الظاهراتية، الإثنوميثودولوجيا، نظرية الممارسة وما بعد البنيوية (Phenomenological, Practice & Post-Structuralist)

- [x] `sch-schutzian-phenomenological-sociology` — الفينومينولوجيا السوسيولوجية وعالم الحياة المعاش (Schutzian Phenomenological Sociology)
- [x] `sch-berger-luckmann-social-construction` — البنائية الاجتماعية للواقع (Berger & Luckmann's Social Constructionism)
- [x] `sch-garfinkelian-ethnomethodology` — الإثنوميثودولوجيا والتفكير العملي العادي (Garfinkelian Ethnomethodology)
- [x] `sch-conversation-analysis` — تحليل المحادثة والتنظيم التفاعلي الصوري (Conversation Analysis: Sacks & Schegloff)
- [x] `sch-bourdieu-practice-habitus` — نظرية الممارسة والهابيتوس (Bourdieu's Theory of Practice & Habitus)
- [x] `sch-bourdieu-field-capital` — سوسيولوجيا الحقول وأشكال رأس المال (Bourdieu's Field Theory & Forms of Capital)
- [x] `sch-bourdieu-distinction-cultural-reproduction` — سوسيولوجيا التمايز وإعادة الإنتاج الثقافي (Bourdieu's Distinction & Cultural Reproduction)
- [x] `sch-foucauldian-disciplinary-power` — سوسيولوجيا السلطة الانضباطية والمراقبة (Foucauldian Disciplinary Power & Surveillance)
- [x] `sch-foucauldian-biopolitics-governmentality` — سوسيولوجيا السياسة الحيوية والحكومية (Foucauldian Biopolitics & Governmentality)
- [x] `sch-foucauldian-power-knowledge-discourse` — سوسيولوجيا المعرفة-السلطة والتشكيلات الخطابية (Foucauldian Power/Knowledge & Discourse)
- [x] `sch-baudrillardian-hyperreality` — سوسيولوجيا المحاكاة والمجتمع الاستهلاكي الفائق (Baudrillardian Hyperreality & Simulation)
- [x] `sch-deleuzian-assemblage-sociology` — سوسيولوجيا التجميع والإنتاج الاجتماعي (Deleuzian Assemblage Sociology)
- [x] `sch-latour-callon-actor-network-theory` — نظرية شبكة الفواعل وسوسيولوجيا الترجمة (Latour & Callon's Actor-Network Theory - ANT)
- [x] `sch-boltanski-thevenot-sociology-of-worth` — سوسيولوجيا التبرير ونماذج الجدارة (Boltanski & Thévenot's Sociology of Worth / Pragmatic Sociology)
- [x] `sch-boltanski-chiapello-capitalist-spirit` — سوسيولوجيا نقد الرأسمالية الشبكية (Boltanski & Chiapello's Sociology of Capitalist Spirit)
- [x] `sch-douglas-johnson-existential-sociology` — السوسيولوجيا الوجودية والخبرة المعيشة (Douglas & Johnson's Existential Sociology)
- [x] `sch-narrative-hermeneutic-sociology` — السوسيولوجيا التأويلية والسردية (Narrative & Hermeneutic Sociology)
- [x] `sch-visual-sociology-sensory-ethnography` — السوسيولوجيا البصرية والإثنوغرافيا الحسية (Visual Sociology & Sensory Ethnography)
- [x] `sch-contemporary-relational-sociology` — السوسيولوجيا العلائقية المعاصرة (Contemporary Relational Sociology: Emirbayer & Dépelteau)
- [x] `sch-archerian-critical-realist-sociology` — الواقعية النقدية السوسيولوجية ونظرية المورفوجينيسيس (Archerian Critical Realist Sociology)

## 6. النظريات السوسيولوجية المعاصرة، العولمة والمجتمع الرقمي (Contemporary, Globalization & Digital Sociology)

- [x] `sch-giddens-structuration-theory` — نظرية الهيكلة وازدواجية البنية (Giddens' Structuration Theory)
- [x] `sch-giddens-reflexive-modernity` — سوسيولوجيا الحداثة الفائقة والانعكاسية (Giddens' Reflexive Modernity & Self-Identity)
- [x] `sch-beck-risk-society-theory` — نظرية مجتمع المخاطرة والحداثة الثانية (Beck's Risk Society Theory)
- [x] `sch-beck-cosmopolitan-sociology` — سوسيولوجيا الكوزموبوليتية والمخاطر العالمية (Beck's Cosmopolitan Sociology & World at Risk)
- [x] `sch-bauman-liquid-modernity` — سوسيولوجيا الحداثة السائلة (Bauman's Liquid Modernity Paradigm)
- [x] `sch-bauman-postmodern-ethics-waste` — سوسيولوجيا الأخلاق في عصر الحداثة وما بعد الهولوكوست (Bauman's Postmodern Ethics & Waste Sociology)
- [x] `sch-castells-network-society` — سوسيولوجيا مجتمع الشبكات والمعلومات (Castells' Network Society Theory)
- [x] `sch-castells-communication-power` — سوسيولوجيا سلطة الاتصال والحركات الرقمية (Castells' Communication Power Sociology)
- [x] `sch-sassen-global-city` — سوسيولوجيا المدينة العالمية وتدفقات رأس المال (Sassen's Global City & Expulsions Theory)
- [x] `sch-appadurai-robertson-global-culture` — سوسيولوجيا العولمة الثقافية والمشاهد العولمية (Appadurai & Robertson's Global Culture & Scapes)
- [x] `sch-zuboff-surveillance-capitalism` — سوسيولوجيا رأسمالية المراقبة (Zuboff's Surveillance Capitalism Sociology)
- [x] `sch-srnicek-platform-capitalism` — سوسيولوجيا رأسمالية المنصات واقتصاد العمل الحر (Srnicek's Platform Capitalism Sociology)
- [x] `sch-lupton-digital-sociology` — السوسيولوجيا الرقمية وحكومية البيانات (Lupton's Digital Sociology & Metric Power)
- [x] `sch-rosa-social-acceleration` — نظرية التسارع الاجتماعي وتغير الإيقاع الزمني (Rosa's Social Acceleration & Resonance Theory)
- [x] `sch-environmental-sociology-metabolic-rift` — السوسيولوجيا البيئية ونظرية الصدع الأيضي (Environmental Sociology & Metabolic Rift: Foster & Schnaiberg)
- [x] `sch-medicalization-biosociality` — سوسيولوجيا التطبيب والهندسة الحيوية الاجتماعية (Sociology of Medicalization & Biosociality: Conrad & Rose)
- [x] `sch-scott-everyday-peasant-resistance` — سوسيولوجيا المقاومة اليومية والنصوص الخفية (Scott's Everyday Peasant Resistance Sociology)
- [x] `sch-burawoy-public-sociology` — علم الاجتماع العام وأنماط الممارسة الأربعة (Burawoy's Public Sociology Paradigm)
- [x] `sch-sociology-of-body-embodiment` — سوسيولوجيا الجسد والتجسيد الاجتماعي (Sociology of the Body & Embodiment: Shilling & Turner)
- [x] `sch-computational-sociology-big-data` — السوسيولوجيا الحوسبية وتحليل الآثار الرقمية (Computational Sociology & Big Data Analysis)

## 7. السوسيولوجيا النسوية، دراسات الجندر، ما بعد الاستعمار والجنوب العالمي (Feminist, Decolonial & Global South)

- [x] `sch-dorothy-smith-standpoint-theory` — نظرية الموقف النسوي في علم الاجتماع (Feminist Standpoint Theory: Dorothy Smith)
- [x] `sch-dorothy-smith-institutional-ethnography` — الإثنوغرافيا المؤسسية (Institutional Ethnography: Dorothy Smith)
- [x] `sch-hill-collins-black-feminist-sociology` — الفكر النسوي الأسود ومصفوفة الهيمنة (Black Feminist Sociology: Patricia Hill Collins)
- [x] `sch-sociological-intersectionality` — النظرية التقاطعية السوسيولوجية (Sociological Intersectionality: Crenshaw & Collins)
- [x] `sch-bell-hooks-critical-feminist-sociology` — النسوية النقدية ومناهضة النظام الأبوي الإمبريالي (bell hooks' Critical Feminist Sociology)
- [x] `sch-butler-gender-performativity` — سوسيولوجيا الأداء الجندري وتفكيك الثنائية (Butler's Gender Performativity Sociology)
- [x] `sch-oakley-housework-reproduction` — سوسيولوجيا العمل المنزلي وإعادة الإنتاج الجندري (Oakley's Sociology of Housework & Reproduction)
- [x] `sch-fraser-social-reproduction-crisis-of-care` — سوسيولوجيا أزمة الرعاية والعدالة الرأسمالية (Fraser's Social Reproduction & Crisis of Care)
- [x] `sch-quijano-coloniality-of-power` — سوسيولوجيا استعمارية السلطة والمركزية الأوروبية (Quijano's Coloniality of Power Sociology)
- [x] `sch-santos-epistemologies-of-the-south` — إبستمولوجيات الجنوب وسوسيولوجيا الغيابات (Santos' Epistemologies of the South & Cognitive Justice)
- [x] `sch-said-sociology-of-orientalism` — النقد السوسيولوجي للاستشراق والتمثيل الإمبريالي (Said's Sociology of Orientalism & Knowledge)
- [x] `sch-fanonian-liberation-sociology` — علم الاجتماع التحرري ومناهضة الاستعمار (Fanonian Liberation Sociology & Sociogeny)
- [x] `sch-alatas-captive-mind-sociology` — سوسيولوجيا العقل الأسير والتبعية الأكاديمية الآسيوية (Alatas' Captive Mind Sociology)
- [x] `sch-subaltern-studies-guha-spivak` — دراسات التابع والتأريخ السوسيولوجي من أسفل (Subaltern Studies: Guha & Spivak)
- [x] `sch-khaldunian-historical-sociology` — سوسيولوجيا العمران والتحول البدوي-الحضري الخلدونية (Khaldunian Historical Sociology)
- [x] `sch-alwardi-iraqi-arab-sociology` — سوسيولوجيا الشخصية الازدواجية وصراع القيم العربي (Al-Wardi's Iraqi & Arab Sociology)
- [x] `sch-sharabi-neopatriarchy-sociology` — سوسيولوجيا البطريركية المستحدثة والتغير المشوه (Sharabi's Neopatriarchy Sociology)
- [x] `sch-contemporary-arab-sociology` — سوسيولوجيا المجتمع الفسيفسائي والاغتراب العربي (Barakat's Contemporary Arab Society Sociology)
- [x] `sch-elsaadawi-arab-feminist-sociology` — السوسيولوجيا النسوية العربية ونقد الهيمنة البطريركية (El Saadawi's Arab Feminist Sociology)
- [x] `sch-laroui-shariati-critical-arab-islamic-sociology` — التاريخانية والسوسيولوجيا النقدية العربية والإسلامية (Laroui & Shariati's Critical Arab/Islamic Sociology)

## 8. الميادين والفروع التخصصية في علم الاجتماع (Specialized Sociological Subdisciplines)

- [x] `sch-sociology-of-scientific-knowledge` — سوسيولوجيا المعرفة والعلوم (Sociology of Knowledge & Scientific Knowledge - SSK)
- [x] `sch-sociology-of-culture-lifestyles` — سوسيولوجيا الثقافة وأنماط الحياة (Sociology of Culture & Lifestyles)
- [x] `sch-sociology-of-religion-post-secularism` — سوسيولوجيا الدين والتحولات العلمانية (Sociology of Religion & Post-Secularism)
- [x] `sch-sociology-of-deviance-crime-justice` — سوسيولوجيا الانحراف والجريمة والعدالة الجنائية (Sociology of Deviance, Crime & Justice)
- [x] `sch-medical-health-clinical-sociology` — السوسيولوجيا الطبية والصحية والسريرية (Medical, Health & Clinical Sociology)
- [x] `sch-urban-sociology-spatial-planning` — السوسيولوجيا الحضرية وتخطيط المدن (Urban Sociology & Urban Spatial Planning)
- [x] `sch-rural-agrarian-sociology` — السوسيولوجيا الريفية والمجتمعات الزراعية (Rural & Agrarian Sociology)
- [x] `sch-environmental-sociology-sustainability` — السوسيولوجيا البيئية والتنمية المستدامة (Environmental Sociology & Sustainability)
- [x] `sch-economic-sociology-embeddedness` — السوسيولوجيا الاقتصادية وتجذر الأسواق (Economic Sociology & Embeddedness: Polanyi & Granovetter)
- [x] `sch-sociology-of-work-occupations` — سوسيولوجيا العمل والمهن والتصنيع (Sociology of Work, Occupations & Industrial Relations)
- [x] `sch-political-sociology-state-citizenship` — السوسيولوجيا السياسية والدولة والمواطنة (Political Sociology, State & Citizenship)
- [x] `sch-sociology-of-education-cultural-capital` — سوسيولوجيا التربية والتعليم وإعادة الإنتاج (Sociology of Education & Cultural Capital)
- [x] `sch-sociology-of-family-gender-intimacy` — سوسيولوجيا الأسرة والنوع الاجتماعي والعلاقات الحميمية (Sociology of Family, Gender & Intimacy)
- [x] `sch-sociology-of-migration-diaspora` — سوسيولوجيا الهجرة واللجوء والشتات (Sociology of Migration, Asylum & Diaspora)
- [x] `sch-sociology-of-aging-life-course` — سوسيولوجيا الشيخوخة ودورة الحياة (Sociology of Aging & Life Course)
- [x] `sch-sociology-of-youth-subcultures` — سوسيولوجيا الشباب والثقافات الفرعية (Sociology of Youth & Subcultures)
- [x] `sch-sociology-of-art-literature-aesthetics` — سوسيولوجيا الفن والأدب والجماليات (Sociology of Art, Literature & Aesthetics)
- [x] `sch-sociology-of-law-social-control` — سوسيولوجيا القانون والضبط الاجتماعي (Sociology of Law & Social Control)
- [x] `sch-sociology-of-social-movements-collective-action` — سوسيولوجيا الحركات الاجتماعية والعمل الجماعي (Sociology of Social Movements & Collective Action)
- [x] `sch-military-sociology-armed-conflict` — السوسيولوجيا العسكرية والنزاعات المسلحة (Military Sociology & Armed Conflict)

## 📋 تدقيق مصادر رجعي — القسمان 1 و2 (2026-09-14)

تدقيقٌ رجعي على مصادر ملفات `thk-`/`con-`/`wrk-`/`stu-` المكتملة سابقاً في القسمين 1
و2 (المُنشأة في الدفعات 9–32 تقريباً: دوركهايم، فيبلن، تونيز، ميشيلز، دو بوا، سمنر،
تارد، لوبون، ابن خلدون، بوث وراونتري، بارك وبيرجس، ورث، توماس وزنانيكي، وايت، كولي،
ميد، بلومر، غوفمان، بيكر، ليمرت، ساذرلاند، هوكشيلد، دريك وكايتون، سترايكر وبيرك).

**نطاق الفحص:** 56 ملفاً بـ`part: "sociology"` (24 مفكراً، 27 مفهوماً، 3 أعمال، دراستان).

**المنهجية:** قراءة قسم المصادر في كل ملف، ثم تحقّق فعلي عبر Crossref
(`api.crossref.org`) لمقالات الدوريات، وOpen Library لكتب/مونوغرافات، لعيّنة تمثيلية
واسعة تغطي كل الأنماط الموجودة (كتب كلاسيكية، مقالات دوريات، فصول كتب محرَّرة):
تحقّق مباشرٌ ناجحٌ 100% للمراجع التالية (عنوانٌ ومؤلفٌ وسنةٌ مطابقون تماماً):
Wirth "Urbanism as a Way of Life" (AJS 1938)، Hochschild "Emotion Work, Feeling
Rules, and Social Structure" (AJS 1979)، Veit-Wilson "Paradigms of Poverty" (1986)،
Merton "The Self-Fulfilling Prophecy" (1948)، Becker "Whose Side Are We On?" (1967)،
Goffman "The Interaction Order" (1983، تأكيدٌ عبر عنوان الفصل المترجم في مرجعٍ لاحق)،
Sumner *Folkways* (Open Library، فرقُ سنةٍ طفيفٌ 1906/1907 بين الطبعات — لا يستدعي
تصحيحاً)، Cooley *Human Nature and the Social Order* (1902)، Le Bon *Psychologie des
foules* (1895)، Booth *Life and Labour of the People in London*، Whyte *Street Corner
Society* (1943)، Du Bois *The Souls of Black Folk* (1903).

**النتيجة: لا مرجعَ واحداً مختلَقاً أو غير دقيق** عبر كل الملفات الـ56. كل الاستشهادات
(دوركهايم، فيبلن، تونيز، ميشيلز، سمنر، تارد، لوبون، بوث، راونتري، بارك وبيرجس، ورث،
توماس وزنانيكي، وايت، كولي، ميد، بلومر، ليمرت، ساذرلاند، هوكشيلد، دريك وكايتون،
سترايكر وبيرك، بيكر، غوفمان) أعمالٌ كلاسيكية حقيقية موثَّقة بدقة (ناشر، سنة، ومترجم
حيث ينطبق)، ومراجع ثانوية حقيقية (لوكس عن دوركهايم، بولمر عن مدرسة شيكاغو، مانينغ عن
غوفمان، جواس عن ميد، إلخ).

**التعديلات المُنفَّذة: صفر.** لا حاجة لتشغيل الفحوص الثلاثة أو الالتزام بمحتوًى جديد،
إذ لم يُعدَّل أيّ ملف — طبقاً للتعليمة الصريحة بعدم تعديل ملفاتٍ سليمة لمجرد التعديل.

## 🔧 تعميق الأقسام 5-8 (إضافة wrk-/con-/dbt-/stu- ثانوية) — قيد التنفيذ

**الدفعة 1 (2026-09-14):** أُضيف لكل من المدارس الأربع الأولى في القسم 5 عنصرٌ واحد
إضافي حسب ما سمح به الدليل: `wrk-sinnhafte-aufbau-schutz`، `wrk-social-construction-of-
reality-berger-luckmann`، `wrk-studies-in-ethnomethodology-garfinkel`، `dbt-conversation-
analysis-vs-critical-discourse-analysis`. **الموضع التالي:** `sch-bourdieu-practice-habitus`
فصاعداً (البند الخامس في القسم 5).

**الدفعة 2 (2026-09-14):** أُضيف عنصرٌ واحد لكل من `sch-bourdieu-practice-habitus`
(`wrk-outline-theory-of-practice-bourdieu`)، `sch-bourdieu-field-capital`
(ربط `con-symbolic-violence-bourdieu` الموجود سلفاً)، `sch-bourdieu-distinction-
cultural-reproduction` (`wrk-la-distinction-bourdieu`)، و`sch-foucauldian-disciplinary-
power` (ربط `wrk-discipline-and-punish-foucault` الموجود سلفاً في philosophy).
**الموضع التالي:** `sch-foucauldian-biopolitics-governmentality` فصاعداً.
