# Fundamentals: Frameworks, Models & Architectures Review 01

**Review date:** November 18, 2026  
**Disposition:** **Model-grounded coverage and architecture review; recommendations pending subject-inventory adoption.**  
**Current inventory:** Twelve approved navigational knowledge areas, 109 tracked canonical subject articles; **109 is a historical/current snapshot, not a fixed number**.  
**Repository evidence:** [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [77-item lexical ledger](NAMED-MODEL-LEXICAL-LEDGER-01.md) · [CI run](https://github.com/TannerPhillips-SecurityEducation/Security-Education/actions/runs/44279824463)  
**Scope boundary:** General technical, scientific, computational, and sociotechnical foundations. Specialized security models go in [Security Foundations](../security-foundations/README.md); execution of security workflows goes in [Operational Foundations](../operational-foundations/README.md).

## 1. Executive findings

The existing corpus already explains many foundational **concepts and mechanisms** in substantial detail. Its weak point is not simply that model names are missing: explanations are sometimes **disconnected from established named models, formal representations, architectures and source-defined limits**, which reduces discoverability and makes intellectual lineage harder to see.

**Do not invert that finding into “add one article per named model.”** Several frameworks are methodology, domain-specific architectural styles, teaching heuristics, or illustrations that do not deserve independent canonical Fundamentals subjects. Other missing subjects may require distinct mathematical or semantic treatment regardless of which popular model names appear.

The present **109-heading inventory may expand or contract** when justified. In particular, G-01 mathematics breadth, G-04 general temporality, and G-06 AI/ML remain open architecture decisions. The twelve approved area identities remain the present navigation baseline; changing them requires a separate decision.

## 2. Evidence and limits

### 2.1 Automated named-model diagnostic

A read-only [Python scanner](tools/audit_named_models.py) examined **109 canonical subject Markdown files across all 12 existing knowledge areas**, outside fenced code blocks, using 77 chosen model/framework/architecture names and aliases. A corrected second run normalizes common Unicode apostrophes and dashes. Its recorded results:

| Measure | Result |
| --- | ---: |
| Canonical articles scanned | **109** |
| Approved navigation areas scanned | **12** |
| Named external/model concepts sampled | **77** |
| Names with a lexical match in one or more articles | **38** |
| Names with a match in the intended area | **36** |
| Names with no literal alias match in the sample | **39** |

**Interpretation:** These counts measure selected **word/alias presence only**. They do **not** measure conceptual coverage, technical correctness, source verification, framework adoption, completeness, or whether a given model belongs in Fundamentals. A cited source can count as a hit; an accurately explained unnamed mechanism can count as a nonmatch. The earlier run had 35 lexical hits; correcting punctuation matching increased that figure to 38, demonstrating why raw absence counts must not drive architecture decisions.

The [full 77-item evidence ledger](NAMED-MODEL-LEXICAL-LEDGER-01.md) records candidate source class, area, matched article counts, and example file basenames, so another reader can reproduce or dispute any observation.

### 2.2 Direct content inspection

A model-assisted reading pass sampled **18 articles** across the twelve knowledge areas, including [Algebra and Functions](mathematics-logic/algebra-and-functions.md), [Measurement](scientific-analytical-reasoning/measurement.md), [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md), [Signal Conversion](physical-electrical-principles/signal-conversion.md), [Information Theory](information-data/information-theory.md), [Computing Components](digital-systems-hardware/computing-components.md), [Computability](computation-algorithms/computability.md), [Programming Paradigms](software-programming/programming-paradigms.md), [Kernels](operating-system-principles/kernels.md), [Protocols and Layering](communication-distributed-systems/protocols-and-layering.md), [Architecture and Composition](systems-engineering/architecture-and-composition.md), [Human Cognition and Perception](human-sociotechnical-systems/human-cognition-and-perception.md), [Electrical Circuits](physical-electrical-principles/electrical-circuits.md), [Physical Control Mechanisms](physical-electrical-principles/physical-control-mechanisms.md), [System Lifecycle](systems-engineering/system-lifecycle.md), [Decision-Making](human-sociotechnical-systems/decision-making.md), [Human Error](human-sociotechnical-systems/human-error.md), and [Communication Models](communication-distributed-systems/communication-models.md).

**Direct examples of meaningful existing depth:**

- The [Computability](computation-algorithms/computability.md) article explicitly distinguishes Turing machines and the **Church–Turing thesis**, including why the thesis is not a mathematical theorem establishing every physical system's capability. The original lexical scanner missed the en-dash spelling; the corrected scanner recognized it.
- [Electrical Circuits](physical-electrical-principles/electrical-circuits.md) develops the resistor equation `v=iR`, KCL/KVL and their lumped-circuit limits. It is inaccurate to claim that the physics of Ohm's law is missing merely because the literal phrase is not present.
- [Signal Conversion](physical-electrical-principles/signal-conversion.md) explains sampling, the Nyquist frequency, aliasing, reconstruction assumptions and error limits, even without a named standalone “Nyquist-Shannon theorem” section.
- [Information Theory](information-data/information-theory.md) already treats Shannon entropy, mutual information and channel capacity with stated model assumptions.
- [Architecture and Composition](systems-engineering/architecture-and-composition.md) already distinguishes architecture from diagrams and develops multiple views; an ISO 42010 cross-reference would improve conceptual grounding rather than automatically require a new architecture article.
- [Measurement](scientific-analytical-reasoning/measurement.md) already uses VIM vocabulary and traceability and discusses uncertainty; the source gap is **more explicit GUM measurement-model grounding**, not an absence of measurement theory.
- [Human Error](human-sociotechnical-systems/human-error.md) discusses slips, mistakes, violations and system conditions without making a “Swiss cheese model” citation its basis; the model could deepen comparative treatment but is not evidence that the article is empty.

The 18-article check was **not** an exhaustive manual reading of every sentence in all 109 articles and does not confer new Reviewed or Verified status.

## 3. Critical distinctions between knowledge structures

| Type | Core question | General example | Do **not** confuse with |
| --- | --- | --- | --- |
| **Principle / law** | What relation, constraint or regularity applies under defined conditions? | Kirchhoff constraints | An unconditional law outside its applicability domain |
| **Formal model** | What structures, states, operators and inference rules are defined? | Finite-state automaton, Turing machine | A direct observation of a physical system |
| **Statistical/explanatory model** | What relationships or distributions are postulated? | Causal graphs, Markov models | Proof of causation or certainty |
| **Reference architecture** | What abstract responsibilities/interfaces/partitions organize systems? | OSI reference model | A mandated implementation stack |
| **Architecture description standard** | How should architectures be described and viewpoints related? | ISO/IEC/IEEE 42010 | The architecture itself or a prescribed design method |
| **Modeling language / notation** | How are structural, behavioral or semantic claims represented? | UML, SysML | A guarantee that a model matches reality |
| **Engineering process framework** | How are engineering activities and evidence organized? | ISO/IEC/IEEE 15288 | A universal sequence of lifecycle phases |
| **Heuristic / teaching model** | What mental organization is useful for reasoning? | Testing pyramid, some design mnemonics | A universal technical standard or theorem |
| **Implementation pattern** | How is a concrete mechanism assembled in a class of systems? | MVC architecture | An independent foundational ontological category |

The distinction matters for two official standards. [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) explicitly distinguishes **architecture** from **architecture description** and does not prescribe specific architecting methods. [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) supplies a systems lifecycle-process framework but does not mandate one lifecycle model or methodology. These are different, compatible scopes.

## 4. Twelve-area review matrix

| Existing knowledge area | Named items mentioned / sampled | Evidence-informed assessment | Recommended direction |
| --- | ---: | --- | --- |
| Mathematics & Logic | 5 / 6 | Algebra, logic and graph theory have real coverage; linear algebra has only limited scope and topology is dispersed. | **Consider new explicit subjects** for linear algebra and potentially geometry/topology (G-01); preserve existing subjects unless genuine overlap is proven |
| Scientific & Analytical Reasoning | 5 / 6 | VIM vocabulary and experimental reasoning appear; a dedicated GUM uncertainty-model reference is not named. | Deepen [Measurement](scientific-analytical-reasoning/measurement.md) with JCGM GUM scope, propagation, assumptions and decision rules |
| Models & Abstraction | 3 / 7 | Formal transitions and semantics are substantively explained, but Petri nets, UML, SysML and abstract interpretation are not named by the selected aliases. | Deepen formal-model family comparisons; **consider a discoverable modeling formalisms subject** only if existing conceptual/formal models becomes overloaded |
| Physical & Electrical Principles | 2 / 6 | Ohm's relation, Kirchhoff laws and sampling are explained; absence of names does not mean missing mechanics. | Add source-grounded comparative context for Fourier analysis, feedback/controller models and electromagnetic applicability, at the appropriate depth |
| Information & Data | 4 / 5 | Shannon information and provenance are represented; entity–relationship modeling not named. | Add relational/entity–relationship and PROV model distinctions to existing canonical information/data and database articles |
| Digital Systems & Hardware | 2 / 6 | Hardware responsibilities and ISA concepts are treated, but von Neumann, Harvard and Flynn reference architectures are not named in the sample. | Prioritize **computer architectural models and contrasts**; evaluate a distinct architecture subject if a single existing article cannot own the depth |
| Computation & Algorithms | 4 / 7 | Turing machines, the Church–Turing thesis, asymptotics and concurrency appear; lambda calculus, CSP and RAM cost models are unnamed. | Deepen computability and concurrency comparisons; reserve added subjects for irreducibly distinct formal treatments |
| Software & Programming | 3 / 7 | Paradigms, type/semantics and design contracts are treated; MVC, SOLID and testing pyramid are not in the alias sample. | Add **illustrative linked design models selectively**, not one permanent Fundamentals heading per software heuristic |
| Operating System Principles | 4 / 5 | Kernel architectures, VM, copy-on-write and POSIX are present; explicit process-lifecycle name is absent. | Add named-model examples where useful; no immediate extra OS heading justified |
| Communication & Distributed Systems | 4 / 8 | Layering, messages, ordering and distributed state have meaningful depth; OSI/TCP-IP models and CAP are not explicitly named by the scan. | Compare OSI reference versus Internet protocol-suite layering; explain CAP, consistency and impossibility **with assumptions** |
| Systems & Engineering | 2 / 7 | Architecture/views, lifecycle, reliability and verification appear, but ISO 42010, ISO 15288 and model-based systems engineering are unnamed. | Prioritize named standards grounding and the distinction between architecture, architecture description, viewpoints and lifecycle processes |
| Human & Sociotechnical Systems | 0 / 7 | The sampled human cognition/decision/error articles are substantive despite no exact alias matches to seven selected models. | Add comparative coverage of cognitive load, signal detection, interaction and systems-oriented human error **without reducing people to one model** |

**Area counts are lexical diagnostics, not coverage scores or performance rankings.** Relevance and editorial decisions require article-level review.

## 5. Model-grounded candidate changes (not yet adopted)

These are **change candidates**, not approvals, new root directories, or a commitment to produce a particular total subject count.

| Review ID | Candidate change | Justification / source orientation | Preferred action |
| --- | --- | --- | --- |
| FMA-01 | Linear algebra and vector-space models | [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) treats matrix operations, vector spaces, linear transformations and eigenstructure beyond current Algebra and Functions depth. This is existing G-01. | **Consider adding a Mathematics & Logic subject** |
| FMA-02 | Geometry, topology and spatial relations | G-01; topology and geometrical structure cannot be equated with graph topology alone. | **Consider adding or explicitly splitting scope** after distinguishing geometric vs network usage |
| FMA-03 | General time and temporal models | G-04: temporal order, duration, clock readings, timestamps, intervals, causal order and uncertainty have separate concepts. | **Consider adding a canonical Models & Abstraction subject** with physical and distributed time cross-links |
| FMA-04 | Statistical learning and AI/ML model families | G-06; [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/) includes AI among computing knowledge areas; the Fundamentals corpus has no approved explicit AI/ML subject inventory. | **Evaluate one or more new subjects or a new area by separate architectural decision** |
| FMA-05 | Modeling languages and formal behavioral formalisms | [OMG UML 2.5.1](https://www.omg.org/spec/UML), [OMG SysML](https://www.omg.org/sysml/), automata, Petri nets, model checking and different representation types. | **Deepen existing Models & Abstraction, consider a separate subject only if needed** |
| FMA-06 | Architecture description / viewpoints | [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) distinguishes architecture and its descriptions. | **Deepen Architecture and Composition first**, then assess whether separate ownership is warranted |
| FMA-07 | Computer architecture models | Stored-program, von Neumann/Harvard arrangements, Flynn classification, memory hierarchy and ISA-versus-microarchitecture. | **Consider a Digital Systems & Hardware architecture subject**; compare alternatives accurately |
| FMA-08 | Communications reference models | [ISO/IEC 7498-1:1994](https://www.iso.org/standard/20269.html) is the OSI reference model, not a physical implementation specification; [RFC 1122](https://www.rfc-editor.org/info/rfc1122/) describes the Internet protocol suite's layering. | **Deepen Protocols and Layering and Communication Models** before adding a heading |
| FMA-09 | Distributed-system impossibility and consistency | Lamport happens-before, consensus impossibility, linearizability, qualified CAP discussion. | **Deepen Distributed State and Synchronization/Coordination**, linked to temporal canonical treatment |
| FMA-10 | Metrological measurement models | [JCGM VIM](https://www.bipm.org/en/doi/10.59161/jcgm200-2012), [GUM](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e); versioned supplements/amendments must be checked when used. | **Deepen Measurement and Uncertainty and Confidence**, do not create a duplicate metrology division |
| FMA-11 | Provenance and relational model comparisons | [W3C PROV-O](https://www.w3.org/TR/prov-o/), relational/entity–relationship modeling, data provenance versus source integrity. | **Deepen Data Provenance, Databases, Metadata**, canonical source per distinction |
| FMA-12 | Human performance models | Cognitive load, signal detection, action/feedback models, human-error barriers and sociotechnical context; scope varies by original model. | **Deepen existing Human & Sociotechnical subjects**; add heading only if depth genuinely needs a distinct owner |
| FMA-13 | System lifecycle and process architecture | [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) names life-cycle processes without prescribing one sequence; V-model is an illustrative engineering model. | **Deepen System Lifecycle and Verification/Validation** |
| FMA-14 | Control-system and physical models | Fourier, Nyquist-Shannon, feedback loops and plant dynamics; PID is one controller family, not a universal architecture. | **Deepen existing Physical & Electrical and Systems & Engineering**, avoid control-model proliferation |

### 5.1 Candidates for contraction, not automatic deletion

The permission to **contract** matters as much as expansion. Test these pairs, but preserve their distinctions unless a genuine duplicate explanation is documented:

| Pair | Why not merge automatically |
| --- | --- |
| [Observation](scientific-analytical-reasoning/observation.md), [Measurement](scientific-analytical-reasoning/measurement.md), [Evidence](scientific-analytical-reasoning/evidence.md) | Sensing, quantified determination and claim-relative support are not the same |
| [State, Events, and Transitions](models-abstraction/state-events-and-transitions.md) and [State and Behavior](systems-engineering/state-and-behavior.md) | General state-transition models versus system-engineering behavior explanations |
| [Data Structures and Formats](information-data/data-structures-and-formats.md) and [Computational Data Structures](computation-algorithms/computational-data-structures.md) | Representation/storage formats versus abstract data types and computational operations |
| [Physical Control Mechanisms](physical-electrical-principles/physical-control-mechanisms.md) and [Feedback and Control](systems-engineering/feedback-and-control.md) | Physical plant/actuator constraints versus system-level feedback structure |
| [Architecture and Composition](systems-engineering/architecture-and-composition.md) and [Systems and Subsystems](systems-engineering/systems-and-subsystems.md) | Organizational principles and composition versus boundary-relative whole/part concepts |
| [Communication Models](communication-distributed-systems/communication-models.md) and [Collaboration and Communication](human-sociotechnical-systems/collaboration-and-communication.md) | Machine/protocol exchange contracts versus sociotechnical coordination and meaning |

**Current finding:** None of these six candidate pairings justifies immediate deletion, merging, or status inheritance from the existing evidence alone. Real contractions should occur only after a detailed duplicate-content comparison, retained canonical owner selection, redirect/cross-link design, and review of the resulting article.

## 6. Suggested execution order and review gates

1. **Resolve structural gaps first:** G-01 mathematics breadth; G-04 general temporality; G-06 foundational AI/ML. Because **109 is flexible**, assess new subjects/splits without forcing them into overloaded existing articles.
2. **Close terminology/source gaps within existing subjects:** Prioritize GUM/VIM, ISO 42010/15288, OSI versus RFC 1122, named computing architectures, formal-model families and validated human-factors models.
3. **Compare actual content before merging:** Inspect all sections, examples, sources, unique mechanisms, boundaries and cross-links; perform semantic rather than keyword-only deduplication.
4. **Adjudicate each change with evidence:** Mark *deepen, add, split, merge, retain, retire, outside scope*; record source grounding, conceptual owner, affected article/area path, scope caveats and disposition.
5. **Update canonical inventory only after the decision is recorded:** Revise counts, subject IDs/aliases, area indexes, relationships, development states, coverage tracker and cross-domain references together.
6. **Technical acceptance remains separate:** Source-level verification, cross-domain consistency, external link freshness and qualified human review still remain open as in the original seven publication gates.

**No automatic amendments have been made to the 109 subject files or the 12 area inventories in this audit.** The method, evidence, findings and change candidates are published for architectural adjudication. The 109 count is explicitly **not fixed**.

## 7. Source register (representative primary references, not all claims audited)

- [BIPM / JCGM 200:2012, International Vocabulary of Metrology](https://www.bipm.org/en/doi/10.59161/jcgm200-2012).
- [BIPM / JCGM 100:2008, Guide to the Expression of Uncertainty in Measurement](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e). Check [BIPM's publication list](https://www.bipm.org/en/committees/jc/jcgm/publications/) for later amendments and relevant supplements.
- [MIT OpenCourseWare, 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/).
- [ACM/IEEE-CS/AAAI CS2023 Computer Science Curricula](https://csed.acm.org/).
- [ISO/IEC 7498-1:1994 OSI Basic Reference Model](https://www.iso.org/standard/20269.html).
- [IETF RFC 1122 Internet Host Communication Layers](https://www.rfc-editor.org/info/rfc1122/).
- [ISO/IEC/IEEE 42010:2022 Architecture Description](https://www.iso.org/standard/74393.html).
- [ISO/IEC/IEEE 15288:2023 System Life Cycle Processes](https://www.iso.org/standard/81702.html).
- [OMG Unified Modeling Language 2.5.1](https://www.omg.org/spec/UML).
- [OMG SysML, including v2 specification](https://www.omg.org/sysml/).
- [W3C PROV-O Provenance Ontology](https://www.w3.org/TR/prov-o/).
- [Foundational distributed event-ordering paper](https://lamport.org/pubs/time-clocks.pdf).

**Source limitations:** Official landing pages establish scope, version, abstract and/or standards status where accessible; they do not establish passage-level verification of every individual claim in this report. ISO documents may require licensed full-text access. This is a model-assisted architecture audit, not independent peer review or publication acceptance.

[Fundamentals](README.md) · [Architecture and living inventory rule](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control) · [Full lexical evidence](NAMED-MODEL-LEXICAL-LEDGER-01.md) · [Coverage decisions](COVERAGE-GAP-DECISIONS.md) · [Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
