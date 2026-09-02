# Task 2.39
الحالة: مكتمل
العملية: تحقق وجود + تدقيق قرائي كامل لعشرة مفكرين (تسعة موثّقون فعلياً + ازدواج واحد حُجر) | الملفات: 10

## الأرقام
جمل القائمة السوداء: قبل 3 (theophrastus, simplicius, numenius) → بعد 0
`## المصادر` موجودة: قبل 1/10 (thk-okot-pbitek فقط بشكل غير مكتمل) → بعد 9/10 (كل الملفات الموثّقة، عدا thk-rick-doblin المحجور)
edges.belongs_to بنص حر لا slug: قبل 2 (mitch-albom, yang-xiong) → بعد 0
روابط related بtitle متضارب مع الملف المستهدف: قبل 11 (7 في yang-xiong + 3 في okot-pbitek + 1 في marx) → بعد 0
روابط related غير مبرَّرة في المتن: قبل 5 (4 كاسيرر/برغسون + 1 hegelianism-psychoanalysis في marx) → بعد 0 (حُذفت 4، وبُرِّر الخامس في المتن)
ملفات محجورة (دمج+إحالة): 1 (thk-rick-doblin)

## أمر التحقق
`python3 scripts/preflight_check.py --report agents_specs/reports/minimax/T2/task-2.39.md` → ✅ 10 ملف — صفر مخالفات آلية
grep يدوي على الـ17 جملة من القائمة السوداء على الملفات العشرة → 0 تطابق

## قرارات اتخذتها
- **thk-theophrastus**: موثّق (تلميذ أرسطو، 371–287 ق.م، مؤسس علم النبات ومؤلف "الطبائع" — تاريخياً مؤكد بمصادر أكاديمية مستقلة). حذفت جملة القائمة السوداء وقسم الاقتباسات الفارغ، أضفت `## المصادر` (Diogenes Laertius, Fortenbaugh, Rusten, Sharples)، دقّقت gaps لتكون محددة بدل نص عام مكرر.
- **thk-mill**: موثّق (John Stuart Mill، شخصية شهيرة جداً — تحققت من التواريخ والنسب، كلها صحيحة). أضفت `## المصادر` (Autobiography, Collected Works, Reeves, Skorupski). صحّحت "Three Essays on Religion (1874)" لتوضيح أنه نُشر بعد وفاته (توفي 1873). برّرت رابط ctx-1848 بجملة في المتن عن مراجعة "مبادئ الاقتصاد السياسي" في ضوء ثورات 1848.
- **thk-marx**: موثّق (Karl Marx، شخصية شهيرة جداً — تحققت من التواريخ والنسب والمؤلفات، كلها صحيحة). أضفت `## المصادر` (MEGA, McLellan, Berlin, Fowkes). حذفت 4 روابط related غير مبرَّرة وغير ذات صلة (wrk-essay-on-man-cassirer، wrk-symbolic-forms-cassirer، wrk-matter-and-memory-bergson، wrk-time-and-free-will-bergson — تلوّث نسخ-لصق واضح، كاسيرر وبرغسون لا صلة لهما بالمتن). صحّحت title رابط rel-hegelianism-psychoanalysis (كان يحمل عنواناً فرعياً "من ماركس إلى لاكان" غير موجود في الملف الفعلي) وبرّرته بجملة في المتن عن مدرسة فرانكفورت. برّرت روابط ctx- الثلاثة الباقية (مانشستر، كومونة باريس 1871، أزمة 2008) بجمل في المتن. أضفت "بعد وفاته" قبل كل سنة لاحقة لـ1883 مذكورة في المتن (1932 المخطوطات، 1955 ماركوزه، 1993 دريدا، 2008 الأزمة المالية).
- **thk-mitch-albom**: موثّق (صحفي وكاتب أمريكي حقيقي، "ثلاثاءات مع موري" 1997 كتاب حقيقي موثّق). حذفت جملة القائمة السوداء. صحّحت `edges.belongs_to` الذي كان نصاً حراً "السرديات النفسية والإنسانية" لا slug فعلياً → `edges: []` وسجّلت المدرسة الغائبة في missing-schools.md. أضفت `## المصادر`.
- **thk-simplicius**: موثّق (فيلسوف أفلاطوني محدث، شارح أرسطو، 490–560م — تاريخياً مؤكد). حذفت جملة القائمة السوداء وقسم الاقتباسات، أضفت `## المصادر` (Sorabji series, Hadot, Baltussen, Brittain & Brennan).
- **thk-okot-pbitek**: موثّق (شاعر وفيلسوف أوغندي حقيقي، "أغنية لاوينو" 1966 عمل حقيقي موثّق). صحّحت 3 روابط related بtitle متضارب (thk-alexis-kagame، sch-african-decolonial، con-ubuntu-african-humanism)، وحذفت رابط thk-rcabrera الخاطئ تماماً (الملف المستهدف تحت هذا الـslug يوثّق شخصاً آخر كلياً — أكينسولا أكيووو لا روبن روميرو كابريرا — كان نسخ-لصق خاطئ). أضفت `## المصادر`. صحّحت صياغة تاريخين لاحقين لوفاته (1982) ليحملا "بعد وفاته" (1986، 1991).
- **thk-rick-doblin**: **حُجر (دمج + إحالة، لا "غير موجود")**. الشخص حقيقي (ريك دوبان/دابلن، مؤسس MAPS 1986) لكن الملف ازدواج كامل لملف موجود بالفعل تحت slug آخر لنفس الشخص: `thk-rmdoblin` — الذي كان بالفعل يحمل `## المصادر` كاملة بمصادر أكاديمية حقيقية (Doblin 2002، Mitchell et al. 2021 في *Nature Medicine*، أرشيف MAPS). الملف الأصلي thk-rick-doblin كان يعترف بالازدواج داخل متنه الظاهر (رابط related لـthk-rmdoblin موصوف بـ"نسخة قديمة") بدل حسم القرار — وهذا بالضبط ما تحذّر منه القاعدة 11. حُوّل لقالب حجر/إحالة قياساً على سابقة thk-pkuhn المسجّلة في quarantine-minimax-archive، مسجَّل في quarantine-minimax.md. **ملاحظة سؤال المستخدم عن ازدواج محتمل مع thk-rmdoblin: مؤكَّد، وقد حُسم بالدمج.**
- **thk-numenius**: موثّق (نومينيوس الأفامي، أفلاطونية وسطى، ~150–200م — تاريخياً مؤكد، مصدر شذراته يوسابيوس وكليمنضس). حذفت جملة القائمة السوداء (الاقتباس الفعلي الموجود سليم ومُسنَد فأُبقي عليه)، أضفت `## المصادر` (Eusebius, Des Places, Dillon, Porphyry).
- **thk-schleiermacher**: موثّق (فريدريش شلايرماخر، أب الهرمنيوطيقا الحديثة، 1768–1834 — تاريخياً مؤكد). حذفت جملة القائمة السوداء (الاقتباس الموجود سليم فأُبقي عليه)، أضفت `## المصادر` (Bowie, Crouter, Dilthey, Grondin). صحّحت صياغة سنة نشر "Hermeneutik und Kritik" (1838، بعد وفاته) لتحمل الإشارة الصريحة.
- **thk-yang-xiong**: موثّق (فيلسوف وشاعر صيني من عصر هان، 53 ق.م–18م — تاريخياً مؤكد). صحّحت `edges.belongs_to` من نص حر "الكونفوشية الهانية" (لا slug فعلياً) → `edges: []` وسجّلت المدرسة الغائبة في missing-schools.md (مميّزةً عن sch-confucian-early). صحّحت 7 روابط related بtitle متضارب مع الملف المستهدف الفعلي (thk-dong-zhongshu، thk-confucius، thk-mencius، thk-xunzi، sch-confucian-early، sch-yinyang، sch-legalism، con-yin-yang). حذفت اقتباساً منسوباً لمترجم غير موثَّق ("مايكل ليو") لعدم القدرة على التحقق منه، وأضفت `## المصادر` حقيقية بدلاً منه (Nylan, Knechtges, Ban Gu's Hanshu). صحّحت خطأ مطبعي في عنوان قسم "موقعه منتيار" → "موقعه من التيار".

## متوقف عنده (لرئيس التحرير)
- لا شيء — الدفعة اكتملت بالكامل بلا نقاط معلّقة.

## الملفات
content/ar/thinkers/thk-theophrastus.md
content/ar/thinkers/thk-mill.md
content/ar/thinkers/thk-marx.md
content/ar/thinkers/thk-mitch-albom.md
content/ar/thinkers/thk-simplicius.md
content/ar/thinkers/thk-okot-pbitek.md
content/ar/thinkers/thk-rick-doblin.md
content/ar/thinkers/thk-numenius.md
content/ar/thinkers/thk-schleiermacher.md
content/ar/thinkers/thk-yang-xiong.md
