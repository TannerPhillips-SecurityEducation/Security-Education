# Fundamentals: Canonical Concept Boundary Decisions

**Version:** v0.1  
**Status:** Working ownership resolutions for architectural review; not complete technical reference articles or a change to the approved taxonomy.  
**Baseline:** 12 approved knowledge areas and 109 approved subject headings.  
**Inputs:** [Original 20 overlaps and 10 open gaps](CONCEPT-OVERLAP-REVIEW.md), [canonical ownership crosswalk](CANONICAL-OWNERSHIP-REGISTER.md), and [governing architecture](ARCHITECTURE.md).

## Resolution method

A **general concept** and its **specialized implementation** can each have canonical explanations at different scopes. A shared word does not imply identical mechanisms; different words do not automatically imply separate concepts.

The canonical-owner descriptions below are **working editorial decisions**, not newly ratified concept definitions or graph predicates. They cite existing approved knowledge areas. No concept articles are implied to exist yet, and no Knowledge Checks or Practical Assessments belong in this reference.

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
| [B-11](#b-11) | Time, hardware clocks, and event ordering | Mathematics & Logic: units/duration; Models & Abstraction: modeled events | Digital Systems owns physical clocks; Distributed Systems owns event ordering and synchronization. General temporality lacks an adequately established canonical home. |
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

## Open exception: General temporality (B-11)

**Partially resolved.** Time *units* belong in Mathematics & Logic; hardware timing belongs in Digital Systems; event/order semantics in Models & Abstraction and Communication & Distributed Systems. Those distinctions do **not** establish where a complete domain-agnostic concept of *time and temporality* belongs. Retain the time gap in the [ten candidate coverage questions](CONCEPT-OVERLAP-REVIEW.md), without creating a new area.

## Rules for future canonical authoring

1. State the scope of the general concept; do not rely on a specific operating system, provider, product, or security practice for its definition.
2. Give a genuine specialized mechanism its own scoped explanation, explicitly linked to the general one.
3. Make distinctions operationally meaningful using one discriminating example or counterexample.
4. Preserve approved knowledge-area names and all 109 subject headings. A decision does not rename folders or change their ownership by fiat.
5. Link to actual canonical article URLs **only once those articles exist**; otherwise refer to the existing area inventory.
6. Review relationships for direction, assumptions, and context; the vocabulary of link types remains illustrative, not formally ratified.

## Primary references consulted for boundary terminology

- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final): digital identity proofing, authentication, federation.
- [RFC 3986: Uniform Resource Identifier](https://www.rfc-editor.org/rfc/rfc3986): identification, reference, and resource distinction.
- [BIPM VIM measurement definition](https://jcgm.bipm.org/vim/en/2.1.html): measurands, methods, and measurement conditions.
- [SEBoK System Validation](https://sebokwiki.org/wiki/System_Validation): V&V in systems engineering.
- [SEBoK System Requirements](https://sebokwiki.org/wiki/System_Requirements): requirement-specific V&V distinctions.
- [NIST Cyber-Physical Systems glossary](https://csrc.nist.gov/glossary/term/cyber_physical_systems): physical and computational integration.

These sources inform selected terms. The full set of working ownership decisions is an **editorial architecture proposal**, not a claim that an external standard mandates this taxonomy.

## Resolution status

- **20 of 20 groups mapped:** working general owners, contextual distinctions, and discriminating examples.
- **B-11 exception:** general temporality remains an open coverage decision.
- **10 candidate gaps:** remain open until separately dispositioned.
- **Approved taxonomy:** untouched; no additional areas or subject headings.
- **Reference articles:** not yet written or validated.

[Fundamentals](README.md) · [Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Relationship conventions](../../RELATIONSHIPS.md)
