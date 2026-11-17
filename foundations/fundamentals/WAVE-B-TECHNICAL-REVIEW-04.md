# Wave B Technical Review: Batch 04

**Review date:** November 17, 2026  
**Scope:** Feedback and Control; Emergence and Complexity; Reliability and Failure; Requirements; Verification and Validation; System Lifecycle.  
**Method:** Second-pass review of the six GitHub articles; comparison of material claim groups with MIT OpenCourseWare, NASA Systems Engineering Handbook and SEBoK reference descriptions; independent arithmetic checks of the invented examples; conceptual boundary review; and GitHub file-destination checks of article-local relative links.  
**Disposition:** **36 material claim families reviewed** across six articles. The six articles pass the **scoped model-assisted technical review** after the documented clarification. This is neither exhaustive standards conformance, complete claim-to-source verification, independent human expert review, nor publication acceptance.

## Claim-to-source ledger

### Feedback and Control
[Reviewed article](systems-engineering/feedback-and-control.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| FC-01 | Control and feedback have distinct purposes; open versus closed loops | [MIT 2.14 Feedback Control](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/); model-defined loop, not a physical parts mandate |
| FC-02 | Reference, plant, controller, measurement, actuator and disturbance are contextual roles | MIT 2.14; several roles may share an implementation |
| FC-03 | Negative feedback does not guarantee stability | MIT 2.14; gain, delay, saturation and model assumptions matter |
| FC-04 | Discrete scalar feedback recurrence | Verified `y[k+1]=y[k]+0.5(20-y[k])`: outputs 18, 19, 19.5 from y[0]=16; error halves each step |
| FC-05 | Convergence condition and oscillation boundary | Derived `e[k+1]=(1-K)e[k]`; `|1-K|<1` iff `0<K<2`; **clarified** monotonic convergence for 0<K≤1 (where applicable), alternating convergent error for 1<K<2, nonconvergent alternating error at K=2 for nonzero initial error |
| FC-06 | Stability, robustness, observability and controllability are different concepts | MIT 2.14; article explicitly limits formal definitions to applicable models |

### Emergence and Complexity
[Reviewed article](systems-engineering/emergence-and-complexity.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| EC-01 | Emergence is attributed to organized whole-system interactions | [SEBoK Emergence and Complexity](https://sebokwiki.org/wiki/Emergence_and_Complexity); not a claim of unexplainable effects |
| EC-02 | Complicated versus complex is a useful, not absolute, distinction | SEBoK; scale, interactions, environment and observer matter |
| EC-03 | Structural, dynamic, organizational and epistemic perspectives | Editorial examples, expressly not a ratified universal complexity taxonomy |
| EC-04 | Queue growth under overload | Two workers ×5 items/minute give at most 10/minute; sustained arrivals 11/minute lead to ≥1 item/minute backlog growth, ≥10 items after 10 minutes under stated assumptions |
| EC-05 | Feedback, nonlinearity and adaptation can shape system behavior | SEBoK; no universal inference that all complex systems are nonlinear |
| EC-06 | Simulation and observed behavior have distinct evidence limitations | SEBoK and [NASA system design](https://www.nasa.gov/reference/4-0-system-design-processes/); model-generated behavior does not certify target-world behavior |

### Reliability and Failure
[Reviewed article](systems-engineering/reliability-and-failure.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| RF-01 | Reliability requires a defined function, conditions and time interval | [SEBoK RAM](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability); fixed condition and failure definition explicit |
| RF-02 | Reliability, availability and maintainability are distinct measures | SEBoK RAM; repair may increase availability without changing failure-free survival probability |
| RF-03 | `R(t)=P(T>t)` for time to failure under stipulated convention | SEBoK RAM; nonrepairable-item interpretation qualified |
| RF-04 | Two independent 0.9-reliable components in series and ideal parallel | Independent computations: `0.9²=0.81`, `1-(0.1)²=0.99`; independence, adequate switchover and no common causes are necessary scenario assumptions |
| RF-05 | Long-run availability `A=U/(U+D)` has model requirements | Example means U=90, D=10 yields 0.90 under the article's steady-state/renewal assumptions; this is not `R(100)` |
| RF-06 | Failure mode, cause, effect, risk and detection are distinct | [NASA Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/); severity alone does not specify probability |

### Requirements
[Reviewed article](systems-engineering/requirements.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| RQ-01 | Stakeholder need, system requirement and design solution are not interchangeable | [NASA Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/); example distinguishes objectives and implementations |
| RQ-02 | Requirements need subject, criteria and defined context | NASA requirements guidance; “respond quickly” has no threshold |
| RQ-03 | Functional, quality, performance, interface and constraint concerns overlap | Editorial distinctions, not five newly approved subject categories |
| RQ-04 | `≤200 ms` example is testable only with declared event endpoints and conditions | NASA guidance; 200 ms is hypothetical, not an empirical or universal engineering standard |
| RQ-05 | Requirements traceability and allocation differ from proof of compliance | [NASA Requirements Management](https://www.nasa.gov/reference/6-2-requirements-management/); illustrative need→requirement→function→procedure→evidence links are not a new graph predicate vocabulary |
| RQ-06 | Requirements validation versus product verification | [NASA Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/); requirements can be precise but misaligned with stakeholder purpose |

### Verification and Validation
[Reviewed article](systems-engineering/verification-and-validation.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| VV-01 | Verification addresses requirements; validation addresses intended use | [NASA Product Realization](https://www.nasa.gov/reference/5-0-product-realization/); kept separate from scientific falsification |
| VV-02 | Verification records require evaluated item, requirements, conditions and evidence | NASA Product Realization; pass status limited to scope |
| VV-03 | Inspection, analysis, demonstration and test differ | [NASA Systems Engineering Appendix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/); category list used illustratively |
| VV-04 | Per-event response-time example | `[120,158,190,205,175]` ms yields sum 848, mean 169.6 ms, maximum 205 ms, **four of five** within 200 ms; a passing mean cannot satisfy a per-event requirement violated by one case |
| VV-05 | Product validation needs representative purpose and context | NASA Product Realization; component verification cannot prove an integrated system useful |
| VV-06 | Version, integration, measurement uncertainty and acceptance authority matter | NASA guidance; prior pass or waiver is not universal approval |

### System Lifecycle
[Reviewed article](systems-engineering/system-lifecycle.md)

| ID | Claim group | Evidence / finding |
| --- | --- | --- |
| LC-01 | Lifecycle models describe conception through retirement under selected scope | [SEBoK Life Cycle Models](https://sebokwiki.org/wiki/Life_Cycle_Models); stages are not universal laws |
| LC-02 | Project lifecycle differs from system lifecycle | SEBoK Life Cycle Models; delivery project may end while system remains in use |
| LC-03 | Stages and recurring processes are distinct; overlap and iteration may occur | SEBoK: concurrency and iteration depend on the model |
| LC-04 | Decision evidence and configuration management are lifecycle concerns | [NASA Program/Project Lifecycle](https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/) and [NASA Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/); authorizations do not prove zero residual risk |
| LC-05 | Optional v2 diagnostic field is not a universal compatibility guarantee | Invented v1/v2 example: a v1 parser may reject unknown fields, and changed semantics may break consumers despite optionality |
| LC-06 | System retirement differs from data deletion or project completion | SEBoK Life Cycle Models; general temporality G-04 remains unresolved |

## Correction committed before acceptance

**Feedback and Control:** The scalar discrete-time example now explicitly distinguishes non-oscillatory convergence, alternating convergent error and a marginal nonconvergent oscillation. This qualifier follows directly from the model's recurrence. All other worked arithmetic checks passed without requiring correction.

The article examples are **original conditional models**, not measurements of equipment or case studies attributed to MIT, NASA or SEBoK.

## Numerical checks

| Example | Independently computed |
| --- | --- |
| Discrete feedback `y[0]=16, r=20, K=0.5` | 18 → 19 → 19.5 |
| Persistent demand 11 and maximum capacity 10 items/minute | ≥10 queued items after 10 minutes (given stated assumptions) |
| Independent two-component series reliability | 0.81 |
| Ideal redundant parallel reliability | 0.99 |
| Modeled availability with U=90, D=10 | 0.90 |
| Response-time example sum and average | 848 ms and 169.6 ms |
| Response-time threshold 200 ms | 4 pass, 1 fail; maximum 205 ms |

## Link scope and status

The six articles contained **66 relative Markdown-link occurrences** mapping to **22 distinct relative file destinations**. All **22/22** distinct file paths were fetched successfully through GitHub. This validates file existence, **not** fragments/anchors, external links, link semantics, or the entire repository graph.

**Reviewed (model-assisted)** and **Core claims checked** reflect this bounded technical pass. They do not mean full source-level **Verified**, independent human peer review, standards certification, or final **Published** approval.

The approved **12 knowledge areas / 109 subject headings** remain unchanged. **G-01**, **G-04**, and **G-06** remain open; no assessments, new subject categories or mandatory implementation platforms were introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
