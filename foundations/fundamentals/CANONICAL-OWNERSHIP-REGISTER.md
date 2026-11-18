# Fundamentals: Canonical Ownership & Relationship Register

**Status:** Working architectural register v1.6. The **12 area identities and 109 subject headings are approved**; the particular subject scope explanations and relationships here are **proposed for review**, not newly ratified canonical definitions.

This register connects the existing subject inventory to the [governing architecture](ARCHITECTURE.md). It establishes the intended **general canonical responsibility** for each approved heading and an illustrative relationship to another **existing approved heading**.

## Reading this register

- **Approved subject:** Exact heading from the connected GitHub inventory, unchanged.
- **Proposed canonical scope:** The general concepts and mechanisms this subject is expected to own.
- **Related approved subject:** A descriptive, directed relationship to another existing heading. The relation words are illustrative and are **not** a ratified graph-predicate vocabulary.
- **Links:** Live direct links now point to **fifty-five Reviewed (model-assisted) articles** and **four Wave C Batch 01 Drafts**; headings without articles still link to their approved area indexes. Direct references do not mean independent human peer review or final publication.
- **Granularity:** One heading may require multiple articles, and a single well-scoped explanation can serve more than one heading. Do not assume 109 headings equal 109 indivisible concepts.

Only **domain-agnostic knowledge** belongs in Fundamentals. Security-specific objectives and protections belong to Security Foundations, applied security operations to Operational Foundations, and technical implementations to the appropriate specialized domain. No assessments are included.

See [Coverage Gap Decision Register](COVERAGE-GAP-DECISIONS.md) for the ten gaps' working dispositions and remaining scope decisions. See [Concept Overlap and Coverage Review](CONCEPT-OVERLAP-REVIEW.md) for unresolved ownership collisions and candidate gaps. The [Canonical Concept Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md) supplies 20 working non-conflation rules and concrete examples, with a general-temporality coverage exception.

## 01. Mathematics & Logic (8 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Numbers and numerical systems** | [Reviewed canonical article](mathematics-logic/numbers-and-numerical-systems.md) · Abstract number sets, arithmetic, order, and positional notation | *represented digitally by* → [Bits and bytes](information-data/bits-and-bytes.md) |
| **Sets and relations** | [Reviewed canonical article](mathematics-logic/sets-and-relations.md) · Membership, subsets, and formally defined binary relations | *applied as conceptual* → [Relationships](models-abstraction/relationships.md) |
| **Boolean and predicate logic** | [Reviewed canonical article](mathematics-logic/boolean-and-predicate-logic.md) · Truth functions, predicates, quantification, entailment, and logical validity | *implemented electronically through* → [Digital logic](digital-systems-hardware/digital-logic.md) |
| **Algebra and functions** | [Reviewed canonical article](mathematics-logic/algebra-and-functions.md) · Mappings, variables, expressions, equations, and function composition | *supports mathematical formulation of* → [Algorithms](computation-algorithms/README.md) |
| **Discrete mathematics** | [Reviewed canonical article](mathematics-logic/discrete-mathematics.md) · Finite structures, counting, recurrences, and mathematical induction | *supports construction of* → [Algorithm design](computation-algorithms/README.md) |
| **Graph theory** | [Reviewed canonical article](mathematics-logic/graph-theory.md) · Vertices, edges, paths, connectivity, and hierarchical structures | *models* → [Dependencies](systems-engineering/dependencies.md) |
| **Probability and statistics** | [Reviewed canonical article](mathematics-logic/probability-and-statistics.md) · Random variables, distributions, and mathematical statistical inference | *informs epistemic* → [Uncertainty and confidence](scientific-analytical-reasoning/uncertainty-and-confidence.md) |
| **Units and quantities** | [Reviewed canonical article](mathematics-logic/units-and-quantities.md) · Quantities, dimensions, units, scaling, and conversion | *enables* → [Measurement](scientific-analytical-reasoning/measurement.md) |

## 02. Scientific & Analytical Reasoning (8 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Observation** | [Reviewed canonical article](scientific-analytical-reasoning/observation.md) · Acquisition of phenomena, observer scope, and observational limitations | *can supply* → [Evidence](scientific-analytical-reasoning/evidence.md) |
| **Measurement** | [Reviewed canonical article](scientific-analytical-reasoning/measurement.md) · Operational quantification, instrument calibration, and measurement uncertainty | *uses* → [Units and quantities](mathematics-logic/units-and-quantities.md) |
| **Evidence** | [Reviewed canonical article](scientific-analytical-reasoning/evidence.md) · Relevance, sufficiency, provenance, and support for claims | *may require* → [Data provenance and lifecycle](information-data/data-provenance-and-lifecycle.md) |
| **Hypotheses and experiments** | [Reviewed canonical article](scientific-analytical-reasoning/hypotheses-and-experiments.md) · Testable claims, experimental controls, confounders, and replication | *used to investigate* → [Causality and correlation](scientific-analytical-reasoning/causality-and-correlation.md) |
| **Deduction, induction, and abduction** | [Reviewed canonical article](scientific-analytical-reasoning/deduction-induction-abduction.md) · Deductive entailment, inductive generalization, and abductive explanation | *draws on formal* → [Boolean and predicate logic](mathematics-logic/boolean-and-predicate-logic.md) |
| **Causality and correlation** | [Reviewed canonical article](scientific-analytical-reasoning/causality-and-correlation.md) · Association, causal effects, interventions, and confounding | *uses* → [Probability and statistics](mathematics-logic/probability-and-statistics.md) |
| **Uncertainty and confidence** | [Reviewed canonical article](scientific-analytical-reasoning/uncertainty-and-confidence.md) · Known limits, estimates, epistemic uncertainty, and calibrated confidence | *partly quantified using* → [Probability and statistics](mathematics-logic/probability-and-statistics.md) |
| **Validation and falsification** | [Reviewed canonical article](scientific-analytical-reasoning/validation-and-falsification.md) · Empirical claim criticism, refutation, replication, and model revision | *distinct from engineering* → [Verification and validation](systems-engineering/verification-and-validation.md) |

## 03. Models & Abstraction (10 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Entities and attributes** | [Reviewed canonical article](models-abstraction/entities-and-attributes.md) · General entities, properties, values, and type-versus-instance distinctions | *represented in data by* → [Datasets, records, fields, and values](information-data/datasets-records-fields-and-values.md) |
| **Identity and distinction** | [Reviewed canonical article](models-abstraction/identity-and-distinction.md) · Sameness, difference, reference, and persistence through change | *specialized for communication in* → [Addressing and naming](communication-distributed-systems/README.md) |
| **Relationships** | [Reviewed canonical article](models-abstraction/relationships.md) · General associations, direction, cardinality, and context qualification | *formalized in* → [Sets and relations](mathematics-logic/sets-and-relations.md) |
| **Boundaries** | [Reviewed canonical article](models-abstraction/boundaries.md) · Inclusion, exclusion, separation, limitations, and interface distinctions | *used to delimit* → [Systems and subsystems](systems-engineering/systems-and-subsystems.md) |
| **Abstraction** | [Reviewed canonical article](models-abstraction/abstraction.md) · Selection and suppression of detail to support models and multiple views | *specialized as* → [Hardware abstraction](digital-systems-hardware/README.md) |
| **Classification** | [Reviewed canonical article](models-abstraction/classification.md) · Criteria for categories, classes, membership, and differentiation | *organized into* → [Ontologies and taxonomies](models-abstraction/ontologies-and-taxonomies.md) |
| **Ontologies and taxonomies** | [Reviewed canonical article](models-abstraction/ontologies-and-taxonomies.md) · Conceptual categories, kinds, and typed semantic relations | *may be constrained by* → [Schemas](models-abstraction/schemas.md) |
| **Schemas** | [Reviewed canonical article](models-abstraction/schemas.md) · Representation constraints, fields, structures, and admissible values | *applied in* → [Data structures and formats](information-data/data-structures-and-formats.md) |
| **State, events, and transitions** | [Reviewed canonical article](models-abstraction/state-events-and-transitions.md) · General state descriptions, events, and transitions between conditions | *specialized as system* → [State and behavior](systems-engineering/state-and-behavior.md) |
| **Conceptual and formal models** | [Reviewed canonical article](models-abstraction/conceptual-and-formal-models.md) · Models, assumptions, formalization, abstraction fidelity, and interpretation | *evaluated through* → [Validation and falsification](scientific-analytical-reasoning/validation-and-falsification.md) |

## 04. Physical & Electrical Principles (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Matter and energy** | [Draft canonical article](physical-electrical-principles/matter-and-energy.md) · Physical matter, energy, transfer, and constraints on physical systems | *constrains* → [Computing components](digital-systems-hardware/computing-components.md) |
| **Electricity** | [Draft canonical article](physical-electrical-principles/electricity.md) · Charge, voltage, current, resistance, and electrical power | *governs* → [Electrical circuits](physical-electrical-principles/electrical-circuits.md) |
| **Electrical circuits** | [Draft canonical article](physical-electrical-principles/electrical-circuits.md) · Behavior of interconnected passive and active electrical elements | *forms the physical basis of* → [Electronics](physical-electrical-principles/README.md) |
| **Electronics** | Semiconductors, switching, amplification, and electronic component functions | *enables* → [Digital logic](digital-systems-hardware/digital-logic.md) |
| **Analog and digital signals** | Physical continuous signals versus sampled or discrete representations | *processed through* → [Signal conversion](physical-electrical-principles/README.md) |
| **Waves and frequency** | Oscillation, frequency, phase, wavelength, and propagation | *supports* → [Transmission and signaling](communication-distributed-systems/README.md) |
| **Sensors and actuators** | Transduction between physical phenomena and actionable system inputs/outputs | *used in system* → [Feedback and control](systems-engineering/feedback-and-control.md) |
| **Signal conversion** | Sampling, quantization, analog-digital and digital-analog conversion | *supports data capture for* → [Measurement](scientific-analytical-reasoning/measurement.md) |
| **Physical control mechanisms** | Actuation and regulation of physical processes | *generalized by* → [Feedback and control](systems-engineering/feedback-and-control.md) |

## 05. Information & Data (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Symbols and encoding** | [Reviewed canonical article](information-data/symbols-and-encoding.md) · Symbol systems, mappings, character codes, and representations | *realized digitally as* → [Bits and bytes](information-data/bits-and-bytes.md) |
| **Bits and bytes** | [Reviewed canonical article](information-data/bits-and-bytes.md) · Binary digits, byte grouping, and digital representation units | *grounded in numerical* → [Numbers and numerical systems](mathematics-logic/numbers-and-numerical-systems.md) |
| **Information theory** | [Reviewed canonical article](information-data/information-theory.md) · Entropy, information content, and theoretical communication constraints | *constrains* → [Communication channels](communication-distributed-systems/README.md) |
| **Data types** | [Reviewed canonical article](information-data/data-types.md) · Value domains, types, constraints, and interpretation | *used in* → [Programming languages](software-programming/README.md) |
| **Datasets, records, fields, and values** | [Reviewed canonical article](information-data/datasets-records-fields-and-values.md) · Collections, records, field granularity, and field values | *models properties of* → [Entities and attributes](models-abstraction/entities-and-attributes.md) |
| **Data structures and formats** | [Reviewed canonical article](information-data/data-structures-and-formats.md) · Logical containers, structured formats, serialization, and data representations | *distinct from operational* → [Computational data structures](computation-algorithms/README.md) |
| **Metadata** | [Reviewed canonical article](information-data/metadata.md) · Descriptions of structure, semantics, context, and lineage | *supports* → [Data provenance and lifecycle](information-data/data-provenance-and-lifecycle.md) |
| **Databases and queries** | [Reviewed canonical article](information-data/databases-and-queries.md) · Data persistence, logical models, query operations, and retrieval concepts | *uses* → [Data structures and formats](information-data/data-structures-and-formats.md) |
| **Data provenance and lifecycle** | [Reviewed canonical article](information-data/data-provenance-and-lifecycle.md) · Origin, lineage, transformation, retention, and change history | *supports evaluation of* → [Evidence](scientific-analytical-reasoning/evidence.md) |

## 06. Digital Systems & Hardware (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Digital logic** | [Reviewed canonical article](digital-systems-hardware/digital-logic.md) · Physical switching systems implementing logical and sequential behavior | *realizes* → [Boolean and predicate logic](mathematics-logic/boolean-and-predicate-logic.md) |
| **Computing components** | [Draft canonical article](digital-systems-hardware/computing-components.md) · Hardware organization of processors, memory, peripherals, and interconnects | *is a type of* → [Systems and subsystems](systems-engineering/systems-and-subsystems.md) |
| **Processors and instruction sets** | Processor execution organization, instruction encoding, and ISA models | *is a target of* → [Compilation and interpretation](software-programming/README.md) |
| **Memory and storage** | Volatile and nonvolatile storage media, latency, and memory hierarchy | *managed abstractly by* → [Memory management](operating-system-principles/README.md) |
| **Buses and interfaces** | Physical/logical device interconnects and signal transfer | *accessed using* → [Drivers and devices](operating-system-principles/README.md) |
| **Input/output** | Hardware interactions with peripherals and physical environments | *exposed through* → [System calls](operating-system-principles/README.md) |
| **Timing and clocks** | Clock generation, cycles, physical timing, and timing domains | *supports* → [Scheduling](operating-system-principles/README.md) |
| **Firmware** | Hardware-oriented software used for initialization and control | *participates in* → [System initialization](operating-system-principles/README.md) |
| **Hardware abstraction** | Interfaces hiding low-level implementation differences from software | *specializes general* → [Abstraction](models-abstraction/abstraction.md) |

## 07. Computation & Algorithms (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Computability** | Computational models, decidability, and the limits of computable problems | *sets limits on* → [Algorithms](computation-algorithms/README.md) |
| **Algorithms** | Defined procedures transforming inputs into outputs | *realized through* → [Programming languages](software-programming/README.md) |
| **Algorithm design** | Construction strategies, invariants, correctness, and choice of procedures | *evaluated using* → [Complexity](computation-algorithms/README.md) |
| **Complexity** | Theoretical asymptotic time/space growth of procedures | *distinct from system-wide* → [Emergence and complexity](systems-engineering/emergence-and-complexity.md) |
| **Computational data structures** | Abstract data types, operation costs, and implementation tradeoffs | *represented through* → [Data structures and formats](information-data/data-structures-and-formats.md) |
| **Iteration and recursion** | Repeated and recursively defined computation, termination, and base cases | *expressed using* → [Programming paradigms](software-programming/README.md) |
| **Concurrency and parallelism** | Overlapping versus simultaneous computational progress | *implemented through* → [Processes and threads](operating-system-principles/README.md) |
| **Synchronization** | Mutual exclusion, ordering, races, deadlock, and coordination of computations | *specialized across nodes in* → [Synchronization and coordination](communication-distributed-systems/README.md) |
| **Computational efficiency** | Practical performance costs, locality, profiling, and resource tradeoffs | *compared with asymptotic* → [Complexity](computation-algorithms/README.md) |

## 08. Software & Programming (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Programming languages** | Software language forms, grammars, execution constructs, and ecosystems | *express* → [Algorithms](computation-algorithms/README.md) |
| **Syntax and semantics** | Programming grammar, syntactic structure, semantic meaning, and interpretation | *uses* → [Symbols and encoding](information-data/symbols-and-encoding.md) |
| **Programming paradigms** | Imperative, declarative, functional, object, and event-driven styles | *structure* → [Algorithms](computation-algorithms/README.md) |
| **Compilation and interpretation** | Translation, parsing, intermediate forms, linking, and interpretation | *targets* → [Processors and instruction sets](digital-systems-hardware/README.md) |
| **Runtime environments** | Execution libraries, services, managed runtimes, and memory lifetimes | *interacts with* → [Kernels](operating-system-principles/README.md) |
| **Modules and dependencies** | Packages, imports, modularity, versioning, and dependency management | *specializes* → [Dependencies](systems-engineering/dependencies.md) |
| **Software interfaces** | Function, API, ABI, and compatibility contracts between software components | *specializes* → [Components and interfaces](systems-engineering/components-and-interfaces.md) |
| **Error handling** | Software exceptions, error signaling, propagation, and recovery | *distinct from system-level* → [Reliability and failure](systems-engineering/reliability-and-failure.md) |
| **Testing and software lifecycle** | Software construction, testing, releasing, maintenance, and retirement | *specializes* → [System lifecycle](systems-engineering/system-lifecycle.md) |

## 09. Operating System Principles (10 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Kernels** | Privileged coordination of execution, resource protection, and OS abstraction | *builds on* → [Hardware abstraction](digital-systems-hardware/README.md) |
| **System calls** | Protected OS interfaces and kernel transitions for requested operations | *exposes* → [Software interfaces](software-programming/README.md) |
| **Processes and threads** | Process isolation, address spaces, execution threads, and states | *realizes* → [Concurrency and parallelism](computation-algorithms/README.md) |
| **Scheduling** | Allocation of processor time among runnable work | *influences* → [Computational efficiency](computation-algorithms/README.md) |
| **Memory management** | Virtual addressing, allocation, page translation, and memory protection | *manages* → [Memory and storage](digital-systems-hardware/README.md) |
| **Filesystems** | Persistent file/directory organization, access paths, and metadata | *implements structured storage for* → [Data structures and formats](information-data/data-structures-and-formats.md) |
| **Drivers and devices** | Operating-system abstractions for hardware device operations | *uses* → [Buses and interfaces](digital-systems-hardware/README.md) |
| **Execution contexts** | Privilege modes, environments, address spaces, and executing state | *specializes* → [State, events, and transitions](models-abstraction/state-events-and-transitions.md) |
| **System initialization** | Boot sequence, firmware handoff, kernel start, and service initialization | *follows* → [Firmware](digital-systems-hardware/README.md) |
| **Resource management** | Allocation, quotas, accounting, and contention for shared system resources | *constrains* → [Computational efficiency](computation-algorithms/README.md) |

## 10. Communication & Distributed Systems (9 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Communication models** | Generic senders, receivers, channels, messages, and exchange patterns | *applies* → [Relationships](models-abstraction/relationships.md) |
| **Transmission and signaling** | Encoding and propagation of signals carrying information | *uses* → [Analog and digital signals](physical-electrical-principles/README.md) |
| **Communication channels** | Communication paths and constraints including medium, capacity, and noise | *constrained by* → [Information theory](information-data/information-theory.md) |
| **Protocols and layering** | Communication conventions, protocol rules, state, layering, and encapsulation | *complements interface contracts in* → [Software interfaces](software-programming/README.md) |
| **Addressing and naming** | Names, locators, address scopes, binding, and resolution | *extends reference concepts in* → [Identity and distinction](models-abstraction/identity-and-distinction.md) |
| **Latency and throughput** | Delay, data rates, queueing, jitter, and performance measures | *uses* → [Units and quantities](mathematics-logic/units-and-quantities.md) |
| **Reliability and ordering** | Message loss, duplication, delivery guarantees, acknowledgements, and ordering | *extends system* → [Reliability and failure](systems-engineering/reliability-and-failure.md) |
| **Distributed state** | Replication, consistency, clocks, and partial-failure uncertainty | *specializes* → [State, events, and transitions](models-abstraction/state-events-and-transitions.md) |
| **Synchronization and coordination** | Coordination among autonomous processes through ordering, clocks, and agreement | *extends computational* → [Synchronization](computation-algorithms/README.md) |

## 11. Systems & Engineering (11 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Systems and subsystems** | [Reviewed canonical article](systems-engineering/systems-and-subsystems.md) · Systems of interest, environments, nested wholes, and subsystem organization | *defined using* → [Boundaries](models-abstraction/boundaries.md) |
| **Components and interfaces** | [Reviewed canonical article](systems-engineering/components-and-interfaces.md) · System components, responsibilities, interfaces, and their contracts | *instantiates* → [Relationships](models-abstraction/relationships.md) |
| **Architecture and composition** | [Reviewed canonical article](systems-engineering/architecture-and-composition.md) · Composition, decomposition, architectural views, patterns, and tradeoffs | *represented through* → [Conceptual and formal models](models-abstraction/conceptual-and-formal-models.md) |
| **Dependencies** | [Reviewed canonical article](systems-engineering/dependencies.md) · Necessary relationships, constraints, propagation, and critical paths | *represented with* → [Graph theory](mathematics-logic/graph-theory.md) |
| **State and behavior** | [Reviewed canonical article](systems-engineering/state-and-behavior.md) · Whole-system states, outputs, changes, invariants, and dynamic behavior | *applies* → [State, events, and transitions](models-abstraction/state-events-and-transitions.md) |
| **Feedback and control** | [Reviewed canonical article](systems-engineering/feedback-and-control.md) · Feedback loops, sensors, controllers, stability, and control objectives | *applies physical* → [Physical control mechanisms](physical-electrical-principles/README.md) |
| **Emergence and complexity** | [Reviewed canonical article](systems-engineering/emergence-and-complexity.md) · Whole-system emergent behavior and nonlinearity | *distinct from algorithmic* → [Complexity](computation-algorithms/README.md) |
| **Reliability and failure** | [Reviewed canonical article](systems-engineering/reliability-and-failure.md) · Faults, failures, availability, redundancy, maintainability, and recovery | *quantifiable using* → [Probability and statistics](mathematics-logic/probability-and-statistics.md) |
| **Requirements** | [Reviewed canonical article](systems-engineering/requirements.md) · Stakeholder needs, functional/quality specifications, and traceability | *evaluated through* → [Verification and validation](systems-engineering/verification-and-validation.md) |
| **Verification and validation** | [Reviewed canonical article](systems-engineering/verification-and-validation.md) · Conformance to requirements versus fitness for intended use | *distinct from empirical* → [Validation and falsification](scientific-analytical-reasoning/validation-and-falsification.md) |
| **System lifecycle** | [Reviewed canonical article](systems-engineering/system-lifecycle.md) · Conception, design, operation, maintenance, evolution, and retirement | *specialized for software in* → [Testing and software lifecycle](software-programming/README.md) |

## 12. Human & Sociotechnical Systems (8 headings)

| Approved subject | Proposed canonical responsibility | Illustrative relationship to another approved subject |
| --- | --- | --- |
| **Human cognition and perception** | [Reviewed canonical article](human-sociotechnical-systems/human-cognition-and-perception.md) · Human attention, memory, perception, interpretation, and cognitive limits | *shapes* → [Human-computer interaction](human-sociotechnical-systems/human-computer-interaction.md) |
| **Decision-making** | [Reviewed canonical article](human-sociotechnical-systems/decision-making.md) · Choice under constraints, incomplete knowledge, uncertainty, and goals | *informed by* → [Evidence](scientific-analytical-reasoning/evidence.md) |
| **Human-computer interaction** | [Reviewed canonical article](human-sociotechnical-systems/human-computer-interaction.md) · People interacting with software, devices, and whole technical systems | *evaluated for* → [Usability and accessibility](human-sociotechnical-systems/usability-and-accessibility.md) |
| **Usability and accessibility** | [Reviewed canonical article](human-sociotechnical-systems/usability-and-accessibility.md) · Inclusive, usable, effective, and accessible human-system experiences | *informs* → [Requirements](systems-engineering/requirements.md) |
| **Human error** | [Reviewed canonical article](human-sociotechnical-systems/human-error.md) · Human mistakes, slips, and organizational conditions contributing to error | *may affect* → [Reliability and failure](systems-engineering/reliability-and-failure.md) |
| **Collaboration and communication** | [Reviewed canonical article](human-sociotechnical-systems/collaboration-and-communication.md) · Human coordination, collaboration, shared language, and information exchange | *structured by* → [Organizational structures](human-sociotechnical-systems/organizational-structures.md) |
| **Organizational structures** | [Reviewed canonical article](human-sociotechnical-systems/organizational-structures.md) · Roles, responsibilities, authority, governance, and organizational relationships | *shape* → [Requirements](systems-engineering/requirements.md) |
| **Ethics and professional responsibilities** | [Reviewed canonical article](human-sociotechnical-systems/ethics-and-professional-responsibilities.md) · Professional obligations, harms, accountability, and responsible conduct | *informs human* → [Decision-making](human-sociotechnical-systems/decision-making.md) |

## Canonical article integration

The original **109 approved subject headings and 12 area assignments** remain unchanged. There are **55 Reviewed (model-assisted)** articles, including the [Wave B Batch 05 48-family audit](WAVE-B-TECHNICAL-REVIEW-05.md), plus **four substantive Wave C Batch 01 Drafts**. All 26 Wave A and 28 Wave B headings are internally Reviewed; Digital Logic is the additional Reviewed pilot in Wave C. Human expert review, complete source validation and final publication acceptance remain outstanding. The crosswalk is navigational and conceptual, not a ratified formal knowledge-graph schema.

## Register integrity

| Measure | Value |
| --- | ---: |
| Approved knowledge areas covered | 12 |
| Approved subject headings preserved | 109 |
| Illustrative directed relationships | 109 |
| Canonical articles created by this register | 0 |
| Formal subject-ID schema or graph engine introduced | 0 |

## Ownership-review procedure

1. Confirm whether the proposed general canonical responsibility is precise, independent of vendors and domains, and within the approved area scope.
2. Check whether overlapping terms denote the **same concept** or genuinely distinct mechanisms or contextual implementations.
3. Review the relationship's target, direction, context, and phrasing. Do not infer taxonomic *is-a* solely from directory location.
4. Consult the [20 overlap groups and 10 candidate gap questions](CONCEPT-OVERLAP-REVIEW.md) before creating a new canonical document.
5. Replace broad area-index links with precise subject links after meaningful, source-verified reference articles exist.

The register **does not** demonstrate that the subject explanations or review gates have been completed.

[Fundamentals](README.md) · [Knowledge relationships](../../RELATIONSHIPS.md)
