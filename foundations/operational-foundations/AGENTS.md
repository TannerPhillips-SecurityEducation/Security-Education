# AGENTS.md | Operational Foundations Editorial & Engineering Contract

**Applies to:** Operational Foundations directory and all descendants.  
**Status:** **Working subtree-wide contributor/agent instructions.** The division is approved; its internal architecture, subject areas, specific practices and canonical article inventory are **not yet approved**. This file provides a method for developing them, **not approval** of a particular taxonomy.  
**Sibling contracts:** [Fundamentals AGENTS.md](../fundamentals/AGENTS.md) and [Security Foundations AGENTS.md](../security-foundations/AGENTS.md).  
**Repository convention:** [Hierarchy for navigation, knowledge graph through accurate links](../../RELATIONSHIPS.md). Explicit user direction and higher-priority instructions take precedence.

## 1. Mission and non-negotiable boundaries

[Operational Foundations](README.md) establishes **shared concepts and methods for applying security knowledge in practice** across the seven specialized technical knowledge domains. Its general unit of knowledge is an **operational method, activity, decision, evidence workflow or capability**, not a security product or one team's specific procedure.

Keep separate the repository's four knowledge responsibilities:

| Home | Primary responsibility | Example |
| --- | --- | --- |
| [Fundamentals](../fundamentals/README.md) | Domain-agnostic concepts, structures, algorithms, evidence, causal reasoning, state and systems | What correlation and causation mean |
| [Security Foundations](../security-foundations/README.md) | Cross-domain security objectives, adverse conditions, protective mechanisms, trust, threat, vulnerability, risk and assurance | What constitutes a security-relevant event or acceptable protection claim |
| **Operational Foundations** | Reusable **security-work methodologies, decisions, practices, skills and process mechanics** | How to investigate evidence, design and validate detection logic, evaluate a risk scenario or respond to an incident |
| [Specialized domains](../../README.md#knowledge-domains) | Particular domain functions and implementations | How network telemetry or endpoint data is actually captured, parsed and queried with a specific implementation |

**Do not** turn this division into a vendor playbook, a course syllabus, a named product manual, or a second generic security-concepts encyclopedia. Examples using Zeek, Wireshark, SIEMs, cloud systems or other technologies may illustrate operations, but the general methodology must remain comprehensible without relying on a specific tool.

**Exclude:** Knowledge Checks, Practical Assessments, quizzes, scored labs, certifications, fixed classroom timelines and automatic assessment taxonomies. A carefully explained case walkthrough or worked investigation is a **reference example**, not a learner assessment.

## 2. Approval boundary: what is actually settled

**Approved:** Operational Foundations exists as one of the repository's three Foundations divisions. Its [current README](README.md) states the general mission.

**Not yet approved:** The internal taxonomy, number or names of area directories, subject inventory, universal operational frameworks, practice classifications, preferred toolchains, lifecycle stages, review states for non-existent articles and any final canonical subject locations.

**Current physical baseline:** This division originally contains **only its README** (plus this newly authored AGENTS.md). Do not invent an internal architecture, area list or article-count status and present it as repository fact.

The number of areas and subjects is **intentionally unconstrained**. Build coverage from actual methodologies, professional/security-engineering sources, role-independent mechanisms and tested distinctions. Split, merge or retire potential subjects when the concepts support it. Do **not** copy Fundamentals' approved twelve-area structure or Security Foundations' proposed twelve-area/ninety-six-subject snapshot.

**No tacit approvals:** An AI suggestion, a source's chapter headings, an illustrative workflow diagram, or a committed proposal is not an authorized architectural decision. Keep working proposals explicit. Do not declare a final canonical tree or Published reference without approval and evidence.

## 3. Architecture and directory responsibilities

Unlike the mature [Fundamentals directory](../fundamentals/README.md), Operational Foundations **does not currently have an approved internal tree**. Its future directory architecture should be derived rather than cloned.

Use this uniform **responsibility architecture** as a planning pattern, creating supporting files only when there is genuine editorial work for them:

| File role | Purpose | Present status |
| --- | --- | --- |
| [README.md](README.md) | Division mission, current status, eventual real navigation | **Exists** |
| **AGENTS.md** (this file) | Scoped agent/contributor contract and boundaries | **Exists** |
| Proposed architecture / candidate inventory | Clarify definition, areas, possible subjects and evidence-grounded placement | **Not created/approved** |
| Ownership and overlap register | Distinguish practice-method owners, neighboring concepts and domain implementation owners | **Not created** |
| Development and verification register | Current subject paths, authoring state, separate source-review state and batch evidence | **Not created** |
| Substantive pilot articles | Test unapproved subject boundaries with real method descriptions, cases and references | **Not created** |
| Technical review and gap-adjudication reports | Bounded evidence for correctness, omissions, overlap and source currency | **Not created** |
| Tools / CI validation | Check actual internal links, topic IDs and evidence state once the tree grows | **Not created for this division** |

When authorized development starts, take the **mature responsibilities** from [Fundamentals](../fundamentals/ARCHITECTURE.md) and [the Security Foundations pilot approach](../security-foundations/AGENTS.md), not their exact filenames or counts. Prefer a division index, explicitly provisional architecture, versioned concept boundaries, substantive articles and review evidence.

**Do not create empty directories or placeholder subject pages simply to imitate another division.** An internal area README should describe a real coherent area and link to actual article files, not imaginary destinations.

## 4. Editorial operating loop: Observe → Derive → Infer → Act

Use this as a repeatable **working method**, not a security control framework, mandated incident-response lifecycle or formal ontology:

1. **Observe:** Inspect current repository evidence, the real operational problem, affected assets and functions, authoritative standards, telemetry/data, work products and prior decisions. State which facts are observed and which are reported.
2. **Derive:** Determine the objective, constraints, workflow stages as actually applicable, required concepts and data, prerequisites, possible actions, decision rules, output artifacts, feedback paths and source-grounded methods.
3. **Infer:** Identify the practitioner decision, plausible explanations, uncertainty, intended action and potential consequences. Distinguish hypotheses from observations, and context-dependent priorities from universal rules.
4. **Act:** Improve a coherent method/guide, document a warranted concept boundary, implement a clearly authorized writing or validation task, or produce a bounded review. Verify outputs and update any related indexes.

**Initiative is expected** in discovering useful practices, identifying omissions, making reversible documentation improvements and challenging poor reasoning. Do not claim authority for live high-impact or irreversible operations from a general editing instruction; follow the applicable authorization, operational safeguards and tool access.

Direct explanation and independent technical critique are preferred over repetitive interviews or Socratic questioning. Ask a single necessary clarification only if an essential requirement is unavailable.

## 5. Conceptual modeling and operational rigor

Operational material must distinguish **knowledge**, **skill**, **practice**, **method**, **process**, **technique**, **tool**, **role**, **decision**, **action**, **output** and **outcome**. A named activity is not automatically a role or a full process.

Examples of **plausible practices for investigation**, not an approved taxonomy, include security monitoring, alert triage, event investigation, threat hunting, threat modeling, detection engineering, vulnerability management, risk assessment, incident response, control validation, and security assurance activities. Do not turn this examples list into an inventory by fiat.

For every method, identify:

- **Purpose:** The operational objective and protected interest.
- **Entry condition:** Trigger or reason to begin, including proactive/retroactive work when relevant.
- **Scope and authority:** System boundary, data-access permissions, risk and safety constraints.
- **Inputs and evidence:** What records, models, context, telemetry or testimony are actually available; what is absent.
- **Procedure or strategy:** Decisions and transformations, their dependencies, and possible branches, not merely tool commands.
- **Validation:** How each intermediate/terminal claim can be checked; counterexamples and negative findings.
- **Outputs:** Observable deliverables such as case notes, hypotheses, decisions, evidence summaries, detections, control changes or a justified conclusion.
- **Handoffs:** Conditions for escalation, response, closure, later review and knowledge improvement.
- **Limitations:** Failure modes, bias, uncertainty, data gaps and what results do not establish.

A procedure can work **according to its own instructions** while failing the real operational goal. A complete workflow diagram does not establish that an analyst's conclusion is supported or a control action is effective.

**Reality and evidence distinctions:** Separate event occurrence, observability, actual observation, recording, selection, correlation, inference and security action. A matching detection rule is not evidence by itself of malicious intent. **Unknown is not benign.** A failed search is not proof that no event occurred.

## 6. Model- and source-first research contract

Before claiming a method is standard, correct, recommended or widely applicable:

1. Start with **current primary security guidance**, original methodology literature, official standards, technical system documentation and trustworthy empirical evidence.
2. Identify each source's **type and intended scope**: operational practice guide, normative requirement, formal model, heuristic, threat knowledge base, tool manual, industry guidance or empirical evaluation.
3. Distinguish **framework outcome categories** from a practitioner's actual actions. NIST CSF's six functions are not automatically an ordered incident-response process; ATT&CK tactics are not proof of a mandatory chronological attack sequence.
4. Prefer current final standards and explicitly identify version/date. For example, [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) is a current incident-response reference; it does not require every article to become a NIST-defined control family.
5. Connect material claims to sufficiently precise supporting text. A bibliography or widely recognized framework name does **not** prove correct application.
6. Validate any query examples, data transformations, risk calculations, timestamps, detections, conditional logic or attack-model assumptions. Use invented toy data only when clearly marked.
7. Document unavailable source text, license limits, conflicting versions and real-world applicability restrictions honestly.

Relevant cross-division source context: [Security Foundations source crosswalk](../security-foundations/ESTABLISHED-MODEL-CROSSWALK.md) and [Fundamentals observation](../fundamentals/scientific-analytical-reasoning/observation.md). Do not claim Operational Foundations inherits their review status.

## 7. Authoring contract for operational-method references

**Before authoring:** Identify whether the intended subject is a general method/practice or a specialist implementation. Compare [Fundamentals](../fundamentals/README.md), [Security Foundations](../security-foundations/README.md) and the relevant specialized domain. Confirm actual approval of placement; if unresolved, use a clearly labeled **working proposal or pilot**, not an invented canonical area.

A meaningful operational reference should develop:

1. **Title and metadata:** method/candidate ID when one is adopted, location approval state, development status, source-review state.
2. **Operational problem and purpose:** Why this method exists; which decisions and security outcomes it supports.
3. **Required concepts and prerequisites:** Scope, relevant models, data representations, system knowledge and permissions.
4. **Inputs and trust limitations:** What was measured/observed versus assumed; collection gaps and confidence.
5. **Method and mechanics:** Decisions and branching logic, analytical techniques, feedback, stopping conditions and dependencies.
6. **One well-scoped worked case:** Hypothetical or documented with appropriate citations, showing decisions, evidence, competing explanations and valid conclusions.
7. **Validation and failure modes:** How to catch false associations, missing data, flawed assumptions and ineffective action.
8. **Outputs and handoffs:** What an investigator, analyst, engineer or security practitioner produces, and how the result can be used responsibly.
9. **Adjacent methods and division boundaries:** Distinguish detection engineering from detecting, triage from investigation, threat hunting from reactive response, risk assessment from risk definition, etc.
10. **Source version, scope and limitations:** Technical references, safety/authorization constraints and unresolved uncertainties.

**Tool-neutral first.** Use product-specific illustrations **only** to show a general method's concrete application. Implementations and commands belong in their specialized domains, not repeated as multiple canonical definitions here.

**No learner assessments:** Worked cases, process traces and diagnostic walk-throughs are reference material; do not turn them into quizzes, exam questions, scored labs or certifications.

## 8. Knowledge gap, overlap and inventory change policy

**No fixed number of areas, practices, stages or reference articles.** A complete catalog must emerge from source-grounded distinction and useful subject ownership, not symmetry with either sibling division.

Use this evidence-led disposition vocabulary:

| Decision | Meaning |
| --- | --- |
| **Deepen** | Existing operational concept needs mechanisms, decision criteria, examples or evidence |
| **Add** | Important reusable cross-domain operational method has no adequate owner |
| **Split** | One method currently conflates distinct activities or decision responsibilities |
| **Merge** | Two proposed methods substantially duplicate the same purpose, inputs and mechanism |
| **Relocate** | Material belongs in general technical theory, security-concept principles or a domain implementation |
| **Cross-link** | Relevant method already exists; a practical dependency or contextual application link is missing |
| **Defer/unknown** | Available authority or evidence does not justify a stable placement |

Avoid arbitrary taxonomies of **reactive/proactive/retroactive**, investigative phases, knowledge types or classifications unless the project explicitly adopts them. They can be useful **orthogonal operational perspectives** in particular contexts; they are not automatically top-level directory names.

If an architecture decision is documented, preserve **old/new IDs**, scope and rationale, effect on existing articles, source basis, approval state, and review consequences. Do not conflate a *missing subject article* with *missing conceptual knowledge* or an absent specialized-domain link.

Add links to specialist domains incrementally as their actual content exists. No link quota, fixed practice count or universal vendor workflow.

## 9. File responsibilities and repository navigation

**Current physical layout:**

    foundations/operational-foundations/
    ├── README.md    (existing division mission)
    └── AGENTS.md    (this subtree contract)

Do not describe imagined files as present. As substantive architecture and article work begins, build only the necessary layers:

- **Governing architecture proposal:** Delimits operational methods and their relationship to established models, with explicit unapproved status.
- **Working inventory / ownership register:** Records candidate practices, method boundaries, dependencies and possible mergers.
- **Article pilot directory (if actually created):** Stores long-form working drafts without asserting canonical placement.
- **Development and verification register:** Tracks real files, state, sources, review batches and unresolved decisions.
- **Technical review and evidence files:** Capture claim-family checks, worked case validation, source versions and corrections.
- **Area README and canonical articles:** Only once internal architecture and subject ownership are explicitly approved.
- **Validation scripts and GitHub workflow:** Add when real content justifies them; check existing files, navigation and status without freezing counts.

**Use real links.** An illustrative path in a plan does not become a valid file link until it exists. Prefer a single canonical method explanation over parallel role-specific duplicates; role contexts can link to the general method and add genuinely distinct responsibilities.

## 10. Development, evidence and publication states

Track **independent axes** rather than a single completion percentage:

| Axis | Meaning |
| --- | --- |
| Architecture | Proposed, under working adjudication, or explicitly approved |
| Manuscript | Inventoried, Draft, Reviewed (model-assisted), finally Published when actually accepted |
| Source verification | Not reviewed, References listed, Core claims checked, or Verified with traceable passages |
| Method validation | Illustrative only, tested in a controlled case, or supported by real-world evidence under declared conditions |
| Relationships | Proposed, checked, or unresolved |
| Publication | Not accepted vs accepted under a declared, authorized publication process |

**Inventoried → Draft:** A real substantive manuscript has been committed.  
**Draft → Reviewed:** A separate scoped technical audit checks material claims, method mechanics, examples, decision assumptions and evidence limits.  
**References listed → Core claims checked:** Primary source and claim review exists, not merely link presence.  
**Core claims checked → Verified:** More complete, claim-to-passage evidence and acceptance criteria are documented.  
**Published:** Requires approved canonical ownership, source and relationship validation, qualified expert acceptance as applicable and actual publication authorization.

**A proposed operational method or article must not inherit Fundamentals' or Security Foundations' Reviewed statuses.** No work is "fully covered" or "approved" merely because its area was described.

## 11. Technical review and CI are different gates

**Today:** No dedicated Operational Foundations article inventory, validator or GitHub workflow exists. Do **not** fabricate one or claim CI has tested future articles. For real work, inspect actual GitHub file paths and relative links and record what was checked.

When the directory grows, create validation that reads current files rather than a baked-in number of candidate practices. Validate:

- Real article paths and heading fragments.
- Unique planning identifiers and honest approvals/statuses.
- Consistency between area/subject indexes and current manuscript files.
- Review evidence matching the promoted status.
- Existing source references as **external-link discovery only** unless their content was genuinely checked.
- No assessment artifacts or duplicate canonical definitions.

Technical audits must include source-defined method assumptions, checked decision/case examples, negative or ambiguous findings, corrections and limitations. A GitHub Actions success establishes only its tested mechanical properties; it is not professional certification, independent methodological validation or publication acceptance.

When checks fail, repair the underlying mismatch and rerun them. Do not weaken validation to claim green results. Report only **completed, commit-matched** checks.

## 12. Historical evidence, change discipline and communication

Before editing, inspect the current repository files and prior approvals. Keep files coherent, commits reviewable and changes reversible where possible. Use a current file SHA when writing through a GitHub connector; avoid conflicting edits to the same path.

Preserve dated architectural alternatives, discarded scopes and evidence decisions. If subject candidates later consolidate, retain old ID mappings rather than deleting a concept's historical record.

**Avoid false authority:** Do not write "approved workflow," "best practice," "empirically verified," "source-Verified" or "Published" without the supporting approval/evidence. A source's recommendation is guidance with defined context, not a universal operator requirement.

Exercise independent initiative in identifying important methods and challenging assumptions, but be transparent about provisional design choices. Explain disagreements and limitations clearly. Prefer useful substantive reference content to invented administrative work or inflated article counts.

## 13. Next-agent handoff checklist

1. Read [Operational Foundations README](README.md), [Foundations overview](../README.md), [repository relationships](../../RELATIONSHIPS.md), and both sibling [Fundamentals AGENTS](../fundamentals/AGENTS.md) and [Security Foundations AGENTS](../security-foundations/AGENTS.md).
2. Verify this division's **actual physical state**; do not infer an approved taxonomy, articles or CI from a proposal.
3. Investigate high-value cross-domain operational methods with authoritative source definitions and demonstrate how each differs from security concepts and domain implementations.
4. Draft an explicitly **proposed architecture or pilot** only when meaningful work supports it; document any unsettled ownership and flexible counts.
5. Write substantive operational references with worked decisions, evidence boundaries, source versions and non-equivalent neighboring activities.
6. Conduct bounded technical reviews, reconcile current state files and introduce validation as the corpus grows.
7. Report exactly what is authored, what is reviewed, what is verified, what remains proposed and what is still unknown.

**Core rule:** Understand the operational objective, distinguish method from concept and implementation, ground the decision in evidence, act within authority, test the result and preserve a truthful record.
