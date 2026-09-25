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
1. Only one writer on `content/ar` at a time. All the other Atlas chats must be closed (see MISSIONS_INDEX, the concurrency rule).
2. Sonnet agents get **bounded, checkable batches**: an explicit slug list, an explicit target, and ≤40 files. Opus (this chat) verifies every batch before commit: word counts, integrity checker, and 3 random full reads per batch.
3. Batches never share slugs. Each agent writes only the files on its list.
4. No invented references. Every Sources section needs at least 2 references with title and year. Arabic tradition comes first.
5. Commit after each verified batch, with a message that gives real counts.

## 2. Phases

### Phase 0: hygiene (Opus, 1 session)
- Archive the 10 old Atlas chats.
- Run `check_content_integrity.py` and fix AR errors to 0.
- Resolve the 751 EN orphans: move them to `content/en/_orphans/` and extract their Arabic-worthy content later.
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
