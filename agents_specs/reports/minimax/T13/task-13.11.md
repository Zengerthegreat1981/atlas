# Task 13.11 — المدارس الغائبة (دفعة 11)
الحالة: مكتمل | الملفات الجديدة: 4 (104/~147 مدرسة إجمالاً الآن)

## العملية
10 subagents. 3 اكتشفوا ملفات موجودة مسبقاً (تحقق فقط)، 4 أنتجوا ملفات جديدة فعلية، و2 اكتشفا تكراراً حقيقياً يحتاج قرار دمج شخصي مني (Milan، Structural Family Therapy) — طبّقت الدمج بنفسي وفق قاعدة 6. تحقق شخصي نهائي بـpreflight + grep قائمة سوداء + إصلاح مخالفة عنوان حقيقية إضافية اكتُشفت (thk-ydolan).

## ✅ الملفات الجديدة (4)
- **sch-mimetic-theory** (SCH-506) — نظرية الرغبة المحاكية (رينيه جيرار، 1961-1978)
- **sch-filial-therapy** (SCH-0506*) — العلاج العلائقي الوالدي/باللعب (غورني/أكسلاين/لاندريث، 1964)
- **sch-holotropic-breathwork** (SCH-0507*) — التنفس الهولوتروبي (غروف، منتصف السبعينيات)
- **sch-psychosynthesis** (SCH-505) — السيكوسينتيسيز (أساجيولي، 1926)

*(نفس ملاحظة تصادم ترقيم الدفعة السابقة — subagents متوازية أنتجت نفس الرقم أحياناً، يحتاج فحص قبل الترقية)*

## ⚠️ دمجان فعليان طبَّقتهما بنفسي (قاعدة 6)
1. **br-milan-strategic (جديد) ↔ sch-milan-systemic (موجود مسبقاً في drafts)**: كلاهما يغطي نفس الفريق (سيلفيني-بالازولي/بوسكولو/تشيكين/براتا، 1967-1971). **الملف الجديد (br-milan-strategic، BRN-0335) أُبقي كنسخة الأساس** لتصنيفه الأدق (تيار تابع لـsch-systemic-family، مطابقاً لـbelongs_to الفعلي في thk-mselvini) وتغطيته الأعمق (الانشقاق 1979-1980، مفهومي الفضول/اللاتوقير عند تشيكين، تطور توم أندرسون للفريق العاكس). **sch-milan-systemic حُوِّل لملف إحالة redirect_to: br-milan-strategic**. أعضاء إضافيون في الملف القديم (thk-mandolfi، thk-llosi، thk-vcarrera، thk-lonan) لم يُنقلوا تلقائياً — يحتاجون تحققاً من انتمائهم الفعلي أولاً.
2. **sch-structural-family-therapy (جديد) ↔ br-structural-family (معتمد بالفعل في content/ar/branches/)**: تكرار حقيقي. **الملف المعتمد (br-structural-family، BRN-0235) أُبقي كنسخة الأساس** (ملف حي معتمد، لا مسودة). الإضافة الحقيقية الوحيدة في المسودة الجديدة (ربط thk-mnichols غير الموجود في الملف المعتمد) **نُقلت مباشرة إلى br-structural-family.md** (تعديل بسيط على ملف معتمد). **sch-structural-family-therapy حُوِّل لملف إحالة redirect_to: br-structural-family**.

## ✅ ملفات مؤكَّدة موجودة مسبقاً (3 — تحقق فقط)
- sch-adlerian (SCH-373) بدل الاسم المطلوب sch-adlerian-individual-psychology
- sch-art-therapy (SCH-374)
- sch-solution-focused (SCH-0369، content/ar/schools/ معتمد) — لاحظ subagent تصحيح تاريخ تأسيس خاطئ في بريف التاسك (1982 لا 1978)

## ⚠️ إصلاح إضافي اكتُشف ومُطبَّق مني شخصياً
- **thk-ydolan.md**: رابط مكسور فعلي (`thk-sdeshazer` غير موجود؛ الاسم الصحيح `thk-sdeshacer`) + عدم تطابق تشكيل حرفي في العنوان ("شيزَر" بتشكيل مقابل "شيزر" بدونه في الملف الفعلي) — صُحح كلاهما.
- **br-sport-psychology.md** (من 13.10): تأكدت أن إضافة thk-rsuinn سليمة بعد preflight.

صفر slugs مخترعة، صفر مصادر ملفَّقة جديدة.

## قرارات جودة بارزة
- sch-mimetic-theory: لم يُثبَّت ادّعاء تأثير جيرار على بيتر ثيل (لا مصدر أكاديمي موثوق) — أُسقط بدل تأكيده كحقيقة.
- sch-holotropic-breathwork: تحقق من وجود thk-sgrof/thk-cgrof/thk-wrichards قبل الربط، لا افتراض.
- sch-filial-therapy: صلة thk-mahoney بالمدرسة أقل توثيقاً من لاندريث — سُجِّلت كفجوة صريحة بدل فرض الرابط.

## متوقف عنده (لرئيس التحرير)
- تصادم ترقيم SCH بين subagents متوازية (نفس ملاحظة 13.10) — يحتاج فحص وإعادة ترقيم قبل الترقية.
- أعضاء br-milan-strategic المحتملون (mandolfi/losi/carrera/onnis) من الملف القديم — يحتاجون تحققاً قبل الإضافة.
- طلبات slug مسجلة: Colapinto، Montalvo، Rosman، Fishman (العلاج البنيوي)، Edith Kramer (فن)، Clive Robbins (موسيقى) — بعضها ربما مسجل مسبقاً في requests-minimax.md، يحتاج مراجعة تجميعية.
- ازدواج ملفَّي thk-assagioli / thk-robert-assagioli (نفس الشخص، ملفان منفصلان) — اكتُشف أثناء 13.11، لم يُلمس (خارج نطاق مهمة المدارس)، يحتاج قرار دمج منفصل.

## الملفات (مسار كامل، الجديدة والمعدَّلة)
- جديد: content/ar/drafts/minimax/schools/sch-mimetic-theory.md, sch-filial-therapy.md, sch-holotropic-breathwork.md, sch-psychosynthesis.md
- جديد ثم أُبقي كأساس دمج: content/ar/drafts/minimax/branches/br-milan-strategic.md
- حُوِّل لإحالة: content/ar/drafts/minimax/schools/sch-milan-systemic.md, sch-structural-family-therapy.md
- تعديل جانبي على ملفات معتمدة: content/ar/branches/br-structural-family.md (أُضيف thk-mnichols)، content/ar/thinkers/thk-ydolan.md (أُصلح رابط مكسور)
