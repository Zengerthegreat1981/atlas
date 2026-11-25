---
slug: "br-computational-linguistics"
id: "BRN-1118"
type: "فرع"
part: "linguistics"
level: "متوسط"
title: "Computational Linguistics"
en: "Computational Linguistics"
crumb: "Linguistics ← Branches ← Computational Linguistics"
active_start: 1950
active_end: "مستمر"
edges:
- rel: "belongs_to", target: "Computational Linguistics & NLP", target_type: "مدرسة"
related:
- id: "sch-computational-linguistics-nlp", title: "Computational Linguistics & Natural Language Processing", type: "مدرسة"
- id: "sch-corpus-linguistics", title: "Corpus Linguistics and Its Methods", type: "مدرسة"
gaps: []
---

# Computational Linguistics: Modeling Language Computationally

A branch that combines linguistics and computer science to build computational models capable of analyzing, generating, and translating natural language. It ranges from purely theoretical questions (which formal structures describe the composition of language?) to direct engineering applications (machine translation, voice assistants, and large language models).

## From Early Machine Translation to Crisis

The branch practically began with early American machine translation projects during the Cold War, driven by an intelligence need to translate Russian documents quickly. Excessive optimism about an imminent solution based on simple dictionaries and rules led to a shock when the ALPAC report of 1966 concluded that high-quality machine translation was far more distant than funders had expected. American funding declined sharply for more than a decade, pushing researchers toward deeper theoretical questions rather than hasty application.

## From Rules to Statistics to Neural Networks

The field later went through three major methodological waves: **rule-based systems**, which rely on grammatical rules and dictionaries written by hand using explicit linguistic knowledge; then **statistical systems** since the late 1980s and 1990s, which learn translation and analysis patterns from large bilingual text corpora without explicitly hand-written rules; and then **neural networks** (neural language models from the early 2000s, and from about 2014 the encoder-decoder and attention-based sequence-to-sequence models for translation), which in turn paved the way for the Transformer architecture on which today's large language models are built.

## Computational Linguistics as a Theoretical Field

Alongside engineering applications, the branch developed basic formal tools for theoretical linguistics itself: formal syntactic grammars, computational semantics that represents sentence meaning mathematically, and computational morphological analysis for languages with complex inflection (such as Arabic). The late practical success of large language models has sparked intense theoretical debate about whether it carries implications for the nature of human language acquisition and its presumed innate structure, or whether it is a separate engineering achievement that does not affect traditional linguistic questions.

## Its Relationship to Corpus Linguistics

The branch closely intersects with corpus linguistics: large digital text corpora provide the raw material on which all modern computational models are trained, while computational linguistics in turn provides automated tools (such as part-of-speech tagging and automatic grammatical parsing) used to analyze those same corpora.

## The Transformer Architecture

The "Transformer" architecture, introduced by Vaswani and colleagues in 2017, replaced recurrent sequential processing with self-attention, which relates any token in a sequence to any other regardless of distance. The design scaled more readily than earlier recurrent encoder-decoder models and became the basis of subsequent large language models used for generation, translation, and other tasks.

## Computational Processing of Arabic: Special Challenges

Computational linguistics faces particular challenges when dealing with Arabic: rich morphological inflection (a single Arabic verb can take dozens of forms depending on tense, subject, and number); the practical absence of diacritics in most written texts (which increases lexical and grammatical ambiguity); and the mixture of formal written Modern Standard Arabic with diverse colloquial dialects in texts actually circulating on the internet. These factors require specialized morphological analysis tools (morphological segmenters that handle Arabic roots and patterns), which are not necessarily needed for European languages that are morphologically simpler, such as English.

## Ethics of Large Language Models

The enormous expansion in the size of recent large language models has raised new ethical and methodological questions within this branch that go beyond purely technical performance: biases embedded in vast training data (which may reflect social, cultural, or linguistic biases already present in the texts used for training); a notable disparity in performance quality between high-resource languages (such as English, for which vast training data is available) and low-resource languages (which may have only very limited amounts of digital text, making model performance on them much weaker); and these issues intersect directly with the concerns of the language documentation and language policy branches.

## Distinguishing Understanding from Generation

The branch systematically distinguishes between computational "understanding" tasks (such as classifying a text by topic or extracting specific information from it) and "generation" tasks (producing a new coherent text, such as translation or summarizing a long text). Each category requires somewhat different techniques and quality assessments. Modern models have excelled at both to varying degrees of success, though evaluating the quality of free generation (unlike understanding, which can be scored with simple binary classification) remains more difficult and methodologically subjective.

## Sources

- Jurafsky, Daniel, and James H. Martin. *Speech and Language Processing*. 2nd ed., Pearson, 2008.
- Vaswani, Ashish, et al. "Attention Is All You Need." *Advances in Neural Information Processing Systems* 30, 2017.
- Hutchins, W. John. *Machine Translation: Past, Present, Future*. Ellis Horwood, 1986.
