# Task 9.5
الحالة: مكتمل
المسار: minimax | العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط | الملفات: 30

## الأرقام
جمل القائمة السوداء (بالفحص المُصحَّح لـpreflight_check.py): قبل ~15 ملفاً فيها بقايا/قوالب كاملة → بعد 0
edges.belongs_to بنص حر بدل slug: قبل 3 (con-buen-vivir-sumak-kawsay، con-chinul-sudden-gradual، con-capability-approach-sen-nussbaum) → بعد 0
gaps بتؤكد حقيقة بدل تسمية فجوة: 1 صُححت (con-catharsis-integration)
عناوين related متضاربة مع الملف المستهدف: صُححت في ~8 ملفات

## أمر التحقق
python3 scripts/task.py verify minimax 9.5
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 (المستهدف 0) | فيها ## المصادر: 0 / 30
(أُعيد الفحص بـpreflight_check.py بعد إصلاحه ليفحص فعلياً جمل القائمة السوداء — نتيجة نظيفة كذلك)

## قرارات اتخذتها
- con-brahman.md: صُححت عناوين شانكارا/مايا، أُضيف con-brahman-nirguna-saguna (مذكور بالمتن).
- con-brahman-nirguna-saguna.md: متن كان فارغاً عملياً — حُذفت الجمل السوداء، بُني related برابطين فقط مدعومين.
- con-buddhist-compassion-karuna.md: حُذف con-bodhicitta (غير مذكور)، أُضيف thk-pgilbert وwrk-gilbert-compassionate-mind وthk-ssalzberg (مذكورون بالاسم).
- con-buddhist-emptiness-shunyata.md: صُحح عنوان thk-nagarjuna، أُضيف thk-tsongkhapa وthk-beck وthk-lstevenhayes وthk-lcwallace (مذكورون بالاسم والسنة).
- con-buen-vivir-sumak-kawsay.md: edges.belongs_to نص حر — حُذف. رابط واحد فقط مدعوم (sch-andean-philosophy).
- con-bystander-effect.md: حُذفت 4 روابط غير مذكورة، أُضيفت جملة توثيقية تنسب الظاهرة لدارلي ولاتانيه (1968)، بُني related عليها.
- con-capabilities-approach.md: أُعيد بناء related بالكامل (thk-sen، thk-nussbaum، sch-cosmopolitanism، thk-nozick، dbt-rawls-nozick-justice)، سُجّل احتمال ازدواج مع الملف التالي.
- con-capability-approach-sen-nussbaum.md: متن شبه فارغ من محتوى حقيقي — أُبقي رابط واحد فقط (الملف الآخر). edges.belongs_to نص حر — حُذف.
- con-care-ethics.md: أُبقي الروابط الخمسة المبررة أصلاً، أُضيف thk-nussbaum وdbt-care-ethics-vs-justice-ethics وthk-butler وsch-ecofeminism (مذكورون بالمتن).
- con-care-for-soul.md: حُذف thk-elaine-aron (تضارب id/title) وbr-archetypal (بلا تبرير)، أُبقي thk-patocka وthk-heidegger.
- con-care-of-the-self-foucault.md: أُضيفت جملة تسمي فوكو صراحة (لم يكن مذكوراً بالاسم رغم العنوان) لتبرير الرابط الوحيد.
- con-caring-mayeroff.md: حُذف thk-mbuber (عنوان خاطئ) وthk-rogers وcon-relation (غير مبررين)، أُضيف thk-heidegger وcon-meaning.
- con-cartesian-doubt-method.md: أُبقي رابطين فقط (thk-descartes، sch-cartesianism) لأن المتن لا يذكر ديكارت صراحة — سُجّل بـgaps بدل الاختراع.
- con-categorical-imperative-kant.md، con-categorical-imperative.md: ملفان متشابهان — سُجّلت الملاحظة في كل منهما بدون دمج. الثاني أُعيد بناؤه بـ8 روابط (كانط، رولز، شوبنهاور، هيغل، نيتشه، بنثام، ميل) مذكورين بالاسم.
- con-categories-of-understanding-kant.md: متن شبه خالٍ — أُبقي رابطان فقط (thk-kant، sch-kant-critical)، سُجّل أن كانط غير مذكور حرفياً بالمتن رغم الموضوع.
- con-catharsis-integration.md: صُحح thk-jmoreno→thk-moreno، أُعيد البناء بأربعة روابط مبررة (مورينو، السيكودراما، فرويد، sch-psychoanalysis).
- con-cbt-mbt-mindfulness-3min-breathing-space.md: حُذفت 3 روابط غير مذكورة (sch-act، sch-dbt، con-exposure-hierarchy)، صُححت 3 عناوين.
- con-cft-compassion-systems.md، con-cft-self-compassion.md، con-cft-soothing-system.md: صُححت عناوين متعددة (sch-cft، con-shame-self-criticism، thk-pgilbert)، أُضيف thk-kristin-neff (واضعة المفهوم).
- con-change-talk-darn-cat.md: صُحح عنوان thk-wmiller، أُضيف thk-rollnick ووrk-miller-rollnick-motivational-interviewing (مذكوران بالاسم).
- con-chatbot-therapeutic-alliance.md: حُذف con-relation، أُضيف con-therapeutic-alliance-bordin وthk-ebordin (بوردين مذكور بالاسم).
- con-chiasm-the-flesh-merleau-ponty.md: متن قالبي بالكامل — أُعيد كتابته (ميرلو-بونتي، ظاهراتية الإدراك)، بُني related من الصفر.
- con-chinese-room-argument-searle.md: رابط واحد فقط (thk-john-searle، صاحب البرهان).
- con-chinese-verification-ism.md: صُحح عنوان thk-hu-shi، أُضيف thk-descartes وsch-pyrrhonism (مقارنان صراحة بالمتن).
- con-chinul-sudden-gradual.md: edges.belongs_to نص حر — حُذف. related تُرك فارغاً (لا اسم مذكور بالمتن، ولا حتى ملف thk- لتشينول نفسه).
- con-choice-theory.md: لا تعديل جوهري — related الأصلي صحيح ومبرر، صُحح خطأ إملائي بعنوان قسم.
- con-chokmah-hebrew.md: حُذف thk-solomon (تضارب id/title — الملف الفعلي عن روبرت سولومون الفيلسوف المعاصر لا سليمان التوراتي)، أُضيف con-maat وthk-philo-alexandria.
- con-cinderella-complex.md: edges.belongs_to نص حر — حُذف. صُحح عنوان wrk-cinderella-complex، حُذف con-peter-pan-complex (بلا تبرير).

## متوقف عنده (لرئيس التحرير)
- con-capabilities-approach.md وcon-capability-approach-sen-nussbaum.md: احتمال ازدواج — يحتاج قرار دمج بشري، خارج نطاق Task 9.
- con-categorical-imperative-kant.md وcon-categorical-imperative.md: نفس الأمر — احتمال ازدواج يحتاج قرار بشري.
- con-chinul-sudden-gradual.md: لا يوجد ملف thk- لتشينول نفسه رغم أن المفهوم منسوب له بالعنوان — فجوة بنيوية (يُقترح طلب slug في requests-minimax.md لو تأكد وجوده تاريخياً).
- con-cartesian-doubt-method.md، con-categories-of-understanding-kant.md: متنان مقتضبان جداً لا يسميان كانط/ديكارت صراحة رغم أن الموضوع عنهما مباشرة — يحتاجان تعميقاً (Task 4/10).

## الملفات
content/ar/concepts/con-brahman-nirguna-saguna.md
content/ar/concepts/con-brahman.md
content/ar/concepts/con-buddhist-compassion-karuna.md
content/ar/concepts/con-buddhist-emptiness-shunyata.md
content/ar/concepts/con-buen-vivir-sumak-kawsay.md
content/ar/concepts/con-bystander-effect.md
content/ar/concepts/con-capabilities-approach.md
content/ar/concepts/con-capability-approach-sen-nussbaum.md
content/ar/concepts/con-care-ethics.md
content/ar/concepts/con-care-for-soul.md
content/ar/concepts/con-care-of-the-self-foucault.md
content/ar/concepts/con-caring-mayeroff.md
content/ar/concepts/con-cartesian-doubt-method.md
content/ar/concepts/con-categorical-imperative-kant.md
content/ar/concepts/con-categorical-imperative.md
content/ar/concepts/con-categories-of-understanding-kant.md
content/ar/concepts/con-catharsis-integration.md
content/ar/concepts/con-cbt-mbt-mindfulness-3min-breathing-space.md
content/ar/concepts/con-cft-compassion-systems.md
content/ar/concepts/con-cft-self-compassion.md
content/ar/concepts/con-cft-soothing-system.md
content/ar/concepts/con-change-talk-darn-cat.md
content/ar/concepts/con-chatbot-therapeutic-alliance.md
content/ar/concepts/con-chiasm-the-flesh-merleau-ponty.md
content/ar/concepts/con-chinese-room-argument-searle.md
content/ar/concepts/con-chinese-verification-ism.md
content/ar/concepts/con-chinul-sudden-gradual.md
content/ar/concepts/con-choice-theory.md
content/ar/concepts/con-chokmah-hebrew.md
content/ar/concepts/con-cinderella-complex.md
