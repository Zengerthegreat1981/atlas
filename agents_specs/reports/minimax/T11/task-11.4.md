# Task 11.4
الحالة: مكتمل
العملية: critiques/ (آخر 10 ملفات) + أول 20 ملف debates/ — تسمية الطرفين/الناقد بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py (task.py verify minimax 11.4): صفر مخالفات آلية (30/30 ملف)
تحقق يدوي إضافي (grep مباشر لكل جملة من القائمة السوداء الـ18 على الملفات الـ30): صفر تطابق

## ✅ critiques/ (276 ملفاً) — أول 100+ ملفاً منجزة عبر 11.1–11.4؛ debates/ بدأ رسمياً
هذه أول دفعة تُدخل ملفات `debates/` إلى جانب `critiques/`. المنهج تأكد صالحاً للنوعين: كل ملف `dbt-` لازم يوثّق طرفي النقاش الحقيقيين بالاسم/النص/السنة بدل مقارنة نظرية عامة.

## ⚠️ مصادر ملفَّقة/خاطئة إضافية — إجمالي Task 11 تخطى 25 حالة موثَّقة
- **crt-scientific-critique-transpersonal**: 4 مصادر ملفَّقة/غير قابلة للتحقق ("Raimo 1997 *Pseudoscience and Idolatry*"، "Peter Lipton 2004" مُطبَّق بلا صلة، "Andrew Faulkner 2016"، "Lindeman 1996") + خطأ سنة/موضوع لكتاب بلاكمور. استُبدلت بستنجر (1990)، شيرمر (1997)، ويلبر (1995 كمستهدَف)، غروف.
- **dbt-advaita-vs-dvaita**: "Viktor Hosley 2005" غير قابل للتحقق — حُذف وسُجِّل كفجوة.
- **crt-ryle-category-mistake-ghost-machine**: اكتشاف هوية حرج — `thk-ryle` الموجود بالأطلس هو **أنتوني رايل** (مبتكر CAT) وليس **غيلبرت رايل** الفيلسوف صاحب "شبح الآلة" — تم تفادي ربط خاطئ فادح، وسُجِّل طلب slug جديد لغيلبرت رايل بدل الربط الخاطئ.

## قرارات محتوى بارزة
- crt-sellars-myth-of-the-given: تصحيح `belongs_to` من `br-logical-positivism-vienna-circle` الخاطئ إلى `sch-critical-realism` (مطابق فعلياً لـ`thk-wsellars`).
- crt-scientific-critique-transpersonal: تصحيح `edges.target` من slug غير موجود (`sch-transpersonal-psychology`) إلى `sch-transpersonal`.
- dbt-brain-in-a-vat-skepticism: كان قالبياً بالكامل — أُعيد حول بوتنام (1981) ضد بروكنر (1986/1991)، وصُحح `belongs_to` الخاطئ (كان يشير لدائرة فيينا).
- dbt-abrupt-vs-gradual-enlightenment-chan: وثّق مسابقة القصيدتين الفعلية (هوي نينغ ضد شِن شيو) بالنصين الأصليين من سوترا المنصة؛ شِن شيو بلا ملف مفكر — سُجِّل طلب slug بدل اختراعه.
- ثلاثية بوبر وثلاثية ما-بعد-كولونيالية (من 11.3) لم تُلمس هنا؛ لا تكرار جديد مكتشف في هذه الدفعة.

صفر slugs مخترعة — كل حالة غموض (thk-gilbert-ryle، thk-brueckner، شِن شيو، تايلور/شفايتزر) سُجِّلت في `agents_specs/requests-minimax.md` بدل الربط أو الاختراع.

## متوقف عنده (لرئيس التحرير)
- **⚠️ مستمر**: النمط المنهجي لمصادر ملفَّقة في critiques/ ما زال يظهر في كل دفعة تقريباً (Task 11 الآن > 25 حالة موثَّقة عبر 11.1–11.4) — التوصية بتدقيق منفصل قائمة.
- طلبات slug جديدة مسجّلة: thk-gilbert-ryle، thk-renan، thk-sacy، thk-bernard-lewis، thk-brueckner، thk-shenxiu، thk-paul-taylor (بيئي)، thk-schweitzer.

## الملفات
crt-rorty-mirror-of-nature, crt-ryle-category-mistake-ghost-machine, crt-said-orientalism-epistemic-critique, crt-sandel-unencumbered-self, crt-schopenhauer-critique-of-optimism, crt-scientific-critique-transpersonal, crt-sellars-myth-of-the-given, crt-spivak-can-the-subaltern-speak, crt-taha-abderrahmane-critique-of-western-modernity, crt-wang-yangming-critique-of-external-learning, dbt-a-priori-vs-a-posteriori, dbt-abrupt-vs-gradual-enlightenment-chan, dbt-acceptance-vs-cognitive-change, dbt-adhd-overdiagnosis-overmedication, dbt-advaita-vs-dvaita, dbt-aging-psychotherapy, dbt-ai-personhood-and-moral-status, dbt-ambedkar-vs-gandhi-caste, dbt-analytic-synthetic-distinction, dbt-anarchism-vs-state, dbt-anatta-vs-atman-brahman, dbt-anthropocentrism-vs-biocentrism-ethics, dbt-antidepressants-efficacy-debate, dbt-asalat-al-wujud-vs-asalat-al-mahiyya, dbt-attachment-stability, dbt-aurobindo-vs-vivekananda, dbt-boss-binswanger, dbt-brain-in-a-vat-skepticism, dbt-brief-vs-long-term-therapy, dbt-british-yalom
