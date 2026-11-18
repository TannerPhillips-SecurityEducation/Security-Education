# Fundamentals: Canonical Concept Boundary Decisions

**Version:** v0.2  
**Status:** Approved conceptual boundary guidance (20 groups); [model architecture adjudication](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md) assigned seven additional subjects subsequently authored and scoped-reviewed under [Wave F](WAVE-F-TECHNICAL-REVIEW-01.md). Twelve areas unchanged; comprehensive source verification and independent publication acceptance pending.  
**Baseline:** 12 knowledge areas; **109-heading historical snapshot, 116 current headings**, all 116 internally Reviewed (model-assisted) under Wave A–F.  
**Inputs:** [Original 20 overlaps and 10 open gaps](CONCEPT-OVERLAP-REVIEW.md), [canonical ownership crosswalk](CANONICAL-OWNERSHIP-REGISTER.md), and [governing architecture](ARCHITECTURE.md).

## Resolution method

A **general concept** and its **specialized implementation** can each have canonical explanations at different scopes. A shared word does not imply identical mechanisms; different words do not automatically imply separate concepts.

The canonical-owner distinctions below are **approved architectural guidance**, not fully verified technical definitions or a ratified graph-predicate vocabulary. They cite existing approved knowledge areas. No concept articles are implied to exist yet, and no Knowledge Checks or Practical Assessments belong in this reference.

## Twenty boundary decisions

| ID | Overlap | General canonical ownership | Distinction / contextual ownership |
| --- | --- | --- | --- |
| [B-01](#b-01) | Identity, identifiers, and authentication | Models & Abstraction: identity/distinction; Information & Data: identifier representations | Identity determines sameness; an identifier refers within a scope; authentication evaluates a claim under security mechanisms. Identity Knowledge owns implementation. |
| [B-02](#b-02) | Boolean logic, electronic gates, and software conditions | Mathematics & Logic: Boolean/predicate logic | Digital Systems owns gate circuits; Software & Programming owns language expression semantics. Logical truth, voltage, and truthiness are different representations. |
| [B-03](#b-03) | Data structures and computational structures | Information & Data: data structures and formats | Computation & Algorithms owns abstract data types, invariants, operations and complexity. A serialized structure does not dictate computational performance. |
| [B-04](#b-04) | Syntax, semantics, and encoding | Information & Data: symbols/encoding; Models & Abstraction: interpretation of conceptual models | Software & Programming owns programming-language grammar and execution meaning. Encoding maps symbols; syntax specifies valid forms; semantics provides interpretation. |
| [B-05](#b-05) | Measurement, signal conversion, and sampling | Scientific & Analytical Reasoning: measurement, procedures, calibration, uncertainty | Physical & Electrical Principles owns sensor transduction and conversion; Digital Systems owns timing hardware. Digitization alone is not a validated measurement. |
| [B-06](#b-06) | Observation, records, and evidence | Scientific & Analytical Reasoning: observation and evidence | Information & Data owns record structures and provenance; Operational Foundations owns security investigations. An observation is not automatically evidence for a particular claim. |
| [B-07](#b-07) | State, events, transitions, and system behavior | Models & Abstraction: general state, occurrence, transition concepts | Systems & Engineering owns dynamic system behavior; OS Principles owns process states; Distributed Systems owns replicated states. An event need not produce a distinct modeled state. |
| [B-08](#b-08) | Control, feedback, and industrial controllers | Systems & Engineering: general feedback and control | Physical & Electrical Principles owns actuation; Industrial Knowledge owns controllers and OT mechanisms. Feedback is one control strategy, not all control. |
| [B-09](#b-09) | Algorithmic and emergent complexity | Computation & Algorithms: computational complexity; Systems & Engineering: emergence/complexity | Asymptotic resource growth, implementation performance, and interaction-driven system complexity are not interchangeable. |
| [B-10](#b-10) | Probability, uncertainty, and confidence | Mathematics & Logic: probability/statistical models | Scientific & Analytical Reasoning owns epistemic confidence, uncertainty qualification and evidence limits; Measurement owns metrological uncertainty. |
| [B-11](#b-11) | Time, hardware clocks, and event ordering | Mathematics & Logic: units/duration; Models & Abstraction: modeled events | Digital Systems owns physical clocks; Distributed Systems owns event ordering and synchronization. General temporal-model concepts now have a canonical home in [Temporal Concepts and Models](models-abstraction/temporal-concepts-and-models.md), separately reviewed under Wave F. |
| [B-12](#b-12) | Software interfaces, APIs, and protocols | Software & Programming: software interfaces and contracts | Communication & Distributed Systems owns protocol/layering rules; Application Knowledge owns concrete APIs. An API contract and exchange protocol overlap but differ. |
| [B-13](#b-13) | Concurrency, threads, and coordination | Computation & Algorithms: concurrency, parallelism, synchronization | OS Principles owns process/thread mechanisms; Distributed Systems owns cross-node coordination under partial failure. Concurrency need not imply parallel execution. |
| [B-14](#b-14) | Drivers, buses, devices, and I/O | Digital Systems & Hardware: general I/O and buses/interfaces | Operating System Principles owns driver abstractions; Endpoint owns platform drivers. OS requests are not electrical bus operations themselves. |
| [B-15](#b-15) | Databases and cloud-managed services | Information & Data: generic databases, queries, persistence | Cloud Knowledge owns provider-managed database services and deployment-specific operations, without redefining generic database concepts. |
| [B-16](#b-16) | Reliability, availability, and security objectives | Systems & Engineering: reliability, failure, availability, resilience | Security Foundations owns availability as a security objective and security threats/controls. Reliability failures and malicious disruption may both affect availability. |
| [B-17](#b-17) | Scientific validation, engineering verification, software testing | Scientific & Analytical Reasoning: validation/falsification; Systems & Engineering: V&V | Software & Programming owns test techniques. Scientific hypothesis testing, requirement conformance, intended-use validation, and testing evidence differ. |
| [B-18](#b-18) | Human error, program errors, and hardware/system failures | Human & Sociotechnical Systems: human error; Systems & Engineering: faults/failure | Software & Programming owns exceptions and error handling; Physical/Hardware areas own physical failure mechanisms. Related failures do not imply individual blame. |
| [B-19](#b-19) | Identity, names, and addresses | Models & Abstraction: identity/distinction; Communication & Distributed Systems: naming/addressing | Information & Data owns identifier encoding; Network owns specific addressing systems. An address can act as a locator without defining persistent identity. |
| [B-20](#b-20) | Sensors, devices, and IoT/industrial systems | Physical & Electrical Principles: sensors, actuators; Digital Systems: components | IoT and Industrial domains own integrated connected/industrial implementations. A sensor component is not necessarily a full connected system. |

## Working examples and non-conflation tests

### B-01

**Identity, identifiers, and authentication:** A machine can retain identity after an IP address change; knowing its username is not proof of a claimant.

### B-02

**Boolean logic, electronic gates, and software conditions:** A∧B is formal; a CMOS gate has physical timing; a conditional expression has language-specific evaluation.

### B-03

**Data structures and computational structures:** A JSON array is a representation; a queue ADT specifies operations; a ring buffer can implement it.

### B-04

**Syntax, semantics, and encoding:** UTF-8 encodes '1+1'; grammar parses it; semantic rules determine its meaning.

### B-05

**Measurement, signal conversion, and sampling:** An ADC returns counts; calibration and a specified measurand establish interpretable temperature values.

### B-06

**Observation, records, and evidence:** A DNS-log entry records an observation; relevance to a threat hypothesis depends on context and corroboration.

### B-07

**State, events, transitions, and system behavior:** 'Connection established' can be an event; ESTABLISHED can be a protocol state; process state has a different context.

### B-08

**Control, feedback, and industrial controllers:** Thermostat feedback is a principle; a PLC is an implementation that may perform open- or closed-loop control.

### B-09

**Algorithmic and emergent complexity:** O(n) algorithmic behavior cannot by itself characterize the emergent failure behavior of a distributed system.

### B-10

**Probability, uncertainty, and confidence:** A confidence interval is not interchangeable with an analyst's qualitative 'high confidence'.

### B-11

**Time, hardware clocks, and event ordering:** Two nodes can assign conflicting wall-clock timestamps even when causal order is known.

### B-12

**Software interfaces, APIs, and protocols:** An HTTP-based API uses HTTP without being the entire HTTP protocol specification.

### B-13

**Concurrency, threads, and coordination:** A single-core event loop is concurrent; networked leader election requires distributed coordination.

### B-14

**Drivers, buses, devices, and I/O:** A system call reaches a driver, which may operate an interface and device.

### B-15

**Databases and cloud-managed services:** SQL predicate meaning is generic; managed service configuration and billing are provider-specific.

### B-16

**Reliability, availability, and security objectives:** A worn-out disk causes accidental outage; a DDoS attack affects service availability without disk failure.

### B-17

**Scientific validation, engineering verification, software testing:** A unit test checks specified cases; an acceptance review asks whether stakeholder needs are met.

### B-18

**Human error, program errors, and hardware/system failures:** An unclear procedure can trigger a misconfiguration, an exception, and a service failure in one causal chain.

### B-19

**Identity, names, and addresses:** A hostname can resolve to new IP addresses while the service remains the same logical resource.

### B-20

**Sensors, devices, and IoT/industrial systems:** A thermistor is a sensor; a thermostat or industrial transmitter combines more mechanisms.

## General temporality: owner and scoped article reviewed; full source verification remains (B-11; G-04)

**Canonical owner and scoped technical review now established.** F-03-11 [Temporal Concepts and Models](models-abstraction/temporal-concepts-and-models.md) owns general instants, intervals, durations and temporal ordering, supported by the [Wave F six-family review of that article](WAVE-F-TECHNICAL-REVIEW-01.md). Time *units* remain in Mathematics & Logic; hardware timing remains in Digital Systems; distributed causal-order algorithms remain in Communication & Distributed Systems. **B-11's owner-placement and initial content gap are resolved; complete source-passage verification and cross-domain acceptance remain open.** See [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks).

## Rules for future canonical authoring

1. State the scope of the general concept; do not rely on a specific operating system, provider, product, or security practice for its definition.
2. Give a genuine specialized mechanism its own scoped explanation, explicitly linked to the general one.
3. Make distinctions operationally meaningful using one discriminating example or counterexample.
4. Preserve approved knowledge-area names and historical subject-ID mappings. The current inventory is 116 headings; subject additions, merges, or renames require recorded adjudication rather than silent scope changes.
5. Link to actual canonical article URLs **only once those articles exist**; otherwise refer to the existing area inventory.
6. Review relationships for direction, assumptions, and context; the vocabulary of link types remains illustrative, not formally ratified.

## Primary references consulted for boundary terminology

- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final): digital identity proofing, authentication, federation.
- [RFC 3986: Uniform Resource Identifier](https://www.rfc-editor.org/rfc/rfc3986): identification, reference, and resource distinction.
- [BIPM VIM measurement definition](https://jcgm.bipm.org/vim/en/2.1.html): measurands, methods, and measurement conditions.
- [SEBoK System Validation](https://sebokwiki.org/wiki/System_Validation): V&V in systems engineering.
- [SEBoK System Requirements](https://sebokwiki.org/wiki/System_Requirements): requirement-specific V&V distinctions.
- [NIST Cyber-Physical Systems glossary](https://csrc.nist.gov/glossary/term/cyber_physical_systems): physical and computational integration.

These sources inform selected terms. The conceptual ownership boundaries were approved for this repository; external standards do not mandate this editorial taxonomy, and specific technical explanations still require evidence and review.

## Resolution status

- **20 of 20 groups mapped and approved as architectural boundaries:** general owners, contextual distinctions, and discriminating examples. The B-11 owner-placement decision is resolved, while comprehensive source and cross-domain verification remain open.
- **B-11 exception:** the formerly missing general-temporality canonical home and scoped explanation are established; complete source verification and publication acceptance remain open.
- **10 candidate gaps:** have separate working dispositions in the [Coverage Gap Decision Register](COVERAGE-GAP-DECISIONS.md); seven are assigned to existing headings for authoring, and three require architectural decisions.
- **Approved taxonomy:** untouched; no additional areas or subject headings.
- **Reference articles:** not yet written or validated.

[Fundamentals](README.md) · [Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Relationship conventions](../../RELATIONSHIPS.md)
