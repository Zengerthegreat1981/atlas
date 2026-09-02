# Task 1.11
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- التحقق: 0 جمل قائمة سوداء، 0 سقالة ظاهرة، 25/25 فيها ## المصادر
- الملفات المؤكَّدة (شخصيات حقيقية موثَّقة): 14 ملف
  - thk-sspeer (Susan A. Speer, Lancaster, discursive psych)
  - thk-zlipowski (Zbigniew J. Lipowski, McGill, psychosomatic 1924-1997)
  - thk-mtotton (Mark Totton, body psychotherapy/addiction)
  - thk-mforgatch (Marion Forgatch, Oregon, PMTO)
  - thk-rshort (Robert Short, Imago Dei, Duke Divinity)
  - thk-opfister (Oskar Pfister, Swiss pastor/analyst 1873-1956)
  - thk-ortega (José Ortega y Gasset, Spanish philosopher 1883-1955)
  - thk-sleclaire (Serge Leclaire, Lacanian 1924-1994)
  - thk-mandolfi (Mauro Andolfi, Milan multigenerational)
  - thk-pchodron (Pema Chödrön, Buddhist nun 1936-)
  - thk-rackoff (Russell Ackoff, systems theory 1919-2009)
  - thk-mfarkas (Marianne Farkas, recovery movement, BU)
  - thk-mgriffiths (Mark Griffiths, behavioral addiction, NTU)
  - thk-michael-yarp (Michael Yapko, hypnosis, real content with slug typo)
  - thk-paci (Enzo Paci, existential phenomenology 1911-1976)
- الملفات الـplaceholder (شخصيات غير قابلة للتحقق الكافي): 10 ملفات
  - thk-pekkajokinen (Pekka Jokinen, Open Dialogue — اشتبه بـJaakko Seikkula)
  - thk-peter-bloom (Peter Bloom, psychedelic therapy — اشتبه بـPeter M. Bloom في دراسات الأعمال)
  - thk-masaaki-takahashi (Masaaki Takahashi, Naikan — اسم شائع ياباني)
  - thk-mmejia (Margarita Mejía, Colombian Jungian)
  - thk-wboechat (Walter Boechat, Brazilian Jungian)
  - thk-rosemaryalara (Rosemary Alara, Scientology critic)
  - thk-ma-rosario-alfelor (Ma. Rosario Alfelor, Filipino psychology)
  - thk-michaelsweeting (Michael Sweeting, Te Whare Tapa Whā)
  - thk-spiper (Stefan B. Piper, critical psychology — اشتبه بـIan Parker)
  - thk-pgodfrey (Peter A. Godfrey, bodywork)
- ملفات placeholder موصوفة في gaps مع توصية الحجر في `agents_specs/quarantine-minimax.md`

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.11
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0)
  سقّالة ظاهرة متبقية: 0 (المستهدف 0)
  فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها
- **thk-rackoff**: الـslug خطأ كتابي لـ'Russell Ackoff' (1919-2009). وثّقت التصحيح في الـgaps لكن لا يمكن إصلاح الـslug آلياً.
- **thk-michael-yarp**: الـslug خطأ كتابي لـ'Michael Yapko' (الأكثر شهرة كـMichael D. Yapko، Trancework 1984). المحتوى موثَّق لكن الـslug يحتاج تصحيح.
- **thk-ortega**: أضفت الاقتباس الشهير «أنا هو أنا وظرفي» في قسم الاقتباسات (لم يكن موجوداً في المسوَّد، لكن النص الأصلي موثَّق في *Meditaciones del Quijote* 1914).
- **thk-opfister**: وثّقت المراسلات مع فرويد (The Letters of Sigmund Freud and Oskar Pfister, 1963) كمرجع أساسي.
- **thk-pchodron**: صحّحت الاسم الأصلي (Deirdre Blomfield-Brown) ووثّقت علاقتها بـChögyam Trungpa وShambhala.
- **thk-mgriffiths**: وثّقت تأثيره في إدراج Gaming Disorder في ICD-11 (2018).
- **thk-rmosak** (من Task 1.10): قارن مع Harold Mosak في Adlerian — خلط محتمل في الـslug.
- **placeholder policy**: بقيت ملتزماً بـRule 5.

## متوقف عنده (لرئيس التحرير)
- **2 أخطاء slug في Task 1.11**: thk-rackoff وthk-michael-yarp يحتاجان تصحيح slug (لكن التصحيح يكسر الروابط في `related:`).
- **تراكم الـplaceholders**: مع Task 1.11، أصبح المجموع التراكمي للـplaceholders منذ بداية Task 1 نحو 100 ملف من أصل 275+ ملف. **التوصية العاجلة**: مراجعة `agents_specs/quarantine-minimax.md` لتأكيد منطقية الإدراج، أو نقل المعلومات إلى ملفات المدارس (sch-) أو التقنيات (tec-).
- **صراع الـslugs (متزايد)**: 3 ملفات جديدة في Task 1.11 تحتمل صراعاً.
- **thk-paci**: أطروحته في «الماركسية-الظاهراتية» تحتاج ربطاً مع ملف sch-existential-therapy (وإن كان التصنيف هنا موضع نقاش).
- **thk-mfarkas**: توفيت 2010، أرشيفاتها في BU Sargent College يجب التحقق منه.

## الملفات
content/ar/thinkers/thk-pekkajokinen.md
content/ar/thinkers/thk-peter-bloom.md
content/ar/thinkers/thk-sspeer.md
content/ar/thinkers/thk-masaaki-takahashi.md
content/ar/thinkers/thk-zlipowski.md
content/ar/thinkers/thk-mtotton.md
content/ar/thinkers/thk-mmejia.md
content/ar/thinkers/thk-wboechat.md
content/ar/thinkers/thk-rosemaryalara.md
content/ar/thinkers/thk-ma-rosario-alfelor.md
content/ar/thinkers/thk-mforgatch.md
content/ar/thinkers/thk-rshort.md
content/ar/thinkers/thk-opfister.md
content/ar/thinkers/thk-ortega.md
content/ar/thinkers/thk-sleclaire.md
content/ar/thinkers/thk-michaelsweeting.md
content/ar/thinkers/thk-mandolfi.md
content/ar/thinkers/thk-pchodron.md
content/ar/thinkers/thk-rackoff.md
content/ar/thinkers/thk-mfarkas.md
content/ar/thinkers/thk-spiper.md
content/ar/thinkers/thk-mgriffiths.md
content/ar/thinkers/thk-michael-yarp.md
content/ar/thinkers/thk-pgodfrey.md
content/ar/thinkers/thk-paci.md
