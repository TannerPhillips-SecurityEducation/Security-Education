# Security and Insecurity

**Candidate subject:** SF-01-01 · Security Meaning & Objectives  
**Working area:** [Security Meaning & Objectives](README.md) · **Fundamentals-style structure adopted; individual subject placement still provisional**  
**Artifact type:** Substantive working area reference; internal area membership remains **provisional**, not source-Verified or Published.  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md), five material claim groups; full source verification and independent expert acceptance pending  
**Governance:** [Security Foundations Architecture Proposal](../ARCHITECTURE.md) · [Living candidate inventory v0.3](../SUBJECT-INVENTORY-PROPOSAL.md)

## Security is conditional protection, not an absolute label

**Security** concerns the extent to which protected interests can be maintained against relevant adverse events, actions and conditions, in a specified system, environment and time horizon, under declared assumptions. **Insecurity** concerns an actual failure or weakness of the protections needed to satisfy those interests under relevant conditions. **Uncertainty about security** concerns what an observer can *justifiably establish* from evidence. A lack of assurance evidence does not, by itself, prove either that the system is insecure or that it is secure. Neither term is a universal property of a device, product, person, location or network without identifying the interests and assumptions involved.

For example, “this service is secure” is too broad to be technically assessed. A narrower claim might be: “Under the specified interface, authority and adversary assumptions, unauthorized readers cannot retrieve protected customer records through the evaluated access paths.” This claim can be examined, but it says nothing by itself about lost backups, unmodeled side channels, damaged hardware, legal obligations or future software defects.

A security claim therefore has at least five ingredients:

| Element | Example | Why it matters |
| --- | --- | --- |
| Protected interest | Customers' privacy and access to their records | Security is relative to something worth protecting |
| System and boundary | A named service, its storage and supported interfaces | An omitted interface can invalidate an overbroad claim |
| Desired property | No unauthorized record disclosure | Identifies what a violation would mean |
| Threat and operating assumptions | Identified capabilities, failure conditions, identities, dependencies and period | Determines which events the claim addresses |
| Evidence and confidence | Tests, design arguments, logs, independent evaluation, limitations | A claim is not demonstrated by asserting it |

**Three possible assessments must remain separate:** (1) a protection property is shown to hold under specific assumptions, (2) a violation or failure is shown to occur, or (3) the available evidence is insufficient to establish either. The third state is **unknown or unassured**, not automatically insecure.

The word **secure** is often used as a binary shorthand, but real protection has multiple properties and evidentiary limitations. Security is not simply the absence of observed attacks, and a control's presence is not proof that the desired property holds.

## Confidentiality, integrity and availability are distinct objectives

The **CIA triad** is an established information-security lens consisting of **confidentiality**, **integrity** and **availability**. It is foundational but not exhaustive. NIST's [information security glossary](https://csrc.nist.gov/glossary/term/information_security) describes protecting information and systems from unauthorized access, use, disclosure, disruption, modification or destruction to provide confidentiality, integrity and availability.

- **Confidentiality:** Constraints on disclosure or access to protected information. Encryption can help protect some confidentiality properties but does not decide who should have access or ensure that all keys and endpoints remain trustworthy.
- **Integrity:** Protection against unauthorized modification or loss of specified information/system correctness properties. A cryptographic checksum can detect selected changes without proving that a correctly transmitted value was true when initially recorded.
- **Availability:** Timely, reliable access to system functions or information for authorized needs under specified conditions. An online server can be available yet return incorrect or unauthorized data.

A service can meet one property while failing another. A publicly accessible document archive may be highly available while failing a particular confidentiality requirement. A locked-down system may preserve secrecy but become unusable when authorized access is required.

**Authenticity**, **accountability**, **privacy**, **safety**, **reliability** and **resilience** are related but distinct claims. It is misleading to call them all synonyms of confidentiality, integrity or availability. For example, a correct safety shutdown can intentionally reduce immediate availability while protecting people.

## Security objectives, requirements, controls and assurance

A **security objective** states the desired protection outcome. A **security requirement** makes a specified part of that outcome assessable. A **control** is a selected safeguard or behavior intended to satisfy some requirements. An **assurance argument** explains why evidence justifies confidence in the security claim.

```text
Protected Interest
       ↓ motivates
Security Objective
       ↓ becomes assessable through
Security Requirements
       ↓ may be supported by
Controls and Architectural Constraints
       ↓ evaluated by
Evidence → Bounded Assurance Claim
```

The arrows describe **conceptual relationships**, not a universal project sequence. A requirement does not guarantee that a control will be selected correctly, a control does not guarantee effective protection, and evidence about one configuration does not guarantee protection across all future configurations.

NIST [SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) is an authoritative starting point for protection needs, systems security engineering and trustworthiness. Its engineering processes are not automatically definitions of the Security Foundations concepts themselves.

## Threats, vulnerabilities and risk are not synonyms

**Threat source**: a potential origin of adverse action or conditions. **Threat event**: an occurrence that can produce adverse consequences. **Vulnerability**: a particular weakness or exposure under conditions enabling a security violation. **Risk**: a scenario-relative consideration of adverse consequences and uncertainty.

A severe storm can be a relevant non-adversarial threat event without a malicious actor. A software weakness may exist even if no one has attempted to exploit it. An observed authentication failure may be benign or suspicious; it does not by itself prove an intrusion.

A published severity score, such as CVSS Base, is not automatically an organization's risk. FIRST explicitly distinguishes [CVSS v4.0 vulnerability severity metrics](https://www.first.org/cvss/v4.0/specification-document) from threat and environmental context.

## Worked example: contrasting protection claims

Suppose a shared record service has these stipulated properties:

- Read requests are permitted only for authenticated users assigned to the appropriate record group.
- A write operation leaves an audit record.
- Backups run once daily.
- A service interruption of several hours is possible if the primary host fails.

Now consider three statements:

**Claim A: “Only assigned users can read customer records.”** This is a confidentiality/authorization claim requiring evidence about policy and every relevant read path, identity assumptions, storage access and possible bypasses. Successful logins by assigned users alone do not establish it.

**Claim B: “All changes are trustworthy because audit records exist.”** This does not follow. The system may record an unauthorized or incorrect change faithfully, or records may be incomplete. Audit logging can support accountability and investigation without guaranteeing initial data integrity.

**Claim C: “The system is resilient because it has backups.”** This does not follow either. Backup age, restoration success, credential compromise, recovery time and environmental dependencies affect the actual protection. A 24-hour backup interval does not guarantee a recovery point of exactly 24 hours under all conditions.

These scenarios are invented to distinguish **objective, mechanism, observation and inference**. They are not measurements of a real product.

## Conceptual boundaries and related references

- [Systems and Engineering](../../fundamentals/systems-engineering/README.md) owns general system boundaries and requirements; [Evidence](../../fundamentals/scientific-analytical-reasoning/evidence.md) owns the general logic of evidentiary support.
- [Threat Sources and Threat Events](../threats-hazards-adversarial-behavior/threat-sources-and-threat-events.md) owns causes and potential occurrences of adverse outcomes.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns context-dependent exploitable weaknesses.
- [Access-Control Policy Models](../trust-identity-authority-principles/access-control-policy-models.md) owns the semantics of authorizing protected actions.
- [Security Observation and Evidence](../security-observation-evidence/observable-observed-and-recorded.md) owns what can be asserted from sensors and records.
- [Operational Foundations](../../operational-foundations/README.md) owns threat modeling, risk assessment, monitoring, incident response and other *methods of practice*.
- Network, Endpoint, Application, Cloud, Industrial, IoT and Identity Knowledge own the specialized implementations of common protection concepts.

## Source orientation

- [NIST information security glossary](https://csrc.nist.gov/glossary/term/information_security), CIA and information-system protection terms.
- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), stakeholder protection needs, trustworthiness and security engineering.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), threat/risk assessment concepts and conditions.
- [Common Criteria / ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1), evaluated security properties and scope limits.

**Source limitation:** This article is a bounded conceptual synthesis. The named standards have their own intended environments and do not decree a universal definition of every security problem. Primary publication landing pages and selected scope statements are cited; complete clause verification and independent qualified expert review remain open.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md). This is a **working pilot**, not an approved permanent canonical article, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot register](../pilots/README.md) · [Candidate inventory](../SUBJECT-INVENTORY-PROPOSAL.md)
