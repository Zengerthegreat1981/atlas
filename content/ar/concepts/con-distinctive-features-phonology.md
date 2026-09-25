---
slug: "con-distinctive-features-phonology"
id: "CON-11004"
type: "مفهوم"
part: "linguistics"
level: "متوسط"
linguistic_level: "phonology"
cultural_origin: "anglo-european"
title: "السماتُ التمييزية (Distinctive Features)"
en: "Distinctive Features"
crumb: "علم اللغة ← البنيويةُ ونشأةُ العلم الحديث ← السماتُ التمييزية"
edges:
- rel: "belongs_to", target: "sch-prague-linguistic-circle", target_type: "مدرسة"
related:
- id: "thk-nikolai-trubetzkoy", title: "نيكولاي تروبتسكوي", type: "مفكر"
- id: "con-phoneme", title: "الفونيم", type: "مفهوم"
- id: "sch-generative-phonology", title: "الصرفُ التوليديُّ والصواتةُ التوليدية (Generative Phonology)", type: "مدرسة"
gaps: []
---

# السماتُ التمييزية

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

وحداتٌ تحليليةٌ أصغرُ من الفونيم، تصف الخصائصَ النطقية أو السمعية الثنائية (أو المتدرِّجة) التي يُبنى منها كلُّ فونيمٍ في نظام اللغة الصوتي، كـ[صوتي±] (Voiced)، [أنفي±] (Nasal)، أو [استمراري±] (Continuant).

## من الفونيم إلى ما دونه

قبل هذا التحليل، كان الفونيمُ يُعامَل عادةً بوصفه أصغرَ وحدةٍ صوتيةٍ وظيفية غيرَ قابلةٍ للتجزئة. أظهر تروبتسكوي ثم ياكوبسون أن الفونيمَ نفسَه يمكن تحليلُه إلى حزمةٍ من السمات الأصغر، وأن هذه السماتِ (لا الفونيماتُ) هي الوحدةُ الحقيقية التي تعمل عليها القواعدُ الصواتية وتنتشر عبرها التأثيراتُ الصوتية بين الأصوات المتجاورة (كالتماثل الصوتي، Assimilation).

## الصوريةُ الثنائية

في صياغتها الأكثر تأثيراً (ياكوبسون وهالة، 1952)، تُمثَّل السماتُ قيماً ثنائيةً (+/−) تنطبق أو لا تنطبق على كلّ فونيم، بحيث يتحدَّد كلُّ فونيمٍ بمصفوفةٍ فريدة من هذه القيم — نظامٌ صوريٌّ سمح بتفسير أنماط التماثل والتناوب الصوتي عبر لغاتٍ متعدّدة بقواعدَ موحَّدة.

## الأثر

صار هذا المفهومُ ركيزةً أساسيةً في الصواتة التوليدية (نمط SPE عند تشومسكي وهالة)، وفي النظرية التفاؤلية اللاحقة، وفي تصنيف أنظمة الأصوات عبر لغات العالم نمطياً.

## المصادر

- Jakobson, Roman; Fant, C. Gunnar M.; Halle, Morris (1952). *Preliminaries to Speech Analysis*. MIT Press.
- Trubetzkoy, Nikolai S. (1939/1969). *Principles of Phonology*. University of California Press.
