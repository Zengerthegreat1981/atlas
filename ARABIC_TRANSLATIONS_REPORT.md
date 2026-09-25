# Arabic Translations Report

**Report Date:** 2026-09-25 10:58:40

## Executive Summary

- **Total English Psychology Terms:** 51,052
- **Terms with Arabic Translations:** 22,395
- **Coverage:** 43.9%
- **Terms Flagged for Review:** 21,876

## Translation Source Distribution

| Source | Count | Percentage |
|---|---|---|
| Extracted from Arabic DB | 527 | 2.4% |
| Semantic Mapping | 21868 | 97.6% |
| Generated | 0 | 0.0% |

## Confidence Distribution

| Confidence Level | Count | Status |
|---|---|---|
| 90-100% | 519 | High Confidence ✓ |
| 80-89% | 8 | Medium Confidence |
| 70-79% | 0 | Review Recommended |
| <70% | 21868 | Needs Review |

## Translation Quality Metrics

- **High Confidence Translations:** 527 (2.4%)
- **Requires Manual Review:** 21876 (97.7%)
- **Average Confidence:** 60.8%

## Implementation Notes

### Approach 1: Extracted from Arabic Database
- Direct matches between English terms and existing Arabic entries
- Highest confidence (80-95%)
- No manual translation required

### Approach 2: Semantic Mapping
- Uses relationships from Task A to guide translation
- Medium confidence (60-80%)
- Requires review by native speaker

### Approach 3: Generated
- Template-based generation for terms without matches
- Lowest confidence (<70%)
- Requires professional translation

## Next Steps

1. Validate high-confidence extractions
2. Manual review and correction of 70-89% confidence translations
3. Professional translation for <70% confidence terms
4. Update YAML frontmatter in all term files
5. Add `ar_source` field with source attribution
6. Commit changes with comprehensive git message

## Files to Update

- All 65,529 English term files (term-*.md)
- Adding/updating: `ar:` and `ar_source:` fields

---

**Generated:** 2026-09-25T10:58:40.032046
