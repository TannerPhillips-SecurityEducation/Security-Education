# Security Foundations: Governing Architecture Proposal

**Edition:** v0.4 · November 18, 2026  
**Status:** **Fundamentals-style directory organization adopted by explicit user direction**; exact security area/subject taxonomy **proposed and not ratified**  
**Approved parent:** Security Knowledge → Foundations → Security Foundations  
**Current working inventory:** [12 provisional knowledge-area directories and 96 candidate subjects](SUBJECT-INVENTORY-PROPOSAL.md), both flexible. Actual working area files, IDs and statuses are in the [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md). Directory pattern adopted; final semantic taxonomy approval remains open.  
**Repository constraints:** Hierarchy for navigation; knowledge graph through explicit links; no formal graph schema adopted; no Knowledge Checks or Practical Assessments.

## 1. Governing definition (proposed)

> **Security Foundations establishes the shared objectives, conditions, concepts, principles, mechanisms, and evidentiary relationships needed to understand security and insecurity across systems and domains.**

Security is considered relative to **a protected interest**, **a system and its environment**, **an objective or acceptable outcome**, **assumptions about relevant threats and conditions**, and **the grounds for confidence** that the objective can be met. A system is not globally or permanently "secure" just because it has a control, passes a checklist, or produces no alerts.

The division explains **what protection means, what can go wrong, how protections can work, and what justifies security claims**. It is security-specific but not vendor-, technology-, platform-, operations-, or domain-specific. It does not presume security is a property of a network alone.

## 2. Position among the three approved Foundations divisions

| Division | Governing knowledge responsibility | Illustrative canonical material |
| --- | --- | --- |
| [Fundamentals](../fundamentals/README.md) | General technical, scientific, mathematical, logical, computational and systemic concepts independent of security | Systems, identity as distinction, state, events, data, probability, logic, communication, models |
| **Security Foundations** | Shared security-specific meaning, adverse conditions, protective principles, risk concepts, trust assumptions, security evidence and assurance | Confidentiality, threat, vulnerability, attack surface, trust boundary, controls, security claims |
| [Operational Foundations](../operational-foundations/README.md) | Cross-domain *methods and activities* for applying security knowledge | Investigation, threat hunting, incident response, vulnerability management, security assessment and monitoring workflows |
| [Specialized knowledge domains](../../README.md#knowledge-domains) | Particular domain functions, mechanisms, interfaces, implementations and their constraints | Network protocols and sensor implementations, OS protections, IAM systems, cloud policies, OT controllers |

**Boundary rule:** A general event is a Fundamentals concept; a *security-relevant* event and the limits of judging it belong here; deciding whether to escalate that event through a triage workflow belongs to Operational Foundations; collecting or implementing the telemetry belongs in the applicable specialized function.

Likewise, general identity is not synonymous with authentication. Security Foundations owns the **shared conceptual distinction** between identification, authentication, authorization and authority; [Identity Knowledge](../../identity/README.md) owns the detailed identity and access functions, mechanisms and implementations.

## 3. A security-reality model (explanatory, not a formal ontology)

```text
Stakeholders and protected interests
              │ establish protection needs
              ▼
     Security objectives and requirements
              │ apply to
              ▼
       System and environment ◄──── Trust assumptions / boundaries
              │
   ┌──────────┼─────────────────────┐
   │          │                     │
   ▼          ▼                     ▼
Threats / hazards    Weaknesses and exposure    Controls / secure design
   │          │                     │
   └──────────┴─────────┬───────────┘
                        ▼
        Possible events and consequences
                        │
                        ▼
     Contextual risk under uncertainty

   Observable conditions and events
                        ▼
             Actual observations
                        ▼
            Recorded representations
                        ▼
        Evidence → Inferences → Claims
                        │
                        ▼
             Assurance and limits
```

This sketch is deliberately **not** a claim of a universal linear causal chain, a probability formula, or a deterministic ontology.

- Threat events and harmful consequences can arise from adversaries, accidents, environmental hazards, or systemic failures. An exploit of a vulnerability is **one** pathway, not a prerequisite for all losses.
- A weakness, vulnerability, exposure, an attempted attack, a confirmed compromise, and an adverse consequence are **different** propositions. A critical weakness need not imply high scenario-specific risk, and a severe consequence need not establish a particular exploit path.
- Controls may change opportunities, likelihoods, impacts, observability, recovery, or trust assumptions. No control is presumed complete, error-free, or independent from the rest of the system.
- General risk estimation involves scenario, consequences, likelihood or frequency where meaningful, uncertainty, time horizon, and decision context. **Risk = likelihood × impact** is not adopted as a universal theory or always-valid numeric operation.
- Reality, observability, observation, recording, evidence and interpretation are not interchangeable. A missing indicator does not demonstrate absence of malicious activity. Intent and attribution require inference beyond an event record.

## 4. Twelve candidate knowledge areas

The grouping is proposed navigation, **not** the approved twelve-area Fundamentals taxonomy and **not** a mandate to have twelve categories here.

| Candidate area | Distinctive question |
| --- | --- |
| 01. Security Meaning & Objectives | What must be protected, and which properties count? |
| 02. Protected Interests, Assets & Harm | Whose interests matter and what loss would be adverse? |
| 03. Threats, Hazards & Adversarial Behavior | What actors or conditions could produce unwanted events, including non-adversarial causes? |
| 04. Weaknesses, Vulnerabilities & Exposure | What conditions enable or amplify failures? |
| 05. Security Risk & Uncertainty | How might harms occur and how uncertain are our judgments? |
| 06. Trust, Identity & Authority Principles | On what grounds do entities and actions receive trust or permission? |
| 07. Security Controls & Defense Mechanisms | Which protections exist and how might they work or fail? |
| 08. Secure Design & Architecture | How are protections arranged within systems and boundaries? |
| 09. Cryptography & Information Protection | What properties can cryptographic means supply and under what assumptions? |
| 10. Security Observation & Evidence | What is observable, recorded, inferred or reasonably demonstrated? |
| 11. Security Failure & Resilience | What happens when protection fails and how can valued functions survive? |
| 12. Security Assurance, Governance & Accountability | What supports credible claims and legitimate decisions? |

Full candidate headings and working scopes appear in the [Subject Inventory Proposal](SUBJECT-INVENTORY-PROPOSAL.md). No subject articles or implementation-specific directories are created merely by this proposal.

## 4A. Established security models as primary conceptual anchors

**Architecture requirement (proposed):** The division must use **existing, accurately characterized security models, theories, technical standards, and scholarly frameworks** to develop and test its concepts. The repo shall not invent a replacement security model just to obtain symmetrical navigation categories. The [Established Model & Framework Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) is the evidence-oriented review register and source map.

The four examples below illustrate complementary scopes; they are **not a new security lifecycle**:

| Concern | Established external anchors | Distinction |
| --- | --- | --- |
| **Protection properties** | CIA Triad; classical confidentiality/integrity models | A required property differs from a mechanism and from proof that the property holds |
| **Threats and adversarial actions** | STRIDE; Diamond Model; MITRE ATT&CK; Unified Kill Chain; CAPEC | Threat class, intrusion event, tactic/technique, and ordered attack progression are different units of analysis |
| **Weakness, risk and defense** | MITRE CWE; CVSS; NIST SP 800-30; D3FEND; NIST SP 800-53; Zero Trust | Weakness, vulnerability severity, contextual risk, defensive technique, control catalog and architecture are not equivalent |
| **Observation, resilience and assurance** | Pyramid of Pain; NIST SP 800-160 Vol. 1 and Vol. 2; NIST CSF 2.0 | An indicator, inference, control claim, resilience capability and organizational outcome require distinct evidence |

**Source precedence and classification:** Use original papers and current normative documents for model definitions. Identify whether each source is a formal model, explanatory model, heuristic, taxonomy, scoring system, technical catalog, engineering guidance, or operational framework. Record publication versions and limits. A framework's authority in its own scope does not make its internal structure the approved hierarchy of Security Foundations.

**Key limits:** The CIA Triad is foundational but non-exhaustive; an ATT&CK tactic is not necessarily a temporal attack phase; the Unified Kill Chain is not an assertion that all attacks follow one sequence; CVSS Base describes severity rather than organizational risk; D3FEND does not independently establish control effectiveness; and the six NIST CSF functions are concurrent risk-management outcomes, not concept areas.

**Architectural consequence:** The working **12-area/96-subject** inventory is revisionable **in either dimension**, including additions, splits, merges, relocations and retirements. [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md) records four additions and two consolidations from the original 94-subject version. The vocabulary, assumptions and boundaries of published models can inform article scopes, but imported model categories must not automatically become new root directories or formal graph predicates.

## 5. Governing architectural requirements

### 5.1 Security specificity without domain dependence

To qualify for Security Foundations, a concept must require **security meaning** yet apply across more than one specialized knowledge domain. Platform names may be examples, never organizing principles. General mathematical, computational, scientific and systems explanations remain in Fundamentals.

### 5.2 One conceptual owner, many contextual uses

A concept has one canonical home for its **general security meaning**, while domain specialists may own genuinely different implementations and behavior. Cross-reference, do not duplicate. A directory is a navigational classification, not evidence of an "is-a" relation.

### 5.3 Explain causal and protective mechanisms

A reference must do more than name a control or threat. It should explain preconditions, actors or system elements, the relevant security property, plausible mechanisms, where the claim stops, relevant failures, and what evidence supports it.

### 5.4 Separate reality from interpretation

Record distinctions between event occurrence, observable behavior, captured data, evidence, inference and security assertion. Distinguish *unknown*, *benign*, *anomalous*, *suspicious* and *malicious* when useful without treating any one scale as a ratified repository-wide classifier. Syntax, semantics, pragmatics, content, context and inferred intent may support explanation; they are not declared equivalent triads or a new ontology.

### 5.5 Make security conditional and assessable

A general statement such as "this is secure" should be refined into a claim about **specified assets, objectives, boundaries, threats, assumptions, consequences and evidence**. Where limits or dependencies are unknown, say so. Do not equate compliance, cryptographic use, the absence of alerts, or use of a recognized framework with verified effectiveness.

### 5.6 Preserve separate protection interests

Confidentiality, integrity, availability, authenticity, accountability, safety, privacy, continuity and resilience are related but are not automatically synonyms or always co-optimized. Describe conflicts and tradeoffs rather than imposing a universal objective ordering.

### 5.7 Use standards as evidence, not as taxonomy by default

NIST CSF 2.0 supplies six *cybersecurity risk-management outcome functions*: Govern, Identify, Protect, Detect, Respond, Recover. These are **not adopted as the twelve Security Foundations knowledge-area categories**, and their naming does not replace the separate conceptual or operational responsibilities. Framework mappings may be maintained as secondary views.

MITRE ATT&CK describes observed adversary behavior; CWE describes weakness classes. Neither is an exhaustive or universal ontology of security. Use them as specific sources with explicit applicability limits.

### 5.8 Exclude assessments and hidden approvals

No Knowledge Checks, Practical Assessments, quizzes, graded labs or certification tracks. Proposed headings, relation types, source authority rules, state vocabularies and technical architecture changes are not approved merely by being placed in Markdown.

## 4B. Adopting the Fundamentals structural baseline

The repository owner explicitly selected **uniform directory organization while preserving knowledge-specific content**. [Adjudication 03](AREA-STRUCTURE-ADJUDICATION-03.md) applies the same **division → knowledge area → area `README.md` → substantive subject articles** pattern as Fundamentals. Area directories currently host fourteen reviewed working articles, while unpiloted concepts are visible as Inventoried entries in area indexes. This *structural convention* is approved; **the twelve specific area names, memberships and ninety-six current subjects remain working hypotheses, both variable**. No additional article is required merely to make area counts symmetrical.

[Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) tracks all candidates and actual article paths, while the [Working Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) records proposed semantic homes. Neither register alone ratifies a formal taxonomy.

## 5A. Living architecture, consolidation and pilot contract

This architecture is governed as **a hypothesis that must survive source-backed concept comparison**, not as a number to complete. The number and identity of **areas** and **subjects** can independently expand or contract. Proposed divisions/subjects are not automatically approved by editing an index.

The [second source-grounded adjudication](ARCHITECTURE-ADJUDICATION-02.md) consolidated **SF-02-06 into SF-02-05**, split **SF-03-08** responsibilities across **SF-03-03 and SF-10-08**, and added four conceptually distinct candidates **SF-04-08, SF-06-09, SF-08-09, SF-09-09**. The historical IDs are preserved by an explicit mapping rather than reused.

**Working article rule (revised by explicit user direction):** New substantive knowledge articles belong inside the relevant **provisional knowledge-area directory**, adjacent to its `README.md`, following the [Fundamentals baseline](../fundamentals/README.md). The organization is adopted, but the exact area/subject identities and semantic ownership remain unratified. Existing 14 substantive articles have been relocated; former [pilot paths](pilots/README.md) are compatibility aliases, not duplicate bodies. Review status and source-verification level are independent of this relocation; see [Area Structure Adjudication 03](AREA-STRUCTURE-ADJUDICATION-03.md).

**Source authority rule:** Current standards and original papers control claims within their actual scopes. [The current 30-source crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) includes authentication and access models, noninterference, leakage mechanisms, cryptographic protocols and evaluations. Cite version/date and distinguish policy models, claims, implemented mechanisms, observed outcomes and operational procedures.

## 6. Editorial contract for future canonical articles (proposed)

A candidate article should provide, as applicable:

1. **Definition and boundary:** precise security-specific meaning and non-examples.
2. **Why it matters:** protected interest, potential failure, harm or decision affected.
3. **Structure and mechanism:** actors, state, preconditions, functions, failure modes and constraints.
4. **Distinctions:** adjacent concepts that must not be conflated.
5. **Worked explanation:** a vendor-neutral scenario with explicit assumptions and plausible alternatives.
6. **Relationships:** links to canonical Fundamentals concepts, other Security Foundations articles and relevant specialized domains/operational methods.
7. **Sources and uncertainty:** primary source references for material claims, with scope, qualifications and unsupported conclusions made visible.

These facets guide article quality; they are **not** seven additional category types or mandatory identical headings.

## 7. Cross-domain applications without duplicated definitions

| Domain | Illustrative application of shared Security Foundations | Where implementation belongs |
| --- | --- | --- |
| [Network](../../network/README.md) | Trust boundaries, exposure, authenticity, communication integrity | Network functional categories and concrete protocols |
| [Endpoint](../../endpoint/README.md) | Process isolation, execution trust, privileges, persistence, compromise | Endpoint OS/function documentation |
| [Application](../../application/README.md) | Input trust, authorization, software weakness, secure defaults | Application functions and concrete implementations |
| [Cloud](../../cloud/README.md) | Shared responsibility, identity trust, control plane exposure | Cloud functions and provider-specific indexes |
| [Industrial](../../industrial/README.md) | Safety-security tradeoffs, availability, consequence, resilience | Industrial functions, devices and protocols |
| [IoT](../../iot/README.md) | Device identity, lifecycle trust, constrained protection | IoT device functions and implementations |
| [Identity](../../identity/README.md) | Authentication, authorization, identity claims, delegation | IAM functions, credential mechanisms and platforms |

These examples are intended links between concepts and contexts, **not approval of new domain categories**.

## 8. Placement and overlap decision procedure

When adding or moving material, decide in order:

1. **Is security meaning necessary?** If no, favor Fundamentals.
2. **Is this a principle or meaning versus an operational method?** Procedures and workflows belong to Operational Foundations.
3. **Does it depend on a specialized implementation or domain function?** Assign that mechanism to the relevant specialized domain.
4. **Who owns the generic definition?** Link to existing canonical content rather than copy it.
5. **What is being claimed?** Specify scope, assumptions, counterexamples, testable consequences and source evidence.
6. **Is the placement settled?** Record contested cases in the [Ownership Boundaries](OWNERSHIP-BOUNDARIES.md) proposal; do not silently ratify them.

## 9. Source orientation and applicability

Authoritative source starting points, not blanket endorsement of every proposed heading:

- [NIST SP 800-160 Vol. 1 Rev. 1: Engineering Trustworthy Secure Systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), system-level security concepts and engineering.
- [NIST SP 800-160 Vol. 2 Rev. 1: Developing Cyber-Resilient Systems](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), resilience and protection under adverse conditions.
- [NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final), threat events, vulnerabilities, consequences and uncertainty within its federal information-system scope.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), organizational cybersecurity risk-management outcomes, not a conceptual ontology.
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final), conditional trust and resource-focused security architectures.
- [NIST SP 800-63-4: Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final), an identity-specific reference rather than a universal definition of all identity.
- [MITRE CWE](https://cwe.mitre.org/about/), classes of software and hardware weakness.
- [MITRE ATT&CK](https://attack.mitre.org/resources/pre-introduction/), observed cyber-adversary behaviors.

**Verification limit:** These documents ground the *choice to investigate* candidate concepts; they have not been used here to verify every future claim or certify the candidate taxonomy.

## 9A. Required model-to-concept cross-references

For a future Security Foundations article where an established model is material, document the model's original purpose, unit of analysis, represented concepts/relations, assumptions, supported security claims, important counterexamples, primary source/version, and explicit non-equivalences with adjacent models. An external model may inform multiple candidate areas; that is a **cross-link**, not duplicate conceptual ownership.

Durable canonical publication still depends on ratifying the relevant subject placement. **Before that ratification, substantive working articles are authored directly within [the provisional area directories](README.md#working-knowledge-areas), with each area `README.md` listing all candidate subjects and existing articles.** The [historical pilot register](pilots/README.md) preserves old links. The current [working inventory](SUBJECT-INVENTORY-PROPOSAL.md) records four additions and two consolidations from an earlier baseline and remains revisionable.

## 10. Architectural acceptance boundary

**Already approved:** Security Foundations as an independent division alongside Fundamentals and Operational Foundations, the seven specialized knowledge domains, the domain/function/implementation navigation policy, and repository exclusion of Knowledge Checks and Practical Assessments.

**Proposed, not approved:** This governing definition's precise wording, the twelve-area grouping, the **96 working candidate subjects**, their ownership decisions, article editorial contract, and any proposed publication gates. Neither 12 nor 96 is a quota. Architecture approval is distinct from technical review of future articles.

Next: evaluate [Ownership Boundaries](OWNERSHIP-BOUNDARIES.md) and [Development Plan](DEVELOPMENT-PLAN.md); decide the candidate taxonomy and contested overlaps; only then build the canonical article hierarchy.

[Security Foundations index](README.md) · [Candidate subjects](SUBJECT-INVENTORY-PROPOSAL.md) · [Foundations](../README.md) · [Knowledge relationships](../../RELATIONSHIPS.md)
