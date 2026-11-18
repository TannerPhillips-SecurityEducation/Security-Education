# Fundamentals | Model, Framework & Architecture Adjudication 01

**Date:** November 18, 2026  
**Status:** Working inventory architecture implemented; **new subject content remains Inventoried / Not reviewed**, not authored or Published.  
**Inputs:** [Foundational Models Audit 01](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md), [Coverage Gap Decisions](COVERAGE-GAP-DECISIONS.md), [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md), [Concept Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md), and original canonical subject articles.  
**Governance:** The 109-heading inventory was never a fixed target. Keep twelve currently approved **navigation areas**. Expand or contract individual subjects only where concept boundaries support it; do not claim this is a new formal ontology or graph-predicate set.

## 1. Adjudicated subject-inventory change

| Measure | Pre-change historical snapshot | After this working inventory change |
| --- | ---: | ---: |
| Knowledge areas | 12 | **12, unchanged** |
| Canonical articles with scoped model-assisted review | 109 | **109, unchanged** |
| Additional inventoried headings without canonical articles | 0 | **7** |
| Total currently tracked subject headings | 109 | **116** |
| Independently human peer-reviewed / Published articles | 0 | **0** |

This is a **subject-inventory architecture change**, not a claim that newly scoped subjects have been authored or peer-reviewed. All preceding Wave A–E audit denominators remain historical observations, not an automatic **116/116 Reviewed** assertion. Administrative F-XX-YY identifiers are tracking keys, not ontological primitives.

### Seven distinct subjects added to the working inventory

| New ID | Knowledge area and scoped subject | Why existing owners were insufficient | Governing source orientation | Boundaries |
| --- | --- | --- | --- | --- |
| **F-01-09** | Mathematics & Logic: **Linear Algebra and Vector Spaces** | Elementary algebra mentions matrices but does not develop vector spaces, bases, linear maps, rank, eigenstructure or matrix models as a coherent subject | [MIT 18.06 Linear Algebra](https://www.mit.edu/~18.06/) | Existing [Algebra and Functions](mathematics-logic/algebra-and-functions.md) owns elementary algebraic relationships; this subject owns linear structures, maps and assumptions |
| **F-01-10** | Mathematics & Logic: **Geometry and Spatial Reasoning** | Coordinate systems, geometry of distance/angle, geometric transformations and spatial reasoning deserve an explicit canonical home instead of being assumed inside graph theory | [MIT mathematics: Geometry & Topology](https://math.mit.edu/academics/undergrad/subjects/189x.php) | Owns spatial/geometric relations, not graph connectivity or all continuous-topological properties |
| **F-01-11** | Mathematics & Logic: **Topology and Continuity** | The structural meaning of topological spaces, continuity, connectedness and neighborhoods is not equivalent to a graph topology or spatial coordinates | [MIT 18.901 Intro to Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/) | Distinguish topological connectedness from graph connectivity, and topology from geometric distance/angle |
| **F-03-11** | Models & Abstraction: **Temporal Concepts and Models** | Existing events/state and hardware/distributed-clock articles do not establish one general home for instants, intervals, durations, orderings and timestamp interpretation | [Maintaining Knowledge About Temporal Intervals (1983)](https://urresearch.rochester.edu/institutionalPublicationPublicView.action?institutionalItemVersionId=10115); [State, Events and Transitions](models-abstraction/state-events-and-transitions.md) | General time representation only; SI time units, hardware clocks, network time, and causal event ordering remain in respective existing homes |
| **F-06-10** | Digital Systems & Hardware: **Computer Architecture Models** | Processor/ISA and hardware-component articles explain individual mechanisms but lack a discoverable treatment comparing stored-program and Harvard organizations, Flynn classifications, and levels of computer architecture | [MIT 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) | Focus on abstract hardware organization and architecture comparison; [Processors and Instruction Sets](digital-systems-hardware/processors-and-instruction-sets.md) owns detailed ISA/implementation distinction |
| **F-07-10** | Computation & Algorithms: **Artificial Intelligence Foundations** | Planning, agents, search and knowledge representation are not reducible to general algorithm design or statistical learning | [CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/) | Core AI concepts, models, reasoning and intelligent-agent formulation; no vendor products, no security AI methodology, no requirement that AI = ML |
| **F-07-11** | Computation & Algorithms: **Machine Learning Foundations** | Learning from data, fitting and evaluating models, generalization and distribution shift constitute a distinct mechanism family | [CS2023 Artificial Intelligence coverage](https://csed.acm.org/knowledge-areas/); [Probability and Statistics](mathematics-logic/probability-and-statistics.md) | Owns computational learning paradigm and training/inference mechanisms; math owns probability and optimization prerequisites, data area owns datasets/provenance, not one article per neural architecture |

**Architectural acceptance of a heading does not imply acceptance of its eventual technical content.** All seven remain **Inventoried**, with no Markdown article body claimed or missing file link fabricated.

## 2. Adjudication of all fourteen original review cases

| FMA ID | Outcome | Canonical location / decision |
| --- | --- | --- |
| FMA-01 | **Add one heading** | F-01-09 Linear Algebra and Vector Spaces |
| FMA-02 | **Add two distinct headings** | F-01-10 Geometry and Spatial Reasoning; F-01-11 Topology and Continuity |
| FMA-03 | **Add one heading** | F-03-11 Temporal Concepts and Models, separating general time from physical clocks and causal ordering |
| FMA-04 | **Add two distinct headings** | F-07-10 Artificial Intelligence Foundations; F-07-11 Machine Learning Foundations |
| FMA-05 | **Deepen existing coverage** | [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md) and [State, Events, and Transitions](models-abstraction/state-events-and-transitions.md), with bounded UML/SysML/Petri-net examples; do not add a heading per notation |
| FMA-06 | **Deepen existing coverage** | [Architecture and Composition](systems-engineering/architecture-and-composition.md), emphasizing architecture vs description per ISO/IEC/IEEE 42010:2022 |
| FMA-07 | **Add one heading** | F-06-10 Computer Architecture Models |
| FMA-08 | **Deepen existing coverage** | [Protocols and Layering](communication-distributed-systems/protocols-and-layering.md) / [Communication Models](communication-distributed-systems/communication-models.md); contrast OSI with the Internet protocol suite, not normative layering mandates |
| FMA-09 | **Deepen existing coverage** | [Distributed State](communication-distributed-systems/distributed-state.md), [Synchronization and Coordination](communication-distributed-systems/synchronization-and-coordination.md), and F-03-11 temporal concepts; formal limits on CAP and consensus progress |
| FMA-10 | **Deepen existing coverage** | [Measurement](scientific-analytical-reasoning/measurement.md) and [Uncertainty and Confidence](scientific-analytical-reasoning/uncertainty-and-confidence.md); JCGM VIM/GUM applicability |
| FMA-11 | **Deepen existing coverage** | [Databases and Queries](information-data/databases-and-queries.md), [Data Provenance and Lifecycle](information-data/data-provenance-and-lifecycle.md), and [Metadata](information-data/metadata.md); ER/relational and PROV |
| FMA-12 | **Deepen existing coverage** | [Human Cognition and Perception](human-sociotechnical-systems/human-cognition-and-perception.md), [Decision-Making](human-sociotechnical-systems/decision-making.md), and [Human Error](human-sociotechnical-systems/human-error.md); no universal human performance formula |
| FMA-13 | **Deepen existing coverage** | [System Lifecycle](systems-engineering/system-lifecycle.md) and [Verification and Validation](systems-engineering/verification-and-validation.md); distinguish 15288 processes from the system lifecycle itself |
| FMA-14 | **Deepen existing coverage** | [Feedback and Control](systems-engineering/feedback-and-control.md) and [Physical Control Mechanisms](physical-electrical-principles/physical-control-mechanisms.md); Fourier/PID as conditional models, not ontology roots |

**Dispositions:** 5 review cases result in **7 newly inventoried subjects**; the other 9 lead to deeper treatment within existing canonical owners. No existing reviewed article is deleted, merged or retitled. No thirteenth area or security-specific framework is introduced.

## 3. Resolution of historical coverage questions

- **G-01 Mathematics breadth: canonical *placement* resolved**, content remains unwritten for F-01-09/10/11. Distinguish linear, geometric and topological structures; graph connectivity is a separate notion.
- **G-04 General temporality: canonical *placement* resolved** at F-03-11. The old B-11 boundary exception remains relevant as a **content/verification issue**, not a missing conceptual owner. Physical clock implementation and distributed happens-before remain independently owned.
- **G-06 AI/ML: canonical *placement* resolved** at F-07-10/11, while mathematical foundations, data governance and sociotechnical effects keep their existing canonical homes. Completeness across symbolic and learning-based AI is **not** yet verified.
- **Other G-02/03/05/07/08/09/10**: existing-location dispositions retained; further depth work is tracked without pretending the prior audits verified every framework.

## 4. Contraction decision

The six candidate overlap pairs examined in [Audit 01](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md#51-candidates-for-contraction-not-automatic-deletion) remain **distinct enough to retain** on current evidence. In particular, observation ≠ measurement ≠ evidence; general state/transition semantics ≠ a system-engineering behavior model; information representation ≠ computational data structures; and physical actuation constraints ≠ abstract feedback-control models.

**No consolidation is adopted in this pass.** Contraction remains allowed in future when duplicate-content evidence, canonical ownership and safe link/ID migrations support it. Neither the historical count 109 nor the new working count 116 is a target to defend.

## 5. Implementation and editorial controls

1. [Mathematics & Logic](mathematics-logic/README.md), [Models & Abstraction](models-abstraction/README.md), [Digital Systems & Hardware](digital-systems-hardware/README.md) and [Computation & Algorithms](computation-algorithms/README.md) carry the seven additional **Inventoried** headings, without links to nonexistent article files.
2. [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) must separately show 109 historically Reviewed + seven Inventoried, total 116; [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) must show those owners and relationships without asserting publication.
3. [Fundamentals index](README.md) and [Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) distinguish prior Wave A–E 109/109 review outcomes from current 116-heading inventory.
4. New articles require source-led definitions, distinctions, worked examples and review, rather than automatically inheriting earlier evidence. Before publishing, audit technical depth, internal/external links, cross-domain coverage and independent qualified human acceptance.
5. A model name in a source, scanner or table does **not** mean the model is adequately explained. The original 77-item lexical audit remains a **109-article historical sample**.

## 6. Source authorities and precise limits

- [MIT Linear Algebra](https://www.mit.edu/~18.06/) covers matrices, transformations, vector spaces and eigenvalue problems.
- [MIT 18.901 Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/) distinguishes topological continuity and connectedness from geometric metric notions.
- [MIT Geometry & Topology curriculum](https://math.mit.edu/academics/undergrad/subjects/189x.php) illustrates geometry and topology as related but distinct mathematical subjects.
- [Allen, *Maintaining Knowledge About Temporal Intervals*](https://urresearch.rochester.edu/institutionalPublicationPublicView.action?institutionalItemVersionId=10115) provides a historically significant temporal-interval reasoning model, not one universal theory of physical time.
- [ACM/IEEE-CS/AAAI CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/) identifies AI as a recognized computing knowledge area; it is **curricular precedent**, not a directive to add a thirteenth repository area.
- [MIT 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) anchors general hardware organization, instruction and memory models.
- [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) is for **architecture descriptions**, not a universal architecture methodology; [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) addresses lifecycle **processes**, not mandatory lifecycle stages.

These references support **architecture-level differentiation**. Full clause-by-clause source review, independent peer review, and source-verified teaching articles remain future tasks.

[Fundamentals](README.md) · [Inventory change policy](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control) · [Original audit](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) · [Development register](DEVELOPMENT-VERIFICATION-REGISTER.md)
