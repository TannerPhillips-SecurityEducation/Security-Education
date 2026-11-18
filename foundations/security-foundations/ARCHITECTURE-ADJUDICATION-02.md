# Security Foundations | Model-Grounded Architecture Adjudication 02

**Date:** November 18, 2026  
**Status:** **Working research/adjudication proposal, not ratification of an internal Security Foundations taxonomy.** The division itself is approved. This record authorizes editorial experimentation and article *pilots* in this repository, not final subject ownership or publication approval.  
**Inputs:** [94-subject working inventory v0.2](SUBJECT-INVENTORY-PROPOSAL.md), [20 established models](ESTABLISHED-MODEL-CROSSWALK.md), [25 ownership-boundary cases](OWNERSHIP-BOUNDARIES.md), [Fundamentals](../fundamentals/README.md), [Operational Foundations](../operational-foundations/README.md).  
**Change policy:** Both the **number of knowledge areas** and **number of subject headings** remain flexible. Never force symmetry with Fundamentals or preserve a number just because it was previously inventoried.

## 1. Proposed numerical reconciliation

| Measurement | Earlier working snapshot | Revised working snapshot | Status |
| --- | ---: | ---: | --- |
| Knowledge areas | 12 | **12** | Still proposed, subject to addition/split/merge/retirement |
| Candidate headings | 94 | **96** | **+4 newly scoped, −2 consolidated** |
| Existing candidate IDs retained as active | 94 | **92** | Two redundant planning IDs now have documented successors |
| New candidate IDs | 0 | **4** | Four additional distinct security-concept scopes |
| Original planning IDs preserved for audit history | 94 | **94** | Retired IDs are not erased from historical v0.2 |
| Ratified internal taxonomy | 0 | **0** | Division approval is not approval of all subject names |
| Independently human-published articles | 0 | **0** | Drafts, if authored, need technical and publication gates |

**Arithmetic:** 94 − 2 + 4 = **96 active working candidates**. Neither 96 nor twelve is a target, limit, or certification of coverage.

## 2. Consolidations that remove redundant proposed ownership

| Historical ID | Earlier concept | Revised disposition | Rationale and canonical boundaries |
| --- | --- | --- | --- |
| **SF-02-06** | Adverse consequences and affected interests | **Consolidate into SF-02-05: Adverse outcomes, consequences, and harm** | General security-specific harm, stakeholders and consequences belong in one coherent conceptual owner. **SF-05-03** separately estimates consequences *in a risk scenario*. Do not duplicate general harm definitions because different frameworks describe impact differently. |
| **SF-03-08** | Attribution and intent uncertainty | **Distribute and retire as independent heading:** actor capability/objective/intent hypotheses in **SF-03-03**; observation-to-attribution evidence and epistemic uncertainty in **SF-10-08** | Attribution is an evidentiary inference, not a distinct threat mechanism. Maintaining a second article here would duplicate SF-10-08 and tempt unsupported statements about actor identity. Record both successors because intent and evidence are not equivalent. |

This is **not removal of the concepts**. Old planning identifiers are historical aliases with explicit replacements; subsequent source verification or coverage work may reverse a consolidation with evidence.

## 3. Four distinct additions recommended for the working inventory

| New planning ID | Candidate subject / conceptual owner | Why distinct | Grounding and safety boundaries |
| --- | --- | --- | --- |
| **SF-04-08** | **Side channels, covert channels, and unintended information leakage** (Weaknesses, Vulnerabilities & Exposure) | The observable or actively exploited **leakage mechanism** needs explanation beyond ordinary exposed interfaces and exploitable flaws. A side channel and a covert channel are different mechanisms. | [NIST side-channel definition](https://csrc.nist.gov/glossary/term/side_channel); [NIST covert-channel definition](https://csrc.nist.gov/glossary/term/covert_channel). Domain-specific cache, power, EM, timing, storage and protocol implementations remain in their domains. |
| **SF-06-09** | **Access-control policy models** (Trust, Identity & Authority Principles) | Distinguishes rule structures such as DAC, MAC, RBAC and ABAC, the subject/action/object/condition relationships and decision semantics from **identification/authentication** and from enforcement implementations. | [NIST SP 800-162 ABAC (2019 updated final)](https://csrc.nist.gov/pubs/sp/800/162/upd2/final); [NIST SP 800-207 zero trust](https://csrc.nist.gov/pubs/sp/800/207/final). Avoid requiring a particular IAM product or assuming authorization implies authenticated identity. |
| **SF-08-09** | **Information-flow security and noninterference** (Secure Design & Architecture) | Distinguishes **which information can influence which observations** from decisions permitting a subject to access a resource. Classical noninterference is a model-relative property, not automatically guaranteed by MAC or encryption. | [NIST information-flow control](https://csrc.nist.gov/glossary/term/information_flow_control); [Cornell information-flow security lecture](https://www.cs.cornell.edu/courses/cs513/2005fa/MCinfo01.iflow_lecture_1.html). Formal confidentiality/integrity flow models are not assumed to hold for every physical timing channel. |
| **SF-09-09** | **Cryptographic composition and protocol security** (Cryptography & Information Protection) | Secure individual primitives do not automatically compose into an authenticated secure exchange. Nonce usage, associated-data binding, authentication, key derivation, transcript binding and replay context are separate protocol obligations. | [RFC 5116 AEAD](https://www.rfc-editor.org/info/rfc5116/), [NIST SP 800-38D GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final), [NIST SP 800-57 Pt.1 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), [RFC 9846 TLS 1.3 (2026)](https://www.rfc-editor.org/info/rfc9846/). Do not prescribe TLS or any algorithm as the universal implementation. |

**Not added as new subjects:** Cryptographic algorithm agility and quantum-resistant transitions remain planned depth in **SF-09-07 Key lifecycle and cryptographic failures**, informed by [FIPS 203/204/205](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography) and [NIST SP 800-227](https://csrc.nist.gov/pubs/sp/800/227/final). Common Criteria and NIST control-assessment criteria belong as source-grounded examples under **SF-12-01/02**, not a parallel governance taxonomy. The CIA Triad belongs as an explicitly attributed protection-objectives lens across **SF-01-03/04/05**, not an additional subject heading.

## 4. Whole-corpus coverage decision by candidate area

| Area | Revised candidate count | What the area must explain | Main gap/overlap disposition |
| --- | ---: | --- | --- |
| SF-01 Security Meaning & Objectives | **8** | Security context, CIA and broader protection properties; distinguish availability, accessibility, correctness and safety | Deepen original security-property models, no new root |
| SF-02 Protected Interests, Assets & Harm | **6** | Stakeholders, assets, interests, dependency-criticality and adverse harms | Consolidate 02-06 into 02-05; distinguish harm from risk estimation |
| SF-03 Threats, Hazards & Adversarial Behavior | **7** | Intentional/nonintentional threats, adversary capabilities, attack patterns, paths and assumptions | Retire duplicative 03-08; keep attribution-evidence with 10-08 |
| SF-04 Weaknesses, Vulnerabilities & Exposure | **8** | Flaw, vulnerability, exploitability, reachability, severity and unintended leakage | Add side/covert channel mechanisms under 04-08; avoid equating all exposure with vulnerability |
| SF-05 Security Risk & Uncertainty | **8** | Scenario, uncertainty, likelihood, consequences and treatment choices | Keep CVSS Base severity distinct from stakeholder risk; threat source ≠ risk |
| SF-06 Trust, Identity & Authority Principles | **9** | Principal, claims, trust, identification/authentication/authorization, policy decisions and zero trust assumptions | Add dedicated access-policy model subject 06-09 |
| SF-07 Security Controls & Defense Mechanisms | **8** | Safeguards, mechanisms, coverage and demonstrated effectiveness | NIST SP 800-53 is a catalog; MITRE D3FEND a defensive-knowledge ontology; neither independently verifies efficacy |
| SF-08 Secure Design & Architecture | **9** | Mediation, isolation, formal properties, design tradeoffs and noninterference | Add policy-relative information-flow models 08-09, distinct from leakage pathways 04-08 |
| SF-09 Cryptography & Information Protection | **9** | Cryptographic services, entropy, encryption, authentication, keys and protocol composition | Add composition 09-09; deepen 09-07 with algorithm agility/PQC, not a new crypto taxonomy per FIPS |
| SF-10 Security Observation & Evidence | **8** | Security event/observable/recorded distinctions, alerts, inference, evidence quality and epistemic limits | Keep observation and inference separate; no universal binary or forced five-state scale |
| SF-11 Security Failure & Resilience | **8** | Compromise, containment, degraded security, recovery and adaptation | Separate exploitation mechanism (04) from compromised state (11) |
| SF-12 Security Assurance, Governance & Accountability | **8** | Defensible assurance claims, policy obligations, governance, evaluation and ethics | Use Common Criteria and ISO 15408 as bounded evidence models; governance outcomes are not security concepts |
| **Total** | **96** | | |

## 5. Non-equivalences required in technical articles

| Distinct subjects | Why keeping them separate matters |
| --- | --- |
| Threat source / threat event / adversary / hazard | Not all events have an intentional actor, and the presence of a source does not prove occurrence |
| Weakness / vulnerability / exploitation / compromise | General flaw class, context-enabled use, actual violating action and security state have different evidence |
| Harm / likelihood / severity / scenario risk | An actual consequence is not a probabilistic risk scenario; a severity label is not the system's risk |
| Identity / authentication / authorization / policy enforcement | A represented identity, authentication proof, decision rule and enforcement action are different commitments |
| Access control / information flow / side channel / covert channel | Authorized object operations do not necessarily constrain all implicit disclosures or cooperating channels |
| Encryption / authentication / key establishment / protocol security | Successful encryption does not authenticate an endpoint or establish all replay and origin properties |
| Control existence / control behavior / measured effectiveness / assurance | A deployed control is not evidence that it satisfied an objective in the tested environment |
| Observation / record / inference / attribution | A log field may support a hypothesis but does not independently prove author, intent or timeline |
| Framework outcome / security concept / operational practice | NIST CSF outcomes, ATT&CK behavior, threat-modeling workshops and canonical security meanings have different scopes |

## 6. Source updates and verification guards

**TLS source update:** [RFC 9846 (July 2026)](https://www.rfc-editor.org/info/rfc9846/) supersedes RFC 8446 while retaining TLS 1.3, tightening key-share reuse constraints and clarifying protocol security. Do not cite RFC 8446 as the latest specification.

The source crosswalk should explicitly include:

- [NIST SP 800-63-4 (2025)](https://csrc.nist.gov/pubs/sp/800/63/4/final) for assurance terminology across identity proofing, authenticators and federation. Detailed provision and implementation remain in Identity Knowledge.
- [NIST SP 800-53 Release 5.2.0 (2025)](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls) as a current control catalog/version note, without assuming a listed safeguard is effective.
- [FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document) for Base/Threat/Environmental/Supplemental distinction; CVSS-B is severity, not organizational risk.
- [NIST SP 800-57 Rev.5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), [SP 800-90A Rev.1](https://csrc.nist.gov/pubs/sp/800/90/a/r1/final), [FIPS 197 updated 2023](https://csrc.nist.gov/pubs/fips/197/final), [SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final), [NIST PQC FIPS 203/204/205](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography), and [SP 800-227 (2025)](https://csrc.nist.gov/pubs/sp/800/227/final) for separate crypto concept scopes.
- [Common Criteria ISO/IEC 15408-1:2022](https://www.iso.org/standard/72891.html) for a technical evaluation model; certification applies to a specified **target of evaluation and evaluated security properties**, not to any unexamined deployment.
- [NIST SP 800-30 Rev.1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) for risk vocabulary and separation of adversarial/non-adversarial sources, while risk-assessment execution belongs in Operational Foundations.

These are **primary reference starting points**. Their source type and publisher-specified scope are identified, but no complete norm-by-norm verification or empirical security assertion has been performed.

## 7. Article pilots before ratifying the hierarchy

Because the proposed twelve-area architecture is not ratified, place initial substantive manuscript pilots in **`pilots/`** rather than creating their proposed area directories as though approved. Each pilot carries a candidate planning ID and its source state, with explicit links to Fundamentals and proposed neighboring subjects. The pilots are editorial content, **not finalized canonical locations**.

Recommended first pilots cover:
1. SF-01-01 Security and Insecurity (scope and protection claims)
2. SF-03-01 Threat Sources and Threat Events (adversarial/nonadversarial sources)
3. SF-04-02 Vulnerabilities and Exploitability (weakness versus exploitation)
4. SF-06-09 Access-Control Policy Models (DAC/MAC/RBAC/ABAC)
5. SF-08-09 Information-Flow Security and Noninterference
6. SF-09-09 Cryptographic Composition and Protocol Security

Add more pilots or consolidate them when actual prose reveals overlap. Do **not** represent their completion as **96/96 Reviewed**.

## 8. Deferred review and acceptance

The next step is to author those pilots with substantive definitions, worked contrasts, original technical citations and explicit model conditions. Then conduct a separate scoped technical review, check all links, and reconcile the *pilot* development register. Full claim-to-passage verification, qualified independent human review and publication acceptance remain separate gates.

**Administrative scope IDs are not formal ontology predicates, stable permanent URLs, or an approval of the internal taxonomy.** No Knowledge Checks, Practical Assessments, fixed reading order or vendor-specific mandatory tool is introduced.

[Security Foundations](README.md) · [Revised candidate inventory](SUBJECT-INVENTORY-PROPOSAL.md) · [Source crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) · [Development plan](DEVELOPMENT-PLAN.md)
