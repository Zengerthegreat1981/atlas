# Closed v1 scope for the English Philosophy module (audit P0.5, §4.2). AR slugs reused where they exist.
SCOPE = {
"schools-ancient-medieval": """sch-academy-platonic sch-aristotelianism sch-stoicism sch-epicureanism sch-pyrrhonism sch-academic-skepticism sch-sophistry
sch-neoplatonism sch-patristics sch-scholasticism sch-thomism sch-ockhamism sch-augustinianism sch-atomism-greek sch-renaissance-humanism""",
"schools-early-modern-modern": """sch-cartesianism sch-leibnizianism sch-spinozism sch-british-empiricism sch-lockeanism sch-humeanism sch-enlightenment
sch-kant-critical sch-german-idealism sch-hegelianism sch-marxism sch-pragmatism-classical sch-utilitarianism sch-classical-liberalism-early""",
"schools-contemporary": """sch-phenomenology sch-phenomenology-existential sch-existentialism sch-existentialism-atheist sch-hermeneutics sch-vienna-circle
sch-logical-atomism sch-ordinary-language sch-phil-mind-analytic sch-analytic-metaphysics sch-phil-science sch-post-structuralism sch-deconstruction
sch-frankfurt-school sch-rawlsianism sch-communitarianism sch-postcolonial-philosophy sch-postmodernism-philosophical sch-decolonial-philosophy""",
"schools-islamic-indian-chinese-other": """sch-islamic-peripatetic sch-ashariyya sch-mutazila sch-ishraqiyya sch-transcendent-theosophy sch-andalusian-philosophy
sch-islamic-sufism sch-advaita-vedanta sch-vedanta sch-nyaya sch-samkhya sch-jainism sch-buddhism-early sch-madhyamaka sch-yogacara sch-charvaka
sch-confucian-early sch-daoism-philosophical sch-mohism sch-legalism sch-neoconfucianism sch-lixue sch-xinxue sch-kyoto sch-ubuntu sch-ethnophilosophy
sch-african-professional-philosophy sch-egyptian-maat sch-zoroastrian-philosophy""",
"thinkers-ancient-medieval": """thk-socrates thk-plato thk-aristotle thk-heraclitus thk-parmenides thk-epicur thk-epictetus thk-marcus-aurelius thk-plotinus
thk-augustine thk-aquinas thk-william-ockham thk-ibn-sina thk-al-farabi thk-al-kindi thk-al-ghazali thk-ibn-rushd thk-ibn-tufayl thk-ibn-arabi
thk-suhrawardi thk-mulla-sadra thk-fakhr-razi thk-ashari thk-buddha thk-nagarjuna thk-shankara thk-mahavira thk-confucius thk-mencius thk-xunzi
thk-laozi thk-zhuangzi thk-zhu-xi thk-wang-yangming""",
"thinkers-modern-contemporary": """thk-descartes thk-spinoza thk-leibniz thk-hobbes thk-locke thk-hume thk-rousseau thk-voltaire thk-kant thk-fichte thk-schelling
thk-hegel thk-schopenhauer thk-mill thk-bentham thk-peirce thk-dewey thk-bergson thk-brentano thk-dilthey thk-nishida thk-gfrege thk-bertrand-russell
thk-lwittgenstein thk-rcarnap thk-jaustin thk-wquine thk-karl-popper thk-thomas-kuhn thk-hputnam thk-nagel thk-john-searle thk-daniel-dennett
thk-david-chalmers thk-rawls thk-nozick thk-macintyre thk-sandel thk-rorty thk-merleau-ponty thk-gadamer thk-ricoeur thk-derrida thk-deleuze
thk-habermas thk-adorno thk-arendt thk-mbuber thk-mohammed-abed-al-jabri thk-arne-naess thk-biko""",
"concepts": """con-dialectics con-intentionality con-epoche-suspension con-cogito con-res-cogitans-res-extensa con-hermeneutic-circle con-shunyata
con-anatta-non-self-concept con-dao con-li con-ren con-wahdat-al-wujud con-universals-debate con-hylomorphism con-monad con-will-to-power
con-falsificationism-popper con-hard-problem-of-consciousness con-functionalism-mind con-sense-vs-reference con-social-contract-theory
con-natural-law-aquinas-concept con-lived-body con-alienation-marx con-anamnesis-recollection con-ataraxia con-atman-brahman-vedanta con-maya-vedanta
con-ahimsa con-nirvana-extinction con-yin-yang con-knowledge-by-presence-ilm-huduri con-asalat-al-wujud-primacy-of-existence con-absolute-spirit-hegel
con-autonomy-kantian con-eudaimonia-wellbeing con-virtue-ethics con-orientalism""",
"works": """wrk-republic-plato wrk-apology-plato wrk-nicomachean-ethics wrk-metaphysics-aristotle wrk-meditations-on-first-philosophy-descartes
wrk-critique-of-pure-reason-kant wrk-critique-of-practical-reason-kant wrk-spinoza-ethics wrk-hegel-phenomenology-spirit wrk-tractatus
wrk-philosophical-investigations-wittgenstein wrk-kuhn-structure-revolutions wrk-two-dogmas wrk-the-social-contract-rousseau wrk-on-liberty-mill
wrk-the-prince-machiavelli wrk-daodejing wrk-lunyu wrk-tahafut-al-falasifa-ghazali wrk-al-shifa-avicenna wrk-summa-theologiae-aquinas
wrk-on-the-genealogy-of-morals-nietzsche wrk-philosophy-mirror-nature wrk-monadology-leibniz wrk-consolation-philosophy
wrk-an-inquiry-into-the-good-nishida wrk-hikmat-al-ishraq-suhrawardi wrk-fusus-al-hikam-ibn-arabi wrk-al-muqaddimah-ibn-khaldun""",
"debates": """dbt-mind-body-dualism-vs-physicalism dbt-free-will-vs-determinism dbt-realism-vs-nominalism dbt-advaita-vs-dvaita dbt-thomism-vs-scotism
dbt-qadar-free-will-in-kalam dbt-extended-mind-clark-chalmers dbt-liberalism-vs-communitarianism dbt-rawls-nozick-justice dbt-human-nature-debate""",
}
NEW = {
 "fld-philosophy": ("fields", "Philosophy", "Module root: what philosophy is, its main branches, traditions covered, how the atlas is organised, reading path"),
 "fld-logic": ("fields", "Logic", "deductive/inductive reasoning, validity vs soundness, formal logic, fallacies, non-classical logics, history (Aristotle to Frege to Godel), limits"),
 "fld-epistemology": ("fields", "Epistemology", "knowledge, justified true belief and Gettier, rationalism/empiricism, skepticism, internalism/externalism, social epistemology"),
 "fld-metaphysics": ("fields", "Metaphysics", "being, substance, universals, causation, time, modality, personal identity, free will; debates"),
 "fld-philosophy-of-mind": ("fields", "Philosophy of Mind", "dualism, physicalism, functionalism, consciousness, intentionality, personal identity, AI"),
 "fld-philosophy-of-language": ("fields", "Philosophy of Language", "meaning, reference, speech acts, Frege, Wittgenstein, Kripke, pragmatics"),
 "fld-philosophy-of-science": ("fields", "Philosophy of Science", "demarcation, induction, falsification, paradigms, realism vs anti-realism, explanation"),
 "fld-political-philosophy": ("fields", "Political Philosophy", "legitimacy, justice, liberty, social contract, major traditions"),
 "fld-aesthetics": ("fields", "Aesthetics", "beauty, the sublime, art, taste, major theories (Plato, Kant, Hume), debates"),
 "fld-ethics-overview": ("fields", "Ethics (Overview)", "normative, meta and applied ethics; virtue, duty, consequences; pointer to the Ethics module; why it sits beside philosophy"),
}
