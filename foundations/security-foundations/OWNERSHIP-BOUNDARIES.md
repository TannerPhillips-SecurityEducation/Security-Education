# Security Foundations: Proposed Canonical Ownership Boundaries

**Working edition:** v0.4 · November 18, 2026  
**Status:** Proposed, **not approved**. These are editorial routing recommendations, not formal knowledge-graph predicates or decisions to move existing content.

## Purpose

Prevent the future Security Foundations inventory from becoming a second copy of the approved [Fundamentals](../fundamentals/README.md) corpus or a catch-all container for domain implementations and security operations. The [Architecture Proposal](ARCHITECTURE.md) supplies the governing selection rules; the [Candidate Subject Inventory](SUBJECT-INVENTORY-PROPOSAL.md) supplies provisional navigation.

Use the [Established Security Models Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) to distinguish formal models, behavioral descriptions, heuristics, taxonomies and control catalogs before assigning subject ownership.

Security concepts may be **related** across articles without being ontologically identical. Each distinct explanation should have one canonical general home, with linked applications and distinct mechanism-specific homes. A Markdown link demonstrates navigation, **not** correctness of the claimed relationship.

## Working overlap ledger (34 cases: original 25 plus 9 evidence-led additions)

| Case | Canonical general meaning | Boundary and contextual ownership |
| --- | --- | --- |
| B-01: General events vs security events | [Fundamentals](../fundamentals/README.md) owns general event/state models. | Security Foundations owns security-relevant conditions, observables, interpretations and assertions; Operational Foundations owns incident work. |
| B-02: Identity as distinction vs acting principal | [Fundamentals](../fundamentals/README.md) owns generic identity, distinction and representation. | Security Foundations owns principal/authority/trust meanings; [Identity Knowledge](../../identity/README.md) owns proofing, authentication and IAM mechanisms. |
| B-03: Threat vs risk | Security Foundations' threat area owns potential sources and events. | Security Foundations' risk area owns scenario-specific consequences, likelihood, uncertainty and decisions; avoid treating a threat as a risk score. |
| B-04: Threat vs vulnerability | Threat area owns potential adverse acts or causes. | Weakness/exposure area owns enabling system conditions; either may exist without the other. |
| B-05: Weakness vs vulnerability | Weakness/exposure area owns generic flaw classes. | Same area owns context-dependent exploitable conditions; MITRE CWE is a reference for weakness classes, not universal vulnerability diagnosis. |
| B-06: Exposure vs attack surface | Weakness/exposure area owns both terms and their differences. | Network, cloud, application and other domains own concrete externally reachable interfaces, assets and configurations. |
| B-07: Severity vs risk | Weakness/exposure area owns generic severity and exploitability distinctions. | Risk area owns scenario- and stakeholder-dependent risk; a published severity rating is not automatically an organization's risk. |
| B-08: Intent vs behavioral evidence | Threat area owns actor motives as a conditional hypothesis. | Evidence area owns observations and limits on inferring intent; operational intelligence production belongs in Operational Foundations. |
| B-09: Security objectives vs controls | Security meaning/objectives area owns desired outcomes. | Controls area owns protective mechanisms; the presence of a control does not establish that an objective was achieved. |
| B-10: Security requirements vs policy | Security meaning/objectives area owns property-oriented goals and requirement concepts. | Assurance/governance area owns normative requirements, policy distinctions and obligations; implementation rules remain contextual. |
| B-11: Trust boundary vs architectural barrier | Trust/authority area owns meanings and assumptions of trust boundaries. | Secure architecture area owns mediation, isolation and structural enforcement; specific segmentations remain in their domain. |
| B-12: Authentication vs authorization | Trust/authority area owns the general separation. | [Identity Knowledge](../../identity/README.md) owns implementing authentication, identity services, authorization and lifecycle processes. |
| B-13: Zero trust vs network segmentation | Trust/authority area owns the security principle of no implicit trust by location alone. | Secure architecture owns system-level application; networks, identity and cloud own implementation mechanisms. |
| B-14: Cryptographic mathematics vs security claims | [Fundamentals](../fundamentals/README.md) owns general mathematics, encoding, algorithms and computation. | Cryptography/information protection area owns security properties, assumptions and failure modes; implementation in relevant domain. |
| B-15: Cryptographic keys vs IAM credentials | Cryptography area owns general purpose and limits of key establishment, secrecy, and rotation. | [Identity Knowledge](../../identity/README.md) owns credential/key management as an identity function; other domains own concrete key uses. |
| B-16: Information integrity vs evidence integrity | [Fundamentals](../fundamentals/README.md) owns general data and representation. | Cryptography area owns integrity properties; evidence area owns provenance/continuity of security evidence. |
| B-17: Monitoring vs security interpretation | Evidence area owns security-relevant observations and alert/indicator semantics. | Operational Foundations owns monitoring and triage practice; specialized domains own sensor pipelines. |
| B-18: Detection algorithm vs detection practice | [Fundamentals](../fundamentals/README.md) owns general algorithmic/statistical principles. | Evidence area owns error/coverage/uncertainty implications; Operational Foundations owns detection engineering and execution. |
| B-19: Compromise vs incident response | Failure/resilience area owns conditions and consequences of compromise. | Operational Foundations owns declaring, responding to and learning from incidents; domains own product behaviors. |
| B-20: Resilience vs continuity and recovery work | Failure/resilience area owns properties of resistance, survivability, trusted restoration. | Operational Foundations owns recovery planning and execution; specialized systems own specific failover mechanisms. |
| B-21: Assurance vs compliance | Assurance/governance area owns claims, evidence, confidence, requirements and limitations. | Operational Foundations owns assessment/audit workflows; conformity with a rule is not automatically proof of effective security. |
| B-22: Security vs privacy vs safety | Security meaning/objectives area owns their distinct foundational meanings and interactions. | Other areas and domains elaborate relevant requirements without forcing one objective to subsume all others. |
| B-23: Threat models vs modeling workshops | Threat area owns concepts, explicit assumptions and model limitations. | Operational Foundations owns performing threat-modeling activities and maintaining model artifacts. |
| B-24: Risk concepts vs risk assessment activities | Risk area owns threat scenarios, likelihood, consequence and uncertainty concepts. | Operational Foundations owns assessment processes, prioritization and treatment execution. |
| B-25: Supply-chain trust vs purchasing processes | Secure architecture area owns dependency and inherited-trust principles. | Operational Foundations owns supplier-risk processes; cloud, software, endpoint and other domains own concrete dependency mechanisms. |

| B-26: Access-control policy vs enforcement | **SF-06-09** owns generic DAC/MAC/RBAC/ABAC decision models and subject/action/object/condition semantics. | **SF-08-02** owns reference mediation as a mechanism; [Identity Knowledge](../../identity/README.md) owns actual IAM and enforcement implementations. Policy evaluation is not proof of enforcement. |
| B-27: Information-flow property vs access authorization | **SF-08-09** owns observable dependencies under a declared confidentiality/integrity flow policy, including noninterference assumptions. | **SF-06-09** owns authorization of actions; **SF-04-08** owns possible side/covert leakage pathways. An allowed read is not proof that later information flow is controlled. |
| B-28: Side channel vs covert channel | **SF-04-08** owns the distinction between unintended observable side effects enabling inference and deliberate hidden communication between cooperating parties. | Network, Endpoint, Application, Industrial and other domains own concrete measurable timing, power, cache, protocol or storage mechanisms. A model of a side channel is not evidence of an actual leak. |
| B-29: Cryptographic primitive vs composed protocol | **SF-09-09** owns general AEAD/nonce/key-binding/composition and replay-security obligations. | **SF-09-03/04/06/07** own primitive goals and key lifecycle; [Network](../../network/README.md), [Application](../../application/README.md), [Identity](../../identity/README.md) and other domains own specific protocols and deployments. Passing primitive tests is not protocol verification. |
| B-30: Consolidated harm and attribution owners | **SF-02-05** now owns general adverse outcomes, consequences and harm, with legacy SF-02-06 as an alias; **SF-03-03** owns actor-intent hypotheses. | **SF-05-03** owns estimating loss for a risk scenario; **SF-10-08** owns evidence and attribution inference, absorbing the old SF-03-08 evidence scope. Do not mistake metadata attribution for proof of actor or motive. |

| B-31: Threat/violation vs compromise vs incident handling | **SF-03/SF-04** own threat events and exploitation conditions; **SF-11-01** owns compromised state, loss of protected properties, and the difference between demonstration and suspicion. | **SF-10** owns evidence/attribution limits; [Operational Foundations](../operational-foundations/README.md) owns declaring, investigating and responding to incidents. An alert is not proof of system-wide compromise. |
| B-32: Resilience goals vs recovery objectives vs executing restoration | **SF-11-04** owns anticipate/withstand/recover/adapt, bounded survivability and robustness; **SF-11-07** owns RTO/RPO/MTD meanings and trusted-restoration requirements. | [Fundamentals](../fundamentals/README.md) owns generic reliability/feedback; [Operational Foundations](../operational-foundations/README.md) owns actual continuity planning and incident recovery. Service availability after restart does not prove security-state restoration. |
| B-33: Privacy harm vs confidentiality violation | **SF-01-08** owns the distinct protected objectives; **SF-02-05** owns harm to interests; **SF-12-08** owns rights, legitimacy and governance constraints. | A privacy violation can result from **authorized data processing**, without breach or unauthorized disclosure. Identity, Cloud, Application and other domains own implementations; privacy assessment procedures are Operational Foundations. |
| B-34: Safety and human harm vs security availability/controls | **SF-01-08** owns safety/security/reliability distinctions; **SF-12-08** owns legitimacy and human-impact constraints; **SF-11** owns resilience and purposeful degradation. | [Industrial Knowledge](../../industrial/README.md) owns sector implementations and safety instrumentation. A safe shutdown may reduce availability; security control count is not safety assurance. The applicability of ISO/IEC Guide 51 and IEC 61508 is source-specific. |

## Cross-division routing examples

| Candidate topic | Route | Rationale |
| --- | --- | --- |
| Causal inference, probability, logical implication | Fundamentals | General analytical structures used by security, not intrinsically security-specific |
| Confidentiality, threat source, exploitable weakness, least privilege, trust assumption | Security Foundations (proposed article home) | Shared security semantics, protection properties and mechanisms |
| Vulnerability prioritization process, triage, threat hunting, detection engineering, incident response | Operational Foundations | Cross-domain methods of practice; this division's detailed taxonomy remains unapproved |
| Zeek sensor/telemetry pipelines, Suricata rule engines, endpoint protection drivers | Specialized Network/Endpoint domain as appropriate | Concrete technology mechanisms and domain-specific functions |
| Authenticating a person with a device and credential | Identity domain, linked to shared authentication principles | Mechanism, protocol and lifecycle, not the definition of security authority |
| Assessing the quality of evidence from a security event | Security Foundations for concepts; Operational Foundations for procedures | Evidence meaning versus applying an investigation workflow |
| Mapping concepts to NIST CSF, ATT&CK, CWE | Secondary relationship/index | These are established external frameworks, not this repository's automatic canonical hierarchy |

## Established-model boundary checks (working, not ratified)

| Models or representations | Boundary to preserve |
| --- | --- |
| CIA versus STRIDE | Security property versus threat-identification prompts |
| Diamond Model versus ATT&CK | Four-feature intrusion-event relationship model versus evolving adversary-behavior knowledge base |
| ATT&CK versus Unified Kill Chain | Tactic/technique descriptions versus abstract cyber-attack progression; ATT&CK tactic order is not a fixed timeline |
| CWE versus CAPEC versus CVSS | Weakness class versus attack pattern versus severity scoring; no one-to-one implication or organizational risk score |
| Zero Trust versus ABAC | Architecture principles versus a particular model of policy-based authorization decisions |
| NIST SP 800-53 versus D3FEND | Control catalog versus structured defensive-technique knowledge; neither independently proves effectiveness |
| Pyramid of Pain versus evidence quality | A heuristic about adversary adaptation cost is not a reliability guarantee for an indicator or attribution claim |
| NIST CSF versus Security Foundations | Organizational risk-management outcomes are not a conceptual knowledge taxonomy |

## Deferred decisions requiring architectural review

1. **Where to split identity semantics from identity implementation:** Avoid creating a second complete IAM theory in Security Foundations. Treat the abstract principal/claim/authority concepts here; preserve the existing Identity Knowledge function tree.
2. **How far to take cryptography:** Security goals, nonce/AEAD assumptions and protocol-composition principles are shared; algorithm internals may depend on Fundamentals; concrete protocol stacks, deployment mechanisms and key infrastructure belong to domain implementations.
3. **How far to take security evidence:** Define indicators, anomalies, confidence and inferential limits; do not absorb evidence collection, SOC triage or investigation workflows.
4. **How to represent safety and privacy:** Include explicit distinctions and consequences while respecting distinct legal, ethical, and technical disciplines; no assumption all three are reducible to cybersecurity.
5. **Whether 12 provisional categories and 96 working subjects are the right grain:** Both counts can expand or contract after concept/source and overlap evidence; old IDs remain traceable under [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md).
6. **How source-specific models are represented:** Preserve NIST, MITRE and other frameworks as accurately attributed references; do not equate their taxonomies or blindly import labels.

## Acceptance conditions for a boundary

A placement can be adopted only when its proposed subject has a clear definition, purpose, exclusion cases, related canonical general concept, intended operational/divisional owner, and at least one practical cross-domain application without duplicated canonical explanation. Record unresolved collisions explicitly rather than pretending the correct home is self-evident.

**No approvals implied:** Neither these case IDs nor the descriptive relationship words form an approved ontology or machine-enforced relation vocabulary.

[Security Foundations](README.md) · [Architecture](ARCHITECTURE.md) · [Development plan](DEVELOPMENT-PLAN.md) · [Repository relationships](../../RELATIONSHIPS.md)
