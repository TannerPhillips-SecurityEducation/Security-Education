# Control Placement and Coverage

**Candidate subject:** SF-07-05 · Security Controls & Defense Mechanisms  
**Working area:** [Security Controls & Defense Mechanisms](README.md) · Fundamentals-style article placement adopted; subject taxonomy provisional  
**Artifact:** Substantive working knowledge reference, not a final canonical publication or network-hardening guide  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 09](../PILOT-TECHNICAL-REVIEW-09.md), 7 article-specific material claim groups; full source verification and independent expert acceptance pending  
**Authority:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership register](../CANONICAL-OWNERSHIP-REGISTER.md) · [Coverage review SG-08](../COVERAGE-AND-GAPS-REVIEW-03.md)

## An effective control in the wrong place cannot protect an omitted path

A control can correctly enforce its assigned policy yet provide no protection against an action that never passes through it. **Control placement** concerns where a safeguard is situated relative to protected assets, interactions, transitions and trust boundaries. **Control coverage** concerns which declared scenarios, system states, interfaces, paths and operating modes fall within that safeguard's applicable enforcement or observation scope.

These concepts differ from **control effectiveness**, which asks whether a control actually achieved its intended protective effect under the tested conditions. A well-positioned but defective authorization check may have claimed coverage without effective protection. A perfectly functioning check can be irrelevant to an alternate interface that bypasses it.

[NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Appendix E §E.9 (printed p. 88 / PDF index 103), frames defense in depth around lines of defense along **loss scenarios**. [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), Appendix D §D.5.1.3 (**printed p. 115 / PDF index 130, visually re-inspected**), includes external, internal, development, operations, maintenance and supply-chain dimensions in the attack-surface discussion. Thus a public network boundary is not a complete model of where security controls may need to apply.

## The anatomy of a control placement claim

At minimum, the claim should identify:

| Dimension | Technical meaning | Example of an unresolved question |
| --- | --- | --- |
| Protected operation | What action or state transition requires mediation? | Does access to plaintext require authorization every time? |
| Subject and authority | Which principals, system processes or roles may initiate it? | Can a background worker use the same privilege path? |
| Resource boundary | Which object, interface, environment or dependency is being protected? | Is a backup copy inside the same policy boundary? |
| Entry and exit surfaces | How can a request or result cross the boundary? | Does the rule mediate an administrative API? |
| Control position | Where is the relevant decision or sensor applied? | Is the check before data disclosure or after it? |
| Enforcement state | Which configurations, failover modes and exceptions preserve the function? | Is there an emergency mode with different privileges? |
| Observer scope | Which activity is visible to telemetry and for how long? | Are internal transfers monitored, or only edge traffic? |
| Evidence | Which tests and records support applicability and actual effect? | Were denied operations tested through every modeled path? |

This matrix is an editorial aid, not a NIST-mandated inventory schema. It does not provide an assessment procedure, which belongs to [Operational Foundations](../../operational-foundations/README.md).

### Protection must be evaluated over state and time

A safeguard's placement cannot be evaluated only from one architecture diagram. Maintenance, recovery, changeover, cache warmup, emergency operation and delegation can alter the resource-access graph.

Define a modeled set \(\mathcal{P}(s,t)\) of possible paths for a protected action in system state \(s\) at time \(t\). Let \(C(p,s,t)\) denote the set of safeguards that are **structurally applicable** to path \(p\) under those conditions, whether they enforce or merely observe. Separately, \(E(p,s,t)\) is the subset with **applicable enforcement capability** and \(O(p,s,t)\) is the subset with **applicable observation capability**. Their required behavior must be verified rather than inferred from position alone.

A minimal *structural applicability* requirement is:

\[
\forall (s,t)\in\mathcal{D},\ \forall p\in\mathcal{P}(s,t),\quad C(p,s,t)\neq\varnothing,
\]

where \(\mathcal{D}\) is the explicitly declared state/time scope. This authored expression is not a formal compliance test or a theorem that the modeled \(\mathcal P\) is complete. It also says nothing about *whether the present control responds correctly*.

If a policy requires every unauthorized read to be blocked, a detector that merely observes the read does not satisfy that policy even when it covers every path. A stronger **structural necessity** for that prevention claim is \(E(p,s,t)\ne\varnothing\) for every relevant unauthorized-read path in the declared scope. **Even that condition is not sufficient**: the applicable enforcement controls must make the correct decisions and remain trustworthy under the tested conditions. The **function** of each safeguard must match the protection objective.

## Worked coverage matrix: document service

Consider an invented application with a protected document stored in a database. Three modeled access paths and three controls are:

- **C1**: gateway filtering of external requests, enforcing a source/protocol policy;
- **C2**: object-level authorization by the application;
- **C3**: database credentials restricted to specific service identities.

| Modeled path | C1 gateway | C2 object authorization | C3 database identity restriction | Scope observation |
| --- | --- | --- | --- | --- |
| P1: external web request through application | Applicable | Applicable | Applicable | Several barriers, but each has a different decision scope |
| P2: scheduled internal export worker | Not traversed | Unknown until specified | Applicable | Gateway is irrelevant; object permissions need independent review |
| P3: emergency database maintenance | Not traversed | Not traversed | Applicable under its special role | Privileged legitimate operations have a different policy and risk |
| P4: offline backup restore | Not traversed | Not traversed | May not apply to restored copy | An additional protection boundary may be required |

The table describes **intended applicability**, not demonstrated effect, and treats C3 as a *database identity check*, not an object-authorization system. A valid service account can reach data on behalf of a user whom that service has not properly authorized. C3 allowing an authorized database account to retrieve a record is therefore not proof that every returned document is authorized to its ultimate recipient. P4 may be entirely missing from a design diagram centered only on live requests.

This case illustrates why one component can be correctly implemented and still fail to cover a policy claim that was stated too broadly.

## Coverage is path-relative and property-relative

A control that blocks communications across one network interface may not constrain data stored on a removable drive. An integrity check can be useful for tampering but does not automatically keep the checked bytes confidential. A sensor that observes TLS connection metadata may not observe protected application content.

Consequently, coverage should be stated as a relation among **a property**, **an adverse scenario**, **a path**, and **the specific control response**. Claims that a product "covers the network" or "protects all endpoints" are too broad without the network boundary, supported protocols, deployed agents, bypass routes, fail conditions and evidence.

One control may also be **logically placed** at a point but **temporally too late** to prevent loss. An asynchronous alert after an unauthorized disclosure can support investigation or later containment; it cannot retroactively prevent the first disclosure.

The reviewed [Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md) article owns these service distinctions. [Defense in Depth and Diversity](defense-in-depth-and-diversity.md) owns why multiple coordinated barriers may be justified. This article owns their **spatial and logical applicability**.

## Managed boundaries versus complete mediation

[NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) includes **SC-7 Boundary Protection**, which concerns managed interfaces at external boundaries and key internal interfaces. The current published minor release **5.2.0 (August 2025)** updates the control catalog as recorded on the official publication page; it should not be confused with a universal rule requiring every internal access to pass through one firewall.

Complete mediation is a stronger security-design principle: all relevant protected actions should be checked against the applicable authority decision at the appropriate point. A boundary firewall is one possible mechanism for selected communication flows. Application authorization, resource-owner policy, physical controls and service-to-service identity restrictions may be required for other flows.

NIST SP 800-160 Vol. 1 Rev. 1 distinguishes **Trustworthy System Control**, **Continuous Protection** and **Defense in Depth** as separate engineering concepts in Appendix E. A control's existence at a network edge does not establish either complete mediation or continuous protection through every operating mode.

## Observation coverage and enforcement coverage are distinct

A security sensor can observe a subset of events, while an enforcement component can reject a subset of attempted actions. Their limits may differ.

| Claim | Meaning | What requires separate evidence |
| --- | --- | --- |
| Coverage of inputs | Which requests or flows reach the control | The declared path set is complete |
| Detection coverage | Which relevant behaviors are observable and classified | Reliability of detection under other workloads or evasion |
| Enforcement coverage | Which actions can actually be permitted or denied | Correct and authorized decisions in every relevant mode |
| State coverage | Whether function persists during fault, failover and recovery | Protection of the transition itself |
| Temporal coverage | Whether control applies when the protected event occurs | Synchronized policy rollout and timely observation |
| Trust coverage | Whether a trustworthy identity, policy, sensor or key supports the decision | The control's own dependencies are not compromised |

For example, a packet-collection system may see most external traffic but miss lateral movement over an unsupported link, local memory access or end-to-end encrypted content. Increasing packet visibility can improve some detection opportunities but cannot by itself prove that access-control decisions were enforced.

An absence of records is weak evidence of absence unless retention, sensor health and query coverage are established. [Observable, Observed, and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) owns this epistemic boundary.

## A structural test cannot certify effectiveness

Imagine an audit finds that all four *known* paths pass at least one documented security control. That is a useful topology finding, but it does not prove:

1. all possible paths have been discovered;
2. the controls enforce the right properties;
3. trust dependencies are sound and available;
4. the controls behave correctly under attacked or degraded conditions;
5. the collected records truthfully reflect the relevant events.

[NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) describes assessment procedures and methods such as examine, interview and test; it is distinct from the SP 800-53 control catalog. A selected control, even with correct architecture placement, is not self-validating.

The requirement to substantiate coverage belongs to the assurance argument. This article defines the *meaning* and model limits; actual assessments and operational monitoring belong to Operational Foundations.

## Source relationships and outstanding review

- [Defense in Depth and Diversity](defense-in-depth-and-diversity.md) owns coordination of barriers, not the claim that every path has been covered.
- [Control Bypass, Failure, and Evasion](control-bypass-failure-and-evasion.md) owns why nominally placed controls may not mediate or detect the relevant activity.
- [Redundancy, Diversity, and Common-Mode Failure](../security-failure-resilience/redundancy-diversity-and-common-mode-failure.md) owns whether shared dependencies defeat alternative paths.
- [Attack Paths, Stages, and Dependencies](../threats-hazards-adversarial-behavior/attack-paths-stages-and-dependencies.md) owns proposed adversarial transitions, not control correctness.
- [Information-Flow Security and Noninterference](../secure-design-architecture/information-flow-security-and-noninterference.md) owns policy-level information influence.
- [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns claims, evidence and uncertainty.
- [Fundamentals: Models & Abstraction](../../fundamentals/models-abstraction/README.md) owns general abstraction semantics; [Operational Foundations](../../operational-foundations/README.md) owns coverage testing and deployment.

**Primary source starting points:**
- [NIST SP 800-160 Vol. 1 Rev. 1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), Appendix E **E.9 Defense in Depth** (printed p. 88 / PDF index 103), and adjacent continuous-protection and trustworthy-control principles. Source pages visually inspected.
- [NIST SP 800-160 Vol. 2 Rev. 1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf), Appendix D **D.5.1.3 Reduce Attack Surfaces**, printed p. 115 / PDF index 130, verified in the rendered primary source.
- [NIST SP 800-53 Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), SC-7 boundary protection and control-family context; [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), assessment rather than listing.
- [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/), countermeasure technique relationships, explicitly not a proof of effectiveness or prescriptive prioritization.

**Editorial limitations:** The paths, controls, set notation and table are invented and not a demonstration of an actual system, complete path inventory or correctly enforced protection. No assumption that every threat uses a network interface is justified. [Technical Review 09](../PILOT-TECHNICAL-REVIEW-09.md) separately documents seven material claim groups, including inspected attack-surface source text and the corrected enforcement-versus-observation coverage distinction. This article is **Reviewed (model-assisted) / Core claims checked**, not a proof of comprehensive real-world path coverage, fully source-Verified, independently accepted, taxonomy-ratified or Published.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
