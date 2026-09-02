# Task 3.24
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-jrubin..thk-karl-popper (شامل يونغ وكانط وكافكا وكانمان وبوبر).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 3 / 35 (thk-judah-halevi، thk-jweir [ambiguous أصلاً]، thk-kapila)
- **أخطر اكتشاف: thk-jspence** — كان يخلط هوية جو سبنس الحقيقية (مصوّرة بريطانية 1934-1992، مؤسِّسة Photo-Therapy) بهوية جودي ويزر الكندية (لها ملف معتمد منفصل بالفعل thk-judy-weiser). أُعيد كتابة الملف بالكامل عن جو سبنس الحقيقية. **تصحيح هوية جذري يستحق مراجعة بشرية قبل الترقية.**
- **حجران جديدان**: thk-jtolman (لا أثر خارجي، المؤسِّسة الفعلية للعلاج الاجتماعي فعلياً لويز هولزمان)، وthk-jwpark (لا أثر لـ"جي-وو بارك" كمؤسِّس KAJA، المؤسِّس الفعلي بو-يونغ لي — الملف نفسه كان يحذّر مسبقاً).
- **ادعاء وفاة غير موثّق أُزيل: thk-jteasdale** — كان يجزم بوفاته 2023 بلا مصدر؛ كل المصادر المتاحة تصفه كمتقاعد لا يزال يدرّس. أُزيل الادعاء واستُبدل بـ"مستمر".
- **أثر تحريري داخلي تسرّب للنشر: thk-kardiner** — فقرة meta كانت موجَّهة لمحرر سابق تعترف بحذف اسم مختلَق ("روكفلر ويلبر")، لكنها بقيت منشورة في الملف المعتمد كأنها محتوى. حُذفت.
- **تصنيف تصحيحي عالي الحساسية**: thk-jsandoval (كان مصنَّفاً sch-psychoanalysis رغم أن كل المادة عن اليونغية النقدية → br-jungian)، thk-jseikkula (نص حر "الحوار المفتوح" → sch-systemic-family).
- **نمط تصنيف "تشكيلات الأسرة" تراكم مرة أخرى: thk-jschneider** — نفس فجوة bhellinger/gweber/hbeaumont المسجَّلة سابقاً، الآن 4 ملفات على الأقل بحاجة slug واحد.
- **نمط "gaps تدّعي حذف رابط لسه موجود" استمر**: thk-jseikkula (thk-maryolson موجود فعلياً كملف معتمد).
- **نمط false positive في فحص الجنس (حالة إضافية)**: thk-kalff (دورا كالف) — تُركت الصيغة المؤنثة الصحيحة عمداً.
- **فجوتا تصنيف تراكمتا بشدة هذه الدفعة**: "علم النفس الشعبي/الصحافة العلمية" (julie-smith + هاري/برادشو/بيترسون/ميرفي/رونسون من دفعات سابقة) و"الاقتصاد السلوكي" (kahneman، يحتمل تيفرسكي/ثالر لاحقاً).
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً (jrubin→sch-psychoanalysis، jshotter→br-social-constructionism، jsteiner، jwatson، jweakland [بلا slug]، jweiss، kafka، kalff→br-jungian، kanada). حالات كثيرة بلا slug مطابق (jsandoval→br-jungian [مُصحح]، judson-brewer [إدمان]، judy-weiser [تصوير علاجي]، julie-smith [شعبي]، kahneman [اقتصاد سلوكي]) أُفرغت مع تسجيل طلبات.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{jrubin,jsandler,jsandoval,jschneider,jseikkula,jshotter,jspence,jsteiner,jteasdale,judson-brewer,judy-weiser,julie-smith,jung,justin-martyr,jwatson,jweakland,jweir,jweiss,jweizenbaum,jwheelwright,jwiener,jwolpe,jwpark,jzinker,kafka,kahneman,kalff,kamalashila,kanada,kant,kardiner,karl-popper}.md
→ ✅ 31 ملف — مخالفة واحدة فقط (kalff) مؤكَّدة false positive وتُركت كما هي.
3 ملفات سليمة تماماً بلا مسودة، ملفان حُجرا (jtolman، jwpark).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title.

## متوقف عنده (لرئيس التحرير)
- **thk-jspence**: تصحيح هوية جذري (خلط كامل مع جودي ويزر) — أولوية عالية جداً للمراجعة قبل الترقية.
- **thk-jteasdale**: إزالة ادعاء وفاة غير موثّق (2023) — يستحق تأكيداً إضافياً إن أمكن.
- **thk-jtolman وthk-jwpark**: حجران جديدان جاهزان، يحتاجان قراراً بسحب الملفين المعتمدين أو استبدالهما بالشخص الصحيح (لويز هولزمان، بو-يونغ لي).
- **thk-kardiner**: أثر تحريري داخلي تسرّب للنشر — يستحق فحصاً هل نفس النمط موجود في ملفات أخرى.
- **thk-jsandoval وthk-jseikkula**: تصنيفات مُصحَّحة تصنيفياً لا فقط صياغياً — تستحق مراجعة قبل الترقية.
- **فجوة `sch-family-constellations`**: الآن 4 ملفات معتمدة تنتظرها.
- **فجوتا "علم نفس شعبي" و"اقتصاد سلوكي"**: تراكم حاد يستحق slugs موحَّدة.

## الملفات
content/ar/thinkers/thk-jrubin.md
content/ar/thinkers/thk-jsandler.md
content/ar/thinkers/thk-jsandoval.md
content/ar/thinkers/thk-jschneider.md
content/ar/thinkers/thk-jseikkula.md
content/ar/thinkers/thk-jshotter.md
content/ar/thinkers/thk-jspence.md
content/ar/thinkers/thk-jsteiner.md
content/ar/thinkers/thk-jteasdale.md
content/ar/thinkers/thk-jtolman.md
content/ar/thinkers/thk-judah-halevi.md
content/ar/thinkers/thk-judson-brewer.md
content/ar/thinkers/thk-judy-weiser.md
content/ar/thinkers/thk-julie-smith.md
content/ar/thinkers/thk-jung.md
content/ar/thinkers/thk-justin-martyr.md
content/ar/thinkers/thk-jwatson.md
content/ar/thinkers/thk-jweakland.md
content/ar/thinkers/thk-jweir.md
content/ar/thinkers/thk-jweiss.md
content/ar/thinkers/thk-jweizenbaum.md
content/ar/thinkers/thk-jwheelwright.md
content/ar/thinkers/thk-jwiener.md
content/ar/thinkers/thk-jwolpe.md
content/ar/thinkers/thk-jwpark.md
content/ar/thinkers/thk-jzinker.md
content/ar/thinkers/thk-kafka.md
content/ar/thinkers/thk-kahneman.md
content/ar/thinkers/thk-kalff.md
content/ar/thinkers/thk-kamalashila.md
content/ar/thinkers/thk-kanada.md
content/ar/thinkers/thk-kant.md
content/ar/thinkers/thk-kapila.md
content/ar/thinkers/thk-kardiner.md
content/ar/thinkers/thk-karl-popper.md
