# Compromise and Loss of Security

**Candidate subject:** SF-11-01 · Security Failure & Resilience  
**Artifact type:** Substantive working article pilot; proposed canonical ownership, **not ratified**  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md) (five material claim groups); complete source verification and qualified independent review remain open  
**Architecture:** [Flexible working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Proposed ownership boundaries](../OWNERSHIP-BOUNDARIES.md)

## A security violation, a compromised state and evidence about either are distinct

A **security violation** occurs when a specified security requirement, policy or protected property is breached under relevant conditions. A **compromise** concerns loss or violation of protection of an asset, system, key, process or information under a particular security model. What is compromised, by whom or what, and to what extent must be established rather than inferred from an alert label.

The [NIST glossary for compromise](https://csrc.nist.gov/glossary/term/compromise) collects **source-dependent definitions**. Some concern unauthorized disclosure or modification of protected information; others describe a judgment, based on evidence, that a system-security policy was violated; key compromise has specialized meanings. Consequently, the term is not one universal binary flag meaning that *every component is under an attacker's control*.

A **suspected compromise** is an evidence-based hypothesis, not the same proposition as a demonstrated security-property violation. An **incident** is defined by its governing organizational, legal or standards context and may cover actual or imminent adverse security conditions without requiring proof that every suspected asset has been compromised. [NIST's incident glossary](https://csrc.nist.gov/glossary/term/security_incident) provides multiple such source-scoped meanings.

| Security concept | Illustrative question | Not sufficient to prove |
| --- | --- | --- |
| Weakness | Is a control missing or incorrectly designed? | That anyone exercised it |
| Exploitation attempt | Did activity try to exploit a vulnerability? | That the action succeeded |
| Security violation | Did an actual result violate the defined protection property? | That all assets were compromised |
| Compromised state | Which information, authority or system boundary has lost its expected protection? | The real actor's identity or intent |
| Suspicion or finding | What claim is supported by observed evidence? | The complete ground truth |
| Consequence | What protected interests were affected? | The future likelihood of recurrence |
| Residual capability | What protected functions still work after the event? | That remaining operation is trustworthy |

The proposed SF-04-05 subject owns the *mechanism and act of exploitation*. SF-11-01 owns the **resulting security conditions and bounded consequences**. SF-10 owns evidentiary observation and attribution; Operational Foundations owns declaring and handling incidents.

## Security loss can be partial, layered and conditional

Security is not an indivisible substance that disappears uniformly across a system. Confidentiality, integrity, availability, authenticity, access-control assurance, and other protections can fail differently, for different objects and time intervals.

A document may have been disclosed without evidence that its source data were modified. A machine can stop serving legitimate requests while its stored records remain intact. A privileged session may be exposed while a cryptographic key remains uncompromised, or a key may be compromised without proof of its subsequent use.

**Scope is necessary.** A claim that one user's credentials were exposed does not establish that the entire identity provider was compromised. Conversely, a known compromised principal may create unresolved questions about systems and transactions influenced by that principal.

A security state may also be **unknown**. The absence of observed malicious activity, or the presence of a vendor "healthy" status, does not independently establish a trusted operating state.

## Violations, persistence and trust of dependent components

A system can appear to resume normal behavior while unsafe conditions persist. Possible retained effects include altered authorization policies, exposed secrets, substituted binaries, untrusted firmware, modified scheduled tasks, changed dependencies, malicious persistence mechanisms or invalid integrity evidence. These are distinct possibilities and cannot be asserted for a real target without evidence.

A **trust dependency** matters when a restored service relies on components or keying material whose integrity or origin is not established. Restoring an apparently clean application onto a compromised administrative environment may recreate the possibility of an unauthorized action.

The proposed SF-11-08 subject concerns adversarial persistence and the assumptions it changes. [Cryptographic Composition and Protocol Security](cryptographic-composition-and-protocol-security.md) addresses key and protocol properties. [Security Claims and Assurance Arguments](security-claims-and-assurance-arguments.md) addresses what justifies declaring a recovered state trustworthy.

## Containment is not restoration; restoration is not proof of trust

**Containment** constrains an adverse effect or its propagation under a defined system boundary. **Restoration** recovers selected functions, data or configuration. **Trusted restoration** additionally requires evidence that the recovered state meets the security properties that matter.

A rebuilt service may become available but still accept an unauthorized credential. A backup may be authentic yet contain data that were already corrupted before the backup was made. Redundancy may preserve service availability while replicating the same incorrect or malicious data to every copy.

The relevant distinctions are:

- **Functional restoration:** The specified service can operate again.
- **Data recovery:** Selected state can be recovered to an identified point or version.
- **Security-state assurance:** There are justified grounds to believe the recovered system's authority, integrity, confidentiality and dependencies meet their stated requirements.
- **Residual uncertainty:** Remaining unknowns are documented, not relabeled as proof of safety.

The detailed response, eradication, restoration workflows and incident communications belong to [Operational Foundations](../../operational-foundations/README.md). [NIST SP 800-61 Rev. 3 (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) is a current operational incident-response reference, **not** the classification scheme for this foundational article.

## Worked example: three different security states

Assume an invented records service with correctly defined object-level read permissions.

**Situation A: Failed attempt.** An unauthorized caller requests restricted record R; the service returns denial and its response contains no protected record data. The observed behavior supports a denial for this particular request. It does not demonstrate the presence of a compromised state.

**Situation B: Confirmed unauthorized read.** The same policy forbids user U from reading R, but the service's response is verified to contain R's confidential contents. This is evidence of a confidentiality violation under the stipulated policy. It does **not** establish that R was modified, that the entire server is controlled by an adversary, or who physically operated U's session.

**Situation C: Service restored but trust unknown.** The service is restarted from an older image and responds to authorized test requests, yet the source of its administrative signing key has not been checked. The evidence supports *functional availability* for the tested requests; whether the recovery is **trustworthy** remains uncertain.

The same event may support multiple claims, but each claim needs its own proof obligations. A single alert or a passed smoke test should not be used as a universal proxy for compromise, restoration and assurance.

## Compromise is not a universal threat-intent conclusion

A storm, accidental deletion, human error or malfunction can violate specified security objectives without being evidence of malicious agency. Some legal and technical incident definitions encompass such non-adversarial conditions. In other contexts, "compromise" may be reserved for unauthorized disclosure, modification or control. A knowledge reference must **state the adopted definition**, rather than forcing all security failures into an adversary model.

Likewise, a suspected intrusion event can be represented under the Diamond Model or mapped conditionally to ATT&CK behavior. Those mappings do not themselves identify a person or show that the hypothesized compromise succeeded.

## Dependencies and canonical boundaries

- [Security and Insecurity](security-and-insecurity.md): conditional protection properties and epistemic uncertainty.
- [Threat Sources and Threat Events](threat-sources-and-threat-events.md): sources and possible harmful occurrences.
- [Vulnerabilities and Exploitability](vulnerabilities-and-exploitability.md): weaknesses, exposure and attempted exploit pathways.
- [Observable, Observed, and Recorded](observable-observed-and-recorded.md): sensor, logging and inference limits.
- [Resilience, Survivability, and Robustness](resilience-survivability-and-robustness.md): continued valued function, damage limitation and trustworthy recovery.
- [Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md): generic system-failure concepts, not security-specific compromise judgments.
- [Operational Foundations](../../operational-foundations/README.md): investigation, containment and recovery execution.
- [Endpoint Knowledge](../../../endpoint/README.md), [Cloud Knowledge](../../../cloud/README.md), [Application Knowledge](../../../application/README.md): concrete implementation and evidence.

## Source references

- [NIST glossary: Compromise](https://csrc.nist.gov/glossary/term/compromise), multiple context-specific definitions including information and key compromise.
- [NIST glossary: Security Incident](https://csrc.nist.gov/glossary/term/security_incident), distinct source-scoped incident meanings.
- [NIST SP 800-160 Vol. 2 Rev. 1 (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), systems security engineering under adverse and compromised conditions.
- [NIST SP 800-61 Rev. 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final), incident-response recommendations (operational methodology, not canonical compromise ontology).

**Editorial limitation:** The examples are hypothetical. Distinct NIST glossary senses are not interchangeable definitions; a specific regulatory or technical scope must be documented. This is a working pilot, not a forensic conclusion, a certified recovery procedure or a ratified canonical article. Claim-to-passage technical review remains pending.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md). This remains a **pilot**, not a ratified canonical subject, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](README.md)
