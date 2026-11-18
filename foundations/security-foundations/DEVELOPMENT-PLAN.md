# Security Foundations: Architecture & Development Plan

**Working edition:** v0.1 · November 17, 2026  
**Status:** Proposed plan; **no approval of internal taxonomy or article publication is asserted**  
**Scope:** Security Knowledge → Foundations → Security Foundations  
**Proposed inputs:** [Architecture](ARCHITECTURE.md) · [94-heading Candidate Inventory](SUBJECT-INVENTORY-PROPOSAL.md) · [25-case Ownership Boundaries](OWNERSHIP-BOUNDARIES.md)

## 1. Mission and deliverable

Develop an authoritative, technically detailed, vendor-neutral, interconnected **security knowledge reference** whose concepts can be understood and applied across the seven specialized domains. This is not an introductory certification syllabus or an operations handbook.

A complete article must explain not merely *what a term means*, but **why the property matters, how relevant conditions or mechanisms work, where the claim fails, what can be observed, and what sources justify it**. The repository remains a reference with no Knowledge Checks, Practical Assessments, quizzes, graded labs or fixed reading order.

## 2. Existing baseline and proposed scope

| Measure | Current disposition |
| --- | --- |
| Approved divisions | Fundamentals; Security Foundations; Operational Foundations |
| Security Foundations division | Approved, existing index only before this proposal |
| Internal Security Foundations taxonomy | **Not approved** |
| Working knowledge areas | 12 **proposed** |
| Working subject headings | 94 **proposed** |
| Canonical Security Foundations subject articles created by this architecture pass | **0** |
| Substantive technical review of the proposed future subject articles | Not started |
| Specialized knowledge domains | Seven existing approved domain entries |
| Formal relationship predicate vocabulary / graph engine | Neither approved nor implemented |

The subject inventory is a **candidate discovery and coverage instrument**, not an immutable quota or authorization to create 94 article directories. The area IDs are planning references only.

## 3. Engineering workstreams

### Workstream A: Scope approval and canonical ownership

- Review all 12 candidate areas and 94 proposed subjects for coverage, overlap, clarity, and correct granularity; merge, split, rename or remove as justified.
- Resolve the [25 proposed ownership boundaries](OWNERSHIP-BOUNDARIES.md) with special care around identity, cryptography, risk assessment, security observations, privacy and safety.
- Cross-check against the **109 approved Fundamentals headings**. Do not reopen the approved Fundamentals structure by stealth, and do not treat its internally Reviewed articles as fully published.
- Review the current [Operational Foundations](../operational-foundations/README.md) remit without inventing or approving its internal subject taxonomy.
- Map relationships to the seven specialized domains using canonical function links, not duplicate technical definitions.
- **Exit condition:** An explicitly approved Security Foundations governing definition, area list, subject inventory and recorded unresolved exceptions.

### Workstream B: Reference and source mapping

For each future approved subject, establish:

1. Canonical definition and adjacent non-equivalent terms.
2. Claims requiring proof, derivation or cited primary-source authority.
3. Sources appropriate to the claim: original specifications, authoritative scientific/technical publications, or primary project documentation.
4. Limits of applicability: threat model, assumptions, architecture, jurisdiction, time, uncertainty, exceptions and contradictory guidance.
5. A source-to-claim ledger that distinguishes verified evidence from editorial interpretation.

Example source families: NIST SP 800-160 (systems security engineering and resilience), SP 800-30 (risk), SP 800-53 (control catalog, with active updates), SP 800-207 (zero trust), SP 800-63-4 (digital identity), NIST CSF 2.0 (organizational outcome framing), MITRE CWE (weakness), MITRE ATT&CK (adversary behavior). These references are **not** interchangeable, exhaustive, or necessarily generalizable outside their original scopes.

**Exit condition:** A traceable source plan and explicit evidence limitations for each authorized article batch.

### Workstream C: Controlled article pilots

After taxonomy approval, start with a deliberately varied sample to calibrate security-specific depth and boundary integrity. **Illustrative candidates, not a commitment to author before approval:**

| Pilot candidate | Why test it early |
| --- | --- |
| Security and insecurity | Tests whether security is defined conditionally, without ungrounded absolutes |
| Threat sources and threat events | Tests adversarial and non-adversarial applicability |
| Weaknesses and root causes | Tests weakness/vulnerability/exposure separation |
| Risk, scenarios, and time horizon | Tests distinctions among harm, likelihood and risk |
| Trust and trust assumptions | Tests the security/Identity Knowledge boundary |
| Controls, safeguards, and security functions | Tests mechanism versus protection outcome |
| Observable, observed, and recorded | Tests security evidence versus reality and telemetry |
| Security claims and assurance arguments | Tests what counts as credible support for security claims |

The remaining security subjects should follow by cohesive batches and cross-references, not a rigid educational prerequisite chain.

**Exit condition:** Pilot editorial contract calibrated, source limitations recorded, definition overlaps resolved, and no accepted article labeled Published without its acceptance evidence.

### Workstream D: Article development and cross-reference

Suggested wave grouping, changeable after the architecture review:

| Proposed wave | Areas addressed | Focus |
| --- | --- | --- |
| A: Meaning & adverse conditions | 01–05 | Security properties, protected interests, threat, weakness and risk |
| B: Protective principles & design | 06–09 | Trust, controls, architecture and information protection |
| C: Interpretation & justified confidence | 10–12 | Security evidence, resilience, assurance and governance |

Each article should connect to the necessary Fundamentals concepts, sibling Security Foundations concepts, Operational Foundations practices **when those canonical practice articles exist**, and one or more relevant specialized domain functions. Never fabricate a missing canonical article; use a division/function index or explicitly mark a future target.

**Exit condition:** Approved subjects receive substantive vendor-neutral content and correctly routed references.

### Workstream E: Review, verification and acceptance

- Validate each material technical claim at the **source-passage** level, not merely via presence of an external link.
- Independently recompute quantitative examples and inspect assumptions, boundary conditions and failure cases.
- Verify internal Markdown paths, fragment anchors and relevant external source addresses; distinguish availability from semantic support.
- Reconcile contradictions and duplicates across Security Foundations, Fundamentals, Operational Foundations and specialized domain functions.
- Evaluate explanatory depth, clarity, counterexamples, cross-domain relevance and limits of security judgments.
- Preserve separate states for **Draft**, **Reviewed (model-assisted)**, **Verified with documented evidence**, and **Published after explicit acceptance**; do not claim independent peer review unless actually completed.
- Obtain qualified independent human expert review for consequential areas and adjudicate findings before final publication acceptance.

**Exit condition:** Evidence exists for all defined acceptance gates and every unresolved exception is visible.

## 4. Proposed completion gates

These gates are **proposed for Security Foundations**, modeled on the repository's separation of authoring, verification and publication. They are not yet adopted as binding governance.

| Gate | Evidence needed |
| --- | --- |
| G1 Architecture | Definition, area inventory and ownership boundaries explicitly ratified |
| G2 Coverage | Shared security concepts necessary across all seven domains have a home |
| G3 Consistency | No material contradiction or unnecessary duplicated canonical definition |
| G4 Explanation | Every approved subject has substantive concepts, mechanisms, distinctions and meaningful examples |
| G5 Traceability | Technical claims, uncertainty, sources and cross-domain dependencies are reviewable |
| G6 Navigation | Subject and relationship links resolve; no false claims of existing unpublished pages |
| G7 Acceptance | Scoped technical validation, review limitations and qualified human acceptance recorded |

A successful Markdown build or model-assisted audit can satisfy portions of G5/G6; it cannot by itself establish G7.

## 5. Working article contract

A future article should contain the following **substantive content**, with flexible headings:

- Security definition, scope and exclusions.
- Protection interests, operating assumptions and relevant failure or attack conditions.
- Mechanisms, causal pathways, or technical constraints, without fake universal formulas.
- Related but distinct concepts with non-examples.
- One or more clearly labeled, reproducible or logically testable examples as appropriate.
- Explicit concepts/contexts/implementations and canonical cross-links.
- Authority-based source references, limitations and contested claims.

Do not silently reduce risk to "likelihood × impact", anomaly to malicious intent, detection to proof of compromise, zero trust to "no trust", cryptography to perfect security, or compliance to assurance.

## 6. Source governance

- Prefer official and primary sources for normative technical claims.
- Distinguish **descriptive scientific evidence**, **normative specification**, **threat knowledge bases**, **measurement**, **editorial model**, and **illustrative example**.
- State when a source defines terms for a particular setting (e.g., United States federal systems), rather than importing the language as a universal law.
- Avoid stale citations to draft/superseded standards where current final sources exist. Capture the publication version/date when it materially changes the conclusion.
- Do not infer that a source's concepts imply a repository taxonomy approval.

## 7. Proposed progress tracking

Record each authorized subject's administrative planning ID, area, canonical path, development state, source-review state, cross-domain owners, review evidence, known unknowns and exceptions. Keep **architecture-approval status** separate from **article technical-review status** and **publication acceptance**. A file existing in GitHub does not prove any of those stronger states.

Do not instantiate a formal ontology, graph engine, vendor-specific learning pathway, certifications or graded assessments merely to track this work.

## 8. Immediate next decision package

1. Review the proposed [governing definition and twelve categories](ARCHITECTURE.md).
2. Adjudicate the [94 candidate headings](SUBJECT-INVENTORY-PROPOSAL.md), adjusting grain and placement to avoid duplication.
3. Resolve [25 boundary cases](OWNERSHIP-BOUNDARIES.md) or mark them explicitly deferred.
4. Adopt a final architecture baseline, **then** create the canonical subject structure and begin source-led pilot articles.

**Current disposition:** The architecture package is **implemented as a working proposal**. No new internal Security Foundations area or subject has been approved or published by this work.

[Security Foundations](README.md) · [Foundations](../README.md) · [Security Knowledge](../../README.md)
