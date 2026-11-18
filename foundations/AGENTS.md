# AGENTS.md | Foundations: Shared Knowledge Governance

**Applies to:** `foundations/` and all descendant divisions.  
**Inherits:** [Repository SOP](../AGENTS.md), which governs variable content, evidence-based writing, proactive collaboration, truthful approval states, and validation.  
**Status:** Operational instructions, not a new taxonomy, a mandatory study sequence, or authorization to publish. Division-specific contracts supplement this file where their approved scope requires different treatment.

## 1. Mission and knowledge ownership

Foundations owns **reusable knowledge that crosses technical and security domains**. The three approved divisions have different responsibilities:

| Division | Canonical responsibility | Subtree instructions |
| --- | --- | --- |
| [Fundamentals](fundamentals/README.md) | Domain-agnostic scientific, mathematical, logical, computational, informational and systems concepts and mechanisms | [Fundamentals AGENTS](fundamentals/AGENTS.md) |
| [Security Foundations](security-foundations/README.md) | Shared security-specific objectives, properties, threats, conditions, risk, safeguards, evidence, trust and assurance | [Security Foundations AGENTS](security-foundations/AGENTS.md) |
| [Operational Foundations](operational-foundations/README.md) | Reusable methods, practices, analytic and decision processes for doing security work | [Operational Foundations AGENTS](operational-foundations/AGENTS.md) |

The seven specialized [knowledge domains](../README.md#knowledge-domains) own their concrete functions and implementations. **Knowledge may be relevant in several places while retaining one general canonical home.**

## 2. Explicit approvals and architecture limits

The **three divisions** are approved. Their **internal architecture states are not equal**:

- Fundamentals has an approved governing architecture and twelve current approved navigation areas. Its subject inventory is living and revisionable.
- Security Foundations is an approved division whose **Fundamentals-style area/README/article directory pattern is explicitly adopted**. Its 12 current area names and 96 subject candidates remain provisional. Twenty substantive working articles now reside within area directories: 18 have scoped model-assisted reviews (Reviews 01–05), and two new cryptography manuscripts (SF-09-02 and SF-09-07) are **Draft / References listed** awaiting their next separate review batch. Semantic ownership, complete source verification and publication remain unratified and independent.
- Operational Foundations is approved as a division but has **no approved internal subject taxonomy**. Do not fabricate one to match sibling divisions.

Proposed taxonomies, mathematical primitives, relationship predicates and fixed numbers of chapters, articles, areas or categories are **not** user-approved merely because they appear in working files. Preserve explicit user approval separately from agent recommendations and historical project proposals.

## 3. Navigational architecture

**Approved governing principle:** [Hierarchy for navigation, knowledge graph for relationships](../RELATIONSHIPS.md). A directory is a useful place to discover knowledge, not an ontological assertion that everything beneath it is the same kind of entity.

**Use Fundamentals' navigational pattern** across developed Foundations corpora: division index → meaningful area directories → area README → substantive subject articles. **Do not copy its exact twelve categories, titles or subject quotas.** Security Foundations currently uses this pattern with provisional area membership; Operational Foundations has no authored taxonomy yet. Build and revise actual area identities from sources and explicit governance.

A foundational concept gets **one general owner**. Other locations explain distinct contextual extensions and link to the owner without duplicating the complete definition.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe** real current files, governing definitions, prior decisions, source material and actual validation.
2. **Derive** concept structure, intended scope, dependencies, conditions, mechanisms and the correct division.
3. **Infer** true knowledge gaps, duplicate ownership, stale claims, source uncertainty and useful next work.
4. **Act** with the smallest justified substantive change, update related records and validate the actual outcome.

This is a working SOP, **not** an article template or universal ontology. Prefer direct explanation, independent critique and initiative over repetitive or Socratic questioning. Do not falsely claim unavailable background execution.

## 5. Technical and epistemic distinctions

Keep clear the difference between **entity, event, observation, record, evidence and inference**; **concept, mechanism, implementation and operational action**; **cause, correlation, hypothesis and intent**; **mathematical model and measured reality**; **source reference and verified source support**.

Unknown is a legitimate result. Missing telemetry or a failed search does not prove the underlying event did not occur. A security classification does not establish a real actor's motive. An internally sound model does not prove its physical or organizational assumptions.

Distinguish **syntax / semantics / pragmatics** from **content / context / intent**, without converting them into a mandated universal taxonomy.

## 6. Authority and sources

Use appropriate original papers, current normative standards, source-maintainer documentation and trustworthy measured or empirical evidence. Identify publication version, source type, unit of analysis, assumptions, scope and limitations.

A model, taxonomy, heuristic, engineering guide and standard are **not interchangeable** sources of authority. Cite sufficiently precise passages for material claims when feasible. Correct obsolete technical references and record when full source access is unavailable.

**A bibliography is not verification.** Recompute examples and test counterexamples, assumptions and non-equivalent concepts.

## 7. Authoring and content variability

The content governs length, structure, model depth, worked examples, visuals, equations and references. **No fixed word count, section count, article count or symmetrical number of subjects per area** is allowed as a substitute for knowledge depth.

Articles should explain what a concept or method **is**, why it matters, its structure, governing principles, mechanisms, conditions, failure modes, evidence, boundaries and source limitations in a fluent technical narrative. Use formal arguments, concise tables or diagrams only when they improve comprehension.

**Do not add Knowledge Checks, Practical Assessments, quizzes, scored labs or mandatory course progression** to this reference repository.

## 8. Coverage and change governance

Classify identified work as **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. A missing article, absent search keyword, missing link and genuine canonical knowledge gap are distinct findings.

Subject inventories **may expand or contract** with recorded conceptual and source-backed rationale. Keep historical IDs and old-to-new mappings when relocating or consolidating articles. Do not infer a new area from one popular model or imported standards chapter.

Cross-division and specialized-domain links should be added **incrementally where actual content exists**, never to satisfy a numerical link quota.

## 9. File and status responsibilities

- [Foundations README](README.md) describes the three approved division purposes and real navigation.
- Division READMEs describe current corpus state and actual canonical/pilot paths.
- Architecture files govern explicit approved versus proposed scope.
- Candidate inventories and ownership records describe coverage and canonical responsibilities.
- Article manuscripts contain substantive knowledge.
- Review and source-evidence records document **what was checked and what remains unknown**.
- Technical scripts and CI check mechanical properties, not factual truth or publication acceptance.

Do not create placeholder directories, duplicate root indexes, or fake article files simply to imitate a more developed division.

## 10. Independent review state axes

Track separately: **architecture approval**, **content development** (Inventoried/Draft/Reviewed), **source-review depth** (Not reviewed/References listed/Core claims checked/Verified), **relationship review**, and **publication acceptance**.

**Flexible-batch authoring requirement:** **Draft batch → Review batch.** A batch may contain **one or multiple articles**, with size chosen for concept coherence and the depth of evidence rather than an arbitrary quota. The next authoring-related response following a Draft batch reviews **all articles from that batch that remain Draft**, optionally together with other outstanding Drafts, before a different Draft batch begins. A Review can cover several articles in one bounded, article-attributed audit. Only promote articles actually supported by their own review evidence; unresolved manuscripts stay Draft. Source-level verification and publication remain separate gates.

Model-assisted technical review can support a scoped Reviewed status only with a separate material-claim audit; it is not complete passage verification or independent human peer review. Final Published status requires actual publication gates and authorization. Historical wave review outcomes cannot automatically be inherited by new or merged work.

## 11. Validation and automation

Validate actual Markdown links, headings, article paths, IDs, review statuses and inventory counts after changes. Reconcile division/area navigation, ownership and source records. Use existing [Fundamentals CI](../.github/workflows/fundamentals-internal-links.yml) and [Security Foundations CI](../.github/workflows/security-foundations-integrity.yml) where applicable.

A repository-wide structural check may verify instruction inheritance and current navigation, but **green CI is not technical peer review**. Operational Foundations currently has no independently established subject-inventory validator. Do not invent a passing workflow.

## 12. Change discipline and communication

Read current files and latest Git state before writing. Preserve date-scoped historical audits while correcting stale statements in active navigation. Use current blob SHAs in GitHub edits and avoid conflicting writes. Explicitly record what is user-approved versus agent-proposed.

Report completed files, changes, validations, limits and next meaningful work. Avoid filler, unearned confidence and repetitive questions. If substantive work remains, say so without disguising a partial batch as full publication readiness.

## 13. Next-agent handoff

1. Read the [root SOP](../AGENTS.md), this file and the relevant division's `AGENTS.md`.
2. Inspect current division README, approved architecture, actual articles and working inventories.
3. Verify canonical division ownership against adjacent Fundamentals, Security Foundations and Operational Foundations concepts.
4. Identify the most useful source, depth, knowledge-gap or structural improvement rather than chasing a count.
5. Produce substantive edits, source and material-claim evidence and honest review states.
6. Validate real paths and reconcile all affected documents.
7. Preserve flexible scope and explicit architecture approvals.

**Governing rule:** Shared knowledge deserves one defensible home; depth follows complexity, relationships follow genuine dependencies, and evidence governs review claims.
