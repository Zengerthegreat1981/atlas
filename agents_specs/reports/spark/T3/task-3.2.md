# Task 3.2
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد). هذه الدفعة غطت أضخم شخصيات التراث العربي-الإسلامي في الأطلس (الفارابي، الغزالي، الكندي، البيروني، أبو بكر الرازي...) بالإضافة لشخصيات معاصرة.

## الأرقام
- ملفات فيها جملة القائمة السوداء: أغلبية الدفعة → 0
- ملفات سليمة تماماً (بلا مسودة): 1 / 35 (thk-ambedkar)
- `edges.belongs_to.target` بنص حر بدل slug: ~12 حالة → صُححت لـslugs موجودة فعلاً، أو حُذفت مع تسجيل طلب في requests-spark.md لو مفيش slug مناسب (لا اختراع)
- **أخطاء نسبة/هوية جسيمة مكتشفة:**
  - **thk-al-mawardi**: وصف الخليفة القادر بالله بأنه "آخر خليفة عباسي" — خطأ فادح (الخلافة استمرت حتى 1258)؛ وادعاء تأثيره على مونتسكيو ولوك غير موثّق، حُذف.
  - **thk-al-farabi**: عنوانان لاتينيان خطأ منسوبان لـ"كتاب الحروف" (ينتميان فعلياً لعمل مختلف: إحصاء العلوم)؛ صُححا.
  - **thk-al-ghazali**: `sch-wahdat-alwujud` كانت مرتبطة به مباشرة رغم أن المصطلح يُنسب لابن عربي بعد وفاته بقرن — حُذف الرابط.
  - **thk-al-razi-abu-bakr**: `belongs_to` كان نصاً حراً مخترعاً بلا سند، والمتن نفسه يقر أن الرازي "بلا مدرسة" — حُذف الرابط بدل اختراع slug.
  - **thk-akaptchuk**: استشهادات بحثية مختلَقة بالكامل (Ho 1994، Li، Yang & Lu 2018، Kerr 2018) — حُذفت جميعاً.
  - **thk-alan-fruzzetti**: استشهاد ذاتي خاطئ ("Fruzzetti مع Fruzzetti" بدل مارشا لينهان الحقيقية) وعنوان كتاب مختلَق بالكامل — صُححا.
  - **thk-amy-cuddy**: تأليف ورقة 2010 والتراجع 2016 نُسب خطأً لـ"داتشر كِلتنر" — المؤلفة الحقيقية دانا كارني — صُحح في موضعين.
  - **thk-anajam**: **خطأ هوية جسيم** — الملف خلط بين عادل نجّام (أستاذ علاقات دولية حقيقي) وشخص مختلَق في علم النفس الإسلامي؛ المحتوى المختلق حُذف بالكامل. **قرار حساس معلّق**.
  - **thk-anan-ben-david**: استحالة زمنية (سعديا الفيومي وُلد بعد وفاة عنان بقرن، لا يمكن أن يكون نافسه سنة 770م) — صُححت.
  - **thk-amo**: عنوانا عملين وتاريخاهما خاطئان (خلط بين أعمال مختلفة لنفس المؤلف) — صُححا؛ عملان آخران غير موثقين حُذفا بالكامل.
  - **thk-akelman**: تضارب هوية جوهري (اسمان مختلفان لنفس "الشخص" بلا تفسير: أميت ميمن/أميت كلمان) — لم يُخمَّن حل، وُثِّق الغموض. **مرشح لـTask 2**.
- **تعارض عابر للتاسكات اكتُشف ومُصحح**: `thk-alemma` كانت لسه رابطة بـ`thk-gillian-abbott` كـ`related` صحيح، رغم أن Task 2 حجرها بالفعل كشخص غير موثّق الوجود — حُذف الرابط.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{akaptchuk,akelman,al-biruni,al-farabi,al-ghazali,al-kawakibi,al-kindi,al-mawardi,al-razi-abu-bakr,al-shahrazuri,al-sharif-al-jurjani,al-taftazani,al-tawhidi,alain-de-botton,alan-fruzzetti,alazm,albertus-magnus,alecmiller,alemma,alexander-aphrodisias,alexis-kagame,allameh-tabatabai,alvinmahrer,amadiume,amarlatt,amenemope,amiller,amir-levine,ammonius-hermiae,amo,amuller,amy-cuddy,anajam,anan-ben-david}.md
→ ✅ 34 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للأخطاء الجسيمة. باقي الـ23 ملفاً الأخرى (akelman جزئياً، al-biruni، al-kawakibi، al-kindi، al-shahrazuri، al-sharif-al-jurjani، al-taftazani، al-tawhidi، alazm، albertus-magnus، alecmiller، alemma، alexander-aphrodisias، alexis-kagame، allameh-tabatabai، alvinmahrer، amadiume، amenemope، amiller، amir-levine، ammonius-hermiae، amuller) صُححت فيها بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي، حذف روابط `related` بلا سبب مذكور بالمتن، وتصحيحات تواريخ صغيرة (إضافة "بعد وفاته" حيث لزم).

## متوقف عنده (لرئيس التحرير)
- **thk-anajam**: يحتاج قراراً تحريرياً — إما كتابة سيرة عادل نجّام الحقيقية (سياسات عامة، خارج نطاق علم النفس أصلاً) أو تحديد الشخص الصحيح صاحب الإسهام في علم النفس الإسلامي الإدراكي وفتح slug مستقل له.
- **thk-akelman**: تضارب هوية (اسمان مختلفان بلا تفسير) — مرشح مباشر لتطبيق معيار Task 2 (موثّق/غير موجود/غامض) بدل الكتابة تحت افتراض.
- **thk-akaptchuk**: هل ربطه بمدرسة "علم النفس الكونفوشي" مبرر أصلاً بعد حذف كل الأدلة المختلَقة الداعمة له؟ مرشح لمراجعة Task 2.
- **thk-al-razi-abu-bakr**: لا يوجد slug تصنيف مناسب له في الأطلس (فيلسوف مستقل لا مدرسة له) — هل يُطلب تصنيف جديد أم يبقى بلا `belongs_to`؟
- **thk-alvinmahrer**: لا يوجد slug لمدرسة "العلاج بالخبرة/التجريبي" رغم كثافة الملفات المرتبطة بها — يستحق `sch-` مستقل. طلب مسجَّل في requests-spark.md.
- **thk-al-mawardi**: حذف ادعاء تأثيره على مونتسكيو ولوك — لو فيه مصدر أصلي يدعمه فعلاً، يستحق مراجعة قبل حسم الحذف نهائياً.
- **thk-amarlatt**: سنة صياغة "تأثير انتهاك الامتناع" (1973 مقابل 1985 الموثقة في كتاب Marlatt & Gordon) تحتاج تأكيداً من مصدر أولي أبكر.

## الملفات
content/ar/thinkers/thk-akaptchuk.md
content/ar/thinkers/thk-akelman.md
content/ar/thinkers/thk-al-biruni.md
content/ar/thinkers/thk-al-farabi.md
content/ar/thinkers/thk-al-ghazali.md
content/ar/thinkers/thk-al-kawakibi.md
content/ar/thinkers/thk-al-kindi.md
content/ar/thinkers/thk-al-mawardi.md
content/ar/thinkers/thk-al-razi-abu-bakr.md
content/ar/thinkers/thk-al-shahrazuri.md
content/ar/thinkers/thk-al-sharif-al-jurjani.md
content/ar/thinkers/thk-al-taftazani.md
content/ar/thinkers/thk-al-tawhidi.md
content/ar/thinkers/thk-alain-de-botton.md
content/ar/thinkers/thk-alan-fruzzetti.md
content/ar/thinkers/thk-alazm.md
content/ar/thinkers/thk-albertus-magnus.md
content/ar/thinkers/thk-alecmiller.md
content/ar/thinkers/thk-alemma.md
content/ar/thinkers/thk-alexander-aphrodisias.md
content/ar/thinkers/thk-alexis-kagame.md
content/ar/thinkers/thk-allameh-tabatabai.md
content/ar/thinkers/thk-alvinmahrer.md
content/ar/thinkers/thk-amadiume.md
content/ar/thinkers/thk-amarlatt.md
content/ar/thinkers/thk-ambedkar.md
content/ar/thinkers/thk-amenemope.md
content/ar/thinkers/thk-amiller.md
content/ar/thinkers/thk-amir-levine.md
content/ar/thinkers/thk-ammonius-hermiae.md
content/ar/thinkers/thk-amo.md
content/ar/thinkers/thk-amuller.md
content/ar/thinkers/thk-amy-cuddy.md
content/ar/thinkers/thk-anajam.md
content/ar/thinkers/thk-anan-ben-david.md
