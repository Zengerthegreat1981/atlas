# Task 2.31
الحالة: مكتمل
العملية: تحقق وجود 26 مفكراً مشكوكاً فيهم (thk-m→thk-s) وتطبيق واحد من ثلاث نتائج: موثّق / غير موجود / غامض | الملفات: 26

## الأرقام
جمل القائمة السوداء متبقية: قبل 24 → بعد 0 (task.py verify)
سقّالة ظاهرة متبقية: 0
ملفات فيها ## المصادر: 24 / 26 (الاثنان الباقيان ملفا حجر بلا سيرة تُوثَّق)
preflight_check.py: قبل 6 مخالفات → بعد 0 مخالفات

## أمر التحقق
`python3 scripts/task.py verify minimax 2.31` → جمل القائمة السوداء متبقية: 0 | سقّالة ظاهرة متبقية: 0 | فيها ## المصادر: 24 / 26
`python3 scripts/preflight_check.py --report agents_specs/reports/minimax/T2/task-2.31.md` → ✅ 26 ملف — صفر مخالفات آلية

## قرارات اتخذتها
- thk-mccullough: موثّق (James P. McCullough Jr., VCU، مؤسس CBASP) — أُعيد كتابته بمصادر حقيقية (VCU faculty page، CBASP.org، الكتاب المرجعي 2000). أُزيل ادعاء "تعارض هوية" الخاطئ من gaps (لا تعارض فعلياً بين title وen).
- thk-nkrumah: موثّق (كوامي نكروما، أول رئيس لغانا) — تنظيف قائمة سوداء + مصادر (Birmingham 1998، أعماله الأصلية).
- thk-savarkar: موثّق (V. D. Savarkar، صاحب مصطلح Hindutva) — تنظيف + مصادر (Keer 1966، Bakhle 2010) + تصحيح سنتين بعد وفاته (1980، 1992) بإضافة "بعد وفاته".
- thk-nussbaum: موثّق (مارثا نوسباوم، جامعة شيكاغو) — تنظيف + مصادر.
- thk-wdoherty: موثّق (William J. Doherty، مؤسس Discernment Counseling، جامعة مينيسوتا) — صُحّح edges.belongs_to من نص حر إلى br-discernment-counseling الحقيقي؛ أُعيد رابط ستيفن هاريس (مؤلف مشارك موثّق فعلياً) وأُزيلت أربعة روابط غير موثّقة الصلة المباشرة رغم وجود ملفاتها.
- thk-tillich: موثّق (بول تيليش) — أُضيف ## المصادر (كان الملف بلا قسم مصادر رغم وجود اقتباس).
- thk-schultz-hencke: موثّق (Harald Schultz-Hencke، له مدخل Wikipedia) — صُحّح edges.belongs_to إلى br-schultz-hencke الحقيقي + مصادر (Cocks 1985 عن معهد غورينغ).
- thk-mchace: موثّق (Marian Chace، مؤسسة DMT الأمريكية، وثّقتها ADTA) — لا توجد مدرسة/تيار بصيغة slug لـ«العلاج بالحركة والرقص» في الأطلس فأُفرغ edges (تُسجَّل في missing-schools.md)، أُزيلت 3 روابط غير موثقة الصلة، أُضيفت مصادر.
- thk-zehr: موثّق (Howard Zehr، «الأب الروحي» للعدالة التصالحية) — صُحّح edges إلى br-restorative-justice + مصادر.
- thk-rmenakem: موثّق (Resmaa Menakem، مؤلف My Grandmother's Hands) — صُحّح edges إلى sch-polyvagal-informed-therapy + مصادر + أُعيدت صياغة gap عن سنة الميلاد بحيث تسمّي فجوة لا تؤكد حقيقة.
- thk-mbembe: موثّق (Achille Mbembe) — تنظيف + مصادر.
- thk-mwagreich: **غير موجود** — لم يُعثر على أي دليل مستقل على "Moris H. Wagreich" في التنويم التحليلي؛ الأسماء الموثّقة (Brenman، Gill) مختلفة تماماً. النسخة الأصلية نُقلت لـ quarantine-minimax-archive، والملف الحي حُوّل لقالب حجر موحّد، وسُجّل في quarantine-minimax.md.
- thk-maimonides: موثّق (ابن ميمون) — صُححت عناوين ابن رشد والفارابي في related لتطابق عناوين ملفاتهم الفعلية حرفياً + مصادر.
- thk-nasir-khusraw: موثّق (ناصر خسرو) — أُضيفت مصادر (Hunsberger 2000، Encyclopaedia Iranica).
- thk-maximus-confessor: موثّق (مكسيموس المعترف) — أُضيفت مصادر (Louth 1996، Blowers 2016).
- thk-seyberg: موثّق لكن بهوية خاطئة — **أُعيد كتابته بالكامل**: الشخص الفعلي الموثّق هو شيلا إم. إيبِرغ (Sheila M. Eyberg، مؤسِّسة PCIT وECBI)، لا "Steven M. Eyberg" المتزوج من "Shirley Eyberg" كما في النسخة السابقة — لم يُعثر على أي دليل لوجود هذين الاسمين. صُحّح الجنس النحوي بالكامل في العناوين والمتن.
- thk-mperelman: موثّق (Michael A. Perelman، Weill Cornell) — صُحّح edges إلى br-sex-therapy + مصادر.
- thk-rice: موثّق لكن بهوية خاطئة — **أُعيد كتابته بالكامل**: الشخص الفعلي هو لورا إن. رايس (Laura N. Rice، جامعة يورك، تلميذة روجرز، شريكة غرينبرغ)، لا "Robert E. Rice" (مذكَّر) كما في النسخة السابقة. صُحّح الجنس النحوي، وصُحّح edges/related لاستخدام slugs حقيقية (tec-process-experiential بدل نص حر) وعنوان مطابق لعنوان الملف الفعلي.
- thk-said: موثّق (إدوارد سعيد) — تنظيف + مصادر.
- thk-rawls: موثّق (جون رولز) — تنظيف + مصادر.
- thk-ptedeschi: **غير موجود** — لم يُعثر على دليل لـ"Raphael G. Tedeschi" في الاستشارات متعددة الثقافات؛ الاسم الأقرب الموثَّق فعلياً (Richard G. Tedeschi) باحث في النمو ما بعد الصدمة، مجال مختلف تماماً — يرجّح اختلاق/خلط هوية. حُجر بنفس آلية mwagreich.
- thk-senghor: موثّق (ليوبولد سنغور) — تنظيف + مصادر.
- thk-mignolo: موثّق (Walter Mignolo) — تنظيف + مصادر (حُذف ادعاء غير موثّق عن تأثيره في BDS).
- thk-pwehman: موثّق (Paul Wehman، VCU، رائد التوظيف المدعوم) — صُحّح edges إلى br-psychiatric-vocational-rehab + مصادر + أُزيل رابط غير موثّق الصلة.
- thk-sri-aurobindo: موثّق (شري أوروبندو) — تنظيف + مصادر + تصحيح سنتين بعد وفاته (1951، 1968) بإضافة "بعد وفاته" وتصحيح نسبة تأسيس أوروفيل لميرا ألفاسا لا له مباشرة.
- thk-mir-damad: موثّق (ميرداماد، مؤسس مدرسة أصفهان) — أُضيفت مصادر (Corbin، Rizvi، Encyclopaedia Iranica).

## متوقف عنده (لرئيس التحرير)
- thk-mchace: لا توجد مدرسة/تيار بصيغة slug لـ«العلاج بالحركة والرقص (DMT)» — سُجّلت في missing-schools.md، تحتاج كتابة سياقة عبر Task 13.
- روابط داخلية سابقة (thk-ieyberg، thk-erikpearson، thk-jacqueline-peart، thk-nancy-harness، thk-tom-cornwell، thk-bill-matthews، thk-jenniferschwab، thk-kathylaurenceau، thk-timothyclanton، thk-lfish، thk-daniellevision، thk-mary-whitehouse، thk-susan-koch، thk-jlueger) أُزيلت من related الملفات المصحَّحة لعدم توثيق الصلة المباشرة من مصدر أولي في هذه الدفعة، رغم أن ملفاتها موجودة فعلياً في الأطلس — قد تحتاج مراجعة قرائية منفصلة (Task 3) لتحديد إن كانت صلاتها الأصلية صحيحة.
- ملفان محجوران (thk-mwagreich، thk-ptedeschi) قد يكون لهما روابط واردة (inbound links) من ملفات أخرى لم تُفحص في هذه الدفعة — تحتاج بحثاً منفصلاً عن `id: "thk-mwagreich"` و`id: "thk-ptedeschi"` عبر الأطلس.

## الملفات
content/ar/thinkers/thk-mccullough.md
content/ar/thinkers/thk-nkrumah.md
content/ar/thinkers/thk-savarkar.md
content/ar/thinkers/thk-nussbaum.md
content/ar/thinkers/thk-wdoherty.md
content/ar/thinkers/thk-tillich.md
content/ar/thinkers/thk-schultz-hencke.md
content/ar/thinkers/thk-mchace.md
content/ar/thinkers/thk-zehr.md
content/ar/thinkers/thk-rmenakem.md
content/ar/thinkers/thk-mbembe.md
content/ar/thinkers/thk-mwagreich.md
content/ar/thinkers/thk-maimonides.md
content/ar/thinkers/thk-nasir-khusraw.md
content/ar/thinkers/thk-maximus-confessor.md
content/ar/thinkers/thk-seyberg.md
content/ar/thinkers/thk-mperelman.md
content/ar/thinkers/thk-rice.md
content/ar/thinkers/thk-said.md
content/ar/thinkers/thk-rawls.md
content/ar/thinkers/thk-ptedeschi.md
content/ar/thinkers/thk-senghor.md
content/ar/thinkers/thk-mignolo.md
content/ar/thinkers/thk-pwehman.md
content/ar/thinkers/thk-sri-aurobindo.md
content/ar/thinkers/thk-mir-damad.md
