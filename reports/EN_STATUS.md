# EN execution status — 2026-11-15 (pass 1 of ASTRA_FULL_AUDIT_EN_2026-11-15.md)

Measured on the working tree used for this pass (936 EN files; differs from the audit snapshot's 944).

## Done
- **P0-02 parser:** new `scripts/atlas_frontmatter.py` (quoted / unquoted / multi-line / short-related, bare `null`,
  stray list items after `related: []`, `sources`). `build_atlas.py` uses it, resolves missing related titles from the
  target node, reports every unreadable line and fails under `--strict`. AR build node set unchanged (14,364);
  differences are recovered fields/links only. 41 genuinely malformed AR files are reported, not touched.
- **P0-03 locale:** EN build now emits `lang="en" dir="ltr"`, EN title/description, English top-bar/menu/footer,
  module-driven English home ("Browse by discipline", counts from data), `#module:<part>` pages and an explicit
  "Page not found" route (no silent fallback to a school). Checked in a browser pane over HTTP: home, module page, 404.
  Not done: full in-article UI strings, `data_extras-en.json`, schools drawer, mobile/keyboard/perf testing.
- **P0-04 gate:** `scripts/check_en_release.py` (+ `--strict`) writes `reports/en-release-check.json` and
  `reports/en-scope-registry.csv` (module, status, flags per file) and compares source vs `data-en.json`/`index-en.html`.
- **Outputs rebuilt:** `data-en.json`, `index-en.html` now contain all 936 nodes (were 130).
- **P2.5 partial:** 46 `[EN TRANSLATION NEEDED]` files translated from their own Arabic reference text (no added facts).
  Machine-assisted translation: **needs human review**. 3 files remain stubs (Arabic source was only bracket stubs):
  `con-division-labor`, `thk-abdalla-salem`, `wrk-womans-evolution`/`thk-akira-fujii` (see registry, status `placeholder`).
- **§6.1.2 related:** 152 unresolved EN `related` items — 21 repointed to a unique match, 131 removed;
  every decision in `reports/en-related-decisions.csv` (restorable).
- **P0-01 docs:** `TRANSLATION_RULE.md` and `content/en/README.md` rewritten (English-first; 65,529-term claim marked unverified).

## Remaining blockers (per `check_en_release.py --strict`)
- 221 files with `pending` markers (mostly sociology) — editorial work.
- 3–4 stub files above; 26 short bodies; 147 files with no module (unclassified) and 454 without explicit `part`.
- Edge targets given by name rather than slug (549) — canonical-slug pass (P5.2).
- Modules with zero EN content: linguistics, political economy, religious studies, legal theory, ethics, psychiatry, Arab thought.
- Duplicate-ID groups: 0 in this tree. 65,529-term reconciliation, source verification, licensing, a11y/mobile/perf: not done.


---
# Pass 2 (2026-11-15) — sociology pending, labels, UI strings

## Done
- **Sociology "pending":** 216 files reviewed against their bodies; stale templated gaps deleted where the body
  covers the topic, the rest reworded to "X: not yet covered" (disclosed gaps, no word "pending"). Reviewers made
  per-file judgments by reading; numbered-school and thinker filler was *not* read in full by them.
- **Nameless filler:** 30 numbered "Sociological School 11–40" entries moved to `content/en/drafts/schools/`
  (excluded from build, see its README). 52 filler sociology thinker entries rewritten with real, conservative
  bios (350–550 words, real works only). **Machine-written: needs human fact-check**; reviewers flagged doubtful items
  (Abdel-Malek dates, Al-Wardi, Ibn Khaldun details, Collins posts). Coser's `dates` corrected to 1913-2003.
- **Modules:** `part:` written into 454 files that lacked it (crumb-derived + 29 manual decisions, logged in
  `reports/en-part-assignments.csv`). 147 "unclassified" → 0. `reports/en-scope-matrix.md` generated.
- **Arabic removed from EN display fields:** titles, crumbs, dates, related titles, edge targets (190+ files).
  Types/levels stay Arabic in source (shared internal keys) and are shown in English via the build map.
- **UI:** 741 Arabic UI fragments translated into `scripts/template/ui_strings_en.json` and applied at EN build
  (machine translation, needs a native read). EN home now points at the module home. Verified in a browser pane:
  home, module pages, node pages, type index, timeline, drawers, search, 404 — 0 Arabic characters, no JS errors;
  mobile (375px) no horizontal overflow after the skip-link fix; search returns results; local load ~0.4 s.

## Still open
- 120 files carry disclosed "not yet covered" gaps (strict gate still counts them); 3 stubs with no source text
  (`con-division-labor`, `thk-abdalla-salem`, `thk-akira-fujii`, plus `wrk-womans-evolution`, `thk-ming-ming-kuo`,
  `thk-sergio-carrasco` are minimal) need author input; 26 short bodies.
- Modules with no EN content: linguistics, political economy, religious studies, legal theory, ethics, psychiatry,
  Arab thought, bridges — each needs a closed scope list first (see scope matrix).
- Source verification of all claims, licensing, screen-reader and full keyboard audit, performance on release data.
- Edge targets are still names (e.g. "Anthropology", 313 edges), not canonical slugs; module root nodes don't exist yet.
- `data_extras-en.json` not created (Arabic view data is unused by the EN pages I exercised).

---
# Pass 3 (2026-11-15/16) — Psychology and Philosophy v1

Scope: `reports/scope/psychology-scope.md`, `reports/scope/philosophy-scope.md` (closed v1 lists; anything else is backlog).

## Psychology (309 EN entries)
- 204 entries translated from AR assets with the same ids/slugs, 11 authored (module root `fld-psychology`, methods,
  intelligence, memory systems, learning theories, replication crisis, ...), 29 thin stubs expanded, 4 overlapping
  concept pairs retitled/cross-linked.
- All 309 passed a fact-check/clean-up pass; ~250 corrections are logged in `reports/scope/corrections.txt`
  (the Arabic drafts contained many errors: wrong codes, invented people/studies, misattributions).
## Philosophy (325 EN entries)
- 239 translated from AR assets (same ids/slugs), 10 branch introductions authored (`fld-philosophy` root + 9 fields),
  6 empty-source thinker stubs (Socrates, Aristotle, Buddha, Confucius, Zhuangzi, Naess) written properly,
  then every entry fact-checked; garbled/invented names in the Arabic drafts were removed or corrected.
- Reading paths added to both module roots; module pages link to them.

## Caveats (important)
- All content is machine-assisted and checked from model knowledge without web access. `review-candidate` is NOT
  "reviewed": a human subject-matter pass is still needed, especially for clinical entries (disorders, instruments,
  techniques; DSM-5-TR/ICD-11 codes) and for bibliographic details (editions, translators, Arabic translations).
- ~310 files carry disclosed "not yet covered" gaps (informational). `thk-habermas`: unverifiable death claim removed.
- Related links to targets outside the closed scope were removed (see `reports/en-related-decisions.csv` for the last run).
- Scope matrix numbers: psychology 309, philosophy 325 vs AR inventories of 3,522 / 2,846 (inventory, not target).

---
# Pass 4 — Sociology v1 (2026-11-16)
- Scope list `reports/scope/sociology-scope.md` (152 entries: 148 selected from AR assets by inbound links + 4 field intros).
- 445 sociology entries now in EN: 148 translated (same ids/slugs), 4 authored (`fld-sociology` root, theory, methods, stratification),
  293 pre-existing; **all 445 fact-checked** (corrections appended to `reports/scope/corrections.txt`).
- Many Arabic drafts were templated and contained invented names, studies and statistics; these were removed or corrected.
  Entries whose titles could not be matched to a real work were retitled or reduced (see `reports/scope/sociology-duplicates.md`,
  which also lists possible duplicate entities for a merge/redirect decision).
- Reading paths added to `fld-sociology`; module page links to it.
- Same caveat as before: machine-assisted, no web access; human review required.

---
# Pass 5 — Linguistics v1 (2026-11-16), built with Haiku + Sonnet
- Scope `reports/scope/linguistics-scope.md`. 153 entries translated from AR assets by **Haiku** (same ids/slugs), 5 field intros authored by Sonnet
  (`fld-linguistics` root, phonetics-phonology, syntax-semantics, sociolinguistics, Arabic linguistics); all 158 fact-checked by **Sonnet**.
- Model pilot: Haiku was audited on 8 entries against their Arabic sources by Sonnet — about 0.5 substantive issues per entry (no fabricated sources,
  no omitted sections). Haiku is used for translation only; Sonnet remains the fact-check gate. The fact-check still found many errors
  (mostly inherited from the Arabic drafts: invented examples, corrupted names, misattributed claims). See `reports/scope/corrections.txt`.
- Reading paths added to `fld-linguistics`. Same caveat: machine-assisted, no web access; human review required.

---
# Pass 6 — Political economy v1 (2026-11-17), Haiku translation + Sonnet fact-check
- Scope `reports/scope/political-economy-scope.md`: 157 entries translated by Haiku from AR assets (same ids/slugs), 4 field intros authored by Sonnet
  (`fld-political-economy` root, macro/money, development, labour/distribution); all 161 fact-checked by Sonnet (corrections in `reports/scope/corrections.txt`).
- Reading paths added to `fld-political-economy`. Same caveat: machine-assisted, no web access; human review required.

---
# Pass 7 — Religious studies v1 (2026-11-17), Haiku translation + Sonnet fact-check
- Scope `reports/scope/religious-studies-scope.md`: 145 entries translated by Haiku from AR assets (same ids/slugs), 4 field intros authored by Sonnet
  (`fld-religious-studies` root, theory & method, ritual/myth/symbol, religion & society); all 149 fact-checked by Sonnet.
- Reading paths added to `fld-religious-studies` (grouped by type). Same caveat: machine-assisted, no web access; human review required —
  particularly for entries touching living religious traditions and Islamic studies.

---
# Pass 8 — Legal theory v1 (2026-11-18), Haiku translation + Sonnet fact-check
- Scope `reports/scope/legal-theory-scope.md`: 122 entries translated by Haiku from AR assets, 4 field intros by Sonnet (`fld-legal-theory` root,
  rights & justice, legal reasoning, comparative & Islamic legal thought); all 126 fact-checked by Sonnet. Entries are legal *theory*, not legal advice.
- Reading paths auto-generated (`scripts/scope/auto_paths.py`, grouped by type). Same caveat: machine-assisted; human (legal-expert) review required.

---
# Pass 9 — Ethics v1 (2026-11-19), Haiku translation + Sonnet fact-check
- Scope `reports/scope/ethics-scope.md`: 123 entries translated by Haiku from AR assets (schools, concepts, works — the Arabic ethics tree has no thinker files; ethicists live in the Philosophy module),
  4 field intros by Sonnet (`fld-ethics` root, normative, metaethics/moral psychology, applied); all 127 fact-checked by Sonnet. Note `fld-ethics-overview` (Philosophy module) remains.
- Reading paths auto-generated. Same caveat: machine-assisted; human review required.

---
# Pass 10 — Psychiatry v1 (2026-11-20), Haiku translation + Sonnet fact-check
- Scope `reports/scope/psychiatry-scope.md`: 119 entries translated by Haiku from AR assets, 3 field intros by Sonnet (`fld-psychiatry` root,
  classification & diagnosis, biological/social models); all 122 fact-checked by Sonnet with extra clinical-content rules (descriptive only, cautions added).
- **Clinical review is mandatory before publication**: diagnostic criteria, trial results and prevalence figures were checked from model knowledge only.
- Reading paths auto-generated.
