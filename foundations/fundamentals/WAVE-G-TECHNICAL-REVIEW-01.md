# Wave G | Established Frameworks, Models & Architectures: Depth Audit 01

**Audit date:** November 18, 2026  
**Scope:** Thirteen existing Fundamentals articles across eight approved knowledge areas, revised after the [77-name model-diagnostic pass](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) and [adjudication](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md).  
**Review method:** Reopened the canonical GitHub articles; examined model definitions and primary reference summaries from ISO, IETF, OMG, BIPM/JCGM, W3C, MIT, the FAA, UK HSE and engineering references; checked three material claim families per revised article, recomputed quantitative illustrations and reviewed canonical ownership. The FAA report's signal-detection matrix and the Gilbert/Lynch CAP exposition were also inspected as PDF page images.  
**Outcome:** **39 material claim families across 13 article revisions pass the bounded model-assisted review.** The model-assisted Reviewed status of these articles remains supported within this new scope, with existing review histories retained separately.

This review is **not** complete ISO/OMG standard clause verification, exhaustive sentence-to-source checking, independent human peer review, a real-system benchmark or final Published acceptance. External standards and scholarly models are sources for technical definitions, **not** authorization to create one Fundamentals subject per named model.

## Review evidence: source-defined claim groups

### F-03-10 · Models & Abstraction · conceptual and formal models

[Revised canonical article](models-abstraction/conceptual-and-formal-models.md)  
**Source orientation:** [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/); [OMG SysML](https://www.omg.org/sysml/); [MIT Petri Nets](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-094.pdf)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| FM-01 | Representation type | Correctly distinguishes state transition systems, Petri nets, UML/SysML modeling languages, and formal specifications rather than calling every diagram an architecture. |
| FM-02 | Petri semantics | Places, transitions and token marking appear in a minimal one-token enabling/firing example; general arc weights and complex firing rules are not claimed as universal. |
| FM-03 | Version and verification limits | OMG SysML v2 final adoption noted without treating its language family as a required repo technology; model conformance is not system behavior proof. |

### F-11-03 · Systems & Engineering · architecture and composition

[Revised canonical article](systems-engineering/architecture-and-composition.md)  
**Source orientation:** [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| AC-01 | Architecture vs description | Official ISO 42010 scope explicitly distinguishes architecture from architecture description; no prescribed engineering method, tool, or format is claimed. |
| AC-02 | Viewpoint and view | Stakeholder/concern/viewpoint/view/model-kind distinctions are presented as representational concerns, not a fixed list of universal system levels. |
| AC-03 | Cross-view example | Heating-system connection, wiring and timing descriptions require reconciliation; diagram existence does not establish timing/requirement satisfaction. |

### F-11-11 · Systems & Engineering · system lifecycle

[Revised canonical article](systems-engineering/system-lifecycle.md)  
**Source orientation:** [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| SL-01 | Lifecycle processes vs stages | ISO abstract explicitly allows concurrent, iterative and recursive use of processes and disclaims a prescribed lifecycle model. |
| SL-02 | System vs project lifecycle | System longevity and project time horizon remain different units of analysis; V-model not misrepresented as mandatory ISO sequence. |
| SL-03 | Change example | Post-deployment actuator modification correctly raises revisiting requirements, verification and safety claims, without treating a project as restarted. |

### F-10-04 · Communication & Distributed Systems · protocols and layering

[Revised canonical article](communication-distributed-systems/protocols-and-layering.md)  
**Source orientation:** [ISO/IEC 7498-1](https://www.iso.org/standard/20269.html); [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122.html#section-1.1.3)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| PL-01 | Reference architectures | OSI seven layers and Internet suite application/transport/internet/link distinctions are attributed to separate reference models; one-to-one mapping explicitly rejected. |
| PL-02 | Transport semantics | TCP byte stream contrasted with UDP datagrams and application framing; no implication that layer boundaries alone guarantee isolation. |
| PL-03 | End-to-end claim limits | IP/link/transport/application acceptance treated as different observations; diagram does not certify actual delivery or effect. |

### F-10-08 · Communication & Distributed Systems · distributed state

[Revised canonical article](communication-distributed-systems/distributed-state.md)  
**Source orientation:** [Gilbert/Lynch CAP exposition (MIT)](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| DS-01 | CAP theorem scope | Atomic read/write consistency, availability response and communication partition assumptions stated; 'pick any two' slogan rejected. |
| DS-02 | Partitioned register example | Completed write X=6 at A, subsequent stale read X=5 at B conflicts with the stipulated linearizable register contract; refusal/delay changes availability. |
| DS-03 | Risk of overgeneralization | No universal real-system behavior, vendor-specific protocol, recovery-time or data-loss conclusion inferred from the mathematical result. |

### F-02-02 · Scientific & Analytical Reasoning · measurement

[Revised canonical article](scientific-analytical-reasoning/measurement.md)  
**Source orientation:** [JCGM 100:2008](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e); [JCGM publications](https://www.bipm.org/en/committees/jc/jcgm/publications)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| ME-01 | GUM method and version | Type A/B distinguish evaluation methods and not random/systematic error; 2026 amendment's existence confirmed in JCGM publication list, not exhaustive clause review. |
| ME-02 | Uncertainty propagation | For uncorrelated sum, standard uncertainty sqrt(.2²+.3²)=sqrt(.13)=0.360555...; covariance and model assumptions stated. |
| ME-03 | Coverage and decision limits | No automatic 95% coverage from k factor; threshold decision rule requires separate definition and applicability. |

### F-05-09 · Information & Data · data provenance and lifecycle

[Revised canonical article](information-data/data-provenance-and-lifecycle.md)  
**Source orientation:** [W3C PROV-DM](https://www.w3.org/TR/prov-dm/); [PROV-O](https://www.w3.org/TR/prov-o/); [PROV Constraints](https://www.w3.org/TR/prov-constraints/)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| PV-01 | Core PROV classes | Entity, Activity, Agent correspond to source-defined concepts; relation distinctions were checked against W3C recommendations. |
| PV-02 | Derivation example | R used by C, N generated by C and derived from R are separate claims; use/generation alone does not establish derivation or accuracy. |
| PV-03 | Evidence and validity limits | PROV-conformant graph cannot alone establish authenticated, complete or true process history; provenance validity separate from fact truth. |

### F-05-08 · Information & Data · databases and queries

[Revised canonical article](information-data/databases-and-queries.md)  
**Source orientation:** [ISO SQL/Foundation](https://www.iso.org/standard/76584.html); [PostgreSQL table expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| DB-01 | Relational vs ER models | Relational tuple-based structure distinguished from conceptual entity–relationship modeling and physical storage. |
| DB-02 | SQL semantics caveat | SQL bags and nulls prevent naive mathematical-set equivalence; key and foreign-key constraints require explicit enforcement. |
| DB-03 | Join-grain example | Three orders for C1 and one for C2 => four matched joined rows but two distinct customer IDs; inner join excludes unmatched customers. |

### F-12-01 · Human & Sociotechnical Systems · human cognition and perception

[Revised canonical article](human-sociotechnical-systems/human-cognition-and-perception.md)  
**Source orientation:** [FAA human-factors report](https://hf.tc.faa.gov/publications/2007-human-factors-analysis/full_text.pdf); [HSE Workload](https://www.hse.gov.uk/humanfactors/topics/workload.htm)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| HC-01 | Cognitive load scope | Task and presentation demands distinguish workload from assumed fixed individual intelligence or universal memory-item limit. |
| HC-02 | SDT outcome matrix | Hit/miss/false alarm/correct rejection verified against FAA table on printed page 8; criterion differs from discrimination sensitivity. |
| HC-03 | Cross-domain inference limits | Alarm count does not establish individual competence, base rate or real-system detector accuracy. |

### F-12-02 · Human & Sociotechnical Systems · decision making

[Revised canonical article](human-sociotechnical-systems/decision-making.md)  
**Source orientation:** [FAA Signal Detection Theory](https://hf.tc.faa.gov/publications/2007-human-factors-analysis/full_text.pdf)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| DM-01 | Decision threshold vs sensitivity | Action criterion and ability to discriminate are distinguished; under the stated model, criterion shifts may change hits and false alarms. |
| DM-02 | Expected-loss calculation | 2(1−p) < 20p implies p>1/11≈0.090909; independently recomputed exact expression. |
| DM-03 | Conditions and transfer limits | Toy decision excludes action cost during real hazard, delays, secondary consequences and uncertainty; no practical threshold recommendation. |

### F-12-05 · Human & Sociotechnical Systems · human error

[Revised canonical article](human-sociotechnical-systems/human-error.md)  
**Source orientation:** [UK HSE Managing Human Failures](https://www.hse.gov.uk/humanfactors/topics/humanfail.htm)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| HE-01 | Error categories | Unintentional slip/lapse/mistake versus intentional violation aligns with HSE; intentional deviation not assumed malicious. |
| HE-02 | Layered-barrier heuristic | Swiss-cheese style layered-defense framing declared heuristic, not a calculated probability or proven individual causal chain. |
| HE-03 | Control inference example | Ambiguous field mapping versus training distinguished; prevention and effectiveness need evidence, not blame inference. |

### F-11-06 · Systems & Engineering · feedback and control

[Revised canonical article](systems-engineering/feedback-and-control.md)  
**Source orientation:** [MIT 2.14 feedback](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/); [MathWorks PID](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| FC-01 | Ideal PID model | Proportional+integral+derivative terms correctly scoped as one possible controller, not a universal stability design. |
| FC-02 | Saturation example | Kp=2, e=3 yields command 6; actuator clamp at 5 means plant receives at most 5 in model. |
| FC-03 | Implementation limitations | Windup, derivative noise, discrete sampling, delay and plant dynamics flagged; PID adoption does not imply stable response. |

### F-04-09 · Physical & Electrical Principles · physical control mechanisms

[Revised canonical article](physical-electrical-principles/physical-control-mechanisms.md)  
**Source orientation:** [MIT 2.14 control](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/); [MathWorks PID](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html)

| Claim ID | Material claim reviewed | Bounded finding |
| --- | --- | --- |
| PC-01 | Controller vs physical plant | Actuator saturation, power limits, physical delay and noise separate computed commands from achieved effects. |
| PC-02 | Ideal thermal calculation | 700-W request capped at 500 W; with C=1000 J/K and no losses, dT/dt=500/1000=0.5 K/s, not 0.7. |
| PC-03 | Physical safety limits | The toy calculation does not claim real thermal response/safety; requires energy balance, sensor evidence, disturbances and verification. |

## Independently recomputed illustrative values

| Example | Calculation | Result and limitation |
| --- | --- | --- |
| Uncorrelated additive input uncertainties | sqrt(0.2²+0.3²) | **sqrt(0.13)≈0.360555**, conditional on standard-uncertainty and zero-covariance assumptions |
| Toy two-action decision criterion | 2(1−p)<20p | **p>1/11≈0.090909**, conditional on stipulated costs and posterior estimate |
| Saturating ideal proportional controller | Kp·e=2·3=6, output capped at 5 | Command 6, physical modeled input at most 5; no plant-stability inference |
| Ideal heat-transfer rate | 500 W / (1000 J/K) | **0.5 K/s** maximum in lossless lumped model, not measured temperature |
| Customer/order join grain | 3 matching orders for C1 plus 1 for C2 | **4 matched rows, 2 distinct customer IDs**, contingent on unique order keys |
| Two-way illustrative system-provenance relationship | Used(R,C); WasGeneratedBy(N,C); WasDerivedFrom(N,R) | Distinct PROV claims; generation and use need not universally establish derivation |

The engineering/measurement/decision values are hypothetical; their exact arithmetic does not establish the proposed model's empirical validity.

## Model and architecture ownership decisions

- **FMA-05 formal models:** Finite state, Petri nets, UML and SysML remain illustrative representation families in [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md). No new subject or mandatory modeling language.
- **FMA-06 architecture:** ISO 42010 applies to architecture **descriptions**, views/viewpoints and associated model conventions. It does not prescribe the architecture or development method.
- **FMA-08 communications:** Seven-layer OSI and RFC 1122's Internet architecture remain distinct conceptual reference models, not a one-to-one mapping to physical protocol modules.
- **FMA-09 distributed systems:** CAP concerns a specified atomicity/availability/partition model. No timeless “choose two of three” slogan or real-system service guarantee is asserted.
- **FMA-10 measurement:** JCGM GUM evaluation/propagation and the 2026 nonlinearity amendment are linked as scoped technical sources, not as claims of measured system accuracy.
- **FMA-11 provenance:** W3C PROV relations, relational model, ER model and SQL implementation semantics have separate canonical meanings.
- **FMA-12 human factors:** SDT, cognitive-load ideas and barrier heuristics are attributed and bounded, rather than treated as universal formulas for human performance.
- **FMA-13 life cycle:** ISO 15288 processes are distinguished from the life-cycle stages and from a mandatory V-model.
- **FMA-14 control systems:** PID control is one control algorithm family; abstract controller specification and physical actuation limits retain separate canonical homes.

## Corrections and limitations

1. **Source currency:** The JCGM publications catalog as checked on November 18, 2026 lists JCGM 100:2008, a 2026 amendment addressing nonlinear models, and other guides in the current GUM suite. This review confirms publication metadata, **not** complete examination of the amendment.
2. **Model identity:** ISO 42010:2022 and ISO 15288:2023 have distinct scopes; OMG UML 2.5.1 and SysML v1/v2 should not be conflated; the original MIT Petri-net material was used for conceptual comparison, not proof of full model-checker semantics.
3. **PDF/authority checks:** The FAA 2007 report's printed page 8 supports the SDT matrix and criterion discussion. MIT's CAP review supports atomic-consistency and eventual-response definitions within its system model. Neither source should be generalized into an empirical claim about unrelated environments.
4. **Source limits:** Some full ISO standards and referenced original papers may be licensed or incompletely accessible. Primary publisher abstracts and reference landing pages were used for scope where the full text was not available. The audit does not claim exhaustive normative compliance checks.
5. **Portfolio:** The twelve-area, **116-subject** inventory remains unchanged. All 116 retain a **Reviewed (model-assisted)** development state and a separate **Core claims checked** source-review state. No new Known Checks, Practical Assessments, mandatory platform or graph schema introduced.
6. **Outstanding publication work:** Full claim-to-passage verification, external link/fragment freshness, semantic relationship consistency across the corpus, seven-domain adequacy and qualified human expert acceptance.

## Reproducible checks

The existing [Fundamentals navigation/inventory workflow](https://github.com/TannerPhillips-SecurityEducation/Security-Education/actions/workflows/fundamentals-internal-links.yml) checks article links, heading fragments and status counts. The passing CI result must be inspected separately from this claim-review document; green CI is **not** independent technical peer review.

[Fundamentals index](README.md) · [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Original Models Audit](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md)
