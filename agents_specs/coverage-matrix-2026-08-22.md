# Coverage Matrix — Atlas Psychology Section
**Generated**: 2026-08-22 (final update after MiniMax bridge + orphan pipeline)

## Totals (all approved files)

| Type | Count |
|---|---|
| axioms | 4 |
| branches | 135 |
| concepts | 466 |
| contexts | 13 |
| critiques | 29 |
| debates | 57 |
| dialogues | 3 |
| disorders | 109 |
| events | 72 |
| experiences | 3 |
| instruments | 96 |
| metaphors | 3 |
| questions | 3 |
| relations | 35 |
| schools | 368 |
| studies | 115 |
| syndromes | 191 |
| techniques | 333 |
| terms | 3 |
| thinkers | 1694 |
| works | 301 |
| **Total** | **4033** |

## Orphan distribution

| Type | Orphans |
|---|---|
| axioms | 4 |
| branches | 47 |
| concepts | 182 |
| contexts | 8 |
| critiques | 15 |
| debates | 36 |
| dialogues | 2 |
| disorders | 47 |
| events | 62 |
| experiences | 2 |
| instruments | 69 |
| metaphors | 2 |
| questions | 1 |
| relations | 24 |
| schools | 14 |
| studies | 83 |
| syndromes | 126 |
| techniques | 73 |
| terms | 2 |
| thinkers | 689 |
| works | 161 |
| **Total orphans** | **1649** (40.9% of total) |

## Psychology Schools (38 total)

| School slug | Items | Status |
|---|---|---|
| sch-psychoanalysis | 430 | Major |
| sch-existential-therapy | 376 | Major |
| sch-dbt | 56 | Major |
| sch-cognitive-behavioral | 53 | Major |
| sch-act | 49 | Major |
| sch-behaviorism | 37 | Major |
| sch-humanistic | 27 | Major |
| sch-systemic-family | 25 | Major |
| sch-developmental | 14 | Adequate |
| sch-social-psychology | 12 | Adequate |
| sch-positive-psychology | 10 | Adequate |
| sch-gestalt-therapy | 8 | Adequate |
| sch-narrative-therapy | 8 | Adequate |
| sch-indigenous-psychology | 8 | Adequate |
| sch-transpersonal | 7 | Adequate |
| sch-biological-neuro | 6 | Adequate |
| sch-eft | 6 | New — adequate |
| sch-istdp | 4 | New — adequate |
| sch-african-psychology | 4 | New — minimal |
| sch-istdp | 4 | New |
| sch-emdr | 3 | New — minimal |
| sch-ifs | 3 | New — minimal |
| sch-ipt | 3 | New — minimal |
| sch-islamic-psychology | 3 | New — minimal |
| sch-cft | 3 | New — minimal |
| sch-rebt | 3 | New — minimal |
| sch-solution-focused | 3 | New — minimal |
| sch-confucian-psychology | 3 | New — minimal |
| sch-somatic-experiencing | 3 | New — minimal |
| sch-aedp | 3 | New — minimal |
| sch-buddhist-psychology | 2 | New — minimal |
| sch-imago | 2 | New — minimal |
| sch-motivational-interviewing | 2 | New — minimal |
| sch-liberation-psychology | 2 | New — minimal |
| sch-polyvagal-informed-therapy | 2 | New — minimal |
| sch-psychedelic-assisted-therapy | 2 | New — minimal |
| sch-eft-couples | 1 | New — minimal |
| sch-sensorimotor-psychotherapy | 1 | New — minimal |

## Architectural changes (DRs)

- **DR-001**: Added `register` field (academic/clinical/popular/philosophical).
- **DR-002**: Added `cultural_origin` field (8 values: islamic-arabic, east-asian, indigenous, european-continental, etc.).
- **DR-003**: Added `evidence_level` field (6 values: well-established, experimental, theoretical, emerging, controversial, unverified).
- **DR-004**: Coverage matrix methodology — count by `belongs_to` edge, not by `related` list.

## Bridge section

- `thk-james-william` (William James): ACCEPTED → part: "bridge", crumb updated.
- `thk-merleau-ponty`, `thk-gbateson`, `thk-fromm`: REJECTED (strict §5.3 reading excludes researchers and clinical practitioners).

## Worker over-reach incident

- Worker (bg_2ac986cf) over-reached: modified 599 files including content rewrites.
- Mitigation: stopped worker, reverted all changes with `git checkout HEAD -- .`, re-applied structural and manual passes with strict scope.
- New worker contract: explicit slugs, explicit dirs, no rewrites of approved files, only `related:` section modifications.
