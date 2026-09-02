# Task 2.27
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 10

## الأرقام
جمل القائمة السوداء: قبل 6 (موزعة على thk-rsharma×1 صريحة + thk-tsexton×1 + thk-rado×1 + thk-walzer×1 + thk-sankara×1 + thk-togden×1 + thk-tausk×1، بعضها بصياغة متغيّرة عن النص الحرفي) → بعد 0 (تأكيد grep حرفي).
قرارات: موثّق 7 (thk-skripke, thk-rado, thk-walzer, thk-sankara, thk-togden, thk-tausk, thk-tleary) · حُجر 2 (thk-tsexton, thk-rsharma) · إحالة ازدواج 1 (thk-pdeegan≡thk-patdeegan).
أخطاء هوية مصححة: 3 (thk-rado عنوان خطأ «ثيودور»→«ساندور»؛ thk-walzer تاريخ وفاة مختلَق 2026 وهو حيّ فعلياً؛ thk-tausk رابط وقصة خاطئان — آنا فرويد/ماري بونابرت بدل هيلين دويتش الموثّقة).

## أمر التحقق
grep حرفي على جمل القائمة السوداء الـ17 على الملفات العشرة → 0 تطابق.
python3 scripts/preflight_check.py <الملفات العشرة> → ✅ 10 ملف — صفر مخالفات آلية (بعد تصحيح تاريخين: سنة 2022 في thk-sankara احتاجت «بعد وفاته» أقرب لها، وtitle في related لـthk-rmritchie كان يجب مطابقة «رالف ميتزner» الحرفي في الملف المستهدف).

## قرارات اتخذتها
- thk-skripke: موثّق — Saul Kripke، فيلسوف/منطقي أمريكي (1940–2022) مؤكَّد بمصادر مستقلة (Britannica, Daily Nous). أُعيد كتابة المتن (كان مشوّشاً بأسماء أعمال مختلطة)، صُحح active_end من 2020 إلى 2022 (سنة وفاته)، أُضيف `## المصادر`.
- thk-tsexton: غير موجود — بحث ويب مباشر (PCIT + "Toni Sexton") لم يُظهر أي وجود مستقل؛ الملف الأصلي كان يعترف صراحة بجملة القائمة السوداء وبروابط "أُزيلت لعدم التحقق" — تناقض قاعدة 11. حُجر، النسخة الأصلية أُرشفت، سُجّل في quarantine-minimax.md.
- thk-rado: موثّق — Sándor Radó (1890–1972)، محلل نفسي مجري-أمريكي مؤكَّد (Encyclopedia.com, Jewish Virtual Library). العنوان في frontmatter كان خطأً «ثيودور رادو» بينما `en` يقول Sándor — صُحح إلى «ساندور رادو». أُعيد كتابة المتن بمصادر حقيقية.
- thk-rsharma: غير موجود — بحث ويب مباشر ("Ramcharan Sharma" + Vedic Psychology) لم يُظهر أي دليل على وجوده أو على كتاب "Vedic Psychology: A Handbook". حُجر، أُرشف، سُجّل في quarantine-minimax.md.
- thk-walzer: موثّق — Michael Walzer، فيلسوف سياسي أمريكي، حيّ فعلياً حتى تاريخ اليوم (تأكيد بحث ويب: IAS Princeton يصفه بصيغة المضارع، لا وفاة مسجَّلة). الملف الأصلي كان يزعم "1935–2026" و`active_end: 2025` أي وفاة مختلَقة — صُححت إلى "مواليد 1935" و`active_end: "مستمر"`. أُصلح أيضاً edges.belongs_to من نص حر "الجمهورية المدنية الجديدة" (غير موجود كـslug) إلى `sch-civic-republicanism` الحقيقي، وصُحح title في related ليطابق عنوان الملف المستهدف فعلياً "الجمهورية المدنية (Civic Republicanism)".
- thk-pdeegan: ازدواج مؤكَّد — نفس الشخص الموثّق فعلياً على `thk-patdeegan` (دفعة 2.14، Patricia E. Deegan). حُوّل لقالب إحالة صريح (على نمط thk-mwhitehouse/thk-mary-whitehouse)، `edges: []`، `related` يشير فقط لـthk-patdeegan.
- thk-sankara: موثّق — Thomas Sankara، رئيس بوركينا فاسو (1983–1987)، هوية مؤكَّدة (متن، عنوان، `en` متطابقون). صُححت كلمة مشوّهة "بلفور" إلى توضيح موثَّق (كومباوريه بدعم فرنسي)، وأُضيفت عبارة "بعد وفاته" قبل ذكر إدانة كومباوريه القضائية 2022 (بعد active_end=1987).
- thk-togden: موثّق — Thomas Ogden، محلل نفسي أمريكي (مواليد 1946)، مؤكَّد (Wikipedia, PeoplePill). أُعيد كتابة المتن بتفاصيل سيرة دقيقة (أمهرست، ييل، تافيستوك، سان فرانسيسكو).
- thk-tausk: موثّق — Victor Tausk (1879–1919)، محلل نفسي مؤسِّس مبكر، مؤكَّد (Wikipedia, Roazen 1969). الرابط الأصلي لـthk-afreud وذكر "ماري بونابرت" في قصة انتحاره كانا خطأ هوية — الرواية الموثّقة فعلياً عن هيلين دويتش (استبدل الرابط بـthk-deutsch).
- thk-tleary: موثّق — Timothy Leary (1920–1996)، عالم نفس ورمز ثقافي أمريكي، مؤكَّد (Britannica). أُعيد كتابة المتن، صُحح title في related ليطابق حرفياً عنوان الملف المستهدف thk-rmritchie ("رالف ميتزner").

## متوقف عنده (لرئيس التحرير)
- thk-rmritchie: عنوانه الفعلي "رالف ميتزner" (خليط عربي/لاتيني — الاسم الصحيح Ralph Metzner = "رالف ميتزنر" عربياً بالكامل). هذا خطأ في الملف المستهدف نفسه (خارج نطاق دفعة thk-m→z المسموح لي بالكتابة فيها إذا كان ضمن نطاقي، لكنه لم يكن ضمن قائمة دفعتي) — يحتاج تصحيحاً منفصلاً.
- طلب slug جديد أو تأكيد: لا يوجد.

## الملفات
content/ar/thinkers/thk-skripke.md
content/ar/thinkers/thk-tsexton.md
content/ar/thinkers/thk-rado.md
content/ar/thinkers/thk-rsharma.md
content/ar/thinkers/thk-walzer.md
content/ar/thinkers/thk-pdeegan.md
content/ar/thinkers/thk-sankara.md
content/ar/thinkers/thk-togden.md
content/ar/thinkers/thk-tausk.md
content/ar/thinkers/thk-tleary.md
