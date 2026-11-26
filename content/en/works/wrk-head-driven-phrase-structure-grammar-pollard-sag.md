---
slug: "wrk-head-driven-phrase-structure-grammar-pollard-sag"
id: "WRK-12219"
type: "أثر"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "Head-Driven Phrase Structure Grammar"
en: "Head-Driven Phrase Structure Grammar"
crumb: "Linguistics ← Works ← Head-Driven Phrase Structure Grammar"
dates: "United States · 1994"
country: "United States"
language: "English"
active_start: 1994
active_end: 1994
edges:
- rel: "belongs_to", target: "Lexical-Functional Grammar and HPSG", target_type: "مدرسة"
related: []
gaps: []
---

# Head-Driven Phrase Structure Grammar

The standard 1994 statement of Head-Driven Phrase Structure Grammar (HPSG), by Carl Pollard and Ivan A. Sag. It presents a full formal version of a non-transformational theory that represents phonological, syntactic and semantic information in unified feature structures called signs.

## The Formal Apparatus: Type Hierarchy and Feature Structures

The book provides a precise formal apparatus built on a "type hierarchy": a layered classification of linguistic entities (from the general sign down to the word and the phrase) in which each subtype inherits the features of the type above it, with the option of adding specific constraints. Well-formed sentences are derived through unification between compatible feature structures, with no transformational movement.

## The Head as the Axis of Phrase Structure

The framework holds that every grammatical phrase is "head-driven": the head word in a phrase (such as the verb in a verb phrase) determines most of the grammatical and semantic properties of the whole phrase. This happens through general compatibility principles, such as the Head Feature Principle, applied uniformly across all types of phrases. The grammatical category of a mother node is derived directly from its head daughter by the same rule in every tree, which reduces the need for special rules for each phrase type.

## Historical Context of Composition

HPSG took shape in the mid-1980s, in a broader turn away from the complexity of transformational grammar. Pollard and Sag drew on non-transformational work including Generalized Phrase Structure Grammar (Gerald Gazdar and colleagues), categorial grammar, and the Lexical-Functional Grammar of Joan Bresnan and Ronald Kaplan. They aimed at a declarative theory: well-formed sentences satisfy constraints together, rather than being produced by ordered transformations that convert one structure into another. Pollard and Sag's *Information-Based Syntax and Semantics*, volume 1 (1987), was the immediate precursor. A planned second volume did not appear. The 1994 book revised the framework and became its usual reference.

## Unified Representation of Linguistic Information

A key feature of HPSG is that it represents all levels of linguistic analysis (phonology, morphology, syntax, semantics and pragmatics) within a single unified feature structure called the "sign." The notion echoes Saussure's concept of the linguistic sign, but it is given precise formal detail through typed feature structures. Any word or phrase is therefore represented as a single object that carries its phonological information, its syntactic category (through a feature called *category*) and its semantic structure (through a feature called *content*) at the same time. This allows direct and constrained interaction between these levels without separate interfaces between them.

## Type Hierarchy and Multiple Inheritance

The book organises linguistic entities in a network of types that permits multiple inheritance: a subtype can inherit properties from more than one supertype at once. This allows economical expression of cross-cutting generalisations. For instance, nouns and adjectives share the property of gender and number agreement while differing in other properties, without repeating the same constraints in each type. The typed-feature-structure formalism has also been used in other grammar frameworks and in computational grammar engineering.

## Impact

The book became the founding reference for the HPSG framework, which gained wide adoption in computational linguistics because of its precise formalism, which can be applied directly in automatic parsers. It also influenced the later development of Sag's sign-based construction grammar. The framework has been used to describe the grammars of typologically diverse languages around the world, including attempts to describe some phenomena of Arabic grammar. Well-known computational resources have been developed for it, such as the LKB grammar development system (Copestake) and the Grammar Matrix (Bender and colleagues, University of Washington), which allows researchers to start building new HPSG-style grammars for additional languages from a shared core.

## Relation to the Arabic Grammatical Tradition

There is no historical link between HPSG and traditional Arabic grammar. Computational linguists have since written HPSG fragments for Standard Arabic, including treatments of agreement, case and relatively free word order, using typed feature structures to carry morphological information that English expresses more sparsely. Arabic was not part of the 1994 book's empirical base. Later grammars of other languages are the evidence usually cited for the framework's cross-linguistic use.

## Sources

- Pollard, Carl; Sag, Ivan A. (1994). *Head-Driven Phrase Structure Grammar*. University of Chicago Press.
- Pollard, Carl; Sag, Ivan A. (1987). *Information-Based Syntax and Semantics*. CSLI Publications.
- Sag, Ivan A.; Wasow, Thomas; Bender, Emily M. (2003). *Syntactic Theory: A Formal Introduction*. CSLI Publications.
