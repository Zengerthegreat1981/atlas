---
slug: "sch-computational-linguistics-nlp"
id: "SCH-9222"
type: "مدرسة"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "Computational Linguistics & NLP"
en: "Computational Linguistics & NLP"
crumb: "Linguistics ← Schools ← Computational Linguistics & NLP"
dates: "United States · 1950 to present"
country: "United States"
language: "English"
active_start: 1950
active_end: "مستمر"
edges: []
related:
- id: "sch-corpus-linguistics", title: "Corpus Linguistics", type: "مدرسة"
- id: "sch-generative-grammar", title: "Generative-Transformational Grammar", type: "مدرسة"
- id: "con-distributional-semantics-word-embeddings", title: "Distributional Semantics and Word Embeddings", type: "مفهوم"
gaps: []
---

# Computational Linguistics and Natural Language Processing

A branch that combines the study of language with computer science to build formal and computational models for understanding, generating, and analyzing natural language automatically, from early machine translation attempts to contemporary natural language processing (NLP).

## Beginnings and Automata Theory

The field emerged in the 1950s alongside the development of automata theory and early digital computing, drawing on the grammatical formalisms developed by Chomsky (context-free grammars) as tools that could be implemented computationally. Early systems relied on manually written grammatical and lexical rules (rule-based NLP).

## The Machine Translation Crisis and the ALPAC Report

The report of the US Automatic Language Processing Advisory Committee (ALPAC) in 1966 judged that early machine translation had not produced results proportionate to its cost. US government funding for machine translation then fell sharply. Work did not stop everywhere: research continued in Europe and in some American laboratories, and many projects turned to narrower tasks such as morphological analysis and parsing before statistical methods brought full translation back to the center of the field.

## The Statistical Turn

From the late 1980s, and especially in the 1990s, the field shifted to statistical and machine learning approaches that extract their patterns from large annotated text corpora rather than from fully hand-written rules, methodologically intersecting with corpus linguistics. Among the key tools of this period were probabilistic "n-gram" models for predicting successive words, and Hidden Markov Models (HMM) for tasks such as part-of-speech tagging and speech recognition. These tools were developed by researchers such as Frederick Jelinek at IBM laboratories, drawing on signal-processing methods originally applied to automatic speech recognition.

## From Count Vectors to Neural Networks

Distributional semantics treats a word's meaning as recoverable, in part, from the contexts in which it occurs. Latent semantic analysis (Deerwester and colleagues, 1990) was an early matrix-based version. In 2013 Tomas Mikolov and colleagues released word2vec, which learns dense vectors from prediction. ELMo (Peters and colleagues, NAACL 2018) and BERT (Devlin and colleagues, preprint 2018, NAACL 2019) then produced contextual representations: the vector for a word depends on the sentence in which it appears. BERT is a Transformer encoder trained with a masked-word objective; it is not itself a generative chatbot.

## The Transformer Architecture and Large Language Models

The Transformer architecture, introduced by Vaswani and colleagues in 2017, relies on attention so that each token can be related directly to others in the sequence. Subsequent large language models, including BERT and the GPT series (the latter from OpenAI, beginning with Radford and colleagues in 2018), use this architecture or close variants. Their fluency has renewed debate about what statistical learning implies for theories of acquisition. Success at prediction is not, by itself, evidence for or against an innate grammar.

## The Relationship to Linguistic Theory

The relationship between computational linguistics and traditional linguistic theory (especially Chomsky's generative grammar) has been a continuing methodological tension since the field's founding. While early systems drew directly on generative grammatical formalisms, later statistical and neural approaches gradually moved away from positing explicitly interpreted grammatical structures (such as deep tree structures), preferring to learn patterns directly from data without prior linguistic assumptions. This raises a question that remains open: are computational systems purely applied tools separate from theoretical questions, or does their practical success carry real implications about the nature of human language and its mechanisms of acquisition? The question has returned with new urgency with the emergence of large language models and their capacity to produce grammatically coherent language without explicit grammatical programming.

## Applications and Social Impact

The field's applications have extended beyond machine translation to include automatic summarization, question answering, sentiment analysis, voice assistants, and dialogue systems. These applications have also provoked growing ethical and social debates about algorithmic bias derived from training data, and about the marginalization of languages with few computational resources, including Arabic in its many dialects despite its wide spread, in the development of these systems compared with English.

## Computational Linguistics and Arabic

Automatic processing of Arabic has faced particular challenges that have attracted independent research interest: the absence of diacritics in texts that are usually written without them (which makes the morphological decomposition of a single word ambiguous, sometimes even for humans without context); the richness of non-linear derivational morphology based on root and pattern; and the wide variation between Modern Standard Arabic and the many colloquial dialects, which often lack standardized spelling conventions. These challenges led specialist researchers to develop Arabic-specific morphological analysis tools (such as the Buckwalter Arabic Morphological Analyzer, AlKhalil Morpho Sys and MADAMIRA, which analyse an Arabic word into stem, pattern and affixes) because tools designed for languages with largely concatenative morphology such as English transfer poorly.

## Sources

- Jurafsky, Daniel, & Martin, James H. *Speech and Language Processing* (2nd ed.). Prentice Hall, 2008.
- Manning, Christopher D.; Schütze, Hinrich (1999). *Foundations of Statistical Natural Language Processing*. MIT Press.
- Pierce, John R.; et al. (1966). *Language and Machines: Computers in Translation and Linguistics* (the ALPAC report). National Academy of Sciences.
- Vaswani, Ashish; et al. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems* 30.
- Deerwester, Scott; Dumais, Susan T.; Furnas, George W.; Landauer, Thomas K.; Harshman, Richard (1990). "Indexing by Latent Semantic Analysis." *Journal of the American Society for Information Science* 41(6).
- Mikolov, Tomas; Chen, Kai; Corrado, Greg; Dean, Jeffrey (2013). "Efficient Estimation of Word Representations in Vector Space." arXiv:1301.3781.
- Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of NAACL-HLT*.
- Peters, Matthew E.; et al. (2018). "Deep Contextualized Word Representations." *Proceedings of NAACL-HLT*.
- Radford, Alec; Narasimhan, Karthik; Salimans, Tim; Sutskever, Ilya (2018). "Improving Language Understanding by Generative Pre-Training." OpenAI technical report.
