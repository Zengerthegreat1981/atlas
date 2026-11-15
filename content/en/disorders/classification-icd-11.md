---
slug: "classification-icd-11"
id: "CLS-0002"
type: "نظام تصنيف تشخيصي"
level: "مبتدئ"
title: "International Classification of Diseases, 11th Revision (ICD-11)"
en: "International Classification of Diseases, 11th Revision (ICD-11)"
crumb: "Psychology ← Disorders ← ICD-11"
active_start: 2019
active_end: "مستمر"
language: "English"
part: "psychology"
edges: []
related:
- id: "classification-dsm-5-tr", title: "Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR)", type: "نظام تصنيف تشخيصي"
gaps:
  - "The detailed clinical descriptions within the 2024 CDDR for each subcategory: not yet covered; the file covers only the structure of Chapter Six."
  - "Update releases of ICD-11 after 2022: not yet covered."
---
# International Classification of Diseases, 11th Revision (ICD-11)

The official classification system adopted by the World Health Organization (WHO) for diseases and mental health, the eleventh revision. It was adopted in May 2019 by the WHO member states, and came into force on 1 January 2022. ICD-11 covers all diseases (not only mental disorders), and Chapter Six (Chapter 06) covers mental, behavioural, and neurodevelopmental disorders.

## The clinical ceiling

This file documents only the structure of an official classification system adopted by the WHO (ICD-11), its history, and its scope; it is not a diagnostic tool. Listing a category within Chapter Six here does not constitute a diagnosis of any individual, and actual diagnosis requires the application of the CDDR criteria by a qualified specialist.

## Historical context

ICD-1 was issued in 1893 (the Bertillon classification), and developed through successive editions. ICD-10 (1992) was the internationally adopted edition for two decades. ICD-11 (2019) is the first substantial update since ICD-10, and included a broad restructuring of the chapter on mental disorders, adopting dimensional models in several cases (such as personality disorders).

## Structure of Chapter Six (Chapter 06: Mental, behavioural or neurodevelopmental disorders)

- **6A00-6A0Z**: Neurodevelopmental disorders
- **6A20-6A2Z**: Schizophrenia or other primary psychotic disorders
- **6A40-6A4Z**: Catatonia
- **6A60-6A8Z**: Mood disorders
- **6B00-6B0Z**: Anxiety or fear-related disorders
- **6B20-6B2Z**: Obsessive-compulsive or related disorders
- **6B40-6B4Z**: Disorders specifically associated with stress
- **6B60-6B6Z**: Dissociative disorders
- **6B80-6B8Z**: Feeding or eating disorders
- **6C00-6C0Z**: Elimination disorders
- **6C20-6C2Z**: Disorders of bodily distress or bodily experience
- **6C40-6C5Z**: Disorders due to substance use or addictive behaviours
- **6C70-6C7Z**: Impulse control disorders
- **6C90-6C9Z**: Disruptive behaviour or dissocial disorders
- **6D10-6D11.5**: Personality disorders and related traits
- **6D30-6D3Z**: Paraphilic disorders
- **6D50-6D5Z**: Factitious disorders
- **6D70-6E0Z**: Neurocognitive disorders
- **6E20-6E2Z**: Mental or behavioural disorders associated with pregnancy, childbirth or the puerperium
- **6E40**: Psychological or behavioural factors affecting disorders or diseases classified elsewhere
- **6E60-6E6Z**: Secondary mental or behavioural syndromes associated with disorders or diseases classified elsewhere
- **6E8Y**: Other specified mental, behavioural or neurodevelopmental disorders
- **6E8Z**: Mental, behavioural or neurodevelopmental disorders, unspecified

## Main differences from DSM-5-TR

1. **Complex PTSD as a separate diagnosis**: ICD-11 includes Complex PTSD (6B41) as an independent entity, whereas DSM-5-TR does not include it as a separate diagnosis.
2. **Dimensional personality disorders**: ICD-11 adopts a dimensional model with 5 prominent traits (Negative Affectivity, Detachment, Disinhibition, Dissociality, Anankastia) in place of DSM-5-TR's categorical classification.
3. **Prolonged Grief Disorder**: ICD-11 introduced it first (6B42), and DSM-5-TR adopted it in 2022.
4. **Bipolar and Depressive organization**: ICD-11 groups them under "Mood disorders", whereas DSM-5-TR separates them as two independent chapters.
5. **Substance-related grouping**: ICD-11 uses the grouping "Disorders due to substance use or addictive behaviours" (including gambling and gaming), whereas DSM-5-TR uses "Substance-Related and Addictive Disorders" and, separately, substance/medication-induced disorders within other chapters.
6. **Gaming Disorder**: ICD-11 includes it in Chapter Six (6C51); DSM-5-TR places it under "Conditions for Further Study".

## The codes

ICD-11 uses a new, independent code system, different from ICD-10. Each disorder has a code beginning with 6A, 6B, 6C, 6D, or 6E according to the subchapter. The code is entered as the `icd11_code` field in the frontmatter.

## Application in the Atlas

Every `dis-` file is linked to this system through an edge of type `classified_in` pointing to `classification-icd-11`. The `icd11_code` field in the frontmatter holds the specific diagnostic code for each disorder.

## The clinical documents (CDDR)

In 2024 the WHO issued a separate guide, "Clinical Descriptions and Diagnostic Requirements for ICD-11 Mental, Behavioural and Neurodevelopmental Disorders (CDDR)", used as a clinical diagnostic tool for the mental disorders covered in ICD-11.

## Sources

- World Health Organization. (2019). *International Classification of Diseases, 11th Revision (ICD-11)*, adopted by the 72nd World Health Assembly; in effect from 1 January 2022. WHO.
- World Health Organization. (2024). *Clinical Descriptions and Diagnostic Requirements for ICD-11 Mental, Behavioural and Neurodevelopmental Disorders (CDDR)*. WHO.
