# Disorders Scope List — Atlas Project
## DSM-5-TR + ICD-11 Current Clinical Categories

**Status:** planning artifact (not part of atlas output)
**Date:** 2026-08-20
**Scope:** Current clinical categories only. Historical/retired DSM-III/IV diagnoses **deferred indefinitely** (do not touch).

---

## Schema (Final, agreed 2026-08-20)

```yaml
---
slug: "dis-ocd"  # kebab-case, consistent with existing dis- and tec-
id: "[DRAFT-UNKNOWN]"
type: "اضطراب/حالة إكلينيكية"
level: "مبتدئ" | "متوسط" | "متقدم"
title: "اضطراب الوسواس القهري"
en: "Obsessive-Compulsive Disorder (OCD)"
crumb: "الاضطرابات والحالات الإكلينيكية ← فصل DSM-5-TR ← الاسم العربي"
dsm5tr_code: "300.3"   # DSM-5-TR ICD-10-CM code
icd11_code: "6B20"    # ICD-11 code
active_start: YYYY
active_end: "مستمر"
language: "متعدد اللغات"
edges:  # flow style, one line per item (NOT multi-line block — match existing atlas convention)
  - rel: "classified_in", target: "classification-dsm-5-tr", target_type: "نظام تصنيف"
  - rel: "classified_in", target: "classification-icd-11", target_type: "نظام تصنيف"
related:  # simple list, no extra fields. Rationale + stage go in body section.
  - id: "tec-cbt-exp-in-vivo-exposure-with-response-prevention", title: "...", type: "تقنية/تدخل علاجي"
  - id: "syn-obsessive-thoughts", title: "الأفكار الوسواسية", type: "متلازمة"
  ...
gaps:  # ≥2 required
  - "لم يُراجع من مصدر أولي مباشر بعد."
  - "لا يوجد اقتباس مباشر موثوق متاح."
---
```

**Stub files (real, in `content/ar/drafts/disorders/`):**
- `classification-dsm-5-tr.md` (✅ created 2026-08-20)
- `classification-icd-11.md` (✅ created 2026-08-20)

These are the real targets for `classified_in` edges. They are `type: "نظام تصنيف"` (a new type, but acceptable since the build script is generic over type strings).

**Related section rules:**
- Plain list (id, title, type) — no priority/stage fields
- Rationale + stage + severity go in body section "التقنيات المرتبطة حسب المدرسة والمرحلة" (added per file)
- Cross-link to `syn-` files (already exist for: acute-anxiety, panic, depressive-symptoms, anger, emotional-numbing, insomnia, chronic-pain, obsessive-thoughts, craving-urge, loneliness-isolation, hypervigilance, dissociation)

**Disorders tiering:**

**Tiering logic:**
- **Tier A** (high relevance): CBT/ACT/DBT are established first/second-line treatments. Build first.
- **Tier B** (moderate relevance): These schools are adjunctive, third-line, or partial-evidence. Build after A.
- **Tier C** (low/no direct CBT-ACT-DBT relevance): Pharmacological or other primary. Build as thin reference-only entries with honest `gaps`.

**Count:** Tier A = 23 · Tier B = 27 · Tier C = 60+ · **Total = 110+** (exact count depends on how aggressively "Other Specified"/"Unspecified" catch-alls are split — typically a single file per category is built, treating specifiers as `notes` fields).

---

## Tier A — High Relevance (Build First, 23 disorders)

### Anxiety Disorders (6)
- `dis-separation-anxiety` — Separation Anxiety Disorder · DSM-5-TR: 309.21 · ICD-11: 6B05
- `dis-selective-mutism` — Selective Mutism · DSM-5-TR: 312.23 · ICD-11: 6B06
- `dis-specific-phobia` — Specific Phobia · DSM-5-TR: 300.29 · ICD-11: 6B03
- `dis-social-anxiety-disorder` — Social Anxiety Disorder · DSM-5-TR: 300.23 · ICD-11: 6B04
- `dis-panic-disorder` — Panic Disorder · DSM-5-TR: 300.01 · ICD-11: 6B02 (✅ already exists as `dis-panic-disorder`)
- `dis-agoraphobia` — Agoraphobia · DSM-5-TR: 300.22 · ICD-11: 6B00
- `dis-gad` — Generalized Anxiety Disorder · DSM-5-TR: 300.02 · ICD-11: 6B02 (✅ already exists)

### Obsessive-Compulsive and Related Disorders (3)
- `dis-ocd` — Obsessive-Compulsive Disorder · DSM-5-TR: 300.3 · ICD-11: 6B20 (CBT with ERP is gold standard; DBT used for co-occurring emotion dysregulation)
- `dis-body-dysmorphic-disorder` — Body Dysmorphic Disorder · DSM-5-TR: 300.7 · ICD-11: 6B21 (CBT/ERP)
- `dis-hoarding-disorder` — Hoarding Disorder · DSM-5-TR: 300.3 · ICD-11: 6B24 (CBT specialized protocols)

### Trauma- and Stressor-Related Disorders (3)
- `dis-ptsd` — Posttraumatic Stress Disorder · DSM-5-TR: 309.81 · ICD-11: 6B41 (✅ already exists)
- `dis-acute-stress-disorder` — Acute Stress Disorder · DSM-5-TR: 308.3 · ICD-11: 6B41
- `dis-adjustment-disorders` — Adjustment Disorders · DSM-5-TR: 309.xx · ICD-11: 6B43

### Depressive Disorders (4)
- `dis-mdd` — Major Depressive Disorder · DSM-5-TR: 296.xx · ICD-11: 6A71 (✅ already exists)
- `dis-persistent-depressive-disorder` — Persistent Depressive Disorder (Dysthymia) · DSM-5-TR: 300.4 · ICD-11: 6A72
- `dis-premenstrual-dysphoric-disorder` — Premenstrual Dysphoric Disorder · DSM-5-TR: 625.4 · ICD-11: N94.3 (used in this section because of clinical relevance)
- `dis-disruptive-mood-dysregulation` — Disruptive Mood Dysregulation Disorder · DSM-5-TR: 296.99 · ICD-11: 6A05

### Bipolar and Related Disorders (2)
- `dis-bipolar-i` — Bipolar I Disorder · DSM-5-TR: 296.xx · ICD-11: 6A60 (CBT adjunct only — psychoeducation + mood monitoring)
- `dis-bipolar-ii` — Bipolar II Disorder · DSM-5-TR: 296.89 · ICD-11: 6A61

### Feeding and Eating Disorders (3)
- `dis-anorexia-nervosa` — Anorexia Nervosa · DSM-5-TR: 307.1 · ICD-11: 6B80 (CBT-E is leading psychotherapy)
- `dis-bulimia-nervosa` — Bulimia Nervosa · DSM-5-TR: 307.51 · ICD-11: 6B81 (CBT-BN is leading treatment)
- `dis-binge-eating-disorder` — Binge-Eating Disorder · DSM-5-TR: 307.51 · ICD-11: 6B82

### Sleep-Wake Disorders (1)
- `dis-insomnia-disorder` — Insomnia Disorder · DSM-5-TR: 780.52 · ICD-11: 7A00 (CBT-I is first-line, gold standard)

### Substance-Related and Addictive Disorders (1)
- `dis-alcohol-use-disorder` — Alcohol Use Disorder · DSM-5-TR: 303.90 · ICD-11: 6C40.1 (motivational interviewing + CBT + DBT)

---

## Tier B — Moderate Relevance (27 disorders)

### Anxiety / OCD-related (more)
- `dis-substance-induced-anxiety` — Substance/Medication-Induced Anxiety Disorder · DSM-5-TR: 291.8/292.89 · ICD-11: 6B07
- `dis-anxiety-due-to-medical` — Anxiety Disorder Due to Another Medical Condition · DSM-5-TR: 293.84 · ICD-11: 6B08
- `dis-trichotillomania` — Trichotillomania · DSM-5-TR: 312.39 · ICD-11: 6B25.0 (Habit Reversal Training is gold standard)
- `dis-excoriation-disorder` — Excoriation Disorder · DSM-5-TR: 698.4 · ICD-11: 6B25.1

### Trauma- and Stressor-Related
- `dis-reactive-attachment` — Reactive Attachment Disorder · DSM-5-TR: 313.89 · ICD-11: 6B44
- `dis-prolonged-grief` — Prolonged Grief Disorder · DSM-5-TR: 309.82 · ICD-11: 6B42 (✅ already exists; CBT for PGD is leading treatment)

### Depressive / Bipolar
- `dis-cyclothymia` — Cyclothymic Disorder · DSM-5-TR: 301.13 · ICD-11: 6A04
- `dis-substance-induced-mood` — Substance/Medication-Induced Depressive/Bipolar Disorder · DSM-5-TR: 291.89 · ICD-11: 6A86/6A85
- `dis-depressive-due-to-medical` — Depressive Disorder Due to Another Medical Condition · DSM-5-TR: 293.83 · ICD-11: 6A84

### Dissociative Disorders
- `dis-dissociative-identity` — Dissociative Identity Disorder · DSM-5-TR: 300.14 · ICD-11: 6B65 (Phase-oriented trauma treatment, CBT for symptoms)
- `dis-dissociative-amnesia` — Dissociative Amnesia · DSM-5-TR: 300.12 · ICD-11: 6B66
- `dis-depersonalization-derealization` — Depersonalization/Derealization Disorder · DSM-5-TR: 300.6 · ICD-11: 6B64 (CBT specialized protocols)

### Somatic Symptom Disorders
- `dis-somatic-symptom-disorder` — Somatic Symptom Disorder · DSM-5-TR: 300.82 · ICD-11: 6C20 (CBT, ACT used)
- `dis-illness-anxiety` — Illness Anxiety Disorder · DSM-5-TR: 300.7 · ICD-11: 6C20.2 (CBT leading)
- `dis-functional-neurological-symptom` — Functional Neurological Symptom Disorder (Conversion) · DSM-5-TR: 300.11 · ICD-11: 6C20.4 (CBT, ACT)
- `dis-psychological-factors-medical` — Psychological Factors Affecting Other Medical Conditions · DSM-5-TR: 316 · ICD-11: 6E40

### Personality Disorders (all DSM-5-TR categorical, with ICD-11 dimensional note)
- `dis-borderline-personality` — Borderline Personality Disorder · DSM-5-TR: 301.83 · ICD-11: 6D11 (DBT is the gold standard, schema therapy, CBT for symptoms)
- `dis-avoidant-personality` — Avoidant Personality Disorder · DSM-5-TR: 301.82 · ICD-11: 6D10.0
- `dis-dependent-personality` — Dependent Personality Disorder · DSM-5-TR: 301.6 · ICD-11: 6D10.1
- `dis-obsessive-compulsive-personality` — Obsessive-Compulsive Personality Disorder · DSM-5-TR: 301.4 · ICD-11: 6D10.2
- `dis-narcissistic-personality` — Narcissistic Personality Disorder · DSM-5-TR: 301.81 · ICD-11: 6D10.3
- `dis-antisocial-personality` — Antisocial Personality Disorder · DSM-5-TR: 301.7 · ICD-11: 6D10.4
- `dis-schizoid-personality` — Schizoid Personality Disorder · DSM-5-TR: 301.20 · ICD-11: 6D10.5
- `dis-schizotypal-personality` — Schizotypal Personality Disorder · DSM-5-TR: 301.22 · ICD-11: 6D10.6 (in DSM-5-TR Schizophrenia Spectrum)

### Impulse Control (partial)
- `dis-intermittent-explosive` — Intermittent Explosive Disorder · DSM-5-TR: 312.34 · ICD-11: 6C73 (DBT, CBT, anger management)
- `dis-kleptomania` — Kleptomania · DSM-5-TR: 312.32 · ICD-11: 6C71 (CBT)
- `dis-pyromania` — Pyromania · DSM-5-TR: 312.33 · ICD-11: 6C72

---

## Tier C — Low/Indirect Relevance (60+ disorders — Pharmacological primary, or other-modality)

### Neurodevelopmental (6)
- `dis-intellectual-disability` — Intellectual Disability · DSM-5-TR: 319 · ICD-11: 6A00
- `dis-autism-spectrum` — Autism Spectrum Disorder · DSM-5-TR: 299.00 · ICD-11: 6A02
- `dis-adhd` — Attention-Deficit/Hyperactivity Disorder · DSM-5-TR: 314.0x · ICD-11: 6A05 (CBT adjunct: behavioral organization; DBT skills useful for emotion regulation)
- `dis-specific-learning-disorder` — Specific Learning Disorder · DSM-5-TR: 315.xx · ICD-11: 6A03
- `dis-developmental-coordination` — Developmental Coordination Disorder · DSM-5-TR: 315.4 · ICD-11: 6A04
- `dis-tic-disorders` — Tic Disorders · DSM-5-TR: 307.2x · ICD-11: 8A05.0 (Comprehensive Behavioral Intervention for Tics - CBIT)

### Schizophrenia Spectrum (5)
- `dis-schizophrenia` — Schizophrenia · DSM-5-TR: 295.90 · ICD-11: 6A20 (CBTp for psychosis as adjunct)
- `dis-schizoaffective` — Schizoaffective Disorder · DSM-5-TR: 295.70 · ICD-11: 6A21
- `dis-delusional` — Delusional Disorder · DSM-5-TR: 297.1 · ICD-11: 6A22
- `dis-brief-psychotic` — Brief Psychotic Disorder · DSM-5-TR: 298.8 · ICD-11: 6A23
- `dis-schizophreniform` — Schizophreniform Disorder · DSM-5-TR: 295.40 · ICD-11: 6A24

### Neurocognitive (3)
- `dis-major-neurocognitive` — Major Neurocognitive Disorder (Dementia) · DSM-5-TR: 625.4 · ICD-11: 6D71
- `dis-mild-neurocognitive` — Mild Neurocognitive Disorder · DSM-5-TR: 331.83 · ICD-11: 6D72
- `dis-delirium` — Delirium · DSM-5-TR: 780.09 · ICD-11: 6D70

### Substance-Related (specific substances — partial, 8+)
- `dis-cannabis-use` — Cannabis Use Disorder
- `dis-stimulant-use` — Stimulant Use Disorder (cocaine, amphetamine)
- `dis-opioid-use` — Opioid Use Disorder
- `dis-sedative-use` — Sedative/Hypnotic/Anxiolytic Use Disorder
- `dis-hallucinogen-use` — Hallucinogen-Related Disorders
- `dis-inhalant-use` — Inhalant Use Disorder
- `dis-tobacco-use` — Tobacco Use Disorder
- `dis-gambling-disorder` — Gambling Disorder · DSM-5-TR: 312.31 · ICD-11: 6C50 (CBT leading)

### Sleep-Wake (others, 4)
- `dis-hypersomnolence` — Hypersomnolence Disorder
- `dis-narcolepsy` — Narcolepsy
- `dis-breathing-related-sleep` — Obstructive Sleep Apnea Hypopnea
- `dis-nightmare-disorder` — Nightmare Disorder (Image Rehearsal Therapy is CBT)

### Sexual Dysfunctions (7)
- `dis-delayed-ejaculation` — Delayed Ejaculation
- `dis-erectile-disorder` — Erectile Disorder
- `dis-female-orgasmic` — Female Orgasmic Disorder
- `dis-female-sexual-interest-arousal` — Female Sexual Interest/Arousal Disorder
- `dis-genito-pelvic-pain` — Genito-Pelvic Pain/Penetration Disorder
- `dis-male-hypoactive-sexual-desire` — Male Hypoactive Sexual Desire Disorder
- `dis-premature-ejaculation` — Premature (Early) Ejaculation
(All: sex therapy approaches, often combined with CBT techniques)

### Gender Dysphoria (1)
- `dis-gender-dysphoria` — Gender Dysphoria · DSM-5-TR: 302.85 · ICD-11: HA60 (affirmative therapy)

### Disruptive, Impulse-Control, Conduct (2)
- `dis-odd` — Oppositional Defiant Disorder
- `dis-conduct-disorder` — Conduct Disorder

### Paraphilic (3)
- `dis-voyeuristic` — Voyeuristic Disorder
- `dis-exhibitionistic` — Exhibitionistic Disorder
- `dis-fetishistic` — Fetishistic Disorder

### Elimination (2)
- `dis-enuresis` — Enuresis
- `dis-encopresis` — Encopresis

### Feeding (others, 3)
- `dis-pica` — Pica
- `dis-rumination` — Rumination Disorder
- `dis-arfid` — Avoidant/Restrictive Food Intake Disorder (ARFID)

### Other/Medication-Induced (10+)
- `dis-factitious` — Factitious Disorder
- `dis-catatonia` — Catatonia
- `dis-parkinsonism-medication` — Medication-Induced Parkinsonism
- (other medication-induced movement disorders)
- `dis-other-specified-mental` — Other Specified Mental Disorder
- `dis-unspecified-mental` — Unspecified Mental Disorder

---

## Deferred (Out of Scope, Do Not Build)

**Historical/Retired DSM-III/IV diagnoses** (per `disorders-taxonomy-execution-plan.md`):
- Asperger's Disorder (DSM-IV) → merged into ASD in DSM-5
- Ego-Dystonic Sexual Orientation (DSM-III-R) → removed
- Gender Identity Disorder (DSM-IV) → replaced by Gender Dysphoria
- Hypochondriasis (DSM-IV) → replaced by Illness Anxiety + Somatic Symptom Disorder
- Neurasthenia (DSM-IV Appendix B) → not in DSM-5
- Various DSM-IV "Not Otherwise Specified" categories → consolidated in DSM-5
- "Mixed Anxiety-Depressive Disorder" (ICD-11 reserves as 6A73 but not in DSM-5-TR)
- Specific social phobia subtypes (e.g., performance-only subtype in DSM-IV)
- All DSM-III/IV personality disorder severity scales

**Other deferred categories:**
- ICD-11 "Complex PTSD" as separate diagnosis (DSM-5-TR PTSD, ICD-11 6B41)
- ICD-11 dimensional personality model (only used as `notes` field in categorical DSM-5-TR dis- files)
- ICD-11 Gaming Disorder (in Chapter 06 since 2022; can be added later if requested)

---

## Major DSM-5-TR vs ICD-11 Divergences (worth noting per `dis-` file `notes` field)

1. **Complex PTSD**: ICD-11 has it as separate diagnosis (6B41), DSM-5-TR has it only in "Conditions for Further Study". Atlas dis- files will use the **DSM-5-TR diagnosis** (PTSD), with a `notes` field flagging ICD-11's separate category.

2. **Personality Disorders**: DSM-5-TR has 10 categorical PDs. ICD-11 has **dimensional model** with 5 prominent trait domains (Negative Affectivity, Detachment, Dissociation, Dissociality, Anankastia, Anxiousness) plus severity. Atlas dis- files will use the **DSM-5-TR categorical labels** with `notes` mentioning ICD-11 dimensional approach.

3. **Prolonged Grief Disorder**: DSM-5-TR introduced it as 309.82 in 2022. ICD-11 had it earlier as 6B42. Aligned in both now.

4. **Bipolar/Depressive organization**: DSM-5-TR separates them as distinct chapters; ICD-11 groups them under "Mood disorders" (6A60-6A8Z).

5. **Disorder due to substance**: ICD-11 uses "Disorder due to substance use" pattern; DSM-5-TR uses "Substance/Medication-Induced [X] Disorder".

6. **Coding systems**: DSM-5-TR uses ICD-10-CM codes (inherited from ICD-10). ICD-11 uses new ICD-11 codes (6Axx, 6Bxx, 6Cxx, 6Dxx, 6Exx).

7. **Hoarding**: Both have it; DSM-5-TR under OCD-related, ICD-11 under "Obsessive-compulsive or related disorders" (6B24).

8. **Binge-Eating Disorder**: Both have it. Aligned.

9. **Disruptive Mood Dysregulation Disorder**: DSM-5-TR only (controversial); not in ICD-11 as such.

10. **Avoidant/Restrictive Food Intake Disorder (ARFID)**: Both have it. Aligned.

---

## Recommended Build Order

1. **Pilot (Phase 2):** GAD, MDD, BPD, PTSD, Insomnia Disorder
2. **Tier A batch 1 (anxiety + OCD + trauma):** Separation Anxiety, Selective Mutism, Specific Phobia, Social Anxiety, Agoraphobia, OCD, BDD, Hoarding, Acute Stress, Adjustment Disorders
3. **Tier A batch 2 (mood + bipolar):** PDD, PMDD, DMDD, Bipolar I, Bipolar II
4. **Tier A batch 3 (eating + sleep + substance):** Anorexia, Bulimia, Binge Eating, Alcohol Use Disorder
5. **Tier B:** Begin with Personality Disorders (especially BPD has rich DBT connection), then dissociation, then somatic
6. **Tier C:** Build last, thin entries with honest gaps

**Total scope:** 110+ files (if all Tier A + B + C). **Realistic scope for Atlas:** Tier A + B = ~50 files. Tier C = separate future phase, gated on user request.
