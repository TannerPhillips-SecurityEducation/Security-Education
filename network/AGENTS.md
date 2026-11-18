# AGENTS.md | Network Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `network/` and all descendants.  
**Inherited authority:** [Repository-wide AGENTS.md](../AGENTS.md) governs variable content, evidence, initiative, approvals, and validation. This document adds domain-specific obligations without changing the approved [Domain → Function → Implementation](../README.md#knowledge-domains) navigation.  
**Status:** Working contributor instructions, **not** a new subject taxonomy, publication decision, or mandatory technical platform.  
**Primary classification:** Network Function. Deeper implementation and subject taxonomies remain unapproved until explicitly established.

## 1. Mission and non-negotiable boundaries

Explain the functions, architectures, mechanisms, protocols and implementations that move, identify, forward, transform, protect, observe and maintain communication across networks. A network function is the primary unit of navigation, not a vendor device family or a security operations discipline.

**Scope boundary:** A general communication, flow, state, timing or protocol-model definition belongs in Fundamentals. Shared threat/control/security assertions belong in Security Foundations. Threat hunting, detection engineering, incident triage and other security work methods belong in Operational Foundations. Network-specific forwarding, resolution, exchanges, interfaces, sensors and telemetry production belong here.

This is a **technical reference** rather than an assessment or certification program. No Knowledge Checks, Practical Assessments, quizzes, graded labs, compulsory course modules, or fake deployment evidence. The root SOP's variable article length, depth, diagrams, tables, examples, and flexible subject count apply here without exception.

## 2. Approved structure versus future proposals

The [domain README](README.md) identifies the **existing approved functional navigation categories**. Their presence authorizes function-first navigation, **not** unreviewed deeper subtopics, permanent implementation directories, a fixed article count, or a formally adopted ontology.

The actual current tree contains function/category READMEs, with **no substantive implementation-reference corpus yet**. Do not invent a completion percentage or silently create one article for every possible technology.

**Canonical home:** A topic's general definition has one appropriate home. Keep alternate views pointing to that article. Proposed new function categories, merges, secondary directories, and persistent technical implementations require evidence and an applicable architectural decision.

## 3. Existing directory navigation

### Primary function categories

- [Architecture & Topology](architecture-topology/README.md)
- [Infrastructure](infrastructure/README.md)
- [Communication & Protocols](communication-protocols/README.md)
- [Addressing & Naming](addressing-naming/README.md)
- [Switching & Routing](switching-routing/README.md)
- [Network Services](network-services/README.md)
- [Network Operations](network-operations/README.md)

### Secondary perspectives and alternatives

No additional provider, platform, industry, product or device-class root taxonomy is approved here. Alternate lenses may be added as documented indexes after placement review.

**Placement rule:** Topologies, network environments, media, device classes, protocol families and vendor implementations can supply alternative discovery views when justified, but none is currently an approved extra root category.

**Do not** mistake these directory titles for a proof that real-world systems divide into disjoint classes, or that a software, hardware or service feature has only one relationship.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Inspect the current domain index, actual function READMEs, current source specifications, related Foundations subjects, actual code/captures/configuration where supplied, and existing repository history.
2. **Derive:** Establish the unit of analysis, functional scope, interfaces, representations, state, dependencies, assumptions, relevant model types and authoritative reference boundaries.
3. **Infer:** Identify what is missing, where concepts overlap, what mechanisms are supported, which conclusions are uncertain and whether a claim describes an abstract model or a real implementation.
4. **Act:** Make the smallest valuable, justified improvement: source-grounded article, function scope refinement, traceable relationship link, reviewed architecture proposal, error correction or validation. Reconcile affected indexes and evidence.

Use the loop as a collaboration method, not an obligatory template for article headings or a replacement for actual system behavior. Avoid repetitive confirmation, Socratic questioning and unearned agreement. Challenge technical falsehoods with evidence.

## 5. Domain-specific distinctions and failure modes

- **Packet/frame / flow / connection / stream / transaction / session / event:** These are different observational or communication units, not synonyms or automatic one-to-one mappings.
- **Network architecture / topology / physical location / logical relationship:** A graph connection does not determine cable placement, reachability, latency or security zoning.
- **Protocol specification / implementation / packet trace:** Normative syntax, semantics and pragmatics differ from a particular stack's choices and from what a sensor actually captured.
- **Address / name / identity / route / interface:** Resolution, labeling, addressing and forwarding describe related but different mappings.
- **Control plane / data plane / management plane / telemetry plane:** Identify the modeled function and interface; avoid assuming every device has identical physical separation.
- **Packet evidence / derived network telemetry / inference / alert:** A decoded packet is not a proof of a human actor or malicious intent.
- **NSM / NTA / NDR:** Network Security Monitoring, Network Telemetry Analytics, and Network Detection and Response are useful linked security-operational perspectives, **not automatically new Network Knowledge root folders**.

**Non-equivalence principle:** A name, vendor diagram, successful API command or available telemetry cannot silently stand in for a distinct function, action, observed result, security property or implementation guarantee.

## 6. Authoritative sources and evidence standards

Relevant original IETF RFCs and Internet-Drafts when clearly labeled; IEEE 802 material as applicable; official protocol registries; verified vendor implementation manuals for explicitly named systems; measured captures/traces only with provenance, sensor placement, loss and timing assumptions. Check whether a standard is historic, updated or obsoleted.

For each significant claim identify **source type**, edition/version, applicable layer, context, constraints and meaningful counterexamples. Prefer current normative/primary material. A vendor's product feature is not by itself an industry standard; an old standard may be historically important but no longer current.

**Model versus evidence:** Hypothetical traces and diagrams must be labeled illustrative. Measurements require provenance, instrument placement and uncertainty as appropriate. Bibliography presence does not equal passage-level verification.

## 7. Authoring substantive function and implementation references

A technically useful article answers, in **variable and topic-appropriate depth**:

- What is the actual **network function**, and what problem or system role does it serve?
- What structures, entities, inputs, outputs, interfaces, state and prerequisites participate?
- How does the mechanism operate? Trace the communication or network-function lifecycle with actual units: origin → representation/encapsulation → addressing/naming → transmission/forwarding → receipt/interpretation, including error paths, timing and scope. Explain how a log record or sensor arises from activity without equating capture with complete visibility.
- What assumptions, operational limits, failures and version differences matter?
- How does the relevant implementation differ from shared Fundamentals principles or general Security Foundations protections?
- What evidence supports the important claims and worked results, and what remains **Unknown**?

**Illustrative worked-case direction:** For a hypothetical DNS query, distinguish application question, name-resolution semantics, UDP/TCP transport choices, source/destination addressing, response codes and what a capture point can establish. A successful DNS response does not by itself establish endpoint authorization or application-level trust.

Use narrative technical explanations, exact diagrams, tables, traces, mathematics or code where they genuinely help. **No fixed article word count, chapter count, example count or diagrams quota.** Distinguish official requirements, derived explanations and invented examples. Link to actual canonical Foundations materials.

## 8. Knowledge gaps, granularity and scope changes

Use evidence-led dispositions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. A missing page, absent model name, thin implementation detail and genuinely absent concept demand different remedies.

**Domain-specific placement:** Put the first reusable explanation of routing under **Switching & Routing**, name resolution under **Addressing & Naming**, transport/protocol exchanges under **Communication & Protocols**, and capture/maintenance techniques as network functions only when distinct from the cross-domain investigative method. A Zeek or Suricata implementation is contextual, not the general definition of network security.

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

**Domain-specific review:** Check stated packet/protocol field names, direction, connection semantics, RFC requirements versus optional behavior, illustrative addresses, timing, packet loss, decoding uncertainty, and protocol-version interoperability. Never invent a captured PCAP or claim complete telemetry coverage.

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
4. Build deep references from approved network-function READMEs, prioritizing precise protocol exchanges, network activity units and observability boundaries before product-specific walkthroughs.
5. Make one coherent technical/structural improvement; inspect real paths, links, example validity and claim limits.
6. Update navigation and review evidence without inventing architectural approvals or permanent subject quotas.
7. Report the completed work, its validation scope and remaining uncertainties.

**Governing rule:** Function before product. Evidence before confidence. Canonical ownership before duplication. Complexity determines depth. Architecture and content remain truthfully revisionable.
