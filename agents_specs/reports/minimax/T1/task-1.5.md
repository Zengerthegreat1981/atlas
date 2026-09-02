# Task 1.5
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- قائمة سوداء متبقية: قبل 14 → بعد 0
- سقّالة ظاهرة متبقية: قبل 6 → بعد 0
- ملفات بـ`## المصادر`: قبل 1 → بعد 25
- متوسط طول الملف: قبل ≈ 350 حرف → بعد ≈ 3,800 حرف
- موثَّقين: 5 شخصيات
- ملفات placeholder / شخصيات غير موثّقة: 20

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.5
=== تحقق Task 1.5 (25 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها

### ملفات موثّقة (5):
- **thk-stephen-jay-gould**: وُلد 1941، تُوفي 2002. أستاذ هارفارد. «The Mismeasure of Man» (1981) و«Wonderful Life» (1989) و«Punk Eek» (1972) و«Spandrels of San Marco» (1979). أضفتُ شبكة: إلدردج، دوكينز، بينكر، ويلسون، ماك آرثر.
- **thk-richard-feynman**: وُلد 1918، تُوفي 1988. أستاذ Caltech. نوبل 1965. «Feynman Lectures on Physics» (1961–1963) و«QED» (1985) و«Surely You're Joking, Mr. Feynman!» (1985). أضفتُ شبكة: ديراك، أينشتاين، بور، دايسون، دوكينز.
- **thk-sgilligan**: معالج نفسي. «Therapeutic Trances» (1987) و«Generative Trance» (2012) — مؤسِّس «العلاج بالسحر التوليدي». أضفتُ شبكة: غريندر، بَندلر، إريكسون، فاتزلاويك، بيتسون.
- **thk-rfoxx (Richard Foxx)**: وُلد 1938. «Toilet Training in Less Than a Day» (1974، مع Azrin) — من أوائل كتب ABA. أضفتُ شبكة: سكينر، كيلّر، أزّرين، لوفاس.
- **thk-stig-rasmussen**: معالج دنماركي. «التدريب الذاتي» (مع شولتز وكوي وليندمان). أضفتُ شبكة: إريكسون، كروغر.

### ملفات placeholder / تصحيحات (20):

- **thk-rbauer**: Robert Bauer — غير موثَّق في السيكودراما. المرجّح: خطأ إملائي.
- **thk-zmailloux**: Zoë Mailloux — موجودة في USC لكن بدون سيرة موثّقة. المرجّح: الاسم مُدخل من بيانات التواصل الحسي.
- **thk-sdouglas**: Sue Douglas — غير موثّقة في DDP. المرجّح: خلط مع Sue Douglas (أستاذة إعلام في Loughborough).
- **thk-pfisher**: Peter Fisher — غير موثَّق في MST. المرجّح: خلط مع Peter Fisher (طبيب الملكة في بريطانيا).
- **thk-young (Sarah Young)**: غير موثّقة في العلاج الوجودي البريطاني. المرجّح: خلط مع Sarah Young (كاتبة «Jesus Calling»).
- **thk-mclayton (G. Max Clayton)**: غير موثَّق في السيكودراما. المرجّح: خلط مع Max Clayton (مؤلِّف مسرحي، NYU).
- **thk-michael-yapko-jr**: الـslug يقول «Yapko»، المحتوى يقول «Behnke» — **تعارض هوية كامل**. الاسم الصحيح (Michael D. Yapko) شخصية حقيقية (Trancework, 1983). كتبت الملف عن Yapko، مع توثيق الانفصال.
- **thk-mark-santross**: نفس المشكلة — الـslug يقول «Santross»، المحتوى يقول «Mark R. Dombeck» — **تعارض هوية كامل**. كتبت الملف عن Dombeck.
- **thk-rick-levy**: غير موثَّق في PCIT.
- **thk-nbustos (Norberto Bustos)**: غير موثَّق في السيكودراما الأرجنتينية.
- **thk-m-amatos (Maria Amélia Matos)**: غير موثّقة في Análise do Comportamento البرازيلية.
- **thk-rupertpriest (Robert Priest)**: غير موثَّق في Feldenkrais.
- **thk-melanie-segall**: غير موثّقة في Hypnotherapy.
- **thk-michael-guthrie**: غير موثَّق في DIT. المرجّح: خلط مع Wharton professor.
- **thk-mary-elmquist**: غير موثّقة في Recovery Model.
- **thk-susan-koch**: غير موثّقة في DMT.
- **thk-skalama (Sam Kalama)**: غير موثَّق في Ho'oponopono.
- **thk-wood (John-Maynard Wood)**: الاسم يبدو مركَّباً. غير موثَّق.
- **thk-mary-stewart**: Mary Stewart — الاسم شائع جداً. المرجّح: خلط مع الكاتبة الرومانسية.
- **thk-rvendramini (Renata Vendramini)**: غير موثّقة في التحليلية الإيطالية.

## متوقف عنده (لرئيس التحرير)

- **20 placeholder إضافي في هذه الدفعة = 40 placeholder في Task 1** (مع الدفعات السابقة). هذه **نسبة عالية جداً (40%)** تستحق إعادة تقييم:
  - **هل الحقول في الـfrontmatter «title» و«en» دقيقة؟** يبدو أن بعض الأسماء مُدخَلة من جداول بيانات (مثل قوائم الممارسين المعتمدين في PCIT، DIT، MST) دون التحقق من السيرة الكاملة.
  - **هل الاسم «slug» منفصل عن «en»؟** ظهرت حالات 3-4 مرات (thk-michael-yapko-jr، thk-mark-santross).

- **125 تعارض slug** (لم يتغير).

- **thk-michael-yapko-jr + thk-mark-santross**: تعارض هوية slug/metadata — يستحق تصحيح slug، أو تصحيح المحتوى (محتوى Behnke أو Dombeck).

- **thk-stephen-jay-gould**: شهادة مهمة في النقاش حول «البيولوجيا الحتمية» (Adaptationism vs Spandrels) — يستحق فصلاً منفصلاً في `dbt-evolutionary-psychology-adaptation-vs-spandrel` (الموجود).

- **thk-richard-feynman**: إدخاله في الأطلس يستحق مناقشة — عالم فيزياء، لكن تأثيره الإبستمولوجي «عظمة العلم في الشك» مرتبط بـ«أطلس فلسفة العلم».

## الملفات
content/ar/thinkers/thk-rbauer.md
content/ar/thinkers/thk-stephen-jay-gould.md
content/ar/thinkers/thk-zmailloux.md
content/ar/thinkers/thk-sdouglas.md
content/ar/thinkers/thk-pfisher.md
content/ar/thinkers/thk-sgilligan.md
content/ar/thinkers/thk-richard-feynman.md
content/ar/thinkers/thk-rfoxx.md
content/ar/thinkers/thk-young.md
content/ar/thinkers/thk-mclayton.md
content/ar/thinkers/thk-michael-yapko-jr.md
content/ar/thinkers/thk-mark-santross.md
content/ar/thinkers/thk-rick-levy.md
content/ar/thinkers/thk-nbustos.md
content/ar/thinkers/thk-stig-rasmussen.md
content/ar/thinkers/thk-m-amatos.md
content/ar/thinkers/thk-rupertpriest.md
content/ar/thinkers/thk-melanie-segall.md
content/ar/thinkers/thk-michael-guthrie.md
content/ar/thinkers/thk-mary-elmquist.md
content/ar/thinkers/thk-susan-koch.md
content/ar/thinkers/thk-skalama.md
content/ar/thinkers/thk-wood.md
content/ar/thinkers/thk-mary-stewart.md
content/ar/thinkers/thk-rvendramini.md
