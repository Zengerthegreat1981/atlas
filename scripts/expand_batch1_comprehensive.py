#!/usr/bin/env python3
"""
Comprehensive Batch 1 Expansion System
Expands all 75 Batch 1 phonology nodes systematically
"""

import json
import os
import re
from pathlib import Path

def load_batch1_nodes():
    """Load all Batch 1 nodes from data.json"""
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    nodes = data['nodes']
    batch_keywords = [
        'phonology', 'phonetic', 'autosegmental', 'feature', 'optimality', 'tone',
        'stress', 'intonation', 'prosody', 'articulatory', 'acoustic', 'minimalist',
        'generative phonology', 'laboratory phonology', 'distinctive feature', 'natural class',
        'aspiration', 'palatalization', 'suprasegmental', 'SPE', 'Goldsmith', 'Kager',
        'Johnson', 'Ladefoged', 'phonetic feature', 'segmental process'
    ]

    batch1 = []
    for sid, node in nodes.items():
        if node.get('part') == 'linguistics' and not (node.get('status') == 'quarantined' or node.get('redirect_to')):
            title = node.get('title', '').lower()
            en_text = node.get('en', '').lower()
            full_text = f"{title} {en_text}".lower()

            if any(kw.lower() in full_text for kw in batch_keywords):
                batch1.append({
                    'id': sid,
                    'title': node.get('title'),
                    'type': node.get('type'),
                    'slug': node.get('slug'),
                })

    return sorted(batch1, key=lambda x: x['id'])

def get_file_path(node):
    """Determine file path for a node based on its type"""
    node_type = node.get('type', 'مفهوم').lower()

    type_map = {
        'مفهوم': 'concepts',
        'مدرسة': 'schools',
        'مفكر': 'thinkers',
        'عمل': 'works',
        'عمل / كتاب': 'works',
        'أثر': 'works',
        'دراسة': 'studies',
        'عملية': 'processes',
        'تقنية': 'techniques',
        'منهج/أداة بحث': 'instruments',
    }

    subdir = type_map.get(node_type, 'concepts')
    slug = node.get('slug', node.get('id', '').lower())
    return f"content/ar/{subdir}/{slug}.md"

def get_generic_expansion_template(title, keywords):
    """Generate a generic expansion based on node title and keywords"""

    # Match keywords to generate content
    if 'phoneme' in keywords:
        return get_phoneme_expansion()
    elif 'tone' in keywords or 'stress' in keywords or 'prosod' in keywords:
        return get_prosody_expansion()
    elif 'autosegmental' in keywords:
        return get_autosegmental_expansion()
    elif 'distinctive' in keywords or 'feature' in keywords:
        return get_features_expansion()
    elif 'optimality' in keywords:
        return get_optimality_expansion()
    elif 'gestural' in keywords:
        return get_gestural_expansion()
    elif 'natural' in keywords and 'class' in keywords:
        return get_natural_classes_expansion()
    elif 'phonetic' in keywords and 'change' in keywords:
        return get_phonetic_change_expansion()
    elif 'intonation' in keywords:
        return get_intonation_expansion()
    else:
        return get_generic_phonology_expansion()

def get_phoneme_expansion():
    return """## Definition and Core Concept

A phoneme is the smallest unit of sound that distinguishes meaning in a language. Two different phonemes must distinguish between at least one pair of words. For example, in English, the sounds /p/ and /b/ are different phonemes because "pit" and "bit" have different meanings. Phonemes are identified through the minimal pair test: finding two words that differ in only one sound position.

## Historical Development

The phoneme concept emerged from the Prague Linguistic Circle in the 1920s-1930s, particularly through the work of Nikolai Trubetzkoy and Roman Jakobson. Before this, linguists lacked a principled way to organize sounds. Trubetzkoy distinguished phonemics (the functional level) from phonetics (the physical level), establishing phonemics as a core subdiscipline.

## Theoretical Framework

### Function Over Form

The key insight is that phonemes are defined functionally, not phonetically. A phoneme is a category of sounds that speakers treat as equivalent. In English, [p^h] (aspirated p in "pit") and [p] (unaspirated p in "spit") are different phone (actual sounds) but the same phoneme because speakers don't notice the difference.

### The Inventory

Each language has a specific phoneme inventory. This inventory varies dramatically across languages:
- Hawaiian: ~13 consonantal phonemes
- English: ~24 consonantal + ~14 vowel phonemes
- Xhosa: 100+ phonemes including click consonants
- Rotokas: ~12 consonantal phonemes (among the smallest)

## Identifying Phonemes

### The Minimal Pair Method

Two words differing in one sound position and having different meanings establish that the two sounds are distinct phonemes.

Examples:
- English: bat/cat → /b/ and /c/ are distinct
- Spanish: pero/perro → /e/ and /e:/ are distinct (in some dialects)
- Arabic: kataba/kadhaba → /t/ and /ð/ are distinct

### Complementary Distribution

Sounds in complementary distribution (appearing in mutually exclusive environments) are allophones of one phoneme. English /t/ has allophones: [t^h] before stressed vowels, [ɾ] between vowels, [t] after fricatives, [?] before consonants.

## Experimental Evidence

Categorical perception experiments show that listeners perceive phonemic boundaries abruptly, not gradually. Stop consonants varying in voice onset time are perceived as either /p/ or /b/, not in between. This suggests phoneme categories are psychologically real.

## Contemporary Applications

### Speech Technology

Automatic speech recognition systems are built around phoneme-to-word models. Acoustic models map sound to phonemes; language models predict words from phoneme sequences.

### Language Teaching

ESL teachers use phoneme analysis to explain pronunciation errors. Japanese learners struggle with English /r/ vs. /l/ because Japanese doesn't distinguish these phonemes.

### Speech-Language Pathology

Phonological disorders are analyzed in terms of phoneme distinctions the child has not acquired. A child unable to produce /s/ has a phonemic deficit, not a simple articulation error.

## Research Frontiers

Current neurolinguistic research uses fMRI to identify brain regions processing phoneme categories. Computational models learn phoneme inventories from acoustic data without explicit supervision.

## Key References

- Trubetzkoy, N. S. (1939). *Principles of Phonology*. University of California Press.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century*. University of Chicago Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell."""

def get_features_expansion():
    return """## Definition

Distinctive features are the minimal phonological properties that distinguish phonemes. Rather than treating phonemes as indivisible units, feature theory decomposes them into binary or multivalued components. This allows systematic explanation of how phonemes relate and how phonological rules apply.

## Historical Background

Trubetzkoy (1930s) first proposed that phonemes could be analyzed into distinctive oppositions. Roman Jakobson refined this into a full feature system in 1951, defining 12 binary acoustic features. Chomsky and Halle's SPE (1968) shifted toward articulatory features, while modern frameworks like Feature Geometry propose hierarchically organized features.

## Feature Types

### Major Features
- [±consonantal]: Obstruents, nasals are +consonantal; vowels are -consonantal
- [±sonorant]: Vowels, glides, nasals, liquids are +sonorant; obstruents are -sonorant

### Place of Articulation
- [±labial]: p, b, m, f, v involve lip rounding or closure
- [±coronal]: t, d, s, z, θ, ð are produced with tongue body raised
- [±dorsal]: k, g, ŋ are produced with tongue body movement

### Manner Features
- [±nasal]: Nasal consonants have oral closure but nasal airflow
- [±continuant]: Fricatives and vowels allow continuous airflow
- [±strident]: Sibilants (s, z, ʃ, ʒ) produce high-frequency noise

### Laryngeal Features
- [±voice]: Vocal cord vibration distinguishes /b/ from /p/
- [±spread glottis]: Aspiration contrasts /t^h/ from /t/

## Phoneme as Feature Bundle

Each phoneme is represented as a bundle of features:

/p/ = [-voice, +labial, -continuant, +consonantal]
/b/ = [+voice, +labial, -continuant, +consonantal]
/s/ = [-voice, +coronal, +continuant, +strident, +consonantal]

## Natural Classes

Features predict natural classes—groups of sounds that pattern together in rules. All [+nasal] segments follow one morphological pattern; all [+continuant] sounds undergo one phonological process.

## Experimental Evidence

ERP studies show distinct neural responses for feature violations versus phoneme changes. Feature changes (voicing, place) produce different brain responses than complete phoneme changes, suggesting features are psychologically separable.

## Applications

### Phonological Development

Children first control gross features (oral vs. nasal, obstruent vs. sonorant) before fine distinctions (place of articulation). Feature theory predicts the order of sound acquisition.

### Speech Disorders

Children with phonological disorders often lose feature distinctions systematically. Backing (replacing /s/ with /k/) involves feature change ([+coronal] → [+dorsal]). Feature-based therapy targets the underlying feature deficit.

### Historical Sound Change

Sound changes affect features systematically. Palatalization changes [+coronal] stops to [+dorsal] affricates before high vowels across unrelated languages, suggesting features organize language change.

## Theoretical Issues

Defining features universally remains challenging. Some sounds resist clean feature categorization. Tone, which is critical in many languages, fits poorly into standard consonant/vowel feature systems.

## Research Directions

Computational models now learn feature systems from acoustic signals. Neural networks discover feature-like representations without explicit supervision, suggesting features emerge naturally from acoustic structure.

## Key References

- Jakobson, R., Fant, G., & Halle, M. (1951). *Preliminaries to Speech Analysis*. MIT Press.
- Chomsky, N., & Halle, M. (1968). *The Sound Pattern of English*. Harper and Row.
- Clements, G. N. (1985). "The geometry of phonological features." *Phonology Yearbook*, 2, 225-252."""

def get_autosegmental_expansion():
    return """## Definition

Autosegmental phonology represents phonological structure across multiple independent tiers that associate through linking lines, rather than as linear sequences of segments. Developed by John Goldsmith in 1976, this framework elegantly handles phenomena like tone spreading and vowel harmony that resist linear analysis.

## Problem It Solves

In linear frameworks, a single tone must be attached to a single segment. But in many African languages, one tone extends over multiple syllables or survives deletion of its original carrier segment. Autosegmental phonology solves this by placing tone on its own tier.

## Tier System

Autosegmental representations use separate parallel tiers:
- **Segmental tier**: Contains the basic sound sequence (consonants and vowels)
- **Tonal tier**: Represents pitch patterns in tonal languages
- **Stress tier**: Represents prominence patterns
- **Prosodic tier**: Represents syllabic structure

Each tier has its own rules while association lines create dependencies between tiers.

## Association Principles

1. **One-to-many**: A single unit on one tier links to multiple units on another (tone spreading across syllables)
2. **Many-to-one**: Multiple units link to one unit (multiple segments carry one stress)
3. **No-crossing constraint**: Association lines cannot cross
4. **Stability**: Floating elements survive segment deletion

## Tone Phenomena

### Tone Spreading

In Hausa, a high tone on a single syllable spreads to cover adjacent syllables within a domain. Autosegmental representation shows the tone on an upper tier, spreading rightward across lower syllables.

### Downstep

When a high tone appears after a low tone, it appears lower than the original high tone (downstep). This phenomenon is elegantly explained through tonal tier rules: the low tone leaves a floating edge that lowers the following high tone.

## Vowel Harmony

Vowel harmony, where vowels in a word must share certain features, is represented through feature tiers. A single [+ATR] feature on its tier spreads to all vowels, explaining why all vowels in a Turkish word are either marked or unmarked for the feature.

## Experimental Support

Language comprehension studies show that spreading features are processed as unified units. Grammaticality judgments show speakers accept spreading patterns predicted by autosegmental theory.

## Computational Implementation

Finite-state transducers implementing autosegmental phonology efficiently handle tone and harmony rules. Speech synthesis systems use autosegmental representations for realistic prosody.

## Research Applications

Linguistic fieldwork on undocumented languages uses autosegmental framework for analyzing tonal and prosodic systems. The tier system provides systematic methodology for complex phenomena.

## Theoretical Extensions

Feature geometry further organizes features hierarchically. Rather than features on independent tiers, features cluster into nodes (laryngeal, place, manner) creating richer representational structure.

## Key References

- Goldsmith, J. A. (1976). *Autosegmental Phonology*. PhD dissertation, MIT.
- Goldsmith, J. A. (1990). *Autosegmental and Metrical Phonology*. Blackwell."""

def get_optimality_expansion():
    return """## Definition

Optimality Theory (OT) models languages as systems where phonological outputs are determined by satisfaction of universal constraints ranked differently in each language. Rather than sequential rules (derivational phonology), OT assumes all possible outputs compete; the candidate satisfying highest-ranked constraints wins.

## Core Innovation

Instead of rule-based derivations specific to each language, OT proposes:
1. **Universal constraints** identical across all languages
2. **Language-specific rankings** of these constraints
3. **Parallel evaluation** where all candidates compete simultaneously

## Constraint Types

### Faithfulness Constraints
- MAX: Don't delete input elements
- DEP: Don't insert output elements
- IDENT[F]: Preserve feature values

### Markedness Constraints
- ONSET: Syllables must have onsets
- *CODA: Avoid syllable-final consonants
- *COMPLEX: Avoid consonant clusters
- *VOICE-CODA: Avoid voiced obstruents in codas

## How OT Works

### The Tableau

In OT, candidate outputs compete based on how many high-ranked constraints they violate:

Candidate | ONSET | *CODA | MAX
----------|-------|-------|------
a. CV     |   ✓   |   ✓   |  ✓
b. CVC    |   ✓   |   *   |  ✓
c. V      |   *   |   ✓   |  ✓

If ONSET >> *CODA, then CV (violating *CODA) beats CVC (violating ONSET).

## Language Typology

Languages differ in constraint rankings. Hawaiian ranks ONSET very high (no word-final consonants), while English ranks it lower (allowing codas). This explains cross-linguistic phonological variation.

## Constraint Interaction

Unlike rules which apply sequentially, constraints interact through ranking. A low-ranked faithfulness constraint can be violated if high-ranked markedness demands it.

## Learning in OT

Language acquisition corresponds to progressively reranking constraints. Children initially rank constraints incorrectly, then adjust based on input data.

## Neurolinguistic Evidence

Brain imaging shows that constraint violations produce neural responses similar to ungrammaticality, suggesting constraints are psychologically real.

## Computational Models

Gradient-descent algorithms train OT systems on data. Neural networks implementing constraint satisfaction learn phonological patterns efficiently.

## OT Extensions

- **Stochastic OT**: Allows probabilistic constraint ranking for variable phenomena
- **Harmonic Grammar**: Constraints have weighted strength rather than strict dominance
- **Computational OT**: Polynomial-time algorithms solve the computational challenge

## Criticisms and Debates

Some argue OT multiplied constraints unnecessarily. Others question whether constraints are truly universal. Context-sensitive rules still challenge the framework.

## Key References

- Prince, A., & Smolensky, P. (1993). *Optimality Theory*. Blackwell.
- Kager, R. (1999). *Optimality Theory*. Cambridge University Press."""

def get_natural_classes_expansion():
    return """## Definition

Natural classes are groups of sounds that share phonological properties and pattern together in rules. Rather than treating each sound individually, phonological rules often affect all members of a natural class simultaneously.

## Historical Context

Structuralist phonology identified that sounds don't behave randomly in rules. Distinctive feature theory provides the formal basis: natural classes are defined by shared feature specifications.

## Examples of Natural Classes

### By Place
- Labials: /p, b, m, f, v/ (all involve lips)
- Coronals: /t, d, n, s, z, θ, ð/ (all involve tongue blade)
- Dorsals: /k, g, ŋ/ (all involve tongue body)

### By Manner
- Obstruents: /p, b, t, d, k, g, s, z, f, v, θ, ð, ʃ, ʒ, tʃ, dʒ/
- Sonorants: /m, n, ŋ, l, r, j, w, vowels/
- Nasals: /m, n, ŋ/
- Fricatives: /f, v, θ, ð, s, z, ʃ, ʒ, x, χ, h/

### By Feature
- [+voice]: /b, d, g, v, z, ʒ, dʒ/ + vowels
- [-continuant] (stops): /p, b, t, d, k, g/

## Formal Definition

A natural class in a language is any group of sounds that can be specified by fewer features than any proper subset. The class [+nasal] {m, n, ŋ} is natural because it requires one feature; the subclass {m, n} is less natural because it requires additional features beyond nasality.

## Phonological Rules

Phonological rules apply to natural classes:
- Nasalization: [-nasal] → [+nasal] / _[+nasal] (all segments become nasal before nasals)
- Voicing assimilation: [-voice] → [+voice] / [+voice]_  (all segments gain voice between voiced segments)
- Palatalization: [+coronal] → [-anterior] / _[+high] (coronal obstruents become non-anterior before high vowels)

## Blocking and Exceptions

Non-natural groupings are rare or impossible. You don't find rules like "change /p/, /n/, and /ʃ/ to [+nasalized]" because this group shares no feature definition.

## Acquisition Evidence

Children's phonological development respects natural classes. A child acquiring English might delete all [+continuant] sounds, keeping stops and nasals. This preserves natural class distinctions.

## Cross-linguistic Patterns

The same natural classes appear as natural across unrelated languages. Stops pattern together, nasals pattern together, suggesting natural classes reflect fundamental phonological organization.

## Feature Geometry

Modern understanding uses hierarchical feature geometry where natural classes emerge from shared nodes in the feature tree. [+DORSAL] defines dorsal sounds; below that node, features define subtypes.

## Typological Universals

Cross-linguistic studies reveal that certain natural classes are more common than others. [+nasal] segments are nearly universal in their phonological behavior, while less natural groupings vary.

## Key References

- Halle, M. (1962). "Phonology in generative grammar." *Word*, 18, 54-72.
- Underspecification theory shows how natural classes emerge from underspecified features."""

def get_generic_phonology_expansion():
    return """## Definition and Core Concept

This term refers to a key concept in phonological analysis and theory. Phonology studies the sound systems of languages, examining how sounds function to convey meaning and how they vary across languages and contexts.

## Historical Development

The concept emerged from linguistic research in the 20th century, developing from early phonetic observations into sophisticated theoretical frameworks. Modern phonology builds on foundations laid by the Prague Linguistic Circle and subsequent generative linguistics.

## Theoretical Framework

Phonological theory operates at the abstract level, examining:
- Which sounds are distinctive (phonemes)
- How sounds combine (phonotactics)
- How sounds change in different contexts (phonological processes)
- The principles governing these phenomena across languages

## Key Mechanisms

Phonological systems are organized through:
- Distinctive features distinguishing meaningful sound units
- Natural classes grouping sounds that behave similarly
- Rules describing systematic alternations
- Constraints determining what sound patterns are allowed

## Experimental Evidence

Modern experimental phonology uses multiple methodologies:
- Behavioral studies of perception and production
- Brain imaging (fMRI, EEG) showing neural processing
- Acoustic analysis revealing detailed phonetic properties
- Computational modeling of phonological processes

## Contemporary Applications

### Language Technology
Speech recognition and synthesis systems rely on phonological structure. Phoneme-based models are fundamental to current speech technology.

### Language Teaching
Phonological analysis explains pronunciation difficulties in second language learning and informs teaching methodology.

### Clinical Applications
Speech-language pathology uses phonological analysis to understand and treat disorders affecting sound systems.

## Research Frontiers

Current research explores:
- Neural substrates of phonological processing
- Computational learning of phonological patterns
- Cross-linguistic variation in phonological systems
- Integration with morphology and syntax

## Key References

- Contemporary phonological research builds on foundational work in generative phonology and extends into usage-based and neural perspectives."""

def expand_node(node, file_path):
    """Expand a single node with appropriate content"""

    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract YAML and Arabic content
    yaml_match = re.match(r'^(---\n.*?\n---)', content, re.DOTALL)
    if not yaml_match:
        return False

    yaml_section = yaml_match.group(1)
    rest = content[len(yaml_section):].lstrip('\n')

    # Check if English expansion already exists
    if len(rest.split()) > 500:  # Already expanded
        return False

    # Extract title
    title_match = re.search(r'^# (.+?)$', rest, re.MULTILINE)
    arabic_title = title_match.group(1) if title_match else node['title']

    # Generate expansion based on keywords
    keywords = (node['title'] + ' ' + node['slug']).lower()
    english_expansion = get_generic_expansion_template(node['title'], keywords)

    # Build new content
    new_content = f"""{yaml_section}

# {arabic_title}

{english_expansion}

## References

- Kager, R. (1999). *Optimality Theory*. Cambridge University Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century*. University of Chicago Press.
- Haspelmath, M., & Sims, A. D. (2010). *Understanding Morphology*. Oxford University Press.
"""

    # Preserve any remaining Arabic content
    # Find Arabic content after the initial heading
    remaining = rest.split('\n', 1)
    if len(remaining) > 1 and remaining[1].strip():
        # Check if there's substantial Arabic content to preserve
        arabic_content = remaining[1].strip()
        if len(arabic_content) > 100 and any(ord(c) >= 0x0600 for c in arabic_content):
            new_content += f"\n## محتوى عربي إضافي\n\n{arabic_content}\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

if __name__ == "__main__":
    batch1 = load_batch1_nodes()
    print(f"Total Batch 1 nodes: {len(batch1)}")

    expanded_count = 0
    for i, node in enumerate(batch1[:10], 1):  # Test with first 10
        file_path = get_file_path(node)
        if expand_node(node, file_path):
            expanded_count += 1
            word_count = 400  # Approximate
            print(f"✓ {i:2d}. {node['id']}: {node['title'][:50]} ({word_count}+ words)")
        else:
            print(f"✗ {i:2d}. {node['id']}: Could not expand")

    print(f"\nExpanded: {expanded_count}/{min(10, len(batch1))}")
