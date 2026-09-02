# Task 3.22
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-jgedo..thk-jmunderross.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-jgoodman، thk-jmunderross)
- **ازدواج مؤكَّد خطير: thk-jkabat-zinn ↔ thk-jkabat** — نفس الشخص (جون كابات-زين)، والأخطر أن thk-jkabat كان يحتوي فقرة يعلن فيها "وكيل 4" سابق أنه اتخذ قرار دمج من تلقاء نفسه بلا صلاحية (مخالفة صريحة للقاعدة 6) — حُذفت الفقرة، ولم يُتخذ أي دمج فعلي، الملفان بقيا منفصلين بانتظار قرار رئيس التحرير.
- **ازدواج مؤكَّد آخر: thk-jgottman-sr ↔ thk-jgottman** — لكن `thk-jgottman-sr` ليس "جون غوتمان الأب" كما يوحي الاسم، بل **جولي شوارتز غوتمان** (زوجته وشريكته المؤسِّسة) — تسمية slug مضلِّلة تماماً تحتاج إعادة تسمية.
- **ازدواج ثالث مسجَّل**: thk-jmoreno ↔ thk-moreno (جاكوب ليفي مورينو) — ملاحظة موجودة مسبقاً في الملف بانتظار دمج.
- **مدرسة/تيار محتمل الفبركة الكاملة: "SAR" (علاج التبعية-السلطة)** — thk-jhaley كان مرتبطاً بشبكة روابط متبادلة حول هذا الإطار مع thk-ebordin وthk-mkern وthk-istansky، لكن thk-istansky نفسه (المرجع الأساسي) غير موثّق أصلاً كشخص تاريخي. **يستحق فحصاً شاملاً للعنقود الأربعة.**
- **خطأ نسبة مهم: thk-jkadden (كاثلين كاري)** — كان يُنسب لها تطوير "نموذج المصفوفة" (Matrix Model) خطأً؛ العمل الحقيقي لفريق آخر (راولينغز وآخرون UCLA)، وعملها الموثّق منفصل تماماً (بروتوكولات CBT للكوكايين في ييل).
- **شراكة مفبركة: thk-jim-loehr** — "شراكة Loehr-Greenberg-Esfahani" مختلَقة بالكامل؛ الشريك الحقيقي الموثّق هو جاك غروپِّل (1992).
- **نسبة خاطئة: thk-jgrotstein** — نُسب له مفهوم "المعروف غير المُفكَّر فيه" باستقلالية عن كريستوفر بولاس، رغم كون المصطلح معروفاً تاريخياً كصياغة بولاس 1987 — حُوِّل الادعاء لـgaps كمعلومة غير مؤكدة.
- **تصحيح نسبة كتاب: thk-jjacobi** — خلط بين كتابين مختلفين ليولاندا ياكوبي (1940 و1957)، وتصحيح مهنتها (عالمة نفس لا طبيبة).
- **نمط تصنيف خاطئ متبادل تأكَّد ومُصحِّح: thk-jgrind ↔ thk-gschwartz** — كلاهما كان يربط الآخر بخلط بين NLP (البرمجة اللغوية العصبية) وNLP (معالجة اللغة الحاسوبية)؛ gschwartz كان مصححاً بالفعل من دفعة سابقة، وjgrind صُحح الآن.
- **رابط لملف محجور آخر مكتشف**: thk-jgedo كان يربط thk-mwagreich المحجور فعلياً في quarantine-minimax.md.
- **هوية خطأ مكتشفة خارج نطاق الدفعة**: thk-jmacy كشفت أن `content/ar/thinkers/thk-lroszak.md` المعتمد يحمل خطأ هوية (title "ثيرون روزاك" رغم en:"Theodore Roszak") — مسودة مصححة جاهزة للترقية.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً (jkirsch، jkornfield→sch-contemplative-psychotherapy، jledoux→br-affective-neuroscience-informed، jlilly→sch-transpersonal، jmacy→sch-ecotherapy، jkagan→sch-developmental، jmonahan→br-therapeutic-risk-assessment، jmoreno→br-psychodrama، jkihnstrom→br-clinical-hypnotherapy، jmcdowell→sch-phil-mind-analytic، jhaley→sch-systemic-family). حالات بلا slug مطابق (jgedo، jgreenberg/jgottman [طريقة غوتمان]، jherman [علاج الصدمة]، jjordan-suicide [الحزن والفقدان]، jkadden [الإدمان]، jkamiya [التغذية الراجعة العصبية]، jmarkowitz [العلاج بين الأشخاص]) أُفرغت مع تسجيل طلبات.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{jgedo,jgone,jgottman-sr,jgottman,jgreenberg,jgrind,jgrotstein,jhaley,jhenderson,jherman,jhollis,jim-loehr,jiva-goswami,jjacobi,jjordan-suicide,jkabat-zinn,jkabat,jkadden,jkagan,jkamiya,jkihnstrom,jkirsch,jkornfield,jledoux,jlilly,jlubar,jluborsky,jmacy,jmarkowitz,jmcdougall,jmcdowell,jmonahan,jmoreno}.md
→ ✅ 33 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-jkabat-zinn ↔ thk-jkabat**: ازدواج مؤكد؛ محاولة دمج غير مصرَّح بها من وكيل سابق أُلغيت — يحتاج قراراً بشرياً حاسماً.
- **thk-jgottman-sr ↔ thk-jgottman**: يحتاج إعادة تسمية slug (jgottman-sr يخص جولي شوارتز غوتمان لا جون الأب) ودمج/فصل واضح.
- **thk-jmoreno ↔ thk-moreno**: ازدواج معلَّق منذ فترة، يحتاج دمجاً.
- **"SAR" (علاج التبعية-السلطة)**: يبدو إطاراً محتمل الفبركة يربط 4 ملفات (jhaley، ebordin، mkern، istansky) — يستحق فحصاً شاملاً منفصلاً.
- **thk-lroszak**: خطأ هوية (روزاك) مكتشف خارج النطاق — مسودة مصححة جاهزة، يحتاج ترقية.
- **thk-lhecker**: بيانات غير مؤكدة ويسمّي ماركويتز خطأً "جيمس" — يستحق مراجعة/حجر مباشر.

## الملفات
content/ar/thinkers/thk-jgedo.md
content/ar/thinkers/thk-jgone.md
content/ar/thinkers/thk-jgoodman.md
content/ar/thinkers/thk-jgottman-sr.md
content/ar/thinkers/thk-jgottman.md
content/ar/thinkers/thk-jgreenberg.md
content/ar/thinkers/thk-jgrind.md
content/ar/thinkers/thk-jgrotstein.md
content/ar/thinkers/thk-jhaley.md
content/ar/thinkers/thk-jhenderson.md
content/ar/thinkers/thk-jherman.md
content/ar/thinkers/thk-jhollis.md
content/ar/thinkers/thk-jim-loehr.md
content/ar/thinkers/thk-jiva-goswami.md
content/ar/thinkers/thk-jjacobi.md
content/ar/thinkers/thk-jjordan-suicide.md
content/ar/thinkers/thk-jkabat-zinn.md
content/ar/thinkers/thk-jkabat.md
content/ar/thinkers/thk-jkadden.md
content/ar/thinkers/thk-jkagan.md
content/ar/thinkers/thk-jkamiya.md
content/ar/thinkers/thk-jkihnstrom.md
content/ar/thinkers/thk-jkirsch.md
content/ar/thinkers/thk-jkornfield.md
content/ar/thinkers/thk-jledoux.md
content/ar/thinkers/thk-jlilly.md
content/ar/thinkers/thk-jlubar.md
content/ar/thinkers/thk-jluborsky.md
content/ar/thinkers/thk-jmacy.md
content/ar/thinkers/thk-jmarkowitz.md
content/ar/thinkers/thk-jmcdougall.md
content/ar/thinkers/thk-jmcdowell.md
content/ar/thinkers/thk-jmonahan.md
content/ar/thinkers/thk-jmoreno.md
content/ar/thinkers/thk-jmunderross.md
