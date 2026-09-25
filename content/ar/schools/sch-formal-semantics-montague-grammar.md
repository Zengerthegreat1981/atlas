---
slug: "sch-formal-semantics-montague-grammar"
id: "SCH-9216"
type: "مدرسة"
part: "linguistics"
level: "متقدم"
linguistic_level: "semantics"
cultural_origin: "anglo-european"
title: "الدلالةُ الصوريةُ ونحوُ مونتاغيو (Formal Semantics)"
en: "Formal Semantics (Montague Grammar)"
crumb: "علم اللغة ← التوليدية وما بعدها ← الدلالةُ الصورية"
dates: "الولايات المتحدة · من 1970 إلى الوقت الحاضر"
country: "الولايات المتحدة"
language: "الإنجليزية"
active_start: 1970
active_end: "مستمر"
edges: []
related:
- id: "thk-richard-montague", title: "ريتشارد مونتاغيو", type: "مفكر"
- id: "thk-kazimierz-ajdukiewicz", title: "كازيمير أجدوكيفيتش", type: "مفكر"
- id: "thk-joachim-lambek", title: "يواكيم لامبك", type: "مفكر"
- id: "thk-barbara-partee", title: "باربارا بارتة", type: "مفكر"
- id: "sch-generative-grammar", title: "النحوُ التوليديُّ التحويليّ (Generative-Transformational Grammar)", type: "مدرسة"
- id: "sch-gricean-pragmatics", title: "التداوليةُ الغرايسية (Gricean Pragmatics)", type: "مدرسة"
- id: "con-presupposition-projection-problem", title: "الافتراضُ المسبَق ومشكلةُ الانتقال (Presupposition & the Projection Problem)", type: "مفهوم"
- id: "con-focus-particles", title: "جسيماتُ التركيز (Focus Particles)", type: "مفهوم"
- id: "con-generalized-quantifiers-barwise-cooper", title: "الكمّياتُ المعمَّمة عند بارواز وكوبر (Generalized Quantifiers)", type: "مفهوم"
- id: "thk-angelika-kratzer", title: "أنجيليكا كراتزر", type: "مفكر"
- id: "con-kratzer-modal-base-ordering-source", title: "القاعدةُ الموجِّهيةُ ومصدرُ الترتيب عند كراتزر (Modal Base & Ordering Source)", type: "مفهوم"
- id: "thk-irene-heim", title: "إيرين هايم", type: "مفكر"
- id: "con-file-change-semantics-heim", title: "دلالةُ تغيير الملفّ عند هايم (File Change Semantics)", type: "مفهوم"
- id: "con-categorial-grammar-montague", title: "النحوُ الفئويُّ وأساسُه المنطقي في نحو مونتاغيو (Categorial Grammar)", type: "مفهوم"
- id: "con-possible-worlds-semantics-kripke", title: "دلالات العوالم الممكنة والمنطق الموجه (Possible Worlds)", type: "مفهوم"
- id: "thk-david-dowty", title: "ديفيد داوتي", type: "مفكر"
- id: "con-thematic-proto-roles-dowty", title: "الأدوارُ الموضوعية البدئية عند داوتي (Thematic Proto-Roles)", type: "مفهوم"
- id: "con-donkey-sentences-anaphora", title: "جملُ الحمار وإشكاليةُ الإحالة الضميرية (Donkey Sentences)", type: "مفهوم"
- id: "thk-jon-barwise", title: "جون بارواز", type: "مفكر"
- id: "thk-robin-cooper", title: "روبِن كوبر", type: "مفكر"
- id: "thk-hans-kamp", title: "هانز كامپ", type: "مفكر"
- id: "thk-mats-rooth", title: "ماتس روث", type: "مفكر"
- id: "thk-lauri-karttunen", title: "لوري كارتونن", type: "مفكر"
- id: "thk-knud-lambrecht", title: "كنود لامبرخت", type: "مفكر"
gaps:
  - "لا `belongs_to`/`evolved_from`: نشأت الدلالةُ الصوريةُ من تقاطع المنطق الرياضي بأعمال مونتاغيو المنطقية المستقلة عن سلالة تشومسكي التوليدية، لا كامتدادٍ تاريخيٍّ مباشرٍ منها؛ سُجِّلت العلاقةُ بـ`related` لا بعلاقة انحدار."
  - "**سُدَّ بالكامل 2026-09-22 (الدفعة 238)**: أُنشئت `thk-angelika-kratzer` وعقدتُها المفهومية `con-kratzer-modal-base-ordering-source`، مستشهَدٌ بعملها المشترك مع Heim في مصادر هذا الملفّ دون أن تكون هي نفسُها موصولةً بعقدةٍ سابقاً."
---

# الدلالةُ الصوريةُ ونحوُ مونتاغيو

تيارٌ في الدلالة اللسانية أسّسه الفيلسوف والمنطقي الأمريكي **ريتشارد مونتاغيو** في أواخر الستينيات، يطبّق أدوات المنطق الرياضي والدلالة الصورية (Model-Theoretic Semantics) على تحليل معنى الجمل في اللغات الطبيعية بالدقة نفسها التي تُحلَّل بها اللغات الصورية في المنطق، منطلقاً من أطروحته الشهيرة بأنه «لا يوجد فرقٌ نظري مهم بين اللغات الطبيعية واللغات الصورية للمنطقيين» (English as a Formal Language، 1970).

## مبدأ التركيبية

يقوم نحو مونتاغيو على **مبدأ التركيبية** (Principle of Compositionality)، الذي صِيغ لاحقاً في عبارةٍ صارت شعاراً للحقل: «النحو جبر، والدلالة جبر، والمعنى تشاكلٌ (Homomorphism) بينهما». بموجب هذا المبدأ، يُشتقّ معنى أي تعبيرٍ مركّب آلياً من معاني مكوّناته وطريقة تركيبها النحوي فقط، بحيث تُقابل كل قاعدةٍ نحوية قاعدةَ تفسيرٍ دلالي موازية تعمل عليها تلقائياً — نُشرت هذه المعالجة الأشهر في مقالته «The Proper Treatment of Quantification in Ordinary English» (المعروفة اختصاراً بـPTQ، 1973).

## المنطق المكثَّف والعوالم الممكنة

استعمل مونتاغيو منطقاً كثيفَ النمط (Intensional Logic) لمعالجة دلالة الجمل عبر **دلالات العوالم الممكنة** (Possible Worlds Semantics)، مميّزاً بين **الامتداد** (Extension) — مرجع التعبير في عالمٍ ولحظةٍ بعينهما — و**الكثافة** (Intension) — الدالّة التي تربط كل عالمٍ ممكن ولحظة بامتداد التعبير فيهما. مكّن هذا التمييز من تفسير ظواهر معقدة كانت تستعصي على الدلالة الامتدادية البسيطة، مثل الأفعال الموجِّهة (كـ«يعتقد» أو«يجب») والجمل الشرطية، بربطها بمجموعاتٍ من العوالم الممكنة بدل مرجعٍ واحدٍ ثابت.

## الكمّيات المعمَّمة والنحو الفئوي

استند مونتاغيو إلى **النحو الفئوي** (Categorial Grammar)، الذي طوّره سابقاً كازيمير أجدوكيفيتش ويواكيم لامبك، ليُخصِّص لكل مقولةٍ نحوية نوعاً دلالياً موازياً (فالاسم من نوع الأفراد، والفعل اللازم دالّةٌ من الأفراد إلى قيم الصدق، وهكذا). ومكّنت هذه الآلية من معالجة العبارات الكمّية («كل»، «بعض»، «معظم») بوصفها **كمّياتٍ معمَّمة** (Generalized Quantifiers)، وهو إطارٌ صاغه لاحقاً جون بارواز وروبِن كوبر بصورةٍ أعمّ، وأصبح أداةً معيارية في تحليل بنية الجملة الاسمية منطقياً.

## التطور اللاحق: هايم وكراتزر وكامپ

طوّرت **باربارا بارتة** أعمال مونتاغيو وجعلتها متاحةً منهجياً للسانيين غير المتخصصين في المنطق، فربطتها بأدوات النحو التوليدي. ثم وسّعت **إيرين هايم** الإطار عبر «دلالة تغيير الملفّ» (File Change Semantics) لمعالجة الإحالة الضميرية عبر الجمل، خصوصاً في «جمل الحمار» (Donkey Sentences) المعضلة منطقياً، بالتوازي مع «نظرية تمثيل الخطاب» (DRT) التي طوّرها هانز كامپ لغرضٍ مشابه. وأضافت **أنجيليكا كراتزر** تحليلاً دلالياً دقيقاً للأفعال الموجِّهة عبر مفهومَي «القاعدة الموجِّهية» و«مصدر الترتيب».

## الأثر والعلاقة بالتداولية

رغم استقلال الدلالة الصورية تاريخياً عن سلالة تشومسكي التوليدية النحوية (إذ نشأت من تقاطع المنطق الرياضي والفلسفة التحليلية لا من علم اللغة البنيوي)، أصبحت اليوم الإطار السائد في تحليل معنى الجملة أكاديمياً، وتفاعلت مع التداولية الغرايسية في معالجة ظواهر الافتراض المسبق وجسيمات التركيز وبنية المعلومة، مكوِّنةً حقلاً بينيّاً بين الدلالة الصورية والتداولية الصورية.

## المصادر

- Montague, Richard. "The Proper Treatment of Quantification in Ordinary English." In *Approaches to Natural Language*, eds. Hintikka et al. Reidel, 1973.
- Partee, Barbara H. "Montague Grammar." In *Handbook of Logic and Language*, eds. van Benthem & ter Meulen. Elsevier, 1997.
- Heim, Irene, & Kratzer, Angelika. *Semantics in Generative Grammar*. Blackwell, 1998.
- Barwise, Jon, & Cooper, Robin. "Generalized Quantifiers and Natural Language." *Linguistics and Philosophy*, 4(2), 1981.
- Dowty, David R., Wall, Robert E., & Peters, Stanley. *Introduction to Montague Semantics*. D. Reidel, 1981.

