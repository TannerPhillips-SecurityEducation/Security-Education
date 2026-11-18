# Security Foundations

> **Scope:** Shared concepts and principles for understanding security and insecurity across technical systems and the seven specialized knowledge domains.

**Division status:** Approved.  
**Internal architecture status:** Model-grounded working proposal **v0.3**, **not ratified**.  
**Candidate coverage:** **Twelve provisional areas and 96 active candidate subjects** after four source-grounded additions and two consolidations. Both numbers remain flexible. **Eight substantive article pilots** exist under [pilots](pilots/README.md); no permanent canonical article tree has been ratified.

## Architectural documentation

- [**Governing Architecture Proposal**](ARCHITECTURE.md): Definition, conceptual protection model, divisional scope, proposed knowledge areas, placement tests, and editorial requirements.
- [**Candidate Subject Inventory**](SUBJECT-INVENTORY-PROPOSAL.md): 12 proposed areas, 96 active candidate subjects, with documented earlier-ID aliases, and revised intended canonical scopes.
- [**Established Security Models & Frameworks Crosswalk**](ESTABLISHED-MODEL-CROSSWALK.md): 26 established model, standard, taxonomy and technical-reference groups aligned to candidate conceptual responsibilities, with primary-source starting points and limits.
- [**Canonical Ownership & Boundary Review**](OWNERSHIP-BOUNDARIES.md): 30 working cross-division, cross-model and cross-domain boundary cases requiring architectural review.
- [**Development & Verification Plan**](DEVELOPMENT-PLAN.md): Scope approval, sources, controlled pilots, article authoring, technical review, and publication acceptance.

## Architecture adjudication and pilot development

- [**Architecture Adjudication 02**](ARCHITECTURE-ADJUDICATION-02.md): Full 94-to-96 reconciliation, including two consolidated IDs and four added candidate subjects, supported by model/source boundaries. Both the area and subject counts may expand or contract.
- [**Eight Source-Led Article Pilots**](pilots/README.md): Substantive exploratory articles across security objectives, threats, vulnerabilities, authorization policies, information-flow security, cryptographic composition, security observation, and assurance. **They are not final canonical locations or Published articles.**
- [**Source Crosswalk v0.2**](ESTABLISHED-MODEL-CROSSWALK.md): 26 reference groups, including 2025/2026 source-version context, cryptographic specifications and noninterference/side-channel distinctions.

**Governance separation:** The division is approved; the internal hierarchy and 96 candidate subjects are **not yet ratified**. Article authoring, technical audit, source-passage verification, qualified independent review and final publication acceptance are separate evidence states. No draft count or working model is a required future quota.

## The governing distinction

[Fundamentals](../fundamentals/README.md) explains **how technical systems work** without making security their organizing principle. **Security Foundations** explains protection objectives, threats, vulnerabilities, risk, trust, safeguards, evidence and assurance. [Operational Foundations](../operational-foundations/README.md) owns shared **methods for performing security work**. The [seven specialized domains](../../README.md#knowledge-domains) own their functions and implementation details.

For example, the general meaning of *an event* belongs in Fundamentals. The security relevance of an event and the evidentiary limits of classifying it are candidate concerns here. Incident triage is an operational activity, while collecting events with a named sensor belongs to the relevant technical domain.

## Model-grounded interpretation

Security Foundations should not invent new laws of security where tested models already exist. The [Established Model Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) uses the CIA Triad, STRIDE, Diamond Model, Unified Kill Chain, MITRE ATT&CK, Pyramid of Pain, CWE/CAPEC/CVSS, NIST risk guidance, Zero Trust, D3FEND, systems security engineering and NIST CSF as **complementary views**. They do not form a single interchangeable hierarchy, and some are frameworks, taxonomies or heuristics rather than formal models.

The 12 areas below are **working navigation hypotheses**, not a forced reflection of any one of those models. Their names, number and 96-subject working inventory remain open to revision based on model coverage, conceptual overlap and source evidence.

## Candidate coverage at a glance

| Area | Provisional knowledge area | Active candidate subjects |
| --- | --- | ---: |
| 01 | Security Meaning & Objectives | 8 |
| 02 | Protected Interests, Assets & Harm | 6 |
| 03 | Threats, Hazards & Adversarial Behavior | 7 |
| 04 | Weaknesses, Vulnerabilities & Exposure | 8 |
| 05 | Security Risk & Uncertainty | 8 |
| 06 | Trust, Identity & Authority Principles | 9 |
| 07 | Security Controls & Defense Mechanisms | 8 |
| 08 | Secure Design & Architecture | 9 |
| 09 | Cryptography & Information Protection | 9 |
| 10 | Security Observation & Evidence | 8 |
| 11 | Security Failure & Resilience | 8 |
| 12 | Security Assurance, Governance & Accountability | 8 |

| **Total** | **12 proposed areas** | **96 active candidates** |

**None of these proposed areas or their 96 current subjects is automatically approved by being listed here.** The area count, subject names, ownership decisions and precise definition remain subject to architectural review. This is a knowledge reference, not a course or assessment platform: no Knowledge Checks or Practical Assessments.

[Foundations](../README.md) · [Security Knowledge](../../README.md) · [Knowledge relationship conventions](../../RELATIONSHIPS.md)
