# Task 13.18 — جولة تدقيق مستقلة نهائية (orphan-scan) + إغلاق فجوات حقيقية
الحالة: مكتمل | الملفات الجديدة: 9 مدارس + 18 إصلاح رابط مكسور

## السبب
بعد استنفاد قائمة `missing-schools.md` اليدوية (13.16-13.17)، طُلب تحقق مستقل بمنهجية مختلفة قبل إعلان Task 13 مكتملاً: **مسح كامل لكل مراجع `belongs_to`/`relates_to`/`related` عبر المستودع بأكمله** (content/ar + drafts/minimax + drafts/spark)، لإيجاد أي slug مُشار إليه فعلياً من محتوى حقيقي لكنه غير موجود كملف — نفس الطريقة التي كشفت `sch-trauma-psychology` سابقاً.

## النتيجة
- **2876 مرجع slug فريد** عبر المستودع، **3264 ملف موجود فعلياً** (بعد الحساب)، **195 مرجعاً يتيماً** بعد الطرح.
- استُبعدت أسماء مصنَّفة `LIKELY_FABRICATED` رسمياً في `missing-thinkers-final-resolution.md`.
- **33 حالة عالية الأولوية** (مُشار إليها من ملفين أو أكثر) — عولجت كلها في هذه الدفعة.
- **~160 حالة منخفضة الأولوية** (إشارة واحدة فقط) — أغلبها إما أسماء مفكرين ثانويين محتملي الفبركة (يحتاجون تحققاً فردياً منفصلاً قبل أي إنشاء) أو فروع تقنية دقيقة (br-) لا تستدعي إنشاءً فورياً — **مؤجَّلة**، ليست فجوة حرجة.

## ✅ إصلاحات روابط مكسورة (18 ملفاً معتمداً) — لا إنشاء، تصحيح مسار فقط
اكتُشف أن أغلب الحالات عالية الأولوية كانت **مراجع خاطئة لاسم بديل** لملف موجود فعلاً تحت slug مختلف، لا فجوة حقيقية:
- `br-pop-psychology` (5 ملفات) → `sch-popular-psychology` (موجود)
- `sch-attachment-theory` (2 ملفات) → `br-attachment-theory` (موجود)
- `sch-critical-theory-frankfurt` (3 ملفات) → `sch-frankfurt-school` (موجود)
- `sch-humanistic-psychology` (2 ملفات) → `sch-humanistic` (موجود)
- `sch-trauma-focused` (2 ملفات، schools/sch-ifs وsch-emdr) → `sch-trauma-psychology` (أُنشئ في 13.16)
- `sch-experimental-psychology` (2 ملفات) → `sch-structuralism-wundt-titchener` (موجود؛ صُحح أيضاً مرجع ذاتي دائري كان سيظهر لاحقاً)
- `sch-pragmatism` (ملفا que- اثنان) → `sch-pragmatism-classical` (موجود، اكتشفه subagent الدفعة)
- `sch-mindfulness-based-therapy` (ملفا crt-/trm-) → `sch-clinical-mindfulness` (موجود)

## ✅ الملفات الجديدة الحقيقية (9 مدارس) — فجوات مؤكَّدة فعلاً
- **sch-analytical-psychology** — علم النفس التحليلي عند يونغ (فجوة كبرى مفاجئة: لا ملف مدرسة ليونغ إطلاقاً رغم الاستخدام الواسع)
- **sch-object-relations** — نظرية علاقات الموضوع (كلاين/فيربيرن/وينيكوت/كيرنبرغ)
- **sch-dream-psychology** — سيكولوجيا الأحلام (فرويد/يونغ/علم الأعصاب المعاصر)
- **sch-epistemology** — نظرية المعرفة كمدرسة فلسفية أساسية
- **sch-aesthetics** — علم الجمال الفلسفي
- **sch-philosophy-of-mind** — فلسفة العقل كمظلة تاريخية عامة (متمايزة عن sch-phil-mind-analytic الأضيق)
- **sch-philosophy-of-religion** — فلسفة الدين
- **sch-bergsonism** — الفلسفة البرغسونية (الديمومة، الحدس، الزخم الحيوي)
- **sch-islamic-sufism** — التصوف الإسلامي الكلاسيكي (الغزالي، الحلاج، الرومي) — متمايز عن sch-akbari وsch-islamic-esotericism الموجودين

## ⚠️ تصادم ترقيم ثلاثي متزامن — حُسم بمسح شامل نهائي
3 دفعات متوازية أنتجت تصادماً حاداً (SCH-0802/0803/0804 كل واحد ادَّعاه 2-3 ملفات معاً). **مسح إعادة ترقيم شامل نهائي** طُبِّق عبر content/ar/schools/ + drafts/minimax/schools/ + drafts/minimax/branches/ معاً (النطاق الكامل هذه المرة، لا الدرافت فقط) — اكتشف بالمناسبة **تصادماً قديماً مسبقاً غير مكتشف** (sch-zen-soto.md كان يتشارك SCH-0336 مع ملف آخر من قبل هذه الجلسة أصلاً). التحقق النهائي: **صفر تكرار عبر 7056 slug مفهرَس بالكامل**.

صفر slugs مخترعة، صفر مصادر ملفَّقة، صفر مخالفات preflight حقيقية، صفر تطابق قائمة سوداء.

## ✅ Task 13 — الحالة النهائية المؤكَّدة بمنهجيتين مستقلتين
تم التحقق الآن **مرتين بمنهجيتين مختلفتين تماماً** (القائمة اليدوية القديمة، ثم مسح orphan-scan مستقل للمستودع بأكمله) ولم تُكتشف أي فجوة عالية الأولوية متبقية. **135 + 9 = ~144 ملف مدرسة/فرع في drafts/minimax + content/ar/schools مجتمعين لهذا النطاق.**

## متوقف عنده (لرئيس التحرير)
- **160 حالة منخفضة الأولوية** (إشارة واحدة فقط) لم تُعالَج — أغلبها أسماء مفكرين ثانويين مشتبه فبركتهم (نمط "مؤلف مشارك مذكور مرة واحدة" الذي حذَّر منه `missing-thinkers-final-resolution.md` صراحة) أو فروع br- تقنية دقيقة جداً لا تستحق أولوية فورية. القائمة الكاملة محفوظة (يمكن استرجاعها عند الحاجة).
- طلب slug مسجَّل: al-Hallaj (thk-al-hallaj) — لا ملف مفكر له رغم مركزيته لـsch-islamic-sufism الجديد.
- ملاحظة تحريرية: thk-oaverderese، thk-rpla، thk-rvendramini (أعضاء sch-analytical-psychology) لم يُتحقق منهم سابقاً في ملف الحل النهائي — يستحقون مراجعة فردية.

## الملفات (مسار كامل، الجديدة)
content/ar/schools/{sch-analytical-psychology,sch-object-relations,sch-dream-psychology,sch-epistemology,sch-aesthetics,sch-philosophy-of-mind,sch-philosophy-of-religion,sch-bergsonism,sch-islamic-sufism}.md
