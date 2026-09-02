# Task 2.29
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 26

## الأرقام
جمل القائمة السوداء: قبل 26 (تقريباً، منتشرة في gaps أو "## اقتباسات مختارة" في أغلب الملفات) → بعد 0
فيها ## المصادر: قبل 0/26 → بعد 26/26
edges.belongs_to بنص حر بدل slug: قبل 7 (shenggeler, wdunn, wwhite, pappelbaum, mfeldenkrais, tjames, tsilvester) → بعد 0 (6 حُوّلت لـslug حقيقي، 1 حُذفت edges وسُجّلت في missing-schools.md)
روابط related غير مبرَّرة في المتن (نسخ-لصق قالبي متطابق: thk-shiggins/thk-ellis/thk-ecker) في 4 ملفات (ryle, morin, schauer, wells-adrian) → أُزيلت من الأربعة
روابط related متضاربة id/title (preflight): 2 (shenggeler: shonwald، unamuno: ortega) → 0
مخالفات preflight_check.py: 9 → 0

## أمر التحقق
python3 scripts/task.py verify minimax 2.29
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 26 / 26

python3 scripts/preflight_check.py <26 ملف الدفعة>
→ ✅ 26 ملف — صفر مخالفات آلية.

grep يدوي على كل ملف بالنص الحرفي لجمل القائمة السوداء (الاثنتان الأكثر شيوعاً في هذه الدفعة):
grep -l "لا يوجد اقتباس مباشر موثوق متاح\|يمثل هذا المفهوم لبنة تأسيسية\|حظي هذا المفهوم بمراجعات" <26 ملف>
→ لا نتائج (exit 1) — تأكيد صفر فعلي، مش بس preflight.

## قرارات اتخذتها
جميع الـ26 اسماً في هذه الدفعة **موثّقون فعلياً** — كلهم أشخاص حقيقيون معروفون في مجالاتهم (فلاسفة كلاسيكيون/معاصرون، معالجون وباحثون سريريون موثّقون بمؤسساتهم الأكاديمية). لم يُحجر أي ملف في هذه الدفعة. القرار الموحّد لكل ملف: **موثّق → أعيدت كتابة/تصحيح ما يلزم + إضافة ## المصادر**.

- thk-masson-oursel: موثّق (مؤسس الفلسفة المقارنة، فرنسا). أُضيفت ## المصادر (3 مراجع)، وأُعيدت صياغة gaps المبهمة.
- thk-mwilliams: موثّق (Mark Williams، أحد مؤسسي MBCT، أكسفورد). حُذفت جملة القائمة السوداء من gaps، أُضيفت ## المصادر.
- thk-philo-alexandria: موثّق (فيلون الإسكندري). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر (3 مراجع أكاديمية).
- thk-shenggeler: موثّق (Scott Henggeler، مؤسس MST). edges.belongs_to حُوّل من نص حر "العلاج متعدد الأنظمة (MST)" إلى br-mst الحقيقي. حُذف رابط thk-charles-glisson (كان gap يقول إنه أُزيل لكنه كان لا يزال في related — تناقض صُحّح). صُحّح عنوان thk-sschoenwald ("سونيا ك. شونوالد" بدل "سونيا شونوالد" ليطابق الملف). حُذف قسم "اقتباسات مختارة" (كان يحتوي جملة القائمة السوداء فقط)، أُضيفت ## المصادر.
- thk-maslow: موثّق (أبراهام ماسلو). حُذفت جملة القائمة السوداء من gaps، أُضيفت ## المصادر.
- thk-meharding: موثّق (M. Esther Harding، محللة يونغية رائدة). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-samuels: موثّق (Andrew Samuels، جامعة Essex). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-wquine: موثّق (W.V.O. Quine). أُضيفت ## المصادر. صُحّح خطأ في active_end (كان 1996 خطأً، والصحيح 2000 — سنة وفاته، وقد ظل أستاذاً في هارفارد حتى وفاته) بعدما رصده preflight_check.py كسنة متن (2000) بعد active_end بلا تفسير.
- thk-zoja: موثّق (Luigi Zoja، رئيس سابق لـIAAP). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-unamuno: موثّق (ميغيل دي أونامونو). أُضيفت ## المصادر، أُعيدت صياغة gaps المبهمة. صُحّح عنوان thk-ortega ("خوسيه أورتيغا إي غاسيت" بدل "خوسيه أورتيجا إي جاسيت" ليطابق الملف الحقيقي).
- thk-wdunn: موثّق (Winnie Dunn، Sensory Profile). edges.belongs_to حُوّل من نص حر "التكامل الحسي" إلى br-sensory-integration الحقيقي. حُذفت جملة القائمة السوداء، أُضيفت ## المصادر. أُعيدت صياغة gap كان preflight يعتبره "تأكيد حقيقة" بدل فجوة.
- thk-rwalsh: موثّق (Roger Walsh، UC Irvine). حُذف قسم اقتباسات القائمة السوداء، أُضيفت ## المصادر.
- thk-pappelbaum: موثّق (Paul Appelbaum، Columbia). edges.belongs_to حُوّل من نص حر "تقييم المخاطر العلاجي" إلى br-therapeutic-risk-assessment الحقيقي. حُذف رابط thk-cwebster المكرر مرتين في gaps مع تناقض (كان يقول "أُزيل" لكنه لا يزال في related). أُضيفت ## المصادر.
- thk-tagore: موثّق (رابندراناث طاغور). أُضيفت ## المصادر.
- thk-wells-adrian: موثّق (Adrian Wells، مؤسس MCT). حُذفت جملة القائمة السوداء من gaps. حُذفت الروابط الثلاثة غير المبرَّرة في المتن (thk-shiggins/thk-ellis/thk-ecker — نسخ-لصق قالبي ظهر متطابقاً حرفياً في 4 ملفات مختلفة تماماً في هذه الدفعة). أُضيفت ## المصادر.
- thk-spillius: موثّق (Elizabeth Bott Spillius). حُذفت جملة القائمة السوداء. صُحّحت جملة "هو المرجع" إلى "يُعدّ المرجع" (كانت تُطلق مؤشر preflight الجندري كذباً — الملف مؤنث بالكامل، لكن "هو" كانت تشير لموضوع مذكر لا للمفكرة). أُضيفت ## المصادر.
- thk-wwhite: موثّق (William L. White، مؤرخ حركة التعافي). edges.belongs_to حُوّل من نص حر إلى br-recovery-oriented. حُذف رابطان غير مؤكَّدين (thk-gene-ennis، thk-mary-elmquist) لعدم القدرة على تأكيد أهميتهما في المتن. حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-schauer: موثّق (Maggie Schauer، NET). حُذفت الروابط الثلاثة غير المبرَّرة (shiggins/ellis/ecker، نفس نمط النسخ-اللصق). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-ptahhotep: موثّق (بتاح حتب، نص حكمة مصري قديم). أُضيفت ## المصادر (2 مرجعين أكاديميين في الأدب المصري القديم).
- thk-ryle: موثّق (Anthony Ryle، مؤسس CAT). حُذفت الروابط الثلاثة غير المبرَّرة (shiggins/ellis/ecker). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-morin: موثّق (Charles M. Morin، CBT-I). حُذفت الروابط الثلاثة غير المبرَّرة (shiggins/ellis/ecker). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-mfeldenkrais: موثّق (Moshé Feldenkrais). edges.belongs_to حُذف كلياً (لا يوجد ملف مدرسة/تيار حي لـ«طريقة فيلدنكرايس» — سُجّلت في missing-schools.md). حُذفت 5 روابط related كانت gaps تقول إنها "أُزيلت" لكنها ظلت موجودة فعلياً (تناقض صُحّح: thk-lavinia-shaw، thk-markrees، thk-rupertpriest، thk-stephenburgess، thk-yvaniedmon). حُذف قسم اقتباسات القائمة السوداء، أُضيفت ## المصادر. (ملاحظة تقنية: أثناء التعديل انكسر سطر "---" الفاصل للـfrontmatter سهواً، فصُحّح فوراً بعد ما رصده preflight_check.py.)
- thk-tjames: موثّق (Tad James، NLP). edges.belongs_to حُوّل من نص حر إلى br-nlp-systemic. حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-tsilvester: موثّق (Trevor Silvester، Cognitive Hypnotherapy). edges.belongs_to حُوّل من نص حر إلى br-clinical-hypnotherapy. حُذفت 3 روابط غير مبرَّرة في المتن (thk-dspiegel، thk-hcrsilneck، thk-wkroger). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-shamdasani: موثّق (Sonu Shamdasani، محرر الكتاب الأحمر ليونغ). حُذفت جملة القائمة السوداء، أُضيفت ## المصادر.
- thk-nisesilveira: موثّقة (Nise da Silveira، رائدة الإصلاح النفسي البرازيلي). حُذفت جملة القائمة السوداء. أُعيد صياغة gap عن قانون 2001 (بعد وفاتها 1999) ليتجنب صياغة "تأكيد حقيقة" رصدها preflight، وأُضيف توضيح زمني واضح. أُضيفت ## المصادر.

## متوقف عنده (لرئيس التحرير)
- لا يوجد ملف متوقف — الدفعة الـ26 اكتملت بالكامل: توثيق مع مصادر حقيقية، صفر حجر (كل الأسماء موثّقة).
- **طلب متابعة:** طريقة فيلدنكرايس (thk-mfeldenkrais) بلا مدرسة/تيار حي — سُجّلت في agents_specs/missing-schools.md لصالح Task 13.
- **ملاحظة نمطية للمراجعة العامة:** لوحظ نمط نسخ-لصق متطابق حرفياً (thk-shiggins/thk-ellis/thk-ecker كـrelated) في 4 ملفات مختلفة تماماً من دفعات سابقة غير هذه الدفعة أيضاً على الأرجح (ryle, morin, schauer, wells-adrian هنا) — يستحق فحصاً أوسع عبر thk-* الأخرى بنفس القالب في دفعات تالية.

## الملفات
content/ar/thinkers/thk-masson-oursel.md
content/ar/thinkers/thk-mwilliams.md
content/ar/thinkers/thk-philo-alexandria.md
content/ar/thinkers/thk-shenggeler.md
content/ar/thinkers/thk-maslow.md
content/ar/thinkers/thk-meharding.md
content/ar/thinkers/thk-samuels.md
content/ar/thinkers/thk-wquine.md
content/ar/thinkers/thk-zoja.md
content/ar/thinkers/thk-unamuno.md
content/ar/thinkers/thk-wdunn.md
content/ar/thinkers/thk-rwalsh.md
content/ar/thinkers/thk-pappelbaum.md
content/ar/thinkers/thk-tagore.md
content/ar/thinkers/thk-wells-adrian.md
content/ar/thinkers/thk-spillius.md
content/ar/thinkers/thk-wwhite.md
content/ar/thinkers/thk-schauer.md
content/ar/thinkers/thk-ptahhotep.md
content/ar/thinkers/thk-ryle.md
content/ar/thinkers/thk-morin.md
content/ar/thinkers/thk-mfeldenkrais.md
content/ar/thinkers/thk-tjames.md
content/ar/thinkers/thk-tsilvester.md
content/ar/thinkers/thk-shamdasani.md
content/ar/thinkers/thk-nisesilveira.md
