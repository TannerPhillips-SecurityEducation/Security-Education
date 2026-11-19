# Fundamentals | Administrative Editorial Pass 03: Conformance Evidence, Provenance Revisions, and Search Visibility

**Pass date:** November 19, 2026  
**Program:** [Administrative Editorial Passes](../../ADMINISTRATIVE-EDITORIAL-PASSES.md)  
**Scope:** Three existing Reviewed (model-assisted) Fundamentals manuscripts. A0 targeted inspection, A1 consistency, A2 mechanism/depth, A3 independently checked examples, A4 canonical cross-links, A5 bounded source/claim assessment.  
**Status:** Model-assisted administrative and scoped technical review. Not source-complete verification, independent expert review, final publication approval or a new subject wave.  
**Security Foundations:** No new drafts or scope changes. Its pause at 39 Reviewed, 0 Drafts and 57 not authored remains intact.

## 1. Baseline and findings

| Existing article | Observed gap | Change made |
| --- | --- | --- |
| [Verification and Validation](systems-engineering/verification-and-validation.md) | Defined methods and a numeric failure, but did not trace the evidence identifiers, configuration, decision rule or the consequences of bounded measurement error | Added five-record requirement trace and a second outcome under explicit ±8 ms guaranteed error |
| [Data Provenance and Lifecycle](information-data/data-provenance-and-lifecycle.md) | Correct initial unit conversion without a versioned correction/impact example; two remaining references misrepresented general temporality as unresolved | Added two-version source/output lineage with recomputation, downstream impact and model-validity limits; reconciled temporal-owner references |
| [Search and Information Retrieval](information-data/search-and-information-retrieval.md) | Precise existing postings/phrase examples but no concrete distinction between source-state, older indexed visibility, and recall measured against the current source corpus | Added fourth document, indexed-snapshot comparison, explicit relevance rule and two independently recalculated precision/recall cases |

These are targeted manuscript observations, not an exhaustive review of all Fundamentals claims or a quality score.

## 2. Claim-level technical check of the new material

### V. Verification: evidence, test rule and decision boundary

- **V1. Requirement-to-observation trace.** The existing sample times `[120,158,190,205,175]` satisfy the per-case requirement in four of five cases when stipulated exact, while `205 > 200` is a counterexample. Their mean is `848/5=169.6` ms and cannot replace the per-case decision.
- **V2. Measurement bounded-error case.** The *different stipulated assumption* `|actual - observed| ≤ 8` ms gives `190±8 → [182,198]` (conforming), `205±8 → [197,213]` (indeterminate). The rule for an upper limit is `upper ≤ 200` to demonstrate conformance; `lower > 200` to demonstrate nonconformance; neither applies to E4. This is an assumed **maximum error bound**, not a measured calibration result or confidence interval.
- **V3. Evidence scope and product validity.** The trace does not prove every input in an unspecified operating envelope is covered, nor that comfort needs were validated. Acceptance, waiver, observed result, and conformance judgment remain distinct.

**Primary source examined:** [NASA *Product Realization*, sections 5.3–5.4](https://www.nasa.gov/reference/5-0-product-realization/), which distinguishes verified requirements from validation against stakeholder expectations, instrumentation, anomaly handling and technical reporting. The numeric test and bounded-error decision example are editorial hypothetical constructions, independently recalculated here.

### P. Provenance: revision semantics and impact

- **P1. Transformation correctness is relative to source.** `(68−32)×5/9=20` °C and `(77−32)×5/9=25` °C. Both are accurate calculations from their own recorded inputs; neither proves what physically occurred.
- **P2. Revised entity and derivation.** Distinct source and derived versions, conversion activities, revision relationships and downstream use prevent an unqualified claim that one value describes the entire revision history.
- **P3. Model validity and completeness.** A PROV-consistent history is not necessarily truthful, complete or attributable in a forensic sense; unknown exports remain invisible to a missing-link graph.

**Primary sources examined:** [W3C PROV-DM, W3C Recommendation 30 April 2013](https://www.w3.org/TR/prov-dm/), especially derivation and revision, and [W3C PROV Constraints, W3C Recommendation 30 April 2013](https://www.w3.org/TR/prov-constraints/), concerning structural validity. The correction example is explicitly constructed and not a record of an actual instrument event.

**Editorial consistency correction:** Replaced two obsolete claims that general temporal models remained unresolved. General temporality is now owned under [Temporal Concepts and Models](models-abstraction/temporal-concepts-and-models.md), without changing this article's canonical provenance responsibility.

### R. Retrieval: source and index snapshots

- **R1. Corpus and index boundary.** Earlier snapshot has D1–D3, current source S1 adds `D4: red fox stays nearby`; the old index cannot return newly stored D4 under the stipulated visibility condition.
- **R2. Phrase matching and evaluation.** Current-source exact phrase matches `{D1,D4}`; older searchable snapshot returns `{D1}` giving `precision=1/1=1`, `recall=1/2=0.5`; after index visibility refresh both are `2/2=1`. The relevance set is stipulated as exact phrase satisfaction, not a sampled human judgment set.
- **R3. Implementation qualification.** Reader/version visibility is one valid mechanism, not proof that every storage/index architecture has the same lag or refresh semantics.

**Source examined:** [Apache Lucene 10.5.2 `DirectoryReader`](https://lucene.apache.org/core/10_5_2/core/org/apache/lucene/index/DirectoryReader.html), with version-specific reader-refresh semantics. Existing [Stanford IR textbook](https://nlp.stanford.edu/IR-book/) retains general lexical indexing and retrieval-evaluation ownership; the four-document example is editorial and toy-sized.

**Bounded claim groups recorded: 9** (V1–V3, P1–P3, R1–R3), independently recomputed at the level shown. No test hardware, measurement instrument, PROV validator, or live search engine was executed.

## 3. Review and limitations

**Cross-checks:** E4 fails under exact values but is indeterminate under the new assumed bounded-error rule; the two unit conversions are calculated correctly; index-recall denominator changes when the evaluation corpus expands from three to four records; a structurally valid trace does not establish historical truth. These counterexamples prevent the new prose from claiming more than the stipulated models allow.

**Unchanged maturity:** The three articles retain their earlier Reviewed (model-assisted) states. This new ledger supports only the **new material's scoped model-assisted check**; it does not retroactively re-audit all previous sentences, sources, or approval conditions. No Security Foundations drafting, canonical ownership change, subject expansion, or independent publication acceptance occurred.

**Integrity gate:** The committing revision must be checked by actual GitHub workflows, not inferred from links appearing in Markdown. Successful navigation/inventory checks prove structural properties, not factual correctness.

## 4. Remaining opportunities

Potential next deep-understanding targets include [Measurement](scientific-analytical-reasoning/measurement.md) for instrument decision rules, [Evidence](scientific-analytical-reasoning/evidence.md) for inference and source limits, and [Uncertainty and Confidence](scientific-analytical-reasoning/uncertainty-and-confidence.md) for probabilistic confidence versus measurement bounds. Such work is **proposed for future selection based on observed gaps**, not an automatic fourth batch.

[Fundamentals](README.md) · [Program](../../ADMINISTRATIVE-EDITORIAL-PASSES.md) · [Pass 02](ADMINISTRATIVE-EDITORIAL-PASS-02.md)
