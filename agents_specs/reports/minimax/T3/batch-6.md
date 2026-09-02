# Task 3 — batch-6 (thk-stephen-hawking → thk-tteo)

الحالة: مكتمل
العملية: تدقيق قرائي (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) + تصحيح مخالفات preflight | الملفات: 39

## الأرقام
- مخالفات preflight: قبل التصحيح (بعد إصلاح المشاكل الأولية) 64 → بعد 0
- ملفات حُجرت جديدة بموجب القاعدة 11: 3 (thk-struchhold، thk-teruo-ohta، thk-steven-haber)
- ملفات حجر قديمة صُححت بنيوياً (YAML مكسور): 3 (thk-takeshiyasumaru، thk-theresaglasser، thk-tom-cornwell)
- روابط `related`/`edges` مكسورة أو متضاربة صُححت أو حُذفت: ~55 عبر الدفعة
- أخطاء جنس نحوي صُححت: 2 (thk-strindberg، thk-trub — كلاهما ذكور، كان العنوان "أهم أعمالها")
- أخطاء نسبة/هوية صُححت: 1 جوهري (thk-trisley: "جيرالد بيجو" خطأ → الصحيح "سيدني و. بيجو" thk-sbijou)
- مدارس مفقودة جديدة سُجّلت في missing-schools.md: 2 (علم النفس الفردي الأدلري، العلاج بالحركة والرقص)

## أمر التحقق
`python3 scripts/preflight_check.py <39 ملف>` → ✅ 39 ملف — صفر مخالفات آلية (exit 0)

## قرارات اتخذتها

- **thk-struchhold** (Hubertus Struchhold): حُجر. الملف نفسه "محاولة توثيق" تعترف بعدم وجود أي أثر في 6 قواعد بيانات ألمانية/أوروبية للعلاج الوجودي، لكنه كان منشوراً بشبكة روابط واثقة (كيركغارد، هايدغر، سارتر، فرويد، يالوم) — تناقض تقتضي القاعدة 11 حسمه بحجر.
- **thk-teruo-ohta**: حُجر لنفس السبب (لا نتائج في J-STAGE/CiNii اليابانية، احتمال خلط مع شخصيات أخرى).
- **thk-steven-haber**: حُجر. الـgaps تعترف صراحة "لا توجد سيرة ذاتية كاملة منشورة... يعتمد على شهادة AEDP Institute فقط" رغم متن واثق يصفه كمن "رسّخ AEDP" في علاج الإدمان.
- **thk-takeshiyasumaru / thk-theresaglasser / thk-tom-cornwell**: كانت محجورة مسبقاً لكن الـfrontmatter كان مكسوراً (كتلتا YAML منفصلتان بـ`---` مكرر، وgaps خارج الكتلة) — صُححت البنية ونُظّفت edges/related لتصبح فارغة (متسقة مع كون الملف محجوراً).
- **thk-trisley**: خطأ هوية حقيقي — "جيرالد بيجو" (Gerald R. Bijou) غير موجود، الشخصية الحقيقية "أبو ABA التجريبي" هي سيدني و. بيجو (Sidney W. Bijou)، له ملف مستقل `thk-sbijou`. صُححت التسمية في المتن والروابط.
- **thk-strindberg**: تصحيح جنس نحوي ("أهم أعمالها"→"أهم أعماله")، وتصحيح `active_end` من 1907 إلى 1912 (سنة وفاته الفعلية) لحسم تضارب السنة المذكورة في المتن.
- **thk-tony-white**: نفس نمط تصحيح `active_end` (2010→2013، سنة وفاته الفعلية) بدل استخدام صياغة التفافية لسنة وفاته الذاتية.
- **عشرات الروابط `related` المكسورة**: صُححت بمطابقة الاسم الحقيقي حيث وُجد ملف صحيح (مثال: thk-rdawkins→thk-richard-dawkins، thk-jyoung→thk-young-jeffrey، thk-cgjung→thk-jung، thk-irvin-yalom→thk-yalom، thk-i-lovaas→thk-lovaas، thk-jbijou→thk-sbijou)، أو حُذفت مع تسجيل السبب في `gaps` حين لا يوجد ملف مطابق إطلاقاً (مثال: thk-jbardeen، thk-rpenrose، thk-sweinberg، thk-mgell-mann في ملف هوكينغ؛ thk-nelderrige، thk-rmacarthur، thk-eo-wilson في ملف غولد؛ عدة مفاهيم con-* غير موجودة).
- **thk-tgrandin**: حُذفت ملاحظة بحثية مسرَّبة داخل المتن ("لم أجد اسم متطابق") مع الرابط المرفق thk-uricardo غير الموجود.
- **8 روابط `edges.belongs_to` نصية حرة** حُوّلت إلى slugs حقيقية موجودة (tec-contemplative-psychotherapy، br-ai-chatbot-therapy، br-nlp-systemic، tec-hakomi، br-ddp، tec-morita-therapy، br-restorative-justice، sch-solution-focused، tec-authentic-movement)، وواحد صُحح من slug غير موجود (`sch-phil-physics`) إلى موجود (`sch-phil-science`).
- **thk-tstone / thk-trudi-schoop**: `edges.belongs_to` كان نصاً حراً بلا slug مطابق أصلاً (علم النفس الفردي الأدلري، العلاج بالحركة والرقص) → حُوّل لـ`edges: []` وسُجّل في `missing-schools.md`.
- **thk-tteo**: نفس الإجراء لـ"علم النفس النقدي" (مسجَّل مسبقاً في missing-schools.md).

## متوقف عنده (لرئيس التحرير)
- لا شيء متوقف — كل المخالفات صُححت وpreflight يرجع صفر.

## الملفات
```
content/ar/thinkers/thk-stephen-hawking.md
content/ar/thinkers/thk-stephen-jay-gould.md
content/ar/thinkers/thk-steven-haber.md
content/ar/thinkers/thk-steven-pinker.md
content/ar/thinkers/thk-stirner.md
content/ar/thinkers/thk-straus.md
content/ar/thinkers/thk-strindberg.md
content/ar/thinkers/thk-struchhold.md
content/ar/thinkers/thk-suhrawardi.md
content/ar/thinkers/thk-susan-anderson.md
content/ar/thinkers/thk-suttie.md
content/ar/thinkers/thk-syoung.md
content/ar/thinkers/thk-takanen.md
content/ar/thinkers/thk-takeshiyasumaru.md
content/ar/thinkers/thk-tandersen.md
content/ar/thinkers/thk-tandreas.md
content/ar/thinkers/thk-tatossian.md
content/ar/thinkers/thk-tbickmore.md
content/ar/thinkers/thk-tbrach.md
content/ar/thinkers/thk-teruo-ohta.md
content/ar/thinkers/thk-tgillingham.md
content/ar/thinkers/thk-tgrandin.md
content/ar/thinkers/thk-thales.md
content/ar/thinkers/thk-theresaglasser.md
content/ar/thinkers/thk-tim-ferriss.md
content/ar/thinkers/thk-tkora.md
content/ar/thinkers/thk-tleary.md
content/ar/thinkers/thk-tmoriyama.md
content/ar/thinkers/thk-todes.md
content/ar/thinkers/thk-tom-cornwell.md
content/ar/thinkers/thk-tony-white.md
content/ar/thinkers/thk-tpichot.md
content/ar/thinkers/thk-trisley.md
content/ar/thinkers/thk-trub.md
content/ar/thinkers/thk-trudakova.md
content/ar/thinkers/thk-trudi-schoop.md
content/ar/thinkers/thk-tstone.md
content/ar/thinkers/thk-tstromsted.md
content/ar/thinkers/thk-tteo.md
```
