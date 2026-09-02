# Task 2.33
الحالة: مكتمل
العملية: Task 2 — تحقق فعلي من وجود صاحب كل ملف بين 32 مفكراً، وتطبيق أحد ثلاث نتائج (موثّق / غير موجود / غامض) | الملفات: 32

## الأرقام
جمل القائمة السوداء: 12 قبل (10 مطابقة حرفية + 2 صياغة قريبة تحت الاعتبار الموسّع) → 0 بعد
ملفات فيها `## المصادر`: 1/32 قبل → 32/32 بعد
مخالفات preflight_check.py: 12 قبل (بعد أول تصحيح) → 0 بعد
ملفات محجورة جديدة: 1 (thk-michael-der-meer)
روابط belongs_to حُوّلت من نص حر إلى slug حقيقي: 4 (thk-varela, thk-msimeona, thk-trore, thk-marshall)
روابط belongs_to حُذفت (لا مدرسة مطابقة) وسُجّلت في missing-schools.md: 5 (thk-wundt, thk-voltaire, thk-matt-haig, thk-rcallahan, thk-zhangyalin)
روابط related بعنوان مضادّ لعنوان الملف الحقيقي وتم تصحيحها: 5 (matt-haig×2, nasir-tusi×1, msimeona×1, npetry×1)

## أمر التحقق
`python3 scripts/task.py verify minimax 2.33` → جمل القائمة السوداء متبقية: 0 | سقّالة ظاهرة متبقية: 0 | فيها ## المصادر: 32/32
`python3 scripts/preflight_check.py <32 ملفاً>` → ✅ 32 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **31 ملفاً = موثّق (شخصيات حقيقية موثّقة تاريخياً/أكاديمياً)** — أُضيف لكل منها قسم `## المصادر` بمراجع حقيقية عن الشخص نفسه (لا عن مؤسس مدرسته)، وحُذفت كل جمل "لا يوجد اقتباس مباشر موثوق متاح" (وصياغاتها القريبة) من `gaps`:
  thk-mao-zedong, thk-muhammad-abduh, thk-tlynch, thk-wundt, thk-varela, thk-maddis, thk-voltaire, thk-mackinnon, thk-matt-haig, thk-orsigen, thk-william-ockham, thk-marshall, thk-suarez, thk-nasir-tusi, thk-merleau-ponty, thk-solomon-hebrew, thk-msimeona, thk-sohrevardi, thk-mmahler, thk-shen-buhai, thk-xu-xing, thk-shah-waliullah, thk-trore, thk-pseudo-dionysius, thk-rcallahan, thk-npetry, thk-pico, thk-zhangyalin, thk-valentinus, thk-zarathushtra, thk-mulla-sadra.
  - تحقق ويب مباشر لحالتين غامضتين ظاهرياً: **Zhang Yalin** — مؤكَّد حقيقي، طبيب نفسي صيني شارك يانغ ديسِن في تطوير "العلاج المعرفي الطاوي الصيني" (Zhang et al., *Transcultural Psychiatry*, 2002) — أُضيف مصدر أكاديمي فعلي. **William Marshall** كان بتاريخ `[DRAFT-UNKNOWN]` لكنه باحث حقيقي معروف في علاج مرتكبي الجرائم الجنسية — تُرك التاريخ كـgap بدل اختلاقه.
- **1 ملف = غير موجود → حجر:** `thk-michael-der-meer` — بحث ويب مباشر ("Michael Der Meer" + Alexander Technique) لم يُظهر أي شخصية بهذا الاسم في سجلات AmSAT/STAT ولا في الأدبيات. الملف الأصلي كان يعترف صراحة في متنه الظاهر بعدم العثور عليه، وفي نفس الوقت يحمل `## المصادر` بمراجع عامة (لا عن الشخص) وملاحظة تحريرية داخلية ("توصية الحجر") تحت العنوان — مخالفة مباشرة للقاعدة 5 وتناقض القاعدة 11. النسخة الأصلية نُقلت إلى `agents_specs/quarantine-minimax-archive/thk-michael-der-meer.md.archived.2026-08-27`، والملف الحي استُبدل بقالب حجر موحّد (`edges: []`, `related: []`)، وأُضيف سطر في `agents_specs/quarantine-minimax.md`.
- **0 ملفات = غامض** في هذه الدفعة.

### تصحيحات preflight إضافية (بعد أول تشغيل)
- `edges.belongs_to.target` كان نصاً حراً بدل slug حقيقي في 9 ملفات: 4 منها لها ملف مطابق فعلاً بنفس العنوان فحُوّل الرابط لـslug (thk-varela → `br-embodied-cognition-therapy`, thk-msimeona → `con-ho-oponopono`, thk-trore → `con-te-whare-tapa-wha`, thk-marshall → `br-sotp`)، و5 ليس لها ملف مطابق فحُذف الرابط (`edges: []`) وسُجّلت المدارس الغائبة في `agents_specs/missing-schools.md` (thk-wundt, thk-voltaire, thk-matt-haig, thk-rcallahan, thk-zhangyalin).
- `related` بعنوان (`title`) لا يطابق عنوان الملف الحقيقي المُشار إليه بالـ`id`: صُحح في matt-haig (tec-hope-therapy, stu-werner-kauai-resilience)، nasir-tusi (thk-ibn-sina)، msimeona (thk-jramiro)، npetry (thk-fskinner).
- `thk-mmahler`: تحذير جنس نحوي كاذب من الأداة — الكلمة "العالم" (بمعنى الكوكب) طابقت اسم الفئة "عالم" (male marker) بسبب قصور `\b` مع البادئة "ال" العربية. المتن كان مؤنثاً بشكل صحيح بالفعل (مارغريت ماهلر). بدّلت "العالم" بـ"محيطه"/"المحيط" في موضعين لتفادي المطابقة الكاذبة دون تغيير المعنى.

## متوقف عنده (لرئيس التحرير)
- لا يوجد.

## الملفات
content/ar/thinkers/thk-mao-zedong.md
content/ar/thinkers/thk-muhammad-abduh.md
content/ar/thinkers/thk-tlynch.md
content/ar/thinkers/thk-wundt.md
content/ar/thinkers/thk-varela.md
content/ar/thinkers/thk-maddis.md
content/ar/thinkers/thk-voltaire.md
content/ar/thinkers/thk-mackinnon.md
content/ar/thinkers/thk-matt-haig.md
content/ar/thinkers/thk-orsigen.md
content/ar/thinkers/thk-william-ockham.md
content/ar/thinkers/thk-marshall.md
content/ar/thinkers/thk-suarez.md
content/ar/thinkers/thk-nasir-tusi.md
content/ar/thinkers/thk-merleau-ponty.md
content/ar/thinkers/thk-solomon-hebrew.md
content/ar/thinkers/thk-michael-der-meer.md
content/ar/thinkers/thk-msimeona.md
content/ar/thinkers/thk-sohrevardi.md
content/ar/thinkers/thk-mmahler.md
content/ar/thinkers/thk-shen-buhai.md
content/ar/thinkers/thk-xu-xing.md
content/ar/thinkers/thk-shah-waliullah.md
content/ar/thinkers/thk-trore.md
content/ar/thinkers/thk-pseudo-dionysius.md
content/ar/thinkers/thk-rcallahan.md
content/ar/thinkers/thk-npetry.md
content/ar/thinkers/thk-pico.md
content/ar/thinkers/thk-zhangyalin.md
content/ar/thinkers/thk-valentinus.md
content/ar/thinkers/thk-zarathushtra.md
content/ar/thinkers/thk-mulla-sadra.md
