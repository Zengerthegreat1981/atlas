# Task 1.9
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- التحقق: 0 جمل قائمة سوداء، 0 سقالة ظاهرة، 25/25 فيها ## المصادر
- الملفات المُحدَّثة: 25/25 (مقابل مسودَّات سابقة)
- الملفات المؤكَّدة (شخصيات حقيقية موثَّقة): 15 ملف
  - thk-wiseman (Hadas Wiseman, هوفا، SPR)
  - thk-madinier (Gabriel Madinier, فيلسوف فرنسي 1895-1958)
  - thk-mtselvini (Matteo Selvini, ابن Mara Selvini Palazzoli)
  - thk-rcermak (Sharon Cermak, USC OT)
  - thk-mviederman (Milton Viederman, Cornell)
  - thk-mainieri (Lina Mainieri, دازاين برازيلي)
  - thk-meitingon (Max Eitingon, IPA, برلين پولي‌كلينيك)
  - thk-nbepstein (Norman Epstein, Maryland)
  - thk-schneider (Kirk Schneider, Saybrook)
  - thk-ruilinzhou (Zhou Ruilin, TCT الصين)
  - thk-suttie (Ian Suttie, Tavistock 1889-1935)
  - thk-takanen (Kimmo Takanen, فنلندا)
  - thk-rschaaf (Roseann Schaaf, Jefferson ASI-EBP)
  - thk-steven-haber (Steven Haber, AEDP)
  - thk-ppenn (Peggy Penn, Houston Galveston)
  - thk-zoroaster (Zarathustra)
- الملفات الـplaceholder (شخصيات غير قابلة للتحقق الكافي): 9 ملفات
  - thk-melissaschaefer (Melissa Schaefer, MST)
  - thk-randystabler (Randy Stabler, MST)
  - thk-yongjingqi (Yong Jingqi, TCT الصين)
  - thk-shirley-murray (Shirley Murray, Alexander Technique)
  - thk-margaretbodkin (Margaret Bodkin, Experiential)
  - thk-rklenck (ملف استعراضي للجمعيات البريطانية الخمس)
  - thk-mingshengli (Li Mingsheng, TCT الصين)
  - thk-tom-cornwell (Tom Cornwell, RJ NZ)
  - thk-sharron-hapai (Sharron Hapai, Te Whare Tapa Whā)
- ملفات placeholder موصوفة في gaps مع توصية الحجر في `agents_specs/quarantine-minimax.md`

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.9
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0)
  سقّالة ظاهرة متبقية: 0 (المستهدف 0)
  فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها
- **thk-rklenck**: أبقيت الملف الاستعراضي للجمعيات البريطانية الخمس (SAP, IGAP, BJAA, AJA, GAP) لأنه مفيد كمدخل تاريخي للمقارنة بين التيارات اليونغية البريطانية، مع توصية بفصل كل جمعية لملف مستقل وربطها بمفكِّريها الفرديين.
- **thk-ppenn**: صحَّحت الخطأ في المسوَّدة: بِن عملت في **معهد هيوستن-غالفيستون** (Houston Galveston) لا «مركز أوستن»، مع [غوليشيان](thk-hgoolishian) و[أندرسون](thk-handerson).
- **thk-sharron-hapai**: وثَّقت أن الـslug الأصلي `thk-trore` كان خطأً كتابياً لـ'Mason Durie' (الذي أُنشئ تحت `thk-mdurie`)، وهذا فسَّر بعض الخلط في الأسماء.
- **placeholder policy**: تبنَّيت Rule 5 من MINIMAX بصرامة — لا أكتب سيرة ذاتية مختلقة للأسماء غير القابلة للتحقق، لكن أحتفظ بالعنوان في الفهرس مع توثيق مفصَّل لمحاولات التوثيق في قسم `## محاولة التوثيق` وتوصية الحجر في `agents_specs/quarantine-minimax.md`.
- **blacklist removal**: حذفتُ «لا يوجد اقتباس مباشر موثوق متاح» من كل الفجوات (gaps) واستبدلتها بصياغة مهنية تشرح سبب عدم التحقق.
- **scaffold removal**: استبدلتُ «ملاحظة معمارية» بـ«توصية الحجر» في thk-melissaschaefer.

## متوقف عنده (لرئيس التحرير)
- **تراكم الـplaceholders**: مع Task 1.9، أصبح المجموع التراكمي للـplaceholders منذ بداية Task 1 نحو 80 ملفاً من أصل 200+ ملف. **التوصية العاجلة**: مراجعة `agents_specs/quarantine-minimax.md` لتأكيد منطقية الإدراج، أو نقل المعلومات إلى ملفات المدارس (sch-) أو التقنيات (tec-).
- **صراع الـslugs (125 حالة)**: بعض المسوَّدات الجديدة (مثل thk-melissaschaefer) تحتمل صراعاً مع ملفات موجودة في `content/ar/drafts/EXISTING_SLUGS.md`. التحقق اليدوي مطلوب.
- **thk-rklenck**: ملف استعراضي للجمعيات الخمس يحتاج إلى فصل. مؤجَّل لمهمة لاحقة.
- **thk-sharron-hapai**: الـslug الأصلي خاطئ (كان thk-trore ثم نُقل). التحقق من أسماء Māori (Hāpai) في الفهارس الدولية أمر مطلوب.

## الملفات
content/ar/thinkers/thk-wiseman.md
content/ar/thinkers/thk-melissaschaefer.md
content/ar/thinkers/thk-madinier.md
content/ar/thinkers/thk-mtselvini.md
content/ar/thinkers/thk-rcermak.md
content/ar/thinkers/thk-randystabler.md
content/ar/thinkers/thk-mviederman.md
content/ar/thinkers/thk-mainieri.md
content/ar/thinkers/thk-yongjingqi.md
content/ar/thinkers/thk-shirley-murray.md
content/ar/thinkers/thk-meitingon.md
content/ar/thinkers/thk-nbepstein.md
content/ar/thinkers/thk-schneider.md
content/ar/thinkers/thk-margaretbodkin.md
content/ar/thinkers/thk-ruilinzhou.md
content/ar/thinkers/thk-rklenck.md
content/ar/thinkers/thk-suttie.md
content/ar/thinkers/thk-mingshengli.md
content/ar/thinkers/thk-takanen.md
content/ar/thinkers/thk-tom-cornwell.md
content/ar/thinkers/thk-rschaaf.md
content/ar/thinkers/thk-steven-haber.md
content/ar/thinkers/thk-sharron-hapai.md
content/ar/thinkers/thk-ppenn.md
content/ar/thinkers/thk-zoroaster.md
