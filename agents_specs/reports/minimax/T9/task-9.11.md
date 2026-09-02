# Task 9.11
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط | الملفات: 30

## الأرقام
جمل القائمة السوداء: عشرات → 0
سقّالة ظاهرة (edges بنص حر بدل slug): 6 حالات مصححة → 0
تطابق id/title مكسور: 5+ حالات مصححة → 0
## المصادر موجود: 2/30 (باقي 28 يحتاجون Task 10 — خارج نطاق Task 9)

## أمر التحقق
`python3 scripts/task.py verify minimax 9.11` → صفر قائمة سوداء، صفر سقّالة، 2/30 مصادر (متوقع، Task 9 لا يشترط مصادر)
`python3 scripts/preflight_check.py` على الـ30 ملف → صفر مخالفات (بعد جولتين تصحيح)

## قرارات اتخذتها
- 10 subagents متوازية، كل واحد أخذ 3 ملفات، أعادوا بناء `related` من الصفر بعد فتح كل ملف مستهدف والتحقق من تطابق العنوان فعلياً.
- صححت بنفسي بعد preflight: `con-facilitated-communication-failure` (edges بنص حر "حركات مثيرة للجدل" → edges: []، سُجّل في missing-schools.md)، `con-family-sandplay` (حذف جملة قائمة سوداء من gaps)، `con-feminist-psychoanalysis` (title "جوليا ميتشِل"→"جوليت ميتشل"، حذف قسم اقتباسات فارغ)، `con-fitrah-aql-maturidi` (حذف قسم اقتباسات فارغ)، `con-five-love-languages`/`con-five-second-rule`/`con-five-stages-of-grief`/`con-fogg-behavior-model` (edges بنص حر → `sch-popular-psychology` الموجود فعلاً، ثلاثتهم الأخيرة `register: popular` فعلياً فينطبق).
- اكتُشفت مشكلة هوية جوهرية في `con-fear.md`: `thk-lazarus` و`thk-barrett` الحيّان في الأطلس شخصان مختلفان تماماً عمّن يُقصدان في المتن (ريتشارد لازاروس، ليزا فيلدمان باريت) — لم تُربط، سُجّلت في gaps وrequests-minimax.md لتنبيه رئيس التحرير.
- طلبات slug جديدة مسجّلة في `requests-minimax.md`: `thk-shen-dao`، `thk-batja-mesquita`، `wrk-` لكتاب الغزالي إحياء علوم الدين (شرح عجائب القلب)، `con-tazkiyat-al-nafs`.
- ملاحظة ازدواج (لم تُحسم، خارج نطاق Task 9): `wrk-levine-waking-the-tiger` مقابل `wrk-waking-the-tiger` لنفس الكتاب.

## متوقف عنده (لرئيس التحرير)
- `con-fear.md`: احتمال التباس thk-lazarus/thk-barrett بين شخصين مختلفين — يحتاج قرار بشري (هل يُنشأ slug صحيح منفصل؟).
- 28/30 ملفاً بلا `## المصادر` — هذا متوقع لأن Task 9 مخصص للروابط فقط؛ Task 10 سيتولى التعميق والمصادر.

## الملفات
- content/ar/concepts/con-externalizing-problem-reauthoring.md
- content/ar/concepts/con-fa-shu-shi-legalism.md
- content/ar/concepts/con-fa.md
- content/ar/concepts/con-facilitated-communication-failure.md
- content/ar/concepts/con-facticity.md
- content/ar/concepts/con-fallacy-of-affirming-consequent.md
- content/ar/concepts/con-fallacy-of-denying-antecedent.md
- content/ar/concepts/con-false-self-vs-true-self.md
- content/ar/concepts/con-falsificationism-popper.md
- content/ar/concepts/con-family-projection-process.md
- content/ar/concepts/con-family-resemblance-wittgenstein.md
- content/ar/concepts/con-family-sandplay.md
- content/ar/concepts/con-family-structure.md
- content/ar/concepts/con-fate-mohist.md
- content/ar/concepts/con-fear.md
- content/ar/concepts/con-felt-sense-tracking.md
- content/ar/concepts/con-felt-sense.md
- content/ar/concepts/con-feminine-principle.md
- content/ar/concepts/con-feminist-psychoanalysis.md
- content/ar/concepts/con-fitrah-aql-maturidi.md
- content/ar/concepts/con-fitrah-nafs-qalb-model.md
- content/ar/concepts/con-five-love-languages.md
- content/ar/concepts/con-five-principles-mutazila.md
- content/ar/concepts/con-five-second-rule.md
- content/ar/concepts/con-five-stages-of-grief.md
- content/ar/concepts/con-floating-man-argument-avicenna.md
- content/ar/concepts/con-flow-state-popular.md
- content/ar/concepts/con-flow.md
- content/ar/concepts/con-focal-practices.md
- content/ar/concepts/con-fogg-behavior-model.md
