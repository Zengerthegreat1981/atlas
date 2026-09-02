# Task 12.3
الحالة: مكتمل
المسار: spark | العملية: contexts/experiences/metaphors: تصنيف الصوت السردي + التعميق | الملفات: 30

## الأرقام
جمل القائمة السوداء: قبل غير محسوب دفعة بدفعة (فحص لاحق) → بعد 0
سقّالة gaps قالبية ظاهرة: → بعد 0
ملفات فيها `## المصادر`: 0/30 (تقريباً، عدا استثناءات قليلة) → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 12.3
→
```
=== تحقق Task 12.3 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 30 / 30
```
(preflight_check.py على الـ30 ملف: ✅ صفر مخالفات آلية، بعد جولتين تصحيح لعناوين روابط `related` غير مطابقة لعناوين الملفات الحقيقية.)

## قرارات اتخذتها
- **exp-augustine-garden-milan-tolle**: تحويل كامل لضمير المتكلم (الاعترافات، الكتاب الثامن)؛ اقتباسان مباشران من ترجمة تشادويك 1991 (رومية 13: 13-14، صراع الإرادتين)؛ تواريخ 386م/397-400م/387م؛ ربط بويليام جيمس (أصناف الخبرة الدينية، 1902)؛ تصحيح `edges` من `sch-christian-philosophy` (غير موجود) إلى `sch-christian-mysticism-medieval` (معتمد).
- **exp-beauvoir-discovery-of-otherness**: ضمير المتكلم استناداً لمذكرات بوفوار "قوة الأشياء" (1963)؛ تفاصيل نشر 1949 (غاليمار)، ترجمة بارشلي 1953 ونقدها، والترجمة الكاملة 2009.
- **exp-awe-and-wonder**: أُبقي وصفياً (ظاهرة عامة) وعُمّق بـKeltner & Haidt 2003، Piff et al. 2015، Burke 1757.
- **exp-bessel-van-der-kolk-vietnam-vets**: ضمير المتكلم؛ حالة "توم"، دراسة PET 1994 (Harvard Review of Psychiatry)، مركز الصدمة ببروكلاين؛ تصحيح عنوان رابط `que-embodied-trauma-body-memory`.
- **exp-boethius-prison-consolation**: ضمير المتكلم؛ تأريخ دقيق (523-524/525م، بافيا، بلاط ثيودوريك)؛ بنية Prosimetrum؛ Rota Fortunae وأثرها على ألفريد العظيم وتشوسر؛ تصحيح عنوان رابط `thk-boethius`.
- **exp-bruce-perry-waco-siege-children**: ضمير المتكلم؛ حصار واكو أبريل 1993، 21 طفلاً، شهادة الكونغرس 1995، ChildTrauma Academy 1996، تسلسل NMT؛ تصحيح عنوان رابط `thk-bperry`.
- **exp-buddha-four-sights-renunciation**: ضمير المتكلم (سيدهارتا غوتاما) استناداً لـBuddhacharita وNidanakatha؛ أسماء دقيقة (كابيلافاستو، ياشودارا، راهولا، تشانا).
- **exp-camus-algerian-poverty-sun**: ضمير المتكلم؛ تواريخ سيرة دقيقة (1913 مونادوفي، وفاة الأب، لوي جيرمان، أعماله 1937/1942/1951)؛ استُبدلت أسماء slugs مقترحة غير موجودة (`thk-albert-camus`) بالموجود فعلاً (`thk-camus`).
- **exp-carl-sagan-pale-blue-dot-awe**: ضمير المتكلم؛ فوياجر 1، 14 فبراير 1990، كتاب 1994؛ تصحيح عنوان رابط `que-sacred-in-secular-world`.
- **exp-childhood-amnesia**: أُبقي وصفياً وعُمّق بفرويد (1899/1905)، Nelson & Fivush 2004، Loftus & Pickrell 1995، Qi Wang 2001/2006؛ إضافة `thk-elizabeth-loftus` (موجود فعلاً).
- **exp-chogyam-trungpa-crazy-wisdom**: ضمير المتكلم استناداً لمذكراته Born in Tibet (1966)؛ تواريخ 1959/1960/1974/1987.
- **exp-clara-barton-civil-war-nursing**: ضمير المتكلم؛ أنتيتام 1862، لقاء هنري دونان 1869، تأسيس الصليب الأحمر الأمريكي 1881.
- **exp-conversion-experience**: أُبقي وصفياً وعُمّق باستبيانات إدوين ستاربَك (1899)، نهضات جوناثان إدواردز (1734-35)، تحوّل بِل ويلسون (1934).
- **exp-david-duran-indigenous-soul-wound**: ضمير المتكلم؛ عناوين كتبه (1995، 1990، 2006/2019)؛ ربط بأبحاث ماريا يلو هورس براف هارت (1998)؛ تصحيح عنوان رابط `que-intergenerational-healing-rituals`.
- **exp-deja-vu**: أُبقي وصفياً وعُمّق بإميل بويراك (1876)، آلان براون (2004)، وايلدر بنفيلد (1963)، فابريس بارتولوميه (2012)، كريس مولن (2005)؛ تصحيح تنسيق YAML في `gaps` كان معطوباً من الأصل.
- **exp-depersonalization** و**exp-derealization-depersonalization**: **تكرار محتمل محسوم بدون حذف** — نفس المتلازمة DSM-5 تحت عنوانين. مُيِّز الأول ليغطي حصراً تبدد الشخصية (Sierra & David)، والثاني ليغطي حصراً تبدد الواقع (Schilder 1914، Jaspers 1913) + التوازي الفلسفي (ديكارت، سارتر)؛ كل ملف يربط بالآخر مع توضيح الفرق في المتن، وكلاهما يربط بـ`dis-depersonalization-derealization`.
- **exp-derrida-algerian-jewish-exclusion**: ضمير المتكلم؛ إلغاء مرسوم كريميو 1940، الطرد أكتوبر 1942.
- **exp-descartes-stove-heated-room**: أُبقي slug/title/edges كما هي (رابط وارد من ctx-counter-reformation-jesuit-education)؛ عُمّق بضمير المتكلم؛ تاريخ 10 نوفمبر 1619، نويبورغ آن دير دوناو.
- **exp-dostoevsky-mock-execution-siberia**: ضمير المتكلم؛ ساحة سيمينوفسكي، 22 ديسمبر 1849/3 يناير 1850، جماعة بتراشيفسكي.
- **exp-dream-freud**: إعادة تأطير كسرد فرويد الذاتي لتحليله الذاتي (حلم إيرما، يوليو 1895)؛ حذف جملة القائمة السوداء؛ تصحيح عناوين روابط `thk-jung` و`con-unconscious`.
- **exp-eckhart-tolle-night-transformation**: ضمير المتكلم؛ 1948 لونن، انهيار لندن 1977، The Power of Now 1997.
- **exp-edith-eger-ballerina-auschwitz**: ضمير المتكلم؛ 1927 كوشيتسه، ترحيل مايو 1944؛ تصحيح عنوان رابط `wrk-eger-the-choice`.
- **exp-elyn-saks-schizophrenia-center**: ضمير المتكلم؛ 1955، أوكسفورد، جامعة USC، منحة ماك آرثر 2009.
- **exp-ernest-shackleton-endurance-survival**: ضمير المتكلم؛ 5 ديسمبر 1914 الإبحار، 21 نوفمبر 1915 الغرق، 30 أغسطس 1916 الإنقاذ.
- **exp-existential-boredom**: أُبقي وصفياً وعُمّق بهايدغر 1927، سفيندسن 2005، كامو 1942، يالوم 1980؛ حُذف رابطان لـslugs غير موجودين (`thk-svendsen`, `con-being`) واستُبدلا بـ`thk-camus` الموجود فعلاً؛ أُضيف قسم `## المصادر` (كان ناقصاً بعد الدفعة الأولى، أُضيف لاحقاً أثناء التحقق).
- **exp-fanon-martinique-french-racism**: ضمير المتكلم؛ 1925 فور-دو-فرانس، الخدمة 1944، صدور Peau noire 1952.
- **exp-flashback-ptsd**: أُبقي وصفياً؛ عُمّق بـDSM-III 1980 (شاتان، ليفتون)، DSM-5 2013، Ehlers & Clark 2000.
- **exp-flow-state-csikszentmihalyi**: أُبقي وصفياً؛ Beyond Boredom and Anxiety 1975، Flow 1990، ورقة 2000 مع سليغمان.
- **exp-foucault-tunisia-revolt**: ضمير المتكلم؛ تونس 1966-1968، انتفاضة مارس 1968، تأسيس GIP فبراير 1971.

## متوقف عنده (لرئيس التحرير)
- **exp-buddha-four-sights-renunciation**: يحتاج تدقيق بشري لدقة الاستشهاد بـBuddhacharita/Nidanakatha.
- **exp-camus-algerian-poverty-sun** و**exp-carl-sagan-pale-blue-dot-awe**: العبارات الشهيرة المتداولة ("الفقر تحت الشمس"، "انظر مرة أخرى لتلك النقطة") إعادة صياغة تقريبية لا اقتباس حرفي مؤكد — يحتاج تدقيق على النص الأصلي قبل اعتمادها كاقتباس مباشر.
- **exp-boethius-prison-consolation**: تاريخ إعدام بوئثيوس مختلف عليه أكاديمياً (524 أو 525م) — أُشير للاثنين في المتن.
- **exp-childhood-amnesia**: لا يوجد ملف `thk-` مؤكد لكاثرين نيلسون أو تشي وانغ في الأطلس — لم تُخترع slugs لهما.
- **exp-chogyam-trungpa-crazy-wisdom**: فجوة غير محلولة عن سلوكه الشخصي تحتاج مصدراً أولياً مستقلاً عن مذكراته.
- **exp-depersonalization**: رابطا `con-self` و`thk-sierra` غير موجودين في الأطلس بعد — لم يُربطا.
- **exp-derealization-depersonalization**: نسبة مصطلح 1914 لشيلدر تعتمد على مراجعة ثانوية (Sierra & David 2011) لا النص الألماني الأصلي.
- **exp-derrida-algerian-jewish-exclusion**: نص منشور فيشي 1940 (الحاكم شاتيل) يحتاج توثيقاً أرشيفياً أدق من السير الثانوية.
- **exp-dostoevsky-mock-execution-siberia** و**exp-dream-freud** و**exp-descartes-stove-heated-room**: التمييز بين الرواية الذاتية الموثقة (رسالة/مراسلات) والرواية الأدبية غير المباشرة (رواية الأبله؛ سيرة بايي 1691 لرؤى ديكارت) مسجّل صراحة في `gaps`.
- **exp-eckhart-tolle-night-transformation**, **exp-edith-eger-ballerina-auschwitz**, **exp-elyn-saks-schizophrenia-center**: كل السرد بضمير المتكلم مبني على مذكرات/مقابلات موثقة علناً لا اقتباسات حرفية مؤكدة حرفياً — يستحق مراجعة بشرية لدقة الصياغة المنقولة.
- **exp-foucault-tunisia-revolt**: تحويل ضمير المتكلم تفسير أسلوبي لمضمون مقابلة تروبادوري 1978 الموثقة، لا اقتباس حرفي — يستحق تدقيقاً على النص الأصلي.
- **exp-conversion-experience**: لا شيء متوقف.

## الملفات
content/ar/experiences/exp-augustine-garden-milan-tolle.md
content/ar/experiences/exp-awe-and-wonder.md
content/ar/experiences/exp-beauvoir-discovery-of-otherness.md
content/ar/experiences/exp-bessel-van-der-kolk-vietnam-vets.md
content/ar/experiences/exp-boethius-prison-consolation.md
content/ar/experiences/exp-bruce-perry-waco-siege-children.md
content/ar/experiences/exp-buddha-four-sights-renunciation.md
content/ar/experiences/exp-camus-algerian-poverty-sun.md
content/ar/experiences/exp-carl-sagan-pale-blue-dot-awe.md
content/ar/experiences/exp-childhood-amnesia.md
content/ar/experiences/exp-chogyam-trungpa-crazy-wisdom.md
content/ar/experiences/exp-clara-barton-civil-war-nursing.md
content/ar/experiences/exp-conversion-experience.md
content/ar/experiences/exp-david-duran-indigenous-soul-wound.md
content/ar/experiences/exp-deja-vu.md
content/ar/experiences/exp-depersonalization.md
content/ar/experiences/exp-derealization-depersonalization.md
content/ar/experiences/exp-derrida-algerian-jewish-exclusion.md
content/ar/experiences/exp-descartes-stove-heated-room.md
content/ar/experiences/exp-dostoevsky-mock-execution-siberia.md
content/ar/experiences/exp-dream-freud.md
content/ar/experiences/exp-eckhart-tolle-night-transformation.md
content/ar/experiences/exp-edith-eger-ballerina-auschwitz.md
content/ar/experiences/exp-elyn-saks-schizophrenia-center.md
content/ar/experiences/exp-ernest-shackleton-endurance-survival.md
content/ar/experiences/exp-existential-boredom.md
content/ar/experiences/exp-fanon-martinique-french-racism.md
content/ar/experiences/exp-flashback-ptsd.md
content/ar/experiences/exp-flow-state-csikszentmihalyi.md
content/ar/experiences/exp-foucault-tunisia-revolt.md
