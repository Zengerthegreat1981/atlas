# Task 16.1 — أعمال غائبة (wrk-، دفعة 1: فرويد + سكينر + ساس + هيرمان + غوفمان)
الحالة: مكتمل | الملفات: 10

## العملية
إنشاء 10 ملفات عمل (`wrk-`) لأهم النصوص المؤسسة الغائبة عن الأطلس، عبر subagents مستقلين، preflight فوري لكل ملف، ثم توحيد ترقيم id يدوياً بعد التصادم.

## الملفات
- wrk-studies-hysteria-freud — دراسات في الهستيريا (فرويد وبروير، 1895)
- wrk-mourning-and-melancholia — الحداد والكآبة (فرويد، 1917)
- wrk-ego-and-id-freud — الأنا والهو (فرويد، 1923)
- wrk-civilization-discontents — قلق في الحضارة (فرويد، 1930)
- wrk-science-human-behavior-skinner — العلم والسلوك الإنساني (سكينر، 1953)
- wrk-walden-two-skinner — والدن اثنان (سكينر، 1948)
- wrk-beyond-freedom-dignity — ما وراء الحرية والكرامة (سكينر، 1971)
- wrk-myth-mental-illness-szasz — أسطورة المرض النفسي (ساس، 1961)
- wrk-trauma-recovery-herman — الصدمة والتعافي (هيرمان، 1992)
- wrk-asylums-goffman — المصحات (غوفمان، 1961)

## الأرقام
preflight_check.py على العشرة معاً: صفر مخالفات (بعد إصلاح تصادم ids: 6 ملفات كانت تحمل ids placeholder/متضاربة، أُعيد ترقيمها يدوياً WRK-2100–2106 مع التأكد أنها لا تتصادم مع أعلى id معتمد فعلي WRK-0810).

## قرارات اتخذتها
- **wrk-asylums-goffman**: لم يُربط بـ`thk-goffman` لأن ملفه في `content/ar/drafts/spark/thinkers/` لا يزال مسودة غير معتمدة (id placeholder) — سُجّل في gaps بدل الربط بملف غير معتمد.
- **wrk-science-human-behavior-skinner**: صُحح `active_end` لسكينر في هذا الملف نفسه (كان يخلق تعارضاً زائفاً مع سنوات لاحقة مذكورة بشكل مشروع مثل 1971).

## متوقف عنده (لرئيس التحرير)
- **إزدواج wrk- الثقيل المذكور في Task 16 لم يُحسم بعد** (being-nothingness × 3، ظاهراتية الإدراك × 3، بنية الثورات العلمية × 2) — هذا عمل تدقيق/دمج منفصل عن الإنشاء، يحتاج جلسة `task.py verify` مخصصة لعدّ الروابط الواردة قبل تحديد المعتمد. لم يُنفَّذ ضمن هذه الدفعة لأنه خارج نطاق "تاسك واحد = عملية واحدة".
- **wrk-goffman**: يحتاج ترقية `thk-goffman` (مسار Spark) للاعتماد قبل ربط أعمال غوفمان به.
- Task 16 لا يزال فيه: بارتليت *التذكّر*، هِب *تنظيم السلوك*، نايسر *علم النفس المعرفي*، دوبور *مجتمع الاستعراض*، كانغيلم *السوي والمرضي* (كانغيلم نفسه في مسار Spark) — و**كل حوارات `dia-`** (فرويد–فيرينتزي، كلاين–أنا فرويد، آيزنك 1952، كاندل 1998، بينكر–غولد، يونغ–باولي، أينشتاين–فرويد، الجابري–حنفي) — لم تُنشأ بعد، مُدرجة للدفعة التالية.

## الملفات
content/ar/drafts/minimax/works/{wrk-studies-hysteria-freud,wrk-mourning-and-melancholia,wrk-ego-and-id-freud,wrk-civilization-discontents,wrk-science-human-behavior-skinner,wrk-walden-two-skinner,wrk-beyond-freedom-dignity,wrk-myth-mental-illness-szasz,wrk-trauma-recovery-herman,wrk-asylums-goffman}.md
