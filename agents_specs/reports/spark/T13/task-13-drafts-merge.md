# Task 13 — دمج مسار drafts/thinkers القديم في drafts/spark/thinkers

الحالة: مكتمل
العملية: نقل (move) 56 ملف مفكر من `content/ar/drafts/thinkers/` إلى `content/ar/drafts/spark/thinkers/` | الملفات: 56

## الفحص قبل النقل
- فحص تعارض بالاسم (filename): **صفر تعارض** — لا يوجد أي ملف من الـ56 له نفس اسم الملف في `drafts/spark/thinkers/`.
- فحص تعارض بعنوان `title` في الـfrontmatter (بحث عن كل عنوان من الـ56 داخل frontmatter لكل ملف
  من الـ1200 في `drafts/spark/thinkers/`): **صفر تطابق حقيقي**. (فحص أولي بالبحث النصي الحر أظهر
  تطابقات كاذبة كثيرة — أسماء الـ56 مذكورة داخل حقول `related` لملفات أخرى، وليست ملفات مستقلة
  بنفس الاسم؛ التحقق الدقيق بمطابقة سطر `title:` نفسه فقط أزال كل هذه الحالات الكاذبة).
- **لا يوجد أي حالة دمج حقيقية مطلوبة** — كل الـ56 ملفاً أشخاص جدد فعلاً غير موجودين بأي slug آخر
  في `drafts/spark/thinkers/`.

## الأرقام
عدد ملفات `drafts/spark/thinkers/`: قبل 1200 → بعد 1257 (فرق 57 = 56 ملف .md + إزالة `.DS_Store` لم يُحتسب)
عدد ملفات `content/ar/drafts/thinkers/`: قبل 56 (+`.DS_Store`) → بعد 0 (المجلد أُزيل بالكامل)

## أمر التحقق
`python3 scripts/build_slug_index.py` → ✅ فهرس الـslugs: 6913 عنصر (6621 معتمد + 292 مسودة).
⚠️ تعارضات slug بين المعتمد والمسودات: 1116 (بلا تغيير ملموس عن الرقم المُبلَّغ سابقاً — هذه
التعارضات في معظمها بين ملفات approved قديمة وslugs في drafts/spark غير متعلقة بالـ56 ملف المنقول؛
لم يظهر أي من أسماء الـ56 (`thk-malan`, `thk-maslach`, ... `thk-zurayk`) في قائمة التعارض).

## قرارات اتخذتها
- نُقلت كل الـ56 ملفاً بالـ`mv` (نقل لا نسخ) بنفس أسماء الملفات (slugs) بلا أي تعديل محتوى.
- حُذف `.DS_Store` (ملف نظام macOS بلا محتوى) من `content/ar/drafts/thinkers/` قبل حذف المجلد الفارغ.
- المجلد `content/ar/drafts/thinkers/` أُزيل بالكامل (`rmdir`) — المسار القديم مقفول رسمياً من الآن.

## متوقف عنده (لرئيس التحرير)
- لا شيء. لم تظهر أي حالة تعارض محتوى جوهري تستحق سؤالاً.

## الملفات
thk-malan.md, thk-maslach.md, thk-mccrae.md, thk-melika.md, thk-metzinger.md, thk-mikulincer.md,
thk-moffitt.md, thk-moscovici.md, thk-muran.md, thk-najati.md, thk-neisser.md, thk-nijenhuis.md,
thk-okasha.md, thk-pargament.md, thk-philippa-foot.md, thk-philippe-pinel.md, thk-politzer.md,
thk-rachman.md, thk-rassool.md, thk-raymond-cattell.md, thk-richard-lazarus.md, thk-rothman.md,
thk-rubinstein.md, thk-rutter.md, thk-salkovskis.md, thk-schacter.md, thk-selye.md,
thk-seyyed-hossein-nasr.md, thk-sharabi.md, thk-shaver.md, thk-shedler.md, thk-sifneos.md,
thk-soueif.md, thk-spearman.md, thk-sperling.md, thk-sroufe.md, thk-stanley-hall.md,
thk-sternberg.md, thk-strawson.md, thk-tomasello.md, thk-tomkins.md, thk-tononi.md,
thk-treisman.md, thk-tronick.md, thk-tulving.md, thk-van-der-hart.md, thk-vico.md, thk-wallon.md,
thk-walter-cannon.md, thk-whitehead.md, thk-yerkes.md, thk-yusuf-murad.md, thk-zahavi.md,
thk-zajonc.md, thk-zayour.md, thk-zeno-citium.md, thk-zurayk.md
