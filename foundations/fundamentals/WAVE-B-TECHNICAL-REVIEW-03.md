# Wave B Technical Review: Batch 03

**Review date:** November 17, 2026  
**Scope:** Components and Interfaces; Architecture and Composition; Dependencies; State and Behavior.  
**Method:** Reopened all four canonical GitHub drafts; checked six material claim groups in each against the linked NASA, SEBoK, mathematics and modeling sources; independently recomputed their worked quantitative/state examples; inspected cross-subject boundaries; and fetched all distinct internal Markdown **file destinations** referenced by the four articles.  
**Disposition:** **24 material claim families reviewed.** All four articles pass a **scoped model-assisted technical review**, after one documented formalism clarification. This does **not** constitute exhaustive independent source validation, human peer review, certification, or final publication acceptance.

## Claim-to-source review ledger

### Components and Interfaces
[Reviewed article](systems-engineering/components-and-interfaces.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| CI-01 | Components are system-boundary-relative constituents, not universally fixed objects | [NASA Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/); distinction retained between chosen system-of-interest and decomposition |
| CI-02 | Function, responsibility and implementation need not map one-to-one | [NASA Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/); the climate-control allocation is an illustrative original model |
| CI-03 | Interfaces specify exchanges and context beyond mere connections | [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); boundary, endpoints, characteristics and change control are supported |
| CI-04 | Syntactic, semantic and behavioral compatibility are distinct | [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/) and conceptual article semantics; these labels are editorial explanatory distinctions, not a NASA-mandated three-class taxonomy |
| CI-05 | Fahrenheit/Celsius numerical mismatch shows type compatibility is insufficient | Independently computed `(68−32)×5/9 = 20`; accepting `68` as °C would change the physical interpretation even when the value parses |
| CI-06 | Interface contracts express conditional expectations, not implementation guarantees | NASA Interface Management; internal/external designation depends on system boundary; acceptance tests have scope limits |

### Architecture and Composition
[Reviewed article](systems-engineering/architecture-and-composition.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| AC-01 | System architecture expresses organization, relationships, constraints and environment | [SEBoK System Architecture Design Definition](https://sebokwiki.org/wiki/System_Architecture_Design_Definition); article does not equate an architecture with a single diagram |
| AC-02 | Functional, logical and physical architectures may represent distinct viewpoints | [NASA Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/); illustrative views are not newly approved knowledge categories |
| AC-03 | Composition is not automatically inverse to decomposition | [NASA Design Solution Definition](https://www.nasa.gov/reference/4-4-design-solution-definition/); component integration depends on interface/operational compatibility |
| AC-04 | Architecture and performance requirements constrain candidate compositions | NASA Logical Decomposition; 200 ms timing value is a **hypothetical requirement**, not empirical controller performance |
| AC-05 | Redundancy introduces tradeoffs and can retain common-cause failure | NASA Design Solution Definition; the two-sensor design comparison is illustrative and explicitly conditional |
| AC-06 | Model, integration, product verification and validation are different stages/claims | [NASA Product Realization](https://www.nasa.gov/reference/5-0-product-realization/); architecturally plausible design is not automatically a verified system |

### Dependencies
[Reviewed article](systems-engineering/dependencies.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| DP-01 | Dependency denotes stated, contextual reliance rather than all forms of relation | NASA Logical Decomposition and [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/); edge meaning is declared, not inferred from shape |
| DP-02 | Necessary, conditional and substitutable requirements have distinct logic | AND/OR requirements represented as illustrative engineering semantics; alternative resources can invalidate a naive single-path failure claim |
| DP-03 | Downstream propagation is conditional on behavioral and environmental assumptions | Original recorder/storage/power example; no unsupported numerical probability or guaranteed outage is asserted |
| DP-04 | Directed graph cycles and scheduling precedence must not be conflated with control feedback loops | MIT graph theory and model-specific semantics; DAG topological ordering by itself does not guarantee implementation feasibility |
| DP-05 | Critical-path example is arithmetically consistent under fixed-duration, finish-to-start, unlimited-resource assumptions | Recomputed A→B→D = `2+3+4=9`, A→C→D = `2+5+4=11`; earliest completion 11 time units |
| DP-06 | Graph reachability flags possible impact, not guaranteed disruption | NASA Logical Decomposition; actual failures depend on fallbacks, modes, timing and other assumptions |

### State and Behavior
[Reviewed article](systems-engineering/state-and-behavior.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| SB-01 | System state and observed status are distinct selected descriptions | [NASA System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/); observable output need not recover hidden physical state |
| SB-02 | State, inputs, outputs and transition rules are separable modeling elements | [NASA Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/); examples remain domain independent |
| SB-03 | Deterministic function notation differs from probabilistic/nondeterministic transition semantics | **Corrected:** `s[k+1]=F(s[k],u[k])` gives one successor for fixed inputs where F is defined; alternative formalisms need kernels/relations |
| SB-04 | Hysteresis controller's state trace follows the stipulated thresholds | Independently evaluated `OFF@17→ON`, `ON@20→ON`, `ON@23→OFF`, `OFF@20→OFF`; explicitly a toy input/output model |
| SB-05 | Invariant/safety/liveness statements apply to specified reachable models | [Formal model article](models-abstraction/conceptual-and-formal-models.md); modeled state membership does not prove real equipment cannot fail |
| SB-06 | Sampled-step indexing does not specify actual duration, concurrency or complete observability | NASA System Design Processes; general time/temporality G-04 remains unresolved |

## Technical correction before acceptance

**State and Behavior:** Clarified that `F` and `G` as written define **deterministic** state/output mappings over admitted arguments. Probabilistic systems may instead use stochastic transition kernels and nondeterministic systems relations or sets of successors. The previous text could suggest that the same deterministic notation represented all three without qualification.

The other three references passed the scoped review without requiring changes to their material technical claims. Their original examples are not attributed to NASA/SEBoK as published case studies.

## Numerical and trace verification

| Example | Recomputed result |
| --- | --- |
| `68 °F → °C` | 20 °C |
| Precedence network A(2), B(3), C(5), D(4) | Critical A→C→D = 11 time units; A→B→D = 9 |
| Hysteresis initial state `OFF`; input `[17,20,23,20]` °C; thresholds 18/22 °C | Post-step states: ON, ON, OFF, OFF |
| Invariant `state ∈ {OFF,ON}` for the stipulated two-state model | Holds by construction; physical failure not excluded |

## Link and source-review limits

The four articles contain **47 relative Markdown link occurrences** resolving to **16 distinct file destinations**. Each distinct destination was reopened through the GitHub contents interface: **16/16 found**. This check does not establish validity of URL fragments, external web availability, all other repository links, or the completeness of sources behind each statement.

The documented claim groups were checked against cited authoritative materials, and original examples against their own assumptions. Review scope is **Core claims checked**, not `Verified`. The audit is model-assisted; no independently commissioned human expert review is claimed.

## Architecture and acceptance boundaries

- **Components and Interfaces** owns constituent responsibilities and interaction contracts; **Architecture and Composition** owns system-wide structure and alternatives; **Dependencies** owns reliance/propagation models; **State and Behavior** owns whole-system evolution.
- General boundaries, abstract state concepts, graph theory and formal models remain in their existing canonical subject articles.
- All four are **Reviewed (model-assisted)**. **Published**, independent human review and full source verification remain open.
- The original **12 approved knowledge areas / 109 approved subject headings** are unchanged.
- **G-01** mathematics breadth, **G-04** general temporality and **G-06** AI/ML remain open architecture decisions. No new assessment content or mandatory ontology/predicate standard has been added.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
