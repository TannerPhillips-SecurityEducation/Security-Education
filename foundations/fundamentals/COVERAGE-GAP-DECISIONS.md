# Fundamentals: Coverage Gap Decision Register

**Status:** Working architectural disposition v0.2; seven new headings Inventoried through [Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md), not yet authored or technically reviewed.  
**Baseline:** 12 knowledge areas unchanged; **116 current headings = 109 historical Reviewed articles + 7 new Inventoried subjects**. The earlier 109-heading snapshot remains in audit history.  
**Input:** [Concept Overlap and Coverage Review](CONCEPT-OVERLAP-REVIEW.md), [Canonical Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md), [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md).

## Decision rule

A subject is **covered by existing headings, pending authoring** when an approved heading has a credible canonical scope for that material. This is *placement coverage*, not completed or source-verified reference content. A subject **requires an architectural decision** when its scope or discoverable conceptual ownership cannot responsibly be assumed without an explicit choice.

## Disposition summary

| Disposition | Count | Cases |
| --- | ---: | --- |
| Existing canonical owners, depth/source verification still required | 7 | G-02, G-03, G-05, G-07, G-08, G-09, G-10 |
| Canonical subject placement assigned, article content pending | 3 | G-01, G-04, G-06 |
| New **Inventoried** headings added | 7 | 3 mathematics, 1 temporal model, 1 computer architecture, 2 AI/ML; no new knowledge area |
| Published canonical articles created by this register | 0 | None |

## Framework, Model & Architecture coverage pass (November 18, 2026)

The [Foundational Models, Frameworks & Architectures Audit 01](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) introduces an **evidence-backed review of 77 named technical models/frameworks/architectures** over the current 109-article snapshot. Its 14 FMA review cases are **candidate changes and deepening tasks**, not eleven new gaps, additional approved headings, or an automatic amendment to the ten G-01–G-10 cases below.

**Count clarification:** The **109 tracked subject headings are not fixed**. Changes can add, split, merge, rename or retire headings after recorded coverage/ownership analysis. The old 12-area/109-heading counts remain the **historical baseline for previous audits**, not a requirement to accommodate every new model within existing headings.

**Later adjudication:** [Architecture Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md) subsequently assigned G-01 to F-01-09/10/11, G-04 to F-03-11 and G-06 to F-07-10/11, and inventoried F-06-10 computer architecture models. **The original audit by itself did not approve those changes; the later recorded adjudication changed the inventory.**

## Ten coverage cases

### G-01: Linear algebra, geometry, topology

**Disposition:** **Canonical placement resolved**, new subjects F-01-09/10/11 Inventoried; explanatory content and technical review pending

**Canonical responsibilities:** Mathematics & Logic: Algebra and functions; Discrete mathematics; Graph theory.

**Required domain-agnostic coverage:** Vectors, matrices, transformations, coordinate geometry, continuity and elementary topology. Distinguish graph topology from general mathematical topology.

**Rationale:** Approved headings support some mathematical prerequisites, but do not guarantee coverage of these distinct topics.

**Next action:** Author and source-verify F-01-09 Linear Algebra and Vector Spaces, F-01-10 Geometry and Spatial Reasoning, and F-01-11 Topology and Continuity as distinct canonical subjects. No new area required.

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

**Disposition:** **Canonical placement resolved** at F-03-11 Temporal Concepts and Models; article and technical verification pending

**Canonical responsibilities:** Models & Abstraction: State/events/transitions (candidate general owner); Mathematics: Units and quantities; Digital Systems: Timing and clocks; Distributed Systems: Synchronization and coordination.

**Required domain-agnostic coverage:** Instants, intervals, durations, temporal ordering, simultaneity, timestamps, physical time scales, clock readings, event causality.

**Rationale:** Existing headings cover units and implementations but do not explicitly establish the general canonical theory of temporality. Boundary exception B-11 remains.

**Next action:** Author F-03-11 within Models & Abstraction; keep units, physical clocks and distributed causal-order mechanisms with their existing distinct owners.

**Evidence required to close the content gap:** A coherent comparison of duration, instant, timestamp and causal partial order, including unsynchronized clocks.

### G-05: Signal processing

**Disposition:** Covered by existing headings, pending authoring

**Canonical responsibilities:** Physical & Electrical Principles: Analog and digital signals; Waves and frequency; Signal conversion; Scientific Reasoning: Measurement.

**Required domain-agnostic coverage:** Frequency representation, filtering, sampling, quantization, noise, aliasing and reconstruction.

**Rationale:** The approved signals and conversion headings have clear ownership of these mechanisms.

**Next action:** Develop content under existing headings. Avoid claims of perfect reconstruction without assumptions.

**Evidence required to close the content gap:** A sampling/aliasing example explicitly identifying band-limit and sampling assumptions.

### G-06: Artificial intelligence and machine learning

**Disposition:** **Canonical placement resolved** at F-07-10 Artificial Intelligence Foundations and F-07-11 Machine Learning Foundations; content and source verification pending

**Canonical responsibilities:** Mathematics: Probability and statistics; Computation: Algorithms and Algorithm design; Information & Data: Data types, datasets, provenance; Human & Sociotechnical Systems: Decision-making.

**Required domain-agnostic coverage:** Symbolic reasoning vs learned models; training vs inference; supervised/unsupervised/reinforcement learning; loss, features, generalization, overfitting, evaluation, drift, limitations; planning and knowledge representation.

**Rationale:** CS2023 treats AI as a substantial distinct knowledge area. Distributed prerequisite topics in the existing twelve do not guarantee discoverable, complete AI/ML treatment.

**Next action:** Author distinct AI and machine-learning foundational articles under Computation & Algorithms, using the existing mathematics, data and sociotechnical prerequisites. A thirteenth area was not created.

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


## Three scoped canonical placements (content not yet verified)

**G-01 Mathematics breadth.** Three distinct subject headings (F-01-09/10/11) are now Inventoried in Mathematics & Logic. The mathematical depth and source-supported examples remain to be developed; no new area was required.

**G-04 General temporality.** F-03-11 Temporal Concepts and Models is now Inventoried in Models & Abstraction. The B-11 owner-placement question is resolved, but source-verified content and cross-domain alignment are still open.

**G-06 AI/ML.** F-07-10 Artificial Intelligence Foundations and F-07-11 Machine Learning Foundations are now Inventoried in Computation & Algorithms. AI is not defined as synonymous with ML. **No thirteenth area was added**; content depth and cross-domain completeness remain unverified.

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
- Preserve the **historical** 12-area/109-heading audit snapshot; the newly adjudicated **current inventory is 12 areas/116 headings**. Further changes require versioned rationale, cross-links and status reconciliation.
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

All ten cases have **working dispositions**. Seven retain plausible existing canonical homes requiring depth/source verification; **three now have newly inventoried canonical placement but still require articles and technical review**. General temporality's *owner* is assigned while its substantive coverage is not verified. The 12 approved areas remain unchanged; the current subject inventory contains **116 headings**.

[Fundamentals index](README.md) · [Governing architecture](ARCHITECTURE.md) · [Development plan](CURRICULUM-DEVELOPMENT-PLAN.md)
