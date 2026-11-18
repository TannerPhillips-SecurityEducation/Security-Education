# AGENTS.md | Endpoint Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `endpoint/` and all descendants.  
**Inherited authority:** [Repository-wide AGENTS.md](../AGENTS.md) governs variable content, evidence, initiative, approvals, and validation. This document adds domain-specific obligations without changing the approved [Domain → Function → Implementation](../README.md#knowledge-domains) navigation.  
**Status:** Working contributor instructions, **not** a new subject taxonomy, publication decision, or mandatory technical platform.  
**Primary classification:** Host System Function. Deeper implementation and subject taxonomies remain unapproved until explicitly established.

## 1. Mission and non-negotiable boundaries

Explain host functions and concrete implementation mechanisms across operating systems, including initialization, execution, memory, storage, devices, communication, user interaction, identity enforcement and maintenance. A host function is the primary canonical home; an operating-system family is a discovery perspective.

**Scope boundary:** Fundamentals owns general processor, OS, concurrency, filesystems and memory principles. Security Foundations owns shared privilege, authentication, control and assurance meanings. Operational Foundations owns investigative, hunting and defensive procedures. Endpoint Knowledge owns actual host-function mechanisms and OS-specific semantics, not IAM systems as a whole.

This is a **technical reference** rather than an assessment or certification program. No Knowledge Checks, Practical Assessments, quizzes, graded labs, compulsory course modules, or fake deployment evidence. The root SOP's variable article length, depth, diagrams, tables, examples, and flexible subject count apply here without exception.

## 2. Approved structure versus future proposals

The [domain README](README.md) identifies the **existing approved functional navigation categories**. Their presence authorizes function-first navigation, **not** unreviewed deeper subtopics, permanent implementation directories, a fixed article count, or a formally adopted ontology.

The actual current tree contains function/category READMEs, with **no substantive implementation-reference corpus yet**. Do not invent a completion percentage or silently create one article for every possible technology.

**Canonical home:** A topic's general definition has one appropriate home. Keep alternate views pointing to that article. Proposed new function categories, merges, secondary directories, and persistent technical implementations require evidence and an applicable architectural decision.

## 3. Existing directory navigation

### Primary function categories

- [System Initialization & Boot](system-initialization-boot/README.md)
- [Execution & Scheduling](execution-scheduling/README.md)
- [Memory & Resource Management](memory-resource-management/README.md)
- [Storage & Filesystems](storage-filesystems/README.md)
- [Device & I/O Management](device-io-management/README.md)
- [Connectivity & Communication](connectivity-communication/README.md)
- [User Sessions & Interaction](user-sessions-interaction/README.md)
- [Identity & Access Enforcement](identity-access-enforcement/README.md)
- [Monitoring & Maintenance](monitoring-maintenance/README.md)

### Secondary perspectives and alternatives

- [Windows](windows/README.md)
- [Linux](linux/README.md)
- [macOS](macos/README.md)
- [Unix & BSD](unix-bsd/README.md)
- [Android](android/README.md)
- [iOS & iPadOS](ios-ipados/README.md)
- [Other & Specialized OS](other-specialized-os/README.md)

**Placement rule:** Operating-system-family indexes are **secondary**, do not own independent duplicate canonical definitions. Windows, Linux, macOS, Unix/BSD, Android, iOS/iPadOS and specialist systems may implement the same function differently. Do not automatically treat kernel ancestry, distribution and product platform as identical categories.

**Do not** mistake these directory titles for a proof that real-world systems divide into disjoint classes, or that a software, hardware or service feature has only one relationship.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Inspect the current domain index, actual function READMEs, current source specifications, related Foundations subjects, actual code/captures/configuration where supplied, and existing repository history.
2. **Derive:** Establish the unit of analysis, functional scope, interfaces, representations, state, dependencies, assumptions, relevant model types and authoritative reference boundaries.
3. **Infer:** Identify what is missing, where concepts overlap, what mechanisms are supported, which conclusions are uncertain and whether a claim describes an abstract model or a real implementation.
4. **Act:** Make the smallest valuable, justified improvement: source-grounded article, function scope refinement, traceable relationship link, reviewed architecture proposal, error correction or validation. Reconcile affected indexes and evidence.

Use the loop as a collaboration method, not an obligatory template for article headings or a replacement for actual system behavior. Avoid repetitive confirmation, Socratic questioning and unearned agreement. Challenge technical falsehoods with evidence.

## 5. Domain-specific distinctions and failure modes

- **Process / thread / task / service / execution context:** Programmer-visible semantics, runtime scheduling units and platform-specific terms must not be made equivalent without evidence.
- **Kernel / user space / driver / firmware / bootloader / hypervisor:** Distinguish layers of authority, execution and trust rather than treating all privileged code as one component.
- **Virtual memory / physical memory / page / mapping / allocation / cache / swap:** A virtual address is not an absolute physical location or proof of ownership.
- **File / filesystem / volume / mount / handle / permission:** Names, objects, metadata and enforcement mechanisms differ across operating systems.
- **Account / principal / process token / session / effective authority:** A process running with a user's credentials is not proof of which human performed an action.
- **System event / audit record / trace / performance metric:** A generated record has collection and retention boundaries and cannot represent everything the OS did.
- **Platform behavior / portable standard:** POSIX guarantees, Linux kernel behavior, Windows APIs, Apple platforms and Android lifecycle contracts have different applicability.

**Non-equivalence principle:** A name, vendor diagram, successful API command or available telemetry cannot silently stand in for a distinct function, action, observed result, security property or implementation guarantee.

## 6. Authoritative sources and evidence standards

Official OS vendor and kernel documentation, primary API and ABI specifications, current Microsoft Learn, Apple Developer, Android Developers, Linux kernel documentation, The Open Group/POSIX where applicable, source code and test results with precise versions. Historic manuals or tool output do not prove current cross-platform behavior.

For each significant claim identify **source type**, edition/version, applicable layer, context, constraints and meaningful counterexamples. Prefer current normative/primary material. A vendor's product feature is not by itself an industry standard; an old standard may be historically important but no longer current.

**Model versus evidence:** Hypothetical traces and diagrams must be labeled illustrative. Measurements require provenance, instrument placement and uncertainty as appropriate. Bibliography presence does not equal passage-level verification.

## 7. Authoring substantive function and implementation references

A technically useful article answers, in **variable and topic-appropriate depth**:

- What is the actual **host system function**, and what problem or system role does it serve?
- What structures, entities, inputs, outputs, interfaces, state and prerequisites participate?
- How does the mechanism operate? Describe what happens between an input/action and the host effect, including process boundary, privilege checks, scheduler/driver/kernel role, state transitions, observable traces and failure paths. Keep general OS theory distinct from each platform's exposed API and implementation choices.
- What assumptions, operational limits, failures and version differences matter?
- How does the relevant implementation differ from shared Fundamentals principles or general Security Foundations protections?
- What evidence supports the important claims and worked results, and what remains **Unknown**?

**Illustrative worked-case direction:** Trace a hypothetical process opening a file: process identity and authority → pathname/handle lookup → filesystem metadata and access checks → storage/page-cache interaction → result/error record. An 'access denied' result for one path is not proof that all other paths are blocked.

Use narrative technical explanations, exact diagrams, tables, traces, mathematics or code where they genuinely help. **No fixed article word count, chapter count, example count or diagrams quota.** Distinguish official requirements, derived explanations and invented examples. Link to actual canonical Foundations materials.

## 8. Knowledge gaps, granularity and scope changes

Use evidence-led dispositions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. A missing page, absent model name, thin implementation detail and genuinely absent concept demand different remedies.

**Domain-specific placement:** Define generic host execution under **Execution & Scheduling**; concrete operating-system APIs and examples live beneath the applicable function, with Windows/Linux/macOS/Android indexes linking to the same canonical destination. Separate endpoint device enforcement from the broader Identity-domain lifecycle and policy services.

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

**Domain-specific review:** Verify platform release/kernel build, API signatures, namespaces, identifiers, privilege context, access mode, error code semantics, logging settings, filesystem behavior, and test environment. Do not claim one OS's commands work unchanged on all others.

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
4. Deepen the nine existing functional scopes before creating platform-specific implementation catalogs. Prefer functional examples across multiple OSes only where verified.
5. Make one coherent technical/structural improvement; inspect real paths, links, example validity and claim limits.
6. Update navigation and review evidence without inventing architectural approvals or permanent subject quotas.
7. Report the completed work, its validation scope and remaining uncertainties.

**Governing rule:** Function before product. Evidence before confidence. Canonical ownership before duplication. Complexity determines depth. Architecture and content remain truthfully revisionable.
