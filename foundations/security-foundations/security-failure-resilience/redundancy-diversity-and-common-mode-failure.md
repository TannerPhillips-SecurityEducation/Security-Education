# Redundancy, Diversity, and Common-Mode Failure

**Candidate subject:** SF-11-05 · Security Failure & Resilience  
**Working area:** [Security Failure & Resilience](README.md) · Approved Fundamentals-style directory placement; specific semantic ownership provisional  
**Artifact:** Substantive cross-domain working reference, not a final canonical publication or an availability engineering runbook  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 09](../PILOT-TECHNICAL-REVIEW-09.md), 9 article-specific material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [SG-08 gap and overlap finding](../COVERAGE-AND-GAPS-REVIEW-03.md) · [Working ownership](../CANONICAL-OWNERSHIP-REGISTER.md)

## More copies do not guarantee a more trustworthy system

A system can be replicated, geographically separated and apparently highly available while every replica shares the same security weakness, credential, update channel or policy error. Conversely, multiple independent protective controls may make an unauthorized action harder without providing any continued service after one entire component fails.

**Redundancy** provides additional instances of a capability, component, data item or path so a system can continue to satisfy a requirement if one element becomes unavailable or unsuitable. **Diversity** uses meaningful differences among components, implementations, environments, control flows or operations to reduce the likelihood that one cause affects them in the same way. **Common-mode failure** occurs when one event or mechanism produces equivalent failures across replicated elements. **Common-cause dependencies** can make failures correlated even when the individual components look independent.

These ideas overlap but answer different questions:
- **Redundancy:** Can another instance provide required function after a specific failure?
- **Diversity:** Are alternatives sufficiently different under the relevant threat and failure mechanisms?
- **Independence:** Can a failure of one component occur without automatically causing failure of the other under the declared model?
- **Trustworthiness:** Does the alternative preserve the required authorization, integrity, confidentiality, safety and provenance properties?
- **Continuity:** Does the organization still obtain the required capability in the relevant time and operating mode?

[NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Appendix **E.26 Redundancy**, printed p. 98 / PDF index 113, explicitly states that replicated functions/paths require a combination strategy, such as failover, concurrent use, voting, agreement or consensus, and warns that redundant elements are susceptible to common-mode failure. The next sentence identifies **diversity as a means to address** that concern, not an automatic proof it has been eliminated.

This article owns **system-level replication, diversity and common-mode dependence**. The related [Defense in Depth and Diversity](../security-controls-defense-mechanisms/defense-in-depth-and-diversity.md) (SF-07-04) owns **coordinated protective barriers**, which can use diversity without necessarily requiring redundant execution of a service.

## Replica, redundant path, backup and protective barrier are different

| Mechanism | What it could contribute | Important missing claim |
| --- | --- | --- |
| Two active service instances | Continued service after loss of one instance | Both enforce the correct authorization policy |
| Independent network routes | Delivery if one route is unavailable | Both have equivalent security/identity treatment |
| Replicated database | Availability or recoverability of data copies | Corrupted or unauthorized data does not propagate to all replicas |
| Offline protected backup | Historical data recovery after specified failures | Backup was unmodified, accessible and restorable to a trusted state |
| Independent policy engine | Alternate authorization decision path under some failures | Policies and trust inputs are independently correct |
| Two security sensors | Additional observation vantage or coverage | Both observe the same protected events, or their evidence is independent |
| Diverse software implementations | Reduced susceptibility to one implementation-specific defect | Shared specification, dependency or operator error cannot compromise all |

Each row is **a conditional capability**, not a universal property of its category. Copies can be stale, corrupted, misconfigured or unavailable. A second component can add complexity and new attack surfaces.

[NIST SP 800-160 Vol. 2 Rev. 1 (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), Appendix D **§D.5.2.5 Plan and Manage Diversity**, printed p. 126 / PDF index 141, explicitly warns that apparently diverse products may share underlying components, and that genuine diversity can increase attack surface, cost and configuration inconsistency. **§D.5.2.6 Maintain Redundancy**, printed p. 127 / PDF index 142, additionally requires attention to **single points of failure and shared resources** and warns that malware can propagate across homogeneous replicas. These passages were re-inspected in the rendered source. Diversity must be considered in relation to the **common failure mechanisms** the design is attempting to avoid.

## Service-continuation topology and shared dependencies

For a toy model, define two service replicas A and B with an alternative relationship, but both need a common control component C:

\[
S=C\land(A\lor B).
\]

The system cannot provide its modeled service unless C works and at least one of A or B works. Its logical loss condition is

\[
\neg S=\neg C\lor(\neg A\land\neg B).
\]

Under this particular Boolean model, the minimal failure cut sets are \(\{\neg C\}\) and \(\{\neg A,\neg B\}\). **The replicated A/B pair does not remove the single-point dependence on C.** The identity follows by De Morgan's law, and all eight Boolean assignments of A, B and C give the matching complement. The identity is **logical**, not a derivation of failure probabilities or a claim that each component's health is independent.

~~~text
                        Required capability S
                        /                \
                 Replica A              Replica B
                        \                /
                         \              /
                       Shared dependency C
                    identity / policy / storage
                       / monitoring / power
~~~

The sketch is a simplified dependency argument, not a measured architecture or claim that every shared identity service is untrustworthy. C may be essential only for some functions or operating states. A real service may have cached policies, degraded alternatives, timeouts or failure behavior that requires a different model.

[Value, Criticality, and Dependencies](../protected-interests-assets-harm/value-criticality-and-dependencies.md) already owns the *general dependency relation and the same Boolean cut-set form*. This article applies that relation specifically to **replication, common-mode failure and continued trustworthy operation**, without creating a duplicate owner of graph theory.

## A quantitative counterexample to naïve replication claims

Assume **hypothetically** that:
- Replica A is available with probability \(0.90\) over a defined observation interval.
- Replica B is available with probability \(0.90\) over the same interval.
- Their availability events are **independent**.
- At least one available replica is sufficient for the service.
- All other prerequisites are initially ignored.

Then

\[
P(A\lor B)
=1-P(\neg A\land\neg B)
=1-(0.10)^2
=0.99.
\]

This gives **99% modeled service availability**, not a forecast of a real service or proof of secure behavior.

Now suppose both replicas require a shared component C with availability \(0.95\), and **C is independently available relative to the A/B pair** under this toy distribution. The service-success condition is \(C\land(A\lor B)\):

\[
P(S)=P(C)\,P(A\lor B)
=0.95\times0.99
=0.9405.
\]

The result is **94.05% modeled service availability**. The multiplication requires C's availability to be **independent of the union event (A or B)**, which the stipulated independence of C from the full A/B state vector guarantees. It is not justified by the separate marginal percentages alone. The shared dependency C can dominate the benefit of replication even when each replica is relatively available.

**Countermodel:** If A and B's failures always coincide, while both still have 90% marginal availability, then \(P(A\lor B)=0.90\), *not* 0.99. If C is independently available at 0.95, the modeled overall availability becomes \(0.95\times0.90=0.855\), or **85.5%**. Identical marginal percentages therefore cannot establish independent redundancy. These figures are not empirical measurements, NIST-defined thresholds, or universal availability formulas. The independence assumptions are **part of the example**, not something established by writing an equation. If A and B share an unmodeled vulnerability, supplier or administrative action, they may fail together more often than the simple independent model predicts. A causal or probabilistic analysis requires appropriate system-specific evidence.

It is also incorrect to infer confidentiality or integrity from the availability number. Two highly available replicas can **both consistently return unauthorized data** under the same flawed policy.

## Common mode is not simply "correlation"

A **common-mode failure** is a single event or failure mechanism causing two or more equivalent elements to fail **in the same or equivalent manner**, consistent with NIST SP 800-160v1r1 E.26 (printed p. 98 / PDF index 113). A **common cause** can affect several resources without necessarily producing identical failure modes. **Correlation** is a statistical relationship among observed states, not identification of the common cause or proof of how it propagated. The two are connected but not equivalent.

A shared administrative credential could permit unauthorized changes to A and B. A common update might deploy the same defect. An electrical fault might disrupt a shared power supply. Those are candidate shared causal mechanisms.

If two independent systems experience outages at the same time during a public incident, the temporal correlation alone does not establish which shared mechanism caused it. Conversely, an unobserved common cause may exist even when available samples are insufficient to show a significant statistical correlation.

An adequate statement needs:
- the specified function or security property;
- which replicated resources are assumed interchangeable;
- which components and trust roots are shared;
- how the assumed source could affect both;
- whether the failure is simultaneous, sequential or propagated;
- evidence connecting the source to the effects;
- what alternative operation remains acceptable after the failure.

NIST's engineering warning about common mode should not be misconstrued as a proof that every redundant design is insecure. It is a design-risk distinction requiring actual verification.

## Diversity, heterogeneity and independence have different scopes

Diversity can exist in architecture, implementation, supply chain, geography, administrator authority, network transport, timing, data formats or recovery paths.

**Architectural diversity:** two systems implement the same service using meaningfully different internal designs. Their differences might reduce identical failure conditions but introduce different interfaces and costs.

**Implementation diversity:** separate codebases or runtime choices may avoid some shared defects. They can still share a vulnerability if derived from the same insecure specification.

**Geographic diversity:** separation can protect against localized physical hazards. It does not guarantee independence of cloud administration, DNS, credential authority, deployment pipeline or software update source.

**Administrative diversity:** different privileged identities and approval paths can reduce the effects of one compromised account, but a shared identity provider or unprotected emergency account may reintroduce common dependence.

**Supply-chain diversity:** separate vendors can reduce some concentration risks, but both may include the same subcomponents or dependencies.

**Data/backup diversity:** multiple versions and immutable or offline copies may mitigate rapid propagation of corrupted data. They do not prove that a backup is correct, authorized to restore, or free from persistent adversarial changes.

Diversity can reduce particular failure correlations **while increasing operational complexity and new exposure paths**. NIST SP 800-160 Vol. 2 Rev. 1 §D.5.2.5 specifically calls attention to this tradeoff and the possibility of merely *apparent* diversity.

## Fault tolerance, failover, voting and integrity

Replicas must be **used according to a design**, not merely created. Relevant arrangements include:
- active/standby failover;
- load-balancing among equivalent service instances;
- concurrent execution with voting or consensus;
- backup and restore with integrity/provenance checks;
- geographically separated or functionally alternative recovery capability.

These arrangements have different properties. Voting over three identical corrupted outputs may preserve **consensus without correctness**. A standby instance configured with the same excessive privilege may preserve **availability without authorization**. A replicated database can rapidly propagate authorized changes and unauthorized corruptions alike.

A majority rule can help under specific fault assumptions, but it is not universally a Byzantine-fault-tolerant protocol. The result depends on the assumed number and type of faulty replicas, network synchrony, membership integrity, authenticated communication and the actual consensus algorithm. Without those details, describing “three instances and a majority” does not prove integrity under malicious faults.

The security claim is consequently not only "can the system continue?" but "can it continue to satisfy the **right** property, in the **right state**, using **trustworthy inputs and dependencies**?"

## Redundancy can interact with defensive layering

Some designs coordinate different defensive mechanisms along one loss scenario. Others replicate one critical protection mechanism so that it remains available after localized failure. A resilient system may require both, but these are different design obligations.

For example, duplicating an authentication service may preserve its availability. Requiring both authentication and resource-level authorization may provide distinct decision layers. If both decisions depend on the same erroneous identity binding, neither duplication nor layering alone proves effective protection.

[Defense in Depth and Diversity](../security-controls-defense-mechanisms/defense-in-depth-and-diversity.md) owns **coordinated safeguards and loss barriers**. This SF-11-05 article owns **replication, alternative operation, shared dependencies and failure diversity**. The working owners are distinct, consistent with [Gap Review SG-08](../COVERAGE-AND-GAPS-REVIEW-03.md); the precise subject names remain provisional until governance accepts them.

## State, restoration and evidence limitations

A working backup service does not establish that restored data is trustworthy. A successful failover at 10:00 does not mean every transaction had the intended authorization or that no attacker persisted in the replacement instance.

[Recovery Objectives and Trusted Restoration](recovery-objectives-and-trusted-restoration.md) owns RTO/RPO/MTD and assurance that restored state is acceptable. [Resilience, Survivability, and Robustness](resilience-survivability-and-robustness.md) owns whole-system capacities to anticipate, withstand, recover and adapt to adverse conditions. [Compromise and Loss of Security](compromise-and-loss-of-security.md) owns the boundary of actual security compromise.

This article adds the **mechanism-level understanding of repeated function and failure dependence**. It does not prescribe backup runbooks, deployment architectures, configuration settings or incident operations.

## Canonical relationships and primary sources

- [Defense in Depth and Diversity](../security-controls-defense-mechanisms/defense-in-depth-and-diversity.md): coordinated protective layers rather than replicated function.
- [Control Placement and Coverage](../security-controls-defense-mechanisms/control-placement-and-coverage.md): which interfaces and state paths a control covers.
- [Control Bypass, Failure, and Evasion](../security-controls-defense-mechanisms/control-bypass-failure-and-evasion.md): specific reasons protective functions are not delivered.
- [Value, Criticality, and Dependencies](../protected-interests-assets-harm/value-criticality-and-dependencies.md): general security-dependent criticality and Boolean cut sets.
- [Resilience, Survivability, and Robustness](resilience-survivability-and-robustness.md): overarching cyber-resilience and system-survivability objectives.
- [Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md): domain-neutral reliability mathematics and failure semantics.
- [Operational Foundations](../../operational-foundations/README.md): actual architecture, continuity, migration, testing and risk-assessment procedures.

**Primary source starting points:**
- [NIST SP 800-160 Vol. 1 Rev. 1 (2022)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), Appendix **E.26 Redundancy**, printed p. 98 / PDF index 113. The original page, including its warning about common mode and mention of diversity, was visually inspected.
- [NIST SP 800-160 Vol. 2 Rev. 1 (2021)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf), Appendix D **§D.5.2.5 Plan and Manage Diversity** (printed p. 126 / PDF index 141), **§D.5.2.6 Maintain Redundancy** (printed p. 127 / PDF index 142), and **Table D-15** (printed p. 136 / PDF index 151). The inspected primary pages warn about apparent diversity, propagation across homogeneous resources, shared dependencies and increased attack surface.
- [NIST SP 800-53 Rev. 5 / Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), control-catalog context; [SP 800-53B Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final), federal baseline/tailoring context, not empirical system resilience.
- [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), actual assessment-method framework distinct from the existence of redundant components.

**Editorial limitations:** A/B/C logic, invented probabilities, diagrams and case examples depend on explicit simplifying assumptions. They do not establish measured availability, correlated-failure probabilities, secure replication, Byzantine tolerance, or a real-world recovery guarantee. The separate [Technical Review 09](../PILOT-TECHNICAL-REVIEW-09.md) checks nine bounded material claim groups, the NIST source pages, complete Boolean logic, independence assumptions and the new correlated-failure countermodel. The manuscript is **Reviewed (model-assisted) / Core claims checked**, not empirical system availability evidence, formal proof of Byzantine tolerance, full source verification, independent expert acceptance, canonical ratification or Published.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
