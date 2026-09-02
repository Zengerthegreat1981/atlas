# Task 3.9
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي. **المحاولة الأولى فشلت بالكامل (كل الـ7 subagents) بسبب ضرب حد جلسة API — لم يُكتب أي ملف ولم يحدث أي تلف، وأُعيدت الدفعة بالكامل من الصفر بعد تصفير الحد.**

## الأرقام
- ملفات سليمة تماماً (بلا مسودة): 0 / 35 — كل ملف في هذه الدفعة كان فيه خطأ واحد على الأقل.
- **أخطر اكتشاف: thk-dewey (جون ديوي)** — قسم "الأثر" بالكامل تقريباً كان يحتوي أسماء مختلَقة/غير قابلة للتحقق بنمط يشبه التوليد العشوائي ("جاستلر"، "لورنس لاوسن"، "بروديك"، "رولاند فيفرن"، "جودج كوهين") — حُذفت واستُبدلت بمادة موثقة فعلياً (رورتي 1979، كورنيل ويست).
- **هوية مشكوكة (مرشح Task 2): thk-deng-yuanhai** — لا مصدر أولي يؤكده كمؤسس للعلاج المعرفي الطاوي الصيني (الأدبيات تنسب التأسيس ليانغ ديشن وتشانغ يالين)، وتعارض اسم واضح مع `thk-jingqiyong` (عنوانه المعتمد فعلياً "يانغ ديشن" لا "جينغ تشي-يونغ").
- **ازدواج slug مؤكَّد**: `thk-dale-carnegie` و`thk-carnegie` (من دفعة 3.7) كلاهما عن نفس الشخص (ديل كارنيجي، 1888-1955) — يحتاج قرار دمج.
- **أخطاء نسبة**: `thk-david-nichols` (كتاب *DMT: The Spirit Molecule* منسوب له خطأً، والمؤلف الحقيقي ريك ستراسمان)، `thk-depston` (كتاب *Re-Authoring Lives* كان منسوباً لمايكل وايت منفرداً بدل تأليف مشترك مع إبستون نفسه)، `thk-dbaucom` (عنوان كتاب خاطئ)، `thk-dan-kiley` (تناقض اسم وتاريخ ميلاد داخلي).
- **أخطاء جنس**: `thk-davoine` (صيغة فعل مذكرة "نقل" لامرأة، صُححت لـ"نقلت").
- **نمط "روابط محجورة/مزعوم إزالتها فعلياً لسه موجودة" — استمر الاكتشاف**: `thk-dan-fisher` (thk-gene-ennis، thk-kurtz-sherman محجوران فعلياً وأُزيلا)، `thk-deniswaitley` (thk-bobbeck، thk-charlesfaulkner)، `thk-deraldwing-sue` (3 روابط).
- **إصلاح تنسيق edges**: `thk-deng-yuanhai` كان `belongs_to`/`developed` نصاً حراً رغم وجود slug حقيقي مطابق (`sch-taoist-cognitive-therapy`) — صُحح.
- **تراكم طلب `sch-popular-psychology`**: أصبح 8 طلبات منفصلة عبر Task 3 (راجع تنبيه مجمَّع مُضاف في `requests-spark.md`).

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{dai-zhen,dale-carnegie,damascius,damasio,dan-ariely,dan-fisher,dan-kiley,dan-millman,dana,daniel-dennett,daniel-gilbert,darcy-woebot,david-berceli,david-chalmers,david-nichols,davoine,dayananda,dbaucom,dbaumrind,dchamberlain,dchopra,dcooper,de-bono,dedwards,deleuze,democritus,deng-yuanhai,deniswaitley,depston,deraldwing-sue,derrida,descartes,deutsch,dewaelhens,dewey}.md
→ ✅ 35 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة، وتصحيح تعارضات id/title (Heidegger، James، Iyengar).

## متوقف عنده (لرئيس التحرير)
- **thk-dewey**: نمط الأسماء المختلَقة في قسم "الأثر" يستحق فحصاً لباقي محتوى الملف قبل الترقية، ومراجعة هل نفس النمط موجود في ملفات أخرى كتبها نفس المصدر الأصلي.
- **thk-deng-yuanhai**: يحتاج تطبيق معيار Task 2 (موثّق/غير موجود/غامض) قبل أي ترقية — الأدلة الحالية تشير لعدم دقة الهوية.
- **thk-dale-carnegie ↔ thk-carnegie**: قرار دمج مطلوب.
- **thk-david-nichols**: حذف *DMT: The Spirit Molecule* من أعماله قرار عالي الثقة (نُسب فعلياً لريك ستراسمان) — يُطبَّق فوراً عند الترقية.
- **طلب `sch-popular-psychology` المجمَّع**: 8 ملفات الآن بانتظار هذا الـslug — أُضيف تنبيه موحَّد في `requests-spark.md`.
- **`thk-darcy-woebot`**: تصحيح الانتماء المؤسسي (UCSF → ستانفورد) بثقة معتدلة، يستحق تأكيداً.

## الملفات
content/ar/thinkers/thk-dai-zhen.md
content/ar/thinkers/thk-dale-carnegie.md
content/ar/thinkers/thk-damascius.md
content/ar/thinkers/thk-damasio.md
content/ar/thinkers/thk-dan-ariely.md
content/ar/thinkers/thk-dan-fisher.md
content/ar/thinkers/thk-dan-kiley.md
content/ar/thinkers/thk-dan-millman.md
content/ar/thinkers/thk-dana.md
content/ar/thinkers/thk-daniel-dennett.md
content/ar/thinkers/thk-daniel-gilbert.md
content/ar/thinkers/thk-darcy-woebot.md
content/ar/thinkers/thk-david-berceli.md
content/ar/thinkers/thk-david-chalmers.md
content/ar/thinkers/thk-david-nichols.md
content/ar/thinkers/thk-davoine.md
content/ar/thinkers/thk-dayananda.md
content/ar/thinkers/thk-dbaucom.md
content/ar/thinkers/thk-dbaumrind.md
content/ar/thinkers/thk-dchamberlain.md
content/ar/thinkers/thk-dchopra.md
content/ar/thinkers/thk-dcooper.md
content/ar/thinkers/thk-de-bono.md
content/ar/thinkers/thk-dedwards.md
content/ar/thinkers/thk-deleuze.md
content/ar/thinkers/thk-democritus.md
content/ar/thinkers/thk-deng-yuanhai.md
content/ar/thinkers/thk-deniswaitley.md
content/ar/thinkers/thk-depston.md
content/ar/thinkers/thk-deraldwing-sue.md
content/ar/thinkers/thk-derrida.md
content/ar/thinkers/thk-descartes.md
content/ar/thinkers/thk-deutsch.md
content/ar/thinkers/thk-dewaelhens.md
content/ar/thinkers/thk-dewey.md
