# Task 1.8

الحالة: مكتمل
العملية: تراث/دفعة كانت "مُطالَبة" (claimed) بدون تنفيذ — أُعيد تنفيذها بالكامل تحت إشراف مباشر
(subagents بدفعات 5 ملفات + `preflight_check.py` فوري لكل دفعة) | الملفات: 25

## الأرقام
هوية موثّقة وأُصلحت بالكامل: 12/25 (منها 3 تصحيح هوية/جنس/مدرسة خاطئة: thk-mendelowitz →
Edward وليس Robert Mendelowitz، thk-plangevin → **خطأ جنس كامل** كان مكتوب "روني لانجفان" أنثى
والشخص الحقيقي Ronald Langevin رجل، thk-mlemlij → مدرسة خاطئة "يونغي" والصح تحليل نفسي فرويدي IPA)
هوية غير موثّقة (حُوّلت لملف غامض + حجر): 13/25

## أمر التحقق
`python3 scripts/preflight_check.py <كل ملفات الدفعة>` → ✅ صفر مخالفات آلية على كل الدفعات الفرعية
(4 مجموعات × 5 ملفات؛ أول مجموعة اتنفذت بـ`isolation: remote` كاختبار — النتيجة كانت في git
worktree منفصل واحتاجت دمج يدوي (`cp` + `build_slug_index.py`) قبل ما تُعتبر منفَّذة فعلياً، ده
درس مهم لأي تشغيل remote مستقبلي).

## قرارات اتخذتها
- نفس منهج 1.6: شخص غير موثّق ببحث فعلي → ملف غامض + حجر، مش سيرة واثقة.
- thk-nchomsky (نعوم تشومسكي): شخصية حقيقية كبرى كانت مكتوبة بشكل ناقص — أُعيد كتابتها بعمق يليق
  بحجمها الحقيقي (١٩٥٩ نقد Verbal Behavior، Syntactic Structures ١٩٥٧، الثورة المعرفية، عمله
  السياسي).
- thk-pyszczynski (Tom Pyszczynski، أحد مؤسسي Terror Management Theory): active_start كان خاطئاً
  (2003 بدل 1986) — اتصحح.

## متوقف عنده (لرئيس التحرير)
- thk-plangevin: الـslug (P-) ما بيطابقش الاسم الحقيقي (Ronald/R-) — ممكن legacy mismatch، يحتاج
  مراجعة لو نطلب slug جديد أو نسيبه.

## الملفات
thk-madelung, thk-marciamarx, thk-markrees, thk-markwelch, thk-marodriguez, thk-mbogenschutz,
thk-mendelowitz, thk-mhosokawa, thk-mking, thk-mlemlij, thk-mrothery, thk-myuen, thk-nchomsky,
thk-paul-thorne, thk-plangevin, thk-pridgway, thk-pyszczynski, thk-rcukierman, thk-rresnick,
thk-shih-chao-hwei, thk-smadigan, thk-stephen-talley, thk-tkora, thk-wmuller, thk-yihuazhu
