# مراجعة قرنطينة — الدفعة B (20 ملف thk-)

الحالة: مكتمل
الملفات: 20 (thk-savodnik, thk-wolf, thk-raphael, thk-rhanson, thk-mrolls, thk-moss, thk-mnichols,
thk-rkaes, thk-mayeroff, thk-rshort, thk-sleclaire, thk-mtotton, thk-philippe-cunningham,
thk-robert-emery, thk-sstanley, thk-svami-akhilananda, thk-roland-tolentino, thk-peperzak,
thk-robert-rotella, thk-bill-ohanlon)

## الأرقام

`preflight_check.py` قبل → بعد: **124 مخالفة → 0 مخالفة** (20/20 ملف نظيف).

توزيع المخالفات المصححة حسب النوع:

| النوع | العدد | طريقة التصحيح |
|---|---|---|
| `related`: id غير موجود فعلاً كملف | ~78 | حُذف الرابط؛ لو كان مهماً سُجّل في `gaps` أنه أُزيل لعدم وجود ملف. عدد منها كان له slug بديل حقيقي (مثلاً thk-hkohut → thk-kohut، thk-wreich → thk-reich، thk-simoneweil → thk-weil، thk-mheidegger → thk-heidegger...) فاستُبدل بدل الحذف |
| `related`: id/title متضاربان (نسخ-لصق) | ~14 | صُحّح الـtitle ليطابق حرفياً عنوان الملف المستهدف الحقيقي (مثلاً "يوجين مينكوفسكي" → "أوجين مينكوفسكي"، "لودفيغ بنسوانغر" → "لودفيغ بينسوانغر"، "جان-بول سارتر" → "جان بول سارتر"...) |
| `edges`: target نص حر مش slug | 10 | استُبدل بـslug حقيقي من `schools/`/`branches/` حيث وُجد (مثل br-sotp، br-affective-neuroscience-informed، sch-eft-couples، sch-imago، br-lacanian، br-sport-psychology، sch-solution-focused). حيث لم يوجد مقابل دقيق (3 حالات: العلاج الأسري البنيوي، طريقة غوتمان، علم النفس الفيدي) حُذف الرابط (`edges: []`) وسُجّل في `agents_specs/missing-schools.md` |
| `gaps`: سطر يؤكد حقيقة بدل ما يسمي فجوة | 15 | حُذفت جمل من نوع "سنة الميلاد (س) والوفاة (ص) موثّقتان" واستُبدلت بفجوات حقيقية (روابط محذوفة، أسماء غير موثقة) |
| سنة في المتن بعد `active_end` بلا إشارة وفاة | 2 | thk-raphael (2015 بعد active_end=1995) وthk-mayeroff (1979 ثم 2010 بعد active_end=1971) — أُزيلت الإشارة الزائدة للسنة من المتن الرئيسي، وأُضيفت عبارة "بعد وفاته" صراحة عند ذكر طبعة لاحقة (Mayeroff، طبعة 2010) |

## قرارات اتخذتها

- استبدلت أي id مكسور بـslug حقيقي **فقط** عندما وجدت ملفاً فعلياً بنفس الشخص/المفهوم (تحقق يدوي بـ`find`/`grep` على `content/ar/`)، لا اختراع.
- لم أخترع أي slug جديد إطلاقاً. حيث لا يوجد بديل حقيقي حذفت الرابط وسجلت السبب في `gaps` (لملفات thk-/con-/dis-) أو في `missing-schools.md` (لملفات schools/branches عبر `edges`).
- 3 مدارس/تيارات لم يوجد لها ملف مطابق دلالياً فعلياً أُضيفت إلى `agents_specs/missing-schools.md`:
  العلاج الأسري البنيوي (من thk-mnichols)، طريقة غوتمان الزوجية (من thk-sstanley)، علم النفس الفيدي (من thk-svami-akhilananda).
- صححت أسماء ثنائيات مكررة صامتة لنفس الشخص (مثال: thk-jlacan/thk-llacan في thk-sleclaire.md كانا نسخاً زائدة عن thk-lacan الموجود بالفعل — حُذفا).
- لم أعدّل أي محتوى سردي/تحليلي غير مرتبط بالمخالفات الآلية (لا تعميق، لا مصادر جديدة) التزاماً بمبدأ "تاسك واحد = عملية واحدة".

## أمر التحقق

```
python3 scripts/build_slug_index.py
python3 scripts/preflight_check.py <الملفات العشرين> → ✅ 20 ملف — صفر مخالفات آلية.
```

## الملفات

content/ar/thinkers/thk-savodnik.md · thk-wolf.md · thk-raphael.md · thk-rhanson.md · thk-mrolls.md ·
thk-moss.md · thk-mnichols.md · thk-rkaes.md · thk-mayeroff.md · thk-rshort.md · thk-sleclaire.md ·
thk-mtotton.md · thk-philippe-cunningham.md · thk-robert-emery.md · thk-sstanley.md ·
thk-svami-akhilananda.md · thk-roland-tolentino.md · thk-peperzak.md · thk-robert-rotella.md ·
thk-bill-ohanlon.md
