# Task 15.2 — المفكرون الفلاسفة الغائبون (دفعة 2، نطاق m-z)
الحالة: مكتمل | الملفات: 9

## الملفات
- thk-metzinger (متسنغر) — منقول ومصحح من موقع قديم
- thk-whitehead (وايتهد) — منقول ومصحح
- thk-wallon (فالون) — منقول ومصحح
- thk-politzer (بوليتزر) — منقول ومصحح
- thk-dzahavi (دان زاهافي) — **جديد، لكن بحل ازدواج معقد** (راجع أدناه)
- thk-zeigarnik (بليوما زايغارنيك) — جديد
- thk-sechenov (إيفان سيتشينوف) — جديد
- thk-nikolas-rose (نيكولاس روز) — جديد
- thk-zeno-citium (زينون الرواقي) — جديد

## الأرقام
preflight_check.py على مجلدي schools/+thinkers/ التراكميين (73 ملفاً): صفر مخالفات، بعد إعادة ترقيم شاملة
لتصادمات id متكررة عبر كل الوكلاء المتوازيين.

## قرار حرج اتخذته: ازدواج ثلاثي لدان زاهافي
اكتُشف أثناء التنفيذ أن دان زاهافي موجود بالفعل **بثلاث هويات slug معلّقة مختلفة**:
1. `content/ar/drafts/thinkers/thk-zahavi.md` — مسودة كاملة موجودة من قبل (موقع مشترك قديم).
2. `content/ar/thinkers/thk-sgallagher.md` (ملف **معتمد**) يشير إليه بـ`id: "thk-dzahavi"` في `related`.
3. المهمة المطلوبة كانت تُنشئ `thk-dan-zahavi` كنسخة ثالثة.

**القرار:** اعتُمد `thk-dzahavi` (يطابق ما يتوقعه الملف المعتمد `thk-sgallagher.md`، وهو الأعلى حجية بين
الثلاثة لأنه منشور فعلاً). نُسخ محتوى المسودة الموجودة (`thk-zahavi.md`، لم يُلمس أو يُحذف) إلى
`content/ar/drafts/minimax/thinkers/thk-dzahavi.md` بعد تصحيح slug وid، وصُحح الرابط المقابل في
`thk-metzinger.md` (كان يشير لـ`thk-zahavi` القديم) ليشير لـ`thk-dzahavi` الجديد.

## قرارات أخرى
- استُبعد دوركهايم/بورديو/غوفمان/كانغيلم/كلاينمان/كيرماير/لورمان/إيان هاكينغ من هذه الدفعة لأنهم في نطاق
  حروف a-l (مسار Spark) — بعضهم موجود بالفعل في `content/ar/drafts/spark/thinkers/`.

## متوقف عنده (لرئيس التحرير)
- **thk-sgallagher.md (ملف معتمد) يحتوي رابطاً لـ`thk-dzahavi` كان معلَّقاً (broken) قبل هذه الدفعة —
  الآن أصبح صالحاً بعد ترقية `thk-dzahavi.md` من المسودة.** يُنصح بمراجعة وترقية `thk-dzahavi.md` بأولوية
  لإصلاح هذا الرابط في المحتوى المعتمد.
- Task 15 لا يزال فيه عشرات الأسماء غير المغطاة من نطاق m-z (نيد بلوك، بارناس، راتكليف، هامان، ياكوبي،
  شليغل، نوفاليس، همبولت، ستيغلر مكتمل، مارك فيشر يخص a-l، إلخ).

## الملفات
content/ar/drafts/minimax/thinkers/{thk-metzinger,thk-whitehead,thk-wallon,thk-politzer,thk-dzahavi,thk-zeigarnik,thk-sechenov,thk-nikolas-rose,thk-zeno-citium}.md
