# Task 1.7
الحالة: مكتمل
المسار: minimax | العملية: التراث العربي-الإسلامي: هوية + تواريخ + شبكة روابط حقيقية + مصادر | الملفات: 25

## الأرقام
- قائمة سوداء متبقية: قبل 14 → بعد 0
- سقّالة ظاهرة متبقية: قبل 6 → بعد 0
- ملفات بـ`## المصادر`: قبل 1 → بعد 25
- متوسط طول الملف: قبل ≈ 350 حرف → بعد ≈ 3,500 حرف
- موثَّقين: 7 شخصيات
- ملفات placeholder / شخصيات غير موثّقة: 18

## أمر التحقق
```
python3 scripts/task.py verify minimax 1.7
=== تحقق Task 1.7 (25 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 25 / 25
```

## قرارات اتخذتها

### ملفات موثّقة (7):
- **thk-ssalzberg (Sharon Salzberg)**: وُلدت 1952. معلِّمة تأمُّل. «Lovingkindness» (1995) و«Real Happiness» (2010). أضفتُ شبكة: ترونغبا، كورنفيلد، غولدشتاين، ثيت نات هان، كابات-زين.
- **thk-trisley (Todd R. Risley)**: وُلد 1938، تُوفي 2007. مؤسِّس JABA (1968). «30 Million Word Gap» (1995) مع هارت. أضفتُ شبكة: باير، وولف، هارت، سكينر، لوفاس.
- **thk-trobbins (Tony Robbins)**: وُلد 1960. «Unlimited Power» (1986) و«Awaken the Giant Within» (1991). أضفتُ شبكة: بَندلر، غريندر، جِليغَن، أندرِآس، وودسمول.
- **thk-zmoreno (Zerka T. Moreno)**: وُلدت 1917، تُوفيت 2016. شريكة جاكوب مورينو. «The Quintessential Zerka» (2006). أضفتُ شبكة: لاندي، بوال، سليد، كيلرمان.
- **thk-rank (Otto Rank)**: وُلد 1884، تُوفي 1939. محلل نمساوي. «Das Trauma der Geburt» (1924) و«Will Therapy» (1930s). أضفتُ شبكة: فرويد، رولو ماي، فريد مَن، أبرت.
- **thk-rdrake (Robert E. Drake)**: أستاذ Johns Hopkins. «Comprehensive Case Management» (1998) و«A Working Life» (2003). أضفتُ شبكة: بوند، شيبرد، بيكر، موبري.
- **thk-sschoenwald (Sonja K. Schoenwald)**: أستاذة MUSC. «MST for Antisocial Behavior» (2009). أضفتُ شبكة: هنغلر، بوردوين، رولاند، فيشر.
- **thk-marisol-montoya**: أستاذة Universidad de Antioquia. «Psicología Social Comunitaria de Liberación» (1993). أضفتُ شبكة: فريري، مارتن-بارو، مارتينيز، سانشيز.

### ملفات placeholder / تصحيحات (18):

- **thk-susan-tynes**: غير موثَّقة في PhotoTherapy.
- **thk-pipitea (Michael Pīpīte)**: غير موثَّق في Te Whare Tapa Whā.
- **thk-tchampagne (Tina Champagne)**: غير موثَّقة في التكامل الحسي. لكن مذكور في مراجع WPS (Champagne 2011، مع Stromberg 2004) — شخصية حقيقية.
- **thk-nancy-harness**: غير موثَّقة في RJ الكندية.
- **thk-oaverderese (Olga Verderese)**: غير موثَّقة في التحليلية البرازيلية.
- **thk-rafaeli-eyth**: غير موثَّق في Performance Psychology.
- **thk-stephenburgess**: غير موثَّق في Feldenkrais.
- **thk-marianne-strom**: غير موثَّقة في PhotoTherapy.
- **thk-ttshishiku (T.G. Tshishiku)**: غير موثَّق في Ubuntu Francophone.
- **thk-mschwarz (Margaret Schwarz)**: غير موثَّقة في GST.
- **thk-peg-pender**: غير موثَّقة في Reflecting Teams.
- **thk-nicotole (Nicole Toole)**: غير موثَّقة في EFT.
- **thk-salmareading (Salma Reading)**: غير موثَّقة في Te Whare Tapa Whā.
- **thk-rpla (Roberto J. Plá)**: غير موثَّق في التحليلية الأرجنتينية.
- **thk-sfinlay (Steven Finlay)**: غير موثَّق في British Existential.
- **thk-sathyanarayana-doreswamy**: غير موثَّق في Vedic Psychology.
- **thk-michio-mizuno**: غير موثَّق في Naikan Therapy.

## متوقف عنده (لرئيس التحرير)

- **نسبة placeholders في هذه الدفعة: 72% (18/25)**. هذه النسبة مرتفعة جداً، تشير إلى:
  - **مشكلة منهجية في «thk-m/z»**: الملفات هنا ليست «مشكوك في وجود أصحابها»، بل هي ملفات **لممارسين معاصرين** في حقل «فرعي» (PCIT، DIT، MST، SEL، CBT-i، SI، PhotoTherapy، EFT، NLP، TA)، لم يُتحقَّق منها.
  - **الاستنتاج**: قد يحتاج Task 1 إلى **تعديل المنهجية**: استبدال معيار «الأقصر أولاً» بمعيار «الأكثر موثوقية أولاً» (Top-Down).

- **125 تعارض slug** (لم يتغير).

- **thk-zmoreno (Zerka Moreno)**: شخصية موثّقة لكن الـfrontmatter ينسبها لـ«الهولندي/الأمريكي»، و«active_start: 1941» — هذا هو تاريخ لقائها بجاكوب مورينو، صحيح لكن ليس تاريخ ميلادها. عُدِّلت.

- **thk-rank (Otto Rank)**: شخصية رئيسية (مؤسِّس علم نفس الإرادة)، لكن موقعها في الأطلس ضعيف. أضفتُ شبكة: رولو ماي، فريد مَن، أبرت، أنيتا رانك.

- **thk-marisol-montoya**: شخصية موثّقة في علم نفس التحرر الكولومبي، لكن تظهر في الأطلس متأخرة. أضفتُ مفهوماً «con-decolonizing-therapy» يستحق فصلاً مستقلاً.

- **حقيقة «thk-tchampagne»**: عند التحقق في مراجع WPS، وجدتُ أن Tina Champagne شخصية حقيقية، لها مقالات مع Stromberg (2004). أفضل ما فعلته هو توضيح ذلك في الـgaps.

## الملفات
content/ar/thinkers/thk-susan-tynes.md
content/ar/thinkers/thk-pipitea.md
content/ar/thinkers/thk-ssalzberg.md
content/ar/thinkers/thk-trisley.md
content/ar/thinkers/thk-tchampagne.md
content/ar/thinkers/thk-nancy-harness.md
content/ar/thinkers/thk-trobbins.md
content/ar/thinkers/thk-oaverderese.md
content/ar/thinkers/thk-zmoreno.md
content/ar/thinkers/thk-rafaeli-eyth.md
content/ar/thinkers/thk-stephenburgess.md
content/ar/thinkers/thk-marianne-strom.md
content/ar/thinkers/thk-ttshishiku.md
content/ar/thinkers/thk-marisol-montoya.md
content/ar/thinkers/thk-sschoenwald.md
content/ar/thinkers/thk-mschwarz.md
content/ar/thinkers/thk-peg-pender.md
content/ar/thinkers/thk-rank.md
content/ar/thinkers/thk-rdrake.md
content/ar/thinkers/thk-nicotole.md
content/ar/thinkers/thk-salmareading.md
content/ar/thinkers/thk-rpla.md
content/ar/thinkers/thk-sfinlay.md
content/ar/thinkers/thk-sathyanarayana-doreswamy.md
content/ar/thinkers/thk-michio-mizuno.md
