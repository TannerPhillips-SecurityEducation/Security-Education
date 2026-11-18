# Recovery Objectives and Trusted Restoration

**Candidate subject:** SF-11-07 · Security Failure & Resilience  
**Working area:** [Security Failure & Resilience](README.md) · The Fundamentals-style directory structure is adopted; subject ownership remains provisional  
**Artifact type:** Substantive working reference, not an approved canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Pilot Technical Review 04](../PILOT-TECHNICAL-REVIEW-04.md), six bounded material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [Security Foundations proposal](../ARCHITECTURE.md) · [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md)

## Recovery is not merely restarting a system

**Recovery objectives** describe the conditions under which capabilities, data, and protected outcomes must be restored after disruption. **Trusted restoration** is the additional security requirement that the resulting system state, authority relationships, and dependencies have sufficient evidence to justify renewed reliance. These are related but different claims. A service may resume responding while continuing to execute malicious code, disclose information to an unauthorized principal, or depend on an untrusted identity service.

A restoration objective must therefore name the function being restored, the acceptable state of its information, the time boundary, any permitted degraded operation, the relevant trust assumptions, and the evidence that will support an assertion of recovery. Not every objective is a numerical deadline. Some are safety or integrity conditions that must hold before a service is permitted to resume.

[NIST SP 800-184 (2016)](https://csrc.nist.gov/pubs/sp/800/184/final) addresses cybersecurity-event recovery planning, including prioritization, dependencies, realistic exercises, milestones, and improvement. [NIST SP 800-160 Volume 2 Revision 1 (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) places **recover** alongside anticipate, withstand and adapt as cyber-resiliency engineering goals. Neither publication guarantees that service restoration itself proves freedom from compromise.

## What must be restored?

Recovery has several independently assessable dimensions:

| Dimension | Desired result | Distinct failure |
| --- | --- | --- |
| Function | An essential operation serves its intended users | A process is running, but the essential transaction fails |
| Information state | Data is sufficiently complete, current and correct for its purpose | An available database contains corrupted or excessively stale records |
| Security authority | Credentials, identities, privileges and policy enforcement remain appropriate | A restored host accepts an adversary-controlled administrator credential |
| Dependencies | Upstream services, networks, time, keys and configuration meet necessary assumptions | A recovered application relies on a compromised identity provider |
| Evidence | Relevant tests and observations substantiate claims within stated limits | A dashboard indicates “healthy” but only checks network reachability |
| Protected outcomes | Recovery respects required privacy, safety and other protection constraints | Rapid restoration causes unauthorized disclosure or dangerous physical behavior |

These dimensions are an **editorial decomposition** for examining recovery claims, not a quoted NIST taxonomy. A given architecture may require additional dimensions.

Restoration also depends on the **trustworthiness of the recovery source**. A backup with a valid checksum is shown to match the bytes against which that checksum was computed; that fact alone says nothing about whether those bytes contained malware, fraudulent records, unauthorized access rules or compromised secrets. A verified signature can establish a claim about origin or integrity only under the validity and control of the relevant signing keys and verification policy.

## Time and recoverable state are different objectives

[NIST SP 800-34 Revision 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), in its federal information-system contingency-planning context, distinguishes:

- **Recovery Time Objective (RTO):** A recovery time limit associated with unacceptable impact on the supporting system resource and mission/business process. The start and end conditions must be defined when measuring performance.
- **Recovery Point Objective (RPO):** The point in time to which data must be restored, often expressed as the maximum tolerable age or loss window of recoverable data at disruption.
- **Maximum Tolerable Downtime (MTD):** The total disruption a mission/business process can tolerate before significant harm; it is not simply another label for the recovery objective of one supporting system resource. Under the source's business-impact-analysis model, the resource RTO normally must be shorter than the process MTD, including any additional time needed to resume or reprocess work.

These are *objectives*, not measurements of what occurred. In NIST SP 800-34 Rev. 1, the RTO/MTD/RPO distinctions appear in Chapter 3, §3.2.1, printed page 17 (PDF page index 30); the RPO is a data-recovery point, not a direct measurement of every transaction ultimately lost. An **achieved restoration time** and **achieved recovery point** must be compared against them. Because different organizations and standards may define the recovery interval differently, comparisons must use the same boundaries.

For a hypothetical service let the failure time be (t_f), restoration of the required function be (t_r), and latest trusted recoverable data point be (t_p). Under an explicitly simplified measurement model:

```text
Observed recovery duration = t_r - t_f
Observed data-loss window = t_f - t_p
```

This illustrative arithmetic assumes clocks are consistent and that the selected data point is actually usable and trusted. It is not a universal definition of RTO, RPO or incident duration. Replication, journaling, transactional recovery, asynchronous dependencies and partially restored operations can complicate the measurement.

### Worked example: timely but untrusted

A fictional payment service has an RTO of two hours and an RPO of fifteen minutes. A disruption occurs at **09:40**. Its latest usable checkpoint is **09:30**. The core transaction service is reachable and functionally tested at **10:50**.

- Under the stated event-to-service measurement convention, recovery duration is **70 minutes** (09:40 to 10:50), inside the 120-minute RTO; this does not by itself establish that all dependent business processing finished within an MTD.
- The checkpoint is **10 minutes** before disruption (09:30 to 09:40), within the stated 15-minute RPO window *if that point is recoverable, complete and valid for the required data*. Meeting this age window does not prove the precise quantity of lost transactions.
- During the event an attacker acquired an administrative token. If the token remains usable after restoration, neither successful timing test establishes **trusted restoration**.
- If investigators cannot establish that the 09:30 checkpoint is free of the attacker's modifications, the claim that its *trusted* recovery point is 09:30 remains **unknown**.

The outcome is **functional restoration demonstrated; RTO and provisional RPO targets met under the assumptions; restoration of security not yet established**. A single “recovered” flag would erase this material distinction.

## Establishing a justified restoration state

A useful security assertion has the form:

> Under the specified threat model and available evidence, the required function and protected state satisfy the declared restoration conditions at the stated time.

The evidence may need to cover more than the restored workload:

1. **Source provenance and integrity:** Identify the restoration image, data source and configuration version; assess whether the source was created before or after suspected compromise, and whether its verification mechanisms are trustworthy.
2. **Authority and control:** Determine whether credentials, signing keys, sessions, trust anchors, recovery administrators and delegated privileges could perpetuate unauthorized control.
3. **System and dependency state:** Examine the boot and execution environment, service configuration, policy and necessary external dependencies. A clean application binary does not establish a clean host or identity plane.
4. **Functional and protective behavior:** Test required operations *and* meaningful authorization, integrity, confidentiality and safety constraints under representative conditions.
5. **Residual uncertainty:** Record detection blind spots, unexamined dependencies, unknown initial compromise times, and the limits of available logs or snapshots.

This is a conceptual **claim-and-evidence framework**, not a prescribed incident-response playbook. The practical sequencing of acquisition, eradication, restoration, communications and incident command belongs in [Operational Foundations](../../operational-foundations/README.md). Security-critical decisions may require additional independent evidence and organizational authorization before resumption.

There is no universal test that proves an arbitrary complex restored system contains no compromise. Evidence can increase confidence within a bounded threat model; it cannot eliminate unexamined paths, unseen adversary actions or unknown defects. [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns that broader justification problem.

## Restoration can reintroduce the original failure

Returning to a prior state is not necessarily returning to a *safe* state. An old image might restore an exploitable vulnerability, an unpatched dependency, a compromised secret, an unsafe configuration, or an adversary-created account. Conversely, rebuilding from newly verified components can still fail if it reuses a compromised root of trust or reimports contaminated data.

Consider two backups taken at 08:00 and 09:30. An intrusion is discovered at 10:00, but the initial compromise time is uncertain. Selecting the most recent backup can reduce ordinary data loss while increasing the chance of restoring compromised state. Selecting the older backup may reduce one exposure but increase data loss and still does not establish cleanliness. The relevant decision turns on evidence of compromise chronology, data validation, protected interests and dependencies, not backup age alone.

An apparently successful recovery can also reproduce the root cause of failure. Resilience therefore includes learning and adaptation, but **adaptation is not identical to restoration**. [Resilience, Survivability, and Robustness](resilience-survivability-and-robustness.md) addresses the broader system capability; [Compromise and Loss of Security](compromise-and-loss-of-security.md) covers the conditions and evidence of compromise.

## Boundaries and relationships

- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md): contextual protection requirements that restoration must satisfy.
- [Controls, Safeguards, and Security Functions](../security-controls-defense-mechanisms/controls-safeguards-and-security-functions.md): safeguards whose effective operation may need re-establishment.
- [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md): risk-based selection of recovery tolerance and residual risk.
- [Fundamentals: Reliability and Failure](../../fundamentals/systems-engineering/reliability-and-failure.md) and [Dependencies](../../fundamentals/systems-engineering/dependencies.md): domain-agnostic failure and dependency mechanisms.
- [Operational Foundations](../../operational-foundations/README.md): execution of recovery, continuity, investigation and response.
- [Network](../../../network/README.md), [Endpoint](../../../endpoint/README.md) and [Identity](../../../identity/README.md): concrete mechanisms, infrastructure and implementation boundaries.

## Primary sources and review limits

- [NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems* (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final): contingency-planning definitions and recovery-objective context. It is a historical scoped reference, not a current universal recovery mandate.
- [NIST CSRC glossary: RTO](https://csrc.nist.gov/glossary/term/recovery_time_objective) and [RPO](https://csrc.nist.gov/glossary/term/recovery_point_objective): concise source-attributed terminology.
- [NIST SP 800-184, *Guide for Cybersecurity Event Recovery* (2016)](https://csrc.nist.gov/pubs/sp/800/184/final): recovery planning, restoration dependencies, testing and continual improvement.
- [NIST SP 800-160 Vol. 2 Rev. 1, *Developing Cyber-Resilient Systems* (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final): cyber-resiliency goals and engineering scope.

**Evidence limitation:** Primary-source landing pages and accessible excerpts were consulted for concept and scope selection. A separately recorded **scoped model-assisted review** now covers six material claim groups in [Review 04](../PILOT-TECHNICAL-REVIEW-04.md), including direct visual inspection of NIST SP 800-34r1's RTO/RPO/MTD passage. Complete source-passage verification, independent expert review and publication acceptance remain open. Its restoration dimensions, example and claim framework are editorial interpretations, not quoted NIST requirements.

[Security Foundations](../README.md) · [Area index](README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
