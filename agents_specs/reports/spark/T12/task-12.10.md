# Task 12.10
الحالة: مكتمل
المسار: spark | العملية: metaphors (30/30 met- خالصة) | الملفات: 30

## الأرقام
جمل القائمة السوداء: → بعد 0
سقّالة gaps قالبية ظاهرة: → بعد 0
ملفات فيها `## المصادر`: → بعد 30/30

## أمر التحقق
python3 scripts/task.py verify spark 12.10
→
```
=== تحقق Task 12.10 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 30 / 30
```
preflight_check.py على الـ30 ملف: ✅ صفر مخالفات آلية.

## قرارات اتخذتها
- **met-quine-web-of-belief**، **met-rawls-original-position**، **met-rogers-growing-plant**: مصادر أصلية دقيقة (كواين 1951، رولز 1971، روجرز 1961)؛ تصحيح عناوين روابط.
- **met-russell-celestial-teapot** و**met-russell-inductivist-turkey**: توضيح أن راسل وثّق مثال الديك الرومي أصلاً بصيغة **دجاجة** (المشكلات الفلسفية 1912)، والصيغة الشائعة بالديك الرومي انتشرت عبر تلميذه أييه.
- **met-sartre-cafe-waiter-bad-faith** و**met-sartre-paperknife-essence**: الوجود والعدم 1943، محاضرة 1946.
- **met-satir-family-mobile**، **met-schema-modes-theatre**: Peoplemaking 1972، Schema Therapy 2003.
- **met-schopenhauer-porcupines**: تصحيح عنوان `thk-schopenhauer` ("أرتور" لا "آرثر").
- **met-self-as-actor-mask** و**met-self-as-mask-persona**: **تكرار محسوم بتمييز حقيقي** — الأول يركز حصراً على الأصل المسرحي الإغريقي وتطبيق غوفمان الاجتماعي (1956/1959)، والثاني حصراً على برسونا يونغ التحليلية (1921/1928)؛ كل ملف يحيل صراحة للآخر.
- **met-self-as-narrative**، **met-self-as-prison**، **met-self-as-project-sartre**: **عائلة "الذات كـ..." الثلاثية محسومة بتمييز واضح** — السرد (ريكور/ماكادامز)، السجن (نتيجة الهروب من الحرية)، المشروع (الحالة الأصيلة التي يخونها سوء الإيمان)؛ تصحيح `related` حرج في met-self-as-prison (con-bad-faith كان بعنوان خاطئ "سوء النية" بدل "سوء الإيمان" — كان سيُرفض فوراً حسب معيار القبول #6).
- **met-sensorimotor-somatic-container**: **تمييز صريح** بين حاوية أوغدن الجسدية-الفسيولوجية وحاوية بيون النفسية-العلائقية رغم تشابه الكلمة الإنجليزية.
- **met-ship-of-theseus**، **met-sisyphus-camus**: بلوتارخ (~القرن الأول م)، أسطورة سيزيف 1942.
- **met-skinner-box-metaphor**: تصحيح عنوان `thk-fskinner` ("بورهوس فريدريك" لا "بوريس فريدريك").
- **met-society-as-organism**: **طلب slug جديد مسجَّل رسمياً** (`sch-sociology` غير موجود) — استُخدم مؤقتاً `sch-social-psychology` مع توثيق الحل المؤقت في `gaps` وفي `agents_specs/requests-spark.md`.
- **met-spandrels-of-san-marco**: تصحيح عنوان رابط `dbt-evolutionary-psychology-adaptation-vs-spandrel`.
- **met-spinoza-blind-will-nature**، **met-stoic-dog-tied-to-cart**: الأخلاق 1677، مثال الكلب الرواقي (زينون/خريسيبوس، محفوظ عبر هيبوليتوس).
- **met-stream-of-consciousness-james**: مُيِّز صراحة عن `met-mind-as-water-stream` (من دفعة سابقة) — هذا الملف يقتصر على مصطلح جيمس التقني 1890، والآخر على التوظيف التأملي المعاصر؛ تصحيح عنوان `thk-james` ("وليم" لا "وليام").
- **met-sufi-reed-flute-masnavi**، **met-suhrawardi-light-shadow**: المثنوي 1258-1273، حكمة الإشراق 1186.
- **met-therapy-as-alchemy**: **إعادة كتابة كاملة** — الملف الأصلي كان معطوباً شكلياً وفيه خطأ واقعي (خلط تسميتي Citrinitas وRubedo)، وقائمة أمثلة أدبية غير موثقة (شوبنهاور/باختين/هاري بوتر) حُذفت لعدم وجود مصدر يربطها فعلياً.
- **met-therapy-as-archaeology**: **إعادة كتابة لتفادي تكرار met-freud-archaeology-psyche** — أُعيد توجيه الملف بالكامل للتوظيفات اللاحقة/الرافضة (EMDR، الوجودي، ACT/DBT الرافضان صراحة للتنقيب التاريخي)، مع إبقاء ملف فرويد الأصلي كما هو تماماً.
- **met-therapy-as-detective**: **إعادة كتابة** — الملف الأصلي كان حشواً غير موثق (أدلر "محقق اجتماعي"، لاينغ، قسم عن هولمز/بروفايلر) حُذف بالكامل واستُبدل بمصدر واحد موثق (بيك 1979، بادسكي 1993)؛ تصحيح `edges.belongs_to` من `sch-psychodynamic` (غير موجود) إلى `sch-cognitive-behavioral`.
- **met-therapy-as-dialogue**: **تصحيح خطأ عنوان جوهري** — العنوان والمتن الأصليان كانا عن "استعارة البهلوان الفكري" غير المرتبطة بمحتوى بوبر/أنا-أنت الفعلي في الملف؛ صُحح العنوان بالكامل ليطابق المحتوى.

## متوقف عنده (لرئيس التحرير)
- **met-russell-inductivist-turkey**: العلاقة الدقيقة بين صيغة الدجاجة الموثقة (1912) وصيغة الديك الرومي الشفهية تحتاج تتبعاً أدق لمصادرها الأولية.
- **met-satir-family-mobile**: تناقض إملائي قائم أصلاً في الكوربس بين "فرجينيا"/"فيرجينيا" ساتير عبر ملفات مختلفة — لم يُصحح خارج نطاق هذه الدفعة.
- **met-self-as-actor-mask/met-self-as-mask-persona**: القرار بإبقاء ملفين منفصلين (بدل الدمج) يستحق تأكيداً بشرياً.
- **met-sensorimotor-somatic-container**: التأريخ الدقيق لأسبقية استخدام أوغدن للمصطلح نسبة لبيون غير محسوم.
- **met-society-as-organism**: القرار المؤقت باستخدام `sch-social-psychology` بدل `sch-sociology` (غير الموجود) يحتاج تأكيداً أو إنشاء slug مخصص لاحقاً — مسجَّل في `agents_specs/requests-spark.md`.
- **met-sufi-reed-flute-masnavi**: دقة النقل الفارسي للبيت الافتتاحي تحتاج تدقيقاً بشرياً.
- **met-suhrawardi-light-shadow**: تاريخ إعدام السهروردي والنسبة للملك الظاهر تحتاج تأكيداً من مصدر أولي إضافي.
- **met-therapy-as-archaeology/detective/dialogue**: استشهادات دريدا (1972) وفوكو (1976) وبادسكي (1993) تحتاج تدقيقاً ببليوغرافياً دقيقاً (رقم الصفحة/الناشر) لم يتيسر التحقق منه الكامل.

## الملفات
content/ar/metaphors/met-quine-web-of-belief.md
content/ar/metaphors/met-rawls-original-position.md
content/ar/metaphors/met-rogers-growing-plant.md
content/ar/metaphors/met-russell-celestial-teapot.md
content/ar/metaphors/met-russell-inductivist-turkey.md
content/ar/metaphors/met-sartre-cafe-waiter-bad-faith.md
content/ar/metaphors/met-sartre-paperknife-essence.md
content/ar/metaphors/met-satir-family-mobile.md
content/ar/metaphors/met-schema-modes-theatre.md
content/ar/metaphors/met-schopenhauer-porcupines.md
content/ar/metaphors/met-self-as-actor-mask.md
content/ar/metaphors/met-self-as-mask-persona.md
content/ar/metaphors/met-self-as-narrative.md
content/ar/metaphors/met-self-as-prison.md
content/ar/metaphors/met-self-as-project-sartre.md
content/ar/metaphors/met-sensorimotor-somatic-container.md
content/ar/metaphors/met-ship-of-theseus.md
content/ar/metaphors/met-sisyphus-camus.md
content/ar/metaphors/met-skinner-box-metaphor.md
content/ar/metaphors/met-society-as-organism.md
content/ar/metaphors/met-spandrels-of-san-marco.md
content/ar/metaphors/met-spinoza-blind-will-nature.md
content/ar/metaphors/met-stoic-dog-tied-to-cart.md
content/ar/metaphors/met-stream-of-consciousness-james.md
content/ar/metaphors/met-sufi-reed-flute-masnavi.md
content/ar/metaphors/met-suhrawardi-light-shadow.md
content/ar/metaphors/met-therapy-as-alchemy.md
content/ar/metaphors/met-therapy-as-archaeology.md
content/ar/metaphors/met-therapy-as-detective.md
content/ar/metaphors/met-therapy-as-dialogue.md
