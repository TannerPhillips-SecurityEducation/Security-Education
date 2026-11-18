# Security Foundations | Pilot Technical Review 01

**Review date:** November 18, 2026  
**Scope:** Eight substantive source-led article **pilots**, in the approved Security Foundations division but **without approval of the proposed internal area taxonomy**.  
**Technical method:** Review of **40 material claim groups** (five per pilot), definitions and counterexamples; selected original/official NIST, IETF, FIRST, MITRE, ISO and Common Criteria sources checked for **scope, publication status and key model requirements**; logically assessed worked examples and cross-division ownership.  
**Disposition:** All eight pilot articles have passed this **bounded model-assisted technical/editorial review**, after the specific corrections documented below. Their next source state is **Core claims checked**; no complete sentence-level source verification, qualified independent human peer review, final canonical placement or Published status is claimed.

## Essential correction log

1. **Security is not a certainty state:** [Security and Insecurity](pilots/security-and-insecurity.md) was revised to distinguish an actually deficient security property from an *unknown/unassured* security claim. A lack of evidence does not prove insecurity or security.
2. **TLS 1.3 source currency:** [RFC 9846 (July 2026)](https://www.rfc-editor.org/info/rfc9846/) **obsoletes RFC 8446 (2018)**. [Cryptographic Composition and Protocol Security](pilots/cryptographic-composition-and-protocol-security.md) now cites the current specification, distinguishes its key-share constraints, and retains correctly qualified **0-RTT replay** warnings.
3. **Common Criteria ISO edition:** [ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1) **supersedes the 2022 Part 1 edition**. The [Security Claims and Assurance Arguments](pilots/security-claims-and-assurance-arguments.md) article and the source crosswalk were corrected. [CC:2022 Revision 1](https://www.commoncriteriaportal.org/files/ccfiles/CC2022PART1R1.pdf) is a separate, explicitly named scheme reference with useful TOE/PP/ST definitions.
4. **Access control version:** [NIST SP 800-162 updated final](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) includes August 2, 2019 updates; `upd2` in its URL should not be mistaken for a new formal "Revision 2".
5. **Assurance gate:** A pilot that passes this review remains in **pilots/** until the internal Security Foundations area/subject ownership is explicitly ratified. A model-assisted review does not approve its future URL or the proposed twelve areas/ninety-six subjects.

## Material claim-group ledger

### SF-01-01: Security and Insecurity

**Pilot:** [security-and-insecurity.md](pilots/security-and-insecurity.md)  
**Primary source orientations:** [NIST information security](https://csrc.nist.gov/glossary/term/information_security); [NIST SP 800-160 Vol.1 Rev.1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [FIRST CVSS v4](https://www.first.org/cvss/user-guide)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Bounded security propositions | Protected interest, operating context, assumptions and evidence must be explicit; 'secure' without scope is not a validated proposition. |
| 02 | Security vs evidentiary uncertainty | Corrected wording to distinguish actual failure/weakness from missing assurance. Unknown evidence does not prove security or insecurity. |
| 03 | CIA vs other interests | Confidentiality, integrity and availability are separate information-security properties, not a complete ontology of privacy, safety, reliability and authenticity. |
| 04 | Requirement, control and assurance | Objective, testable requirement, safeguard deployment and evidence-backed claim are conceptually separate; control existence is not measured success. |
| 05 | Worked counterexample | A successful login, existence of audit logs, and presence of backups support bounded facts, not universal authorization, integrity or restoration guarantees. |

### SF-03-01: Threat Sources and Threat Events

**Pilot:** [threat-sources-and-threat-events.md](pilots/threat-sources-and-threat-events.md)  
**Primary source orientations:** [NIST SP 800-30 Rev.1](https://csrc.nist.gov/pubs/sp/800/30/r1/final); [MITRE ATT&CK get started](https://attack.mitre.org/resources/pre-introduction/); [MITRE CAPEC](https://capec.mitre.org/)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Threat source / threat event / violation | Potential source, actual occurrence and successful violation are different claims; no automatic harm or compromise follows. |
| 02 | Adversarial vs non-adversarial | Storm and power loss are valid non-adversarial adverse conditions; actor identity/intent need separate evidence. |
| 03 | Preconditions and observation | An attempted protected-file request is not evidence of unauthorized read, and transport success is not evidence of policy violation. |
| 04 | Model non-equivalence | STRIDE, ATT&CK tactic/technique, Diamond intrusion-event relations, CAPEC patterns and Unified Kill Chain progression have different units of analysis. |
| 05 | Worked three-scenario contrasts | Denial, storm outage and overbroad-role access have distinct causes and claim scopes; no numeric likelihood or intent is inferred. |

### SF-04-02: Vulnerabilities and Exploitability

**Pilot:** [vulnerabilities-and-exploitability.md](pilots/vulnerabilities-and-exploitability.md)  
**Primary source orientations:** [MITRE CWE](https://cwe.mitre.org/about/); [FIRST CVSS v4.0](https://www.first.org/cvss/user-guide); [NIST SP 800-30 Rev.1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Weakness class vs vulnerable instance | CWE describes weakness types, not proof that a specific target is affected/exploitable. |
| 02 | Reachability and preconditions | A flaw can exist without a reachable path; enabled interface alone does not prove a vulnerability. |
| 03 | Exploitation vs compromise state | An attempted exploit, achieved violation and broader compromised state require distinct facts and owners. |
| 04 | CVSS severity vs contextual risk | FIRST explicitly warns CVSS Base measures severity, not organizational risk; Threat/Environmental metrics and stakeholder context affect interpretation. |
| 05 | Worked object-level access example | A reachable document endpoint can enforce correct policy; failure to verify object-specific permission permits violation only under stipulated authority/data conditions. |

### SF-06-09: Access-Control Policy Models

**Pilot:** [access-control-policy-models.md](pilots/access-control-policy-models.md)  
**Primary source orientations:** [NIST SP 800-162 updated Aug 2019](https://csrc.nist.gov/pubs/sp/800/162/upd2/final); [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final); [NIST 800-63-4 (2025)](https://csrc.nist.gov/pubs/sp/800/63/4/final)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Access decision vs authentication and mediation | Principal identity claim, authentication, policy permit/deny and observed enforcement outcome are distinct; authorization may be conditioned on attributes. |
| 02 | DAC/MAC/RBAC/ABAC model scopes | Discretionary grants, mandatory label constraints, role permissions and attribute/policy decisions are models, not universal IAM implementations. |
| 03 | ABAC policy evaluation | NIST 800-162 defines subject, object, operation and optional environment attributes; example Alpha/public/verified permits, restricted label denies. |
| 04 | Policy vs enforcement | PDP/PEP functions are distinguishable; logically valid permit/deny output cannot prove complete mediation or absence of alternate paths. |
| 05 | Zero trust non-equivalence | NIST 800-207 rejects implicit trust by network location; Zero Trust is not simply ABAC or a new authorization class. |

### SF-08-09: Information-Flow Security and Noninterference

**Pilot:** [information-flow-security-and-noninterference.md](pilots/information-flow-security-and-noninterference.md)  
**Primary source orientations:** [NIST information flow control](https://csrc.nist.gov/glossary/term/information_flow_control); [Cornell information-flow lecture](https://www.cs.cornell.edu/courses/cs513/2005fa/MCinfo01.iflow_lecture_1.html); [NIST covert and side channels](https://csrc.nist.gov/glossary/term/covert_channel)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Model-relative noninterference | With low inputs/environment fixed, low observations invariant to high inputs under selected deterministic model. This is not a universal physical leak test. |
| 02 | Implicit vs explicit flow | Control dependence on secret can reveal information even without direct assignment; example public=1 iff secret>0 is valid counterexample. |
| 03 | Output and timing toy proof | For request=4 Design A always returns 8 in the specified value model; Design B gives 8 vs 9 for h=0/h=1; timing may violate stronger model. |
| 04 | Label/declassification assumptions | Information-flow constraints, allowed declassification, and subject/action authorization are separate policy commitments. |
| 05 | Side vs covert channels | NIST distinguishes indirect side effects enabling inference from unintended cooperating communication that violates policy; mere timing differences do not prove exploitability. |

### SF-09-09: Cryptographic Composition and Protocol Security

**Pilot:** [cryptographic-composition-and-protocol-security.md](pilots/cryptographic-composition-and-protocol-security.md)  
**Primary source orientations:** [RFC 5116 AEAD](https://www.rfc-editor.org/info/rfc5116/); [RFC 9846 TLS 1.3 (Jul 2026)](https://www.rfc-editor.org/info/rfc9846/); [NIST SP 800-227 KEMs](https://csrc.nist.gov/pubs/sp/800/227/final)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Primitive goals and composition | Encryption, MAC, signatures, key establishment/KEM, AEAD, key schedule and authorization make different claims; one cannot prove the others. |
| 02 | AEAD and nonce constraints | RFC 5116 distinguishes plaintext, associated data and algorithm-specific nonce handling; GCM nonce reuse under same key can fatally degrade protection. |
| 03 | KEM vs signatures | NIST SP 800-227 / FIPS 203 address encapsulation, while FIPS 204/205 concern distinct signatures; KEM alone does not bind real-world peer identity. |
| 04 | TLS 1.3 current specification correction | Corrected obsolete RFC 8446 to RFC 9846 (July 2026); current RFC continues 0-RTT replay caveats and includes new key-share reuse restrictions. |
| 05 | Replay/identity counterexample | A previously valid signature/tag may verify on replayed bytes; acceptance requires application/protocol freshness and authorized action semantics. |

### SF-10-02: Observable, Observed, and Recorded

**Pilot:** [observable-observed-and-recorded.md](pilots/observable-observed-and-recorded.md)  
**Primary source orientations:** [NIST SP 800-92 logging](https://csrc.nist.gov/pubs/sp/800/92/final); [W3C PROV-DM](https://www.w3.org/TR/prov-dm/); [RFC 5424 Syslog](https://www.rfc-editor.org/info/rfc5424/)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Event / observation / record | An occurrence, sensing act, representation and security interpretation are distinct; records may be mistaken or generated absent actual sensing. |
| 02 | Visibility gaps and negative evidence | Sensor omission, drops, expiry, filter/search mismatch and non-occurrence have different epistemic meanings; no alerts does not prove no attack. |
| 03 | Record provenance and identity | A schema field or signed record supports bounded representation/authenticity claims, not proof of human identity, truth of original reading or complete logging. |
| 04 | Telemetry/indicator/detection/alert | Raw data, selected signs, rule/classification result and notification are not identical objects; detection rule success does not prove malicious intent. |
| 05 | Worked event records | Toy network, service and alert records cannot independently prove same causal event, exact document bytes, identity or severity without corroborating context. |

### SF-12-01: Security Claims and Assurance Arguments

**Pilot:** [security-claims-and-assurance-arguments.md](pilots/security-claims-and-assurance-arguments.md)  
**Primary source orientations:** [NIST SP 800-160 v1r1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [ISO 15408-1:2026](https://www.iso.org/standard/15408-1); [CC:2022 revision 1](https://www.commoncriteriaportal.org/files/ccfiles/CC2022PART1R1.pdf)

| Group | Audited claim family | Finding and limitation |
| --- | --- | --- |
| 01 | Assurance claim/argument/evidence | Security assurance rests on bounded claims, reasoning, assumptions and relevant evidence; catalog compliance or a passed test alone is insufficient. |
| 02 | TOE, ST, PP vocabulary | Common Criteria describes an evaluated target, target-specific security claims and reusable security needs; these do not equal proof of every later deployment. |
| 03 | Common Criteria edition correction | Corrected withdrawn ISO/IEC 15408-1:2022 citation to current 2026 fifth edition; distinguished CC:2022 Revision 1 as a scheme reference. |
| 04 | Verification vs validation | Requirement satisfaction differs from intended use suitability; an internally sound formal model can omit material system effects. |
| 05 | Worked 100-case example | 100 observed test successes establish tested-case outcomes under harness assumptions, not universal correctness, exhaustive attack coverage or probabilistic confidence. |

## Worked-explanation checks

| Subject | Model or contrast inspected | Audited result |
| --- | --- | --- |
| Security and Insecurity | Protection objective, audit logging and daily backup | None demonstrates every possible confidentiality/integrity/resilience outcome; knowledge uncertainty remains separate |
| Threat Source/Event | Unauthorized request denied vs storm outage vs overbroad role | Attempt, environmental disruption and authorization failure have distinct source/cause/property implications |
| Vulnerability/Exploitability | Public document endpoint with object-level permission enforced or absent | Exposure alone does not establish vulnerability; violating disclosure needs an actual policy and content outcome |
| Access Control | Example subject.department=Alpha, owner_department=Alpha, label=public, session=verified | Permit under toy ABAC rule; changing label to restricted yields Deny. No attribute-authenticity or enforcement proof |
| Information flow | request=4, secret h=0 vs h=1, Design A and B | A returns 8 for both under value-only model; B returns 8/9, counterexample to simplified noninterference |
| Cryptographic composition | Validly signed request replayed | Signature/tag may verify unchanged bytes; duplicate action prevention depends on protocol or application state |
| Security observation | Three invented network/service/alert records | Each is a producer assertion; causal association, human identity, and ground truth remain hypotheses |
| Assurance | 100 successful selected test cases | No exhaustive claim about every configuration/input, and no statistically justified coverage percentage |

These are **illustrative logical cases**, not experiments on real hardware, enterprise networks or security products.

## Source classification and confidence

- **Authoritative specification/standard scope checked:** RFC 5116 (AEAD), RFC 9846 (TLS 1.3 current version), NIST SP 800-162 (ABAC 2019 update), ISO/IEC 15408-1:2026 (current Part 1 scope), CC:2022 Revision 1 (related scheme glossary). 
- **Guidance/source model scope checked:** NIST SP 800-160v1r1 engineering/assurance concepts, SP 800-30r1 risk terminology, SP 800-207 zero trust principles, NIST SP 800-227 KEM purpose, FIRST CVSS v4 guidance, MITRE ATT&CK adversary behavior categories, and NIST side/covert channel definitions.
- **Conceptual synthesis:** The proposed protection, observation and assurance explanation structures are **editorial models**, not claims that a standards body has ratified this repository's diagram or ontology.
- **Unverified portions:** Detailed original proofs for Bell–LaPadula/Biba, every Common Criteria clause, every NIST SP 800-53 item, all internal and external link destinations, published attack attribution, quantitative real-world security efficacy and independently human peer-reviewed acceptance are **not claimed**.

## Remaining architectural and knowledge gaps

The working [candidate inventory](SUBJECT-INVENTORY-PROPOSAL.md) is **96**, with twelve candidate navigation areas. Both figures remain flexible. Passing these pilot reviews does not prove the other **88 unpiloted candidate subjects** are sufficient, necessary or correctly scoped. Continuing gap analysis should prioritize:

- **Risk context** (SF-05), including loss uncertainty versus CVSS severity, as a separate pilot.
- **Security controls, coverage, resilience and adverse failure** (SF-07/SF-11), to test whether control effectiveness, resilience and assurance can be explained without duplicating Fundamentals.
- **Privacy versus security/safety** (SF-01/SF-12), with explicit protected-interest distinctions and rights/harm boundaries.
- **Weakness chains vs information-flow leakage** (SF-04/SF-08), ensuring side/covert channels and policy noninterference remain non-equivalent.
- **Source-passage verification**, external URL freshness, formal-model assumptions and review by qualified human experts.

**No Knowledge Checks, Practical Assessments, mandatory vendor products or formal graph predicate schema have been introduced.** The eight files remain under `pilots/` and are not ratified canonical subject pages.

[Security Foundations](README.md) · [Pilot register](pilots/README.md) · [Architecture Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md) · [Development plan](DEVELOPMENT-PLAN.md)
