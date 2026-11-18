# Security Foundations

> **Scope:** Shared concepts and principles for understanding security and insecurity across technical systems and the seven specialized knowledge domains.

**Division status:** Approved.  
**Internal architecture status:** Model-grounded working proposal **v0.2**, **not approved**.  
**Candidate coverage:** Twelve provisional knowledge areas and 94 candidate subject headings (v0.2 boundary refinements). No canonical subject articles have been created by this architecture pass.

## Architectural documentation

- [**Governing Architecture Proposal**](ARCHITECTURE.md): Definition, conceptual protection model, divisional scope, proposed knowledge areas, placement tests, and editorial requirements.
- [**Candidate Subject Inventory**](SUBJECT-INVENTORY-PROPOSAL.md): 12 proposed areas, 94 candidate subjects, and revised intended canonical scopes.
- [**Established Security Models & Frameworks Crosswalk**](ESTABLISHED-MODEL-CROSSWALK.md): 20 established models, taxonomies, control references and heuristics aligned to candidate conceptual responsibilities, with primary-source starting points and limits.
- [**Canonical Ownership & Boundary Review**](OWNERSHIP-BOUNDARIES.md): 25 cross-division and cross-domain overlap cases requiring architectural review.
- [**Development & Verification Plan**](DEVELOPMENT-PLAN.md): Scope approval, sources, controlled pilots, article authoring, technical review, and publication acceptance.

## The governing distinction

[Fundamentals](../fundamentals/README.md) explains **how technical systems work** without making security their organizing principle. **Security Foundations** explains protection objectives, threats, vulnerabilities, risk, trust, safeguards, evidence and assurance. [Operational Foundations](../operational-foundations/README.md) owns shared **methods for performing security work**. The [seven specialized domains](../../README.md#knowledge-domains) own their functions and implementation details.

For example, the general meaning of *an event* belongs in Fundamentals. The security relevance of an event and the evidentiary limits of classifying it are candidate concerns here. Incident triage is an operational activity, while collecting events with a named sensor belongs to the relevant technical domain.

## Model-grounded interpretation

Security Foundations should not invent new laws of security where tested models already exist. The [Established Model Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) uses the CIA Triad, STRIDE, Diamond Model, Unified Kill Chain, MITRE ATT&CK, Pyramid of Pain, CWE/CAPEC/CVSS, NIST risk guidance, Zero Trust, D3FEND, systems security engineering and NIST CSF as **complementary views**. They do not form a single interchangeable hierarchy, and some are frameworks, taxonomies or heuristics rather than formal models.

The 12 areas below are **working navigation hypotheses**, not a forced reflection of any one of those models. Their names, number and 94-subject inventory remain open to revision based on model coverage, conceptual overlap and source evidence.

## Candidate coverage at a glance

| Area | Topic |
| --- | --- |
| 01 | Security Meaning & Objectives |
| 02 | Protected Interests, Assets & Harm |
| 03 | Threats, Hazards & Adversarial Behavior |
| 04 | Weaknesses, Vulnerabilities & Exposure |
| 05 | Security Risk & Uncertainty |
| 06 | Trust, Identity & Authority Principles |
| 07 | Security Controls & Defense Mechanisms |
| 08 | Secure Design & Architecture |
| 09 | Cryptography & Information Protection |
| 10 | Security Observation & Evidence |
| 11 | Security Failure & Resilience |
| 12 | Security Assurance, Governance & Accountability |

**None of these proposed areas or their 94 subjects is approved merely because this index lists them.** The area count, subject names, ownership decisions and precise definition remain subject to architectural review. This is a knowledge reference, not a course or assessment platform: no Knowledge Checks or Practical Assessments.

[Foundations](../README.md) · [Security Knowledge](../../README.md) · [Knowledge relationship conventions](../../RELATIONSHIPS.md)
