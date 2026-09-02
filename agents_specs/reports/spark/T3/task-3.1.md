# Task 3.1
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد).

## الأرقام
- ملفات فيها جملة القائمة السوداء (بصيغها المختلفة): 30+ / 35 → 0
- ملفات بلا أي خطأ إطلاقاً (سيبت بلا مسودة): 1 / 35 (thk-ahiqar)
- `edges.belongs_to.target` بنص حر بدل slug حقيقي: 6 حالات → 0 (كلها صُححت لـslugs موجودة فعلاً في EXISTING_SLUGS، صفر اختراع)
- أخطاء تواريخ حقيقية (active_end/start مستحيل أو غير موثق): 6 حالات، أبرزها:
  - **thk-ajernberg**: سنة الوفاة كانت خاطئة كلياً (2013 بدل 1993) — صُححت بمصدر خارجي (goodtherapy.org, theraplay.org)
  - **thk-abalint**: `active_end: "مستمر"` رغم وفاتها 1939 — صُححت
  - **thk-adorno**: `active_start` و`active_end` كانا بعيدين عن نشاطه الفعلي (1931–1969 بدل تواريخ متأخرة/مبتورة) — صُححا
  - **thk-abbagnano**, **thk-abdallah-laroui**: تواريخ نهاية نشاط مخترعة بلا سند نصي → حُيّدت لـ`null` بدل التخمين
- أخطاء نسبة/هوية حقيقية جسيمة: 3 حالات
  - **thk-achristensen**: مؤلفان مختلقان بالكامل ("دانييل جاكوبسون" و"جيسيكا ديماراي") كانا منسوبين لطبعة 2015 من كتاب IBCT — استُبدلا بالمؤلف الحقيقي (براين دوس)
  - **thk-abraham-geiger**: عبارة تنسب له نقد كتاب لفرانتس روزنتسفايغ (1921) — مستحيلة زمنياً (جيغر توفي 1874) — حُذفت بالكامل، وصُحح اسم خصمه من "زانزفين" (غير موجود) إلى "زخريا فرانكل" (الاسم الصحيح المطابق للمتن نفسه)
  - **thk-aalladin**: عنوانا كتابين غير موثقين استُبدلا بالعنوانين الحقيقيين، وحُذف ادعاء شراكة غير مسندة مع تريفور سيلفستر
- **خطأ تصنيف جوهري**: thk-adorno كان مصنّفاً `belongs_to: sch-existential-therapy` رغم أن متن الملف نفسه يصفه كناقد صريح للوجودية الهايدجرية — تناقض مباشر صُحح إلى `sch-frankfurt-school` (**قرار حساس، انظر تحت**)
- أخطاء جنس (ضمائر/صيغ لا تطابق جنس الشخص): 3 حالات في thk-afreud (أنا فرويد وُصفت بأفعال مذكرة "توفي"/"رتبها" بدل "توفيت"/"رتّبتها"، وخطأ حسابي في عمرها 86 بدل 87)

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{aabdelkhalek,aabrer,aalladin,aalvarez,abalint,abandura,abbagnano,abd-al-karim-al-jili,abdallah-laroui,abraham-geiger,abramovitch,abu-al-barakat-al-baghdadi,abu-al-hasan-al-amiri,abu-sulayman-al-sijistani,achristensen,adam-grant,adamblatner,adams,adler,adorno,adud-al-din-al-iji,aferro,afghani,afreud,agoldstein,agreen,ahmad-sirhindi,ahofmann,aichhorn,ainsworth,aizenstat,aj-ayer,ajanov,ajernberg}.md
→ ✅ 34 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
كل ملف من الـ34 المذكورين أعلاه (ما عدا thk-ahiqar السليم بلا مسودة) دُقّق بالترتيب الستة (هوية→جنس→تواريخ→نسبة→اقتباسات→نتائج)، وحُذفت منه جملة/جمل القائمة السوداء، وصُححت أي مخالفة `edges` أو تاريخ أو نسبة مكتشفة. أبرز القرارات التفصيلية:
- **thk-aabdelkhalek**: `belongs_to` من نص حر إلى `br-islamic-positive-psychology` (موجود فعلاً).
- **thk-aabrer** (كارل أبراهام): صُحح `part` من philosophy إلى psychology.
- **thk-aalladin**: راجع أعلاه — عنوانا كتاب واستبدال شراكة غير مسندة.
- **thk-abandura** (ألبرت باندورا): صُححت سنة "تجارب Bobo Doll" من 1973 (غير موجودة) لـ1961/1963 الموثقتين، وصُحح تعارض id/title في رابط سكينر.
- **thk-abbagnano**: `belongs_to` من sch-existential-therapy (إكلينيكي) إلى sch-existentialism (فلسفي) لأنه فيلسوف لا معالج؛ `active_end` حُيّد لعدم وجود سند.
- **thk-abd-al-karim-al-jili**: حذف قسم اقتباسات بالكامل (القائمة السوداء)، ملاحظة غياب `related` سُجّلت لفريق Task 1.
- **thk-abdallah-laroui**: `active_end` حُيّد (لا سند لادعاء وفاة 2024) — **قرار حساس**، انظر تحت.
- **thk-abraham-geiger**: راجع أعلاه — أخطر تصحيح نسبة في الدفعة (استحالة زمنية).
- **thk-abramovitch, thk-abu-al-barakat-al-baghdadi, thk-abu-al-hasan-al-amiri, thk-abu-sulayman-al-sijistani**: حذف قسم/جملة القائمة السوداء فقط، باقي المحتوى (هوية/تواريخ/نسبة) تحقق سليم.
- **thk-achristensen**: راجع أعلاه — مؤلفان مختلقان.
- **thk-adam-grant**: `belongs_to` بنص حر بلا slug مقابل → حُذف الرابط وسُجّل طلب slug جديد (`sch-organizational-psychology`) في `agents_specs/requests-spark.md`.
- **thk-adamblatner**: `belongs_to` إلى `sch-psychodrama`؛ حُذفت 3 روابط related كانت متناقضة مع gaps نفسها (تدّعي الحذف وتُبقيها).
- **thk-adams**: حُذفت جملة انتساب مؤسسي غير موثّق (SPEP-UK) — **قرار حساس**.
- **thk-adler**: `active_start` من null إلى 1902 (انضمامه لحلقة فرويد، حقيقة تاريخية لا تخمين).
- **thk-adorno**: راجع أعلاه — تصحيح تصنيف جوهري. **قرار حساس**.
- **thk-afghani**: `edges` من نص حر إلى `sch-arab-renaissance`؛ إضافة "بعد وفاته" صريحة لسنتي 1899/1911.
- **thk-afreud**: تصحيحات جنس وحسابية (راجع أعلاه).
- **thk-agoldstein**: `belongs_to` إلى `br-aggression-treatment`؛ حذف سطر gaps مكرر.
- **thk-agreen** (أندريه غرين): `belongs_to` إلى `br-lacanian`.
- **thk-ahmad-sirhindi**: إعادة صياغة gap قريبة من القائمة السوداء.
- **thk-ahofmann** (ألبرت هوفمان): `belongs_to` إلى `sch-psychedelic-assisted-therapy`.
- **thk-aichhorn**: استبدال جملة gaps قالبية بفجوة محددة.
- **thk-ainsworth**: حذف اقتباسين غير موثقين؛ `edge` من نص حر إلى `br-attachment-theory`.
- **thk-aizenstat**: حذف جملة القائمة السوداء من gaps.
- **thk-aj-ayer**: حذف قسم اقتباسات؛ إبقاء عبارة سردية موثقة تاريخياً ضمن المتن — **قرار حساس**، انظر تحت.
- **thk-ajanov** (آرثر يانوف): `belongs_to` إلى `br-primal-therapy`.
- **thk-ajernberg**: راجع أعلاه — أخطر تصحيح تاريخ في الدفعة، بمصدر خارجي.

## متوقف عنده (لرئيس التحرير)
- **thk-adorno**: تغيير `belongs_to` من الوجودية إلى مدرسة فرانكفورت قرار محتوى جوهري لشخصية تأسيسية كبرى، وليس تصحيحاً تجميلياً — يستحق مراجعة بشرية مباشرة قبل الترقية.
- **thk-abdallah-laroui**: هل العروي حي فعلاً حتى الآن؟ الملف الأصلي افترض `active_end: 2024` بلا مصدر داخل المتن؛ حُيّد لـ`null` بدل التخمين.
- **thk-adams**: هل انتساب "SPEP-UK" صحيح من مصدر خارج معرفة النموذج؟ حُذف احتياطياً لعدم القدرة على التحقق.
- **thk-aalladin**: فصل علادين عن "مدرسة سيلفستر" التجارية — لو فيه مصدر داخلي يوثّق تعاوناً فعلياً، يُراجَع قبل الترقية.
- **thk-aj-ayer**: عبارة سردية («أنه كان كله خاطئاً تقريباً») موثقة تاريخياً على نطاق واسع (يُرجَّح من مقابلة برايان ماجي 1978) لكن بلا مصدر/سنة دقيقين في متناول الـsubagent — تُركت في السياق السردي (مش في قسم اقتباسات مستقل)؛ قرار مفتوح هل تُحذف تطبيقاً صارماً لقاعدة 5.
- **thk-abraham-geiger**: يستحق تتبع مصدر خطأ "زانزفين"/كتاب روزنتسفايغ الأصلي — احتمال دمج بيانات من ملف مختلف تماماً (روزنتسفايغ) في وقت إنشاء الملف.
- **thk-ajernberg**: تصحيح سنة الوفاة (1993 بدل 2013) بُني على بحث خارجي (goodtherapy.org/theraplay.org) لا مصدر داخل الأطلس — يحتاج تأكيداً من نعي معاصر أو سجل وفيات قبل الترقية.

## الملفات
content/ar/thinkers/thk-aabdelkhalek.md
content/ar/thinkers/thk-aabrer.md
content/ar/thinkers/thk-aalladin.md
content/ar/thinkers/thk-aalvarez.md
content/ar/thinkers/thk-abalint.md
content/ar/thinkers/thk-abandura.md
content/ar/thinkers/thk-abbagnano.md
content/ar/thinkers/thk-abd-al-karim-al-jili.md
content/ar/thinkers/thk-abdallah-laroui.md
content/ar/thinkers/thk-abraham-geiger.md
content/ar/thinkers/thk-abramovitch.md
content/ar/thinkers/thk-abu-al-barakat-al-baghdadi.md
content/ar/thinkers/thk-abu-al-hasan-al-amiri.md
content/ar/thinkers/thk-abu-sulayman-al-sijistani.md
content/ar/thinkers/thk-achristensen.md
content/ar/thinkers/thk-adam-grant.md
content/ar/thinkers/thk-adamblatner.md
content/ar/thinkers/thk-adams.md
content/ar/thinkers/thk-adler.md
content/ar/thinkers/thk-adorno.md
content/ar/thinkers/thk-adud-al-din-al-iji.md
content/ar/thinkers/thk-aferro.md
content/ar/thinkers/thk-afghani.md
content/ar/thinkers/thk-afreud.md
content/ar/thinkers/thk-agoldstein.md
content/ar/thinkers/thk-agreen.md
content/ar/thinkers/thk-ahiqar.md
content/ar/thinkers/thk-ahmad-sirhindi.md
content/ar/thinkers/thk-ahofmann.md
content/ar/thinkers/thk-aichhorn.md
content/ar/thinkers/thk-ainsworth.md
content/ar/thinkers/thk-aizenstat.md
content/ar/thinkers/thk-aj-ayer.md
content/ar/thinkers/thk-ajanov.md
content/ar/thinkers/thk-ajernberg.md
