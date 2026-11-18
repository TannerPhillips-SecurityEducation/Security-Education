# Security, Privacy, Safety, and Reliability

**Candidate subject:** SF-01-08 · Security Meaning & Objectives  
**Working area:** [Security Meaning & Objectives](README.md) · **Fundamentals-style structure adopted; individual subject placement still provisional**  
**Artifact type:** Substantive working area reference; internal area membership remains **provisional**, not source-Verified or Published.  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md) (five material claim groups); complete source verification and qualified independent review remain open  
**Architecture:** [Working candidate inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership boundaries](../OWNERSHIP-BOUNDARIES.md)

## Related protection objectives are not interchangeable

**Security, privacy, safety and reliability** can be mutually reinforcing, but each addresses a different class of interests and failure conditions. A system can be reliable while consistently performing a privacy-invasive action. A security control can be correctly enforced while interfering with a safety-critical function. A safe physical outcome does not prove that data were kept confidential.

The terms must be qualified by the system boundary, the legitimate interests involved, the operating environment and the governing requirements. Neither one universal "secure" label nor the CIA Triad exhausts the protection needs of individuals and systems.

| Area | Central protection concern | Distinct failure example |
| --- | --- | --- |
| **Security** | Prevent or limit violations of stated protection properties under relevant adverse conditions | Unauthorized disclosure, modification or denial of protected capability |
| **Privacy** | Prevent or limit harmful or otherwise unacceptable impacts on individuals from data processing and loss of appropriate control/context | Sensitive inference or discriminatory use from otherwise authorized collection |
| **Safety** | Reduce risk of harm to people, property or environment below the applicable tolerability threshold | Physical injury from unsafe actuation or failure to enter a safe state |
| **Reliability** | Perform a specified function consistently under defined conditions and time | Service fails too frequently or deviates from its required function |
| **Resilience** | Preserve, regain or adapt valued functions despite adverse conditions | Service cannot maintain essential mission functions after disruption |

These are comparative explanations rather than mandatory, mutually exclusive categories. A particular failure may implicate multiple objectives.

## Privacy risk is not limited to confidentiality breaches

The [NIST Privacy Framework 1.0 (January 2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) provides a voluntary approach for managing privacy risk associated with data processing and protecting individuals. Its approach recognizes that **authorized data processing can produce problematic outcomes**, including discrimination, distress or loss of autonomy, even when no external attacker breaches a system.

The [NIST glossary on information-system-related privacy risks](https://csrc.nist.gov/glossary/term/info_system_related_privacy_risks) explicitly includes harms arising from (1) a breach and (2) authorized data processing that generates a problematic result.

A service can therefore meet many cybersecurity controls yet still present a privacy problem when it collects unnecessary personal information, correlates contexts that people reasonably expect to remain separate, retains data beyond the justified purpose, or uses data for consequences that affect individuals unfairly.

**Confidentiality** asks whether information is disclosed contrary to a specified protection requirement. **Privacy** also asks what information is processed, for whose purpose, by whose authority, with what aggregation/inference, and with what consequences for individuals or groups.

Anonymization, encryption and access-control enforcement may reduce selected privacy risks but do not automatically remove the possibility of identification, reidentification, inference, harmful use or unfair decisions. A framework's adoption is not evidence of a system's actual treatment of affected people.

**Edition note (November 2026):** NIST's public [Privacy Framework 1.1 project](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) shows a **2025 Initial Public Draft**, not a published final 1.1 edition. Accordingly this article uses the final 1.0 as its stable normative source orientation, while monitoring future releases.

## Safety refers to harmful physical consequences and acceptable risk

[ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), confirmed current after a 2025 review, provides guidance for incorporating safety into standards and addresses people, property and the environment. In that framework, safety is linked to freedom from **intolerable risk**, not a promise that every hazard has been eliminated.

A **hazard** is a potential source of harm in a chosen safety context. A **hazardous event** involves conditions under which that source may produce harm; an actual injury is a **consequence**. Threats to confidentiality and hazards to bodily health may interact, but they are not synonyms.

**Functional safety** concerns the safety-related functions that equipment or systems must perform under specified conditions. [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515) applies to electrical, electronic and programmable electronic safety-related systems and supplies a framework for functional safety. A 2026 third-edition preview is published separately; a preview is not automatically the normative edition used for every existing certification or implementation.

A safety function may deliberately disable a process or deny a command to prevent unacceptable harm. Under its specified safety requirements, a safe shutdown might be correct even though an availability objective for the affected service is not met during the shutdown.

A cybersecurity attack can compromise an industrial safety function, but safety also encompasses accidental faults, environmental conditions and unintended interactions without a malicious actor. Neither discipline subsumes the other.

## Reliability is conditional functional performance, not proof of security

A reliable system consistently performs its **specified functions** over a stated interval and operating conditions. Reliability can be expressed probabilistically under a chosen failure model, but the relevant event and population must be defined.

For example, if a component has a **constant hazard rate** λ in an idealized exponential lifetime model, its reliability is `R(t)=exp(−λt)`. This is a property of that particular stochastic model, not a universal formula for every component or a measure of whether the component is secure.

**Worked model:** With λ=0.01 per hour, the ideal model gives `R(10 hours)=exp(−0.1)≈0.9048`. That is the model-implied probability of no specified failure over ten hours, not the probability of no adversarial compromise, safe operation or privacy protection.

If a system reliably sends an individual's movements to an unauthorized purpose, it may be highly reliable *at performing a harmful function*. Reliability does not determine the legitimacy of the requirement. [Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) owns the general reliability mathematics and assumptions; this subject owns the cross-objective comparison.

## Worked scenario: an automated building

Consider an invented smart-building platform that records occupants' location for evacuation support and controls emergency exits.

**Security question:** Does access-control policy prevent unauthorized parties from reading live location records or commanding exit devices?

**Privacy question:** Does the building unnecessarily retain and correlate personal movement histories, or use them for unrelated employment decisions, even if administrators were technically permitted to access them?

**Safety question:** Do emergency controls enable safe egress under fire, power loss or controller malfunction, under the applicable hazard assumptions?

**Reliability question:** Do sensors, actuators and software perform their specified tasks within required times and conditions?

**Resilience question:** If the network is unavailable or a component is compromised, can essential safety functions continue or recover in a trustworthy form?

A rule that blocks all exit-control communication might strengthen resistance to unauthorized remote commands in one threat model while creating unacceptable danger in another. A privacy-preserving retention limit might complicate some security investigations, but longer retention is not automatically justified. The correct architecture must consider the **specific protected interests and conditions**, not declare that security always trumps safety or privacy.

These are hypothetical distinctions, not assertions about building code, labor law or a real facility.

## Tradeoffs require legitimate authority, not only technical optimization

Protection choices may change consequences for people who are not owners of the system. A privacy-intrusive measure can impose risks on monitored individuals even if the organization gains security visibility. An overly restrictive safety or access rule may deny essential services to legitimate users.

A defensible decision must specify whose interests were considered, whether a restriction is legitimate and proportionate, what alternatives exist, and what evidence supports the expected benefit and resulting harms. Those issues lead into [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md).

This pilot describes **which objectives differ**. The ethical/governance subject owns **how conflicting obligations, legitimate authority, rights and human impact constrain protection choices**. Neither provides a universal legal verdict.

## Conceptual and cross-domain boundaries

- [Security and Insecurity](security-and-insecurity.md) owns the scope and epistemic status of security claims.
- [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md) owns scenario-relative impact and uncertainty.
- [Resilience, Survivability, and Robustness](../security-failure-resilience/resilience-survivability-and-robustness.md) owns preserving essential outcomes under adversity.
- [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) owns rights, governance and proportionality.
- [Fundamentals: Probability and Statistics](../../fundamentals/mathematics-logic/probability-and-statistics.md) owns probability models; [Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) owns general component/system reliability.
- [Industrial Knowledge](../../../industrial/README.md) owns actual safety controllers and sector-specific engineering; [Identity Knowledge](../../../identity/README.md) owns identity mechanisms; [Operational Foundations](../../operational-foundations/README.md) owns the performance of risk, safety and privacy assessments as methods.

## Source references and applicability

- [NIST Privacy Framework 1.0, final (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final), voluntary privacy risk management.
- [NIST privacy-risk glossary](https://csrc.nist.gov/glossary/term/info_system_related_privacy_risks), privacy harms from breaches and authorized processing.
- [NIST Privacy Framework 1.1 project](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11), initial-public-draft versus final status.
- [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), general safety aspects, confirmed current in 2025.
- [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515), functional-safety requirements for E/E/PE systems (2010 edition remains separately identified).
- [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), cyber-resiliency goals distinct from reliability and safety.

**Limit:** NIST and ISO/IEC sources define terms for particular frameworks; they do not authorize importing one universal cross-domain taxonomy, prove a concrete product is safe/private, or substitute for jurisdiction-specific legal obligations. Complete source-passage validation and independent expert review remain outstanding.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md). This remains a **pilot**, not a ratified canonical subject, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](../pilots/README.md)
