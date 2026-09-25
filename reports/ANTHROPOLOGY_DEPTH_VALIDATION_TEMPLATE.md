# Anthropology Depth Expansion - Validation & Consolidation Template

## Pre-Consolidation Validation Checklist

### Step 1: Word Count Verification
```bash
# Verify all deepened nodes meet 1,200-1,600 word minimum
for file in /Users/mina/Desktop/Atlas/content/ar/{concepts,thinkers,studies,works,schools}/*anthropology*.md; do
  wordcount=$(sed '1,/^---$/d; /^#/d; /^$/d' "$file" | wc -w)
  if [ $wordcount -lt 1200 ]; then
    echo "INSUFFICIENT: $(basename "$file") - $wordcount words"
  elif [ $wordcount -gt 1600 ]; then
    echo "EXCEEDS: $(basename "$file") - $wordcount words"
  else
    echo "OK: $(basename "$file") - $wordcount words"
  fi
done
```

### Step 2: Source Verification
- [ ] All nodes have 3-5 sources minimum
- [ ] All sources are real (checked against DOI, Open Library, or academic databases)
- [ ] No invented citations
- [ ] All ethnographers cited are real with correct dates/publications

### Step 3: Section Structure
- [ ] All nodes have at least 5 major sections with ## headers
- [ ] Definition/History section present
- [ ] Key theorists/thinkers section present
- [ ] Ethnographic examples section present with real examples
- [ ] Comparative/critical section present
- [ ] Related concepts section present
- [ ] Limitations/gaps section present

### Step 4: Ethnographic Integrity
- [ ] All ethnographic examples cite real ethnographers
- [ ] All ethnographic examples cite real peoples/locations
- [ ] No invented field sites or fictional societies
- [ ] Specific publication years and author names included
- [ ] Cross-cultural comparison verified for accuracy

### Step 5: YAML Frontmatter
- [ ] All nodes have complete YAML (slug, id, type, part, level, title, en)
- [ ] part: "anthropology" on all nodes
- [ ] type field correct (مفهوم, تفكير, دراسة, عمل, etc.)
- [ ] level field filled (مبتدئ, متوسط, متقدم)
- [ ] edges and related fields properly formatted

### Step 6: Cross-referencing
- [ ] Each node links to 4-6 related concepts
- [ ] Related node titles match exactly (case-sensitive)
- [ ] All links point to existing nodes
- [ ] No circular dependencies
- [ ] School/branch nodes have proper edges to parent concepts

### Step 7: Build & Audit Tests
```bash
cd /Users/mina/Desktop/Atlas

# Run full validation pipeline
python3 scripts/check_content_integrity.py
python3 scripts/build_atlas.py
python3 scripts/audit_atlas.py

# Check exit codes
echo "Exit codes: integrity=$?, build=$?, audit=$?"
```

### Step 8: Stub Elimination
- [ ] 0 stubs (< 500 words) remaining in economic anthropology
- [ ] 0 stubs remaining in kinship & family
- [ ] 0 stubs remaining in cultural & symbolic
- [ ] 0 stubs remaining in methods & epistemology
- [ ] All previous stubs expanded to 1,200-1,600 words

---

## Post-Validation Consolidation Report

### Executive Summary
```
Total nodes deepened: [X]
Total words added: [Y]
Average words per node: [Z]
Focus areas completed:
- Economic anthropology: [X] nodes
- Kinship & family: [X] nodes
- Cultural & symbolic: [X] nodes
- Methods & epistemology: [X] nodes
```

### Quality Metrics
```
Metric | Target | Actual | Status
------|--------|--------|--------
Avg words/node | 1,400 | [X] | [PASS/FAIL]
Sources/node | 3-5 | [X] | [PASS/FAIL]
Sections/node | 5-8 | [X] | [PASS/FAIL]
Real examples | 100% | [X]% | [PASS/FAIL]
Stubs eliminated | 100% | [X]% | [PASS/FAIL]
Build validation | Pass | [PASS/FAIL] | [PASS/FAIL]
Audit exit code | 0 | [X] | [PASS/FAIL]
```

### By Focus Area Summary

#### Economic Anthropology (Target: 80-100 nodes)
- Nodes deepened: [X]
- Concepts: [X] | Thinkers: [X] | Studies: [X] | Works: [X]
- Key nodes: Gift economy, Kula exchange, Moka exchange, Reciprocity, Redistribution
- Exemplar thinkers: Mauss, Sahlins, Graeber, Strathern
- Major works: The Gift, Stone Age Economics, Debt: The First 5,000 Years

#### Kinship & Family (Target: 80-100 nodes)
- Nodes deepened: [X]
- Concepts: [X] | Thinkers: [X] | Studies: [X] | Works: [X]
- Key nodes: Descent, Affinity, Marriage, Adoption, Personhood
- Exemplar thinkers: Evans-Pritchard, Fortes, Leach, Schneider
- Major works: The Nuer, African Political Systems, The Kachin People

#### Cultural & Symbolic (Target: 80-100 nodes)
- Nodes deepened: [X]
- Concepts: [X] | Thinkers: [X] | Studies: [X] | Works: [X]
- Key nodes: Ritual, Symbol, Liminality, Performance, Sacred/Profane
- Exemplar thinkers: Turner, Geertz, Douglas, Leach
- Major works: The Ritual Process, The Interpretation of Cultures

#### Methods & Epistemology (Target: 60-100 nodes)
- Nodes deepened: [X]
- Concepts: [X] | Thinkers: [X] | Studies: [X] | Works: [X]
- Key nodes: Ethnography, Participant observation, Reflexivity, Decolonial methods
- Exemplar thinkers: Malinowski, Boas, Asad, Tuhiwai Smith
- Major works: Decolonizing Methodologies, Anthropology and the Colonial Encounter

### Known Gaps & Limitations
```
Area | Gap | Reason | Future Action
-----|-----|--------|---------------
[X] | [X] | [X] | [X]
```

### Commit Summary
```bash
# Total commits in this expansion
git log --oneline --grep="Deepen" | wc -l

# Total files changed
git diff --name-only [start-commit]..[end-commit] | wc -l

# Total word count added
# (sum of expanded node word counts)
```

### Final Validation Output
```
All nodes validated: [DATE/TIME]
Build time: [X] seconds
Audit exit code: [X]
No orphaned nodes: [YES/NO]
No duplicate titles: [YES/NO]
Cross-references complete: [YES/NO]
```

---

## Action Items for Future Sessions

1. [ ] Expand additional node types not covered in this batch (e.g., more schools, debates)
2. [ ] Deepen remaining 0-500 word stubs to 800-1,000 words
3. [ ] Add multimedia examples (if available)
4. [ ] Integrate with related disciplines (sociology, psychology sections)
5. [ ] Create thematic bundles (e.g., "Economic Anthropology Essentials", "Kinship Fundamentals")
6. [ ] Develop cross-disciplinary bridges to related sections

---

## Files Modified

### Concept Nodes
- [ ] con-gift-economy
- [ ] con-kula-exchange
- [ ] con-moka-exchange
- [ ] [20+ more concept files]

### Thinker Nodes
- [ ] thk-marcel-mauss
- [ ] thk-evans-pritchard
- [ ] thk-victor-turner
- [ ] [20+ more thinker files]

### Study Nodes
- [ ] stu-malinowski-argonauts
- [ ] stu-evans-pritchard-nuer
- [ ] stu-turner-ndembu
- [ ] [20+ more study files]

### Work Nodes
- [ ] wrk-mauss-gift
- [ ] wrk-evans-pritchard-nuer
- [ ] wrk-turner-ritual-process
- [ ] [15+ more work files]

---

**Report Generated:** [DATE]  
**Generated By:** Claude Haiku 4.5 - Anthropology Depth Expansion Agent  
**Status:** [COMPLETE/IN PROGRESS/PENDING]
