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
gaps:
  - "ماثيو إ. پيترز (مؤلِّفُ ELMo الرئيسي) وجاكوب دِڤلن (قائدُ فريق BERT) باحثانِ هندسيان بارزان في اللسانيات الحاسوبية، لكن لم يُعثر على مادّةٍ سيريةٍ مستقلّة كافية (خارج ورقتَي 2018/2019 أنفسِهما) تبرِّر عقدةَ مفكرٍ مستقلّة بمعايير الجودة المعتمَدة هنا؛ الفجوةُ محفوظةٌ صراحةً بدل اختلاق سيرةٍ رقيقة."
---

# التمثيلاتُ المتّجهيةُ السياقية (ELMo وBERT)

## التعريف

التمثيلاتُ المتّجهيةُ السياقية (Contextualized Word Embeddings) جيلٌ من تمثيلات الكلمات الحاسوبية يمنح كلَّ ظهورٍ للكلمة متّجهاً مختلفاً بحسب سياقها الجملي الفعلي، خلافاً للتمثيلات الساكنة الأقدم كـWord2Vec وGloVe التي تُخصِّص متّجهاً واحداً ثابتاً لكل كلمة بصرف النظر عن معناها المقصود. جاء هذا التحوّلُ حلاً لمشكلة تعدّد المعنى (Polysemy): فكلمة "bank" تحصل على التمثيل المتجهي نفسِه في "نهر" و"مصرف" ضمن النماذج الساكنة، وهو ما تصححه النماذجُ السياقية.

## ELMo: التمثيلاتُ من نماذج اللغة

قدَّم ماثيو پيترز وزملاؤه نموذج ELMo (Embeddings from Language Models) عام 2018، الذي يشتقُّ تمثيلَ الكلمة من مجموع مرجَّحٍ لمخرجات طبقاتٍ متعدّدة من شبكاتِ LSTM ثنائية الاتجاه، مدرَّبةٍ للتنبؤ بالكلمة التالية والسابقة في السياق معاً. يمثّل هذا التمثيلُ خلاصةَ معالجة الجملة بأكملها لا الكلمة المفردة معزولةً، فيتغيّر متّجهُ الكلمة نفسِها بتغيّر الجملة المحيطة بها.

## BERT: المحوِّلاتُ ثنائيةُ الاتجاه

طوّر جاكوب دِڤلن وفريقُه في غوغل نموذج BERT (Bidirectional Encoder Representations from Transformers) عام 2019، مستبدِلاً بنيةَ LSTM المتعاقبة عند ELMo بمشفِّر محوِّل (Transformer Encoder) قائمٍ على آلية الانتباه الذاتي (Self-Attention)، التي تحسب العلاقاتِ بين كل الكلمات في الجملة بالتوازي بدل التعاقب. دُرِّب BERT بمهمّتين ذاتيتَي الإشراف: نمذجةُ اللغة المقنَّعة (Masked Language Modeling)، حيث يُخفى جزءٌ من الكلمات ويُطلَب من النموذج توقّعها من السياق المحيط في الاتجاهين معاً، وتوقّعُ الجملة التالية (Next Sentence Prediction).

## الفارقُ البنيوي والوظيفي

يمنح الانتباهُ الذاتي عند BERT ميزةً حاسمة على البنية المتعاقبة لـELMo: القدرةَ على ربط أي كلمتين في الجملة مباشرةً بصرف النظر عن المسافة بينهما، وبمعالجةٍ متوازية أسرع تدريباً. كما يُستخدَم BERT عادةً بطريقة "الضبط الدقيق" (Fine-Tuning)، إذ تُدرَّب كل أوزان النموذج المُدرَّب مسبقاً على مهمّةٍ لاحقة محدَّدة، بينما استُخدم ELMo غالباً بطريقة "قائمة على السمات" (Feature-Based) يُضاف فيها تمثيلُه جاهزاً إلى معمارية نموذجٍ مخصَّص للمهمّة.

## الأثر على معالجة اللغة الطبيعية

أحدثت هذه التمثيلاتُ السياقية نقلةً نوعية في أداء مهامِّ معالجة اللغة الطبيعية كافّة — من الإجابة عن الأسئلة إلى تحليل المشاعر والتعرّف على الكيانات المسمّاة — وأسّس BERT تحديداً نمطَ "التدريب المسبق ثم الضبط الدقيق" الذي صار المعيارَ السائد في الحقل، ومهّد الطريقَ مباشرةً لنماذج اللغة الكبرى اللاحقة القائمة على معمارية المحوِّل ذاتها.

## المصادر

- Peters, M. E., et al. (2018). "Deep Contextualized Word Representations." *Proceedings of NAACL-HLT 2018*.
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of NAACL-HLT 2019*.
- Vaswani, A., et al. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems*.
- Ethayarajh, K. (2019). "How Contextual are Contextualized Word Representations?" *Proceedings of EMNLP-IJCNLP 2019*.

