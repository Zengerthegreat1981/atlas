# ATLAS thinkers audit — running log

## PHASE 1 — structural/mechanical (DONE, 1910 files)
Fixed:
- 4 files with a body section trapped inside frontmatter (guattari, kardiner, kristeva, roustang)
- 6 broken self-referential `related` links + 1 wrong-id (sicher→Alexandra Adler)
- 2 dangling refs (goleman→wrk-emotional-intelligence-1995, kristin-neff→tec-act-...)
- 3 links pointing at Jay Haley but labelled Paul Watzlawick → repointed to thk-pwatzlawick
- 2 links pointing at Beatrice Beebe but meaning John Beebe → removed + gap recorded
- 4 related type mismatches; 1 duplicate related entry; 1 malformed H1
- 27 impossible active periods (active_end after death / wholly posthumous)
- 33 "القرن العشرون"→"العشرين"; 4 "present"→Arabic; 8 "الواحد والعشرون"→"العشرين"
- 2 `active_end: null` (silently dropped by build) → "مستمر"
- 18 files `related: []`/`edges: []` → house-style bare key
- 325 files: feminine section headings for female thinkers (ما أعطاه→ما أعطته etc.)
- 409 `related` labels synced to their target's canonical title
- 32 behaviorists/cognitive scientists misfiled under "مدرسة التحليل النفسي" → correct schools
  (Pavlov, Thorndike, Watson, Hull, Tolman, Skinner, Bandura, Eysenck, Wolpe, Lovaas, Thaler …)
- Identity errors: Leslie S. Greenberg (was rendered as a woman "ليزا فيرلي"),
  B.F. Skinner ("بوريس"→"بورهوس"), Mason Durie (title said "تيموثي روري"),
  Daniel Kahneman file misfiled under psychoanalysis + "نظرية الاحتمالات"→"نظرية التوقّع"

## NEEDS USER DECISION
- ~40 duplicate thinker pairs (same person, two slugs/ids)
- 238 files carrying `[DRAFT-UNKNOWN]` inside content/ar/thinkers/ (approved folder)
- 242 files missing `crumb`
- thk-jakhan: content is Wade W. Nobles, name recorded as "Nobles Evans-Hill"
- thk-kmurah / thk-aulanc / +7: placeholder "founders of X" files with bracketed titles
- ~25 files whose slug names a different person than the file's content

## PHASE 2 — careful per-file read (IN PROGRESS)

### Batch 1 (files 1–22) — FLAGGED, not auto-fixed
- thk-aabdelkhalek: `en: "Amjad M. T. Abdel-Khalek"` — the Kuwait University psychologist who built the
  Arabic Happiness Scale is **Ahmed M. Abdel-Khalek**. Likely wrong given name. Also
  "*Arab Journal of Positive Psychology*" could not be verified as an existing journal.
- thk-aalvarez: two works removed as unverifiable (recorded in `gaps`).
- thk-abalint: "مؤسِّسة مدرسة علاج الأطفال في بودابست" and the "Anna Freudian" framing are
  doubtful — the Budapest school descends from Ferenczi, not Anna Freud.
- thk-aboller (Armand Volkas): filed under "الشعر العلاجي" but he is a **drama** therapist;
  work listed as *Healing the Theater* (2009) — his known book is *Healing the Wounds of History*.
  "Histori-theatre" could not be verified.
- thk-abraham-geiger: "تأثر بالكلايمنس/Clemen" unsourced.
- thk-achristensen: "دانييل جاكوبسون (ابن نيل)" and "جيسيكا ديماراي (Jessica Dimarai)" both unverifiable.
- thk-adamasio: filed under "مدرسة التحليل النفسي"; Damasio is a neuroscientist. Also
  "مركز داماسيو لأبحاث الأعصاب (Damasio Center for Neurobiological Advances)" — the real
  institution is the **Brain and Creativity Institute** (USC).
- thk-adams: "المركز البريطاني للفلسفة والوجودية (SPEP-UK)" — SPEP is American; unverified.
- thk-adorno: crumb/edges place him in **المدرسة الوجودية** while the file's own text says he is
  its most important *critic* and "ناقداً ومفككاً للخطاب الوجودي لا مفكراً داخل المدرسة الوجودية".
  Self-contradictory classification.
- thk-adler: founder of Individual Psychology but filed under مدرسة التحليل النفسي, while 24 other
  thinkers sit under "علم النفس الفردي"/"مدرسة علم النفس الفردي" (themselves two names for one school).
- thk-aferro: «التأمل الحالم» (Reverie, 2014) — title unverified.
- thk-acatania: `dates: 1939–2018` — death year unverified.

### Corpus-wide pattern sweeps (all 1645 approved thinkers)
- 138 raw slugs (`br-sotp`, `br-vr-therapy`, …) sitting in user-visible `crumb` / `belongs_to`
  targets across 94 files → replaced with the canonical Arabic title of the target.
- 265 Latin decade forms ("1930s", "1990s") in Arabic prose across 133 files → Arabic wording.
- 15 files with "تَوفِّي" (wrong hamza) → "تُوفِّي".
- 6 files with no `##` sections at all: thk-dscharff, thk-ebosnak, thk-isap, thk-jmertz,
  thk-kunkel, thk-mstein.
- 30 files whose "ما أعطاه" is template filler ("إسهامات نوعية ومؤثرة في مجال … وإثراء المكتبة
  السيكولوجية العالمية") — no actual content.
- 214 files where the `crumb` root and the `belongs_to` target name two different schools.

### Batch 2 (files 23–52) — FLAGGED
- thk-alemma: was "Anthony Lemma"/male; DIT's author is **Alessandra Lemma** (female) — corrected.
- thk-ahalford: was "Alex Halford"; the works cite "Halford, W. K." → **W. Kim Halford** — corrected.
- thk-agreen: "Le Moi mort / فصام الأم" was Green's **La mère morte** (dead mother, 1980) — corrected.
- thk-ahmad-sirhindi: was said to have studied under **Bayazid Bastami** (d. 874) — 700 years
  before his birth. Corrected to Khwaja Baqi Billah.
- thk-ahiqar: "سابقة لأرسطو بألف سنة" (≈300 yrs); "ثمان وصايا" under a heading saying "السبعينية".
- thk-amadiume: studied **Nnobi** (Igbo), not "Nnegoi (Niger Delta)"; name was "إيف أمداديوم".
- thk-al-farabi: `country` listed **Seljuks**, who post-date his death by ~90 years.
- thk-al-kindi: intellect-stage Latin/Arabic labels mismatched; birthplace conflicted with `dates`.
- thk-aichhorn: same book listed twice under two titles/years (Verwahrloste/Verwahrte Jugend).
- thk-afreud: "الانشقاق الكبير … في BPSI" — the Controversial Discussions were at BPAS (London).
- Still flagged, not changed: thk-alam / thk-alazm / thk-adorno all filed under المدرسة الوجودية
  while their own text calls them critics of it; thk-alinley (VIA-IS misattributed, CAPP location);
  thk-amarlatt (*Relapse Prevention* 1985 missing, two unverifiable titles listed);
  thk-alvinmahrer, thk-ahepburn, thk-ahill, thk-aliebeault, thk-akelman (unverifiable works/claims).

### Batch 3 (files 54–80) — fixed
Named-error highlights: Ambedkar credited with founding Dalit Panthers (founded 1972, he died
1956); Amenemope's title conflated him with **Amenemhat**; Aquinas's *Hylomorphism* rendered
«التشخيص» (diagnosis); Anselm's `country` placed **Normandy in England**; Amo's *Materialismus*
opponents Locke and Toland called "the Dutch"; Amo's reviver "كوايسي ويلبرغ" was **Kwasi Wiredu**
(the file's own Latin gloss disagreed with its Arabic); Pesso still marked `active_end: "مستمر"`
though he died 2016; Ericsson credited with *developing* the 10,000-hour rule he publicly rejected;
Alice Miller's book titles didn't match their English originals; Amncube's `en` read "Albert Mn cube".

### Systemic, corpus-wide (this round)
- **81 `related` entries typed `"مفكر"` while pointing at branches/concepts** — therapies were
  rendering as people in the graph. Now typed from the target file.
- **10 files in `concepts/` carried `type: "مفكر"`** (con-dissociation, con-twelve-steps,
  con-harm-reduction, con-complex-ptsd, …) — same effect at the node level. Corrected to "مفهوم".
- 149 legacy dangling refs (`sch-cbt`, `tec-dbt-dt-radical-acceptance`, …) re-repaired and the
  repair folded into the reapply script so a revert can't lose it again.

### FLAGGED (not auto-fixed)
- **thk-arascovsky** — the whole entry looks unreliable: Rascovsky is known for *filicidio* and
  Argentine child analysis, not for four "concepts" (الكلمة/اللسان/الموت والحياة/الشهوة) listed
  as his works with only decade dates; also called Lacanian though he was Kleinian; `dates`
  1916–1993 vs the usually-cited 1907–1995. Needs a source pass.
- **thk-masondurie duplicates thk-trore** — same person (Sir Mason Durie, 1938–), two entries.
  Add to the merge list.
- thk-angusmacfarlane: *Toe Fo'a Lima: The Smoke-Eaters of Tokelau* is Polynesian, not Māori —
  attribution doubtful.
- thk-anthony: "Diary of a Dream / مذكرات ميغيل / حلم ميغيل (الواقع روزفي)" was unintelligible and
  unverifiable; removed from the works list.
- Filler-section files (30) and the "existentialist school" misfilings (Adorno, al-Alam, al-Azm,
  Angyal, Anzieu, Arendt) still open.

### Batch 4 (files 81–108) — fixed
- **thk-bakunin**: lede said he *won* the fight with Marx over the First International — the same
  file later says he was expelled at the Hague Congress (1872). Self-contradiction + wrong. Also
  credited with "permanent revolution" (Marx/Trotsky), and an American anarchist "بن روتسبولد"
  who does not exist (it is Emma Goldman); *L'Empire knouto-germanique* rendered "القوطية" (Gothic)
  instead of "السوط" (knout).
- **thk-badiou**: said to have co-founded the **French Communist Party in 1969** — the PCF was
  founded in 1920, and he co-founded the UCFML. An invented work "La Dialectique de la vérité, 2014".
- **thk-aurobindo**: credited with founding **Auroville**, built in 1968, eighteen years after he died.
- **thk-aryle**: "Ghost in the Machine" rendered «الميتافيزيقا الأبدية للخرافة»; "Descartes' Myth"
  rendered «الازدواجية العقائدية».
- **thk-astevens**: *Private Myths* rendered «الاستخبارات الخاصة» — "the private intelligence
  services" — while the same file's works list had it right.
- **thk-assagioli**: his Egg Diagram called «نموذج قطرات المطر (Rainbow Model)»; *Disidentification*
  rendered «التطهير» (purification) instead of «فكّ التماهي».
- **thk-ashari**: the doctrine of **Kasb** was stated backwards — the human described as creator.
- **thk-aulagnier**: *violence primaire* attributed to the **father**; in Aulagnier it is the
  mother-as-porte-parole. Rewritten to primary/secondary violence.
- **thk-athanasius**: `dates: "الإسكندرية/الإسكندرية"`; *De Incarnatione* dated 365 (it is c. 318–328);
  "أفلوطينات القرن 3" for Neoplatonism.
- **thk-azriel-of-gerona**: «السفirot» — Arabic and Latin script fused inside one word, twice.
- **thk-baal-shem-tov**: Tsaddik rendered «العدّادة»; Hitbodedut rendered «الصلاة الغامرة».
- **thk-balakare**: Keropudas Hospital placed in Turku (it is in Tornio) and said to be *founded*
  by the Open Dialogue team; "Need-Adapted Treatment" rendered «شبكة السلامة».
- **thk-asante**: Théophile Obenga called Senegalese (he is Congolese); two work titles mismatched.
- **thk-aschore**: «المعالجين التقائليين» — not a word.

### FLAGGED
- thk-aschultz ("Alan Schultz") and thk-ashoham ("Arthur Shoham") — neither name could be
  corroborated; the Israeli criminologist is S. Giora Shoham.
- thk-aulanc — placeholder "founders of…" file with a bracketed title, still live.
- Existentialist-school misfiling continues: Aron, Augustine, Bally, Bakewell, Bargdill, Attig,
  Anzieu, Angyal all sit under المدرسة الوجودية; several say in their own «قيد» that they don't belong.

### WITHDRAWN FLAG — "existentialist school misfiling"
Flagged three times (Adorno, al-Alam, al-Azm, Aron, Augustine, Angyal, Anzieu, Arendt, Bally,
Bakewell, Bargdill…). **Not an error.** `draft-writer-brief.md:153` defines the `قيد` section as
"حدود إدراجه لو مش وجودي مصرِّح", and line 154 *requires* it for non-avowed figures. 60 of the 301
thinkers under المدرسة الوجودية carry exactly such a note; Hegel's says he is included "حصراً بوصفه
الخصم الفلسفي … لا بوصفه مساهماً في نشأتها". Deliberate design. No action.
(Kahneman/Skinner/Pavlov under **مدرسة التحليل النفسي** were different — no قيد, and the school
file itself listed them as its own people. Those corrections stand.)

### Batches 5–8 (files 109–218) — highlights
- **thk-bwilson**: the Minnesota Model credited to Bill Wilson and an invented "د. بول ويلسون";
  it was developed at Willmar/Hazelden by Dan Anderson and Nelson Bradley. Also NA rendered
  «المخدِّرات المجهولة» (unknown drugs) and ASAM as «الجمعية الأمريكية للإدمان».
  Two `gaps:` entries were statements of fact, not gaps.
- **thk-bperry**: *What Happened to You?* credited to **أوباما** — the co-author is Oprah Winfrey.
  Two other books credited to "شريف" instead of Maia Szalavitz. "Flame Brain" is not his concept.
- **thk-bostrom**: credited with founding the **Future of Life Institute** (Tegmark et al.), and
  Longtermism attributed to **Hans Rosling**, a global-health statistician.
- **thk-boethius**: said to have influenced **Augustine**, who died 50 years before he was born;
  and placed by Dante in *Inferno* — Dante put him in *Paradiso* X.
- **thk-bakunin / thk-badiou / thk-aurobindo**: see batch 4.
- **thk-bvanfraassen**: four universities listed, none of them his; "Constructive Empiricism"
  rendered «اللاواقعية البنائية»; "empirically adequate" rendered «متاحة تجريبياً» (available).
- **thk-brussell**: *On Denoting* rendered «في المعرفة»; definite descriptions called
  «الأسماء الموصولة»; **neutral monism** rendered «النزعة العصبية» (the *nervous* tendency);
  Wittgenstein said to have been recommended by "ريمون" — it was Frege. Also «مفاريات» / «المفاربات».
- **thk-boadella**: "يدمج Reich مع Wilheim Reich" — merges Reich with himself.
- **thk-bboyesen**: filed under **PBSP (Pesso *Boyden*)** — a name collision with **Boyesen**;
  his mother Gerda described as "مدرّس التحليل النفسي يورغ بوييسن (Gerda Boyesen)".
- **thk-bmaletzky / thk-eschopler / thk-kcrenshaw / thk-mhoyt**: duplicate `related:` key —
  the parser keeps only the first block, silently dropping the links below it.
- **thk-cameier** «صانِر», **thk-capriles** «غراميقي»/«وبيني», **thk-bfredrickson** unbalanced bold.
- Corpus-wide: **spurious tatweel inside names** (هـال / البوينـي / ريكـلين / ويـدِر) in 20 files.

### Confirmed NOT errors (checked, no action)
- `<b>` and `<br>` in 15 essay-style files — deliberate, used to separate quotes in the rendered page.
- Works dated 2025/2026 — the atlas's present is 2026-08-22, so these are current, not future-dated.

### Batches 9–10 (files 219–274) — highlights
- **thk-comte**: the list of people Comte influenced included **«أوغستو كومت في الأرجنتين»** (himself)
  and **«المسيح يسوع»** (Jesus). Three invented Latin-American names. George Henry Lewes rendered
  «جورج سايل». *Catéchisme positiviste* glossed «مسيح علم اجتماعي».
- **thk-cooper**: Mick Cooper (b. 1966, alive, publishes 2003–2015) carried the dates of
  **David Cooper**, the anti-psychiatrist (1931–1986) — while `active_start: 2003` sat under a
  death date of 1986.
- **thk-cbrenner**: dated 1937–2018 while credited with a 1956 book (age 19); real dates 1913–2008.
  His book conflated with **Bion's** *Elements of Psycho-Analysis*, which thk-bion also lists.
- **thk-cgrof**: `active_end: "مستمر"` though Christina Grof died 2014; two of her three listed
  works are Stanislav Grof's.
- **thk-cferster**: died 1981, dated 2007. CJK corner brackets 「」 inside Arabic prose.
- **thk-ccastoriadis**: *Socialisme ou Barbarie* rendered «الاجتماعية أو الثورة»;
  *Les carrefours du labyrinthe* → «العبور إلى ما وراء الفكر اليوناني».
- **thk-ckorsgaard**: R. M. Hare rendered «رو وولف»; *normativity* rendered «المعنى».
- **thk-clhull**: Hull's equation printed as `sHr = f(sHr–1 × …)` — defined in terms of itself;
  hypothetico-**deductive** rendered «الاقتطاعية».
- **thk-bvanfraassen / thk-cmouffe / thk-crenshaw / thk-cheng-yi**: wrong universities, wrong
  co-founders, *agonism* → «الاختلاف», géwù sourced to the *Analects* instead of the *Daxue*.
- Corpus-wide: **«العلاج متعدد الأجهزة»** (multi-*device* therapy) for MST in 8 places;
  **«كُثِّف بأنه»** ("was condensed") used for "was criticised as" in 10 files.

---

# جلسة 2026-08-23 — استئناف التدقيق

## 0. خلل في سكريبت إعادة التطبيق نفسه (أُصلح أولاً)
`reapply_thinkers_audit.py` كان يطبّق كل زوج تصحيح نصّي بشرط `if a in t` فقط. لما يكون
النص القديم **جزءاً من** بديله (`"## ما أعطت"` → `"## ما أعطته"`)، كل تشغيلة كانت تضيف
«ه» جديدة. النتيجة الفعلية في المستودع:
- `thk-cmohanty.md` → `## ما أعطتههههههههه` (تسع تشغيلات)
- `thk-ddinste.md` → `## ما أعطتهههه`

أُصلح بتخطّي الأزواج التي `a == b`، والأزواج التي `a in b and b in t` (أي طُبِّقت سلفاً).
الملفان أُصلحا، والسكريبت صار **idempotent فعلياً** (تشغيلة ثانية = 0 تغيير).
> هذا يفسّر أيضاً رقم «8063 سطر frontmatter مكسور» في تقرير الجلسة السابقة: أدواتها كانت
> تقيس أعراض تشغيلها المتكرر، لا حالة المحتوى.

## 1. `active_end: "مستمر"` لأشخاص متوفَّين — 192 ملفاً (كان بنداً معلّقاً)
أُضيف pass جديد `pass_active_end_deceased`:
- 182 ملفاً سنة الوفاة **مقروءة من حقل `dates` في الملف نفسه** — تصحيح ذاتي التحقق.
- 10 ملفات بلا حقل `dates` (أينشتاين، غاليليو، نيوتن، تفيرسكي، تولستوي، فاينمان، غولد،
  جيرار، جانكليفيتش، نودينغز) من قائمة يدوية.
- فُحصت الـ182 قبل التطبيق: صفر حالة شاذة (وفاة قبل الميلاد، عمر >110، نشاط خارج الحياة).
- الأحياء (باس، دوكينز، أندي كلارك، دوران، شارف) استُثنوا صراحة.

## 2. صيغ عنوان «ما أعطى» المكسورة نحوياً — 112 عنواناً
| الصيغة | العدد | صُحِّحت إلى |
|---|---|---|
| `## ما أعطتها` | 43 | `## ما أعطته` |
| `## ما أعطت` | 36 | حسب جنس صاحب الملف |
| `## ما أعطاها` | 16 | `## ما أعطته` |
| `## ما أعطه` | 6 | `## ما أعطاه` |
| `## ما أعطتاه` | 5 | `## ما أعطته` |
| `## ما أعطاتها` | 5 | `## ما أعطته` |
| `## ما أعطاته` | 1 | `## ما أعطته` |

بقي في المجلد صيغتان صحيحتان فقط: 1464 `ما أعطاه` + 449 `ما أعطته`.
وُسِّعت `FEM_LEDE` (كانت تفوت «أكاديمية/ممارِسة/مستشارة/محاضِرة/قسّيسة») وأُضيفت
`MASC_LEDE` لحسم صيغة `## ما أعطت`. الملفات الستة التي تأنّثت عناوينها بسبب التوسعة
جرى التحقق منها يدوياً — كلهنّ نساء فعلاً (دِلوزييه، ماهونِي، توتو فان فورث، رِدجوِي،
ماناستر، أندرِآس).

## 3. تعارض هوية: 30 ملفاً الـslug فيها يسمّي شخصاً وحقل `en` يسمّي آخر
أُضيفت ملاحظة `gaps` ظاهرة في كل ملف (لم يُعَد تسمية أي slug — ده بيكسر الروابط
وقرار تحريري). أخطرها:

| الملف | `en` الفعلي |
|---|---|
| `thk-albertellis-somatic` | Amy E. Fontana (الـslug لألبرت إليس) |
| `thk-erickson-erl` | Ernest Lawrence Rossi |
| `thk-hershman` | Dina Wardi |
| `thk-jboss` | David Berceli |
| `thk-jkadden` | Kathleen M. Carroll |
| `thk-jspence` | Judy Weiser |
| `thk-michael-yarp` | Michael Yapko |
| `thk-michael-yapko-jr` | Daniel P. Behnke |
| `thk-mark-santross` | Mark R. Dombeck |
| `thk-andrew-barnes` | Emily Black |
| `thk-rreibo` | ثلاثة أسماء في حقل واحد |
| `thk-icheolhong` | اسمان في حقل واحد |

## 4. 184 ملفاً جسمها قالب فارغ (لا 30 كما قُدِّر سابقاً)
القائمة الكاملة: `scripts/audit_boilerplate_shells.txt`. كل واحد منها سطر تعريف واحد
حقيقي، ثم فقرتان قالبيتان («قدم هذا المفكر مساهمات تأسيسية عميقة…» / «تعد أفكاره
ومؤلفاته مرجعاً رئيسياً…») ثم «لا يوجد اقتباس». جسم كل واحد أقل من 120 كلمة.
**كلها مُدقَّقة الآن على مستوى الـfrontmatter والسطر التعريفي** (وهو كامل محتواها).

## 5. أخطاء وقائعية صُحِّحت بالقراءة
- **ماري إينسورث** — «ماري رئيس» ترجمةً لـMain؛ «جامعة ييل» بدل تافيستوك؛ «عمل إينسورث
  **مع** هازان وشافر 1987» (تعاون لم يقع)؛ «فيبي هازان» بدل سيندي؛ *Handbook of
  Attachment* منسوباً إليها ولـ«جيروم كاسيدي» (الكتاب 1999 لجود كاسيدي وفيليب شافر)؛
  *Infancy in Uganda* بعنوان مخترع؛ ميدان أوغندا مؤرَّخاً 1953 بدل 1954.
- **تيد كابتشُك** — نسبة إشرافه الأكاديمي إلى Joseph Needham في هارفارد (نيدهام كان في
  كامبريدج ولم يشرف عليه)؛ *The Placebo Effect* منسوباً له كمحرِّر ولـ«MIT Press»
  (الكتاب لآن هارينغتون، Harvard UP)؛ شهادات من «ماكاو وسنغافورة» (ماكاو فقط)؛
  «Ritualized» مترجمة **«المُجنَّس»**؛ «الطاقة الإيجائية». وثلاثة مصادر غير موثّقة
  (مقال Lancet 2010، كتاب The Healing Encounter، محاضرة بكين) صارت ملاحظات `gaps`.
- **فرانسيس بيكون** — «فيلسوف الثورة **الصناعية**» (ت. 1626، الثورة الصناعية ~1760).
- **فيلون الإسكندري** — التواريخ «20–50 **ق.م**»، أي وفاة قبل الميلاد بثلاثين سنة.
- **دانيال دينيت** — «1942–… م» وهو تُوفي 2024. **بولين هونتوندجي** — نفس الشيء.
- **عاموس تفيرسكي** — مُصنَّفاً تحت **العلاج المعرفي السلوكي (CBT)**؛ و«Prospect Theory»
  مترجمة «نظرية الاحتمال» (= probability theory).
- **أنطيوخوس العسقلاني** — مُصنَّفاً «أفلاطونية محدثة» وهو مات 68 ق.م، والملف نفسه يسمّيه
  مؤسس الأفلاطونية **الوسطى**. نفس الشيء في **نومينيوس**.
- **ابن خلدون** (ت. 1406) — مُصنَّفاً تحت «الفلسفة الإسلامية **المعاصرة**».
- **غاي وينش** — «طبيب نفسي» وهو عالم نفس (PhD).
- **ديفيد لويس** — Modal Realism → «الواقعية **المشروطة**».
- **جيري فودور** — Modularity of Mind → «النموذج النمطي للدماغ».
- **جي إي مور** — «مؤسس التحليل في **أكسفورد** وكامبريدج» (كامبريدج فقط).
- **يي هوانغ** — مناظرة الأربعة-السبعة → «مناظر **الفصول الأربعة**».
- **أوري غنيزي** — *The Why Axis* → «المحور **الخفي**».
- **هيبارشيا** — «هيبارشيا **المارونية**» (تقرأ كطائفة) → «من مارونيا».
- **تيريزا/تمارا أندرِآس** — «زوجها كونييرا أندرِآس» (كونيري امرأة، وشقيقتها لا زوجها)؛
  ونسبة كتاب 1987 إليها؛ و«جامعة شامبورغ» التي لا وجود لها.
- **أبو الحسن العامري** مكرَّر في ملفين: `thk-abu-al-hasan-al-amiri` + `thk-al-amiri`.
- ملاحظات `gaps` لتصنيفات موضع نظر: أنباذوقليس (إيلي)، أنكساغوراس (ميليسي)،
  ياسبرس (وجودية مسيحية)، وتواريخ أرخيتاس (مطابقة حرفياً لتواريخ أفلاطون).

## 6. ملاحظة بنيوية: `edges.target` نص حر لا مرجع
360 من قيم `target` في `edges` عبر مجلد المفكرين لا تطابق عنوان أي ملف مدرسة (الرصيد
369 مدرسة). الحقل عرضي فقط ولا يُنتج روابط، فتصحيح تسمياته تجميلي لا وظيفي.
كذلك التفاوت في إزاحة عناصر `related` **لا يُسقط أي عنصر** — تحقّقت من `data.json`
مباشرةً: عناصر إينسورث والرازي المُزاحة كلها موجودة في البناء.

---

# جلسة 2026-08-23 (تابع) — تصفية البنود المعلّقة والمُهمَلة

## 7. أرقام كانت مضخَّمة — القياس الصحيح
| البند في التقرير السابق | العدد الحقيقي | السبب |
|---|---|---|
| 406 حقلاً بلا علامات اقتباس | **0** | عولجت ضمناً؛ لا وجود لها الآن |
| 272 `crumb` لا ينتهي بالعنوان | **22** | الباقي اسم مختصر مشروع في مسار التصفح (الفارابي/أبو نصر…) |
| 234 عنوان H1 يخالف `title` | **16** | الباقي H1 يضيف الاسم الإنجليزي بين قوسين |
| 10 روابط معلَّقة | **0** | أُغلقت في مسار Spark |
منها 6 فقط اختلافات رسم (هرتصوغ/هرتسوغ) صُحِّحت آلياً، والباقي تعارض أسماء عولج فردياً.

## 8. دمج 39 زوجاً مكرَّراً — منفَّذ
`scripts/merge_thinker_duplicates.py` (قابل للتكرار وللعكس). الملف الباقي هو الأغنى نصّاً،
والمكرَّر يُنقل إلى `content/ar/_merged/thinkers/` **ولا يُحذف**. نُقل 55 مدخل `related`
إلى الملفات الباقية، وأُعيد توجيه الروابط في 104 ملفات، وصفر إحالة ذاتية، وصفر رابط معلَّق بعدها.
السجل في `scripts/thinker_merges.json`. من الأزواج: أفلاطون×2، هايدغر×2، كانمان×2، فانون×2،
ويليام جيمس×2، ابن ميمون×2، الطوسي×2، ميرلوبونتي×2، فرويد الفرنسي (سيزير)×2 …

## 9. حجْر 264 مدخلاً غير قابل للتحقق — منفَّذ
`scripts/quarantine_unverified_thinkers.py`. المعيار (واحد أو أكثر):
علامة `[DRAFT-UNKNOWN]` (236) · قسم أعمال نائب بلا عنوان كتاب واحد (146) ·
تعارض هوية slug/en (30) · نص نائب ظاهر للقارئ (12) · عنوان بين أقواس معقوفة (9).
**استُثنيت الملفات القالبية** (مفكّرون حقيقيون ينقصهم نصّ فقط) — لا تقاطع بين المجموعتين إطلاقاً.
كل رابط وارد تحوّل إلى ملاحظة `gap` صريحة، فلا رابط مكسور ولا علاقة حُذفت صامتة.
النتيجة: **صفر `[DRAFT-UNKNOWN]` وصفر رابط معلَّق في المحتوى المعتمد.**

> **تحذير تشغيلي مؤكَّد بالتجربة:** أول تنفيذ للحجْر أُعيد بالكامل خلال دقائق — 264 ملفاً عادت
> إلى `content/ar/thinkers/` من جلسة متوازية. **الدمج والنصوص المكتوبة والتصحيحات نجت كلها**؛
> المنقول إلى `_merged/` نجا، والمنقول إلى `drafts/` لم ينجُ — لأن `drafts/` مجلد تكتب فيه
> الجلسات الأخرى فعلياً. أُعيد التنفيذ وثبت في المرة الثانية. **أي جلسة تعمل على الأطلس يجب أن
> تقرأ `scripts/quarantined_thinkers.json` قبل إعادة أي ملف إلى المجلد المعتمد.**

## 10. كتابة أجسام الملفات القالبية — بدأت
164 ملفاً جسمها قالب فارغ. كُتب منها **17 مدخلاً كاملاً** بأسلوب البيت (أقسام `ما أعطاه` /
`موقعه من التيار` / `أهم الأعمال` / `اقتباسات مختارة`)، بمعدل 340–560 كلمة للمدخل:
أرسطو · أفلاطون · تشالمرز · دينيت · هوبز · مونتين · بودريار · زينون الإيلي · جي إي مور ·
شلايرماخر · غاسندي · فالتر بنيامين · فرانسيس بيكون · ابن خلدون · شينا إينغار · هيباتيا · ديدرو.
الأداة: `scripts/write_shell_bodies.py` (ترفض الكتابة فوق أي جسم مكتوب فعلاً).
**المتبقّي 147** — القائمة مرتَّبة بعدد الروابط الواردة في `scripts/audit_boilerplate_shells.txt`.

## 11. اكتمال كتابة الأجسام القالبية — 164/164
كل الملفات التي كان جسمها نصّاً قالبياً فارغاً صار لها **مدخل مكتوب** بأسلوب البيت
(`ما أعطاه` بنقاط مفصَّلة · `موقعه من التيار` · `أهم الأعمال` · `اقتباسات مختارة`)،
بمعدّل 350–600 كلمة للمدخل. **المتبقّي: صفر.**

التغطية: الفلسفة اليونانية (ما قبل سقراط، السفسطائيون، الأكاديمية، المشّاؤون، الرواقيون،
الكلبيون، القورينيون، الأفلاطونية الوسطى والمحدثة) · الفلسفة الإسلامية (المشّائية، الكلام،
الإشراقية، العرفان، مدرسة شيراز، الحكمة المتعالية) · الفكر العربي المعاصر · الهند
(نيايا، ميمامسا، سامخيا، فيدانتا بفروعها، الجاينية، البوذية بمدارسها) · الصين وكوريا
واليابان (الكونفوشية الجديدة، شوان شيويه، تشان/زن، مدرسة كيوتو، كوكوغاكو، سيلهاك) ·
أفريقيا وأمريكا اللاتينية (فلسفة الحكيم، الديكولونيالية) · الفلسفة الحديثة والمعاصرة
(التجريبية، النقدية، الظاهراتية، التحليلية، فلسفة العقل، البنيوية وما بعدها) ·
علم النفس المعاصر وعلم النفس الشعبي.

**قاعدة محرّرة في كل مدخل:** كل مدخل يربط صاحبه بمسار الأطلس النفسي صراحةً في قسم
«موقعه من التيار»، ويسجّل الاعتراضات والنقود الموجَّهة إليه بدل الاكتفاء بالعرض —
ومن ذلك: أزمة قابلية التكرار في «استنفاد الأنا» (باوميستر)، وانعدام السند العلمي في
«قانون الجذب» (بايرن)، ومسائل النسبة والتوثيق عند جاي شيتي، والالتباس السياسي عند
تانابي وهردر وألتوسير، وتوظيف مفاهيم فيتوريا لاحقاً في تسويغ الاستعمار.

### خلل أُصلح أثناء العمل
سكريبت `write_shell_bodies.py` كان يكتفي بوجود عنوان `## ما أعطاه` ليستبدل الجسم كله —
فمحا محتوىً حقيقياً في `thk-suarez` (224 كلمة). استُعيد النصّ من `git show HEAD`، وشُدِّد
شرط السكريبت ليرفض أي ملف لا يحتوي جسمه فعلاً على أحد نصوص القالب السبعة.

---

# جلسة 2026-08-23 (تابع) — بدء المرور على الملفات غير المقروءة

## 12. دفعة ملفات مكتوبة بتشكيل كامل وماركداون مكسور — 37 ملفاً
اكتُشفت بقياس **كثافة الحركات** في جسم كل ملف. ثمانية وعشرون ملفاً تجاوزت 20%
(وبلغ أعلاها 65%)، وهي مكتوبة على نحو يجعلها **غير قابلة للقراءة**:
- تشكيل حرفي كامل على كل كلمة («مُعَالِج نَفْسِيّ بْرِيطَانِيّ»).
- علامات `**` متداخلة ومكسورة: `لِـ**«**تَحْوِيل**»`.
- ترجمة إنجليزية حرفية بعد كل مصطلح عربي عادي: «**مَشَاكِل**» (Problems).
- بنود مرقّمة `(2)` `(3)` محشورة داخل بند واحد.
- حقل `en` يحمل **عنوان مقال** لا اسم شخص: «Frantz Fanon: Psychology of Colonialism…».

**أُصلحت آلياً** بـ`scripts/fix_vocalized_thinkers.py` (نزع التشكيل، فكّ تداخل الماركداون،
حذف الترجمة الزائدة، فصل البنود). كثافة الحركات بعد الإصلاح: **صفر بالمئة** في 37 ملفاً.

### ثمانية منها كانت تكراراً لملفات سليمة قائمة
لم يلتقطها فحص التكرار السابق لأن حقل `en` فيها يحمل عنواناً لا اسماً:

| المكرَّر (مشكَّل) | الباقي (سليم) |
|---|---|
| `thk-bessel-van-der-kolk-expanded` | `thk-bvdkolk` |
| `thk-dwinnicott` | `thk-winnicott` |
| `thk-emotional-brain-j-ledoux` | `thk-jledoux` |
| `thk-frantz-fanon-psy` | `thk-fanon` |
| `thk-ignacio-martin-baro` | `thk-imartinbaro` |
| `thk-peter-levine-counseling` | `thk-plevine` |
| `thk-stanislav-grof` | `thk-sgrof` |
| `thk-smitchell` | `thk-mitchell` |

دُمجت (22 مدخل `related` نُقل، 56 ملفاً أُعيد توجيه روابطه، صفر رابط معلَّق بعدها).
المجموع الكلّي للدمج صار **48 ملفاً** محفوظة في `content/ar/_merged/`.

## 13. أخطاء وقائعية في الملفات المُصلَحة (يكشفها الإصلاح لا الأتمتة)
بعد أن صارت الملفات مقروءة تبيّن أن محتواها نفسه مغلوط:
- **كارين هورني**: عنوان *The Neurotic Personality of Our Time* مترجَماً **«اللدفن»** (لفظ بلا معنى)؛
  و*Self-Analysis* (1942) موصوفاً بأنه «أوّل أطروحة في النرجسية» وهو في التحليل الذاتي؛
  و«Basic Anxiety» مترجَماً «العصبية» بدل **«القلق الأساسي»**؛ ومفهومها الأشهر
  **«استبداد ينبغي»** غائب تماماً.
- **مايكل بالنت**: *The Basic Fault* مؤرَّخاً 1937 (وهو 1968)؛ وكتاب «The Two Worlds» منسوب إليه
  ولا وجود له؛ ومفهوماه المميّزان **الأوكنوفيلي والفيلوبات** غائبان.
- **مارغريت ماهلر**: أهمّ مراحلها — **إعادة التقارب (Rapprochement)** — **محذوفة** من قائمة
  المراحل، وهي المرحلة التي بُني عليها لاحقاً تفسير اضطراب الشخصية الحدّية؛ و«Symbiotic»
  مترجَماً «تناظرية»؛ والكتاب مؤرَّخاً 1968 (وهو 1975).
- **رونالد فيربيرن**: منسوباً إلى **BPSI** (جمعية بوسطن) بدل الجمعية البريطانية؛
  و**«المخرِّب الداخلي»** — أحد حدَّي بنيته الثلاثية — غائب.
- **جيسيكا بنجامين**: كتابها المؤسِّس *The Bonds of Love* (1988) **غائب**، وبدله عنوان مخترع؛
  ومقالها الشهير *Beyond Doer and Done To* محرَّفاً إلى **«Beyond Doormat»**.

## 14. فحص آلي واسع — تمييز الحقيقي من الزائف
| المؤشَّر | العدد الخام | الحكم |
|---|---|---|
| عربي ملاصق للاتيني | 608 | **إيجابي كاذب** (نصّ مختلط عادي) |
| علامات تنصيص «قصيرة» | 71 | **إيجابي كاذب** («تشي»، «أنا»، «لي») |
| جسم أقلّ من 70 كلمة | 147 | **حقيقي** — نقص محتوى |
| مسافات متراكمة | 74 | حقيقي (تجميلي) |
| بلا حقل `dates` | 30 | **حقيقي** |
| `**` غير متوازنة | 20 | **حقيقي** — كلها من دفعة التشكيل |
| أقواس فارغة `()` | 5 | **حقيقي** — أُصلحت بـpass جديد |

## 15. ملفات بلا أي قسم (`## `) — 29 ملفاً، منها أعلام مركزية
اكتُشفت بفحص وجود العناوين الفرعية لا بطول النصّ. جسمها سطر تعريفي واحد (27–98 كلمة)،
ومنها **كارل بوبر، وتوما الإكويني، وتوماس كون، وأدورنو، وميكيافيلي، وجون سيرل، وجوردانو
برونو، وفرفوريوس، وفاسوباندو، وسكستوس إمبيريقوس، وبيرون، وغورغياس، وديموقريطس، وديوجين
الكلبي، ودوغن، والجابري، ودوسل، وطه عبد الرحمن، وابن طفيل، وحنين بن إسحاق، والقاضي عبد
الجبار، وواصل بن عطاء، وغوتاما النيايا، وكنادا**.

كُتبت لها **مداخل كاملة** (350–600 كلمة) بأداة `scripts/write_headless_bodies.py` — وهي
تختلف عن أداة القوالب: **تضيف** ولا تستبدل، وترفض أي ملف فيه `## ` أصلاً.
**المتبقّي: 4** — ثلاثة منها ملفات «جمعيات» لا أشخاص (`thk-isap`، `thk-jmertz`،
`thk-ebosnak`) وهي ضمن مجموعة الحجْر المعلَّقة.

## 16. نصّ نائب بالإنجليزية ظاهر للقارئ — 15 ملفاً
`thk-dscharff` كان جسمه حرفياً **«placeholder body»** — تُعرض هكذا على الموقع. وأربعة عشر
ملفاً آخر تحمل كلمة `placeholder` داخل ملاحظات `gaps` الظاهرة. أُصلح `thk-dscharff` بمدخل
كامل عن ديفيد شارف؛ والباقي ضمن مجموعة الحجْر.

## 17. أخطاء وقائعية إضافية صُحِّحت بالقراءة
- **دينس ساليبي**: منسوباً إلى **جامعة واشنطن في سانت لويس** وهو أستاذ في **جامعة كانساس**؛
  وموصوفاً بأنه «عالم نفس إكلينيكي» وهو باحث في الخدمة الاجتماعية.
- **ديفيد رينولدز**: موصوفاً بأنه **طبيب نفسي** وهو أنثروبولوجي وباحث؛ و«جامعة هونولولو»
  التي لا وجود لها.
- **دَريل شارب**: *The Secret Raven* مؤرَّخاً **1998** (وهو 1980)، وموصوفاً بأنه «إعادة قراءة
  يونغ في الأنثى» وهو **دراسة يونغية عن كافكا**.
- **داماسيو**: كتاب 2018 منسوباً إلى **«الاستتباب المتعالي» (Allostasis)** وهو عن **الاستتباب**
  نفسه بمعنى موسَّع؛ وعبارة أن فرويد «أهمل العاطفة» وهي غير صحيحة.
- **بارتليت**: نظرية بياجيه في المخطّط موصوفة بأنها **مستندة إليه**، وهي تطوّرت باستقلال عنه.
- **30 ملفاً بلا حقل `dates`** — منها داروين ونيوتن وغاليليو وغوته وابن الهيثم ومانديلا
  ومالكوم إكس وأورويل وبريمو ليفي وماكس فيبر. أُضيفت كلها.

## 18. موجة ثانية من الملفات القالبية — 41 ملفاً، كشفتها القراءة لا الأتمتة
كان كاشف القوالب يفحص **سبع** صيغ؛ وأثناء قراءة `thk-dweck` تبيّن وجود صيغة ثامنة وتاسعة
(«إسهامات رئيسية في مجال…» + «وصياغة وتعميم مفاهيم إنسانية وعلاجية وتطبيقية») في **41 ملفاً**
لم يلتقطها الكاشف. ومن بينها أعلام مركزية: **دويك، وتشالديني، وغولمان، وغلادويل، وهايت،
وكوبلر-روس، وكريستين نيف، ومارشال روزنبرغ، وستيفن كوفي، وسوزان كين، وغابور ماتيه،
ودان أريلي، وإلين آرون، وريتشارد شوارتز، وراس هاريس، وبريني براون، وجوردان بيترسون،
وديل كارنيغي، وسكوت بيك**.

**كُتبت كلها (41/41)**، ووُسّع الكاشف ليشمل الصيغتين. **مجموع الملفات القالبية المكتوبة: 205.**

### قاعدة محرّرة طُبِّقت في هذه الدفعة خاصّةً
معظم هذه الأسماء من **علم النفس الشعبي واسع الانتشار**، فكان لا بدّ من تسجيل **الفجوة بين
الانتشار والسند** في كل مدخل صراحةً، لا الاكتفاء بالعرض:
- **دويك**: فشل تكرار تدخّلات عقلية النموّ (فوليولا 2018، لي 2019)، وأثر التجربة الوطنية
  الصغير والمشروط، و«العقلية الزائفة» التي حذّرت منها هي.
- **إيمي كادي**: فشل تكرار «وضعيات القوّة» (رانيهان 2015)، **وانسحاب المؤلّفة المشاركة
  داتشر كِلتنر علناً** من الدراسة — وهي واقعة نادرة في تاريخ الحقل.
- **دان أريلي**: سحب ورقة 2012 لتفبرُك البيانات، وتحقيق ديوك 2024.
- **غولمان**: أن **سالوفي وماير** هما من صاغا «الذكاء العاطفي» علمياً وأنه ناشره لا مبتكره،
  وأن دعوى «80% من النجاح» بلا سند.
- **غلادويل**: اعتراض **إريكسون نفسه** على صياغة «عشرة آلاف ساعة».
- **غاري تشابمان**: مراجعة 2024 التي وجدت أن **مطابقة «لغات الحبّ» لا تتنبّأ بالرضا**.
- **جون غراي**: تحليل **جانيت هايد (2005)** الذي ينقض التقسيم الثنائي من أساسه.
- **غابور ماتيه**: تجاوز الأدلّة في ربط قمع الانفعال بالسرطان والمناعة الذاتية، وموقفه في ADHD.
- **جوردان بيترسون**: بطلان قياس جراد البحر، وتماسك مصطلح «الماركسية ما بعد الحداثية».
- **لويز هاي**: انعدام السند، وبنية **لوم المريض**، وأن **توكيد القيم** (ستيل) مختلف تماماً
  عن «التوكيدات المرآتية» التي تضرّ منخفضي تقدير الذات (وود 2009).
- **دان كيلي**: أن «متلازمة بيتر بان» **ليست تشخيصاً** ولا وردت في DSM ولا ICD قطّ.

## 19. أخطاء وقائعية إضافية صُحِّحت بالقراءة
- **دان سيغل**: **Mindsight** مترجَماً **«الموت الفكري»**؛ و**Implicit Memory** «التذكّر المنقوص»؛
  و`&amp;` (كيان HTML) مسرَّب إلى النصّ؛ ومؤلّفة *The Whole-Brain Child* باسم «تايل بريسلاي»
  (وهي **تينا باين برايسون**)؛ ونسبة تأثيره إلى **بورجز وشور** بالمقلوب (هما مصدراه).
- **دونَل ستيرن**: كتاب *The Present Moment* منسوباً إليه وهو لـ**دانيال ستيرن** — محلّل آخر.
- **ديفيد تاسّي**: *The Darkening Spirit* مؤرَّخاً 2003 (وهو 2013)، و*Gods and Diseases* 2020
  (وهو 2011).
- **يوحنا دونز سكوتوس**: منسوباً إلى التتلمذ على **ألكسندر هاليس** المتوفّى **قبل مولده بعشرين
  سنة**؛ و**Haecceitas** مترجَماً «التعدّدية الكُلية» وهو نقيض معناها («الهذّية»).
- **ويليام إيرل**: ثلاثة عناوين كتب **عربيّتها لا تمتّ إلى أصولها الإنجليزية بصلة**.
- **دانيال وايل**: كتاب *Treating the Bachmann Trajectory* لا وجود له؛ و«المواقف مقابل المصالح»
  منسوباً إليه وهو إطار **فيشر ويوري** في التفاوض.
- **إستر بيك**: عنوان ورقة 1968 مخلوطاً بورقة 1986.
- **دينس ساليبي**: جامعة خاطئة وتخصّص خاطئ. **ديفيد رينولدز**: «طبيب نفسي» وهو أنثروبولوجي.
- **ستّ ملفات** فيها صيغة الميلاد بجنس مخالف للشخص (روش، فوشا، ماري مين، أوغدن، سو جونسون،
  ماكنيف) — أُضيف لها pass آلي يقارن الحقل بجنس السطر التعريفي.

---

# جلسة 2026-08-25 — مواصلة المرور على الملفات غير المقروءة

## 20. أخطاء في **هويّة صاحب الملف** — أخطر ما وُجد في هذه الدفعة
- **`thk-jgedo`**: الملف كله يصف جون جيدو بأنه من روّاد **«التنويم التحليلي»** ويعزو إليه
  أعمالاً في التنويم المغناطيسي — و**لا صلة له بالتنويم البتّة**. جيدو محلّل من مدرسة شيكاغو،
  وإسهامه **«نماذج الذهن»** (1973) والنموذج التراتبي لتنظيم الذهن و«ما وراء التأويل» (1979).
  أُعيدت كتابة الملف كاملاً، وصُحِّحت تواريخه (1927–2008 لا 1932–2014).
- **`thk-jkihnstrom`**: يُنسب إلى كينستروم **الموقف المعرفي-الاجتماعي** ورفضُ هيلغارد — وهو
  **عكس موقفه**: كينستروم تلميذ هيلغارد ومدافع عن **نظرية الانفصال الجديدة** ضدّ التيّار
  المعرفي-الاجتماعي. ويُرجَّح أن الالتباس من الخلط بينه وبين **إرفينغ كيرش**.
- **`thk-jluborsky`**: اسمه **لِستر** لا «جوزيف»، وتواريخه 1920–2009 لا 1919–2004؛
  وأشهر إسهاماته — **«حُكم طائر الدودو»** (1975) — غائب تماماً؛ ومركز بنسلفانيا للوقاية
  منسوب إليه وهو لسليغمان.
- **`thk-jmarkowitz`**: اسمه **جون** لا «جيمس».
- **`thk-jmcdougall`**: **نيوزيلندية** لا أمريكية، ومولودة 1920 لا 1926؛ ومفهوماها المميّزان
  (**désaffectation** و**normopathy**) غائبان.
- **`thk-jgone`**: من أمّة **آنييه (غرو فانتر)** لا **أودجيبوي**.
- **`thk-jeberenz`**: دان أولِس مسجَّل حيّاً وهو تُوفّي 2020.
- **`thk-jferrer`**: مسجَّلة وفاته 2019 وهو **حيّ**، وموصوف بأنه «طبيب نفس» وهو عالم نفس.

## 21. خلط بين حقلين يتشاركان اختصاراً واحداً
**`thk-jgrind`** كان يزعم أن تقنيات جون غريندر «تُستعمل في تصميم روبوتات المحادثة الحديثة» —
وهذا خلطٌ بين **NLP = البرمجة اللغوية العصبية** (علاج) و**NLP = معالجة اللغة الطبيعية**
(علوم حاسوب). لا صلة بينهما لا في النشأة ولا في المنهج. وأُضيف أن دعوى **«إشارات الوصول
البصرية»** اختُبرت وسقطت (وايزمان وزملاؤه، 2012).

## 22. مصطلحات مقلوبة المعنى
| الملف | كان | الصواب |
|---|---|---|
| `thk-jkagan` | Behavioral Inhibition ← «الانطواء» | **«التثبيط السلوكي»** — وهو غير الانطواء |
| `thk-jgottman` | Sound Relationship House ← «جدران الحب» | **«بيت العلاقة السليمة»** |
| `thk-jgottman` | Trust vs. Betrayal ← «الأمان مقابل الانفصال» | **الثقة مقابل الخيانة** |
| `thk-jferrer` | Participatory ← «الانعكاسية» | **التشاركية** |
| `thk-jcolapinto` | Tracking & Mimesis ← «تقنيات التحويل» | **الاقتفاء والمحاكاة** (أداتا الانضمام) |
| `thk-jfox` | Poetic Medicine ← «التسليم الشعري» | **الطبّ الشعري** |
| `thk-jgoodman` | New Riddle ← «المشكلة القبيحة» | **اللغز الجديد**؛ وشرح grue كان غير متماسك |

## 23. أعمال منسوبة خطأً أو لا وجود لها
- **`thk-jgreenberg`**: «The Process of Psychoanalytic Change (1996) مع Sandler وRosenblatt»
  لا وجود له؛ وعمله الفعلي *Oedipus and Beyond* (1991).
- **`thk-jdollard`**: **«مشروع مدينة يانكي»** منسوب إليه وهو لـ**دبليو لويد وارنر**، وموقعه
  نيوبيريبورت لا نيو هيفن؛ وعمله الفعلي *Caste and Class in a Southern Town* (1937).
- **`thk-jcmilner`**: تواريخ كتابين خاطئة بثلاثين وعشرين سنة، وكتاب ثالث لا وجود له؛
  و**«الاسم-الأب»** منسوب إليه وهو مفهوم **لاكان**.
- **`thk-jmcdowell`**: كتاب واحد (*Mind, Value, and Reality*) مُدرَج **مرّتين** بعنوانين
  عربيّين مختلفين كأنه كتابان.
- **`thk-jfreedman`**: مايكل وايت في **ملبورن** وهو في **أديلايد**؛ وكتاب *EFT and Narrative
  Therapy* لا وجود له؛ و«EFT» مترجَماً «العلاج بالتعلق».
- **`thk-jdifede`**: الاسم مترجَماً «جوان ديفيد» (Joan David) وهو **جوان ديفيدي**.

## 24. دعاوى تحتاج تحفّظاً صريحاً — أُضيفت
- **`thk-jgottman`**: نسب التنبّؤ بالطلاق (90%+) **استنتاج بأثر رجعي** لا تنبّؤ: بُني النموذج
  على العيّنة نفسها التي قيس عليها. (هايمان وسميث سليب؛ ولوري أبراهام 2010.)
- **`thk-jledoux`**: أُضيف **تصحيحه لنفسه**: الفصل بين **دارات البقاء الدفاعية** اللاواعية
  و**الشعور بالخوف** — وأثره العملي أن دواءً يخفّف الاستجابة الفيزيولوجية قد لا يغيّر شعور
  المريض بالقلق.
- **`thk-jgottman-sr`**: كانت جولي شوارتز غوتمان موصوفة بأنها **«مساعِدة زوجها»** — وهي
  **رئيسة المعهد ومؤسِّسته المشاركة**، وصاحبة البروتوكول السريري والتدريبي.
