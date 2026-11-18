# Randomness, Entropy, and Nonces

**Candidate subject:** SF-09-02 · Cryptography & Information Protection  
**Working area:** [Cryptography & Information Protection](README.md) · Fundamentals-style structure adopted; subject ownership and area taxonomy remain provisional  
**Artifact type:** Substantive working security-knowledge reference, not a permanently approved canonical publication  
**Development state:** Draft · **Source-review state:** References listed; original standards and source status checked during authoring, **separate claim-led technical Review batch pending**  
**Architecture:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Source crosswalk](../ESTABLISHED-MODEL-CROSSWALK.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)

## Randomness, entropy, and uniqueness solve different security problems

Cryptographic systems frequently require values an adversary cannot predict, values that will not repeat, or values that distinguish one operation from another. These requirements overlap, but no one term describes all three.

A **random variable** is specified by a probability distribution over possible values. **Entropy** quantifies uncertainty under that distribution and a particular notion of uncertainty; in security analysis, the relevant quantity depends on the attacker's prior information and capabilities. A **cryptographically secure pseudorandom generator** produces outputs computationally difficult to distinguish from suitable random outputs under defined assumptions, despite being a deterministic function of internal state. A **nonce** is a value used for a particular cryptographic invocation or exchange, often to prevent repetition of relevant inputs. Its obligation to be unique, unpredictable or both is determined by the *specific algorithm and protocol*, not by the word “nonce.”

A perfectly predictable, never-repeating counter can be suitable as a nonce for one construction. It is **not** a suitable secret encryption key. A secret drawn unpredictably may be an excellent key, while independent random nonce generation can still create accidental repetitions as the number of invocations grows.

| Requirement | Meaning under a declared model | Example | A wrong inference |
| --- | --- | --- | --- |
| Unpredictability | An observer cannot feasibly anticipate a value before disclosure, given their view | Seed material for a cryptographic generator | “It looks irregular, so an attacker cannot predict it” |
| Uniqueness | Values used within a relevant scope do not repeat | Distinct AEAD nonce for each invocation under one key | “It is a long random string, so it cannot collide” |
| Freshness | The value/action meets an exchange-specific temporal or anti-replay rule | A challenge bound to one authentication session | “The nonce was once unique, so a repeated request is always rejected” |
| Secrecy | Unauthorized principals cannot learn protected information | A private key or generator's secret state | “The nonce must be secret for every encryption scheme” |
| Statistical entropy | A modeled source has measurable distributional uncertainty | A physical noise source under validation assumptions | “A hash expands the amount of entropy supplied” |

The subject connects to [Key Lifecycle and Cryptographic Failures](key-lifecycle-and-cryptographic-failures.md), which owns how cryptographic keys are generated, protected, rotated and retired, and to [Cryptographic Composition and Protocol Security](cryptographic-composition-and-protocol-security.md), which owns how primitives, nonce obligations, transcript context and anti-replay properties interact in protocols.

## The anatomy of a trustworthy random-bit generator

Randomness is not normally delivered to a cryptographic application by sampling ambient signals and calling the raw bytes “secure.” A defensible design specifies how uncertainty is obtained, estimated, conditioned and carried into generator state.

~~~text
Physical / other noise phenomenon
               |
               v
        Sampling process
               |
               v
     Entropy-source evaluation
     health tests / conditions
               |
               v
  Conditioning and entropy estimate
               |
               v
      Generator instantiation
   seed material + secret state
               |
               v
  Deterministic generation / reseeding
               |
               v
 Keys, salts, challenges, and other values
       each with its own usage rules
~~~

This diagram is an explanatory decomposition, not a literal claim that every approved NIST construction contains one identical set of components or that every failure is captured by a single health test.

The [NIST SP 800-90 series](https://csrc.nist.gov/projects/random-bit-generation/publications) assigns different source-defined responsibilities:

- **SP 800-90B (final, 2018):** entropy-source design, health testing and estimation of entropy; its [publication page](https://csrc.nist.gov/pubs/sp/800/90/b/final) notes errata identified in 2025.
- **SP 800-90A Revision 1 (final, 2015):** deterministic random bit generator (**DRBG**) mechanisms using cryptographic constructions based on hash functions or block ciphers, including state/seed handling. [Rev. 2 remains a pre-draft proposal in the current NIST project listing](https://csrc.nist.gov/projects/random-bit-generation/publications).
- **SP 800-90C (final, September 2025):** complete random bit generator (**RBG**) constructions combining relevant DRBG and entropy-source capabilities, with separate RBG1/RBG2/RBG3/RBGC classes. [NIST publication](https://csrc.nist.gov/pubs/sp/800/90/c/final).

An entropy source can pass a statistical health check and still fail outside its tested environmental conditions. A DRBG can implement an approved algorithm while receiving weak or duplicated initial state. A system can gather strong initial entropy yet expose its generator state through memory disclosure, debugging, virtualization or a compromised dependency.

**The whole generation path is the security boundary.** Compliance with an individual generator primitive does not automatically establish an application's end-to-end key unpredictability.

## The difference between Shannon entropy and min-entropy

Not all entropy measures answer the same question. For discrete \(X\) with probabilities \(p_x\), Shannon entropy is

\[
H(X)=-\sum_x p_x \log_2 p_x.
\]

The **min-entropy** of the distribution is

\[
H_\infty(X)=-\log_2\bigl(\max_x p_x\bigr).
\]

Shannon entropy measures average information-theoretic uncertainty, while min-entropy bounds the success probability of the single most likely guess under the *specified distribution*. Predictability under an adversary's available side information is not captured by blindly computing either quantity from unconditioned output frequencies.

### Worked example: biased bits

Suppose a toy source emits 1 with probability \(0.75\) and 0 with probability \(0.25\). Assume for this example that each sample is identically distributed and independent of previous samples, and that the attacker knows these probabilities.

\[
H(X)=-0.75\log_2 0.75-0.25\log_2 0.25
\approx 0.811278\ {\rm bits/sample}.
\]

\[
H_\infty(X)=-\log_2 0.75\approx0.415037\ {\rm bits/sample}.
\]

The most likely guess succeeds with probability 0.75 for one sample. Under the stipulated **independent** samples, the probability of guessing the entire \(n\)-sample vector by always choosing its most likely outcome is \(0.75^n\), and the min-entropy of the vector is \(n\,H_\infty(X)\). If the samples are correlated, or if an attacker learns relevant hidden state, that multiplication may be invalid.

An ordinary program printing a long hash of a constant input still contains **zero fresh unpredictability** to an attacker who knows the input and algorithm. Deterministic processing can condition and distribute the unpredictability it receives under relevant assumptions, but cannot create independent secret entropy from known data.

Statistical tests also cannot prove unpredictability against every computationally capable observer. An excellent-looking sequence may be generated from a public seed and be completely predictable to someone who knows it.

## Deterministic expansion is not a contradiction

A DRBG is deterministic given its internal state and input. Its usefulness comes from the difficulty of predicting its output *without* knowing the protected state, assuming the mechanism remains within its specified security strength and operational limits.

Relevant states and transitions include **instantiation**, **generation**, **reseed**, and **uninstantiation**. They carry separate questions:

- Was the initial seed derived from an appropriately characterized entropy source?
- Could two processes receive the same secret state, for example by cloning a virtual-machine image or restoring an unmodified snapshot?
- Can an attacker recover state through process memory, tracing, logs, or compromised infrastructure?
- When and how is entropy incorporated again, and how do failures propagate?
- Are outputs used as keys, long-term secrets, nonces, or public labels under compatible requirements?

A reseed may restore some desired protections under a mechanism's explicit model. It does not retroactively erase an adversary's copies of past ciphertexts, compromised keys, or revealed prior outputs. Some generators define **prediction resistance** or **backtracking resistance** relative to specified attack states and reseeding behavior; neither should be inferred solely from one successful randomness test.

The generator also cannot justify **nonce uniqueness** by itself when the application needs a hard no-repeat guarantee across concurrency, restarts, shards, sender identities or key epochs.

## Nonces, initialization vectors, challenges, salts and counters

The same number of bits may be placed into different protocol fields and serve fundamentally different purposes.

| Value | Primary job | Secrecy / unpredictability / uniqueness requirement |
| --- | --- | --- |
| Nonce in an AEAD construction | Distinguish invocations under a key and support algorithm-specific security bounds | Often **unique per key**, not secret; exact rules depend on the AEAD |
| Initialization vector (IV) | Initialize a specified cipher mode | Mode-specific: some need unpredictable IVs, others demand strict uniqueness |
| Challenge nonce | Bind a response to a particular live exchange or proof | Usually requires freshness; unpredictability may prevent precomputation in the threat model |
| Password salt | Distinguish password-hash computations and resist amortized precomputation | Typically public; appropriate length, uniqueness and generation rules depend on the password scheme |
| KDF salt | Supply the derivation function's defined salt input | In [HKDF](https://www.rfc-editor.org/rfc/rfc5869.html) it need not be secret; recommendation depends on the protocol |
| Sequence or monotonic counter | Track ordered operations or construct a unique input in a persistent scope | Predictable is often acceptable; **repetition across reset/wraparound is not** |
| Cryptographic secret key | Supply the private secret to a cryptographic construction | Must meet scheme-specific strength and confidentiality requirements; uniqueness alone does not suffice |

These labels are not globally disjoint. Some standards use *IV* as the concrete input that functions as a nonce, and some handshake specifications call values “random” while additionally requiring their cryptographic role to be precisely defined.

For the widely used [RFC 8439 AEAD_CHACHA20_POLY1305](https://www.rfc-editor.org/rfc/rfc8439.html), the 96-bit nonce must **not repeat with the same key**; the RFC expressly recommends generating it so that uniqueness is assured rather than assuming that random sampling can never collide. Its counter and multi-sender examples are protocol-specific. [RFC 5116](https://www.rfc-editor.org/rfc/rfc5116.html) describes the authenticated-encryption interface and nonce handling, and [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) specifies GCM/GMAC IV requirements. The latter remains a 2007 final publication with a revision announced in 2024; readers must not assume that every AEAD inherits one mode's nonce rules.

## The birthday collision is a probability, not a uniqueness guarantee

For **independent uniformly sampled \(n\)-bit values**, the probability of at least one duplicate among \(q\) draws, for \(q\le 2^n\), is

\[
P_{\mathrm{collision}}
=1-\prod_{i=0}^{q-1}\left(1-\frac{i}{2^n}\right).
\]

When \(q\) is substantially smaller than the space of values, a common approximation is

\[
P_{\mathrm{collision}}
\approx 1-\exp\left(-\frac{q(q-1)}{2^{n+1}}\right).
\]

As an **illustrative statistical counterexample**, choose a 64-bit value randomly for each of \(q=2^{32}\) independent requests. The approximation gives

\[
P_{\mathrm{collision}}
\approx 1-e^{-1/2}\approx0.39347,
\]

or about **39.3% chance of at least one repeat**. That is *not* the collision probability of every 64-bit field or of properly managed deterministic 64-bit counters. It follows only from this uniform independent sampling model and volume.

A counter that is never reset, wrapped or shared incorrectly can meet a defined uniqueness obligation without any randomness whatsoever. But a counter stored only in volatile memory may repeat after power loss. A server farm whose instances use the same key and begin counters at zero may generate duplicate key/nonce pairs even though each instance is locally monotonic.

**Uniqueness is a system property of key scope, state ownership and lifecycle**, not a visual property of nonce bytes.

## What repeated key/nonce pairs can break

A nonce error becomes important because of *how the cryptographic algorithm uses that nonce*. The consequences are not interchangeable across all constructions.

For a stream-cipher-style encryption using the same effective keystream \(Z\) twice,

\[
C_1=P_1\oplus Z,\quad C_2=P_2\oplus Z
\quad\Rightarrow\quad C_1\oplus C_2=P_1\oplus P_2.
\]

The equality is an algebraic identity under the repeated-keystream assumption. It explains why recovering relationships between otherwise secret messages may become possible. For the concrete ChaCha20-Poly1305 AEAD in RFC 8439, reusing the key/nonce pair also repeats the one-time Poly1305 key and undermines authenticity protections, but a particular attack's outcome still depends on its messages and observation conditions.

GCM nonce reuse has different internal algebra and potentially severe confidentiality/authenticity consequences under its own standard and threat model. Do not import a ChaCha-specific failure story into every GCM case, or infer that merely detecting a repeated public field proves a successful forgery.

The correct response to a suspected collision is to establish the **actual key and nonce scopes**, algorithm, state, affected messages and evidence of reuse. Replacing one bad nonce after the fact does not retroactively re-protect ciphertexts created under a reused pair.

## Generation failures that span devices and time

A security argument about random inputs and unique nonces must consider more than the algorithm source file. Typical failure modes include:

1. **Predictable seed state:** a time, PID, public counter or user-supplied string is mistaken for a secret entropy source.
2. **Identical generator snapshots:** cloned instances resume with matching DRBG state and produce identical outputs.
3. **Counter rollback:** recovery from a snapshot resets a nonce sequence while the cryptographic key remains in use.
4. **Multi-sender collisions:** two nodes choose the same per-key nonce namespace without coordination.
5. **State disclosure:** process compromise reveals generator state or key material, making otherwise strong algorithms unable to meet their original threat assumptions.
6. **Incorrect implementation boundaries:** a correct primitive is called with the wrong key epoch, truncated identifier, nonce width, or encoding.
7. **Unavailable or degraded entropy source:** a deployment continues generating sensitive keys despite an unresolved source-health or instantiation failure.

These are plausible *mechanisms*, not allegations about a particular vendor or proof that every incident resulted in compromise. The appropriate design may separate sender nonce namespaces, persist monotonic state with crash-safety assumptions, rekey on recovery, or rely on a protocol-specific randomness and key-management design. Whether a given change actually satisfies a standard requires implementation evidence.

## Canonical boundaries and sources

- [Key Lifecycle and Cryptographic Failures](key-lifecycle-and-cryptographic-failures.md) owns generation/ownership/protection/retirement and the response to compromised or duplicated keying material.
- [Cryptographic Composition and Protocol Security](cryptographic-composition-and-protocol-security.md) owns how AEAD nonce, authentication, transcript binding and replay rules combine into a secure protocol.
- [Information-Flow Security and Noninterference](../secure-design-architecture/information-flow-security-and-noninterference.md) addresses observable influences of secrets beyond direct access.
- [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) addresses what logs and observations can substantiate about alleged misuse.
- [Fundamentals: Information Theory](../../fundamentals/information-data/information-theory.md) owns general mathematical information quantities, not security-specific cryptographic guarantees.
- [Fundamentals: Probability and Statistics](../../fundamentals/mathematics-logic/README.md) owns general probability mechanisms and assumptions, including independence and conditionality.
- [Operational Foundations](../../operational-foundations/README.md) owns actual key-generation validation, forensic investigation and response workflows; specialized [Network](../../../network/README.md), [Endpoint](../../../endpoint/README.md), [Application](../../../application/README.md) and [Identity](../../../identity/README.md) knowledge own concrete implementations.

### Primary source starting points and status

- [NIST Random Bit Generation project publication register](https://csrc.nist.gov/projects/random-bit-generation/publications): source status for **SP 800-90A Rev.1 final (2015)**, **90B final (2018, 2025 errata noted)**, and **90C final (September 2025)**. **90A Rev.2 is a 2025 pre-draft call**, not a final standard as of this edition.
- [NIST SP 800-90A Rev.1](https://csrc.nist.gov/pubs/sp/800/90/a/r1/final), DRBG constructions and state model.
- [NIST SP 800-90B](https://csrc.nist.gov/pubs/sp/800/90/b/final), entropy-source characterization, estimation and health testing.
- [NIST SP 800-90C](https://csrc.nist.gov/pubs/sp/800/90/c/final), complete random-bit generator constructions and defined RBG classes.
- [RFC 8439](https://www.rfc-editor.org/rfc/rfc8439.html), ChaCha20-Poly1305 nonce and repeated-key/nonce consequences, especially §§2.8, 4.
- [RFC 5116](https://www.rfc-editor.org/rfc/rfc5116.html), authenticated-encryption interface, nonce formation and uniqueness scope.
- [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final), GCM/GMAC modes and IV constraints; final 2007 with later revision planning.
- [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869.html), HKDF extraction, expansion, non-secret salt and contextual separation.

**Editorial limitation:** The entropy and collision examples are mathematics under *stipulated distributions and independence*, not results of a real RNG or measured security incident. The article makes no claim that passing statistical tests proves entropy-source validation or that a universal rule applies to all AEAD algorithms. Its source references and calculations require a **separate scoped Review batch** with article-specific claim groups before the manuscript may become Reviewed (model-assisted). Full standards-passage verification, expert peer review, taxonomy ratification and publication acceptance remain open.

[Security Foundations](../README.md) · [Working area](README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
