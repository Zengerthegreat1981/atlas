# Task 9.30
الحالة: مكتمل
العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py: صفر مخالفات آلية (30/30 ملف)
جمل القائمة السوداء متبقية: 0
سقّالة ظاهرة متبقية: 0

## أمر التحقق
python3 scripts/task.py verify minimax 9.30 → جمل القائمة السوداء 0، سقّالة ظاهرة 0

## ⚠️ اكتشاف مهم — أولوية قصوى لرئيس التحرير
**تعارض ترميز Unicode حقيقي أثّر على preflight_check.py**: ملف `con-epoché-phenomenological-reduction.md` كان اسمه على القرص مكتوباً بترميز **NFD** (e + علامة نبر مركّبة U+0301) بينما الروابط الواردة إليه من ملفات أخرى (con-epoche-phenomenological-reduction، con-epoche-suspension) كانت بترميز **NFC** (é كحرف واحد U+00E9) — نفس الشكل المرئي، بايتات مختلفة تماماً. تم تصحيح الـid في الملفين المُشيرين ليطابقا ترميز اسم الملف الفعلي على القرص. **هذا ليس تكراراً تحريرياً عادياً — قد يكون نفس الملف بترميزين مختلفين تسبب في انقسام صامت.** يحتاج فحصاً عاجلاً: هل `con-epoche-phenomenological-reduction.md` و`con-epoché-phenomenological-reduction.md` محتواهما متطابق فعلياً (نسخة مكررة بالخطأ بترميزين)، أم ملفان متمايزان فعلاً؟ الملف الثالث `con-epoche-suspension.md` (عن بيرون الشكاك) موضوعه مختلف فعلياً (نظرية الشك اليوناني القديم مقابل الفينومينولوجيا الهوسرلية) فهو غالباً ليس تكراراً.

سُجّل بأولوية قصوى في `agents_specs/requests-minimax.md`.

## قرارات اتخذتها
- con-enmeshment-disengagement: طلب slug (wrk- لكتابي مينوشين 1974/1978)
- con-eternal-recurrence-nietzsche/con-eternal-return: إعادة بناء، ازدواج مسجّل بلا دمج
- con-ethics-of-care-concept: thk-gilligan، thk-nel-noddings مضافان صراحة، ازدواج مع con-care-ethics مسجّل
- con-evidence-based-practice: توسيع (kernberg، foucault، heidegger، merleau-ponty، said)
- con-existence-existentialism: wrk-sartre-being-and-nothingness، con-dasein-being-there، con-anguish-angst
- con-existential-risk: إعادة بناء (bostrom، sch-transhumanism، Superintelligence 2014)
- con-experiential-avoidance: con-relational-frame-theory، ملاحظة صحيحة (thk-lazarus شخص مختلف عن Folkman/Lazarus النفسي)
- con-expressivism-quasi-realism-blackburn / con-extended-mind-clark-chalmers: كانا جملة واحدة — أُعيد كتابة المتن بالكامل
- con-exposure-hierarchy: con-systematic-desensitization، con-reciprocal-inhibition
- باقي الملفات (con-enactivism-embodied-cognition، con-endurantism-vs-perdurantism، con-entitlement-theory-nozick، con-epiphenomenalism-mind، con-episteme-foucault، con-epistemic-injustice-fricker-concept، con-epistemological-anarchism، con-esse-est-percipi، con-ethics، con-eudaimonia-wellbeing، con-evolutionary-psychoanalysis، con-existential-guilt-ontological، con-existential-vacuum، con-experiential-focusing، con-explanatory-gap-levine، con-exposure-habituation): إضافات/تصحيحات صغيرة أو تحقق فقط.

صفر slugs مخترعة عبر الدفعة كلها.

## متوقف عنده (لرئيس التحرير)
- **⚠️ عاجل**: تعارض ترميز Unicode con-epoché-phenomenological-reduction — احتمال ازدواج ملف فعلي بترميزين مختلفين، وليس تكراراً تحريرياً عادياً (راجع القسم أعلاه)
- con-eternal-recurrence-nietzsche / con-eternal-return: ازدواج محتمل
- con-ethics-of-care-concept / con-care-ethics: ازدواج محتمل

## الملفات
con-enactivism-embodied-cognition, con-endurantism-vs-perdurantism, con-enmeshment-disengagement, con-entitlement-theory-nozick, con-epiphenomenalism-mind, con-episteme-foucault, con-epistemic-injustice-fricker-concept, con-epistemological-anarchism, con-epoche-phenomenological-reduction, con-epoche-suspension, con-epoché-phenomenological-reduction, con-esse-est-percipi, con-eternal-recurrence-nietzsche, con-eternal-return, con-ethics-of-care-concept, con-ethics, con-eudaimonia-wellbeing, con-evidence-based-practice, con-evolutionary-psychoanalysis, con-existence-existentialism, con-existential-guilt-ontological, con-existential-risk, con-existential-vacuum, con-experiential-avoidance, con-experiential-focusing, con-explanatory-gap-levine, con-exposure-habituation, con-exposure-hierarchy, con-expressivism-quasi-realism-blackburn, con-extended-mind-clark-chalmers
