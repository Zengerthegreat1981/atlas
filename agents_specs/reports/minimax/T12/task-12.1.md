# Task 12.1 — أول دفعة في Task 12 (dialogues/questions/terms/axioms)
الحالة: مكتمل
العملية: axioms/ (كل ملفات axi-/axm- في هذه الدفعة) — تعميق + تسمية صاحب المبدأ الفعلي بالاسم والنص والسنة + مصادر (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 12.1): صفر مخالفات آلية (30/30 ملف، 30/30 فيها ## المصادر)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء + عبارة "تمثل هذه البديهية حجر زاوية" الإضافية): صفر تطابق

## حالة الملفات قبل البدء
معظم ملفات axi- (21 ملف) كانت **نسخاً متطابقة تقريباً من قالب واحد موحَّد** يحتوي جمل القائمة السوداء حرفياً ("لا يوجد اقتباس مباشر موثوق متاح"، "تمثل هذه البديهية حجر زاوية...") بدون تسمية صاحب المبدأ الفعلي، بدون سنة، بدون مصادر. ملفات axm- (9 ملفات) كانت أفضل حالاً نسبياً (بعضها كان موثقاً بالفعل) لكن فيها أخطاء نسبة ومصادر ناقصة.

## ⚠️ أخطاء هوية/نسبة حقيقية اكتُشفت وصُححت
- axi-existence-precedes-essence-axiom: `thk-kuhn` كان سيُستخدم خطأً لتوماس كون (فيلسوف العلم) بينما هو فعلياً **رولاند كون** (طبيب نفسي سويسري) — تم تفادي الربط الخاطئ واستخدام `thk-thomas-kuhn` الصحيح.
- axm-actualizing-tendency: صفة "Actualization of the Organism" كانت منسوبة لاسم "أنجل" غير موجود — المصدر الحقيقي هو **كورت غولدشتاين** (*The Organism*, 1939)، الذي صاغ المصطلح قبل روجرز وماسلو فعلياً.
- axm-cognitive-unconscious: `target: "جون كيلستروم"` كان نصاً حراً بدل slug — صُحح إلى `thk-jkihnstrom` مع تصحيح التهجئة المتضاربة في المتن.
- axm-cognitive-consistency: `formulated_by` كانت تشاور اسماً نصياً "ليون فستنجر" بدل الـslug `thk-lfestinger`.

## أصحاب المبادئ الموثَّقون في هذه الدفعة (عيّنة)
توما الأكويني (analogia entis، natural law)، كانط (الأمر القطعي، 1785)، ديكارت (الكوجيتو، 1637/1644)، إبكتيتوس (ثنائية التحكم)، رولز (مبدأ الاختلاف/حجاب الجهل، 1971)، أرسطو (الوسط المستبعد، مبدأ الهوية، عدم التناقض)، سارتر (الوجود يسبق الماهية، 1943/1945)، بوبر (القابلية للتفنيد، 1934)، بنثام/ميل (أكبر سعادة)، ميل (مبدأ الضرر، 1859)، بروتاغوراس (هومو مينسورا)، لايبنتز (مبدأ السبب الكافي، 1686)، سبينوزا (الجوهر الواحد، 1677)، لوك (تابولا راسا، 1690)، سكوتس (univocity of being)، شليك/حلقة فيينا (معيار التحقق، 1936)، نيتشه (إرادة القوة)، روجرز/غولدشتاين (الميل لتحقيق الذات)، كوزميدس وتوبي (التكيف، 1992)، بافلوف (الإشراط الكلاسيكي)، فستنجر (الاتساق المعرفي، 1957)، بيك/إليس (الوساطة المعرفية)، بارتليت (المخطط المعرفي، 1932)، كيلستروم (اللاوعي المعرفي، 1987)، ميشيل (تأجيل الإشباع، 1970/1989).

صفر slugs مخترعة. صفر مصادر ملفَّقة مكتشفة في هذه الدفعة (نقيض واضح عن نمط critiques/debates في Task 11).

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل — دفعة نظيفة نسبياً، معظم المشاكل كانت قالبية (نص موحَّد متكرر) وليست تلفيقاً.

## الملفات
axi-analogia-entis-axiom, axi-categorical-imperative-universal, axi-cogito-ergo-sum-rule, axi-dichotomy-of-control-axiom, axi-difference-principle-rule, axi-excluded-middle, axi-existence-precedes-essence-axiom, axi-falsificationism-demarcation, axi-greatest-happiness-principle, axi-harm-principle-rule, axi-homo-mensura-axiom, axi-natural-law-first-precept, axi-primum-nocere, axi-principle-of-identity, axi-principle-of-non-contradiction, axi-principle-of-sufficient-reason, axi-substance-monism-axiom, axi-tabula-rasa-rule, axi-univocity-of-being-axiom, axi-veil-of-ignorance-rule, axi-verification-criterion, axi-will-to-power-axiom, axm-actualizing-tendency, axm-adaptation, axm-classical-conditioning, axm-cognitive-consistency, axm-cognitive-mediation-principle, axm-cognitive-schema, axm-cognitive-unconscious, axm-delayed-gratification
