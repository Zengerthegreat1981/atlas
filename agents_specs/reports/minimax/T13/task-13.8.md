# Task 13.8 — المدارس الغائبة (دفعة 8)
الحالة: مكتمل | الملفات: 13 (82/~147 مدرسة إجمالاً الآن)

## العملية
10 subagents مكلَّفين بـ10 مرشحين من `missing-schools.md`؛ اثنان قرَّرا بحق عدم إنشاء ملفات (تكرار فعلي لمحتوى موجود)، والباقي أنتج 13 ملفاً (بعضهم انقسم لعدة ملفات فرعية مستقلة بدل مظلة مصطنعة واحدة).

## ✅ قرارات "عدم إنشاء" صحيحة — اكتشاف تكرار محتوى
- **الجشطالت الجسدي (Naranjo)**: مُوثَّق بالفعل كتيار فرعي داخل `sch-gestalt-therapy.md` — لم يُنشأ ملف مكرر. اكتُشفت مشكلة حقيقية بدلاً من ذلك: `thk-mparlett` و`thk-rfrank` (الأعضاء اليتامى) لهما `edges: []` فارغة رغم أن `thk-gnaranjo` (نفس التيار) مربوط بـ`belongs_to: sch-gestalt-therapy` — **يحتاج إصلاح ربط خارج نطاق Task 13** (تعديل ملفات content/ar المعتمدة، ليس drafts).
- **علم النفس الإيجابي العابر للثقافات / العلاج بالفضائل / علم نفس الرفاهية**: الثلاثة مُوثَّقون بالفعل كتيارات فرعية صريحة داخل `sch-positive-psychology.md` — لم تُنشأ ملفات مكررة.

## الملفات الجديدة (13)
- sch-daoism-umbrella — مظلة الداووية (فلسفية + دينية)
- sch-rolfing — الرولفينغ والتكامل الهيكلي (إيدا رولف)
- sch-prep-couples — برنامج PREP (ماركمن/ستانلي/بلومبرغ/رودس) — دمج سجلَّين مكرَّرين في missing-schools.md
- sch-gestalt-psychology-berlin — علم النفس الجشطالتي الإدراكي (مدرسة برلين، 1912) — متمايز صراحة عن sch-gestalt-therapy
- sch-open-dialogue — الحوار المفتوح (سيكولا/أولسون، فنلندا)
- sch-behavioral-economics — الاقتصاد السلوكي (كانمان/تفيرسكي/ثالر)
- sch-logical-behaviorism — السلوكية المنطقية (رايل/مالكولم)
- sch-mind-brain-identity-theory — نظرية الهوية العقل-الدماغ (بليس/سمارت)
- sch-eliminative-materialism — المادية الإقصائية (آل تشيرشلاند)
- sch-popperianism / sch-kuhnianism / sch-lakatosianism / sch-feyerabendianism — أربعة مذاهب فلسفة العلم (بوبر/كون/لاكاتوش/فايرأباند)، فُصلت كملفات مستقلة بدل مظلة مصطنعة لأن كل مذهب له مؤسس وحجج مستقلة تماماً

## قرارات جودة بارزة
- ثلاثية فلسفة العلم الأربعة تُرتبط ببعضها عبر related — preflight الجزئي أظهر مخالفات كاذبة (drafts لا تُفهرَس في الفحص الجزئي)؛ preflight الكامل (`--glob`) أكَّد صفر مخالفات فعلياً — تحقَّقتُ بنفسي.
- sch-behavioral-economics: حُذف رابط `evolved_from: sch-cognitive-psychology` لأنه لا يزال draft غير منشور — سُجِّل في gaps بدل الربط المكسور.
- sch-mind-brain-identity-theory: لا ملف thk- لـPlace أو Smart (المؤسسَين الفعليَّين) — ذُكرا بالاسم في المتن فقط، الفجوة مسجَّلة.

صفر slugs مخترعة، صفر مصادر ملفَّقة.

## متوقف عنده (لرئيس التحرير)
- **⚠️ إصلاح ربط مطلوب** (خارج drafts/): `thk-mparlett.md` و`thk-rfrank.md` يحتاجان `edges: belongs_to → sch-gestalt-therapy` (نفس نمط thk-gnaranjo) — هذا تعديل على ملفات معتمدة، خارج صلاحية Task 13 الحالية.
- تفيرسكي وصنستاين (شريكا تأسيس فعليان للاقتصاد السلوكي) بلا ملف thk- — طلب مسجَّل.

## الملفات (مسار كامل)
content/ar/drafts/minimax/schools/sch-daoism-umbrella.md, sch-rolfing.md, sch-prep-couples.md, sch-gestalt-psychology-berlin.md, sch-open-dialogue.md, sch-behavioral-economics.md, sch-logical-behaviorism.md, sch-mind-brain-identity-theory.md, sch-eliminative-materialism.md, sch-popperianism.md, sch-kuhnianism.md, sch-lakatosianism.md, sch-feyerabendianism.md
