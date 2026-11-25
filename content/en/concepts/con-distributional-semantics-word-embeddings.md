---
slug: "con-distributional-semantics-word-embeddings"
id: "CON-11263"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "semantics"
cultural_origin: "anglo-european"
title: "Distributional Semantics and Word Embeddings"
en: "Distributional Semantics & Word Embeddings"
crumb: "Linguistics ← Concepts ← Distributional Semantics and Word Embeddings"
edges:
- rel: "belongs_to", target: "Computational Linguistics & NLP", target_type: "مدرسة"
related:
- id: "sch-computational-linguistics-nlp", title: "Computational Linguistics and Natural Language Processing", type: "مدرسة"
gaps: []
---

# Distributional Semantics and Word Embeddings

## Definition

Distributional semantics is an approach to studying word meaning. Rather than defining meaning logically or conceptually, it derives meaning statistically from the contexts of a word's actual use in large texts. It rests on the distributional hypothesis, formulated by the linguist John Rupert Firth in his famous saying: "You shall know a word by the company it keeps." Zellig Harris also laid its theoretical groundwork in the 1950s ("Distributional Structure," 1954), and count-based vector methods such as Latent Semantic Analysis (Deerwester et al., 1990) preceded the neural embeddings discussed below.

## From the Hypothesis to Computational Representation

Computationally, this hypothesis is implemented by representing each word as a numerical vector. The vector is derived from counting how often the word co-occurs with other words across a large text corpus. Semantically similar words therefore lie close together in vector space, while unrelated words lie far apart. This idea became the basis of modern word embeddings, which transform the linguistic unit from a discrete symbol into a point in a multidimensional geometric space.

## Word2Vec and GloVe

In 2013 Tomas Mikolov and colleagues at Google introduced the Word2Vec algorithm. It learns word vectors by training a simple neural network to predict neighboring words within a context window (the Skip-gram model), or to predict a word from its context (the CBOW model). A team at Stanford University presented a parallel alternative called GloVe (Global Vectors). It fits word vectors directly to corpus-wide word co-occurrence statistics, aiming to combine the strengths of count-based and prediction-based methods.

## Geometric Properties of the Semantic Space

Mikolov, Yih, and Zweig (2013) reported that some semantic relations appear as roughly regular offsets in this space. A much-cited case is that the vector for "king," minus "man," plus "woman," falls near "queen." The result is approximate: many analogies fail, and the offset method is a probe of the space rather than a definition of meaning.

## The Fundamental Limitation: Static Representation

These early representations are static. Each word type receives one vector, so they do not separate "bank" as a financial institution from "bank" as the side of a river. Contextual models assign a vector to each token in its sentence. ELMo (Peters et al. 2018) derives token representations from a bidirectional language model. BERT (Devlin et al. 2019) derives them from a Transformer pretrained with a masked-word objective.

## Impact

Distributional vectors changed much of computational language processing by replacing sparse symbolic encodings, such as one-hot vectors, with dense vectors in which distributional similarity is geometric. Contextual models and later large language models still learn representations from patterns of co-occurrence in text, although a token vector is no longer a single stored word type.

## Sources

- Firth, J. R. (1957). "A Synopsis of Linguistic Theory 1930-1955." In *Studies in Linguistic Analysis*. Blackwell.
- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space." *arXiv:1301.3781*.
- Mikolov, T., Yih, W.-t., & Zweig, G. (2013). "Linguistic Regularities in Continuous Space Word Representations." *Proceedings of NAACL-HLT 2013*, 746-751.
- Pennington, J., Socher, R., & Manning, C. D. (2014). "GloVe: Global Vectors for Word Representation." *Proceedings of EMNLP 2014*, 1532-1543.
- Peters, M. E., Neumann, M., Iyyer, M., Gardner, M., Clark, C., Lee, K., & Zettlemoyer, L. (2018). "Deep Contextualized Word Representations." *Proceedings of NAACL-HLT 2018*, 2227-2237.
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of NAACL-HLT 2019*, 4171-4186.
- Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). "Indexing by Latent Semantic Analysis." *Journal of the American Society for Information Science*, 41(6), 391-407.
- Harris, Z. S. (1954). "Distributional Structure." *Word*, 10(2-3), 146-162.
