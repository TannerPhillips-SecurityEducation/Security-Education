# AGENTS.md | Security Foundations Editorial & Engineering Contract

**Applies to:** `foundations/security-foundations/` and its descendants.  
**Purpose:** Give AI agents and human contributors a durable operating contract for discovering, architecting, authoring, reviewing, and maintaining cross-domain Security Foundations knowledge.  
**Authority:** Working repository instructions for executing authorized editorial work. **Not** approval of the proposed internal Security Foundations taxonomy, any manuscript's permanent canonical location, an external standard, or final publication. Explicit user direction and higher-priority instructions take precedence.  
**Status of this file:** An operational guide derived from the observed Fundamentals workflow and explicitly established Security Knowledge constraints. Review and revise as the project develops.  
**Sibling contracts:** [Fundamentals AGENTS.md](../fundamentals/AGENTS.md) and [Operational Foundations AGENTS.md](../operational-foundations/AGENTS.md). All three share thirteen operating sections while preserving each division's actual architecture-approval state.

**Inherited root SOP:** [Repository AGENTS.md](../../AGENTS.md) governs evidence, variable depth/granularity, editorial autonomy, non-Socratic collaboration, approvals, provenance and validation across the repository. This file adds division-specific requirements; it does not override higher-priority instructions or turn proposed knowledge structures into approved ones.

**Foundations-level inheritance:** [Foundations AGENTS.md](../AGENTS.md) governs shared cross-division ownership, flexible inventories, evidence and review boundaries; this file supplies the domain-specific rules.

## 1. Mission and non-negotiable boundaries

Security Foundations explains **what security and insecurity mean, what can go wrong, how security properties and controls operate, and what evidence justifies protection claims** across technical systems and the seven specialized knowledge domains.

Preserve four different knowledge responsibilities:

| Home | Owns | Does **not** primarily own |
| --- | --- | --- |
| [Fundamentals](../fundamentals/README.md) | Domain-agnostic mathematics, logic, models, information, systems, computation, physical mechanisms and scientific reasoning | Security-specific properties or operational response methods |
| **Security Foundations** | Shared security-specific objectives, conditions, threat/vulnerability/risk models, trust, protection principles, evidence and assurance | Vendor implementations, one domain's procedures or full operational workflows |
| [Operational Foundations](../operational-foundations/README.md) | Cross-domain **methods and activities of security work**, including assessment, threat hunting, investigation, detection engineering and response | The only definition of general security concepts |
| [Specialized domains](../../README.md#knowledge-domains) | Network, Endpoint, Application, Cloud, Industrial, IoT and Identity **functions and implementations** | Duplicate general foundational definitions |

The approved repository principle is **hierarchy for navigation, knowledge graph through explicit links**. A folder is an editorial navigation choice, not automatically an ontological `is-a` assertion. Read [repository relationship rules](../../RELATIONSHIPS.md) before creating a new ownership structure.

**Exclude** Knowledge Checks, Practical Assessments, quizzes, graded labs, certification tracks, fixed classroom schedules and artificial course modules. Worked and falsifiable examples are welcome; they are not assessments. Do not impose vendors, operating systems, cloud providers, security platforms or a single product as the organizing principle.

## 2. Approval boundary: what is actually settled

**Explicitly established repository facts:**

- The **Security Foundations division** is approved alongside Fundamentals and Operational Foundations.
- The seven specialized domains exist and use **Domain → Function → Implementation** as primary navigation.
- The [Security Foundations architecture](ARCHITECTURE.md), [subject inventory](SUBJECT-INVENTORY-PROPOSAL.md), [ownership boundaries](OWNERSHIP-BOUNDARIES.md) and [development plan](DEVELOPMENT-PLAN.md) are **working proposals**, not a ratified internal taxonomy.
- The current working inventory has **12 proposed areas and 96 active subject candidates**, and **both numbers can increase or decrease**. These are descriptive snapshots, **not quotas or completion targets**.
- Earlier candidate identifiers and decisions must remain traceable. [Architecture Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md) records four additions and two consolidations from an earlier 94-candidate snapshot.
- [Pilots](pilots/README.md) are substantive working manuscripts under an unratified internal structure; their technical review does **not** approve final canonical placement.
- The existing model/source map and boundary ledger are evidence catalogs, not standardized universal taxonomies or permanently fixed-size lists.

**Do not convert:** proposed → approved, mentioned → covered, authored → reviewed, reviewed → verified, verified → published, or a model's original labels → repository governing ontology **without corresponding evidence and authorization**.

An instruction or suggestion written by an agent is **not** a user decision. Record assistant recommendations as recommendations and preserve the distinction from explicit user approvals.

## 3. Architecture learned from the Fundamentals corpus

The **observed architecture** of [Fundamentals](../fundamentals/README.md) is a reusable *system of responsibilities*, not a requirement to copy its twelve directories or subject count.

| Fundamentals layer and real example | Function | Transfer to Security Foundations |
| --- | --- | --- |
| [Governing architecture](../fundamentals/ARCHITECTURE.md) | Definition, scope, non-goals, ownership and placement rules | [Working Security Foundations architecture](ARCHITECTURE.md), with explicit approval status |
| [Division index](../fundamentals/README.md) | Navigable entry point, accurate inventory, development and review evidence | [Security Foundations index](README.md) |
| Area `README.md` indexes, e.g. [Mathematics & Logic](../fundamentals/mathematics-logic/README.md) | Area scope, active subject list, actual article links, current status | **Only after the proposed Security Foundations areas are ratified**; do not create fake canonical area trees |
| Canonical subject articles, e.g. [Search and Information Retrieval](../fundamentals/information-data/search-and-information-retrieval.md) | Definition, structures, mechanisms, source-grounded examples, boundaries, limitations, related concepts | [Working substantive pilots](pilots/README.md) before canonical ratification |
| [Canonical ownership register](../fundamentals/CANONICAL-OWNERSHIP-REGISTER.md) | One general meaning owner, bounded related concepts and relationship links | [Ownership boundaries](OWNERSHIP-BOUNDARIES.md); add a formal subject-owner register when needed, not by inventing relationships |
| [Overlap and gap decisions](../fundamentals/CONCEPT-BOUNDARY-DECISIONS.md), [coverage triage](../fundamentals/COVERAGE-AND-SOURCE-TRIAGE-02.md) | Non-equivalences, source-backed additions/splits/merges, historical identifiers | [Security architecture adjudication](ARCHITECTURE-ADJUDICATION-02.md) and [coverage review](COVERAGE-AND-GAPS-REVIEW-03.md) |
| [Development/verification register](../fundamentals/DEVELOPMENT-VERIFICATION-REGISTER.md) | Path, current state, separate source evidence, review batch and known open work | [Pilot index](pilots/README.md) now; expand to a dynamic development register as article count and ratification warrant |
| [Technical review waves](../fundamentals/WAVE-H-TECHNICAL-REVIEW-01.md) | Claim families, source scope, recomputation, corrections, review limitations | [Security pilot technical reviews](PILOT-TECHNICAL-REVIEW-01.md), [02](PILOT-TECHNICAL-REVIEW-02.md), [03](PILOT-TECHNICAL-REVIEW-03.md) |
| [Publication-readiness audit](../fundamentals/PUBLICATION-READINESS-AUDIT-01.md) | Inventory and link integrity separated from complete verification/publication | Explicit Security Foundations publication gates; an automated pass is **not** publication acceptance |
| [Fundamentals inventory validator](../fundamentals/tools/check_inventory.py) and [Fundamentals CI](../../.github/workflows/fundamentals-internal-links.yml) | Link, heading fragment, inventory, model-mention and source-coverage diagnostics | [Security Foundations structure validator](tools/check_foundations_structure.py) and [Security CI](../../.github/workflows/security-foundations-integrity.yml) |

**Important finding from direct inspection:** Fundamentals contains **historical narratives and some stale denominators/status sentences** in area READMEs and earlier plans, even when current inventories, article paths and latest audit records are correct. Never take a historical heading, an older “N/N reviewed” claim, or a prior report's denominator as the current truth without reconciliation.

The Fundamentals architecture shows **approved navigation disciplines**, subject articles, review ledgers, and reference links. **Security Foundations is not at the same architecture-approval stage.** Preserve that asymmetry.

## 4. Editorial operating loop: Observe → Derive → Infer → Act

Use this as a **working method**, not a newly ratified security ontology or mandated article heading system.

1. **Observe:** Inspect the actual repository tree, active governing files, subject inventory, article bodies, source originals, previous decisions and the latest CI evidence. Identify what is **observed versus merely reported**.
2. **Derive:** Distinguish concepts by their unit of analysis, structure, principles, mechanism, boundaries, source type, applicability, assumptions and canonical owner. Compare related Fundamentals and Security/Operational concepts.
3. **Infer:** Identify missing explanatory depth, true coverage gaps, duplication, uncertain interpretation, contradictory definitions, outdated standards and warranted changes. Mark hypotheses, unresolved questions and possible alternatives; **do not convert guesses into observations or user approvals**.
4. **Act:** Choose the smallest coherent high-value change: deepen an article, add a pilot, reconcile a source, correct a boundary, propose or document a split/merge, fix a link or implement a validated architecture decision. Record its effects and check the result.

**Exercise initiative over both what to investigate and how to execute.** Do not require repetitive approval questions for ordinary reversible drafting, analysis, auditing, link repair or technically justified documentation corrections within the existing authorized project. **Do not unilaterally represent major architecture decisions as approved**, fabricate external review, publish as final, delete/move approved content, or make irreversible changes beyond actual authorization. Ask a straightforward clarification only when a material missing fact cannot be resolved from the project.

## 5. Conceptual modeling and scientific rigor

A Security Foundations article should explain a concept's **meaning, structure, governing constraints, mechanisms, relationships and limits** in fluent, substantive prose. Avoid dictionary-only or outline-only articles.

Always distinguish, when relevant:

- **Entity / condition / occurrence / event / attempted action / resulting state**.
- **What could be observable / what was observed / what was recorded / what was inferred / what was asserted**.
- **Claim / assumption / evidence / confidence / uncertainty / unknown**.
- **Weakness / vulnerability / exposure / exploitability / attempted exploitation / security violation / compromise**.
- **Threat source / threat event / adversary objective / observed behavior / intent attribution**.
- **Security property / requirement / policy decision / implemented control / demonstrated control outcome / assurance**.
- **Likelihood / severity / harm / consequence / risk scenario / affected stakeholder / time horizon**.
- **Authentication / authorization / information-flow policy / enforcement / observed effect**.
- **Confidentiality / integrity / availability / authenticity / accountability / privacy / safety / reliability / resilience**.

**Unknown is an epistemic result, not evidence of benignness, maliciousness, security or insecurity.** An anomaly does not prove intent; an alert does not prove compromise; no alerts does not prove absence of attacks. A CVSS severity score is not automatically organizational risk; a listed NIST control or D3FEND mapping does not establish protection effectiveness.

Distinguish **syntax, semantics and pragmatics** where protocol, policy, data or query meaning benefits. Distinguish **content, context and inferred intent**, without equating these three dimensions with the previous three or forcing them into an external model.

Use established conceptual models such as CIA, STRIDE, Diamond Model, Unified Kill Chain, ATT&CK, CWE, CAPEC, CVSS, Zero Trust, D3FEND, and formal information-flow/access models **only for their own documented purposes**. A named model is not automatically a universal phase sequence, causal proof, formal theorem or navigation category.

## 6. Model- and source-first research contract

Before making a consequential technical assertion or creating a model-grounded article:

1. **Find the strongest applicable source**, preferably an original paper, normative specification, official standards publisher, or authoritative maintainer documentation.
2. **Identify its type:** formal model, technical standard, explanatory framework, empirical study, taxonomy, heuristic, scoring rubric, control catalog, operational guide or editorial analogy.
3. **Record the source version/date, intended unit, domain and limits.** Prefer current final publications for current normative claims. Check whether a draft, superseded document, archival paper or later amendment is being used.
4. **Separate source statements from editorial derivations and hypothetical illustrations.** A source can justify the definition of a model without establishing all examples, recommendations or real-world effects.
5. **For each important claim, connect the claim to a sufficiently precise source location.** A bibliography or URL count alone does not establish semantic support. Note unavailable full-text or licensed standards honestly.
6. **Independently test worked arithmetic, logical examples, non-examples, invariants and counterexamples.** State the assumptions under which results follow.
7. **When sources disagree**, compare publication date, scope, terminology and model assumptions; preserve contested alternatives or flag unknowns rather than manufacture certainty.

Start with the [established model crosswalk](ESTABLISHED-MODEL-CROSSWALK.md), but **do not assume its source list is exhaustive or immune to becoming stale**. Examples of previously important currency corrections are RFC 9846 superseding RFC 8446 as a TLS 1.3 source, and ISO/IEC 15408-1:2026 superseding the 2022 ISO Part 1 edition. Always recheck versions when material.

## 7. Authoring contract for each Security Foundations pilot

**Before drafting:** Confirm the candidate's active ID and scope in [the working inventory](SUBJECT-INVENTORY-PROPOSAL.md); inspect overlapping pilots and [ownership boundaries](OWNERSHIP-BOUNDARIES.md); check the related Fundamentals reference; decide the intended canonical concept and what this pilot explicitly excludes.

**Use a substantive, adaptable article structure:**

- Title and frontmatter: candidate ID, working/proposed area, **pilot** status, development state, source-review state, scope authority.
- A precise opening definition and the **problem or protected interest** it addresses.
- Anatomy, participating entities/relations, assumptions and relevant properties.
- Mechanisms, policy/causal constraints and conditions for behavior.
- Related but non-equivalent concepts, alternative models and failure conditions.
- At least one **worked, technically inspectable example or counterexample** where the topic supports it; no invented measurements presented as real evidence.
- Source-grounded applicability, uncertainties and explicit limitations.
- Relative links to actual Fundamentals, Security Foundations pilots, Operational Foundations indexes or real specialized-domain pages **only when meaningful**.

**Editorial style:** Write a living technical textbook, not a glossary dump, marketing copy, certification outline or conversational agent report. Be precise, readable and explanatory; use small tables/diagrams where they clarify rather than decorate. Define abbreviations on first meaningful use. Prefer grounded distinctions and defensible examples over ornamental complexity.

**No false content:** Do not invent standards text, URLs, versions, file paths, observations, test results, authority names, citations or completed source checks. Avoid “always,” “never,” “proven secure,” and similar absolute guarantees unless genuinely supported by a formal scope and evidence.

**Article placement now:** `pilots/<lowercase-kebab-subject>.md`. **Do not** create the proposed `SF-01/` or similarly named canonical area trees merely to mirror Fundamentals. After internal architecture ratification, migrate approved canonical owners with real redirects/updated links and preserved history as necessary.

## 8. Knowledge gap, overlap and inventory change policy

The candidate area count and subject count are **living variables**, not quotas. No agent should optimize for reaching 96, filling twelve categories symmetrically, one article per named model, or any fixed historical count.

When reviewing coverage, classify each case as:

| Disposition | When appropriate |
| --- | --- |
| **Deepen** | A subject already owns the concept but lacks mechanism, example, limit or source support |
| **Add** | A distinct cross-domain security-specific concept has no adequate canonical owner |
| **Split** | One proposed subject contains independently coherent concepts needing separate owners |
| **Merge/consolidate** | Two or more subjects substantially duplicate canonical meaning |
| **Relocate** | The canonical meaning belongs in Fundamentals, Operational Foundations or a specialized domain |
| **Cross-link** | The concept already exists in the correct owner; only navigation/dependency context is missing |
| **Defer/unknown** | Source evidence or conceptual boundary is insufficient |

For each significant proposed change, document **prior/new identifiers, reason, source-model basis, affected articles/indexes, old-to-new owner mappings, unresolved alternatives, approval state and review consequences**. Preserve retired IDs in history; do not silently reuse them. A merged replacement must not inherit a blanket technical-review claim from its components.

Distinguish a **coverage deficit** from a **missing article**, a **missing named-model mention**, a **missing link**, or a **missing claim-to-passage reference**. All require different remedies.

**Cross-domain links are incremental.** Add them when relevant domain content exists; do not institute a link-count target or pretend an uncreated destination exists. Uncertain cross-domain applicability is not proof that a topic deserves its own Security Foundations subject.

## 9. File responsibilities and repository navigation

**Current Security Foundations working layout:**

```text
foundations/security-foundations/
├── AGENTS.md                         # This subtree-wide editorial/engineering contract
├── README.md                         # Division index; current working and review status
├── ARCHITECTURE.md                   # Proposed governing concept and placement rules
├── SUBJECT-INVENTORY-PROPOSAL.md     # Active, revisionable candidate area/subject map
├── ARCHITECTURE-ADJUDICATION-*.md    # Versioned add/split/merge/retire decisions
├── ESTABLISHED-MODEL-CROSSWALK.md    # Model types, primary sources, versions, limits
├── OWNERSHIP-BOUNDARIES.md           # Cross-division/within-security overlap cases
├── COVERAGE-AND-GAPS-REVIEW-*.md     # Diagnosed gaps and next depth work
├── DEVELOPMENT-PLAN.md              # Workstreams, state transitions, proposed gates
├── PILOT-TECHNICAL-REVIEW-*.md       # Bounded article-level claim audits
├── pilots/
│   ├── README.md                     # Actual pilot paths and current states
│   └── <descriptive-subject>.md      # Substantive manuscripts with candidate IDs
└── tools/                            # Link, inventory and structure checks
```

**File roles are distinct:** `README.md` is navigation and current status; `ARCHITECTURE.md` governs *proposed* scope; inventory lists active candidate coverage; adjudications preserve decisions and history; sources ground model claims; ownership ledgers describe concept homes; the development plan governs workflow; article pilots contain **knowledge**; technical reviews contain **what was checked**; tools test mechanical consistency.

**Do not** bury the only canonical explanation inside an audit file, mistake a review artifact for a substantive article, multiply competing root indexes, or treat article publication state as a directory naming convention.

If the working structure is ratified later, follow Fundamentals' pattern of **a division index + an area README + a substantive canonical article in its one proper home**, with ownership/development registers and versioned reviews maintained at division scope. Exact directories and counts require their own approval.

## 10. Development, evidence and publication states

Track at least these **separately**, in current article frontmatter and [the pilot register](pilots/README.md):

| Axis | Possible states | Minimum meaning |
| --- | --- | --- |
| **Architecture status** | Proposed / adjudicated working / explicitly approved | Whether a subject's *canonical home and governing taxonomy* are authorized |
| **Development state** | Inventoried / Draft / Reviewed (model-assisted) / Published | Whether an article exists, passed a bounded review, and gained final acceptance |
| **Source-review state** | Not reviewed / References listed / Core claims checked / Verified | Depth and evidence of actual claim-to-source examination |
| **Relationship review** | Proposed / checked / unresolved | Whether intended concept links and owner boundaries were actually evaluated |
| **Publication status** | Unpublished / accepted | Independent acceptance and required publication gates, not simply a merged commit |

**Promotion rules:**

- **Inventoried → Draft:** Substantive article written, no fabricated authoring result.
- **Draft → Reviewed:** Create a **separate scoped technical audit** naming the articles, claim families, primary source versions, worked checks, corrections, exceptions and limitations. Then update the article and pilot index to the same state.
- **References listed → Core claims checked:** Only after a real, documented second-pass claim-group/source review, not after merely adding bibliography links.
- **Core claims checked → Verified:** Requires documented, sufficiently complete claim-to-passage review under explicit acceptance criteria. Do not infer this from broad topical corroboration.
- **Reviewed/Verified → Published:** Requires independently established publication criteria, **approved architecture/canonical location**, meaningful source and relationship evidence and qualified human acceptance as applicable. **Agents may not self-certify publication.**

Prior wave and batch counts remain **historical**. Every newly authored, materially changed, split or merged article needs its **own** review evidence. No magic inheritance of “all N/N Reviewed.”

## 11. Technical review and CI are different gates

Every substantive batch should yield:

1. **A bounded review ledger:** candidate IDs, real article links, material claim groups, source versions, inspected passage/range where possible, worked arithmetic, counterexamples, corrections and outstanding unknowns.
2. **An article state update:** only after the review exists, with explicit evidence links and correct source-review level.
3. **A pilot/index reconciliation:** paths, names, IDs, statuses, source groups and count denominators all reflect the same current snapshot.
4. **Mechanical validation:** internal Markdown targets, heading fragments, candidate IDs, source/boundary register uniqueness and pilot development-state consistency.
5. **A concise completion report:** what changed, what passed, what is still unverified and which higher-level approvals remain open.

When a local checkout is available, run from repository root:

```bash
python3 foundations/security-foundations/tools/check_foundations_structure.py
python3 foundations/security-foundations/tools/check_internal_links.py
python3 foundations/security-foundations/tools/check_candidate_inventory.py
```

Relevant GitHub Actions workflow: [`security-foundations-integrity.yml`](../../.github/workflows/security-foundations-integrity.yml).

These scripts discover the current inventory instead of enforcing a permanent subject-count quota. **Green checks establish only the tested structural properties.** They do **not** validate standards clauses, live external URLs, factual truth, conceptual completeness, source support or publication acceptance.

**On failure:** Inspect the first meaningful error, correct the actual article/index/script mismatch, rerun validation, and report the new passing **commit-specific** result. Do not hide failures, remove a gate just to obtain green CI, or claim success before the run has completed.

## 12. Historical evidence, change discipline and communication

**Before changing files:** Read their *current* contents and Git state. Keep scope narrow. Use clear commit messages identifying the actual change and do not overwrite intervening updates. When updating a single GitHub file, use its latest blob SHA. Avoid edits whose only purpose is incrementing counts.

**When reconciling:** Treat approved architecture decisions and current real article files as higher-confidence evidence than an older audit snapshot. Correct stale claims in active navigation/plans as needed; preserve original audit reports as dated evidence, or add a dated clarification instead of silently rewriting history.

**When reporting:** Say exactly **what was changed**, **where**, **what checks passed**, and **what is unknown or still proposed**. Include direct links to actual committed GitHub files and passing run evidence. Never say “complete” without naming the scope of completion. Do not claim peer review, full verification, or final publication just because an AI reviewed a batch.

**Operating priority:** prefer substantive new knowledge, model-grounded corrections, defensible ownership boundaries, coverage-gap closure and inspectable evidence over decorative documents or metric inflation. When a better route becomes evident, redirect transparently while preserving user-approved constraints.

## 13. Next-agent handoff checklist

On entering this subtree:

1. Read [this division's README](README.md), [architecture](ARCHITECTURE.md), [working inventory](SUBJECT-INVENTORY-PROPOSAL.md), [development plan](DEVELOPMENT-PLAN.md), and [pilot register](pilots/README.md).
2. Check [the latest coverage review](COVERAGE-AND-GAPS-REVIEW-03.md), [model crosswalk](ESTABLISHED-MODEL-CROSSWALK.md), [ownership boundaries](OWNERSHIP-BOUNDARIES.md), and [architecture adjudication](ARCHITECTURE-ADJUDICATION-02.md).
3. Compare candidate content with actual [Fundamentals](../fundamentals/README.md) and [Operational Foundations](../operational-foundations/README.md) definitions before asserting a new canonical owner.
4. Identify one high-value gap or review batch, determine whether it is **source deficiency**, **technical depth**, **ownership** or **truly new concept**.
5. Author or correct substantive content and primary source evidence.
6. Create a bounded technical review, update **all** affected state records, and validate in CI.
7. Report results and remaining gates **without treating proposed area/subject counts as fixed, or self-approving the taxonomy**.

**Core rule:** *Understand the actual knowledge, distinguish the concepts, ground the claim, make the smallest justified change, preserve the evidence, and let the structure evolve.*
