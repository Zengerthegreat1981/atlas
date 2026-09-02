# Task 11.8
الحالة: مكتمل
العملية: debates/ — تسمية الطرفين الحقيقيين بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.8): صفر مخالفات آلية (30/30 ملف)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء الـ18 على الملفات الـ30): صفر تطابق

## ✅ عنقود nature-nurture الكبير (6 ملفات) — استقلال مؤكَّد، تنظيف روابط عشوائية نمطي
الستة ملفات (dbt-nature-nurture، -behavioral-genetics-vs-constructionism، -cognitive-modules-vs-domain-general، -gene-environment-interaction، -intelligence-personality، -mencius-xunzi) فُحصت بالكامل وتأكدت زاوية مستقلة فعلياً لكل واحد (عام/تمهيدي، وراثة سلوكية مقابل بنائية، وحدات معرفية فطرية، آلية GxE جينية-بيئية، ذكاء/شخصية، الفلسفة الصينية الكلاسيكية) — لا دمج. اكتُشف نمط متكرر: روابط `related` عشوائية منسوخة عبر الملفات الثلاثة الأولى (بولبي/بياجيه/فيغوتسكي/إريكسون/دوي/فونت/لوك/سبنسر بلا أي تبرير نصي) — حُذفت جميعاً.

## ⚠️ أخطاء هوية حقيقية إضافية
- dbt-nature-nurture-behavioral-genetics-vs-constructionism: "فرانك فراي (Frank Galton)" خطأ فادح — صُحح إلى **فرانسيس غالتون**. كما تجنَّب subagent ربطاً خاطئاً محتملاً: `thk-sbouchard` الموجود بالأطلس هو **ستيفان بوشار** (كندي معاصر) وليس **توماس بوشار** (صاحب دراسة توائم مينيسوتا 1990) — لم يُربط.
- dbt-nature-nurture: عنوان `thk-fskinner` كان معكوساً — صُحح.
- dbt-nishida-vs-tanabe: `gaps` كانت تدّعي زوراً أن ملف تانابه هاجيمي "غير موجود بعد" رغم وجوده فعلياً — أُصلح والرابط أُضيف.

## ⚠️ مصادر ملفَّقة إضافية
- dbt-pharmacogenomics-vs-clinical-judgment-antidepressant: 6 أسماء غير قابلة للتحقق بالكامل ("هيوغو تشابلييه"، "مات شيدوف"، "كيران براتشر"، "مالكولم وود"، "أليكس بوم"، وتعبير "جينوميك فارماكولوجي" المُختلَق) — حُذفت واستُبدلت بأطراف حقيقية موثَّقة (ديفيد مرازيك/فريق مايو كلينيك، تجربة GUIDED لغريدن 2019، مراجعة زايير-كارلين النقدية 2018).

## ✅ حل عناقيد تداخل بالفصل التحريري
- psychodynamic-evidence (جودة الأدلة الداخلية، شيدلر 2010 ضد ثومبز/ليلينفيلد/ماكاي 2011) مقابل psychodynamic-vs-cbt-effectiveness (مقارنة مباشرة بالمعالجة المعرفية-السلوكية) — زاويتان مستقلتان فعلياً، لا تداخل.
- psychotherapy-vs-medication (خوارزمية اختيار العلاج، STAR*D) مقابل psychotherapy-vs-pharmacotherapy-depression (فاعلية عامة والدواء الوهمي، كيرش 2008) — زاويتان مستقلتان، إحالة صريحة مضافة بينهما.

## قرارات محتوى بارزة
- dbt-philosophical-zombies-chalmers: كان يحتوي جملتين من القائمة السوداء — أُعيد حول تشالمرز (1996) ضد دينيت (1991/1995).
- dbt-moral-realism-vs-moral-relativism: كان فيه 4 جمل قائمة سوداء حرفية — أُعيد حول هارمان ضد طومسون (مناظرة منشورة فعلياً 1996).
- dbt-process-experiential-vs-cbt: كان بصيغة تشكيل/ترجمة مكسورة غير قابلة للنشر — أُعيد كتابته بالكامل.
- dbt-prolonged-grief-disorder-legitimacy: أُعيد حول پريغرسون (World Psychiatry 2021) ضد كاتشياتوري وفرانسيس (The Lancet Psychiatry 2022).

صفر slugs مخترعة. طلبات slug جديدة عديدة مسجَّلة (هارمان، طومسون، ماكي، تشومسكي، بينكر، كوزميدس، توبي، وغيرهم).

## متوقف عنده (لرئيس التحرير)
- لا تداخلات جديدة غير محسومة — كل عنقود فُحص إما استقل فعلياً أو انفصل تحريرياً.

## الملفات
dbt-moral-foundations-pluralism, dbt-moral-realism-vs-moral-relativism, dbt-nature-nurture-behavioral-genetics-vs-constructionism, dbt-nature-nurture-cognitive-modules-vs-domain-general, dbt-nature-nurture-gene-environment-interaction, dbt-nature-nurture, dbt-nature-vs-nurture-intelligence-personality, dbt-nature-vs-nurture-mencius-xunzi, dbt-neuroethics-cognitive-enhancement, dbt-new-materialism-vs-linguistic-turn, dbt-nishida-vs-tanabe, dbt-object-oriented-ontology-vs-relationality, dbt-panpsychism-vs-physicalism, dbt-pharmacogenomics-vs-clinical-judgment-antidepressant, dbt-philosophical-zombies-chalmers, dbt-positivity-mandate-critique, dbt-posthumanism-vs-transhumanism, dbt-presentism-vs-eternalism-time, dbt-problem-of-universals, dbt-process-experiential-vs-cbt, dbt-projective-tests-validity, dbt-prolonged-grief-disorder-legitimacy, dbt-psychodynamic-evidence, dbt-psychodynamic-vs-cbt-effectiveness, dbt-psychology-replication-crisis, dbt-psychotherapy-ingredients-active, dbt-psychotherapy-vs-medication, dbt-psychotherapy-vs-pharmacotherapy-depression, dbt-qadar-free-will-in-kalam, dbt-qualitative-vs-quantitative-psychology
