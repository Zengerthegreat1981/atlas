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
