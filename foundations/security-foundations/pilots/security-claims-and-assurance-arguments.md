# Security Claims and Assurance Arguments

**Candidate subject:** SF-12-01 · Security Assurance, Governance & Accountability  
**Artifact type:** Working article pilot; proposed canonical location not ratified  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md), five material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [v0.3 proposal](../ARCHITECTURE.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)

## Assurance is a reasoned claim supported by bounded evidence

**Security assurance** concerns justified confidence that specified security requirements and protective properties are satisfied by a defined system under declared assumptions and conditions. It is not the absence of discovered problems, a categorical promise of perfect security, or a synonym for certification.

A **security claim** is a proposition about the security of a defined target. An **assurance argument** explains why available evidence supports that proposition, through explicit reasoning, assumptions, counterarguments, and the relevance of the evidence.

A simple conceptual structure is:

```text
Security Claim
     ↑ justified by
Argument / Reasoning
     ↑ supported by
Evidence + Assumptions + Boundaries
     ↑ collected/evaluated under
Methods, Tools, People, and Conditions
```

An evidence file may be authentic while still irrelevant to a claim. A proof may be valid relative to a mathematical model that omits important implementation behavior. A test can demonstrate a selected outcome in a tested configuration without establishing the result for untested versions, environments or adversaries.

[NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) provides systems security engineering and trustworthiness terminology; the [Current Common Criteria Part 1 / ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1) supplies security evaluation concepts for specified IT products and evaluated security properties. Their scopes are not universal proof of all security requirements.

## A claim requires a precise target and conditions

A useful claim names:

| Element | Example | Consequence of omission |
| --- | --- | --- |
| Target/system of interest | Application release 3.4, configured with access policy P | A different version might not satisfy the claim |
| Security property | Unauthorized principals cannot read restricted records | “Secure” remains too broad |
| Threat/operating assumptions | Authentication works under the tested credential and device assumptions | Success may not transfer to compromised identities |
| Evaluated boundary | Public API access and documented service interface | Internal storage or physical interfaces might be outside scope |
| Time/configuration horizon | Current release with specified controls active | The claim may decay after change |
| Supporting evidence | Policy analysis, tests, code review, independent evaluation | Unsubstantiated optimism is not assurance |

A statement like “this application passed a penetration test” identifies an activity, not an adequate security claim. The test's scope, methods, timing, findings and uncertainty determine what it can support.

## Verification, validation and security evaluation

**Verification** asks whether the specified system or work product satisfies defined requirements or properties. **Validation** asks whether the intended use and needs are adequately satisfied in the relevant environment. **Security evaluation** examines selected protection claims through declared criteria, evidence and methods.

These are not the same thing. A system can correctly implement a flawed security requirement. A program can pass tests but fail in a newly introduced state. A cryptographic algorithm can be standardized while the deployment violates necessary key or nonce assumptions.

**Formal verification** proves or checks properties of a formal model or artifact under defined semantics. Formal model checking may cover a state space within model assumptions; it does not necessarily establish correct sensor signals, hardware emissions, real identity, or all environmental conditions.

**Operational monitoring** may add evidence about deployed behavior but is not a replacement for adequate requirements or architectural reasoning. It also cannot prove the nonexistence of undetected attacks.

## Common Criteria source edition and scope

**Edition note (November 2026):** [ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1) is the current published fifth edition of *Evaluation criteria for IT security, Part 1*. It supersedes the withdrawn **ISO/IEC 15408-1:2022** edition. The related [CC:2022 Revision 1](https://www.commoncriteriaportal.org/files/ccfiles/CC2022PART1R1.pdf) remains an accessible scheme reference that defines the TOE, PP and ST vocabulary, but should not be mislabeled as the latest ISO edition. Detailed clauses and compatibility across editions need a separate standards check.

## Common Criteria establishes a bounded target-of-evaluation result

The [Common Criteria / ISO/IEC 15408-1:2026](https://www.iso.org/standard/15408-1) defines a structured security evaluation model involving a **Target of Evaluation (TOE)**, **Security Target (ST)**, **Protection Profile (PP)** and applicable security functional and assurance requirements.

These terms serve different purposes:

- **TOE:** The specific target subject to evaluation, with a defined boundary.
- **Security Target:** A description of that target's security requirements and claimed security functions under a stated evaluation context.
- **Protection Profile:** Reusable security-problem definitions and requirements for a class of products or similar target scope.
- **Assurance criteria/evaluation:** Defined activities and evidence used to reach bounded confidence about those requirements, rather than an unconditional security rating for every future configuration.

A successful product evaluation is meaningful **for the evaluated properties, versions, configurations, assumptions and methodology**. It does not guarantee all later deployments are safe, or that every possible threat was considered.

Likewise, NIST SP 800-53 provides a **catalog of controls** while SP 800-53A supplies associated assessment procedures. Presence in a catalog, selection in a baseline, implementation in a product and successful evaluation against a security objective are different facts.

## Claims can be decomposed, but arguments are not automatically sound

A broad security claim might be decomposed into subclaims about identification, authorization, enforcement, cryptographic protection and reliable audit records.

```text
CLAIM: Protected records cannot be read by unauthorized principals
  Subclaim A: Request principals are reliably identified under model M
  Subclaim B: Policy P denies unauthorized reads
  Subclaim C: Every relevant read path is mediated
  Subclaim D: Unprotected copies or outputs are excluded or addressed
  Evidence: tests, proofs, configuration records, source reviews...
```

Even if each subclaim is checked against some evidence, the composition can fail if **there are unexamined paths, contradictory assumptions, untrusted dependencies or outdated configurations**. A logically coherent argument can be unsound when its premises do not hold in reality.

An assurance argument should make its weakest major assumptions visible, rather than hiding them behind generic badges such as “compliant” or “enterprise grade.”

## Worked example: tested rule versus demonstrated security

Imagine a file service with 100 identified test requests. Every unauthorized test request is denied, and every permitted request is served, under the test harness and sample configuration.

**Supported statement:** The tested configuration produced the expected authorization outcome for those 100 cases.

**Unsupported statement:** All possible unauthorized file reads have been prevented. The test set may not cover every principal/resource combination, alternate interface, stale session, policy change, code path, dependency or failure mode.

A stronger assurance case might add policy model review, analysis of complete mediation, access-path enumeration, configuration inventory, negative tests for alternative interfaces, and independent validation of test logging. But even that would yield **bounded confidence**, not mathematical proof about unspecified conditions.

The number “100” is an invented test count, not a statistical confidence interval or claim of empirically measured coverage.

## The assurance claim changes as systems and threats change

An accepted claim at time t₀ may become stale when software changes, a key is compromised, a supplier is replaced, a user role is altered, or a new vulnerability makes an assumption false.

**Assurance decay** is not necessarily a universal mathematical degradation curve. It is the practical need to reassess whether the evidence and assumptions still match the target and its environment. A previously valid proof for one release does not automatically certify a modified implementation.

A change record and a new test can help refresh confidence, but *which evidence is sufficient* depends on the property, criticality and scope. Incident-response procedures and audit workflows belong to [Operational Foundations](../../operational-foundations/README.md); the shared theory of what an assurance claim means belongs here.

## Related conceptual ownership

- [Security and Insecurity](security-and-insecurity.md) owns the meaning and conditions of desired protection.
- [Observable, Observed and Recorded](observable-observed-and-recorded.md) owns the limits of security data and evidence.
- [Vulnerabilities and Exploitability](vulnerabilities-and-exploitability.md) owns enabling conditions for violating security requirements.
- [Information-Flow Security and Noninterference](information-flow-security-and-noninterference.md) owns formal policy properties that an assurance argument might reference.
- [Fundamentals: Verification and Validation](../../fundamentals/systems-engineering/verification-and-validation.md) owns the general engineering distinction.
- [Fundamentals: Evidence](../../fundamentals/scientific-analytical-reasoning/evidence.md) owns general claim-relative support.
- [Operational Foundations](../../operational-foundations/README.md) owns actual audit and assessment activities.

## Authoritative source starting points

- [NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), security engineering, protection needs, assurance and trustworthiness.
- [ISO/IEC 15408-1:2026 / Common Criteria](https://www.iso.org/standard/15408-1), target, security target, protection profiles, evaluation context.
- [NIST SP 800-53 Rev.5 Release 5.2.0 announcement](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls), control catalog versus implementation.
- [NIST SP 800-53A Rev.5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), selected assessment procedures and their scope.

**Editorial limitation:** This is a conceptual assurance explanation, not an evaluation certification or a claim that any real system complies with a standard. Source passage verification, standards license scope, independent qualified expert review and internal Security Foundations taxonomy ratification remain open.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md). This is a **working pilot**, not an approved permanent canonical article, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](README.md)
