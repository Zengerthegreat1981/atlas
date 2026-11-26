---
slug: con-variable
id: SOC-14253
type: مفهوم
part: sociology
level: متوسط
title: "Variable: Measurement and Variation in Social Research"
en: "Variable"
crumb: "Sociology ← Variable"
dates: ''
active_start: 1900
active_end: مستمر
edges: []
related: []
gaps: []
sociological_tradition: other
sociological_paradigm: micro-macro
---
# Variable: Measurement and Variation in Social Research

A **variable** is any characteristic that can take more than one value and can therefore vary across the cases a researcher studies — people, organisations, countries, or moments in time. Age, income, years of schooling, religious affiliation, and level of trust in government are all variables; a constant, by contrast, is a characteristic that does not vary within the study, such as the nationality of a sample drawn entirely from one country. The concept of the variable is the basic building block of quantitative social research: it is what allows sociologists to describe patterns, compare groups, and test explanations.

## Definition and Types

Variables are classified by their role in an explanation. The **independent variable** is the factor presumed to cause or influence an outcome; the **dependent variable** is the outcome being explained. In a study of whether education raises earnings, education is the independent variable and earnings the dependent one. An **intervening variable** stands between the two — education may raise earnings partly by giving access to professional networks — while a **control variable** is held constant, statistically or by design, so that its influence does not confuse the result. A **confounding variable** is an uncontrolled third factor, such as family wealth, that is related to both education and earnings and can create a misleading association.

Variables are also classified by their level of measurement, a scheme set out by Stanley Smith Stevens in "On the Theory of Scales of Measurement" (1946). **Nominal** variables place cases in categories without order, such as religion or nationality. **Ordinal** variables rank cases, such as levels of agreement from "strongly disagree" to "strongly agree." **Interval** variables have equal distances between values but no true zero, such as temperature in Celsius or calendar years. **Ratio** variables add a meaningful zero, such as income or age. The level of measurement determines which statistical techniques are appropriate: one may compute a mean income but not a mean religion.

## Development: Operationalisation

The decisive step in using variables is **operationalisation**: turning an abstract concept into a concrete, measurable procedure. The work of Paul Lazarsfeld, represented in *The Language of Social Research* (1955, edited with Morris Rosenberg), set out how abstract concepts are translated into indicators that are then combined into an index. A concept such as "alienation", for example, might be measured through questionnaire items about powerlessness, meaninglessness, and isolation. Operationalisation makes research transparent and replicable, because other researchers can inspect the indicators and judge whether they capture the concept.

But it also creates a permanent tension. A concept is always richer than its indicators: "social class" reduced to income alone misses wealth, status, and power, while "religiosity" reduced to church attendance misses belief and private practice. Hubert Blalock, in *Causal Inferences in Nonexperimental Research* (1964), drew attention to the gap between theoretical concepts and their measures, on whose quality the soundness of any finding depends.

## Causality and the Variable

The language of variables carries an implicit model of causality: change the independent variable and the dependent variable should change. Donald Campbell and Julian Stanley's *Experimental and Quasi-Experimental Designs for Research* (1963; book edition 1966) set out the conditions for such claims — association, temporal order, and the elimination of alternative explanations. In practice, most sociological data are observational rather than experimental: researchers cannot assign people to social classes or religions. They therefore rely on statistical control, comparing people who differ in one variable while resembling each other in others, and on careful reasoning about which direction causation runs. Does unemployment cause poor health, or does poor health cause unemployment? The variable framework forces the question into the open, even when it cannot settle it.

## Examples

Consider a study of voting. The dependent variable might be turnout in an election; independent variables could include age, education, income, and political interest. Cross-tabulation might show that turnout rises with education — but the relationship could be confounded by income, since educated people tend to earn more. Controlling for income tests whether education matters on its own. Or consider a study of health: the variable "body mass index" operationalises the concept of obesity, while "self-rated health" captures a person's own assessment. The two variables correlate but are not identical, and the choice between them shapes the conclusions.

## Variables in Computational and Big-Data Research

Computational social science works with records such as search logs, social media posts, transaction data, and digitised archives. Here variables are usually constructed after the fact, not designed in advance. A researcher may turn millions of documents into counts of words, assign each a topic or tone with a statistical model, or derive network measures such as the number of a person's connections. Justin Grimmer and Brandon Stewart (2013) stressed that automated text methods rest on simplified models of language and that their output must be validated for each task, commonly by comparison with careful human reading. Matthew Salganik, in *Bit by Bit* (2018), noted that large digital sources are often incomplete, unrepresentative, and affected by changes in the systems that generate them: a rise in some recorded behaviour may reflect a redesigned interface instead of a change in people. Machine-learning studies may also use thousands of predictors, or features, chosen for predictive performance. Such variables can forecast an outcome well without identifying its causes, so the distinctions between independent, dependent, and confounding variables still matter whenever the aim is explanation. Access restrictions and privacy obligations further limit which variables others can inspect or reproduce.

## Measurement Invariance across Cultures and Languages

Comparing groups on a variable assumes that the measure works in the same way in each. Measurement invariance, or equivalence, is the property that people with the same standing on an underlying trait have the same expected responses whatever group they belong to. It can fail because translation shifts the meaning of an item, because an example is familiar in one setting only, or because groups use response scales differently, for instance in their tendency to agree or to choose extreme options. A common test uses multi-group confirmatory factor analysis in successive steps. Configural invariance requires the same pattern of items and factors; metric invariance requires equal factor loadings, which supports comparing relationships among variables; scalar invariance also requires equal intercepts, which supports comparing latent means. William Meredith (1993) gave an influential statistical treatment, and Eldad Davidov and colleagues (2014) reviewed its use in cross-national research, where strict equality often fails across many countries. Partial or approximate invariance offers alternatives, but statistics cannot replace careful translation, pretesting, and qualitative study of how respondents understand questions. A difference in scores may otherwise be an artefact of the instrument.

## Critique and Contemporary Relevance

Qualitative researchers have long criticised the variable framework for fragmenting social life. A person's experience of poverty is not a set of separate variables — income, housing, health — but a lived whole, and reducing it to variables can strip away meaning and context. Feminist and critical scholars add that the choice of which variables to measure reflects power: what is counted is what counts, and the experiences of marginalised groups are often the ones left unmeasured.

Despite these criticisms, the variable remains indispensable. Survey research, official statistics, and the new computational social science all depend on it. Contemporary debates concern measurement across cultures — whether a variable such as "trust" means the same thing in different languages — and the use of variables derived from digital traces, where the researcher did not design the measurement at all. The concept of the variable is, in the end, the concept of making social life countable without forgetting what counting leaves out.

## Sources

- Blalock, Hubert M. *Causal Inferences in Nonexperimental Research*. University of North Carolina Press, 1964.
- Campbell, Donald T., and Julian C. Stanley. *Experimental and Quasi-Experimental Designs for Research*. Rand McNally, 1966 (first published 1963).
- Lazarsfeld, Paul F., and Morris Rosenberg, eds. *The Language of Social Research: A Reader in the Methodology of Social Research*. Free Press, 1955.
- Stevens, Stanley Smith. "On the Theory of Scales of Measurement." *Science* 103, no. 2684 (1946): 677–680.
- Davidov, Eldad, Bart Meuleman, Jan Cieciuch, Peter Schmidt, and Jaak Billiet. "Measurement Equivalence in Cross-National Research." *Annual Review of Sociology* 40 (2014).
- Grimmer, Justin, and Brandon M. Stewart. "Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts." *Political Analysis* 21, no. 3 (2013).
- Meredith, William. "Measurement Invariance, Factor Analysis and Factorial Invariance." *Psychometrika* 58, no. 4 (1993).
- Salganik, Matthew J. *Bit by Bit: Social Research in the Digital Age*. Princeton University Press, 2018.
