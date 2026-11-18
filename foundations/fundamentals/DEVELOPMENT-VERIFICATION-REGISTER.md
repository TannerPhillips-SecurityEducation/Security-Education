# Fundamentals: Development and Verification Register

**Working edition:** v1.19  
**Scope:** **12 knowledge areas and 116 tracked subjects, all internally Reviewed (model-assisted):** 109 legacy articles plus 7 newly audited under Wave F. The 109-heading baseline remains historical, and the total is not fixed.  
**Purpose:** Track authoring, source validation, relationships, canonical article paths, and outstanding architecture decisions without overstating completion.

## Interpretation and status

- **Inventoried:** Approved heading exists in its area index, but no canonical subject article is yet claimed.
- **Pilot queued:** One of the six approved first authoring targets; a queued article is **not** published or technically validated.
- **Draft:** Substantive article has been committed and can be reviewed; not necessarily source-verified or accepted.
- **Reviewed:** A documented scoped technical and editorial audit has passed for the stated subject. Across the present 109 articles the reviews are **model-assisted**; no independent human peer review, complete source verification or final publication is implied.
- **Published:** Canonical reference accepted under the [seven completion gates](README.md#completion-gates), including link and source checks. A commit alone does **not** constitute this status.

**Source review** is tracked separately from development state: **Not reviewed**, **References listed**, **Core claims checked**, or **Verified**. *References listed* indicates linked sources. *Core claims checked* means a documented second-pass source review and example checks occurred, but does not establish complete claim-to-source verification or independent human acceptance. *Verified* requires evidence of a complete scoped technical acceptance review. **Relationship state:** The separate [116-heading canonical ownership register](CANONICAL-OWNERSHIP-REGISTER.md) includes the 109 historical article links and seven proposed conceptual links; they are not a fully verified graph.

**IDs are administrative tracking identifiers only**, not a ratified formal ontology, graph predicate set, or new knowledge-category taxonomy. No Knowledge Checks, Practical Assessments, or quizzes will appear in this repository.

## Portfolio-wide progress

| Measure | Initial baseline |
| --- | ---: |
| Approved knowledge areas | 12 |
| Approved subject headings | 109 |
| Initial authoring pilot targets | 6 |
| Initially completed canonical articles | 0 |
| Initially source-verified canonical articles | 0 |
| Architectural gap decisions still requiring explicit scope approval | 3 (G-01, G-04, G-06) |
| Concept overlap boundaries | 20 approved at architectural level; article-level verification remains |

> The table above is the baseline **at initial register creation**. Current item states are below and must be updated as authoring proceeds.

## Subject-count governance (living inventory)

**November 18, 2026 clarification:** The tracked 109 subject headings are a **versioned snapshot, not a frozen target**. The subject inventory may expand or contract as framework/model/architecture coverage and overlap reviews substantiate additions, splits, consolidations and retirements. The 12 existing knowledge areas remain the current approved navigational baseline; changing those areas requires its own review.

Keep retired/superseded IDs and historical per-wave status counts auditable. When the inventory changes, reconcile all area indexes and this register's denominators. New or significantly altered subjects begin with **their own evidence-backed development and source-review state**; do not mechanically transfer the old 109/109 reviewed claim to a different version of the corpus.

## Current progress: 116 authored and Reviewed (model-assisted); publication acceptance pending

| Development / evidence state | Current heading count | Evidence |
| --- | ---: | --- |
| **Reviewed (model-assisted)** | **116** | 109 legacy subjects under Wave A–E audits plus 7 new subjects under [Wave F's 42-family technical audit](WAVE-F-TECHNICAL-REVIEW-01.md); independent expert acceptance pending |
| **Draft** | **0** | No currently unreviewed authoring drafts; scoped model-assisted review does not establish publication readiness |
| **Inventoried without article** | **0** | All 116 currently tracked headings have canonical article files, with distinct source-review evidence |
| **Core claims checked** | **116** | Legacy scoped audits plus [Wave F](WAVE-F-TECHNICAL-REVIEW-01.md); not complete sentence-level claim verification |
| **Finally accepted / human peer-reviewed** | **0** | No final independent expert acceptance recorded |

**Wave A authoring coverage:** All 26 of 26 approved Wave A headings have substantive, internally Reviewed articles (26/26). Three additional Reviewed references are original pilot subjects belonging to later waves.

**Scope controls:** G-01, G-04 and G-06 have canonical subject placements, authored articles and scoped model-assisted technical review. **Stronger complete source verification, cross-domain coverage acceptance and independent publication review remain open.** No new knowledge area, graph predicate vocabulary, Knowledge Checks or Practical Assessments were introduced.

## Next acceptance gate

1. **Completed scoped internal authoring and technical review:** The legacy **109/109** references retain Wave A–E Reviewed evidence, and all **7/7** newly inventoried references have passed [Wave F's 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md). The **116/116** current subjects are internally Reviewed (model-assisted), with separate **Core claims checked** states, not stronger `Verified` or independent human acceptance.
2. **Completed preliminary inventory/navigation audit:** [Publication Readiness Audit 01](PUBLICATION-READINESS-AUDIT-01.md) examined the pre-report snapshot of **152 Fundamentals Markdown files**, including all 109 articles and twelve area indexes. It checked **2,681 inline relative Markdown-link occurrences**, finding **zero missing file destinations**. The **55 fragment links** corresponded to **32 existing target heading slugs**. All 109 direct ownership links aligned with the register, and all twelve area indexes showed the correct subjects and review states. This is **not** an external URL or exhaustive Markdown semantic audit.
3. **Current publication-quality work:** Strengthen comprehensive claim-to-source traceability, verify external links, evaluate depth and consistency, review model/architecture cross-links, and test seven-domain coverage of the 116 subjects.
4. **Human acceptance and publication remain pending:** Obtain independent qualified expert peer review, adjudicate findings, and satisfy all seven [Fundamentals completion gates](README.md#completion-gates) before marking any article or the corpus **Published**.
5. **Architecture placement, authoring and scoped internal review completed:** G-01 mathematics, G-04 temporality and G-06 AI/ML now have Reviewed (model-assisted) articles; complete source validation and independent publication acceptance remain open. No Knowledge Checks, Practical Assessments or mandatory vendors were added.

**Current inventory reconciliation:** **116 headings = 109 previously Reviewed articles + 7 independently scoped Wave F Reviewed articles**. All seven new canonical paths appear below. Source state is **Core claims checked** for all 116; none is fully source-Verified, independently expert reviewed or Published.

## Detailed coverage by approved knowledge area

### 01. Mathematics & Logic (Wave A; 8 headings)

**Area index:** [Mathematics & Logic](mathematics-logic/README.md). **Coverage questions:** [G-01](COVERAGE-GAP-DECISIONS.md#g-01-linear-algebra-geometry-topology), [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-01-01 | Numbers and numerical systems | [Reviewed article](mathematics-logic/numbers-and-numerical-systems.md) | Reviewed | Core claims checked | [Wave A Batch 02 audit](WAVE-A-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-01-02 | Sets and relations | [Reviewed article](mathematics-logic/sets-and-relations.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-01-03 | Boolean and predicate logic | [Reviewed article](mathematics-logic/boolean-and-predicate-logic.md) | Reviewed | Core claims checked | [Wave A Batch 01 audit](WAVE-A-TECHNICAL-REVIEW-01.md); model-assisted review, human sign-off not claimed |
| F-01-04 | Algebra and functions | [Reviewed article](mathematics-logic/algebra-and-functions.md) | Reviewed | Core claims checked | [Wave A Batch 03 audit](WAVE-A-TECHNICAL-REVIEW-03.md); model-assisted, human approval not claimed |
| F-01-05 | Discrete mathematics | [Reviewed article](mathematics-logic/discrete-mathematics.md) | Reviewed | Core claims checked | [Wave A Batch 04 audit](WAVE-A-TECHNICAL-REVIEW-04.md); model-assisted review, human acceptance not claimed |
| F-01-06 | Graph theory | [Reviewed article](mathematics-logic/graph-theory.md) | Reviewed | Core claims checked | [Wave A Batch 05 audit](WAVE-A-TECHNICAL-REVIEW-05.md); model-assisted, no human peer review |
| F-01-07 | Probability and statistics | [Reviewed article](mathematics-logic/probability-and-statistics.md) | Reviewed | Core claims checked | [Batch 06 audit](WAVE-A-TECHNICAL-REVIEW-06.md); model-assisted, no human peer review |
| F-01-08 | Units and quantities | [Reviewed article](mathematics-logic/units-and-quantities.md) | Reviewed | Core claims checked | [Wave A Batch 07 audit](WAVE-A-TECHNICAL-REVIEW-07.md); model-assisted, no human peer review |
| F-01-09 | Linear algebra and vector spaces | [Reviewed article](mathematics-logic/linear-algebra-and-vector-spaces.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |
| F-01-10 | Geometry and spatial reasoning | [Reviewed article](mathematics-logic/geometry-and-spatial-reasoning.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |
| F-01-11 | Topology and continuity | [Reviewed article](mathematics-logic/topology-and-continuity.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |

### 02. Scientific & Analytical Reasoning (Wave A; 8 headings)

**Area index:** [Scientific & Analytical Reasoning](scientific-analytical-reasoning/README.md). **Coverage questions:** [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-07](COVERAGE-GAP-DECISIONS.md#g-07-data-quality-and-semantics), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-02-01 | Observation | [Reviewed article](scientific-analytical-reasoning/observation.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-02-02 | Measurement | [Reviewed article](scientific-analytical-reasoning/measurement.md) | Reviewed | Core claims checked | [Wave A Batch 02 audit](WAVE-A-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-02-03 | Evidence | [Reviewed article](scientific-analytical-reasoning/evidence.md) | Reviewed | Core claims checked | [Wave A Batch 01 audit](WAVE-A-TECHNICAL-REVIEW-01.md); model-assisted review, human sign-off not claimed |
| F-02-04 | Hypotheses and experiments | [Reviewed article](scientific-analytical-reasoning/hypotheses-and-experiments.md) | Reviewed | Core claims checked | [Wave A Batch 03 audit](WAVE-A-TECHNICAL-REVIEW-03.md); model-assisted, human approval not claimed |
| F-02-05 | Deduction, induction, and abduction | [Reviewed article](scientific-analytical-reasoning/deduction-induction-abduction.md) | Reviewed | Core claims checked | [Wave A Batch 04 audit](WAVE-A-TECHNICAL-REVIEW-04.md); model-assisted review, human acceptance not claimed |
| F-02-06 | Causality and correlation | [Reviewed article](scientific-analytical-reasoning/causality-and-correlation.md) | Reviewed | Core claims checked | [Wave A Batch 05 audit](WAVE-A-TECHNICAL-REVIEW-05.md); model-assisted, no human peer review |
| F-02-07 | Uncertainty and confidence | [Reviewed article](scientific-analytical-reasoning/uncertainty-and-confidence.md) | Reviewed | Core claims checked | [Batch 06 audit](WAVE-A-TECHNICAL-REVIEW-06.md); model-assisted, no human peer review |
| F-02-08 | Validation and falsification | [Reviewed article](scientific-analytical-reasoning/validation-and-falsification.md) | Reviewed | Core claims checked | [Wave A Batch 07 audit](WAVE-A-TECHNICAL-REVIEW-07.md); model-assisted, no human peer review |

### 03. Models & Abstraction (Wave A; 10 headings)

**Area index:** [Models & Abstraction](models-abstraction/README.md). **Coverage questions:** [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking), [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-03-01 | Entities and attributes | [Reviewed article](models-abstraction/entities-and-attributes.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-03-02 | Identity and distinction | [Reviewed article](models-abstraction/identity-and-distinction.md) | Reviewed | Core claims checked | [Wave A Batch 03 audit](WAVE-A-TECHNICAL-REVIEW-03.md); model-assisted, human approval not claimed |
| F-03-03 | Relationships | [Reviewed article](models-abstraction/relationships.md) | Reviewed | Core claims checked | [Wave A Batch 02 audit](WAVE-A-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-03-04 | Boundaries | [Reviewed article](models-abstraction/boundaries.md) | Reviewed | Core claims checked | [Wave A Batch 04 audit](WAVE-A-TECHNICAL-REVIEW-04.md); model-assisted review, human acceptance not claimed |
| F-03-05 | Abstraction | [Reviewed article](models-abstraction/abstraction.md) | Reviewed | Core claims checked | [Wave A Batch 05 audit](WAVE-A-TECHNICAL-REVIEW-05.md); model-assisted, no human peer review |
| F-03-06 | Classification | [Reviewed article](models-abstraction/classification.md) | Reviewed | Core claims checked | [Batch 06 audit](WAVE-A-TECHNICAL-REVIEW-06.md); model-assisted, no human peer review |
| F-03-07 | Ontologies and taxonomies | [Reviewed article](models-abstraction/ontologies-and-taxonomies.md) | Reviewed | Core claims checked | [Wave A Batch 07 audit](WAVE-A-TECHNICAL-REVIEW-07.md); model-assisted, no human peer review |
| F-03-08 | Schemas | [Reviewed article](models-abstraction/schemas.md) | Reviewed | Core claims checked | [Wave A Batch 07 audit](WAVE-A-TECHNICAL-REVIEW-07.md); model-assisted, no human peer review |
| F-03-09 | State, events, and transitions | [Reviewed article](models-abstraction/state-events-and-transitions.md) | Reviewed | Core claims checked | [Wave A Batch 01 audit](WAVE-A-TECHNICAL-REVIEW-01.md); model-assisted review, human sign-off not claimed |
| F-03-10 | Conceptual and formal models | [Reviewed article](models-abstraction/conceptual-and-formal-models.md) | Reviewed | Core claims checked | [Wave A Batch 07 audit](WAVE-A-TECHNICAL-REVIEW-07.md); model-assisted, no human peer review |
| F-03-11 | Temporal concepts and models | [Reviewed article](models-abstraction/temporal-concepts-and-models.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |

### 04. Physical & Electrical Principles (Wave C; 9 headings)

**Area index:** [Physical & Electrical Principles](physical-electrical-principles/README.md). **Coverage questions:** [G-05](COVERAGE-GAP-DECISIONS.md#g-05-signal-processing). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-04-01 | Matter and energy | [Reviewed article](physical-electrical-principles/matter-and-energy.md) | Reviewed | Core claims checked | [Wave C Batch 01 audit](WAVE-C-TECHNICAL-REVIEW-01.md); model-assisted, independent human review not claimed |
| F-04-02 | Electricity | [Reviewed article](physical-electrical-principles/electricity.md) | Reviewed | Core claims checked | [Wave C Batch 01 audit](WAVE-C-TECHNICAL-REVIEW-01.md); model-assisted, independent human review not claimed |
| F-04-03 | Electrical circuits | [Reviewed article](physical-electrical-principles/electrical-circuits.md) | Reviewed | Core claims checked | [Wave C Batch 01 audit](WAVE-C-TECHNICAL-REVIEW-01.md); model-assisted, independent human review not claimed |
| F-04-04 | Electronics | [Reviewed article](physical-electrical-principles/electronics.md) | Reviewed | Core claims checked | [Wave C Batch 02 audit](WAVE-C-TECHNICAL-REVIEW-02.md); model-assisted, independent human review not claimed |
| F-04-05 | Analog and digital signals | [Reviewed article](physical-electrical-principles/analog-and-digital-signals.md) | Reviewed | Core claims checked | [Wave C Batch 02 audit](WAVE-C-TECHNICAL-REVIEW-02.md); model-assisted, independent human review not claimed |
| F-04-06 | Waves and frequency | [Reviewed article](physical-electrical-principles/waves-and-frequency.md) | Reviewed | Core claims checked | [Wave C Batch 02 audit](WAVE-C-TECHNICAL-REVIEW-02.md); model-assisted, independent human review not claimed |
| F-04-07 | Sensors and actuators | [Reviewed article](physical-electrical-principles/sensors-and-actuators.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-04-08 | Signal conversion | [Reviewed article](physical-electrical-principles/signal-conversion.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-04-09 | Physical control mechanisms | [Reviewed article](physical-electrical-principles/physical-control-mechanisms.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |

### 05. Information & Data (Wave B; 9 headings)

**Area index:** [Information & Data](information-data/README.md). **Coverage questions:** [G-07](COVERAGE-GAP-DECISIONS.md#g-07-data-quality-and-semantics), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-05-01 | Symbols and encoding | [Reviewed article](information-data/symbols-and-encoding.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-05-02 | Bits and bytes | [Reviewed article](information-data/bits-and-bytes.md) | Reviewed | Core claims checked | [Wave B Batch 01 audit](WAVE-B-TECHNICAL-REVIEW-01.md); model-assisted, no human peer review |
| F-05-03 | Information theory | [Reviewed article](information-data/information-theory.md) | Reviewed | Core claims checked | [Wave B Batch 01 audit](WAVE-B-TECHNICAL-REVIEW-01.md); model-assisted, no human peer review |
| F-05-04 | Data types | [Reviewed article](information-data/data-types.md) | Reviewed | Core claims checked | [Wave B Batch 01 audit](WAVE-B-TECHNICAL-REVIEW-01.md); model-assisted, no human peer review |
| F-05-05 | Datasets, records, fields, and values | [Reviewed article](information-data/datasets-records-fields-and-values.md) | Reviewed | Core claims checked | [Wave B Batch 01 audit](WAVE-B-TECHNICAL-REVIEW-01.md); model-assisted, no human peer review |
| F-05-06 | Data structures and formats | [Reviewed article](information-data/data-structures-and-formats.md) | Reviewed | Core claims checked | [Wave B Batch 02 audit](WAVE-B-TECHNICAL-REVIEW-02.md); model-assisted, no human peer review |
| F-05-07 | Metadata | [Reviewed article](information-data/metadata.md) | Reviewed | Core claims checked | [Wave B Batch 02 audit](WAVE-B-TECHNICAL-REVIEW-02.md); model-assisted, no human peer review |
| F-05-08 | Databases and queries | [Reviewed article](information-data/databases-and-queries.md) | Reviewed | Core claims checked | [Wave B Batch 02 audit](WAVE-B-TECHNICAL-REVIEW-02.md); model-assisted, no human peer review |
| F-05-09 | Data provenance and lifecycle | [Reviewed article](information-data/data-provenance-and-lifecycle.md) | Reviewed | Core claims checked | [Wave B Batch 02 audit](WAVE-B-TECHNICAL-REVIEW-02.md); model-assisted, no human peer review |

### 06. Digital Systems & Hardware (Wave C; 9 headings)

**Area index:** [Digital Systems & Hardware](digital-systems-hardware/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-06-01 | Digital logic | [Reviewed article](digital-systems-hardware/digital-logic.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-06-02 | Computing components | [Reviewed article](digital-systems-hardware/computing-components.md) | Reviewed | Core claims checked | [Wave C Batch 01 audit](WAVE-C-TECHNICAL-REVIEW-01.md); model-assisted, independent human review not claimed |
| F-06-03 | Processors and instruction sets | [Reviewed article](digital-systems-hardware/processors-and-instruction-sets.md) | Reviewed | Core claims checked | [Wave C Batch 02 audit](WAVE-C-TECHNICAL-REVIEW-02.md); model-assisted, independent human review not claimed |
| F-06-04 | Memory and storage | [Reviewed article](digital-systems-hardware/memory-and-storage.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-05 | Buses and interfaces | [Reviewed article](digital-systems-hardware/buses-and-interfaces.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-06 | Input/output | [Reviewed article](digital-systems-hardware/input-output.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-07 | Timing and clocks | [Reviewed article](digital-systems-hardware/timing-and-clocks.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-08 | Firmware | [Reviewed article](digital-systems-hardware/firmware.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-09 | Hardware abstraction | [Reviewed article](digital-systems-hardware/hardware-abstraction.md) | Reviewed | Core claims checked | [Wave C Batch 03 audit](WAVE-C-TECHNICAL-REVIEW-03.md); model-assisted, independent human peer review pending |
| F-06-10 | Computer architecture models | [Reviewed article](digital-systems-hardware/computer-architecture-models.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |

### 07. Computation & Algorithms (Wave D; 9 headings)

**Area index:** [Computation & Algorithms](computation-algorithms/README.md). **Coverage questions:** [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-06](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-07-01 | Computability | [Reviewed article](computation-algorithms/computability.md) | Reviewed | Core claims checked | [Wave D Batch 01 audit](WAVE-D-TECHNICAL-REVIEW-01.md); model-assisted, human review pending |
| F-07-02 | Algorithms | [Reviewed article](computation-algorithms/algorithms.md) | Reviewed | Core claims checked | [Wave D Batch 01 audit](WAVE-D-TECHNICAL-REVIEW-01.md); model-assisted, human review pending |
| F-07-03 | Algorithm design | [Reviewed article](computation-algorithms/algorithm-design.md) | Reviewed | Core claims checked | [Wave D Batch 01 audit](WAVE-D-TECHNICAL-REVIEW-01.md); model-assisted, human review pending |
| F-07-04 | Complexity | [Reviewed article](computation-algorithms/complexity.md) | Reviewed | Core claims checked | [Wave D Batch 01 audit](WAVE-D-TECHNICAL-REVIEW-01.md); model-assisted, human review pending |
| F-07-05 | Computational data structures | [Reviewed article](computation-algorithms/computational-data-structures.md) | Reviewed | Core claims checked | [Wave D Batch 02 audit](WAVE-D-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-07-06 | Iteration and recursion | [Reviewed article](computation-algorithms/iteration-and-recursion.md) | Reviewed | Core claims checked | [Wave D Batch 02 audit](WAVE-D-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-07-07 | Concurrency and parallelism | [Reviewed article](computation-algorithms/concurrency-and-parallelism.md) | Reviewed | Core claims checked | [Wave D Batch 02 audit](WAVE-D-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-07-08 | Synchronization | [Reviewed article](computation-algorithms/synchronization.md) | Reviewed | Core claims checked | [Wave D Batch 02 audit](WAVE-D-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-07-09 | Computational efficiency | [Reviewed article](computation-algorithms/computational-efficiency.md) | Reviewed | Core claims checked | [Wave D Batch 02 audit](WAVE-D-TECHNICAL-REVIEW-02.md); model-assisted, human peer review not claimed |
| F-07-10 | Artificial intelligence foundations | [Reviewed article](computation-algorithms/artificial-intelligence-foundations.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |
| F-07-11 | Machine learning foundations | [Reviewed article](computation-algorithms/machine-learning-foundations.md) | Reviewed | Core claims checked | [Wave F 42-family audit](WAVE-F-TECHNICAL-REVIEW-01.md); model-assisted, full source and independent peer review pending |

### 08. Software & Programming (Wave D; 9 headings)

**Area index:** [Software & Programming](software-programming/README.md). **Coverage questions:** [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-08-01 | Programming languages | [Reviewed article](software-programming/programming-languages.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-02 | Syntax and semantics | [Reviewed article](software-programming/syntax-and-semantics.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-03 | Programming paradigms | [Reviewed article](software-programming/programming-paradigms.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-04 | Compilation and interpretation | [Reviewed article](software-programming/compilation-and-interpretation.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-05 | Runtime environments | [Reviewed article](software-programming/runtime-environments.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-06 | Modules and dependencies | [Reviewed article](software-programming/modules-and-dependencies.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-07 | Software interfaces | [Reviewed article](software-programming/software-interfaces.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-08 | Error handling | [Reviewed article](software-programming/error-handling.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |
| F-08-09 | Testing and software lifecycle | [Reviewed article](software-programming/testing-and-software-lifecycle.md) | Reviewed | Core claims checked | [Wave D Software 54-family audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); model-assisted, human peer review pending |

### 09. Operating System Principles (Wave E; 10 headings)

**Area index:** [Operating System Principles](operating-system-principles/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-09-01 | Kernels | [Reviewed article](operating-system-principles/kernels.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-02 | System calls | [Reviewed article](operating-system-principles/system-calls.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-03 | Processes and threads | [Reviewed article](operating-system-principles/processes-and-threads.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-04 | Scheduling | [Reviewed article](operating-system-principles/scheduling.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-05 | Memory management | [Reviewed article](operating-system-principles/memory-management.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-06 | Filesystems | [Reviewed article](operating-system-principles/filesystems.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-07 | Drivers and devices | [Reviewed article](operating-system-principles/drivers-and-devices.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-08 | Execution contexts | [Reviewed article](operating-system-principles/execution-contexts.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-09 | System initialization | [Reviewed article](operating-system-principles/system-initialization.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |
| F-09-10 | Resource management | [Reviewed article](operating-system-principles/resource-management.md) | Reviewed | Core claims checked | [Wave E Operating System Principles technical audit](WAVE-E-TECHNICAL-REVIEW-01.md); model-assisted, independent human peer review pending |

### 10. Communication & Distributed Systems (Wave E; 9 headings)

**Area index:** [Communication & Distributed Systems](communication-distributed-systems/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks), [G-08](COVERAGE-GAP-DECISIONS.md#g-08-distributed-consistency-and-partial-failure). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-10-01 | Communication models | [Reviewed article](communication-distributed-systems/communication-models.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-02 | Transmission and signaling | [Reviewed article](communication-distributed-systems/transmission-and-signaling.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-03 | Communication channels | [Reviewed article](communication-distributed-systems/communication-channels.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-04 | Protocols and layering | [Reviewed article](communication-distributed-systems/protocols-and-layering.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-05 | Addressing and naming | [Reviewed article](communication-distributed-systems/addressing-and-naming.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-06 | Latency and throughput | [Reviewed article](communication-distributed-systems/latency-and-throughput.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-07 | Reliability and ordering | [Reviewed article](communication-distributed-systems/reliability-and-ordering.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-08 | Distributed state | [Reviewed article](communication-distributed-systems/distributed-state.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |
| F-10-09 | Synchronization and coordination | [Reviewed article](communication-distributed-systems/synchronization-and-coordination.md) | Reviewed | Core claims checked | [Wave E Communication & Distributed Systems technical audit](WAVE-E-TECHNICAL-REVIEW-02.md); model-assisted, independent human peer review pending |

### 11. Systems & Engineering (Wave B; 11 headings)

**Area index:** [Systems & Engineering](systems-engineering/README.md). **Coverage questions:** [G-08](COVERAGE-GAP-DECISIONS.md#g-08-distributed-consistency-and-partial-failure), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-11-01 | Systems and subsystems | [Reviewed article](systems-engineering/systems-and-subsystems.md) | Reviewed | Core claims checked | [50-claim-family audit](PILOT-CLAIM-SOURCE-AUDIT.md); model-assisted, no human peer review |
| F-11-02 | Components and interfaces | [Reviewed article](systems-engineering/components-and-interfaces.md) | Reviewed | Core claims checked | [Wave B Batch 03 audit](WAVE-B-TECHNICAL-REVIEW-03.md); model-assisted, no independent human peer review |
| F-11-03 | Architecture and composition | [Reviewed article](systems-engineering/architecture-and-composition.md) | Reviewed | Core claims checked | [Wave B Batch 03 audit](WAVE-B-TECHNICAL-REVIEW-03.md); model-assisted, no independent human peer review |
| F-11-04 | Dependencies | [Reviewed article](systems-engineering/dependencies.md) | Reviewed | Core claims checked | [Wave B Batch 03 audit](WAVE-B-TECHNICAL-REVIEW-03.md); model-assisted, no independent human peer review |
| F-11-05 | State and behavior | [Reviewed article](systems-engineering/state-and-behavior.md) | Reviewed | Core claims checked | [Wave B Batch 03 audit](WAVE-B-TECHNICAL-REVIEW-03.md); model-assisted, no independent human peer review |
| F-11-06 | Feedback and control | [Reviewed article](systems-engineering/feedback-and-control.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |
| F-11-07 | Emergence and complexity | [Reviewed article](systems-engineering/emergence-and-complexity.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |
| F-11-08 | Reliability and failure | [Reviewed article](systems-engineering/reliability-and-failure.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |
| F-11-09 | Requirements | [Reviewed article](systems-engineering/requirements.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |
| F-11-10 | Verification and validation | [Reviewed article](systems-engineering/verification-and-validation.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |
| F-11-11 | System lifecycle | [Reviewed article](systems-engineering/system-lifecycle.md) | Reviewed | Core claims checked | [Wave B Batch 04 audit](WAVE-B-TECHNICAL-REVIEW-04.md); model-assisted, no independent human peer review |

### 12. Human & Sociotechnical Systems (Wave B; 8 headings)

**Area index:** [Human & Sociotechnical Systems](human-sociotechnical-systems/README.md). **Coverage questions:** [G-06](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-12-01 | Human cognition and perception | [Reviewed article](human-sociotechnical-systems/human-cognition-and-perception.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-02 | Decision-making | [Reviewed article](human-sociotechnical-systems/decision-making.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-03 | Human-computer interaction | [Reviewed article](human-sociotechnical-systems/human-computer-interaction.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-04 | Usability and accessibility | [Reviewed article](human-sociotechnical-systems/usability-and-accessibility.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-05 | Human error | [Reviewed article](human-sociotechnical-systems/human-error.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-06 | Collaboration and communication | [Reviewed article](human-sociotechnical-systems/collaboration-and-communication.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-07 | Organizational structures | [Reviewed article](human-sociotechnical-systems/organizational-structures.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |
| F-12-08 | Ethics and professional responsibilities | [Reviewed article](human-sociotechnical-systems/ethics-and-professional-responsibilities.md) | Reviewed | Core claims checked | [Wave B Batch 05 audit](WAVE-B-TECHNICAL-REVIEW-05.md); model-assisted, independent human review not claimed |

## Required update procedure

1. Preserve exact subject wording and **tracker ID** when updating the current snapshot. For an explicitly reviewed merge, split, rename or retirement, record old-to-new mappings and redirects rather than silently deleting history; the total number of subjects may increase or decrease.
2. Once an actual article exists, replace *Not authored / Queued* with a **relative Markdown link to the real file**, and mark the development state **Draft**.
3. Link sources near relevant claims, record what has been independently checked, and only then promote **Source review** to **Verified**.
4. Replace broad, area-level conceptual references with precise canonical article links when those destinations exist.
5. Keep the three pending architectural decisions [G-01 mathematical breadth](COVERAGE-GAP-DECISIONS.md#g-01-linear-algebra-geometry-topology), [G-04 general temporality](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks), and [G-06 AI/ML](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning) visible until explicitly resolved.
6. Make a separate technical/editorial pass after pilot drafting before declaring an article **Reviewed** or **Published**.

## Approved exclusions

This is a **technical knowledge reference**, not an evaluation course: no Knowledge Checks, Practical Assessments, quizzes, test questions, grades, or learner scoring. Worked explanatory examples and verification of factual correctness are encouraged.

[Fundamentals](README.md) · [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Governing Architecture](ARCHITECTURE.md)
