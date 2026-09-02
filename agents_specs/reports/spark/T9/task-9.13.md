# Task 9.13
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 20

## الأرقام
evidence_level موجود: 0/20 → 20/20
جمل القائمة السوداء: عدد غير مؤكد (≥5 ملفات فيها بقايا) → 0/20
مشاكل related/edges ميكانيكية مكتشفة أثناء العمل (عناوين غير مطابقة، targets نصية بدل slugs، edges.developed_by خاطئة): ~10 حالات → 0

## أمر التحقق
python3 scripts/task.py verify spark 9.13
→
=== تحقق Task 9.13 (20 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 20
فيها الحقل evidence_level: 20 / 20

python3 scripts/preflight_check.py <20 ملفاً معاً>
→ ✅ 20 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- tec-systemic-nlp-tad-james.md, tec-time-line-therapy.md: evidence_level = "controversial" — تقنيات مشتقة من NLP، مصنّفة صراحة كمثيرة للجدل في SPARK.md.
- tec-tfp.md: evidence_level = "probably-efficacious"؛ ذُكرت دراستا Clarkin et al. 2007 وDoering et al. 2010 نصياً دون اختلاق ملف stu- مقابل (لا يوجد بالأطلس)، وثُبِّتت الفجوة في gaps بدل تركها ضمنية. أُصلح title مغلوط لـthk-fyeomans.
- tec-theraplay.md: evidence_level = "experimental" — القاعدة البحثية (RCT كبرى) غير موثقة بثقة كافية؛ لم تُخترع دراسة حاسمة، تُرك الحقل موثقاً كفجوة صريحة بدلاً من ذلك.
- tec-wet.md: evidence_level = "well-established" استناداً لتجربة عدم-دونية معشاة (Sloan, Marx, Lee & Resick 2018, JAMA Psychiatry) تُثبت تكافؤه مع PE وCPT؛ لا يوجد ملف stu- لهذه الدراسة فوُثّق كفجوة.
- tec-writing-therapy.md: evidence_level = "probably-efficacious" (لا well-established) بسبب صغر حجم الأثر في تحليل Frattaroli 2006؛ صُحح edges.developed_by ليشير فعلياً لـthk-jpennebaker بدل نص حر، وحُذف edges.belongs_to لأنه أشار لنص حر بلا ملف sch- مطابق (وُثّق كفجوة).
- عدة ملفات أخرى (9.13 دفعة كاملة): حُذفت جمل قائمة سوداء متبقية من محاولات سابقة، وصُححت عناوين related غير مطابقة لعناوين الملفات الفعلية، وحُوّلت targets نصية حرة في edges إلى slugs حقيقية أو حُذفت مع توثيق السبب في gaps.
- في كل الملفات: لم تُخترع أي دراسة/مبتكر/مدرسة غير موجودة فعلياً بالأطلس — كل رابط ناقص وُثّق في gaps باسم slug مقترح بدل اختراعه.

## متوقف عنده (لرئيس التحرير)
- لا شيء يحتاج تدخلاً بشرياً فورياً — كل الفجوات المتبقية موثقة داخل gaps كل ملف (دراسات حقيقية بلا ملف stu- مقابل، مثل Clarkin et al. 2007، Doering et al. 2010، Sloan et al. 2018، Pennebaker & Beall 1986، Frattaroli 2006).

## الملفات
content/ar/techniques/tec-structural-family-therapy.md
content/ar/techniques/tec-supportive-expressive.md
content/ar/techniques/tec-supportive-psychotherapy.md
content/ar/techniques/tec-systemic-nlp-tad-james.md
content/ar/techniques/tec-tawakkul-cognitive-reframing.md
content/ar/techniques/tec-tf-cbt.md
content/ar/techniques/tec-tfp.md
content/ar/techniques/tec-theraplay.md
content/ar/techniques/tec-time-line-therapy.md
content/ar/techniques/tec-tldp.md
content/ar/techniques/tec-transdiagnostic-cbt.md
content/ar/techniques/tec-trauma-discharge-somatic.md
content/ar/techniques/tec-tre.md
content/ar/techniques/tec-two-chair-dialogue-eft.md
content/ar/techniques/tec-unified-protocol.md
content/ar/techniques/tec-vaginal-dilator-therapy.md
content/ar/techniques/tec-vr-exposure-ptsd.md
content/ar/techniques/tec-vr-exposure.md
content/ar/techniques/tec-wet.md
content/ar/techniques/tec-writing-therapy.md
