# Security Foundations

> **Scope:** Shared concepts and principles for understanding security and insecurity across technical systems and the seven specialized knowledge domains.

**Division status:** Approved.  
**Structural organization:** **Fundamentals-style division → area README → substantive area article** pattern explicitly adopted; individual area names, subject ownership and 96-candidate inventory remain **provisional and flexible**.  
**Current coverage:** **12 provisional knowledge-area directories, 96 candidate subjects, 29 Reviewed (model-assisted), 0 Draft and 67 not yet authored**. All 29 substantive working articles reside inside their provisional area directories. The original fourteen [historical pilot aliases](pilots/README.md) remain functional. Eight separate scoped technical reviews checked **179 material claim groups**. Area identities and subject counts remain provisional and flexible; no publication approval is implied.

## Contributor and Agent Operating Contract

[**AGENTS.md: Security Foundations Editorial & Engineering Contract**](AGENTS.md) applies to this division and its descendants. It transfers the observed **architecture, canonical ownership, substantive authoring, source evidence, scoped technical-review, change-control, and validation discipline** from the [Fundamentals reference corpus](../fundamentals/README.md) while retaining this division's **unratified, flexible working taxonomy**.

This file is a reusable **operating guide**, not authorization to claim new user approvals, automatically promote pilots to permanent canonical pages, or infer publication acceptance from green CI. It also requires reconciliation of current article and review states rather than carrying forward stale historical counts.

**Authoring sequence:** **Draft batch → Review batch.** Both stages may involve **multiple articles**, with variable batch size and technical depth governed by concepts and evidence, not a one-article limit. The next authoring-related response after a Draft batch reviews all its pending manuscripts; a single documented audit may cover several articles, but each needs its own material-claim findings and evidence status. Reconcile article and area registers and validate **before drafting another batch**. Reviewed is not Verified or Published. [Review 04](PILOT-TECHNICAL-REVIEW-04.md) demonstrates a three-article review batch. Historical `pilots/` redirects are mandatory only for manuscripts documented in [Adjudication 03's relocation map](AREA-STRUCTURE-ADJUDICATION-03.md).

## Architectural documentation

- [**Governing Architecture Proposal**](ARCHITECTURE.md): Definition, conceptual protection model, divisional scope, proposed knowledge areas, placement tests, and editorial requirements.
- [**Candidate Subject Inventory**](SUBJECT-INVENTORY-PROPOSAL.md): 12 proposed areas, 96 active candidate subjects, with documented earlier-ID aliases, and revised intended canonical scopes.
- [**Established Security Models & Frameworks Crosswalk**](ESTABLISHED-MODEL-CROSSWALK.md): 30 established model, standard, taxonomy and technical-reference groups aligned to candidate conceptual responsibilities, with primary-source starting points and limits.
- [**Canonical Ownership & Boundary Review**](OWNERSHIP-BOUNDARIES.md): 34 working cross-division, cross-model and cross-domain boundary cases requiring architectural review.
- [**Development & Verification Plan**](DEVELOPMENT-PLAN.md): Scope approval, sources, controlled pilots, article authoring, technical review, and publication acceptance.

## Architecture adjudication and pilot development

- [**Architecture Adjudication 02**](ARCHITECTURE-ADJUDICATION-02.md): Full 94-to-96 reconciliation, including two consolidated IDs and four added candidate subjects, supported by model/source boundaries. Both the area and subject counts may expand or contract.
- [**Working Article Register and Historical Compatibility Paths**](pilots/README.md): Indexes 29 Reviewed (model-assisted) working area manuscripts and preserves the original 14 historic pilot aliases without duplicate substantive bodies.
- [**Area Structure Adjudication 03**](AREA-STRUCTURE-ADJUDICATION-03.md): User-approved Fundamentals-style folder pattern, 12 provisional area indexes, 14 relocations and honest structural-versus-taxonomy approval limits.
- [**Development & Verification Register**](DEVELOPMENT-VERIFICATION-REGISTER.md): All 96 candidate IDs, actual article paths and their independent authoring/source states.
- [**Working Canonical Ownership Register**](CANONICAL-OWNERSHIP-REGISTER.md): Provisional subject owners, precise conceptual boundaries, actual manuscripts and historical consolidations.
- [**Pilot Technical Review 01**](PILOT-TECHNICAL-REVIEW-01.md): 40 claim groups across the original eight pilots; corrected insecurity/uncertainty and current TLS/Common Criteria versions.
- [**Pilot Technical Review 02**](PILOT-TECHNICAL-REVIEW-02.md): 10 additional claim groups across the risk and defensive-controls pilots, separating severity from risk and control listings from measured effects.
- [**Pilot Technical Review 03**](PILOT-TECHNICAL-REVIEW-03.md): 20 additional material claim groups for compromise, resilience, RTO/RPO, privacy harms from authorized processing, safety and human-impact constraints.
- [**Pilot Technical Review 04**](PILOT-TECHNICAL-REVIEW-04.md): 18 material claim groups covering evidentiary inference, recovery objectives and compliance versus security effectiveness, with source checks, example recomputation and documented corrections.
- [**Pilot Technical Review 05**](PILOT-TECHNICAL-REVIEW-05.md): 10 material claim groups for SF-04-08 (side/covert channels, information leakage), including source terminology, SC-31 bandwidth scope and verified information-theory arithmetic.
- [**Pilot Technical Review 06**](PILOT-TECHNICAL-REVIEW-06.md): 19 claim groups for randomness/nonces and key lifecycle/failures, including checked standards versions, entropy/collision/counter arithmetic, and key-hierarchy corrections.
- [**Pilot Technical Review 07**](PILOT-TECHNICAL-REVIEW-07.md): 30 article-specific claim groups across five Protected Interests, Assets & Harm manuscripts, with inspected NIST/FIPS source figures, Boolean validation, harm-evidence corrections and a worked Pareto comparison.
- [**Pilot Technical Review 08**](PILOT-TECHNICAL-REVIEW-08.md): 32 material claim groups across four adversarial-behavior manuscripts; NIST source-event boundaries, ATT&CK procedures, Diamond capability semantics, and formal opportunity/path checks.
- [**Coverage & Gaps Review 03**](COVERAGE-AND-GAPS-REVIEW-03.md): Reconciles the fourteen Reviewed pilots against 96 working subject candidates, identifies eight next subject/depth/overlap priorities, and separates knowledge gaps from unpiloted headings.
- [**Source Crosswalk v0.3**](ESTABLISHED-MODEL-CROSSWALK.md): 30 evidence groups, including NIST Privacy Framework, ISO/IEC safety principles, recovery-objective guidance, current incident-response methods and earlier cryptographic/formal policy models.

**Governance separation:** The Security Foundations division and Fundamentals-style directory pattern are adopted; the twelve current area names and 96 candidate subject memberships remain provisional. **All 29 authored working articles are Reviewed (model-assisted) / Core claims checked**, including the SF-03-02/03/05/06 batch under [Technical Review 08](PILOT-TECHNICAL-REVIEW-08.md). None is fully Source-Verified, independently expert-accepted, Published or permanently canonical-approved.

## The governing distinction

[Fundamentals](../fundamentals/README.md) explains **how technical systems work** without making security their organizing principle. **Security Foundations** explains protection objectives, threats, vulnerabilities, risk, trust, safeguards, evidence and assurance. [Operational Foundations](../operational-foundations/README.md) owns shared **methods for performing security work**. The [seven specialized domains](../../README.md#knowledge-domains) own their functions and implementation details.

For example, the general meaning of *an event* belongs in Fundamentals. The security relevance of an event and the evidentiary limits of classifying it are candidate concerns here. Incident triage is an operational activity, while collecting events with a named sensor belongs to the relevant technical domain.

## Model-grounded interpretation

Security Foundations should not invent new laws of security where tested models already exist. The [Established Model Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) uses the CIA Triad, STRIDE, Diamond Model, Unified Kill Chain, MITRE ATT&CK, Pyramid of Pain, CWE/CAPEC/CVSS, NIST risk guidance, Zero Trust, D3FEND, systems security engineering and NIST CSF as **complementary views**. They do not form a single interchangeable hierarchy, and some are frameworks, taxonomies or heuristics rather than formal models.

The 12 areas below are **working navigation hypotheses**, not a forced reflection of any one of those models. Their names, number and 96-subject working inventory remain open to revision based on model coverage, conceptual overlap and source evidence.

## Working knowledge areas

| Area | Working knowledge area | Candidate subjects | Reviewed substantive articles | Draft | Not authored |
| --- | --- | ---: | ---: | ---: | ---: |
| 01 | [Security Meaning & Objectives](security-meaning-objectives/README.md) | 8 | 2 | 0 | 6 |
| 02 | [Protected Interests, Assets & Harm](protected-interests-assets-harm/README.md) | 6 | 5 | 0 | 1 |
| 03 | [Threats, Hazards & Adversarial Behavior](threats-hazards-adversarial-behavior/README.md) | 7 | 5 | 0 | 2 |
| 04 | [Weaknesses, Vulnerabilities & Exposure](weaknesses-vulnerabilities-exposure/README.md) | 8 | 2 | 0 | 6 |
| 05 | [Security Risk & Uncertainty](security-risk-uncertainty/README.md) | 8 | 1 | 0 | 7 |
| 06 | [Trust, Identity & Authority Principles](trust-identity-authority-principles/README.md) | 9 | 1 | 0 | 8 |
| 07 | [Security Controls & Defense Mechanisms](security-controls-defense-mechanisms/README.md) | 8 | 1 | 0 | 7 |
| 08 | [Secure Design & Architecture](secure-design-architecture/README.md) | 9 | 1 | 0 | 8 |
| 09 | [Cryptography & Information Protection](cryptography-information-protection/README.md) | 9 | 3 | 0 | 6 |
| 10 | [Security Observation & Evidence](security-observation-evidence/README.md) | 8 | 2 | 0 | 6 |
| 11 | [Security Failure & Resilience](security-failure-resilience/README.md) | 8 | 3 | 0 | 5 |
| 12 | [Security Assurance, Governance & Accountability](security-assurance-governance-accountability/README.md) | 8 | 3 | 0 | 5 |
| **Total** | **12 provisional areas** | **96** | **29** | **0** | **67** |

**These directories follow the Fundamentals baseline:** each area contains its own `README.md` and the substantive articles currently assigned to it. Some areas have multiple articles; others currently contain only an inventory README. **Do not invent article files to equalize counts.**

**The shared directory pattern is explicitly adopted, but the individual proposed area identities and 96 candidate subjects are not automatically ratified merely by appearing here.** The area count, subject names, ownership decisions and precise definition remain subject to architectural review. This is a knowledge reference, not a course or assessment platform: no Knowledge Checks or Practical Assessments.

[Foundations](../README.md) · [Security Knowledge](../../README.md) · [Knowledge relationship conventions](../../RELATIONSHIPS.md)
