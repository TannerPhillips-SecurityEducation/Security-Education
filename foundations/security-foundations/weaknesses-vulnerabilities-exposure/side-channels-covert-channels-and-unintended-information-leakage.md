# Side Channels, Covert Channels, and Unintended Information Leakage

**Candidate subject:** SF-04-08 · Weaknesses, Vulnerabilities & Exposure  
**Working area:** [Weaknesses, Vulnerabilities & Exposure](README.md) · Fundamentals-style directory pattern adopted; area membership and subject ownership remain provisional  
**Artifact type:** Substantive security-knowledge working manuscript, not an approved canonical publication  
**Development state:** Draft · **Source-review state:** References listed; official terminology and source scopes consulted during drafting, **separate material-claim technical review pending**  
**Architecture:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Gap review SG-02](../COVERAGE-AND-GAPS-REVIEW-03.md) · [Working ownership](../CANONICAL-OWNERSHIP-REGISTER.md)

## Information may cross a boundary without an authorized read

A system can correctly prevent an unauthorized process from opening a protected file and still reveal something about its contents through the time taken to process a request, a shared resource's changing state, an emitted signal, or a diagnostic record. **Preventing direct access to a value does not necessarily prevent the value from influencing an observable effect.**

This subject examines three related but non-equivalent concepts:

- A **side channel** is an indirect observation path in which behavior or physical effects of an operation provide information about otherwise protected state. A source need not intentionally transmit a message, and an observer may choose inputs or repeat measurements.
- A **covert channel**, in the classical security-policy sense, is an unintended or unauthorized communication path by which *cooperating entities* transfer information contrary to a defined flow policy while using capabilities the system otherwise permits them. It often relies on shared timing or storage behavior.
- **Unintended information leakage** is a broader outcome or potential weakness: information that policy or design intended to restrict becomes available through some inadequately controlled representation, action, output, or side effect. Leakage can occur through a side channel, a covert channel, a misconfigured log, or a direct but inappropriate response. Those paths are not all of the same type.

The [NIST side-channel glossary](https://csrc.nist.gov/glossary/term/side_channel) discusses inference from execution time, memory behavior, and indirect hardware effects. The [NIST covert-channel glossary](https://csrc.nist.gov/glossary/term/covert_channel), drawing on the CNSSI 4009-2022 and RFC 4949 vocabulary, emphasizes cooperating entities and security-policy violation. [MITRE CWE-208](https://cwe.mitre.org/data/definitions/208.html) describes observable timing discrepancies, while [CWE-514](https://cwe.mitre.org/data/definitions/514.html) describes covert communication paths. These sources classify related phenomena using different units of analysis; their labels should not be made synonymous.

## Anatomy of an information-leakage claim

To reason about any proposed channel, name the **protected information**, the **intended policy**, the **producer of a signal**, the **resource or behavior carrying the signal**, the **recipient's actual observation**, and the **conditions under which that observation could convey forbidden information**.

| Element | Technical question that determines the claim |
| --- | --- |
| Protected value or state | What fact is meant to remain unavailable to this observer: a key bit, record existence, authorization state, identity, or other information? |
| Policy and boundary | Which principal or compartment may know that fact? Is the alleged flow actually forbidden, permitted, or explicitly declassified? |
| Source and influence | What computation, process, device, or cooperating sender can cause a relevant observable difference? |
| Channel resource | Is the carrier execution latency, cache occupancy, queue depth, power, storage flags, message metadata, or another variable? |
| Observation model | What can the recipient read or measure, with what resolution, placement, permissions, timing, and noise? |
| Decoding or inference | How might observable variations distinguish protected states or encode sender-selected symbols? |
| Evidence and limits | Is there only a theoretical possibility, a measured dependency, a demonstrated recovery, or an observed real disclosure? |

The essential security proposition is conditional: **under a particular threat model and policy, the observer can distinguish or recover a protected property from an available signal**. It is not enough to observe that a device has varying execution times or emits electromagnetic energy. There must be a defensible relation between *what is protected* and *what is observable*.

The general distinctions among a [weakness, vulnerability and exploitability](vulnerabilities-and-exploitability.md) apply. A candidate leakage mechanism is not automatically reachable, exploitable, successfully exploited, or evidence of compromise.

## Side channels: incidental influence becomes an observation

A side-channel mechanism can be expressed as a causal chain:

~~~text
Protected information S
           |
           v
Computation / system behavior     <--- public inputs and environment
           |
           v
Observable side effect Y
           |
   sensor / timing / measurement
           v
Observer's evidence about S
~~~

The authorized operation may produce the correct public answer, but its *way of operating* can depend on a secret. The observer does not require a cooperating insider. The observer does require some feasible measurement capability and enough signal to support the claimed inference.

Side effects can arise from several physical or logical sources:

| Carrier | Illustrative effect | Important qualification |
| --- | --- | --- |
| Execution time | Secret-dependent early termination changes response latency | Network scheduling and jitter may obscure, but do not automatically erase, a statistical dependency |
| Memory and shared caches | Secret-influenced memory accesses affect shared-resource occupancy or access time | A shared microarchitecture and observer vantage are prerequisites in the specific case |
| Power, electromagnetic or acoustic effects | A device's physical behavior varies with internal work | The observer needs a suitable physical sensor, proximity, and measurement conditions |
| Resource consumption | Queue length, CPU load, storage activity, or contention depends on protected activity | Correlation may reflect public workload or third-party causes instead of the protected value |
| Protocol/response metadata | Length, ordering, presence of fields, or error category exposes internal state | Some metadata is explicitly permitted; other cases are direct output disclosure rather than a side channel |

A leak through an *explicit error message* identifying a private record can be an ordinary unauthorized output. Its existence does not require a timing side channel. Conversely, timing variation may be a side-channel weakness even if the application returns identical success/failure text for every candidate secret state.

### Inspectable timing example

Imagine a hypothetical service comparing a caller-provided candidate with a secret sequence. Its comparison routine stops at the first mismatch. For otherwise equivalent inputs, the amount of work increases with the number of matching leading positions. A caller who can submit repeated candidates and observe timing may learn something about how much of a prefix matched.

This is the behavioral family behind [MITRE CWE-208](https://cwe.mitre.org/data/definitions/208.html). It does **not** follow that every early-exit comparison is remotely exploitable: the secret's reuse, API exposure, timing resolution, rate limits, concurrent load, implementation behavior, and attacker control of inputs all matter.

Now consider a counterexample. A routine's execution time varies with an **already public** input size, and the remaining secret-dependent work does not produce a distinguishable effect under the declared observation model. The variable timing alone is not evidence of additional secret disclosure. If the public input's size itself encodes restricted information, that becomes a different policy and source-of-dependency question.

## Covert channels: cooperating entities repurpose a resource

A covert channel has a different causal organization. One cooperating entity is able to influence an allowed resource state; another can observe the consequence. The resource is **not intended as a policy-authorized message carrier between them**.

~~~text
Protected-side sender               Unprivileged-side receiver
       |                                      ^
       |  modulates allowed resource use       | measures/reads
       v                                      |
     Shared storage state or timing behavior
                  |
        Policy-forbidden information transfer
~~~

Two classical mechanisms are especially useful:

- **Covert storage channel:** one entity sets or influences a storage location, flag, status field, shared identifier, or other persistent/readable state, and the receiver interprets it as encoded information. The [NIST covert-storage-channel glossary](https://csrc.nist.gov/glossary/term/covert_storage_channel) and [MITRE CWE-515](https://cwe.mitre.org/data/definitions/515.html) describe this class.
- **Covert timing channel:** a sender modulates its use of a shared resource or the schedule of activity; the receiver recognizes differences in observed delays or event timing. The [NIST covert-timing-channel glossary](https://csrc.nist.gov/glossary/term/covert_timing_channel) and [MITRE CWE-385](https://cwe.mitre.org/data/definitions/385.html) provide source-scoped descriptions.

As a simplified thought experiment, two otherwise isolated processes may both be permitted to observe a shared workload indicator. A high-trust sender can deliberately increase or decrease resource use in agreed observation intervals; a lower-trust receiver interprets those changes as symbols. If the policy forbids communication across that boundary, the *combined behavior* can constitute a covert channel despite each permitted resource operation remaining within its local access authorization.

This is an illustrative design model, not an implementation recipe or a demonstrated exploitation result. A timing side effect that unintentionally reveals a program's own secret need **not** involve a cooperating sender and is more accurately called a side channel in this context. The same resource can support different channel classifications depending on actor cooperation, policy, and causal mechanism.

## How much information can an observation convey?

A channel should be assessed using more than its mere existence. A relevant quantitative question is whether the observable signal reduces uncertainty about a protected variable *after the public context is accounted for*.

Let **S** denote a modeled secret, **Y** the observation, and **L** the publicly available inputs and conditions. In an explicitly probabilistic model, the **conditional mutual information**

\[
I(S;Y\mid L) = H(S\mid L) - H(S\mid Y,L)
\]

measures how much observing Y reduces uncertainty about S, *on average, under the chosen probability distribution*. A model with \(I(S;Y\mid L)=0\) has no additional statistical information about S in Y **within that model**. It is not a field certification that all unmodeled observations, inputs, times, or physical effects are safe. Mutual information also does not, by itself, identify the causal mechanism or a real person's intent.

For deliberately encoded covert communication, a related but different question is **channel capacity**: the maximum reliable information rate permitted by a specified channel model under its constraints. Rate depends on signaling opportunities, noise, synchronization, resource limits, and coding assumptions. NIST SP 800-53 Rev. 5, control [SC-31: Covert Channel Analysis](https://csrc.nist.gov/projects/cprt/catalog), addresses examining potential covert storage/timing avenues and analyzing their bandwidth; it does not define one universal numerical rate for all systems.

### Worked model: noisy binary resource channel

Suppose **hypothetically** that cooperating entities could use a shared state for at most **four symbol intervals per second**. Each intended binary symbol is independently flipped with probability \(p=0.1\), symmetrically for zeros and ones. Assume the receiver can distinguish intervals and that this channel is adequately modeled by a *binary symmetric channel*.

Its standard Shannon capacity in **bits per channel use** is:

\[
C_{\mathrm{use}}=1-H_2(p), \qquad
H_2(p)=-p\log_2(p)-(1-p)\log_2(1-p).
\]

For \(p=0.1\), \(H_2(0.1)\approx 0.468996\), so

\[
C_{\mathrm{use}}\approx0.531004\ \text{bits/use},
\qquad
C_{\mathrm{ideal}}\leq 4C_{\mathrm{use}}\approx2.124018\ \text{bits/s}.
\]

The inequality acknowledges the explicitly stipulated ceiling of four channel uses per second. The binary symmetric channel formula is an ideal asymptotic model, not an observed transport rate. The underlying asymptotic result assumes an appropriate encoder/decoder, arbitrarily long blocks in principle, the stationary independent symmetric noise model, and otherwise ideal timing. A simple uncoded receiver does **not** automatically achieve this rate. Synchronization, resource contention, distribution shifts, finite messages, defensive controls, and threat-model restrictions may reduce the achievable rate substantially.

Under that same ideal binary model, zero flip probability permits one bit/use, whereas \(p=0.5\) makes the observation statistically independent of the input and gives zero capacity. **Adding random delay is not a general proof of eliminating a timing leak**: whether it changes the relevant conditional distribution or merely increases measurement cost must be established.

The model illustrates how leakage claims can be quantified without presenting a fictional “measured exfiltration bandwidth.” No measurements of a real device, application, network, or attacker are asserted.

## Conditions necessary to substantiate a leakage claim

Several questions control whether a modeled channel becomes a defensible security finding.

**Policy:** Is the recipient barred from learning the relevant fact? A public status signal is not a breach merely because another process can observe it. The relevant protection objective must be explicit.

**Influence:** Can the protected value or a sender actually affect the observed resource? A coincidental timing pattern does not establish a secret-dependent computation.

**Access and location:** Can the observer measure the signal at sufficient fidelity? Physical distance, isolation, operating-system permissions, network path, sampling limits, and process scheduling can change the answer.

**Distinguishability:** Are distributions or decoded states separable beyond sampling bias and noise? Repeated observations can help, but only when the model and dependencies justify combining them. One visible delay is usually inadequate evidence of key recovery.

**Control, cooperation, and intent:** Is there one process involuntarily revealing information, or cooperating entities deliberately encoding it? An observed pattern may be compatible with cooperation without proving who intended it.

**Evidence:** A vulnerability hypothesis, a controlled demonstration, a quantified leakage rate, and a confirmed past incident are distinct claims. Confidence should track the actual experiment and source provenance.

The [Security Observation & Evidence](../security-observation-evidence/README.md) area owns how to assess observations and uncertainty. Incident investigation, red-team testing, monitoring, and remediation workflows belong to [Operational Foundations](../../operational-foundations/README.md), not to this conceptual article.

## Mitigation must address the actual mechanism and boundary

There is no single universally effective “side-channel fix.” Security engineering can reduce exploitable information flow through complementary mechanisms:

| Protective approach | What it tries to change | What it does not automatically prove |
| --- | --- | --- |
| Secret-independent algorithms and implementations | Reduce secret-dependent differences in operations visible to an attacker | Source-level constant-time intent is not a guarantee across compilers, caches, hardware, and surrounding protocol behavior |
| Architectural separation and isolation | Remove or reduce shared observation resources, privilege paths, or physical proximity | Logical isolation may leave shared cache, scheduler, power, and service metadata |
| Uniform externally visible behavior | Reduce differences in error messages, response sizes, timing, or metadata when appropriate | Padding and random jitter do not necessarily remove distributional differences or indirect effects |
| Restricting measurement or repeated access | Reduce feasible sampling, query budget, or receiver access | Rate limiting can make exploitation harder without eliminating a channel or its theoretical capacity |
| Explicit information-flow design | Define permitted influence and declassification; constrain unauthorized signaling paths | A formal model proves only what its semantics, observer, and implementation assumptions cover |
| Mechanism-specific evaluation | Examine leakage under relevant observers, data classes, loads, and hardware conditions | A finite suite of passing measurements does not establish an unconditional absence of leakage |

In NIST SP 800-53, **SC-31** is an *analysis-oriented security control*, not a promise that every system must eliminate every conceivable covert channel or that selecting a control establishes its effectiveness. The original [RFC 4949 glossary](https://www.rfc-editor.org/rfc/rfc4949.html) is *Informational* (2007), not a normative Internet Standard; its vocabulary is useful with that authority limit. Similarly, CWE entries describe **weakness classes**, not proof that a specific target leaks information.

Good mitigation decisions also respect availability, performance, and safety constraints. Eliminating all shared resources is seldom feasible. A justified security claim identifies the unacceptable information flow, the observer and workload, the reduction strategy, and the evidence that the remaining behavior is acceptable under declared assumptions.

## Canonical boundaries and cross-domain relationships

This subject owns **leakage mechanisms, cooperating covert signaling, observation prerequisites, uncertainty, and security-weakness significance**. It does not take over the separate policy model, low-level hardware design, protocol implementation, or operational detection method.

- [Information-Flow Security and Noninterference](../secure-design-architecture/information-flow-security-and-noninterference.md) (SF-08-09) owns **formal flow policy, noninterference properties, proof models, and the meaning of a permitted influence**. This SF-04-08 draft instead explains ways observable effects can violate or appear to violate those properties.
- [Vulnerabilities and Exploitability](vulnerabilities-and-exploitability.md) (SF-04-02) owns the general difference among weakness, vulnerability, exposure, precondition, and actual violation.
- [Observable, Observed, and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) and [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) own what can be concluded from a measured effect and its records.
- [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md) owns distinct protected interests and the limits of reducing privacy or safety to a narrow confidentiality test.
- [Fundamentals: Conceptual and Formal Models](../../fundamentals/models-abstraction/conceptual-and-formal-models.md) provides the general distinction between a model, its assumptions, and its real implementation. [Fundamentals: Information & Data](../../fundamentals/information-data/README.md) owns generic representation and information mechanisms.
- [Endpoint](../../../endpoint/README.md), [Network](../../../network/README.md), [Application](../../../application/README.md), [Cloud](../../../cloud/README.md), [Industrial](../../../industrial/README.md), and [IoT](../../../iot/README.md) own actual hardware, resource scheduling, protocol, software, and physical-process implementations. [Operational Foundations](../../operational-foundations/README.md) owns execution of security testing and response.

## Source register and outstanding verification

- [NIST glossary: Side Channel](https://csrc.nist.gov/glossary/term/side_channel), source-attributed to NIST AI 100-2e2025; provides a bounded description of inference from program and hardware behavior.
- [NIST glossary: Covert Channel](https://csrc.nist.gov/glossary/term/covert_channel), source-attributed to CNSSI 4009-2022 and NIST SP 800-53 Rev. 5; differentiates cooperating policy-violating communication from incidental observation.
- [NIST glossaries: Covert Storage Channel](https://csrc.nist.gov/glossary/term/covert_storage_channel) and [Covert Timing Channel](https://csrc.nist.gov/glossary/term/covert_timing_channel), source-attributed to CNSSI 4009-2022 / NIST SP 800-53 Rev. 5.
- [MITRE CWE-208: Observable Timing Discrepancy](https://cwe.mitre.org/data/definitions/208.html), [CWE-514: Covert Channel](https://cwe.mitre.org/data/definitions/514.html), [CWE-515: Covert Storage Channel](https://cwe.mitre.org/data/definitions/515.html), and [CWE-385: Covert Timing Channel](https://cwe.mitre.org/data/definitions/385.html), descriptive weakness classes; relationship hierarchies are a catalog, not proof of any one real vulnerability.
- [NIST Cybersecurity and Privacy Reference Tool](https://csrc.nist.gov/projects/cprt/catalog), SP 800-53 Rev. 5 Release 5.2.0 (August 2025), including control SC-31 Covert Channel Analysis. An identified control requirement or bandwidth estimate is not a demonstrated exploit.
- [IETF RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) (2007), an *Informational* glossary, not an Internet Standard; source for the classic storage/timing/cooperation distinctions.

**Editorial limits:** The binary symmetric channel and shared-resource examples are expressly hypothetical and depend on the listed assumptions. This manuscript has **References listed / Draft** status. Formal mutual-information and channel-capacity equations are established information-theoretic tools, but their applicability to any concrete system requires an independently established signal, distribution, observer and policy. A separate scoped technical review must audit the equations, interpretation of CWE relationships, source versions, physical/logical counterexamples, and cross-article boundaries before this work can become **Reviewed (model-assisted) / Core claims checked**. Full source-passage verification, independent expert review, taxonomy acceptance, and Published status are not claimed.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
