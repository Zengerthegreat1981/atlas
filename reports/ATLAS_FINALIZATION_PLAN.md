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
0b. **Automation:** the scheduled task `atlas-worker` runs every 30 min. It uses `reports/.atlas_worker.lock` (heartbeat) and spawns 2 Sonnet subagents per run.
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
