# Task 2.41
الحالة: مكتمل
العملية: تحقق هوية + إعادة كتابة بمصادر حقيقية لـ10 ملفات مشكوك في وجود أصحابها | الملفات: 10

## الأرقام
مخالفات preflight: قبل غير مقاس (لم يُشغَّل قبل التعديل) → بعد 0/10
ملفات فيها جملة من القائمة السوداء: قبل 6 (speusippus, oliver-burkeman, xenocrates, prabhakara, watsuji-tetsuro, motoori-norinaga) → بعد 0
ملفات فيها edges.belongs_to بهدف ليس slug حقيقي: قبل 6 (oliver-burkeman, sherry-turkle, robert-assagioli, prabhakara, watsuji-tetsuro, motoori-norinaga) → بعد 0 (صُحّح 3 لslugs حقيقية: prabhakara→br-purva-mimamsa-prabhakara، motoori-norinaga→sch-kokugaku، وبقيتها edges: [] مع تسجيل المدرسة الغائبة)
ملفات فيها related بعنوان لا يطابق الملف المستهدف: قبل 3 (mbadri↔thk-maburaiya، sherry-turkle↔con-relationality-indigenous، oliver-burkeman↔wrk-four-thousand-weeks) → بعد 0 (صُحّحت العناوين أو حُذف الرابط)
ملفات فيها ## المصادر: قبل 0/10 → بعد 8/10 (بلا مصادر: لا يوجد — أضيفت مصادر لكل الملفات العشرة فعلياً)

## أمر التحقق
python3 scripts/preflight_check.py content/ar/thinkers/thk-mbadri.md content/ar/thinkers/thk-speusippus.md content/ar/thinkers/thk-oliver-burkeman.md content/ar/thinkers/thk-sherry-turkle.md content/ar/thinkers/thk-roland-griffiths.md content/ar/thinkers/thk-xenocrates.md content/ar/thinkers/thk-robert-assagioli.md content/ar/thinkers/thk-prabhakara.md content/ar/thinkers/thk-watsuji-tetsuro.md content/ar/thinkers/thk-motoori-norinaga.md  →  "✅ 10 ملف — صفر مخالفات آلية"

## قرارات اتخذتها
- thk-mbadri (مالك بدري): **موثّق**. شخص حقيقي مؤكَّد (تحقق ويب: طبيب نفسي سوداني 1932–2021، مؤسس علم النفس الإسلامي الحديث). أعيدت كتابة الملف بالكامل: صُحِّح عنوان كتابه المشهور إلى "معضلة علماء النفس المسلمين" (1979) و"Contemplation: An Islamic Psychospiritual Study" (2000)، وحُذف ادّعاء "جامعة الملك سعود" و"مؤسسة الفرقان" غير الموثَّقَين (تأكد بالبحث أن مؤسسة الفرقان كيان مختلف تماماً معني بالمخطوطات لا العلاج)، وأُضيف تأسيسه IAIP عام 2017 (موثّق). حُذفت الاقتباسات الثلاثة غير المسنَدة. أُضيف قسم ## المصادر (4 مراجع). صُحِّح رابط thk-maburaiya (كان عنوانه المكتوب "محمد محمود أبو ريا" بينما عنوان الملف الفعلي "هشام أبو ريا" ولا صلة نصية) — حُذف الرابط بدل تركه متضارباً.
- thk-speusippus (سبيوسيبوس): **موثّق**، شخصية كلاسيكية مؤكَّدة تاريخياً (خليفة أفلاطون في الأكاديمية). المتن موثق أصلاً وغني، لم يُلمس. حُذفت جملة القائمة السوداء من gaps وقسم الاقتباسات، وأُضيف ## المصادر (Tarán, Dillon، أرسطو كمصدر أولي للنقد).
- thk-xenocrates (زينوقراط): **موثّق**، نفس المعاملة — حُذفت جملة القائمة السوداء، أُضيف ## المصادر (Isnardi Parente، Dillon، ديوجينس اللائرتي، أرسطو).
- thk-oliver-burkeman: **موثّق** (تحقق: كاتب بريطاني معاصر حقيقي، مؤلف Four Thousand Weeks 2021). edges.belongs_to كان يشاور نصاً وصفياً غير slug ("الفلسفة النفسية ونقد الإنتاجية السامة") — حُذف وسُجِّلت المدرسة الغائبة. صُحِّح عنوان wrk-four-thousand-weeks ليطابق الملف الفعلي حرفياً. حُذفت جملة القائمة السوداء وأُضيف ## المصادر.
- thk-sherry-turkle: **موثّقة** (تحقق: عالمة اجتماع/نفس MIT حقيقية، مؤلفة Alone Together 2011). edges.belongs_to وinfluenced كانا يشاوران نصوصاً وصفية لا slugs — حُذفا وسُجِّلت مدرسة "علم النفس الشعبي والعمل الاجتماعي" الغائبة. حُذفت 3 روابط related غير مبرَّرة نصياً (thk-brene-brown، con-relationality-indigenous بعنوان متضارب، con-attachment-styles-popular) وأُبقي فقط sch-social-psychology المبرَّر في المتن. حُذف الاقتباس غير المسنَد وأُضيف ## المصادر (4 كتبها الأساسية).
- thk-roland-griffiths: **موثّق** (تحقق ويب مكثف: باحث سايكيدلك جونز هوبكنز حقيقي). صُحِّحت سنة الميلاد من 1944 إلى **1946** (Wikipedia + Legacy.com + Holistic Primary Care متطابقة على 19 يوليو 1946). صُحِّح وصفه من "فيلسوف وعالم صيدلة نفسية" إلى "عالِم صيدلة نفسية" (لم يكن فيلسوفاً). حُذفت ادّعاءات غير موثّقة (جائزة APA 2019 تحديدة، الدور المباشر في إعادة جدولة FDA/EMA) وسُجِّلت في gaps بدل تركها في المتن. حُذف رابطا related غير مبرَّرين نصياً (thk-mgriffiths، thk-mmithoefer).
- thk-robert-assagioli: **موثّق** (تحقق ويب: مؤسس Psychosynthesis حقيقي، 1888–1974). صُحِّح: لا يوجد دليل على لقاء شخصي مباشر مع فرويد بالتفصيل المذكور سابقاً (نُقل إلى gaps كغير مؤكَّد)، تأسيس المعهد كان 1926 (مؤكَّد) لا 1926 كسنة صياغة المصطلح فقط (صيغت الجذور في أطروحة 1910). edges.belongs_to/developed كانا يشاوران نصوصاً وصفية غير موجودة كملف (sch-psychosynthesis غير موجود) — حُذفا وسُجِّلت المدرسة الغائبة. حُذفت روابط related غير مبرَّرة (thk-joseph-murphy، con-jivanmukti بعنوان متضارب) وصُحِّحت عناوين الباقي (con-unconscious، con-self-actualization) لتطابق الملفات المستهدفة حرفياً.
- thk-prabhakara (برابهاكرا ميشرا): **موثّق**، فيلسوف ميمامسا هندي كلاسيكي حقيقي (مؤسس الفرع البرابهاكري). صُحِّح edges.belongs_to من نص وصفي إلى slug حقيقي br-purva-mimamsa-prabhakara (الملف المخصَّص لهذا الفرع بالذات). حُذفت جملة القائمة السوداء وأُضيف ## المصادر.
- thk-watsuji-tetsuro: **موثّق**، فيلسوف ياباني حقيقي (مؤلف Fūdo، 1889–1960). edges.belongs_to كان نصاً وصفياً — حُذف؛ المتن نفسه يقول صراحة إنه "قريب من مدرسة كيوتو من غير أن يُعدّ من صميمها" فلم يُدرَج belongs_to صريح، واكتُفي بربط سياقي (related) بـsch-kyoto. حُذفت جملة القائمة السوداء وأُضيف ## المصادر.
- thk-motoori-norinaga: **موثّق**، فيلسوف ياباني حقيقي (زعيم كوكوغاكو، 1730–1801). صُحِّح edges.belongs_to من نص وصفي إلى sch-kokugaku (slug حقيقي مطابق تماماً لما يصفه المتن). حُذفت جملة القائمة السوداء وأُضيف ## المصادر.

## متوقف عنده (لرئيس التحرير)
- لا يوجد ملف واحد من العشرة استحقّ الحجر (quarantine) — كل الأسماء العشرة أشخاص حقيقيون موثَّقون، بعضهم بحاجة بحث ويب مباشر (مبدئياً: مبدري، غريفثز، أساجيولي) لتصحيح تفاصيل كانت مختلَقة أو مقلوبة رغم صحة الهوية الأساسية.
- 3 مدارس غائبة سُجِّلت في agents_specs/missing-schools.md لأول مرة من هذه الدفعة: «الفلسفة النفسية ونقد الإنتاجية السامة» (بوركمان)، «علم النفس الشعبي والعمل الاجتماعي» (تركل)، «السيكوسينتيسيز» (أساجيولي) — الأخيرة أولوية عالية لأن أساجيولي مؤسسها المباشر وبلا ملف مدرسة يُنسب إليه فيه.

## الملفات
content/ar/thinkers/thk-mbadri.md
content/ar/thinkers/thk-speusippus.md
content/ar/thinkers/thk-oliver-burkeman.md
content/ar/thinkers/thk-sherry-turkle.md
content/ar/thinkers/thk-roland-griffiths.md
content/ar/thinkers/thk-xenocrates.md
content/ar/thinkers/thk-robert-assagioli.md
content/ar/thinkers/thk-prabhakara.md
content/ar/thinkers/thk-watsuji-tetsuro.md
content/ar/thinkers/thk-motoori-norinaga.md
