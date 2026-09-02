# روابط `edges` معلَّقة — فئة عيوب كانت غير مرئية، وتسليم لمسار MiniMax

التاريخ: 2026-09-02 · من مسار Spark

## الاكتشاف
`preflight_check.py` كان يتحقق من **شكل** هدف `edges` فقط (هل يشبه `sch-x`/`br-x`؟) ولا يتحقق من
**وجود** ملف له — بخلاف فحص `related` الذي يفتح الملف الهدف فعلاً. فأي slug مكتوب بشكل صحيح لكن
بلا ملف كان **يمرّ صامتاً**: رابط معلَّق يبدو سليماً في المصدر ولا يُحلّ في البناء.

**القياس عند الاكتشاف: 37 إشارة إلى 26 slug غير موجود** عبر المعتمد كله.

## ✅ أُصلح (فحص + أرض Spark)
1. **أُضيف تحقق الوجود** إلى `check_edges_target` عبر `_slug_exists_anywhere()`.
   المسودات **مقبولة** كهدف عن قصد: 106 ملفاً معتمداً يشاور على slugs في `drafts/` بانتظار
   الترقية، وهو اصطلاح قائم لا خطأ. المرفوض هو الاسم الذي لا ملف له **إطلاقاً**.
2. **أرض Spark: 7 → 0.** وكلها كانت أخطاء كتابة لأسماء موجودة فعلاً:

| الملف | كان | صار |
|---|---|---|
| `ctx-french-salons-encyclopedie` | `sch-european-enlightenment` | `sch-enlightenment` |
| `ctx-weimar-republic-hyperinflation-cabaret` | `sch-critical-theory` | `sch-frankfurt-school` |
| `ctx-nazi-totalitarianism-shoah` | `sch-critical-theory` | `sch-frankfurt-school` |
| `thk-leo-tolstoy` | `sch-existentialism-theistic` | `sch-existentialism-religious` |
| `exp-childhood-amnesia` | `sch-developmental-psychology` | `sch-developmental` |
| `wrk-symbolic-forms-cassirer` | `sch-philosophy-symbolic-forms` | `sch-neokantian` |
| `wrk-essay-on-man-cassirer` | `sch-philosophy-symbolic-forms` | `sch-neokantian` |

لاحظ أن ملف الوايمار كان يذكر «مدرسة فرانكفورت» في `related` بينما هدفه المعلَّق `sch-critical-theory`
— والاسم الحقيقي `sch-frankfurt-school` كان موجوداً طوال الوقت. وكاسيرر: استُخدم `sch-neokantian`
لأنه **ما يشاور عليه ملف كاسيرر نفسه**، فالعملان يتبعان مؤلفهما.

## ⛔ 30 إشارة باقية — كلها في أرض MiniMax، لم تُلمس
قاعدة SPARK.md رقم 1 تحصر Spark في `thk-a`→`thk-l` ومجلداته؛ الباقي لـMiniMax. **لم يُعدَّل أي منها.**

**أخطاء كتابة على الأرجح (الـslug الصحيح موجود بالفعل):**
| المعلَّق | المرشَّح الموجود فعلاً |
|---|---|
| `br-feldenkrais` ×2 | `sch-feldenkrais` («طريقة فيلدنكرايس») |
| `br-evolutionary-psychology` | `sch-evolutionary-psychology` |
| `br-dance-movement-therapy` ×2 | `sch-dance-movement-therapy` / `tec-dance-movement-therapy` |
| `br-vedic-psychology` | `sch-vedic-psychology` |
| `br-photo-therapy` ×2 | `tec-phototherapy` |
| `br-self-hypnosis` ×2 | `tec-self-hypnosis-progressive` |
| `br-aba` · `br-aba-advanced` | `br-aba-autism` |
| `paul-gilbert` | `thk-pgilbert` (بادئة `thk-` ناقصة) |
| `thk-jwberry` | `thk-john-berry` |

**⚠️ حالتان تبدوان تشابه أسماء لا خطأ كتابة — تحتاج انتباهاً:**
- `thk-cbartlett` (شيريل بارتليت، «الرؤية بعينين» مع الميكماك) — أقرب موجود `thk-bartlett` وهو
  **فريدريك بارتليت** عالم الذاكرة، **شخص آخر تماماً**. لا تربطهما.
- `thk-amarshall` (ألبرت مارشال، نفس السياق) — أقرب موجود `thk-marshall` وهو **ويليام مارشال**.
  **شخص آخر.**

**فجوات حقيقية (لا slug لها إطلاقاً):** `sch-critical-theory`(في ملفات MiniMax) ·
`sch-continental-philosophy` ×2 · `sch-psychodynamic-therapy` ×2 · `sch-metaphysics` ·
`sch-sociology` (مطلوب أصلاً في `requests-spark.md`) · `sch-hwabyung` ×2 ·
`br-feminist-psychology` ×2 · `br-body-mind-centering` ×2 · `br-british-existential` ·
`br-race-culturally-aware`.

**بعد إضافة تحقق الوجود، سيبلّغ الفحص عن هذه الثلاثين تلقائياً** لأي دفعة تشتغل على تلك الملفات.

---

# ملحق: توحيد حلّ الـslug في الفحص، وسلَّجان وهميان

## 🔧 `resolve_path_for_slug` كان يستثني المسودات — ولم يعد
كان فحص `related` يستثني `drafts/` تماماً، فكان **كل** رابط إلى مسودة يُبلَّغ كـ«id مش بيشاور
لأي ملف موجود». الحجم: تشغيل الفحص على `drafts/spark/` أعطى **244 مخالفة، منها 205 من هذا
النوع**؛ وفُحصت الـ108 معرّفات المتفرّدة يدوياً فكانت **108/108 موجودة فعلاً**. أي ضجّة كاملة
لا عيوب.

وكان في ذلك تناقض صريح: تحقق الوجود الذي أُضيف لـ`edges` اليوم **يقبل** المسودات (لأن الربط بها
اصطلاح قائم، 106 حالة)، بينما `related` **يرفضها**.

**التوحيد:** `resolve_path_for_slug` تقبل المسودات الآن، مع **تفضيل المعتمد** عند وجود نسختين
حتى تُقارَن العناوين بالنسخة المعتمدة.

**الأثر المقيس:** `content/ar/drafts/spark/` من **244 مخالفة → صفر** (252 ملفاً نظيفة تماماً).
وفي `thinkers` a–l: 280 → 278.

## سلَّجان وهميان أُزيلا
- **`thk-kristin-buss`** كان يشاور على `thk-mark-santross` (لا ملف له) — **وملفه نفسه يحمل في
  `gaps` سطراً يقول إن الرابط أُزيل**! أي أن دفعة سابقة كتبت السجل ولم تنفّذ الحذف. أُزيل السطر
  فعلياً ليطابق الواقع سجلَّه.
- **`thk-lcozolino`** كان يشاور على `thk-rkeller` (لا ملف له، ولا ذكر في المتن) — أُزيل وسُجِّل بصدق.

**نمط يستحق الانتباه:** «مسجَّل ولم يُنفَّذ». ظهر هنا، وظهر في نفس الجلسة في موجة `slug-fix`
(تصحيح اسم يُطبَّق على ملف صاحبه ولا يُعمَّم على الروابط الوارِدة). **لا يكفي أن يقول التقرير إن
شيئاً أُصلح — لازم التحقق من القرص.** وهذا بالضبط ما فرضته مراجعة اليوم على نفسها.

## الحصيلة النهائية لأرض Spark
| | بداية الجلسة | الآن |
|---|---|---|
| `thinkers` a–l | 2,672 مخالفة / 1,082 ملف | **276 / 195** |
| باقي مجلدات Spark | 157 | **106** |
| `drafts/spark/` | 244 (منها 205 كاذبة) | **صفر** |

**والـ276 الباقية كلها غير قابلة للإصلاح الآلي بحكم طبيعتها:**
198 تضارب عنوان (81% اختصارات مشروعة — **قرار اصطلاح للمحرر**) · 77 جنس نحوي (**صنف إيجابيات
كاذبة معروف**، يحتاج عيناً بشرية) · 1 اصطلاح «(كمظلة)» مقصود.
**أي إن العيوب الآلية القابلة للإصلاح في مفكري Spark = صفر.**
