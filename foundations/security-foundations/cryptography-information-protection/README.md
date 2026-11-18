# Cryptography & Information Protection

**Division:** [Security Foundations](../README.md)  
**Working area ID:** SF-09  
**Architecture status:** **Provisional area membership and naming**, within a user-approved **Fundamentals-style directory architecture**. The number and names of areas and subjects can expand or contract.  
**Current content:** **9 candidate subjects; 3 substantive articles**, all Reviewed (model-assisted); 6 without an article. No source-Verified or Published claims.

## Scope and canonical ownership

This working area groups **cryptography & information protection** concepts that share a security-specific explanatory purpose. Boundaries follow the [working inventory](../SUBJECT-INVENTORY-PROPOSAL.md), [ownership decisions](../OWNERSHIP-BOUNDARIES.md), and [governing architecture proposal](../ARCHITECTURE.md), not a rigid formal ontology. Generic science/technical concepts belong in [Fundamentals](../../fundamentals/README.md); security practices belong in [Operational Foundations](../../operational-foundations/README.md); product-specific implementations belong to the seven specialized domains.

The area may be renamed, split, consolidated, or relocated when stronger conceptual and source evidence justifies it. **A directory is a navigation home, not automatically a ratified subject taxonomy.**

## Subject inventory and actual articles

| ID | Proposed subject or actual article | Development and source state | Intended conceptual responsibility |
| --- | --- | --- | --- |
| SF-09-01 | Cryptographic security properties and assumptions | **Inventoried / not authored** | Distinguish confidentiality, integrity, authenticity, and security models. |
| SF-09-02 | [Randomness, entropy, and nonces](randomness-entropy-and-nonces.md) | **Reviewed (model-assisted)** · Core claims checked in [Review 06](../PILOT-TECHNICAL-REVIEW-06.md) | Explain unpredictable values, uniqueness, and misuse consequences. |
| SF-09-03 | Encryption and confidentiality | **Inventoried / not authored** | Distinguish encryption goals from authorization and secure endpoint operation. |
| SF-09-04 | Hashes and message authentication | **Inventoried / not authored** | Distinguish digest computation, keyed authentication, and integrity evidence. |
| SF-09-05 | Digital signatures and origin evidence | **Inventoried / not authored** | Explain signed-message verification and limits of signer attribution. |
| SF-09-06 | Key establishment and trust anchors | **Inventoried / not authored** | Describe how participants obtain keys and establish justified reliance. |
| SF-09-07 | [Key lifecycle and cryptographic failures](key-lifecycle-and-cryptographic-failures.md) | **Reviewed (model-assisted)** · Core claims checked in [Review 06](../PILOT-TECHNICAL-REVIEW-06.md) | Explain creation, storage, rotation, compromise, expiration, and recovery. |
| SF-09-08 | Data protection across states | **Inventoried / not authored** | Compare at rest, in transit, and in use without claiming one mechanism solves all. |
| SF-09-09 | [Cryptographic composition and protocol security](cryptographic-composition-and-protocol-security.md) | **Reviewed (model-assisted)** · Core claims checked | Define AEAD, nonce and associated-data obligations, key binding, authentication, replay context and why individually secure primitives do not automatically establish secure protocols. |

**Review interpretation:** All three manuscripts have separate scoped technical audits: SF-09-09 under [Review 01](../PILOT-TECHNICAL-REVIEW-01.md), and SF-09-02/SF-09-07 under [Review 06](../PILOT-TECHNICAL-REVIEW-06.md). Their states are **Reviewed (model-assisted) / Core claims checked**, not full source verification, independent expert acceptance, publication, or permanent area-taxonomy approval.

## Development and relationships

New substantive references belong **inside this area directory**, directly under its `README.md`, following the [Fundamentals area pattern](../../fundamentals/mathematics-logic/README.md). Each article owns a coherent security-specific concept and links meaningfully to related areas and sources. Do not add a file merely to match the number of subjects in another area or the length of a Fundamentals chapter.

For development/review use [AGENTS.md](../AGENTS.md), [Development Plan](../DEVELOPMENT-PLAN.md), [Scope and Gap Review](../COVERAGE-AND-GAPS-REVIEW-03.md) and the [historical pilot register](../pilots/README.md). Substantive articles in this directory are the current working manuscript source; historical `pilots/` paths remain navigation aliases.

[Security Foundations](../README.md) · [All candidate subjects](../SUBJECT-INVENTORY-PROPOSAL.md) · [Root SOP](../../../AGENTS.md)
