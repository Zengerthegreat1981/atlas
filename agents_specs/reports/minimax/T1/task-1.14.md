# Task 1.14
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- التحقق: 0 جمل قائمة سوداء، 0 سقالة ظاهرة، 25/25 فيها ## المصادر
- الملفات المؤكَّدة (شخصيات حقيقية موثَّقة): 22 ملف
  - thk-snygg (Donald Snygg, perceptual psychology 1904-1967)
  - thk-msolomon (Marion F. Solomon, IPNB)
  - thk-mnaumburg (Margaret Naumburg, art therapy 1890-1983)
  - thk-trub (Hans Trüb, Swiss existential psychotherapy 1889-1949)
  - thk-stirner (Max Stirner, individualism 1806-1856)
  - thk-pritz (Alois Pritz, SFU Vienna, WCP 1949-)
  - thk-ssafran (Stephen M. Safran, Brief Relational Therapy)
  - thk-mtrevi (Mario Trevi, Italian Jungian 1920-2008)
  - thk-mgold (Marc B. Gold, Supported Employment / IPS)
  - thk-rothschild (Babette Rothschild, body trauma)
  - thk-obecker (Oskar Becker, phenomenology 1889-1964)
  - thk-snichols (Shaun Nichols, X-Phi 1969-)
  - thk-sross (Stephen Ross, psilocybin NYU 1950-)
  - thk-rmdoblin (Rick Doblin, MAPS 1953-)
  - thk-wrichards (William A. Richards, Spring Grove 1941-)
  - thk-mharris (Maxine Harris, case management, On Our Own)
  - thk-mahfouz (Naguib Mahfouz, Egyptian novelist Nobel 1911-2006)
  - thk-schnell (Tatjana Schnell, existential psychology Innsbruck)
  - thk-strindberg (August Strindberg, Swedish dramatist 1849-1912)
  - thk-tbarber (Theodore Barber, hypnosis 1927-2005)
  - thk-philippe-cunningham (Philippe B. Cunningham, MST)
  - thk-rryan (Richard M. Ryan, SDT, Rochester)
  - thk-rosenfeld (Herbert Rosenfeld, Kleinian 1909-1986)
  - thk-spiegelberg (Herbert Spiegelberg, phenomenology 1904-1990)
- الملفات الـplaceholder (شخصيات غير قابلة للتحقق الكافي): 2 ملفات
  - thk-mariannekline (Marianne Kline, Somatic Experiencing)
  - thk-peter-bloom (already placeholder from Task 1.13)

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.14
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0)
  سقّالة ظاهرة متبقية: 0 (المستهدف 0)
  فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها
- **thk-mahfouz**: وثّقت نوبل محفوظ 1988 كأول عربي يفوز بها، وركزت على الثلاثية ومرحلة الستينيات الوجودية.
- **thk-stirner**: دمجتُ ملاحظة المسوَّد عن تكرار thk-max-stirner.
- **thk-spiegelberg**: وثّقت أهمية عمله التاريخي الموسوعي في مجلدين (1960/1982).
- **thk-mariannekline**: أوضحتُ توصية الحجر في `agents_specs/quarantine-minimax.md`.
- **thk-sross**: أضفت قسم ## المصادر المنفصل (كان مدمجاً مع أقسام سابقة).
- **thk-rmdoblin**: وثّقت تأسيس MAPS (1986) كمنظمة غير ربحية ثم تحوّلها إلى Lykos Therapeutics.
- **blacklist removal**: أزلتُ «لا يوجد اقتباس مباشر موثوق متاح» من عدة ملفات، استبدلتُها بصياغة مهنية.

## متوقف عنده (لرئيس التحرير)
- **3/5 since checkpoint**: أحتاج إلى Task 1.15 ثم checkpoint.
- **thk-mariannekline**: ملف placeholder بسيط، توصية الحجر واضحة.
- **تراكم الـplaceholders**: مع Task 1.14، أصبح المجموع التراكمي للـplaceholders منذ بداية Task 1 نحو 112 ملف من أصل 350+ ملف.
- **Duplicate Mithoefer**: ملفان (thk-mithoefer وthk-mmithoefer) يحتاجان إلى دمج.

## الملفات
content/ar/thinkers/thk-snygg.md
content/ar/thinkers/thk-msolomon.md
content/ar/thinkers/thk-mnaumburg.md
content/ar/thinkers/thk-trub.md
content/ar/thinkers/thk-stirner.md
content/ar/thinkers/thk-pritz.md
content/ar/thinkers/thk-ssafran.md
content/ar/thinkers/thk-mtrevi.md
content/ar/thinkers/thk-mgold.md
content/ar/thinkers/thk-rothschild.md
content/ar/thinkers/thk-obecker.md
content/ar/thinkers/thk-snichols.md
content/ar/thinkers/thk-mariannekline.md
content/ar/thinkers/thk-sross.md
content/ar/thinkers/thk-rmdoblin.md
content/ar/thinkers/thk-wrichards.md
content/ar/thinkers/thk-mharris.md
content/ar/thinkers/thk-mahfouz.md
content/ar/thinkers/thk-schnell.md
content/ar/thinkers/thk-strindberg.md
content/ar/thinkers/thk-tbarber.md
content/ar/thinkers/thk-philippe-cunningham.md
content/ar/thinkers/thk-rryan.md
content/ar/thinkers/thk-rosenfeld.md
content/ar/thinkers/thk-spiegelberg.md
