# Task 11.1
الحالة: مكتمل
العملية: debates+critiques: تسمية الطرفين/الناقد بالاسم والنص والسنة (10 subagents متوازية) | الملفات: 30

## الأرقام
preflight_check.py: صفر مخالفات آلية (30/30 ملف)

## أمر التحقق
python3 scripts/task.py verify minimax 11.1 → صفر مخالفات

## أول دفعة في Task 11 — اكتشافات متعددة
ملفات كانت قالبية بالكامل (بلا ناقد/نص/سنة محددين، متن من القائمة السوداء) واتصلحت من الصفر:
- crt-adorno-horkheimer-dialectic-of-enlightenment، crt-al-azm-critique-of-religious-thought
- crt-al-jabri-critique-of-irfani-reason، crt-arkoun-critique-of-theological-dogmatism
- crt-baudrillard-critique-of-hyperreality، crt-beauvoir-critique-of-patriarchal-othering
- crt-butler-critique-of-heteronormativity، crt-cesaire-critique-of-colonialism

## ⚠️ اكتشاف خطير — مصادر ملفَّقة
في crt-commodification-critique.md كان فيه إسناد لمرجعين لا وجود لهما ("Felix Marton 2014"، "Ronen Berg 2014") — بحث فعلي لم يجد أي أثر لهما في أدبيات نقد علم النفس الإيجابي. اتصلحوا بأسماء المؤلفين الحقيقيين (Carl Cederström وAndré Spicer). **هذا نمط خطير يستحق فحصاً أوسع في باقي ملفات critiques/.**

## قرارات اتخذتها
- crt-critique-of-couples-therapy-effectiveness / crt-critique-of-couples-therapy: **تأكيد أنهما ليسا تكراراً** (فعالية إحصائية مقابل نقد فلسفي/سلطوي)
- edges نص حر بدل slug: اتصلح في crt-anti-psychiatry-critique، crt-baudrillard-critique-of-hyperreality، crt-critical-race-critique-psychology
- إصلاح إزاحة YAML مكسورة في عدة ملفات (crt-critique-of-burnout-industry، crt-critique-of-cbt، crt-critique-of-couples-therapy، crt-critique-of-evolutionary-psychology، crt-critique-of-existential-therapy، crt-critique-of-family-systems)
- باقي الملفات (crt-adhd-overdiagnosis، crt-adorno-jargon-authenticity-critique، crt-borderline-gendered-diagnosis، crt-critique-of-act-dbt، crt-critique-of-emdr، crt-critique-of-emotionally-focused، crt-critique-of-gestalt-therapy، crt-critique-of-gratitude-research، crt-critique-of-grit-research، crt-critique-of-humanistic-therapy، crt-critique-of-ifs-internal-family-systems، crt-critique-of-mindfulness): تصحيحات id/title، جمل قائمة سوداء، ## المصادر ناقصة.

صفر slugs مخترعة (باستثناء تصحيح المصادر الملفَّقة أعلاه بأسماء حقيقية).

## متوقف عنده (لرئيس التحرير)
- **⚠️ عاجل**: نمط مصادر ملفَّقة مكتشف — يستحق فحصاً منهجياً في باقي critiques/ (276 ملف)

## الملفات
crt-adhd-overdiagnosis, crt-adorno-horkheimer-dialectic-of-enlightenment, crt-adorno-jargon-authenticity-critique, crt-al-azm-critique-of-religious-thought, crt-al-jabri-critique-of-irfani-reason, crt-anti-psychiatry-critique, crt-arkoun-critique-of-theological-dogmatism, crt-baudrillard-critique-of-hyperreality, crt-beauvoir-critique-of-patriarchal-othering, crt-borderline-gendered-diagnosis, crt-butler-critique-of-heteronormativity, crt-cesaire-critique-of-colonialism, crt-commodification-critique, crt-critical-race-critique-psychology, crt-critique-of-act-dbt, crt-critique-of-burnout-industry, crt-critique-of-cbt, crt-critique-of-couples-therapy-effectiveness, crt-critique-of-couples-therapy, crt-critique-of-emdr, crt-critique-of-emotionally-focused, crt-critique-of-evolutionary-psychology, crt-critique-of-existential-therapy, crt-critique-of-family-systems, crt-critique-of-gestalt-therapy, crt-critique-of-gratitude-research, crt-critique-of-grit-research, crt-critique-of-humanistic-therapy, crt-critique-of-ifs-internal-family-systems, crt-critique-of-mindfulness
