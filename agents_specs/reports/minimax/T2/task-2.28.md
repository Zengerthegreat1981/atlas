# Task 2.28
الحالة: مكتمل
المسار: minimax | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 10

## الأرقام
جمل القائمة السوداء: 10 قبل (سطر واحد لكل ملف تقريباً) → 0 بعد
`## المصادر`: 0/10 قبل → 10/10 بعد
belongs_to بslug مخترع أو نصّي: 3 (srosenberg, tnhat, srhoades×1, rsuinn×1) → 0 (حُوّل لـslug حقيقي أو أُزيل + سُجّل في missing-schools.md)
related بعنوان غير مطابق للملف المستهدف: 2 (thk-sartre، thk-mbuber في thk-marcel) → 0
عناوين أقسام بجنس نحوي غلط: 1 ملف (thk-resick: "ما أعطاه/موقعه/أهم أعماله" لامرأة) → 0
خطأ هوية: 1 (thk-tnhat: "لاما" بدل "راهب زن") → مصحّح
مخالفات preflight_check.py: 2 (gaps بصيغة تؤكد حقيقة) → 0 (exit code 0)

## أمر التحقق
python3 scripts/task.py verify minimax 2.28
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 | فيها ## المصادر: 10 / 10

python3 scripts/preflight_check.py <10 ملفات> → ✅ 10 ملف — صفر مخالفات آلية. (exit code 0)

## قرارات اتخذتها
جميع العشرة أشخاص حقيقيون وموثّقون — لا حجْر ولا غموض في هذه الدفعة:

- **thk-srosenberg** (Stanley Rosenberg): موثّق — معالج يدوي دنماركي، مؤلف *Accessing the Healing Power of the Vagus Nerve* (North Atlantic Books, 2017). صُحّح `belongs_to` من نص حر إلى `sch-polyvagal-informed-therapy`، وأُضيف رابط `thk-stephen-porges` (كان مذكوراً بالاسم الخاطئ `thk-sporges` غير الموجود في gaps)، وحُذفت جملة القائمة السوداء من gaps.
- **thk-rycroft** (Charles Rycroft): موثّق — محلّل نفسي بريطاني، مؤلف *A Critical Dictionary of Psychoanalysis* (1968). حُذفت جملتا القائمة السوداء/الغموض من gaps واستُبدلتا بفجوة محددة (تفاصيل تدريبه في British Psychoanalytical Society).
- **thk-tnhat** (Thich Nhat Hanh / تِك نات هان): موثّق — راهب بوذي فيتنامي مؤسس Plum Village. **خطأ هوية مصحّح:** كان الملف يصفه بـ"لاما" (مصطلح للبوذية التبتية) بينما هو راهب من تقليد الزِن الفيتنامي. صُحّح `belongs_to` إلى `sch-engaged-buddhism`، وحُذف قسم "اقتباسات مختارة" بالكامل لأنه كان يحتوي فقط على جملة القائمة السوداء.
- **thk-resick** (Patricia A. Resick): موثّق — مطوّرة علاج المعالجة المعرفية (CPT) لـPTSD. **خطأ جنس نحوي مصحّح:** كانت عناوين الأقسام مذكّرة ("ما أعطاه"، "موقعه من التيار"، "أهم أعماله") رغم أن ريسك امرأة — صُحّحت لصيغة المؤنث. أُزيل placeholder `[DRAFT-UNKNOWN]` من `dates`.
- **thk-michael-eigen** (Michael Eigen): موثّق — محلّل نفسي أمريكي، مؤلف *The Psychoanalytic Mystic* (1998). صُحّح تناقض ترجمة عنوان *Faith of the Faithless* (كان مترجماً بصيغتين مختلفتين في نفس الملف)، وحُدد تعارض سنة الميلاد (1936 مقابل 1942) كفجوة بدل الجزم بأحدهما.
- **thk-srhoades** (Galena K. Rhoades): موثّقة — باحثة PREP مع هوارد ماركمن وسكوت ستانلي. `belongs_to` كان يشاور نصاً حراً "PREP (برنامج تعزيز العلاقة والوقاية)" وليس slug حقيقياً — لا يوجد ملف مدرسة لهذا البرنامج في الأطلس، فأُزيل الرابط وسُجّل في `missing-schools.md`.
- **thk-wimmer** (Franz Martin Wimmer): موثّق — فيلسوف نمساوي، مؤسس الفلسفة البين-ثقافية الأكاديمية. الملف كان بالفعل بجودة جيدة (روابط مطابقة، مصادر واقعية) — تعديلات طفيفة فقط على صياغة gaps.
- **thk-marcel** (Gabriel Marcel): موثّق — فيلسوف وجودي فرنسي مسيحي. **مخالفة معيار 4 مصحّحة:** رابط `thk-sartre` كان بعنوان "سارتر" بينما عنوان الملف الفعلي "جان بول سارتر"؛ ورابط `thk-mbuber` كان بعنوان "مارتن بوبر" بينما العنوان الفعلي "مارتن بُبَر" — صُحح الاثنان بالتطابق الحرفي.
- **thk-rsuinn** (Richard M. Suinn): موثّق — عالم نفس رياضي أمريكي، رئيس APA Division 47 سابقاً. `belongs_to` كان يشاور نصاً حراً "علم نفس الأداء" وليس slug — أُزيل وسُجّل في missing-schools.md. من 7 روابط `related` أصلية، أُبقي فقط على `thk-ogilvie` (المبرَّر بجملة جديدة في المتن)؛ أُزيلت 6 روابط غير مبرَّرة في المتن إطلاقاً (بما فيها رابط لخبرة تبدد الواقع لا علاقة لها بعلم نفس الرياضة، ورابط لأكاديمية إعلام غير مختصة، ورابط بعنوان "ماريان كركمار" بينما اسمها الحقيقي "مارينا كركمار").
- **thk-wilderson** (Frank B. Wilderson III): موثّق — فيلسوف ومؤسس الأفروبيسيميزم، مؤلف *Afropessimism* (2020). حُذفت جملة القائمة السوداء من gaps فقط؛ باقي الملف كان سليماً.

## متوقف عنده (لرئيس التحرير)
- لا شيء — لم يُصادَف أي ملف "غير موجود" في هذه الدفعة (لا إضافة لـ`quarantine-minimax.md`).
- **ملاحظة:** thk-rsuinn يحتوي روابط لملفات أخرى (thk-rafaeli-eyth بالذات) تعلن في gapsها الخاصة شكاً جدياً في وجود صاحبها — هذا الملف خارج نطاق دفعتي، لكن يستحق مراجعة Task 2 مستقلة.
- سُجّلت مدرستان غائبتان في `agents_specs/missing-schools.md`: PREP (Prevention and Relationship Enhancement Program) وعلم نفس الأداء الرياضي (Sport/Performance Psychology).

## الملفات
content/ar/thinkers/thk-srosenberg.md
content/ar/thinkers/thk-rycroft.md
content/ar/thinkers/thk-tnhat.md
content/ar/thinkers/thk-resick.md
content/ar/thinkers/thk-michael-eigen.md
content/ar/thinkers/thk-srhoades.md
content/ar/thinkers/thk-wimmer.md
content/ar/thinkers/thk-marcel.md
content/ar/thinkers/thk-rsuinn.md
content/ar/thinkers/thk-wilderson.md
