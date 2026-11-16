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

These representations revealed striking mathematical properties. Semantic relations between words are reflected in vector arithmetic. Subtracting the vector for "man" from the vector for "king" and adding the vector for "woman" yields a vector close to "queen." This suggests that the learned vector space captures some analogical relations without explicit guidance, relying only on patterns of contextual distribution in the corpus, although such analogy results are approximate and not uniformly reliable.

## The Fundamental Limitation: Static Representation

The fundamental weakness of these early representations is that they are static. Each word receives one fixed vector, regardless of its intended meaning in a particular use. They cannot distinguish between "bank" in the sense of a financial institution and "bank" in the sense of a riverbank. This limitation led to the emergence of contextual vector representations such as ELMo and BERT, which derive a different vector for each actual occurrence of a word according to its specific sentence.

## Impact

Distributional semantics revolutionized computational natural language processing. It replaced the discrete, symbolic representation of words (such as one-hot encoding) with a dense geometric space that captures semantic similarity automatically. It became an important foundation for subsequent language-processing architectures, including contextual models and large language models, which learn their representations from distributional patterns in text.

## Sources

- Firth, J. R. (1957). "A Synopsis of Linguistic Theory 1930-1955." In *Studies in Linguistic Analysis*. Blackwell.
- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space." *arXiv:1301.3781*.
- Pennington, J., Socher, R., & Manning, C. D. (2014). "GloVe: Global Vectors for Word Representation." *Proceedings of EMNLP 2014*.
- Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). "Indexing by Latent Semantic Analysis." *Journal of the American Society for Information Science*, 41(6), 391-407.
- Harris, Z. S. (1954). "Distributional Structure." *Word*, 10(2-3), 146-162.
