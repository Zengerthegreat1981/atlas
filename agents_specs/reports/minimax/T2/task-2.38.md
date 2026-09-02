# Task 2.38
الحالة: مكتمل
العملية: توثيق/تدقيق دفعة 37 مفكراً مشكوكاً في وجودهم | الملفات: 37

## الأرقام
- موثّق (أُعيد التوثيق بمصادر حقيقية): 37/37
- غير موجود (حجر): 0/37
- غامض: 0/37
- ملفات فيها `## المصادر` قبل الدفعة: 1/37 (thk-rrackoff فقط)
- ملفات فيها `## المصادر` بعد الدفعة: 37/37
- جمل قائمة سوداء محذوفة: 24 (17 نسخة حرفية من "لا يوجد اقتباس مباشر موثوق متاح"/صيغ قريبة منها في gaps وفي "## اقتباسات مختارة")
- روابط `edges.belongs_to` بنص حر صُححت لـslug حقيقي: 10 (musonius كان سليماً أصلاً؛ xiong-shili، nakbar، pierre-gassendi، yi-i-yulgok، yi-hwang-toegye، posner، wang-fuzhi صُححت لـslugs موجودة؛ rrackoff صُححت لمسودة sch-general-systems-theory الموجودة كملف؛ tsongkhapa رُبط بـsch-madhyamaka بدل مدرسة غيلوغ غير الموجودة)
- روابط `edges` حُذفت وسُجّلت في `missing-schools.md`: 1 (thk-titchener — "البنائية النفسية Psychological Structuralism" لا يوجد لها ملف مدرسة مستقل؛ sch-structuralism الحالي بنيوية لغوية لا نفسية)
- روابط `related` بعنوان (`title`) متضارب مع الملف المستهدف الحقيقي صُححت: 13 (raju×2، rrackoff×1 بعد حذف 5 روابط لملفات غير موجودة، nakbar×2 بعد حذف 3 روابط لملفات/مفاهيم غير موجودة، tsongkhapa×1، zalman×2، posner×1، richard-bernstein×2، wang-fuzhi×1)
- روابط `related` بid لملفات غير موجودة أصلاً حُذفت: 8 (rrackoff: thk-pcheckland، thk-cemery، thk-wdmills، con-interactive-planning، con-idealized-redesign؛ nakbar: thk-kobi، dis-self-concept، con-african-psychology)
- سطور `gaps` تؤكد حقيقة بدل ما تسمي فجوة (مخالفة شرط القبول 5) صُححت: 2 (thk-rrackoff، thk-nakbar)
- إشارات "بعد وفاته/وفاتها" أُضيفت أو صُححت قرب سنة بعد `active_end`: 12 مرجعاً عبر 5 ملفات (montesquieu×4، spencer×4، zalman×2، pierre-gassendi×1، montaigne×1)
- محتوى مُختلَق/مشكوك أُزيل: فقرة "الأثر الفلسفي اللاحق" في thk-titchener (ربط وهمي بين تيتشنر ونظرية التنافر المعرفي لفستنغر، وخطأ في اسم آيزنك الأول، وشخصية "لايتمان" غير موثّقة)؛ co-author وهمي "M. J. Bochnak" في thk-posner (اسم مؤلف كتاب Posner 1973 الحقيقي هو Posner منفرداً)؛ جملة تفريق زائفة عن "Michael E. Posner" و"Michael L. Posner" في thk-posner؛ رابط id/title متضارب كلياً (`exp-antonin-artaud-rodez-asylum` بعنوان "أنطونيو داماسيو") في thk-posner
- خطأ مطبعي "其他人" (حروف صينية مقحمة خطأ) في thk-rrackoff صُحح إلى "وآخرين"

## أمر التحقق
`python3 scripts/preflight_check.py <37 ملف>` → قبل: 28 مخالفة (13 تضارب id/title، 8 روابط لملفات غير موجودة، 2 gaps تؤكد حقيقة، 2 جملة قائمة سوداء، 3 سنة بعد active_end بلا "بعد وفاته") → بعد: **0 مخالفة**، خروج 0.

## قرارات اتخذتها
جميع الـ37 اسماً تبيّن أنهم شخصيات موثّقة تاريخياً (فلاسفة يونانيون/رومان/صينيون/كوريون/هنود/تبتيون/عرب/غربيون معروفون في المراجع الأكاديمية القياسية: SEP، مصادر جامعية محكّمة، إلخ). لم يُقرَّر "غير موجود" لأي ملف. القرار الوحيد المتكرر هو **موثّق** مع تدقيق وتصحيح:
- **إعادة توثيق كاملة (إضافة `## المصادر`)**: 36 ملفاً كانت بلا القسم فعلياً (rrackoff كان الوحيد الذي يملكه، وzalman أُضيف له لاحقاً بعد أن اتضح غيابه رغم وجود اقتباس).
- **حذف الجملة السوداء "لا يوجد اقتباس مباشر موثوق متاح" وما يشبهها**: حُذفت من قسم "اقتباسات مختارة" (فاستُبدل بمصادر) ومن `gaps` في 17 ملفاً، مع حذف قسم "اقتباسات مختارة" كلياً حيث لا يوجد اقتباس موثّق بديل (raju، nimbarka، sadr-al-din-al-qunawi، إلخ) بدل تركه فارغاً أو معاداً صياغته بجملة مشابهة.
- **thk-titchener**: أخطر ملف في الدفعة من ناحية المحتوى — كان مربوطاً بـ`edges.belongs_to` بمدرسة خاطئة تماماً (الظاهراتية الوجودية) رغم أن تيتشنر بنائي تجريبي لا وجودي. حُذف الرابط، سُجّلت المدرسة الصحيحة الغائبة (`missing-schools.md`)، وحُذفت فقرة كاملة فيها روابط مُختلَقة (فستنغر↔تيتشنر، آيزنك بالاسم الخطأ، "لايتمان" غير موثّق).
- **thk-nakbar**: كان فيه خلط هوية بين Wade Nobles وJoseph Baldwin تحت id واحد (`thk-jakhan`)، صُحح العنوان للمطابق الفعلي لملف thk-jakhan ("ويد نوبلز")، وحُذفت 3 روابط لعناصر غير موجودة في الأطلس أصلاً.
- **thk-rrackoff**: نصف روابط `related` (5 من 8) كانت تشاور على IDs غير موجودة أصلاً في الأطلس (Checkland، Emery، Mills، ومفهومان) — حُذفت، وأُبقي فقط على الروابط الحقيقية (برتالانفي، بير، تشرتشمان بعد تصحيح عنوانه).
- **مدارس مفقودة جديدة سُجّلت (1)**: "البنائية النفسية (فونت–تيتشنر)" في `missing-schools.md`.

## متوقف عنده (لرئيس التحرير)
- الـslug الحالي `thk-rrackoff` مكتوب بخطأ إملائي (حرف r إضافي) عن Russell Ackoff؛ التصحيح البشري لإعادة التسمية محتاج تنسيقاً لأن الروابط الواردة تعتمد عليه.
- سنة وفاة مراد وهبة (thk-murad-wahba) غير مؤكدة بدقة في المصادر المتاحة هنا (frontmatter يضع 2024 تقديراً)؛ سُجّلت في `gaps`.
- تعارضات slug عامة (464 تعارض) ظهرت عند تشغيل `build_slug_index.py` — كلها موجودة مسبقاً في المستودع (تعارضات مسودات Spark/MiniMax القديمة) وليست ناتجة عن هذه الدفعة.
- ملف `thk-amncube` له نسختان متضاربتان في الهوية (المعتمد: "ألبرت مْنكوبِي"؛ مسودة Spark: "نكازيلو نكوبي") — لم أُصلحه لأنه خارج نطاق كتابتي (مجلد Spark)، فحذفت الرابط إليه من thk-nakbar بدل الإبقاء على تضارب.

## الملفات
content/ar/thinkers/thk-musonius-rufus.md
content/ar/thinkers/thk-raju.md
content/ar/thinkers/thk-rrackoff.md
content/ar/thinkers/thk-philon-larissa.md
content/ar/thinkers/thk-xiong-shili.md
content/ar/thinkers/thk-shao-yong.md
content/ar/thinkers/thk-zhuangzi.md
content/ar/thinkers/thk-michael-pollan.md
content/ar/thinkers/thk-wang-yangming.md
content/ar/thinkers/thk-shantarakshita.md
content/ar/thinkers/thk-mou-zongsan.md
content/ar/thinkers/thk-pierre-gassendi.md
content/ar/thinkers/thk-nakbar.md
content/ar/thinkers/thk-zhang-zai.md
content/ar/thinkers/thk-montesquieu.md
content/ar/thinkers/thk-yi-i-yulgok.md
content/ar/thinkers/thk-posidonius.md
content/ar/thinkers/thk-thrasymachus.md
content/ar/thinkers/thk-titchener.md
content/ar/thinkers/thk-yi-hwang-toegye.md
content/ar/thinkers/thk-murad-wahba.md
content/ar/thinkers/thk-tsongkhapa.md
content/ar/thinkers/thk-zalman.md
content/ar/thinkers/thk-vyasatirtha.md
content/ar/thinkers/thk-posner.md
content/ar/thinkers/thk-nimbarka.md
content/ar/thinkers/thk-sadr-al-din-al-qunawi.md
content/ar/thinkers/thk-montaigne.md
content/ar/thinkers/thk-proudhon.md
content/ar/thinkers/thk-shantideva.md
content/ar/thinkers/thk-richard-bernstein.md
content/ar/thinkers/thk-spencer.md
content/ar/thinkers/thk-sayf-al-din-al-amidi.md
content/ar/thinkers/thk-qutb-al-din-al-shirazi.md
content/ar/thinkers/thk-tayeb-tizini.md
content/ar/thinkers/thk-strato-lampsacus.md
content/ar/thinkers/thk-wang-fuzhi.md
