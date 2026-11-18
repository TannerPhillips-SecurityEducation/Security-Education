# Ethical, Human, and Societal Constraints

**Candidate subject:** SF-12-08 · Security Assurance, Governance & Accountability  
**Artifact type:** Substantive working article pilot; permanent canonical ownership **not ratified**  
**Development state:** Draft · **Source review:** References listed; scoped technical review pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Ownership-boundary review](../OWNERSHIP-BOUNDARIES.md)

## Security protects interests, including interests of people outside the system owner

An organization's security objectives are not unconstrained simply because the organization owns the infrastructure, employs its operators or can technically implement a control. Security choices affect **users, employees, bystanders, service recipients, suppliers, communities and other stakeholders**, sometimes without those people knowing about the relevant systems.

**Ethical and societal constraints** concern the legitimacy of protection goals and methods, obligations owed to affected people, proportionality of restrictions, rights and human harm, accountability for decisions and the fairness of resulting burdens. These are not identical to cryptographic correctness, vulnerability severity, an audit score or a system's operational availability.

A technically effective security control can still cause harm if it collects or reveals private information unnecessarily, blocks essential services without a defensible reason, treats affected groups unequally, or removes meaningful avenues for review or correction. Conversely, an apparently privacy-preserving choice may create safety risks if it undermines a critical protective function. Claims about such tradeoffs must identify the actual affected interests and conditions.

[Security, Privacy, Safety, and Reliability](security-privacy-safety-and-reliability.md) owns the **distinction among protection objectives**. This article owns **why legitimate authority, human impact, competing obligations and accountability constrain how security is pursued**.

## Rights, legitimacy and legal obligations are not the same as technical permission

The [United Nations Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights) identifies concerns including life and security of person (Article 3), equality before the law (Article 7), and protection against arbitrary interference with privacy, home and correspondence (Article 12). The Declaration is a foundational human-rights instrument, not an executable access-control policy or a substitute for applicable domestic law.

A program can be given technical permission to retrieve an employee's records while lacking a legitimate reason to use them for unrelated surveillance. A valid authorization token shows something about the system's policy and credentials; it does **not by itself** establish the moral, contractual or legal justification for every possible use.

Relevant distinctions include:

| Dimension | General question | What it cannot be replaced with |
| --- | --- | --- |
| Technical authorization | Does the system permit the operation? | Evidence that the operation is ethically justified |
| Legal authority | Is the action permitted or required in the applicable jurisdiction? | A universal claim about all jurisdictions |
| Legitimate objective | Does the measure pursue a valid protection need? | An owner's stated preference alone |
| Necessity | Are the adverse impacts reasonably required to achieve the specified goal? | Mere convenience or technical feasibility |
| Proportionality | Are the benefits and resulting burdens defensible under applicable principles? | A simplistic arithmetic formula for all harms |
| Accountability | Who can explain, review and correct a decision? | A log entry bearing an administrator's username |
| Meaningful remedy | Can affected people challenge or correct an unjustified outcome where appropriate? | A statement that the software passed tests |

The exact legal tests of necessity, proportionality and legitimate authority vary by jurisdiction, institutional context and applicable rights. This article uses these concepts as **questions to examine**, not as legal conclusions or prescriptions.

## Privacy harms may occur without a cybersecurity breach

The [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) recognizes privacy risks from data processing, including actions the organization itself has authorized. Its related [NIST glossary entry](https://csrc.nist.gov/glossary/term/info_system_related_privacy_risks) identifies potential harms to individuals such as discrimination, distress, economic loss and damage to trust.

Such harms can arise even when stored data are encrypted, access checks function correctly and no attacker is observed. Data aggregation and inference can reveal patterns that were never intended to be shared across contexts. A security policy that protects data only from external attackers can therefore leave substantial privacy problems unresolved.

The protected interest is **not merely the organization's own exposure to fines or reputational damage**. Individuals' autonomy, dignity, rights and material well-being are primary interests in their own right. A cost/benefit analysis that counts only organizational costs can omit important consequences.

## Harm, proportionality and unequal burden

**Harm** may involve bodily injury, loss of resources, denial of essential access, disclosure of personal information, stigmatization, discriminatory treatment or diminished freedom to make decisions. The harm's type, severity, distribution, duration, reversibility and likelihood can matter differently.

Two security interventions with similar aggregate costs can distribute burden very differently. An authentication system that repeatedly denies legitimate access to one set of users may present an equity concern even if its global success rate is high. A false-positive detection rule that triggers costly investigations for a narrow population may impose harms that aggregate alert metrics obscure.

Neither nominal equality of a technical rule nor statistical accuracy alone establishes that its outcomes are appropriate. Conversely, a difference in observed outcomes does not by itself identify an unlawful or unjust mechanism: evaluation requires context, explanatory evidence and the relevant governing obligations.

## Worked example: security monitoring versus privacy

Imagine a service that needs to detect unauthorized access to customer records. Two proposed collection designs are considered.

**Design A:** Record authenticated account identifier, attempted resource, timestamp, access decision and sufficient technical context for investigating unauthorized access, with controls on access and retention.

**Design B:** Record all of Design A plus every employee's precise location, private communications and unrelated browsing activity continuously, retaining records indefinitely for unrestricted management use.

A broader dataset may provide additional possible investigation context, but **Design B is not automatically more defensible security**. Its necessity, expected detection benefit, exposure of sensitive data, effects on people, applicable permissions and retention obligations require examination. Data minimization and purpose boundaries can be relevant to both privacy and security.

**What can be assessed from the description?** Design B processes substantially more sensitive information for purposes beyond the defined narrow detection objective. **What cannot be concluded without more evidence?** That Design A is sufficient for every threat, that Design B violates a particular statute, or that one fixed retention period is universally correct.

The example illustrates a **constraint on how security objectives are pursued**, not a ready-made monitoring policy.

## Worked example: safety and service availability

Suppose a controlled industrial process has an emergency interlock whose role is to prevent injury when a hazardous condition occurs. Disabling the interlock might make the service appear more available but increase the risk of physical harm.

Conversely, a blanket security rule denying all control messages during an emergency could prevent a necessary safety action. Neither "always stay online" nor "always deny" is an adequate universal principle.

The protected interests, safety function, failure conditions, control authority and acceptable risk must be modeled explicitly. [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html) addresses safety concepts applicable to people, property and environment; technical implementation of safety instrumentation belongs in the appropriate specialized domain.

## Accountable security governance and assurance

A defensible security justification should identify **whose goals are being pursued**, who is authorized to make tradeoffs, what evidence supports expected protection, and which people might bear adverse impacts. An organization can document controls and still lack a defensible argument for the harms or exclusions created by those controls.

[Security Claims and Assurance Arguments](security-claims-and-assurance-arguments.md) owns structured support for security claims. This pilot adds the question **whether the claim's objective and acceptable conditions are legitimate for affected stakeholders**.

The [NIST Privacy Framework](https://www.nist.gov/privacy-framework) helps organizations structure privacy risk management without substituting for legislation. NIST's **Privacy Framework 1.1** is still shown publicly as an initial-public-draft project rather than a clearly final edition as of this review. Use [PF 1.0 final](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) as the stable source for its privacy-risk definitions.

Security policy design can be informed by fairness, access, transparency, consent where applicable, oversight, meaningful challenge and proportionality, but the valid application of each principle depends on context and legal norms. This foundational discussion does not convert a contested ethical judgment into a universal technical theorem.

## Canonical boundaries

- [Security, Privacy, Safety, and Reliability](security-privacy-safety-and-reliability.md): definitions and non-equivalence of protection interests.
- [Security and Insecurity](security-and-insecurity.md): security as a conditional claim and uncertainty as distinct from demonstrated failure.
- [Risk, Scenarios, and Time Horizon](risk-scenarios-and-time-horizon.md): likelihood, affected interests and consequence uncertainty, not authority to accept any harm.
- [Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md): mechanism and effectiveness, not the legitimacy of every intended use.
- [Observable, Observed, and Recorded](observable-observed-and-recorded.md): source, record, attribution and epistemic limits.
- [Fundamentals: Human Error](../../fundamentals/human-sociotechnical-systems/human-error.md), [Decision-Making](../../fundamentals/human-sociotechnical-systems/decision-making.md), and [Evidence](../../fundamentals/scientific-analytical-reasoning/evidence.md): general human and evidentiary concepts.
- [Operational Foundations](../../operational-foundations/README.md): governance processes, risk and privacy assessments, safety evaluation and operational decision workflows.

## Authoritative references and limitations

- [UN Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights), Articles 3, 7, 12 and 29 for general rights and proportionality/limitations context.
- [NIST Privacy Framework 1.0, final (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final), individual privacy interests and risk from processing.
- [NIST privacy-risk glossary](https://csrc.nist.gov/glossary/term/info_system_related_privacy_risks), harm from breaches and authorized data use.
- [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), safety aspects for people, property and environment.
- [NIST SP 800-160 Vol.1 Rev.1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), security engineering, stakeholders and protection needs.

**Limits:** This article is a technical-ethical conceptual synthesis, not legal advice, a final moral calculus, a finding of institutional misconduct or a security compliance certificate. The norms and obligations applicable in any given jurisdiction or organization require independent legal and factual evaluation. Source-level review, independent human acceptance and internal taxonomy ratification remain open.

[Security Foundations](../README.md) · [Pilot Register](README.md)
