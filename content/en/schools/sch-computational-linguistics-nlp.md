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

The report of the American "ALPAC" committee in 1966 was a decisive turning point in the history of the field. It concluded that early machine translation, based on simple direct rules, had not achieved sufficient practical progress relative to its cost. This led to an almost complete halt in funding for machine translation research in the United States for many years, and pushed researchers to redirect the field toward more modest and attainable problems (such as partial morphological and syntactic analysis) before returning later to the ambition of full translation with more mature tools.

## The Statistical Turn

From the late 1980s, and especially in the 1990s, the field shifted to statistical and machine learning approaches that extract their patterns from large annotated text corpora rather than from fully hand-written rules, methodologically intersecting with corpus linguistics. Among the key tools of this period were probabilistic "n-gram" models for predicting successive words, and Hidden Markov Models (HMM) for tasks such as part-of-speech tagging and speech recognition. These tools were developed by researchers such as Frederick Jelinek at IBM laboratories, drawing on signal-processing methods originally applied to automatic speech recognition.

## The Representational Revolution: From Vectors to Neural Networks

Building on earlier work such as latent semantic analysis (1990), the 2000s and 2010s saw the rise of "distributional semantics," based on the premise that a word's meaning can be approximated statistically from the contexts in which it repeatedly appears in large texts. This culminated in algorithms that represent words as dense numerical vectors (such as Word2Vec, developed by Tomas Mikolov and colleagues in 2013). The approach later evolved into "contextualized" representations such as ELMo and BERT (both 2018), which produce a different representation of the same word depending on its actual sentence context, rather than a single fixed representation as in the previous generation.

## The Transformer Architecture and Large Language Models

The "Transformer" architecture, introduced by Google researchers in 2017 on the basis of the "attention" mechanism, brought a radical change that made it possible to train large language models on vast quantities of text with unprecedented computational efficiency. It led directly to the emergence of today's large language models (such as the GPT series and BERT and its successors), which revived older theoretical debates about the nature of language acquisition and linguistic innateness from an entirely new computational angle.

## The Relationship to Linguistic Theory

The relationship between computational linguistics and traditional linguistic theory (especially Chomsky's generative grammar) has been a continuing methodological tension since the field's founding. While early systems drew directly on generative grammatical formalisms, later statistical and neural approaches gradually moved away from positing explicitly interpreted grammatical structures (such as deep tree structures), preferring to learn patterns directly from data without prior linguistic assumptions. This raises a question that remains open: are computational systems purely applied tools separate from theoretical questions, or does their practical success carry real implications about the nature of human language and its mechanisms of acquisition? The question has returned with new urgency with the emergence of large language models and their capacity to produce grammatically coherent language without explicit grammatical programming.

## Applications and Social Impact

The field's applications have extended beyond machine translation to include automatic summarization, question answering, sentiment analysis, voice assistants, and dialogue systems. These applications have also provoked growing ethical and social debates about algorithmic bias derived from training data, and about the marginalization of languages with few computational resources, including Arabic in its many dialects despite its wide spread, in the development of these systems compared with English.

## Computational Linguistics and Arabic

Automatic processing of Arabic has faced particular challenges that have attracted independent research interest: the absence of diacritics in texts that are usually written without them (which makes the morphological decomposition of a single word ambiguous, sometimes even for humans without context); the richness of non-linear derivational morphology based on root and pattern; and the wide variation between Modern Standard Arabic and the many colloquial dialects, which often lack standardized spelling conventions. These challenges led specialist researchers to develop Arabic-specific morphological analysis tools (such as the Buckwalter Arabic Morphological Analyzer, AlKhalil Morpho Sys and MADAMIRA, which analyse an Arabic word into stem, pattern and affixes) because tools designed for languages with largely concatenative morphology such as English transfer poorly.

## Sources

- Jurafsky, Daniel; Martin, James H. (2023). *Speech and Language Processing* (3rd ed. draft). Pearson.
- Manning, Christopher D.; Schütze, Hinrich (1999). *Foundations of Statistical Natural Language Processing*. MIT Press.
- Pierce, John R.; et al. (1966). *Language and Machines: Computers in Translation and Linguistics* (the ALPAC report). National Academy of Sciences.
- Vaswani, Ashish; et al. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems* 30.
