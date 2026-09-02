# Task 9 — pastoral-counseling, pbsp, pcit
الحالة: مكتمل
العملية: ربط + evidence_level + تعميق متن لثلاث ملفات techniques | الملفات: 3

## الأرقام
روابط related: قبل 1/1/5 → بعد 2/3/6 (على الترتيب)
evidence_level: قبل غائب في الثلاثة → بعد traditional / experimental / well-established

## أمر التحقق
python3 scripts/build_slug_index.py  →  ✅ فهرس 6902 عنصر، بلا تعارضات جديدة من هذا التعديل

## قرارات اتخذتها
- tec-pastoral-counseling.md: أضفت `evidence_level: traditional` (لا تجارب ضبط عشوائي تسند الممارسة، مقاربة تاريخية-مؤسسية). صححت عنوان `br-transpersonal-psychology` ليطابق الملف الفعلي ("...(القوة الرابعة)"). أضفت رابط `tec-meaning-centered-psychotherapy` كتقنية منافسة علمانية لنفس فئة الأزمات الوجودية، مع تبرير في المتن. ذكرت أنطون بويسن (مؤسس Clinical Pastoral Education 1925) بالاسم في المتن دون اختراع slug له — سُجِّل الطلب.
- tec-pbsp.md: أضفت `evidence_level: experimental` (الأدبيات المتاحة دراسات حالة/سلاسل صغيرة غير مضبوطة). أضفت روابط `thk-apesso` و`thk-dboyden` (المبتكران — تحققت من وجودهما في EXISTING_SLUGS.md) بعد التأكد أنهما معتمدان. صححت عنوان `tec-psychodrama` ليطابق الملف الفعلي ("...(مورينو)"). أضفت فقرة مقارنة بالسيكودراما توضح سبب الربط.
- tec-pcit.md: أضفت `evidence_level: well-established` (مطابق لتوجيه المهمة — PCIT مصنّف كذلك في أدبيات العلاج القائم على الأدلة للاضطرابات السلوكية عند الأطفال). أضفت رابط `thk-ieyberg` (تحققت: en="Sheila M. Eyberg"، والعنوان العربي "شيرلي إِيبِرغ" هو تعريب Sheila وليس اسماً مختلفاً — طابقت `en` قبل الربط). أضفت فقرة "التقنية المنافسة" (PMT وCOS) بتبرير الفرق التقني في المتن.

## متوقف عنده (لرئيس التحرير)
- tec-pastoral-counseling.md: لا يوجد slug لأنطون بويسن (Anton Boisen) — مسجَّل في `agents_specs/requests-spark.md`.
- tec-pbsp.md: لا توجد دراسة ضبط عشوائي محكّمة موثقة تسند فعالية PBSP — سُجِّلت الفجوة بدلاً من اختراع مصدر.
- tec-pcit.md: لا يوجد slug لدراسة/تجربة بعينها بأرقامها (حجم عينة، نتيجة) تسند تصنيف well-established — سُجِّلت الفجوة بدقة بدلاً من اختراع رقم.

## الملفات
content/ar/techniques/tec-pastoral-counseling.md
content/ar/techniques/tec-pbsp.md
content/ar/techniques/tec-pcit.md
