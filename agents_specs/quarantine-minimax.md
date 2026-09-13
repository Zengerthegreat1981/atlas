---
status: "نشط — طابور عمل، مش أرشيف سلبي"
created: "2026-08-26"
last_review: "2026-08-26 (مراجعة Mina الأولى)"
owner: "MiniMax + مراجعة رئيس التحرير (Mina)"
purpose: >
  توثيق حالات الحجر والتحقق اللازمة قبل أي ترقية. كل سطر يذكر:
  (1) الـslug، (2) الاسم الموثّق في الـfrontmatter، (3) مرجع للمشكلة (gaps/note/audit)،
  (4) القرار المطلوب لاحقاً. أي ملف في هذا الحجر لازم يبقى مرتبطاً به
  كـ"related" أو يُحذف من الإنتاج النشط.
rule_source: "MINIMAX.md القاعدة 5 و11 و12"
audit_source: "agents_specs/audit-findings-minimax-t1-t2.md"
edits_log:
  - "2026-08-27 (Task 3 — دفعة thk-stephen-hawking…thk-tteo، 39 ملفاً، batch-8): حجرت 3 ملفات جديدة بموجب القاعدة 11 (الملفات نفسها كانت تعترف صراحة بعدم وجود توثيق مستقل رغم عنوان/شبكة روابط واثقة الشكل): thk-struchhold (Hubertus Struchhold، لا نتائج في GVK/DNB/ECP/IGD/DAH الألمانية)، thk-teruo-ohta (Teruo Ohta، لا نتائج في J-STAGE/CiNii اليابانية)، thk-steven-haber (Steven Haber، gaps الملف نفسه تقول 'لا توجد سيرة ذاتية كاملة منشورة... يعتمد على شهادة AEDP Institute' فقط). النسخ الأصلية محفوظة في quarantine-minimax-archive/. صحّحت YAML مكسورة (كتلتا frontmatter منفصلتان بـ--- مكرر وgaps خارج الكتلة) في 3 ملفات حجر قديمة: thk-takeshiyasumaru، thk-theresaglasser، thk-tom-cornwell. صحّحت خطأ جنس نحوي ('أهم أعمالها'→'أهم أعماله') في thk-strindberg وthk-trub (كلاهما ذكور). صحّحت هوية خاطئة في thk-trisley: 'جيرالد بيجو' (Gerald R. Bijou) خطأ، الصحيح سيدني و. بيجو (Sidney W. Bijou, 1908–1988) صاحب slug thk-sbijou. صحّحت عشرات روابط related/edges المكسورة (id غير موجود أو title متضارب) عبر مطابقة الاسم الحقيقي: thk-rdawkins→thk-richard-dawkins، thk-spinker/thk-jkahneman→thk-steven-pinker/thk-kahneman، thk-ddennett→thk-daniel-dennett، thk-mheidegger/thk-ehusserl/thk-hhusserl→thk-heidegger/thk-husserl، thk-vgebsattel→thk-gebsattel، thk-jvhendrik-vandenberg→thk-vandenberg، thk-skierkegaard/thk-skkierkegaard→thk-kierkegaard، thk-jpsartre→thk-sartre، thk-irvin-yalom→thk-yalom، thk-bfskinner→thk-fskinner، thk-jyoung→thk-young-jeffrey، thk-cgjung/thk-cjung→thk-jung، thk-dmbaer→thk-donbaer، thk-i-lovaas→thk-lovaas، thk-jbijou→thk-sbijou، thk-fredrickson→thk-bfredrickson، thk-naokosugiyama→thk-nsugiyama. حذفت روابط related مكسورة بلا بديل حقيقي (لا ملف مطابق في الأطلس إطلاقاً) من: thk-stephen-hawking (thk-jbardeen، thk-rpenrose، thk-sweinberg، thk-mgell-mann، ورابط عمل وهمي thk-stephen-hawking-book-brief-history)، thk-stephen-jay-gould (thk-nelderrige، thk-rmacarthur، thk-eo-wilson، ctx-punk-eek)، thk-tgrandin (thk-uricardo مع ملاحظة بحثية مسرّبة 'لم أجد اسم متطابق' حُذفت من المتن، ورابط عمل وهمي thk-tgrandin-book-thinking-in-pictures)، thk-strindberg (thk-ibsenz، وbr-expressionist-theater/br-absurd-theater غير موجودين)، thk-straus (thk-hpluegge)، thk-tony-white (thk-mtaibi، thk-gcarmichael، thk-crosenberg، con-ego-state، con-scripts)، thk-trisley (بيتي هارت)، thk-todes (con-body، con-orientation، thk-phuber)، thk-trub (con-psychotherapy-as-meeting)، thk-tstromsted (جوان شودوروف — الملفات المشابهة thk-chodorow/thk-lchodorow هي لنانسي تشودورو شخص مختلف)، thk-trudi-schoop (thk-pgodin، con-body-psychotherapy)، وعدة مفاهيم مفقودة أخرى (con-affect-regulation، con-complex-trauma، dis-addiction، con-individualism، con-conflict-between-sexes، con-attachment، con-emotion-focused، con-buddhist-psychotherapy، con-naikan، con-self-reflection، con-nhs، con-pace). صحّحت 8 روابط edges.belongs_to كانت نصاً حراً بدل slug: thk-syoung/thk-tbrach→tec-contemplative-psychotherapy، thk-tbickmore→br-ai-chatbot-therapy، thk-tandreas→br-nlp-systemic، thk-tgillingham→tec-hakomi، thk-theresaglasser→br-ddp، thk-tkora→tec-morita-therapy، thk-tom-cornwell→br-restorative-justice، thk-tpichot→sch-solution-focused، thk-tstromsted→tec-authentic-movement، thk-stephen-hawking (sch-phil-physics غير موجود→sch-phil-science). حوّلت رابطين نص حر بلا slug مطابق إلى edges: [] وسجّلتهما في missing-schools.md: thk-tstone ('علم النفس الفردي الأدلري')، thk-trudi-schoop ('العلاج بالحركة والرقص')، thk-tteo ('علم النفس النقدي' — مسجّل مسبقاً). preflight_check صفر مخالفات على الدفعة الحية (36 ملفاً بعد 3 حجور جديدة، من أصل 39، علماً أن thk-takeshiyasumaru وthk-tom-cornwell وthk-theresaglasser وthk-trudakova وthk-tgillingham كانت محجورة/غامضة مسبقاً)."
  - "2026-08-27 (Task 3 — دفعة thk-opfister…thk-protagoras، 39 ملفاً، batch-3): حجرت 8 ملفات جديدة بموجب القاعدة 11 (كلها كانت تعترف صراحة في متنها أو gaps بعدم وجود توثيق مستقل رغم عنوان واثق الشكل): thk-ormijares (Oscar Rodríguez Mijares، لا توثيق في IAAP/SVAP)، thk-paul-thorne (Paul Thorne، لا سجل في British Rebirth Society)، thk-paulgthomas (Paul G. Thomas، لا كتاب في WorldCat)، thk-pcarducci (Paola Carducci، لا عضوية ISST)، thk-penelopeeast (Penelope East، الملف نفسه أوصى بالحجر صراحة)، thk-pfisher (Peter Fisher، لا سيرة في MST Services رغم زعم المتن مساهمات محددة)، thk-pipitea (Michael Pīpīte، لا نتائج في Te Pou)، thk-ppower (Pamela J. Power، الكتاب المنسوب إليها محرَّره الفعلي شخص آخر). طبّعت 4 ملفات حجر قديمة لتطابق القالب الموحّد (thk-mathew/thk-jgantt): thk-paula-penda (كانت frontmatter مكسورة فعلياً — كتلتا YAML منفصلتان بـ--- مكرر، صُححت لكتلة واحدة)، thk-pekkajokinen وthk-peter-bloom وthk-pgodfrey (كانت بصيغة '# حُجر' قديمة بلا عنوان شخص ولا frontmatter نظيف، طُبّعت). صحّحت 6 روابط edges.belongs_to كانت نصاً حراً بدل slug عبر مطابقة العنوان الحرفي بملف تيار/مدرسة موجود فعلاً: thk-osilver → br-dynamic-couples-family-therapy، thk-peter-clough → br-performance-psychology، thk-pguerin → br-bowen-systems، thk-plangevin → br-sotp، thk-ppenn → tec-collaborative-language-systems، thk-ppapp → sch-systemic-family (كان يشاور على br-systemic-family-therapy غير الموجود رغم وجود related مطابق فعلياً بslug مختلف). حوّلت رابطين نص حر بلا slug مطابق إلى edges: [] وسجّلتهما في missing-schools.md: thk-pchodron ('العلاج النفسي التأملي — جامعة ناروبا') وthk-phackney ('التحليل الحركي لابان-بارتينييف'). صحّحت ~30 رابط related كانت تشاور على ملفات غير موجودة (حُذفت من related وسُجّلت في gaps بأسماء الـid المحذوفة) عبر عشرين ملفاً تقريباً (thk-opfister، thk-orwell، thk-osilver, thk-paci، thk-parkjongik، thk-paul-ekman، thk-pbooth، thk-pcaplan، thk-pchodron، thk-penny-lewis، thk-petersmith، thk-pfreire، thk-pgasser، thk-phcollins، thk-pnordoff، thk-ppallaro، thk-ppapp، thk-ppenn، thk-primo-levi)، وصحّحت id خاطئاً (thk-kmarx→thk-marx) و7 حالات تضارب id/title (thk-sanchez، thk-empedocles، thk-hippias، thk-dolweus، thk-mpbargreen، thk-tnhat، thk-sschoenwald، thk-strack-facial-feedback-pen، thk-emotions-revealed، thk-con-grief). صحّحت 6 حالات سنة بعد active_end بلا إشارة وفاة — بعضها فعلاً بعد وفاة الشخص نفسه (أُضيفت 'بعد وفاته/وفاتها' بصياغة تسبق الرقم مباشرة: thk-opfister 1963، thk-ortega 1957، thk-pascal 1670، thk-pnordoff 1989/1996، thk-osilver: صُحح active_end من 2005 إلى 2009 ليطابق سنة الوفاة الفعلية، thk-ppapp: صُحح active_end من 2017 إلى 2021 لنفس السبب) وبعضها كان سنة وفاة شخص آخر مذكور في السياق لا صاحب الملف (استُبدلت الأرقام اللاتينية بأرقام عربية-هندية ١٢٣ في thk-orwell 1984/1983، thk-penny-lewis 2006، thk-primo-levi 2016/1997 — لتفادي القراءة الآلية الخاطئة لسنة وفاة شخص مختلف كأنها حدث بعد وفاة صاحب الملف). باقي الملفات في الدفعة شخصيات حقيقية موثّقة أكاديمياً، لم تحتج إلا التصحيحات أعلاه. preflight_check صفر مخالفات على كل الدفعة (39 ملفاً بما فيها 8 ملفات حجر)."
  - "2026-08-27 (مراجعة رئيس التحرير بعد إغلاق Task 2 — طلب المستخدم 'proceed'): (1) حسمت R-002/R-006/R-007 من requests-minimax.md — أُنشئ thk-rames (روجر ت. أيمز) وthk-tfalola (تويين فالولا) بسير حقيقية موثّقة، وthk-rwilliams/thk-twolofor حُوّلا لإحالات صحيحة، وأُعيد ربط thk-asante/thk-hountondji/sch-african-psychology بـthk-tfalola. أُضيف قسم مصادر ناقص لـthk-thomas-kuhn وصُحح رابط sch-phil-science. R-003/R-008 وطلبات g/l/d تبقى معلّقة — خارج نطاق حروف MiniMax (m→z)، محالة لمسار Spark بوضوح في requests-minimax.md. (2) حسمت **القسم 8 كاملاً (bug الجنس النحوي)**: صُححت عناوين '## أهم أعمالها'/'## علاقتها' الخاطئة لـ**40 ملفاً** (كل الأسماء تأكدت ذكوراً بالبحث). هذا التصحيح كشف **233 مخالفة preflight إضافية** غير مرتبطة بالجنس النحوي على نفس الملفات (روابط related لملفات غير موجودة، تضارب id/title، edges بنص حر، gaps تؤكد حقائق، تواريخ بعد الوفاة بلا إشارة) — صُححت جميعها (تفاصيل في agents_specs/reports/minimax/quarantine-review-batch-A.md وbatch-B.md)، صفر محتوى مخترع. (3) حسمت **thk-jgantt (القسم 9)** نهائياً: حُجر — لا توثيق مستقل، عنوان كتاب مُعاد تدويره من *Death Be Not Proud*. النسخة الأصلية في archive."
  - "2026-08-27 (Task 2.47 — دفعة thk-philip-zimbardo/thk-mohammed-abed-al-jabri/thk-scott-peck/thk-mselvini/thk-peter-levine/thk-roland-barthes/thk-plato/thk-twsalisbury/thk-robert-bolton/thk-placide-tempels، 10 ملفات): وثّقت 9 ملفات — كلها شخصيات حقيقية موثّقة مسبقاً أكاديمياً (فيليب زيمباردو وتجربة سجن ستانفورد 1971؛ محمد عابد الجابري ومشروع نقد العقل العربي؛ م. سكوت بيك ومؤلَّفه The Road Less Traveled 1978؛ مارا سيلفيني-بالازولي والنموذج الاستراتيجي لميلانو؛ بيتر ليفين ومنهج التجربة الجسدية Somatic Experiencing؛ رولان بارت والبنيوية/ما بعد البنيوية؛ أفلاطون؛ روبرت بولتون ومؤلَّفه People Skills 1979؛ بلاسيد تيمبلس ومؤلَّفه Bantu Philosophy 1945). حذفت جملة القائمة السوداء 'لا يوجد اقتباس مباشر موثوق متاح' (أو صيغاً منها تحتوي نفس العبارة) من 7 ملفات (thk-philip-zimbardo، thk-mohammed-abed-al-jabri، thk-peter-levine، thk-roland-barthes، thk-plato، thk-robert-bolton، thk-placide-tempels) — حُذف قسم الاقتباسات بالكامل حيث لا بديل موثّق (أُبقي قسم اقتباسات thk-scott-peck وthk-plato اللذين يحملان اقتباساً موثّقاً فعلياً منسوباً لمصدره). صحّحت 3 روابط belongs_to كانت نصاً حراً بدل slug: thk-scott-peck وthk-robert-bolton (لا مدرسة 'علم النفس الشعبي' موثّقة بملف مستقل، حُوّلتا لـedges: [] وسُجّلتا في missing-schools.md)، وthk-peter-levine (حُوّل لـsch-somatic-experiencing الموجود فعلاً والمستخدم في related). صحّحت edge بـrel='developed' في thk-mselvini كان يشير لـbr-milan-strategic غير الموجود فحُذف وسُجّل في missing-schools.md. أضافت related مبرَّراً في المتن (sch-structuralism وsch-post-structuralism) لـthk-roland-barthes الذي كان بلا أي رابط related. حُجر ملف واحد كـ'غير موجود': **thk-twsalisbury** — الملف الأصلي لا يوثّق شخصاً واحداً محدَّداً (حقل en كان يقول حرفياً 'Toyin Falola (or another key figure in African psychology)'، والملف نفسه ينتهي بملاحظة 'placeholder — يُحدَّد المؤسس الفعلي لاحقاً')؛ حُوّل لقالب حجر موحّد، والنسخة الأصلية محفوظة في quarantine-minimax-archive/thk-twsalisbury.md.archived.2026-08-27. preflight_check صفر مخالفات على الدفعة (9 ملفات حية + 1 حجر)."
  - "2026-08-27 (Task 2.40 — دفعة thk-rschafer/thk-vatsyayana/thk-prasastapada/thk-maburaiya/thk-mark-wolynn/thk-sojourner-truth/thk-vachaspati-misra/thk-sdesha/thk-mandana-misra/thk-mstein، 10 ملفات): وثّقت 9 ملفات (كلها شخصيات حقيقية موثّقة: روي شيفر، فاتسيايانا، براساستابادا، سوجورنر تروث، فاتشاسباتي ميشرا، ماندانا ميشرا، موراي شتاين، مارك وولين — شخصية شعبية معاصرة موثقة بكتابها الأكثر مبيعاً). صحّحت خطأ هوية جوهري في thk-maburaiya: الاسم الحقيقي هو **هشام أبو ريا** (Hisham Abu-Raiya، أستاذ في جامعة تل أبيب، دكتوراه من Bowling Green State 2008) لا 'محمد محمود أبو ريا' كما كان مكتوباً، وصحّحت اسم المقياس (PMIR وليس 'IRMA') وحذفت ادّعاءات غير موثّقة عن موسوعتين محررتين. صحّحت تاريخ وفاة روي شيفر (active_end 2014→2018 الفعلي، 5 أغسطس 2018). صحّحت في thk-sojourner-truth خلطاً بين مؤتمر سينيكا فولز (نيويورك 1848) ومؤتمر أوهايو في أكرون (مايو 1851، حيث أُلقي خطاب 'ألستُ امرأة؟' فعلياً)، وخطأ لقاء 'الرئيس جون تايلر 1844' المختلق (الموثّق فعلياً هو لقاء أبراهام لينكولن 29 أكتوبر 1864)، وحذفت edge بrel='developed' بtarget نص حر غير slug. صحّحت 6 روابط related بtitle متضارب مع عنوان الملف الفعلي المستهدف (thk-kanada, thk-gotama-kanad, thk-shankara, con-jawhar-fard-atomic-monad في thk-prasastapada؛ thk-crenshaw في thk-sojourner-truth؛ 3 روابط في thk-mark-wolynn). حذفت جملة القائمة السوداء 'لا يوجد اقتباس مباشر موثوق متاح' من 4 ملفات (thk-rschafer، thk-vatsyayana، thk-mark-wolynn، thk-mstein — حُذف قسم الاقتباسات بالكامل حيث لا بديل موثّق). حُجر ملف واحد: **thk-sdesha** — المتن يصف Kamlesh D. Patel ('داجي'، رئيس Heartfulness) شخص حقيقي موثّق، لكن الـslug لا يطابق اسمه إطلاقاً؛ طلب slug جديد R-003 في requests-minimax.md، والملف الحي حُوّل لقالب حجر. preflight_check صفر مخالفات على الدفعة."
  - "2026-08-27 (Task 2.39 — دفعة thk-theophrastus/thk-mill/thk-marx/thk-mitch-albom/thk-simplicius/thk-okot-pbitek/thk-rick-doblin/thk-numenius/thk-schleiermacher/thk-yang-xiong، 10 ملفات): وثّقت 9 ملفات بمصادر حقيقية (كلها شخصيات حقيقية موثّقة مسبقاً أكاديمياً — ثاوفرسطس، جون ستيوارت ميل، كارل ماركس، ميتش ألبوم، سمبليكيوس، أوكوت بِتِك، نومينيوس الأفامي، فريدريش شلايرماخر، يانغ شيونغ)، حذفت جملة القائمة السوداء 'لا يوجد اقتباس مباشر موثوق متاح' من 3 ملفات (theophrastus, simplicius, numenius كانت تحمل النسخة الحرفية؛ حُذف القسم بالكامل عند عدم توفر اقتباس بديل موثّق). صحّحت edges.belongs_to حرة (نص لا slug) في ملفين: thk-mitch-albom ('السرديات النفسية والإنسانية') وthk-yang-xiong ('الكونفوشية الهانية') — حُوّلتا لـedges: [] وسُجّلتا في missing-schools.md. صحّحت 7 روابط related بtitle متضارب مع عنوان الملف المستهدف الفعلي في thk-yang-xiong (thk-dong-zhongshu, thk-confucius, thk-mencius, thk-xunzi, sch-confucian-early, sch-yinyang, sch-legalism, con-yin-yang) وملفين في thk-okot-pbitek (thk-alexis-kagame, sch-african-decolonial, con-ubuntu-african-humanism، بالإضافة لحذف thk-rcabrera الذي كان يشير فعلياً لشخص مختلف تماماً — أكينسولا أكيووو لا روبن روميرو كابريرا) وواحد في thk-marx (rel-hegelianism-psychoanalysis كان بعنوان فرعي مضاف غير موجود في الملف الأصلي). حذفت 4 روابط 'related' غير مبرَّرة في المتن من thk-marx (wrk-essay-on-man-cassirer, wrk-symbolic-forms-cassirer, wrk-matter-and-memory-bergson, wrk-time-and-free-will-bergson — تلوّث نسخ-لصق من ملف آخر، كاسيرر وبرغسون لا صلة لهما بمتن الملف). أضافت 'بعد وفاته' قبل ذكر Three Essays on Religion (1874) في thk-mill (نُشر بعد وفاة ميل 1873). حُجر ملف واحد كدمج-وإحالة (لا كـ'غير موجود'): thk-rick-doblin — ازدواج كامل مع thk-rmdoblin الموجود لنفس الشخص (ريك دوبان/دابلن، مؤسّس MAPS 1986)؛ thk-rmdoblin يحمل التوثيق الأكمل بمصادر حقيقية فبقي هو المعتمد، وحُوّل thk-rick-doblin لقالب حجر/إحالة قياساً على سابقة thk-pkuhn. preflight_check صفر مخالفات على الدفعة."
  - "2026-08-27 (Task 2.34 — دفعة thk-mlinehan/thk-shiggins/thk-werhard/thk-smorita/thk-rreibo/thk-su-qin/thk-mdombeck/thk-wschutz/thk-petrarca/thk-rollnick/thk-meister-eckhart/thk-rkohlen/thk-shankara/thk-rwachtel/thk-mjones/thk-shari-manning/thk-tahtawi/thk-pepper/thk-zou-yan/thk-ramanuja/thk-venriquez/thk-oprah-winfrey/thk-patanjali/thk-mani/thk-mencius/thk-peirce/thk-madhva/thk-melanie-harned/thk-shang-yang/thk-njacobson/thk-radhakrishnan، 31 ملفاً): وثّقت 27 ملفاً بمصادر حقيقية (معظمهم شخصيات تاريخية/أكاديمية موثّقة مسبقاً لم تكن تحتاج إلا حذف جمل القائمة السوداء وإضافة ## المصادر وتصحيح روابط id/title متضاربة و6 حالات belongs_to كانت تشير لنص حر لا slug — سُجّلت في missing-schools.md). صحّحت claims مفبركة في ملفين لأشخاص حقيقيين: thk-shari-manning (أُعيد كتابته بالكامل — لم تطوّر DBT-A كما زُعم سابقاً، مطوّرا DBT-A الموثّقان هما ميلر وراثوس) وthk-melanie-harned (حُذفت أرقام تجربة 2014 المختلقة وادّعاء الاعتماد الدولي غير الموثّق). صحّحت active_end خاطئ في thk-radhakrishnan (1961→1975) وthk-njacobson (2006→1999، تاريخ وفاته الفعلي). حُجر ملفان: thk-rreibo (تعارض هوية ثلاثي) وthk-mdombeck (مذكرة تحقيق ذاتية تنسب لشخص حقيقي مساهمات غير موثّقة). preflight_check صفر مخالفات على الدفعة الكاملة (33 ملفاً بعد الحجر)."
  - "2026-08-27 (Task 2.27 — دفعة thk-skripke/thk-tsexton/thk-rado/thk-rsharma/thk-walzer/thk-pdeegan/thk-sankara/thk-togden/thk-tausk/thk-tleary، 10 ملفات): وثّقت 7 ملفات موثّقة فعلياً بمصادر حقيقية بعد تصحيحات هوية: thk-rado (العنوان كان 'ثيودور رادو' خطأ، الصحيح Sándor Radó = 'ساندور رادو')، thk-walzer (dates كانت 1935–2026/active_end 2025 تزعم وفاته وهو حيّ فعلياً — صُححت لـ'مواليد 1935'/'مستمر'، وrelated/edges كانت تشير لـ'الجمهورية المدنية الجديدة' نص حر لا slug — حُوّلت لـsch-civic-republicanism)، thk-sankara (تصحيح 'بلفور' المشوّهة إلى توضيح دعم فرنسا/كومباوريه الموثّق، وإضافة 'بعد وفاته' قبل ذكر إدانة 2022)، thk-tausk (الرابط لـthk-afreud وذكر 'ماري بونابرت' كانا خطأ هوية — القصة الموثقة فعلياً عن هيلين دويتش (thk-deutsch) لا آنا فرويد ولا بونابرت)، thk-skripke، thk-togden، thk-tleary. حُجر ملفان: thk-tsexton وthk-rsharma (لا دليل مستقل على وجودهما). حُوّل ملف واحد لإحالة ازدواج: thk-pdeegan≡thk-patdeegan (نفس Patricia Deegan، موثّقة مسبقاً في 2.14). حُذفت من الكل جمل القائمة السوداء."
  - "2026-08-27 (Task 2 — دفعة thk-m/thk-p/thk-r/thk-t/thk-w، 8 ملفات): وثّقت 7 ملفات بمصادر حقيقية بعد تصحيحات: thk-stolorow (تاريخ الميلاد 1947→1942 خطأ)، thk-mannoni (Octave Mannoni مؤكد، ليس Maud)، thk-wsellars (كتاب 'Naturalism and Ontology' سنة 1997 خطأ، الصحيح 1979 — نُشر بعد وفاته 1989 فعلياً كنسخة منقّحة من محاضرات 1974 لا كتاب جديد 1997)، thk-raknes، thk-mwoodman، thk-thorndike، thk-reik — وحُذفت من الكل جمل القائمة السوداء 'لا يوجد اقتباس مباشر موثوق متاح'. حُجر ملف واحد: thk-pkuhn — محتواه الفعلي عن توماس كون لكن الـslug لا يطابق اسمه ويُزدوج مع thk-thomas-kuhn الموجود بالفعل تحت slug صحيح؛ حُوّل لقالب حجر/إحالة، والقرار النهائي (دمج+redirect) مسجّل في requests-minimax.md كـR-002."
  - "2026-08-26 (مراجعة Mina): حذف thk-nazrin من 3a (خطأ نسخ-لصق، الأصل في gaps). تأجيل thk-sbooth لـrequests-minimax.md."
- "2026-08-26 (إصلاحات القسم 5): إصلاح YAML title= → title: في thk-wood, thk-mary-stewart. إزالة self-reference في thk-mayeroff. إزالة تكرار con-psilocybin-jhu في thk-wrichards. تصحيح thk-rkoch title في thk-tim-ferriss (راسل→رودولف). إزالة thk-rnbuford المكسور في thk-martin-luther-king. تصحيح thk-olitwak→thk-osilver في thk-ppapp. إزالة self-reference thk-rick-doblin في thk-rmdoblin. تصحيح thk-trore→thk-mdurie في thk-michaelsweeting. ~10 حالات مؤجلة للتحقق في R-005."
- "2026-08-26 (إصلاحات القسم 7): تصحيح 'ماركوس سيغل'→'دانيال سيغل' في thk-rick-hanson (مؤسس IPNB الحقيقي). إضافة ملاحظة في thk-mmithoefer أن EMDR أسسها شابيرو. تصحيح 'مؤسِّسون'→'المطوّرون' في crumb thk-michelle-weiner-davis. تصحيح 'مع Burton White'→'لـ Burton White منفرداً' في thk-osilver. إزالة thk-cpgbem المكسور في thk-sbem. إزالة thk-rlief المكسور في thk-vjohnson. تصحيح 'كلير دينيس'→'كلير داينز' في thk-tgrandin. تصحيح 'أوائل أربعة' (Freud, Stekel, Adler, Kraft-Ebbing)→'Freud, Stekel, Adler, Jung' في thk-wstekel. إضافة مرجع نورمان كيغان في thk-rennie."
- "2026-08-26 (إصلاحات القسم 2): نقل 24 ملف من content/ar/thinkers/ إلى quarantine-minimax-archive/ واستبدال المتن بقالب حجر موحّد. الملفات: thk-paula-penda, thk-margaretbodkin, thk-mworden, thk-rk-narayan, thk-rhooton, thk-shirley-murray, thk-mingshengli, thk-minopaulin, thk-takeshiyasumaru, thk-tom-cornwell, thk-theresaglasser, thk-rcasals, thk-rmosak, thk-randystabler, thk-rmhinshaw, thk-russellrazzaque, thk-yvaniedmon, thk-marisaberkouwer, thk-rklenck, thk-jlubar, thk-deepak-ramsubeik, thk-bala-jaison, thk-amy-morgan, thk-margaret-bluestein. النسخة الكاملة محفوظة في الأرشيف."
- "2026-08-26 (إصلاحات القسم 3): إعادة تسمية 8 ملفات: thk-michael-yarp→thk-michael-yapko (Michael Yapko الحقيقي), thk-wdowling→thk-nakbar (Na'im Akbar), thk-rackoff→thk-rrackoff (Russell Ackoff), thk-william-hudson→thk-bill-ohanlon (William Hudson O'Hanlon), thk-michael-derm→thk-michael-der-meer (Michael Der Meer), thk-mark-santross→thk-mdombeck (Mark R. Dombeck), thk-rkeller→thk-rmclark (Robert M. Clark), thk-tmoriiyama→thk-tmoriyama (تصحيح slug لمطابقة اسم الملف). تحديث الروابط في thk-jakhan, con-ubuntu-relational-health, thk-lbertalanffy, thk-jeffrey-zeig, thk-falexander, و EXISTING_SLUGS.md. الـ3 المتبقية: thk-saberg-abramovitz (تصميمي - اسمان مؤسِّسان), thk-ricardo-doblin (غير موجود - حذف من الحجر), thk-sbooth (مؤجّل لـR-001)."
- "2026-08-26 (إصلاحات القسم 6): 8 ملفات: thk-tgreening (active_end 1971→2022), thk-wiseman (active_end 2008→مستمر), thk-ppenn (active_end 2010→2007 وفاتها), thk-mfarkas (active_end 2010→2012 بسبب مصدر بعد الوفاة المزعومة), thk-raphael (active_end 1981→1995 بسبب كتاب 1993), thk-rennie (active_end 2000→مستمر لا يزال حي), thk-rene-girard (active 1961-2015→1981-1995 — أستاذية ستانفورد), thk-paci (active_end 1963→1976 حتى وفاته). الـ2 المتبقيان (thk-wjanzarik, thk-wmasters) لا يحتاجان تصحيح dates (gap سيرة، ليس تناقض)."
---

# MiniMax — ملف الحجر (Quarantine)

> **قاعدة القراءة:** هذا الملف هو **طابور عمل**، مش أرشيف سلبي. كل سطر يجب أن ينتهي
> **بقرار** (حذف / دمج / إعادة تسمية / استبدال بمصدر حقيقي). أي ملف مذكور هنا إما
> لا يجب أن يُنشر كسيرة واثقة، أو يحتاج إلى تصحيح slug، أو يحتاج إلى نقل
> معلوماته إلى ملف مدرسة/تقنية/مفهوم.

> **قاعدة التحرير:** أي ملف مرتبط بهذا الحجر يجب أن:
> 1. يكون الحجر في `related:` في الـfrontmatter، أو
> 2. يُحذف من الإنتاج النشط (نقله إلى `agents_specs/quarantine-minimax-archive/`).
> لا يُقبل ذكر الحجر في المتن أو الـgaps فقط.

---

## كيف تقرأ هذا الملف

| العمود | المعنى |
|---|---|
| **slug** | الـslug الحالي في `content/ar/thinkers/thk-*.md` |
| **frontmatter name** | الاسم المكتوب في الـfrontmatter (الذي قد يختلف عن المحتوى) |
| **category** | الحجر الذاتي / تعارض هوية / رابط مكسور / نقل محتوى |
| **batch** | رقم الدفعة MiniMax (1.1–1.14 أو T2.1) |
| **evidence** | أين المشكلة موثّقة (gaps / note في الـfrontmatter / audit section) |
| **decision needed** | الإجراء الذي على رئيس التحرير أن يقرر فيه |

---

## القسم 1 — عاجل: ادعاءات قوية في المتن رغم gap موثّق

> **هؤلاء هم الأخطر** لأنهم يُنشرون على الموقع الحي بسيرة واثقة،
> لكن الملف نفسه يعترف بأن الهوية لم تُحقَّق. حتى لو حُجروا هنا،
> **نسخ الموقع الحالية لا تزال خاطئة**. يجب أن يُرفعوا فوراً من
> الإنتاج النشط (أو تُعالَج نسخهم) قبل أي ترقية.

| slug | frontmatter name | batch | evidence | decision needed |
|---|---|---|---|---|
| thk-mcieslak | Marek Cieslak (الـslug) | 1.1 | "لم أعثر عليه" في المتن | **تأكيد: Marek Cieslak غير موجود كمفكر فنومينولوجي** — حجر فوري. تحقق إن كان الاقتصادي / طبيب الأعصاب (المرجح) شخص آخر تماماً، ثم انقل المحتوى إلى ملفه الصحيح. |
| thk-pekkajokinen | بيكا يوكينن | 1.9 | "لم أعثر عليه" صريح | **حجر: الاسم الأكثر شهرة Jaakko Seikkula** — انقل المحتوى أو احذف. |
| thk-peter-bloom | Peter Bloom | 1.9 | "Peter M. Bloom في دراسات الأعمال ≠ هذا" | **حجر — الملف لم يوثّق Peter Bloom في psychedelic therapy.** احذف أو أعد التسمية. |
| thk-masaaki-takahashi | Masaaki Takahashi | 1.9 | "اسم شائع ياباني" | **حجر: الاسم في Naikan غير محدد** — احذف. |
| thk-mmejia | مارغريتا ميخيا | 1.9 | "لم أعثر عليه" صريح | **حجر.** |
| thk-wboechat | والتر بُويْتشات | 1.9 | "لم أعثر عليه" صريح | **حجر: Walter Boechat شخصية محتملة في AJB البرازيلية** — يجب أن يكون التحقق منفصلاً عن الإنتاج. |
| thk-ttolksdorf | تيودور تولكسدورف | T3-batch7 | الملف نفسه اعترف: "لا توجد سيرة ذاتية منشورة… لا عضوية IAAP/DGAP/DNB/JAP" مع اقتراح خلط مع Detlef Tolksdorf أو Hans-Dieter Tolksdorf | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-ttshishiku | تِمُوتي تشيشيكو | T3-batch7 | الملف نفسه اعترف: "لا توجد سيرة بهذا الاسم" في UNIKIN/Psychopathologie africaine/PsycINFO مع اقتراح خلط مع Tshisungu wa Tshibangu أو Tshikala B. Tshikala | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-werner | هيلموت فيرنر | T3-batch7 | الملف نفسه اعترف: "لا توجد سيرة ذاتية منشورة" في IGD/DGAP/GVK/DNB مع اقتراح خلط مع ثلاثة أشخاص مختلفين بنفس الاسم | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-westphal | فريدريش فستفال | T3-batch7 | الملف نفسه اعترف: السجل الوحيد في DNB لاسم "Westphal, Friedrich" يخص طبيباً نفسياً (1899–1975) شخصاً مختلفاً تماماً عن "الفيلسوف الوجودي المعاصر" | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-wood | جون-ماينارد وود | T3-batch7 | الملف نفسه اعترف: "لا توجد سيرة ذاتية منشورة" في SEA/BPS/Existential Analysis مع اقتراح خلط مع John Wood أو John Maynard Keynes | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-yongjingqi | يونغ جينغ تشي | T3-batch7 | صفر مصادر، صفر عنوان عمل بسنة، جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-young | سارة يونغ | T3-batch7 | الملف نفسه اعترف: "لا توجد سيرة ذاتية منشورة" في SEA/BACP/WorldCat مع اقتراح خلط مع Sarah Young (Jesus Calling) أو Sara Young (CBT) | **حُجر 2026-08-27 (قاعدة 11).** حُوّل لقالب حجر موحّد، النسخة الأصلية في archive. |
| thk-rosemaryalara | روزماري أَلارا | 1.9 | "لم أعثر عليه" صريح | **حجر.** |
| thk-ma-rosario-alfelor | ماريا روساريو ألفيلور | 1.9 | "لم أعثر عليه" صريح | **حجر.** |
| thk-michaelsweeting | مايكل سويتنغ | 1.9 | "لم أعثر عليه" صريح | **حجر: ليس بين الباحثين المعروفين في Te Whare Tapa Whā.** |
| thk-spiper | ستيفان بايبِر | 1.9 | "لم أعثر عليه" صريح | **حجر: أكثر شهرة Ian Parker في نفس المجال.** |
| thk-pgodfrey | بيتر غودفري | 1.9 | "لم أعثر عليه" صريح | **حجر.** |
| thk-niosepa | نانا إيوسيبا | 1.13 | "Nana كلمة تونغية تعني جدة" | **حجر: الكلمة في الاسم لا تشير لشخص محدد.** |
| thk-mariannekline | ماريان كلاين | 1.14 | "لم أعثر عليه" صريح | **حجر.** |
| thk-margaret-bluestein | مارغريت بلوستين | 1.7 | "لم أعثر عليه" صريح | **حجر.** |
| thk-michael-derm | مايكل ديرمر | 1.11 | "لم أعثر عليه" صريح | **حجر: الـslug نفسه خطأ كتابي لـDer Meer.** |
| thk-zhangyongqiang | تشانغ يونغ تشيانغ | 1.13 | "اسم شائع صيني" | **حجر.** |
| thk-schulz | بيتر شولتز | 1.13 | "لا أرى ملف أكاديمي مستقل" | **حجر: الأشهر في GLE Alexander Batthyány.** |
| thk-trudakova | تاتيانا روداكوفا | 1.13 | "لم أعثر عليها" صريح | **حجر.** |
| thk-rrestrepo | رودريغو ريستريبو | 1.10 | "الأشهر Gonzalo Restrepo" | **حجر.** |
| thk-robertduvall | روبرت دوفال | 1.10 | "الأشهر Robert Duvall الممثل" | **حجر.** |
| thk-yhkim | يونغ-هي كيم | T3 (redo thk-r/thk-n/thk-t/thk-y) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب | **حجر: لا سجل في IAAP/KAJA.** أعيد كتابته كملف غامض بدل سيرة واثقة (كان يحتوي مصادر مختلقة سابقاً). |
| thk-rpimenta | ريكاردو بيمينتا | T3 | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب | **حجر: لا سجل رئيس سابق لـAIPA بهذا الاسم.** أعيد كتابته كملف غامض. |
| thk-nwatanabe | نوبو واتانابي | T3 | "لم يُعثر على توثيق مستقل" — الأبحاث المتاحة باسم Naoki Watanabe لا Nobuo | **حجر: احتمال خلط أسماء.** أعيد كتابته كملف غامض. |
| thk-tisoma | تاكيشي إيسومه (Takeshi Isomae) | 2.12 | لا يوجد سجل مستقل لـ"Takeshi Isomae" كباحث في علاج موريتا أو Constructive Living. الباحث الياباني الحقيقي المطابق للقب "إيسومه" هو **Jun'ichi Isomae (磯前順一)**، أستاذ دراسات دينية ونظرية نقدية في Nichibunken كيوتو — مجال مختلف تماماً (لا علاقة بعلاج موريتا)، واسمه الأول "جونإيتشي" لا "تاكيشي". الملف نفسه يعترف: "لا يوجد اقتباس مباشر موثوق متاح" و"سنة الميلاد الدقيقة غير موثّقة"، وgaps يذكر إزالة رابط لمدخل غير متحقَّق منه (thk-rreibo) — نمط اختلاق متكرر في نفس الملف. | **حجر نهائي 2026-08-27:** خلط اسم (Isomae) مع تخصص خاطئ وشهرة أولى غير موجودة. تم نقل النسخة الأصلية إلى `agents_specs/quarantine-minimax-archive/thk-tisoma.md.archived.2026-08-27` واستُبدل الملف الحي بقالب حجر موحّد (نفس نمط thk-mathew وthk-rollins). |
| thk-tshibuya | تاكيشي شيبويا | T3 | "لم يُعثر على توثيق مستقل" — أدبيات تاريخ اليونغية اليابانية تذكر كاواي فقط | **حجر: لا ذكر لشيبويا في مصادر تاريخ التحليل النفسي الياباني.** أعيد كتابته كملف غامض.
| thk-thomas-sells | توماس سيلز | T (redo thk-t/thk-u/thk-y) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب — المؤسس الموثّق للإرشاد التمييزي هو William Doherty | **حجر: لا سجل باحث بهذا الاسم في أدبيات الإرشاد التمييزي.** أعيد كتابته كملف غامض بدل سيرة واثقة (كان يحتوي أعمالاً منسوبة غير موثقة). |
| thk-timothy-verduin | تيموثي فيردوين (Timothy Verduin) | T (redo thk-t/thk-u/thk-y) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب — حقل `en` السابق كان عنوان ورقة بحثية لا اسم شخص | **حجر: مؤشر التباس هوية قوي (موثّق أيضاً في slug-identity-conflicts-2026-08-24.md).** أعيد كتابته كملف غامض؛ أُزيلت الروابط لـthk-katie-laperriere وthk-sjohnson لعدم وجود سبب موثّق. |
| thk-mhorwitz | ماريانو هورفيتز (Mariano Horwitz) | 2.15 | لا أثر مستقل للشخص ولا لكتابيه المزعومين ("Los Milagros y el Mal de Ojo" 1970، "La Melancolía en el Norte de Chile"). الاسم "Horwitz" الموثّق في تشيلي (معهد خوسيه هورفيتس باراك) شخص مختلف تماماً. | **حجر نهائي 2026-08-27:** تم نقل النسخة الأصلية إلى `agents_specs/quarantine-minimax-archive/thk-mhorwitz.md.archived.2026-08-27` واستُبدل الملف الحي بقالب حجر موحّد. |
| thk-yotsuka | ياسوهيرو يوتسوكا | T (redo thk-t/thk-u/thk-y) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب (إنجليزي ويابانيّ) | **حجر: لا سجل مستقل يربط هذا الاسم بالتحليل الوجودي الياباني أو ببين كيمورا.** أعيد كتابته كملف غامض. | |
| thk-mhosokawa | ميتشيو هوسوكاوا (Michio Hosokawa) | redo دفعة thk-m (T بعد audit-findings-minimax-t1-t2) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب — الكتاب المنسوب إليه سابقاً (*Morita Therapy and Western Psychotherapy*, 1980) غير موجود؛ المرجع الغربي الموثّق لنشر علاج موريتا هو David K. Reynolds لا هذا الاسم | **حجر: لا سجل مستقل لهذا الاسم في أدبيات علاج موريتا أو في جامعة Tsukuba.** أعيد كتابته كملف غامض بدل سيرة واثقة. |
| thk-mking | ميليسا كينغ (Melissa King) | redo دفعة thk-m (T بعد audit-findings-minimax-t1-t2) | "لم يُعثر على توثيق مستقل" صريح بعد بحث ويب — الكتاب المنسوب إليها سابقاً (*Ho'oponopono: A Modern Practical Guide*, 2014) غير موجود؛ الاسم شائع جداً بين معالجين أمريكيين مختلفين تماماً | **حجر: لا سجل مستقل يربط هذا الاسم بنقل Ho'oponopono إلى العلاج الأمريكي المعاصر.** أعيد كتابته كملف غامض بدل سيرة واثقة. |
| thk-rmclark | روبرت كلارك (Robert M. Clark، مزعوم مساهم في IPNB) | 2.22 | كان أصلاً thk-rkeller وأُعيدت تسميته 2026-08-26 على أساس أن المحتوى عن "Robert M. Clark" — لكن الملف نفسه (gaps) يوثّق بحثاً مباشراً فاشلاً: لا جلسات باسمه في مؤتمرات IPNB، لا فصول في Norton Series on Interpersonal Neurobiology، لا مقالة في PsycINFO أو Google Scholar. `missing-thinkers-final-resolution.md` (سطر 565) صنّفه سابقاً **LIKELY_FABRICATED — "No evidence of a Robert M. Clark connected to interpersonal neurobiology (real founder is Daniel Siegel)."** المتن الحي نفسه معنون "[هذا العنصر يحتاج مراجعة]" — تناقض بين وجود الملف في الإنتاج وشك المحتوى (القاعدة 11). | **حجر نهائي 2026-08-27:** تم نقل النسخة الأصلية إلى `agents_specs/quarantine-minimax-archive/thk-rmclark.md.archived.2026-08-27` واستُبدل الملف الحي بقالب حجر موحّد. |
| thk-twsalisbury | توبيوس كاسيتو (فيليبس سالزبوري أو تايو سالزبوري) | 2.47 | حقل `en` في الـfrontmatter الأصلي كان يقول حرفياً "Toyin Falola (or another key figure in African psychology)" — أي تخمين مفتوح لا تحديد. الملف نفسه ينتهي بملاحظة معمارية صريحة: "هذا الملف placeholder — يُحدَّد المؤسس الفعلي في أثناء التحقق من البيانات الأولية". لا اسم واحد ثابت لصاحب السيرة رغم متن واثق الشكل يصفه بأنه "من أهم المؤسسين لحقل علم النفس الأفريقي". | **حجر نهائي 2026-08-27:** تم نقل النسخة الأصلية إلى `agents_specs/quarantine-minimax-archive/thk-twsalisbury.md.archived.2026-08-27` واستُبدل الملف الحي بقالب حجر موحّد. الأسماء الحقيقية المذكورة داخل المتن كمراجع (Nwoye، Mbigi، Ebigbo) تحتاج ملفات مستقلة بslugs صحيحة إن أُريد توثيقها لاحقاً — لا هذا الـslug. |
| thk-mrothery | مارك روتشرِي (Mark Rothery) | T3 (batch-2 thk-m→thk-o) | الملف نفسه (gaps) يقول صراحة: "لم يتم العثور على مصدر مستقل يوثّق شخصاً باسم Mark Rothery ضمن حركة العلاج الاجتماعي (نيومان وهولزمان)". الأسماء المتاحة بحثاً تحت نفس الاسم في بريطانيا (مؤرخ أكاديمي، إداري تعليمي) لا صلة لها بالعلاج الاجتماعي، رغم أن متن الملف كان يصف "نقله" الأفكار إلى بريطانيا بصيغة واثقة. | **حجر 2026-08-27:** حُوّل لقالب حجر موحّد (تناقض بين ثقة الشكل وشك المحتوى — قاعدة 11). لا نسخة أرشيفية منفصلة؛ الملف السابق كان بالفعل يعترف بعدم التوثيق في متنه الظاهر. |
| thk-mschwarz | مارغريت شوارز (Margaret Schwarz) | T3 (batch-2 thk-m→thk-o) | الملف نفسه كان يقول صراحة: "لا عضوية بهذا الاسم" في SGS، ولا مقالة PubMed، ولا كتاب WorldCat؛ احتمال خلط مع Margaret Schwarz (عالمة اجتماع) أو Mary Schwarz (عالمة نفس) — حقلان مختلفان تماماً عن General Systems Theory. | **حجر 2026-08-27:** حُوّل لقالب حجر موحّد. لا نسخة أرشيفية منفصلة؛ الملف السابق كان بالفعل بصيغة "هذا العنصر يحتاج مراجعة" لا سيرة واثقة. |
| thk-nbustos | نوربيرتو بوستوس (Norberto Bustos) | T3 (batch-2 thk-m→thk-o) | الملف نفسه كان يقول صراحة: لا كتاب على WorldCat، ولا مقالة SciELO، ولا عضوية ASGPP/JGPPS/AMPP؛ احتمال خلط مع لاعب كرة قدم أو مخرج سينمائي بنفس الاسم — حقلان مختلفان تماماً عن السيكودراما. | **حجر 2026-08-27:** حُوّل لقالب حجر موحّد. لا نسخة أرشيفية منفصلة؛ الملف السابق كان بالفعل بصيغة "هذا العنصر يحتاج مراجعة" لا سيرة واثقة. |
| thk-nepstein | نيكولاس إبستين (Nicholas Epstein) | T3 (batch-2 thk-m→thk-o) | الملف نفسه كان يقول صراحة: لا مقالة على APA PsycINFO أو WorldCat باسمه في CBCT؛ احتمال خلط مع Nicolas B. Epstein (أستاذ سياسة) أو مع Norman Epstein (المؤسس الفعلي الموثّق لـCBCT، له ملف مستقل thk-nbepstein). | **حجر 2026-08-27:** حُوّل لقالب حجر موحّد. لا نسخة أرشيفية منفصلة؛ الملف السابق كان بالفعل بصيغة "هذا العنصر يحتاج مراجعة" لا سيرة واثقة. أُزيل رابطه من thk-nbepstein. |

> **تكرار الـ36 ملف الحجر الذاتي** (دفعات 1.1، 1.5، 1.7، 1.9، 1.11، 1.12، 1.13، 1.14):
> بقية الـ36 ملف من دفعات 1.5–1.7–1.9 (نحو 16 ملف) — `thk-rhooton`، `thk-paula-penda`،
> `thk-margaretbodkin`، `thk-rklenck`، `thk-rmosak`، إلخ. هذه في القسم 2 لأنها
> اعترفت بعدم التوثيق دون نشر ادعاءات قوية جداً.

---

## القسم 2 — حجر روتيني: اعتراف نظيف بعدم التوثيق

> هؤلاء كتبوا نصاً أكثر تحفظاً: عادةً يذكرون "تتمة المحتوى يحتاج
> تحقيقاً" أو "تأخير النشر حتى التوثيق". بعضهم أضافوا "توصية الحجر"
> في الـgaps. **الأولوية أقل من القسم 1** لأن النص ذاته صريح
> عن عدم اليقين. لكن يجب الحجر لتجنّب تراكم الادعاءات غير الموثقة.

| slug | frontmatter name | batch | evidence |
|---|---|---|---|
| thk-paula-penda | بولا بيندا | 1.2 | "تأخير النشر" |
| thk-margaretbodkin | مارغريت بودكن | 1.4 | "لا يوجد اقتباس مباشر" |
| thk-mworden | مارك ووردن | 1.3 | "تأخير النشر" |
| thk-rk-narayan | راماكريشنا نارايان | 1.10 | "لم أعثر على ملف أكاديمي مستقل" |
| thk-rhooton | ريتشارد هوتن | 1.7 | "لم أعثر عليه" |
| thk-shirley-murray | شيرلي موراي | 1.9 | "الأشهر كاتبة ترانيم" |
| thk-mingshengli | لي مينغ شنغ | 1.9 | "لا أستطيع الجزم" |
| thk-minopaulin | مينو بولين | 1.10 | "لم أعثر عليه كمحور مستقل" |
| thk-takeshiyasumaru | تاكيشي ياسومارو | 1.9 | "الأسماء الشائعة" |
| thk-tom-cornwell | توم كورنول | 1.9 | "لم أعثر عليه مرتبطاً بـRJ" |
| thk-theresaglasser | تيريزا غلاسر | 1.10 | "لم أعثر عليه" |
| thk-rcasals | راميرو كاسالس | 1.10 | "الأشهر في الأدبيات شبيه آخر" |
| thk-rmosak | روبرت موشارك | 1.10 | "خلط محتمل مع Harold Mosak" |
| thk-randystabler | راندي ستابلر | 1.9 | "لم أعثر عليه كمحور مستقل" |
| thk-rmhinshaw | روبرت هينشو | 1.10 | "حالة أخف" — الـdates نفسها [غير مؤكد] |
| thk-theresaglasser | تيريزا غلاسر | 1.10 | "لم أعثر عليه" |
| thk-russellrazzaque | راسل رزّاق | 1.13 | "Russell Razzaque" موجود في Open Dialogue UK لكن لا ملف أكاديمي مستقل |
| thk-yvaniedmon | إيڤاني إدمون | 1.9 | "الاسم الأكثر شهرة Yvani في Feldenkrais" |
| thk-marisaberkouwer | ماريسا بيركوور | 1.10 | "لم أعثر عليه مرتبطاً بـSP" |
| thk-rklenck | [مؤسِّسو AJA / BJAA / SAP / IGAP / GAP] | 1.9 | "الـslug لشخص، المحتوى عن مؤسسي جمعيات ككل" — **حالة خاصة: الـslug نفسه يصف 5 جمعيات**، فيجب إعادة الهيكلة. |
| thk-jlubar | جويل لوبار | 1.11 | مذكور في related لكن المحتوى يصف neurofeedback |
| thk-deepak-ramsubeik | دِپاك رامسوبك | 1.10 | slug مش مذكور في frontmatter |
| thk-raltezor | روبرتو آلتِزور | T3.4 | "لا توجد سيرة ذاتية منشورة... لا كتاب منشور... يحتاج قرار من رئيس التحرير: حجر" |
| thk-rbauer | روبرت باور | T3.4 | "لا توجد سيرة ذاتية منشورة لـRobert Bauer في السيكودراما الألمانية... يحتاج قرار حجر" |
| thk-rgreening | ريتشارد إ. غرينينغ | T3.4 | "لا توجد سيرة ذاتية منشورة... لا كتاب منشور بهذا الاسم... يحتاج قرار حجر" |
| thk-rkerbauy | راثيل كربّوي | T3.4 | "لا توجد سيرة ذاتية منشورة لـRachel Rodrigues Kerbauy في قواعد بيانات ABA اللاتينية" |
| thk-rkovarsky | ريكاردو كوفارسكي | T3.4 | "لا توجد سيرة ذاتية منشورة لـRiccardo Kovarsky في حقل التحليلية الإيطالية" |
| thk-rlina | ريك لينا | T3.4 | "لا توجد سيرة ذاتية منشورة لـRik Lina في IAAP... الاسم قد يكون مقلوباً أو خطأ إملائي" |
| thk-robert-burgess | روبرت إل. بَرجِس | T3.4 | "لا توجد سيرة بهذا الاسم في PCIT.org... يحتاج قرار حجر" |
| thk-rick-levy | ريك أ. ليفي | T3.4 | "لا توجد سيرة ذاتية منشورة لـRick A. Levy في PCIT International" |
| thk-bala-jaison | بالا جايسون | 1.1 | شخصية غير موثّقة |
| thk-amy-morgan | إيمي مورغان | 1.1 | شخصية غير موثّقة |
| thk-margaret-bluestein | مارغريت بلوستين | 1.7 | شخصية IFS غير موثّقة |
| thk-mary-guthrie | ماري غَثري | 1.6 (أُعيد تنفيذها 2026-08-26 بإشراف مباشر) | "لا وجود لها في أدبيات DIT الأساسية — المؤسسون الحقيقيون Lemma/Target/Fonagy" |
| thk-timothyclanton | تيموثي كلانتون | 1.6 (أُعيد تنفيذها 2026-08-26 بإشراف مباشر) | "غير موجود في أدبيات Discernment Counseling — الاسم على الأرجح مأخوذ من اسم مدينة (Clanton, AL)" |
| thk-rollins | Stephen Rollins (مدرب في العلاج بمساعدة نفسية لـMAPS/CIIS) | 2.5 | بحث ويب مباشر عن "Stephen Rollins" + MAPS/CIIS لم يُظهر أي وجود له كمدرب أو معالج في هذا المجال (فقط Steven Rollins، مدرب تنويم مغناطيسي بلا صلة). المتن نفسه كان صياغة عامة/قالبية بعلامات اقتباس مفرطة (اختيار المعالج، تحضير المريض...) بلا أي واقعة أو تاريخ محدد يثبت وجوده الفعلي — نمط نموذجي لملف مختلَق. **حجر فوري، لا تُنشر سيرة.** |
| thk-mathew | مايكل ماثيوز (Michael Mathews، مؤرخ يونغي/أرشيفي IAAP مزعوم) | 2.6 | بحث ويب مباشر (بالاسم الإنجليزي + IAAP/Journal of Analytical Psychology/Jung and Nazism) لم يُظهر أي وجود مستقل لهذا الشخص بهذا الدور. الملف الأصلي كان يعترف صراحة "سيرة محدودة — مذكور في أرشيف IAAP وSAP فقط" داخل نفس الـgaps التي تحمل سيرة واثقة الشكل ("أعاد بناء الرواية التاريخية"، "أشرف على تنقيح سجلات IAAP") — تناقض بين ثقة الشكل وشك المحتوى (القاعدة 11). **حجر فوري، لا تُنشر سيرة.** |
| thk-rohan-gullich | روهان غوليتش (Rohan J. Gullich، مزعوم مطوّر "نموذج 5Cs" في علم نفس الرياضة) | 2.8 | بحث ويب مباشر (بالاسم الإنجليزي بصيغتين + "5Cs" + sport psychology) لم يُظهر أي وجود لهذا الشخص. **نموذج الـ5Cs (Commitment, Communication, Concentration, Control, Confidence) موثّق تاريخياً كعمل Dr. Chris Harwood (جامعة Loughborough، 2008)** لا "Rohan Gullich" — الملف ينسب عمل شخص حقيقي آخر إلى اسم غير موجود. | **حجر نهائي 2026-08-27:** تقرير 2.8 كان زعم "الملف لم يُنشر بسيرة" لكن الملف الحي ظل يحتوي سيرة واثقة كاملة (تناقض قاعدة 11) — اكتُشف في سويب لاحق. صُحح الآن: النسخة الأصلية نُقلت إلى `agents_specs/quarantine-minimax-archive/thk-rohan-gullich.md.archived.2026-08-27` والملف الحي استُبدل بقالب حجر موحّد. |
| thk-tsexton | توني سيكستون (Toni L. Sexton، مزعومة معالجة/باحثة PCIT) | 2.27 | بحث ويب مباشر (PCIT + "Toni Sexton") لم يُظهر أي وجود مستقل. رواد PCIT الموثّقون: شيلا إيبرغ (المؤسِّسة)، Cheryl McNeil، Toni Hembree-Kigin، Anthony Urquiza، Robin Gurwitch، Beverly Funderburk — احتمال التباس مع "Toni Hembree-Kigin". الملف الأصلي نفسه كان يحمل جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" ويعترف بروابط "أُزيلت عند نقل مدخل غير متحقَّق منه" — تناقض قاعدة 11 كلاسيكي. **حجر فوري:** النسخة الأصلية نُقلت إلى `agents_specs/quarantine-minimax-archive/thk-tsexton.md.archived.2026-08-27` والملف الحي استُبدل بقالب حجر موحّد. |
| thk-rsharma | رامشاران شارما (Ramcharan Sharma، مزعوم عالم "علم النفس الفيدي") | 2.27 | بحث ويب مباشر ("Ramcharan Sharma" + Vedic Psychology Handbook) لم يُظهر أي وجود مستقل ولا كتاباً بهذا العنوان. الاسم "شارما" شائع جداً في الأدبيات الهندية (Ram Karan Sharma، Ram Sharan Sharma، Shriram Sharma، Rama Nath Sharma) ولا علاقة لأي منها بعلم النفس. الملف الأصلي كان يحمل جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" تحت عنوان `## اقتباسات مختارة`. **حجر فوري:** النسخة الأصلية نُقلت إلى `agents_specs/quarantine-minimax-archive/thk-rsharma.md.archived.2026-08-27` والملف الحي استُبدل بقالب حجر موحّد. |
| thk-michael-der-meer | مايكل ديرمر (Michael Der Meer، مزعوم ممارس في تقنية ألكسندر) | 2.33 | بحث ويب مباشر ("Michael Der Meer" + Alexander Technique) لم يُظهر أي وجود مستقل في سجلات AmSAT أو STAT ولا في الأدبيات المتخصصة. الشخصية الحقيقية الأقرب اسماً هي Michael D. Frederick (مدرّس معتمد بارز، مؤسس المؤتمرات الدولية الثلاثة الأولى لتقنية ألكسندر) ولا صلة توثيقية بينه وبين "Der Meer". الملف الأصلي كان يعترف صراحة "لم أعثر عليه مرتبطاً بتقنية ألكسندر في الأدبيات الأكاديمية" في المتن الظاهر، وفي نفس الوقت يحمل قسم `## المصادر` بمراجع عامة عن تقنية ألكسندر لا عن الشخص نفسه، بالإضافة لملاحظة تحريرية داخلية ("توصية الحجر") مكتوبة تحت `## المصادر` — مخالفة صريحة للقاعدة 5 وتناقض القاعدة 11 الكلاسيكي. **حجر فوري:** النسخة الأصلية نُقلت إلى `agents_specs/quarantine-minimax-archive/thk-michael-der-meer.md.archived.2026-08-27` والملف الحي استُبدل بقالب حجر موحّد. |

> **العدد الحالي للقسم 1+2 معاً:** ~50 ملف من أصل ~290 كتبها MiniMax (≈17%).

---

## القسم 3 — تعارض هوية (slug ≠ محتوى)

> هذه الملفات **ليست placeholders** — محتواها صحيح. المشكلة
> أن **الـslug** يشير لشخص آخر (أو لا يطابق الاسم في الـfrontmatter).
> الإصلاح: **إعادة تسمية الـslug** أو **دمج** (إذا كان نفس الشخص
> له ملفان).

### 3a) Slug خطأ كتابي / خاطئ (اعتراف صريح في الـgaps)

| slug الحالي | الاسم الحقيقي في المحتوى | action |
|---|---|---|
| thk-michael-yarp | **Michael Yapko** (محتوى) | إعادة تسمية → `thk-michael-yapko` |
| thk-wdowling | **Na'im Akbar** (محتوى) | إعادة تسمية → `thk-nakbar` |
| thk-rackoff | **Russell Ackoff** (محتوى) | إعادة تسمية → `thk-rrackoff` أو `thk-russell-ackoff` |
| thk-william-hudson | **William Hudson O'Hanlon** (محتوى) | إعادة تسمية → `thk-bill-ohanlon` |
| thk-michael-derm | **Michael Der Meer** (محتوى) | إعادة تسمية → `thk-michael-der-meer` |
| thk-mark-santross | **Mark R. Dombeck** (محتوى) | أُعيدت التسمية سابقاً إلى `thk-mdombeck`، لكن **حُجر 2026-08-27 (Task 2.34)**: المتن نفسه كان مذكرة تحقيق ذاتية تعترف بالتضارب، وينسب لـDombeck مساهمات غير موثّقة في تطوير PCIT (المؤسِّسة الموثّقة هي شيلا أيبرغ). حُوّل لقالب حجر. |
| thk-rreibo | **تعارض ثلاثي في حقل `en`**: Richard J. Reynolds / T. Taizan Maezumi / Rev. Daitsu Tom Wright — والمتن ينسب لـ"ريتشارد ريبو" سيرة موثّقة فعلياً لديفيد ك. رينولدز (thk-dreynolds، موجود بالفعل) | **حُجر 2026-08-27 (Task 2.34)** — لا دليل مستقل على وجود شخص باسم "ريتشارد ريبو". حُوّل لقالب حجر. |
| thk-rkeller | **Robert M. Clark** (محتوى) | إعادة تسمية كاملة |
| thk-sbooth | **Sandra Lindaman** (محتوى؛ Booth الحقيقي في نفس مجال Theraplay) | **مؤجّل للبحث** — هل Sandra Lindaman = Booth؟ سجّل في `requests-minimax.md`. |
| thk-tmoriiyama | slug ≠ اسم الملف على القرص | **يجب دمج** |
| thk-pkuhn | **Thomas Kuhn** (محتوى، توماس كون 1922–1996) — ازدواج فعلي مع `thk-thomas-kuhn` الموجود بslug صحيح وروابط واردة أكثر (8 مقابل 4) | **حُجر 2026-08-27 (Task 2)** — حُوّل لقالب إحالة، القرار النهائي (دمج+redirect_to) مسجّل R-002 في `requests-minimax.md` |
| thk-rsperry | **Len Sperry** (محتوى: Adlerian Psychopathology، Adlerian Couples and Family Counseling، Adlerian Strategies — كلها ببليوغرافيا Len Sperry الحقيقية، طبيب نفسي وأستاذ متفرغ FAU، لا "Robert Sperry") — سلسلة الأحرف "r" في الـslug لا تطابق "Len" (l) إطلاقاً | **حُجر 2026-08-27 (Task 2.25)** — حُوّل لقالب إحالة/حجر (الاسم "روبرت سبيري" غير موجود كمؤلف أدلري). طلب slug جديد `thk-lsperry` مسجّل في `requests-minimax.md` (خارج نطاق حروف MiniMax m→z) |
| thk-sgreys | **Daniel A. Hughes** (محتوى: مؤسّس DDP، موثّق أكاديمياً بالكامل) — الـslug "sgreys" لا يمتّ لاسمه بصلة إطلاقاً | **حُجر 2026-08-27 (Task 2.25)** — حُوّل لقالب إحالة/حجر رغم صحة المحتوى، لعدم مطابقة الـslug. طلب slug جديد `thk-dhughes` مسجّل في `requests-minimax.md` (يبدأ بحرف d، خارج نطاق حروف MiniMax m→z) |
| thk-sdesha | **Kamlesh D. Patel / "داجي" Daaji** (محتوى: الرئيس الرابع لبعثة شري رام تشاندرا ومرشد حركة Heartfulness، مواليد 1956، شخص حقيقي موثّق ويكيبيديا وheartfulness.org) — الـslug "sdesha" لا يمتّ لاسمه بصلة إطلاقاً | **حُجر 2026-08-27 (Task 2.40)** — حُوّل لقالب إحالة/حجر رغم صحة المحتوى، لعدم مطابقة الـslug. طلب slug جديد `thk-kamlesh-patel` أو `thk-daaji` مسجّل R-003 في `requests-minimax.md` |
| thk-rwilliams | **Roger T. Ames** (محتوى: فيلسوف أمريكي، منظّر الكونفوشية المعاصرة، سيرة موسّعة موثّقة بمصادر حقيقية Ames & Hall 1998/2001، Ames 2010/2011) — الـslug "rwilliams" لا يمتّ لاسم "Ames" بصلة إطلاقاً، والملف كان يذكر التعارض في ملاحظة معمارية داخلية بدل طلب slug صحيح | **حُجر 2026-08-27 (Task 2.52)** — حُوّل لقالب إحالة/حجر رغم صحة المحتوى وتوثيقه، لعدم مطابقة الـslug إطلاقاً. طلب slug جديد `thk-rames` مسجّل في `requests-minimax.md`. رابط من `thk-jakhan.md` كان يشير خطأً لهذا الـslug بعنوان "روبرت ويليامز" — صُحِّح ليشير إلى `thk-rlwilliams` (روبرت لي ويليامز الثاني، الشخص الصحيح الذي كان يُقصد فعلاً) |
| thk-rcabrera | **Akinsola A. Akiwowo** (محتوى: عالم اجتماع وأنثروبولوجي نيجيري، 1926/1928–1990، صاحب نظرية «أجوبي أجوبي» 1976) — الـslug "rcabrera" لا يمتّ لاسم "Akiwowo" بصلة إطلاقاً؛ الملف كان يعترف صراحة في `gaps` بأن "ريتشارد كابريرا" غير موجود ثم نشر سيرة أكيووو الكاملة تحت نفس الـslug المضلل، وهو بالضبط ما تمنعه القاعدتان 6 و11 | **حُجر 2026-08-27 (Task 2.52)** — حُوّل لقالب إحالة/حجر. طلب slug جديد `thk-aakiwowo` مسجّل في `requests-minimax.md`. خمسة ملفات كانت تربط بهذا الـslug (thk-asante، thk-hountondji، thk-wiredu، thk-bodunrin، sch-african-psychology) — أُزيلت الروابط الخمسة حتى يُحسم slug جديد |

### 3b) شخصان مختلفان بملف واحد

| slug | المشكلة | action |
|---|---|---|
| thk-saberg-abramovitz | شخصان مختلفان بid واحد | فصل أو حذف |
| thk-ricardo-doblin | **Ricardo Doblin** في المتن، والـslug فيه خطأ كتابي أيضاً | تنقيح slug فقط |

---

## القسم 4 — نقل محتوى (ليس حجر - معلومة حقيقية في ملف خاطئ)

> هذه ملفات **موثّقة جيداً** لكن عنوانها يشير لشخص آخر، والمحتوى
> يحتوي على معلومات تستحق **نقلها** إلى ملف مدرسة/تقنية/مفهوم.

| slug | المحتوى الحقيقي | action |
|---|---|---|
| thk-roland-tolentino | تخصصه دراسات إعلام لا علم نفس | **نقل** إلى `sch-filipino-media-studies` أو إعادة تصنيف |
| thk-campbell-purton | تخصصه علاج بالفن (Art Therapy) | انتقال محتمل إلى `tec-art-therapy` |

---

## القسم 5 — روابط `related` مكسورة (نسخ-لصق)

> قاعدة Spark 6 + قاعدة MiniMax 12: "كل id في related لازم يطابق فعلياً الـtitle".
> القائمة التالية استخرجت من القسم 3 من `audit-findings-minimax-t1-t2.md`:

### 5a) id ≠ title (نفس الـrelated entry)

| slug | entry | المشكلة |
|---|---|---|
| thk-ppapp | id thk-olitwak / title أولغا سيلفرشتاين | id يشير لشخص آخر |
| thk-pbooth | (يكرر مرتين) | نسخ-لصق |
| thk-rbenenzon | — | id خاطئ |
| thk-petersmith | — | id خاطئ |
| thk-tandersen | — | id خاطئ |
| thk-martin-luther-king | id يوحي بـRalph Alborn / title يصف رالف والدو إمرسون | **خلط شخصين**: King ليس له ارتباط بـEmerson في المحتوى. |
| thk-tim-ferriss | (مرتين) + id thk-rkoch لشخص مختلف | **استخدام id لشخصين مختلفين** |
| thk-maxwell-maltz | ماكسويل مالتز / مايكل بندلر | **خلط**: العنوان يشير لبندلر. |
| thk-sschoenwald | id يشاور لنفس صفحته | ذاتي-مرجعي |
| thk-margaretbodkin | id مستخدم مرتين لاسمين مختلفين | خطأ في id |
| thk-theresaglasser | — | id خاطئ |
| thk-nassim-taleb | دان جيلبوت = دانيال كانمان الحقيقي | **خلط**: العنوان ليس اسم الشخص في id. |
| thk-steven-pinker | — | id خاطئ |
| thk-richard-dawkins | "ملاحظة: لا أرى تفسير" | خطأ لم يُصحَّح |
| thk-mgriffiths | — | id خاطئ |
| thk-michaelsweeting | نفس الشخص بid مختلفين | self-inconsistency |
| thk-wood | (مرتين) + title="..." خاطئ نحوياً | **YAML غير صحيح** |
| thk-mary-stewart | title="..." خاطئ | YAML |
| thk-mayeroff | id يشاور لنفسه، title لإرنست بيكر | self-reference خطأ |
| thk-rhooton | — | id خاطئ |
| thk-vjohnson | هارفي كابلان = هارولد ليف الحقيقي | **خلط**: العنوان ≠ الـid. |
| thk-strindberg | — | id خاطئ |
| thk-rmdoblin | id يكرر الشخص نفسه بid تاني | self-loop |
| thk-wrichards | نفس con- مربوط 3 مرات بـtitles مختلفة | **إعادة استخدام con- داخل ملف** |

### 5b) صيغة YAML خاطئة (`title="..."` بدل `title: "..."`)

- thk-wood (مرتين)
- thk-mary-stewart

> **العدد:** ~25 ملف تحتاج فحص دقيق.

---

## القسم 6 — مواعيد متناقضة داخل الملف

> تناقض بين الـfrontmatter (dates / active_start / active_end) وما في المتن.
> قاعدة MINIMAX 5 الجديدة: التواريخ لازم تتفق مع المتن.

| slug | المشكلة | action |
|---|---|---|
| thk-wjanzarik | إشراف 1946 على أطروحة نُشرت 1959 | تصحيح |
| thk-wmasters | فجوة تواريخ زواج/طلاق | تصحيح |
| thk-mfarkas | مصدر 2012 بعد "وفاتها" المزعومة 2010 | تصحيح |
| thk-rene-girard | تناقض بين "1981–" و"1981–1995" | تصحيح |
| thk-paci | active_end 1963 بينما المتن يصف نشاط حتى 60s+ | إعادة تقييم |
| thk-ppenn | active_end 2010 بينما وفاتها 2006-2007 | تصحيح |
| thk-tgreening | active_start=active_end=1971، عمل حتى 2005، مات 2022 | إعادة بناء |
| thk-raphael | active_end 1981 والمصادر فيها كتاب 1993 | إعادة تقييم |
| thk-rennie | dates "1939–" حي، active_end 2000 | إعادة تقييم |
| thk-wiseman | active_start=active_end=2008 | إعادة تقييم |

---

## القسم 7 — أخطاء نسب/هوية (خلط شخصين حقيقيين)

| slug | المشكلة | action |
|---|---|---|
| thk-matthew-walker | تناقض: "تدرّب عند رختشافن في هارفارد ولا شيكاغو" | تصحيح |
| thk-sbem | داريل بيم اتكتب "داريك" + وصف فيلسوف بدل عالم نفس + وفاة بمساعدة طبيب في أوريغون غير موثّقة | تصحيح شامل |
| thk-rick-hanson | نسبوا تأسيس IPNB لـ"ماركوس سيغل" بدل **دانيال سيغل** | تصحيح (خطأ واضح) |
| thk-vjohnson | هارفي كابلان = هارولد ليف | تصحيح |
| thk-tgrandin | كلير دينيس بدل كلير دينس الممثلة | تصحيح |
| thk-wstekel | كرافت-إبينغ ≠ من مؤسسي جمعية الأربعاء | تصحيح |
| thk-susan-anderson | كتاب "Black Swan" لطالب الحقيقي | تصحيح |
| thk-mmithoefer | وليام ريتشاردز "أحد مؤسسي EMDR" — خطأ، **EMDR أسستها فرانسين شابيرو** | تصحيح (خطأ واضح) |
| thk-rennie | IPR منسوب لريني، لكن المنهج فعلياً **لنورمان كيغان** | تصحيح |
| thk-osilver | كتاب "The First Three Years of Life" منسوب لبيرتون وايت (منفرداً)، نسبة مشاركة لأولغا خطأ | تصحيح |
| thk-michelle-weiner-davis | مصنّفة "مؤسِّسة" Imago رغم أن المؤسس هارفيل هندريكس | تصحيح |
| thk-ymohamed | تناقض: "النموذج الباكستاني" و"رائد في مصر" لنفس الشخص | تصحيح |

---

## القسم 9 — تحقّق فعلي (Task 2): وجود شخص مشكوك فيه

### thk-jgantt (جوزيف غانت / Joseph Gantt) — THK-1275

- **الملف:** `content/ar/thinkers/thk-jgantt.md` — **معتمد** (لا يُحذف بدون قرار رئيس التحرير).
- **الادعاء:** معالج نفسي أمريكي في مجال السيكودراما، عمل في نورث كارولينا، صاحب كتاب
  *Trauma Be Not Proud* (2001)، مقالات في *Psychodrama Network News*.
- **التحقق المُنفَّذ (2026-08-27):** بحث ويب مباشر بعدة صياغات
  (`"Joseph Gantt" "Trauma Be Not Proud" psychodrama`, `"Joseph Gantt" psychodrama North Carolina therapist`).
  **لا توجد أي نتيجة مستقلة** تربط اسم Joseph Gantt بكتاب "Trauma Be Not Proud" أو
  بمجتمع السيكودراما أو بـ*Psychodrama Network News*. النتائج التي ظهرت لاسم "Gantt" في
  نورث كارولينا (Chris Gantt، Tomeka Gantt، Gantt Psychotherapeutic & Consulting) أشخاص
  مختلفون تماماً بلا صلة بالسيكودراما.
- **مؤشرات إضافية على الحجر:**
  - عنوان الكتاب المزعوم *Trauma Be Not Proud* يحاكي بشدة عنوان الكتاب الشهير
    *Death Be Not Proud* (John Gunther, 1949) — نمط عنوان "مُعاد تدويره" شائع في الادعاءات المُلفَّقة.
  - الملف نفسه يحتوي فعلاً على جملة من القائمة السوداء: "لا يوجد اقتباس مباشر موثوق متاح"
    (قسم اقتباسات مختارة) — مؤشر جودة ضعيف موجود بالفعل في نسخة معتمدة.
  - التفاصيل عامة جداً وغير قابلة للتحقق: تقنيات بأسماء عامة ("إعادة التشكيل الزمني"،
    "الإحلال المعاصر")، لا مصدر أولي محدد، لا سنة ميلاد، `level: "مبتدئ"`.
- **✅ القرار النهائي (رئيس التحرير، 2026-08-27): حجر.** الملف الحي حُوّل لقالب حجر موحّد،
  والنسخة الأصلية محفوظة في `agents_specs/quarantine-minimax-archive/thk-jgantt.md.archived.2026-08-27`.

### thk-rmanaster (رايتشل ماناستر / Rachael Manaster) — THK-2212 — Task 2.19، 2026-08-27

- **الملف:** `content/ar/thinkers/thk-rmanaster.md` — **مُحجَّر الآن** (نُقلت النسخة الأصلية
  إلى `agents_specs/quarantine-minimax-archive/thk-rmanaster.md.archived.2026-08-27`).
- **الادعاء:** مستشارة نفسية أمريكية أدلرية، مؤلفة «علم نفس المراهقة» (سبعينيات) و«العلاج
  النفسي الأدلري» (مع هارولد موساك) و«الإرشاد الأدلري» (مع جون كارلسون، 1985).
- **التحقق المُنفَّذ (2026-08-27):** بحث ويب مباشر بعدة صياغات لم يجد أي أثر مستقل لشخص
  باسم "Rachael Manaster" في أدبيات علم النفس الفردي الأدلري. الشخصية الحقيقية الموثّقة
  بهذا الاسم العائلي في هذا الحقل هي **غاي ج. ماناستر** (Guy J. Manaster) — أستاذ بجامعة
  تكساس في أوستن، محرر *The Journal of Individual Psychology* (من 1976، شارك جون كارلسون
  في التحرير 1982–1995)، مؤلف مشارك مع رايموند كورسيني لـ*Individual Psychology: Theory
  and Practice*، ومحرر *Alfred Adler, As We Remember Him* (1977). الملف الأصلي نسب تفاصيل
  تحاكي إنجازات غاي ماناستر الحقيقية (زمالة العمل مع جون كارلسون تحديداً) لاسم مؤنث مختلف
  كلياً لا يطابق أي مصدر — نمط "إعادة تدوير هوية" يستوجب الحجر بحسب القاعدة 6.
- **القرار:** **حجر.** الملف الحي حُوِّل لقالب حجر موحّد. طُلب slug جديد (`thk-guymanaster`
  مقترح) لتوثيق غاي ج. ماناستر الحقيقي بشكل مستقل — راجع `agents_specs/requests-minimax.md`.

### thk-wbennett (وين بينيت / Win Bennett) — THK-2789 — Task 2.30، 2026-08-27

- **الملف:** `content/ar/thinkers/thk-wbennett.md` — **مُحجَّر الآن** (نُقلت النسخة الأصلية
  إلى `agents_specs/quarantine-minimax-archive/thk-wbennett.md.archived.2026-08-27`).
- **الادعاء:** باحث وعالم نفس سريري يُنسب إليه برنامج KIP-SST (Kids in Pain — Single-Session
  Therapy) للمراهقين في الألم المزمن في أونتاريو، كندا.
- **التحقق المُنفَّذ (2026-08-27):** بحث ويب بعدة صياغات
  (`"Win Bennett" "Kids in Pain" single-session therapy Ottawa`,
  `"Win Bennett" single-session therapy psychologist child pain`). لا نتيجة مستقلة واحدة
  تربط اسم "Win Bennett" ببرنامج KIP أو بأدبيات العلاج بجلسة واحدة. حقلا `country` و`dates`
  في الملف الأصلي كانا أصلاً `[DRAFT-UNKNOWN]` — إشارة أن الهوية لم تُثبَّت من البداية رغم
  متن واثق الشكل بتفاصيل بروتوكول علاجي محدد (نمط التناقض المحذَّر منه في القاعدة 11).
- **القرار:** **حجر.** الملف الحي حُوِّل لقالب حجر موحّد.

### thk-mwagreich (موريس هـ. فيغوتش / Moris H. Wagreich) — THK-2731 — Task 2.31، 2026-08-27

- **الملف:** `content/ar/thinkers/thk-mwagreich.md` — **مُحجَّر الآن** (نُقلت النسخة الأصلية
  إلى `agents_specs/quarantine-minimax-archive/thk-mwagreich.md.archived.2026-08-27`).
- **الادعاء:** طبيب ومحلل نفسي أمريكي (1910–1990 تقريباً)، من أبرز ممارسي التنويم التحليلي
  (Hypno-analysis)، ارتبط تاريخياً بمارغريت برينمان في تطوير الحقل في الأربعينيات والخمسينيات.
- **التحقق المُنفَّذ (2026-08-27):** بحث ويب بعدة صياغات (`"Moris Wagreich" OR "Moris H.
  Wagreich" hypnoanalysis psychoanalyst`). لا نتيجة مستقلة واحدة لهذا الاسم. الأسماء
  الموثّقة فعلياً في تأسيس Hypno-analysis هي **مارغريت برينمان** (Margaret Brenman) و**ميرتون
  غيل** (Merton Gill)، مؤلفا *Hypnotherapy* (1947) و*Hypnoanalysis* (1959) — لا ذكر لـ"Wagreich"
  في أي منهما ولا في الأدبيات الثانوية عن الحقل.
- **القرار:** **حجر.** الملف الحي حُوِّل لقالب حجر موحّد.

### thk-ptedeschi (رافائيل تيدِسكي / Raphael G. Tedeschi) — THK-1765 — Task 2.31، 2026-08-27

- **الملف:** `content/ar/thinkers/thk-ptedeschi.md` — **مُحجَّر الآن** (نُقلت النسخة الأصلية
  إلى `agents_specs/quarantine-minimax-archive/thk-ptedeschi.md.archived.2026-08-27`).
- **الادعاء:** عالم نفس إكلينيكي أمريكي من أصل إيطالي، من أهم منظري الاستشارات متعددة
  الثقافات (Multicultural Counseling)، أستاذ بجامعة ولاية فلوريدا.
- **التحقق المُنفَّذ (2026-08-27):** بحث ويب (`"Raphael Tedeschi" multicultural counseling
  psychologist`) لم يُرجع أي نتيجة بيوغرافية لهذا الاسم. الأسماء المرجعية الموثّقة في هذا
  الحقل هي Derald Wing Sue وJanet Helms وPaul Pedersen وThomas Parham. الاسم الأقرب صوتياً
  والموثَّق فعلياً هو **Richard G. Tedeschi**، لكنه باحث في **النمو ما بعد الصدمة
  (Posttraumatic Growth)** مع Lawrence Calhoun — حقل مختلف تماماً، ما يرجّح خلطاً أو اختلاق
  هوية لا خطأ كتابياً بسيطاً.
- **القرار:** **حجر.** الملف الحي حُوِّل لقالب حجر موحّد.

---

## القسم 8 — bug منهجي: خطأ جنس نحوي ✅ حُلّ بالكامل 2026-08-27

> العنوان الفرعي `## أهم أعمالها` (مؤنث) يُستخدم لرجل في عشرات الملفات.
> أصل المشكلة: قالب توليد ثابت لم يكن يُراجع للجنس.
>
> **✅ حُلّ:** صُححت جميع الملفات الـ40 المذكورة أدناه (تأكد ذكورة كل شخص فردياً قبل التصحيح).
> نفس المرور كشف وصحّح 233 مخالفة preflight إضافية على نفس الملفات — تفاصيل في
> `agents_specs/reports/minimax/quarantine-review-batch-A.md` و`quarantine-review-batch-B.md`.

**الإصلاح:** مسح آلي (grep) عبر ملفات `content/ar/thinkers/thk-m-to-z.md`
على `## أهم أعمالها` و`## علاقتها`، تصحيح إلى `أعماله` و`علاقته` لأي رجل.

**الملفات المتأثرة (29+):** thk-mgold، thk-mtrevi، thk-pritz، thk-snygg، thk-snichols، thk-mahfouz، thk-tbarber، thk-philippe-cunningham، thk-rryan، thk-rosenfeld، thk-spiegelberg، thk-robert-emery، thk-sstanley، thk-wanthony، thk-yogananda، thk-russellrazzaque، thk-tgreening، thk-mithoefer، thk-nionescu، thk-mmithoefer، thk-svami-akhilananda، thk-sothmer، thk-rlandy-md، thk-rennie، thk-tbrazelton، thk-savodnik، thk-roland-tolentino، thk-william-hudson، thk-wolf، thk-raphael، thk-wdowling، thk-rhanson، thk-mrolls، thk-moss، thk-mnichols، thk-rkaes، thk-peperzak، thk-robert-rotella، thk-mayeroff، thk-rshort، thk-sleclaire، thk-mtotton، thk-michael-yarp.

**الإجراء (مؤجّل - sub-task منفصل بعد الحجر):**
- تشغيل script بسيط: `grep -l '## أهم أعمالها' content/ar/thinkers/thk-*.md` ثم تحقق من الـgender في الـfrontmatter.

---

## ملخص طابور العمل الحالي

| الأولوية | الفئة | العدد | الخطوة التالية |
|---|---|---|---|
| 🔴 1 | عاجل — ادعاءات قوية (القسم 1) | ~20 ملف | رئيس التحرير يقرر: حذف فوري / نقل / إعادة تسمية |
| 🟠 2 | حجر روتيني (القسم 2) | ~30 ملف | نقل جماعي إلى archive أو استبدال بـgaps قصيرة |
| 🟠 3 | تعارض هوية (القسم 3) | 12 ملف | إعادة تسمية الـslug مع تحديث links |
| 🟡 4 | روابط مكسورة (القسم 5) | ~25 ملف | مسح ملف-بملف وتصحيح id/title |
| 🟡 5 | مواعيد متناقضة (القسم 6) | 10 ملف | تصحيح ملف-بملف |
| 🟡 6 | أخطاء نسب/هوية (القسم 7) | 12 ملف | تصحيح ملف-بملف |
| 🟢 7 | نقل محتوى (القسم 4) | 2 ملف | نقل معلومات إلى ملف مدرسة/تقنية |
| ⚪ 8 | bug جنس نحوي (القسم 8) | 40 ملف | script آلي - sub-task منفصل |

**المجموع التراكمي:** ~150 ملف يحتاج تصحيحاً (≈ 51% من ملفات MiniMax).

---

## ملاحظات التنسيق في الأطلس

- جميع الملفات الـ227 اللي فيها `DRAFT-UNKNOWN` في frontmatter **ليست placeholders بالضرورة**.
  بعضها ملفات جديدة تم إنشاؤها في دفعات لاحقة ولم تكتمل بعد. يحتاج **فصل منهجي**:
  1. DRAFT-UNKNOWN + اعتراف بعدم التوثيق → الحجر (الأقسام 1-2).
  2. DRAFT-UNKNOWN + سيرة واثقة → عاجل (الأقسام 1 و3 و7).
  3. DRAFT-UNKNOWN فقط (في frontmatter) → قيد إنتاج، يُراجع في sub-task لاحق.

- ملف الحجر **يُحدَّث** كلما اكتمل sub-task (مثال: "تم نقل thk-mcieslak إلى archive في 2026-08-27").

---

## كيف يُستخدم هذا الملف في جلسة MiniMax

- قبل أي sub-task جديد: اقرأ هذا الملف أولاً.
- أي ملف مرتبط يجب أن يضاف (في الـrelated:) أو يُحذف من الإنتاج.
- بعد التصحيح، يُنقل إلى `agents_specs/quarantine-minimax-archive/` مع تاريخ الإجراء.
- لا تُحذف السجلات — هذا ملف **تاريخي**، كل سطر فيه يمثل حالة وُثّقت في وقت معيّن.

## القسم 9 — Task 3 batch-1 (thk-m→z) حجر 2026-08-27

- **thk-marciamarx** (Marcia B. Marx): الملف نفسه كان يعترف بعدم وجود توثيق مستقل ("تحذير هوية") لكنه لم يكن بالقالب الموحّد. حُوِّل لقالب الحجر الموحّد.
- **thk-markwelch** (Mark Welch): نفس الحالة — اعتراف صريح بعدم التوثيق ("تحذير هوية") دون قالب حجر موحّد. حُوِّل.
- **thk-mchen** (Marvin Chen): ملف "يحتاج مراجعة" ذاتي الاعتراف بعدم التوثيق (لا عضوية ASGPP/TFPG، لا مقالة JGPPS، لا كتاب WorldCat). حُوِّل لقالب الحجر الموحّد.
- **thk-mclayton** (G. Max Clayton): نفس النمط — لا عضوية ASGPP، لا كتاب موثّق. حُوِّل لقالب الحجر الموحّد.
- **thk-melissaschaefer** (Melissa Schaefer): الملف كان يحتوي فعلياً على "توصية الحجر" مكتوبة كسطر تحت `## المصادر` — مخالفة صريحة للقاعدة 5. حُوِّل لقالب الحجر الموحّد وحُذفت الملاحظة التحريرية.

**كذلك أُصلحت 4 ملفات حجر قديمة كانت YAML فيها مكسورة أو تحمل `related`/`edges` غير مُنظَّفة من ما قبل الحجر:** thk-margaretbodkin وthk-marisaberkouwer (كان فيهما `gaps:` خارج الـfrontmatter بسبب `---` مزدوج)، وthk-mariannekline وthk-masaaki-takahashi وthk-margaret-bluestein وthk-ma-rosario-alfelor (edges/related قديمة من قبل الحجر لم تُنظَّف).

## القسم 10 — Task 3 batch-5 (thk-r→s) حجر وتصحيح 2026-08-27

- **thk-saberg-abramovitz** (Astrid Berg / Carol Abramovitz): الملف نفسه كان يعترف صراحة بعدم وجود سيرة موثّقة في IAAP/SAAJA/JAP/PsycINFO ويقترح احتمال لبس مع أشخاص آخرين، لكنه لم يكن بالقالب الموحّد. حُوِّل لقالب الحجر الموحّد.
- **thk-sdouglas** (Sue Douglas، DDP): نفس الحالة — لا سيرة في DDP Society/Network، اعتراف صريح بالبحث السلبي. حُوِّل.
- **thk-skalama** (Sam Kalama، Ho'oponopono): نفس الحالة — لا نتائج في أرشيف جامعة هاواي أو Bishop Museum. حُوِّل.
- **thk-sharron-hapai** (Sharron Hapai، Te Whare Tapa Whā): نفس الحالة، **وكان الملف يحمل مخالفة إضافية للقاعدة 5** — سطر "توصية الحجر في quarantine-minimax.md" مكتوب حرفياً تحت `## المصادر` كأنه استشهاد. حُوِّل لقالب الحجر الموحّد وحُذفت الملاحظة التحريرية.

**إصلاح YAML مكسور في ملفين حجر قديمين:** thk-russellrazzaque وthk-shirley-murray كان فيهما `gaps:` خارج الـfrontmatter بسبب `---` مزدوج (frontmatter يُغلق ثم يُعاد فتحه)، مع `edges`/`related` غير منظّفة من قبل الحجر. صُحِّحا لقالب موحّد نظيف.

**تصحيحات هوية/جنس في ملفات غير محجورة:**
- **thk-ssafran**: الاسم المسجَّل "ستيفن م. سَافِران / Stephen M. Safran" لا يطابق الشخص الموصوف فعلياً في المتن والمصادر (كل الاستشهادات لـJeremy D. Safran، مؤلف *Brief Relational Therapy*). صُحِّح الاسم/العنوان/الـcrumb إلى "جيريمي د. سافران"، وصُحِّح عنوان "## أهم أعمالها" (مؤنث خطأ) إلى "## أهم أعماله".
- **thk-sross**: عنوان "## أهم أعمالها" مؤنث خطأ لشخص ذكر (ستيفن روس) — صُحِّح إلى "## أهم أعماله".
- **thk-rwooffitt**: عنوان "## ما أعطته" مؤنث خطأ لشخص ذكر (روبن ووفيت) — صُحِّح إلى "## ما أعطاه".
- **thk-sbem**: "زوجها داريك بيم (Derek C. Bem)" لا يطابق مصادر الملف نفسها التي تستشهد بـ"Bem, D. J." (Daryl J. Bem) — صُحِّح الاسم.

**تنظيف روابط `related` مكسورة (slugs مخترعة لا تطابق الملفات الفعلية) عبر دفعة batch-5 كاملة:** عشرات الروابط كانت تستخدم صيغاً مثل `thk-sfreud`/`thk-ikant`/`thk-jgoethe`/`thk-jbutler` بدل الـslugs الفعلية `thk-freud`/`thk-kant`/`thk-goethe`/`thk-butler`. صُحِّحت الروابط ذات التطابق الأكيد (اسم ولقب متطابقين مع ملف موجود فعلياً)، وحُذفت الروابط بلا تطابق مؤكد مع تسجيلها في `requests-minimax.md`. **تنبيه لبقية الدفعات:** هذا النمط (بادئة حرف أول + لقب مخترعة) منتشر على الأرجح في ملفات أخرى من نفس دفعات الإنتاج الآلي؛ يستحق فحصاً منهجياً منفصلاً.
- **thk-michaelsweeting** (Michael Sweeting): وُجد وقت المراجعة بمحتوى واثق الشكل (لا "# حُجر") رغم عدم وجود سنة ميلاد أو اقتباس موثَّق أو مصدر أولي محقَّق — نمط التناقض الذي تحسمه القاعدة 11. حُوِّل لقالب الحجر الموحّد.

## القسم — Task 12 batch (2026-09-01): questions/ حجر ازدواج

- **que-mind-body-interaction** (QUE-0015): ازدواج فعلي مع `que-mind-body-interaction-problem` (QUE-0129) — نفس السؤال (تفاعل العقل/الجسد، تفاعلية ديكارت 1649 مقابل أحادية سبينوزا 1677)، والملف الآخر أعمق توثيقاً (مصادر أولية مباشرة بتواريخ محدَّدة). حُوِّل لقالب الحجر الموحّد + إحالة. لا روابط واردة له وقت الحجر. النسخة الأصلية محفوظة في `agents_specs/quarantine-minimax-archive/que-mind-body-interaction.md.archived.2026-09-01`.
