# Resilience, Survivability, and Robustness

**Candidate subject:** SF-11-04 · Security Failure & Resilience  
**Working area:** [Security Failure & Resilience](README.md) · **Fundamentals-style structure adopted; individual subject placement still provisional**  
**Artifact type:** Substantive working area reference; internal area membership remains **provisional**, not source-Verified or Published.  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md) (five material claim groups); complete source verification and qualified independent review remain open  
**Architecture:** [Proposed Security Foundations](../ARCHITECTURE.md) · [Working candidate inventory](../SUBJECT-INVENTORY-PROPOSAL.md)

## Resilience concerns valued function despite adverse conditions

**Resilience** concerns a system's capability to sustain, regain or adapt the valued outcomes it exists to deliver in the presence of disturbances, adverse conditions or compromise, within defined bounds. **Cyber resiliency** narrows attention to systems that use or depend on cyber resources and to adverse stresses, attacks and compromises affecting those resources. It is not equivalent to a high uptime percentage or a backup product.

[NIST SP 800-160 Volume 2 Revision 1 (December 2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) describes cyber resiliency through four high-level goals: **anticipate, withstand, recover and adapt**. These are goals for engineering and mission assurance, not an obligatory four-step workflow that every organization performs in that order. The NIST publication distinguishes goals, objectives, techniques, approaches and design principles, and permits context-driven selection.

A system may have impressive nominal availability while failing to withstand a targeted compromise. Conversely, a system may intentionally reduce a noncritical function to preserve a safety-critical operation or protect restricted information.

## Robustness, resilience, survivability and reliability answer different questions

| Concept | Central question | Boundary |
| --- | --- | --- |
| Reliability | Does the system perform a specified function over a defined time and condition set? | Does not automatically include hostile adaptation or trustworthy restoration |
| Robustness | How sensitive is a specified behavior to a bounded class of disturbances or model variations? | No guarantee outside the declared disturbance set |
| Resistance | Can adverse conditions be prevented or their immediate effects limited? | No guarantee of continuing operation after resistance fails |
| Survivability | Can essential mission/service functions persist despite significant adverse effects? | May involve reduced nonessential capability |
| Resilience | Can essential outcomes be anticipated, withstood, recovered and adapted to under stated adversity? | Not reducible to redundancy, backup count or uptime |
| Recoverability | Can defined function and state be reestablished under accepted conditions? | Does not by itself show restored trustworthiness |

These terms overlap in practice and vary across standards. Their utility depends on spelling out the **valued function, adversarial and environmental assumptions, acceptable degradation, time horizon and evidence**.

[Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) owns generic reliability and failure models. This pilot owns the **security-relevant use of resilient system properties**, particularly when trust assumptions and adversarial adaptation matter.

## Anticipate, withstand, recover, adapt

NIST SP 800-160v2r1's four goals can be understood as follows without imposing a process order:

- **Anticipate:** Maintain capabilities and preparedness to consider adverse conditions and threats that may affect valued objectives.
- **Withstand:** Sustain selected essential functions or limit their degradation while adverse effects are occurring.
- **Recover:** Restore relevant capabilities and appropriate trust following adverse events.
- **Adapt:** Change system behavior, architecture or operating assumptions so future conditions are better addressed.

The concepts are **complementary and potentially overlapping**. A system can adapt while a disruption is still unfolding; an already degraded system may still provide partial essential functions. A restored service might work again without its security properties being established.

Resilience claims are conditional: NIST's framework does not assert every cyber-resource-dependent system can recover from every adversary or environmental condition. A specific system's resilience must be assessed against a threat model and valued outcomes.

## Containment, blast radius and common-mode failure

**Containment** limits the propagation or consequences of unwanted conditions across defined boundaries. The metaphor **blast radius** refers to the scope of assets, capabilities or stakeholders potentially affected. It does not define a universal geographic radius or a measured numerical hazard footprint.

**Redundancy** introduces additional components or paths capable of supporting a function. But two services may rely on the same identity provider, configuration service, certificate authority, power supply or administrative account. This is a **common-mode failure** risk: redundant elements may not fail independently.

**Diversity** may reduce shared causes of failure when implementations, dependencies or operational conditions genuinely differ. Yet diversity introduces costs, complexity and integration problems. Two different technologies can still share the same policy mistake or supply-chain dependency.

For example, two replicated services that share the same compromised signing key may both return valid-looking signed responses under an invalid trust assumption. Replication can help keep responses available without restoring authenticity.

## Graceful degradation can be a security choice

**Graceful degradation** preserves prioritized functions under reduced capacity or trust, instead of treating all functions as either fully available or completely unavailable. A service might disable external document sharing while preserving local read-only access to already authenticated users.

The choice is not universally "fail closed" or "fail open." For safety-critical processes, denying every request could create physical danger; for high-confidentiality operations, continuing a function with unknown identity assurance may create unacceptable disclosure. The appropriate behavior depends on **which interests and harms** the design protects.

A degradation mechanism can be **safe under one requirement and insecure under another**. Its claims must describe the constraints and tradeoffs rather than treating a generic engineering slogan as sufficient.

## RTO, RPO and MTD describe different recovery constraints

[NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) distinguishes recovery-related concepts:

- **Recovery Time Objective (RTO):** A target maximum period for restoring a specified system resource or service capability before intolerable impact under the defined contingency context.
- **Recovery Point Objective (RPO):** A point in time to which data must be recoverable, defining a tolerated amount of data loss or staleness relative to the disruption.
- **Maximum Tolerable Downtime (MTD):** A broader acceptable outage limit for the relevant mission or business process, not an alternative name for RTO.

RTO is **about the time to restore capability**. RPO is **about recoverable data state**. A system can meet RTO but miss RPO, or meet RPO while restoring too slowly. The metrics have different accounting boundaries and source-defined caveats.

**Worked example:** A service has a two-hour RTO and a 15-minute RPO under a hypothetical planning model. Its last complete, usable data checkpoint was at 09:00. A failure occurs at 09:40, and the service is successfully restored at 11:00.

- The downtime is 80 minutes, satisfying the stipulated **120-minute RTO** if measured from 09:40 to functional restoration at 11:00.
- The last data checkpoint predates the failure by **40 minutes**. If there is no incremental log, journal, or later recoverable copy, the data-recovery result does **not** satisfy a 15-minute RPO in this model.
- Even if the service starts and accepts requests, **trusted restoration is not demonstrated** until the integrity of the image, keys, configuration, dependencies and recovered state has been sufficiently supported.

These are invented timestamps. They do not characterize any real business, data-loss distribution, service-level obligation or incident-response performance.

## Trusted restoration and continuous evolution

Recovery from a security compromise requires attention to **trust inheritance**. Backups, credentials, policy stores and administrative components may contain or reproduce untrusted state. A validly stored backup is not automatically a clean backup. Restarting a service does not necessarily remove an adversary's retained authority.

The related [Compromise and Loss of Security](compromise-and-loss-of-security.md) pilot owns what a compromise can mean and what evidence supports that claim. [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns the justification for calling the restored state trustworthy.

An adaptation may change attack exposure, service performance or rights affected by data processing. Its intended benefit can also introduce a new vulnerability or privacy/safety consequence. A resilient design must consider *what should be preserved* rather than simply increasing the probability of continuing some operation.

## Mechanisms, workflows and canonical boundaries

- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md): protected interests and conditional security claims.
- [Compromise and Loss of Security](compromise-and-loss-of-security.md): security-property violation, compromised state and uncertainty.
- [Controls, Safeguards, and Security Functions](../security-controls-defense-mechanisms/controls-safeguards-and-security-functions.md): implementation and evidence of safeguards that might support resilience.
- [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md): impact and likelihood under a defined risk scenario.
- [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md): cross-objective conflicts and protected interests.
- [Fundamentals: Feedback and Control](../../fundamentals/systems-engineering/feedback-and-control.md), [Dependencies](../../fundamentals/systems-engineering/dependencies.md) and [Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md): general system mechanisms.
- [Operational Foundations](../../operational-foundations/README.md): continuity planning, incident response, backup/restore execution and testing.
- [Network Knowledge](../../../network/README.md), [Industrial Knowledge](../../../industrial/README.md) and other domains: concrete implementations, redundancy, safety constraints and failover mechanisms.

## Primary reference starting points

- [NIST SP 800-160 Vol. 2 Rev. 1, Developing Cyber-Resilient Systems (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), definitions, goals and engineering scope.
- [NIST glossary: Cyber Resiliency](https://csrc.nist.gov/glossary/term/cyber_resiliency), concise source-bound terms.
- [NIST SP 800-34 Rev. 1 (2010, updated 2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), RTO/RPO/MTD and contingency-planning scope. Use as a concept source, not a claim that its procedures are the current universal standard.
- [NIST SP 800-61 Rev. 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final), operational incident-response guidance, separate from foundational resilience properties.

**Editorial limitation:** This pilot explains conceptual system properties and invented examples, not how to perform incident response or guarantee recovery in any environment. Source-passage technical review and independent human acceptance remain open; the 12-area/96-subject inventory is still proposed and flexible.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md). This remains a **pilot**, not a ratified canonical subject, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](../pilots/README.md)
