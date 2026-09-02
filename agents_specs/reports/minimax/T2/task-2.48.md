# Task 2.48
الحالة: مكتمل
العملية: تحقق وجود + حذف عبارات القائمة السوداء + تصحيح belongs_to حرة النص + مطابقة عناوين related | الملفات: 10

## الأرقام
مطابقات القائمة السوداء: قبل 16 → بعد 0
edges.belongs_to نص حر (غير slug): قبل 6 → بعد 0 (تحويل 2، حذف مع تسجيل في missing-schools.md 4)
عناوين related غير مطابقة لعنوان الملف المستهدف: قبل 6 → بعد 0
مخالفات آلية (preflight): قبل 2 → بعد 0

## أمر التحقق
`python3 scripts/preflight_check.py <10 ملفات>` → ✅ 10 ملف — صفر مخالفات آلية.
`grep` يدوي على الـ17 جملة من القائمة السوداء على الملفات العشرة → 0 تطابق.

## قرارات اتخذتها
- **thk-ukim** (ويتشول كيم، Uichol Kim): موثّق. حذفت edge `evolved_from` إلى `sch-cross-cultural-psychology` (غير موجود، سُجِّل في missing-schools.md). صححت title الرابط `sch-confucian-psychology` (كان "…الكونفوشيوسي" والصحيح "…الكونفوشي") في related والمتن. حذفت جملتي القائمة السوداء من gaps وأعدت صياغة الفجوات. أضفت `## المصادر` (3 مراجع حقيقية من أعمال كيم).
- **thk-marshall-rosenberg** (مؤسس التواصل اللاعنفي NVC): موثّق. تحققت أنه شخص مختلف تماماً عن `thk-srosenberg` (ستانلي روزنبرغ، العصب المبهم) — لا ازدواج. حوّلت `belongs_to` من نص حر "علم النفس الإنساني والتواصل اللاعنفي" إلى slug حقيقي `sch-humanistic` (تلميذ روجرز المباشر، امتداد تطبيقي للعلاج المتمركز حول الشخص). صححت عناوين `wrk-nonviolent-communication` و`con-nonviolent-communication` في related لتطابق الملفين الفعليين. حذفت قسم "اقتباسات مختارة" (كان يحوي الجملة السوداء فقط) واستبدلته بـ`## المصادر` (كتابان + سجل CNVC المؤسسي).
- **thk-stephen-covey**: موثّق. `belongs_to` كان نصاً حراً "علم النفس الشعبي والقيادة الشخصية" بلا ملف مدرسة مطابق → `edges: []` وسُجِّلت المدرسة الغائبة في missing-schools.md. صححت عنوان `con-seven-habits` في related. حذفت قسم الاقتباسات الفارغ، أضفت `## المصادر`.
- **thk-sasch** (سولومون آش): موثّق. صححت عنوان `stu-lewin-leadership-climates` في related ليطابق الملف الفعلي. صححت `active_end` من 1990 (تقاعده) إلى 1996 (وفاته، وهي السنة المذكورة صراحة في المتن) لحل مخالفة "سنة بعد active_end بلا تفسير". حذفت قسم الاقتباسات الفارغ، أضفت `## المصادر` (3 مراجع أكاديمية أصلية).
- **thk-nausiphanes** (نوسيفانس الطيبي): موثّق (شهادة أبيقور وديوجانس اللايرتيوس). حوّلت `belongs_to` من نص حر "المدرسة الذرية القديمة" إلى slug حقيقي `sch-atomism-greek`. صححت عنوان `con-atom-void` في related. أضفت `## المصادر` (ديوجانس اللايرتيوس، سكستوس إمبيريكوس، مرجع أكاديمي حديث).
- **thk-stanley-milgram** (تجربة الطاعة): موثّق. حذفت جملة القائمة السوداء من gaps وقسم الاقتباسات، أضفت `## المصادر` (3 مراجع أصلية بما فيها مقاله الأصلي 1963 وكتابه 1974).
- **thk-nedra-tawwab** (الحدود النفسية، معاصرة): موثّقة. `belongs_to` نص حر "علم النفس الشعبي والعلاقات الأسرية" بلا ملف مدرسة مطابق → `edges: []` وسُجِّلت في missing-schools.md. صححت عنواني `wrk-set-boundaries-find-peace` و`con-boundaries-psychological` في related. حذفت قسم الاقتباسات، أضفت `## المصادر`.
- **thk-susan-cain** (Quiet، الانطواء): موثّقة. `belongs_to` نص حر "علم النفس الشعبي والشخصية" بلا ملف مدرسة مطابق → `edges: []` وسُجِّلت في missing-schools.md. صححت عنوان `wrk-quiet-2012` في related (كان "الهدوء" والعنوان الفعلي "هادئ: قوة الانطوائيين…"). حذفت قسم الاقتباسات، أضفت `## المصادر`.
- **thk-rmwashburn** (مايكل واشبورن): موثّق. صححت عنوان `thk-eugenetaylor` في related (كان "يوجين تايلور" والصحيح "يوجين تيلور") وعنوان `sch-transpersonal`. حذفت جملة القائمة السوداء من gaps. أضفت `## المصادر` (كتاباه الرئيسيان).
- **thk-robert-greene**: موثّق. `belongs_to` نص حر "علم النفس الشعبي وسيكولوجيا القوة" بلا ملف مدرسة مطابق → `edges: []` وسُجِّلت في missing-schools.md. حذفت قسم الاقتباسات، أضفت `## المصادر`.

كل الملفات العشرة كانت لأشخاص حقيقيين موثّقين فعلاً — لا حالة "غير موجود" ولا "غامض" في هذه الدفعة، فلم يُحدَّث `quarantine-minimax.md`.

## متوقف عنده (لرئيس التحرير)
لا شيء. الدفعة اكتملت بالكامل.

## الملفات
- content/ar/thinkers/thk-ukim.md
- content/ar/thinkers/thk-marshall-rosenberg.md
- content/ar/thinkers/thk-stephen-covey.md
- content/ar/thinkers/thk-sasch.md
- content/ar/thinkers/thk-nausiphanes.md
- content/ar/thinkers/thk-stanley-milgram.md
- content/ar/thinkers/thk-nedra-tawwab.md
- content/ar/thinkers/thk-susan-cain.md
- content/ar/thinkers/thk-rmwashburn.md
- content/ar/thinkers/thk-robert-greene.md
