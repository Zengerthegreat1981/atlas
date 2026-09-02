# Task 12.6
الحالة: مكتمل
المسار: spark | العملية: contexts/experiences/metaphors: تصنيف الصوت السردي + التعميق (أول دفعة تضم met-) | الملفات: 30

## الأرقام
جمل القائمة السوداء: → بعد 0
سقّالة gaps قالبية ظاهرة: → بعد 0
ملفات فيها `## المصادر`: بعد التوحيد اليدوي لـ9 ملفات (exp-wittgenstein + 8 met-) → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 12.6
→
```
=== تحقق Task 12.6 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 30 / 30
```
preflight_check.py على الـ30 ملف: ✅ صفر مخالفات آلية.

## قرارات اتخذتها
- **exp-schopenhauer-frankfurt-isolation**: ضمير المتكلم؛ عزلة فرانكفورت 1833-1860.
- **exp-seneca-forced-suicide-nero**: أمر نيرون بالانتحار عام 65م، رواية تاسيتوس (Annales XV.60-64).
- **exp-shame-vs-guilt-existential**: **تصحيح واقعي جوهري** — النص الأصلي نسب خطأً كتاب "The Anatomy of Human Destructiveness" (1973، لإريك فروم فعلياً) والتمييز الإكلينيكي خزي/ذنب لحنه أرندت؛ صُحح للمصدر الصحيح: هيلين بلوك لويس، Shame and Guilt in Neurosis (1971). صُحح أيضاً `edges.belongs_to` من `sch-psychodynamic-therapy` (غير موجود) إلى `sch-existential-therapy` (معتمد).
- **exp-socrates-oracle-delphi**: استشارة خيريفون لأوراكل دلفي من "الدفاع" لأفلاطون.
- **exp-solzhenitsyn-gulag-cancer-ward**: اعتقال فبراير 1945، غولاغ إكيباستوز، جناح السرطان 1968.
- **exp-spinoza-excommunication-amsterdam**: حرم/خيريم 27 يوليو 1656.
- **exp-stanislav-grof-lsd-holotropic**: تجربة LSD الأولى 1956 في براغ (فجوة: تضارب 1956/1957 حسب مصادر مختلفة).
- **exp-stephen-hawking-als-diagnosis**: تشخيص شتاء 1962-1963.
- **exp-steven-hayes-panic-carpet-act**: حذف اقتباس مختلَق واستبداله بوصف غير مقتبس؛ جامعة نورث كارولينا-غرينزبورو 1978.
- **exp-susanna-kaysen-mclean-hospital**: **تصحيح خطأ واقعي** — مستشفى ماكلين في بلمونت بولاية ماساتشوستس، لا "فيرجينيا" كما كان في النص الأصلي.
- **exp-swedenborg-spiritual-opening**: أزمة أبريل 1744، رؤية لندن 1745.
- **exp-temple-grandin-autism-squeeze-machine**: بناء الآلة الفعلي في Franklin Pierce College (لا جامعة أريزونا كما ورد في التوجيه الأولي) — استُخدمت الرواية الأوثق توثيقاً وفق قاعدة عدم اختراع الوقائع.
- **exp-teresa-avila-transverberation**: رؤية "اختراق القلب" من "حياتي" لتريزا الأفيلية (1562-1565).
- **exp-thich-nhat-hanh-vietnam-peace**: تأسيس SYSS 1964، نفي 1966، Plum Village 1982.
- **exp-tolstoy-midlife-crisis**: أزمة 1874-1879، "اعتراف" منشور جنيف 1884.
- **exp-unheimlich-freud**: مقالة Das Unheimliche 1919، مثال حكاية هوفمان "رجل الرمل".
- **exp-vertigo-existential-sartre**: تصحيح عنوان رابط `con-bad-faith` ("سوء الإيمان" لا "سوء النية").
- **exp-virginia-satir-family-sculpting**: **تصحيح مؤسسة** — عملها الفعلي الموثق في معهد إيسالن (1966-1968) لا "معهد أسبن" كما ورد في التوجيه الأولي وتعذّر توثيقه.
- **exp-william-blake-visionary-art**: رؤية بيكهام راي ~1767 (موثقة عبر سيرة جيلكريست 1863).
- **exp-william-james-panic-freewill**: أزمة خريف 1870، تأثير رينوفييه.
- **exp-william-styron-darkness-visible**: اكتئاب أكتوبر 1985 بباريس، الكتاب 1990.
- **exp-wittgenstein-ww1-trenches**: تطوع أغسطس 1914، أسر مونتي كاسينو 1918-1919؛ أُضيف `## المصادر` يدوياً بعد التوحيد.
- **met-act-chess-board، met-act-finger-trap، met-act-holding-a-heavy-backpack، met-act-leaves-on-a-stream، met-act-passengers-on-the-bus، met-act-quicksand-struggle، met-act-tug-of-war-monster**: أول دفعة استعارات (met-) — كل ملف: مصدر الصورة (Hayes, Strosahl & Wilson 1999/2012)، ما تقوله الاستعارة ولا يقوله التعبير المجرد، نقد صريح لحدودها؛ أُضيف `## المصادر` يدوياً لكل ملف بعد التوحيد (كانت الفقرات موجودة لكن بلا العنوان الرسمي، أو بصيغة "اقتباسات مختارة" فارغة استُبدلت).
- **met-al-ghazali-mirror-heart**: استعارة مرآة القلب من "إحياء علوم الدين" (شرح عجائب القلب) للغزالي؛ تصحيح عنواني رابطين (`thk-al-ghazali`، `tec-islamic-muraqabah-muhasabah`) ليطابقا العنوان الحقيقي.

## متوقف عنده (لرئيس التحرير)
- **exp-shame-vs-guilt-existential**: التصحيح الواقعي (أرندت→لويس) جوهري وليس تعميقاً أسلوبياً فقط — يستحق مراجعة تحريرية صريحة للتأكد من القبول.
- **exp-solzhenitsyn-gulag-cancer-ward**: تاريخ تشخيص السرطان الدقيق في إكيباستوز غير مؤكد من مصدر واحد قاطع.
- **exp-spinoza-excommunication-amsterdam**: لم يُقتبس نص الحرم حرفياً (فقط مُلخّص) تجنباً لاختراع ترجمة غير موثقة.
- **exp-stanislav-grof-lsd-holotropic**: تضارب تاريخ الجلسة الأولى (1956 مقابل 1957) بين مصادر سيرته الذاتية.
- **exp-stephen-hawking-als-diagnosis**: رواية الطفل المصاب بسرطان الدم في المستشفى مصدرها سيرته الذاتية فقط دون توثيق مستقل.
- **exp-susanna-kaysen-mclean-hospital**: تفاصيل رفيقات الجناح (جورجينا تاكر، أساس شخصية ليزا رو) تعتمد على الكتاب نفسه بلا سجل أرشيفي مستقل.
- **exp-temple-grandin-autism-squeeze-machine**: التناقض بين التوجيه الأولي (جامعة ولاية أريزونا) والرواية الموثقة فعلياً (Franklin Pierce College) — يستحق تأكيداً من فريق التحرير.
- **exp-teresa-avila-transverberation**: تاريخ الرؤية غير محدد بدقة من تريزا نفسها؛ ونسبة تأثيرها المباشر على تمثال برنيني تحتاج تدقيقاً إضافياً.
- **exp-virginia-satir-family-sculpting**: التناقض بين التوجيه الأولي (معهد أسبن) والرواية الموثقة (إيسالن) — يستحق تأكيداً من فريق التحرير مثل ملف غراندن.
- **exp-william-james-panic-freewill**: نسب الشهادة لجيمس نفسه استنتاج لاحق من بيري (1935) لا اعتراف مباشر موثق من جيمس شخصياً في مصدر أولي واحد.
- **exp-wittgenstein-ww1-trenches**: التواريخ مبنية على معرفة تاريخية عامة موثقة لا مراجعة مباشرة لسيرة أولية واحدة محددة.
- **met-act-*** (كل ملفات الاستعارات السبع): أرقام الصفحات الدقيقة في طبعة 1999/2012 لم تُراجع.
- **met-al-ghazali-mirror-heart**: أسبقية الغزالي على المحاسبي في صياغة استعارة مرآة القلب غير محسومة تاريخياً؛ مسجَّلة في `gaps`.

## الملفات
content/ar/experiences/exp-schopenhauer-frankfurt-isolation.md
content/ar/experiences/exp-seneca-forced-suicide-nero.md
content/ar/experiences/exp-shame-vs-guilt-existential.md
content/ar/experiences/exp-socrates-oracle-delphi.md
content/ar/experiences/exp-solzhenitsyn-gulag-cancer-ward.md
content/ar/experiences/exp-spinoza-excommunication-amsterdam.md
content/ar/experiences/exp-stanislav-grof-lsd-holotropic.md
content/ar/experiences/exp-stephen-hawking-als-diagnosis.md
content/ar/experiences/exp-steven-hayes-panic-carpet-act.md
content/ar/experiences/exp-susanna-kaysen-mclean-hospital.md
content/ar/experiences/exp-swedenborg-spiritual-opening.md
content/ar/experiences/exp-temple-grandin-autism-squeeze-machine.md
content/ar/experiences/exp-teresa-avila-transverberation.md
content/ar/experiences/exp-thich-nhat-hanh-vietnam-peace.md
content/ar/experiences/exp-tolstoy-midlife-crisis.md
content/ar/experiences/exp-unheimlich-freud.md
content/ar/experiences/exp-vertigo-existential-sartre.md
content/ar/experiences/exp-virginia-satir-family-sculpting.md
content/ar/experiences/exp-william-blake-visionary-art.md
content/ar/experiences/exp-william-james-panic-freewill.md
content/ar/experiences/exp-william-styron-darkness-visible.md
content/ar/experiences/exp-wittgenstein-ww1-trenches.md
content/ar/metaphors/met-act-chess-board.md
content/ar/metaphors/met-act-finger-trap.md
content/ar/metaphors/met-act-holding-a-heavy-backpack.md
content/ar/metaphors/met-act-leaves-on-a-stream.md
content/ar/metaphors/met-act-passengers-on-the-bus.md
content/ar/metaphors/met-act-quicksand-struggle.md
content/ar/metaphors/met-act-tug-of-war-monster.md
content/ar/metaphors/met-al-ghazali-mirror-heart.md
