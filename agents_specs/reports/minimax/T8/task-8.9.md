# Task 8.9
الحالة: مكتمل
العملية: schools: ## المصادر + cultural_origin (سويب يدوي مباشر، مش عبر `task.py get`) | الملفات: 40

## الأرقام
## المصادر موجود: قبل 0/40 → بعد 40/40
cultural_origin موجود: قبل 0/40 → بعد 40/40
باقي مجلد schools/ بلا ## المصادر: 90 → 50

## أمر التحقق
`python3 scripts/preflight_check.py <40 ملفاً>` → **صفر مخالفات من أول تجميع** (أنظف دفعة لحد الآن — صفر تصحيحات إضافية لازمة في 8 من 10 مجموعات)

## قرارات اتخذتها
- نمط متكرر واضح الآن: ملفات فيها "## المؤلفات المرجعية" (نصوص أولية تراثية للمدرسة نفسها) تُترك دائماً بجانب "## المصادر" الجديد (مراجع أكاديمية ثانوية) لأنهما مختلفا الغرض والمضمون فعلياً — طُبّق هذا القرار باتساق في: sch-salafism-modern، sch-realism-medieval، sch-scholasticism، sch-shiraz، sch-scotism، sch-scottish-common-sense، sch-second-scholasticism.
- توحيد/إعادة تسمية أقسام مصادر موجودة مسبقاً بنفس الغرض: sch-psychoanalysis (## المرجع الموصى)، sch-social-contract (## المؤلفات المرجعية — هنا كان فعلاً نفس الغرض)، sch-rebt (## أهم المرجعيات الأكاديمية)، sch-sensorimotor-psychotherapy (## المطبوعات التأسيسية الرئيسية).
- ملفات اكتفت بمصدرين فقط عمداً: `sch-shingaku.md` — مرجعان أكاديميان قياسيان مؤكدان، لا اختراع لمصدر ثالث.
- **صفر edges بنص حر أو تعارضات id/title في كامل هذه الدفعة** — أول دفعة نظيفة تماماً من أول تجميع بدون أي تصحيح preflight إضافي.

## متوقف عنده (لرئيس التحرير)
- لا شيء جديد.

## الملفات
content/ar/schools/sch-psychoanalysis.md
content/ar/schools/sch-pure-land.md
content/ar/schools/sch-pyrrhonism.md
content/ar/schools/sch-social-contract.md
content/ar/schools/sch-pythagorean.md
content/ar/schools/sch-queer-theory.md
content/ar/schools/sch-quinean-naturalism.md
content/ar/schools/sch-radical-democracy.md
content/ar/schools/sch-rangaku.md
content/ar/schools/sch-rawlsianism.md
content/ar/schools/sch-realism-medieval.md
content/ar/schools/sch-rebt.md
content/ar/schools/sch-renaissance-humanism.md
content/ar/schools/sch-renaissance-naturalism.md
content/ar/schools/sch-renaissance-neoplatonism.md
content/ar/schools/sch-romanticism.md
content/ar/schools/sch-sage-philosophy.md
content/ar/schools/sch-sakya.md
content/ar/schools/sch-salafism-modern.md
content/ar/schools/sch-samkhya.md
content/ar/schools/sch-sanlun.md
content/ar/schools/sch-schelling.md
content/ar/schools/sch-scholasticism.md
content/ar/schools/sch-scientific-realism.md
content/ar/schools/sch-scotism.md
content/ar/schools/sch-scottish-common-sense.md
content/ar/schools/sch-second-scholasticism.md
content/ar/schools/sch-sensorimotor-psychotherapy.md
content/ar/schools/sch-seon.md
content/ar/schools/sch-shaiva-siddhanta.md
content/ar/schools/sch-shakta-tantra.md
content/ar/schools/sch-shingaku.md
content/ar/schools/sch-shingon.md
content/ar/schools/sch-shinto-philosophical.md
content/ar/schools/sch-shiraz.md
content/ar/schools/sch-shramana.md
content/ar/schools/sch-shuddhadvaita.md
content/ar/schools/sch-sikh-philosophy.md
content/ar/schools/sch-sikolohiyang-pilipino.md
content/ar/schools/sch-silhak.md
