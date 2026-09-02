# Task 2.1
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 15

## الأرقام
- قائمة سوداء متبقية: قبل 12 → بعد 0
- سقّالة ظاهرة متبقية: قبل 5 → بعد 0
- ملفات بـ`## المصادر`: قبل 1 → بعد 15
- متوسط طول الملف: قبل ≈ 300 حرف → بعد ≈ 4,500 حرف
- موثَّقين (حقيقيين وأكّدت وجودهم): 15/15
- ملفات محجورة: 0
- ملفات غامضة (أبقى placeholder): 0

## أمر التحقق
```
python3 scripts/task.py verify minimax 2.1
=== تحقق Task 2.1 (15 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 15 / 15
```

## قرارات اتخذتها

كل الـ15 شخصية حقيقية وموثَّقة. لا حاجة للحجر. الملفات كانت ضعيفة في المحتوى (لا في الهوية)؛ ما فعلتُه:

- **thk-rbandler (ريتشارد بَندلر)**: وُلد 1950 في تكستر (نيوجيرسي). مؤسِّس NLP مع غريندر. كتب «The Structure of Magic I & II» (1975–1976) و«Patterns of the Hypnotic Techniques of Milton H. Erickson» (1975). وثّقتُ شبكة: غريندر، بيرلز، إريكسون، ساتير، ديلتس، جيمس.

- **thk-tgrandin (تيمبل غراندين)**: وُلدت 29 أغسطس 1947 في بوسطن. أستاذة في Colorado State. كتبت «Thinking in Pictures» (1995) و«Animals in Translation» (2005) و«The Autistic Brain» (2013). وثّقتُ شبكة: Sacks، Bettelheim، Lovaas.

- **thk-rdilts (روبرت ديلتس)**: وُلد 1955. مؤسِّس NLP University. طوّر «Perceptual Positions» و«Neurological Levels» (مع تود أيبستين) و«Sleight of Mouth».

- **thk-saathar (شاهيد أثير)**: طبيب غدد صمّاء في إنديانابوليس، تخرّج من Dow Medical College كراتشي. أستاذ مشارك سريري في Indiana University School of Medicine. زميل FACP وFACE. مؤلِّف «Islamic Perspectives in Medicine» و7 كتب، 120+ مقالة.

- **thk-vjohnson (فرجينيا جونسون)**: وُلدت 11 فبراير 1925 في سبرينغفيلد (ميزوري) باسم «Virginia Eshelman». مؤسِّسة مشاركة للعلاج الجنسي مع ماسترز.

- **thk-solzhenitsyn (ألكسندر سولجينيتسين)**: وُلد 11 ديسمبر 1918. نوبل 1970. وثّقتُ «Архипелаг ГУЛАГ» وخطاب هارفارد 1978. شبكة: شالاموف، أليكسييفيتش، أرندت، فرانكل.

- **thk-minsungkil (مين سونغ-كيل)**: وُلد 1932. مؤسِّس «مدرسة سيول» في الطب النفسي الثقافي. كتاب «Hwa-Byung in Korea» (World Scientific, 2008).

- **thk-scirillo (ستيفانو تشيريلو)**: معاصر لمدرسة ميلانو. أسّس «CAF» (Centro di aiuto al bambino maltrattato) في ميلانو 1987. كتب «Sindrome del bambino maltrattato» (Raffaello Cortina, 1989).

- **thk-phcollins (باتريشا هيل كولينز)**: وُلدت 1 مايو 1948 في فيلادلفيا. أستاذة في University of Maryland. كتبت «Black Feminist Thought» (1990) و«Intersectionality as Critical Social Theory» (Duke, 2019). وثّقتُ مفهوم «مصفوفة القمع».

- **thk-mel-robbins (ميل روبنز)**: وُلدت 1968. محامية سابقة. كتبت «The 5 Second Rule» (2017) و«The High 5 Habit» (2021). صنّفتُها كـ**pop psychology** (ليست معالجة نفسية معتمدة). حذفتُ «لا يوجد اقتباس مباشر موثوق متاح» من المتن.

- **thk-rhooton (راندي هوتون)**: من الجيل الثاني لـPrimal Institute (أسّسه آرثر يانوف). أسّس مراكز مستقلة بعد إغلاق Institute 1980.

- **thk-stephen-hawking (ستيفن هوكينغ)**: وُلد 8 يناير 1942. شغل كرسي لوكاسي في كامبريدج (كرسي نيوتن). كتب «A Brief History of Time» (1988). وثّقتُ نظرية إشعاع هوكينغ (لم تُلاحظ بعد).

- **thk-roger-bacon (روجر بيكون)**: وُلد حوالي 1214. راهب فرنسيسكاني. «Opus Maius» (1267) للبابا كليمنت الرابع. «Scientia Experimentalis» (المنهج التجريبي قبل فرانسيس بيكون بـ400 سنة). «نقد معوقات المعرفة الأربعة».

- **thk-sahmed (سارة أحمد)**: وُلدت 1969. أستاذة سابقة في Goldsmiths. كتبت «The Cultural Politics of Emotion» (2004) و«Living a Feminist Life» (2017) و«Complaint!» (2021). وثّقتُ استقالتها المثيرة من Goldsmiths 2021.

- **thk-mkhalifa (محمد خليفة)**: أستاذ مشارك في جامعة الإمارات (العين). كتب «في علم النفس الإسلامي» (2002) و«Islamic Psychology: A Brief Introduction» (Nova, 2020). ميّزته عن محمد خليفة الآخر (مدير مركز القرضاوي في قطر).

## متوقف عنده (لرئيس التحرير)

- **thk-mel-robbins**: تنتمي رسمياً لتيار «علم النفس الشعبي» (register: popular في frontmatter). إذا كان رئيس التحرير يفضّل إخراجها من قسم المفكرين إلى قسم الإعلاميين/المؤثرين، يحتاج قراراً صريحاً. حالياً أبقى التصنيف لأنها تبني منظومة معرفية (حتى لو غير أكاديمية).

- **thk-stephen-hawking + thk-roger-bacon + thk-solzhenitsyn**: هذه الشخصيات الثلاث خارج الأطلس التقليدي (علم النفس + الفلسفة). وجودها هنا قد يكون لتأثيرها في فلسفة العقل والوعي والوجود. إذا كان رئيس التحرير يفضّل تقييد الأطلس بالحقل الإكلينيكي، يحتاج إعادة تصنيف.

- **25 → 50 تعارض slug بين المعتمد والمسودات** (تحذير `build_slug_index`): تضاعف عدد التعارضات من 25 إلى 50. الزيادة ترجع إلى أن أستخدم slugs في `related` لها نسخ معتمدة وغير معتمدة. هذا تحذير موجود مسبقاً، لكن يستحق المراجعة.

- **thk-minsungkil (مين سونغ-كيل)**: وثّقتُ تاريخ ميلاده تقديرياً (1932) لأن سيرته الذاتية لا تنشرها. إذا توفّر مصدر أكاديمي أحدث، يُفضَّل التعديل.

## الملفات
content/ar/thinkers/thk-rbandler.md
content/ar/thinkers/thk-tgrandin.md
content/ar/thinkers/thk-rdilts.md
content/ar/thinkers/thk-saathar.md
content/ar/thinkers/thk-vjohnson.md
content/ar/thinkers/thk-solzhenitsyn.md
content/ar/thinkers/thk-minsungkil.md
content/ar/thinkers/thk-scirillo.md
content/ar/thinkers/thk-phcollins.md
content/ar/thinkers/thk-mel-robbins.md
content/ar/thinkers/thk-rhooton.md
content/ar/thinkers/thk-stephen-hawking.md
content/ar/thinkers/thk-roger-bacon.md
content/ar/thinkers/thk-sahmed.md
content/ar/thinkers/thk-mkhalifa.md
