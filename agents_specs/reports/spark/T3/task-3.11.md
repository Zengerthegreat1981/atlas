# Task 3.11
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-dubose..thk-ekris.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 3 / 35 (thk-earle، thk-egaston، thk-eknobe)
- **ازدواج slug مؤكَّد**: `thk-de-bono` (THK-6228، من دفعة 3.9) و`thk-edward-de-bono` كلاهما معتمد ويصفان نفس الشخص بالضبط (إدوارد دي بونو، 1933–2021) بنفس التواريخ — thk-de-bono أعمق بكثير (اقتباس موثّق، 11 عملاً). يحتاج قرار دمج + إحالة من رئيس التحرير.
- **وفاتان غير مسجلتين اكتُشفتا ببحث خارجي**: `thk-eimber` (إيفان إمبير-بلاك) كانت مُعامَلة كحيّة (`active_end: مستمر`, مواليد 1945) بينما تُوفيت فعلياً في مايو 2024 (مواليد 1944 الصحيح) — صُحح بمصادر متعددة (Legacy.com، Guilford Journals، Ackerman Institute). `thk-ehutchins` كانت تواريخه غامضة "القرن العشرين"/1970–2010 — صُححت إلى 1934–2016 (SFI Journal، si-directory.com).
- **أخطاء تواريخ/وقائع حساسة**: `thk-edith-stein` — خلط بين تاريخ اعتناقها الكاثوليكية (قرار 1921 مقابل تعميد فعلي 1 يناير 1922) وخلط بين تطويبها (1987) وتقديسها (1998) — صُححا مع توضيح "بعد وفاتها" لكل تواريخ لاحقة لـ1942.
- **تكرار slug آخر مكتشَف**: `thk-nchomsky` و`thk-noam-chomsky` كلاهما معتمد لنفس الشخص (نعوم تشومسكي) — اكتُشف أثناء تنظيف روابط `thk-ekandel` (كان يربط الاثنين خطأً رغم عدم ذكر تشومسكي في المتن). يحتاج دمجاً وإحالة.
- **رابط id/title متضارب**: `thk-eengelhardt` كان يربط `thk-dmercieca` بعنوان "إيفا ميرسيكا" بينما العنوان المعتمد الفعلي "دانييلا ميرسيكا" — حُذف. `thk-edeci` كان يربط `thk-csikszentmihalyi` بعنوان خاطئ إملائياً — صُحح. `thk-ectolman` كان يربط `thk-fskinner` بعنوان مختصر "ب. ف. سكينر" بدل العنوان الكامل المعتمد — صُحح.
- **رابط محجور محذوف**: `thk-eengelhardt` كان يربط `thk-mcieslak` المحجور رسمياً في quarantine-minimax.md — حُذف.
- **أسماء/كتب غير موثّقة حُذفت**: `thk-ecker` (مطوّر ثالث مختلق "ريبيكا سليغلوف" + 12 رابط `related` بلا أي سبب في المتن)، `thk-ekman` (نسبة نظرية التقييم لإيكمان خطأً — تعود للازاروس/سكيرر)، `thk-earl-nightingale` (كمّ كبير من الادّعاءات السردية غير الموثّقة: استعارة السفينة، روابط مختلقة بـSemco وقاعدة 10,000 ساعة)، `thk-dzurilla` (ادّعاء إثني غير موثّق + مؤلف ثالث خاطئ)، `thk-ekeleman` (تصنيف مدرسة خاطئ تحت PBSP بدل مدرسته الخاصة).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدة ملفات (efriedman→br-bowen-systems، ehutchins→tec-rolfing، eimber→br-dynamic-couples-family-therapy، ejung/ekandel→sch-biological-neuro، edeci→sch-humanistic، edferguson→br-adlerian، ekramer→sch-art-therapy، ebordin→sch-integrative-eclectic، duckworth→sch-positive-psychology، dweck→sch-developmental). حالات بلا slug مطابق (dwile، eckhart-tolle، ekeleman) أُفرغ `edges` وسُجِّلت طلبات جديدة في `requests-spark.md`، من ضمنها تكرار إضافي لفجوة `sch-popular-psychology` (الآن 9 طلبات متراكمة).
- **جمل القائمة السوداء** حُذفت/أُعيد صياغتها في نحو 20+ ملفاً من هذه الدفعة (النمط الأشيع: "لا يوجد اقتباس مباشر موثوق متاح").

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{dubose,duckworth,duns-scotus,dweck,dwile,dzurilla,earl-nightingale,ebick,ebordin,eburne,eckartsberg,ecker,eckhart-tolle,ectolman,edeci,edferguson,edie,edinger,edith-stein,edward-de-bono,eengelhardt,efriedman,egendlin,ehutchins,eimber,ejung,ekandel,ekeleman,ekman,ekramer,ekris}.md
→ ✅ 33 ملف — صفر مخالفات آلية (thk-earle وthk-egaston سليمان تماماً، بلا مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإصلاح تسلسل تواريخ (إضافة "بعد وفاته/ها" صراحة).

## متوقف عنده (لرئيس التحرير)
- **thk-de-bono ↔ thk-edward-de-bono**: ازدواج مؤكد لنفس الشخص — يحتاج دمجاً + إحالة حسب القاعدة 6.
- **thk-nchomsky ↔ thk-noam-chomsky**: ازدواج مؤكد آخر — يحتاج دمجاً + إحالة.
- **thk-eimber**: وفاتها (مايو 2024) لم تكن مسجَّلة إطلاقاً في النسخة المعتمدة — أولوية عالية للترقية.
- **طلب `sch-popular-psychology` المجمَّع**: 9 طلبات الآن عبر الدفعات (أُضيف thk-earl-nightingale وthk-eckhart-tolle).
- **`thk-ekris`/`thk-ekramer`**: روابط تاريخية حقيقية (رابابورت، نومبرغ) حُذفت لعدم ذكرها نصياً في المتن — يستحق إعادة ربط لاحقة بعد توثيق الصلة في النص.

## الملفات
content/ar/thinkers/thk-dubose.md
content/ar/thinkers/thk-duckworth.md
content/ar/thinkers/thk-duns-scotus.md
content/ar/thinkers/thk-dweck.md
content/ar/thinkers/thk-dwile.md
content/ar/thinkers/thk-dzurilla.md
content/ar/thinkers/thk-earl-nightingale.md
content/ar/thinkers/thk-earle.md
content/ar/thinkers/thk-ebick.md
content/ar/thinkers/thk-ebordin.md
content/ar/thinkers/thk-eburne.md
content/ar/thinkers/thk-eckartsberg.md
content/ar/thinkers/thk-ecker.md
content/ar/thinkers/thk-eckhart-tolle.md
content/ar/thinkers/thk-ectolman.md
content/ar/thinkers/thk-edeci.md
content/ar/thinkers/thk-edferguson.md
content/ar/thinkers/thk-edie.md
content/ar/thinkers/thk-edinger.md
content/ar/thinkers/thk-edith-stein.md
content/ar/thinkers/thk-edsch.md
content/ar/thinkers/thk-edward-de-bono.md
content/ar/thinkers/thk-eengelhardt.md
content/ar/thinkers/thk-efriedman.md
content/ar/thinkers/thk-egaston.md
content/ar/thinkers/thk-egendlin.md
content/ar/thinkers/thk-ehutchins.md
content/ar/thinkers/thk-eimber.md
content/ar/thinkers/thk-ejung.md
content/ar/thinkers/thk-ekandel.md
content/ar/thinkers/thk-ekeleman.md
content/ar/thinkers/thk-ekman.md
content/ar/thinkers/thk-eknobe.md
content/ar/thinkers/thk-ekramer.md
content/ar/thinkers/thk-ekris.md
