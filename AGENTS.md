# AGENTS.md | Security Knowledge Repository: Governing Standard Operating Procedure

**Scope:** Repository root and every descendant directory in `Security-Education`, unless a more specific, compatible subtree `AGENTS.md` provides additional requirements.  
**Status:** Operational instructions for contributors and AI agents, grounded in the repository's approved architecture, the user's explicit collaboration and editorial constraints, and demonstrated source-led working methods. This file is **not** a new subject taxonomy, a formal ontology, or approval to publish.  
**Authority limit:** Higher-priority platform and developer instructions, applicable law and safety requirements, and the user's explicit current instructions take precedence. This repository file cannot grant unavailable tools, asynchronous execution, unrestricted external authority, or permission to bypass security controls.  
**Mission:** Develop a living, authoritative, vendor-neutral security and technical **knowledge reference**, with **hierarchy for navigation** and **meaningful cross-linked relationships**.

## 1. Recognize explicit specifications, inferred practices and proposals

Do not collapse these sources of authority.

| Classification | Meaning | How to treat it |
| --- | --- | --- |
| **User-explicit specification** | Directly stated or explicitly approved by the user | Follow within applicable authority; do not replace with an agent preference |
| **Repository-approved architecture** | A governing division, domain, function, boundary or other decision recorded as approved | Preserve unless a subsequent authorized decision changes it |
| **Observed successful practice** | A method demonstrated in the repo's previous work, such as claim-led audits and CI reconciliation | Reuse where it serves the task; do not misrepresent it as an explicitly ratified universal rule |
| **Derived/inferred preference** | A reasonable conclusion about preferred collaboration, technical depth or formatting from prior work | Treat as a working default, open to revision and clearly separate from user approval |
| **Proposed structure/model** | A candidate taxonomy, concept mapping, title, ontology, rule, process, metadata field or implementation | May be researched, tested or drafted; not approved by suggestion, commit or favorable review alone |
| **Unknown or conflicting fact** | Insufficient or contradictory evidence or instruction | Investigate, mark uncertainty, preserve alternatives and avoid unsupported certainty |

**Provenance rule:** Never turn "the agent recommended" into "the user requested," or "the article says" into "the source proved." Historical Git commits and audit reports support **what was done at that time**, not necessarily the current approved state.

## 2. Root repository mission and approved navigation

The [repository README](README.md) and [relationship conventions](RELATIONSHIPS.md) govern established structural commitments.

### Foundations

- [Fundamentals](foundations/fundamentals/README.md): Domain-agnostic concepts, structures, principles, mechanisms and dependencies. Its governing architecture is approved; individual subject inventory totals are living.
- [Security Foundations](foundations/security-foundations/README.md): Cross-domain security meanings, protection objectives, threats, weaknesses, risk, trust, controls, evidence and assurance. The division is approved; its **internal working architecture is not yet ratified**.
- [Operational Foundations](foundations/operational-foundations/README.md): Shared cross-domain methods, decisions and practices used to perform security work. The division is approved; its **internal subject taxonomy is not yet approved**.

### Seven specialized knowledge domains

The approved primary navigation model is **Domain → Function → Implementation**:

| Domain | General canonical responsibility |
| --- | --- |
| [Network](network/README.md) | Network functions, communication, infrastructure, services and their implementations |
| [Endpoint](endpoint/README.md) | Host and endpoint functions, with operating-system families as appropriate discovery perspectives |
| [Application](application/README.md) | Application functions, with application type as an alternative index |
| [Cloud](cloud/README.md) | Cloud functions/services, with provider-specific discovery and implementation context |
| [Industrial](industrial/README.md) | Industrial functions and mechanisms within their proper system context |
| [IoT](iot/README.md) | Connected-device functions, interactions, roles and implementations |
| [Identity](identity/README.md) | Identity and access functions, systems, mechanisms and implementations |

Functions are primary navigation. Operating systems, cloud providers, application types, specific technologies and products may be **secondary perspectives** pointing to the canonical function/implementation article. Do not duplicate an entire general definition for each index.

**A directory is navigation, not automatic ontological parentage.** A concept can relate to many functions and domains while keeping one properly scoped canonical general owner.

**Content exclusion across this repository:** No Knowledge Checks, Practical Assessments, quizzes, grades, scored labs, exam banks, assessment taxonomies, fixed training schedules or mandatory certification pathways. This is a **knowledge reference**, not a classroom delivery platform. Worked technical examples and realistic demonstrations are welcome when they teach the underlying knowledge.

## 3. Core SOP: Observe → Derive → Infer → Act

Use this as an **operating method**, not as a required article outline, a formal security ontology or a claim that human cognition follows one universal sequence.

1. **Observe:** Inspect current repository files/tree, approved rules, relevant source originals, actual code/data where applicable, prior decisions, article bodies, development states, open gaps and CI results. Distinguish what exists from what is assumed or remembered.
2. **Derive:** Determine precise concepts, the system boundary, relationships, models, structures, mechanisms, evidence requirements, prerequisites, units and relevant context. Compare existing canonical homes before proposing a new one.
3. **Infer:** Identify the likely intent of the task, warranted conclusions, gaps, duplication, misconceptions, conflicting authority, alternative explanations and what is **unknown**. Label assumptions rather than silently manufacturing facts.
4. **Act:** Use the tools genuinely available to perform the most valuable justified research, writing, technical correction, indexing, review or validation. Preserve provenance, reconcile affected documents, and report the actual result.

**Separate observation, derivation, inference and action in the work itself**, even when the final explanatory prose flows naturally and does not label every sentence.

For factual determinations use **True / False / Unknown**, or another source-appropriate distinction when useful. "Unknown" is an actual outcome, not a synonym for false, benign, malicious or irrelevant. For security discussions, **Unknown / Benign / Anomalous / Suspicious / Malicious** may be a useful illustrative scale, but it is **not automatically a mandatory repository-wide classifier**.

## 4. Variable content is an explicit governing requirement

**Consistency of epistemic rigor does not require uniformity of content form.** The content must dictate the structure.

**Never freeze any of the following merely for symmetry or easy progress reporting:**

- The **number of areas, subjects, subtopics, articles, chapters, sections, examples, illustrations, source links, relationships, diagrams, tables or pages**.
- The length of an article, paragraph, explanation, example, section, review, wave, batch or manuscript.
- The depth of treatment across articles: simple ideas may be covered concisely; complex ideas may require multiple submodels, proofs, cases or companion articles.
- The number of headings per area or the number of topics assigned to each domain.
- A single outline, template, heading order, count of bullets, table shape or "one paragraph per subheading" recipe.
- The ratio of prose to equations, diagrams, code, traces, screenshots or tables.
- The requirement that every source model, standard, technical acronym or implementation receive its own canonical subject.
- A fixed development order, wave size, article batch size or percentage of completion derived solely from subject counts.
- A uniform complexity level or artificial requirement that each article have equal size, citations or illustrative examples.

**Variability is deliberate, not permission for shallow or incomplete content.** Make each work product **as extensive as the concept needs and no longer than it earns**. A concise definition can be complete for one issue; a formal system may demand mathematical treatment, counterexamples, alternative architectures and extensive source analysis. A dense table is worthwhile where it disambiguates; a narrative is better where causality, sequence or tradeoffs need explanation.

The reusable contract is about **questions that must be answered appropriately**, not a rigid document skeleton:

- What is the subject, and why does it matter?
- What are its constituent entities, structures, variables, states, relations, constraints or assumptions?
- How does its behavior or mechanism work, and what makes it different from adjacent concepts?
- What can be observed, measured, verified, tested or inferred?
- Under which conditions does the explanation hold, fail or remain uncertain?
- How is it supported by authoritative sources, and what do those sources **not** establish?

Not every one of these deserves a dedicated heading in every article. Combine or separate sections according to conceptual coherence. **There is no default article word-count minimum or maximum.** Do not invent a quota. If a source or explicitly approved artifact has its own real limit, honor it only for that artifact.

## 5. Variable architecture, scope, granularity and development

Treat knowledge architecture as **a navigational hypothesis continuously tested against reality**, while preserving explicitly approved divisions and governing boundaries.

- Area and subject inventories can **expand or contract**, whether by adding, splitting, merging, renaming, retiring or moving material with justified evidence.
- The governing count is **the currently recorded, verified inventory snapshot**, not a permanent ceiling, floor or a progress goal to defend.
- A subject can have one article, several tightly scoped articles, or be adequately contained within another subject. Do not force **one concept = one file = one directory**.
- A new concept should not become an area simply because an established source uses it as a major heading.
- An alternate view should be an index or relationship, not a duplicate of the same canonical knowledge.
- The approved **Fundamentals** area baseline has its own governance; the internal **Security Foundations** and **Operational Foundations** subject taxonomies require separate authorization. One division's maturity does not authorize copying its exact folders into another.
- A substantive manuscript can reside **inside a provisional area directory** while its precise semantic ownership remains unratified. Security Foundations adopts the **Fundamentals-style area README plus article** pattern by explicit user direction; historical `pilots/` paths are link-preserving aliases, not additional substantive knowledge.
- Recording an addition/consolidation requires the reason, source/model justification, old/new identifiers, canonical ownership, link/path changes, affected status and explicit approval state.
- Retired IDs and decision histories remain traceable. Do not silently rewrite or delete the past.

**Change-classification options:** Deepen existing content, add a genuinely distinct subject, split a compound subject, merge duplicates, relocate to a more accurate owner, cross-link an existing concept, or defer an uncertain decision. A **missing article** is different from a **missing concept**, **missing reference**, **missing model name**, **missing cross-link** or **missing proof**.

**Cross-domain links grow as real content grows.** Do not treat direct-link counts as quality scores or force every Fundamentals article to link into every domain. Links must be relevant, point to files that actually exist and explain genuine relationships.

## 6. Canonical ownership and precise knowledge distinctions

The default is **one general canonical owner** for a coherent concept, with links to genuinely distinct applied mechanisms and implementations.

A placement decision should ask whether the content is:

| Kind of knowledge | Proper default location |
| --- | --- |
| General logical/mathematical/structural/scientific principle | Fundamentals |
| General information/system/computational mechanism | Fundamentals |
| Shared security-specific objective, property, threat, trust, vulnerability, protection or assurance concept | Security Foundations |
| Reusable cross-domain security activity, workflow, analytic method, decision or response capability | Operational Foundations |
| Actual technology, host/network/cloud/application/industrial/IoT/identity function or implementation | The corresponding specialized domain |

Distinguish these pairs or families whenever materially relevant:

- **Concept / structure / principle / mechanism / function / operation / implementation**.
- **Identity / entity / attribute / relation / boundary / type / schema**.
- **Entity / event / state / transition / trace / history**.
- **Dataset / record / field / value / provenance / evidence**.
- **Observation / observed thing / recording / measurement / inference / assertion**.
- **Cause / correlation / hypothesis / explanation / intent**.
- **Law / formal model / statistical model / explanatory framework / heuristic / reference architecture / standard / product**.
- **Threat / vulnerability / exposure / attempted exploitation / violation / compromise / risk / consequence**.
- **Authentication / authorization / access policy / enforcement / information flow / assurance**.
- **Security / privacy / safety / reliability / resilience**.
- **Operational objective / method / procedure / tactic / technique / tool / role / result**.

Use **syntax / semantics / pragmatics** for language and interaction; use **content / context / intent** for what is represented, what surrounds it and what purpose may be inferred. These are distinct lenses, **not interchangeable**. Any new triad, universal principle, ontology, knowledge graph predicate set, diagram convention or global classification model needs its own scope and evidence before being treated as a repository invariant.

## 7. Model-first, source-first and evidence-first research

Before authoring or changing consequential technical claims:

1. **Search the local repository first** for a canonical owner, existing explanation, prior model comparison, contested boundary and active approval.
2. Consult the strongest relevant **original papers, current normative technical standards, authoritative documentation, primary empirical studies** or other credible sources. Current editions matter when versions affect meaning.
3. **Classify the authority:** formal proof/model, empirical finding, standards requirement, architecture description, taxonomy, heuristic, scoring method, control catalog, operational guidance or teaching reference. Do not present all as laws.
4. Extract the **defined unit of analysis, terms, conditions, inputs, limits, version/date and actual proposition supported**. Check the source's stated scope.
5. Distinguish **source-established facts**, editorial derivations, illustrative assumptions, hypotheses, recommendations and unresolved unknowns.
6. **Recompute** arithmetic, formulas, algorithms, graph counts, sample queries, uncertainty, timestamps and worked examples. For formal claims, consider a counterexample and the conditions under which a theorem applies.
7. Validate external references and passage relevance when the task requires more than listing sources. Note inaccessible or licensed primary materials honestly.
8. If sources conflict, compare editions, definitions, applicability and evidence rather than smoothing over a real disagreement.
9. When research uncovers a missing concept or false existing assumption, document the correction and its implications for the working architecture. Do not insert a model name solely to increase lexical coverage.

**Evidence cannot be substituted:** A green Markdown-link check does not show a source supports a claim. A screenshot, title or bibliography does not prove a mechanism. A detected anomaly does not prove intent. A model fitting data does not automatically establish causation. A cited vendor implementation does not become the general definition.

**Source/version hygiene:** Avoid representing old final publications or drafts as current standards when newer official versions exist. Preserve accurate historical citations where historically relevant, while stating supersession, publication status and any unverified clauses.

## 8. Authoring: narrative education with flexible explanatory form

**Default editorial direction:** A **living technical textbook** in natural, professional language, with subtle narrative progression rather than a stack of glossary definitions or a repetitive AI-generated outline. Explain **why**, **what**, **how**, **under which conditions**, **how we know**, and **what remains uncertain**, following the concept's natural dependencies.

- Open with the subject's meaningful definition and context. Begin from first principles only when the reader actually needs them.
- Explain mechanisms and examples carefully enough to be inspectable and reproducible; do not replace substance with polished phrasing.
- Use direct prose, thoughtful transitions, concise tables, meaningful diagrams, code, queries, traces and mathematics where they genuinely clarify.
- Prefer **narrative exposition**, not "definition → three bullets → generic example → summary" repeated mechanically in every article.
- A concept may require a deep worked model; another may need only a focused distinction and reference. Both can be excellent.
- Distinguish what a representation **depicts** from what is actually observable or measurable. A visual is not evidence simply because it looks authoritative.
- Explain a reader's prerequisites and guide navigation through **actual relationships and links** without imposing a mandatory study order.
- Avoid unsupported confidence, unsupported standard quotations, duplicate definitions, boilerplate summaries, placeholder padding, promotional copy, stock AI phrasing and vague statements of "importance" that teach nothing.
- Avoid patronizing reassurance and reflexive flattery. Correct technical mistakes plainly and respectfully.
- **Do not use Socratic inquiry** or question-driven teaching. Contribute explanation, independent reasoning, critique, options and concrete technical work. Ask only a necessary straightforward clarification when the work genuinely cannot proceed otherwise.

**Variable media:** Choose a table for a precise comparison, a diagram for a relational/causal flow, code for execution or syntax, mathematics for formal models, and prose for causal explanation or conceptual development. Do not require all of them in every article.

**User-authored artifacts take their own style.** Emails, posts, professional articles, books, educational manuals and repository references differ. Do not apply one assistant voice or one document layout indiscriminately.

## 9. Modes of knowledge and non-prescriptive learning order

A knowledge reference should make material discoverable from multiple valid viewpoints:

- **Structural:** constituent parts and their relationships.
- **Functional:** what a component or system does.
- **Operational:** how an action or method is performed.
- **Behavioral and temporal:** states, transitions, sequences, change and time.
- **Epistemic:** observation, data, evidence, uncertainty, inference and limitations.
- **Application and implementation:** how general knowledge manifests in a real context.

These are **editorial lenses**, not an automatically approved new hierarchy or exhaustive taxonomy. Use as many as a topic needs. Readers can follow prerequisites, reverse-trace a concept from a specialized implementation, or explore relationships nonlinearly. Do not force everyone through one linear reading path.

Where knowledge or competence is discussed, distinguish **knowing what**, **knowing how**, **knowing when/why**, and **demonstrating effective action** when useful. Those are explanations, not permission to insert exercises or assessments into this repository.

## 10. Collaboration SOP and agent initiative

The intended working relationship is with an **independent technical collaborator**, not a passive typist or a sycophant.

- **Take initiative over WHAT is worth investigating as well as HOW to execute the assigned work.** Identify valuable corrections, missing prerequisites, false assumptions, contradictions, source/version changes and opportunities to increase quality.
- **Challenge the user constructively when factual or conceptual claims are incorrect.** Independent thought and falsifiable tests are preferred over agreement for its own sake.
- **Avoid repetitive confirmation requests, staged interviews and Socratic questioning.** When scope is adequately established, proceed with available tools.
- **Use approved project context**, already stated constraints, actual GitHub files and available sources before asking the user to repeat them.
- **Make warranted, reversible changes** such as source-backed writing, audits, link repairs, editorial reconciliations and clearly identified working proposals without needing a permission ritual for every step.
- **Make conceptual redirections transparent** when evidence supports a more valuable path; preserve the reason and affected decisions.
- **Respect explicit approval boundaries** for new governing structures, irreversible deletion, externally publishing content, credentials, operational changes and other high-impact actions.
- **Never claim independent background work** or promise work will be delivered later without an actual scheduling/automation capability and authorized execution. Progress belongs in the current interactive task.
- **Report candidly** what was completed, what failed, what remains unknown, and what can or cannot be done with current tools.
- User instructions to **"Proceed"** mean continue the active scoped objective directly, not reopen resolved questions or promote an unapproved proposal to approved status.

**No reflexive questions:** Direct, original analysis and useful execution are the default. One concise clarification is acceptable only when an essential missing detail cannot be resolved from existing context.

**Uniform layout, tailored substance:** Wherever a Foundations corpus is actively developed, use a division `README.md`, coherent knowledge-area directories, each area's `README.md`, and substantive subject Markdown within those areas. Security Foundations has now adopted this **Fundamentals-style pattern** while retaining flexible, provisional individual area/subject identities. **Uniform structure never forces identical counts, article sizes, source types or semantic ownership.**

## 11. Repository architecture, links and file responsibilities

**Root [README](README.md):** Approved repository navigation and scope. **Root [RELATIONSHIPS](RELATIONSHIPS.md):** Canonical location and relationship conventions. **Root AGENTS (this file):** Cross-repository SOP.

**Subtree `AGENTS.md` files** narrow the SOP to local meaning and maturity:

- [Fundamentals AGENTS.md](foundations/fundamentals/AGENTS.md): approved governing architecture, variable subject inventory, substantive canonical content and existing review controls.
- [Security Foundations AGENTS.md](foundations/security-foundations/AGENTS.md): user-approved **Fundamentals-style area/README/article structure**, with flexible provisional area identities, **29 Reviewed (model-assisted) working manuscripts and zero Drafts**, including four SF-03 articles covered under the separate [Technical Review 08](foundations/security-foundations/PILOT-TECHNICAL-REVIEW-08.md); full source verification, taxonomy approval and publication acceptance remain separate.
- [Operational Foundations AGENTS.md](foundations/operational-foundations/AGENTS.md): shared security methodologies with **no approved internal taxonomy or article inventory yet**.

**Specialized domain contracts (all inherit this root SOP):**

- [Network AGENTS.md](network/AGENTS.md): communication functions, protocols, traffic units, telemetry and network-specific implementation evidence.
- [Endpoint AGENTS.md](endpoint/AGENTS.md): OS-aware host functions, privileged behavior, execution/storage boundaries and OS-family secondary indexes.
- [Application AGENTS.md](application/AGENTS.md): function-first application behavior, state, APIs, validation, authorization and application-type discovery indexes.
- [Cloud AGENTS.md](cloud/AGENTS.md): cloud-service functions, resource and control/data planes, provider-specific semantics and provider secondary indexes.
- [Industrial AGENTS.md](industrial/AGENTS.md): industrial physical processes, controllers, instruments, safety constraints and operational-technology implementations.
- [IoT AGENTS.md](iot/AGENTS.md): connected-device functions and roles, gateways, sensor/actuator evidence, constrained resources and lifecycle states.
- [Identity AGENTS.md](identity/AGENTS.md): proofing, credentials, authentication, authorization, federation, privilege and identity assurance.

**Repository automation:** [GitHub Actions AGENTS.md](.github/AGENTS.md) defines least-privilege CI, truthful pass/fail evidence, safety constraints and dynamic inventory checks.

Each top-level directory now has a **tailored 13-section operating contract**. These contracts refine, but cannot silently override, this SOP's flexible content, canonical ownership, explicit approval and evidence requirements.

Domain README and function indexes remain the source of truth for domain-approved navigation and implementation placement.

File purposes must remain distinct:

| File type | Responsibility |
| --- | --- |
| `AGENTS.md` | Agent/contributor execution and quality instructions within its subtree |
| `README.md` | Navigation, scope, real article links and current state |
| Architecture decision / governing document | What is approved, proposed, excluded and how placement is adjudicated |
| Candidate inventory / ownership register | What concept should belong where and which IDs map to actual owners |
| Canonical subject article / clearly labeled pilot | Substantive technical knowledge and context, not just an index |
| Development and verification register | Real files, status, review evidence, remaining gates |
| Coverage/overlap review | True gaps, duplicate ownership, conflicting models and reasoned dispositions |
| Technical audit / review wave | Material claims checked, corrections, examples verified, scope and evidence limits |
| `tools/`, `.github/workflows/` | Deterministic integrity checks and diagnostics, never silent replacement for factual review |

**One canonical home per coherent concept.** Alternative pathways link to real destinations. Keep current relative links and heading fragments correct. Do not create empty placeholder directories or advertise nonexistent content.

## 12. Approval, evidence and publication are distinct state axes

Maintain *independent*, inspectable states:

| Axis | Meaning |
| --- | --- |
| **Architecture** | Proposed / working adjudication / explicitly approved |
| **Content development** | Inventoried / Draft / scoped Reviewed (model-assisted) / Published where authorized |
| **Source review** | Not reviewed / References listed / Core claims checked / Verified under explicit claim-to-source criteria |
| **Relationship review** | Proposed / examined / supported / unresolved |
| **Method or empirical validation** | Illustrative model / experimentally tested in scope / real-world evidence bounded to actual conditions |
| **Publication** | Unaccepted / accepted under declared gates and qualified review |

Rules for progression:

- **Inventoried → Draft** requires an actual substantive manuscript, not a proposed title.
- **Draft → Reviewed** requires a **separate scoped audit** that identifies material claim groups, authoritative sources, worked calculations, corrections and remaining uncertainties.
- **References listed → Core claims checked** requires real second-pass source/claim review rather than inserting URLs.
- **Core claims checked → Verified** requires sufficiently complete, documented claim-to-passage checking under approved criteria.
- **Reviewed or Verified → Published** requires actual canonical ownership, applicable acceptance gates, qualified independent review where required and explicit authorization.
- A historical batch's `N/N Reviewed` **does not automatically transfer** to later-added or merged subjects.

**Never self-certify final publication** from model-assisted reviews, CI, article count or user compliments. Mark unknown states truthfully.

## 13. Workflow: small coherent changes with complete reconciliation

**User-explicit sequential authoring rule (November 18, 2026): Draft batch → Review batch.** A Draft batch may contain **one or many substantive articles**, and a Review batch may assess **one or many articles**. Select batch size dynamically by conceptual coherence, source/evidence needs, available capacity and reviewability; **never impose one article per response, a fixed batch quota or symmetrical area coverage**. After delivering a Draft batch, the **next authoring-related response/execution** reviews all currently unreviewed articles from that batch (and may include additional existing Drafts), applying justified corrections, recording claim-led source/model limits, reconciling every affected status and validating the result **before starting another Draft batch**. Each article advances individually only if its own claim groups are adequately supported; unresolved articles remain **Draft**. Existing Reviewed articles with valid audits need not be reviewed again without material changes. This is a sequence and evidence requirement, not fixed counts, automatic publication approval or a demand to equalize article depths.

For a significant repository task:

1. **Read** the current root and local instructions, architecture, relevant area indexes, actual article body, inventory, ownership ledger, technical reviews and GitHub state.
2. **Select and scope** the next most valuable work. Name what is approved, proposed, excluded, missing, or uncertain. Inspect source models.
3. **Plan** enough to avoid duplicate files, wrong canonical placement, semantic regressions or destructive edits; do not overplan a trivial fix.
4. **Implement** substantive content, source correction, review work or justified architecture changes. Avoid placeholder padding and unnecessary metadata proliferation.
5. **Validate content** through source-relevant checks, exact computations, counterexamples, conceptual boundary review, and actual file/link inspection.
6. **Record review evidence** separately for newly reviewed or materially revised articles; enumerate what was checked and what was not.
7. **Reconcile** article metadata, area/division/root README indexes, subject and owner registers, historical counts and current review states.
8. **Run structural CI** where available and inspect the final job result. A queued/in-progress run is not a passing validation.
9. **Report** committed paths, source/review limitations, tests and outcome, any open decisions, and the next evidence-grounded priority.

**Reproducibility:** Use concrete tool outputs, real file paths, actual source URLs and exact review-run links. When editing with GitHub, read the latest file and use its current content SHA; avoid simultaneous updates to the same path and avoid overwriting another contributor's work.

**Efficiency:** Prefer the minimum set of coherent edits necessary to improve the real knowledge. If a big task cannot be fully completed in the present run, do meaningful verified work and state the boundary; do not substitute an ungrounded completion promise.

## 14. Change governance, versioning and technical integrity

- **Preserve historical audit files as dated evidence.** Append an explicit correction or follow-up when a later review changes the facts. Do not retrofit an old review denominator to the newest inventory.
- **Correct stale current summaries** when they conflict with the present register, actual article files or accepted decisions; mark historical sections as historical rather than silently removing them.
- **Keep inventories dynamic.** Validation must read current registered subjects, real article paths and actual counts; hardcoding a provisional count as a permanent expected value is a bug.
- **Source authority is contextual.** Latest standards do not erase historically significant sources but need accurate edition labels and supersession descriptions.
- **Maintain review granularity.** An article-specific review cannot certify a corpus, a corpus lexical scan cannot certify an article, and a technical review cannot certify user acceptance.
- **No gratuitous refactors.** Do not rename directories or move canonical pages to satisfy aesthetics without confirming approval, redirects/updated links, relationships, source states and Git history.
- **No hidden destructive work.** Follow the actual authorization boundaries and prefer reversible steps.
- **Maintain readable Markdown.** Keep informative links, stable navigation and appropriately scoped examples. Avoid excessive duplicate boilerplate across areas.

**Structural CI is mechanical.** It detects only the classes of failures the scripts actually check. It does not prove scientific truth, security effectiveness, source accuracy, system completeness or independent human publication acceptance.

## 15. Response and handoff conventions

Responses to the repository owner should be:

- **Direct, technically candid and useful.** No patronizing explanation, performative praise, unnecessary Socratic sequences or manufactured enthusiasm.
- **Evidence-specific.** Distinguish observed facts, models, derived results, unverified hypotheses, proposals, and actual approvals.
- **Narrative-first when teaching.** Use diagrams, concise comparison tables or quantitative demonstrations where they help, without rigidly repeating a template.
- **Outcome-oriented.** Summarize what was accomplished and link to the committed files, review records and passing validation when available.
- **Transparent about limitations.** Say which sources were not fully inspected and which quality gates remain open.
- **Respectful of the user's initiative and agency.** Contribute independent thought; do not decide that inferred user preferences are binding specifications when they were never approved.

### First actions on entering this repository

1. Inspect [README.md](README.md), [RELATIONSHIPS.md](RELATIONSHIPS.md) and the relevant subtree `AGENTS.md`.
2. Verify real tree structure, files and latest approvals before relying on any older conversation summary or prior audit count.
3. Determine the division/domain-specific authority and choose the correct canonical owner.
4. Consult primary sources, articulate the key concepts and uncertainties, then do the useful work with available tools.
5. Validate, reconcile, and report the **scope-limited actual result**.

**Governing standard:** *Structure follows knowledge. Depth follows complexity. Evidence governs claims. Initiative advances work. Approval remains explicit. Everything stays revisable where reality warrants it.*
