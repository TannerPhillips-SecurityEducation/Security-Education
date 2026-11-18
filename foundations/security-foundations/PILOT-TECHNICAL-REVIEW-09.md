# Security Foundations | Technical Review 09: Defense Depth, Coverage, Failure, and Redundancy

**Review date:** November 18, 2026  
**Scope:** Four separately authored Draft manuscripts: **SF-07-04**, **SF-07-05**, **SF-07-06** in [Security Controls & Defense Mechanisms](security-controls-defense-mechanisms/README.md), and **SF-11-05** in [Security Failure & Resilience](security-failure-resilience/README.md). **31 bounded material claim groups:** 8 + 7 + 7 + 9, respectively.  
**Method:** Separate source-led, model-assisted technical second pass after Draft Batch 09. Compared claims with NIST SP 800-160 Vol. 1 Rev. 1 and Vol. 2 Rev. 1 original publication pages; checked NIST SP 800-53 versus 800-53A current Release 5.2.0 source statuses; inspected MITRE D3FEND's explicit non-efficacy caveat; independently recalculated joint probabilities, Boolean dependency cut sets, replication assumptions, and coverage implications; applied corrections to each substantive manuscript.  
**Disposition:** All four revised manuscripts qualify for **Reviewed (model-assisted) / Core claims checked**. This is a bounded technical source and logic review, **not** full source-passage verification, independent qualified human review, field testing, formal proof that real systems are secure, permanent taxonomy acceptance, or Published status.

## 1. SF-07-04 | Defense in Depth and Diversity

**Manuscript:** [Defense in Depth and Diversity](security-controls-defense-mechanisms/defense-in-depth-and-diversity.md)  
**Primary source basis:** [NIST SP 800-160v1r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), Appendix **E.9 Defense in Depth** (printed p. 88 / PDF page index 103), **E.11 Diversity (Dynamicity)** (printed p. 89 / index 104); [NIST SP 800-160v2r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf), Appendix **D.5.2.4–5** (printed pp. 125–126 / indexes 140–141), Table D-15 (printed p. 136 / index 151).

| Group | Material proposition or test | Second-pass finding, correction and limits |
| --- | --- | --- |
| 09-04-01 | Defense in depth is coordinated protection, not product count | **Pass.** NIST v1 E.9, visually inspected, names three pillars: successive barriers on loss scenarios, avoiding a single defensive point, and diversity of technical/operational/organizational barriers. A count of controls does not prove useful coordination or protection. |
| 09-04-02 | Coordinated mechanisms (active) and architectural arrangement (passive) differ | **Pass.** The inspected E.9 page explicitly separates active coordination from passive architecture. The working article describes their interaction without treating the NIST principle as a mandatory fixed number of layers or a deployed-system certification. |
| 09-04-03 | A nonempty path/barrier set is not a proof of prevention | **Pass after correction.** The authored \(\forall p\in\mathcal P_{\rm modeled},B(p)\ne\varnothing\) requires some claimed applicable mechanism on each modeled path. A detector that observes disclosure **after** it happens can satisfy this structure yet fail a preventive objective. The article now explicitly separates presence, function and effectiveness. |
| 09-04-04 | Diversity is about relevant variation and failure modes, not supplier branding | **Pass with source precision.** NIST v1 E.11 is named **Diversity (Dynamicity)**, not simply an unqualified claim of different products. NIST v2 D.5.2.5 specifically warns that different products can share hidden components and that diversity can enlarge attack surface, lifecycle cost and configuration inconsistency. Inspected both pages and corrected the name and limits. |
| 09-04-05 | Probabilities of passing two defenses need conditional evidence | **Recomputed.** If \(P(E_1)=.20\) and \(P(E_2\mid E_1)=.60\), \(P(E_1\cap E_2)=.12\) (12%). The naïve \(0.2\times0.2=.04\) requires independence not established. A consistent illustrative joint distribution with both bypassed .12, only E1 .08, only E2 .08, neither .72 gives each marginal .20. The corrected article now makes that feasibility explicit. |
| 09-04-06 | Logical layering can share a single common trust dependency | **Pass.** Authentication and object authorization might share a compromised identity provider, storage or administrative policy. Diversity of nominal functions does not guarantee independence, correct authorization or safety under actual failure. |
| 09-04-07 | Layering and redundancy have distinct goals and owners | **Pass.** SF-07-04 concerns coordinated loss barriers and defense architecture; SF-11-05 separately owns replicated critical function, shared failure mechanisms and continuity. Two identical servers may help service availability while preserving the same authorization flaw. This is an editorial ownership distinction, not an approved global ontology. |
| 09-04-08 | Cataloged controls or D3FEND techniques are not efficacy claims | **Pass.** [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/) explicitly states that its taxonomy does not prescribe, prioritize or characterize countermeasure effectiveness. [NIST SP 800-53 Rev. 5 Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) catalogs controls, whereas [SP 800-53A Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) provides separate assessment methods. Neither mere selection nor a green registry validates a real defensive layer. |

**Corrections applied:** Clarified the gap between structural barrier intersection and prevention, the precise name and source limits of E.11, and a consistent joint probability counterexample with dependent bypasses. The four-layer service sketch remains expressly hypothetical.

## 2. SF-07-05 | Control Placement and Coverage

**Manuscript:** [Control Placement and Coverage](security-controls-defense-mechanisms/control-placement-and-coverage.md)  
**Source basis:** NIST v1 E.9 (p. 88/index 103), [NIST SP 800-160v2r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf) **D.5.1.3 Reduce Attack Surfaces** (p. 115/index 130), [NIST SP 800-53 Rev. 5 SC-7](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

| Group | Material proposition or test | Second-pass finding, correction and limits |
| --- | --- | --- |
| 09-05-01 | Position, structural applicability and actual effect are different | **Pass.** A correctly operating safeguard may be absent from an alternate path; a well-positioned mechanism may be faulty. Placement and effect are independent requirements for a scoped protection claim. |
| 09-05-02 | Attack surfaces include internal and non-network exposures | **Pass with source check.** NIST v2 D.5.1.3, visually inspected on printed p. 115/index 130, explicitly covers external/internal access and development, operations, maintenance and supply-chain environments. The article now lists those boundary classes and does not equate attack surface with a public firewall interface. |
| 09-05-03 | The path coverage quantifier is a necessary structural model | **Pass after correction.** The authored \(C(p,s,t)\ne\varnothing\) for each modeled path/state/time allowed *either* observation *or* enforcement. The article now defines \(E(p,s,t)\) and \(O(p,s,t)\) separately. A claimed preventive requirement needs an **applicable enforcer** on each relevant path, and correct trustworthy enforcement beyond mere membership. These are conceptual necessary conditions, not sufficient certifications. |
| 09-05-04 | The invented four-path document example preserves control scope | **Pass with qualification.** P1 web, P2 internal worker, P3 maintenance and P4 offline backup can have different authorization/sensor boundaries. A database account identity check can be applicable while leaving end-user **object authorization unproved**. Added this explicit correction; “applicable” is not “effective.” |
| 09-05-05 | Complete mediation and SC-7 boundary protection are not identical | **Pass.** SC-7 addresses defined managed communication interfaces; it is not by itself universal application object mediation. NIST v1 also separates continuous protection from defense depth and trustworthy control. |
| 09-05-06 | Enforcement, detection, temporal and state coverage cannot be combined into one opaque score | **Pass.** Observation of encrypted metadata cannot establish observation of plaintext, and an alert after disclosure cannot retroactively block it. Missing records do not prove no event occurred without coverage/retention evidence. |
| 09-05-07 | SP 800-53A assessment is separate from selecting SP 800-53 controls | **Pass.** NIST's current SP 800-53A publication (Rev. 5, **Release 5.2.0 issued August 27, 2025**) describes distinct assessment objectives, examine/interview/test methods and tailoring; the design's control list does not establish its success outside the assessed conditions. |

**Corrections applied:** Separated the enforcement and observation predicates; qualified database credential checking versus end-user object authorization; added inspected attack-surface scope categories.

## 3. SF-07-06 | Control Bypass, Failure, and Evasion

**Manuscript:** [Control Bypass, Failure, and Evasion](security-controls-defense-mechanisms/control-bypass-failure-and-evasion.md)  
**Source basis:** [NIST SP 800-160v1r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf) Appendix E (including **Continuous Protection** and **E.9 Defense in Depth**); [NIST SP 800-160v2r1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf) coordinated protection; [MITRE ATT&CK Defense Evasion](https://attack.mitre.org/tactics/TA0005/); [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/).

| Group | Material proposition or test | Second-pass finding, correction and limits |
| --- | --- | --- |
| 09-06-01 | Bypass, control failure, evasion, misconfiguration and non-coverage are not synonyms | **Pass.** These editorial classes describe *why a claimed safeguard may not constrain an action*, not a source-prescribed exhaustive security ontology. A policy-authorized exception may skip an ordinary control without automatically constituting a security violation; the article now says this explicitly. |
| 09-06-02 | An absent alert has multiple technical explanations | **Pass.** No sensor, failed retention, absent rule, false-negative model, suppressed notification and no follow-up action have distinct evidentiary requirements. None automatically establishes that an adversary deliberately evaded detection. |
| 09-06-03 | Evasion is an actor-behavior hypothesis beyond observed non-detection | **Pass after clarification.** ATT&CK Defense Evasion concerns adversarial behavior designed to avoid security controls, not a classification automatically assigned to every non-matching event. The corrected article makes intentional adaptation an evidence-requiring inference. |
| 09-06-04 | Fail-open and fail-closed must be relative to specified property and legitimate exception policy | **Pass with caveat.** NIST v1 Continuous Protection recognizes intentionally disabling protection as an exception to the period protection is required; it does **not** authorize hostile override. The article now distinguishes source principle from legitimacy and specific stakeholder harms. |
| 09-06-05 | A normal/failed/constrained-recovery decision path illustrates distinct outcomes | **Pass with correction.** The hypothetical payment approver's fail-closed mode may block unauthorized approvals *under that particular authorization boundary*, while harming availability. It does not prove all system confidentiality, integrity or safety requirements remain valid. Fail-open keeps service moving but abandons that authorization assertion. |
| 09-06-06 | Shared policy, identity and collection dependencies can undermine several safeguards | **Pass.** Two sensors using one queue may both lose usable records if the shared queue fails even when sensor devices still run. SF-11-05 owns the common-mode/replication analysis; SF-07-06 owns what failed in the individual claimed control. |
| 09-06-07 | Catalog and assessment methods cannot establish universal protection | **Pass.** D3FEND expressly disclaims efficacy evaluation; SP 800-53A's examine/interview/test methods produce bounded evidence, not proof outside their conditions. Operational test procedure ownership remains in Operational Foundations. |

**Corrections applied:** Separated authorized exceptions from bypass violations; made “evasion” a deliberate behavior hypothesis rather than a synonym for false negative; limited the claim about intentional overrides; narrowed the hypothetical fail-closed outcome to the authorization property actually modeled.

## 4. SF-11-05 | Redundancy, Diversity, and Common-Mode Failure

**Manuscript:** [Redundancy, Diversity, and Common-Mode Failure](security-failure-resilience/redundancy-diversity-and-common-mode-failure.md)  
**Source basis:** [NIST SP 800-160v1r1 E.26 Redundancy](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), printed p. 98/index 113, visually inspected; [NIST SP 800-160v2r1 D.5.2.5 Plan and Manage Diversity](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf), printed p. 126/index 141, and **D.5.2.6 Maintain Redundancy**, p. 127/index 142; Table D-15 printed p. 136/index 151.

| Group | Material proposition or test | Second-pass finding, correction and limits |
| --- | --- | --- |
| 09-11-01 | Redundancy, diversity and defense in depth are different design objectives | **Pass.** E.26 defines redundancy through replicated functions/elements and warns about common-mode failure. E.9 concerns coordinated barriers along loss scenarios. An identical second server may support availability without improving confidentiality/integrity. |
| 09-11-02 | Shared dependency can defeat two redundant branches | **Pass with complete Boolean check.** \(S=C\land(A\lor B)\) implies \(\neg S=\neg C\lor(\neg A\land\neg B)\). Independently enumerated all **eight** Boolean assignments; loss and \(\neg S\) match throughout. Minimal failure cut sets under this model: **{\(\neg C\)}** and **{\(\neg A,\neg B\)}**. No failure rate is implied by the Boolean identity. |
| 09-11-03 | Independence is an assumption, not a consequence of having two replicas | **Pass.** For independently available A and B, each with \(P(A)=P(B)=.9\), \(P(A\lor B)=1-(.1)^2=.99\). Marginals alone do not establish the independence of their failure events. |
| 09-11-04 | A third shared dependency can reduce effective modeled service availability | **Recomputed.** With \(P(C)=.95\) and C independent of the **union A-or-B event**, \(P(S)=.95\times.99=.9405\), or **94.05%**. Clarified that independence from the A/B state vector suffices but is not established by the component availability numbers. No deployed service measurements are inferred. |
| 09-11-05 | Identical marginal replica availability can coexist with complete failure dependence | **Recomputed countermodel.** If A and B are available or unavailable together, each still with marginal .9, \(P(A\lor B)=.9\), not .99; with C independent at .95, \(P(S)=.95\times.9=.855\) (**85.5%**). Added this direct contradiction of the false “two copies multiply reliability” inference. |
| 09-11-06 | Common mode, common cause and statistical correlation differ | **Pass with terminology correction.** NIST v1 E.26 describes one event causing multiple same/equivalent elements to fail in the **same manner**. A common cause can yield different symptoms, and observed statistical correlation alone does not identify a cause. |
| 09-11-07 | Source explicitly warns about homogeneous malware propagation, apparent diversity and shared resources | **Pass with direct page verification.** Inspected NIST v2 **D.5.2.6**, p. 127/index 142: redundancy may enhance availability but must protect spare resources; homogeneous malware can propagate, and design must examine single failure points/shared dependencies. D.5.2.5 p. 126/index 141 notes diverse products may hide identical components or introduce new attack surfaces. Added the previously omitted D.5.2.6 source. |
| 09-11-08 | Voting/consensus and successful continuation do not establish integrity under malicious faults | **Pass.** Three identical faulty outputs can agree while being wrong; an availability failover may restore function but share a compromised policy. No Byzantine-fault-tolerance claim is supported without a specified protocol, fault and synchrony model. |
| 09-11-09 | Redundancy and failure-dependency owner is distinct from defensive barrier design | **Pass.** SF-11-05 concerns replicated function, shared failure causes, diversity and acceptable continuation; SF-07-04 concerns the organization and coordination of safeguards against defined losses. SF-02-04 owns generic dependency logic; SF-11-07 owns trusted restoration. These are **provisional editorial** ownership decisions, not permanent taxonomy ratification. |

**Corrections applied:** Added direct NIST v2 redundancy section and page, source-scoped common-mode definition, fully described the independence assumptions, verified the Boolean cut sets, and introduced the perfectly correlated-replica countermodel.

## Independent mathematical and logical verification

### 1. Joint bypasses

Given \(P(E_1)=.2\), \(P(E_2\mid E_1)=.6\):

\[
P(E_1\cap E_2)=P(E_1)P(E_2\mid E_1)=.12.
\]

One coherent joint distribution with marginal \(P(E_1)=P(E_2)=.2\) is:

| Event state | Probability |
| --- | ---: |
| E1 and E2 | 0.12 |
| E1 only | 0.08 |
| E2 only | 0.08 |
| Neither | 0.72 |
| **Total** | **1.00** |

Under these values, \(P(E_2\mid E_1)=.12/.2=.6\). Naïve multiplication of the two .2 marginals gives .04 and is invalid because the events are dependent. All these probabilities are **invented for a mathematical counterexample**.

### 2. Replication and common prerequisites

Under the Boolean service model, \(S=C\land(A\lor B)\), De Morgan's law gives \(\neg S=\neg C\lor(\neg A\land\neg B)\). Exhaustive evaluation of 8 input tuples confirmed this identity; the two minimal failure cut sets above follow when A, B, C denote functioning prerequisites.

With independent replica availability events at .90 each:

\[
P(A\lor B)=1-P(\neg A\land\neg B)=.99.
\]

If C is available with probability .95 and independent of that union:

\[
P(S)=.95\times.99=.9405.
\]

If A and B instead always fail together, each retains .90 availability but their union has probability .90. With C still independent, \(P(S)=.95\times.90=.855\). This shows why marginals, independence, and common prerequisites are distinct model inputs. It **does not** measure a real architecture, a real attacker or an acceptable service level.

### 3. Coverage as a scoped relation

The path-coverage predicates in SF-07-04 and SF-07-05 express **applicability**, not prevention effectiveness. A nonempty *sensor* set on a modeled path can coexist with zero applicable *enforcement* controls. An application authorization control that does not traverse an administrative route can function perfectly and still fail the system-wide protection claim. No graph completeness, sensor fidelity or correctness is established by a symbolic quantifier.

## Source register and uncompleted gates

- [NIST SP 800-160 Vol. 1 Rev. 1, November 2022](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Appendix E.9, E.11 and E.26, visually inspected at printed pp. 88, 89 and 98.
- [NIST SP 800-160 Vol. 2 Rev. 1, December 2021](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), Appendix D.5.1.3, D.5.2.4–6, and D-15, visually inspected at printed pp. 115, 125, 126, 127 and 136.
- [NIST SP 800-53 Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), control catalog; [NIST SP 800-53A Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), assessment procedures (NIST notice August 27, 2025). A control's presence and successful assessment within defined scope do not establish all-system security.
- [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/), explicitly nonprescriptive and not effectiveness-evaluating; [MITRE ATT&CK Defense Evasion](https://attack.mitre.org/tactics/TA0005/), adversary-behavior classification, not automatic proof of intent.

**Remaining limitations:** Full claim-by-passage verification across every source, qualified independent human peer review, observed failure frequencies, deployed architecture testing, complete path inventories, field-based loss and effectiveness measures, Byzantine fault tests, and approval of the working knowledge-area taxonomy have **not** been performed. The structural validation workflow tests registration and links, **not** the truth of scientific claims. No other candidate article inherits this review, and previously completed audit scopes remain historical.

**Development transition justified:** SF-07-04, SF-07-05, SF-07-06 and SF-11-05 individually advance **Draft → Reviewed (model-assisted)** and **References listed → Core claims checked**, based on these **31 separate material claim groups**. Prior Technical Reviews 01–08 contain **179** recorded claim groups across 29 Reviewed articles; this audit brings the total to **210 groups across 33 Reviewed manuscripts**, **0 Draft**, **63 Inventoried without article**. These numbers are a review ledger, not a measure of publication readiness.

[Security Foundations](README.md) · [Working Article Register](pilots/README.md) · [Development/Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Working Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md)
