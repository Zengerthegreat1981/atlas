---
slug: "con-autosegmental-phonology-goldsmith"
id: "CON-11903"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "phonology"
cultural_origin: "anglo-european"
title: "الصواتةُ متعدّدةُ الطبقات عند غولدسميث (Autosegmental Phonology)"
en: "Autosegmental Phonology (Goldsmith)"
crumb: "علم اللغة ← التوليدية وما بعدها ← الصواتةُ متعدّدةُ الطبقات عند غولدسميث"
edges:
- rel: "belongs_to", target: "sch-generative-phonology", target_type: "مدرسة"
related:
- id: "sch-generative-phonology", title: "الصرفُ التوليديُّ والصواتةُ التوليدية (Generative Phonology)", type: "مدرسة"
- id: "thk-john-goldsmith", title: "جون غولدسميث", type: "مفكر"
- id: "con-vowel-harmony", title: "توافقُ الصوائت (Vowel Harmony)", type: "مفهوم"
- id: "con-feature-geometry-clements", title: "هندسةُ السمات عند كليمنتس (Feature Geometry)", type: "مفهوم"
gaps: []
---

# الصواتةُ متعدّدةُ الطبقات عند غولدسميث

## Definition

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
- Goldsmith, J. A. (1990). *Autosegmental and Metrical Phonology*. Blackwell.

## References

- Kager, R. (1999). *Optimality Theory*. Cambridge University Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century*. University of Chicago Press.
- Haspelmath, M., & Sims, A. D. (2010). *Understanding Morphology*. Oxford University Press.

## محتوى عربي إضافي

إطارٌ صواتيٌّ صاغه جون غولدسميث (1976) يحرِّر التمثيلَ الصوتي من افتراض السلسلة الخطّية الواحدة الذي بُني عليه نموذجُ SPE عند تشومسكي وهالة، مستبدلاً إياه بتمثيلٍ عبر طبقاتٍ متوازية مترابطة.

## المشكلةُ: النغمةُ وتوافقُ الصوائت يتحدّيان الخطّية

الظواهرُ التي دفعت غولدسميث لهذا الابتكار: في كثيرٍ من اللغات النغمية، تمتدّ نغمةٌ واحدة (مرتفعةٌ أو منخفضة) عبر عدّة مقاطعَ متتالية، أو تبقى ثابتةً حتى بعد حذف المقطع الذي "حملها" أصلاً (فتنتقل إلى المقطع المجاور) — سلوكٌ يصعب تمثيلُه إن كانت النغمةُ مجرّد سمةٍ ملحَقة بقطاعٍ صوتيٍّ واحدٍ ضمن سلسلةٍ خطّية صارمة.

## الطبقاتُ المتوازية وخطوطُ الربط

الحلُّ: فصلُ التمثيل الصوتي إلى **طبقاتٍ متوازية مستقلّة** (Autosegmental Tiers) — طبقةٌ للقطاعات الصوتية القطعية (الصوامت والصوائت المتتالية)، وطبقةٌ منفصلة للنغمة (أو لسمة توافق الصوائت) — تُربَط هذه الطبقاتُ بـ**خطوط ربطٍ** (Association Lines) لا تُلزَم بعلاقةٍ واحدٍ لواحد؛ فقد ترتبط نغمةٌ واحدة بعدّة قطاعاتٍ متتالية (Spreading)، أو ينتقل خطُّ ربطٍ من قطاعٍ محذوف إلى القطاع المجاور (Stability) محافظاً على النغمة رغم حذف حاملها الأصلي.

## تفسيرُ توافق الصوائت

يُعالَج توافقُ الصوائت (Vowel Harmony) بالمنطق نفسِه: سمةٌ صوتية معيّنة (كخاصية "الأمامية" أو "الاستدارة") توضَع في طبقتها المستقلّة وتنتشر عبر خطوط الربط إلى كلّ الصوائت المتتالية المعنية في الكلمة الواحدة، بدل تكرار السمة نفسِها يدوياً على كلّ صائتٍ منفرد في تمثيلٍ خطّي.

## الأثر

صار هذا الإطارُ المعيارَ السائد لتحليل اللغات النغمية وظواهر توافق الصوائت عبر لغات العالم، وأثّر عميقاً في تطوّر النظرية الصواتية اللاحقة بما فيها بعضُ افتراضات تمثيل السمات في النظرية التفاؤلية، وصار أداةً تحليليةً لا غنى عنها في الوصف الصوتي المقارَن المعاصر.

## المصادر

- Goldsmith, John A. (1976). *Autosegmental Phonology* (PhD dissertation). MIT.
- Goldsmith, John A. (1990). *Autosegmental and Metrical Phonology*. Blackwell.
