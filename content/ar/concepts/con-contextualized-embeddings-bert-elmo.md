---
slug: "con-contextualized-embeddings-bert-elmo"
id: "CON-12011"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "التمثيلاتُ المتّجهيةُ السياقية (ELMo وBERT)"
en: "Contextualized Word Embeddings (ELMo, BERT)"
crumb: "علم اللغة ← اللغةُ والحاسوبُ والقياس ← التمثيلاتُ المتّجهيةُ السياقية"
edges:
- rel: "belongs_to", target: "sch-computational-linguistics-nlp", target_type: "مدرسة"
related:
- id: "sch-computational-linguistics-nlp", title: "اللسانياتُ الحاسوبيةُ ومعالجةُ اللغة الطبيعية (Computational Linguistics & NLP)", type: "مدرسة"
- id: "con-distributional-semantics-word-embeddings", title: "الدلالةُ التوزيعية وتمثيلاتُ الكلمات المتّجهية (Distributional Semantics & Word Embeddings)", type: "مفهوم"
- id: "con-transformer-attention-mechanism", title: "معماريةُ المحوِّل وآليةُ الانتباه (Transformer & Attention Mechanism)", type: "مفهوم"
- id: "con-word2vec-mikolov", title: "خوارزميةُ Word2Vec عند ميكولوف", type: "مفهوم"
gaps: []
---

# التمثيلاتُ المتّجهيةُ السياقية (ELMo وBERT)

نقلةٌ منهجية محورية في تمثيل معنى الكلمة حاسوبياً، تجاوزت قصورَ تمثيلات الكلمات المتّجهية الكلاسيكية (كـWord2Vec) التي تُسنِد لكلّ كلمةٍ متّجهاً ثابتاً واحداً بصرف النظر عن السياق الذي وردت فيه.

## مشكلةُ التمثيل الثابت: كلمةٌ واحدة، معانٍ متعدّدة

عابت التمثيلاتُ المتّجهيةُ التقليدية أنها تُسنِد للكلمة الواحدة (كـ"عين" في العربية، أو "bank" في الإنجليزية) متّجهاً واحداً ثابتاً، رغم أن الكلمةَ قد تحمل معانيَ مختلفةً جذرياً بحسب سياقها ("عينُ الماء" مقابل "عين الإنسان"). هذا يُفقِد النموذجَ القدرةَ على التمييز الدلالي السياقي الدقيق.

## الحلّ: تمثيلٌ يُبنى ديناميكياً من السياق

قدّم نموذجُ ELMo (Embeddings from Language Models، 2018) ثم BERT (Bidirectional Encoder Representations from Transformers، 2018) حلاً جذرياً: لا تُخزَّن الكلمةُ بمتّجهٍ ثابتٍ سلفاً، بل يُحسَب متّجهُ تمثيلها **ديناميكياً في كلّ مرّة** بناءً على الجملة الكاملة المحيطة بها، عبر شبكاتٍ عصبيةٍ عميقة (شبكاتٌ تكرارية عند ELMo، ومعماريةُ المحوِّل والانتباه عند BERT) تُدرَّب مسبقاً على كمّياتٍ ضخمة من النصوص غير الموسومة بمهمّةٍ عامّة (كالتنبؤ بكلمةٍ محجوبة من سياقها).

## التدريبُ المسبَق والضبطُ الدقيق

أرست هذه النماذجُ نمطاً منهجياً جديداً ساد لاحقاً في اللسانيات الحاسوبية: **التدريبُ المسبَق** (Pre-training) على مهمّةٍ لغويةٍ عامّة بكمّياتٍ هائلة من النصّ غير المُعلَّم، يليه **الضبطُ الدقيق** (Fine-tuning) على مهامَّ محدَّدة أصغر (كتحليل المشاعر أو الإجابة عن الأسئلة) باستعمال كمّيةٍ أقلَّ بكثير من البيانات الموسومة، مستفيداً من المعرفة اللغوية العامّة المكتسَبة في مرحلة التدريب المسبَق.

## الأثر

مهّدت هذه النماذجُ الطريقَ مباشرةً للنماذج اللغوية الكبرى اللاحقة (كسلسلة GPT)، وحوّلت المعيارَ الأساسي لتقييم جودة النماذج اللغوية الحاسوبية من الدقّة على مهمّةٍ واحدةٍ محدَّدة إلى القدرة على التكيّف السريع عبر مهامَّ متعدّدة بفضل التمثيل السياقي الغني المكتسَب مسبقاً.

## المصادر

- Peters, Matthew E. et al. (2018). "Deep Contextualized Word Representations." *NAACL-HLT*.
- Devlin, Jacob et al. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *NAACL-HLT*.
