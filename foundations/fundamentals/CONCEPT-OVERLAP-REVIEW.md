# Fundamentals: Concept Overlap and Coverage Review

**Status:** Working architectural review register, v0.1. No new knowledge areas, subject headings, or graph predicates are ratified by this document.

The approved baseline is 12 knowledge areas and 109 subject headings. The ownership boundaries below are **proposed decisions for review**. They are not evidence that the underlying canonical concept articles already exist.

## Twenty recurring concept-overlap groups

| Potential collision | Proposed general canonical home | Distinction to maintain |
| --- | --- | --- |
| Identity, identifiers, and authentication | [Identity and distinction](models-abstraction/README.md) | Identifiers are data representations; authentication and access are treated in Security Foundations and Identity Knowledge, not identical to logical identity. |
| Boolean logic, gates, and software conditions | [Boolean and predicate logic](mathematics-logic/README.md) | Digital Systems & Hardware covers circuit implementations; Software & Programming covers executable conditions. |
| Data structures and algorithmic structures | [Data structures and formats](information-data/README.md) | Computation & Algorithms covers abstract data types and operational cost, not a second generic format definition. |
| Syntax, semantics, and encoding | [Conceptual and formal models](models-abstraction/README.md) and [Symbols and encoding](information-data/README.md) | Representational symbols differ from meanings; programming language syntax and semantics is an applied specialization. |
| Measurement, signal conversion, and sampling | [Measurement](scientific-analytical-reasoning/README.md) | Physical & Electrical Principles covers physical signal mechanisms and conversion; Digital Systems & Hardware covers timing hardware. |
| Observation, records, and evidence | [Observation](scientific-analytical-reasoning/README.md) and [Evidence](scientific-analytical-reasoning/README.md) | Information & Data owns records and provenance; Operational Foundations owns applied security workflows. |
| State, events, and transitions | [State, events, and transitions](models-abstraction/README.md) | Systems & Engineering owns whole-system dynamics; Operating System Principles owns process-specific states. |
| Control, feedback, and industrial controllers | [Feedback and control](systems-engineering/README.md) | Physical & Electrical Principles owns actuation mechanisms; Industrial Knowledge owns ICS implementations. |
| Algorithm complexity and emergent complexity | [Complexity](computation-algorithms/README.md) and [Emergence and complexity](systems-engineering/README.md) | Separate computational resource-growth measures from nonlinear interactions of whole systems. |
| Probability and confidence | [Probability and statistics](mathematics-logic/README.md) | Scientific & Analytical Reasoning owns epistemic uncertainty and evidential confidence. |
| Time, clock hardware, and ordering | [Units and quantities](mathematics-logic/README.md) | Digital Systems & Hardware owns physical clock circuitry; Distributed Systems owns logical ordering. General temporality needs a coverage review. |
| APIs and communication protocols | [Software interfaces](software-programming/README.md) | Communication & Distributed Systems owns exchange protocols and layering; Application Knowledge owns concrete APIs. |
| Concurrency, threads, and distributed coordination | [Concurrency and parallelism](computation-algorithms/README.md) | Operating System Principles owns thread/process implementation; Distributed Systems owns cross-node coordination. |
| Drivers, buses, and input/output | [Buses and interfaces](digital-systems-hardware/README.md) | Operating System Principles owns driver abstractions; Endpoint Knowledge owns platform-specific implementations. |
| Databases and managed database services | [Databases and queries](information-data/README.md) | Cloud Knowledge describes provider-managed services, not a new generic database definition. |
| Reliability, availability, and security objectives | [Reliability and failure](systems-engineering/README.md) | Security Foundations owns security objectives; specialized domains apply engineering tradeoffs. |
| Scientific validation, engineering verification, software testing | [Validation and falsification](scientific-analytical-reasoning/README.md) and [Verification and validation](systems-engineering/README.md) | Scientific claim criticism, requirements conformance, and software test techniques are related but distinct. |
| Human errors, software errors, and hardware faults | [Human error](human-sociotechnical-systems/README.md) | Software & Programming owns exception/error handling; Systems & Engineering owns fault and failure models. |
| Identity, names, and addresses | [Identity and distinction](models-abstraction/README.md) | Information & Data owns identifier encodings; Communication & Distributed Systems owns locators, name binding, and resolution. |
| Devices, sensors, and IoT objects | [Sensors and actuators](physical-electrical-principles/README.md) | Digital Systems & Hardware owns component organization; Industrial and IoT domains own specific devices and deployments. |

**Boundary rule:** A term appearing in several subjects is not automatically a duplicate. The general concept and its distinct contextual mechanisms can each have legitimate canonical homes. The registers should explicitly link them instead of merging different mechanisms into a vague definition.

## Ten candidate coverage questions

These are **open questions**, not approved new sections.

| Candidate gap | Investigate within | Decision needed |
| --- | --- | --- |
| Linear algebra, geometry, topology | Mathematics & Logic | Review spatial, vector, matrix, geometric, and topological coverage under existing headings before adding any category. |
| Numerical methods and optimization | Mathematics & Logic; Computation & Algorithms | Check numerical error, approximation, convergence, and optimization distinctly from efficiency. |
| Formal methods and model checking | Mathematics & Logic; Models & Abstraction; Software & Programming | Distinguish formal proof, model checking, logical validity, engineering validation. |
| Time, temporality, and clocks | Mathematics & Logic; Models & Abstraction; Digital Systems; Distributed Systems | Clarify duration, timestamps, event ordering, and physical/logical clocks. |
| Signal processing | Physical & Electrical Principles | Check sampling, filtering, frequency analysis, and reconstruction. |
| Artificial intelligence and machine learning | Probability; Computation & Algorithms; Information & Data; Human Systems | Determine minimum domain-agnostic training, inference, and generalization coverage without assuming a thirteenth area. |
| Data quality and semantics | Information & Data; Scientific Reasoning | Check missingness, provenance, bias, representativeness, and semantic mismatch. |
| Distributed consistency and partial failure | Communication & Distributed Systems; Systems & Engineering | Clarify consistency models, failure assumptions, and ordering guarantees. |
| Scientific and engineering validation | Scientific Reasoning; Systems & Engineering; Software & Programming | Clarify experimental falsification, requirements verification, acceptance, and software testing. |
| Lifecycle evolution and versioning | Information & Data; Software & Programming; Systems & Engineering | Separate data, software, schema, and whole-system evolution and versioning. |

For every candidate, record one of three outcomes when reviewed: **covered by an existing approved heading**, **deferred with rationale**, or **requires separate architectural approval**. None of those dispositions has been formally chosen yet.

## Relationship safeguards

- Distinguish **kind-of**, **part-of**, **depends-on**, **represents**, **uses**, **applies-in**, and **is-evidence-for** where the context warrants. The words here are illustrative, **not a ratified predicate vocabulary**.
- Check direction, conditions, scope, and time before assigning a relationship.
- A folder hierarchy is navigational and does not itself assert an ontological parent-child relation.
- Distinguish formal models, measured realities, inferred explanations, and implementations.
- Link to real canonical articles when available. Currently, the above links resolve to the approved area inventories, not complete subject pages.
- Keep domain-specific authentication, incident response, OS/vendor mechanisms, and product descriptions outside Fundamentals.

## Review procedure

1. Confirm the proposed general owner against the [Governing Architecture](ARCHITECTURE.md).
2. Separate a genuine conceptual overlap from a useful contextual extension.
3. Check the [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) for matching heading responsibility and relationship targets.
4. Record the disposition in the authoring workflow without changing the approved taxonomy unless separately approved.
5. Update references and cross-links when substantive canonical articles are published.

[Fundamentals](README.md) · [Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
