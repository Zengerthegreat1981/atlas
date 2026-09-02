# Task 3.28
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-lholzman..thk-lwalker.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 0 / 35 — كل ملف احتاج تصحيحاً واحداً على الأقل.
- **ازدواج مؤكَّد ثالث في هذه الدفعة: thk-lu-jiuyuan ↔ thk-lu-xiangshan** — نفس الفيلسوف الصيني (لو جيو يوان/لو شيانغ شان) بنفس التواريخ (1139-1193) ونفس المدرسة، بملفين منفصلين.
- **ازدواج مؤكَّد رابع: thk-lluborsky ↔ thk-jluborsky** — نفس الشخص (ليستر لوبورسكي) بأسماء slug مختلفة وتواريخ نشاط متضاربة.
- **تصحيح هوية جوهري: thk-lrosenzweig** — كانت تصف شخصاً مختلفاً تماماً ("Lanette Rosenzweig") بينما مؤسِّسة ART الحقيقية هي "Laney Rosenzweig".
- **خطأ نسبة/خلط أشخاص: thk-lstevenhayes** — كتاب "هدم جدار العار (2010) مع McCurry" غير موجود إطلاقاً؛ خلط بين ستيفن هايز وستيف مكّوري (المصوّر الفوتوغرافي، شخص مختلف كلياً). أيضاً "ACT Made Simple" نُسب له خطأً (فعلياً لراس هاريس).
- **هوية مشكوك فيها بقوة: thk-lwalker** — لا إثبات مستقل لوجود "Laura A. Walker" أو كتابها المزعوم؛ أُعيد كتابة الملف بصيغة تحفظية.
- **خطأ زمني/منطقي فادح: thk-lu-jiuyuan** — كان يزعم أن وانغ يانغ مينغ "أسّس المدرسة مع" لو جيو يوان رغم أن وانغ وُلد بعد وفاة لو بـ280 عاماً.
- **محتوى مختلَق حُذف**: thk-lmazza (نموذج "ARAS" مختلَق، الصحيح نموذج RES)، thk-lindatuhiwai (4 ملاحظات gaps متناقضة كانت تدّعي حذف روابط حقيقية موجودة فعلياً).
- **إزالة روابط محجورة كانت لا تزال ظاهرة رغم اعتراف gaps بحذفها**: thk-lorr (4 روابط محجورة فعلياً منذ 2026-08-26 لكنها بقيت في related الملف المعتمد؛ اكتُشف أيضاً أن EXISTING_SLUGS.md نفسه لا يزال يصنّفها "✅ معتمد" رغم الحجر — خلل في البنية التحتية).
- **أخطاء تواريخ/تعيين مؤسسي**: thk-lowinsky (Pacifica: أستاذة متفرغة خطأ، الصحيح محاضرة مساعدة 1991-1999؛ مجلة خاطئة)، thk-lowith (active_end 1953 خطأ، الصحيح 1964)، thk-lholzman/thk-lhubbard (تصنيفات edges غير موجودة).
- **تصحيح موقع تاريخي**: thk-lu-jiuyuan/thk-lu-xiangshan (مناظرة 1175 كانت في يانشان لا نانتشانغ/مراسلات كما زُعم).
- **نمط false positive في فحص الجنس**: thk-louise-hay وthk-lorange — تُركت الصيغ الصحيحة عمداً.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{lholzman,lhubbard,li-zhi,liang-shuming,lieberman,lifton,lindatuhiwai,lindsay-gibson,linton,lluborsky,lmazza,lmunro,locke,loewald,loewenstein,longchenpa,lopezpedraza,lorange,lorde,lorr,louis-althusser,louise-hay,lowen,lowinsky,lowith,lrice,lrosenzweig,lsaari,lstaples,lstevenhayes,lu-jiuyuan,lu-xiangshan,luijpen,lukacs,lwalker}.md
→ ✅ 34 ملف — مخالفة واحدة فقط (louise-hay) مؤكَّدة false positive وتُركت كما هي.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-lu-jiuyuan ↔ thk-lu-xiangshan** وthk-lluborsky ↔ thk-jluborsky: ازدواجان مؤكدان يحتاجان دمجاً.
- **thk-lrosenzweig**: تصحيح هوية جوهري يحتاج تأكيداً قبل الترقية.
- **thk-lwalker**: يُوصى بنقلها للحجر إن لم يظهر إثبات إضافي.
- **خلل بنيوي في EXISTING_SLUGS.md**: لا يعكس حالة الحجر — الملفات المحجورة لا تزال تظهر "✅ معتمد"، يستحق إصلاحاً على مستوى الأداة نفسها.
- **طلبات تصنيف متعددة**: العلاج الاجتماعي (holzman)، الديانيتكس/السيانتولوجيا (hubbard)، ART (rosenzweig)، Rebirthing (lorr)، تعقيد الصدمة التطورية (lindsay-gibson).

## الملفات
content/ar/thinkers/thk-lholzman.md
content/ar/thinkers/thk-lhubbard.md
content/ar/thinkers/thk-li-zhi.md
content/ar/thinkers/thk-liang-shuming.md
content/ar/thinkers/thk-lieberman.md
content/ar/thinkers/thk-lifton.md
content/ar/thinkers/thk-lindatuhiwai.md
content/ar/thinkers/thk-lindsay-gibson.md
content/ar/thinkers/thk-linton.md
content/ar/thinkers/thk-lluborsky.md
content/ar/thinkers/thk-lmazza.md
content/ar/thinkers/thk-lmunro.md
content/ar/thinkers/thk-locke.md
content/ar/thinkers/thk-loewald.md
content/ar/thinkers/thk-loewenstein.md
content/ar/thinkers/thk-longchenpa.md
content/ar/thinkers/thk-lopezpedraza.md
content/ar/thinkers/thk-lorange.md
content/ar/thinkers/thk-lorde.md
content/ar/thinkers/thk-lorr.md
content/ar/thinkers/thk-louis-althusser.md
content/ar/thinkers/thk-louise-hay.md
content/ar/thinkers/thk-lowen.md
content/ar/thinkers/thk-lowinsky.md
content/ar/thinkers/thk-lowith.md
content/ar/thinkers/thk-lrice.md
content/ar/thinkers/thk-lrosenzweig.md
content/ar/thinkers/thk-lsaari.md
content/ar/thinkers/thk-lstaples.md
content/ar/thinkers/thk-lstevenhayes.md
content/ar/thinkers/thk-lu-jiuyuan.md
content/ar/thinkers/thk-lu-xiangshan.md
content/ar/thinkers/thk-luijpen.md
content/ar/thinkers/thk-lukacs.md
content/ar/thinkers/thk-lwalker.md
