# AGENTS.md | Identity Knowledge: Domain Editorial & Engineering Contract

**Applies to:** `identity/` and all descendants.  
**Inherited authority:** [Root AGENTS.md](../AGENTS.md) controls evidence-led collaboration, content variability, approvals and validation. This file adds a **tailored domain SOP**, not a new taxonomy or permission to publish.  
**Navigation model:** Approved [Domain → Function → Implementation](../README.md#knowledge-domains). **Primary classification:** Identity & Access Function.  
**Status:** Substantive implementation article inventory is not yet approved or authored; the existing categories are real navigation/scope documents.

## 1. Mission and knowledge boundaries

Explain identity registration, proofing, lifecycle, authentication, authorization, credentials and keys, federation, delegated/privileged access and governance mechanisms. Identity/access **function** is the canonical home for systems and implementations, not a directory per protocol, vendor or user persona.

**Canonical ownership:** Fundamentals owns identity as distinction, sets/relations, cryptographic mathematics and data structures. Security Foundations owns the **shared meanings** of trust, identification, authentication, authorization, access-control policy, least privilege and security assurance. Operational Foundations owns audits, access reviews and security workflow methods. Identity Knowledge owns **concrete identity proofing, registration, credentials, federation, authorization service and lifecycle implementations**, with application/cloud/endpoint contexts linked rather than duplicated.

The knowledge reference has **no Knowledge Checks, Practical Assessments, graded labs, exam items or mandatory course progression**. Examples and technical walkthroughs may teach, but do not silently become assessment tasks.

## 2. Approved architecture versus working plans

The [domain README](README.md) and its existing function READMEs are approved navigation scope. **Deeper subject taxonomies, implementation folders, formal graph schemas and fixed article counts are not approved merely because a contributor suggested them.**

The current tree contains the functional/secondary README skeleton and **no substantive implementation articles**. Do not report a development percentage or infer deeper coverage from the number of directories. An existing category does not imply every possible technology within it must have its own article.

The [root SOP](../AGENTS.md) applies: article depth, sections, visuals, number of subjects, work sequence and number of area-specific pages follow evidence and conceptual scope, **not symmetry or quotas**.

## 3. Existing directory and category navigation

### Primary identity & access function categories

- [Identity Registration & Proofing](identity-registration-proofing/README.md)
- [Identity Lifecycle Management](identity-lifecycle-management/README.md)
- [Authentication](authentication/README.md)
- [Authorization & Access Control](authorization-access-control/README.md)
- [Credential & Key Management](credential-key-management/README.md)
- [Federation & Trust](federation-trust/README.md)
- [Privileged Access & Delegation](privileged-access-delegation/README.md)
- [Identity Governance & Audit](identity-governance-audit/README.md)

### Secondary and other navigation perspectives

Current root-level secondary indexes are **not** approved; additional perspectives are conceptual, to be introduced only when actual content and decisions justify them.

**Interpretation:** Protocols, providers, directories, identity stores, business/technical roles and deployment architectures may become alternate indexes when content warrants. Do not promote a brand, authentication modality or federation protocol into an additional mandatory root taxonomy.

A folder is **navigation, not automatic ontological parentage**. One subject may participate in many functions, with one canonical explanation and accurate contextual links.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Read actual function README scopes, root/SOP constraints, current domain files, relevant Fundamentals/Security/Operational Foundations, authoritative source originals and real evidence, if supplied.
2. **Derive:** Determine the actual function, entities, state, mechanism, interfaces, data, units, assumptions and boundaries; trace upstream prerequisites and downstream effects.
3. **Infer:** Test whether the claimed behavior follows from the evidence; distinguish missing knowledge, inadequate depth, duplication, unknown conditions, a proposed architecture and an approved implementation.
4. **Act:** Author useful material, fix sources, reconcile relations, conduct a bounded technical review or document a needed structural change, using available tools and actual permission.

Exercise technical initiative, propose better directions transparently, critique false claims and **do not use Socratic questioning**. Ask only when an essential requirement truly remains unresolved.

## 5. Conceptual distinctions that must survive editing

- **Human / organization / workload / device / principal / subject / account / identifier:** A directory account is not automatic proof of a unique human.
- **Claimed identity / identity proofing / authentication / assurance level:** A verified possession factor does not establish every identity attribute.
- **Authentication / authorization / policy evaluation / enforcement:** Authentication success does not entail entitlement to every resource or correct mediation.
- **Credential / secret / cryptographic key / certificate / session token / federation assertion:** Different issuance, validation, storage and revocation semantics.
- **OAuth authorization / OpenID Connect authentication / SAML assertion / WebAuthn ceremony:** Protocol purpose and roles differ; do not equate delegated access with identity proof.
- **Role membership / policy attribute / delegation / privileged session:** Effective authority is context-dependent, may expire, and needs explicit enforcement.
- **Trust anchor / issuer / verifier / relying party / identity provider / resource server:** Trust relationship, cryptographic validity and observed user behavior are separate claims.

Do not equate diagram, source code, service/API response, sensor reading, product marketing statement, formal model and verified real-world effect. Distinguish direct observation, recorded data, derived representation and security inference.

## 6. Technical research and source contract

Use official current NIST digital identity guidelines SP 800-63 series with precise edition and scope, IETF OAuth/OIDC-related RFCs and registries as appropriate, OpenID Foundation specifications, FIDO Alliance and W3C WebAuthn, OASIS SAML standards, and authoritative OS/cloud directory provider implementation documentation. State superseded editions and protocol security caveats accurately.

Identify each source's edition and applicability, model versus implementation scope, safety/security conditions, changed/deprecated semantics and any paid or unavailable full text. Prefer official specs and original authoritative engineering references over unverified summaries.

**Source support is claim-relative:** Citation existence is not claim verification. Explain limitations and counterexamples; label synthetic examples as synthetic. Never fabricate a test environment, packet capture, configuration, field measurement or security evaluation.

## 7. Authoring a substantive technical reference

Each reference develops the **actual function** rather than a vendor glossary entry or a copy of Foundations. Use narrative, mechanisms, tables, state diagrams, code or equations as needed, without uniform length or heading quotas.

A domain article should normally make clear:

- **Purpose and system boundary:** What the identity & access function does and under what relevant conditions.
- **Anatomy:** Participating components, interfaces, representations, inputs, outputs and state.
- **Mechanism:** Trace entity proofing/enrollment → identifier/credential issuance → authentication evidence and protocol exchange → claims/assertion verification → policy decision → enforcement at the resource → audit/refresh/revocation. Not every identity system implements all stages in this order; distinguish optional features and independent trust assumptions.
- **Limits and non-equivalences:** Implementation variation, failure paths, uncertainty and incorrect inferences.
- **Source/evidence:** What the primary normative source states, what example arithmetic or traces establish, and what remains unknown.
- **Cross-domain ownership:** One canonical home, links to true prerequisites and appropriately separate implementation details.

**Worked illustration to adapt, not copy mechanically:** A hypothetical client obtains an OAuth access token and calls a protected API. Distinguish the token's issuer, audience, scope, validity, subject claim, authentication assurance when applicable, API authorization decision and actual resource enforcement. A signed token is not proof of a legitimate human action or object-level permission.

Worked examples should illuminate the target concept and explicitly distinguish what is demonstrated from what is **not established**. Do not force a fixed number of examples, diagrams or sections.

## 8. Subject placement, overlap and living coverage

Use evidence-led actions **Deepen / Add / Split / Merge / Relocate / Cross-link / Defer**. Before making a new subject, confirm existing canonical meaning and approved scope.

**Domain placement:** Enrollment under **Registration & Proofing**, credential creation/retirement under **Credential & Key Management**, federation under **Federation & Trust**, delegated privileged authority under **Privileged Access & Delegation**, and actual policy enforcement under **Authorization & Access Control**. Provider-specific products extend these functional homes rather than defining universal policies.

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

**Technical audit:** Check trust relationships, current specs/algorithms, claims and audiences, issuer keys and validity, session lifetimes, protocol roles, proofing and authentication levels, revocation semantics, recovery channels, delegated scopes, authorization context, logs/attribution and privacy implications. Never publish example real secrets or operational credentials.

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
4. Author function-first identity reference articles beginning with distinctions among proofing, authentication, authorization, federation, credential lifecycle and enforcement, with version-specific worked protocol flows.
5. Make coherent technical changes and update related navigation, ownership, review metadata and links.
6. Validate the result with real file checks or existing CI, without extrapolating tests from other domains.
7. Report only completed work and distinguish Draft, Reviewed, Verified, Published and still-proposed architecture.

**Governing principle:** Function-first navigation. Mechanism and evidence before confident claims. Deep explanations only where warranted. Living coverage rather than fixed quotas.
