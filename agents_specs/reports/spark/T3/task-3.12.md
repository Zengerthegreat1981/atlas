# Task 3.12
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-elaine-aron..thk-fain.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 2 / 35 (thk-emerson، thk-ellis)
- **أخطر اكتشاف: thk-elaine-aron** — 3 روابط `related` (thk-husserl، thk-sartre، wrk-aron-opium-of-intellectuals) كانت تخص فعلياً **ريمون آرون** الفيلسوف الفرنسي، خُلطت بسبب تطابق اللقب فقط مع إلين ن. آرون (باحثة الحساسية العالية) — لا صلة إطلاقاً. حُذفت الثلاثة.
- **رابط id/title متضارب جوهري: thk-elifellows** — العنوان الحقيقي للشخص "جوزيف إل. وايت الابن" (أب علم النفس الأسود، 1932–2017) وليس "إلي فيلوز" أو "جوزيف إيه. وايت" — صُحح الاسم الأوسط (A.→L.) في `title/en/crumb` والمتن، وصُححت 4 روابط id/title متضاربة أخرى (ستيف بيكو، فرانتز فانون، سنغور، جوزيف غون). **قرار حساس**: هل الـslug نفسه (`thk-elifellows`) يستحق إعادة تسمية لاحقاً.
- **وفاتان/تواريخ غير مسجلة بدقة اكتُشفتا ببحث خارجي**: `thk-eugenetaylor` (وفاته 2018 خطأ → الصحيح 2013)، `thk-epolster` (1928–2019 خطأ → الصحيح 1922–2024)، `thk-ewolf` (وفاته 2016 خطأ → الصحيح 2018)، `thk-fain` (ميشيل فان: تواريخ متضاربة 1919-2008/1917-2003 كلاهما خطأ → الصحيح 1917–2007).
- **تصنيف بنيوي متناقض داخلياً**: `thk-empedocles` — الملف المعتمد نفسه يصف أنباذوقليس كـ"تعدُّدي" في المتن بينما `edges.belongs_to` يصنّفه تحت المدرسة الإيلية (تناقض) — لا slug تعدُّدي موجود، فأُفرغ `edges` وسُجِّل طلب `sch-presocratic-pluralism`.
- **رابط بمعرّف خاطئ لشخص آخر تماماً**: `thk-erasmus` كان يربط `thk-tmoore` بعنوان "توماس مور" (السير الإنجليزي 1478-1535) بينما الـslug فعلياً يخص توماس مور المعاصر (مواليد 1946، تلميذ هيلمان) — حُذف، أُبقي فقط `thk-thomas-more` الصحيح.
- **حالة "غامضة" حقيقية**: `thk-esaebel` — بحث خارجي لم يجد أي أثر للشخص في أدبيات DBT لاضطرابات الأكل رغم أن الملف المعتمد كتب سيرة واثقة (والـgaps نفسها كانت تحذّر من عدم التحقق — تناقض داخلي). أُعيد كتابة المتن ليصرّح بالغموض بدل سيرة واثقة، وأُفرغت edges/related بالكامل. **قرار حساس يحتاج حسماً من رئيس التحرير**.
- **نمط "gaps تدّعي حذف رابط لسه موجود" استمر**: thk-emilecoue (4 روابط محجورة)، thk-eschopler (4 روابط)، thk-eugenetaylor (روابط غير موثقة)، thk-ereichelt (thk-cwhitaker-pt محجور).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير من الملفات (تفاصيل في تقارير الفرق) — منها emaroda→br-embodied-relational-therapy، emilecoue→tec-self-hypnosis-progressive، elaszlo→sch-general-systems-theory، ethompson→br-embodied-cognition-therapy، eschopler→br-teacch، ereichelt→br-teacch. حالات بلا slug مطابق (elaine-aron، esther-perel، erickson-erl [مسودة sch-ericksonian-hypnosis]، eschein) أُفرغت مع تسجيل طلبات جديدة، من ضمنها `sch-social-psychiatry-argentina` (بيتشون-ريفيير) و`sch-sensory-processing-sensitivity` و`sch-forensic-cognitive-psychology`.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 20 ملفاً من هذه الدفعة (النمط الأشيع: "لا يوجد اقتباس مباشر موثوق متاح").

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{elaine-aron,elaszlo,elifellows,elizabeth-loftus,emaroda,emilecoue,emmons,empedocles,engels,enidbalint,enrique-dussel,epichon,epicur,epierrakos,epolster,erasmus,ereich,ereichelt,erickson-erl,erigena,erikson,esaebel,eschein,eschopler,esther-perel,ethompson,eugenetaylor,everettshostrom,ewolf,ey,fabry,fahrenberg,fain}.md
→ ✅ 33 ملف — صفر مخالفات آلية (thk-emerson وthk-ellis سليمان تماماً، بلا مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإصلاح تسلسل تواريخ (إضافة "بعد وفاته/ها" صراحة).

## متوقف عنده (لرئيس التحرير)
- **thk-esaebel**: حالة غموض حقيقي يحتاج حسماً — هل يُنقل لـquarantine-spark.md أم يبقى "ambiguous"؟
- **thk-elifellows**: الـslug نفسه دلالياً غير مرتبط باسم الشخص الحقيقي (جوزيف وايت) — قد يستحق إعادة تسمية.
- **thk-elaine-aron ↔ ريمون آرون**: يستحق فحص ملف ريمون آرون نفسه للتأكد من عدم وجود تلوث عكسي.
- **thk-epierrakos/thk-ereich**: `edges.belongs_to → sch-somatic-experiencing` غير دقيق تاريخياً (SE أُنشئت لاحقاً بعقود) — نمط موجود في عنقود كامل (بما فيه الملف المعتمد thk-pierrakos نفسه) يحتاج قراراً تحريرياً شاملاً وليس ملفاً بملف.
- **thk-fkfu وthk-jroddy**: ملفان بمحتوى مفبرك بالكامل ("[بيانات غير متاحة]") اكتُشفا كروابط في thk-ereichelt — يستحقان تسجيلاً مباشراً في quarantine-spark.md.
- **نمط "gaps تدّعي حذف رابط لسه موجود"**: متكرر بشدة عبر عدة دفعات الآن — يستحق فحصاً آلياً شاملاً بدل الاكتشاف اليدوي المتناثر.

## الملفات
content/ar/thinkers/thk-elaine-aron.md
content/ar/thinkers/thk-elaszlo.md
content/ar/thinkers/thk-elifellows.md
content/ar/thinkers/thk-elizabeth-loftus.md
content/ar/thinkers/thk-ellis.md
content/ar/thinkers/thk-emaroda.md
content/ar/thinkers/thk-emerson.md
content/ar/thinkers/thk-emilecoue.md
content/ar/thinkers/thk-emmons.md
content/ar/thinkers/thk-empedocles.md
content/ar/thinkers/thk-engels.md
content/ar/thinkers/thk-enidbalint.md
content/ar/thinkers/thk-enrique-dussel.md
content/ar/thinkers/thk-epichon.md
content/ar/thinkers/thk-epicur.md
content/ar/thinkers/thk-epierrakos.md
content/ar/thinkers/thk-epolster.md
content/ar/thinkers/thk-erasmus.md
content/ar/thinkers/thk-ereich.md
content/ar/thinkers/thk-ereichelt.md
content/ar/thinkers/thk-erickson-erl.md
content/ar/thinkers/thk-erigena.md
content/ar/thinkers/thk-erikson.md
content/ar/thinkers/thk-esaebel.md
content/ar/thinkers/thk-eschein.md
content/ar/thinkers/thk-eschopler.md
content/ar/thinkers/thk-esther-perel.md
content/ar/thinkers/thk-ethompson.md
content/ar/thinkers/thk-eugenetaylor.md
content/ar/thinkers/thk-everettshostrom.md
content/ar/thinkers/thk-ewolf.md
content/ar/thinkers/thk-ey.md
content/ar/thinkers/thk-fabry.md
content/ar/thinkers/thk-fahrenberg.md
content/ar/thinkers/thk-fain.md
