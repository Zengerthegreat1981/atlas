# Task 3 batch-5 (thk-r → thk-s)

الحالة: مكتمل
العملية: تدقيق قرائي (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) + تصحيح مخالفات بنائية | الملفات: 39

## الأرقام
- ملفات صُحِّحت فعلياً (محتوى أو بنية): 30 من 39
- ملفات مُحوَّلة لقالب الحجر الموحّد (rule 11): 4 جديدة (thk-saberg-abramovitz، thk-sdouglas، thk-skalama، thk-sharron-hapai)
- ملفات حجر قديمة أُصلح فيها YAML مكسور (`---` مزدوج + edges/related متبقّية من قبل الحجر): 3 (thk-russellrazzaque، thk-shirley-murray، thk-spiper) + thk-rrestrepo (related متبقٍّ فقط)
- أخطاء هوية جسيمة: 1 (thk-ssafran — "ستيفن م. سَافِران" لشخص مختلف تماماً عن Jeremy D. Safran الموصوف فعلياً بالمتن والمصادر)
- أخطاء جنس نحوي في عناوين الأقسام: 4 (thk-ssafran، thk-sross، thk-rwooffitt، وتصحيح سطر نثري في thk-sshaikh)
- أخطاء نسب/اسم: 1 (thk-sbem — "داريك بيم (Derek C. Bem)" ≠ الاسم الحقيقي لزوجها بحسب مصادر الملف نفسه: Daryl J. Bem)
- روابط `related` بslugs مخترعة غير موجودة (نمط منتشر: بادئة حرف أول + لقب): ~90 رابطاً عبر الدفعة — 31 صُحِّحت لslugs حقيقية مؤكدة (تطابق اسم/لقب)، والباقي حُذف وسُجِّل في requests-minimax.md
- تطابق id/title متضارب بين رابط والملف المستهدف الفعلي: 15 حالة صُحِّحت (عناوين لا تطابق عنوان الملف الحقيقي رغم صحة الـid)
- `edges.belongs_to` بنص حر بدل slug حقيقي: 10 حالات — 8 صُحِّحت لslug فعلي موجود، 2 (لا يوجد ملف مدرسة مطابق) حُذفت وسُجِّلت في requests-minimax.md
- سنوات بعد `active_end` بلا "بعد وفاته/وفاتها": 6 حالات صُحِّحت (rsterba، sbem، schiller×3 مواضع، skalama، solzhenitsyn)

## أمر التحقق
```
python3 scripts/preflight_check.py content/ar/thinkers/thk-rpicard.md ... (39 ملفاً)
```
→ قبل التصحيح: 39 مخالفة (ملف واحد فيه مخالفة على الأقل) | بعد التصحيح: **✅ صفر مخالفات آلية**

## قرارات اتخذتها

- **thk-ssafran**: الاسم/العنوان/الـcrumb "ستيفن م. سَافِران / Stephen M. Safran" لا يطابق الشخص الموصوف — كل الاستشهادات في الملف (Safran, J. D. …) تنسب الأعمال لـJeremy D. Safran (مؤلف *Brief Relational Therapy* الفعلي). صُحِّح الاسم كاملاً + عنوان القسم المؤنث خطأ "## أهم أعمالها"→"## أهم أعماله" + أعيدت صياغة جملة "شارك Jeremy Safran" (كانت تتحدث عن الشخص كأنه طرف ثالث بعد أن أصبح هو ذاته صاحب الملف).
- **thk-sbem**: "داريك بيم (Derek C. Bem)" لزوج ساندرا بيم لا يطابق مصادر الملف نفسها التي تستشهد بـ"Bem, D. J." — صُحِّح إلى "دارِل بيم (Daryl J. Bem)". أُضيف gap بخصوص عدم مراجعة مكان الوفاة (أوريغون مقابل نيويورك) من مصدر أولي.
- **thk-sross / thk-rwooffitt**: عناوين أقسام مؤنثة ("## أهم أعمالها" / "## ما أعطته") لشخصين ذكرين — صُحِّحت لصيغة المذكر.
- **thk-saberg-abramovitz، thk-sdouglas، thk-skalama، thk-sharron-hapai**: الملفات الأربعة كانت بصيغة "يحتاج مراجعة" تعترف صراحة بعدم وجود سيرة موثّقة (بحث سلبي في IAAP/SAAJA/DDP Network/أرشيف هاواي) مع اقتراح احتمال لبس مع أشخاص آخرين — طبّقت قاعدة 11 وحوّلتها لقالب الحجر الموحّد، مع أرشفة النسخ الأصلية في `quarantine-minimax-archive/`. **thk-sharron-hapai** كانت تحمل أيضاً مخالفة صريحة لقاعدة 5 (سطر "توصية الحجر" مكتوب كاستشهاد تحت `## المصادر`) — حُذف.
- **thk-russellrazzaque، thk-shirley-murray، thk-spiper، thk-rrestrepo**: ملفات حجر سابقة (من Task 2/دفعات قديمة) كان فيها YAML مكسور فعلياً — إما `---` مزدوج مع `gaps` خارج الـfrontmatter (russellrazzaque، shirley-murray)، أو `edges`/`related` لم تُنظَّف من قبل الحجر (spiper، rrestrepo). صُحِّحت لقالب حجر نظيف واحد.
- **روابط `related` المخترعة**: نمط اكتُشف عبر الدفعة بالكامل — عشرات الروابط تستخدم صيغة "بادئة حرف أول + لقب" (`thk-sfreud`, `thk-ikant`, `thk-jgoethe`, `thk-jbutler`…) بدل الـslugs الفعلية الموجودة (`thk-freud`, `thk-kant`, `thk-goethe`, `thk-butler`). صُحِّحت الحالات ذات تطابق اسم/لقب مؤكد 1:1، وحُذفت البقية (لا يوجد ملف مطابق، أو تطابق ملتبس — مثال: `thk-jgoldstein` كان يُقصد به جوزيف غولدشتاين، لكن `thk-goldstein` الموجود فعلياً هو **كورت غولدشتاين**، شخص مختلف تماماً، فحُذف الرابط بدل ربطه خطأً). **اكتشاف إضافي:** `thk-zeno-citium` (زينون الكيتيومي، مؤسس الرواقية) مرتبط في `thk-seneca` — لا يوجد ملف له، والموجود فعلاً `thk-zeno-elea` هو **شخص مختلف تماماً** (زينون الإيلي)؛ حُذف الرابط ولم يُستبدل. كل الحذوفات مسجّلة في `requests-minimax.md`.
- **`edges.belongs_to` بنص حر**: 10 ملفات كانت تكتب اسم المدرسة/التيار كنص حر بدل slug (مخالفة صيغة القاعدة 3/شرط preflight). صُحِّحت لـslugs فعلية موجودة (`br-ai-chatbot-therapy`، `br-sensory-integration`، `br-adlerian`، `br-discursive-psychology`، `br-general-systems-cybernetics`، `br-theraplay`، `br-vr-therapy`، `sch-islamic-psychology`)، وحُذف اثنان (لا يوجد ملف "الطاوية المعرفية" ولا "علم النفس النقدي" في الأطلس بعد؛ سُجِّلا كطلب `missing-schools`/`requests-minimax.md`).
- **thk-sgilligan (ملف غير محجور)**: لا مخالفات بنيوية، محتوى سليم — لم يُعدَّل.
- **thk-slima، thk-smcnamee، thk-ssalzberg، thk-sshaikh، thk-sahmed، thk-sbeer، thk-schnell، thk-scirillo، thk-seneca، thk-sgallagher، thk-solzhenitsyn، thk-spencer-johnson، thk-schneider، thk-sbijou، thk-sbooth، thk-rschaaf، thk-rsterba، thk-rpicard، thk-rwatts، thk-sbouchard**: صُحِّحت روابط/عناوين متفرقة (تفاصيل في القسم أعلاه)، لا مشاكل هوية جوهرية.
- **thk-smcniff**: تصحيح لغوي طفيف — "نقد فيتغرينز وساكس" (اسم مشوّه لا معنى له) استُبدل بالاسمين الحقيقيين المذكورين بين قوسين أصلاً (Kay Jamison, Nancy Andreasen) مع تصحيح الصياغة النحوية (مثنى مؤنث).

## متوقف عنده (لرئيس التحرير)
- **مدرسة "العلاج المعرفي الطاوي (Taoist Cognitive Therapy)"** غائبة كملف مدرسة/تيار رغم وجود مفكرين مرتبطين بها (thk-ruilinzhou وغيره) — تحتاج طلب Task 13.
- **"علم النفس النقدي"** (Critical Psychology) غائب أيضاً كملف مدرسة — thk-spiper (محجور بسبب هوية غير موثّقة) كان مرتبطاً به.
- **أشخاص حقيقيون بارزون غائبون بالكامل من الأطلس** اكتُشفوا أثناء تتبع الروابط المكسورة: زينون الكيتيومي (مؤسس الرواقية، لا يوجد ملف — الموجود Zeno of Elea شخص مختلف)، فارلام شالاموف، سفيتلانا أليكسييفيتش، دان زاهافي، جون غريندر (NLP)، جوزيف غولدشتاين (IMS)، روم هارّيه، بيتر سِنغي، ماسون دوري (Sir Mason Durie — مطلوب من ملفين مختلفين في هذه الدفعة). قائمة كاملة في `requests-minimax.md`.
- **نمط ممنهج**: ملاحظة عامة سُجِّلت في `quarantine-minimax.md` (القسم 10) بأن نمط "slug مخترع ببادئة حرف أول + لقب" منتشر على الأرجح في دفعات إنتاج أخرى غير هذه — يستحق فحصاً منهجياً منفصلاً بدل انتظار اكتشافه ملف-بملف.

## الملفات
thk-rpicard, thk-rrestrepo, thk-rschaaf, thk-rsterba, thk-ruilinzhou, thk-russellrazzaque, thk-rwatts, thk-rwooffitt, thk-saberg-abramovitz, thk-sahmed, thk-sbeer, thk-sbem, thk-sbijou, thk-sbooth, thk-sbouchard, thk-schiller, thk-schneider, thk-schnell, thk-schulz, thk-scirillo, thk-sdouglas, thk-seneca, thk-sgallagher, thk-sgilligan, thk-sharron-hapai, thk-shestov, thk-shirley-murray, thk-skalama, thk-slima, thk-smcnamee, thk-smcniff, thk-solzhenitsyn, thk-spencer-johnson, thk-spiper, thk-sross, thk-ssafran, thk-ssalzberg, thk-sshaikh, thk-sspeer
