# Security Foundations: Established Models, Frameworks, and Evidence Crosswalk

**Working edition:** v0.3 · November 18, 2026  
**Status:** Research-backed **architectural review aid**, not ratification of the Security Foundations taxonomy or model choices.  
**Input inventory:** [12 candidate areas / 96 active candidate subjects (v0.3)](SUBJECT-INVENTORY-PROPOSAL.md); historical 94-ID snapshot in Git.  
**Purpose:** Derive concept coverage and boundaries from existing security scholarship and primary technical references instead of inventing an independent security theory.

## 1. Governing rule: models before taxonomic commitments

The approved Security Foundations division should be built from **established meanings, properties, mechanisms and scholarly models**. The twelve navigation areas and their 96 active subject titles are provisional hypotheses about organizing that knowledge, not evidence of conceptual completeness.

A published standard, a scientific model, a classification taxonomy, an engineering principle, a technique catalog and an operational framework have **different authorities and purposes**. No single reference is a universal theory of security.

### Types of established knowledge sources

| Source type | Function | Avoid claiming |
| --- | --- | --- |
| **Formal security model** | Defines subjects, objects, state, transitions or permitted behavior under explicit assumptions | That the model covers every real-world threat or system |
| **Explanatory/analytical model** | Represents aspects of security activity, relationships, causes or progression | That modeled structure is a guaranteed causal history |
| **Heuristic** | Guides comparative reasoning or prioritization under stated assumptions | That it is a proven universal quantitative law |
| **Taxonomy / knowledge base** | Names, distinguishes and links classes of behavior, weaknesses or techniques | That the list is exhaustive, immutable or an ontology of all security |
| **Scoring system** | Summarizes chosen attributes under a declared calculation | That a score alone measures organizational risk |
| **Technical catalog** | Describes families of controls, mitigations or testable requirements | That applying catalog entries guarantees effectiveness |
| **Engineering framework / guidance** | Provides architecture, objectives, principles or structured decision support | That implementation activities are universal concept categories |
| **Operational methodology** | Organizes activities performed by practitioners | That the workflow belongs as the canonical definition of a security concept |

These labels are **editorial source distinctions**, not approved knowledge-graph predicate types.

## 2. Primary model and framework register

The planning IDs here are references for **this document only**; they are not proposed Security Foundations subject headings.

| Reference | Type | What it offers | Security Foundations candidate ownership | Primary or authoritative starting point and limitation |
| --- | --- | --- | --- | --- |
| R-01 CIA Triad | Security property model | Confidentiality, integrity, availability as foundational information-security objectives | SF-01-01–05; SF-01-08 | [NIST information security glossary](https://csrc.nist.gov/glossary/term/information_security). Does not exhaust safety, privacy, authenticity or all system security goals |
| R-02 Bell–LaPadula and Biba | Classical formal policy models | Distinct confidentiality- and integrity-oriented mandatory policy reasoning | SF-01-03–04; SF-08-01–02 | [NIST historic security-model literature entry point](https://csrc.nist.gov/publications/history). **Primary-paper and version-specific formal claims need a dedicated source pass**; do not reduce these models to universal slogans |
| R-03 STRIDE | Threat-identification mnemonic / model | Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege | SF-03-04/07; SF-01-03–07; SF-08-01 | [Microsoft threat-modeling reference](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), [OWASP threat-modeling guidance](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html). Strong for technical designs; not exhaustive of all harms |
| R-04 Attack Trees | Goal-decomposition model | Alternative and conjunctive attack paths rooted in a particular adverse goal | SF-03-06–07; SF-04-04/07 | [OWASP threat-modeling guidance](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html). Proposed paths are hypotheses unless verified |
| R-05 Diamond Model of Intrusion Analysis | Event-oriented intrusion-analysis model | Relates adversary, infrastructure, capability, and victim within an intrusion event | SF-03-03/07; SF-10-01/08 | [Original publication information](https://www.activeresponse.org/publications/); [model overview](https://www.threatintel.academy/diamond/). **An intrusion event model**, not a model of every hazard or a proof of attribution |
| R-06 MITRE ATT&CK | Observation-based adversary-behavior knowledge base | Tactics as adversary goals, techniques/sub-techniques as ways of acting | SF-03-05–07; SF-10-03–05 | [MITRE ATT&CK Get Started](https://attack.mitre.org/resources/enterprise-introduction/). Evolving platform-specific behavior knowledge; not a mandatory chronological attack chain |
| R-07 Unified Kill Chain | Cyber-attack progression model | Tactical phases, including Getting In, Hacking Through and Taking It Out | SF-03-05–07; SF-11-08 | [Unified Kill Chain official site](https://www.unifiedkillchain.com/). Abstract progression; actual attacks can branch, repeat, omit or reorder actions |
| R-08 Pyramid of Pain | Detection-value heuristic | Types of indicators and expected adversarial effort when indicators are denied | SF-10-03–05; SF-03-05; SF-07-08 | [Original 2013 Pyramid of Pain explanation](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html). Not a measured universal cost scale or proof that one detection is effective |
| R-09 MITRE CWE | Weakness-class taxonomy | Common software/hardware weakness classes and relationships | SF-04-01–02/07 | [MITRE CWE about](https://cwe.mitre.org/about/). A weakness class is not an automatically exploitable vulnerability in a particular target |
| R-10 MITRE CAPEC | Attack-pattern knowledge base | Reusable methods and patterns of attacks that exploit weaknesses | SF-03-04–06; SF-04-04–05 | [MITRE CAPEC](https://capec.mitre.org/). Attack patterns are not identical to an observed ATT&CK technique or a specific incident |
| R-11 CVSS v4.0 | Vulnerability-severity scoring framework | Base, Threat, Environmental and Supplemental metrics describing a vulnerability | SF-04-06; SF-05-03–05 | [FIRST CVSS v4 user guide](https://www.first.org/cvss/user-guide). **CVSS-B measures severity, not organizational risk** |
| R-12 NIST SP 800-30 Rev. 1 | Risk-analysis concepts and guidance | Threat sources/events, vulnerabilities, predisposing conditions, likelihood and adverse impact | SF-02-05; SF-03-01–02; SF-04-01–04; SF-05-01–08 | [Final NIST risk-assessment guidance](https://csrc.nist.gov/pubs/sp/800/30/r1/final). U.S. federal information-system/organization focus; risk-assessment *activities* route to Operational Foundations |
| R-13 NIST SP 800-162 ABAC | Access-control model / guidance | Subject, object, requested operation and environment attributes evaluated under policy | SF-06-03–07/09; SF-08-02 | [Updated final NIST ABAC reference](https://csrc.nist.gov/pubs/sp/800/162/upd2/final). Details of identity provisioning and IAM products remain in Identity Knowledge |
| R-14 NIST SP 800-207 Zero Trust | Security architecture principles | No implicit trust based solely on network location or asset ownership; resource-centered decisions | SF-06-01–02/08; SF-08-01–03 | [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final). Not the assertion that no entity can ever be trusted |
| R-15 MITRE D3FEND | Defensive-technique ontology / knowledge graph | Describes defensive countermeasures and links to offensive behaviors | SF-07-01–07; SF-08-01–06 | [MITRE D3FEND](https://d3fend.mitre.org/about/), [D3FEND FAQ](https://next.d3fend.mitre.org/faq/). It **does not** prescribe priorities or characterize effectiveness |
| R-16 NIST SP 800-53 Rev. 5 | Security/privacy control catalog | Broad families of safeguards and control statements | SF-07-01–08; SF-12-03–05 | [NIST SP 800-53 Release 5.2.0](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls). Catalog entries are not proof of implemented or effective controls; the 800-53A assessment procedures have their own purpose |
| R-17 NIST SP 800-160 Vol. 1 Rev. 1 | Systems security engineering guidance | Stakeholder protection needs, requirements, trustworthiness, engineering and assurance | SF-01/02/07/08/12 | [Final NIST systems security engineering guidance](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final). Engineering *processes* are operational, not all Security Foundations navigation areas |
| R-18 NIST SP 800-160 Vol. 2 Rev. 1 | Cyber-resiliency engineering framework | Anticipate, withstand, recover, adapt to adverse cyber conditions | SF-07-04–07; SF-08-06; SF-11-01–08 | [Final NIST cyber-resiliency guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final). Resilience properties differ from incident-response procedures |
| R-19 NIST CSF 2.0 | Organizational risk-management outcome framework | Govern, Identify, Protect, Detect, Respond, Recover | SF-12-03–07; cross-references throughout | [NIST CSF 2.0 FAQ](https://www.nist.gov/cyberframework/faqs). These **six functions are not** the canonical security-concept taxonomy or an ordered process |
| R-20 OWASP LINDDUN | Privacy threat-modeling method | Privacy-specific threats not fully represented by STRIDE | SF-01-08; SF-02-05/07; SF-12-08 | [OWASP privacy threat modeling](https://devguide.owasp.org/en/04-design/01-threat-modeling/05-linddun-go/). Maintains the privacy/security distinction; execution of a modeling exercise belongs in Operational Foundations |

| R-21 Side and covert channel concepts | Distinct leakage-mechanism definitions | Side channels infer information through implementation side effects; covert channels permit hidden policy-violating communication by cooperating entities | SF-04-08; SF-08-09 | [NIST side channel](https://csrc.nist.gov/glossary/term/side_channel); [NIST covert channel](https://csrc.nist.gov/glossary/term/covert_channel). Do not equate the two |
| R-22 Information-flow and noninterference | Formal security-property / policy model | Constrains the influence of high or secret inputs on low-observable outputs under declared semantics | SF-08-01/09; SF-04-08 | [NIST flow-control definition](https://csrc.nist.gov/glossary/term/information_flow_control); [Cornell information-flow policy](https://www.cs.cornell.edu/courses/cs513/2005fa/MCinfo01.iflow_lecture_1.html). Model-relative proofs do not test unmodeled physical side channels |
| R-23 Cryptographic primitive and composition standards | Symmetric encryption/AEAD/key-management specifications | AES, GCM authenticated encryption, nonce requirements, key lifecycles and protocol composition | SF-09-01–09 | [FIPS 197 (2023)](https://csrc.nist.gov/pubs/fips/197/final); [SP 800-38D GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final); [SP 800-57 Pt1 R5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final); [RFC 5116 AEAD](https://www.rfc-editor.org/info/rfc5116/). Secure components do not guarantee protocol security |
| R-24 NIST SP 800-63-4 (2025) | Digital identity assurance guidance | Distinguishes identity proofing, authentication, federation, assertions and authentication assurance | SF-06-03–05/09; SF-01-06 | [SP 800-63-4 final](https://csrc.nist.gov/pubs/sp/800/63/4/final); [SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/B/4/final). IAM implementations remain in Identity Knowledge |
| R-25 Common Criteria ISO/IEC 15408:2026 | IT-product security evaluation criteria | Target of Evaluation, protection profiles, security targets, functionality and assurance criteria | SF-12-01–03; SF-08-01 | [ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1). Evaluation scope and measured properties condition any claim about security |
| R-26 NIST post-quantum cryptography standards | Cryptographic algorithms and migration references | FIPS 203 ML-KEM key establishment, FIPS 204 ML-DSA and FIPS 205 SLH-DSA signature families, and key lifecycle constraints | SF-09-05–07/09 | [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final), [SP 800-227](https://csrc.nist.gov/pubs/sp/800/227/final). KEMs and signature algorithms have different purposes |

| R-27 NIST Privacy Framework 1.0 and PF 1.1 draft | Voluntary privacy-risk management outcome framework | Harm from data processing, including authorized processing with adverse impacts on individuals; privacy is not only confidentiality | SF-01-08; SF-02-05/07; SF-12-08 | [PF 1.0 final (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final); [1.1 project status](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11). **PF 1.1's 2025 IPD is not a final edition** |
| R-28 ISO/IEC Guide 51 and IEC 61508-1 | Safety engineering concepts and functional-safety standard | Safety, intolerable risk of harm, safety functions and safety-related programmable systems, distinct from CIA and ordinary uptime | SF-01-08; SF-02-05; SF-11-04; SF-12-08 | [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html) confirmed in 2025; [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515) current valid edition alongside 2026 pre-release work. These are not general cybersecurity definitions |
| R-29 NIST SP 800-34 Rev. 1 | Contingency planning and recovery-objective reference | RTO, RPO, MTD and system-specific recovery requirements, which describe different time/data objectives | SF-11-04/07; SF-02-04; SF-05-01 | [NIST SP 800-34 Rev. 1 (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), [NIST RPO glossary](https://csrc.nist.gov/glossary/term/recovery_point_objective). Concepts aid foundational distinctions; planning workflows remain in Operational Foundations |
| R-30 NIST SP 800-61 Rev. 3 (2025) | Operational incident-response / cybersecurity risk-management guidance | Incident response recommendations across preparation, detection, response and recovery aligned to NIST CSF 2.0 | SF-11-01/04; SF-10-04/08; Operational Foundations | [NIST SP 800-61 Rev. 3 final (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Supersedes Rev. 2, but **incident-response workflows are operational**, not an alternative conceptual taxonomy of compromise |

## 2A. Version and source-fidelity notes

- **2026 source update:** The [NIST Privacy Framework 1.0 (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) is a final publication. The [Privacy Framework 1.1 project page](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) still identifies an **Initial Public Draft**, not a published final version. Its concepts may inform comparison but should not be cited as a final normative edition.
- **Safety version:** [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html) was confirmed current in 2025; the IEC webstore identifies [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515) as a valid edition with a 2026 edition preview. Do not treat a preview as the mandatory edition for evaluated products.
- **Operational boundary:** [NIST SP 800-61r3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) supersedes Rev. 2 and concerns incident-response practices. **NIST SP 800-160v2r1** describes resilience goals, not a four-step response workflow; NIST SP 800-34r1 distinguishes RTO/RPO/MTD.
- **Source-group count:** R-27 through R-30 are four supplemental source groups for privacy, safety and resilience/incident boundaries; the register now has **30 groups**, not a fixed target or proof of full model coverage.


- [ISO/IEC 15408-1:2026 (fifth edition, May 2026)](https://www.iso.org/standard/15408-1) **supersedes ISO/IEC 15408-1:2022**. The Common Criteria portal still publishes CC:2022 Revision 1; cite it explicitly as that version rather than representing it as the current ISO Part 1 edition.

- [RFC 9846 (July 2026)](https://www.rfc-editor.org/info/rfc9846/) **obsoletes RFC 8446** as the current TLS 1.3 specification. Its continued 0-RTT anti-replay caveats and updated key-share rules are relevant to cryptographic composition; historical RFC 8446 citations must be labeled superseded.

**As of November 18, 2026:** NIST SP 800-53 has Release 5.2.0 (August 2025). NIST SP 800-63 Rev. 4 was finalized in July 2025. NIST SP 800-162's `upd2` URL reflects updates published in August 2019, **not a separately numbered Revision 2**. NIST SP 800-38D remains the published GCM reference with a notice of planned revision. NIST SP 800-227 (2025) supplies final KEM guidance, and FIPS 203, 204 and 205 have distinct encapsulation/signature purposes.

The original twenty references remain R-01 through R-20. **Six supplemental source groups R-21 through R-26** extend this source map; the four new active candidate IDs are defined in [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md). The earlier two consolidated IDs remain historically traceable. Standards scope and publisher metadata have been inspected, but full proofs and standards clauses have not been independently validated.

## 3. Coverage crosswalk: existing twelve *candidate* areas

This crosswalk tests the proposed index against established sources. It **does not mean the twelve areas are approved** or that every proposed article is technically validated.

| Candidate area | Existing-source anchors | Architectural inference / action |
| --- | --- | --- |
| SF-01 Security Meaning & Objectives | CIA, STRIDE, NIST 800-160 Vol. 1 | Preserve CIA as central but non-exhaustive; separate authenticity, accountability, privacy and safety |
| SF-02 Protected Interests, Assets & Harm | NIST 800-160 Vol. 1; NIST 800-30 | Anchor protection needs to affected stakeholders and assets, not merely object inventories |
| SF-03 Threats & Adversarial Behavior | STRIDE; Diamond; ATT&CK; Unified Kill Chain; Attack Trees; CAPEC; NIST 800-30 | Distinguish adversarial behavior from non-adversarial hazards; do not make a tactic sequence universal |
| SF-04 Weaknesses, Vulnerabilities & Exposure | CWE; CAPEC; CVSS; NIST 800-30 | Preserve weakness ≠ vulnerability ≠ exploit; CVSS severity ≠ contextual risk |
| SF-05 Security Risk & Uncertainty | NIST 800-30; CVSS context distinctions | Distinguish context-specific risk from base severity; make assumptions and time horizon explicit |
| SF-06 Trust, Identity & Authority Principles | ABAC; Zero Trust; formal access-control models | Differentiate principal, policy, decision, enforcement, credential, trust; do not duplicate IAM mechanisms |
| SF-07 Security Controls & Defense Mechanisms | D3FEND; NIST 800-53; 800-160 Vol. 2 | Organize around how defenses work and fail, not control IDs or vendor products |
| SF-08 Secure Design & Architecture | NIST 800-160 Vol. 1; Zero Trust; formal security models | Cover reference mediation and formal policies; avoid equating any design pattern with guaranteed security |
| SF-09 Cryptography & Information Protection | CIA; NIST security engineering / architecture references | **Source gap:** dedicated primary cryptographic standards and key-management references are still needed; do not rely on broad frameworks to establish primitive-level claims |
| SF-10 Security Observation & Evidence | Diamond; ATT&CK; Pyramid of Pain; D3FEND | Keep observation, record, indicator, inference, evidence and attribution distinct; none of these models proves actor identity alone |
| SF-11 Security Failure & Resilience | NIST 800-160 Vol. 2; NIST 800-30 | Distinguish resistance, degraded function, survivability and recovery; avoid placing incident-response procedures here |
| SF-12 Security Assurance, Governance & Accountability | NIST 800-160 Vol. 1; NIST CSF 2.0; NIST 800-53 | Separate security claim/evidence from compliance outcome and governance workflow |

## 4. Four worked examples: what model grounding changes

### Example A: Security property versus attack category

An unauthorized change to a configuration can violate **integrity** (CIA). STRIDE may frame the corresponding threat as **tampering**. Both are useful: the first names an objective being violated; the second prompts examination of a class of threats. One is **not** a subtype of the other, and neither demonstrates that a particular attack occurred.

### Example B: Behavior versus event versus progression

An observed authentication-related interaction may be connected to a relevant **ATT&CK** technique if the evidence supports the mapping. A **Diamond Model** event may instead emphasize relationships among a possible adversary, infrastructure, capability and victim. A **Unified Kill Chain** description may position the activity in a hypothetical campaign progression. These are **different representational scopes**, and none automatically proves the identity, intent, stage or future actions of an adversary.

### Example C: Weakness versus severity versus risk

A **CWE** describes a class of weaknesses. **CAPEC** may describe an attack pattern exploiting weaknesses of that kind. **CVSS Base** describes characteristics and severity of a specified vulnerability; it does **not** alone measure organizational risk. A **NIST SP 800-30** scenario brings threat events, predisposing conditions, likelihood, impacts and local context into risk reasoning. These labels are linked but not interchangeable.

### Example D: Control catalog versus defensive technique versus assurance

**NIST 800-53** supplies a control catalog; **D3FEND** describes defensive techniques and relationships. Neither proves that a deployed measure actually prevents a modeled attack in a particular environment. An **800-160 Vol. 1** systems-security assurance argument must separately establish the claimed protection with appropriate requirements, assumptions, verification and evidence.

## 5. Specific architectural review findings

| Finding | Current inventory issue | Proposed disposition, **not approved** |
| --- | --- | --- |
| F-01 Distinct property models | CIA is implicit in individual subjects, but not identified as a named model | Introduce CIA explicitly as an established *lens*, while retaining broader objectives and non-equivalence |
| F-02 Formal policy models | Formal models are hidden under general 'security architecture' wording | Name Bell–LaPadula/Biba, access-control policy models and ABAC as studied examples with precise assumptions and source checks |
| F-03 Threat and hazard scope | SF-03 name says *Adversarial Behavior* while including accidents/hazards | Rename the proposed area *Threats, Hazards & Adversarial Behavior* or else move non-adversarial threats to another approved owner |
| F-04 Behavior-model identities | Adversary behavior, intrusion events, and phases can be conflated | Preserve Diamond, ATT&CK, Unified Kill Chain, CAPEC and STRIDE as separate representations with different units and limits |
| F-05 Exploitation/compromise overlap | SF-04-05 overlaps SF-11-01 | Assign **exploitation mechanism** to SF-04 and **compromise state/consequences** to SF-11 |
| F-06 Consequence estimation overlap | SF-02-06 overlaps SF-05-03 | SF-02 owns *harm/impacted interests*; SF-05 owns *risk-scenario consequence estimation* |
| F-07 Risk confidence overlap | SF-05-04 overlaps SF-10-08 | SF-05 owns uncertainty in risk estimation; SF-10 owns inference uncertainty and evidence limits |
| F-08 Missing explicit deception | SF-03 covers abuse and misuse but social-engineering/deception principles are not explicit | Mention deception and social engineering as possible security mechanisms without importing training procedures |
| F-09 Control-function ambiguity | SF-07 may be read as a catalog of NIST controls | Use D3FEND and 800-53 as different sources; keep mechanism, outcome and measured effectiveness separate |
| F-10 Cryptography authority gap | Broad system-security documents are inadequate for algorithmic/key management specifics | Add specific primary cryptography and key-lifecycle reference mapping before drafting SF-09 articles |
| F-11 Privacy conflation | Security ≠ privacy ≠ safety; LINDDUN has a different protected-interest view | Retain cross-domain distinctions and link dedicated privacy methods rather than declaring privacy a subset of CIA |
| F-12 CSF taxonomy temptation | Govern/Identify/Protect/Detect/Respond/Recover are outcomes, not 12 security subject roots | Maintain CSF as a **secondary crosswalk**, not the Foundations navigation hierarchy |
| F-13 No proof from framework adoption | Risk of labeling a model citation as technical verification | Keep detailed claim-to-source checks and independent human acceptance as publication gates |

## 6. Editorial operating rule for any future article

An article citing an established model should state: **(a)** the model's original purpose, **(b)** unit of analysis, **(c)** core entities/relations or variables, **(d)** assumptions and failure modes, **(e)** one correctly bounded example, **(f)** at least one non-equivalent model and why, **(g)** the primary source and version if applicable, and **(h)** what the model cannot establish.

No model name may be used to suggest that an unobserved fact, a security guarantee, or a taxonomy decision has already been proven.

## 7. Recommendation and governance boundary

**Recommendation:** Continue with the approved Security Foundations division and a **model-grounded architecture**. Keep the current 12-area/96-heading index as a **revisionable candidate**, not as an arbitrarily fixed article quota. Use this crosswalk to adjust labels and ownership before asking for architecture ratification. Keep a separate conceptual explanation for each model rather than mechanically creating one article per source framework.

**Not performed here:** Full primary-paper verification, source-by-source reviews for 96 candidate articles, a revised formally approved taxonomy, detailed model-comparison measurements, or publication acceptance. Some older classical models require further direct primary-source verification.

[Security Foundations index](README.md) · [Architecture](ARCHITECTURE.md) · [Candidate inventory](SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership boundaries](OWNERSHIP-BOUNDARIES.md) · [Development plan](DEVELOPMENT-PLAN.md)
