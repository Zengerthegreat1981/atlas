# Task 3.13
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-fairbairn..thk-foucault.

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 1 / 35 (thk-fakhr-razi)
- **وفاة حديثة غير مسجلة بحث خارجي مهم: thk-foa (إدنا فوا)** — توفيت فعلياً في 24 مارس 2026 (مصادر متعددة: ynet، Inquirer، IOCDF) بينما الملف كان يضعها "مستمرة" — صُححت dates/active_end. نفس الملف فيه عدة كتب مفبركة/منسوبة خطأً (Treating PTSD 2000 لروثباوم بدل كين وفريدمان، "OCD 1998 مع فيكتور ماير" غير موجود، "أطلس إدارة القلق 2005" مفبرك) — حُذفت جميعاً.
- **هوية مفبركة/نسبة خاطئة خطيرة: thk-fosha (ديانا فوشا)** — شخصيتان "إيغور غريم" و"إدموند غيل فيليبس" غير قابلتين للتحقق إطلاقاً حُذفتا. خلط بين "جاي ر. غرينبرغ" (محلل علائقي، شخص مختلف) و"ليزلي غرينبرغ" (مؤسس EFT الحقيقي المقصود) — صُحح. ميلادها الفعلي بوخارست 1952 لا الولايات المتحدة ~1950 — صُحح ببحث خارجي.
- **نسبة خاطئة/مفهوم لشخص آخر: thk-fairbairn** — مفهوم "العوز الأساسي" منسوب خطأً له، والاصطلاح الحقيقي القريب "الخلل الأساسي" يخص مايكل بالينت (شخص آخر) — حُذف المفهوم بدل اختراع بديل، وسُجل كقرار حساس (احتمال نسخ خاطئ من ملف بالينت).
- **تصنيف بنيوي خاطئ متكرر (نمط مكتشف عبر عدة ملفات)**: `sch-existential-therapy` (مدرسة علاجية إكلينيكية) استُخدم خطأً لفلاسفة أكاديميين غير علاجيين — `thk-flusser` وthk-flynn (كلاهما بنفس الخطأ بالضبط)، وأيضاً thk-fc-schiller وthk-fechner كانا يشاوران مدخلاً غير ذي صلة إطلاقاً. صُححت جميعاً إلى `sch-existentialism`/`sch-pragmatism-classical` أو أُفرغت edges.
- **تناقض داخلي حقيقي في الملف المعتمد نفسه: thk-erigena (سبق) وهنا thk-fechner** — تصنيف "الظاهراتية الفلسفية...من هوسرل إلى بينسفانغر وبوس" لا علاقة له بفيخنر مؤسس علم النفس الفيزيائي — أُفرغت edges وسُجل طلب `br-psychophysics-founders`.
- **أخطاء تواريخ حقيقية أخرى**: thk-feng-youlan (active_end 1946 خطأ، الصحيح 1990 — واصل النشر حتى الثمانينيات)، thk-epolster (من دفعة سابقة، مذكور للسياق).
- **أخطاء جنس نحوي**: thk-fmodestin (عناوين مؤنثة لشخص هو رجل فعلياً — باتريك كوريغان) صُححت.
- **نمط "gaps تدّعي حذف رابط لسه موجود" استمر**: thk-falexander (4 روابط، 3 منها محجورة فعلياً)، thk-fmodestin (thk-lfish)، thk-fberlin.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير من الملفات (fdolto→br-lacanian، femery→br-general-systems-cybernetics، falexander→tec-alexander-technique، fberlin→br-sotp، fonagy→br-attachment-theory، fmodestin→br-psychiatric-vocational-rehab). حالات بلا slug مطابق (fkurtz [Hakomi]، fcaine [العلاج بالفن]، fnewman [العلاج الاجتماعي]) أُفرغت مع تسجيل طلبات جديدة، منها تكرار ثالث لفجوة "العلاج بالفن" (كاني، كرامر، نومبورغ الآن جميعاً بانتظار slug واحد).
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في أكثر من 25 ملفاً من هذه الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{fairbairn,falexander,fanon,farber,farley,farrelly,fberlin,fc-schiller,fcaine,fdolto,fechner,federn,femery,feng-youlan,feuerbach,fhaug,fichte,fink,firestone,fkeller,fkurtz,floridi,flusser,flynn,fmesmer,fmodestin,fnewman,foa,fonagy,fondane,fordham,fosha,fouad-zakariya,foucault}.md
→ ✅ 34 ملف — صفر مخالفات آلية (thk-fakhr-razi سليم تماماً، بلا مسودة).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإصلاح تسلسل تواريخ (إضافة "بعد وفاته/ها" صراحة).

## متوقف عنده (لرئيس التحرير)
- **thk-fairbairn**: هل خلط مفهوم "العوز الأساسي" مع بالينت كان نسخاً خاطئاً متعمداً من ملف آخر؟ يستحق مراجعة.
- **thk-foa**: وفاتها (مارس 2026) وكتب مفبركة متعددة — أولوية عالية جداً للترقية والتأكد.
- **thk-fosha**: علاقتها الفعلية بكَلشد/فان دير كولك/ليفين تحتاج توثيقاً نصياً مباشراً قبل أي ترقية.
- **نمط تصنيف `sch-existential-therapy` الخاطئ**: ظهر في 4 ملفات من هذه الدفعة وحدها (flusser، flynn، fc-schiller، fechner) — يستحق فحصاً آلياً شاملاً لباقي الملفات تحت نفس المسار بدل الاكتشاف اليدوي المتناثر.
- **thk-fnewman**: نمط أسماء غير موثقة متكرر حول حركة "العلاج الاجتماعي" (Social Therapy) — يستحق مراجعة العنقود كله.
- **طلب `sch-art-therapy`**: الآن 3 ملفات (فلورنس كاني، إديث كرامر، مارغريت نومبورغ) بانتظاره.

## الملفات
content/ar/thinkers/thk-fairbairn.md
content/ar/thinkers/thk-fakhr-razi.md
content/ar/thinkers/thk-falexander.md
content/ar/thinkers/thk-fanon.md
content/ar/thinkers/thk-farber.md
content/ar/thinkers/thk-farley.md
content/ar/thinkers/thk-farrelly.md
content/ar/thinkers/thk-fberlin.md
content/ar/thinkers/thk-fc-schiller.md
content/ar/thinkers/thk-fcaine.md
content/ar/thinkers/thk-fdolto.md
content/ar/thinkers/thk-fechner.md
content/ar/thinkers/thk-federn.md
content/ar/thinkers/thk-femery.md
content/ar/thinkers/thk-feng-youlan.md
content/ar/thinkers/thk-feuerbach.md
content/ar/thinkers/thk-fhaug.md
content/ar/thinkers/thk-fichte.md
content/ar/thinkers/thk-fink.md
content/ar/thinkers/thk-firestone.md
content/ar/thinkers/thk-fkeller.md
content/ar/thinkers/thk-fkurtz.md
content/ar/thinkers/thk-floridi.md
content/ar/thinkers/thk-flusser.md
content/ar/thinkers/thk-flynn.md
content/ar/thinkers/thk-fmesmer.md
content/ar/thinkers/thk-fmodestin.md
content/ar/thinkers/thk-fnewman.md
content/ar/thinkers/thk-foa.md
content/ar/thinkers/thk-fonagy.md
content/ar/thinkers/thk-fondane.md
content/ar/thinkers/thk-fordham.md
content/ar/thinkers/thk-fosha.md
content/ar/thinkers/thk-fouad-zakariya.md
content/ar/thinkers/thk-foucault.md
