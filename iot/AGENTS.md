# AGENTS.md | IoT Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `iot/` and all descendants.  
**Inherited authority:** [Root AGENTS.md](../AGENTS.md) controls evidence-led collaboration, content variability, approvals and validation. This file adds a **tailored domain SOP**, not a new taxonomy or permission to publish.  
**Navigation model:** Approved [Domain → Function → Implementation](../README.md#knowledge-domains). **Primary classification:** Device Function & Role.  
**Status:** Substantive implementation article inventory is not yet approved or authored; the existing categories are real navigation/scope documents.

## 1. Mission and knowledge boundaries

Explain connected-device functions and roles including sensing, actuation, imaging, tracking, interaction, gateway coordination, edge processing and device lifecycle. The canonical root is a **device function or role**, not a manufacturer, wireless technology or marketing device class.

**Canonical ownership:** Fundamentals owns measurement, computation, data and timing theory. Security Foundations owns general privacy/trust/control properties. Operational Foundations owns incident investigation and security work. Endpoint owns host/OS execution, Network owns transport/protocol mechanisms, Identity owns credentials, Industrial owns process-control equipment. IoT Knowledge owns **connected-device-specific realization and lifecycle constraints** across those interfaces.

The knowledge reference has **no Knowledge Checks, Practical Assessments, graded labs, exam items or mandatory course progression**. Examples and technical walkthroughs may teach, but do not silently become assessment tasks.

## 2. Approved architecture versus working plans

The [domain README](README.md) and its existing function READMEs are approved navigation scope. **Deeper subject taxonomies, implementation folders, formal graph schemas and fixed article counts are not approved merely because a contributor suggested them.**

The current tree contains the functional/secondary README skeleton and **no substantive implementation articles**. Do not report a development percentage or infer deeper coverage from the number of directories. An existing category does not imply every possible technology within it must have its own article.

The [root SOP](../AGENTS.md) applies: article depth, sections, visuals, number of subjects, work sequence and number of area-specific pages follow evidence and conceptual scope, **not symmetry or quotas**.

## 3. Existing directory and category navigation

### Primary device function & role categories

- [Sensing & Measurement](sensing-measurement/README.md)
- [Actuation & Control](actuation-control/README.md)
- [Imaging & Audio](imaging-audio/README.md)
- [Identification & Tracking](identification-tracking/README.md)
- [Human Interaction](human-interaction/README.md)
- [Gateways & Coordination](gateways-coordination/README.md)
- [Edge Computing & Automation](edge-computing-automation/README.md)
- [Device Provisioning & Maintenance](device-provisioning-maintenance/README.md)

### Secondary and other navigation perspectives

Current root-level secondary indexes are **not** approved; additional perspectives are conceptual, to be introduced only when actual content and decisions justify them.

**Interpretation:** Device class, deployment environment, connectivity, OS/runtime, energy budget and vendor ecosystem are alternative dimensions, **not extra approved root directories**. Gateways and bridges are first-class IoT components but may also implement network and identity functions with separate canonical explanations.

A folder is **navigation, not automatic ontological parentage**. One subject may participate in many functions, with one canonical explanation and accurate contextual links.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Read actual function README scopes, root/SOP constraints, current domain files, relevant Fundamentals/Security/Operational Foundations, authoritative source originals and real evidence, if supplied.
2. **Derive:** Determine the actual function, entities, state, mechanism, interfaces, data, units, assumptions and boundaries; trace upstream prerequisites and downstream effects.
3. **Infer:** Test whether the claimed behavior follows from the evidence; distinguish missing knowledge, inadequate depth, duplication, unknown conditions, a proposed architecture and an approved implementation.
4. **Act:** Author useful material, fix sources, reconcile relations, conduct a bounded technical review or document a needed structural change, using available tools and actual permission.

Exercise technical initiative, propose better directions transparently, critique false claims and **do not use Socratic questioning**. Ask only when an essential requirement truly remains unresolved.

## 5. Conceptual distinctions that must survive editing

- **Sensor transduction / measurement / sample / event / telemetry record:** A transmitted value can be stale, uncalibrated, transformed or missing.
- **Actuator command / state report / observed physical effect:** A command acknowledged over a radio is not proof of actuation.
- **Device identity / hardware identifier / user identity / cryptographic credential:** None provides the others automatically.
- **Gateway / bridge / router / broker / hub:** Roles and protocol conversions overlap, but message forwarding is not necessarily trust or semantic preservation.
- **Local edge computation / cloud inference / device automation:** Different execution boundaries affect delay, privacy, reliability and recoverability.
- **Radio range / link reliability / delivered application message / clock synchronization:** Connectivity and temporal guarantees depend on actual protocols and operating conditions.
- **Provisioning / enrollment / pairing / firmware update / revocation / decommissioning:** Different lifecycle operations with distinct trust and state transitions.

Do not equate diagram, source code, service/API response, sensor reading, product marketing statement, formal model and verified real-world effect. Distinguish direct observation, recorded data, derived representation and security inference.

## 6. Technical research and source contract

Use current IETF standards (e.g., relevant CoAP or constrained-network protocol RFCs), IEEE/industry standards when applicable, NIST IoT cybersecurity guidance, primary device/protocol documentation and measured traces with actual radio/channel/sensor context. Specify device model, firmware, power conditions, transport and deployment assumptions for implementation-level claims.

Identify each source's edition and applicability, model versus implementation scope, safety/security conditions, changed/deprecated semantics and any paid or unavailable full text. Prefer official specs and original authoritative engineering references over unverified summaries.

**Source support is claim-relative:** Citation existence is not claim verification. Explain limitations and counterexamples; label synthetic examples as synthetic. Never fabricate a test environment, packet capture, configuration, field measurement or security evaluation.

## 7. Authoring a substantive technical reference

Each reference develops the **actual function** rather than a vendor glossary entry or a copy of Foundations. Use narrative, mechanisms, tables, state diagrams, code or equations as needed, without uniform length or heading quotas.

A domain article should normally make clear:

- **Purpose and system boundary:** What the device function & role does and under what relevant conditions.
- **Anatomy:** Participating components, interfaces, representations, inputs, outputs and state.
- **Mechanism:** Follow device power/lifecycle state → sensing or command generation → local representation → gateway/transport → edge/cloud processing → user or actuator effect → confirmation/error path. Make offline operation, time skew, loss and resource limits explicit.
- **Limits and non-equivalences:** Implementation variation, failure paths, uncertainty and incorrect inferences.
- **Source/evidence:** What the primary normative source states, what example arithmetic or traces establish, and what remains unknown.
- **Cross-domain ownership:** One canonical home, links to true prerequisites and appropriately separate implementation details.

**Worked illustration to adapt, not copy mechanically:** A hypothetical temperature sensor reports 23.4 °C through a gateway. Distinguish actual ambient temperature, sensor calibration, sampling instant, encoded payload, gateway receipt, cloud storage and displayed reading. A successful message receipt does not prove current physical truth.

Worked examples should illuminate the target concept and explicitly distinguish what is demonstrated from what is **not established**. Do not force a fixed number of examples, diagrams or sections.

## 8. Subject placement, overlap and living coverage

Use evidence-led actions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. Before making a new subject, confirm existing canonical meaning and approved scope.

**Domain placement:** A sensor implementation belongs under **Sensing & Measurement**, an automated relay under **Actuation & Control**, a hub under **Gateways & Coordination**, local inference under **Edge Computing & Automation** and firmware/pairing lifecycle under **Device Provisioning & Maintenance**. Link shared networking/identity concepts instead of copying their canonical definitions.

Changes to existing approved function navigation require an explicit architectural disposition, rationale and traceable old/new mapping. Proposed implementation articles and deeper topics may be drafted **only with honest provisional status** until the relevant placement is established.

Do not defend a historical number of categories or files as an eternal requirement. Alternate lenses may link to existing articles, but should not duplicate their definitions.

## 9. File and relationship responsibilities

- [AGENTS.md](AGENTS.md) is this subtree contract, inherited from [root AGENTS.md](../AGENTS.md).
- [README.md](README.md) is current domain navigation, approved functional scope and truthful status.
- `<actual-function>/README.md` documents an approved category and **links to real articles when created**, not fictional paths.
- `<actual-function>/<subject>.md` is an **illustrative future path**, not an assertion of an existing or approved article.
- Secondary indexes and implementation views are navigational relationships to the single canonical home.
- Decision/ownership and technical-audit records, when needed, document **why**, **what** and **what evidence** a change has.

Keep the knowledge-graph links meaningful and current. Do not implement an unapproved global predicate schema or enforce an arbitrary domain-link quota.

## 10. Development, source verification and publication states

Track these **separately**: approval of function/subject placement, actual manuscript development, source-passage review, relationship review, empirical test/effect evidence and publication status.

- **Inventoried → Draft:** A substantive, correctly placed or explicitly provisional manuscript exists.
- **Draft → Reviewed (model-assisted):** A separate scoped technical review checks material claim groups, examples, source versions, counterexamples and limitations.
- **References listed → Core claims checked:** Real source-to-claim scrutiny exists; bibliography alone is insufficient.
- **Verified / Published:** Require appropriate completeness, qualified/authorized acceptance and genuine evidence. **Do not self-certify** or borrow a sibling division's review label.

A new source edition or significantly changed implementation requires reevaluation of affected claims and examples.

## 11. Domain validation and safety constraints

**Technical audit:** Check measurement units/accuracy, device firmware and hardware revisions, radio/link budgets, battery and sleep constraints, time synchronization, gateway transformations, retained/offline state, update signatures, provisioning trust, privacy exposure and physical safety consequences.

Before reporting completion check actual Markdown targets, heading fragments, index references, current approved function names and every new file's review state. Current GitHub Actions check Fundamentals and Security Foundations; **no domain-specific implementation validation workflow currently exists** for this directory. Do not claim a nonexistent CI gate.

If automation is later warranted, introduce it against actual files and intended structural properties, with living counts, read-only safety by default, and validation evidence separated from technical correctness.

## 12. Change control, authority and reporting

Read the latest file before writing; preserve contributor changes and obtain the current blob SHA for updates. Reconcile function indexes and actual article paths. Prefer small, reviewable, reversible commits. Date and source changes precisely.

Don't interpret a vendor guide, model taxonomy, assistant proposal or a green action as user-ratified canonical ownership. Distinguish observed behavior from derived result and inferred intent.

Report the actual files modified, the source/validation checks completed, remaining uncertainty and any approval still pending. Direct, evidence-led explanation and independent critique are preferred over repetitive questioning or praise.

## 13. Next-agent handoff checklist

1. Read [root SOP](../AGENTS.md), [this domain README](README.md), [relationship rules](../RELATIONSHIPS.md) and the relevant approved function READMEs.
2. Confirm the subject's canonical owner and related [Fundamentals](../foundations/fundamentals/README.md), [Security Foundations](../foundations/security-foundations/README.md) and [Operational Foundations](../foundations/operational-foundations/README.md) dependencies.
3. Consult primary source material, including versions, scope and meaningful counterexamples.
4. Develop real device-function references and gateway/lifecycle mechanics before building manufacturer or 'smart home' duplicate product catalogues.
5. Make coherent technical changes and update related navigation, ownership, review metadata and links.
6. Validate the result with real file checks or existing CI, without extrapolating tests from other domains.
7. Report only completed work and distinguish Draft, Reviewed, Verified, Published and still-proposed architecture.

**Governing principle:** Function-first navigation. Mechanism and evidence before confident claims. Deep explanations only where warranted. Living coverage rather than fixed quotas.
