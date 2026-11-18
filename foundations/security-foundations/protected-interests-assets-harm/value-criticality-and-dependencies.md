# Value, Criticality, and Dependencies

**Candidate subject:** SF-02-04 · Protected Interests, Assets & Harm  
**Working area:** [Protected Interests, Assets & Harm](README.md) · Adopted Fundamentals-style directory, provisional concept ownership  
**Artifact:** Substantive working article; not source-Verified or Published  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md), six article-specific material claim groups; complete source verification and qualified independent acceptance pending  
**Working authority:** [Subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)

## Importance depends on purpose, loss and relationships

An asset's **value** is its context-dependent importance or benefit to stakeholders, systems or missions. **Criticality** describes how consequential that asset's loss, degradation or unacceptable behavior would be for a relevant capability or interest under stated conditions. A **dependency** is a relationship in which satisfying some function, need or protection assumption requires something else to hold or be available.

A large acquisition price does not necessarily imply high functional criticality. An inexpensive digital certificate, a time source, or a single policy rule may enable high-consequence failure because other functions depend on it. Conversely, an expensive nonessential display can be readily bypassed without substantially affecting a mission.

The three concepts answer different questions:

| Concept | Distinguishing concern | What it does not establish |
| --- | --- | --- |
| Asset value | Why a stakeholder or system cares about an asset | Exact consequences of every possible failure |
| Criticality | Consequences of losing a function, property or asset under a defined context | Intrinsic universal priority or a measured attack probability |
| Dependency | Conditions or components necessary to achieve an outcome | That all dependency failures cause the same consequence |
| Replaceability | Whether and how a required function can be substituted | That substitution is safe, trusted, timely or affordable |
| Exposure | Whether an adverse condition can reach a relevant path | That the asset is necessarily vulnerable or compromised |

[NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Chapter 3 §§3.6–3.7, connects protection needs to asset loss consequences, system-design dependencies, criticality and priority. Its §3.7, printed pp. 25–27, emphasizes that asset importance changes across lifecycle stages, system states and the interests of those who value it. It is a source for the **conceptual distinction**, not a quantitative algorithm for scoring every asset.

## Direct importance and derived criticality

**Direct importance** can arise because an asset itself embodies a protected interest: sensitive information needs confidentiality, a person needs bodily safety, a record needs integrity, or a capability is needed by its intended beneficiary.

**Derived criticality** can arise because an asset supplies another asset's function. A cryptographic key can be important not for its storage cost but because many systems rely on it to authenticate updates. A shared time source can affect event ordering, key-expiration checks or distributed coordination. The downstream consequence depends on how the consumers use that input and which alternatives or safeguards exist.

A simple Boolean dependency model represents a service S requiring two **jointly necessary** prerequisites A and B. Here *necessary* describes the logical requirement for service operation; **it does not assert statistical independence** of their failures:

\[
\operatorname{Available}(S)=\operatorname{Available}(A)\land\operatorname{Available}(B).
\]

This is an **authored Boolean abstraction**, not an empirical assertion about a real service. If both are essential, the loss of either can prevent S from meeting its declared availability objective. If B is only an optional enrichment feature, the equation must be revised. The model's dependencies are *requirements of the chosen design*, not eternal properties of the component names.

### Dependencies are about protected behavior, not only uptime

A function can continue operating while a dependency loses **integrity**, **authenticity**, or **authority**. An application can be highly available while relying on a compromised identity provider. A manufacturing controller can remain responsive while accepting an incorrect sensor input. Therefore an asset dependency should name *which property is required*.

A more precise statement might be:

> An authorization decision is trustworthy only if the policy evaluation, subject-to-identity binding, policy data integrity, and enforcement path satisfy their declared security assumptions.

A server being “up” is insufficient evidence for that claim. [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns how the dependence is supported by evidence; this article owns its significance for protection.

## Dependency topology, alternatives and common causes

Dependencies may be serial, redundant, optional, transitive or cyclic. Their topology changes what loss means.

~~~text
                    Essential Service S
                      /           \
                     v             v
                  Branch A       Branch B
                       \          /
                        v        v
                   Shared control C
~~~

Suppose the service can function through either A or B, but both rely on the same control-plane dependency C. A model of service availability is:

\[
S=C\land (A\lor B).
\]

Its loss condition is:

\[
\neg S = \neg C \lor(\neg A\land\neg B).
\]

The two **minimal cut sets**, under the assumed Boolean model, are \(\{\neg C\}\) and \(\{\neg A,\neg B\}\). This was independently checked by enumerating all eight Boolean assignments of A, B and C and comparing the stated loss condition to the logical negation of S. It is a **logical truth-table check**, not an empirical failure-rate validation. One common dependency failure can defeat redundancy in two otherwise independent service branches. Geographic distribution does not establish probabilistic independence of failures when both service branches share an identity provider, DNS resolver, recovery credential or controller. **Logical alternatives are not evidence of statistically independent reliability.**

The equation is not a calculated reliability or cyber-risk score. Real availability may have degraded modes, temporal dependencies, retries, recovery behavior and state corruption. Quantifying likelihood also requires failure distributions and evidence that the assumed independence relations hold. Those belong to [Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) and [Security Risk & Uncertainty](../security-risk-uncertainty/README.md).

### A counterexample to “all dependencies are single points of failure”

If A is fully replaceable by B, with verified independent support and a functioning failover path, loss of A need not cause loss of S. Calling every linked component “mission critical” would ignore redundancy and error-tolerant design. A dependency's criticality is conditional on *how the relationship is satisfied*, not merely on appearing in a graph.

Conversely, a component not present in a local application diagram may still be critical through inherited service or supply-chain trust. The graph boundary matters.

## Value changes across time, stakeholders and system states

An asset can be important in one operating condition and less important in another:

- A training dataset may be replaceable during initial development but become the only recoverable evidence for an approved model.
- A temporary identity service may be disposable during a test but necessary for emergency recovery in production.
- A dormant encryption key may be unused for new data yet essential to decrypt archived records.
- A diagnostic stream may appear secondary until its absence makes it impossible to establish whether a prior security violation occurred.
- A safety interlock can constrain service availability, but disabling it can make continued operation unacceptable even when the application remains responsive.

The value of preserving a capability also may depend on **who bears its loss**. One service provider may experience a limited financial penalty while an individual experiences missed medical treatment or exposure to sensitive records. These are different kinds of consequence, not simply two estimates of the provider's asset value.

The [NIST CSF 2.0 Organizational Context category](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters) addresses mission, external dependencies and essential service expectations. The framework informs the conceptual inventory; it does not supply a single global criticality number.

## Worked comparison: an inexpensive, shared trust dependency

Imagine two unrelated applications, A and B, that rely on a shared service to verify the authenticity of their software updates. That verification service uses a low-cost configuration artifact C.

**Case 1:** The artifact is unavailable. Updates may be delayed, while currently running applications remain functional under the hypothetical design.

**Case 2:** The artifact's integrity is compromised, and both consumers accept unauthorized update signatures. The applications may continue operating normally while their integrity guarantees are invalidated.

**Case 3:** The artifact is lost but a tested, independent trust-validation path exists, and the applications can verify updates without changing the security policy. The consequence is smaller.

The same nominal asset has different criticality under the three conditions. Its replacement cost does not determine any of them, and none establishes that an adversary ever exploited the dependency. The example is invented and does not correspond to a particular vendor architecture.

## Categorization is an input, not a final verdict

[FIPS 199 (2004)](https://csrc.nist.gov/pubs/fips/199/final) categorizes U.S. federal information and information systems by **potential impact** from confidentiality, integrity and availability losses. Its low/moderate/high categories are source-specific. Its information-system **high-water mark is computed separately for each security objective across categorized information types**, as illustrated on printed p. 4 (PDF page index 7). This is not a universal hierarchy of moral interests, engineering priorities or measured organizational risk.

A service might rate high for integrity but lower for confidentiality; a public-information service could have no confidential content but still be vital for emergency availability. These different dimensions cannot be faithfully collapsed into a market-price or “number of users” metric without a justified decision model.

[NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), in its federal contingency-planning setting, relates recovery criticality to dependent business processes, including acceptable disruption and recovery requirements. It helps illustrate **why mapping dependencies matters**, but its operational business-impact-analysis procedures belong to [Operational Foundations](../../operational-foundations/README.md).

## Canonical relationships and source scope

- [Assets, Resources, and Protected Interests](assets-resources-and-protected-interests.md) identifies the thing, resource and reason for protection, while this article considers **its relative criticality and inherited dependencies**.
- [Stakeholders and Protection Needs](stakeholders-and-protection-needs.md) owns *who is affected* and what protection expectations exist.
- [Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) owns what particular losses do to affected people and capabilities.
- [Protection Priorities and Constraints](protection-priorities-and-constraints.md) owns how competing protection needs are compared and constrained, without declaring one universal ranking.
- [Resilience, Survivability, and Robustness](../security-failure-resilience/resilience-survivability-and-robustness.md) owns functional continuation and adaptation in adversity.
- [Fundamentals: Dependencies](../../fundamentals/systems-engineering/dependencies.md) owns abstract dependency relations, [Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) owns reliability mathematics, and [Operational Foundations](../../operational-foundations/README.md) owns actual BIA and risk-analysis methods.

### Source references and scope

- [NIST SP 800-160 Vol. 1 Rev. 1 (final 2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Chapter 3 §§3.4–3.7, particularly pp. 25–27, and Appendix H (stakeholder asset prioritization tasks). Published engineering guidance, not a universal asset scoring metric.
- [NIST CSF 2.0 (2024)](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), GV.OC organizational context and dependency outcomes.
- [FIPS 199 (final 2004)](https://csrc.nist.gov/pubs/fips/199/final), U.S. federal potential-impact categorization. Category assignment does not prove attack occurrence or failure probability.
- [NIST SP 800-34 Rev. 1 (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), business criticality, system dependencies and contingency planning within its stated federal context.

**Editorial limitation:** The Boolean dependency model, common-cause cut sets and examples are authored abstractions; physical dependency behavior, actual security consequences and any risk probabilities remain untested. [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md) separately checked six material claim groups and independently enumerated the Boolean model's eight possible assignments, verifying its two minimal failure cut sets. The state is **Reviewed (model-assisted) / Core claims checked**, **not** a validation of real dependencies, failure probabilities or security outcomes. Full source-passage verification, independent expert acceptance, taxonomy approval and Published remain pending.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
