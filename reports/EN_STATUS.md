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
