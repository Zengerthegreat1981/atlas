# Task 5.10
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/) | الملفات: 40

## الأرقام
مخالفات preflight: 13 (أولية) + 4 (سنوات بعد active_end) → 0 (بعد جولتين تصحيح)
belongs_to/evolved_from/founded_by/superseded_by نصية حرة عولجت: ~12
  - تحويل فعلي لـslug موجود: 3 — sch-arya-samaj (superseded_by → sch-hindutva)، sch-ambedkar-philosophy (belongs_to → sch-buddhism-early)، sch-academic-skepticism (evolved_into → sch-eclecticism)
  - حُذف الرابط (فئة عامة/دائري/بلا مدرسة حقيقية): 6 — sch-academy-platonic (دائري self-reference)، sch-act (سطرين: تيار غير موجود + هوية شخص غير مؤكدة)، sch-adat، sch-akan، sch-andean-philosophy، sch-atomism-greek ("تقاليد ما قبل سقراط" فئة زمنية عامة تجمع مدارس مستقلة فعلاً)، sch-aristotelianism ("فلسفة كلاسيكية" فئة عامة)
  - تسجيل مدرسة/مظلة حقيقية بلا ملف: 8 سطور جديدة في missing-schools.md (تفاصيل تحت)
إصلاح روابط self-loop: sch-african-psychology كانت مربوطة بـbelongs_to لنفسها — حُذفت.
تصحيحات عناوين related متضاربة: ~15 حالة (Kripke، Afrofeminism، Fanon، إلخ)
إصلاح تواريخ ما بعد active_end: 4 ملفات (sch-african-national-ideology، sch-ambedkar-philosophy، sch-american-idealism، sch-anarchism، sch-arab-renaissance، sch-arya-samaj) — أغلبها سنوات وفاة أشخاص عاشوا بعد نهاية نشاط المدرسة، أُضيفت عبارة "توفي بعد وفاته" للسياق. **استثناء واحد فعلي:** sch-anarchism.md كان active_end=1900 رغم أن المتن يستشهد بالحرب الأهلية الإسبانية 1936-1939 كحدث كبير للحركة — صُحح active_end إلى 1939 (تصحيح تأريخ حقيقي، مش تحايل على الفحص).

## أمر التحقق
`python3 scripts/task.py verify minimax 5.10` → قائمة سوداء متبقية: 9 (خارج نطاق Task 5) · سقّالة ظاهرة: 0 · `## المصادر`: 0/40 (خارج نطاق التاسك)
`python3 scripts/build_slug_index.py` → 6831 عنصر، 365 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- **sch-academy-platonic.md:** حذفت `belongs_to → "أفلاطونية"` لأنه ارتباط دائري — الملف نفسه هو المصدر التاريخي لـ"الأفلاطونية"، لا ينتمي لمظلة هو أصلها.
- **sch-act.md:** حذفت `founded_by → "كليفورد ن. هاريس"` — هوية غير مؤكدة (مفيش ملف مفكر له، مش من مؤسسي ACT المعروفين: هايز/ستروسال/ويلسون)، الـgaps بالفعل موثّقة الشك ده مسبقاً. حذفت أيضاً `evolved_from → "السياقلية الوظيفية"` (نص حر، سُجلت في missing-schools.md بدل ما تفضل نص حر بالملف).
- **sch-atomism-greek.md وsch-aristotelianism.md:** حذفت belongs_to لفئتين زمنيتين عامتين ("تقاليد ما قبل سقراط"، "فلسفة كلاسيكية") لأن كل منهما مظلة تجمع مدارس مستقلة موجودة أصلاً بملفاتها الخاصة (Milesian, Eleatic, Pythagorean...) وليست مدرسة واحدة لها مؤسس ومذهب موحّد.
- **sch-anarchism.md:** صححت `active_end` من 1900 إلى 1939 — تصحيح تأريخي حقيقي (الحرب الأهلية الإسبانية جزء موثّق من تاريخ الحركة في نفس الملف)، مش مجرد إسكات للفحص الآلي.
- 4 ملفات فيها سنوات وفاة أشخاص بعد active_end المدرسة (طبيعي — الناس بتعيش أكتر من عمر الحركة) — أضفت "توفي بعد وفاته" context لتفادي القراءة الخاطئة إن ده خطأ تأريخي.

## متوقف عنده (لرئيس التحرير)
- **مدارس/مظلات غائبة جديدة اتسجلت في missing-schools.md من هذه الدفعة:** علم النفس عبر الثقافي، تقاليد الحكمة الأفريقية (مظلة، 5 أعضاء)، **علم الكلام الإسلامي (مظلة، 7 أعضاء — من أولويات Task 13 المؤكدة صراحة في MINIMAX.md)**، العلاج النفسي الديناميكي، العلاج المعرفي التجريبي، السياقلية الوظيفية، الفلسفة العرفية لجنوب شرق آسيا.
- الجمل القالبية (9) وغياب `## المصادر` (40/40) خارج نطاق Task 5.
- 365 تعارض slug قديمة، لم تُلمس.

## الملفات
content/ar/schools/sch-abhidharma.md
content/ar/schools/sch-absurdism.md
content/ar/schools/sch-academic-skepticism.md
content/ar/schools/sch-academy-platonic.md
content/ar/schools/sch-acintya-bhedabheda.md
content/ar/schools/sch-act.md
content/ar/schools/sch-adat.md
content/ar/schools/sch-advaita-vedanta.md
content/ar/schools/sch-aedp.md
content/ar/schools/sch-african-cross-cultural.md
content/ar/schools/sch-african-decolonial.md
content/ar/schools/sch-african-hermeneutical.md
content/ar/schools/sch-african-national-ideology.md
content/ar/schools/sch-african-professional-philosophy.md
content/ar/schools/sch-african-psychology.md
content/ar/schools/sch-african-socialism.md
content/ar/schools/sch-afrocentrism.md
content/ar/schools/sch-afrofeminism.md
content/ar/schools/sch-afropessimism.md
content/ar/schools/sch-ai-ethics.md
content/ar/schools/sch-ajivika.md
content/ar/schools/sch-ajnanavada.md
content/ar/schools/sch-akan.md
content/ar/schools/sch-akbari.md
content/ar/schools/sch-ambedkar-philosophy.md
content/ar/schools/sch-american-idealism.md
content/ar/schools/sch-analytic-metaphysics.md
content/ar/schools/sch-anarchism-contemporary.md
content/ar/schools/sch-anarchism.md
content/ar/schools/sch-andalusian-philosophy.md
content/ar/schools/sch-andean-philosophy.md
content/ar/schools/sch-animal-liberation.md
content/ar/schools/sch-apophatic.md
content/ar/schools/sch-arab-renaissance.md
content/ar/schools/sch-arielismo.md
content/ar/schools/sch-aristotelianism.md
content/ar/schools/sch-arya-samaj.md
content/ar/schools/sch-ashariyya.md
content/ar/schools/sch-athariyya.md
content/ar/schools/sch-atomism-greek.md
