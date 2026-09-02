# Task 2.34
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 31

## الأرقام
جمل القائمة السوداء المتبقية: قبل 13 (مواضع في 10 ملفات، أحدها بتكرار في المتن) → بعد 0
ملفات بلا `## المصادر`: قبل 29 → بعد 0 (31/31، شاملاً الملفين المحجورين اللذين يحيلان لملف الحجر كمصدر)
`edges.belongs_to` بـtarget نص حر بدل slug حقيقي: قبل 8 حالات (7 ملفات) → بعد 0 — تحوّلت لـ`edges: []` أو لـslug صحيح، وسُجّلت 6 مدارس فعلية غائبة في `missing-schools.md`
`related` بعنوان (`title`) متضارب مع عنوان الملف المستهدف: قبل 10 روابط في 9 ملفات → بعد 0
`related` بلا جملة تبرير في المتن (نسخ-لصق من ملفات أخرى): قبل 13 رابطاً في 6 ملفات → بعد 0 (حُذفت)
سنة في المتن بعد `active_end` بلا "بعد وفاته/وفاتها": قبل 3 حالات (thk-peirce، thk-njacobson×2) → بعد 0
`active_end` خاطئ صُحِّح: 2 (thk-radhakrishnan 1961→1975، thk-njacobson 2006→1999 تاريخ وفاته الفعلي)
ملفات محجورة: 2 (thk-rreibo، thk-mdombeck)
ملفات أُعيد كتابتها/صُحِّحت claims مفبركة فيها لأشخاص حقيقيين: 2 (thk-shari-manning، thk-melanie-harned)
preflight_check.py: قبل 12 مخالفة (9 ملفات) → بعد 0 مخالفة على كامل الدفعة (33 ملفاً بعد الحجر)

## أمر التحقق
python3 scripts/task.py verify minimax 2.34
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 (المستهدف 0) | فيها ## المصادر: 31 / 31

python3 scripts/preflight_check.py <قائمة الـ33 ملفاً (31 + 2 محجورين)>
→ ✅ 33 ملف — صفر مخالفات آلية.

## قرارات اتخذتها

### موثّقون فعلاً — تصحيح تقني فقط (حذف جملة القائمة السوداء، إضافة ## المصادر، تصحيح related/edges)
27 ملفاً لشخصيات حقيقية موثّقة تاريخياً أو أكاديمياً: thk-mlinehan (مارشا لينهان، DBT)، thk-shiggins (ستيفن هيغينز، إدارة الطوارئ العلاجية)، thk-su-qin (سو تشين، الدبلوماسية الصينية القديمة)، thk-petrarca (بترارك)، thk-rollnick (ستيفن رولنيك، المقابلة التحفيزية)، thk-meister-eckhart (مايستر إيكهارت)، thk-rkohlen (روبرت كولنبرغ، FAP)، thk-shankara (شانكارا)، thk-rwachtel (بول واتشتِل)، thk-mjones (ماكسويل جونز، المجتمع العلاجي)، thk-tahtawi (رفاعة الطهطاوي)، thk-pepper (ستيفن بِبِر)، thk-zou-yan (زو يان)، thk-ramanuja (رامانوجا)، thk-venriquez (فيرجوليو إنريكيز، Sikolohiyang Pilipino)، thk-oprah-winfrey (أوبرا وينفري)، thk-patanjali (باتانجالي)، thk-mani (ماني)، thk-mencius (منسيوس)، thk-peirce (تشارلز ساندرز بيرس)، thk-madhva (مادهافا)، thk-shang-yang (شانغ يانغ)، thk-njacobson (نيل جاكوبسون)، thk-radhakrishnan (رادهاكريشنان)، thk-werhard (ويرنر إيرهارد)، thk-smorita (شوما موريتا)، thk-wschutz (ويليام شوتز).

من ضمن هذه الدفعة، 7 ملفات كان فيها `edges.belongs_to` أو `related.id` يشير لنص حر بدل slug حقيقي، أو عنوان `related.title` متضارب مع الملف المستهدف الفعلي:
- thk-werhard، thk-smorita، thk-wschutz، thk-oprah-winfrey: `belongs_to` كان يشير لأسماء مدارس بصيغة نص حر (EST/Landmark Forum، علاج موريتا، حركة اللقاء الجماعي، علم النفس الشعبي والصحافة العلمية) — لا يوجد لها ملف `sch-` في الأطلس. حُذف الرابط (`edges: []`) وسُجّلت الأربعة في `missing-schools.md`.
- thk-pepper: `belongs_to` كان يشير خطأً لمدرسة الظاهراتية الوجودية (هوسرل/بينسفانغر/بوس) رغم أن بِبِر (فيلسوف سياقية أمريكي) لا صلة موثّقة له بها — حُذف الرابط الخاطئ، وسُجّلت "السياقية الفلسفية الأمريكية" في `missing-schools.md`. حُذفت أيضاً 7 روابط `related` (كاسيرر، جيمس، ديوي، كالكينز، شيلر، مونستربرغ، تيتشنر) لعدم وجود جملة في المتن تبرر صلتهم المباشرة.
- thk-rwachtel: أحد belongs_to لنص حر ("العلاج التكاملي" عام) حُذف وسُجّل في missing-schools.md؛ الآخر ("التحليل النفسي الدوري") حُوّل لـslug صحيح `br-cyclical-psychodynamics`. حُذفت 5 روابط related غير مبرَّرة في المتن (لوين، ستروب، نوركروس، لوبورسكي، ليدز).
- thk-rollnick: `co-developed` تحوّل من نص حر إلى `tec-motivational-interviewing`؛ حُذفت 5 روابط related (br-psychodynamic-humanistic، أساجيولي، دابروفسكي، فاريلي، ليبرمان) لعدم وجود تبرير في المتن.
- thk-petrarca، thk-peirce: `founded` كان يكرر اسم المدرسة كنص حر بدل الإحالة لنفس الـslug المستخدم في `belongs_to` — صُحِّح لـslug فعلي (`sch-renaissance-humanism`، `sch-pragmatism-classical`).
- thk-mjones: `developed` تحوّل من نص حر ("العلاج البيئي المؤسسي") إلى `tec-milieu-therapy`.
- عناوين `related.title` متضاربة صُحِّحت في: thk-mlinehan (tec-dbt-specialized)، thk-shiggins وthk-rkohlen وthk-njacobson (thk-fskinner/tec-behavioral-activation)، thk-tahtawi (ctx-arabic-nahda وsch-arab-renaissance)، thk-mani (sch-gnosticism)، thk-mencius (thk-confucius وthk-xunzi)، thk-peirce (thk-james)، thk-wschutz (tec-encounter-groups)، thk-zou-yan (sch-yinyang)، thk-radhakrishnan (thk-vivekananda).
- thk-shiggins وthk-njacobson: حُذفت روابط related (thk-dmeichenbaum، thk-kelly-george، thk-resick) لا تبرير لها في المتن، رغم وجود الملفات المستهدفة فعلياً — النسخ-لصق من ملفات أخرى هو المشكلة لا الوجود.
- thk-venriquez: 5 روابط related كانت مذكورة في `gaps` كـ"مُزالة" لكنها لم تكن فعلاً محذوفة من `related` — نفّذت الحذف الفعلي ليتطابق المتن مع ما يعلنه.
- thk-radhakrishnan: صُحِّح `active_end` من 1961 إلى 1975 (سنة وفاته) لأن المتن يذكر رئاسته للهند حتى 1967.
- thk-njacobson: صُحِّح `active_end` من 2006 إلى 1999 (تاريخ وفاته الفعلي)، وصُححت `dates` (1950–[غير مؤكد] → 1949–1999)، وأُضيفت إشارات "بعد وفاته" قرب سنتَي 2021 و2001 المذكورتين في المتن (وصُحِّح خطأ سنة نشر ثانوي: الكتاب المذكور هو *Acceptance and Change in Couple Therapy* 1998 لا 2001).
- thk-oprah-winfrey: preflight أظهر تحذير جنس نحوي **كاذب** (false positive على كلمة "عالم" داخل "والعالم" و"طبيب" داخل وصف بروس بيري، لا أوبرا نفسها) — أُعيدت صياغة الجملتين بلا تغيير في المعنى، والعناوين المؤنثة (`## أهم أعمالها`، `## موقعها من التيار`) كانت **صحيحة أصلاً**.

### موثّقون — لكن المتن كان يحتوي على ادعاءات مفبركة، أُعيد كتابته
- **thk-shari-manning** (شاري مانينغ): شخصية حقيقية (معالجة DBT، رئيسة تنفيذية سابقة لـTreatment Implementation Collaborative، مؤلفة *Loving Someone with Borderline Personality Disorder*, 2011)، لكن النسخة السابقة نسبت لها تطوير بروتوكول DBT-A عام 1995 ومنصباً أكاديمياً في جامعة ماساتشوستس وأرقام إحصائية (50-70%) — كلها غير موثّقة. مطوّرا DBT-A الموثّقان فعلياً هما أليك ميلر وجيل راثوس. أُعيد كتابة الملف بالكامل بمصادر حقيقية فقط.
- **thk-melanie-harned** (ميلاني هارنِد): شخصية حقيقية (باحثة DBT-PE، جامعة واشنطن)، لكن النسخة السابقة ذكرت أرقام تجربة Harned et al. 2014 بدقة غير موثّقة (101 مريض، 73%/36%/92%) وادّعاء اعتماد دولي من APA/NICE/ISTSS بلا مصدر. حُذفت الأرقام والادعاء، وأُبقي على وصف عام موثَّق للتجربة مع الاستشهاد المرجعي الصحيح (Harned, Korslund & Linehan, 2014, *Behaviour Research and Therapy*).

### غير موجودين — حجر
- **thk-rreibo** (المزعوم "ريتشارد ريبو"): حقل `en` نفسه يخلط بين ثلاث هويات (Richard J. Reynolds / T. Taizan Maezumi / Rev. Daitsu Tom Wright)، والمتن الأصلي ينسب لهذا "الشخص" أعمالاً وسيرة موثّقة فعلياً لديفيد ك. رينولدز (مؤسس Constructive Living الحقيقي، موجود بالفعل في الأطلس كـ`thk-dreynolds` ومذكور في نفس ملف rreibo كـrelated) وتايزان مايزومي روشي. لا دليل مستقل على وجود شخص باسم "ريتشارد ريبو". النسخة الأصلية محفوظة في `agents_specs/quarantine-minimax-archive/thk-rreibo.md.archived.2026-08-27`.
- **thk-mdombeck**: المتن الأصلي لم يكن سيرة بل مذكرة تحقيق ذاتية تعترف بتضارب بين الـslug المسجَّل سابقاً ("mark-santross") والاسم الوارد (Mark R. Dombeck)، وتنسب له مساهمات محددة في "تطوير مناهج PCIT الجامعية" بلا مصدر أولي — المؤسِّسة الموثّقة لـPCIT هي شيلا أيبرغ. النسخة الأصلية محفوظة في `agents_specs/quarantine-minimax-archive/thk-mdombeck.md.archived.2026-08-27`.

### غامض
لا يوجد. كل الـ31 ملفاً حُسم قرارها بشكل قاطع (موثّق مع تصحيح/إعادة كتابة، أو محجور) — لم يظهر في هذه الدفعة اسم يحتاج تُرِك "زي ما هو" بحالة شك حقيقي غير محسوم.

## متوقف عنده (لرئيس التحرير)
- لا يوجد.

## الملفات
content/ar/thinkers/thk-mlinehan.md
content/ar/thinkers/thk-shiggins.md
content/ar/thinkers/thk-werhard.md
content/ar/thinkers/thk-smorita.md
content/ar/thinkers/thk-rreibo.md
content/ar/thinkers/thk-su-qin.md
content/ar/thinkers/thk-mdombeck.md
content/ar/thinkers/thk-wschutz.md
content/ar/thinkers/thk-petrarca.md
content/ar/thinkers/thk-rollnick.md
content/ar/thinkers/thk-meister-eckhart.md
content/ar/thinkers/thk-rkohlen.md
content/ar/thinkers/thk-shankara.md
content/ar/thinkers/thk-rwachtel.md
content/ar/thinkers/thk-mjones.md
content/ar/thinkers/thk-shari-manning.md
content/ar/thinkers/thk-tahtawi.md
content/ar/thinkers/thk-pepper.md
content/ar/thinkers/thk-zou-yan.md
content/ar/thinkers/thk-ramanuja.md
content/ar/thinkers/thk-venriquez.md
content/ar/thinkers/thk-oprah-winfrey.md
content/ar/thinkers/thk-patanjali.md
content/ar/thinkers/thk-mani.md
content/ar/thinkers/thk-mencius.md
content/ar/thinkers/thk-peirce.md
content/ar/thinkers/thk-madhva.md
content/ar/thinkers/thk-melanie-harned.md
content/ar/thinkers/thk-shang-yang.md
content/ar/thinkers/thk-njacobson.md
content/ar/thinkers/thk-radhakrishnan.md
