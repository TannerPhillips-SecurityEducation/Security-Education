# AGENTS.md | Application Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `application/` and all descendants.  
**Inherited authority:** [Repository-wide AGENTS.md](../AGENTS.md) governs variable content, evidence, initiative, approvals, and validation. This document adds domain-specific obligations without changing the approved [Domain → Function → Implementation](../README.md#knowledge-domains) navigation.  
**Status:** Working contributor instructions, **not** a new subject taxonomy, publication decision, or mandatory technical platform.  
**Primary classification:** Application Function. Deeper implementation and subject taxonomies remain unapproved until explicitly established.

## 1. Mission and non-negotiable boundaries

Explain how applications accept input, compute, manage state, communicate, enforce application-level decisions, run workflows, emit observations and progress through deployment lifecycles. Canonical ownership follows the **application function**, not whether the application is web, mobile or desktop.

**Scope boundary:** Fundamentals owns general algorithms, programming, data structures, interfaces and computation. Security Foundations owns general security-policy, vulnerability and assurance concepts. Operational Foundations owns software-security reviews and defensive operating practices. Endpoint, Cloud and Identity own their own infrastructure and identity-function implementations. This domain owns behavior and mechanics **inside applications**.

This is a **technical reference** rather than an assessment or certification program. No Knowledge Checks, Practical Assessments, quizzes, graded labs, compulsory course modules, or fake deployment evidence. The root SOP's variable article length, depth, diagrams, tables, examples, and flexible subject count apply here without exception.

## 2. Approved structure versus future proposals

The [domain README](README.md) identifies the **existing approved functional navigation categories**. Their presence authorizes function-first navigation, **not** unreviewed deeper subtopics, permanent implementation directories, a fixed article count, or a formally adopted ontology.

The actual current tree contains function/category READMEs, with **no substantive implementation-reference corpus yet**. Do not invent a completion percentage or silently create one article for every possible technology.

**Canonical home:** A topic's general definition has one appropriate home. Keep alternate views pointing to that article. Proposed new function categories, merges, secondary directories, and persistent technical implementations require evidence and an applicable architectural decision.

## 3. Existing directory navigation

### Primary function categories

- [Input & Interaction](input-interaction/README.md)
- [Logic & Processing](logic-processing/README.md)
- [State & Data Management](state-data-management/README.md)
- [Communication & Integration](communication-integration/README.md)
- [Authentication & Authorization](authentication-authorization/README.md)
- [Execution & Workflow Management](execution-workflow-management/README.md)
- [Observability & Error Handling](observability-error-handling/README.md)
- [Deployment & Lifecycle](deployment-lifecycle/README.md)

### Secondary perspectives and alternatives

- [Web Applications](web/README.md)
- [Desktop Applications](desktop/README.md)
- [Mobile Applications](mobile/README.md)
- [Services & APIs](services-apis/README.md)
- [Command-Line Applications](command-line/README.md)
- [Embedded Applications](embedded/README.md)
- [Other & Specialized Applications](other-specialized/README.md)

**Placement rule:** Application-type indexes are alternative views for web, desktop, mobile, service/API, CLI, embedded and other applications, not rival canonical trees. Architecture style, framework, programming language, runtime and security characteristics remain different descriptive dimensions.

**Do not** mistake these directory titles for a proof that real-world systems divide into disjoint classes, or that a software, hardware or service feature has only one relationship.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Inspect the current domain index, actual function READMEs, current source specifications, related Foundations subjects, actual code/captures/configuration where supplied, and existing repository history.
2. **Derive:** Establish the unit of analysis, functional scope, interfaces, representations, state, dependencies, assumptions, relevant model types and authoritative reference boundaries.
3. **Infer:** Identify what is missing, where concepts overlap, what mechanisms are supported, which conclusions are uncertain and whether a claim describes an abstract model or a real implementation.
4. **Act:** Make the smallest valuable, justified improvement: source-grounded article, function scope refinement, traceable relationship link, reviewed architecture proposal, error correction or validation. Reconcile affected indexes and evidence.

Use the loop as a collaboration method, not an obligatory template for article headings or a replacement for actual system behavior. Avoid repetitive confirmation, Socratic questioning and unearned agreement. Challenge technical falsehoods with evidence.

## 5. Domain-specific distinctions and failure modes

- **Input / parsing / validation / normalization / execution:** Accepting a syntactically valid input does not prove its meaning, authority or safety.
- **Interface / API / protocol / transport / integration:** An HTTP endpoint and its business operation are different layers; transport success is not application effect.
- **Business state / session state / persistent storage / event log / cache:** A successful response does not guarantee durable or correct state.
- **Authentication / authorization / application policy enforcement:** Identity proof, access decision and enforced object operation are distinct.
- **Error handling / exception / transaction rollback / observability:** A logged exception is not necessarily a failed business operation or the complete failure cause.
- **Build / deploy / run / release / update / rollback:** A CI success or a signed artifact alone does not show the deployed application functions as intended.
- **Web/mobile/desktop/embedded:** Application type does not determine its primary functional category or an invariant security model.

**Non-equivalence principle:** A name, vendor diagram, successful API command or available telemetry cannot silently stand in for a distinct function, action, observed result, security property or implementation guarantee.

## 6. Authoritative sources and evidence standards

Official language/runtime and framework specifications, platform vendor APIs, published protocol standards, authoritative database client specifications, application design and testing documentation, and primary software-engineering/security references. Validate the version-dependent behavior before copying samples.

For each significant claim identify **source type**, edition/version, applicable layer, context, constraints and meaningful counterexamples. Prefer current normative/primary material. A vendor's product feature is not by itself an industry standard; an old standard may be historically important but no longer current.

**Model versus evidence:** Hypothetical traces and diagrams must be labeled illustrative. Measurements require provenance, instrument placement and uncertainty as appropriate. Bibliography presence does not equal passage-level verification.

## 7. Authoring substantive function and implementation references

A technically useful article answers, in **variable and topic-appropriate depth**:

- What is the actual **application function**, and what problem or system role does it serve?
- What structures, entities, inputs, outputs, interfaces, state and prerequisites participate?
- How does the mechanism operate? Follow a representative operation from input/interaction through validation, business logic, state mutation, integration, output and error paths. Explain the exact boundaries between application behavior and external OS, cloud, identity, network or data-service dependencies.
- What assumptions, operational limits, failures and version differences matter?
- How does the relevant implementation differ from shared Fundamentals principles or general Security Foundations protections?
- What evidence supports the important claims and worked results, and what remains **Unknown**?

**Illustrative worked-case direction:** A hypothetical 'view document' request: client input → route parsing → principal context → object-level authorization → data retrieval → response serialization → logging. An HTTP 200 or a successful UI render does not by itself prove the read was authorized, durable or privacy-compliant.

Use narrative technical explanations, exact diagrams, tables, traces, mathematics or code where they genuinely help. **No fixed article word count, chapter count, example count or diagrams quota.** Distinguish official requirements, derived explanations and invented examples. Link to actual canonical Foundations materials.

## 8. Knowledge gaps, granularity and scope changes

Use evidence-led dispositions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. A missing page, absent model name, thin implementation detail and genuinely absent concept demand different remedies.

**Domain-specific placement:** An API design explanation belongs under **Communication & Integration** or another function as appropriate; web and mobile type indexes should link to that canonical content. Application-specific authorization **enforcement** belongs under **Authentication & Authorization**, while shared access-control policy theory belongs in Security Foundations.

Maintain old-to-new subject mappings, rationales, source versions, current approval states and affected links for any structural revision. The approved navigation functions are the **current** baseline; do not contract or expand them by accidental file creation or because another domain has a different number.

The root SOP's *variable content* requirement governs: article length, technical complexity, subtopic counts, diagrams, tables and pace follow actual knowledge, **not a quota**.

## 9. File and relationship responsibilities

- `AGENTS.md`: Domain-specific agent/editorial instructions; inherits [root SOP](../AGENTS.md).
- `README.md`: Actual domain navigation, scope and current state. Do not make it the only technical reference.
- `<function>/README.md`: Approved function scope and real links to substantive articles once they exist.
- `<function>/<subject>.md`: A proposed example of a future, **approved-placement** implementation reference, not proof a file currently exists.
- Secondary indexes: Multiple discovery views that point to **one canonical document**.
- Scope/ownership decisions: Explain overlap, distinct conceptual responsibility and any change to approved navigation.
- Article review: Specify claims tested, source versions, example checks, limitations and editorial state.
- Tests and tools: Check the actual content/classes implemented; their green result is not expert source approval.

Maintain accurate cross-domain links as related articles develop. **Do not force a numeric cross-link quota or duplicate foundational definitions** for every application.

## 10. Content development and evidence states

Keep separate **architecture approval**, **subject manuscript state**, **source review**, **relationship verification**, **empirical implementation validation**, and **publication**.

Proposed or Inventoried → Draft requires a real substantive file. **Draft → Reviewed (model-assisted)** requires a documented scoped technical audit checking material claims, mechanisms, examples, versions, counterexamples and limitations. **Core claims checked** requires actual source review, not just links. **Verified** and **Published** require their own evidence and authorized gates. Never inherit a sibling division's review status.

Security claims remain conditional. A control listing or successful demonstration does not automatically establish security, safety, privacy or correctness for every environment.

## 11. Checks, risk controls and actual validation

**Domain-specific review:** Check versioned API/serialization rules, field types, failure and retry semantics, authentication claims, object authorization, data consistency, integration boundaries, user-visible effects, and whether test data are invented. Do not mistake a passing unit test for universal runtime correctness.

Before and after edits, inspect the current tree and paths, check all affected local Markdown targets, headings, and references, reconcile function/index scope, verify source editions, and review technically material examples.

**Current validation reality:** This domain has navigation READMEs but no dedicated function/implementation inventory validator or domain CI in the existing tree. Do not claim unperformed automated tests. Follow [repository integrity principles](../AGENTS.md) and develop validation as actual article inventory and automation justify it. GitHub Actions for other divisions are not proof about this domain.

## 12. Approval, versioning and communication discipline

Read current files and their Git history before editing; use the latest blob SHA for updates. Preserve approved categories and historical choices while testing revisions. Record proposed or derived changes as **proposed**, not automatically approved.

Use small reviewable commits and exact file paths. Do not fabricate source passages, captures, deployed tests, certifications or publication. If a scope decision remains open, keep it explicit and author only correctly labeled pilots or drafts in an authorized location.

Report what is **actually written**, reviewed, validated, proposed and unknown. Use direct GitHub links only to real files or completed passing runs. Prefer independent technical reasoning, useful initiative and candid corrections.

## 13. Next-agent handoff checklist

1. Read [root AGENTS.md](../AGENTS.md), [this domain README](README.md), [relationship conventions](../RELATIONSHIPS.md), and relevant function indexes.
2. Confirm that the concept's general owner is not already in [Fundamentals](../foundations/fundamentals/README.md), [Security Foundations](../foundations/security-foundations/README.md), or [Operational Foundations](../foundations/operational-foundations/README.md).
3. Read original/versioned technical sources and identify what the domain-specific function **does**, **how**, **under what conditions** and **with what evidence**.
4. Author substantive function-level references before selecting arbitrary web frameworks or vendors as the hierarchy; use type indexes for navigation as implementations are actually written.
5. Make one coherent technical/structural improvement; inspect real paths, links, example validity and claim limits.
6. Update navigation and review evidence without inventing architectural approvals or permanent subject quotas.
7. Report the completed work, its validation scope and remaining uncertainties.

**Governing rule:** Function before product. Evidence before confidence. Canonical ownership before duplication. Complexity determines depth. Architecture and content remain truthfully revisionable.
