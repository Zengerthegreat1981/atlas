# Task 3.26
الحالة: مكتمل
المسار: spark | العملية: التدقيق القرائي: هوية → جنس → تواريخ → نسبة → اقتباسات → نتائج بحثية | الملفات: 35

نُفذت هذه الدفعة بـ7 subagent متوازي (5 ملفات لكل واحد)، نطاق thk-kkoch..thk-kwitkiewitz (شامل كلاين وكوهوت وكريشنامورتي وكون وويلبر وكوبلر-روس).

## الأرقام
- ملفات سليمة تماماً (بلا مسودة أو غير قابلة للتصحيح ضمن نطاق Task 3): 1 / 35 (thk-kmurah — قائمة مدمَجة لـ19 مؤسِّساً، ليست ملف مفكر فردي).
- **شخصية محتملة الفبركة الكاملة: thk-krischer** — "باري كريشر" غير موثّق كباحث، ولا يوجد بهذا الاسم في أدبيات ART؛ المؤلفون الحقيقيون Goldstein وGlick وGibbs. ملف thk-jcgibbs نفسه كان يسجّل أن الرابط "أُزيل" لكن لم يُحجر فعلياً. أُفرغت السيرة كاملة.
- **ملف مصنَّف رسمياً LIKELY_FABRICATED: thk-knoblauch** — كيان جماعي/placeholder («مؤسِّسو DGAP») مؤكَّد مسبقاً في `missing-thinkers-final-resolution.md` كـ"مرفوض نهائياً — مختلق"، لكن لا يزال منشوراً بسيرة واثقة.
- **هوية غير موثّقة: thk-kstinshoff** — الملف يعترف صراحة بعدم وجود مصدر أولي خارج ورش تدريبية.
- **ثلاثة أخطاء تواريخ جوهرية**: thk-koestenbaum (وفاته ديسمبر 2024 غير مسجلة)، thk-kogan (ميلاده 1955 لا 1935)، thk-kplaut (1913-2009 لا 1907-2000 + ادعاء خاطئ مؤكَّد بأنه شارك في تأسيس IGAP رغم كونه من الجانب المعارض تاريخياً)، thk-kraus (1934-2022 لا 1920-2005).
- **نمط "gaps تدّعي حذف رابط لسه موجود" تأكَّد مرتين إضافيتين**: thk-knakamura (thk-rreibo)، thk-kkoch (thk-lmazza — الرابط كان صحيحاً فعلياً، أُبقي مع تبرير).
- **إزالة رابطين محجورين**: thk-kmorita وthk-knakamura كلاهما كان يربط thk-tisoma المحجور.
- **تصحيح نسبة تاريخي**: thk-krochmal — رابط "thk-solomon" كان يشير فعلياً لشخص مختلف تماماً (روبرت سولومون لا سليمون ميمون).
- **نمط false positive في فحص الجنس**: thk-klein وthk-kristeva — تُركت الصيغ الصحيحة عمداً.
- **أخطاء `edges.belongs_to` نص حر → slug حقيقي**: عدد كبير جداً (kkoch→tec-poetry-therapy، kkoffka→br-gestalt-berlin، klew→sch-social-psychology، klima→sch-existential-therapy، kmaclean→sch-psychedelic-assisted-therapy، kosik→sch-marxism-humanist، kumarila-bhatta→sch-mimamsa، kstinshoff→sch-somatic-experiencing). حالات كثيرة بلا slug مطابق (kleonhard/kraus/kkoch [طب نفسي وصفي وتصنيفي]، kmorita/knakamura [Constructive Living]، krapf، kuki-shuzo [فلسفة يابانية عامة]، kubler-ross، kristin-neff، krishnamurti) أُفرغت مع تسجيل طلبات متعددة.
- جمل القائمة السوداء حُذفت/أُعيد صياغتها في معظم ملفات الدفعة.

## أمر التحقق
python3 scripts/preflight_check.py content/ar/drafts/spark/thinkers/thk-{kkoch,kkoffka,klein,kleonhard,klew,klima,kmaclean,kmorita,knakamura,knoblauch,koestenbaum,kogan,kohut,kosik,kplaut,krapf,kraus,krigby,krippner,krischer,krishnamurti,kristeva,kristin-neff,krochmal,kspence,kstinshoff,kubler-ross,kuhn,kuki-shuzo,kumarila-bhatta,kundakunda,kunkel,kwilber,kwitkiewitz}.md
→ ✅ 34 ملف — صفر مخالفات آلية. thk-kmurah تُرك دون تعديل (خارج نطاق التدقيق القرائي).

## قرارات اتخذتها
راجع "الأرقام" أعلاه للتفصيل الكامل. باقي الملفات صُححت بالأساس: حذف جملة/جمل القائمة السوداء، تصحيح `edges.belongs_to` من نص حر لslug حقيقي أو إفراغه مع تسجيل طلب، حذف روابط `related` بلا سبب مذكور بالمتن أو محجورة/متضاربة id-title، وإصلاح تسلسل تواريخ (إضافة "بعد وفاته/ها" صراحة).

## متوقف عنده (لرئيس التحرير)
- **thk-krischer**: يستحق حذفاً أو استبدالاً بمدخل حقيقي (Barry Glick).
- **thk-knoblauch**: مصنَّف رسمياً LIKELY_FABRICATED منذ فترة لكن لا يزال منشوراً — يستحق حسماً نهائياً (حذف أم إبقاء كعنصر جماعي معلَّم بوضوح).
- **thk-kstinshoff**: هوية غير موثّقة، يحتاج قرار حجر ضمن Task 2.
- **thk-kmurah**: قائمة مدمَجة لـ19 مؤسِّساً في ملف واحد — تحتاج مهمة تقسيم مستقلة، ليست تدقيقاً قرائياً بسيطاً.
- **thk-kplaut**: ادعاء تأسيس IGAP كان خاطئاً بالكامل ومؤكَّداً لا مجرد مشكوك فيه — حُذف فعلياً من المتن، يستحق تأكيداً قبل الترقية.
- **طلبات تصنيف متراكمة**: طب نفسي وصفي/تصنيفي ألماني (kleonhard، kraus، kkoch، قد يخدم kraepelin لاحقاً)، Constructive Living (kmorita، knakamura، dreynolds)، فلسفة يابانية عامة.

## الملفات
content/ar/thinkers/thk-kkoch.md
content/ar/thinkers/thk-kkoffka.md
content/ar/thinkers/thk-klein.md
content/ar/thinkers/thk-kleonhard.md
content/ar/thinkers/thk-klew.md
content/ar/thinkers/thk-klima.md
content/ar/thinkers/thk-kmaclean.md
content/ar/thinkers/thk-kmorita.md
content/ar/thinkers/thk-kmurah.md
content/ar/thinkers/thk-knakamura.md
content/ar/thinkers/thk-knoblauch.md
content/ar/thinkers/thk-koestenbaum.md
content/ar/thinkers/thk-kogan.md
content/ar/thinkers/thk-kohut.md
content/ar/thinkers/thk-kosik.md
content/ar/thinkers/thk-kplaut.md
content/ar/thinkers/thk-krapf.md
content/ar/thinkers/thk-kraus.md
content/ar/thinkers/thk-krigby.md
content/ar/thinkers/thk-krippner.md
content/ar/thinkers/thk-krischer.md
content/ar/thinkers/thk-krishnamurti.md
content/ar/thinkers/thk-kristeva.md
content/ar/thinkers/thk-kristin-neff.md
content/ar/thinkers/thk-krochmal.md
content/ar/thinkers/thk-kspence.md
content/ar/thinkers/thk-kstinshoff.md
content/ar/thinkers/thk-kubler-ross.md
content/ar/thinkers/thk-kuhn.md
content/ar/thinkers/thk-kuki-shuzo.md
content/ar/thinkers/thk-kumarila-bhatta.md
content/ar/thinkers/thk-kundakunda.md
content/ar/thinkers/thk-kunkel.md
content/ar/thinkers/thk-kwilber.md
content/ar/thinkers/thk-kwitkiewitz.md
