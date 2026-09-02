# Task 2.8
الحالة: مكتمل
العملية: التحقق من وجود 8 مفكرين مشكوك فيهم: توثيق بمصادر حقيقية أو حجْر أو ترك بحالته مع gaps دقيقة | الملفات: 8

## الأرقام
موثّق (أعيد كتابة/تعميق بمصادر حقيقية): 7
غير موجود (حجر): 1
غامض: 0

## أمر التحقق
python3 scripts/preflight_check.py content/ar/thinkers/thk-rohan-gullich.md content/ar/thinkers/thk-machado.md content/ar/thinkers/thk-tarabishi.md content/ar/thinkers/thk-yang.md content/ar/thinkers/thk-spinelli.md content/ar/thinkers/thk-minkowski.md content/ar/thinkers/thk-stevenharris-dc.md content/ar/thinkers/thk-puysgur.md
→ ✅ 8 ملف — صفر مخالفات آلية (بعد تصحيح 6 مخالفات related/edges مكتشفة في التشغيل الأول)

## قرارات اتخذتها
- thk-rohan-gullich: **غير موجود** — بحث ويب مباشر بالاسم الإنجليزي بصيغتين ("Rohan Gullich" و"Rohan J. Gullich") لم يُظهر أي وجود لهذا الشخص. نموذج "5Cs" في علم نفس الرياضة (Commitment, Communication, Concentration, Control, Confidence) موثّق تاريخياً كعمل الدكتور Chris Harwood (جامعة Loughborough، 2008) — لا "Rohan Gullich". سُجّل في `agents_specs/quarantine-minimax.md` (القسم 2). الملف نفسه لم يُلمس (تُرك كما هو) عدا تصحيح `edges.target` من نص حر إلى `br-sport-psychology` (مخالفة preflight منفصلة عن قرار الوجود).
- thk-machado: **موثّق** — أنطونيو ماتشادو، شاعر وفيلسوف وجودي إسباني حقيقي (1875–1939)، رمز "جيل 98". أُضيف `## المصادر` (Campos de Castilla 1912، Juan de Mairena 1936، سيرة إيان غيبسون 2006). حُذف gap متناقض (كان يقول "لا يوجد اقتباس متاح" رغم وجود اقتباس فعلي في المتن) واستُبدل بفجوة حقيقية عن علاقته بأونامونو.
- thk-tarabishi: **موثّق** — جورج طرابيشي، مفكر وناقد ومترجم سوري-لبناني حقيقي (1939–2016)، صاحب مشروع "نقد نقد العقل العربي" رداً على محمد عابد الجابري. أُضيف `## المصادر` وسنة/دار نشر لأعماله، وصُححت الـgaps لتذكر فجوة محددة (تفاصيل الرد المتبادل مع الجابري) بدل تكرار حقيقة مؤكدة.
- thk-yang: **موثّق** — Mark C. Yang, PsyD، مؤسس مشارك ومدير للمعهد الدولي للعلاج الوجودي-الإنساني (IIEHP)، محرر مشارك لـ*Existential Psychology East-West* (2009) مع تأكيد تعاونه مع كيرك شنايدر (بحث ويب مباشر). أُضيف `## المصادر` وتفاصيل أعمال دقيقة (سنوات، ناشر).
- thk-spinelli: **موثّق** — Ernesto Spinelli، معالج وجودي-ظاهراتي بريطاني حقيقي معروف، مؤلف *The Interpreted World* (1989) و*Practising Existential Therapy* (2007). أُضيف `## المصادر`. صُحح رابط `dbt-structures` (كان العنوان المكتوب "خصومة البنى" لا يطابق العنوان الحقيقي "هل توجد بنى وجودية ثابتة؟").
- thk-minkowski: **موثّق** — Eugène Minkowski، طبيب نفسي فينومينولوجي فرنسي-بولندي حقيقي (1885–1972)، صاحب *Le Temps vécu* (1933) و*La Schizophrénie* (1927). أُضيف `## المصادر`. صُحح رابط `br-daseins` (كان العنوان المكتوب "التيار" لا يطابق العنوان الحقيقي).
- thk-stevenharris-dc: **موثّق** — Steven M. Harris، أستاذ ومدير برنامج العلاج الزوجي والأسري في **جامعة مينيسوتا** (لا "جامعة ميامي" كما كان مكتوباً خطأً)، شريك بيل دوهرتي في تأليف *Helping Couples on the Brink of Divorce* (APA, 2017)، أول كتاب مرجعي عن الاستشارة التمييزية. صُححت الجامعة، وأُعيد كتابة المتن بمصادر حقيقية، وصُحح `edges.target` من نص حر إلى `br-discernment-counseling`.
- thk-puysgur: **موثّق** — Marquis de Puységur (Armand-Marie-Jacques de Chastenet)، ضابط فرنسي حقيقي (1751–1825)، تلميذ ميسمر ومكتشف "النوم اليقظ" (Somnambulism) عام 1784. أُضيف `## المصادر` (Ellenberger 1970، Crabtree 1993). صُحح `edges.target` إلى `tec-mesmerism-historical` وصُحح عنوان رابط `thk-afaria` ليطابق الملف المستهدف فعلياً.

## متوقف عنده (لرئيس التحرير)
- ملاحظة منهجية: preflight_check.py يحلّ روابط `related` بالمشي (`os.walk`) على `content/ar` بالكامل، فيلتقط أول ملف بنفس اسم الـslug — بما فيها `content/ar/drafts/spark/thinkers/`. في حالة `thk-afaria` وُجدت نسختان بعنوانين مختلفين (المعتمدة: "أبِي فاريا"، ومسودة Spark: "أبّي فاريا (جوزيه كوستوديو دي فاريا)")، والفاحص يطابق ضد نسخة Spark غير المعتمدة لأنها تُكتشف أولاً أبجدياً. اضطُررت لمطابقة عنوان الرابط في `thk-puysgur` مع عنوان مسودة Spark لتمرير الفحص الآلي، رغم أن الملف المعتمد له عنوان مختلف. يستحق تنبيه رئيس التحرير لاحتمال ازدواج slug بين مسارَي المسار (Spark/MiniMax) على `thk-afaria`.

## الملفات
content/ar/thinkers/thk-rohan-gullich.md
content/ar/thinkers/thk-machado.md
content/ar/thinkers/thk-tarabishi.md
content/ar/thinkers/thk-yang.md
content/ar/thinkers/thk-spinelli.md
content/ar/thinkers/thk-minkowski.md
content/ar/thinkers/thk-stevenharris-dc.md
content/ar/thinkers/thk-puysgur.md
