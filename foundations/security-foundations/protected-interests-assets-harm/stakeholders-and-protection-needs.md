# Stakeholders and Protection Needs

**Candidate subject:** SF-02-01 · Protected Interests, Assets & Harm  
**Working area:** [Protected Interests, Assets & Harm](README.md) · Fundamentals-style navigation adopted; area and subject membership remain provisional  
**Artifact:** Substantive working knowledge article, not a final canonical or Published reference  
**Development state:** Draft · **Source-review state:** References listed; initial primary-source comparison completed, separate claim-led Technical Review pending  
**Authority:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Working ownership register](../CANONICAL-OWNERSHIP-REGISTER.md) · [Security Foundations AGENTS](../AGENTS.md)

## Protection begins with affected interests, not a list of controls

A system is built and operated for purposes that matter to people and institutions. Its security does not exist in isolation from those purposes. A **stakeholder** is an individual, group, institution or other legitimately relevant party with an interest in the system's capability, conduct, outcomes, assets, or consequences. A **protection need** is a contextual expectation or necessity that valued interests and assets be preserved against specified unacceptable forms of loss, degradation, misuse or exposure.

A protection need is not necessarily a completed design requirement. It may first appear as a concern: people should not be locked out of emergency assistance; payroll records must not be exposed; a control system must not accept unsafe commands; records must remain attributable to the appropriate process. Engineering turns such needs into sufficiently explicit objectives, constraints, and verifiable requirements, but prematurely choosing a technical mechanism can conceal the real interest.

[NIST SP 800-160 Volume 1 Revision 1 (November 2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Chapter 3 §3.7, printed pp. 25–27, explicitly grounds protection needs in stakeholders' assets, consequences, priorities and constraints. Its Figure 7 distinguishes **stakeholder**, **system**, and **engineering trade** perspectives. Those are useful perspectives, not a mandate for this repository to adopt them as a complete ontology of persons or organizations.

The **stakeholder question** is who or what has an affected interest. The **security question** is which unacceptable changes, actions or outcomes must be prevented, constrained or made recoverable. A person may be affected by a system without owning it, managing it, using it, or being represented by its access-control database.

## Stakeholder, principal, owner and decision authority differ

Several terms often refer to different roles and should not be compressed into “the user.”

| Role | Meaning in this article | Illustrative interest |
| --- | --- | --- |
| Beneficiary or service recipient | Depends on the capability delivered | Timely, reliable access to a critical function |
| Data subject | Information describes or can affect that person | Accuracy, privacy, lawful and legitimate use |
| Operator or maintainer | Performs work and bears operational burdens | Reliable tooling, safe recovery and appropriate access |
| Asset custodian or owner | Has property, contractual or management interests | Protection of information, equipment and delegated control |
| Supplier or partner | Contributes dependencies or receives outputs | Correct interfaces and allocation of responsibility |
| Bystander or indirectly affected party | May be harmed despite not using the system | Physical safety or freedom from unnecessary surveillance |
| Regulator or accountable authority | Establishes or enforces applicable obligations | Sufficient evidence of conformity within a defined jurisdiction |

These roles can overlap and change with time. A single individual may own a device, be the subject of its data, and administer its account. But the roles remain conceptually distinguishable. **A technical principal** is an identity represented in a security mechanism. Not every stakeholder has a technical principal, and possessing a principal does not alone establish authority to determine another stakeholder's acceptable harms.

Likewise, an institutional asset owner can decide some engineering priorities but is not automatically empowered to override an individual's rights, a safety obligation, or a contract that protects a different party. [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) owns the normative legitimacy of these decisions; this article owns the structure of the interests being represented.

## Three perspectives and their associated protection needs

NIST SP 800-160v1r1 §3.7 characterizes a protection-need problem from at least three mutually relevant directions:

**Stakeholder perspective.** An organization needs to deliver a service, preserve its information, meet obligations, and avoid injury or other harms to affected people. That need can exist **before** anyone selects the database, identity provider or network protocol.

**System perspective.** The implemented architecture introduces assets the original service recipient may never know about: signing keys, firmware, internal management credentials, replicated state, caches, control planes and support systems. These assets require appropriate protection because failures in them can defeat the stakeholder's higher-level objective.

**Engineering-trade perspective.** Security must coexist with performance, reliability, physical constraints, safety, cost, usability, maintainability and recovery. Some compromises are acceptable; some are not. A requirement that appears desirable in one dimension may conflict with another protection need or constraint.

The [NIST CSF 2.0 Organizational Context outcomes](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters), particularly **GV.OC-01–04**, address mission, internal and external stakeholders, applicable obligations and critical services expected by external parties. Those outcomes support accounting for affected parties; they are not a universal formula for deciding whose interests always prevail.

## A traceable conceptual chain

Protection-needs reasoning can proceed without treating the following as a mandatory operational workflow:

~~~text
Stakeholder or affected party
       |
       v
Legitimate interest / obligation
       |
       v
Asset, capability or condition of concern
       |
       v
Unacceptable form or consequence of loss
       |
       v
Protection need with scope and constraints
       |
       v
Security objective / testable requirement
       |
       v
Design evidence and assurance argument
~~~

The chain highlights traceability. A control such as encryption is not itself the protected interest. The protected interest may be confidentiality of intimate records, integrity of payment authorization, or the freedom of a person not to be subjected to harmful surveillance. The control is one possible means of satisfying a requirement derived from that interest.

A mature protection-need statement identifies:
- the affected party or legitimate interest;
- the system or environmental boundary;
- the valued capability, information or condition;
- the prohibited or unacceptable form of loss;
- the temporal or operational circumstances;
- the applicable obligations and constraints;
- the evidence by which satisfaction could be meaningfully assessed.

No fixed form is mandated for all needs, and a single system may have conflicting needs. Unknown stakeholders and indirect dependencies should remain **unknown**, not be treated as nonexistent.

## Worked case: a community health appointment service

Consider a hypothetical service scheduling critical care. Its operator values uptime; patients value access, confidentiality and correctness; clinical staff value accurate scheduling and safe workload; a technology supplier depends on functioning interfaces; people who are not registered users may be affected when capacity is unavailable.

Four possible protection needs can coexist:

| Concern | Protected interest | A more precise protection need |
| --- | --- | --- |
| Wrong appointment | Correct access to care | Prevent unauthorized or erroneous changes to scheduled appointments |
| Disclosure | Personal privacy and dignity | Limit access and secondary uses of identifiable information to justified purposes |
| Outage | Timely service availability | Preserve essential scheduling capability during defined disruptions or enable a safe alternative |
| Monitoring | Accountability without unnecessary intrusion | Produce sufficient security evidence while minimizing unrelated sensitive collection |

Installing a stronger authentication mechanism could improve one access-control property but block patients with limited devices. Retaining all usage data indefinitely could help certain retrospective inquiries while creating an unjustified privacy burden. These are **conflicting stakeholder concerns**, not proof that security or privacy should always dominate.

The scenario has no measured frequencies, legal determinations or actual organization. [Protection Priorities and Constraints](protection-priorities-and-constraints.md) owns how to compare competing needs once they have been described. [Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) owns what a lost property can do to affected stakeholders.

## From an expressed need to an evaluable requirement

A broad concern such as “keep information secure” does not identify what evidence would justify success. A narrower requirement might be that only specified roles can access a particular class of records under documented exceptions, and that accesses are auditable without retaining unnecessary unrelated details.

The distinction matters:
- **Protection need:** maintain confidentiality of sensitive patient information.
- **Security objective:** prevent unauthorized exposure of that information in the declared system and environmental scope.
- **Security requirement:** enforce an explicitly defined authorization rule at all designated read paths under stated conditions.
- **Assurance argument:** explain how implementation, configuration, tests and remaining assumptions support the objective.

A requirement can be verified against a specification and yet fail to capture an essential stakeholder concern. This is why stakeholder validation and security verification are not identical. [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns assurance logic, while [Operational Foundations](../../operational-foundations/README.md) owns the execution of elicitation, assessment and authorization processes.

## Scope, evidence and relationships

This article owns **stakeholder interests and the meaning of protection needs**, not a fixed taxonomy of stakeholders, a product design checklist, a legal compliance judgment or an operational process. Its neighboring concepts have deliberately separate owners:

- [Assets, Resources, and Protected Interests](assets-resources-and-protected-interests.md) distinguishes the things under protection from the reasons they matter.
- [Value, Criticality, and Dependencies](value-criticality-and-dependencies.md) explains contextual importance and indirect dependence.
- [Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) explains effects of loss on people and capabilities.
- [Protection Priorities and Constraints](protection-priorities-and-constraints.md) owns comparing protection demands under constraints.
- [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md) distinguishes protection-objective families.
- [Fundamentals: Systems & Engineering](../../fundamentals/systems-engineering/README.md) owns general system/requirement concepts; [Operational Foundations](../../operational-foundations/README.md) owns elicitation and governance activities.

### Primary source starting points

- [NIST SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Chapter 3 §§3.4–3.7, especially §3.7 printed pp. 25–27, and Appendix H stakeholder-security activities. The source's formal engineering tasks are not adopted as this repository's mandatory article outline.
- [NIST CSF 2.0 (2024)](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), GV.OC stakeholder, mission, dependency and obligation outcomes. Framework outcomes are not evidence that a particular stakeholder need has been met.
- [NIST Privacy Framework 1.0 (final 2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final), individuals' privacy interests and processing-related risk; the [1.1 project](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) still publicly identifies an initial public draft, not an established final release in the cited project status.
- [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), safety aspects concerning people, property and the environment, confirmed current following a 2025 review; not a general legal authorization model.

**Editorial limitation:** This is a **Draft / References listed**, not a separately audited or Published manuscript. Its stakeholder roles and conceptual traceability are editorial decompositions informed by source-defined engineering concepts; no single standard dictates this exact list or grants authority to accept other people's harms. A separate multi-article claim-led review is required before advancing its status.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
