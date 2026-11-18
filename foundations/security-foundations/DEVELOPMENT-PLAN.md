# Security Foundations: Architecture & Development Plan

**Working edition:** v0.5 · November 18, 2026  
**Status:** Proposed plan; **no approval of internal taxonomy or article publication is asserted**  
**Scope:** Security Knowledge → Foundations → Security Foundations  
**Proposed inputs:** [Architecture](ARCHITECTURE.md) · [96-heading Flexible Working Inventory](SUBJECT-INVENTORY-PROPOSAL.md) · [30-case Ownership Boundaries](OWNERSHIP-BOUNDARIES.md) · [26-group Established Model Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) · [Architecture Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md)

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
| Working subject headings | **96 proposed**, revised from 94 by four additions and two consolidations; still flexible |
| Final approved canonical Security Foundations articles | **0**; ten working pilot manuscripts now exist, none in a ratified canonical path |
| Substantive technical review of proposed future subject articles | **10 pilots Reviewed (model-assisted)** with [40 claims](PILOT-TECHNICAL-REVIEW-01.md) plus [10 claims](PILOT-TECHNICAL-REVIEW-02.md) checked; complete source-level and independent reviews pending |
| Specialized knowledge domains | Seven existing approved domain entries |
| Formal relationship predicate vocabulary / graph engine | Neither approved nor implemented |

The subject inventory is a **candidate discovery and coverage instrument**, not an immutable quota or authorization to create 96 article directories. The area IDs are planning references only.

## 2A. Progress and status separation (working)

| Workstream | Current status |
| --- | --- |
| Division | Approved |
| Internal taxonomy | 12 proposed areas / **96 active proposed subjects**, both flexible and unratified |
| Source map | **26 established source groups** identified with version and non-equivalence cautions |
| Ownership | **30 working overlap cases** documented; not all individually approved |
| Article development | **Ten substantive Reviewed (model-assisted) pilots** under [pilots/](pilots/README.md); these are not ratified permanent canonical placements |
| Review / publication | [50-family cumulative pilot audits](PILOT-TECHNICAL-REVIEW-01.md) (40 in Review 01, plus [10 in Review 02](PILOT-TECHNICAL-REVIEW-02.md)) completed; complete source-passage verification, qualified human review, and publication acceptance remain open |

**Historical denominators:** Earlier 12/94 and 20-source/25-boundary records remain traceable. **Ten currently Reviewed pilots out of 96 working candidate subjects is a manuscript coverage indicator, not a percentage of architectural approval.** Pilot completion does not change the candidate count without a separately recorded conceptual decision.

## 3. Engineering workstreams

### Workstream A: Scope approval, established-model reconciliation and canonical ownership

- **Begin with the [Established Models Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md):** Test each area and material concept against the model's actual scope, unit of analysis, assumptions, sources, and limits. Do not copy a framework's categories into the subject tree solely because it is well known.
- Reconcile the twelve provisional areas and 96 current candidates against established sources and real prose. **Both counts may expand or contract**; merge, split, rename, move, retire, or add subjects as evidence justifies. Preserve administrative IDs through revisions until a different baseline is explicitly approved.
- Examine the [30 working ownership boundaries](OWNERSHIP-BOUNDARIES.md) with special care around identity, cryptography, risk assessment, security observations, privacy and safety.
- Cross-check against the **120 currently tracked Fundamentals articles**, recognizing that this count can evolve. Do not reopen the approved Fundamentals structure by stealth, and do not treat its internally Reviewed articles as fully published.
- Review the current [Operational Foundations](../operational-foundations/README.md) remit without inventing or approving its internal subject taxonomy.
- Map relationships to the seven specialized domains using canonical function links, not duplicate technical definitions.
- **Exit condition:** An explicitly approved Security Foundations governing definition, model-grounded area list, subject inventory and recorded unresolved exceptions. The working 12/96 counts alone do not establish completeness.

### Workstream B: Reference and source mapping

For each future approved subject, establish:

1. The relevant **established models and source type** (formal model, explanatory model, heuristic, taxonomy, scoring system, control catalog or framework), or a documented reason a concept cannot be reduced to any one source model.

2. Canonical definition and adjacent non-equivalent terms.
3. Claims requiring proof, derivation or cited primary-source authority.
4. Sources appropriate to the claim: original specifications, authoritative scientific/technical publications, or primary project documentation.
5. Limits of applicability: threat model, assumptions, architecture, jurisdiction, time, uncertainty, exceptions and contradictory guidance.
6. A source-to-claim ledger that distinguishes verified evidence from editorial interpretation.

Example source families: NIST SP 800-160 (systems security engineering and resilience), SP 800-30 (risk), SP 800-53 (control catalog, with active updates), SP 800-207 (zero trust), SP 800-63-4 (digital identity), NIST CSF 2.0 (organizational outcome framing), MITRE CWE (weakness), MITRE ATT&CK (adversary behavior). These references are **not** interchangeable, exhaustive, or necessarily generalizable outside their original scopes.

**Exit condition:** A traceable source plan and explicit evidence limitations for each authorized article batch.

### Workstream C: Controlled article pilots

**Begin bounded article pilots before internal taxonomy ratification**, under [pilots/](pilots/README.md), to test terminology and conceptual ownership without creating an unapproved canonical area tree. Only later approval may determine final canonical paths. Source evidence and technical-review status are independent of that governance decision.

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

- Validate each material technical claim at the **source-passage** level, not merely via presence of an external link; distinguish a source's formal definition from a heuristic or an illustrative model.
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
| G1 Architecture | Definition, established-model coverage rationale, area inventory and ownership boundaries explicitly ratified |
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
2. Review the [96 active working candidates](SUBJECT-INVENTORY-PROPOSAL.md), allowing further justified expansion or contraction.
3. Evaluate the [30 working boundary cases](OWNERSHIP-BOUNDARIES.md) and record unresolved collisions.
4. Preserve the [ten authored and scoped-reviewed pilots](pilots/README.md) with [Review 01](PILOT-TECHNICAL-REVIEW-01.md) and [Review 02](PILOT-TECHNICAL-REVIEW-02.md) as separate source-scope evidence. Continue with resilience, privacy/safety and other demonstrated coverage gaps before finalizing canonical paths.

**Current disposition:** [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md) implements a revised working architecture, not a ratified 12-area/96-subject taxonomy. Pilot texts remain pre-publication content and do not imply automatic editorial or expert acceptance.

[Security Foundations](README.md) · [Foundations](../README.md) · [Security Knowledge](../../README.md)
