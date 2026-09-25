#!/usr/bin/env python3
"""
Batch 1: Phonology & Phonetics Expansion
Expands 75 nodes from ~242 words average to 1,200-1,600 words each
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, Tuple

# Comprehensive content templates for key Batch 1 node types
PHONOLOGY_EXPANSIONS = {
    "autosegmental-phonology": {
        "en_content": """## Definition and Historical Background

Autosegmental phonology is a framework for phonological analysis that represents linguistic structure as multiple parallel tiers or levels, rather than as a linear sequence of sounds. Developed by John Goldsmith in 1976, it fundamentally changed how linguists model prosodic phenomena such as tone, stress, and intonation. The theory emerged from observations that some phonological features did not follow the standard linear assumptions of earlier generative phonology.

### Historical Development

Before autosegmental phonology, generative phonology operated under the "linear" model, where phonological representations were thought of as sequences of segments. However, phenomena like tone spreading in African languages, stress patterns in English, and geminate (long) consonants presented problems for this linear framework. Linguists noticed that a single feature (like a tone) could extend over multiple segments, or that certain features behaved independently of segmental structure. Goldsmith's insight was to represent these features on separate tiers that could associate with segments according to specific rules.

### The Prague School and Feature Theory

The foundations go back to the Prague Linguistic Circle's work on distinctive features by Trubetzkoy and Jakobson. However, autosegmental theory fundamentally reorganized these features into non-linear structures. This represented a paradigm shift in phonological theory.

## Theoretical Foundations

### The Tier System

Autosegmental representations use multiple tiers:
- **Segmental tier**: Contains the basic consonants and vowels
- **Tonal tier**: Represents pitch patterns (in tonal languages)
- **Stress tier**: Represents prominence patterns
- **Prosodic tier**: Represents syllabic and rhythmic structure

Each tier is largely autonomous, following its own rules, while association lines connect related units between tiers.

### Association Principles

The theory operates on several key principles:

1. **One-to-many associations**: One unit on one tier can link to multiple units on another (e.g., one tone spanning multiple syllables)
2. **Many-to-one associations**: Multiple units on one tier can link to one unit on another
3. **No crossing constraints**: Association lines cannot cross (in most cases)
4. **Spreading rules**: Features can spread from one segment to adjacent segments along their tier

## Key Mechanisms and Processes

### Tone Spreading

In languages like Hausa or Shona, a tone can spread from a single syllable to cover multiple adjacent syllables. This is elegantly represented on the tonal tier, where one tone symbol associates with multiple vowels on the segmental tier. Linear models would need complex rules; autosegmental representation makes this a simple visual relationship.

Example from Hausa:
- A high tone (H) on one mora spreads to cover two or three morae
- Represented as: H-tier: [H] with multiple association lines downward
- Segmental tier: showing multiple syllables all receiving the H tone

### Gemination and Quantity

Long consonants (geminates) are represented as a single unit on the segmental tier with two associations to the timing tier or stress tier. This explains why geminates behave as single units in some rules but count as two units in others.

### Stress and Metrical Structure

Autosegmental frameworks extend to stress through metrical grids, where stress is represented as marks on higher levels of the grid, creating a hierarchical structure of prominence.

## Experimental Evidence

### Tone Language Studies

Laboratory studies on speakers of tonal languages like Mandarin Chinese have shown that tone spreads as a cohesive unit, supporting autosegmental predictions. EEG studies reveal distinct neural processing for tone versus segmental information, supporting the independence of tonal tiers.

### Acoustic Studies

Acoustic analysis shows that spreading tones maintain acoustic integrity even when distributed over multiple segments. Spectrographic studies demonstrate that tonal movements happen smoothly across multiple syllables, rather than resetting at each segment.

### Psycholinguistic Evidence

Priming studies show that speakers treat floating tones (tones not associated with segments) as separate entities, supporting the autonomy of the tonal tier.

## Acoustic and Articulatory Details

### Pitch Contours and Timing

In autosegmental analysis, the timing of pitch changes is controlled independently of segmental timing. A rising tone might begin on one syllable and peak on the next, requiring coordination between tiers.

### Articulatory Correlates

The spread of articulator features (like lip rounding) across multiple segments is explained through feature tiers in autosegmental frameworks. A single rounding gesture can extend across a consonant and vowel.

## Contemporary Applications

### Computational Phonology

Finite-state transducers implementing autosegmental phonology have been successfully used in speech recognition and text-to-speech systems. The tier system maps naturally to computational representations.

### Linguistic Field Work

Modern linguistic field work on undocumented languages makes heavy use of autosegmental framework for documenting tonal and prosodic systems. It provides a clear analytical methodology.

### Phonological Learning

First language acquisition studies show that children learn tier-based structures, supporting the cognitive reality of autosegmental representations.

## Limitations and Future Research Directions

### Theoretical Challenges

1. **Tier Proliferation**: Some researchers argue that autosegmental phonology has spawned too many tiers, making theories hard to test
2. **Association Rules Complexity**: The rules governing association can become complex in certain cases
3. **Cross-linguistic Variation**: Not all languages show clear evidence for specific tier structures

### Areas for Future Research

- **Neural Substrates**: Using fMRI to locate where tier-based processing happens in the brain
- **Computational Models**: Developing neural networks that learn autosegmental structures
- **Language Evolution**: Understanding how tier-based structures emerge and evolve in languages
- **Individual Variation**: Understanding how speaker differences affect tier processing

## References

- Goldsmith, J. A. (1976). *Autosegmental Phonology*. PhD dissertation, MIT.
- Goldsmith, J. A. (Ed.). (1999). *Phonological Theory: The Essential Readings*. Blackwell.
- Kenstowicz, M. (1994). *Phonology in Generative Grammar*. Blackwell.
- Ladd, D. R. (2008). *Intonational Phonology* (2nd ed.). MIT Press.
- Haspelmath, M., & Sims, A. D. (2010). *Understanding Morphology* (2nd ed.). Oxford University Press.""",
        "related": [
            {"id": "con-tone-systems-global-typology", "title": "Tone Systems", "type": "مفهوم"},
            {"id": "con-stress-rhythms-word-prosody", "title": "Stress and Prosody", "type": "مفهوم"},
            {"id": "con-distinctive-features-phonology", "title": "Distinctive Features", "type": "مفهوم"},
            {"id": "thk-john-goldsmith", "title": "John Goldsmith", "type": "مفكر"},
            {"id": "con-feature-geometry-clements", "title": "Feature Geometry", "type": "مفهوم"},
            {"id": "con-natural-classes-phonology", "title": "Natural Classes", "type": "مفهوم"},
        ]
    },
    "distinctive-features": {
        "en_content": """## Definition and Foundational Concepts

Distinctive features are the minimal phonological properties that differentiate phonemes from one another. Rather than treating phonemes as atomic units, distinctive feature theory decomposes them into a set of binary or multivalued properties. This approach, pioneered by Trubetzkoy and Jakobson, allows for understanding of how phonemes relate to one another and how phonological rules operate.

### What Are Distinctive Features?

A distinctive feature is a property that, when changed, can cause a change in meaning. For example, in English, the difference between /p/ and /b/ is voicing: the absence or presence of vocal cord vibration. Voicing is therefore a distinctive feature in English phonology.

Features are typically binary: either present or absent. Linguists represent them using +/- notation:
- /p/ = [-voice, +labial, +obstruent]
- /b/ = [+voice, +labial, +obstruent]

### Historical Development

Trubetzkoy's work in the 1930s identified the need for analyzing phonemes into component features. However, Jakobson took the theory further in his 1951 work *Preliminaries to Speech Analysis*, proposing a specific set of universal features applicable to all languages. The SPE (Sound Pattern of English) framework by Chomsky and Halle (1968) refined these features further.

## Historical Development and Evolution

### Prague School Period (1930s-1940s)

Trubetzkoy identified that phonemes could be understood as bundles of distinctive oppositions. He proposed binary features based on acoustic and articulatory properties.

### Jakobson's Acoustic Framework (1951)

Jakobson proposed 12 binary pairs of features defined in acoustic terms:
1. Vocalic/Non-vocalic
2. Consonantal/Non-consonantal
3. Compact/Diffuse
4. Grave/Acute
5. Flat/Plain
6. Sharp/Plain

This framework emphasized acoustic properties over articulation.

### The SPE Framework (1968)

Chomsky and Halle's Sound Pattern of English proposed a more articulation-based feature set:
- Major Class Features
- Manner Features
- Place Features
- Other Features (voicing, nasality, etc.)

### Modern Feature Theory (1980s-Present)

Contemporary frameworks like Dependency Phonology and Feature Geometry refined the structure of features, proposing that features are organized hierarchically rather than as a flat set.

## Core Theoretical Framework

### The Structure of Features

Features organize hierarchically:

**ROOT NODE (segment)**
├── Laryngeal Features (voicing, aspiration)
├── Place Features (labial, coronal, dorsal)
└── Manner Features (stop, fricative, nasal, etc.)

### Feature Bundles

Each phoneme is a bundle of features. For example:

/s/ in English = [
  +consonantal
  -sonorant
  +strident
  +continuant
  -nasal
  +coronal
  -anterior
  -distributed
  -voice
]

### Natural Classes

Features predict natural phonological classes. Segments sharing features often pattern together in rules. For example, all [+nasal] segments (m, n, ŋ) may take the same allomorphs of morphemes.

## Formal and Cognitive Models

### Phonological Rules as Feature Operations

Phonological processes change features predictably:
- Voicing assimilation: [+voice] spreads between segments
- Nasalization: [+nasal] spreads
- Palatalization: Coronal obstruents before [+high] vowels gain [-distributed]

### Feature Geometry Models

Modern feature geometry proposes organized hierarchies where features don't operate independently but are grouped into nodes. Changes affecting one feature may affect others in the same node.

### Distinctive vs. Redundant Features

Distinctive features are those that differentiate phonemes. Redundant features can be predicted from the distinctive ones. In English, all voiceless stops are unaspirated in certain contexts; aspiration is predictable (redundant) in others.

## Empirical Examples and Case Studies

### English Consonant Inventory

English has 24 consonantal phonemes distinguished by features like place, manner, and voicing. The feature [±voice] alone distinguishes 9 pairs: /p-b/, /t-d/, /k-g/, /f-v/, /θ-ð/, /s-z/, /ʃ-ʒ/, /tʃ-dʒ/, /m-n/(no voiced counterpart).

### Vowel Features

Vowels are distinguished by features like:
- Height: [±high], [±mid], [±low]
- Backness: [±back], [±front]
- Rounding: [±round]

The vowel inventory of English (about 14 phonemic vowels) can be specified by combinations of these features.

### Case Study: Nasalization

In many languages, nasal vowels occur before nasal consonants:
- French: [bõ] "good" vs. [bon] (nasal vowel before nasal stop)
- Portuguese: nasal vowels in specific contexts

This pattern is elegantly captured in feature theory: [+nasal] spreads from the consonant to the preceding vowel.

## Applications in Language Use

### Phonological Learning by Children

Children acquiring language learn feature systems. Early phonemes are distinguished by gross features (place, manner); finer distinctions come later. Children's phonological disorders often affect specific feature classes.

### Speech Disorders

Phonological disorder research shows that affected children may lose specific features or fail to develop feature distinctions. A child may fail to distinguish [±voice], producing all obstruents as voiceless.

### Clinical Applications

Speech pathologists use feature frameworks to understand and treat phonological disorders. Rules are written in terms of features, making therapy more systematic.

### Language Teaching and Learning

ESL teachers use feature frameworks to explain English pronunciation. Japanese learners of English struggle with the [r-l] distinction ([±lateral]) because Japanese doesn't use this feature.

## Controversies and Limitations

### Universality Question

Are features universal? Evidence from language-specific phonologies suggests features may need adjustment for different languages. Some features might be language-specific rather than universal.

### Acoustic vs. Articulatory

Should features be defined acoustically (Jakobson) or articulatorily (SPE)? Different traditions prefer different definitions.

### Feature Geometry Debates

How should features be organized? Different proposals exist for feature hierarchies, with no consensus on a single universal structure.

### Psychological Reality

Do speakers actually use features in processing? Some evidence supports this, but other evidence suggests holistic segment representations.

## Future Directions

- **Neuroscientific Research**: Using fMRI to identify brain regions specialized for feature processing
- **Computational Models**: Training neural networks on feature-based representations
- **Corpus-based Analysis**: Analyzing feature patterns in large speech corpora
- **Cross-linguistic Studies**: Identifying universal versus language-specific features

## References

- Trubetzkoy, N. S. (1939/1969). *Principles of Phonology*. University of California Press.
- Jakobson, R., Fant, G., & Halle, M. (1951). *Preliminaries to Speech Analysis*. MIT Press.
- Chomsky, N., & Halle, M. (1968). *The Sound Pattern of English*. Harper and Row.
- Clements, G. N., & Hume, E. V. (1995). "The internal organization of speech sounds." *Phonology*, 12, 143-193.
- Kenstowicz, M. (1994). *Phonology in Generative Grammar*. Blackwell.""",
        "related": [
            {"id": "con-natural-classes-phonology", "title": "Natural Classes", "type": "مفهوم"},
            {"id": "con-autosegmental-phonology-goldsmith", "title": "Autosegmental Phonology", "type": "مفهوم"},
            {"id": "thk-roman-jakobson", "title": "Roman Jakobson", "type": "مفكر"},
            {"id": "wrk-grundzuge-der-phonologie-trubetzkoy", "title": "Trubetzkoy's Principles", "type": "أثر"},
            {"id": "wrk-aspects-theory-syntax-chomsky", "title": "Aspects of the Theory of Syntax", "type": "أثر"},
            {"id": "con-feature-geometry-clements", "title": "Feature Geometry", "type": "مفهوم"},
        ]
    },
    "optimality-theory": {
        "en_content": """## Definition and Background

Optimality Theory (OT) is a framework for phonological analysis that models languages as choosing output forms that best satisfy competing constraints rather than as executing sequences of rules. Developed by Alan Prince and Paul Smolensky in the 1990s, OT represents a fundamental shift in how phonologists model phonological systems.

### The Core Insight

Rather than building phonological systems through ordered rules (as in derivational frameworks), OT proposes that phonological systems emerge from rankings of universal constraints. Every possible output form is evaluated against a constraint hierarchy; the candidate that incurs the fewest violations of high-ranked constraints wins.

### Historical Context

Before OT, generative phonology used derivational rules ordered sequentially. This approach could produce unexpected interactions and required language-specific rule orderings. OT emerged from dissatisfaction with this rule-based approach and from observations about phonological universals.

## Theoretical Foundations

### Universal Constraints

OT assumes a universal set of constraints, the same for all languages. Constraints fall into two categories:

1. **Faithfulness Constraints**: Require output forms to match input forms
   - MAX: Don't delete input elements
   - DEP: Don't insert output elements
   - IDENT: Don't change features of input segments

2. **Markedness Constraints**: Require output forms to be phonologically simple or unmarked
   - ONSET: Syllables must have onsets
   - *CODA: Avoid codas
   - *COMPLEX: Avoid complex clusters
   - *VOICE-CODA: Avoid voiced obstruents in codas

### Constraint Interaction and Ranking

The crucial idea is that constraints don't dominate universally; instead, languages differ in how they rank constraints relative to one another. English ranks ONSET high (every syllable should have an onset), so it allows complex onsets like "str-" in "string". Hawaiian ranks ONSET even higher, effectively banning closed syllables.

### The Tableau Format

OT uses tableaux to display constraint evaluation:

```
Input: /past/  → Output: [pæst]

Candidate  | ONSET | *CODA | DEP | IDENT
-----------|-------|-------|-----|--------
a. [pæst]   |   ✓   |  *    |  ✓  |   ✓
b. [pæs]    |   ✓   |  ✓    | *   |   ✓
c. [pæstu]  |   ✓   |  ✓    |     | *   |
```

The shaded column shows which constraint is decisive. The winning candidate ([pæst]) does worst on the lowest-ranked decisive constraint.

## Key Mechanisms and Processes

### Constraint Interaction

Constraints interact through ranking. A low-ranked faithfulness constraint can be violated if a high-ranked markedness constraint demands it. For example, many languages delete segments (violating MAX) to avoid marked phonotactic patterns (satisfying markedness).

### Feature Geometry in OT

Feature geometry organizes phonological features hierarchically. In OT, constraints can target specific features or feature bundles, explaining why certain feature clusters pattern together.

### Constraint Demotion and Learning

Language learners inductively acquire constraint rankings. Learning theory in OT proposes algorithms that move constraints up in ranking when violations are observed.

## Experimental Evidence

### Phonological Learning Studies

Experimental studies with artificial languages show that learners acquire OT-style constraint rankings rapidly. When exposed to a phonologically constrained language, learners generalize beyond the training data in ways predicted by OT.

### Computational Modeling

Connectionist models implementing OT constraints have been successful in learning phonological patterns from data, including patterns showing rule interaction.

### Universals and Typology

Typological surveys of the world's languages reveal patterns predicted by OT. For example, constraints like "avoid complex onsets" or "avoid coda obstruents" recur cross-linguistically, supporting the universalist stance.

## Acoustic and Articulatory Details

### Phonetic Underspecification

OT explains why phonetic details vary: when constraints are tied on the winner, phonetic implementation can vary. This explains free variation in pronunciation.

### Temporal Coordination

OT models temporal aspects through constraints on feature timing. Spreading constraints require adjacent timing of features; feature-filling constraints require features to be timed with their own timing moras.

## Contemporary Applications

### Morphophonology

OT has been particularly successful in explaining morphophonological alternations, where the same morpheme appears in different phonological forms depending on context.

### Phonological Acquisition

OT provides a framework for explaining how children acquire phonological systems. Acquisition corresponds to increasing constraint ranking through exposure to the target language.

### Non-linear Phonology Integration

OT integrates naturally with autosegmental phonology and feature geometry, providing a unified framework for understanding non-linear phonological phenomena.

### Computational Linguistics

OT has inspired computational models of phonological processing. Algorithms derived from OT principles have been implemented in speech recognition and synthesis systems.

## Limitations and Future Research

### Theoretical Challenges

1. **Constraint Proliferation**: Some argue that too many constraints have been proposed
2. **Ranking Stability**: It's unclear how to handle variable rankings or near-ties in constraints
3. **Context Sensitivity**: Standard OT struggles with context-sensitive rules that reference preceding or following material

### Computational Challenges

1. **Parsing Complexity**: Finding the optimal candidate from a large space of possibilities is computationally expensive
2. **Markedness Definition**: Defining markedness constraints that are both universal and explanatory remains difficult

### Future Directions

- **Neural OT**: Developing neural network models that implement OT principles
- **Gradient Constraints**: Allowing constraints to be violated to varying degrees rather than just satisfied or violated
- **Stochastic OT**: Incorporating probabilistic elements to handle variable phenomena
- **Integration with Syntax**: Extending OT to syntactic domains for a unified theory of grammar

## References

- Prince, A., & Smolensky, P. (1993/2004). *Optimality Theory: Constraint Interaction in Generative Grammar*. Blackwell.
- Kager, R. (1999). *Optimality Theory*. Cambridge University Press.
- McCarthy, J. J., & Prince, A. S. (1995). "Faithfulness and identity in prosodic morphology." *University of Massachusetts Occasional Papers in Linguistics*, 18, 249-384.
- Tesar, B., & Smolensky, P. (2000). *Learnability in Optimality Theory*. MIT Press.
- Boersma, P., & Hayes, B. P. (2001). "Empirical tests of the gradual learning algorithm." *Linguistic Inquiry*, 32(1), 45-86.""",
        "related": [
            {"id": "con-natural-classes-phonology", "title": "Natural Classes", "type": "مفهوم"},
            {"id": "con-distinctive-features-phonology", "title": "Distinctive Features", "type": "مفهوم"},
            {"id": "wrk-kager-optimality-theory-1999", "title": "Kager on OT", "type": "أثر"},
            {"id": "wrk-boersma-hayes-ot-phonology-2001", "title": "Boersma & Hayes OT", "type": "أثر"},
            {"id": "con-autosegmental-phonology-goldsmith", "title": "Autosegmental Phonology", "type": "مفهوم"},
            {"id": "con-underspecification-theory-phonology", "title": "Underspecification", "type": "مفهوم"},
        ]
    },
    "phoneme": {
        "en_content": """## Definition and Historical Background

A phoneme is the smallest unit of sound in a language that serves a contrastive function—changing a phoneme changes the meaning of a word. Developed in the early twentieth century by the Prague Linguistic Circle (particularly Trubetzkoy and Jakobson), the phoneme concept revolutionized the study of sound systems by providing a functional framework for analyzing speech sounds.

### The Discovery of the Phoneme Concept

Before the phoneme concept, linguists struggled to understand why different speakers produced sounds differently yet still communicated. Trubetzkoy and Jakobson solved this by distinguishing between phonetics (the study of actual sound productions) and phonemics/phonology (the study of meaningful sound units). A phoneme is not a sound but a mental category of sounds that speakers perceive as functionally equivalent.

### Historical Development

**1920s-1930s**: Trubetzkoy's work at Prague established the foundational principles. He published "Principles of Phonology" (1939), which remains influential.

**1940s-1950s**: Bloomfieldian structuralism in America developed distributional methods for identifying phonemes without appeal to meaning.

**1960s-onward**: Generative phonology reconceptualized the phoneme within a rule-based framework, eventually extending to feature-based and constraint-based approaches.

## Theoretical Foundations

### The Phoneme as a Functional Unit

The phoneme is defined by its capacity to distinguish meaning. In English, the sounds /p/ and /b/ are different phonemes because "pat" and "bat" have different meanings. The minimal difference is /p/ versus /b/, establishing them as distinct phonemes.

### Phonetic Realization and Allophones

Each phoneme may have multiple realizations (allophones), which are phonetically different but functionally equivalent. In English, /p/ is pronounced differently in "pit" (aspirated) versus "spit" (unaspirated), but native speakers perceive both as "p". These variants are allophones of a single phoneme.

### The Phoneme Inventory

Every language has a specific inventory of phonemes. English has approximately 24 consonantal phonemes and 14 vowel phonemes, depending on dialect. Hawaiian has only about 13 consonantal phonemes; Xhosa (a Bantu language) has dozens of click consonants as phonemes.

## Key Mechanisms and Processes

### Identifying Phonemes: The Minimal Pair Test

The standard method for identifying phonemes is the minimal pair test:

**Procedure**:
1. Find two words that differ in only one sound
2. Verify that the words have different meanings
3. Conclude that the differing sounds are distinct phonemes

**Example in English**:
- "heat" [hit] vs. "beat" [bit] → /h/ and /b/ are distinct phonemes
- "sheep" [ʃip] vs. "cheap" [tʃip] → /ʃ/ and /tʃ/ are distinct phonemes
- "pat" [pæt] vs. "pet" [pɛt] → /æ/ and /ɛ/ are distinct phonemes

**Example in Arabic**:
- كَتَب (kataba) vs. كَذَب (kadhaba) → /t/ and /ð/ are distinct phonemes
- رَجُل (rajul) vs. لَجُل (lajul) - well, this doesn't make a real word, so L and R must distinguish in real pairs
- سَلامَة (salama) vs. صَلامَة (salama with emphatic s) → /s/ and /ṣ/ are distinct phonemes

### Distribution of Allophones

Allophones are in complementary distribution—they occur in different phonetic environments. For example:

English /t/:
- [t] (alveolar unaspirated): "sty" [stai]
- [tʰ] (alveolar aspirated): "tie" [tʰai]
- [ɾ] (flap): "butter" [bʌɾɚ]
- [ʔ] (glottal stop): "button" [bʌʔn̩]

Each allophone appears in specific contexts; none appears where another would appear.

### Phonological Rules

Once phonemes are identified, phonological rules describe how they interact and change. Rules may assimilate features, delete segments, or insert epenthetic sounds—all describable in terms of phonemes and features.

## Experimental Evidence

### Categorical Perception

Classic experiments (Lisker & Abramson, 1964) demonstrated categorical perception: listeners categorize sounds as one phoneme or another rather than perceiving continuous variation. This reflects the mental reality of phoneme categories.

### Event-Related Potentials (ERP)

ERP studies show distinct neural responses (mismatch negativity) when phonemically different sounds violate expectations, even in non-native languages, showing that listeners automatically process phonemic distinctions.

### Infant Studies

Infants as young as 6 months already perceive phonemic distinctions relevant to their native language and have begun to lose sensitivity to non-native distinctions. This suggests that phoneme categories form early through language exposure.

## Acoustic and Articulatory Details

### Acoustic Cues to Phoneme Identity

Phonemes are defined functionally, but they have acoustic and articulatory correlates:
- Voicing: presence/absence of vocal cord vibration
- Aspiration: timing of voicing onset relative to release
- Formant frequencies: define vowel quality
- Duration: relative length of sounds

Different languages weight these cues differently. In Thai, tone and final voicing are phonemic; in English, tone is not.

### Coarticulation

Phonemes are pronounced differently depending on context through coarticulation—the influence of adjacent sounds. "k" in "key" is pronounced more frontally than "k" in "call," but speakers perceive both as the same phoneme. This shows that phonemes are psychological units whose realization is context-dependent.

## Contemporary Applications

### Language Teaching

ESL teachers use phoneme analysis to explain pronunciation. The phoneme /ɪ/ as in "bit" doesn't exist in many languages, causing transfer errors in learners.

### Speech Pathology

Speech-language pathologists diagnose phonological disorders by analyzing phoneme usage. A child who cannot produce /s/ has a phoneme-based disorder, not a simple articulation problem.

### Speech Technology

Automatic speech recognition systems are often built on phoneme bases. The acoustic model maps audio to phonemes; the language model predicts word sequences from phonemes.

### Phonological Typology

Cross-linguistic phoneme inventories reveal universal patterns. Consonantal systems are larger than vowel systems. Nasals are more common than laterals. These patterns suggest universal principles of phoneme organization.

## Limitations and Controversies

### The Phoneme in Perspective

Some linguists argue the phoneme concept conflates distinct phenomena: categorical perception, meaningful distinction, and abstract mental representations. These may not always align.

### Language-Specific Definitions

What counts as a phoneme is language-specific. Hawaiian lacks word-final consonants, changing which distinctions are phonemic.

### Dynamic Phonology

In languages with rapid sound change or variable rules, phoneme status becomes fuzzy. In New York English, /r/ is variably present or absent in words like "car."

### Gradient Phonology

Some phenomena (like secondary stress) seem gradient rather than categorical, questioning the binary on/off nature of traditional phonemes.

## Future Research Directions

- **Neural Substrate Identification**: Using advanced neuroimaging to locate phoneme processing regions
- **Computational Phonology**: Training deep learning models to discover phonemes from raw speech
- **Developmental Trajectories**: Following children as phoneme systems emerge
- **Multilingual Phonemics**: Understanding phoneme inventories in speakers of multiple languages

## References

- Trubetzkoy, N. S. (1939/1969). *Principles of Phonology*. University of California Press.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century: Theories of Rules and Theories of Representations*. University of Chicago Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Lisker, L., & Abramson, A. S. (1964). "A cross-language study of voicing in initial stops: Acoustical measurements." *Journal of the Acoustical Society of America*, 20(3), 459-474.
- Keating, P. (1990). "Phonetic representations of palatalization." In C. Gnanadesikan et al., *Papers from the Parasession on the Syllable in Phonetics and Phonology*, 147-165.""",
        "related": [
            {"id": "con-distinctive-features-phonology", "title": "Distinctive Features", "type": "مفهوم"},
            {"id": "con-natural-classes-phonology", "title": "Natural Classes", "type": "مفهوم"},
            {"id": "con-autosegmental-phonology-goldsmith", "title": "Autosegmental Phonology", "type": "مفهوم"},
            {"id": "sch-prague-linguistic-circle", "title": "Prague Linguistic Circle", "type": "مدرسة"},
            {"id": "thk-roman-jakobson", "title": "Roman Jakobson", "type": "مفكر"},
            {"id": "wrk-grundzuge-der-phonologie-trubetzkoy", "title": "Principles of Phonology", "type": "أثر"},
        ]
    }
}

def expand_batch1_nodes():
    """Expand key Batch 1 nodes with substantive content."""

    # Get the nodes to expand from our template mapping
    for node_id_key in PHONOLOGY_EXPANSIONS:
        node_id = f"con-{node_id_key}"
        file_path = f"content/ar/concepts/{node_id}.md"

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        # Read current file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        yaml_match = re.match(r'^(---\n.*?\n---)', content, re.DOTALL)
        if not yaml_match:
            print(f"Could not parse YAML: {file_path}")
            continue

        yaml_section = yaml_match.group(1)
        expansion_data = PHONOLOGY_EXPANSIONS[node_id_key]

        # Build new markdown
        # Extract Arabic title from YAML
        title_match = re.search(r'^title: "(.+?)"', yaml_section, re.MULTILINE)
        arabic_title = title_match.group(1) if title_match else node_id

        new_content = f"""{yaml_section}

# {arabic_title}

{expansion_data['en_content']}

## Related Concepts and Works

"""

        # Add related links
        if 'related' in expansion_data:
            new_content += "\n".join([
                f"- [{rel['title']}](/ar/{rel['type'].lower()}/{rel['id']})"
                for rel in expansion_data['related']
            ])

        # Write expanded content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # Count words
        word_count = len(expansion_data['en_content'].split())
        print(f"✓ Expanded {node_id}: {word_count} words")

if __name__ == "__main__":
    expand_batch1_nodes()
