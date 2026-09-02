# Task 3.19
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-hugo-saint-victor..thk-iparker (شامل هيوم وهوسرل وهيباتيا وكبار فلاسفة الإسلام: ابن سينا، ابن رشد، ابن خلدون، ابن عربي، ابن تيمية، ابن الهيثم).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 6 / 35 (thk-hugo-saint-victor، thk-huishi، thk-husserl، thk-ibn-sina، thk-ibn-taymiyya، thk-ibn-gabirol)
- **شخصية مشكوك فيها بادعاءات حساسة: thk-icheolhong** — لا دليل مستقل على وجود هذه الشخصية بالسيرة الموصوفة (مرتبطة بأبحاث "نساء المتعة")، أُعيد كتابة الملف كـ"غير قابل للتحقق" وأُفرغت edges/related. **قرار حساس جداً يحتاج حجراً رسمياً — السيرة السابقة تتضمن ادعاءات حسّاسة مفبركة على الأرجح.**
- **ازدواج slug سادس مؤكَّد: thk-ieyberg ↔ thk-seyberg** — نفس الشخص (شيلا م. إيبرغ، مؤسِّسة PCIT). حُوِّل الملف لإحالة موصى بدمجها.
- **خطأ سيرة كبير: thk-imartinbaro (إغناثيو مارتن-بارو)** — كان يزعم دراسته بجامعة كمبلوتنسي مدريد وهجرته للسلفادور 1975؛ الصحيح: انضم لليسوعيين 1959، أُرسل للسلفادور 1960، ونال درجاته من جامعة شيكاغو لا كمبلوتنسي (التي منحته فقط دكتوراه فخرية بعد وفاته). **يستحق مراجعة قبل الترقية.**
- **3 أخطاء نسبة حقيقية: thk-ihilgard (إرنست هيلغارد)** — مقياس HGSHS منسوب له خطأً (فعلياً لشور وأورن)، مؤلف مشارك وهمي "جوزيف هيلغارد" لكتاب 1977 (تأليف منفرد فعلياً)، ومؤلفة مشاركة خاطئة لكتاب 1968 (الصحيح زوجته جوزفين هيلغارد لا "أندرو مورغان").
- **خطأ تاريخ واقعي: thk-ihewlen (هيو لين)** — لقاؤه بمورنا سيميونا كان 1982 لا "أوائل التسعينيات"؛ تواريخه (1939-2022) صُححت من [DRAFT-UNKNOWN].
- **تناقضات داخلية مصححة (اقتباس موجود لكن gaps تنفيه)**: thk-huineng، thk-ibn-hazm.
- **نمط false positive رابع في فحص الجنس: thk-hypatia** — هيباتيا امرأة مؤكدة؛ عدد الضمائر المذكرة في سيرتها (سيريل، أوريستس، سقراط سكولاستيكوس) خدع الفحص الآلي. تُركت الصيغة المؤنثة الصحيحة عمداً.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير (ibn-sabin→sch-wahdat-alwujud، iberg→sch-solution-focused، ibieber→br-conversion-therapy، hweiss→tec-hakomi، iparker→sch-critical-psychology). حالات بلا slug مطابق (ibn-hazm [الظاهرية]، ibn-khaldun [علم العمران]، hweiner [الطب النفسي الجسدي]، idmarshall) أُفرغت مع تسجيل طلبات.
- **رابط محجور في ملف iparker**: thk-spiper محجور فعلياً في quarantine-minimax.md — حُذف. وتصحيح id/title (thk-dhook فعلياً "دِنيس فوكس" لا "ديريك هوك" — نسخ-لصق خاطئ من ملف آخر).
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 20 ملفاً.
- عدة ملفات فلسفية إسلامية كانت تفتقر لقسم `## المصادر` — أُضيفت مصادر أكاديمية حقيقية (iamblichus، ibn-al-haytham، ibn-arabi، ibieber).

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{huineng,hunayn-ibn-ishaq,hume,hussein,hweiner,hweiss,hypatia,iamblichus,iberg,ibieber,ibn-al-haytham,ibn-arabi,ibn-bajjah,ibn-hazm,ibn-khaldun,ibn-rushd,ibn-sabin,ibn-tufayl,ibrenner,icheolhong,ieyberg,idmarshall,ihewlen,ifrom,ihilgard,imartinbaro,imre-lakatos,ionesco,iparker}.md
→ ✅ 29 ملف — مخالفة واحدة فقط (hypatia) مؤكَّدة false positive وتُركت كما هي.
6 ملفات سليمة تماماً بلا مسودة (راجع الأرقام أعلاه).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإضافة مصادر أولية حقيقية.

## متوقف عنده (لرئيس التحرير)
- **thk-icheolhong**: يستحق حجراً رسمياً فورياً — ادعاءات حساسة (نساء المتعة) على شخصية غير موثقة.
- **thk-ieyberg ↔ thk-seyberg**: ازدواج مؤكد يحتاج دمجاً.
- **thk-imartinbaro**: إعادة كتابة سيرته التعليمية استندت لبحث خارجي — يستحق مراجعة قبل الترقية.
- **thk-hypatia**: false positive إضافي في فحص preflight_check.py للجنس — نمط متكرر (الآن 4 حالات موثقة) يستحق تحسين الـheuristic.
- **طلبات تصنيف معلَّقة**: `sch-` لمذهب الظاهرية (ابن حزم)، و`sch-` لعلم العمران الخلدوني (قد يكون فريداً لابن خلدون، قرار تصنيفي).

## الملفات
content/ar/thinkers/thk-hugo-saint-victor.md
content/ar/thinkers/thk-huineng.md
content/ar/thinkers/thk-huishi.md
content/ar/thinkers/thk-hume.md
content/ar/thinkers/thk-hunayn-ibn-ishaq.md
content/ar/thinkers/thk-hussein.md
content/ar/thinkers/thk-husserl.md
content/ar/thinkers/thk-hweiner.md
content/ar/thinkers/thk-hweiss.md
content/ar/thinkers/thk-hypatia.md
content/ar/thinkers/thk-iamblichus.md
content/ar/thinkers/thk-iberg.md
content/ar/thinkers/thk-ibieber.md
content/ar/thinkers/thk-ibn-al-haytham.md
content/ar/thinkers/thk-ibn-arabi.md
content/ar/thinkers/thk-ibn-bajjah.md
content/ar/thinkers/thk-ibn-gabirol.md
content/ar/thinkers/thk-ibn-hazm.md
content/ar/thinkers/thk-ibn-khaldun.md
content/ar/thinkers/thk-ibn-rushd.md
content/ar/thinkers/thk-ibn-sabin.md
content/ar/thinkers/thk-ibn-sina.md
content/ar/thinkers/thk-ibn-taymiyya.md
content/ar/thinkers/thk-ibn-tufayl.md
content/ar/thinkers/thk-ibrenner.md
content/ar/thinkers/thk-icheolhong.md
content/ar/thinkers/thk-idmarshall.md
content/ar/thinkers/thk-ieyberg.md
content/ar/thinkers/thk-ifrom.md
content/ar/thinkers/thk-ihewlen.md
content/ar/thinkers/thk-ihilgard.md
content/ar/thinkers/thk-imartinbaro.md
content/ar/thinkers/thk-imre-lakatos.md
content/ar/thinkers/thk-ionesco.md
content/ar/thinkers/thk-iparker.md
