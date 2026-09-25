---
slug: "con-categorial-grammar-montague"
id: "CON-11985"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "semantics"
cultural_origin: "anglo-european"
title: "النحوُ الفئويُّ وأساسُه المنطقي في نحو مونتاغيو (Categorial Grammar)"
en: "Categorial Grammar & Montague's Syntax-Semantics Interface"
crumb: "علم اللغة ← التوليدية وما بعدها ← النحوُ الفئويُّ وأساسُه المنطقي"
edges:
- rel: "belongs_to", target: "sch-formal-semantics-montague-grammar", target_type: "مدرسة"
related:
- id: "sch-formal-semantics-montague-grammar", title: "الدلالةُ الصوريةُ ونحوُ مونتاغيو (Formal Semantics)", type: "مدرسة"
- id: "con-generalized-quantifiers-barwise-cooper", title: "الكمّياتُ المعمَّمة عند بارواز وكوبر (Generalized Quantifiers)", type: "مفهوم"
- id: "thk-richard-montague", title: "ريتشارد مونتاغيو", type: "مفكر"
- id: "thk-kazimierz-ajdukiewicz", title: "كازيمير أجدوكيفيتش", type: "مفكر"
- id: "thk-joachim-lambek", title: "يواكيم لامبك", type: "مفكر"
gaps: []
---

# النحوُ الفئويُّ وأساسُه المنطقي في نحو مونتاغيو

## التعريف

النحوُ الفئويُّ (Categorial Grammar) صيغةٌ نحوية منطقية تُشتقُّ فيها فئاتُ الكلمات والعبارات من فئتين بدائيتين (كالاسم والجملة) عبر قواعدَ دالّية-حجّية (Function-Argument)، بحيث تحدِّد كلُّ فئةٍ نوعَ ما تحتاجه لتكتمل وما تُنتجه. صاغ أساسَها المنطقيَّ كازيمير أجدوكيفيتش عام 1935، وطوّرها يواكيم لامبك رياضياً عام 1958 (حساب لامبك)، لكن مكانتَها المركزية في اللسانيات الدلالية جاءت من تبنّي ريتشارد مونتاغيو لها إطاراً نحوياً موازياً لدلالته الصورية في مطلع السبعينيات.

## التوافق بين النحو والدلالة

الإسهامُ الحاسم لمونتاغيو هو مبدأُ التوافق التام بين الفئة النحوية والنوع الدلالي (Syntax-Semantics Homomorphism): لكل فئةٍ نحوية نوعٌ دلاليٌّ مقابل، ولكل قاعدةِ تركيبٍ نحوي عمليةُ تأليفٍ دلالي مقابلة (غالباً تطبيقُ دالةٍ على حجّةٍ عبر حساب لامبدا)، بحيث يُشتقُّ معنى الجملة تركيبياً من معاني أجزائها بالتوازي التام مع اشتقاق بنيتها النحوية. هذا ما سمّاه مونتاغيو في مقالته الشهيرة "English as a Formal Language" (1970) رفضَ الفارق الجوهري بين اللغات الطبيعية واللغات الصورية.

## الفئات والاشتقاق

في النحو الفئوي، تُبنى الفئاتُ المركّبة من فئتين أوّليتين بمعاملين: `A/B` (عبارةٌ تصبح من النوع A إذا أُلحقت بعبارةٍ من النوع B على يمينها) و`A\B` (النمط نفسُه على اليسار). فالفعل اللازم مثلاً فئتُه `S\NP` (يحتاج اسماً على يساره لينتج جملة)، والصفةُ فئتُها `N/N`. يسمح هذا النظامُ باشتقاق البنية عبر قاعدتين بسيطتين فقط (التطبيق الأمامي والخلفي)، خلافاً لتعقيد قواعد إعادة الكتابة التوليدية.

## من مونتاغيو إلى النحو الفئوي التوليفي

طوّر باحثون لاحقون، وبخاصة مارك ستيدمان، النحوَ الفئويَّ التوليفي (Combinatory Categorial Grammar - CCG) الذي يضيف عملياتِ تأليفٍ أعقد (كالتأليف الدالي والرفع) لمعالجة ظواهرَ كالتنسيق والاستخراج بعيد المدى، وصار من أكثر الصيغ النحوية استخداماً في معالجة اللغة الطبيعية الحاسوبية لسهولة برمجة التوافق الدلالي النحوي فيه آلياً.

## الأثر

أحيا نحوُ مونتاغيو الاهتمامَ باللسانيات الفئوية بعدما كادت تبقى أثراً منطقياً هامشياً، وأصبح الإطارُ المرجعي لكل الدلالة الصورية اللاحقة التي تشترط التأليفية الصارمة، كما امتدَّ أثرُه إلى نظرياتٍ نحوية أخرى كقواعد التركيب المعمَّمة للعبارة (GPSG) وقواعد بنية العبارة القائمة على الرأس (HPSG) التي استعارت مبدأ التوافق النحوي الدلالي دون الالتزام الكامل بصورية مونتاغيو.

## المصادر

- Montague, R. (1970). "English as a Formal Language." In *Linguaggi nella Società e nella Tecnica*. Reprinted in Thomason (ed.), *Formal Philosophy* (1974), Yale University Press.
- Ajdukiewicz, K. (1935). "Die syntaktische Konnexität." *Studia Philosophica*, 1, 1-27.
- Lambek, J. (1958). "The Mathematics of Sentence Structure." *American Mathematical Monthly*, 65(3), 154-170.
- Steedman, M. (2000). *The Syntactic Process*. MIT Press.
- Partee, B. H. (2005). "Reflections of a Formal Semanticist." Ms., University of Massachusetts Amherst.

