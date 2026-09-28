# ATLAS Finalization Plan (control chat: "ATLAS project reports consolidation")

Created 2026-09-25. This is the single source of truth. Every other Atlas chat is retired.
All counts below were measured from `content/` on 2026-09-25 (HEAD `3eb35229a`), not taken from session reports.

## 0. Measured baseline

Census script: `scratchpad/census.py`, which parses frontmatter `part` and counts body words.
Excluded: `drafts/` (525) and `_merged/` (188).

### Arabic (`content/ar`): 12,803 live nodes

| part | nodes | <300w | 300–700w | 700w+ | avg w | mission target |
|---|---|---|---|---|---|---|
| psychology | 3,628 | 1,773 | 1,588 | 267 | 361 | core |
| philosophy | 2,921 | 1,280 | 1,503 | 138 | 357 | core |
| sociology | 1,262 | 1,017 | 241 | 4 | 246 | 1,200–1,500 |
| anthropology | 1,167 | 731 | 409 | 27 | 250 | 1,200–1,400 |
| historiography | 1,007 | 657 | 348 | 2 | 196 | 900–1,100 |
| linguistics | 970 | 745 | 217 | 8 | 242 | 1,200–1,400 |
| religious-studies | 888 | 658 | 226 | 4 | 227 | 700–900 |
| legal-theory | 328 | 286 | 36 | 6 | 147 | 700–900 |
| political-economy | **0** | – | – | – | – | 1,100–1,300 |
| bridge | 216 | 127 | 56 | 33 | 375 | – |
| ethics | 181 | 178 | 3 | 0 | **17** | – |
| psychiatry | 122 | 35 | 80 | 7 | 341 | – |
| arab-thought | 112 | 42 | 69 | 1 | 274 | – |

The reports inflated these counts:
- Anthropology 2 reported "1,400 nodes, 100%". Measured: **1,167**.
- Linguistics 2 reported "1,207". Measured: **970** nodes tagged `linguistics`.
- The Sociology Phase 2 report said nodes were expanded to 1,094–1,098 words. The real files are 560–936 words (the Sociology chat flagged this itself).
- The Psychology files review claimed a "65,529-term production DB". It was reverted, and the files are gone (`content/en/terms` has 1 file).
- Several agents tagged 1,000+-word nodes with fixed word ranges, which is a template signature. Depth expansions need spot audits.

### English (`content/en`): 944 files
- Only about **40** files are real English translations of an AR node, which is **0.3%** of 12,803.
- **751** EN files have no AR counterpart. They are English-only nodes written directly by the sociology, historiography and anthropology sessions, with a median of 47 words. They break the "same slug in both languages" rule.
- **424** EN files still carry `[EN TRANSLATION NEEDED]` or have Arabic bodies.
- `data-en.json` and `index-en.html` were last built 2026-08-19 and are stale. `content/en/README.md` records that EN is **frozen by decision**.
- The integrity checker reports dangling `related` links in EN.

## 1. Operating rules (from memory and MISSIONS_INDEX)
0. **ENGLISH FREEZE (user decision 2026-09-25):** `content/en/` is frozen. Do not create, edit, move or delete any EN file. Phase 3 (English) starts only when Phases 1 and 2 (Arabic) are 100% done. Leave the old Atlas chats in place; do not archive them.
0b. **Automation:** the scheduled task `atlas-worker` runs every 30 min. It uses `reports/.atlas_worker.lock` (heartbeat) and spawns 4 Sonnet subagents per run (user decision 2026-09-26; was 2).
1. Only one writer on `content/ar` at a time. All the other Atlas chats must be closed (see MISSIONS_INDEX, the concurrency rule).
2. Sonnet agents get **bounded, checkable batches**: an explicit slug list, an explicit target, and ≤40 files. Opus (this chat) verifies every batch before commit: word counts, integrity checker, and 3 random full reads per batch.
3. Batches never share slugs. Each agent writes only the files on its list.
4. No invented references. Every Sources section needs at least 2 references with title and year. Arabic tradition comes first.
5. Commit after each verified batch, with a message that gives real counts.

## 2. Phases

### Phase 0: hygiene (Opus, 1 session)
- Archive the 10 old Atlas chats.
- Run `check_content_integrity.py` and fix AR errors to 0.
- ~~EN orphans~~ frozen, see rule 0.
- Rebuild `data.json`.
- Keep this file up to date as the single tracker.

### Phase 1: AR coverage to target (Sonnet, sequential missions)
| mission | now | to add | batches (~40) |
|---|---|---|---|
| legal-theory | 328 | +372 → 700 | ~10 |
| political-economy | 0 | +1,100 (backlog 55 items, batch 0 = add `part` to `audit_atlas.py:420` + DR) | ~28 |
| linguistics | 970 | +230 → 1,200 | ~6 |
| anthropology | 1,167 | +33 → 1,200 | 1 |

### Phase 2: AR depth (Sonnet, largest phase)
Goal: every node reaches ≥300 words, and schools, thinkers and works reach ≥600. There are 7,489 nodes under 300 words today.

Priority order:
1. ethics (178 stubs, avg 17 w)
2. legal-theory
3. historiography
4. linguistics
5. sociology
6. religious-studies
7. anthropology
8. psychology
9. philosophy

Size: about 190 batches of 40.

### Phase 3: English version
- The user must decide the scope first: a full 12.8k translation, or a core subset of schools, thinkers and main concepts (about 4k).
- Pipeline: AR node → EN file with the **same slug**. Sonnet translates and Opus spot-checks.
- Translate `scripts/template/data_extras.json`.
- Run `build_atlas.py en` and the EN audit.

### Phase 4: release
- Full audit for both languages.
- Build `data.json`, `data-en.json` and both index files.
- Push, tag the release, and write the closeout report.

## 3. Progress log
| date | batch | result | commit |
|---|---|---|---|
| 2026-09-25 | baseline census | this file | – |
| 2026-09-26 | worker: Phase 0 check | AR integrity 0 errors (12,622 files); `build_atlas.py ar` rebuilt data.json (12,622 items). Note: legal-theory backlog is 41/41 ticked but the section had only 328 nodes, so new slugs are chosen beyond the backlog | – |
| 2026-09-26 | worker: legal-theory B (Western jurisprudence) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; 1 factual fix after reads | 115d4b4e0 |
| 2026-09-26 | worker: legal-theory A (Islamic legal theory) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; 5 title syncs, 3 factual fixes after reads. legal-theory now 388 | 731a127df |
| 2026-09-26 | worker: legal-theory D (Islamic jurists & institutions) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; 1 source fix, 2 factual fixes after reads | 768077892 |
| 2026-09-26 | worker: legal-theory C (Western theory, private/criminal/comparative) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; 1 fix after reads. **legal-theory measured: 448** (target 700; ~252 to go). Note: ~20 `con-legal-rights-NN` 5-word stubs in legal-theory are junk and should be handled in Phase 2 | 92b570e6d |
| 2026-09-26 | worker: legal-theory E (Islamic jurists & usul) | +28 (14 thk, 5 wrk, 9 con), 28/28 pass after 11 expansions; 2 works skipped as existing duplicates; 1 Arabic source added after reads | 0cdde27b6 |
| 2026-09-26 | worker: legal-theory F (Western, international, comparative) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass after 21 expansions; factual fixes in Welzel and P. J. Williams after reads. **legal-theory measured: 506** (target 700) | 816114c87 |
| 2026-09-26 | worker: legal-theory G (modern Arab & Islamic law) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; 1 citation fix (al-Bishri title) after reads | 8d21c4cee |
| 2026-09-26 | worker: legal-theory H (comparative, legal history, public law, law & society) | +30 (14 thk, 7 wrk, 9 con), 30/30 pass; David/UNIDROIT fix, name spelling normalized, Macaulay filler removed. **legal-theory measured: 566** (target 700) | d69957af5 |
| 2026-09-26 | worker: legal-theory J (criminal-law philosophy, international-law theory) | +35 (16 thk, 8 wrk, 11 con), 35/35 pass; 1 factual fix (Christie) after reads | d2c75df41 |
| 2026-09-26 | worker: legal-theory I (classical fiqh procedure, non-Western traditions) | +35 (16 thk, 8 wrk, 11 con), 35/35 pass after source fixes in 19 files. **legal-theory measured: 636** (target 700) | 5911f2d98 |
| 2026-09-26 | worker: legal-theory K (usul, fiqh of transactions, Arab public law) | +32 (14 thk, 7 wrk, 11 con), 32/32 pass; 1 source replaced after reads | 49492542e |
| 2026-09-26 | worker: legal-theory L (European private law, constitutional theory) | +32 (14 thk, 7 wrk, 11 con), 32/32 pass; 4 factual fixes after reads. **legal-theory measured: 700 — Phase 1 legal-theory target reached.** Next: political-economy batch 0 | a27462df6 |
| 2026-09-26 | worker: Phase 0 hygiene | stripped stray trailing `</content>` artifact from 70 AR files | e561dfc64 |
| 2026-09-26 | worker: political-economy batch 0 | part added to audit vocabulary, economic_school/policy_orientation fields, DR-019 (DR-015 was taken), overlap inventory at agents_specs/political-economy-overlap-inventory.md; audit crash on missing type fixed | fc34d6d60 |
| 2026-09-26 | worker: political-economy 1 (classical & Marxist) | +35 (8 sch, 12 thk, 7 wrk, 8 con), 35/35 pass; Lenin source error fixed in 2 files, 99 inline slugs replaced | be050486b |
| 2026-09-26 | worker: political-economy 2 (Arab/Islamic, scholastic, mercantilist, physiocratic) | +34 (6 sch, 12 thk, 7 wrk, 9 con), 34/34 pass. **political-economy measured: 69** (target 1,100–1,300) | f9b1d08ca |
| 2026-09-26 | worker: **Phase 0 blocker (logged, not fixed)** | audit_atlas.py exits 1 on pre-existing atlas-wide failures (66 proc-/org- nodes with no type/title, 665 with no crumb, 307 dangling edges, 995 isolated nodes, 34 wiki links, etc.; none in files created 2026-09-26). The political-economy mission requires exit=0, so the interim gate is the integrity checker plus no new audit findings (verified: the 69 new nodes add none). Also found: `thk-karl-polanyi` (part `economic-anthropology`) and `con-justice-rawls` (part `ethics`) are outside the audit vocabulary (181 ethics nodes); duplicate `con-surplus-value` / `con-surplus-value-marx`; no live thinker node for Ibn Khaldun | – |
| 2026-09-26 | worker: political-economy 4 (Keynesian, monetarist, new classical) | +35 (5 sch, 14 thk, 7 wrk, 8 con, 1 dbt), 35/35 pass | 34d86c7c1 |
| 2026-09-26 | worker: political-economy 3 (marginalist & neoclassical) | +35 (5 sch, 14 thk, 7 wrk, 9 con), 35/35 pass; audit diff found 12 new findings in batch 4 (related type/title mismatches, 1 duplicate title), fixed in 660a81c5e; audit back to baseline. **political-economy measured: 139** | f060efbc9 |
| 2026-09-26 | worker: political-economy 6 (institutional, evolutionary, historical) | +35 (5 sch, 14 thk, 7 wrk, 8 con, 1 dbt), 35/35 pass | cfbcf5778 |
| 2026-09-26 | worker: political-economy 5 (Austrian, neoliberal, public choice, ordoliberal) | +35 (5 sch, 14 thk, 7 wrk, 8 con, 1 dbt), 35/35 pass; audit diff found 1 duplicate title (German historical school vs historiography), fixed in db84c36ff. **political-economy measured: 209** | 946166b67 |
| 2026-09-26 | worker: political-economy 8 (20 events, 15 methods/tools) | +35 (20 evt, 15 ins), 35/35 pass; 1 chronology fix (infitah) | 851df155b |
| 2026-09-26 | worker: political-economy 7 (development, inequality, feminist, ecological) | +35 (5 sch, 14 thk, 7 wrk, 8 con, 1 dbt), 35/35 pass; 2 factual fixes (Waring). Audit diff found 21 new orphans, linked from their schools in 3c0400b63. **political-economy measured: 279** | f5bb2c021 |
| 2026-09-26 | worker: political-economy 9 (20 debates, 15 studies) | +35, 35/35 pass; gender agreement fix, al-Azhar 2002 / Jeddah 1985 positions added to the Islamic banking debate | d2af59403 |
| 2026-09-26 | worker: political-economy 10 (Arab political economy) | +35 (3 sch, 18 thk, 6 wrk, 8 con), 35/35 pass; Beblawi offices made precise. Audit diff: 16 related-title mismatches and 13 orphans fixed in a01183f61. **political-economy measured: 349** | 6952c8bbf |
| 2026-09-26 | worker: political-economy 12 (15 events, 10 studies, 10 methods) | +35, 35/35 pass | 2c73561e5 |
| 2026-09-26 | worker: political-economy 11 (20 currents, 15 critiques) | +35 (20 br, 15 crt), 35/35 pass; 59 orphans from batches 11-12 linked in 0a573d4f2. **political-economy measured: 419** | 61da6d5a6 |
| 2026-09-26 | worker: political-economy 14 (35 post-1945 thinkers) | +35, 35/35 pass | 47dfb45a0 |
| 2026-09-26 | worker: political-economy 13 (35 pre-1950 thinkers) | +35, 35/35 pass; 2 small fixes; 35 orphans linked and 5 related titles fixed in 428d2e301. **political-economy measured: 489** | 97955548d |
| 2026-09-26 | worker: political-economy 16 (35 core concepts) | +35, 35/35 pass | 395b4ecd1 |
| 2026-09-26 | worker: political-economy 15 (20 schools, 13 works, 2 thinkers) | +35, 35/35 pass after 3 fixes (dangling link, title translation, reversed lineage edge); 27 orphans linked in e27a50f42. **political-economy measured: 559** | 0eb699522 |
| 2026-09-26 | worker: political-economy 18 (35 concepts) | +35, 35/35 pass after 3 added sources | b3e6621dc |
| 2026-09-26 | worker: political-economy 17 (35 classic works) | +35, 35/35 pass; 5 works re-parented (cross-part belongs_to); 28 orphans linked in 7acd6e522. **political-economy measured: 629** | 9d4892e06 |
| 2026-09-26 | worker: political-economy 19 (35 debates) | +35, 35/35 pass; Wages for Housework authorship fixed, 1 doubtful citation dropped | 377c4623c |
| 2026-09-26 | worker: political-economy 20 (20 schools, 15 thinkers) | +35, 35/35 pass; 1 re-parent, 1 softened date, 6 lineage edges fixed; orphans linked in 752c40a14. **political-economy measured: 699** | 88dcbdd38 |
| 2026-09-26 | worker: political-economy 21 (35 thinkers) | +35, 35/35 pass | 4702def3a |
| 2026-09-26 | worker: political-economy 22 (20 currents, 15 critiques) | +35, 35/35 pass; 1 attribution fix; 50 orphans linked in e5c07008c. **political-economy measured: 769** | d83779e64 |
| 2026-09-26 | worker: political-economy 23 (35 concepts) | +35, 35/35 pass | 03cb2bf77 |
| 2026-09-26 | worker: political-economy 24 (25 studies, 10 events) | +35, 35/35 pass; Lebanon sources fixed; 46 orphans, 5 titles, 4 edge types fixed in 3087e71c6. **political-economy measured: 839** | 99f7eb324 |
| 2026-09-26 | worker: political-economy 25 (35 thinkers) | +35, 35/35 pass; fixes: Khurshid Ahmad death year, Berg Report year, Marini re-parented | d64236d4c |
| 2026-09-26 | worker: political-economy 26 (25 schools, 10 methods) | +35, 35/35 pass. Cleanup in 12436b1c3: stray </content> stripped from 106 committed files, 15 reversed lineage edges fixed, 46 orphans linked. **political-economy measured: 909** | 14dd58eed |
| 2026-09-26 | worker: political-economy 27 (35 concepts) | +35, 35/35 pass; original-sin coinage dated to 1999 | 5b53eab34 |
| 2026-09-26 | worker: political-economy 28 (27 works, 8 debates) | +35, 35/35 after re-parenting Marini and Sweezy to a political-economy school; 40 orphans linked in f3262037f; audit diff vs baseline clean. **political-economy measured: 979** | 0070dc02d |
| 2026-09-26 | worker: political-economy 29 (thinkers) | +19: 21 of 41 candidates already existed; al-Najjar dropped as duplicate of thk-ahmad-al-naggar; truncated source lists repaired in Richards, Waterbury, Collier; dated source added to al-Masri | 5cfbaaf51 |
| 2026-09-26 | worker: political-economy 30 (25 concepts, 5 critiques, 5 branches) | +35, 35/35 pass; unverifiable Egypt bread-subsidy source replaced; 38 orphans linked in 014ef4b38; audit diff vs baseline clean. **political-economy measured: 1033** | aea27ddf8 |
| 2026-09-26 | worker: political-economy 31 (25 thinkers, 8 schools) | +33; agent dropped by API error after writing; 2 duplicate schools deleted (neoclassical synthesis, social structures of accumulation); 26 short files extended to ≥680 words | 74b7a5b1e |
| 2026-09-26 | worker: political-economy 32 (15 debates, 20 works) | +35 (agent dropped by API error after writing; files verified); 55 orphans + 12 titles fixed in 54832210b; audit diff vs baseline clean. **political-economy measured: 1101 — lower target reached; next: bridge batch (psychology, sociology, philosophy, anthropology), then Phase 1 linguistics** | d1894b5ee |
| 2026-09-26 | worker: adopt orphaned batch (uncommitted work from an earlier run) | +173 new (134 linguistics, 20 bridge, 19 anthropology) and 12 ethics expansions; 3 dangling links removed, 33 short files expanded, 2 factual fixes | 1586cb986 |
| 2026-09-26 | worker 8-agent round (user asked for 8 agents this round only): ethics depth 0, 2, 3 | 120 ethics stubs written (96 con >=350 w, 24 sch/wrk >=650 w); 12 undated sources fixed; 1 name fix | 91405a746 |
| 2026-09-26 | worker 8-agent round: anthropology | +15 (5 backlog slugs skipped as duplicates); Barth/Delaney fixes. **anthropology measured: 1201 — Phase 1 target reached** | 75b15c5b7, 7b4771bbe |
| 2026-09-26 | worker 8-agent round: linguistics (3 batches) | +27 (12 thk, 15 wrk; 5 dups skipped), +31 modern thinkers + thk-george-a-miller expanded (agent had overwritten it; id restored), +32 classical Arabic lexicographers/grammarians/works; fixes: Kutas P600, al-Hajj Salih dates, Borer, Liberman and Tha'alibi sources. **linguistics measured: 1194** (target 1200, 6 to go) | 249316d64, 5695efd15, 958bbe274 |
| 2026-09-26 | worker 8-agent round: ethics depth 1 | 40 stubs written; 10 undated editions fixed; Sandel/Gilligan/Saladin fixes. **ethics under 300 w: 166 → 6**. data.json rebuilt (14,373 items) | 8b8dae921 |
| 2026-09-26 | worker: linguistics +6 Arabists | Fleisch, Nöldeke, Brockelmann, Bergsträsser, Fischer, Baalbaki; 1 title fix. **linguistics measured: 1200 — all Phase 1 targets reached** | b9a6a1bab |
| 2026-09-26 | worker: legal-theory/ethics depth A–D | 154 stubs written to >=350 w (incl. 20 con-legal-rights-NN); fixes after reads: Schmitt quote, torture jus cogens (Furundžija/Al-Adsani), fabricated slavery source replaced, Byrne, Reichstag decree; inline slugs stripped. **legal-theory+ethics under 300 w: 302 → 148**. data.json rebuilt | 09f4701f0, fa8910295, 76fd26843, f0bcd8be3 |
| 2026-09-26 | worker 12-agent round (user asked for 10–15 agents): legal-theory L0–L3, historiography H0–H7 | legal-theory/ethics: all 148 remaining short nodes written (schools/thinkers/works >=650 w). **legal-theory+ethics under 300 w: 148 → 0 (legal-theory and ethics fully expanded)**. historiography: 320 template stubs (~40 w of filler each) rewritten (272 schools >=650 w, 48 concepts >=350 w). Fixes: 5 drifted ids restored (H2), inline slugs stripped, 2 dangling edges, 1 duplicated paragraph, attribution fixes (al-A'zami/Schacht, Ibn Battuta doubts). Note: 20-concurrent-subagent cap hit because agents fan out; later agents told not to spawn sub-agents. data.json rebuilt | c13a8c4d9, 22056f1e1, 97b65c0ab, 0e0ba6620, 14f6906d4, 4671eda1b, 915b2114a, 122929796, 0da9fae88, 640f92c05, e062b19cf |
| 2026-09-26 | worker 12-agent round (no sub-agent fan-out): historiography HB0–HB11 | 339 of 347 short historiography thinkers/schools/works rewritten to ~650 w (2 files at 587–600 w). HB0/HB6/HB7 agents were cut off by the API session limit: 79 finished files committed, 4 incomplete files reverted. Held back as a phantom entity: thk-abdulhamid-lahiji (no identifiable historian). Fixes after reads: Tabari (SUNY translation dates, edition size), Ibn Abd al-Hakam's madhhab (Maliki), Le Goff article title, Sherira's Iggeret language (Hebrew/Aramaic, not Judeo-Arabic), Manetho (Abydos, Eusebius' Chronicon), Timkat/Genna, a fabricated Ibn al-Athir title, dubious references pruned, inline slugs stripped. **historiography under 300 w: 347 → 9; all parts: 6523**. data.json rebuilt | ec158320c, 8d98e4842, 7b16e67ff, 96df99877, ca23c1a46, 74e280534, 7cbaa6ab4, 469c7aeda |
| 2026-09-27 | worker 15-agent round: linguistics LB0–LB14 (+7 leftover historiography works) | 591 nodes expanded and committed (thinkers/schools/works ≥650 w, others ≥350 w). Quality problems found: LB3 agents padded word counts by pasting paraphrased copies of existing sections (a near-duplicate detector was added; duplicates removed and replaced with new content; all running agents told to stop); many agents said they wrote 3 sources when files had 1 (about 25 source lists completed with real references). Held back as unverifiable or phantom people: thk-kevin-stratos, thk-cynthia-blanton, thk-karen-seymour, thk-kirk-hautvast, thk-cameron-moore, thk-erica-cochrane. Fact fixes: Lichtheim (German, not Swiss), Ahmad Mukhtar Umar (unverified dictionary claim removed), Ibrahim Anis's peers, Zunburiyya question, al-Messaddi birth (1945, Sfax), Mary Catherine O'Connor (Accountable Talk), Apollonius Dyscolus (Greek), Sima Qian dates, Kouloughli works. **Short nodes, all parts: 6523 → 5929; linguistics 780 → 186**. data.json rebuilt | 9474ab00f … 6fe13953f (16 commits) |
| 2026-09-27 | worker 15-agent round RB0–RB14: linguistics tail + sociology | ~515 nodes expanded and committed. My census had wrongly included 75 content/ar/_merged/ archive files (which caused the earlier 'ethics 46 / legal 29' count): all 75 edits reverted and census fixed to exclude _merged/drafts — **ethics and legal-theory are at 0 short**. New gate script (words, ≥2 source bullets, dated years, unique headings, no backticks) plus auto near-dup removal on every batch; about 15 files sent back or fixed for duplicates, short length or thin sources. Held back: wrk-so-what-tagliamonte (unverifiable title), wrk-travels-marco-polo (too short). **Short nodes (excl. _merged): 5291; linguistics 8, historiography 2, sociology 1041 → 713**. data.json rebuilt | f0aebfa67 … 42727161a |
| 2026-09-27 | worker 15-agent round SB0–SB14: sociology | About 550 sociology nodes expanded and committed. Agents running the orchestrator's neardup.py themselves cut down fix-ups (SB3/SB8/SB14 passed on the first try). Six batches (SB2/4/5/6/9/10) were cut off by the **weekly API limit (resets Oct 1, 09:00 Cairo)**: 191 finished files committed, 32 incomplete ones reverted. Fix: Shariati (a nonexistent work 'النباتات' replaced by العودة إلى الذات; Sorbonne/Gurvitch wording). **Short nodes (excl. _merged): 5291 → 4740; sociology 713 → 164**. Per the user: cron changed to every 15 min with 1 Sonnet agent. data.json rebuilt | 91558f5af … ec326f111 |
| 2026-09-27 | worker single-agent batches UB0–UB3 + TB0 (user: one agent at a time) | 164 sociology nodes → all ≥650 w (TB0's 30 under-length works reverted, then redone in UB1–UB3). Found the cron was blocked because this chat is itself a still-running cron session. Fix: Sharabi Arabic title. **sociology short: 164 → 0 (sociology fully expanded)**. data.json rebuilt | ce3a70d28, 63ca62245, 5777b610f, 88bf73ef8, c26a440c1 |
| 2026-09-27 | worker 4-agent round WB0–WB3 + single-agent VB0–VB2 (religious-studies) | 160 + 119 religious-studies nodes expanded; all 4 WB batches passed the gate first time (agents self-ran neardup/bodywc). Fixed an agent counting frontmatter as body words (VB1, 16 files redone). **religious-studies short: 707 → 428; all parts: 4297**. Cron set to 15 min / 4 agents per the user. data.json rebuilt | a4d44c1bc … e80e92e14 |
| 2026-09-28 | worker 4-agent rounds XB0–XB3, YB0–YB3 (religious-studies) | 310 nodes expanded; 9 unverifiable or vague nodes held back and added to the cron skip list (lipton, malini-sen, tillotson, jane-dancy, ryberg, alonso-rodrigues, david-jones-architecture, god-and-politics, simon-johnson, bachmat). Fixes: dangling edges in Reggie Williams, al-Siba'i's al-Sunna (1949 Azhar thesis). Cron SKILL amended with standing settings (4 agents until the user says to go back to 1). **religious-studies short: 428 → 118; all parts: 3987**. data.json rebuilt | bfdddcaf8 … 2896a8512 |
| 2026-09-28 | worker 4-agent round ZB0–ZB3 (religious-studies tail + anthropology start) | 157 nodes expanded; 3 more vague or unverifiable stubs held back (visual-religion, religious-modernities, sacred-images). Catalogue IDs stripped from 3 works. data.json rebuilt | 0c8b3f041 … 1625176e2 |
| 2026-09-28 | worker 4-agent round AB0–AB3 (anthropology) | 159 anthropology nodes expanded; 6 thin source lists completed; 1 unverifiable study held back (stu-abdulrahman-bedouin). data.json rebuilt | 48f5dd5b1 … 5c9a88bf2 |
| 2026-09-28 | worker 4-agent round BB0–BB3 (anthropology) | 148 nodes expanded; 13 unverifiable or title-mismatched nodes held back and added to the skip list; Turner's Forest of Symbols title corrected (Ndembu, not Lele). data.json rebuilt | e7732884b … 193b7a7da |
| 2026-09-28 | worker 4-agent round CB0–CB3 (anthropology thinkers) | 139 thinkers expanded; 19 unverifiable or conflated names held back (skip list updated); Maurice 'Block' → Bloch title fixed; thin source lists completed. **anthropology short: 387 → 248 (213 workable); all parts: 3387**. data.json rebuilt | c9374108a … bf1b16a49 |
| 2026-09-28 | worker 4-agent round DB0–DB3 (anthropology) | 128 nodes expanded; 32 unverifiable, placeholder, discipline-mismatched or title-mismatched stubs held back (skip list now ~90 slugs); thin source lists completed. data.json rebuilt | 937088f3c … 88e67c32a |
