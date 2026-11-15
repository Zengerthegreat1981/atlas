# Closed v1 scope for the English Psychology module (audit P0.5). Each line: slug (AR slug reused when it exists).
# Group = coverage area from the audit §4.1. Entries already in content/en are skipped by the generator.
SCOPE = {
"foundations-and-schools": """sch-psychoanalysis sch-analytical-psychology sch-behaviorism sch-cognitive-psychology sch-cognitive-behavioral
sch-humanistic sch-developmental sch-social-psychology sch-biological-neuro sch-cognitive-neuroscience sch-positive-psychology
sch-object-relations sch-cultural-psychology sch-cross-cultural-psychology sch-critical-psychology sch-evolutionary-psychology
sch-emotion-psychology sch-existential-therapy sch-transpersonal sch-trauma-psychology sch-culture-and-personality
br-classical-psychoanalysis br-jungian br-attachment-theory br-person-centered br-radical-behaviorism br-self-actualization-maslow br-social-learning-theory""",
"clinical-practice": """sch-act sch-dbt sch-emdr sch-mbct sch-narrative-therapy sch-motivational-interviewing sch-systemic-family sch-gestalt-therapy
sch-solution-focused sch-ipt sch-rebt sch-polyvagal-informed-therapy sch-istdp br-structural-family""",
"thinkers": """thk-freud thk-jung thk-adler thk-klein thk-winnicott thk-bion thk-lacan thk-kohut thk-fromm thk-sullivan thk-erikson
thk-rogers thk-maslow thk-fskinner thk-jwatson thk-ipavlov thk-james thk-piaget thk-vygotsky thk-bowlby thk-ainsworth
thk-abandura thk-beck thk-ellis thk-kahneman thk-amos-tversky thk-mseligman thk-csikszentmihalyi thk-elizabeth-loftus thk-dweck
thk-gilligan thk-gardner thk-gallport thk-heysenck thk-cialdini thk-fperls thk-sminuchin thk-mbowen thk-mlinehan thk-lstevenhayes
thk-jkabat-zinn thk-fonagy thk-stephen-porges thk-damasio thk-panksepp thk-dsiegel thk-jherman thk-francine-shapiro thk-gendlin
thk-szasz thk-sdeshacer thk-mwhite thk-wampold thk-ectolman thk-dbaumrind thk-hillman""",
"concepts": """con-unconscious con-transference con-repression con-archetype con-collective-unconscious con-complex con-attachment-styles
con-secure-attachment con-attention con-memory con-working-memory-sentence-parsing con-neuroplasticity con-cognitive-distortion
con-cognitive-dissonance con-classical-conditioning con-operant-conditioning con-social-learning con-latent-learning con-self-actualization
con-self-efficacy con-mentalization con-mindfulness con-flow con-loss-aversion con-fundamental-attribution-error
con-window-of-tolerance con-polyvagal-theory con-differentiation-self con-false-self-vs-true-self con-triangulation
con-intersubjectivity con-felt-sense con-primary-emotion con-emotional-intelligence con-moral-development-gilligan
con-diagnostic-reliability con-somatic-memory con-motivational-interviewing-oars con-hypnotic-trance""",
"research-and-assessment": """stu-asch-conformity stu-milgram-obedience stu-stanford-prison stu-mischel-marshmallow-test stu-bandura-bobo-doll
stu-festinger-cognitive-dissonance stu-bartlett-war-of-ghosts stu-miller-magical-number-seven stu-kahneman-tversky-prospect-theory
stu-kahneman-tversky-heuristics-biases stu-baddeley-hitch-working-memory stu-loftus-misinformation-effect stu-pavlov-classical-conditioning
stu-rosenhan-on-being-sane stu-seligman-maier-learned-helplessness stu-harlow-rhesus-monkeys stu-ainsworth-strange-situation
stu-darley-latane-bystander stu-kohlberg-moral-development stu-clark-doll-test stu-scoville-milner-patient-hm
stu-sperry-gazzaniga-split-brain stu-werner-kauai-resilience stu-dunedin-longitudinal-study stu-harvard-adult-development
stu-wundt-leipzig-1879 stu-tajfel-minimal-group stu-thorndike-puzzle-box stu-tolman-cognitive-maps stu-wertheimer-gestalt stu-lorenz-imprinting
ins-bdi-ii ins-hamilton-hdrs ins-neo-pi-r ins-wais ins-wisc ins-stanford-binet ins-mbti ins-rorschach ins-scid-5 ins-swls ins-cattell-16pf ins-eysenck-epq
dbt-psychology-replication-crisis dbt-nature-vs-nurture-intelligence-personality dbt-projective-tests-validity""",
"disorders-and-classification": """dis-bpd dis-schizophrenia dis-bipolar-i dis-ocd dis-adhd dis-autism-spectrum dis-social-anxiety-disorder
dis-major-neurocognitive dis-somatic-symptom-disorder dis-alcohol-use-disorder dis-acute-stress-disorder dis-adjustment-disorders
dis-dissociative-amnesia classification-dsm-5-tr classification-icd-11""",
"works": """wrk-thinking-fast-slow wrk-freud-interpretation-of-dreams wrk-attachment-loss-volume1 wrk-beck-cognitive-therapy-depression
wrk-flow-csikszentmihalyi wrk-ecrits wrk-hayes-acceptance-commitment-therapy""",
}

# Entries with no Arabic source: authored from scratch (conservative, sourced). slug -> (folder, English title, brief)
NEW = {
 "fld-psychology": ("fields", "Psychology", "Module root: what psychology is, its main subfields, how the atlas is organised, reading path"),
 "con-reliability-validity": ("concepts", "Reliability and Validity", "psychometric concepts, types, limits"),
 "con-experimental-design": ("concepts", "Experimental Design in Psychology", "randomisation, control, between/within designs, confounds, quasi-experiments"),
 "con-research-ethics-psychology": ("concepts", "Research Ethics in Psychology", "informed consent, deception, IRBs, Belmont/APA principles, historical cases"),
 "con-nature-nurture": ("concepts", "Nature and Nurture", "heritability, gene-environment interplay, twin/adoption designs, misconceptions"),
 "con-intelligence": ("concepts", "Intelligence", "Spearman g, Cattell-Horn-Carroll, Gardner critique, IQ testing, Flynn effect, limits"),
 "con-personality-traits": ("concepts", "Personality Traits and the Big Five", "trait theory, Big Five, stability, criticisms"),
 "con-motivation": ("concepts", "Motivation", "drive, incentive, self-determination, expectancy, Maslow critique"),
 "con-memory-systems": ("concepts", "Memory Systems", "sensory/short-term/working/long-term, episodic/semantic/procedural, reconstruction"),
 "con-learning-theories": ("concepts", "Learning Theories", "classical, operant, observational, cognitive learning; comparison"),
 "con-replication-crisis": ("concepts", "The Replication Crisis", "Open Science Collaboration 2015, questionable research practices, preregistration, responses"),
}
