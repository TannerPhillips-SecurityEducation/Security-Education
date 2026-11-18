# Assets, Resources, and Protected Interests

**Candidate subject:** SF-02-02 · Protected Interests, Assets & Harm  
**Working area:** [Protected Interests, Assets & Harm](README.md) · Fundamentals-style structure adopted; precise area and subject ownership remain provisional  
**Artifact type:** Substantive working reference, not permanently canonical or Published  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md), six article-specific material claim groups; complete source verification and qualified independent acceptance pending  
**Governance:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)

## The thing protected is not always the reason for protecting it

An **asset** is something regarded as having value or importance within a given stakeholder, system and operational context. A **resource** is something available for use to support activity or capability, such as computational capacity, physical equipment, time, information, personnel expertise, facilities, keys or supply. A **protected interest** is a legitimate concern, benefit, right, requirement or value whose preservation motivates protection.

These terms overlap without being interchangeable. A server is a resource and may be treated as an asset, but the **reason** its loss matters could be continuity of care, safe production, the correctness of financial records, or the confidentiality of information about people. A right to bodily safety is a protected interest even though treating a human as an item of inventory would distort the moral and legal meaning of that right.

[NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) §§3.4–3.7 describes stakeholder and system assets and emphasizes that the consequence of asset loss depends on the **asset, form of loss and context**. Its Figure 8 on printed p. 26 lists examples such as capabilities, people, data, components, services, reputation, trust and trade secrets. The list is illustrative. NIST Figure 8 includes **humans** among asset types in a systems-engineering consequence model, but the use of *asset* in that model does **not** turn people into property, establish legal ownership over them, or reduce their dignity and rights to asset valuations.

## Three different descriptions of one protection problem

A useful security argument keeps distinct:

1. **Object or asset of concern:** the thing, state, capability or information whose change can be observed or constrained.
2. **Stakeholder interest:** the reason particular changes would be unacceptable.
3. **Protection condition:** the security property or environmental constraint needed to preserve that interest.

| Asset or resource | Protected interest | Possible protection condition |
| --- | --- | --- |
| Service scheduling database | Correct and timely service for people | Authorized changes preserve valid appointments |
| Cryptographic signing key | Integrity and authenticity of decisions or artifacts | Material remains controlled and used only for authorized signing |
| Public emergency notification channel | People's ability to receive trustworthy warnings | Availability and integrity remain adequate in specified emergencies |
| Employee activity logs | Accountability while preserving privacy | Retain necessary evidence without unwarranted sensitive uses |
| Industrial process controller | Safe physical operations and production continuity | Correct commands and safe transition behavior under hazardous conditions |
| Shared cloud dependency | Continuity of downstream services | Failure isolation and recovery preserve critical functions |

The table expresses **possible relationships**, not universal assignments. A log can simultaneously be evidence, sensitive personal information and a resource for a detection function. A signing key can serve many independently affected applications. A hospital system's protection interests are not exhausted by the hospital's purchase price or insurance valuation.

An asset may be valuable because it is scarce, replaceable only at significant cost, indispensable to another capability, tied to rights, or connected to future consequences. These dimensions should not be reduced to one unqualified score.

## Stakeholder assets and system assets

NIST SP 800-160v1r1 §3.7 distinguishes assets important to stakeholders from internal **system assets** that arise from design and implementation. A system's users may be unaware that their access depends on a private signing key, a resolver, a source-code signing process, a hardware trust root or a policy database. Those elements can be essential even if they are not directly useful outside the system.

Consider an online payment service. The customer's protected interest concerns correct, confidential and timely authorized transactions. Internally, the service depends on cryptographic keys, a message queue, an authorization policy, and reconciliation records. These are system assets or resources. Their failure can affect the customer without transferring customer ownership to every internal component.

A single asset can participate in **multiple protective relationships**:

~~~text
               Customer's protected interest
                     Correct transaction
                            ^
                            |
                 Payment ledger integrity
                       /          \
                      v            v
                Key custody   Event-processing queue
                      |            |
                      v            v
                Trust service    Scheduler / storage
~~~

This is an illustrative dependency sketch, not a complete causal graph or proof of correct protection. Some dependencies are indirect, and alternative implementations may remove or replace them. [Value, Criticality, and Dependencies](value-criticality-and-dependencies.md) owns how such relationships affect importance and consequences.

## The asset-resource distinction can change with the boundary

Security descriptions use system boundaries to decide what counts as a resource, output, asset, or external service. A shared identity service is an **internal resource** when the analyzed system includes the entire platform, but an **external dependency** when evaluating one application alone. Either view can be accurate if its boundary is explicit.

Similarly, information can be:
- a protected dataset when confidentiality or integrity matters;
- input to a service whose correctness depends on it;
- a record that supports an assurance or investigation claim;
- a representation of a person whose privacy interests extend beyond the database owner;
- an object already in public circulation whose misuse or alteration can nevertheless cause harm.

The security property changes with the role and context. “Protect the data” may mean confidentiality, integrity, provenance, controlled processing, availability, retention constraints, or some combination.

A common modeling error is **catalog completeness without relationship completeness**. A register might list every hardware item while omitting the people's interests that motivate protection, and it might list every policy objective while overlooking the technical dependencies necessary to satisfy those objectives. Neither list proves that a specific protective function works.

## Direct and derived interests

Some interests relate to an asset directly, such as protecting a private key from disclosure. Others arise through a dependency: a compromised key can support fraudulent transactions; a corrupted sensor can cause a physical controller to perform unsafe actions; a lost directory can block access to otherwise intact information.

The relevant relationship is **not always purely monetary**. Replacing a controller may be inexpensive, but temporary lack of safe control could impose serious harm on people. A service may store publicly available information but still have an important integrity or availability obligation. Conversely, an expensive computer may be unimportant for a particular function if it has a ready, tested replacement.

An information owner may have legal and managerial authority over processing infrastructure while people described in the information retain distinct interests. **Technical ownership and legitimate authority to impose harm are not identical.** The latter is treated in [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md).

## Worked example: a low-cost component, a high-consequence dependency

Imagine a fictitious water-monitoring service with a small telemetry gateway costing **$120**. The gateway transmits a measurement used by a process that determines whether to isolate an unsafe flow. Replacing the box costs $120, but if a failed gateway causes the safety process to receive misleading values, affected stakeholders might experience interruption, damage or injury.

Three different claims are possible:
- **Replacement value:** the hardware itself costs approximately $120, under the scenario's assumptions.
- **Functional criticality:** the gateway is an important input to a safety-related function, conditional on its architecture and alternative safeguards.
- **Consequential harm:** the severity of an unsafe outcome depends on plant behavior, detection, fail-safe controls, exposure and people affected.

It would be technically wrong to conclude that the gateway deserves only “$120 worth of security.” It would be equally wrong to assert that compromising it necessarily causes injury: the design may have independent safeguards or reliable fallback measurements. The scenario is invented and establishes **no actual failure rate, probability of injury or compliance finding**.

[Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) owns the meaning of harm that can follow from loss; [Security Risk & Uncertainty](../security-risk-uncertainty/README.md) owns the chance and estimation of future harm under stated threat scenarios.

## What an asset classification can and cannot establish

Security categorization frameworks use terms such as low, moderate and high to help organizations reason about particular adverse impacts. [FIPS 199 (2004)](https://csrc.nist.gov/pubs/fips/199/final) establishes a **U.S. federal** categorization method for potential impacts of confidentiality, integrity and availability loss, not a universal asset-price list or a formula for all risk. Its information-system **high-water-mark rule applies separately to each of the three security objectives across relevant information types**, rather than assigning one monetary value or identical impact rating to confidentiality, integrity and availability. For an information *type*, confidentiality can be not applicable; for a categorized information *system*, FIPS 199 requires at least low impact for each objective. See the official FIPS 199 text, printed pp. 3–4 (PDF page indexes 6–7).

An asset's label, classification, inventory membership or ownership record can be valuable evidence that someone considered it. None proves that its access is correctly controlled, that its dependencies are safe, or that it is protected against its most consequential forms of loss.

A more useful reference description connects:
- a specific asset or resource and its lifecycle state;
- the stakeholder(s) concerned;
- the capability or protected interest involved;
- the forms of change or loss that matter;
- the trust boundary and dependencies;
- the evidence and remaining unknowns.

The point is not to make every asset description a legal instrument or fixed database schema. It is to prevent vague inventory labels from silently substituting for a security claim.

## Canonical boundaries and source scope

- [Stakeholders and Protection Needs](stakeholders-and-protection-needs.md) owns *whose interests* motivate protection.
- [Value, Criticality, and Dependencies](value-criticality-and-dependencies.md) owns contextual importance and dependency consequences.
- [Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) owns the effects of loss, not estimated future likelihood.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns the condition enabling violations.
- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md) owns the contextual meaning of security itself.
- [Fundamentals: Dependencies](../../fundamentals/systems-engineering/dependencies.md) owns generic dependency mechanics, not what ought to be protected.
- [Operational Foundations](../../operational-foundations/README.md) owns actual asset inventories and classification workflows; specialized domains own their concrete assets and configurations.

### Primary source starting points

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Chapter 3 §§3.4–3.7, Figure 8 (printed p. 26), stakeholder and system assets and context-relative loss.
- [FIPS 199 (final, 2004)](https://csrc.nist.gov/pubs/fips/199/final), potential impact categories in its federal information-system context.
- [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), governance and assets/capabilities as outcomes, not proof of deployment effectiveness.
- [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final), privacy-related protected interests of individuals beyond asset-owner financial loss.

**Editorial limitation:** The gateway's price and system are fictional. Asset categories and relationship models are editorial teaching constructions; cited sources inform the concepts without certifying any specific asset taxonomy. This article has a separate **Reviewed (model-assisted) / Core claims checked** record in [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md), covering six material claim groups including the NIST Figure 8 human-asset caveat and FIPS 199's per-objective information-system categorization. It is **not** Source-Verified, independently expert-accepted, permanently canonical-approved or Published.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
