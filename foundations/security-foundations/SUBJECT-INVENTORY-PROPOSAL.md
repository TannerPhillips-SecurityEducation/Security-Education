# Security Foundations: Candidate Subject Inventory

**Working proposal:** v0.3 · November 18, 2026  
**Approved:** The Security Foundations division exists.  
**Not approved:** The twelve candidate knowledge areas and **96 active candidate subject headings** listed below. Neither count is fixed.  
**Purpose:** A reviewable concept-and-mechanism coverage map, not a committed subject taxonomy or publication record.

## Inventory interpretation

Each proposed area is a **navigation grouping**, not a claim that its members share a single ontological parent type. Titles are provisional. Descriptions mark the intended canonical focus and help prevent duplicate ownership. A heading is **not** a finished article, endorsed curriculum objective, or mandatory reading sequence. After architectural approval, approved subjects can be assigned stable canonical locations.

The proposed inventory draws boundaries between **security-specific principles** and their general mathematical, computational, scientific, or systemic prerequisites in [Fundamentals](../fundamentals/README.md); between principles and **security practices** in [Operational Foundations](../operational-foundations/README.md); and between cross-domain principles and **implemented functions** in the [seven specialized domains](../../README.md#knowledge-domains).

## Proposed subject headings


### SF-01. Security Meaning & Objectives (8 candidates)

Define the meaning, limits, and desired properties of protection.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-01-01 | Security and insecurity | Describe security as a contextual property and insecurity as failure to satisfy protection needs. |
| SF-01-02 | Security objectives and requirements | Distinguish desired properties from testable protection requirements. |
| SF-01-03 | Confidentiality and secrecy | Describe unauthorized disclosure and information-access restrictions. |
| SF-01-04 | Integrity and correctness | Distinguish unauthorized alteration from correctness and data quality. |
| SF-01-05 | Availability and accessibility | Describe intended service accessibility under specified conditions. |
| SF-01-06 | Authenticity and origin assurance | Describe warranted origin or identity claims and their limits. |
| SF-01-07 | Accountability, attribution, and non-repudiation | Distinguish responsibility, actor attribution and evidence of participation; non-repudiation claims are conditional and do not eliminate dispute. |
| SF-01-08 | Security, privacy, safety, and reliability | Separate related objectives rather than treating them as synonyms. |

### SF-02. Protected Interests, Assets & Harm (6 candidates)

Identify whose interests matter, what is protected, and what losses count.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-02-01 | Stakeholders and protection needs | Relate legitimate interests, obligations, and stakeholders to protection. |
| SF-02-02 | Assets, resources, and protected interests | Distinguish valuable assets from the interests they serve. |
| SF-02-03 | Subjects, objects, and protected actions | Identify actors, resources, actions, and protected interactions. |
| SF-02-04 | Value, criticality, and dependencies | Explain contextual importance and dependent protections. |
| SF-02-05 | Adverse outcomes, consequences, and harm | Describe effects on protected interests, stakeholders and dependencies; risk-scenario consequence estimates remain SF-05-03. |
| SF-02-07 | Protection priorities and constraints | Describe competing obligations and the conditions of acceptable protection. |

### SF-03. Threats, Hazards & Adversarial Behavior (7 candidates)

Explain potential sources of adverse events across intentional adversarial action, accidental causes, hazardous conditions, and system failures.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-03-01 | Threat sources and threat events | Distinguish a source capable of causing harm from an event it may cause. |
| SF-03-02 | Adversarial and non-adversarial threat sources | Separate intentional actors from hazardous conditions, accidental events, and system failures; not every harmful event has an adversary. |
| SF-03-03 | Capability, opportunity, and intent | Distinguish ability, circumstances, objectives, and uncertainty about intent. |
| SF-03-04 | Attacks, deception, abuse, and misuse | Describe intentional attacks, deception and social engineering alongside unauthorized or harmful uses; not every misuse is an external exploit. |
| SF-03-05 | Adversarial tactics, techniques, and procedures | Distinguish objectives, behavioral methods, and concrete executions. |
| SF-03-06 | Attack paths, stages, and dependencies | Explain sequences and conditions for multi-step adverse action. |
| SF-03-07 | Threat assumptions and models | Explain model scope and assumptions without prescribing an operational modeling workshop. |

### SF-04. Weaknesses, Vulnerabilities & Exposure (8 candidates)

Explain conditions that make adverse outcomes feasible or more likely.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-04-01 | Weaknesses and root causes | Distinguish general flaw classes from particular vulnerable instances. |
| SF-04-02 | Vulnerabilities and exploitability | Describe context-dependent ways a weakness can be used to violate protection. |
| SF-04-03 | Exposure and attack surface | Describe accessible interfaces, paths, assets, and reachable opportunities. |
| SF-04-04 | Preconditions and reachability | Explain required state, authority, location, timing, and access conditions. |
| SF-04-05 | Exploitation and security violations | Distinguish attempted exploitation, successful violation of a security property, and compromise; the broader state and consequences of compromise belong to SF-11-01. |
| SF-04-06 | Severity, exploitability, and context | Separate generic severity labels from system-specific consequences and risk. |
| SF-04-07 | Weakness chains and dependency failures | Describe interacting flaws and upstream or transitive exposure. |
| SF-04-08 | Side channels, covert channels, and unintended information leakage | Distinguish leakage inferred from side effects, deliberate hidden communication and unintended disclosure; specific hardware/protocol cases remain specialized. |

### SF-05. Security Risk & Uncertainty (8 candidates)

Reason about potential adverse outcomes and choices under incomplete information.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-05-01 | Risk, scenarios, and time horizon | Describe risk relative to a scenario, protected interest, and period. |
| SF-05-02 | Likelihood, frequency, and probability | Distinguish probabilistic quantities and avoid unsupported numerical precision. |
| SF-05-03 | Risk consequence estimation and loss | Apply harm and consequence concepts to a specified risk scenario, stakeholder and horizon; general adverse outcomes remain in SF-02-05. |
| SF-05-04 | Risk uncertainty, confidence, and assumptions | Identify uncertainty within risk scenarios, likelihoods, consequences and assumptions; evidence and attribution uncertainty belong to SF-10-08. |
| SF-05-05 | Inherent and residual risk | Compare risk under explicitly stated control and baseline assumptions. |
| SF-05-06 | Risk appetite, tolerance, and acceptance | Distinguish institutional priorities, thresholds, and accountable decisions. |
| SF-05-07 | Risk treatment and tradeoffs | Explain conceptual choices such as avoidance, reduction, transfer, or acceptance. |
| SF-05-08 | Risk dependencies and changing conditions | Describe correlated threats, cascading consequences, and changing exposure. |

### SF-06. Trust, Identity & Authority Principles (9 candidates)

Explain who or what may make claims, receive authority, and cross boundaries.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-06-01 | Trust and trust assumptions | Treat trust as a contextual reliance claim, not a universal safe/unsafe label. |
| SF-06-02 | Trust boundaries and zones | Explain changes in assumed authority and verification conditions across boundaries. |
| SF-06-03 | Principals, identities, and claims | Distinguish an acting principal, identifiers, represented identity, and assertions. |
| SF-06-04 | Identification, authentication, and authorization | Separate identification, authenticating asserted identities, and authorizing actions; implementation procedures and mechanisms belong to Identity Knowledge. |
| SF-06-05 | Privileges, permissions, and entitlements | Describe authority granted to subjects over resources. |
| SF-06-06 | Least privilege and separation of duties | Explain restrictions on scope and concentration of authority. |
| SF-06-07 | Delegation, impersonation, and confused deputies | Describe delegated authority and misuse of legitimate powers. |
| SF-06-08 | Explicit verification and zero trust principles | Clarify no implicit trust based solely on location or ownership. |
| SF-06-09 | Access-control policy models | Distinguish discretionary, mandatory, role- and attribute-based policy semantics from identity proof and enforcement implementations. |

### SF-07. Security Controls & Defense Mechanisms (8 candidates)

Explain safeguards as mechanisms that alter threats, exposure, effects, or evidence.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-07-01 | Controls, safeguards, and security functions | Distinguish desired properties, policy, defensive technique, security control, deployment and demonstrated protective effect. |
| SF-07-02 | Preventive, detective, corrective, and recovery controls | Compare intended effects without implying strict exclusivity. |
| SF-07-03 | Technical, organizational, and physical controls | Classify by implementation context and shared responsibility. |
| SF-07-04 | Defense in depth and diversity | Explain complementary layers and common-mode failures. |
| SF-07-05 | Control placement and coverage | Explain where safeguards apply and what paths remain uncovered. |
| SF-07-06 | Control bypass, failure, and evasion | Describe ways safeguards cease to supply their claimed protection. |
| SF-07-07 | Compensating controls and residual exposure | Explain alternative protections and unsatisfied requirements. |
| SF-07-08 | Control effectiveness and costs | Distinguish design intent, measured effect, and operational tradeoffs. |

### SF-08. Secure Design & Architecture (9 candidates)

Express protection goals in system structures and design constraints.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-08-01 | Security architecture and formal protection models | Distinguish architecture from explicit policy models, including classical confidentiality/integrity models, and from implementing their mechanisms. |
| SF-08-02 | Reference mediation and complete mediation | Explain how protected actions are checked against security decisions. |
| SF-08-03 | Isolation, segmentation, and containment | Distinguish separation mechanisms from their placement in specific domains. |
| SF-08-04 | Minimization and least functionality | Explain reducing exposed functionality, permissions, and complexity. |
| SF-08-05 | Secure defaults and fail-safe design | Describe defaults and failure behavior in context; avoid universal fail-closed prescriptions. |
| SF-08-06 | Designing for compromise | Explain containment, detection opportunities, and constrained damage assumptions. |
| SF-08-07 | Dependencies and supply-chain trust | Describe inherited trust and indirect protection dependencies. |
| SF-08-08 | Security requirements and design tradeoffs | Relate protection claims to performance, usability, safety, and lifecycle constraints. |
| SF-08-09 | Information-flow security and noninterference | Define restrictions on information influence and observable outputs; distinguish policy proofs from access decisions and empirical absence of leaks. |

### SF-09. Cryptography & Information Protection (9 candidates)

Explain general cryptographic protections, assumptions, and limits without prescribing implementations.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-09-01 | Cryptographic security properties and assumptions | Distinguish confidentiality, integrity, authenticity, and security models. |
| SF-09-02 | Randomness, entropy, and nonces | Explain unpredictable values, uniqueness, and misuse consequences. |
| SF-09-03 | Encryption and confidentiality | Distinguish encryption goals from authorization and secure endpoint operation. |
| SF-09-04 | Hashes and message authentication | Distinguish digest computation, keyed authentication, and integrity evidence. |
| SF-09-05 | Digital signatures and origin evidence | Explain signed-message verification and limits of signer attribution. |
| SF-09-06 | Key establishment and trust anchors | Describe how participants obtain keys and establish justified reliance. |
| SF-09-07 | Key lifecycle and cryptographic failures | Explain creation, storage, rotation, compromise, expiration, and recovery. |
| SF-09-08 | Data protection across states | Compare at rest, in transit, and in use without claiming one mechanism solves all. |
| SF-09-09 | Cryptographic composition and protocol security | Define AEAD, nonce and associated-data obligations, key binding, authentication, replay context and why individually secure primitives do not automatically establish secure protocols. |

### SF-10. Security Observation & Evidence (8 candidates)

Explain how security-relevant claims arise from incomplete, mediated observations.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-10-01 | Security-relevant events and conditions | Distinguish occurrences from enduring states and conditions of interest. |
| SF-10-02 | Observable, observed, and recorded | Separate the existence of evidence, sensing, and persistent representations. |
| SF-10-03 | Telemetry, signals, and indicators | Separate raw observations from interpretable signs of potential significance. |
| SF-10-04 | Detections, findings, and alerts | Describe security judgment artifacts without defining an operational response process. |
| SF-10-05 | Benign, anomalous, suspicious, and malicious interpretations | Distinguish baseline deviation, suspicion, and intent claims; unknown remains valid. |
| SF-10-06 | Evidence provenance and integrity | Explain source, transformation history, completeness, and authenticity of evidence. |
| SF-10-07 | False positives, false negatives, and visibility gaps | Describe errors in judgments and limitations of observing systems. |
| SF-10-08 | Evidentiary confidence, causality, and attribution limits | Distinguish recorded fact, security inference and unsupported certainty; risk-estimation confidence is treated separately in SF-05-04. |

### SF-11. Security Failure & Resilience (8 candidates)

Describe what happens when protection fails and how systems can sustain valued outcomes.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-11-01 | Compromise and loss of security | Distinguish boundary violation, adverse outcomes, and evidence of compromise. |
| SF-11-02 | Failure modes and degraded protection | Describe partial, latent, and cascading protection failures. |
| SF-11-03 | Containment and blast radius | Explain limits on propagation and damage scope. |
| SF-11-04 | Resilience, survivability, and robustness | Distinguish resistance from continued function and adaptation after stress. |
| SF-11-05 | Redundancy, diversity, and common-mode failure | Describe why duplication may or may not improve security outcomes. |
| SF-11-06 | Graceful degradation and safe failure | Balance availability with integrity, safety, and authorization constraints. |
| SF-11-07 | Recovery objectives and trusted restoration | Explain restoration goals and why recovery must establish trustworthy state. |
| SF-11-08 | Persistent compromise and adaptation | Describe how adversarial persistence changes restoration assumptions. |

### SF-12. Security Assurance, Governance & Accountability (8 candidates)

Explain grounds for security confidence and the principles governing protection decisions.

| Planning ID | Candidate subject | Intended ownership / treatment |
| --- | --- | --- |
| SF-12-01 | Security claims and assurance arguments | Tie explicit claims to assumptions, structured arguments, and supporting evidence. |
| SF-12-02 | Verification, validation, and security evaluation | Distinguish conformance to specifications from suitability for protection needs. |
| SF-12-03 | Security policies, standards, and requirements | Distinguish normative obligations from technical mechanisms and procedures. |
| SF-12-04 | Governance, ownership, and accountability | Identify who establishes objectives, authorizes risk, and answers for outcomes. |
| SF-12-05 | Compliance and effective security | Distinguish meeting stated rules from demonstrating protective outcomes. |
| SF-12-06 | Security measurement and assurance limits | Describe observable measures, uncertainty, and incomplete guarantees. |
| SF-12-07 | Continuous change and assurance decay | Explain why protection claims can become stale as systems and threats evolve. |
| SF-12-08 | Ethical, human, and societal constraints | Account for rights, harm, proportionality, and legitimate authority in protection. |

## Established-model grounding, v0.3 review

The [Established Model & Framework Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) tests all twelve candidate areas against named external models and standards, including the CIA Triad, STRIDE, Diamond Model, MITRE ATT&CK, Unified Kill Chain, Pyramid of Pain, NIST SP 800-30, classical access-control models, Zero Trust, D3FEND, NIST SP 800-160, and NIST CSF 2.0.

These sources have distinct scopes, units and limits. The crosswalk does **not ratify** the proposed structure or demonstrate completeness. The earlier 94 planning IDs remain traceable in Git history and [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md); the active working inventory now has **96 candidates** after four additions and two consolidations. In particular:

- **SF-03:** Security threats are not all adversarial; deception and social engineering require explicit coverage.
- **SF-02 versus SF-05:** Actual or possible harm to interests differs from risk-scenario consequence estimation.
- **SF-04 versus SF-11:** Exploitation mechanisms and security violations differ from subsequent compromise states and consequences.
- **SF-05 versus SF-10:** Risk-estimation uncertainty differs from uncertainty in evidence, intent and attribution.
- **SF-06 versus Identity Knowledge:** Shared authentication and authority concepts differ from identity implementation and IAM functions.
- **SF-07 versus SF-08:** Defensive controls, architecture/policy models, and demonstrated effects require separate explanations.
- **SF-09:** Sources for key management, AEAD, cryptographic composition and post-quantum transitions now inform additional conceptual treatment; claim-level verification is still needed.
- **SF-12:** NIST CSF 2.0 is a secondary mapping, not a mandate to use its six risk-management outcome functions as knowledge-area headings.

**Open architectural question:** Whether twelve areas and 96 subjects are the right grain. Neither number is fixed; no internal taxonomy approval or publication is implied.

## Versioned change log: two consolidations and four additions

[Architecture Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md) preserves the two superseded v0.2 planning IDs and their conceptual successors:

| Historical planning ID | Current owner(s) | Rationale |
| --- | --- | --- |
| SF-02-06 | **SF-02-05** | Consolidate general harm, consequences and affected interests; separate scenario risk estimates in SF-05-03 |
| SF-03-08 | **SF-03-03** and **SF-10-08** | Intent hypotheses belong to threat models; attribution claims and epistemic limits belong to security evidence |

Four active candidates were added: **SF-04-08, SF-06-09, SF-08-09, SF-09-09**. Old planning IDs remain in history, not as duplicate active article obligations. The revised **96 is not a fixed target**, and the candidate grouping is not yet ratified.

## Breadth and ownership checks

- **Not a security-domain index:** No candidate is organized around Windows, AWS, Zeek, industrial controllers, identity providers, or any other platform/product. Such applications remain in their approved domain functions.
- **Not an operations catalog:** Threat hunting, vulnerability management, penetration testing, incident response, risk-assessment workshops, detection rule development, and security monitoring workflows are operational methods. Their common underlying security *concepts* may appear here, not their procedures.
- **Not a replacement for Fundamentals:** Logic, probability, general events, generic information, computation, mathematical cryptography prerequisites, and scientific methodology keep their general canonical homes.
- **No forced equivalences:** A threat is not a vulnerability; severity is not risk; an indicator is not proof of compromise; authenticity is not automatically authorization; privacy, safety, and security are related but nonidentical; encryption is not an access-control system.
- **Interpretations need evidence:** Unknown, benign, anomalous, suspicious, and malicious can be useful distinctions, but this inventory does not impose an approved universal classification scale or equate anomaly with intent.
- **Administrative IDs only:** SF-XX-YY is a draft tracking key, not a formal graph predicate, ontology, or automatically ratified numbering system.

## Explicit approval boundary

This document is a **proposal for review**. Approval of the existing Security Foundations division does **not** approve the candidate grouping, individual subjects, their boundaries, or the 96-heading working count. Reconcile with [the governing architecture proposal](ARCHITECTURE.md), [the ownership/overlap review](OWNERSHIP-BOUNDARIES.md), and [the development plan](DEVELOPMENT-PLAN.md) before generating a canonical subject tree.

[Security Foundations index](README.md) · [Foundations](../README.md) · [Repository knowledge relationships](../../RELATIONSHIPS.md)
