# Task 16.2 — الحوارات الغائبة (dia-) + تصنيف صحيح لحالات مشتبهة
الحالة: مكتمل | الملفات: 8 (5 dia- + 2 dbt- + 1 con-)

## العملية
8 subagents لملء قائمة الحوارات المتبقية من تقرير 16.1. ثلاثة منها كانت مُدرجة أصلاً كـ"حوارات" لكن تبيَّن أنها نزاعات منشورة لا لقاءات موثقة فعلياً — **صُنِّفت بشكل صحيح** بدل إجبارها على قالب dia- (نمط "تحقق من النوع أولاً" الذي طُبِّق طوال الجلسة). تصادم ترقيم متكرر (4 حالات) حُسم يدوياً بالكامل.

## ✅ ملفات dia- حقيقية (5) — لقاءات/تبادلات موثقة فعلياً
- **dia-freud-ferenczi** (DIA-0051) — علاقة 25 عاماً (1908-1933): مراسلات >1200 رسالة، رحلة كلارك 1909 المشتركة، القطيعة حول "ارتباك اللغات" 1932
- **dia-klein-anna-freud-controversial-discussions** (DIA-0052) — النقاشات الخلافية في الجمعية البريطانية للتحليل النفسي 1941-1945، أدَّت لانقسام مؤسسي ثلاثي لا يزال قائماً
- **dia-jung-pauli** (DIA-0053) — علاقة 1932-1958: إحالة باولي لتحليل نفسي، أحلامه كمادة بحثية ليونغ، التعاون المفهومي الذي أنتج "التزامن"، كتاب مشترك 1952
- **dia-jabri-hanafi** (DIA-0054) — كتاب "حوار المشرق والمغرب" الفعلي بين الجابري وحنفي حول مقاربتي نقد التراث
- **dia-einstein-freud-why-war** (DIA-0055) — تبادل رسائل 1932 برعاية عصبة الأمم، نُشر ككتيب "لماذا الحرب؟" 1933

## ✅ إعادة تصنيف صحيحة (2 → dbt-، 1 → con-) — تجنُّب فرض حوار غير موثَّق
- **dbt-eysenck-1952-psychotherapy-efficacy** (DBT-2016): جدل آيزنك 1952 حول فعالية العلاج النفسي — نزاع منشور عبر عقود، لا لقاء موثَّق — صُنِّف dbt- بدل dia-
- **dbt-pinker-gould-darwinian-fundamentalism** (DBT-2017): نزاع بينكر-غولد 1997 — تحقق subagent فعلياً عبر بحث ويب أن التبادل كان بالكامل عبر NYRB (أربعة أعداد متتالية 1997)، لا لقاء مباشر — صُنِّف dbt-
- **con-kandel-1998-new-intellectual-framework-psychiatry** (CON-3020): مقالة كاندل الفردية 1998 — لا حوار ثنائي إطلاقاً (مقترح نظري فردي)، وتكرار جزئي مع dbt-mental-illness-brain-disease الموجود مسبقاً كُشف ورُبط بدل التكرار — صُنِّف con- وربط بالملف الأوسع

## ⚠️ تصادم ترقيم متكرر (4 حالات) — حُسم يدوياً بالكامل
- DIA-0051: 2 ملفات (freud-ferenczi، einstein-freud) → أُعيد ترقيم الثاني لـDIA-0055
- DIA-0052: 3 ملفات (klein-afreud، jung-pauli، jabri-hanafi) → أُعيد ترقيم الاثنين الأخيرين لـDIA-0053 وDIA-0054
- DBT-2016: 2 ملفات (eysenck، pinker-gould) → أُعيد ترقيم الثاني لـDBT-2017
تحقُّق نهائي: صفر تكرار عبر `content/ar/drafts/minimax/dialogues/` وdebates/ معاً.

صفر slugs مخترعة، صفر مصادر ملفَّقة، صفر مخالفات preflight، صفر تطابق قائمة سوداء (تحقق شخصي نهائي على الملفات الثمانية).

## قرارات جودة بارزة
- dia-jung-pauli: لا ملف thk- لفولفغانغ باولي (فيزيائي مركزي في العلاقة) — لم يُخترع slug، طلب مسجَّل.
- dia-klein-anna-freud: لا ملف thk- لسيلفيا باين (رأست الجلسات فعلياً) ولا إيلا شارب — طلبات مسجَّلة. تجنَّب subagent خلط thk-sharper (شخص آخر تماماً، Susan Harper) مع Ella Sharpe الحقيقية.
- dbt-pinker-gould: لم يُربط thk-jgould (شخص مختلف تماماً، James Lubin) بالخطأ مع Stephen Jay Gould الحقيقي.

## متوقف عنده (لرئيس التحرير)
- طلبات slug مسجَّلة: فولفغانغ باولي، سيلفيا باين، إيلا شارب.
- Task 16 لا يزال يحتاج (من تقرير 16.1): بارتليت *التذكّر*، هِب *تنظيم السلوك*، نايسر *علم النفس المعرفي*، دوبور *مجتمع الاستعراض*.
- إزدواج wrk- الثقيل المذكور في 16.1 (being-nothingness ×3، ظاهراتية الإدراك ×3، بنية الثورات العلمية ×2) لا يزال بلا حسم — يحتاج جلسة تدقيق/دمج مخصصة.

## الملفات (مسار كامل)
content/ar/drafts/minimax/dialogues/{dia-freud-ferenczi,dia-einstein-freud-why-war,dia-klein-anna-freud-controversial-discussions,dia-jung-pauli,dia-jabri-hanafi}.md
content/ar/drafts/minimax/debates/{dbt-eysenck-1952-psychotherapy-efficacy,dbt-pinker-gould-darwinian-fundamentalism}.md
content/ar/drafts/minimax/concepts/con-kandel-1998-new-intellectual-framework-psychiatry.md
