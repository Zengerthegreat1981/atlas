---
slug: "con-chomsky-hierarchy-formal-language-theory"
id: "CON-11041"
type: "مفهوم"
part: "linguistics"
level: "متقدم"
linguistic_level: "syntax"
cultural_origin: "anglo-european"
title: "هرميةُ تشومسكي ونظريةُ اللغات الصورية (Chomsky Hierarchy)"
en: "Chomsky Hierarchy & Formal Language Theory"
crumb: "علم اللغة ← اللغةُ والحاسوبُ والقياس ← هرميةُ تشومسكي"
edges:
- rel: "belongs_to", target: "sch-computational-linguistics-nlp", target_type: "مدرسة"
related:
- id: "sch-computational-linguistics-nlp", title: "اللسانياتُ الحاسوبيةُ ومعالجةُ اللغة الطبيعية (Computational Linguistics & NLP)", type: "مدرسة"
- id: "sch-generative-grammar", title: "النحوُ التوليديُّ التحويليّ (Generative-Transformational Grammar)", type: "مدرسة"
gaps: []
---

# هرميةُ تشومسكي ونظريةُ اللغات الصورية

تصنيفٌ رياضيٌّ صاغه نعوم تشومسكي عام 1956 يرتِّب اللغاتِ الصورية (Formal Languages، أنظمةَ رموزٍ مولَّدة بقواعدَ رياضيةٍ محدَّدة) في أربع فئاتٍ متداخلة وفق التعقيد الحسابي اللازم للتعرّف عليها، وأثّر بعمقٍ في كلٍّ من نظرية الحوسبة واللسانيات النظرية معاً.

## الفئاتُ الأربع

من الأبسط إلى الأعقد: **اللغاتُ المنتظمة** (Regular، تتعرّف عليها آلاتٌ منتهيةُ الحالات، Finite-State Automata)، **اللغاتُ الخالية من السياق** (Context-Free، تتعرّف عليها آلاتُ الدفع المكدَّسة)، **اللغاتُ الحساسة للسياق** (Context-Sensitive)، و**اللغاتُ غيرُ المقيَّدة تكرارياً** (Recursively Enumerable، تتطلّب آلةَ تورنغ الكاملة). كلُّ فئةٍ أعقد تحتوي كلَّ اللغات الأبسط منها.

## أين تقع اللغة البشرية؟

جادل تشومسكي في *Syntactic Structures* (1957) بأن اللغةَ الطبيعية البشرية تتجاوز قدرةَ اللغات المنتظمة (إذ تحتوي على تراكيبَ متداخلة تعتمد على بنيةٍ شجرية، كالجمل المضمَّنة داخل جملٍ أخرى بتكرارٍ لا نهائيّ نظرياً)، وتتطلّب على الأقلّ قواعدَ خاليةً من السياق (Context-Free Grammars) لوصفها بدقّة — حجّةٌ صورية دعمت لاحقاً أطروحاتِ فقر المحفِّز والنحو الكلّي.

## الأثر

قدّمت هذه الهرميةُ أساساً رياضياً صارماً ربط اللسانياتِ النظرية بعلوم الحاسوب مباشرة، وصارت أداةً معياريةً في تصميم لغات البرمجة والمحلِّلات النحوية الآلية، وأثارت نقاشاتٍ لاحقةً حول الفئة الدقيقة التي تنتمي إليها اللغةُ الطبيعية (إذ اقترح بعضُ الباحثين لاحقاً أنها تتطلّب فئةً وسيطة بين الخالية من السياق والحساسة للسياق).

## المصادر

- Chomsky, Noam (1956). "Three Models for the Description of Language." *IRE Transactions on Information Theory* 2(3).
- Chomsky, Noam (1957). *Syntactic Structures*. Mouton.
