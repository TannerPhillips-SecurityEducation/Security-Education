# Security Foundations

> **Scope:** Shared concepts and principles for understanding security and insecurity across technical systems and the seven specialized knowledge domains.

**Division status:** Approved.  
**Internal architecture status:** Working proposal **v0.1**, **not approved**.  
**Candidate coverage:** Twelve provisional knowledge areas and 94 candidate subject headings. No canonical subject articles have been created by this architecture pass.

## Architectural documentation

- [**Governing Architecture Proposal**](ARCHITECTURE.md): Definition, conceptual protection model, divisional scope, proposed knowledge areas, placement tests, and editorial requirements.
- [**Candidate Subject Inventory**](SUBJECT-INVENTORY-PROPOSAL.md): 12 proposed areas, 94 candidate subjects, and intended canonical scopes.
- [**Canonical Ownership & Boundary Review**](OWNERSHIP-BOUNDARIES.md): 25 cross-division and cross-domain overlap cases requiring architectural review.
- [**Development & Verification Plan**](DEVELOPMENT-PLAN.md): Scope approval, sources, controlled pilots, article authoring, technical review, and publication acceptance.

## The governing distinction

[Fundamentals](../fundamentals/README.md) explains **how technical systems work** without making security their organizing principle. **Security Foundations** explains protection objectives, threats, vulnerabilities, risk, trust, safeguards, evidence and assurance. [Operational Foundations](../operational-foundations/README.md) owns shared **methods for performing security work**. The [seven specialized domains](../../README.md#knowledge-domains) own their functions and implementation details.

For example, the general meaning of *an event* belongs in Fundamentals. The security relevance of an event and the evidentiary limits of classifying it are candidate concerns here. Incident triage is an operational activity, while collecting events with a named sensor belongs to the relevant technical domain.

## Candidate coverage at a glance

| Area | Topic |
| --- | --- |
| 01 | Security Meaning & Objectives |
| 02 | Protected Interests, Assets & Harm |
| 03 | Threats & Adversarial Behavior |
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
