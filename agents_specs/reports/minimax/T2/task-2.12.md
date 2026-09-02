# Task 2.12
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 10

## الأرقام
موثّق: 9 → 9 (تسعة أشخاص حقيقيون موثّقون بمصادر حقيقية أضيفت لهم)
حجر: 1 (thk-tisoma — لا يوجد توثيق مستقل)
غامض: 0

## أمر التحقق
python3 scripts/task.py verify minimax 2.12  →  جمل القائمة السوداء: 0/10 · سقّالة ظاهرة: 0/10 · فيها ## المصادر: 9/10 (الملف العاشر thk-tisoma محجور بلا مصادر مختلَقة، كما تقتضي القاعدة 5)
python3 scripts/preflight_check.py <الملفات العشرة>  →  ✅ 10 ملف — صفر مخالفات آلية (بعد تصحيح 7 مخالفات: 2× edges.belongs_to بنص حر بدل slug حقيقي [thk-wkohler, thk-stephen-lankton]، 1× edges.belongs_to بنص حر لمدرسة غير موجودة أصلاً حُذف [thk-tisoma]، 2× تطابق id/title في related لـthk-fskinner [thk-rherrnstein, thk-mwolf]، 1× سنة بعد active_end بلا إشارة وفاة [thk-muruwwa]، 1× سطر gaps يؤكد حقيقة بدل تسمية فجوة [thk-tisoma])

## قرارات اتخذتها
- thk-sutich (أنتوني سوتيتش): موثّق. مؤسس ورئيس تحرير Journal of Humanistic Psychology (1961) وJournal of Transpersonal Psychology (1969)، شريك ماسلو في تنظيم "القوة الثالثة/الرابعة". أُضيف قسم المصادر، وأُعيدت صياغة سطر gaps لتفادي عبارة القائمة السوداء الحرفية.
- thk-sachs (هانس زاكس): موثّق. محلل نفسي عضو اللجنة السرية، مؤلف The Creative Unconscious (1942). أُضيف قسم المصادر.
- thk-park (كريستال بارك): موثّقة. أستاذة جامعة كونيتيكت، صاحبة Meaning Making Model (نُشر مراراً منذ 1997/2010). أُضيف قسم المصادر.
- thk-muruwwa (حسين مروة): موثّق. مفكر ماركسي لبناني، مؤلف النزعات المادية في الفلسفة العربية الإسلامية (1978)، اغتيل 1987. أُضيف قسم المصادر، وصُححت إشارة السيرة الذاتية المنشورة بعد وفاته (1990) لتفادي تناقض التواريخ.
- thk-wkohler (فولفغانغ كولر): موثّق. أحد مؤسسي الجشطالت الثلاثة، تجارب تينيريفي على الشمبانزي (1917). أُضيف قسم المصادر، وصُحح edges.belongs_to من نص حر إلى slug حقيقي (br-gestalt-berlin).
- thk-stephen-lankton (ستيفن لانكتون): موثّق. من تلاميذ إريكسون المباشرين، مؤلف The Answer Within (1983)، رئيس تحرير American Journal of Clinical Hypnosis. أُضيف قسم المصادر، وصُحح edges.belongs_to إلى slug حقيقي (br-clinical-hypnotherapy).
- thk-rherrnstein (ريتشارد سيرنشتاين): موثّق. عالم نفس هارفارد، صاحب "قانون التطابق" (1961)، شريك في The Bell Curve (1994). أُضيف قسم المصادر، وصُحح عنوان الرابط لـthk-fskinner ليطابق العنوان الحقيقي للملف المستهدف.
- thk-nishitani (كيجي نيشيتاني): موثّق. فيلسوف مدرسة كيوتو، تلميذ هايدجر، مؤلف Religion and Nothingness (1961/1982). أُضيف قسم المصادر.
- thk-mwolf (مونتروز وولف): موثّق. أحد مؤسسي ABA وJABA، مخترع Time-Out وGood Behavior Game (1969). أُضيف قسم المصادر، وصُحح عنوان الرابط لـthk-fskinner.
- thk-tisoma (تاكيشي إيسومه / Takeshi Isomae): **حجر**. لا يوجد سجل مستقل لباحث بهذا الاسم في علاج موريتا أو Constructive Living. الباحث الياباني الحقيقي المطابق للقب "إيسومه" هو Jun'ichi Isomae (磯前順一) — أستاذ دراسات دينية ونظرية نقدية في Nichibunken كيوتو، مجال مختلف تماماً ولا علاقة له بعلاج موريتا، واسمه الأول "جونإيتشي" لا "تاكيشي". الملف نفسه اعترف صراحة بغياب أي اقتباس موثّق وبإزالة رابط سابق لمدخل غير متحقَّق منه (thk-rreibo) — نمط تكرر داخل نفس الملف. سُجِّل في `agents_specs/quarantine-minimax.md` § القسم 1 بالسبب الكامل. لم يُكتب أي سيرة جديدة له، ولم يُحذف edges.belongs_to الوهمي (لم يكن يشاور على slug حقيقي أصلاً) بدل استبداله بواحد مخترع.

## متوقف عنده (لرئيس التحرير)
- thk-tisoma: يحتاج قرار نهائي من رئيس التحرير — إما نقل الملف لأرشيف الحجر (`quarantine-minimax-archive/`) واستبدال متنه بقالب حجر موحّد كما جرى مع دفعات سابقة، أو تركه في القسم 1 من `quarantine-minimax.md` كطابور عمل نشط لحين تحقق إضافي.

## الملفات
content/ar/thinkers/thk-sutich.md
content/ar/thinkers/thk-sachs.md
content/ar/thinkers/thk-park.md
content/ar/thinkers/thk-muruwwa.md
content/ar/thinkers/thk-wkohler.md
content/ar/thinkers/thk-stephen-lankton.md
content/ar/thinkers/thk-rherrnstein.md
content/ar/thinkers/thk-nishitani.md
content/ar/thinkers/thk-tisoma.md
content/ar/thinkers/thk-mwolf.md
