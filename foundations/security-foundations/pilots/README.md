# Security Foundations | Working Article Register and Historical Pilot Paths

**Division:** [Security Foundations](../README.md)  
**Status:** **18 Reviewed (model-assisted), 2 Draft** across five completed scoped audits (**98 material claim groups**). The SF-09-02 and SF-09-07 Drafts await their next separate Review batch; none is source-Verified, permanently approved or Published.  
**Architecture:** [Governing Proposal v0.3](../ARCHITECTURE.md), [Flexible 96-candidate Working Inventory](../SUBJECT-INVENTORY-PROPOSAL.md), [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)  
**Scope:** This register indexes 14 historically relocated manuscripts and 6 newer area-first manuscripts (four Reviewed, **two current Drafts**). All substantive articles live inside provisional knowledge-area directories following the Fundamentals pattern. **Only the historical 14 have `pilots/` navigation aliases**; later articles link directly to their area homes. Current area identities and inventory counts remain revisionable.

## Actual working article locations and historical review register

| Candidate ID | Working article | Development | Source review | Distinct conceptual question |
| --- | --- | --- | --- | --- |
| SF-01-01 | [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md) | **Reviewed (model-assisted)** | Core claims checked | What counts as a conditional security claim rather than an absolute label? |
| SF-03-01 | [Threat Sources and Threat Events](../threats-hazards-adversarial-behavior/threat-sources-and-threat-events.md) | **Reviewed (model-assisted)** | Core claims checked | How do adversarial and non-adversarial threat sources differ from occurrences and consequences? |
| SF-04-02 | [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) | **Reviewed (model-assisted)** | Core claims checked | How do weakness, vulnerability, exposure, exploitation, severity and risk differ? |
| SF-04-08 | [Side Channels, Covert Channels, and Unintended Information Leakage](../weaknesses-vulnerabilities-exposure/side-channels-covert-channels-and-unintended-information-leakage.md) | **Reviewed (model-assisted)** | Core claims checked in [Review 05](../PILOT-TECHNICAL-REVIEW-05.md) | How do indirect secret-dependent effects differ from cooperating, policy-violating covert signaling and ordinary disclosure? |
| SF-06-09 | [Access-Control Policy Models](../trust-identity-authority-principles/access-control-policy-models.md) | **Reviewed (model-assisted)** | Core claims checked | What differentiates policy decision models from authentication and enforcement? |
| SF-08-09 | [Information-Flow Security and Noninterference](../secure-design-architecture/information-flow-security-and-noninterference.md) | **Reviewed (model-assisted)** | Core claims checked | When is a flow/observation permitted and why can access control be insufficient? |
| SF-09-02 | [Randomness, Entropy, and Nonces](../cryptography-information-protection/randomness-entropy-and-nonces.md) | **Draft** | References listed; separate review pending | How do entropy, pseudorandomness, nonces and uniqueness differ, and what failure conditions defeat them? |
| SF-09-07 | [Key Lifecycle and Cryptographic Failures](../cryptography-information-protection/key-lifecycle-and-cryptographic-failures.md) | **Draft** | References listed; separate review pending | How do keys acquire, retain and lose justified protection across generation, deployment, compromise and transition? |
| SF-09-09 | [Cryptographic Composition and Protocol Security](../cryptography-information-protection/cryptographic-composition-and-protocol-security.md) | **Reviewed (model-assisted)** | Core claims checked | When do secure primitives fail to establish complete protocol objectives? |
| SF-10-02 | [Observable, Observed and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) | **Reviewed (model-assisted)** | Core claims checked | What can a security record actually establish about an occurrence or actor? |
| SF-10-08 | [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) | **Reviewed (model-assisted)** | Core claims checked in [Review 04](../PILOT-TECHNICAL-REVIEW-04.md) | How far can records support causal explanations and attribution at different identity levels? |
| SF-12-01 | [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) | **Reviewed (model-assisted)** | Core claims checked | What evidence and arguments support a bounded security property claim? |
| SF-12-05 | [Compliance and Effective Security](../security-assurance-governance-accountability/compliance-and-effective-security.md) | **Reviewed (model-assisted)** | Core claims checked in [Review 04](../PILOT-TECHNICAL-REVIEW-04.md) | Why can conformity evidence and demonstrated security outcomes diverge? |

| SF-05-01 | [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md) | **Reviewed (model-assisted)** | Core claims checked | Scenario-relative likelihood, harm, uncertainty, time horizon and why severity is not organizational risk |
| SF-07-01 | [Controls, Safeguards, and Security Functions](../security-controls-defense-mechanisms/controls-safeguards-and-security-functions.md) | **Reviewed (model-assisted)** | Core claims checked | Protection objective versus selected mechanism, implemented coverage, measured effect and assurance |

| SF-01-08 | [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md) | **Reviewed (model-assisted)** | Core claims checked | Different protected interests, including privacy harm from authorized processing and safety constraints |
| SF-11-01 | [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) | **Reviewed (model-assisted)** | Core claims checked | Security violation, confirmed compromise, suspicion and restoration are not equivalent |
| SF-11-04 | [Resilience, Survivability, and Robustness](../security-failure-resilience/resilience-survivability-and-robustness.md) | **Reviewed (model-assisted)** | Core claims checked | Anticipate, withstand, recover, adapt; RTO/RPO and trusted restoration |
| SF-11-07 | [Recovery Objectives and Trusted Restoration](../security-failure-resilience/recovery-objectives-and-trusted-restoration.md) | **Reviewed (model-assisted)** | Core claims checked in [Review 04](../PILOT-TECHNICAL-REVIEW-04.md) | Recovery-target measurement versus evidenced trusted restoration |
| SF-12-08 | [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) | **Reviewed (model-assisted)** | Core claims checked | Legitimate security authority, privacy rights, proportionality and human harm |

**Record count:** **18 substantive Reviewed working area manuscripts** across [Reviews 01–05](../PILOT-TECHNICAL-REVIEW-05.md), checking **98 bounded material claim groups**, plus **2 new Drafts** (SF-09-02 and SF-09-07) awaiting a separately recorded technical Review batch. **76 of 96** working subject candidates have no substantive article. Historical review counts and the working taxonomy remain distinct from publication approval.

## Pilot technical review evidence

[Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md) checks **40 material claim groups** across the eight articles. The review corrected a conflation between *actual insecurity* and *lack of assurance evidence* and updated standards references to **RFC 9846 (TLS 1.3, July 2026)** and **ISO/IEC 15408-1:2026**.

**All 17 currently authored working manuscripts** have Reviewed (model-assisted) / Core claims checked states with their own bounded technical-review evidence. No article has complete claim-to-passage verification, independent expert acceptance, internal taxonomy ratification or Published status.

**Second pilot audit:** [Pilot Technical Review 02](../PILOT-TECHNICAL-REVIEW-02.md) checks **10 additional material claim groups** concerning risk scenarios, time horizons, vulnerability severity, NIST 800-53/800-53A control and assessment distinctions, MITRE D3FEND, and the difference between deployed safeguards and evidenced effects.

**Wave 03 review:** The four new articles test SF-11's compromise/resilience distinctions, SF-01's privacy/safety/reliability comparison, and SF-12's legitimacy/human-harm constraints. All four have passed [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md) (20 material groups). Source references use NIST SP 800-160v2r1, 800-34r1, 800-61r3, Privacy Framework v1.0, ISO/IEC Guide 51:2014 and relevant human-rights instruments. The proposed areas/subject counts are **not** approved by these manuscript additions.

**Third pilot audit:** [Pilot Technical Review 03](../PILOT-TECHNICAL-REVIEW-03.md) checked 20 material claim groups for compromise, cyber resiliency, recovery constraints, privacy from authorized data use, functional safety and legitimacy. It visually inspected the RTO/RPO/MTD definitions in NIST SP 800-34r1, recomputed the example timings/reliability value, and separated publication from technical review.

**Fourth pilot audit:** [Pilot Technical Review 04](../PILOT-TECHNICAL-REVIEW-04.md) checks **18 material claim groups** across evidentiary inference, trusted recovery and compliance/effectiveness. It recomputes conditional detector and recovery-timing examples, clarifies NIST source boundaries, and records the review-first continuation rule.

**Fifth pilot audit:** [Pilot Technical Review 05](../PILOT-TECHNICAL-REVIEW-05.md) checks ten material claim groups for SF-04-08, recomputes the hypothetical channel-capacity model, distinguishes storage/timing channel categories, and records assumptions and source-version limitations. The manuscript advanced only after the separate review and documented corrections.

## Development states

- **Inventoried:** An editorial subject exists in the working inventory, without an article.
- **Draft:** A substantive manuscript exists with technical explanations and bibliography; source-level review is pending.
- **Reviewed (model-assisted):** A separately recorded bounded technical audit has checked material claims, examples, source scope, counterexamples and boundaries. It is not independent expert approval.
- **Source-Verified:** Stronger claim-to-passage coverage has been documented under an explicit evidence scope.
- **Published:** The internal taxonomy/ownership, required review gates and qualified acceptance have been explicitly satisfied; **none** of the pilot articles has this state.

The distinction between **architecture approval**, **article technical review**, **source verification** and **publication** is mandatory. A pilot may be technically useful and Reviewed before its final canonical path is approved.

## Conceptual ownership and expansion policy

The candidate headings and the number of pilot articles are both flexible. Their suitability is tested against established security models, standards, Fundamentals prerequisites, the separate Operational Foundations responsibility, and the seven specialized knowledge domains. A pilot may be revised, split, merged, archived or moved if evidence supports that action.

Cross-domain links are introduced as related technical subjects and implementations develop, not to meet a numeric quota. No Knowledge Checks, Practical Assessments or fixed curricular reading order are included.

[Security Foundations](../README.md) · [Architecture Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md) · [Development Plan](../DEVELOPMENT-PLAN.md)

## Structural relocation record (November 18, 2026)

The repository owner explicitly requested **uniform Fundamentals-style directory organization with tailored content**, while maintaining flexibility in area/subject counts. All fourteen substantive article bodies have therefore been relocated to the corresponding provisional area directories with their metadata, scoped audit history and source-review state preserved. Former `pilots/<filename>.md` files remain **lightweight navigation aliases** for existing internal/external links. The article paths in the table above are the **real working manuscripts**, not duplicate copies. Area membership remains provisional pending separate governance approval.
