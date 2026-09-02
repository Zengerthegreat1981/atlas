# Task 1.13
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- التحقق: 0 جمل قائمة سوداء، 0 سقالة ظاهرة، 25/25 فيها ## المصادر
- الملفات المؤكَّدة (شخصيات حقيقية موثَّقة): 19 ملف
  - thk-plotinus (Plotinus, Hellenistic philosopher 204-270)
  - thk-mgergen (Mary Gergen, social constructionist feminism)
  - thk-tony-white (Tony White, TA 1932-2013)
  - thk-robert-emery (Robert Emery, EFT 1949-)
  - thk-mimordino-yang (Mary Helen Immordino-Yang, neuroscience 1972-)
  - thk-zambrano (María Zambrano, Spanish existentialism 1904-1991)
  - thk-trudi-schoop (Trudi Schoop, dance therapy 1903-1999)
  - thk-sstanley (Scott Stanley, commitment theory 1958-)
  - thk-wanthony (William Anthony, psychiatric rehab 1942-2017)
  - thk-yogananda (Paramahansa Yogananda 1893-1952)
  - thk-tgreening (Thomas Greening, JHP editor 1930-2022)
  - thk-mithoefer (Michael Mithoefer, MDMA-PTSD)
  - thk-nionescu (Nae Ionescu, Romanian existentialism 1890-1940)
  - thk-tbrazelton (T. Berry Brazelton, pediatrics 1918-2018)
  - thk-mmithoefer (Michael C. Mithoefer — same as thk-mithoefer, different slug)
  - thk-svami-akhilananda (Svami Akhilananda, Hindu psychology 1894-1962)
  - thk-osilver (Olga Silverstein, feminist family therapy 1920-2009)
  - thk-sothmer (Siegfried Othmer, ILF Neurofeedback)
  - thk-rlandy-md (Robert Landy, drama therapy, NYU)
  - thk-rennie (David Rennie, qualitative research 1939-)
- الملفات الـplaceholder (شخصيات غير قابلة للتحقق الكافي): 5 ملفات
  - thk-niosepa (Nana Iosepa, Ho'oponopono Tonga — «Nana» كلمة تونغية، الاسم غير قابل للتوثيق)
  - thk-russellrazzaque (Russell Razzaque, Open Dialogue UK)
  - thk-trudakova (Tatyana Rudakova, Russian Jungian)
  - thk-zhangyongqiang (Zhang Yongqiang, Taoist CBT — اسم شائع)
  - thk-schulz (Peter Schulz, Existential Analysis Austria)

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.13
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0)
  سقّالة ظاهرة متبقية: 0 (المستهدف 0)
  فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها
- **thk-plotinus**: وثّقت أطروحات أفلوطين الثلاثة (الواحد، العقل، النفس) وتأثيره في الفلسفة الإسلامية واللاهوت المسيحي.
- **thk-mithoefer و thk-mmithoefer**: ملفان يشيران إلى نفس الشخص. وثّقت التوصية في الـgaps بدمجهما.
- **thk-tbrazelton**: وثّقت NBAS (Neonatal Behavioral Assessment Scale) كـأداة مستخدمة عالمياً.
- **thk-tgreening**: وثّقت إدارته لمجلة JHP لأكثر من 35 عاماً (1970-2005).
- **thk-mithoefer**: وثّقت تجربة المرحلة الثالثة في *Nature Medicine* (2021) التي أظهرت 67% من المرضى فقدوا معايير PTSD.
- **thk-yogananda**: وثّقت Autobiography of a Yogi (1946) كأحد أكثر الكتب الروحية مبيعاً.
- **blacklist removal**: أزلتُ «لا يوجد اقتباس مباشر موثوق متاح» و«ملاحظة معمارية» من ملف thk-mmithoefer.
- **placeholder policy**: بقيت ملتزماً بـRule 5.

## متوقف عنده (لرئيس التحرير)
- **تراكم الـplaceholders**: مع Task 1.13، أصبح المجموع التراكمي للـplaceholders منذ بداية Task 1 نحو 110 ملف من أصل 325+ ملف. **التوصية العاجلة**: مراجعة `agents_specs/quarantine-minimax.md`.
- **Duplicate Mithoefer**: ملفان يشيران إلى نفس الشخص يحتاجان إلى دمج في الأطلس.
- **2/5 since checkpoint**: أحتاج إلى Task 1.14 ثم Task 1.15 ثم checkpoint.

## الملفات
content/ar/thinkers/thk-plotinus.md
content/ar/thinkers/thk-mgergen.md
content/ar/thinkers/thk-tony-white.md
content/ar/thinkers/thk-robert-emery.md
content/ar/thinkers/thk-mimordino-yang.md
content/ar/thinkers/thk-zambrano.md
content/ar/thinkers/thk-niosepa.md
content/ar/thinkers/thk-trudi-schoop.md
content/ar/thinkers/thk-sstanley.md
content/ar/thinkers/thk-wanthony.md
content/ar/thinkers/thk-yogananda.md
content/ar/thinkers/thk-russellrazzaque.md
content/ar/thinkers/thk-tgreening.md
content/ar/thinkers/thk-mithoefer.md
content/ar/thinkers/thk-nionescu.md
content/ar/thinkers/thk-tbrazelton.md
content/ar/thinkers/thk-mmithoefer.md
content/ar/thinkers/thk-svami-akhilananda.md
content/ar/thinkers/thk-trudakova.md
content/ar/thinkers/thk-osilver.md
content/ar/thinkers/thk-zhangyongqiang.md
content/ar/thinkers/thk-schulz.md
content/ar/thinkers/thk-sothmer.md
content/ar/thinkers/thk-rlandy-md.md
content/ar/thinkers/thk-rennie.md
