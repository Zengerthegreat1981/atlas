# Task 3.14
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ8 subagent متوازي (فرويد أُفرد له subagent مستقل لحساسيته وثقل شبكته، والباقي في 7 مجموعات من 4-6 ملفات). دفعة تحتوي شخصيات مؤسِّسة كبرى (فرويد، فروم، فرانكل، سكينر، غاندي، غاليليو).

## الأرقام
- ملفات سليمة تماماً بلا أي خطأ (بلا مسودة): 0 / 35 — كل ملف احتاج تصحيحاً واحداً على الأقل، معظمها فقط جملة القائمة السوداء.
- **حجر صحي جديد: thk-fvanderzee** — لا أثر لباحث بهذا الاسم في أدبيات علم النفس الإيجابي العابر للثقافات، ولا لكتابه المزعوم *Handbook of Asian Positive Psychology* ولا للأسماء الثلاثة المرتبطة به. سُجِّل في `quarantine-spark.md`، لم تُكتب مسودة.
- **thk-freud**: تقليم جذري لشبكة `related` من 27 رابطاً إلى 3 فقط (الوحيدة المبررة صراحة بالمتن: بروير، فيرينتزي، رانك) — قرار حساس جداً يحتاج حسم رئيس التحرير (هل يُبقى التقليم أم تُوسَّع المقالة لتبرير روابط تاريخية مهمة مثل جمعية الأربعاء 1902؟).
- **هوية مفبركة/خلط جنس خطير: thk-gary-wells** — "جيمس ديسارت" (رجل) مختلَق؛ الشخص الحقيقي **جينيفر ديسارت** (امرأة)، و"إيمي برادلين" غير قابلة للتحقق إطلاقاً — حُذفت. أيضاً خلط بين جامعة آيوا وجامعة ولاية آيوا (مؤسستان مختلفتان)، وحُذف اقتباس غير مسنَد بالكامل.
- **نسبة خاطئة جوهرية: thk-frankanderson** — كان يُنسب له "تأسيس" معهد IFS، بينما المؤسس الحقيقي ريتشارد شوارتز وأندرسون مدرّب أول فقط.
- **نسبة خاطئة: thk-frederickleong** — جامعة خاطئة (ميشيغان بدل ولاية ميشيغان)، و3 روابط related بلا أي علاقة موثقة حُذفت.
- **أخطاء جغرافيا/هوية**: thk-francisco-de-vitoria (سلامنكا كانت مسجَّلة كدولة، ومكان ميلاده الحقيقي برغش لا سلامنكا)، thk-fkeller (سبق).
- **تصنيف بنيوي خاطئ متكرر (النمط المكتشف في 3.13 استمر هنا)**: thk-gaos كان مصنَّفاً تحت `sch-existential-therapy` (مدرسة علاجية) رغم كونه فيلسوفاً لا معالجاً — صُحح إلى `sch-existentialism`.
- **ملف مكرر مؤكَّد: thk-francesharville ↔ thk-francine-shapiro** — كلاهما يصف نفس الشخص (فرانسين شابيرو، مؤسسة EMDR)، وthk-francesharville كان حتى يحمل بقايا خطأ جنس ("فرانسيس" بدل "فرانسين") في `crumb`. يحتاج قرار دمج.
- **أخطاء تواريخ**: thk-frankl (كتابان: تاريخ نشر ألماني أصلي مقابل الترجمة الإنجليزية خُلط في كليهما)، thk-gaos (فترة عمادته 1936-1939 خطأ، الصحيح 1936-1938).
- **نمط "gaps تدّعي حذف رابط لسه موجود" استمر**: thk-gabel (thk-marshall).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير (frankanderson→sch-ifs، frederickleong→sch-multicultural-counseling، gabel/fberlin→br-sotp، gabor-mate→sch-phenomenology-somatic، gallport→sch-humanistic). حالات بلا slug مطابق (fvolkmar [DIR/Floortime]، fukuzawa [الليبرالية اليابانية]، gary-chapman [علم النفس الشعبي الزواجي]، gary-wells [علم شهادة الشهود]) أُفرغت مع تسجيل طلبات جديدة.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 30 ملفاً — النمط الأكثر شيوعاً في هذه الدفعة تحديداً.
- عدة ملفات كانت تفتقر لقسم `## المصادر` بالكامل (فوكس، فبيرلز، فرويد جزئياً، غاندي، غانغيشا، غانسكومب) — أُضيفت مصادر أولية حقيقية موثقة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{foulkes,fperls,francesharville,francine-shapiro,francis-bacon,francisco-de-vitoria,frankanderson,frankl,frederickleong,freeman,freud,frey-rohn,fromm-reichmann,fromm,fskinner,ftustin,fuchs,fukuzawa,furtmuller,fvaughan,fvolkmar,fyeomans,gabel,gabor-mate,gadamer,gadler,galileo-galilei,gallport,gandhi,gangesha,ganscombe,gaos,gary-chapman,gary-wells}.md
→ ✅ 34 ملف — صفر مخالفات آلية (thk-fvanderzee حُجر صحياً بدل كتابة مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإضافة مصادر أولية حقيقية حيث كانت غائبة.

## متوقف عنده (لرئيس التحرير)
- **thk-freud**: تقليم شبكة related من 27→3 قرار جوهري يحتاج حسماً (تقليم صارم أم توسيع المتن لتبرير روابط تاريخية حقيقية؟).
- **thk-francesharville ↔ thk-francine-shapiro**: ملف مكرر مؤكد لنفس الشخص — يحتاج دمجاً وإحالة.
- **thk-gary-wells**: تصحيح جينيفر ديسارت وحذف اقتباس غير مسنَد يحتاجان تأكيداً قبل الترقية؛ وهل يُنشأ `sch-eyewitness-science`؟
- **thk-fvolkmar**: هل يصنَّف فعلياً تحت DIR/Floortime رغم أن دوره كان نقدياً لا انتمائياً؟
- **thk-galileo-galilei**: حقل `part: "psychology"` يبدو خاطئاً لشخصية في تاريخ العلوم لا علم النفس — لم يُعدَّل (خارج نطاق Task 3).
- **thk-fromm-reichmann**: إضافة واقعة زواجها من إريش فروم (سابقاً) تغيّر قراءة رابطها بـthk-fromm من "زميلة" إلى "زوجة سابقة" — يستحق مراجعة ثانية.

## الملفات
content/ar/thinkers/thk-foulkes.md
content/ar/thinkers/thk-fperls.md
content/ar/thinkers/thk-francesharville.md
content/ar/thinkers/thk-francine-shapiro.md
content/ar/thinkers/thk-francis-bacon.md
content/ar/thinkers/thk-francisco-de-vitoria.md
content/ar/thinkers/thk-frankanderson.md
content/ar/thinkers/thk-frankl.md
content/ar/thinkers/thk-frederickleong.md
content/ar/thinkers/thk-freeman.md
content/ar/thinkers/thk-freud.md
content/ar/thinkers/thk-frey-rohn.md
content/ar/thinkers/thk-fromm-reichmann.md
content/ar/thinkers/thk-fromm.md
content/ar/thinkers/thk-fskinner.md
content/ar/thinkers/thk-ftustin.md
content/ar/thinkers/thk-fuchs.md
content/ar/thinkers/thk-fukuzawa.md
content/ar/thinkers/thk-furtmuller.md
content/ar/thinkers/thk-fvanderzee.md
content/ar/thinkers/thk-fvaughan.md
content/ar/thinkers/thk-fvolkmar.md
content/ar/thinkers/thk-fyeomans.md
content/ar/thinkers/thk-gabel.md
content/ar/thinkers/thk-gabor-mate.md
content/ar/thinkers/thk-gadamer.md
content/ar/thinkers/thk-gadler.md
content/ar/thinkers/thk-galileo-galilei.md
content/ar/thinkers/thk-gallport.md
content/ar/thinkers/thk-gandhi.md
content/ar/thinkers/thk-gangesha.md
content/ar/thinkers/thk-ganscombe.md
content/ar/thinkers/thk-gaos.md
content/ar/thinkers/thk-gary-chapman.md
content/ar/thinkers/thk-gary-wells.md
