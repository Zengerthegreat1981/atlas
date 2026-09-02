# Task 3.23
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-jnicolosi..thk-jrotter.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 0 / 35 — كل ملف احتاج تصحيحاً واحداً على الأقل.
- **أخطر اكتشاف: thk-jon-ronson** — تفبرك متعدد المصادر: مكان ميلاد خاطئ، شخصيات كتاب *Them* مختلَقة بالكامل، كتاب "لوسيفر إيفيكت" منسوب خطأً له (فعلياً لفيليب زيمباردو)، كتاب "Dark Medicine" غير موجود إطلاقاً، وعناوين حلقات بودكاست مختلَقة. أُعيد كتابة قسم "ما أعطاه" بالكامل. **يستحق مراجعة العملية التي أنتجت الملف أصلاً بحثاً عن أنماط مشابهة.**
- **حجر صحي جديد: thk-jramiro** — الملف نفسه كان يحمل تحذير تحقّق سابق (لا أثر للشخص أو كتابه، أسماء متضاربة). أُضيف للحجر رسمياً.
- **تعارض هوية محتمل جديد: thk-jonathanbaylin ↔ thk-jbaylin** — يبدو نفس الشخص (جون بايلين، مؤلف مشارك لـ*Brain-Based Parenting* مع دانييل هيوز)، وثبت أن thk-jonathanbaylin ينسب الكتاب لمؤلف مختلَق ("هوزيتون") ويستخدم عنوان كتاب 2016 خاطئاً بمؤلف مختلَق آخر ("سبنسر"). سُجِّل طلب حسم صريح.
- **وفاة حديثة غير مسجلة: thk-john-searle** — توفي فعلياً 17 سبتمبر 2025، الملف كان يذكره حياً.
- **خطأ هوية/تاريخ جوهري: thk-johnshlien** — الملف كان يذكره "1928–" موحياً بأنه حيّ، لكن الصحيح مواليد 1918 ووفاته 2002 (فارق 10 سنوات في الميلاد).
- **نمط "gaps تدّعي حذف رابط لسه موجود" مؤكَّد كنمط متكرر واسع النطاق (3 من 5 ملفات في مجموعة واحدة فقط)**: thk-josephtrimble، thk-jpatterson (رابط محجور فعلياً `thk-brosen`)، thk-jpennebaker (رابط محجور `thk-jbrowne`)، thk-john-braithwaite (4 روابط، 3 منها محجورة فعلياً — الملف المعتمد الحالي لا يزال يحملها). **يستحق فحصاً آلياً شاملاً يقارن `related` بجمل `gaps` ذات صيغة "أُزيل/حُذف" عبر كل الأطلس.**
- **نمط false positive رابع/خامس في فحص الجنس**: thk-jordan (جوديث جوردان) — تُركت الصيغة المؤنثة الصحيحة عمداً.
- **تأكيد شخصين مختلفين لا ازدواج**: thk-jordan-peterson (جوردان بيترسون) وthk-jordan (جوديث جوردان) — لا علاقة، فُحص بعناية بناءً على تنبيه مسبق.
- **أخطاء نسبة أخرى**: thk-john-maxwell ("قانون الاحتضان" باسم إنجليزي مكرر خاطئ)، thk-jpotter (روابط بلا سبب أُصلحت بإضافة سياق DARG الحقيقي).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً هذه الدفعة (johann-gottfried-herder→sch-romanticism، john-braithwaite→br-restorative-justice، john-philoponus→br-neoplatonism-alexandrian، johnshlien→br-person-centered، jpotter→br-discursive-psychology، jose-carlos-mariategui، joseph-barber→sch-ericksonian-hypnosis، jrosenberg→br-ibp، jordan→br-relational-cultural). حالات كثيرة بلا slug مطابق (jnicolosi، jnorcross [تكاملي]، johann-hari، john-bradshaw، john-gray، john-maxwell، john-searle [فلسفة عقل تحليلية]، jordan-peterson، joseph-murphy، jonahlewis [صحافة علمية شعبية]، josselson [بحث سردي]، jpennebaker→sch-writing-therapy، jon-ronson) أُفرغت مع تسجيل طلبات — **تراكم واضح لفجوة "علم النفس الشعبي المعاصر" عبر أكثر من 6 ملفات في هذه الدفعة وحدها**.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{jnicolosi,jnorcross,johann-gottfried-herder,johann-hari,john-bradshaw,john-braithwaite,john-cacioppo,john-damascene,john-gray,john-maxwell,john-philoponus,john-searle,johnmcintosh,johnshlien,jon-ronson,jonahlewis,jonas,jonathan-haidt,jonathanbaylin,jones,jordan-peterson,jordan,jose-carlos-mariategui,joseph-barber,joseph-murphy,josephtrimble,josselson,jparrh,jpatterson,jpennebaker,jpotter,jrathus,jrosenberg,jrotter}.md
→ ✅ 34 ملف — مخالفة واحدة فقط (jordan) مؤكَّدة false positive وتُركت كما هي.
thk-jramiro حُجر بدل كتابة مسودة.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-jon-ronson**: تفبرك متعدد المصادر — يستحق فحص العملية الأصلية بحثاً عن أنماط مشابهة، أولوية عالية.
- **thk-jramiro**: مرشح قوي للسحب النهائي.
- **thk-jonathanbaylin ↔ thk-jbaylin**: تعارض هوية محتمل مع تفاصيل مختلَقة في أحدهما — يحتاج حسماً.
- **thk-john-searle**: تصحيح وفاته (سبتمبر 2025) أولوية عالية.
- **thk-johnshlien**: تصحيح تواريخه (1918-2002 لا "1928-") أولوية عالية.
- **نمط "gaps تدّعي حذف رابط لسه موجود"**: مؤكَّد الآن كمشكلة نظامية واسعة النطاق (وليس حالات معزولة) — يستحق أداة فحص آلية مخصصة قبل الاستمرار في الاكتشاف اليدوي المتناثر.
- **فجوة "علم النفس الشعبي المعاصر"**: تراكم حاد (6+ ملفات هذه الدفعة وحدها) — يستحق إنشاء slug واحد موحَّد بدل التكرار.
- **thk-john-braithwaite**: الملف المعتمد الحالي لا يزال يحمل روابط لملفات محجورة فعلياً — خطأ إنتاج قائم يستحق ترقية سريعة.

## الملفات
content/ar/thinkers/thk-jnicolosi.md
content/ar/thinkers/thk-jnorcross.md
content/ar/thinkers/thk-johann-gottfried-herder.md
content/ar/thinkers/thk-johann-hari.md
content/ar/thinkers/thk-john-bradshaw.md
content/ar/thinkers/thk-john-braithwaite.md
content/ar/thinkers/thk-john-cacioppo.md
content/ar/thinkers/thk-john-damascene.md
content/ar/thinkers/thk-john-gray.md
content/ar/thinkers/thk-john-maxwell.md
content/ar/thinkers/thk-john-philoponus.md
content/ar/thinkers/thk-john-searle.md
content/ar/thinkers/thk-johnmcintosh.md
content/ar/thinkers/thk-johnshlien.md
content/ar/thinkers/thk-jon-ronson.md
content/ar/thinkers/thk-jonahlewis.md
content/ar/thinkers/thk-jonas.md
content/ar/thinkers/thk-jonathan-haidt.md
content/ar/thinkers/thk-jonathanbaylin.md
content/ar/thinkers/thk-jones.md
content/ar/thinkers/thk-jordan-peterson.md
content/ar/thinkers/thk-jordan.md
content/ar/thinkers/thk-jose-carlos-mariategui.md
content/ar/thinkers/thk-joseph-barber.md
content/ar/thinkers/thk-joseph-murphy.md
content/ar/thinkers/thk-josephtrimble.md
content/ar/thinkers/thk-josselson.md
content/ar/thinkers/thk-jparrh.md
content/ar/thinkers/thk-jpatterson.md
content/ar/thinkers/thk-jpennebaker.md
content/ar/thinkers/thk-jpotter.md
content/ar/thinkers/thk-jramiro.md
content/ar/thinkers/thk-jrathus.md
content/ar/thinkers/thk-jrosenberg.md
content/ar/thinkers/thk-jrotter.md
