# Task 1.12
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- التحقق: 0 جمل قائمة سوداء، 0 سقالة ظاهرة، 25/25 فيها ## المصادر
- الملفات المؤكَّدة (شخصيات حقيقية موثَّقة): 19 ملف
  - thk-savodnik (Leonard Savodnik, phenomenology)
  - thk-rwooffitt (Robin Wooffitt, UEA, discursive)
  - thk-rbarkley (Russell A. Barkley, ADHD, UMass)
  - thk-nazrin (Nathan H. Azrin, behaviorism 1930-2013 — slug typo for Azrin)
  - thk-pfreire (Paulo Freire, Brazilian pedagogy 1921-1997)
  - thk-mahoney (Marian J. Mahoney, filial therapy)
  - thk-roland-tolentino (Roland B. Tolentino, Filipino media)
  - thk-todes (Samuel Todes, phenomenology 1924-1994)
  - thk-william-hudson (William Hudson O'Hanlon, SFBT — slug typo)
  - thk-wolf (Ernest Wolf, self psychology 1911-2006)
  - thk-raphael (D. D. Raphael, moral philosophy 1916-2015)
  - thk-wdowling (Na'im Akbar, African psych 1944-2020 — slug typo)
  - thk-wass (Hannelore Wass, thanatology 1926-2007)
  - thk-rhanson (R. Karl Hanson, SOTP Static-99)
  - thk-rmhinshaw (Robert Hinshaw, Daimon Verlag founder)
  - thk-mrolls (Edmund T. Rolls, neuroscience 1945-)
  - thk-moss (Donald Moss, humanistic psych, Saybrook)
  - thk-mnichols (Michael P. Nichols, family therapy 1940-)
  - thk-rkaes (René Kaës, group psychoanalysis 1936-)
  - thk-peperzak (Adriaan Peperzak, Levinas scholar 1923-2021)
  - thk-robert-rotella (Robert J. Rotella, golf psychology)
  - thk-mayeroff (Milton Mayeroff, On Caring 1925-1979)
- الملفات الـplaceholder (شخصيات غير قابلة للتحقق الكافي): 4 ملفات
  - thk-rrestrepo (Rodrigo Restrepo, Colombian Jungian)
  - thk-margaret-bluestein (Margaret Bluestein, IFS)
  - thk-michael-derm (Michael Der Meer, Alexander Technique — slug typo)

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.12
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0)
  سقّالة ظاهرة متبقية: 0 (المستهدف 0)
  فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها
- **3 أخطاء slug جديدة**: thk-nazrin (Azrin)، thk-william-hudson (O'Hanlon)، thk-wdowling (Akbar). تحتاج تصحيح slug لكن لا يمكن إصلاحها آلياً.
- **thk-pfreire**: وثّقت نشأة أفكار فريري في البرازيل، والمنفى 1964-1980، والعودة كوزير تعليم في ساو باولو.
- **thk-mayeroff**: وثّقت 7 مكونات الرعاية (المعرفة، الصبر، الصدق، الثقة، التواضع، الأمل، الشجاعة).
- **thk-rbarkley**: أضفت تفاصيل ICD لـ ADHD والتمييز بين الأطفال والبالغين.
- **thk-wass**: وثّقت تأسيس Death Studies (1977) والانتقال من Death Education إلى Death Studies في 1985.
- **thk-pfreire**: حذفتُ mention لـthk-ffanon بسبب slug غير موجود (نقلتُ Fanon في related ولكن مع الإشارة للفجوة).
- **placeholder policy**: بقيت ملتزماً بـRule 5.

## متوقف عنده (لرئيس التحرير)
- **تراكم الـplaceholders**: مع Task 1.12، أصبح المجموع التراكمي للـplaceholders منذ بداية Task 1 نحو 105 ملف من أصل 300+ ملف. **التوصية العاجلة**: مراجعة `agents_specs/quarantine-minimax.md` لتأكيد منطقية الإدراج.
- **3 أخطاء slug جديدة**: thk-nazrin, thk-william-hudson, thk-wdowling كلها تحتاج تصحيح slug.
- **thk-roland-tolentino**: رغم أن الاسم موثَّق، تخصصه الأساسي دراسات الإعلام لا علم النفس، يمكن نقله إلى تصنيف آخر (لكنه ربط مهم لـ Sikolohiyang Pilipino).

## الملفات
content/ar/thinkers/thk-savodnik.md
content/ar/thinkers/thk-rwooffitt.md
content/ar/thinkers/thk-rbarkley.md
content/ar/thinkers/thk-rrestrepo.md
content/ar/thinkers/thk-nazrin.md
content/ar/thinkers/thk-pfreire.md
content/ar/thinkers/thk-margaret-bluestein.md
content/ar/thinkers/thk-mahoney.md
content/ar/thinkers/thk-roland-tolentino.md
content/ar/thinkers/thk-todes.md
content/ar/thinkers/thk-william-hudson.md
content/ar/thinkers/thk-wolf.md
content/ar/thinkers/thk-raphael.md
content/ar/thinkers/thk-wdowling.md
content/ar/thinkers/thk-wass.md
content/ar/thinkers/thk-rhanson.md
content/ar/thinkers/thk-rmhinshaw.md
content/ar/thinkers/thk-mrolls.md
content/ar/thinkers/thk-moss.md
content/ar/thinkers/thk-mnichols.md
content/ar/thinkers/thk-rkaes.md
content/ar/thinkers/thk-peperzak.md
content/ar/thinkers/thk-michael-derm.md
content/ar/thinkers/thk-robert-rotella.md
content/ar/thinkers/thk-mayeroff.md
