# Fundamentals: Coverage Gap Decision Register

**Status:** Working architectural disposition v0.1; recommendations are not new ratified subject headings, finished reference articles, or a change to the governing taxonomy.  
**Baseline:** 12 approved areas and 109 original subject headings unchanged.  
**Input:** [Concept Overlap and Coverage Review](CONCEPT-OVERLAP-REVIEW.md), [Canonical Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md), [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md).

## Decision rule

A subject is **covered by existing headings, pending authoring** when an approved heading has a credible canonical scope for that material. This is *placement coverage*, not completed or source-verified reference content. A subject **requires an architectural decision** when its scope or discoverable conceptual ownership cannot responsibly be assumed without an explicit choice.

## Disposition summary

| Disposition | Count | Cases |
| --- | ---: | --- |
| Covered by existing headings, pending authoring | 7 | G-02, G-03, G-05, G-07, G-08, G-09, G-10 |
| Architectural decision required | 3 | G-01, G-04, G-06 |
| Approved areas or headings added/renamed | 0 | None |
| Published canonical articles created by this register | 0 | None |

## Framework, Model & Architecture coverage pass (November 18, 2026)

The [Foundational Models, Frameworks & Architectures Audit 01](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) introduces an **evidence-backed review of 77 named technical models/frameworks/architectures** over the current 109-article snapshot. Its 14 FMA review cases are **candidate changes and deepening tasks**, not eleven new gaps, additional approved headings, or an automatic amendment to the ten G-01–G-10 cases below.

**Count clarification:** The **109 tracked subject headings are not fixed**. Changes can add, split, merge, rename or retire headings after recorded coverage/ownership analysis. The old 12-area/109-heading counts remain the **historical baseline for previous audits**, not a requirement to accommodate every new model within existing headings.

**Impact on the three original open decisions:** G-01 may warrant dedicated linear algebra and geometric/topological subjects; G-04 may warrant a canonical general temporal-model subject; G-06 may warrant explicit AI/ML subjects or a separately approved area-level decision. This review **does not resolve or approve** those choices.

## Ten coverage cases

### G-01: Linear algebra, geometry, topology

**Disposition:** Architectural decision required

**Canonical responsibilities:** Mathematics & Logic: Algebra and functions; Discrete mathematics; Graph theory.

**Required domain-agnostic coverage:** Vectors, matrices, transformations, coordinate geometry, continuity and elementary topology. Distinguish graph topology from general mathematical topology.

**Rationale:** Approved headings support some mathematical prerequisites, but do not guarantee coverage of these distinct topics.

**Next action:** Approve explicit depth under existing headings or additional named Mathematics subject headings. No new top-level area proposed.

**Evidence required to close the content gap:** Cross-domain demonstrations of a vector/matrix operation, geometric transformation and graph-vs-topological-space distinction.

### G-02: Numerical methods and optimization

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Mathematics & Logic: Algebra and functions; Computation & Algorithms: Algorithm design and Computational efficiency; Scientific Reasoning: Measurement.

**Required domain-agnostic coverage:** Approximation, rounding and truncation, conditioning, convergence, numerical stability, objective functions, optimization constraints.

**Rationale:** The accepted subjects already cover the underlying mathematics, algorithmic methods and measurement principles.

**Next action:** Develop linked articles without changing category structure; distinguish accuracy from algorithmic performance.

**Evidence required to close the content gap:** Worked numerical error example and a constrained optimization method, with sources and assumptions.

### G-03: Formal methods and model checking

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Mathematics & Logic: Boolean and predicate logic; Models & Abstraction: Conceptual and formal models and State/events/transitions; Systems & Engineering: Verification and validation.

**Required domain-agnostic coverage:** Specifications, state-transition models, invariants, safety/liveness, model checking, proof assumptions, state-space limits.

**Rationale:** Formal representation, logical proof and engineering assurance are already recognized in approved subjects.

**Next action:** Describe these mechanisms in their separate homes; do not imply tests prove deployed systems universally correct.

**Evidence required to close the content gap:** A minimal state-machine specification, invariant, liveness property and careful qualification of model scope.

### G-04: Time, temporality, clocks

**Disposition:** Architectural decision required

**Canonical responsibilities:** Models & Abstraction: State/events/transitions (candidate general owner); Mathematics: Units and quantities; Digital Systems: Timing and clocks; Distributed Systems: Synchronization and coordination.

**Required domain-agnostic coverage:** Instants, intervals, durations, temporal ordering, simultaneity, timestamps, physical time scales, clock readings, event causality.

**Rationale:** Existing headings cover units and implementations but do not explicitly establish the general canonical theory of temporality. Boundary exception B-11 remains.

**Next action:** Approve an explicit temporal-concepts treatment within Models & Abstraction or a separately named subject within an existing area; keep physical clock and distributed-order mechanisms distinct.

**Evidence required to close the content gap:** A coherent comparison of duration, instant, timestamp and causal partial order, including unsynchronized clocks.

### G-05: Signal processing

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Physical & Electrical Principles: Analog and digital signals; Waves and frequency; Signal conversion; Scientific Reasoning: Measurement.

**Required domain-agnostic coverage:** Frequency representation, filtering, sampling, quantization, noise, aliasing and reconstruction.

**Rationale:** The approved signals and conversion headings have clear ownership of these mechanisms.

**Next action:** Develop content under existing headings. Avoid claims of perfect reconstruction without assumptions.

**Evidence required to close the content gap:** A sampling/aliasing example explicitly identifying band-limit and sampling assumptions.

### G-06: Artificial intelligence and machine learning

**Disposition:** Architectural decision required

**Canonical responsibilities:** Mathematics: Probability and statistics; Computation: Algorithms and Algorithm design; Information & Data: Data types, datasets, provenance; Human & Sociotechnical Systems: Decision-making.

**Required domain-agnostic coverage:** Symbolic reasoning vs learned models; training vs inference; supervised/unsupervised/reinforcement learning; loss, features, generalization, overfitting, evaluation, drift, limitations; planning and knowledge representation.

**Rationale:** CS2023 treats AI as a substantial distinct knowledge area. Distributed prerequisite topics in the existing twelve do not guarantee discoverable, complete AI/ML treatment.

**Next action:** Approve an AI/ML cross-area index as an interim path, then decide whether explicit added subjects or a thirteenth area are justified; neither is created here.

**Evidence required to close the content gap:** An approved core concept inventory and canonical placement map covering both ML and non-ML AI foundations.

### G-07: Data quality and semantics

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Information & Data: Metadata; Data provenance and lifecycle; Data types; Datasets/records/fields/values; Scientific Reasoning: Evidence.

**Required domain-agnostic coverage:** Accuracy, completeness, consistency, relevance, missingness, representativeness, semantic fit, timeliness, provenance and interpretation.

**Rationale:** The approved data and evidence headings already address representation and evaluation.

**Next action:** Add explicit quality and meaning requirements to existing articles, linking to scientific evidence evaluation.

**Evidence required to close the content gap:** An example of schema-valid but inaccurate or contextually inappropriate data, with quality limitations.

### G-08: Distributed consistency and partial failure

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Communication & Distributed Systems: Distributed state; Reliability and ordering; Synchronization and coordination; Systems & Engineering: Reliability and failure.

**Required domain-agnostic coverage:** Replication, linearizability and eventual consistency, delay, partitions, retries, idempotency, fault assumptions, ordering and agreement.

**Rationale:** The accepted distributed-state and failure subjects own these principles.

**Next action:** Develop consistency and failure boundaries as depth under existing subjects; do not equate timestamps with causality.

**Evidence required to close the content gap:** Two-node replication scenario with delayed messages, partial failure, assumptions and consistency guarantees.

### G-09: Scientific and engineering validation

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Scientific Reasoning: Validation and falsification; Systems & Engineering: Verification and validation; Software & Programming: Testing and software lifecycle.

**Required domain-agnostic coverage:** Scientific empirical testing and falsifiability; requirement conformance; intended-use validation; software tests as evidence.

**Rationale:** These mechanisms already have different approved canonical homes and were distinguished by overlap B-17.

**Next action:** Author three connected explanations, preserving their different evidence and acceptance criteria.

**Evidence required to close the content gap:** Three comparable cases explaining what claim each method verifies, validates or tests and what it cannot establish.

### G-10: Lifecycle evolution and versioning

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Information & Data: Data provenance and lifecycle; Software & Programming: Modules/dependencies and Testing/software lifecycle; Systems & Engineering: System lifecycle; Models: Schemas.

**Required domain-agnostic coverage:** Data lineage, schema evolution, backward/forward compatibility, software versions, system evolution, change and retirement.

**Rationale:** The existing topics already differentiate which artifact or system is undergoing change.

**Next action:** Develop distinct lifecycle coverage under each owner with explicit links across contexts.

**Evidence required to close the content gap:** Traceable example linking schema revision, software API release, deployment and system lifecycle effects.


## Three explicit architectural decisions

**G-01 Mathematics breadth.** Should linear algebra, geometry and essential topology become explicit approved subject headings in Mathematics & Logic, or be covered through formal scope expansions of the existing headings? A new knowledge area is not automatically needed.

**G-04 General temporality.** Recommend a single canonical general discussion of time-related concepts in Models & Abstraction, clearly distinguished from physical SI measurements, clock hardware and distributed causal ordering. **This remains open**, corresponding to the B-11 exception.

**G-06 AI/ML.** Recommend treating a cross-area AI/ML index as an initial discovery path, while separately evaluating whether a dedicated knowledge area or additional named headings are needed for comprehensive foundational coverage. **No thirteenth area has been added.**

## Cross-domain coverage check

| Domain | Gap topics especially relevant |
| --- | --- |
| Network | G-04 time, G-05 signals, G-08 distributed consistency, G-07 data quality |
| Endpoint | G-02 numerical representation, G-03 formal properties, G-04 clocks, G-10 lifecycle |
| Application | G-03 formal methods, G-06 AI/ML, G-07 data quality, G-10 versioning |
| Cloud | G-04 timestamps, G-06 AI/ML, G-08 consistency, G-10 evolution |
| Industrial | G-02 measurement, G-04 time, G-05 signal processing, G-09 validation |
| IoT | G-04 timekeeping, G-05 sensing and conversion, G-07 data quality, G-10 device lifecycle |
| Identity | G-04 temporal validity, G-06 AI decision support, G-07 information quality, G-09 assurance |

## Authoring controls

- Keep **general concepts** in Fundamentals, security objectives and protections in Security Foundations, security practice in Operational Foundations, and vendor/domain implementations in the seven specialized domains.
- Distinguish scope from source validation: even a justified canonical location does **not** mean a subject is completed.
- Preserve the current 12-area / 109-heading baseline until explicit changes are approved.
- Do **not** add Knowledge Checks, Practical Assessments, quizzes, or grading.
- Use Markdown links to real canonical pages once those pages exist; do not manufacture uncreated article URLs or formally ratify graph predicates here.
- When coverage is judged insufficient, document an explicit expansion request instead of silently enlarging a heading's meaning.

## Authoritative reference starting points

- [ACM/IEEE-CS/AAAI CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/): coverage comparison, including artificial intelligence.
- [NIST Artificial Intelligence glossary](https://csrc.nist.gov/glossary/term/AI) and [Machine Learning glossary](https://csrc.nist.gov/glossary/term/machine_learning): terminology.
- [BIPM SI base unit second](https://www.bipm.org/en/si-base-units/second): time unit, not a complete theory of temporality.
- [Temporal Logic of Actions](https://www.microsoft.com/en-us/research/publication/the-temporal-logic-of-actions/): formal state/transition systems.
- [MIT OpenCourseWare Sampling](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/): sampling and aliasing.
- [W3C Data Quality Vocabulary](https://www.w3.org/TR/vocab-dqv/): accuracy, completeness, consistency and quality concepts.
- [SEBoK Verification](https://sebokwiki.org/wiki/Verification_%28glossary%29) and [Validation](https://sebokwiki.org/wiki/Validation_%28glossary%29): engineering meaning and distinction.

The references support technical coverage checks; none independently authorizes the editorial hierarchy.

## Current outcome

All ten cases have **working dispositions**. Seven have plausible existing homes and **still require actual authoring and verification**; three require explicit architectural approval of their scope/placement. General temporality is not declared resolved. The 12 approved areas and 109 approved subject headings remain unmodified.

[Fundamentals index](README.md) · [Governing architecture](ARCHITECTURE.md) · [Development plan](CURRICULUM-DEVELOPMENT-PLAN.md)
