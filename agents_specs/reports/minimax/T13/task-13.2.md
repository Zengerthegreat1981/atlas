# Task 13.2 — المدارس الغائبة (دفعة 2: فروع علم النفس الأكاديمي الغائبة كلياً)
الحالة: مكتمل | الملفات: 10

## العملية
إنشاء 10 ملفات مدرسة جديدة تغطي "أخطر ثقب في الأطلس" — فروع علم النفس الأكاديمي الغائبة كمدارس بالكامل — عبر subagents مستقلين، preflight فوري لكل ملف.

## الملفات
- sch-cognitive-psychology.md — علم النفس المعرفي/الثورة المعرفية
- sch-structuralism-wundt-titchener.md — البنيوية النفسية (فونت–تيتشنر، متمايزة عن sch-structuralism اللغوية)
- sch-functionalism-james-dewey.md — الوظيفية النفسية (جيمس–ديوي، متمايزة عن sch-functionalism فلسفة العقل)
- sch-psychometrics.md — القياس النفسي/علم النفس الفارقي
- sch-cognitive-neuroscience.md — علم الأعصاب المعرفي
- sch-evolutionary-psychology.md — علم النفس التطوري
- sch-philosophy-of-psychiatry.md — فلسفة الطب النفسي (فولفورد/بولتون/ثورنتون)
- sch-mad-studies.md — دراسات الجنون
- sch-hearing-voices.md — حركة سماع الأصوات (رومه/إيشر/لونغدن)
- sch-second-order-cybernetics.md — السيبرنطيقا من الدرجة الثانية والأوتوبويزيس

## الأرقام
preflight_check.py على الدفعتين معاً (20 ملفاً): صفر مخالفات آلية.

## قرارات اتخذتها
- عدة ملفات (cognitive-psychology, psychometrics, functionalism-james-dewey, philosophy-of-psychiatry,
  mad-studies, hearing-voices, evolutionary-psychology, second-order-cybernetics) لم تربط مؤسسيها
  الفعليين (ميلر، نيسر، غالتون، بينيه، سبيرمان، ثورستون، أنجل، كار، فولفورد، بولتون، ثورنتون،
  LeFrançois، Menzies، Reaume، Beresford، Romme، Escher، Longden، كوزميدس، توبي، فون فورستر، ماتورانا)
  لأن لا ملفات `thk-` لهم بعد — سُجّلوا في `gaps` وبعضهم في `agents_specs/requests-minimax.md`
  بدل اختراع slugs. **هذه قائمة تتقاطع مباشرة مع Task 15.**

## متوقف عنده (لرئيس التحرير)
- طلبات slug جديدة معلّقة في `agents_specs/requests-minimax.md` لمفكرين مؤسسين لهذه المدارس (راجع القسم أعلاه).

## الملفات
content/ar/drafts/minimax/schools/{sch-cognitive-psychology,sch-structuralism-wundt-titchener,sch-functionalism-james-dewey,sch-psychometrics,sch-cognitive-neuroscience,sch-evolutionary-psychology,sch-philosophy-of-psychiatry,sch-mad-studies,sch-hearing-voices,sch-second-order-cybernetics}.md
