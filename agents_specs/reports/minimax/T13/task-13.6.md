# Task 13.6 — المدارس الغائبة (دفعة 6)
الحالة: مكتمل | الملفات: 10

## الملفات
- sch-drama-therapy — علاج الدراما (متمايز عن sch-psychodrama)
- sch-mesmerism — الماسمرية/المغناطيسية الحيوانية
- sch-discernment-counseling — الإرشاد التمييزي (دوهرتي)
- sch-ddp — العلاج التفاعلي النمائي الثنائي
- sch-focusing — التركيز (جندلين)
- sch-socratic — المدرسة السقراطية + المدارس الصغرى (كلبية/قورينائية/ميغارية)
- sch-pre-socratic — تقاليد ما قبل سقراط (مظلة)
- sch-evolutionary-psychoanalysis — التحليل النفسي النمائي/التطوري
- sch-chinese-classical-philosophy — الفلسفة الصينية الكلاسيكية (مظلة)
- sch-elman-hypnosis — أسلوب إلمان في التنويم

## الأرقام
preflight_check.py على مجلدي schools/+thinkers/ التراكميين (93 ملفاً): صفر مخالفات، بعد إعادة ترقيم شاملة أخرى.

## نمط الجودة استمر في هذه الدفعة
كل الوكلاء العشرة راجعوا `agents_specs/missing-thinkers-final-resolution.md` قبل الربط، واستبعدوا بنجاح:
- **sch-discernment-counseling**: استبعد thk-andrew-schnack وthk-thomas-sells (LIKELY_FABRICATED).
- **sch-ddp**: استبعد 5 أسماء مختلقة، وميّز بدقة بين ملفات متشابهة الاسم لأشخاص مختلفين (thk-danbrown-ddp، thk-pfonel).
- **sch-focusing**: اكتشف **تناقضاً** بين تصنيف الحل (VERIFIED لـthk-bala-jaison) وحالة الملف الفعلي (محجور) — اختار عدم الربط بدل الثقة الأعمى بأي من المصدرين منفرداً.
- **sch-drama-therapy**: اكتشف روابط مكسورة في ملفين معتمدين (`thk-pslade`, `thk-rlandy-md` تشير لـ`con-` غير موجودة) — سُجِّلت في `requests-minimax.md`.
- **sch-pre-socratic**: اكتشف 3 ملفات مدارس فرعية (`sch-milesian`, `sch-pythagorean`, `sch-heraclitean`) بها `belongs_to` نصي حر بلا slug — هذا بالضبط النمط الذي يحدده Task 5، مفيد لتقاطع العمل بين التاسكات.
- **sch-mesmerism**: استبعد thk-hbernheim رغم أنه موثّق (VERIFIED) لأن ملف التسوية نفسه يوضح أن تصنيفه تحت "الماسمرية" غير دقيق (مدرسة نانسي مضادة نظرياً لفكرة السائل المغناطيسي العضوي).

## متوقف عنده (لرئيس التحرير)
- Task 13: 59 مدرسة منجزة عبر 6 دفعات من أصل ~147 مقدَّرة أصلاً.
- رابطان مكسوران في ملفات معتمدة (`thk-pslade`, `thk-rlandy-md`) — راجع `requests-minimax.md`.

## الملفات
content/ar/drafts/minimax/schools/{sch-drama-therapy,sch-mesmerism,sch-discernment-counseling,sch-ddp,sch-focusing,sch-socratic,sch-pre-socratic,sch-evolutionary-psychoanalysis,sch-chinese-classical-philosophy,sch-elman-hypnosis}.md
