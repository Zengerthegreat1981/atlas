# English slug map — Phase 2 (2026-11-13)

## Purpose
Record of every Phase 2 slug decision, written BEFORE any file is renamed or moved.
No rename without a manifest entry. No deletions ever — duplicates go to
`content/en/_merged/` with a manifest entry. Never edit `content/ar/`.
Source: `scripts/en_slug_map.json` (generated 2026-11-08: 99 pairs + 6 duplicate EN
twins = 105 conflicts) re-verified against the CURRENT English files on 2026-11-13
after Phase 1 (625 files completed). All 99 pairs verified by reading EN + AR
frontmatter on the Mac; 0 missing on either side.

## Verified counts (99 pairs)
- RENAME (same node, same prefix/folder): 68 — of which Group 1 (thinkers) = 40,
  remaining = 28.
- PREFIX-ONLY (same node, same folder, slug prefix differs, e.g. scl- -> sch-
  inside schools/, hst- -> thk- inside thinkers/): 13 — renames, no folder move.
- CROSS-TYPE, genuine (same node, different folder/type, e.g. wrk- vs stu-,
  scl- vs con-): 12 — needs a folder/type decision, NOT a plain rename.
- COLLISION (different nodes sharing a name): 3.
- HELD: 1 (con-division-labor, Phase 1 held duplicate).
- MERGE-DECISION: 2 (Buber; Becker twins).
- Total: 68 + 13 + 12 + 3 + 1 + 2 = 99. Standing conflicts after Group 1: 59.
- The 6 duplicate EN twins were already archived to `content/en/_merged/` on
  2026-11-08 with a MANIFEST.md entry; verified present 2026-11-13.
- NFD filenames: thk-émile-durkheim and thk-kimberlé-crenshaw — do NOT try to fix
  filenames on this ExFAT volume; frontmatter slugs are NFC and correct.
- Count reconciliation: true Phase 1 universe is 675 files (658 baseline + 17 undercount: 11 in the smaller folders — 53 files, not 42 estimated — plus 6 schools missed by Batch 11's cutoff). 631 completed + 44 held = 675. Corrected 2026-11-13 ~20:04 EET (was 669).

## Group 1 — RESOLVED 2026-11-13 (40 thinker renames, thk -> thk)
Format: old slug (old EN id) -> new slug (AR id). Frontmatter slug and id updated
to the AR values; everything else byte-identical except the noted date fixes.
- thk-ali-al-wardi (SOC-14153) -> thk-alwardi (THK-6447)
- thk-anselm-l-strauss (SOC-14117) -> thk-anselm-strauss (THK-6531)
- thk-arjun-appadurai (ANT-13043) -> thk-appadurai (THK-6388) [date fix: birth 1956 -> 1949]
- thk-arlie-russell-hochschild (SOC-14138) -> thk-hochschild (THK-6520)
- thk-auguste-comte (SOC-14100) -> thk-comte (THK-0853)
- thk-bell-hooks (SOC-14141) -> thk-bhooks (THK-0757)
- thk-boas (ANT-13016) -> thk-franz-boas (THK-6495)
- thk-bruno-latour (ANT-13044) -> thk-latour (THK-6378) [date fix: died "present" -> 2022]
- thk-donna-haraway (ANT-13080) -> thk-haraway (THK-1131)
- thk-douglas (ANT-13017) -> thk-mary-douglas (THK-12790)
- thk-erving-goffman (SOC-14115) -> thk-goffman (THK-6352)
- thk-florian-znaniecki (SOC-14112) -> thk-znaniecki (THK-6411)
- thk-frantz-fanon (SOC-14148) -> thk-fanon (THK-0431)
- thk-geertz (ANT-13013) -> thk-clifford-geertz (THK-6560)
- thk-georg-simmel (SOC-14105) -> thk-simmel (THK-6365)
- thk-gluckman (ANT-13346) -> thk-max-gluckman (THK-6499)
- thk-gregory-bateson (ANT-13072) -> thk-gbateson (THK-0628)
- thk-harriet-martineau (SOC-14106) -> thk-martineau (THK-6370)
- thk-herbert-blumer (SOC-14116) -> thk-blumer (THK-6440)
- thk-herbert-spencer (SOC-14101) -> thk-spencer (THK-1970)
- thk-howard-s-becker (SOC-14114) -> thk-howard-becker (THK-6382)
- thk-immanuel-wallerstein (SOC-14127) -> thk-wallerstein (THK-6472)
- thk-james-s-coleman (SOC-14122) -> thk-coleman (THK-8560) [date fix: died 1992 -> 1995]
- thk-judith-butler (SOC-14142) -> thk-butler (THK-0799)
- thk-karl-marx (SOC-14102) -> thk-marx (THK-1516)
- thk-kimberlé-crenshaw (SOC-14143) -> thk-crenshaw (THK-0859) [NFD filename]
- thk-levistrauss (ANT-13012) -> thk-claude-levi-strauss (THK-2315)
- thk-linda-tuhiwai-smith (ANT-13350) -> thk-lindatuhiwai (THK-1457) [date fix: born 1957 -> 1950]
- thk-max-weber (SOC-14104) -> thk-weber (THK-2864)
- thk-michel-foucault (SOC-14130) -> thk-foucault (THK-2344)
- thk-myerhoff (ANT-13347) -> thk-barbara-myerhoff (THK-8963)
- thk-ortner (ANT-13018) -> thk-sherry-ortner (THK-13386)
- thk-patricia-hill-collins (SOC-14140) -> thk-phcollins (THK-1741)
- thk-pierre-bourdieu (SOC-14129) -> thk-bourdieu (THK-6377)
- thk-ralf-dahrendorf (SOC-14124) -> thk-dahrendorf (THK-6469)
- thk-robert-k-merton (SOC-14120) -> thk-robert-merton (THK-8500)
- thk-talcott-parsons (SOC-14119) -> thk-parsons (THK-7350)
- thk-turner (ANT-13015) -> thk-victor-turner (THK-6561)
- thk-zora-hurston (ANT-13062) -> thk-zora-neale-hurston (THK-8950)
- thk-émile-durkheim (SOC-14103) -> thk-durkheim (THK-6364) [NFD filename]
All 40 rename targets were checked free in content/en/thinkers/ before renaming.

## Remaining renames (28, same prefix/folder) — NOT YET DONE
- con-agency (SOC-14222) -> con-agency-anthropology (CON-18153) [EN sociology-flavoured, AR anthropology practice-theory — same concept, merge check noted]
- con-bilateral (ANT-13157) -> con-bilateral-kinship (CON-12641)
- con-habitus (SOC-14219) -> con-habitus-anthropology (CON-18152)
- con-shaman (ANT-13095) -> con-shamanism (CON-12636)
- con-social-capital (ANT-13291) -> con-econ-anthropology-6 (CON-13006)
- con-rites-passage (ANT-13096) -> con-rite-of-passage (CON-12634)
- sch-comtean-positivism-english (SOC-14000) -> sch-comtean-positivism (SCH-0930)
- sch-durkheimian-functionalism-english (SOC-14003) -> sch-durkheimian-structural-functionalism (SCH-0933)
- sch-marxist-classical-sociology-english (SOC-14002) -> sch-marxist-classical-sociology (SCH-0932)
- sch-parsonian-agil-english (SOC-14009) -> sch-parsonian-structural-functionalism-agil (SCH-0970)
- sch-simmelian-formal-english (SOC-14005) -> sch-simmelian-formal-sociology (SCH-0939)
- tec-phenomenological-method (TEC-0205) -> tec-phenomenological-exploration (TEC-0003)
- wrk-african-systems (ANT-13137) -> wrk-african-political-systems-fortes-evans-pritchard (WRK-9808)
- wrk-argonauts (ANT-13029) -> wrk-argonauts-western-pacific-malinowski (WRK-2115)
- wrk-coming-age (ANT-13130) -> wrk-coming-of-age-samoa-mead (WRK-2119)
- wrk-interpretation-cultures (ANT-13031) -> wrk-interpretation-of-cultures-geertz (WRK-2113)
- wrk-liquid-modernity (SOC-14327) -> wrk-liquid-modernity-bauman (WRK-9889)
- wrk-mind-primitive (ANT-13035) -> wrk-mind-of-primitive-man-boas (WRK-9201)
- wrk-orientalism (SOC-14339) -> wrk-orientalism-said (WRK-0414) [AR gaps flag a second AR dup wrk-orientalism-edward-said, unresolved]
- wrk-outline-of-a-theory-of-practice (SOC-14321) -> wrk-outline-theory-practice-bourdieu (WRK-13169)
- wrk-purity-danger (ANT-13034) -> wrk-purity-and-danger-douglas (WRK-9204)
- wrk-structure-function-primitive (ANT-13341) -> wrk-structure-function-primitive-society-radcliffe-brown (WRK-9408)
- wrk-the-presentation-of-self-in-everyday-life (SOC-14304) -> wrk-goffman-presentation-self (WRK-0328)
- wrk-the-protestant-ethic-and-the-spirit-of-capitalism (SOC-14301) -> wrk-protestant-ethic-spirit-capitalism-weber (WRK-2320)
- wrk-the-second-sex (SOC-14314) -> wrk-second-sex (WRK-0447) [AR gaps flag a second AR dup wrk-the-second-sex-beauvoir, unresolved]
- wrk-the-social-system (SOC-14307) -> wrk-social-system-parsons (WRK-2500)
- scl-psychological-anthropology (ANT-13037) -> sch-psychological-anthropology (SCH-1115) [same schools/ folder, prefix change only]
- wrk-patterns-culture (ANT-13131) -> wrk-patterns-of-culture-benedict (WRK-2118)

## Prefix-only renames (13, same folder, slug prefix differs) — NOT YET DONE
- hst-arrian (HST-0006) -> thk-arrian (THK-12568) [thinkers/]
- hst-posidonius (HST-0009) -> thk-posidonius (THK-2484) [thinkers/]
- hst-xenophon (HST-0003) -> thk-xenophon (THK-12567) [thinkers/]
- scl-applied-anthropology (ANT-13004) -> sch-applied-anthropology-expanded (SCH-12386) [schools/]
- scl-british-functionalism (ANT-13002) -> sch-british-functionalism (SCH-13229) [schools/]
- scl-development-anthropology (ANT-13284) -> sch-applied-anthropology-development (SCH-13221) [schools/; AR is a sub-node of applied anthropology]
- scl-digital-anthropology (ANT-13045) -> sch-digital-anthropology (SCH-1132) [schools/]
- scl-economic-anthropology (ANT-13039) -> sch-economic-anthropology-expanded (SCH-12382) [schools/]
- scl-feminist-anthropology (ANT-13007) -> sch-feminist-anthropology (SCH-1105) [schools/; EN still a stub, 931 B — see Phase 1 misses]
- scl-linguistic-anthropology (ANT-13006) -> sch-linguistic-anthropology-expanded (SCH-12385) [schools/; EN still a stub, 939 B]
- scl-medical-anthropology (ANT-13005) -> sch-medical-anthropology (SCH-1112) [schools/; EN still a stub, 957 B]
- scl-queer-anthropology (ANT-13055) -> sch-queer-anthropology (SCH-13093) [schools/]
- scl-urban-anthropology (ANT-13008) -> sch-urban-anthropology-expanded (SCH-12384) [schools/]

## Genuine cross-type decisions (12) — DO NOT rename without a folder/type decision
- br-conversation-analysis (SOC-14402) -> sch-conversation-analysis (SCH-0929) [EN branch, AR school]
- con-content-analysis (SOC-14265) -> ins-content-analysis-method (INS-0315) [EN concept, AR instrument]
- scl-disability-anthropology (ANT-13054) -> con-disability-anthropology (CON-18128) [EN school, AR concept]
- scl-sensory-anthropology (ANT-13046) -> con-sensory-anthropology (CON-12628) [EN school, AR concept]
- wrk-balinese-cockfight (ANT-13268) -> stu-geertz-balinese-cockfight (STU-1107) [EN work, AR study]
- wrk-nuer (ANT-13129) -> stu-evans-pritchard-the-nuer (STU-1103) [EN work, AR study]
- wrk-political-systems (ANT-13136) -> stu-leach-political-systems-highlands-burma (STU-1278) [EN work, AR study]
- wrk-schism-continuity (ANT-13135) -> stu-turner-schism-continuity (STU-1106) [EN work, AR study]
- wrk-street-corner-society (SOC-14318) -> stu-whyte-street-corner-society (STU-1271) [EN work, AR study]
- wrk-the-sociological-imagination (SOC-14303) -> con-sociological-imagination-mills (CON-10001) [EN work, AR concept]
- scl-cultural-relativism (ANT-13001) -> con-cultural-relativism-boas (CON-3142) [EN school, AR concept]
- scl-political-anthropology (ANT-13038) -> br-political-anthropology-subfield (BRN-1126) [EN school, AR branch]

## Collisions (3) — DO NOT rename; different nodes sharing a name
- br-digital-sociology (SOC-14438) vs wrk-digital-sociology-lupton (WRK-9897): EN is the field/subdiscipline; AR is Lupton's 2014 book only.
- con-kinship (ANT-13019) vs wrk-kinship-anthropology-sahlins (WRK-12457): EN is the general concept; AR is Sahlins' 2013 book "What Kinship Is—And Is Not".
- wrk-forest-symbols (ANT-13033) vs stu-turner-lele-ritual (STU-1618): EN file is actually "The Ritual Process" (liminality/communitas); AR is "The Forest of Symbols" (Ndembu ritual, 1967). EN en field/sources mix both books — content decision needed.

## Held (1) + Merge decisions (2)
- HELD: con-division-labor (ANT-13119) -> con-econ-anthropology-9 (CON-13009): EN is a held duplicate of con-labor-division (ANT-13184); merge/redirect decision, not a rename.
- MERGE-DECISION: thk-buber (THK-0314) vs thk-mbuber (THK-1538): same person 1878–1965, but distinct entries with different school lineages (EN belongs_to existential school; AR belongs_to sch-judaism-existential / philosophy crumb). Needs a merge decision, never a plain rename. RESOLVED 2026-11-13 ~20:11 EET in Group 4: no second EN file existed — only the untranslated thk-buber stub; the AR side had already merged its duplicate (AR gaps note, archived AR duplicate in content/ar/_merged/thinkers/thk-buber.md). Single EN entry completed under thk-buber THK-0314 (1,002 body words, 6 dated sources); no archive needed.
- MERGE: thk-ernest-becker (completed Phase 1 entry) vs EN stub thk-becker.md (THK-0308, [EN TRANSLATION NEEDED], 2,747 B): same person, same id; the stub occupies the AR-matching slug. Merge the stub into the completed file under thk-becker; stub to _merged/ with a manifest entry. NOT a plain rename. RESOLVED 2026-11-13 ~20:10 EET in Group 4: stub archived to content/en/_merged/thinkers/thk-becker.md with a MANIFEST.md entry; completed entry renamed to thk-becker.md; id updated ANT-13071 -> THK-0308 (AR frontmatter confirmed THK-0308; the completed entry had kept its old EN id, as in Group 1); body byte-identical (58 lines, 7,025 B).
- MERGE (found in Group 2, 2026-11-13): tec-phenomenological-method (TEC-0205, 52 lines, 6,298 B, complete Batch 19 entry, title "Phenomenological Exploration") vs tec-phenomenological-exploration (TEC-0003, 61 lines, 7,189 B, complete Batch 19 entry, same title). Same technique, two complete entries; the target slug was already occupied, so the rename was HELD, both files left untouched. Merge decision for a later group — NOT a plain rename. RESOLVED 2026-11-13 ~20:11 EET in Group 4: merged into a single entry under tec-phenomenological-exploration TEC-0003 (65 lines, 8,240 B, 950 body words, 12 dated sources, method file's distinct material folded in, no duplication); method file archived to content/en/_merged/techniques/tec-phenomenological-method.md with a MANIFEST.md entry.

## Phase 1 misses found in Phase 2 scoping (6 untranslated school stubs)
The schools folder holds 86 files: 40 scl-* completed (Batch 11) + 10 sch-* named (Batch 12) + 30 phantom sch-* held + 6 small scl-* stubs (931–957 B, 2026-09-25, unmodified) that Phase 1 never drafted — they sat just above Batch 11's 929-byte cutoff. Three are in the pairs above (#25, #26, #27); three are unmapped (no AR twin in the 99 pairs): scl-structural-anthropology (941 B), scl-ecological-anthropology (940 B), scl-postmodern-anthropology (937 B). They need a Phase 1 cleanup batch (draft + verify) before or alongside the remaining renames. DONE 2026-11-13 ~20:04 EET: cleanup batch drafted, pushed and verified 6/6 PASS (842–955 body words, 8–11 dated sources each); the 3 prefix-only renames for feminist / linguistic / medical anthropology were then resolved in Phase 2 Group 3. Count correction: true Phase 1 universe is 675 files (658 + 17: 11 smaller folders + 6 schools), 631 complete, 44 held.

## Held items (44) awaiting Phase 2 decisions — unchanged, never deleted
- 30 phantom/template schools: sch-sociology-school-11…40 (SOC-14010–SOC-14039, all exactly 10,267 B, byte-identical template bodies). No real school corresponds to any number. DECISION FOR MINA: delete, or assign real schools to the numbers.
- 3 duplicates: con-social-movement (duplicate of con-social-movements), con-division-labor (duplicate of con-labor-division), axm-existence-precedes-essence (AXM-0001; AR counterpart quarantined 2026-09-01, redirect_to axi-existence-precedes-essence-axiom; no EN axi- file exists — decide: create EN entry under axi- slug, or redirect the EN stub).
- 4 unverifiable/conflated/phantom thinkers: thk-akira-fujii, thk-ming-ming-kuo, thk-sergio-carrasco, thk-abdalla-salem.
- 3 conflated/phantom works: wrk-womans-evolution (Reed 1975 vs Leacock 1981), wrk-fighting-back (no such Collins book; likely Fighting Words 1998), wrk-the-sociological-condition (no such book; "Sociology editors · 1900").
- 4 conflated/unverifiable studies: stu-suburban-dreams, stu-the-dignity-deficit, stu-schoolyard-stories, stu-the-second-shift-in-china.

## Other Phase 2 flags recorded across Phase 1 batches
- Redirects: tec-motivational-interviewing AR is a permanent redirect merged into sch-motivational-interviewing (TEC-0254); EN drafted standalone (TEC-0212) — should EN likewise redirect or stand alone? tec-narrative-therapy AR merged into sch-narrative-therapy; EN drafted standalone. wrk-being-nothingness AR is a redirect stub to wrk-sartre-being-and-nothingness (WRK-0794) — three Atlas files for the same Sartre book.
- Second-file duplicates (EN): wrk-concept-anxiety vs wrk-concept-of-anxiety-kierkegaard; wrk-mans-search vs wrk-frankl-mans-search-for-meaning; wrk-being-time vs wrk-being-and-time-heidegger (described as longer/deepened).
- Id mismatches: tec-psychodrama AR TEC-0285 vs EN TEC-0203 (EN id kept). thk-ulf-hannersson is a misspelling — AR confirms Ulf Hannerz; draft uses "Hannerz", slug/id/en field left as-is.
- Slug collisions EN vs AR (same slug, different nodes): con-grief EN CON-19069 existential grief vs AR CON-0577 Jungian "Grief as a Path of Individuation"; con-adaptation EN ANT-13023 vs AR CON-0878 different nodes sharing a slug. con-bad-faith AR gaps note a terms file trm-mauvaise-foi-bad-faith-sartre on the same concept — merge review.
- Title/slug mismatches (inherited from stubs, for Phase 2 / revision): wrk-anthropology-now slug vs title "Tell My Horse" (Hurston 1938); wrk-primitive-society vs "The Raw and the Cooked" (Lévi-Strauss 1964); wrk-cultural-critique vs "Writing Culture" (1986); wrk-empire title "Empire of Time" vs real book "Empires of Time" (1989); wrk-urban-culture (not a Fox book; body identifies "Urban Anthropology" 1977); wrk-kinship-village (no standalone Bailey book verified; body anchors on "Caste and the Economic Frontier" 1957); wrk-ethnographic-fieldwork (descriptive prefix + "Anthropological Locations" 1997); wrk-forest-symbols titled "The Ritual Process" while slug says forest-symbols; wrk-tiwi-wives titled "The Tiwi of North Australia" (Hart & Pilling 1960) while slug suggests Goodale's "Tiwi Wives" (1971); wrk-global-cities vs "The Global City" (1991); wrk-hawaiian-kinship title "Kinship Systems of Polynesia" vs slug; wrk-the-gift English trans. 1950 vs Cunnison 1954; wrk-la-distinction is the French original title.
- con-socialization vs con-socialization-process drafted as distinct (concept vs process); if the distinction is judged insufficient, con-socialization-process is the candidate to hold — Phase 2/4 review.
- con-memory: EN stub is "Memory and History" (anthropology) vs AR psychology/cognitive memory (CON-1076) — scope mismatch, Phase 2/4.
- DIA-0001: AR gaps record the file does not meet the dia- standard (no documented real encounter with date, place, named participants) — editorial decision open.
- AR-side duplicates flagged in AR gaps (not EN work, noted for completeness): wrk-orientalism-edward-said; wrk-the-second-sex-beauvoir; thk-auguste-comte already merged into thk-comte in AR.
- Standing flags for later passes (NOT Phase 2): frontmatter in all completed files still carries Arabic stub values (type/level/active_end/target_type, Arabic edges/related/gaps in some files) — frontmatter-normalisation pass. Crumb conventions diverged (Batch 11 "Anthropology ← Schools ← Title" vs Batch 12 translated stub crumbs) — align in the revision pass (Phase 4).
- Expansion candidates: 84 already-translated thin files logged across Batches 7–16, not counted in the 658, for a later expansion pass.

## Status
- Group 1 (40 thinker renames): RESOLVED 2026-11-13 ~19:51 EET — 22 frontmatter fixes applied one at a time, 18 renames + frontmatter edits, 4 date fixes, verified 40/40 PASS by 4 independent read-only checkers (new slug/id in frontmatter, old paths gone, line counts unchanged). No approval block this time.
- Group 2 (28 remaining renames + 13 prefix-only): RESOLVED 2026-11-13 ~19:56 EET — 37/38 done and verified 37/37 PASS by 4 independent read-only checkers (new slug/id in frontmatter, old paths gone, line counts unchanged). No approval block. HELD (1): tec-phenomenological-method -> tec-phenomenological-exploration — target slug already occupied by a complete Batch 19 entry on the same technique; both files left untouched, recorded above as a new MERGE decision. HELD (3 prefix-only, Phase 1-missed stubs, untouched for the cleanup batch): scl-feminist-anthropology, scl-linguistic-anthropology, scl-medical-anthropology.
- Group 3 (3 prefix-only renames + 12 cross-type decisions): RESOLVED 2026-11-13 ~20:07 EET — 15/15 done and verified 15/15 PASS by 3 independent read-only checkers (new slug/id in frontmatter, old paths gone, line counts unchanged). No approval block. Prefix-only: scl-feminist-anthropology -> sch-feminist-anthropology (SCH-1105); scl-linguistic-anthropology -> sch-linguistic-anthropology-expanded (SCH-12385); scl-medical-anthropology -> sch-medical-anthropology (SCH-1112). Cross-type: br-conversation-analysis -> sch-conversation-analysis (SCH-0929); con-content-analysis -> ins-content-analysis-method (INS-0315); scl-disability-anthropology -> con-disability-anthropology (CON-18128); scl-sensory-anthropology -> con-sensory-anthropology (CON-12628); wrk-balinese-cockfight -> stu-geertz-balinese-cockfight (STU-1107); wrk-nuer -> stu-evans-pritchard-the-nuer (STU-1103); wrk-political-systems -> stu-leach-political-systems-highlands-burma (STU-1278); wrk-schism-continuity -> stu-turner-schism-continuity (STU-1106); wrk-street-corner-society -> stu-whyte-street-corner-society (STU-1271); wrk-the-sociological-imagination -> con-sociological-imagination-mills (CON-10001); scl-cultural-relativism -> con-cultural-relativism-boas (CON-3142); scl-political-anthropology -> br-political-anthropology-subfield (BRN-1126). Flag for revision pass (Phase 4): all 12 cross-type files still carry their old-type frontmatter type/crumb (e.g. مدرسة / عمل / كتاب, old folder crumbs) — slug + id only were changed, per procedure.
- Group 4 (3 merge decisions): RESOLVED 2026-11-13 ~20:11 EET — 3/3 done and verified by coordinator re-read on the Mac (surviving slug/id, archived files in _merged/ with MANIFEST.md entries, old paths not_found). No approval block. Becker twins: stub archived to _merged/thinkers/, completed entry renamed to thk-becker, id ANT-13071 -> THK-0308 (AR confirmed), body byte-identical (58 lines, 7,025 B). Phenomenological technique: single merged entry under tec-phenomenological-exploration TEC-0003 (65 lines, 8,240 B, 950 body words, 12 dated sources), method file archived to _merged/techniques/. Buber: no second EN file existed, so no archive; single EN entry completed under thk-buber THK-0314 (78 lines, 7,512 B, 1,002 body words, 6 dated sources); AR side had already merged its duplicate. Correction to the manifest's Becker note: the two EN files did NOT share an id — the completed entry kept its old EN id ANT-13071 while the stub carried the AR id THK-0308 (the normal Group 1 pattern); the first Becker worker correctly held on this, and the merge proceeded only after AR confirmed THK-0308.
- Remaining: 3 collisions (no rename) + 1 held (con-division-labor) + 44 held items. All 68 renames, all 13 prefix-only renames, all 12 cross-type decisions, and all 3 merge decisions are now resolved. The 6 Phase 1-missed school stubs were drafted and verified in the cleanup batch 2026-11-13 ~20:04 EET (6/6 PASS).
- Next: Phase 3 (data_extras / EN build) and Phase 4 (full revision) after Phase 2.
