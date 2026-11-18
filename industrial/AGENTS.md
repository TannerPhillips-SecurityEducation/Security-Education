# AGENTS.md | Industrial Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `industrial/` and all descendants.  
**Inherited authority:** [Root AGENTS.md](../AGENTS.md) controls evidence-led collaboration, content variability, approvals and validation. This file adds a **tailored domain SOP**, not a new taxonomy or permission to publish.  
**Navigation model:** Approved [Domain → Function → Implementation](../README.md#knowledge-domains). **Primary classification:** Industrial System Function.  
**Status:** Substantive implementation article inventory is not yet approved or authored; the existing categories are real navigation/scope documents.

## 1. Mission and knowledge boundaries

Explain industrial physical processes, instrumentation, control, automation, supervision, safety, communications, process-information systems and engineering/maintenance mechanisms. Industrial **function** is primary; industry sector, equipment class, architectural model and technology/vendor are orthogonal perspectives.

**Canonical ownership:** Fundamentals owns physics, signals, control mathematics, timing, sensor/actuator principles and general reliability. Security Foundations owns shared industrial security properties, risks and assurance concepts. Operational Foundations owns security analysis, assessment and incident methods. Industrial Knowledge owns **actual plant, controller, safety-system, industrial-protocol and supervisory implementations**, and their physical constraints.

The knowledge reference has **no Knowledge Checks, Practical Assessments, graded labs, exam items or mandatory course progression**. Examples and technical walkthroughs may teach, but do not silently become assessment tasks.

## 2. Approved architecture versus working plans

The [domain README](README.md) and its existing function READMEs are approved navigation scope. **Deeper subject taxonomies, implementation folders, formal graph schemas and fixed article counts are not approved merely because a contributor suggested them.**

The current tree contains the functional/secondary README skeleton and **no substantive implementation articles**. Do not report a development percentage or infer deeper coverage from the number of directories. An existing category does not imply every possible technology within it must have its own article.

The [root SOP](../AGENTS.md) applies: article depth, sections, visuals, number of subjects, work sequence and number of area-specific pages follow evidence and conceptual scope, **not symmetry or quotas**.

## 3. Existing directory and category navigation

### Primary industrial system function categories

- [Physical Processes & Equipment](physical-processes-equipment/README.md)
- [Instrumentation & Actuation](instrumentation-actuation/README.md)
- [Control & Automation](control-automation/README.md)
- [Supervisory Systems](supervisory-systems/README.md)
- [Safety & Protection](safety-protection/README.md)
- [Industrial Communications](industrial-communications/README.md)
- [Industrial Information Systems](industrial-information/README.md)
- [Operations & Engineering](operations-engineering/README.md)

### Secondary and other navigation perspectives

Current root-level secondary indexes are **not** approved; additional perspectives are conceptual, to be introduced only when actual content and decisions justify them.

**Interpretation:** Industry sector, equipment/component family, OT architecture, technology and vendor remain distinct possible indexes, not automatically approved root directories. Industrial Knowledge focuses on industrial systems, and broad OT may overlap other domains. Do not turn a generic 'OT' umbrella into unexplained duplicate subjects.

A folder is **navigation, not automatic ontological parentage**. One subject may participate in many functions, with one canonical explanation and accurate contextual links.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Read actual function README scopes, root/SOP constraints, current domain files, relevant Fundamentals/Security/Operational Foundations, authoritative source originals and real evidence, if supplied.
2. **Derive:** Determine the actual function, entities, state, mechanism, interfaces, data, units, assumptions and boundaries; trace upstream prerequisites and downstream effects.
3. **Infer:** Test whether the claimed behavior follows from the evidence; distinguish missing knowledge, inadequate depth, duplication, unknown conditions, a proposed architecture and an approved implementation.
4. **Act:** Author useful material, fix sources, reconcile relations, conduct a bounded technical review or document a needed structural change, using available tools and actual permission.

Exercise technical initiative, propose better directions transparently, critique false claims and **do not use Socratic questioning**. Ask only when an essential requirement truly remains unresolved.

## 5. Conceptual distinctions that must survive editing

- **Physical process / model / measured process variable / controller setpoint / actuator output:** A correct algorithm does not guarantee intended plant behavior.
- **BPCS / DCS / PLC / RTU / SCADA / HMI / safety instrumented system:** These have different control, supervisory, acquisition and independent safety responsibilities; vendor labels can overlap.
- **Safety requirement / security policy / production availability:** A safe shutdown can intentionally reduce output or service availability; none is a synonym for the other.
- **Sensor indication / calibrated measurement / engineering unit / signal conversion:** A displayed number is not proof of physical accuracy or instrument health.
- **Control-loop update period / communication delay / event timestamp:** Physical dynamics and network timing require explicit units and real constraints.
- **Industrial protocol exchange / plant state / equipment command:** Capturing an industrial network frame is not independent proof that a valve or motor moved.
- **Plant hazard / cyber vulnerability / intentional actor:** Physical hazardous consequences can arise from defects, mistakes or environment without malicious agency.

Do not equate diagram, source code, service/API response, sensor reading, product marketing statement, formal model and verified real-world effect. Distinguish direct observation, recorded data, derived representation and security inference.

## 6. Technical research and source contract

Use relevant ISA/IEC 62443 documents with their actual scope and version, IEC 61508/61511 where applicable, ISA-95 for enterprise/control integration where relevant, NIST SP 800-82 for OT security guidance, original protocol specifications and official controller/instrument documentation. Some normative standards are licensed; identify inaccessible clauses. Never guess field device limits or safety ratings.

Identify each source's edition and applicability, model versus implementation scope, safety/security conditions, changed/deprecated semantics and any paid or unavailable full text. Prefer official specs and original authoritative engineering references over unverified summaries.

**Source support is claim-relative:** Citation existence is not claim verification. Explain limitations and counterexamples; label synthetic examples as synthetic. Never fabricate a test environment, packet capture, configuration, field measurement or security evaluation.

## 7. Authoring a substantive technical reference

Each reference develops the **actual function** rather than a vendor glossary entry or a copy of Foundations. Use narrative, mechanisms, tables, state diagrams, code or equations as needed, without uniform length or heading quotas.

A domain article should normally make clear:

- **Purpose and system boundary:** What the industrial system function does and under what relevant conditions.
- **Anatomy:** Participating components, interfaces, representations, inputs, outputs and state.
- **Mechanism:** Explain physical process → sensor/transmitter → controller logic → output module/actuator → physical effect → process feedback, including equipment energy limits, delays, fail-safe states and supervision. Keep model predictions separate from measured plant behavior.
- **Limits and non-equivalences:** Implementation variation, failure paths, uncertainty and incorrect inferences.
- **Source/evidence:** What the primary normative source states, what example arithmetic or traces establish, and what remains unknown.
- **Cross-domain ownership:** One canonical home, links to true prerequisites and appropriately separate implementation details.

**Worked illustration to adapt, not copy mechanically:** For a hypothetical tank-level controller, distinguish sensed level, calibrated reading, configured setpoint, PLC logic output, motor/valve actuation and actual fluid response. A captured command does not prove equipment motion or establish safety integrity.

Worked examples should illuminate the target concept and explicitly distinguish what is demonstrated from what is **not established**. Do not force a fixed number of examples, diagrams or sections.

## 8. Subject placement, overlap and living coverage

Use evidence-led actions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. Before making a new subject, confirm existing canonical meaning and approved scope.

**Domain placement:** Real controller sequencing under **Control & Automation**, safety interlocks under **Safety & Protection**, SCADA display and supervisory commands under **Supervisory Systems**, process history under **Industrial Information Systems**, and physical pumps/valves under **Physical Processes & Equipment**. Cross-link where a single asset participates in several functions.

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

**Technical audit:** Check physical units and sign conventions, instrument calibration, timing/deadlines, safety interlock independence, plant assumptions, protocol versions, actuator saturation, failure mode, maintenance state and whether examples are simulations or actual tested evidence. Do not issue live safety-critical control instructions without explicit authorization and safeguards.

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
4. Prioritize source-grounded control-loop anatomy, safety versus security boundaries, and actual industrial communications without imposing sector or vendor folders.
5. Make coherent technical changes and update related navigation, ownership, review metadata and links.
6. Validate the result with real file checks or existing CI, without extrapolating tests from other domains.
7. Report only completed work and distinguish Draft, Reviewed, Verified, Published and still-proposed architecture.

**Governing principle:** Function-first navigation. Mechanism and evidence before confident claims. Deep explanations only where warranted. Living coverage rather than fixed quotas.
