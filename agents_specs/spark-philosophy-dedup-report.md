# تقرير تدقيق التكرار الشامل لقسم الفلسفة — مسار Spark

**التاريخ:** 21 أغسطس 2026  
**المسار:** خط أنابيب تدقيق سلامة قسم الفلسفة (`spark-philosophy-integrity-audit-pipeline.md`)  
**النطاق:** كافة ملفات قسم الفلسفة (`part: "philosophy"`) والمفكرين والمدارس والأعمال المتداخلة عبر الأطلس  

---

## 1. ملخص إحصائي

| القياس | القيمة |
|---|---|
| **إجمالي ملفات قسم الفلسفة المفحوصة** | 769 ملفاً |
| **إجمالي ملفات الأطلس المفحوصة** | 4,164 ملفاً |
| **حالات التعارض والازدواج المؤكدة (المُعالجة)** | 31 حالة |
| **- مسودات مكررة لملفات معتمدة متطابقة في الـ slug** | 8 حالات حذف مسودة |
| **- فك اشتباك تعارض أسماء متشابهة (سليمان التوراتي vs روبرت سولومون)** | حالة واحدة (إنشاء `thk-solomon-hebrew`) |
| **- مسودات مكررة لمفكرين معتمدين بـ slugs مختلفة** | 6 حالات دمج وحذف مسودة |
| **- مسودات مكررة داخل المسودات (Thinkers & Works)** | 17 حالة دمج وحذف مسودة |
| **حالات "تشابه بنيوي مشروع" (لم تُلمس)** | 10 حالات تقاطع cross-type (مدرسة مقابل تيار/مفهوم) |

---

## 2. حالات التكرار والتعارض المؤكدة (المُعالجة بالكامل)

### الفئة A — مسودات فلسفية مكررة تطابق ملفات معتمدة في الـ Slug (8 حالات)

| المسودة المحذوفة | المعتمد الأصلي المحفوظ | الشخصية / المفكر |
|---|---|---|
| `content/ar/drafts/thinkers/thk-schopenhauer.md` | `content/ar/thinkers/thk-schopenhauer.md` (`THK-0532`) | أرثر شوبنهاور (Arthur Schopenhauer) |
| `content/ar/drafts/thinkers/thk-emerson.md` | `content/ar/thinkers/thk-emerson.md` (`THK-0581`) | رالف والدو إمرسون (Ralph Waldo Emerson) |
| `content/ar/drafts/thinkers/thk-schelling.md` | `content/ar/thinkers/thk-schelling.md` (`THK-0530`) | فريدريش شيلينغ (Friedrich Schelling) |
| `content/ar/drafts/thinkers/thk-kierkegaard.md` | `content/ar/thinkers/thk-kierkegaard.md` (`THK-0101`) | سورين كيركيغارد (Søren Kierkegaard) |
| `content/ar/drafts/thinkers/thk-hegel.md` | `content/ar/thinkers/thk-hegel.md` (`THK-0576`) | جورج فيلهلم فريدريش هيغل (G.W.F. Hegel) |
| `content/ar/drafts/thinkers/thk-rousseau.md` | `content/ar/thinkers/thk-rousseau.md` (`THK-0527`) | جان جاك روسو (Jean-Jacques Rousseau) |
| `content/ar/drafts/thinkers/thk-nishida.md` | `content/ar/thinkers/thk-nishida.md` (`THK-0508`) | كيتارو نيشيدا (Kitaro Nishida) |
| `content/ar/drafts/thinkers/thk-nietzsche.md` | `content/ar/thinkers/thk-nietzsche.md` (`THK-0302`) | فريدريش نيتشه (Friedrich Nietzsche) |

### الفئة B — فك اشتباك تشابه الأسماء (Disambiguation)
- **المشكلة:** مسودة الملك سليمان الحكيم في الحكمة العبرية والتوراتية أُنشئت تحت `thk-solomon` مما تعارض مع الفيلسوف الوجودي الأمريكي المعتمد روبرت سولومون (`thk-solomon` / `THK-0540`).
- **الحل:** إعادة تسمية مسودة الملك سليمان إلى `thk-solomon-hebrew` وتحديث كافة الروابط في مدرسة الحكمة العبرية (`sch-hebrew-wisdom.md`).

### الفئة C — مسودات مكررة لمفكرين معتمدين بـ slugs متباينة (6 حالات)

| المسودة المحذوفة | المعتمد المحفوظ | الإجراء وتحديث الروابط |
|---|---|---|
| `thk-taylor-charles` | `thk-charlestaylor` (`THK-0414`) | دمج المحتوى، حذف المسودة، وتحديث روابط تشارلز تايلور |
| `thk-wdilthey` | `thk-dilthey` (`THK-0377`) | دمج المحتوى، حذف المسودة، وتحديث روابط فيلهلم دلتاي |
| `thk-chomsky` | `thk-nchomsky` (`THK-0598`) | دمج المحتوى، حذف المسودة، وتحديث روابط نعوم تشومسكي |
| `thk-james-william` | `thk-james` (`THK-0004`) | دمج المحتوى، حذف المسودة، وتحديث روابط وليام جيمس |
| `thk-mbuber` | `thk-buber` (`THK-0103`) | دمج المحتوى، حذف المسودة، وتحديث روابط مارتن بوبر |
| `thk-aschutz` | `thk-schutz` (`THK-0382`) | دمج المحتوى، حذف المسودة، وتحديث روابط ألفريد شوتز |

### الفئة D — مسودات مكررة تم دمجها وحذف النسخة الأضعف (17 حالة)

| المسودة المحذوفة | المسودة المحفوظة المكتملة | الموضوع / الشخصية |
|---|---|---|
| `thk-rkahneman` | `thk-kahneman` | دانيال كانمان (Daniel Kahneman) |
| `thk-amacintyre` | `thk-macintyre` | ألاسدير ماكنتاير (Alasdair MacIntyre) |
| `thk-psinger` | `thk-peter-singer` | بيتر سينغر (Peter Singer) |
| `thk-bhooks` | `thk-hooks` | بيل هوكس (bell hooks) |
| `thk-anaess` | `thk-arne-naess` | آرني نايس (Arne Næss) |
| `thk-cgilligan` | `thk-gilligan` | كارول غيليغان (Carol Gilligan) |
| `thk-cmohanty` | `thk-mohanty` | شاندرا تالبادي موهانتي (Chandra Mohanty) |
| `thk-mmaltz` | `thk-maxwell-maltz` | ماكسويل مالتز (Maxwell Maltz) |
| `thk-mcsikszent` | `thk-csikszentmihalyi` | ميهالي تشيكسينتميهالي (Mihaly Csikszentmihalyi) |
| `thk-plevine` | `thk-peter-levine` | بيتر ليفين (Peter Levine) |
| `thk-dana` | `thk-deb-dana` | ديب دانا (Deb Dana) |
| `thk-dsiegel` | `thk-daniel-siegel` | دانيال سيغل (Daniel J. Siegel) |
| `thk-rschwartz` | `thk-richard-schwartz` | ريتشارد شوارتز (Richard C. Schwartz) |
| `wrk-structure-scientific-revolutions` | `wrk-kuhn-structure-revolutions` | بنية الثورات العلمية لتوماس كون (1962) |
| `wrk-self-compassion-neff` | `wrk-self-compassion` | التعاطف مع الذات لكريستين نيف (2011) |
| `wrk-emotional-intelligence-1995` | `wrk-emotional-intelligence` | الذكاء العاطفي لدانيال غولمان (1995) |
| `wrk-milgram-obedience-authority` | `wrk-obedience-to-authority` | الانصياع للسلطة لستانلي ميلغرام (1974) |

---

## 3. حالات التشابه البنيوي المشروع (لم تُلمس)

- **مدارس المظلة مقابل فروعها الفرعية**: مثل مدرسة الفينومينولوجيا العامة (`sch-phenomenology-existential`) مقابل الفينومينولوجيا التأويلية (`sch-phenomenology-hermeneutic`) — هذا تسلسل هرمي طبيعي عبر `edges: belongs_to`.
- **التقاطعات عبر الأنواع (Cross-Type)**: نفس المفهوم النظري يظهر كـ **تيار/فرع** (`br-`) و كـ **مفهوم** (`con-`) أو **أداة/تقنية** (`tec-`)، وهذا تصميم مقصود لخدمة زوايا المعرفة المتعددة في شبكة الأطلس.
