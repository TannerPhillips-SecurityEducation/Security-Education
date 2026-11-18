# Access-Control Policy Models

**Candidate subject:** SF-06-09 · Trust, Identity & Authority Principles  
**Artifact type:** Working article pilot, not a ratified canonical subject  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md), five material claim groups; full source verification and independent expert acceptance pending  
**Working architecture:** [v0.3 subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)

## A policy decision is not an authentication or enforcement event

**Access control** concerns regulating whether a **principal or subject** may perform an **operation** on an **object or resource** under a defined policy and context. An **access-control policy model** specifies the information and rules used to decide that relationship; an implementation must also receive the request, evaluate the policy and enforce the resulting decision.

An access-control decision can be represented abstractly as:

```text
Decision = Policy(Subject, Object, Operation, Environment, State)
```

This is explanatory notation, not a mandated programming interface. The arguments and decision results depend on the particular model; a model might use permissions, security labels, roles, attributes or relations.

**Identification** associates an entity with an identifier or claimed identity. **Authentication** supplies evidence about an identity or credential, under a specified assurance model. **Authorization** decides whether the identified or represented principal is entitled to carry out an action. An authorized action is not established simply because a password was verified.

[Identity Knowledge](../../../identity/README.md) owns authentication protocols, credential services, federation, policy deployment and operational IAM lifecycle mechanisms. This Security Foundations pilot owns the **shared conceptual policy models**, with explicit implementation boundaries.

## Discretionary access control

**Discretionary access control (DAC)** commonly permits subjects or owners to grant or modify selected access rights according to a discretionary model. File permissions and access control lists may be implementation mechanisms for a DAC policy, but the presence of an ACL does not itself fully define the model or prove that the ACL is applied consistently.

If subject A owns object D and the policy permits A to grant read permission to B, A may delegate that selected access under its authority. The system still must enforce the resulting decision and respect any higher-priority constraints.

DAC models should not be equated with unlimited freedom to disclose. An organization can impose mandatory conditions alongside owner-granted permissions.

## Mandatory access control and security labels

**Mandatory access control (MAC)** generally uses system-enforced policy rules that are not left wholly to discretionary subjects or object owners. Classical label-based security models can specify clearance, classifications or integrity levels and restrictions on information transfers.

A multi-level confidentiality example might permit reads only when the subject's clearance dominates the object's label under a specified lattice. Classical **Bell–LaPadula** formal reasoning constrains confidentiality-oriented behavior under its formal policy and transition assumptions. Classical **Biba** models are integrity-oriented and use different policy rules and assumptions. Neither is a universal rule stating that all systems must use a fixed four-level classification scheme.

**Important:** A subject possessing sufficient clearance does not automatically imply the subject needs access; an additional need-to-know or authorization rule may deny it. The relationship between classifications, clearance and discretionary permission depends on the implemented policy.

The [IETF Internet Security Glossary, RFC 4949](https://www.rfc-editor.org/rfc/rfc4949.html) describes Bell–LaPadula and Biba as distinct formal policy models. This article does not claim their original papers have been exhaustively reviewed or reproduce their full transition invariants.

## Role-based access control

**Role-based access control (RBAC)** associates permissions with roles and principals with role memberships or activation rights, under policy constraints. Its value is separating individual identities from the set of permissions associated with organizational functions.

For example:

```text
Role: Reviewer   → read reports
Role: Editor     → read reports, modify drafts
Role: Approver   → authorize publication
```

If a user is assigned only Reviewer, the policy grants read but not modify or approve. **Separation of duties** can be represented as a constraint that prevents conflicting roles being assigned or active together under a chosen model. The policy must specify whether the constraint is static, dynamic or dependent on context.

A role name is not proof of the user's employment title, organizational legitimacy or current need. Role design and membership management are themselves part of the security system and may be erroneous.

## Attribute-based access control

**Attribute-based access control (ABAC)** evaluates attributes associated with the subject, object, requested operation and sometimes environment against authorization policy. The [NIST SP 800-162 updated final (2019)](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) defines ABAC in those terms and gives considerations for applying it.

A simple, invented ABAC rule might be:

```text
Permit read if:
   subject.department == object.owner_department
   AND object.label != "restricted"
   AND environment.session_status == "verified"
Else deny.
```

For a subject in department Alpha, object owned by Alpha, `label="public"`, and a verified session, the rule evaluates to permit. If the object label changes to `restricted`, it evaluates to deny. This is **a policy example**, not an assertion that the attribute values are authentic or that a particular system correctly enforces them.

**Attribute provenance and freshness** matter. A policy decision can be logically correct relative to wrong, stale or attacker-controlled attributes and still violate the intended security objective.

## Policy decision and enforcement are different mechanisms

A system may use a **policy decision point (PDP)** that evaluates rules and a **policy enforcement point (PEP)** that mediates a protected operation. These are architectural functions in many access-control models; not every product must be physically decomposed into two services.

```text
Access Request
     ↓
Policy Inputs + Policy Decision
     ↓
Decision (permit / deny / conditional / indeterminate, as specified)
     ↓
Enforcement at the Protected Action
     ↓
Actual System Effect
```

A permit decision does not guarantee the action happened. A deny decision does not guarantee effective blocking if the request bypassed mediation. A policy checker can be correct while the target object is still accessible through another unprotected interface.

The general **complete mediation** principle demands that access decisions be applied to the relevant protected operations, not merely to an initial login. The proposed SF-08-02 subject owns this mediation principle; application-specific controllers and IAM products retain separate domain ownership.

## Worked comparison: authentication, policy and information flow

A user authenticates successfully. Under the policy, the user has permission to read document D but not publish it.

**Claim 1:** “The user is authenticated.” This concerns identity/credential evidence and the selected authentication context.

**Claim 2:** “The user is authorized to read D.” This concerns a policy decision under current subject, object, operation and environment attributes.

**Claim 3:** “The user can only read D and can never leak its contents.” This is an unjustified leap. After a legitimate read, the principal may copy the information, a process may expose it through logs or timing, or an unmodeled channel may disclose it.

Access control regulates **authorized operations**. [Information-Flow Security and Noninterference](information-flow-security-and-noninterference.md) considers whether data at one security level can influence observations at another. These are different properties and may need complementary controls.

## Least privilege, delegation and zero trust

**Least privilege** limits the authority granted to the permissions necessary for a relevant responsibility. **Separation of duties** distributes authority over sensitive actions. **Delegation** involves granting or transferring limited authority under a defined model, not merely changing a display name.

**Zero trust** is not another DAC/RBAC/ABAC class. [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) emphasizes that network location or asset ownership alone does not confer implicit trust and that resource-centered access decisions require explicit verification. ABAC may support some policy decisions in a zero-trust architecture, but adopting ABAC does not by itself establish a zero-trust architecture or prove control effectiveness.

## Source references and limitations

- [NIST SP 800-162, Guide to Attribute Based Access Control (updated final 2019)](https://csrc.nist.gov/pubs/sp/800/162/upd2/final).
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final).
- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final), with separate identity proofing, authentication and federation guidelines.
- [RFC 4949 Internet Security Glossary](https://www.rfc-editor.org/rfc/rfc4949.html), classical confidentiality/integrity security models.
- [NIST SP 800-53 Rev.5, Release 5.2.0](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls), access-control catalog; not an endorsement of a particular policy algorithm.

**Limits:** This article compares general policy models but does not claim that every DAC/MAC/RBAC/ABAC system shares exact syntax or that a policy decision is self-enforcing. Full original-source technical verification and independent expert publication acceptance remain pending.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md). This is a **working pilot**, not an approved permanent canonical article, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](README.md) · [Identity Knowledge](../../../identity/README.md)
