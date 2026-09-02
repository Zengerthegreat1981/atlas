# Task 13.9 — المدارس الغائبة (دفعة 9)
الحالة: مكتمل | الملفات: 13 (95/~147 مدرسة إجمالاً الآن)

## العملية
10 subagents، كل واحد مرشح من `missing-schools.md`؛ بعضهم أنتج ملفات متعددة (فلسفة الرياضيات انقسمت لـ4 ملفات مستقلة بنفس منطق فلسفة العلم في 13.8). تحقق شخصي نهائي مني بـpreflight + grep قائمة سوداء.

## الملفات (13)
- sch-logicism-math / sch-formalism-math / sch-intuitionism-math / sch-constructivism-math — أربعة مذاهب فلسفة الرياضيات (فريغه-راسل، هيلبرت، براور، بيشوب) تحت مظلة sch-phil-mathematics
- sch-shaiva-traditions — مظلة الشايفية (كشميرية، سيدهانتا، شاكتية-تانترا)
- sch-islamic-esotericism — الباطنية الإسلامية (إسماعيلية، إخوان الصفا، إشراقية) — صحَّحت انتماء خاطئاً كانت الثلاثة تُنسب فيه لـsch-islamic-peripatetic
- sch-gottman-method — طريقة غوتمان الزوجية (جون/جولي غوتمان، روبرت ليفنسون)
- sch-filipino-philosophy — مظلة الفلسفة الفلبينية (Sikolohiyang Pilipino)
- sch-protestant-reformation — الإصلاح البروتستانتي (1517-1648)
- sch-japanese-ethics-umbrella — مظلة الفلسفة الأخلاقية اليابانية (شينغاكو، شنتو فلسفي، كوغاكو)
- sch-astika-umbrella — مظلة المدارس الأرثوذكسية الست الهندوسية (آستيكا)
- sch-shinto-umbrella — مظلة الشنتو (شعبي مبكر، ريوبي، فلسفي)
- sch-modern-japanese-philosophy — مظلة الفلسفة اليابانية المعاصرة (كيوتو وما بعدها، بعد 1868)

## ⚠️ اكتشاف مهم — فجوة توثيق حرجة
**لا يوجد ملف `thk-` مستقل لا لمارتن لوثر ولا لجان كالفن** في الأطلس بالكامل رغم كونهما أهم شخصيتين في الإصلاح البروتستانتي (الوحيد الموجود هو `thk-martin-luther-king` لشخص مختلف تماماً). سُجِّل طلب slug عاجل بدل الاختراع.

## قرارات جودة بارزة
- sch-islamic-esotericism: صُحح انتماء ثلاثة مدارس (sch-ismaili، sch-ikhwan-safa، sch-ishraqiyya) كانت مُصنَّفة خطأً كلها تحت sch-islamic-peripatetic (خلط بين الفلسفة المشائية والباطنية).
- sch-astika-umbrella: صُححت 5 عناوين related غير مطابقة بعد أول preflight فاشل، أُعيد التشغيل بنجاح.
- sch-filipino-philosophy: لم تُخترع slugs لريزال/مابيني/ميركادو لعدم وجود ملفات thk- لهم — سُجِّلت الفجوة بدل الاختراع.

## ⚠️ ملاحظة فنية — قيد معروف في preflight_check.py
الروابط `related` المتبادلة بين ملفات drafts/ الشقيقة (مثال: sch-popperianism ↔ sch-kuhnianism، أو رباعية فلسفة الرياضيات فيما بينها) **لا يمكن أن يحلّها preflight_check.py آلياً** طالما الملفان في drafts/ ولم يُرقَّيا بعد لـcontent/ar/schools/ المعتمد — هذا سلوك متوقع للأداة (تحقّقت شخصياً بعد إعادة بناء فهرس الـslugs، والمخالفات باقية لنفس السبب البنيوي، وليست خللاً حقيقياً). المحتوى نفسه صحيح والعناوين متطابقة فعلياً بين الملفات المتقابلة — تحققتُ يدوياً.
تحقق قائمة سوداء يدوي مباشر (grep) على الـ13 ملفاً الجديدة: **صفر تطابق**.

صفر slugs مخترعة، صفر مصادر ملفَّقة.

## متوقف عنده (لرئيس التحرير)
- **⚠️ عاجل**: لا ملف thk- لمارتن لوثر ولا جان كالفن.
- روابط drafts-إلى-drafts المتبادلة (فلسفة العلم × فلسفة الرياضيات) ستُحلّ تلقائياً عند ترقية الملفات لـcontent/ar/schools/.
- طلبات slug جديدة متعددة مسجَّلة عبر الملفات (تفيرسكي، صنستاين من 13.8؛ ريزال/مابيني من هذه الدفعة).

## الملفات (مسار كامل)
content/ar/drafts/minimax/schools/sch-logicism-math.md, sch-formalism-math.md, sch-intuitionism-math.md, sch-constructivism-math.md, sch-shaiva-traditions.md, sch-islamic-esotericism.md, sch-gottman-method.md, sch-filipino-philosophy.md, sch-protestant-reformation.md, sch-japanese-ethics-umbrella.md, sch-astika-umbrella.md, sch-shinto-umbrella.md, sch-modern-japanese-philosophy.md
