# AGENTS.md | Fundamentals Editorial & Engineering Contract

**Applies to:** Fundamentals directory and all descendants.  
**Status:** Working **subtree-wide agent/contributor instructions** grounded in the [approved Fundamentals architecture](ARCHITECTURE.md). This file does **not** create new conceptual categories, ratify a formal ontology, certify external sources, or imply publication approval.  
**Sibling contracts:** [Security Foundations AGENTS.md](../security-foundations/AGENTS.md) and the [Operational Foundations division](../operational-foundations/README.md). Each division owns a distinct kind of knowledge.  
**Repository convention:** [Hierarchy for navigation, knowledge graph through links](../../RELATIONSHIPS.md). Explicit user direction and higher-priority instructions take precedence over this working guide.

**Inherited root SOP:** [Repository AGENTS.md](../../AGENTS.md) governs evidence, variable depth/granularity, editorial autonomy, non-Socratic collaboration, approvals, provenance and validation across the repository. This file adds division-specific requirements; it does not override higher-priority instructions or turn proposed knowledge structures into approved ones.

**Foundations-level inheritance:** [Foundations AGENTS.md](../AGENTS.md) governs shared cross-division ownership, flexible inventories, evidence and review boundaries; this file supplies the domain-specific rules.

## 1. Mission and non-negotiable boundaries

Fundamentals establishes **domain-agnostic concepts, structures, principles, and mechanisms necessary to understand technical systems and their behavior**, without making a vendor, platform, security practice or specialist domain its organizing principle.

Apply the four **approved** architecture requirements:

1. **Domain independence:** Define general concepts without relying on one domain-specific implementation.
2. **Conceptual and mechanical depth:** Explain meaning, structure, governing principles, mechanisms, and relationships, not terminology alone.
3. **Canonical ownership:** Keep one general definition per coherent concept. Contextual manifestations link to it or explain genuinely different mechanisms.
4. **Specialized extension:** Let the seven specialized domains build on general references without duplicating their definitions.

**Boundary routing:** General state, event, relation, probability, system, data and observation models belong here. [Security Foundations](../security-foundations/README.md) owns shared security-specific protection, risk, threats, controls and assurance. [Operational Foundations](../operational-foundations/README.md) owns the cross-domain **methods and activities** of security work. Network, Endpoint, Application, Cloud, Industrial, IoT and Identity Knowledge own particular functions and implementations.

**Do not create:** Knowledge Checks, Practical Assessments, quizzes, graded labs, certification tracks, training schedules, invented permanent formal primitives or mandatory vendor technology. Worked examples, transparent calculations and falsifiable illustrations **are** permitted.

## 2. Approval boundary: what is actually settled

**Approved:** The Fundamentals governing definition, four requirements and twelve current navigation knowledge areas. The folder names organize study and discovery; they are not by themselves ontological parent-child predicates.

**Current, versioned inventory:** The [division index](README.md) and [development register](DEVELOPMENT-VERIFICATION-REGISTER.md) track a historical progression from 109 to 116 to **120 canonical subject articles**. These numbers are **snapshots, not targets**. The subject list may grow, contract, split, merge, rename and relocate when concept boundaries and authoritative knowledge justify changes.

**Current review status:** The 120 subjects have documented scoped **Reviewed (model-assisted)** states. **Core claims checked** is a distinct, bounded source-review state. Neither means fully source-Verified, independently human peer-reviewed, or finally Published.

**Not approved by implication:** New top-level areas, universal primitives, mandatory graph predicate vocabulary, technology catalogs, assessment content, extra publication approvals or article accuracy merely because a file is linked.

A previous audit's count describes **its own snapshot**. An agent recommendation is **not** an explicit user decision. Do not rewrite a historical report to pretend a later scope was present from the start.

## 3. Architecture and directory responsibilities

The real Fundamentals tree consists of **12 approved area directories** containing their own README and subject articles, a division root of governance/coverage/review documents, and a tools directory:

| Location / file | Authority and purpose |
| --- | --- |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Approved definition, requirements, placement rules, inventory governance |
| [README.md](README.md) | Public division navigation and current subject/review summary |
| Twelve area READMEs, e.g. [Mathematics & Logic](mathematics-logic/README.md), [Systems & Engineering](systems-engineering/README.md) | Area scope, subject order, real canonical links, current status |
| Area article, e.g. [Search and Information Retrieval](information-data/search-and-information-retrieval.md) | Substantive canonical knowledge, assumptions, mechanisms, worked examples and boundaries |
| [CANONICAL-OWNERSHIP-REGISTER.md](CANONICAL-OWNERSHIP-REGISTER.md) | Concept ownership, related subjects, illustrative directional relationships |
| [CONCEPT-BOUNDARY-DECISIONS.md](CONCEPT-BOUNDARY-DECISIONS.md) and [COVERAGE-GAP-DECISIONS.md](COVERAGE-GAP-DECISIONS.md) | Established non-equivalences, missing depth and documented scope decisions |
| [FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md), [COVERAGE-AND-SOURCE-TRIAGE-02.md](COVERAGE-AND-SOURCE-TRIAGE-02.md) | Historical source-grounded additions, consolidations and ID continuity |
| [CURRICULUM-DEVELOPMENT-PLAN.md](CURRICULUM-DEVELOPMENT-PLAN.md) | Workflow and production gates; **curriculum means reference knowledge, not graded training** |
| [DEVELOPMENT-VERIFICATION-REGISTER.md](DEVELOPMENT-VERIFICATION-REGISTER.md) | Actual subject IDs, paths, development/source states and review evidence |
| [WAVE-H-TECHNICAL-REVIEW-01.md](WAVE-H-TECHNICAL-REVIEW-01.md) and earlier Wave A–G reports | Timestamped, bounded audit evidence; not substantive article replacements |
| [PUBLICATION-READINESS-AUDIT-01.md](PUBLICATION-READINESS-AUDIT-01.md) | Historical navigation/readiness check with a **prior** inventory denominator |
| [tools/check_internal_links.py](tools/check_internal_links.py), [tools/check_inventory.py](tools/check_inventory.py) | Mechanical relative-link and inventory/state checks; not technical peer review |

The **knowledge graph is expressed by accurate relationships and real Markdown links**, not by declaring a formal semantic graph schema. Folder placement is for navigation. Maintain one appropriate owner and contextual links, not parallel competing definitions.

## 4. Editorial operating loop: Observe → Derive → Infer → Act

Use the loop as a *method of work*, not a mandated formal chapter template or universal ontology.

1. **Observe:** Read the actual GitHub tree, current governing architecture, source article, area index, development register, previous decisions, references and CI status. Distinguish primary evidence from historical summaries.
2. **Derive:** Establish meaning, structure, applicable principles, mechanisms, assumptions, dependencies, related concepts and source validity. Recompute examples and distinguish abstract theory from observed implementations.
3. **Infer:** Identify real missing knowledge, duplicated ownership, weak or stale evidence, contradictory definitions, insufficient examples, hidden assumptions, and necessary structural revisions. State what remains unknown.
4. **Act:** Make the smallest coherent, high-value supported change; author a substantive article, deepen a weak explanation, correct a source, reconcile relationships, or document a justified structural decision. Record it and run checks.

Proactively decide **which knowledge gap matters**, not merely how to perform assigned edits. You may conduct ordinary reversible research, writing, reviews and link repair without serial permission requests. Do not misrepresent a proposal as user-ratified, silently delete approved material, fabricate external review, or self-certify publication.

## 5. Conceptual modeling and scientific rigor

**Prefer technically precise, readable explanations over catalogues of terms.** Every substantive subject should make the relevant distinctions explicit, such as:

- **Entity, identity, attribute, relation, boundary, event, state and transition**.
- **Observable, actually observed, measured, recorded and inferred**.
- **Dataset, record, field, value, type, schema, metadata and provenance**.
- **Correlation, causation, hypothesis, test, evidence, uncertainty and confidence**.
- **Model, architecture, architecture description, formal notation, heuristic, standard, implementation**.
- **Time instant, interval, duration, timestamp, causal order and physical clock**.
- **Algorithm, representation, computation, implementation, performance and correctness**.
- **Reliability, fault, failure, risk, control and security**, only to clarify ownership and avoid domain conflation.

A mathematical definition holds only under its stated domain and assumptions. A derived number is **not** an empirical measurement. A named framework **mentioned** in an article is not necessarily explained substantively. An informative diagram is not an architecture proof. Do not equate a syntactically valid representation with true semantics or sound inference.

Use **content, context and intent** only as separate relevant notions; distinguish them from **syntax, semantics and pragmatics** rather than claiming they are interchangeable triads. Unknown remains a legitimate epistemic state.

## 6. Model- and source-first research contract

For important definitions and technical claims:

1. Prefer **original scholarly papers**, official standards, authoritative source documentation and verified reference material over aggregator summaries.
2. Identify source class: mathematical proof, scientific claim, empirical evidence, normative standard, model, architecture description, design heuristic, technical specification or teaching material.
3. Record source **edition, publication date, assumptions, scope, units and counterexamples**. Historical sources can remain important, but must not be represented as the current normative edition where superseded.
4. Compare relevant frameworks and model families before deciding that a concept warrants a new article.
5. **Source links are not source verification.** Relate specific material claims to suitably precise supporting passages; label unavailable licensed documents and unresolved source conflicts.
6. Recompute equations, diagrams, toy datasets, boundary cases and examples independently. Differentiate exact model results, approximations and measured evidence.
7. Where sources differ, compare definitions and applicability and preserve uncertainty; do not flatten genuine disagreements.

The [Models/Frameworks Audit](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) and [named-model lexical ledger](NAMED-MODEL-LEXICAL-LEDGER-01.md) are **diagnostics**. A zero lexical match is not proof of a concept gap; a model-name match is not proof of coverage or correctness.

## 7. Authoring contract for each Fundamentals subject

**Before authoring:** Check the subject's current ID, approved area and intended canonical responsibility in the [development register](DEVELOPMENT-VERIFICATION-REGISTER.md), its area README and [ownership register](CANONICAL-OWNERSHIP-REGISTER.md). Inspect adjacent articles and relevant source models. Avoid creating a duplicate owner.

A substantive reference normally includes:

- **Title and metadata:** actual area, ID, development status, separate source-review state and relevant inventory/decision authority.
- **Canonical definition:** what the concept is and why it matters in general technical systems.
- **Structural anatomy:** participating entities, inputs, outputs, relations, units, boundaries and representations as applicable.
- **Governing rules:** mathematical principles, constraints, conditions, model assumptions and recognized exceptions.
- **Mechanism:** what changes, what causes or constrains it, and how behavior is represented or observed.
- **At least one worked example or counterexample** when meaningful: stated assumptions, reproducible steps, correct result, and what cannot be inferred.
- **Non-equivalences and dependencies:** explicit distinctions from related owners, not repetitive encyclopedia definitions.
- **Source references and limitations:** original/authoritative sources with version and scope; unknowns and incomplete verification stated.
- **Real relative links** to its area index, division index, appropriate neighboring concepts and development evidence.

Prefer substantial narrative reference prose with compact supporting tables, diagrams, formulas or traces. Avoid AI filler, unsupported universality, superficial one-paragraph explanations, imaginary citations or tests, and unnecessary reiteration of the project mission inside every article.

## 8. Knowledge gap, overlap and inventory change policy

**Do not defend a historical count.** The 120-article snapshot is useful for reconciliation only. Distinguish these different dispositions:

| Disposition | Evidence |
| --- | --- |
| **Deepen** | Concept has a proper owner but lacks technical detail, source, proof, example or limitation |
| **Add** | A substantial distinct domain-agnostic concept has no adequate canonical owner |
| **Split** | An article combines logically independent subjects needing separate ownership |
| **Merge** | Two canonical descriptions duplicate the same general concept |
| **Relocate** | Material really belongs to Security Foundations, Operational Foundations or a specialized domain |
| **Cross-link** | An adequate article already exists and a meaningful dependency or contextual application link is missing |
| **Defer** | Evidence is insufficient to identify the right owner, concept boundary or scope |

For any adopted structural revision, record **source-grounded rationale**, prior/new IDs, destination, historical mapping, changed status/counts, updated area/root indexes, canonical ownership and review requirements. Do not silently reuse or destroy retired IDs. New/moved/merged content does **not** inherit earlier source-Verified or Reviewed claims without scoped reevaluation.

A **low number of links to the seven specialized domains** is not a missing-knowledge verdict. Add cross-domain links incrementally as real specialist content develops; never enforce an arbitrary coverage-link quota.

Keep Fundamentals' approved twelve area identities separate from the living subject inventory. A proposal to change area structure requires its own explicit governing-architecture decision.

## 9. File responsibilities and repository navigation

**Document-role discipline:**

- **Index:** README at root or area level is for navigation, accurate links and current status, not the only explanation of a concept.
- **Architecture:** Governing definition, approved scope, boundaries, authorization and change rules.
- **Canonical article:** Reusable substantive technical reference at its proper general home.
- **Ownership/boundary record:** Which article defines what, how neighbors differ, and why an overlap is resolved.
- **Coverage triage/adjudication:** What was missing, what evidence warranted a structural change and how old identifiers map to new.
- **Development register:** Actual files, reviewed states, source-review states, prior-wave evidence and outstanding gates.
- **Technical audit:** Scope, claim-group reviews, worked checks, corrections, source versions and explicit limitations.
- **Tool/CI:** Structural checks and lexical/coverage diagnostics, not correctness proofs.

No redundant root indexes or extra unapproved ontologies. Area article paths should be lowercase, descriptive kebab-case Markdown; area README contents must match registered current subjects. A file link must resolve to a real target. Use a directory link only if supported by the repository's actual link rules; explicit README or file destinations are safer.

On a new subject, update the index, tracking rows and ownership register together, instead of writing a file that remains invisible to navigation.

## 10. Development, evidence and publication states

Keep **distinct axes**, not one overloaded "done" flag:

| Axis | Meaning |
| --- | --- |
| Architecture/ownership | Approved subject location or documented proposal/open decision |
| Development | Inventoried, Draft, Reviewed (model-assisted), or final Published when actually accepted |
| Source review | Not reviewed, References listed, Core claims checked, Verified under documented completeness |
| Relationship review | Proposed, supported/checked, or unresolved |
| Publication | Not accepted versus accepted under actual gates |

Promotion rules:

- **Inventoried → Draft** requires a substantive article file with legitimate internal links, examples and source starting points.
- **Draft → Reviewed** requires a **separate documented scoped technical audit** that checks material claims, definitions, examples, source applicability and meaningful corrections.
- **References listed → Core claims checked** requires real claim-review evidence, not only a bibliography.
- **Verified** requires documented sufficiently complete claim-to-passage verification under explicit acceptance criteria.
- **Published** requires the [Fundamentals completion gates](README.md#completion-gates), independent qualified acceptance as required, and truthful current source/relationship status.

Earlier waves are **dated evidence**, not transferable approval for articles created afterward. A code/CI success is neither scientific peer review nor publication.

## 11. Technical review and CI are different gates

Run the existing local checks from the repository root whenever the working copy is available:

    python3 foundations/fundamentals/tools/check_internal_links.py
    python3 foundations/fundamentals/tools/check_inventory.py
    python3 foundations/fundamentals/tools/audit_coverage_and_sources.py
    python3 foundations/fundamentals/tools/audit_named_models.py

The first two are **structural integrity gates**; the latter diagnostics identify possible coverage/source-name patterns, not proof of a concept gap or a verified source. GitHub CI: [Fundamentals navigation and inventory workflow](../../.github/workflows/fundamentals-internal-links.yml).

Review record for a batch should state **specific articles**, count and identity of **material claim groups**, equations and examples recalculated, primary source versions and applicability, counterexamples, corrections, remaining uncertainties and exact outcome. Then reconcile every affected metadata/index/register entry.

When CI fails, inspect the failure and fix the actual mismatch; do not disable validation to claim success. Cite a **completed, commit-matched** run, not a queued job. Never claim external URL verification from a script that checks only relative links.

## 12. Historical evidence, change discipline and communication

**Read current files before editing.** In a connected GitHub workflow, use current file SHA for updates and avoid racing changes to the same path. Make small reviewable commits with truthful messages; preserve relevant contributor work.

Fundamentals contains **older or stale statements about article counts and review states** in some governance files and area READMEs. The [current register](DEVELOPMENT-VERIFICATION-REGISTER.md), actual article metadata and latest audit evidence are stronger than a historical summary, but may still disagree. **Reconcile the discrepancy** rather than silently choosing whichever number is convenient. Preserve dated original audits and append dated corrections where appropriate.

When reporting, distinguish **completed work** from remaining work. Provide real file and successful CI links, identify scope and caveats, and never call model-assisted source checks independent human peer review.

Give candid technical objections when a requested definition is false or creates duplication. Prefer direct analysis and concrete edits to repetitive questions; ask only when an essential fact is absent.

## 13. Next-agent handoff checklist

1. Read [Fundamentals index](README.md), [governing architecture](ARCHITECTURE.md), [development register](DEVELOPMENT-VERIFICATION-REGISTER.md), [ownership register](CANONICAL-OWNERSHIP-REGISTER.md) and [development plan](CURRICULUM-DEVELOPMENT-PLAN.md).
2. Inspect the actual area directory and canonical article; compare relevant [boundary decisions](CONCEPT-BOUNDARY-DECISIONS.md), [gap decisions](COVERAGE-GAP-DECISIONS.md) and recent technical audits.
3. Inspect authoritative current sources and distinguish fact, derivation, hypothesis, recommendation and unknown.
4. Choose one high-value **source, depth, coverage or ownership** improvement. Document any architectural revision without treating a historical count as fixed.
5. Make substantive edits, recompute examples, verify internal paths and prepare bounded source/claim review evidence.
6. Update article metadata, area/root navigation, ownership/tracking and audit records together.
7. Run available local/CI checks and report the exact, limited validated outcome.

**Core rule:** Understand the actual knowledge, distinguish the concepts, ground the claims, make justified changes, preserve evidence and let the inventory evolve.
