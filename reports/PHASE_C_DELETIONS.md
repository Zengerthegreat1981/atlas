# Phase C — Deletions and Merges Log

## TASK 1 — duplicate node pairs (13 pairs found; 14 expected per spec but only 13 exist on disk)

| canonical (kept) | merged-from | part | status | notes |
|---|---|---|---|---|
| sch-legal-pluralism | legal-pluralism | schools | NOT deleted — protected | unprefixed file is pure template stub (no substantive content to merge); it is in protected.txt so cannot be deleted or edited. 5 external files repointed to sch-legal-pluralism. |
| sch-feminist-jurisprudence | feminist-jurisprudence | schools | NOT deleted — protected | unprefixed file is pure template stub; protected.txt. 6 external files repointed. |
| sch-environmental-ethics | environmental-ethics | schools | NOT deleted — protected | unprefixed file is pure template stub; protected.txt. 13 external files repointed. |
| con-categorical-imperative | categorical-imperative | concepts | NOT deleted — protected | merged the one substantive edge (belongs_to sch-deontological-ethics-kant) into con-categorical-imperative; unprefixed file itself left untouched (protected.txt). 3 external files repointed. |
| con-epistemic-justice-anthropology | epistemic-justice-anthropology | concepts | merged + deleted | unprefixed body was junk stub ("Anthropology node CON-19004"); nothing to merge. 0 external links. |
| con-virtue | virtue | concepts | merged + deleted | merged edge belongs_to sch-virtue-ethics-aristotle into con-virtue.md. 0 external links. |
| con-rule-of-law | rule-of-law | concepts | merged + deleted | merged edge belongs_to sch-jurisprudence-natural-law into con-rule-of-law.md. 0 external links. |
| con-artificial-intelligence-ethics | artificial-intelligence-ethics | concepts | merged + deleted | unprefixed body empty (title only); nothing to merge. 1 external reference NOT repointed — it is inside a protected file (see list below). |
| con-separation-of-powers | separation-of-powers | concepts | merged + deleted | merged edge belongs_to sch-constitutional-law-theory into con-separation-of-powers.md. 1 external file repointed. |
| wrk-groundwork-metaphysics-morals-kant | groundwork-metaphysics-morals-kant | works | merged + deleted | unprefixed body was empty headings only; nothing to merge. 1 external file repointed. |
| wrk-after-virtue-macintyre | after-virtue-macintyre | works | merged + deleted | unprefixed body was empty headings only; nothing to merge. 1 external file repointed. |
| wrk-theory-of-justice-rawls | theory-of-justice-rawls | works | merged + deleted | unprefixed body was empty headings only; nothing to merge. 0 external links. |
| wrk-utilitarianism-mill | utilitarianism-mill | works | merged + deleted | unprefixed body was empty headings only; nothing to merge. 1 external file repointed. |

**Protected files with a needed link update I could not make (edit them yourselves / flag to the owning agent):**

- `schools/sch-religion-digital-technology.md` — line ~23, `related:` entry `- id: "artificial-intelligence-ethics", ...` should be repointed to `- id: "con-artificial-intelligence-ethics", ...` (the unprefixed `concepts/artificial-intelligence-ethics.md` it points to has been deleted as part of the TASK 1 merge into `con-artificial-intelligence-ethics`).

The 4 protected unprefixed files themselves (`legal-pluralism.md`, `feminist-jurisprudence.md`, `environmental-ethics.md`, `categorical-imperative.md`) were left completely untouched (not edited, not deleted), per the protection rule — even though TASK 1 would otherwise have deleted them after merging.

## TASK 2 — junk deletions

### A. `part: anthropology` stub body = literally "Anthropology node <ID>" (28 files)

Criteria: (a) body is the fixed stub sentence only, (b) 0 incoming links, (c) not protected.

| slug | part | reason | word count | incoming links removed |
|---|---|---|---|---|
| anthropological-ethics-care | concepts | placeholder stub ("Anthropology node <ID>") | 8 | 0 |
| anthropology-of-anthropology-final | concepts | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| digital-indigeneity | concepts | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| embodied-citizenship | concepts | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| polyculturalism-beyond-multiculturalism | concepts | placeholder stub ("Anthropology node <ID>") | 5 | 0 |
| epistemology-ontology-indigenous-knowledge | debates | placeholder stub ("Anthropology node <ID>") | 8 | 0 |
| collaborative-analysis-methodology | instruments | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| community-visioning-participatory-futures | instruments | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| anthropology-hope-possibility | schools | placeholder stub ("Anthropology node <ID>") | 9 | 0 |
| applied-anthropology-social-justice | schools | placeholder stub ("Anthropology node <ID>") | 9 | 0 |
| indigenous-anthropology-autoethnography | schools | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| relational-anthropology | schools | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| ai-governance-ethnography | studies | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| cryptocurrency-blockchain-ethnography | studies | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| gig-economy-labor-anthropology | studies | placeholder stub ("Anthropology node <ID>") | 9 | 0 |
| mental-health-crisis-global-south | studies | placeholder stub ("Anthropology node <ID>") | 10 | 0 |
| post-conflict-reconciliation-practices | studies | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| tech-worker-ethnography-global | studies | placeholder stub ("Anthropology node <ID>") | 8 | 0 |
| urban-beekeeping-communities | studies | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| vaccine-hesitancy-anthropology | studies | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| ailton-krenak | thinkers | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| chimaomaobi-ibeagha | thinkers | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| diana-betancur-garcia | thinkers | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| jaime-amparo-alves | thinkers | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| pattana-kitiarsa | thinkers | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| siti-zunariyah | thinkers | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| thandi-xaba | thinkers | placeholder stub ("Anthropology node <ID>") | 6 | 0 |
| wangari-mathai-legacy | thinkers | placeholder stub ("Anthropology node <ID>") | 7 | 0 |
| krenak-ideas-postpone-end-world | works | placeholder stub ("Anthropology node <ID>") | 12 | 0 |

### B. Fabricated entities (2 files)

| slug | part | reason | word count | incoming links removed |
|---|---|---|---|---|
| thk-fatima-alkindi | thinkers | fabricated: WebSearch found no trace of this person (per audits/anthropology.md sample #9); generic gendered boilerplate bio, fake 'OpenLibrary records for X' pseudo-source | 11 | 0 |
| thk-peter-kipury | thinkers | fabricated: WebSearch found no trace of this person (per audits/anthropology.md sample #26); same boilerplate pattern | 27 | 0 |

### C. Linguistics template filler, Template A ("دراسة متقدمة لمفهوم X في اللسانيات المعاصرة." + empty edges/related/gaps) and Template B (longer boilerplate paragraph) — 221 files, all `part: linguistics`

Criteria: (a) body is the fixed template sentence(s) only, <60 words (max found: 59), (b) 0 incoming links (verified for all), (c) not protected (0 protected hits).

| slug | dir | word count | incoming links removed |
|---|---|---|---|
| stu-laboratory-production-real-time-changes | studies | 47 | 0 |
| stu-coarticulation-vowel-consonant-cross-lang | studies | 47 | 0 |
| stu-motion-event-typology-talmy-framework | studies | 44 | 0 |
| thk-ray-jackendoff-parallel-architecture | thinkers | 41 | 0 |
| thk-david-dowty-thematic-roles | thinkers | 41 | 0 |
| thk-theo-van-leeuwen-visual-social-semiotics | thinkers | 44 | 0 |
| thk-keith-rayner-eye-tracking | thinkers | 41 | 0 |
| thk-norman-fairclough-critical-discourse | thinkers | 41 | 0 |
| thk-gunther-kress-multimodal-discourse | thinkers | 41 | 0 |
| thk-steven-pinker-language-acquisition | thinkers | 41 | 0 |
| thk-adam-albright-learning-phonology | thinkers | 41 | 0 |
| thk-colin-wilson-constraint-phonology | thinkers | 41 | 0 |
| thk-james-hurford-language-evolution-simulation | thinkers | 41 | 0 |
| thk-marta-kutas-erp-language | thinkers | 41 | 0 |
| thk-louis-goldstein-gestural | thinkers | 41 | 0 |
| thk-paul-portner-modals-imperative | thinkers | 41 | 0 |
| thk-kate-wolff-presupposition | thinkers | 41 | 0 |
| thk-julien-musolino-acquisition | thinkers | 41 | 0 |
| thk-robert-ladd-intonation | thinkers | 41 | 0 |
| thk-paul-bloom-language-acquisition | thinkers | 41 | 0 |
| thk-melissa-redford-prosody | thinkers | 41 | 0 |
| thk-lyn-frazier-parsing-garden-path | thinkers | 41 | 0 |
| thk-adam-kendon-gesture-language-system | thinkers | 41 | 0 |
| thk-catherine-browman-gestures | thinkers | 42 | 0 |
| thk-rachel-walker-harmonies | thinkers | 41 | 0 |
| thk-paul-gee-discourse-identity-learning | thinkers | 41 | 0 |
| thk-anthony-sapir-bilingual-processing | thinkers | 41 | 0 |
| thk-robert-de-jong-reading-fluency | thinkers | 44 | 0 |
| thk-bruce-hayes-metrical-theory | thinkers | 41 | 0 |
| thk-graeme-hirst-discourse-coherence | thinkers | 41 | 0 |
| thk-mark-turner-conceptual-metaphor | thinkers | 41 | 0 |
| thk-chris-mccully-stress | thinkers | 41 | 0 |
| thk-deborah-cameron-language-gender-society | thinkers | 41 | 0 |
| thk-francoise-grosjean-bilingualism | thinkers | 41 | 0 |
| thk-alan-baddeley-working-memory-model | thinkers | 41 | 0 |
| thk-susan-garnham-discourse-referents | thinkers | 41 | 0 |
| thk-alice-turk-speech-production | thinkers | 41 | 0 |
| thk-adele-goldberg-construction-grammar | thinkers | 41 | 0 |
| thk-gilles-fauconnier-blending | thinkers | 41 | 0 |
| thk-donna-erickson-coarticulation | thinkers | 41 | 0 |
| thk-terrence-deacon-evolution-language-symbol | thinkers | 41 | 0 |
| thk-roger-giora-optimal-innovation | thinkers | 41 | 0 |
| thk-shlomo-izre-el-free-indirect-discourse | thinkers | 41 | 0 |
| thk-deirdre-wilson-relevance-theory | thinkers | 41 | 0 |
| thk-beth-levin-verb-semantics | thinkers | 41 | 0 |
| thk-elinor-ochs-socialization-language-culture | thinkers | 41 | 0 |
| thk-angelika-kratzer-modality | thinkers | 41 | 0 |
| thk-leonard-talmy-spatial-semantics | thinkers | 41 | 0 |
| thk-david-mcneill-gesture-speech-integration | thinkers | 41 | 0 |
| thk-manfred-krifka-events-generics | thinkers | 41 | 0 |
| thk-allan-luke-critical-literacy-identity | thinkers | 41 | 0 |
| thk-bertrand-leone-french-phonology | thinkers | 41 | 0 |
| thk-lexicon-hale-keyser-syntax-semantics | thinkers | 48 | 0 |
| thk-malka-rappaport-hovav-event-structure | thinkers | 44 | 0 |
| ins-functional-magnetic-resonance-fmri-bold | instruments | 42 | 0 |
| ins-electroencephalography-eeg-event-related | instruments | 42 | 0 |
| ins-diffusion-tensor-imaging-dti-white-matter | instruments | 44 | 0 |
| wrk-clements-hume-internal-organization-1995 | works | 43 | 0 |
| wrk-prince-smolensky-ot-constraint-2004 | works | 43 | 0 |
| wrk-cole-phonological-structure-1987 | works | 41 | 0 |
| wrk-baddeley-working-memory-psychology-2003 | works | 43 | 0 |
| wrk-talmy-toward-cognitive-semantics-2000 | works | 43 | 0 |
| wrk-krifka-semantics-generics-1995 | works | 43 | 0 |
| wrk-fauconnier-turner-blending-2002 | works | 45 | 0 |
| wrk-fairclough-discourse-critical-society-2010 | works | 41 | 0 |
| wrk-rayner-eye-movements-reading-2012 | works | 43 | 0 |
| wrk-boersma-hayes-ot-phonology-2001 | works | 43 | 0 |
| wrk-pinker-language-instinct-1994 | works | 41 | 0 |
| wrk-goldberg-constructions-2006 | works | 41 | 0 |
| wrk-kratzer-modality-2012 | works | 41 | 0 |
| wrk-kutas-federmeier-erp-language-2011 | works | 45 | 0 |
| wrk-lindsey-colantoni-phonetics-guide-2009 | works | 45 | 0 |
| wrk-hayes-metrical-stress-1995 | works | 43 | 0 |
| wrk-mcneill-hand-mind-gesture-2005 | works | 41 | 0 |
| wrk-frazier-fodor-sausage-machine-parsing-1978 | works | 45 | 0 |
| wrk-deacon-symbolic-species-evolution-1997 | works | 41 | 0 |
| wrk-ladd-phonology-intonation-2008 | works | 43 | 0 |
| wrk-browman-goldstein-articulatory-phonology-1989 | works | 43 | 0 |
| wrk-portner-modality-2009 | works | 43 | 0 |
| wrk-dowty-thematic-proto-roles-1991 | works | 41 | 0 |
| con-multimodal-communication-integration | concepts | 43 | 0 |
| con-conduction-aphasia | concepts | 12 | 0 |
| con-sonority-hierarchy | concepts | 33 | 0 |
| con-metathesis-reordering | concepts | 42 | 0 |
| con-definiteness-indefiniteness | concepts | 42 | 0 |
| con-language-cognition-embodiment | concepts | 42 | 0 |
| con-voice-print-analysis | concepts | 14 | 0 |
| con-algorithmic-transparency | concepts | 12 | 0 |
| con-gesture-iconic-indexic | concepts | 14 | 0 |
| con-comparative-method-application | concepts | 14 | 0 |
| con-agreement-attraction-errors | concepts | 43 | 0 |
| con-matrix-language-embedded | concepts | 14 | 0 |
| con-overlaps-interruptions | concepts | 12 | 0 |
| con-receptive-aphasia | concepts | 12 | 0 |
| con-transformer-models-architecture | concepts | 12 | 0 |
| con-language-nesting-hybridity | concepts | 14 | 0 |
| con-grammaticalization-process-detailed | concepts | 14 | 0 |
| con-authorship-attribution-forensic | concepts | 14 | 0 |
| con-mixed-language-systems | concepts | 14 | 0 |
| con-turn-taking-mechanism | concepts | 18 | 0 |
| con-linguistic-human-rights-v2 | concepts | 14 | 0 |
| con-language-in-education-policy | concepts | 16 | 0 |
| con-language-reasoning-inference | concepts | 42 | 0 |
| con-embodied-cognition-grammar | concepts | 14 | 0 |
| con-language-social-class-stratification | concepts | 43 | 0 |
| con-analogical-leveling | concepts | 14 | 0 |
| con-language-planning-corpus | concepts | 18 | 0 |
| con-language-planning-status | concepts | 16 | 0 |
| con-affectedness-telicity | concepts | 40 | 0 |
| con-lexical-access-cohort-model | concepts | 44 | 0 |
| con-power-control-discourse | concepts | 16 | 0 |
| con-eye-tracking-reading-comprehension | concepts | 43 | 0 |
| con-superior-temporal-sulcus | concepts | 14 | 0 |
| con-inference-types-pragmatics | concepts | 43 | 0 |
| con-conceptual-blending-fauconnier | concepts | 41 | 0 |
| con-parsing-ambiguity-resolution | concepts | 43 | 0 |
| con-ai-ethics-language | concepts | 16 | 0 |
| con-subject-object-asymmetries | concepts | 45 | 0 |
| con-reanalysis-rebracketing | concepts | 16 | 0 |
| con-expressive-aphasia | concepts | 12 | 0 |
| con-syllable-structure-constraints | concepts | 43 | 0 |
| con-place-articulation-features | concepts | 44 | 0 |
| con-cefr-framework | concepts | 14 | 0 |
| con-agent-patient-roles | concepts | 43 | 0 |
| con-parasitic-gaps-phonology | concepts | 41 | 0 |
| con-scope-ambiguity-resolution | concepts | 43 | 0 |
| con-global-aphasia | concepts | 12 | 0 |
| con-coarticulation-mechanics | concepts | 42 | 0 |
| con-click-consonants-production | concepts | 43 | 0 |
| con-embodied-syntax-motor | concepts | 14 | 0 |
| con-lenition-sound-weakening | concepts | 42 | 0 |
| con-toefl-ielts-assessment | concepts | 16 | 0 |
| con-linguistic-imperialism-power | concepts | 14 | 0 |
| con-licensing-phonology-strength | concepts | 42 | 0 |
| con-assimilation-feature-spreading | concepts | 42 | 0 |
| con-polysemy-related-senses | concepts | 42 | 0 |
| con-phenomenology-language-lived-experience | concepts | 41 | 0 |
| con-event-structure-polyadicity | concepts | 43 | 0 |
| con-harmony-agreement-phonology | concepts | 43 | 0 |
| con-binding-anaphora-pronouns | concepts | 44 | 0 |
| con-borrowing-integration | concepts | 14 | 0 |
| con-modality-necessity-possibility | concepts | 42 | 0 |
| con-language-selection-mechanisms | concepts | 43 | 0 |
| con-vowel-harmony-types | concepts | 43 | 0 |
| con-language-ideology-policy | concepts | 14 | 0 |
| con-working-memory-span-language | concepts | 43 | 0 |
| con-narrative-structure-storytelling | concepts | 43 | 0 |
| con-stuttering-neural | concepts | 14 | 0 |
| con-language-evolution-biolinguistics | concepts | 43 | 0 |
| con-repair-correction-mechanism | concepts | 14 | 0 |
| con-segmental-inventory-languages | concepts | 43 | 0 |
| con-hemispheric-asymmetry | concepts | 14 | 0 |
| con-ecological-linguistics-ecolinguistics | concepts | 40 | 0 |
| con-dyslexia-neurobiology | concepts | 16 | 0 |
| con-nasal-harmony-aerodynamics | concepts | 41 | 0 |
| con-sound-change-neogrammararian | concepts | 18 | 0 |
| con-language-planning-acquisition | concepts | 16 | 0 |
| con-music-language-universals | concepts | 14 | 0 |
| con-reduplication-repetition | concepts | 40 | 0 |
| con-digital-discourse-online-interaction | concepts | 41 | 0 |
| con-language-ethics-normativity | concepts | 41 | 0 |
| con-register-style-variation | concepts | 44 | 0 |
| con-consonant-harmony-spreading | concepts | 43 | 0 |
| con-language-proficiency-testing | concepts | 14 | 0 |
| con-self-paced-reading-methodology | concepts | 43 | 0 |
| con-embodied-cognition-language-body | concepts | 41 | 0 |
| con-convergence-contact-induced | concepts | 16 | 0 |
| con-language-power-discourse-dominance | concepts | 42 | 0 |
| con-phonological-opacity | concepts | 41 | 0 |
| con-official-language-designation | concepts | 14 | 0 |
| con-mental-spaces-discourse | concepts | 45 | 0 |
| con-mora-weight-phonology | concepts | 43 | 0 |
| con-deletion-segment-loss | concepts | 42 | 0 |
| con-mismatch-negativity-phonology | concepts | 43 | 0 |
| con-language-maintenance-shift | concepts | 16 | 0 |
| con-endangered-status-assessment | concepts | 14 | 0 |
| con-syntactic-priming-persistence | concepts | 41 | 0 |
| con-minority-language-rights | concepts | 14 | 0 |
| con-language-emotion-affect | concepts | 42 | 0 |
| con-possession-inalienable-alienable | concepts | 40 | 0 |
| con-quantification-universal-existential | concepts | 40 | 0 |
| con-left-anterior-negativity-morphosyntax | concepts | 44 | 0 |
| con-linguistic-variation-social | concepts | 14 | 0 |
| con-word-embedding-bias | concepts | 16 | 0 |
| con-proto-language-reconstruction | concepts | 16 | 0 |
| con-phoneme-monitoring-response-latency | concepts | 43 | 0 |
| con-epenthesis-vowel-insertion | concepts | 42 | 0 |
| con-stylometry-text-analysis | concepts | 14 | 0 |
| con-manner-articulation-features | concepts | 44 | 0 |
| con-thematic-role-assignment-online | concepts | 44 | 0 |
| con-generics-generic-sentences | concepts | 42 | 0 |
| con-hermeneutics-interpretation-meaning | concepts | 40 | 0 |
| con-linguistic-profiling-suspect | concepts | 12 | 0 |
| con-negation-scope-interaction | concepts | 44 | 0 |
| con-visual-semiotics-image-meaning | concepts | 41 | 0 |
| con-discourse-integration-coherence | concepts | 43 | 0 |
| con-archiphoneme-neutralization | concepts | 44 | 0 |
| con-age-grading-apparent-time | concepts | 16 | 0 |
| con-phonological-transparency | concepts | 41 | 0 |
| con-counterfactuality-conditional | concepts | 42 | 0 |
| con-stereotypes-nlp-models | concepts | 18 | 0 |
| con-critical-discourse-analysis-ideology | concepts | 44 | 0 |
| con-phonotactics-constraints-crossling | concepts | 43 | 0 |
| con-sentence-wrap-up-effects | concepts | 43 | 0 |
| con-gpt-generation-models | concepts | 14 | 0 |
| con-discourse-deixis-context | concepts | 43 | 0 |
| con-fairness-metrics-nlp | concepts | 16 | 0 |
| con-transitivity-diathesis-voice | concepts | 42 | 0 |
| con-vowel-shift-great-english | concepts | 14 | 0 |
| con-language-memory-retention | concepts | 42 | 0 |
| con-indigenous-language-endangerment | concepts | 14 | 0 |
| con-word-frequency-effect-recognition | concepts | 44 | 0 |
| con-arcuate-fasciculus | concepts | 12 | 0 |
| con-attention-mechanism-nlp | concepts | 16 | 0 |
| con-intergenerational-transmission | concepts | 16 | 0 |
| con-creole-pidgin-formation | concepts | 16 | 0 |
| con-language-lateralization | concepts | 12 | 0 |
| sch-biosemiotics-language-life | schools | 40 | 0 |
| sch-digital-humanities-text-analysis | schools | 41 | 0 |
| sch-phenomenological-linguistics-lived | schools | 41 | 0 |
| sch-ecolinguistics-language-environment | schools | 40 | 0 |

### D. "Title repeated as body + `## المراجع` → Pending/OpenLibrary CrossRef pending" template stub — 287 files (anthropology, historiography, ethics, legal-theory)

Criteria: (a) body = title line repeated once + a bare 'Pending'-style references line, <60 words (max found: 16), (b) <3 incoming links, (c) not protected.

| slug | dir | part | word count | incoming links removed | link removed from |
|---|---|---|---|---|---|
| wrk-anthro-studies-8 | works | anthropology | 12 | 0 | — |
| wrk-hist-studies-9 | works | historiography | 12 | 0 | — |
| wrk-balinese-character | works | anthropology | 11 | 0 | — |
| wrk-anthro-studies-9 | works | anthropology | 12 | 0 | — |
| wrk-ethnography-mind | works | anthropology | 9 | 0 | — |
| wrk-hist-studies-8 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-2 | works | anthropology | 12 | 0 | — |
| wrk-hist-studies-3 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-6 | works | anthropology | 12 | 0 | — |
| wrk-hist-studies-7 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-7 | works | anthropology | 12 | 0 | — |
| wrk-mediterranean-braudel | works | historiography | 11 | 0 | — |
| wrk-hist-studies-6 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-3 | works | anthropology | 12 | 0 | — |
| wrk-night-battles-ginzburg | works | historiography | 11 | 0 | — |
| wrk-hist-studies-2 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-4 | works | anthropology | 12 | 0 | — |
| wrk-reconstruction-history | works | historiography | 11 | 0 | — |
| wrk-hist-studies-5 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-0 | works | anthropology | 12 | 0 | — |
| wrk-hist-studies-1 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-1 | works | anthropology | 12 | 0 | — |
| wrk-hist-studies-0 | works | historiography | 12 | 0 | — |
| wrk-anthro-studies-5 | works | anthropology | 12 | 0 | — |
| wrk-argonauts-western-pacific | works | anthropology | 11 | 0 | — |
| wrk-hist-studies-4 | works | historiography | 14 | 0 | — |
| wrk-sexual-life-savages | works | anthropology | 11 | 0 | — |
| wrk-comparative-history-method | works | historiography | 11 | 0 | — |
| wrk-coming-age-samoa | works | anthropology | 11 | 0 | — |
| con-legal-comp-31 | concepts | legal-theory | 8 | 0 | — |
| con-legal-48 | concepts | legal-theory | 9 | 0 | — |
| con-hist-doc-20 | concepts | historiography | 9 | 0 | — |
| con-anth-complete-8 | concepts | anthropology | 8 | 0 | — |
| con-syncretism | concepts | anthropology | 12 | 0 | — |
| con-eth-applied-38 | concepts | ethics | 8 | 0 | — |
| con-eth-comp-20 | concepts | ethics | 8 | 0 | — |
| con-legal-rights-43 | concepts | legal-theory | 8 | 0 | — |
| con-ethics-virtue-55 | concepts | ethics | 6 | 0 | — |
| con-anthro-applied-8 | concepts | anthropology | 12 | 0 | — |
| con-anth-final-3 | concepts | anthropology | 8 | 0 | — |
| con-liability | concepts | legal-theory | 10 | 0 | — |
| con-hist-final-28 | concepts | historiography | 12 | 0 | — |
| con-continuity-change | concepts | historiography | 12 | 0 | — |
| con-hist-social-6 | concepts | historiography | 12 | 0 | — |
| con-consequences | concepts | ethics | 10 | 0 | — |
| con-hist-doc-30 | concepts | historiography | 9 | 0 | — |
| con-social-18 | concepts | anthropology | 9 | 0 | — |
| con-social-7 | concepts | anthropology | 9 | 0 | — |
| con-motive | concepts | ethics | 10 | 0 | — |
| con-justice | concepts | ethics | 10 | 0 | — |
| con-determinism-history | concepts | historiography | 10 | 0 | — |
| con-religion-belief | concepts | anthropology | 12 | 0 | — |
| con-hist-doc-24 | concepts | historiography | 9 | 0 | — |
| con-rights-law | concepts | legal-theory | 10 | 0 | — |
| con-legal-comp-35 | concepts | legal-theory | 8 | 0 | — |
| con-ancestor-worship | concepts | anthropology | 12 | 0 | — |
| con-anth-final-7 | concepts | anthropology | 6 | 0 | — |
| con-ethics-virtue-51 | concepts | ethics | 8 | 0 | — |
| con-clan-system | concepts | anthropology | 9 | 0 | — |
| con-legal-rights-47 | concepts | legal-theory | 8 | 0 | — |
| con-anth-final-13 | concepts | anthropology | 6 | 0 | — |
| con-eth-comp-24 | concepts | ethics | 8 | 0 | — |
| con-hist-social-2 | concepts | historiography | 12 | 0 | — |
| con-hist-final-18 | concepts | historiography | 8 | 0 | — |
| con-social-3 | concepts | anthropology | 9 | 0 | — |
| con-hist-doc-34 | concepts | historiography | 9 | 0 | — |
| con-cult-religion | concepts | anthropology | 12 | 0 | — |
| con-hist-social-10 | concepts | historiography | 14 | 0 | — |
| con-contract-law | concepts | legal-theory | 10 | 0 | — |
| con-hist-doc-25 | concepts | historiography | 9 | 0 | — |
| con-legal-comp-34 | concepts | legal-theory | 8 | 0 | — |
| con-anth-final-6 | concepts | anthropology | 8 | 0 | — |
| con-ethics-virtue-50 | concepts | ethics | 8 | 0 | — |
| con-eth-comp-25 | concepts | ethics | 8 | 0 | — |
| con-anth-final-12 | concepts | anthropology | 6 | 0 | — |
| con-legal-rights-46 | concepts | legal-theory | 8 | 0 | — |
| con-hist-social-3 | concepts | historiography | 12 | 0 | — |
| con-hist-final-19 | concepts | historiography | 8 | 0 | — |
| con-myth-mythology | concepts | anthropology | 10 | 1 | concepts/con-magic-religion-frazer.md |
| con-econ-anthropology-14 | concepts | anthropology | 12 | 0 | — |
| con-totemism | concepts | anthropology | 7 | 2 | concepts/con-magic-religion-frazer.md; schools/sch-levi-strauss-structuralism.md |
| con-social-2 | concepts | anthropology | 9 | 0 | — |
| con-polygamy | concepts | anthropology | 9 | 0 | — |
| con-hist-doc-35 | concepts | historiography | 9 | 0 | — |
| con-hist-social-11 | concepts | historiography | 12 | 0 | — |
| con-legal-comp-30 | concepts | legal-theory | 8 | 0 | — |
| con-legal-49 | concepts | legal-theory | 9 | 0 | — |
| con-revolution-permanent | concepts | historiography | 12 | 0 | — |
| con-hist-doc-21 | concepts | historiography | 9 | 0 | — |
| con-anth-complete-9 | concepts | anthropology | 8 | 0 | — |
| con-eth-applied-39 | concepts | ethics | 8 | 0 | — |
| con-legal-rights-42 | concepts | legal-theory | 8 | 0 | — |
| con-eth-comp-21 | concepts | ethics | 8 | 0 | — |
| con-anthro-applied-9 | concepts | anthropology | 12 | 0 | — |
| con-ethics-virtue-54 | concepts | ethics | 6 | 0 | — |
| con-justice-law | concepts | legal-theory | 10 | 1 | studies/stu-bohannan-tiv-bride-price.md |
| con-anth-final-2 | concepts | anthropology | 8 | 0 | — |
| con-bride-service | concepts | anthropology | 9 | 0 | — |
| con-hist-final-29 | concepts | historiography | 10 | 0 | — |
| con-flourishing | concepts | ethics | 10 | 0 | — |
| con-property-law | concepts | legal-theory | 10 | 0 | — |
| con-moiety | concepts | anthropology | 9 | 0 | — |
| con-hist-social-7 | concepts | historiography | 12 | 0 | — |
| con-hist-doc-31 | concepts | historiography | 9 | 0 | — |
| con-social-19 | concepts | anthropology | 9 | 0 | — |
| con-social-6 | concepts | anthropology | 9 | 0 | — |
| con-hist-complete-15 | concepts | historiography | 8 | 0 | — |
| con-eth-applied-32 | concepts | ethics | 8 | 0 | — |
| con-legal-rights-49 | concepts | legal-theory | 8 | 0 | — |
| con-anthro-applied-2 | concepts | anthropology | 12 | 0 | — |
| con-progress-history | concepts | historiography | 12 | 0 | — |
| con-interpretation-meaning | concepts | anthropology | 12 | 0 | — |
| con-mysticism | concepts | anthropology | 12 | 0 | — |
| con-anth-final-9 | concepts | anthropology | 8 | 0 | — |
| con-anth-complete-2 | concepts | anthropology | 8 | 0 | — |
| con-free-will-history | concepts | historiography | 12 | 0 | — |
| con-legal-52 | concepts | legal-theory | 9 | 0 | — |
| con-consequentialism | concepts | ethics | 10 | 0 | — |
| con-social-12 | concepts | anthropology | 9 | 0 | — |
| con-hist-final-22 | concepts | historiography | 8 | 0 | — |
| con-eth-41 | concepts | ethics | 9 | 0 | — |
| con-hist-final-16 | concepts | historiography | 8 | 0 | — |
| con-anthro-applied-6 | concepts | anthropology | 12 | 0 | — |
| con-historical-memory | concepts | historiography | 9 | 0 | — |
| con-eth-applied-36 | concepts | ethics | 8 | 0 | — |
| con-hist-complete-11 | concepts | historiography | 8 | 0 | — |
| con-simultaneity-history | concepts | historiography | 9 | 0 | — |
| con-anth-complete-6 | concepts | anthropology | 8 | 0 | — |
| con-representation | concepts | anthropology | 10 | 0 | — |
| con-collective-memory | concepts | historiography | 9 | 1 | schools/sch-memory-studies-comparative.md |
| con-matrilineage | concepts | anthropology | 9 | 0 | — |
| con-magic-religion | concepts | anthropology | 12 | 1 | concepts/con-magic-religion-frazer.md |
| con-social-16 | concepts | anthropology | 9 | 0 | — |
| con-social-9 | concepts | anthropology | 9 | 0 | — |
| con-legal-56 | concepts | legal-theory | 9 | 0 | — |
| con-eth-45 | concepts | ethics | 9 | 0 | — |
| con-hist-social-8 | concepts | historiography | 12 | 0 | — |
| con-hist-final-26 | concepts | historiography | 8 | 0 | — |
| con-anthro-applied-7 | concepts | anthropology | 12 | 0 | — |
| con-hist-complete-10 | concepts | historiography | 10 | 0 | — |
| con-eth-applied-37 | concepts | ethics | 8 | 0 | — |
| con-happiness | concepts | ethics | 10 | 0 | — |
| con-anth-complete-7 | concepts | anthropology | 8 | 0 | — |
| con-history-future | concepts | historiography | 9 | 0 | — |
| con-social-17 | concepts | anthropology | 9 | 0 | — |
| con-social-8 | concepts | anthropology | 9 | 0 | — |
| con-legal-57 | concepts | legal-theory | 9 | 0 | — |
| con-eth-44 | concepts | ethics | 9 | 0 | — |
| con-virtue | concepts | ethics | 10 | 0 | — |
| con-hist-social-9 | concepts | historiography | 12 | 0 | — |
| con-hist-final-27 | concepts | historiography | 8 | 0 | — |
| con-eth-applied-33 | concepts | ethics | 8 | 0 | — |
| con-hist-complete-14 | concepts | historiography | 8 | 0 | — |
| con-legal-rights-48 | concepts | legal-theory | 8 | 0 | — |
| con-anthro-applied-3 | concepts | anthropology | 12 | 0 | — |
| con-anth-final-8 | concepts | anthropology | 6 | 0 | — |
| con-symbol-symbolism | concepts | anthropology | 12 | 0 | — |
| con-anth-complete-3 | concepts | anthropology | 8 | 0 | — |
| con-discourse-analysis | concepts | anthropology | 12 | 0 | — |
| con-legal-53 | concepts | legal-theory | 9 | 0 | — |
| con-historical-time-concept | concepts | historiography | 9 | 0 | — |
| con-alternative-history | concepts | historiography | 9 | 0 | — |
| con-decline-history | concepts | historiography | 10 | 0 | — |
| con-social-13 | concepts | anthropology | 9 | 0 | — |
| con-hist-final-23 | concepts | historiography | 8 | 0 | — |
| con-eth-40 | concepts | ethics | 9 | 0 | — |
| con-hist-final-17 | concepts | historiography | 10 | 0 | — |
| con-duty | concepts | ethics | 10 | 0 | — |
| con-obligation | concepts | legal-theory | 10 | 0 | — |
| con-hist-complete-13 | concepts | historiography | 8 | 0 | — |
| con-eth-applied-34 | concepts | ethics | 8 | 0 | — |
| con-ethics-virtue-59 | concepts | ethics | 8 | 0 | — |
| con-anthro-applied-4 | concepts | anthropology | 12 | 0 | — |
| con-social-organization | concepts | anthropology | 9 | 0 | — |
| con-anth-complete-4 | concepts | anthropology | 8 | 0 | — |
| con-social-14 | concepts | anthropology | 9 | 0 | — |
| con-monogamy | concepts | anthropology | 9 | 0 | — |
| con-revolution-history | concepts | historiography | 10 | 0 | — |
| con-legal-54 | concepts | legal-theory | 9 | 0 | — |
| con-eth-47 | concepts | ethics | 9 | 0 | — |
| con-uneven-development | concepts | historiography | 14 | 0 | — |
| con-hist-final-24 | concepts | historiography | 8 | 0 | — |
| con-idealism-history | concepts | historiography | 12 | 0 | — |
| con-punishment | concepts | legal-theory | 10 | 0 | — |
| con-anthro-applied-0 | concepts | anthropology | 12 | 0 | — |
| con-eth-applied-30 | concepts | ethics | 8 | 0 | — |
| con-hist-complete-17 | concepts | historiography | 8 | 0 | — |
| con-eth-comp-28 | concepts | ethics | 12 | 0 | — |
| con-materialism-history | concepts | historiography | 12 | 0 | — |
| con-legal-comp-39 | concepts | legal-theory | 8 | 0 | — |
| con-rule-of-law | concepts | legal-theory | 12 | 0 | — |
| con-anth-complete-0 | concepts | anthropology | 8 | 0 | — |
| con-hist-doc-28 | concepts | historiography | 9 | 0 | — |
| con-translation-anthropology | concepts | anthropology | 12 | 0 | — |
| con-legal-50 | concepts | legal-theory | 9 | 0 | — |
| con-social-10 | concepts | anthropology | 9 | 0 | — |
| con-reform-history | concepts | historiography | 10 | 0 | — |
| con-dignity | concepts | ethics | 10 | 0 | — |
| con-hist-final-20 | concepts | historiography | 8 | 0 | — |
| con-initiation | concepts | anthropology | 12 | 0 | — |
| con-eth-43 | concepts | ethics | 9 | 0 | — |
| con-anthro-applied-1 | concepts | anthropology | 12 | 0 | — |
| con-hist-complete-16 | concepts | historiography | 8 | 0 | — |
| con-deontology | concepts | ethics | 10 | 0 | — |
| con-eth-applied-31 | concepts | ethics | 8 | 0 | — |
| con-eth-comp-29 | concepts | ethics | 8 | 0 | — |
| con-world-systems | concepts | historiography | 12 | 0 | — |
| con-legal-comp-38 | concepts | legal-theory | 10 | 0 | — |
| con-deep-time | concepts | historiography | 9 | 0 | — |
| con-anth-complete-1 | concepts | anthropology | 8 | 0 | — |
| con-hist-doc-29 | concepts | historiography | 9 | 0 | — |
| con-sacred-profane | concepts | anthropology | 12 | 0 | — |
| con-legal-51 | concepts | legal-theory | 11 | 0 | — |
| con-social-11 | concepts | anthropology | 9 | 0 | — |
| con-hist-final-21 | concepts | historiography | 8 | 0 | — |
| con-rights | concepts | ethics | 10 | 0 | — |
| con-hist-final-15 | concepts | historiography | 8 | 0 | — |
| con-secret-societies | concepts | anthropology | 12 | 0 | — |
| con-eth-42 | concepts | ethics | 9 | 0 | — |
| con-eth-applied-35 | concepts | ethics | 10 | 0 | — |
| con-hist-complete-12 | concepts | historiography | 8 | 0 | — |
| con-anthro-applied-5 | concepts | anthropology | 12 | 0 | — |
| con-ethics-virtue-58 | concepts | ethics | 6 | 0 | — |
| con-anth-complete-5 | concepts | anthropology | 8 | 0 | — |
| con-social-15 | concepts | anthropology | 9 | 0 | — |
| con-language-culture | concepts | anthropology | 12 | 0 | — |
| con-transnational-history | concepts | historiography | 14 | 1 | schools/sch-world-history-transnational.md |
| con-legal-55 | concepts | legal-theory | 9 | 0 | — |
| con-eth-46 | concepts | ethics | 9 | 0 | — |
| con-hist-final-25 | concepts | historiography | 8 | 0 | — |
| con-hist-doc-26 | concepts | historiography | 9 | 0 | — |
| con-ecstasy-trance | concepts | anthropology | 12 | 0 | — |
| con-legal-comp-37 | concepts | legal-theory | 8 | 0 | — |
| con-eth-38 | concepts | ethics | 9 | 0 | — |
| con-anth-final-5 | concepts | anthropology | 8 | 0 | — |
| con-hist-complete-19 | concepts | historiography | 8 | 0 | — |
| con-anth-final-11 | concepts | anthropology | 6 | 0 | — |
| con-eth-comp-26 | concepts | ethics | 8 | 0 | — |
| con-legal-rights-45 | concepts | legal-theory | 8 | 0 | — |
| con-ethics-virtue-53 | concepts | ethics | 6 | 0 | — |
| con-autonomy | concepts | ethics | 12 | 0 | — |
| con-hist-social-0 | concepts | historiography | 12 | 0 | — |
| con-historical-consciousness | concepts | historiography | 9 | 0 | — |
| con-social-1 | concepts | anthropology | 9 | 0 | — |
| con-hist-doc-36 | concepts | historiography | 9 | 0 | — |
| con-positivism-history | concepts | historiography | 12 | 0 | — |
| con-legal-comp-33 | concepts | legal-theory | 8 | 0 | — |
| con-hist-doc-22 | concepts | historiography | 9 | 0 | — |
| con-ethics-virtue-57 | concepts | ethics | 6 | 0 | — |
| con-legal-rights-41 | concepts | legal-theory | 8 | 0 | — |
| con-eth-comp-22 | concepts | ethics | 8 | 0 | — |
| con-anth-final-1 | concepts | anthropology | 6 | 0 | — |
| con-econ-anthropology-13 | concepts | anthropology | 12 | 0 | — |
| con-hist-social-4 | concepts | historiography | 14 | 0 | — |
| con-hist-doc-32 | concepts | historiography | 9 | 0 | — |
| con-conversion | concepts | anthropology | 12 | 0 | — |
| con-social-5 | concepts | anthropology | 9 | 0 | — |
| con-postcolonial-history | concepts | historiography | 16 | 0 | — |
| con-legal-comp-32 | concepts | legal-theory | 8 | 0 | — |
| con-hist-doc-23 | concepts | historiography | 9 | 0 | — |
| con-ethics-virtue-56 | concepts | ethics | 6 | 0 | — |
| con-anth-final-14 | concepts | anthropology | 6 | 0 | — |
| con-eth-comp-23 | concepts | ethics | 8 | 0 | — |
| con-legal-rights-40 | concepts | legal-theory | 10 | 0 | — |
| con-anth-final-0 | concepts | anthropology | 6 | 0 | — |
| con-patrilineage | concepts | anthropology | 9 | 0 | — |
| con-prophecy-divination | concepts | anthropology | 12 | 0 | — |
| con-econ-anthropology-12 | concepts | anthropology | 12 | 0 | — |
| con-hist-social-5 | concepts | historiography | 12 | 0 | — |
| con-hist-doc-33 | concepts | historiography | 9 | 0 | — |
| con-social-4 | concepts | anthropology | 9 | 0 | — |
| con-hist-doc-27 | concepts | historiography | 9 | 0 | — |
| con-positivism-law | concepts | legal-theory | 12 | 0 | — |
| con-legal-comp-36 | concepts | legal-theory | 8 | 0 | — |
| con-anth-final-4 | concepts | anthropology | 8 | 0 | — |
| con-eth-39 | concepts | ethics | 9 | 0 | — |
| con-hist-complete-18 | concepts | historiography | 8 | 0 | — |
| con-legal-rights-44 | concepts | legal-theory | 8 | 0 | — |
| con-eth-comp-27 | concepts | ethics | 8 | 0 | — |
| con-anth-final-10 | concepts | anthropology | 6 | 0 | — |
| con-ethics-virtue-52 | concepts | ethics | 8 | 0 | — |
| con-counter-factual-history | concepts | historiography | 9 | 0 | — |
| con-hist-social-1 | concepts | historiography | 12 | 0 | — |
| con-intention | concepts | ethics | 12 | 0 | — |
| con-social-0 | concepts | anthropology | 9 | 0 | — |
| con-god-spirits | concepts | anthropology | 12 | 0 | — |
| con-hist-doc-37 | concepts | historiography | 9 | 0 | — |

**Protected file excluded from deletion despite matching Template D pattern:**

- `con-historical-imagination` (concepts/historiography) — matches the title-repeated+Pending stub pattern (9 words) but is listed in protected.txt, so left untouched and NOT deleted.


## Uncertain (not deleted, flagged for human/other-agent review)

- None beyond the protected-file exclusions above. I limited Task 2 to the four precisely-specified, corpus-wide-verified heuristics from the audit reports (Anthropology-node stub, the two named fabricated thinkers, the two linguistics verbatim templates, and the title-duplicated+Pending stub). I did not attempt the broader, fuzzier categories flagged in the audits (e.g. the ~500-file "no sources yet" boilerplate, the arab-thought Phase-3 skeleton batch, general sub-300-word thinness) because those files generally have real, topic-specific, verifiable content (correct names/dates/attributions) and fail the junk test — they are "real but thin," which the spec says to leave alone.

## Integrity checker note (unrelated to this session's edits)

A first `check_content_integrity.py --lang ar` run (13,088 files) flagged one dangling reference: `con-biogenetic-versus-cultural-kinship` → `sch-american-kinship-studies` (related + edge). Investigation showed `schools/sch-american-kinship-studies.md` was an **untracked file** (`git status` confirmed it wasn't yet committed) — i.e. a concurrent session was actively writing it at that moment (per the standing memory note on concurrent Atlas sessions), not a file this Phase C pass touched, deleted, or broke. A re-run of the checker (13,094 files — 6 more than the first run, confirming the other session added files in the interim) came back **clean, zero problems**, confirming this was transient and unrelated to Phase C.

## Round 3

### Merges (Task 1, spec-listed pairs)

- `schools/sch-environmental-ethics.md` ← `schools/environmental-ethics.md`: the duplicate was an unfilled template stub (empty headings only, no body content, `related: []`). No external references to `environmental-ethics` existed elsewhere in content/ar. Deleted with no content to merge.
- `schools/sch-feminist-jurisprudence.md` ← `schools/feminist-jurisprudence.md`: same pattern — empty template stub, no external references. Deleted.
- `schools/sch-legal-pluralism.md` ← `schools/legal-pluralism.md`: same pattern — empty template stub, no external references. Deleted.
- `concepts/con-categorical-imperative.md` ← `concepts/categorical-imperative.md`: both had real content. Kept `con-categorical-imperative` (per spec instruction) and merged in the unique "القيد" (limitation) section and the four-item bibliography from `categorical-imperative.md`, which the canonical file lacked; added `sch-deontological-ethics-kant` to `related`. Repointed the one external reference (`schools/sch-deontological-ethics-kant.md`, related-list entry) from `categorical-imperative` to `con-categorical-imperative`. Deleted `categorical-imperative.md`.
- `schools/sch-virtue-ethics.md` ← `schools/sch-virtue-ethics-aristotle.md`: **BLOCKED** — `sch-virtue-ethics-aristotle` is listed in protected.txt (another session may be editing it). Not touched. 8 files reference it (`con-mean-between-extremes`, `con-practical-wisdom`, `con-eudaimonia-flourishing`, `con-character-ethics`, `con-virtue-habit-formation`, `con-vice`, `con-virtue-development`, `con-moral-exemplars`) — these repoints are listed here for a future pass, not performed.
- `concepts/con-shunyata.md` ← `concepts/con-shunyata-emptiness.md`, `concepts/con-buddhist-emptiness-shunyata.md`:
  - `con-shunyata-emptiness` is listed in protected.txt. **BLOCKED**, not touched. It is a near-duplicate of `con-shunyata` (confirmed: same `en:` title, same Nāgārjuna/Madhyamaka topic; its own `gaps` note already flags this as an unresolved duplicate). 8 files reference it (`wrk-religion-and-nothingness-nishitani`, `con-upaya-skillful-means`, `con-two-truths-doctrine-buddhist`, `con-trisvabhava-three-natures`, `con-one-mind-two-aspects-wonhyo`, `con-kshanikavada-universal-momentariness`, `br-madhyamaka-svatantrika`, `br-madhyamaka-prasangika`) — listed here for a future pass.
  - `con-buddhist-emptiness-shunyata` is not protected. Confirmed it covers the same concept (Śūnyatā/Nāgārjuna/Madhyamaka) from a Buddhist-psychology angle (CBT/ACT applications, Tsongkhapa, Wallace). Merged its unique "في علم النفس" (psychology applications) content and related thinkers (`thk-tsongkhapa`, `thk-beck`, `thk-lstevenhayes`, `thk-lcwallace`, `sch-buddhist-psychology`) into `con-shunyata.md`. Repointed 3 external references (`con-absolute-nothingness-zettai-mu.md`, `sch-buddhist-psychology.md`, `con-pratityasamutpada-dependent-origination.md`) from `con-buddhist-emptiness-shunyata` to `con-shunyata`. Deleted `con-buddhist-emptiness-shunyata.md`.
- `schools/sch-refugee-displacement-anthropology.md` ← `schools/migration-displacement-school.md`: **BLOCKED** — `sch-refugee-displacement-anthropology` (the canonical target) is listed in protected.txt. Not touched; not investigated further since the canonical file itself cannot be edited.

### Merges (Task 1, additional pairs found by scanning for slug ± prefix/suffix with matching `en:` title)

Scanned all `en:` titles within each folder (concepts, schools, thinkers, works, etc.) for near-duplicate slugs. Most matches found (mainly in `thinkers/` and `works/`) were legitimate distinct files — e.g. a person's main profile plus a separate `-bio` sub-file, or genuinely different works/editions — and were left alone. Clear duplicate pairs (same `en:` title, same entity, one side an empty/near-empty template stub or fully overlapping content) that were merged:

- `concepts/con-authenticity.md` ← `concepts/con-authenticity-ethics.md`: the `-ethics` file was a bare template stub (title heading only, no body, `related: []`). No external references. Deleted, no content lost.
- `concepts/con-cosmopolitanism.md` ← `concepts/con-cosmopolitanism-ethics.md`: same pattern — empty stub with blank section headings, no external references. Deleted.
- `schools/sch-medical-anthropology.md` ← `schools/sch-medical-anthropology-expanded.md`: both had real content on the same topic (medical anthropology, same thinkers Kleinman/Farmer/Scheper-Hughes). Merged the "-expanded" file's unique "التطبيقات" section and its Farmer/Lock-Nguyen bibliography entries and `thk-paul-farmer`/`thk-nancy-scheper-hughes` related-links into `sch-medical-anthropology.md`. No external references to the "-expanded" slug existed. Deleted `sch-medical-anthropology-expanded.md`.
- `concepts/con-rule-of-recognition-hart.md` ← `concepts/con-rule-recognition.md`: the latter was a bare template stub, no external references. Deleted.
- `concepts/con-matrix-language-frame-model.md` ← `concepts/con-matrix-language-frame-model-myers-scotton.md`: the latter was literally `[تحت الإنشاء - سيُملأ بتفاصيل شاملة لاحقاً]` (under construction placeholder), no external references. Deleted.
- `schools/sch-conversation-analysis.md` ← `schools/sch-conversational-analysis.md`: the latter was a two-sentence stub, no external references. Deleted.
- `concepts/con-doctrine-of-double-effect.md` ← `concepts/con-doctrine-double-effect.md`: the latter was an empty template stub, no external references. Deleted.
- `schools/sch-comtean-positivism.md` ← `schools/sch-comtian-positivism.md`: both had full, real, non-overlapping content on the same school (same `en: Comtean Positivism`) — one written from a sociology angle, one from a philosophy angle. Kept `sch-comtean-positivism` (more incoming references). Merged unique sections ("المساهمات والفروع", "القيد", extra bibliography, `sch-positivism-latin`/`con-verification-principle` related links) from `sch-comtian-positivism` into it. Repointed 3 external references: `schools/sch-utilitarianism.md` (edge target), `schools/sch-positivism-latin.md` (edge target + related-list id/title), and `thinkers/thk-comte.md` (related-list entry, and rewrote its own `gaps` note that had explicitly — and incorrectly — described the two files as independent). Deleted `sch-comtian-positivism.md`.
- `concepts/con-wahdat-al-wujud.md` ← `concepts/con-wahdat-wujud.md`: the latter was a bare template stub (`[يتطلب توسيع نصي]`, `[سيتم توثيق المصادر]`), no external references, while `con-wahdat-al-wujud` already has full content on Ibn Arabi's doctrine. Deleted the stub.

Pairs identified but **left unmerged** (both sides have substantial, non-overlapping real content and/or the match was judged not a clear duplicate, so out of scope for this pass): `con-rule-of-recognition-hart`-style biography variants in `thinkers/` and `works/` (e.g. `thk-david-graeber`/`thk-graeber`, `wrk-nicomachean-ethics`/`wrk-nicomachean-ethics-aristotle`, etc.) — these look like intentional main-profile + `-bio`/alternate-edition pairs rather than accidental duplicates, and many touch protected.txt-listed files; not investigated further given scope.

### Task 2: unverifiable thinkers

- `thk-jdavid` ("Jordan David") — **BLOCKED**, file is listed in protected.txt. WebSearch for "Jordan David" + social therapy / East Side Institute / Castillo Theatre / Fred Newman / Lois Holzman returned no matching person; the only documented Castillo Theatre figure in that role is Dan Friedman, already noted (and explicitly not substituted) in the file's own `gaps` history. Confirms the file's existing `status: quarantined` finding. No file edit made (protected); flagged here instead.
- `thk-leehyungjun` ("Lee Hyung-Jun", 이형준) — **BLOCKED**, file is listed in protected.txt. WebSearch for 이형준 + 화병 (hwabyung) + ACT (수용전념치료) + 정신과의사 returned no matching psychiatrist; known researchers in this field are Lee Si-hyung (이시형), Min Sung-gil (민성길), and Kim Jong-woo (김종우) — none matches "Lee Hyung-Jun." Confirms the file's own existing `gaps` note reaching the same conclusion. No file edit made (protected); flagged here instead.

### Task 3: placeholder id

- `schools/sch-regional-persian-anthropology.md`: `id: "SCH-[PLACEHOLDER]"` → `id: "SCH-13226"`. Confirmed no other file in content/ar used `SCH-13226` before the change.

### Blocked items requiring a follow-up pass (protected files)

1. Merge `sch-virtue-ethics-aristotle` into `sch-virtue-ethics` and repoint 8 references.
2. Merge `con-shunyata-emptiness` into `con-shunyata` and repoint 8 references.
3. Merge `migration-displacement-school` into `sch-refugee-displacement-anthropology`.
4. Delete/fix `thk-jdavid` and `thk-leehyungjun` (both confirmed unverifiable by WebSearch in this session; both currently already carry accurate `gaps`/`status: quarantined` notes documenting this).
