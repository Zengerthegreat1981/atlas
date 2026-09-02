# Task 2.52
الحالة: مكتمل
العملية: Task 2 (تحقّق وجود شخص) على 10 ملفات مفكرين مطلوبة + إصلاح روابط تابعة في 7 ملفات أخرى | الملفات: 17

## الأرقام
- موثّق (أُعيد كتابة/تصحيح وأُضيف `## المصادر`): 6 (sapolsky, panksepp, wmiller, ttu, vygotsky, piaget)
- موثّق جزئياً (تصحيح + مصادر، مع حذف اقتباس غير موثّق): 1 (vinoba-bhave)
- تحت الحجر (ازدواج slug ≠ محتوى، القاعدة 6): 2 (rwilliams، rcabrera)
- ازدواج (نفس الشخص تحت slug آخر) → إحالة صريحة: 1 (mgrof → sgrof)
- جمل قائمة سوداء محذوفة: 8 مواضع عبر 6 ملفات
- روابط `related`/`edges` مصححة أو محذوفة (id/title متضارب أو target نص حر): 20+ عبر 9 ملفات
- مخالفات preflight قبل الإصلاح: 33 → بعد الإصلاح: 0

## أمر التحقق
`python3 scripts/preflight_check.py --report agents_specs/reports/minimax/T2/task-2.52.md`  →  `✅ 17 ملف — صفر مخالفات آلية`

## قرارات اتخذتها

- **thk-robert-sapolsky**: موثّق (روبرت سابولسكي، Stanford، Behave 2017 وWhy Zebras Don't Get Ulcers 1994 — أعمال حقيقية موثّقة). حذفت قسم الاقتباسات (جملة قائمة سوداء)، أضفت `## المصادر` بأربعة مراجع حقيقية.
- **thk-panksepp**: موثّق (ياكوب بانكسيب، مؤسس علم الأعصاب الوجداني، Affective Neuroscience 1998). حذفت قسم الاقتباسات، أضفت `## المصادر`.
- **thk-wmiller**: موثّق (William R. Miller، المقابلة التحفيزية مع رولنيك 1991). حذفت قسم الاقتباسات، أضفت `## المصادر`. لا ازدواج مع ملف آخر.
- **thk-ttu**: موثّق (Tu Weiming، الكونفوشية الجديدة، هارفارد). صححت جملة مشوّهة/مكسورة في «أهم أعماله» (نص برمجي متسرب: `مع{He(thk-mencius) أشار إليه}`)، حذفت جملة القائمة السوداء من `gaps`، صححت رابط `con-ren` (title كان مضادّاً لعنوان الملف الحقيقي)، أضفت `## المصادر`.
- **thk-vygotsky**: موثّق (ليف فيغوتسكي، النظرية السوسيو-ثقافية). صححت `edges.developed` من نص حر («العلاج المعرفي البنائي») إلى slug حقيقي `br-constructivist-cognitive`. أضفت «بعد وفاته» عند كل سنة لاحقة لـactive_end=1934 (1976، 1962، 1978 — أعمال نُشرت بعد وفاته أو مصطلحات صاغها آخرون لاحقاً). أضفت `## المصادر`.
- **thk-piaget**: موثّق (جان بياجيه). صححت خطأ نسب: النص الأصلي قال إن بياجيه طوّر منهجه العيادي «تحت إشراف كارل يونغ وتيودور فلوغل في زيورخ» — لا يوجد "تيودور فلوغل" في سيرة بياجيه؛ المتعاون الفعلي في مختبر بينيه بباريس هو **تيودور سيمون (Théodore Simon)**، شريك ألفريد بينيه. صححت الجملة. صححت `edges.developed` من نص حر إلى `br-constructivist-cognitive`، وصححت عنواني `con-zpd`/`con-cognitive-development-stages` ليطابقا الملفين المستهدفين فعلياً. أضفت `## المصادر`.
- **thk-vinoba-bhave**: موثّق (فينوبا بهاف، حركة Bhoodan، شخصية غاندية حقيقية وشهيرة). حذفت `edges` الثاني (target نص حر «الغاندية (كفلسفة سياسية-أخلاقية)» بدل slug — والرابط الأول لنفس المدرسة موجود أصلاً عبر `sch-gandhianism`). حذفت الاقتباس المنسوب له (غير موثّق بمصدر وصفحة، صيغ متعددة متضاربة في مصادر ثانوية) ونقلت السبب لـ`gaps`. صححت عنواني `con-ahimsa-non-violence`/`con-satyagraha` ليطابقا الملفين الفعليين. أضفت `## المصادر`.
- **thk-rwilliams**: **تحت الحجر (القاعدة 6)**. المحتوى الفعلي بالكامل عن **روجر ت. أيمز (Roger T. Ames)**، فيلسوف كونفوشي أمريكي موثّق بمصادر حقيقية (Ames & Hall 1998/2001، Ames 2010/2011) — لا علاقة بـ"Williams" إطلاقاً. كان الملف نفسه يحمل ملاحظة معمارية داخلية تعترف بالخطأ («الـslug الصحيح thk-rames») دون طلب فعلي — بالضبط ما تمنعه القاعدة 6. أرشفت النسخة الأصلية، حوّلت الملف لقالب حجر/إحالة (نفس نمط `thk-rsperry`/`thk-sgreys` من دفعات سابقة)، سجّلت طلب slug جديد `thk-rames` في `requests-minimax.md` (R-007) وسطراً في `quarantine-minimax.md`. اكتشفت بالمناسبة أن رابطاً من `thk-jakhan.md` كان يشير خطأً لهذا الـslug بعنوان «روبرت ويليامز» بينما القصد الفعلي كان **روبرت لي ويليامز الثاني** (الموجود فعلاً تحت `thk-rlwilliams`) — صححت الرابط.
- **thk-rcabrera**: **تحت الحجر (القاعدة 6 + 11)**. تحقق مباشر في الملف أكد ملاحظة المستخدم: الشخص الموصوف فعلياً هو **أكينسولا أكيووو (Akinsola A. Akiwowo)**، عالم اجتماع وأنثروبولوجي نيجيري (1926/1928–1990)، صاحب نظرية «أجوبي أجوبي» (1976) — لا علاقة بـ"Cabrera" إطلاقاً. الملف كان يعترف صراحة في `gaps` بأن "ريتشارد كابريرا" غير موجود، ثم ينشر مع ذلك سيرة أكيووو الكاملة تحت الـslug المضلل — تناقض شكل واثق/مضمون شكّاك تحديداً ما تحظره القاعدة 11. أرشفت النسخة الأصلية، حوّلت لقالب حجر/إحالة، سجّلت طلب slug جديد `thk-aakiwowo` (R-008). أزلت الروابط الخمسة الواردة لهذا الـslug من (`thk-asante`، `thk-hountondji`، `thk-wiredu`، `thk-bodunrin`، `sch-african-psychology`) حتى يُحسم slug صحيح.
- **thk-mgrof**: **ازدواج مؤكد**. المحتوى بالكامل هو **ستانيسلاف غروف (Stanislav Grof)** — نفس الشخص الموثَّق فعلاً وبروابط واردة أكثر (20+) تحت `thk-sgrof` (بينما mgrof له 3 روابط واردة فقط). الملف نفسه كان يحوي ملاحظة معمارية تقول إنه «يحل محل thk-sgrof» — وهذا خطأ: القرار الصحيح حسب قاعدة الازدواج هو إبقاء الأفضل ربطاً (`thk-sgrof`) والتحويل. حوّلت `thk-mgrof` إلى `redirect_to: thk-sgrof` صريح، وصححت الرابط الوحيد داخل نطاقي (`sch-transpersonal.md`) الذي كان يشير إليه بعنوان «ستانيسلاف غروف (النسخة المعدلة)» ليشير لـ`thk-sgrof` مباشرة. **ملاحظة نطاق:** ملف `content/ar/techniques/tec-holotropic-breathwork.md` يشير أيضاً لـ`thk-mgrof` لكنه خارج نطاقي (مجلد Spark) — يحتاج تصحيحاً من مسار Spark أو كلود.
- **الملفات الخمسة التابعة** (`thk-bodunrin`, `thk-asante`, `thk-hountondji`, `thk-wiredu`, `thk-jakhan`, `sch-african-psychology`, `sch-transpersonal`): لمسات لازمة لأن preflight رفض 33 مخالفة إجمالاً في الدفعة — عدد كبير منها عناوين `related` قديمة/متضاربة أو `edges` بنص حر بدل slug كانت موجودة أصلاً قبل لمسي (ليست من صنعي)، لكن بما أنني عدّلت هذه الملفات (لإزالة روابط rcabrera/rwilliams المكسورة) وجب تصحيحها كاملة قبل كتابة التقرير حسب القاعدة الإلزامية لـpreflight.

## متوقف عنده (لرئيس التحرير)

- **thk-rwilliams / thk-rcabrera**: يحتاجان قراراً بشرياً لفتح slug جديد فعلي (`thk-rames`, `thk-aakiwowo`) ونقل المحتوى المؤرشف إليه — أنا لا أستطيع اختراع slug جديد.
- **`content/ar/techniques/tec-holotropic-breathwork.md`**: لا يزال يشير لـ`thk-mgrof` (الآن إحالة) بدل `thk-sgrof` — خارج نطاق كتابتي (مجلد Spark).
- **`content/ar/drafts/EXISTING_SLUGS.md`**: يحوي إشارات قديمة لـ`thk-rwilliams`/`thk-rcabrera`/`thk-mgrof` كمعتمدة — يُعاد بناؤه تلقائياً بـ`build_slug_index.py` (نُفّذ)، فلا حاجة لتعديل يدوي.

## الملفات
content/ar/thinkers/thk-rwilliams.md
content/ar/thinkers/thk-rcabrera.md
content/ar/thinkers/thk-robert-sapolsky.md
content/ar/thinkers/thk-panksepp.md
content/ar/thinkers/thk-vinoba-bhave.md
content/ar/thinkers/thk-wmiller.md
content/ar/thinkers/thk-mgrof.md
content/ar/thinkers/thk-ttu.md
content/ar/thinkers/thk-vygotsky.md
content/ar/thinkers/thk-piaget.md
content/ar/thinkers/thk-bodunrin.md
content/ar/thinkers/thk-asante.md
content/ar/thinkers/thk-hountondji.md
content/ar/thinkers/thk-wiredu.md
content/ar/thinkers/thk-jakhan.md
content/ar/schools/sch-african-psychology.md
content/ar/schools/sch-transpersonal.md
