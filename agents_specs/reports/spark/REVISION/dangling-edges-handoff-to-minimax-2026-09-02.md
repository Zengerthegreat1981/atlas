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
