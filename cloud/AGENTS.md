# AGENTS.md | Cloud Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `cloud/` and all descendants.  
**Inherited authority:** [Root AGENTS.md](../AGENTS.md) controls evidence-led collaboration, content variability, approvals and validation. This file adds a **tailored domain SOP**, not a new taxonomy or permission to publish.  
**Navigation model:** Approved [Domain → Function → Implementation](../README.md#knowledge-domains). **Primary classification:** Cloud Service Function.  
**Status:** Substantive implementation article inventory is not yet approved or authored; the existing categories are real navigation/scope documents.

## 1. Mission and knowledge boundaries

Explain cloud-service responsibilities, resource lifecycles, control/data interfaces, deployment boundaries and implementation behavior independently of any provider's commercial catalog. A cloud-service **function** is the canonical navigation unit, not the cloud vendor or the service SKU.

**Canonical ownership:** Fundamentals owns general distributed systems, resource scheduling, APIs, state and storage principles. Security Foundations owns general trust, risk, authorization and assurance. Operational Foundations owns assessment, response and analysis methods. Identity Knowledge owns general identity/access-system functions, Network Knowledge owns transport/routing mechanisms, and Cloud Knowledge owns their **provider-specific cloud-service realization**.

The knowledge reference has **no Knowledge Checks, Practical Assessments, graded labs, exam items or mandatory course progression**. Examples and technical walkthroughs may teach, but do not silently become assessment tasks.

## 2. Approved architecture versus working plans

The [domain README](README.md) and its existing function READMEs are approved navigation scope. **Deeper subject taxonomies, implementation folders, formal graph schemas and fixed article counts are not approved merely because a contributor suggested them.**

The current tree contains the functional/secondary README skeleton and **no substantive implementation articles**. Do not report a development percentage or infer deeper coverage from the number of directories. An existing category does not imply every possible technology within it must have its own article.

The [root SOP](../AGENTS.md) applies: article depth, sections, visuals, number of subjects, work sequence and number of area-specific pages follow evidence and conceptual scope, **not symmetry or quotas**.

## 3. Existing directory and category navigation

### Primary cloud service function categories

- [Compute & Execution](compute-execution/README.md)
- [Storage & Data](storage-data/README.md)
- [Networking & Delivery](networking-delivery/README.md)
- [Identity & Access](identity-access/README.md)
- [Integration & Messaging](integration-messaging/README.md)
- [Security & Protection](security-protection/README.md)
- [Observability & Operations](observability-operations/README.md)
- [Provisioning & Governance](provisioning-governance/README.md)

### Secondary and other navigation perspectives

- [AWS](aws/README.md)
- [Microsoft Azure](azure/README.md)
- [Google Cloud](google-cloud/README.md)
- [Oracle Cloud Infrastructure](oracle-cloud/README.md)
- [IBM Cloud](ibm-cloud/README.md)
- [Other providers](other-providers/README.md)

**Interpretation:** Provider indexes describe alternate discovery routes. A specific provider service should have **one canonical implementation article under its proper cloud function** and can be linked from the provider index. AWS, Azure and GCP terms are not universal synonyms for capabilities or resource semantics.

A folder is **navigation, not automatic ontological parentage**. One subject may participate in many functions, with one canonical explanation and accurate contextual links.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Read actual function README scopes, root/SOP constraints, current domain files, relevant Fundamentals/Security/Operational Foundations, authoritative source originals and real evidence, if supplied.
2. **Derive:** Determine the actual function, entities, state, mechanism, interfaces, data, units, assumptions and boundaries; trace upstream prerequisites and downstream effects.
3. **Infer:** Test whether the claimed behavior follows from the evidence; distinguish missing knowledge, inadequate depth, duplication, unknown conditions, a proposed architecture and an approved implementation.
4. **Act:** Author useful material, fix sources, reconcile relations, conduct a bounded technical review or document a needed structural change, using available tools and actual permission.

Exercise technical initiative, propose better directions transparently, critique false claims and **do not use Socratic questioning**. Ask only when an essential requirement truly remains unresolved.

## 5. Conceptual distinctions that must survive editing

- **Cloud service / cloud provider / resource / account or tenancy boundary:** Provider branding is not a function; a region, subscription, project and identity tenant are not automatically the same isolation object.
- **Control plane / data plane / management API / service endpoint:** Resource configuration success is not proof that data processing or the deployed workload behaves as intended.
- **Compute / container / VM / managed runtime / serverless function:** Abstraction levels, persistence and operational responsibilities differ across models.
- **Region / availability zone / replication / durability / availability:** Redundant placements may share failure domains, quota dependencies or identities.
- **Object / block / file storage and data persistence:** Service durability promises, application commit semantics and successful reads have different assurance scopes.
- **Shared responsibility / actual control ownership / configuration evidence:** Provider documentation does not transfer all customer obligations or verify a deployed configuration.
- **Provider IAM / general identity proofing / application authorization:** A cloud policy decision does not prove the human actor or every downstream application permission.

Do not equate diagram, source code, service/API response, sensor reading, product marketing statement, formal model and verified real-world effect. Distinguish direct observation, recorded data, derived representation and security inference.

## 6. Technical research and source contract

Use official current AWS, Azure, Google Cloud, OCI, IBM and other provider service documentation **for the named implementation**, primary API contracts, change notices, service limits, regional availability and NIST cloud-service models where relevant. Cite exact provider, product, API version, account/resource scope and date. Never assume all providers implement one service model identically.

Identify each source's edition and applicability, model versus implementation scope, safety/security conditions, changed/deprecated semantics and any paid or unavailable full text. Prefer official specs and original authoritative engineering references over unverified summaries.

**Source support is claim-relative:** Citation existence is not claim verification. Explain limitations and counterexamples; label synthetic examples as synthetic. Never fabricate a test environment, packet capture, configuration, field measurement or security evaluation.

## 7. Authoring a substantive technical reference

Each reference develops the **actual function** rather than a vendor glossary entry or a copy of Foundations. Use narrative, mechanisms, tables, state diagrams, code or equations as needed, without uniform length or heading quotas.

A domain article should normally make clear:

- **Purpose and system boundary:** What the cloud service function does and under what relevant conditions.
- **Anatomy:** Participating components, interfaces, representations, inputs, outputs and state.
- **Mechanism:** Trace provisioning intent → control-plane operation → resource state → workload/data-plane behavior → telemetry and failure/retry paths. Distinguish declared desired state, API acknowledgment and observed resource behavior.
- **Limits and non-equivalences:** Implementation variation, failure paths, uncertainty and incorrect inferences.
- **Source/evidence:** What the primary normative source states, what example arithmetic or traces establish, and what remains unknown.
- **Cross-domain ownership:** One canonical home, links to true prerequisites and appropriately separate implementation details.

**Worked illustration to adapt, not copy mechanically:** A hypothetical object-store upload might be accepted by a service API while a consuming application still lacks authorization, consistency guarantees or replicated recoverability under its actual configuration. Distinguish request acknowledgment, stored object identity, encryption, access policy, availability and recovery claims.

Worked examples should illuminate the target concept and explicitly distinguish what is demonstrated from what is **not established**. Do not force a fixed number of examples, diagrams or sections.

## 8. Subject placement, overlap and living coverage

Use evidence-led actions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. Before making a new subject, confirm existing canonical meaning and approved scope.

**Domain placement:** Compute/hosted execution under **Compute & Execution**, object/database semantics under **Storage & Data**, messaging under **Integration & Messaging**, policy/security controls under **Identity & Access** or **Security & Protection** according to implementation function, with one canonical article linked from the provider's secondary index.

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

**Technical audit:** Check service naming and deprecations, provider-specific resource/tenant hierarchy, permission evaluation, control/data-plane API behavior, regional constraints, consistency, encryption/key assumptions, quotas, eventual state, log source limits and price/lifecycle qualifiers if mentioned.

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
4. Develop substantive service-function articles with bounded provider examples and current documentation; do not convert six provider indexes into six duplicated canonical service encyclopedias.
5. Make coherent technical changes and update related navigation, ownership, review metadata and links.
6. Validate the result with real file checks or existing CI, without extrapolating tests from other domains.
7. Report only completed work and distinguish Draft, Reviewed, Verified, Published and still-proposed architecture.

**Governing principle:** Function-first navigation. Mechanism and evidence before confident claims. Deep explanations only where warranted. Living coverage rather than fixed quotas.
