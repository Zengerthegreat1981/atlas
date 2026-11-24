# ATLAS — handout for continuing the English edition on another PC
Written 2026-11-24. Repo: https://github.com/Zengerthegreat1981/atlas (branch `main`, last commit at time of writing: `6e3ba1d`).

## 1. What the project is
The Atlas is a Markdown knowledge base: `content/<lang>/<folder>/<slug>.md`, each file with frontmatter (id, type, part, level, title, en, crumb, edges, related, gaps…).
Arabic is the source (~13,000 assets). The English edition (`content/en`) is being built module by module, then the Arabic edition will be translated/finished (Phase 7).
The plan is in `ASTRA_FULL_AUDIT_EN_2026-11-15.md` (kept on the original PC under `D:\Ai projects\Atlas\`; not necessarily in the repo).

## 2. Current state (2026-11-24)
English v1 drafts exist for 12 modules; the 13th (historiography) is in progress. All pages are **machine-assisted drafts: not verified against sources, not reviewed by a specialist. Do not call them publication-ready.**

| Module | EN pages | | Module | EN pages |
|---|--:|---|---|--:|
| psychology | 309 | | political-economy | 161 |
| philosophy | 325 | | religious-studies | 149 |
| sociology | 445 | | legal-theory | 126 |
| anthropology | ~450 | | ethics | 127 |
| linguistics | 158 | | psychiatry | 122 |
| historiography | 200 (in progress) | | arab-thought | 114 |
| | | | bridges | 108 |

`reports/en-scope-matrix.md` has the live matrix; `reports/EN_STATUS.md` has a section per pass (Pass 14 = historiography, with resume steps).
Release check: `python scripts/check_en_release.py --strict` → CLEAN (0 blockers) at the last run, 2,793 pages.

## 3. What to do next (in order)
1. **Finish historiography** (batches 0–4 of 6 translated by Haiku, committed, UNVERIFIED):
   - batch 5: list `scripts/scope/prompts/lists/hit5.txt` (22 entries) with the translation prompt `trans_prompt_hi.txt`;
   - author 3 field intros (spec `lists/hitnew.txt`): `fld-historiography` (root), `fld-historical-method-sources`, `fld-schools-historical-thought`; ids like `HIS-30001`, `part: "historiography"`, type `مجال`;
   - fact-check all historiography files (registry `reports/en-scope-registry.csv`, module == historiography) in batches of ~30 with `verify_prompt_hi.txt`;
   - `python scripts/scope/auto_paths.py historiography fld-historiography`, `python scripts/scope/write_reading_path.py historiography`, `python scripts/build_en_scope_matrix.py`, `python scripts/scope/render_scope.py historiography "Historiography"`;
   - append a section to `reports/EN_STATUS.md`, copy the corrections log to `reports/scope/corrections.txt`, commit, push.
2. **Make psychology + philosophy publishable** (what is missing): specialist review; fill or accept "not yet covered" gaps (~141 psychology, ~53 philosophy); merge duplicates and fix slug/title mismatches (e.g. `thk-malinowski` vs `thk-bronislaw-malinowski`, `wrk-anthropology-now` is actually "Tell My Horse"); relink the network (see §6); create `data_extras-en.json`; source-verification log; licensing/rights; accessibility/mobile/performance checks.
3. Remaining plan items from the audit: canonical edge slugs (~2,300 edge targets are English names), release freeze, then the Arabic translation.
4. Fallback if no reviewer is available: publish with an "unreviewed machine-assisted draft" label.

## 3b. Open content flags (humans should verify)
- Many entries were rewritten by the fact-check; every substantive correction is logged in `reports/scope/corrections.txt`.
- Items flagged "unverified, left as in source" in that log (e.g. biographical details, some publication data) need a specialist.
- Five anthropology stubs were moved out of the build to `content/en/drafts/` (con-division-labor, thk-abdalla-salem, thk-akira-fujii, thk-ming-ming-kuo, thk-sergio-carrasco): unidentifiable/unusable sources.

## 4. How the pipeline works (per module)
1. `python scripts/select_scope.py <part>` → `reports/scope/<part>-candidates.csv` (Arabic assets ranked by inbound links/length).
2. `bash scripts/scope/prep_module.sh <part> "<Label>" <prefix> '<quota-json>' '<new-fields-json>'` → writes `scripts/scope/<part>_scope.py`, `reports/scope/<part>-translate.json`, batch lists (`<prefix>t0..N.txt`), field spec (`<prefix>tnew.txt`) and prompts. **It writes into a hard-coded scratchpad path (`SP=` at the top of the script): change it to a folder on your PC.**
3. **Haiku** translates each batch (~20 entries) following `trans_prompt_<prefix>.txt` (faithful translation, ids/slugs kept, English edge targets, `active_end: "مستمر"` kept for living scholars/ongoing schools, BCE years negative, stubs → `stubs.txt`).
4. **Sonnet** authors the field intros, then fact-checks every file in batches of ~25–30 (`verify_prompt_<prefix>.txt`). The Arabic drafts contain many invented names, quotations, studies and statistics; the fact-check removes/rewrites them and logs corrections.
5. Fixers + build + gate:
   ```
   python scripts/fix_en_labels.py
   python scripts/fix_en_edge_targets.py
   python scripts/fix_en_related.py
   python scripts/build_atlas.py en --strict
   python scripts/check_en_release.py --strict
   ```
   (set `PYTHONUTF8=1` on Windows.)
6. Reading paths, scope matrix, scope doc, status section, commit + push after each module. Stage only the files you changed (the working tree of the original PC also had ~1,100 unrelated uncommitted changes; do not blanket `git add -A`).

## 5. Rules the owner set
- **Never run more than 1 subagent at a time.** (Earlier, 20 in parallel caused rate-limit failures.) Resume a failed agent with SendMessage.
- Work autonomously; commit and push to the atlas repo after each module.
- Haiku for bulk translation (cheaper/faster), Sonnet for field intros and the fact-check gate.
- "Not yet covered" gap lines are informational; the word **"pending" is a blocker** in the checker (it must not appear in any page).
- Keep ids/slugs from the Arabic assets; do not touch the Arabic tree.
- Push only via the HTTPS URL `https://github.com/Zengerthegreat1981/atlas.git` (SSH remote is not usable from the original PC).

## 6. Why ~3,000 `related` links were removed (and how to restore)
Only ~2,800 of ~13,000 Arabic entries exist in English. `scripts/fix_en_related.py` repoints an unresolved `related` id when there is one unique fuzzy candidate, otherwise it removes the item so the English site has no broken links. Arabic files are untouched. The log is `reports/en-related-decisions.csv` (it is overwritten at each run, so only the latest run is kept; change it to append before the next big run). Relinking = re-adding items whose targets now exist in English.

## 7. Tools on the original PC (set these up again on the new PC)
- Python 3, Git, Node.js (LTS) + Claude Code signed in.
- Optional extra models: Gemini CLI (`npm install -g @google/gemini-cli`, then sign in or set `GEMINI_API_KEY`) and Antigravity `agy` (`agy -p "<prompt>"` works headless, but file-writing runs need permission rules for shell commands in its `settings.json`, or `--dangerously-skip-permissions --sandbox`; a pilot on historiography batch 5 wrote no files for that reason). Anything written by another model must pass the same fact-check + release gate.
- Prompts and batch lists: `scripts/scope/prompts/` (see its README); wait helpers: `scripts/scope/waitlist.py` (adjust its `SP` path).

## 8. Known pitfalls
- Windows console encoding: set `PYTHONUTF8=1`; scripts call `sys.stdout.reconfigure(encoding="utf-8")`.
- One-line quoted `related`/`edges` items: `- id: "x", title: "y", type: "z"` / `- rel: "belongs_to", target: "Name", target_type: "مدرسة"`.
- `data-en.json` and `index-en.html` are gitignored: rebuild after pulling.
- Mobile overflow fix for the English build is already in the EN template (skip-link override).
- Do not add `part:` values outside the 13 modules; `module_of()` in the checker reads `part` (or the first crumb segment).
