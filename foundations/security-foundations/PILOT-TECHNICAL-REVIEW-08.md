# Security Foundations | Technical Review 08: Threat Sources, Actor Conditions, TTPs, and Attack Paths

**Review date:** November 18, 2026  
**Scope:** Four substantive area-first working Drafts in [Threats, Hazards & Adversarial Behavior](threats-hazards-adversarial-behavior/README.md): **SF-03-02**, **SF-03-03**, **SF-03-05**, **SF-03-06**. This audit examines **32 material claim groups**: seven, eight, eight, and nine respectively. **SF-03-04 and SF-03-07 remain Inventoried** without articles and are *not* implicitly covered.  
**Method:** Separate model-assisted claim-led technical review following Draft Batch 08. Compared the claims against publisher-hosted NIST SP 800-30 Rev. 1, ATT&CK's live FAQ and historical MITRE design paper, MITRE's CAPEC comparison, the original Diamond Model, and the Unified Kill Chain's own published description. **Visually inspected rendered PDF pages** where quoted locations, Figure 1 and Section 3.4.1 matter. Independently enumerated the opportunity and alternative-path Boolean examples, investigated actor identity and intent counterexamples, and applied bounded manuscript corrections before status promotion.  
**Disposition:** All four **corrected** manuscripts pass a **scoped model-assisted technical review** and are eligible for **Reviewed (model-assisted) / Core claims checked**. This does not establish complete claim-to-passage verification, independent qualified human review, that the frameworks are exhaustive, a validated live attack model, permanent canonical ownership or publication approval.

## 1. SF-03-02 | Adversarial and Non-Adversarial Threat Sources

**Manuscript:** [Adversarial and Non-Adversarial Threat Sources](threats-hazards-adversarial-behavior/adversarial-and-non-adversarial-threat-sources.md)  
**Primary publisher references:** [NIST SP 800-30 Rev. 1 (final, September 2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Chapter 3 Tasks 2-1 and 2-2, printed pp. 30–31 / PDF page indexes 38–39; [NIST non-adversarial threat glossary](https://csrc.nist.gov/glossary/term/non_adversarial_threat), explicitly sourced to SP 800-160 Vol. 2 Rev. 1; [NIST threat source](https://csrc.nist.gov/glossary/term/threat_source), [threat event](https://csrc.nist.gov/glossary/term/threat_event), and [predisposing condition](https://csrc.nist.gov/glossary/term/Predisposing_Condition) entries.

| Group | Material claim or test | Second-pass finding, correction and boundary |
| --- | --- | --- |
| 08-02-01 | A potential threat source, threat event and realized consequence are different claims | **Pass.** NIST SP 800-30 Task 2-2 concerns *potential* events and sources; neither their presence nor a risk entry proves an event or an adverse impact occurred. The working article retains the source/event distinction already owned by SF-03-01 without creating a new competing definition. |
| 08-02-02 | NIST assesses adversarial capability, intent and targeting separately from non-adversarial effects | **Pass with explicit scope correction.** Directly inspected NIST SP 800-30 Rev. 1 **printed p. 30, PDF index 38**: Task 2-1 names adversarial **capability, intent and targeting**, and non-adversarial **potential range of effects**. Updated the article to say Appendix D scales are **exemplary, tailorable**, not empirically calibrated universal values; storms have no meaningful hostile intent under this model. |
| 08-02-03 | Non-adversarial threats include accidental error, technical and environmental causes | **Pass.** NIST's glossary attributes its concise non-adversarial definition to **SP 800-160 Vol. 2 Rev. 1**. Source variation does not make all failures *security violations*; the relevant security property and accepted operating conditions still matter. |
| 08-02-04 | Source/event associations can be many-to-many | **Pass with correction.** NIST Task 2-2 **printed p. 31, PDF index 39**, visually inspected, explicitly states many sources may initiate a single threat event and a source may initiate many events. The article's \(\mathcal T\subseteq\mathcal S\times\mathcal E\) is **author-created relational notation**, and possible association is not proof of event causation. Added the source-defined note that different source-event pairings can have different likelihood assumptions. |
| 08-02-05 | Vulnerability, predisposing condition, hazard and threat source are not interchangeable | **Pass with source limit.** NIST's [predisposing-condition glossary](https://csrc.nist.gov/glossary/term/Predisposing_Condition) covers conditions raising *or lowering* the likelihood of harmful effect after a threat event. A technical fault or storm is not inherently a malicious principal, and not every source needs a software weakness. |
| 08-02-06 | Mixed adverse episodes need actor- and event-specific classification | **Pass after correction.** The invented power-outage/misconfigured-failover/intentional-read example can contain an accidental upstream condition and a possibly deliberate later event. Added the warning that classifying a whole episode as one source type conceals different causal relationships. The example does not prove an attacker existed. |
| 08-02-07 | Intent and attribution require evidence beyond observed severity or unusual telemetry | **Pass.** A large loss, failed login, or availability failure does not identify a human actor or their objective. The article expressly retains **unknown** intent and links actor identification to SF-10-08. This is not a legal determination or probabilistic threat assessment. |

**Manuscript corrections:** Added visually checked NIST page locations and explicit tailorable-source qualifiers; clarified possible rather than established source-event association; reinforced mixed causal roles; distinguished event/source classification from a single episode-wide label.

## 2. SF-03-03 | Capability, Opportunity, and Intent

**Manuscript:** [Capability, Opportunity, and Intent](threats-hazards-adversarial-behavior/capability-opportunity-and-intent.md)  
**Primary publisher references:** [NIST SP 800-30 Rev. 1, Task 2-1 and Appendix D](https://csrc.nist.gov/pubs/sp/800/30/r1/final), final 2012; [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) for tactic-level goal; [Diamond Model of Intrusion Analysis, Figure 1](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), printed p. 9 / PDF index 8.

| Group | Material claim or test | Second-pass finding, correction and boundary |
| --- | --- | --- |
| 08-03-01 | Actor capability, opportunity, intent and targeting do not imply each other | **Pass.** These are context- and time-relative dimensions. NIST source-defined traits include **capability, intent, targeting**, whereas **opportunity** is explicitly an *additional editorial circumstance/route concept*, not an alleged fourth NIST assessment-scale attribute. |
| 08-03-02 | Effective capability depends on relevant technology and conditions | **Pass.** Possession of a generic tool or published vulnerability knowledge is not sufficient evidence of a working capability against a particular protected interface. A successfully observed act supports only the capability actually demonstrated under those conditions. |
| 08-03-03 | Diamond “capability” feature is different in unit from a source-level capability assessment | **Pass after material correction.** Visually inspected the original Diamond Model **Figure 1, printed p. 9 / PDF index 8**, with four core intrusion-event features: adversary, infrastructure, capability and victim. The Diamond *event capability* (used tool/technique) is not identical to NIST's *threat-source* capability assessment (broader actor means). Corrected the article to distinguish these instead of implying equivalence. |
| 08-03-04 | An opportunity conjunction represents a scoped necessary-condition model | **Recomputed.** For \(O=R\land A\land T\land P\), all **16** Boolean assignments were enumerated: **one** yields true, the all-true tuple; **15** yield false. Corrected the wording to say the all-true assignment proves only the **authored Boolean expression** evaluates true, not that exploitation is really possible or an actor will act. |
| 08-03-05 | Alternative opportunity routes are disjunctive, not automatically chosen | **Pass.** \(O_{\mathrm{total}}=\bigvee_iO_i\) is a logical option model, not a quantified attack-probability formula. An actor may be unaware of an available route, or a separate unmodeled guard may prohibit the actual transition. |
| 08-03-06 | Observed authentication behavior need not disclose motive or operator identity | **Pass.** Multiple failed sign-ins can have malicious or benign causes, and a permitted read need not imply legitimate purpose. The article's case separates observation, constrained derivation, alternative intent hypotheses and absent proof of personal attribution. |
| 08-03-07 | NIST ordinal capability/intent/targeting tables are not calibrated attack probabilities | **Pass with scope correction.** Task 2-1 printed p. 30 names Appendix D Tables D-3, D-4 and D-5 as **exemplary, tailorable scales**. Added the note that the scales require context/rationale; no multiplication or uncalibrated combination of ratings yields a defensible success probability. |
| 08-03-08 | Time-indexed actor variables and the SF-03-08 consolidation do not create a second attribution theory | **Pass with qualification.** \(C_a(t)\), \(O_{a,s}(t)\), \(I_a(t)\), \(T_{a,s}(t)\) are **editorial symbolic placeholders**, not measured continuous or scalar quantities. The former SF-03-08 intent/attribution heading remains consolidated: actor-objective hypotheses here, evidence-to-identity and causal confidence in **SF-10-08**. |

**Manuscript corrections:** Differentiated the Diamond Model's *event capability* from NIST's *source capability*; constrained the 4-input Boolean test to modeled opportunity; stated the NIST ordinal-scale limitation and source page; qualified symbolic time-indexed actors to prevent invented probabilities.

## 3. SF-03-05 | Adversarial Tactics, Techniques, and Procedures

**Manuscript:** [Adversarial Tactics, Techniques, and Procedures](threats-hazards-adversarial-behavior/adversarial-tactics-techniques-and-procedures.md)  
**Primary publisher references:** [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/), consulted November 18, 2026; [MITRE ATT&CK: Design and Philosophy, March 2020 revision](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf), §3.4.1 printed p. 9 / PDF index 18, visually inspected; [MITRE CAPEC versus ATT&CK](https://capec.mitre.org/about/attack_comparison.html) and [CAPEC introduction](https://capec.mitre.org/about/new_to_capec.html); original [Diamond Model](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf) and [Unified Kill Chain](https://www.unifiedkillchain.com/).

| Group | Material claim or test | Second-pass finding, correction and boundary |
| --- | --- | --- |
| 08-05-01 | Tactic means ATT&CK's immediate why; technique means how | **Pass.** The live MITRE FAQ explicitly defines tactics as tactical goals, techniques as how an adversary can achieve those goals, and sub-techniques as more specific behavior. An ATT&CK tactic is not a proven actor's **ultimate personal motive**. |
| 08-05-02 | Procedure means a specific implementation and can involve several techniques | **Pass with precise evidence.** MITRE design paper **§3.4.1, printed p. 9 / PDF index 18**, visually checked, says procedures are specific adversary implementations and may span multiple behaviors. The live FAQ adds that ATT&CK's **Procedure Examples** are source-reported in-the-wild uses. Corrected the draft to distinguish documented procedures from purely **hypothetical locally constructed procedures**. |
| 08-05-03 | ATT&CK tactic labels are not a fixed chronological chain | **Pass.** The article avoids imposing a mandatory sequence, or inferring unobserved stages from a single classified action. The MITRE **2020 paper is historical model-design evidence**, not the complete November 2026 technique inventory. The article now states that scope explicitly. |
| 08-05-04 | ATT&CK behavioral entries and CAPEC weakness-oriented attack patterns differ | **Pass after clarification.** MITRE's [CAPEC comparison](https://capec.mitre.org/about/attack_comparison.html) focuses CAPEC on application vulnerabilities and attack patterns (also including social engineering/supply chain) and ATT&CK on adversary operational behavior. CAPEC execution flow is a **pattern**, not a record that a particular exploit occurred; a catalog relationship need not be one-to-one. |
| 08-05-05 | Diamond event relations and UKC phases are not ATT&CK tactics | **Pass.** The Diamond Model connects adversary/capability/infrastructure/victim as features of an *intrusion event*, while the Unified Kill Chain's own site uses **Getting In, Hacking Through and Taking It Out** as broader progression groupings. Neither is equivalent to an ATT&CK technique list or proof of an individual campaign timeline. |
| 08-05-06 | TTP classes versus tool filenames, hashes and other concrete indicators | **Pass.** One tool can support multiple techniques and one technique may be implemented by several tools. The article properly limits the Pyramid of Pain to a heuristic rather than a universal numeric measure of adversary cost. |
| 08-05-07 | Valid technique classification is not evidence of observed malicious activity | **Pass with clarification.** A rule or log may correspond to legitimate work, a simulation or malicious conduct. The article now explicitly separates *observation fidelity*, *mapping fit* and *adversarial interpretation*, while preserving SF-10-08's separate ownership of identity and intent evidence. |
| 08-05-08 | A tactic, technique, sub-technique, procedure, event and strategic objective are not one hierarchy | **Pass.** The table marks strategic objective and event as **adjoining editorial concepts**, not extra ATT&CK nodes. An example of a procedure may involve multiple techniques; ATT&CK's specific technique relations and platform applicability remain release-dependent and require claim-specific checks for actual detections. |

**Manuscript corrections:** Added the MITRE 2020 source edition and exact visually checked procedure passage; qualified ATT&CK's Procedure Examples as documented in-the-wild behavior; adopted MITRE's own CAPEC-versus-ATT&CK unit distinction; separated behavior-to-model mapping from actor/incident evidence.

## 4. SF-03-06 | Attack Paths, Stages, and Dependencies

**Manuscript:** [Attack Paths, Stages, and Dependencies](threats-hazards-adversarial-behavior/attack-paths-stages-and-dependencies.md)  
**Primary publisher references:** [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Task 2-2 printed p. 31 / PDF index 39, visually inspected; [Diamond Model Figure 1](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), printed p. 9 / PDF index 8, visually inspected; [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/); [MITRE CAPEC](https://capec.mitre.org/about/new_to_capec.html); [Unified Kill Chain](https://www.unifiedkillchain.com/). The graph and guard expressions are **authored abstractions**, not formulas prescribed by these sources.

| Group | Material claim or test | Second-pass finding, correction and boundary |
| --- | --- | --- |
| 08-06-01 | An attack path is a state-transition relation rather than a timestamped story | **Pass.** NIST Task 2-2 recognizes events spanning systems, connectivity and functional dependencies. The working graph \(G=(V,E)\) explicitly declares nodes as relevant states and edges as candidate transitions. It is not evidence of a real intrusion or proof that all potential states have been modeled. |
| 08-06-02 | Path guards depend on evolving state, not one initial snapshot | **Pass after material correction.** The drafted implication \(\operatorname{Feasible}(P,s_0)\Rightarrow\bigwedge_{i=1}^k g_{e_i}(s_{i-1})\) states a **necessary** condition for modeled feasibility. The guards must hold in the states actually reached after preceding transitions. Their truth alone is not sufficient without a valid transition relation, real-world reachability and legitimate observation evidence. |
| 08-06-03 | Model feasibility, configuration reachability, observed traversal and unauthorized outcome differ | **Pass after correction.** An abstract edge can be logically permitted but absent from the deployed implementation; a path can be reachable but not attempted; a record can show an attempt without proving success. The corrected article explicitly enumerates these levels and leaves actual security-violation evidence to its appropriate owner. |
| 08-06-04 | Logical AND and OR express necessary requirements and alternatives, not probabilities | **Recomputed.** \(R\land C\) is true only for \(R=C=1\). For \(P_A\lor P_B\), all **four assignments** were enumerated; the result is false only when both modeled routes are false. There are no probability, independence or completeness assumptions in the Boolean identity. |
| 08-06-05 | Blocking one represented path does not show complete defensive coverage | **Pass with correction.** If \(P_A\) is blocked but \(P_B\) remains feasible, the two-route objective is still available under the model. A control claim needs a defined path set, boundary and evidence; this article never provides live bypass instructions or a complete attack-surface map. |
| 08-06-06 | Timestamp order is not proof of causal order or shared actor | **Pass.** A timestamp may reflect receipt rather than occurrence, sensors may be out of sync, and events may be independent. The three-observation fictional case does not show data exfiltration merely because data transfer followed a login and a catalog query. |
| 08-06-07 | Diamond core features and activity threads are analyst constructs | **Pass.** Inspected Diamond **Figure 1, printed p. 9 / PDF index 8**, showing adversary, capability, infrastructure, victim and optional meta-features. The article now states that particular features can be unknown and that populating a model does not prove real-world identity. Linked-event activity threads are not certificates of common authorship. |
| 08-06-08 | ATT&CK behavior categories, CAPEC pattern flow and UKC stages describe different units | **Pass.** ATT&CK tactics are goals, CAPEC gives reusable weakness-oriented patterns, UKC describes a progression model with three high-level groupings, and Diamond emphasizes intrusion events. No forced one-to-one technique/stage correspondence or universally mandatory sequence is justified. |
| 08-06-09 | Loops, branching, alternative dependencies and evidence gaps matter | **Pass.** The article correctly says a basic DAG is not enough for all repeated-state behaviors; a time-expanded DAG can encode some bounded cases if time is modeled. No real state graph, empirical transition probability, formal completeness proof or retrospective incident reconstruction has been produced. |

**Manuscript corrections:** Explicitly made transition guards necessary but not sufficient; distinguished model-feasible paths from deployed reachability and observed traversal; qualified alternate-route coverage claims; labeled the inspected Diamond figure, unknown vertex values and distinct evidence levels.

## Independent formal checks and conceptual counterexamples

The following checks were performed separately from the original Draft manuscript statements.

### Opportunity conjunction: sixteen complete truth assignments

Let \(O=R\land A\land T\land P\) for four Boolean conditions. Enumerating \(2^4=16\) possible input tuples produces **one true output** (R=A=T=P=1) and **15 false outputs**. This is only a verification of the **declared Boolean gate**. It is not evidence that all relevant real-world conditions were included, that access is unauthorized, or that any adversary used the opportunity.

### Two-route alternative: four complete truth assignments

| Modeled route A | Modeled route B | \(P_A\lor P_B\) |
| ---: | ---: | ---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

This supports the narrow claim that removing *only* A does not prevent the objective if B remains available. It does not demonstrate that the model includes every real route, whether the actor knows any route, or whether all control effects are correctly represented.

### Source-event association versus event causation

A hypothetical service outage could be associated with a power failure, accidental maintenance error or intentional disruption. A source-event candidate relation \(\mathcal T\subseteq\mathcal S\times\mathcal E\) identifies **possible** pairings; its existence is not a causal graph of things known to have happened. This interpretation agrees with NIST Task 2-2's many-to-many language and avoids inventing evidence.

### A counterexample to a linear observed attack

An account authenticates; later, a session queries a catalog; later, a network service transfers bytes. Those three records could be independent or authorized events. One cannot conclude initial exploitation, Discovery, Collection, Exfiltration, one malicious operator or successful compromise without additional identity, object/content, authorization and causality evidence. Model fit alone does not establish malicious intent.

## Corrections and unresolved evidence

| Working subject | Core correction | Unresolved approval / evidence boundary |
| --- | --- | --- |
| SF-03-02 | Source-specific NIST adversarial versus non-adversarial assessment branches; many-to-many possible association; mixed causes | No actual source/event attribution, validated source taxonomy or empirical likelihood |
| SF-03-03 | Diamond event capability ≠ NIST actor-source capability; opportunity Boolean logic and ordinal scales cannot prove exploitability or probability | No calibrated capability scale, measured intent or individual identity proof |
| SF-03-05 | ATT&CK 2020 design source versus live FAQ; in-the-wild procedures; CAPEC pattern versus ATT&CK behavior | No comprehensive current-release technique inventory verification or incident mapping |
| SF-03-06 | Stateful necessary guards versus real reachability; route-coverage logic; event features can remain unknown | No validated live attack graph, actor history, temporal causality or prevention proof |

**Inspected primary pages:** NIST SP 800-30 Rev. 1 **printed pp. 30–31 / PDF page indexes 38–39** (Tasks 2-1, 2-2); Diamond Model original **Figure 1 printed p. 9 / PDF index 8**; MITRE ATT&CK Design and Philosophy **§3.4.1 printed p. 9 / PDF index 18**. These were visually checked from the publisher-hosted PDFs; other linked sources were checked via their official publisher HTML and source records. The live MITRE and NIST pages may change over time; the document specifies its review date.

**Not performed:** Independent qualified peer review; full claim-by-claim verification of every sentence across all sources and versions; a full current ATT&CK technique enumeration or coverage assessment; a real system, network or adversary test; incident attribution; legal determinations; risk-estimation calibration; ratification of twelve working knowledge areas or 96 candidate subjects.

**State transition justified:** Promote SF-03-02, SF-03-03, SF-03-05 and SF-03-06 **Draft → Reviewed (model-assisted)** and **References listed → Core claims checked**, only after applying the corrections and recording their individual claims here. Prior Reviews 01–07 covered **147 material claim groups across 25 manuscripts**; Review 08 adds **32** for a current **179 bounded groups across 29 Reviewed manuscripts**, **0 Draft**, and **67 Inventoried without article**. SF-03-04 and SF-03-07 are still Inventoried; no working taxonomy decision or final publication is inferred from their neighbors.

[Security Foundations](README.md) · [Working article register](pilots/README.md) · [Development and verification register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Working ownership register](CANONICAL-OWNERSHIP-REGISTER.md)
