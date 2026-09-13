import os as _os
# جذرُ المستودع من موضع الملفّ — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import csv

rows = []
with open(_ATLAS_ROOT + '/agents_specs/recheck_batch_4.csv') as f:
    r = list(csv.DictReader(f))

results = {
0: ("CONFIRMED_REAL","Real person is Mary Kruger (IFS Lead Trainer, LMFT, Rimmon Pond Counseling). Corrected name; matches IFS field.","TRUE"),
1: ("LIKELY_FABRICATED","No evidence of a 'Marisa Berkouwer' connected to Sensorimotor Psychotherapy.","N-A"),
2: ("LIKELY_FABRICATED","A real psychologist named Mark R. Dombeck exists but no PCIT connection found; title_ar 'Mark Santross' does not match title_en at all.","N-A"),
3: ("LIKELY_FABRICATED","No specific 'Mark Welch' found connected to experiential therapy; multiple unrelated Mark Welches exist (biologist, ENT nurse researcher, etc).","N-A"),
4: ("LIKELY_FABRICATED","No evidence of a psychology figure named Mary Elmquist in recovery-oriented care.","N-A"),
5: ("LIKELY_FABRICATED","No evidence connecting a Mary Guthrie to Dynamic Interpersonal Therapy (DIT).","N-A"),
6: ("LIKELY_FABRICATED","No specific Mary Stewart found as a TA thought leader; real TA authors are Ian Stewart & Vann Joines.","N-A"),
7: ("LIKELY_FABRICATED","No evidence of a Masaaki Takahashi connected to Naikan therapy.","N-A"),
8: ("LIKELY_FABRICATED","No evidence of a Marvin Chen connected to psychodrama/sociometry.","N-A"),
9: ("LIKELY_FABRICATED","No evidence of a Marek Cieslak in phenomenological psychology research (different Cieslaks found: Matt/Roman Cieslak, unrelated fields).","N-A"),
10: ("LIKELY_FABRICATED","No evidence of a Daniel P. Behnke connected to Ericksonian hypnosis; title_ar 'Daniel Beit' and slug reference Michael Yapko Jr. but no such figure found.","N-A"),
11: ("LIKELY_FABRICATED","No specific Peter Fisher found founding/central to MST; common name, only incidental co-author mentions.","N-A"),
12: ("LIKELY_FABRICATED","No evidence of a Peter A. Godfrey connected to Embodied Relational Therapy (ERT).","N-A"),
13: ("LIKELY_FABRICATED","No evidence of a Cathy/P. Cathy Hackney connected to Body-Mind Centering.","N-A"),
14: ("LIKELY_FABRICATED","No evidence of a Michael Pīpīte connected to Te Whare Tapa Whā (real originator is Sir Mason Durie).","N-A"),
15: ("STILL_UNCERTAIN","A real sex-offender-treatment researcher Ron Langevin exists, but different first name/gender than 'Roni L. Langevin' and no direct SOTP program link confirmed.","N-A"),
16: ("LIKELY_FABRICATED","No evidence of a Rafaeli Eyth connected to performance psychology.","N-A"),
17: ("LIKELY_FABRICATED","No evidence of a Randy Stabler connected to MST; other unrelated Randy Stablers found (automotive, chemical industry).","N-A"),
18: ("LIKELY_FABRICATED","No evidence of a Robert Bauer connected to psychodrama/sociometry as a central figure.","N-A"),
19: ("LIKELY_FABRICATED","No evidence of a Randy Hooton connected to primal therapy.","N-A"),
20: ("STILL_UNCERTAIN","Multiple real 'Rick Levy' psychologists exist but none confirmed as PCIT-specific; ambiguous which one (if any) matches.","N-A"),
21: ("LIKELY_FABRICATED","The real R.K. Narayan is a novelist, not a Vedic psychologist; no separate Vedic-psychology figure by this name found.","N-A"),
22: ("LIKELY_FABRICATED","No evidence of a Robert M. Clark connected to interpersonal neurobiology (real founder is Daniel Siegel).","N-A"),
23: ("LIKELY_FABRICATED","No evidence of a Robert Mosak connected to TEACCH.","N-A"),
24: ("LIKELY_FABRICATED","No evidence of a Robert L. Burgess as a founding/central PCIT figure.","N-A"),
25: ("LIKELY_FABRICATED","No evidence of a Robert E. Cornell connected to Focusing (Gendlin's method); real associated figure is Ann Weiser Cornell (different first name).","N-A"),
26: ("LIKELY_FABRICATED","No evidence of a psychology figure named Robert Duvall connected to Dianetics/Scientology (only the actor Robert Duvall appears, unrelated).","N-A"),
27: ("CONFIRMED_REAL","Robert Fritz is a real author (The Path of Least Resistance) associated with the Psycho-Cybernetics Foundation carrying Maxwell Maltz's legacy.","TRUE"),
28: ("LIKELY_FABRICATED","No evidence of a Rohan J. Gullich connected to sport psychology (real prominent researcher in the area is Arne Güllich, different name).","N-A"),
29: ("STILL_UNCERTAIN","Roland/Rolando B. Tolentino is a real UP Diliman scholar who references Sikolohiyang Pilipino, but he is a film/cultural-studies scholar, not a psychology thinker in that school.","N-A"),
30: ("LIKELY_FABRICATED","No evidence of a Rosemary Alara connected to Dianetics/Scientology.","N-A"),
31: ("LIKELY_FABRICATED","Rachel Brice is a real person but a belly-dance performer, not connected to Body-Mind Centering.","N-A"),
32: ("LIKELY_FABRICATED","No evidence of a Robert Short connected to Imago Relationship Therapy (real founders are Harville Hendrix and Helen LaKelly Hunt).","N-A"),
33: ("LIKELY_FABRICATED","No evidence of a 'Zhou Ruilin' among Chinese Taoist Cognitive Therapy researchers (real names include Zhang, Young, Chang).","N-A"),
34: ("LIKELY_FABRICATED","No evidence of a Robert Priest connected to the Feldenkrais Method.","N-A"),
35: ("LIKELY_FABRICATED","No evidence of a Roberto Viaro connected to Milan Systemic or brief strategic therapy.","N-A"),
36: ("LIKELY_FABRICATED","No evidence of a Salma Reading connected to Te Whare Tapa Whā.","N-A"),
37: ("LIKELY_FABRICATED","No evidence of a Sathyanarayana Doreswamy connected to Vedic psychology as a thinker (only unrelated same/similar-named individuals found).","N-A"),
38: ("CONFIRMED_REAL","Real person is Sandra Lindaman (Senior Training Advisor, Theraplay Institute); title_en 'Sandra Lindaman Booth' and title_ar 'Sara Booth' appear to be a name mix-up but underlying figure matches the Theraplay field closely.","TRUE"),
39: ("LIKELY_FABRICATED","No evidence of a Sue Douglas connected to Dyadic Developmental Psychotherapy (DDP); real founder is Dan Hughes.","N-A"),
40: ("LIKELY_FABRICATED","No evidence of a Sharron Hapai connected to Te Whare Tapa Whā.","N-A"),
41: ("LIKELY_FABRICATED","No evidence of a Shirley Murray connected to the Alexander Technique.","N-A"),
42: ("LIKELY_FABRICATED","No evidence of a Sam Kalama connected to Ho'oponopono as a thinker/teacher.","N-A"),
43: ("LIKELY_FABRICATED","No evidence of a Stefan B. Piper connected to critical psychology.","N-A"),
44: ("LIKELY_FABRICATED","No evidence of a Stephen F. Talley connected to Discernment Counseling (real founder is William Doherty).","N-A"),
45: ("LIKELY_FABRICATED","No evidence of a Stephen Burgess connected to the Feldenkrais Method (a different, unrelated 'Robert Burgess' is a real Feldenkrais practitioner).","N-A"),
46: ("LIKELY_FABRICATED","No evidence of a Stig Rasmussen connected to self-hypnosis (unrelated Rasmussens found: chess player, hypnotist Jørgen Rasmussen).","N-A"),
47: ("LIKELY_FABRICATED","No evidence of a Susan Koch connected to dance/movement therapy (real prominent DMT researchers are Sabine Koch and Nana Koch, different first names).","N-A"),
48: ("LIKELY_FABRICATED","No evidence of a Susan Tynes connected to phototherapy/photo therapy.","N-A"),
49: ("LIKELY_FABRICATED","No evidence of a Takeshi Yasumaru connected to Naikan therapy.","N-A"),
50: ("LIKELY_FABRICATED","No evidence of a Teresa Andreas connected to NLP (real NLP Andreas family figures are Steve, Connirae, and Mark Andreas).","N-A"),
51: ("LIKELY_FABRICATED","No evidence of a Teruo Ohta connected to Naikan therapy.","N-A"),
52: ("LIKELY_FABRICATED","No evidence of a Terry Gillingham connected to Hakomi therapy.","N-A"),
53: ("LIKELY_FABRICATED","No evidence of a Theresa Glasser connected to DDP; real similarly-named psychologist Theresa Glaser found but unrelated field.","N-A"),
54: ("LIKELY_FABRICATED","No evidence of a Thomas Sells connected to Discernment Counseling.","N-A"),
55: ("LIKELY_FABRICATED","No evidence of a Timothy G. Clanton connected to Discernment Counseling.","N-A"),
56: ("LIKELY_FABRICATED","No evidence of a Takeshi Isomae connected to Constructive Living (real founder is David K. Reynolds).","N-A"),
57: ("LIKELY_FABRICATED","No evidence of a Tom Cornwell connected to restorative justice (real restorative-justice author is David J. Cornwell, different first name).","N-A"),
58: ("LIKELY_FABRICATED","No evidence of a Toni L. Sexton connected to PCIT.","N-A"),
59: ("LIKELY_FABRICATED","No evidence of a T.G. Tshishiku connected to Ubuntu psychology.","N-A"),
60: ("LIKELY_FABRICATED","No evidence of a Fabrizio Carrera connected to Milan Systemic family therapy.","N-A"),
61: ("LIKELY_FABRICATED","No evidence of a Wilma Spaulding connected to psychiatric rehabilitation; real researcher William Spaulding (UNL) exists but different first name/gender.","N-A"),
62: ("LIKELY_FABRICATED","No evidence of a Zhu Yihua among Chinese Taoist Cognitive Therapy researchers.","N-A"),
63: ("LIKELY_FABRICATED","No evidence of a Yvani E. Edmon connected to the Feldenkrais Method.","N-A"),
}

with open(_ATLAS_ROOT + '/agents_specs/rechecked_batch_4.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["category","title_ar","title_en","slug","active_period","school","status","note","page_created"])
    for i,row in enumerate(rows if False else r):
        status, note, created = results[i]
        w.writerow([row['category'], row['title_ar'], row['title_en'], row['slug'], row['active_period'], row['school'], status, note, created])

print("done", len(r))
