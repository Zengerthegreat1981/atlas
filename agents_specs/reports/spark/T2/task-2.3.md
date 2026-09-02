# Task 2.3
الحالة: مكتمل
المسار: spark | العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 15

## الأرقام
- موثّق (كُتبت مسودة في drafts/spark/): 13 / 15
- غير موجود (سُجّل في quarantine-spark.md): 1 / 15 (thk-hhuber)
- غامض (تُرك بلا مسودة): 1 / 15 (thk-agarciag)
- **تحسين دائم في `scripts/preflight_check.py`**: استخراج `_prose_body_only()` من إصلاح دفعة 2.2 اتطبّق كمان على `check_gender_headers` — كان بيحسب كلمة `type: "مفكر"` الثابتة في الـfrontmatter كمؤشر ذكورة، فيولّد إنذارات كاذبة متكررة على أي شخصية أنثى (ظهر في 5 ملفات مختلفة في هذه الدفعة وحدها: bakewell, dbecker من الدفعة اللي فاتت + krug, cloemadanes, canderson هنا). بعد الإصلاح: صفر إنذارات كاذبة على الدفعة كاملة.
- هذه الدفعة نُفذت بـ**15 subagent متوازي، ملف واحد لكل subagent** (بدل 3 مجموعات من 5) بناءً على توجيه صريح من المستخدم لرفع التوازي.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-ellison.md content/ar/drafts/spark/thinkers/thk-krug.md content/ar/drafts/spark/thinkers/thk-cloemadanes.md content/ar/drafts/spark/thinkers/thk-brandchaft.md content/ar/drafts/spark/thinkers/thk-berman.md content/ar/drafts/spark/thinkers/thk-lperls.md content/ar/drafts/spark/thinkers/thk-lkohlberg.md content/ar/drafts/spark/thinkers/thk-diclemente.md content/ar/drafts/spark/thinkers/thk-engelhardt.md content/ar/drafts/spark/thinkers/thk-fizzotti.md content/ar/drafts/spark/thinkers/thk-jabra.md content/ar/drafts/spark/thinkers/thk-benedetti.md content/ar/drafts/spark/thinkers/thk-canderson.md
→ ✅ 13 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- `thk-ellison.md` (رالف إليسون) — موثّق، مؤلف *Invisible Man*؛ حذفت جملة القائمة السوداء من gaps.
- `thk-krug.md` (أورا كروغ) — موثّق، شريكة كيرك شنايدر بمعهد EHI.
- `thk-cloemadanes.md` (كلوي مادانيس) — موثّق؛ صُحح رابط belongs_to من نص حر إلى `tec-strategic-family-therapy`، وصُحح عنوان كتاب واحد وسنة ميلاد تقريبية.
- `thk-brandchaft.md` (برنارد براندشافت) — موثّق مع تصحيح سنة الوفاة من 2006 إلى 2010 (**بند حساس**، انظر تحت).
- `thk-berman.md` (إيمانويل بيرمان) — موثّق، محلل نفسي علائقي؛ تأكدت أنه شخص مختلف عن `thk-james-berman` المحجور سابقاً.
- `thk-lperls.md` (لورا بيرلز) — موثّق مع تصحيح جوهري: حذفت ادعاءً غير موثّق بتتلمذها على بوبر/تيليش/شيلر/هوسرل واستبدلته بأساتذتها الحقيقيين (فرتهايمر، غيلب، غولدشتاين).
- `thk-lkohlberg.md` (لورانس كولبرغ) — موثّق؛ صُحح رابط belongs_to من نص حر إلى `sch-developmental`.
- `thk-diclemente.md` (كارلو دي كليمنتي) — موثّق مع تصحيحات: الاسم "كارل"→"كارلو"، حذف ادعاء تأسيس أداة URICA غير موثّق، حذف كتاب مختلَق بالكامل (عنوان ومؤلفة مشاركة غير موجودين)، تقليص related لرابط واحد موثّق فقط.
- `thk-engelhardt.md` (ديتريش فون إنغلهاردت) — موثّق مع تصحيح تاريخ وفاة (كان الملف الأصلي يصفه كحيّ، توفي فعلياً 2024).
- `thk-fizzotti.md` (أوجينيو فيزوتي) — موثّق، تلميذ فرانكل المباشر؛ صُححت active_start/end بالكامل.
- `thk-jabra.md` (جبرا إبراهيم جبرا) — موثّق، مع تصحيح active_start من 1970 إلى 1948.
- `thk-benedetti.md` — موثّق **مع تصحيح هوية جوهري**: الملف الأصلي كان يخلط الاسم بين غايتانو بينيديتي (معالج الفصام الإيطالي-السويسري الحقيقي الذي وصفه المتن فعلياً) وفابريتسيو بينيديتي (باحث بلاسيبو مختلف تماماً) — المتن ثبت على الهوية الصحيحة (غايتانو).
- `thk-canderson.md` (كارول أندرسون) — موثّق؛ سُجّل طلب slug جديد لشريكيها بالتأليف (هوغارتي، رايس) في requests-spark.md بدل اختراع رابط لهما.
- `thk-agarciag.md` — غامض، تُرك كما هو، لا مسودة (لا يقين لا بالوجود ولا بالعدم).
- `thk-hhuber.md` — غير موجود، سُجّل في quarantine-spark.md؛ الملف نفسه كان يحمل تحذير تحقّق سابق.

## متوقف عنده (لرئيس التحرير)
- `thk-brandchaft.md`: تصحيح سنة الوفاة (2006→2010) اعتمد على معرفة النموذج الداخلية بلا مصدر رقمي فوري للتحقق — يستحق تأكيداً قبل الترقية.
- `thk-lkohlberg.md`: ظروف وفاته (انتحار مرجّح بعد معاناة مزمنة) موثقة في السير الرسمية لكن حُذفت من المتن لحساسيتها — قرار النشر من عدمه متروك لرئيس التحرير.
- `thk-diclemente.md`: تقليص شبكة related لرابط واحد فقط (بروتشاسكا) قرار متحفظ لغياب مصدر يوثق تعاوناً مباشراً مع مارلات — قابل للاسترجاع لو توفر مصدر.
- `thk-engelhardt.md`: رابط `belongs_to: sch-existential-therapy` الموروث من الملف الأصلي مشكوك فيه (الرجل مؤرخ طب لا معالج وجودي) لكن تصحيحه خارج نطاق Task 2 — يحتاج مراجعة تصنيف منفصلة.
- `thk-agarciag.md`: يحتاج بحث خارجي فعلي (مش معرفة داخلية) لحسم موثّق/غير موجود.
- `thk-hhuber.md`: يوصى بمراجعة الملف الأصلي المعتمد لسحبه أو نقله فعلياً — نفس التوصية المتكررة لملفات hhuber/klemann/aklinger/bischler المحجورة.

## الملفات
content/ar/thinkers/thk-ellison.md
content/ar/thinkers/thk-krug.md
content/ar/thinkers/thk-cloemadanes.md
content/ar/thinkers/thk-brandchaft.md
content/ar/thinkers/thk-berman.md
content/ar/thinkers/thk-lperls.md
content/ar/thinkers/thk-lkohlberg.md
content/ar/thinkers/thk-diclemente.md
content/ar/thinkers/thk-engelhardt.md
content/ar/thinkers/thk-agarciag.md
content/ar/thinkers/thk-fizzotti.md
content/ar/thinkers/thk-jabra.md
content/ar/thinkers/thk-benedetti.md
content/ar/thinkers/thk-canderson.md
content/ar/thinkers/thk-hhuber.md
