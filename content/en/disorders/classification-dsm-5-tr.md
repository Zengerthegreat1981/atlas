---
slug: "classification-dsm-5-tr"
id: "CLS-0001"
type: "نظام تصنيف تشخيصي"
level: "مبتدئ"
title: "Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR)"
en: "Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR)"
crumb: "Psychology ← Disorders ← DSM-5-TR"
active_start: 2022
active_end: "مستمر"
language: "English"
part: "psychology"
edges: []
related:
- id: "classification-icd-11", title: "International Classification of Diseases, 11th Revision (ICD-11)", type: "نظام تصنيف تشخيصي"
gaps:
  - "The text of the introduction to Section I (the basics of using the manual) is not detailed here: not yet covered; the file covers the general structure only."
---
# Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR)

The official classification system of mental disorders issued by the American Psychiatric Association (APA) in its fifth, text-revised edition (2022). DSM-5-TR follows a categorical model of psychological conditions, and specifies for each disorder particular diagnostic criteria (criteria sets) required for clinical research and clinical practice. It is the most widely used diagnostic reference in the United States, and uses ICD-10-CM codes for insurance and official documentation purposes.

## The Clinical Ceiling

This file documents only the structure, history and scope of an official classification system (DSM-5-TR); it is not a diagnostic tool. Classifying any condition or symptom within the chapters of this manual does not constitute a diagnosis of any individual, and an actual diagnosis requires direct clinical assessment by a qualified specialist who applies the criteria of each disorder.

## Historical Context

The first edition of the DSM appeared in 1952. Its major editions followed (DSM-II 1968, DSM-III 1980, DSM-IV 1994, DSM-5 2013). The text revision DSM-5-TR appeared in 2022 with textual updates and updated ICD-10-CM codes, without radical changes to the categorical structure.

## General Structure

DSM-5-TR consists of three main sections:

- **Section I**: the basics of using the manual (concepts, approach, history of use).
- **Section II**: diagnostic criteria and codes, arranged in 22 chapters running from Neurodevelopmental Disorders to Paraphilic Disorders, followed by Other Mental Disorders and the additional chapters on medication-induced conditions and other conditions that may be a focus of clinical attention.
- **Section III**: assessment measures, culture and diagnosis, an alternative model for personality disorders, conditions for further study.

## The 22 Chapters (Section II)

1. Neurodevelopmental Disorders
2. Schizophrenia Spectrum and Other Psychotic Disorders
3. Bipolar and Related Disorders
4. Depressive Disorders
5. Anxiety Disorders
6. Obsessive-Compulsive and Related Disorders
7. Trauma- and Stressor-Related Disorders
8. Dissociative Disorders
9. Somatic Symptom and Related Disorders
10. Feeding and Eating Disorders
11. Elimination Disorders
12. Sleep-Wake Disorders
13. Sexual Dysfunctions
14. Gender Dysphoria
15. Disruptive, Impulse-Control, and Conduct Disorders
16. Substance-Related and Addictive Disorders
17. Neurocognitive Disorders
18. Personality Disorders
19. Paraphilic Disorders
20. Other Mental Disorders and Additional Codes
21. Medication-Induced Movement Disorders and Other Adverse Effects of Medication
22. Other Conditions That May Be a Focus of Clinical Attention

## Codes

DSM-5-TR uses **ICD-10-CM** codes (not ICD-11) for documentation purposes. In each disorder entry in the Atlas, the code is listed as the `dsm5tr_code` field in the frontmatter.

## Application in the Atlas

Every disorder file (`dis-`) is linked to this system through an edge of type `classified_in` pointing to `classification-dsm-5-tr`. The `dsm5tr_code` field in the frontmatter holds the specific diagnostic code for each disorder.

## Relation to ICD-11

- DSM-5-TR uses ICD-10-CM codes, while ICD-11 uses its own independent coding system.
- In several cases DSM-5-TR and ICD-11 differ in classification (for example: Complex PTSD as a separate diagnosis in ICD-11 with no counterpart in DSM-5-TR).
- Every `dis-` file carries another `classified_in` edge pointing to `classification-icd-11`, and an `icd11_code` field for comparison.

## Sources

- American Psychiatric Association. (2022). *Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR)*. American Psychiatric Association Publishing.
- American Psychiatric Association. (2013). *Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition (DSM-5)*. American Psychiatric Publishing.
