---
slug: "con-unification-grammar-formalism"
id: "CON-11711"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "التوحيدُ بوصفه آليةً حسابية نحوية (Unification-Based Grammar)"
en: "Unification-Based Grammar"
crumb: "علم اللغة ← التوليدية وما بعدها ← التوحيدُ بوصفه آليةً حسابية نحوية"
edges:
- rel: "belongs_to", target: "sch-lexical-functional-grammar-hpsg", target_type: "مدرسة"
related:
- id: "sch-lexical-functional-grammar-hpsg", title: "النحوُ التوليديُّ المعجميُّ الوظيفيّ وHPSG (Lexical-Functional Grammar & HPSG)", type: "مدرسة"
- id: "thk-joan-bresnan", title: "جوان برسنان", type: "مفكر"
- id: "thk-carl-pollard", title: "كارل بولارد", type: "مفكر"
- id: "con-argument-structure-lexicon", title: "بنيةُ الحجج المعجمية (Argument Structure)", type: "مفهوم"
gaps: []
---

# التوحيدُ بوصفه آليةً حسابية نحوية

الآليةُ الحسابية المشتركة التي تجمع بين النحو المعجمي الوظيفي (LFG) وHPSG رغم اختلاف تفاصيلهما التقنية، تستبدل عمليةَ "الحركة" التحويلية التوليدية بعمليةِ "دمجٍ" منطقيةٍ لبنيات معلوماتٍ جزئية.

## بنياتُ السماتِ الجزئية

يمثّل هذا الإطارُ المعلوماتِ النحوية (والصرفية والدلالية أحياناً) في هيئة "بنيات سمات" (Feature Structures)، وهي جداولُ من أزواج سماتٍ-وقيَم قد تكون جزئيةً أو غيرَ محدَّدة الاكتمال. تنشأ الجملةُ الصحيحة نحوياً حين يمكن "توحيدُ" (Unify) بنيات السمات الجزئية لعناصرها المكوِّنة توحيداً متّسقاً بلا تناقض — فإن حاول عنصران تحديدَ قيمتين متعارضتين لسمةٍ واحدة (كأن يتطلّب فعلٌ فاعلاً مفرداً بينما الاسمُ المرشَّح جمعٌ)، يفشل التوحيدُ وتُرفَض الجملةُ نحوياً.

## بديلٌ للحركة التحويلية

يوفّر التوحيدُ بديلاً حسابياً "تصريحياً" (Declarative) لا "إجرائياً" (Procedural) عن الحركة النحوية التحويلية في النظريات التوليدية: بدل افتراض أن الجملةَ "تُشتقّ" عبر خطواتٍ تحويليةٍ متعاقبة من بنيةٍ عميقة إلى بنيةٍ سطحية، تُعامَل كلُّ المعلومات النحوية والدلالية بوصفها قيوداً متزامنة يجب أن تتوحَّد معاً بلا تناقض في الجملة النهائية دفعةً واحدة.

## الأثرُ الحاسوبي

جعلت هذه الآليةُ التصريحية نحوَ التوحيد جذّاباً بشكلٍ خاص في اللسانيات الحاسوبية، إذ تتيح خوارزمياتُ التوحيد تنفيذاً حاسوبياً مباشراً وفعّالاً نسبياً مقارنةً بمحاكاة عمليات الحركة التحويلية المعقَّدة، ما جعل أطرَ LFG وHPSG شائعةَ الاستعمال في أنظمة تحليل اللغة الطبيعية الحاسوبية.

## المصادر

- Bresnan, Joan (2001). *Lexical-Functional Syntax*. Blackwell.
- Pollard, Carl; Sag, Ivan A. (1994). *Head-Driven Phrase Structure Grammar*. University of Chicago Press.
- Shieber, Stuart M. (1986). *An Introduction to Unification-Based Approaches to Grammar*. CSLI Publications.
