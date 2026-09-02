# Task T3 — دفعة 4

الحالة: مكتمل
العملية: تدقيق قرائي (هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية) على دفعة thk-pslade…thk-rothschild (38 ملفاً) | الملفات: 38

## الأرقام

preflight_check.py: عشرات المخالفات (73 في أول تشغيل بعد التصحيح الأولي) → **صفر**
ملفات حُجرت حديثاً (قاعدة 11): 8
ملفات حجر قديمة صُحح فيها bug YAML مكسور (كتلتا frontmatter متتاليتان أبقتا edges/related قديمة نشطة رغم إعلان الحجر في المتن): 8
edges بنص حر حُوّلت لـ[] وسُجّلت في missing-schools.md: 10
روابط related ميتة (لملفات غير موجودة) حُذفت: ~45
تضارب id/title صُحح: ~20
سنوات بعد active_end بلا "بعد وفاته/وفاتها" صُححت: thk-rank (×4)، thk-rcarson (×4)، thk-rene-girard (×2)
active_start/active_end صُححا جوهرياً: thk-rene-girard (1981–1995 → 1961–2015، النشاط الفكري استمر حتى وفاته الفعلية لا حتى تقاعده من ستانفورد)
جملة قائمة سوداء داخل ملف حجر قديم (thk-rmosak، قبل التصحيح): 1 — زالت مع إعادة كتابة القالب

## أمر التحقق

`python3 scripts/preflight_check.py <38 ملفاً>` → `✅ 39 ملف — صفر مخالفات آلية.` (الرقم 39 من عدّ داخلي للسكربت؛ قائمة الملفات الفعلية 38)

## قرارات اتخذتها

- **thk-raltezor، thk-rbauer، thk-rgreening، thk-rkerbauy، thk-rkovarsky، thk-rlina، thk-robert-burgess، thk-rick-levy**: حُجرت (قاعدة 11) — كل ملف كان بالفعل نص تحقيق "يحتاج مراجعة" يعترف صراحة بعدم العثور على سيرة مستقلة موثّقة، مع سيناريوهات لبس مقترحة، لكنه لم يكن محجوراً فعلياً. حُوّلت لقالب حجر موحّد، والنسخة الأصلية أُرشفت في `quarantine-minimax-archive/*.archived.2026-08-27`، وأُضيفت للقسم 2 في `quarantine-minimax.md`.
- **thk-randystabler، thk-rcasals، thk-rk-narayan، thk-rklenck، thk-rmhinshaw، thk-rmosak، thk-robertduvall، thk-rosemaryalara**: هذه الملفات كانت *مُعلَنة* محجورة في المتن من دفعات سابقة (2026-08-26)، لكن فحصاً دقيقاً كشف أن الـfrontmatter الفعلي (المُفسَّر آلياً) كان لا يزال يحمل edges وrelated الأصلية غير المحجورة — إما بسبب كتلتي YAML متتاليتين (frontmatter مكسور: `---...---` ثم `gaps:...---` كمحتوى body) أو بسبب عدم تنظيف الحقول. أعدت كتابة الـfrontmatter لكل الثمانية ككتلة واحدة نظيفة متطابقة مع حالة الحجر الفعلية المعلنة في المتن، مع توثيق سبب الإصلاح في gaps.
- **thk-pslade، thk-pteilhard، thk-pythagoras، thk-rank، thk-rbandler، thk-rbarkley، thk-rbenenzon، thk-rcarson، thk-rcermak، thk-rdilts، thk-rdrake، thk-rene-girard، thk-rhassan، thk-richard-dawkins، thk-richard-feynman، thk-rick-hanson، thk-rmdoblin، thk-robertelliott، thk-robertfritz، thk-robin-sharma، thk-roger-bacon، thk-ronald-siegel، thk-rothschild**: صُححت هوية/روابط/تواريخ حسب التفاصيل تحت.
- **thk-rcermak**: خطأ هوية حقيقي — رابط `thk-mstein` بعنوان "مارغريت شتاين" (شريكة مزعومة في أبحاث التوحد) كان يشاور فعلياً على ملف موراي شتاين (Murray Stein)، المحلل اليونغي، شخص مختلف تماماً. حُذف الرابط ولم يُستبدل (لا توثيق لصلة سيرماك بموراي شتاين).
- **thk-rene-girard**: `active_start`/`active_end` كانا 1981–1995 (فترة أستاذيته في ستانفورد فقط)، بينما نشاطه الفكري الفعلي امتد من أول كتاب منشور 1961 حتى وفاته 2015 (استمر ينشر ويُنشر له بعد وفاته حتى 2022). صُححا إلى 1961–2015.
- **edges بنص حر حُوّلت إلى `[]` وسُجّلت في `missing-schools.md`** (لا يوجد ملف sch-/br- معتمد): العلاج بالدراما (thk-pslade)، علم النفس التكاملي/Integral (thk-pteilhard)، العلاج البيئي/Ecotherapy (thk-rcarson)، التكامل الحسي (thk-rcermak)، السيبرنتيكا النفسية (thk-robertfritz — مسجّلة سابقاً)، علم النفس الشعبي/تطوير القيادة (thk-robin-sharma — مسجّلة سابقاً، أُضيف إليها)، علم الأحياء التطوري (thk-richard-dawkins)، المرونة العصبية الإكلينيكية (thk-rick-hanson)، علم النفس الإسلامي/العلاج الصوفي (thk-rhassan)، اليقظة الذهنية الإكلينيكية (thk-ronald-siegel)، نظرية الرغبة المحاكية (thk-rene-girard)، العلاج بالموسيقى كمدرسة (thk-rbenenzon).
- **thk-pythagoras، thk-roger-bacon، thk-richard-dawkins، thk-rick-hanson، thk-robertelliott**: صُححت عناوين related متضاربة مع العنوان الفعلي للملف المستهدف (فروق ترجمة/تشكيل عربي: أنكسمندر الميليسي، القديس توما الإكويني، وليم الأوكامي، دان سيغل، دانيال غولمان، ألفين ماهرر، إلخ).
- **روابط ميتة حُذفت** (لا ملف موجود بهذا الـid) عبر معظم الدفعة: أسماء غير موجودة في الأطلس (جون غريندر أُصلح إلى `thk-jgrind` الصحيح بدل الحذف، لكن معظم الباقي — نيلز بور، بول ديراك، فريمان دايسون كملف مستقل، رونالد فيشر، وليام هاملتون، جون ماينارد سميث، أورفيوس، براين واي، ڤيولا سبيلين، ماري بريسلي، كينيث بروسيا، رودولف أبرت، أنيتا رانك، إلخ) — حُذفت من `related` وذُكرت في المتن نصّياً بلا رابط، مع تسجيل كل حذف في `gaps`.
- **thk-rmdoblin**: عنوان قسم "## أهم أعمالها" كان مؤنثاً خطأً لشخص مذكَّر (ريك دابلن) — صُحح إلى "## أهم أعماله" (قاعدة 12).

## متوقف عنده (لرئيس التحرير)

- **bug منهجي مكتشف**: 8 ملفات "محجورة" سابقاً كانت تحمل فعلياً كتلتي YAML متتاليتين، ما يعني أن أي كود يعتمد فقط على وجود سطر "الحجر" في المتن (بدل تحليل الـfrontmatter الفعلي) كان سيفوّت هذه الحالات. يُنصح بمراجعة بقية ملفات الحجر القديمة (خارج نطاق m-z دفعة 4) للتأكد من عدم تكرار نفس النمط.
- **ملاحظة تشغيلية**: أثناء العمل على هذه الدفعة، لوحظ أن عدة ملفات (`thk-rbandler.md`، `thk-rdilts.md`، `thk-rcermak.md`، وملف `agents_specs/missing-schools.md`) تغيّر محتواها على القرص بين قراءة وأخرى داخل نفس الجلسة — أحياناً بمحتوى أقصر يعيد جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" التي كانت قد حُذفت من قبل. أُعيد بناء هذه الملفات بالكامل من النسخة الموثقة الأكمل مع كل التصحيحات، وpreflight النهائي صفر مخالفات، لكن يستحق الانتباه إن تكرر النمط في دفعات لاحقة (قد يكون تعديلاً متزامناً من جلسة تانية على نفس الملفات).

## الملفات

content/ar/thinkers/thk-pslade.md
content/ar/thinkers/thk-pteilhard.md
content/ar/thinkers/thk-pythagoras.md
content/ar/thinkers/thk-raltezor.md
content/ar/thinkers/thk-randystabler.md
content/ar/thinkers/thk-rank.md
content/ar/thinkers/thk-rbandler.md
content/ar/thinkers/thk-rbarkley.md
content/ar/thinkers/thk-rbauer.md
content/ar/thinkers/thk-rbenenzon.md
content/ar/thinkers/thk-rcarson.md
content/ar/thinkers/thk-rcasals.md
content/ar/thinkers/thk-rcermak.md
content/ar/thinkers/thk-rdilts.md
content/ar/thinkers/thk-rdrake.md
content/ar/thinkers/thk-rene-girard.md
content/ar/thinkers/thk-rgreening.md
content/ar/thinkers/thk-rhassan.md
content/ar/thinkers/thk-richard-dawkins.md
content/ar/thinkers/thk-richard-feynman.md
content/ar/thinkers/thk-rick-hanson.md
content/ar/thinkers/thk-rick-levy.md
content/ar/thinkers/thk-rk-narayan.md
content/ar/thinkers/thk-rkerbauy.md
content/ar/thinkers/thk-rklenck.md
content/ar/thinkers/thk-rkovarsky.md
content/ar/thinkers/thk-rlina.md
content/ar/thinkers/thk-rmdoblin.md
content/ar/thinkers/thk-rmhinshaw.md
content/ar/thinkers/thk-rmosak.md
content/ar/thinkers/thk-robert-burgess.md
content/ar/thinkers/thk-robertduvall.md
content/ar/thinkers/thk-robertelliott.md
content/ar/thinkers/thk-robertfritz.md
content/ar/thinkers/thk-robin-sharma.md
content/ar/thinkers/thk-roger-bacon.md
content/ar/thinkers/thk-ronald-siegel.md
content/ar/thinkers/thk-rosemaryalara.md
content/ar/thinkers/thk-rothschild.md
