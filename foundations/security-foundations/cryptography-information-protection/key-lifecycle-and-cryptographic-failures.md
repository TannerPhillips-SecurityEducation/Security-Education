# Key Lifecycle and Cryptographic Failures

**Candidate subject:** SF-09-07 · Cryptography & Information Protection  
**Working area:** [Cryptography & Information Protection](README.md) · Fundamentals-style area/README/article structure adopted; subject taxonomy and permanent canonical ownership remain provisional  
**Artifact type:** Substantive security-knowledge working manuscript, not an approved publication or an operational key-management runbook  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 06](../PILOT-TECHNICAL-REVIEW-06.md), ten material claim groups including cryptoperiod and key-hierarchy corrections; full source verification and independent expert acceptance pending  
**Architecture:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Gap review SG-05](../COVERAGE-AND-GAPS-REVIEW-03.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)

## A cryptographic key is a security dependency with a history

A secure primitive cannot protect information if the key on which its security depends was predictably generated, disclosed to an unauthorized principal, used in an incompatible role, duplicated across contexts, or retained beyond the circumstances in which it can be trusted. **Key management is the maintenance of justified security properties across the entire existence and use of cryptographic keying material**, not merely a scheduled operation called “rotation.”

A **cryptographic key** is algorithm-specific keying material that enables an operation such as encryption, decryption, signing, verification, message authentication, key agreement or derivation. A key's **role**, **ownership**, **usage context**, **authorized principals**, **protection level** and **validity/usage period** determine what a compromise would mean. The same bytes used as a symmetric encryption key and as an unrelated protocol authenticator are not automatically safe simply because each individual primitive is secure.

[NIST SP 800-57 Part 1 Revision 5 (2020)](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) supplies the current final general guidance for the security services, types of keying material, protection requirements and key-management functions. **Revision 6 remained an Initial Public Draft** on the [official NIST page](https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd) at this edition's November 2026 source check; its proposed additions, including post-quantum algorithms and separate discussion of key storage, are not yet binding final-text claims.

This article owns **general security-specific key lifecycle conditions, systemic compromise and transition failures**. [Cryptographic Composition and Protocol Security](cryptographic-composition-and-protocol-security.md) owns complete protocol claims and concrete key-schedule composition; [Randomness, Entropy, and Nonces](randomness-entropy-and-nonces.md) owns input unpredictability, generator-state weaknesses and nonce uniqueness. The [Identity](../../../identity/README.md), [Cloud](../../../cloud/README.md), [Endpoint](../../../endpoint/README.md) and other specialized domains own their particular devices, keystores, certificate services and implementations.

## Anatomy: keys have roles, dependencies and authority

A precise key inventory requires more than the bytes themselves:

| Dimension | What must be known |
| --- | --- |
| Key identity and version | Which logical key, material version, algorithm and parameter set is being referenced? |
| Security role | Is the key used for encryption/decryption, signing/verification, authentication, wrapping, derivation, agreement or encapsulation? |
| Ownership and protection domain | Which principals, processes, cryptographic modules, jurisdictions or organizational boundaries can use or export it? |
| Material origin | Was it generated with suitable entropy, derived from an established secret, agreed with a peer, imported, or recovered? |
| Usage scope | Which protocols, datasets, identities, devices, directions and key epochs may use it? |
| Time limits | When may it originate new cryptographic protection, and when may historical material still need to be processed? |
| Dependencies | Which certificates, trust anchors, wrapping keys, parent secrets, hardware and recovery arrangements determine its security? |
| Status and evidence | Can its existence, active use, revocation, compromise, recovery, archival and destruction be substantiated? |

A **public verification key** and its **private signing key** are deliberately asymmetric in confidentiality requirements. A public certificate may be distributable, but its binding between key and subject must still be justified. A symmetric data-encryption key needs confidentiality and appropriate integrity protection; a key-encryption key (KEK) used to wrap it may protect a larger set of dependent keys. The quantity or importance of the assets dependent on a key can magnify the consequences of that key's failure.

Keying material is not limited to a leaf encryption key. It can include master/derivation keys, pre-shared secrets, ephemeral private keys, exported seed state, trust anchors and credentials that enable an adversary to request cryptographic operations through a legitimate service.

## Key lifecycle is a state model, not a universal sequence of commands

A useful conceptual lifecycle is:

~~~text
Policy and intended cryptographic purpose
                |
                v
Generate / establish / import / derive
                |
                v
Bind to identity, owner, role and context
                |
                v
Protect / provision / authorize use
                |
                v
       Active protection or use
                |
       +--------+---------+
       |                  |
       v                  v
Rotate / replace     Suspend / revoke
       |                  |
       v                  v
Retire old key       Contain compromised key
       |                  |
       +--------+---------+
                |
                v
Archive / retain for authorized
historical operations (if required)
                |
                v
Destroy material / revoke access /
verify retention and recovery limits
~~~

The transitions are **not mandatory chronological stages for every key**. An ephemeral session key may never need archival storage. A verification key may remain available to validate previously signed artifacts long after its paired signing key stops producing new signatures. A compromised key may bypass normal retirement schedules and demand urgent replacement and containment.

Key **generation**, **establishment** and **derivation** are also different operations. NIST [SP 800-133 Revision 2 (2020)](https://csrc.nist.gov/pubs/sp/800/133/r2/final) specifically discusses generation of cryptographic keys. Establishing a shared secret with a peer, or deriving multiple context-bound keys from an existing secret, has further protocol assumptions and distinct source publications. NIST's [SP 800-133 Revision 3 (April 2026 Initial Public Draft)](https://csrc.nist.gov/pubs/sp/800/133/r3/ipd) proposes PQC and seed-expansion updates, but **Revision 2 remains the final version** in the checked [NIST key-management publications register](https://csrc.nist.gov/projects/key-management/publications).

Key state can be modeled as a collection of **independent properties** (allowed to sign? allowed to decrypt old material? revoked for trust decisions? known compromised? physically present in a backup?) rather than a simplistic single “active/inactive” bit. The same material can be technically present but no longer authorized for new encryption.

## Cryptoperiod, retirement and lingering decryption obligations

A **cryptoperiod** is the authorized lifetime of a key for relevant uses under a stated policy. For a symmetric key, [NIST SP 800-57 Part 1 Rev. 5, §5.3.5, printed pp. 37–38](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf) distinguishes the **originator-usage period**, when cryptographic protection may be applied, from a potentially longer **recipient-usage period**, when previously protected material may be processed. Its Figure 1 defines the total symmetric-key cryptoperiod from the start of originator usage through the end of recipient usage; some communication cases have coincident periods. The periods vary by key role and service and must not be collapsed into one fixed calendar duration.

The expiry of a **certificate**, the revocation of **trust in a public key**, the retirement of a **private signing key**, the scheduled replacement of an **encryption key**, and the physical destruction of a **storage copy** are distinct events.

Consider an organization that stops encrypting new records with key \(K_0\) and begins using \(K_1\) at a cutover date. If the records were **directly encrypted by \(K_0\)**, merely rewrapping an unrelated DEK cannot remove the need for \(K_0\); those records require authorized retention of \(K_0\) or genuine re-encryption under different content-encryption material. If instead \(K_0\) was a **key-encryption key (KEK)** that wrapped separate DEKs, securely rewrapping those DEKs under a replacement KEK may remove the operational need for \(K_0\), while leaving the underlying content encrypted under the **same DEKs**. The correct outcome depends on the actual key hierarchy and copies still retained. A declaration that “rotation succeeded” must therefore identify **which operations stopped**, **which keys became usable**, **which legacy ciphertexts remain readable**, and **which old material is still retained**.

A short cryptoperiod does not guarantee secrecy if the generation process is compromised. A long period may be inappropriate for a high-volume, high-exposure key even with strong algorithms. Usage quotas, nonce limits, protected-data horizon and operational recovery obligations can constrain the safe period independently of calendar age.

## Key hierarchies, wrapping and dependency scope

Key-management designs often separate a **data-encryption key (DEK)** that encrypts content from a **key-encryption key (KEK)** that protects the DEK, sometimes under a higher-level root. This separation permits some operations without processing all of the underlying data.

~~~text
Root of trust / master material
              |
             KEK_0  (wraps)
           /      \
          v        v
        DEK_A     DEK_B
          |        |
          v        v
       Data A    Data B
~~~

This diagram shows a *hypothetical dependency*. It is not evidence of a deployed service's cryptographic isolation or proof that the wrapping method meets a particular approved standard.

**Rewrapping** a DEK with a new KEK changes the wrapping of the key material; it does **not** automatically re-encrypt the content under that DEK. **Re-encrypting** content changes the content-encryption key and/or ciphertext, under rules appropriate to that cipher mode. **Rekeying** may refer to either operation in casual documentation, so precise system claims should say what actually changed.

A compromise of KEK_0 can give an attacker the ability to unwrap any DEK whose old wrapped copy they obtain under the stated algorithm and authorization assumptions. After replacing KEK_0 with KEK_1, an attacker who retained an old wrapped DEK and KEK_0 may still have access to the dependent DEK. **Future rotation cannot erase copied historical secrets or ciphertexts.** The recovery question is whether dependent keys and protected data need replacement, re-encryption, authorization changes or additional protection, not merely whether the central KEK is now different.

Physical location matters: exporting a key in plaintext, releasing it to an enclave, requesting a non-exportable module to decrypt, backing up a wrapped DEK, and logging a key identifier carry different security implications. “Hardware-backed” and “non-exportable” are meaningful only with a defined module boundary, threat model and implementation behavior.

## The key/nonce pair is a lifecycle obligation

An authenticated-encryption key can fail without the key bytes themselves being leaked. The security argument may depend on the **pair \((K,N)\)**, not on either input in isolation. If a key remains active while a sender's nonce counter resets, repeated key/nonce pairs can violate the assumptions of an otherwise correct AEAD implementation.

The companion [Randomness, Entropy, and Nonces](randomness-entropy-and-nonces.md) explains this mechanism, and [RFC 8439](https://www.rfc-editor.org/rfc/rfc8439.html) provides an algorithm-specific example for ChaCha20-Poly1305. Key-management design must link the **key epoch**, **sender namespace**, **nonce generation state**, **recovery mechanism** and **maximum usage volume**.

### Worked model: rotation calendar versus counter exhaustion

Consider a **fictional** AEAD application that lays out its 96-bit nonce as a 64-bit sender/domain prefix followed by a **32-bit local counter**. For one fixed prefix and one key, the implementation guarantees uniqueness only across the \(2^{32}\) available counter values. Assume that every request consumes one counter value, that a sender emits **1,000 requests per second**, and that no other constraint forces earlier retirement.

\[
2^{32} = 4{,}294{,}967{,}296 \text{ counter values},
\]

\[
T_{\max} = \frac{2^{32}}{1{,}000}
=4{,}294{,}967.296\ {\rm seconds}
\approx49.710\ {\rm days}.
\]

If the organization rotates keys on a **60-day** calendar while the same prefix/counter remains active and the system is continuously busy at the stipulated rate, that schedule is inadequate to prevent wraparound. This is a **toy format and usage calculation**, not a guaranteed operational cryptoperiod or a general AEAD limit. [RFC 5116 §3.2](https://www.rfc-editor.org/rfc/rfc5116.html) presents a *fixed field plus counter field* as a recommended nonce formation strategy, including a four-octet counter option for 12-octet nonces; actual protocol profiles may require different layouts, stronger limits or coordination. Counter capacity alone does not certify compliance with the algorithm's other message/byte usage bounds. Earlier algorithm-specific bounds, sender collisions, state rollback and failures may apply.

Changing only a display label for the key is not rekeying. Conversely, a genuinely fresh key epoch with correctly separated nonce state can reset an implementation-specific usage budget, provided the cryptographic protocol and deployment establish the new key scope.

## Compromise, revocation, rotation and recovery are not synonyms

Security systems frequently label all four activities as “rekey.” A defensible explanation separates their claim types:

| Event or action | What it can establish when correctly executed | What it cannot establish by itself |
| --- | --- | --- |
| Rotation / replacement | New operations begin using new authorized key material | Old copies and data are no longer compromised |
| Revocation | A relying party following relevant policy should reject a key or certificate for defined new decisions | All relying parties received the revocation or all past signatures are invalid |
| Suspension | Usage is temporarily restricted pending a decision | The underlying material has been recovered or securely destroyed |
| Erasure / destruction | A defined material copy becomes unavailable through a specified process | Every backup, memory copy, exported value and adversarial capture is gone |
| Recovery / restoration | Required authorized key functions become available again under a declared evidence model | The restored state is free of unauthorized access |
| Re-encryption | Specified data is transformed under replacement cryptographic protection | All historical plaintext/ciphertext copies ceased to exist |
| Crypto agility / migration | Supported algorithms or key formats can be changed under controlled policy | The new end-to-end protocol or implementation is automatically secure |

After suspected compromise, restoring **trust** may require identifying the interval of exposure, whether an adversary copied secrets, which dependent keys/data were affected, whether public trust bindings can be withdrawn, and how authenticated peers receive replacement material. A certificate revocation is not meaningful to a relying party that never checks or trusts the revocation signal.

Destroying one disk file may not destroy data retained in snapshots, swap, hardware, storage replicas, logs or distributed backups. Key destruction is a claim relative to controlled copies and storage lifecycles, not the metaphysical absence of all possible representations.

The source of a problem can also be procedural rather than mathematical: wrong key labels, incorrect access scopes, reused environments, weak audit evidence and emergency recovery accounts can undermine good cryptographic algorithms.

## Key derivation needs context and suitable input material

A **key-derivation function (KDF)** may take existing keying material and produce purpose-separated keys. This is not a substitute for a suitable source of initial secrecy.

[RFC 5869 (HKDF)](https://www.rfc-editor.org/rfc/rfc5869.html) defines an HMAC-based extract-and-expand construction. Its extract stage produces a pseudorandom key from input keying material and a salt, and its expand stage can use an **info** input to bind derived keys to application or protocol context. The salt is not required to be secret in that specification.

Conceptually:

~~~text
Suitable input keying material  +  protocol salt
                 |
                 v
             HKDF-Extract
                 |
                 v
          Pseudorandom key
                 |
         +-------+-------+
         v               v
  HKDF-Expand(info="send")  HKDF-Expand(info="receive")
         |               |
         v               v
   Traffic key A     Traffic key B
~~~

This schematic illustrates purpose separation, not valid literal protocol label encodings, an executable HKDF implementation or proof that the input has sufficient entropy. Reusing exactly the same input keying material, salt, information context and length reproduces the same deterministic output. **Context separation prevents some accidental key reuse only if its meanings, encodings and trust boundaries are correctly specified.**

The [Key Establishment and Trust Anchors](README.md) candidate area owns whether and how parties justifiably obtain a shared or authenticated key. No concrete article for that candidate is asserted here. The present subject explains what it means to *manage* the resulting material over time.

## Algorithm transitions and post-quantum migration

A cryptographic system has an algorithm lifecycle as well as key lifecycles. When an algorithm's security assumptions, approved strength or interoperability change, keys relying on it may require replacement or different protection.

[NIST SP 800-131A Revision 2 (2019)](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) remains a final published transition guideline; the [NIST key-management project](https://csrc.nist.gov/projects/key-management/key-management-guidelines) still lists **Revision 3 as a public draft / undergoing final review** in the checked publication status. It would be inaccurate to treat a proposed transition rule as a finalized requirement without checking its effective edition and applicability.

Post-quantum migration cannot be reduced to “make every symmetric key longer.” In August 2024, NIST standardized distinct post-quantum constructions:

- [**FIPS 203**](https://csrc.nist.gov/pubs/fips/203/final) specifies **ML-KEM**, a key-encapsulation mechanism for establishing shared secret material.
- [**FIPS 204**](https://csrc.nist.gov/pubs/fips/204/final) specifies **ML-DSA**, a digital-signature algorithm family.
- [**FIPS 205**](https://csrc.nist.gov/pubs/fips/205/final) specifies **SLH-DSA**, another digital-signature family.

A KEM and a signature algorithm are **not interchangeable keys or security functions**. A protocol using a quantum-resistant KEM still needs authenticated peer binding, suitable derivation, authorization, implementation protection, trust management, and migration compatibility controls. Scheme security is conditional on its actual specifications, parameters, implementation and threat model.

Critically, [NIST IR 8547, *Transition to Post-Quantum Cryptography Standards*](https://csrc.nist.gov/pubs/ir/8547/final) became **final in October 2026**, describing NIST's approach to migrating quantum-vulnerable public-key algorithms. It is a **transition roadmap**, not a certification that a specific organization has migrated or proof that a future quantum computer can already break a particular live connection. The policy significance of the report is jurisdiction- and system-dependent.

A long-lived confidentiality threat includes collecting encrypted material now for potential future cryptanalysis. Such a scenario may require earlier modernization for information whose confidentiality must persist for years, while authentication and signature migrations may carry different legacy-verification and trust-anchor problems.

## Failure taxonomy and defensible claims

The table is an **editorial** grouping of key-related failure mechanisms rather than an imported formal universal classification.

| Failure family | Illustrative mechanism | Security claim that fails or becomes uncertain |
| --- | --- | --- |
| Generation or entropy | Secret key derived from predictable state | Unpredictability of key material |
| Distribution or establishment | Public-key substitution or compromised transport of secrets | Binding of key to the expected party |
| Storage and access | Exfiltration of keying material or misuse of an authorized key-service API | Confidentiality or usage authorization |
| Key/nonce usage | Counter reset, reuse across senders or uncoordinated key epoch | Algorithm-specific authenticated-encryption security |
| Context or derivation | Same derived key used across incompatible purposes | Role/domain separation |
| Lifecycle management | Revoked certificate still trusted; retired key still generating new protection | Timely policy enforcement |
| Recovery and backups | Compromised KEK or DRBG state restored from an old snapshot | Trustworthy recovery state |
| Algorithm transition | Continued use of unsuitable legacy public-key protection | Suitability of cryptographic strength for protection horizon |

An observed failed certificate check does not automatically prove private-key compromise. A single missing key-inventory record does not demonstrate exfiltration. Conversely, a perfectly complete inventory is not evidence that no unauthorized key copies exist. Security evidence needs to match the proposition and observation boundary.

This subject's **cryptographic failure** language concerns protection assumptions and lifecycle states, not attribution to a malicious human or the operational conduct of incident response.

## Related knowledge and authoritative references

- [Randomness, Entropy, and Nonces](randomness-entropy-and-nonces.md) owns statistical and cryptographic unpredictability, entropy-source limits, and per-key nonce uniqueness.
- [Cryptographic Composition and Protocol Security](cryptographic-composition-and-protocol-security.md) owns AEAD, key schedule, context binding, replay and whole-protocol composition.
- [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns the claim/evidence basis for an assertion of trust in recovered material.
- [Recovery Objectives and Trusted Restoration](../security-failure-resilience/recovery-objectives-and-trusted-restoration.md) owns the distinction between functional restart and justified restored security state.
- [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) owns scope-relative compromise and the limits of incidental evidence.
- [Fundamentals: Information Theory](../../fundamentals/information-data/information-theory.md) owns entropy and information quantities outside cryptography; specialized [Identity](../../../identity/README.md), [Application](../../../application/README.md), [Endpoint](../../../endpoint/README.md), [Cloud](../../../cloud/README.md) and [Network](../../../network/README.md) own concrete key services and implementations.
- [Operational Foundations](../../operational-foundations/README.md) owns the *procedures* for key rotation, inventory, response, cryptographic migration, audits and recovery.

### Source register and version boundaries

- [NIST SP 800-57 Part 1 Rev. 5 (final, May 2020)](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), general key management, key roles, protection and lifecycle concepts; §5.3.5, printed pp. 37–38 (PDF indexes 49–50), was visually inspected for the originator-/recipient-usage cryptoperiod distinction.
- [NIST SP 800-57 Part 1 Rev. 6 (Initial Public Draft, Dec. 2025)](https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd), proposed updates and current draft status. **Not a final normative source** in this working edition.
- [NIST SP 800-133 Rev. 2 (final, 2020)](https://csrc.nist.gov/pubs/sp/800/133/r2/final), cryptographic key generation. [Rev. 3 (Initial Public Draft, April 2026)](https://csrc.nist.gov/pubs/sp/800/133/r3/ipd) is proposed, not final.
- [NIST SP 800-131A Rev. 2 (final, 2019)](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final), transition of algorithms and key lengths; [NIST key-management project](https://csrc.nist.gov/projects/key-management/key-management-guidelines) notes revision 3 draft status.
- [NIST IR 8547 (final, October 27, 2026)](https://csrc.nist.gov/pubs/ir/8547/final), roadmap for post-quantum cryptography transitions, not a deployed-system assurance report.
- [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) (ML-KEM), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) (ML-DSA), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) (SLH-DSA), final August 2024, distinct quantum-resistant algorithm families; FIPS 203 has a potential-update notice on its publication page.
- [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869.html), HKDF extract/expand, salt, context binding and derivation limits.
- [RFC 8439](https://www.rfc-editor.org/rfc/rfc8439.html), ChaCha20-Poly1305 key/nonce pairing as a particular AEAD obligation.

**Editorial limits:** Lifecycle states, diagrams, algorithms and worked numeric budgets are bounded **explanatory models** and not a standard-mandated key-management architecture, real-world deployment assessment, cryptographic security proof or migration plan. The separate [Technical Review 06](../PILOT-TECHNICAL-REVIEW-06.md) now records ten claim groups, NIST edition checks, visual inspection of the originator/recipient cryptoperiod distinction, mathematical recomputation and role-dependent key-migration corrections. Complete source-passage verification, independent expert acceptance, taxonomy ratification and Published status remain open.

[Security Foundations](../README.md) · [Working area](README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
