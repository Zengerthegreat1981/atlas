---
slug: "con-agree-operation-feature-checking"
id: "CON-11689"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "عمليةُ الاتفاق وفحصُ السمات (Agree & Feature Checking)"
en: "Agree & Feature Checking"
crumb: "علم اللغة ← التوليدية وما بعدها ← عمليةُ الاتفاق وفحصُ السمات"
edges:
- rel: "belongs_to", target: "sch-minimalist-program", target_type: "مدرسة"
related:
- id: "sch-minimalist-program", title: "البرنامجُ الأدنويّ (The Minimalist Program)", type: "مدرسة"
- id: "con-merge-operation-minimalism", title: "عمليةُ الدمج (Merge)", type: "مفهوم"
- id: "con-phase-theory-minimalism", title: "نظريةُ الأطوار (Phase Theory)", type: "مفهوم"
- id: "thk-noam-chomsky", title: "نعوم تشومسكي", type: "مفكر"
gaps: []
---

# عمليةُ الاتفاق وفحصُ السمات

## Definition

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
- Clements, G. N. (1985). "The geometry of phonological features." *Phonology Yearbook*, 2, 225-252.

## References

- Kager, R. (1999). *Optimality Theory*. Cambridge University Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century*. University of Chicago Press.
- Haspelmath, M., & Sims, A. D. (2010). *Understanding Morphology*. Oxford University Press.

## محتوى عربي إضافي

عمليةٌ حسابيةٌ ثانية أساسية في البرنامج الأدنويّ إلى جانب الدمج، تُنظِّم كيفية توافق العناصر النحوية في سماتٍ صرفية معيَّنة (كالعدد والجنس والشخص) عبر مسافاتٍ نحويةٍ قد تكون بعيدة داخل بنية الجملة، دون أن تتطلّب بالضرورة حركةً ظاهرة.

## السماتُ المفسَّرة وغيرُ المفسَّرة

يفترض هذا الإطارُ أن كلَّ عنصرٍ نحوي يحمل حزمةً من "السمات" (Features)، بعضُها "مفسَّرٌ" دلالياً (كسمة الجمع على الاسم نفسِه، التي تحمل معنًى فعلياً) وبعضُها "غيرُ مفسَّر" (كسمة الجمع المكرَّرة على الفعل المطابِق له، التي لا تضيف معنًى جديداً بل تعكس فقط توافقاً نحوياً). يجب "حذفُ" السمات غير المفسَّرة قبل نهاية الاشتقاق (وإلا فشل الاشتقاقُ نحوياً)، وتتحقّق عمليةُ الحذف هذه عبر آلية الاتفاق.

## آليةُ البحث عن المطابق

تعمل عمليةُ الاتفاق عبر "بحثٍ" (Probe) يُطلقه عنصرٌ يحمل سمةً غيرَ مفسَّرة (كالفعل الباحث عن سمة عدد) عن عنصرٍ آخر أسفلَ منه في بنية الجملة يحمل السمةَ نفسَها بشكلٍ مفسَّر (كالاسم الفاعل)؛ حين يجد الفعلُ "الهدفَ" (Goal) المناسب، تُنسَخ قيمةُ السمة من الهدف إلى الباحث، فتُحذَف سمتُه غيرُ المفسَّرة. تفسّر هذه الآليةُ ظاهرةَ الاتفاق النحوي (بين الفعل وفاعله، أو الصفة وموصوفها) دون حاجةٍ لحركةٍ نحويةٍ ظاهرة في كثيرٍ من الحالات.

## الأثر

وحّدت عمليةُ الاتفاق تفسيرَ ظواهرَ اتفاقٍ نحويٍّ متنوّعة عبر لغات العالم في آليةٍ حسابيةٍ واحدة، مكمِّلةً عمليةَ الدمج في تشكيل الجهاز الحسابي الأدنويّ الأساسي للاشتقاق النحوي.

## المصادر

- Chomsky, Noam (2000). "Minimalist Inquiries: The Framework." In Martin, R.; Michaels, D.; Uriagereka, J. (eds.), *Step by Step*. MIT Press.
- Chomsky, Noam (2001). "Derivation by Phase." In Kenstowicz, M. (ed.), *Ken Hale: A Life in Language*. MIT Press.
