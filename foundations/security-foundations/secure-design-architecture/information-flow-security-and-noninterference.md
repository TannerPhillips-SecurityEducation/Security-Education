# Information-Flow Security and Noninterference

**Candidate subject:** SF-08-09 · Secure Design & Architecture  
**Working area:** [Secure Design & Architecture](README.md) · **Fundamentals-style structure adopted; individual subject placement still provisional**  
**Artifact type:** Substantive working area reference; internal area membership remains **provisional**, not source-Verified or Published.  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md), five material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [v0.3 proposal](../ARCHITECTURE.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)

## Security can depend on the influence of information, not only on access decisions

**Information-flow security** concerns restrictions on how information is permitted to move, propagate or affect observable behavior across defined security contexts. Access-control decisions answer whether a principal may perform a protected operation. Information-flow policies instead ask whether information originating at some level, source or trust boundary may influence observations available at another.

The [NIST information-flow control definition](https://csrc.nist.gov/glossary/term/information_flow_control) describes mechanisms controlling information transfer under security policy, distinct from access enforcement. A system may successfully authorize a read from a sensitive file, yet a later unauthorized disclosure may occur through a different output path.

A general information-flow model defines:

| Element | What must be specified |
| --- | --- |
| Sources | Inputs, values, events or states carrying information |
| Security labels or classifications | Relevant confidentiality, integrity or other policy dimensions |
| Flow policy | Which influences/transfers are permitted |
| Observable outputs | What a modeled recipient or adversary can see |
| Attacker/observer capabilities | Whether timing, termination, metadata, errors or physical effects are visible |
| Declassification or exceptions | Which otherwise restricted flows are explicitly allowed |
| Evidence or proof | What demonstrates the property within the model's scope |

**One security policy can permit an action while another prohibits its effect**. A permitted operation is not a guarantee that its result has an acceptable information flow.

## Noninterference is a model-relative property

**Noninterference** is a classical formal information-flow concept. In a confidentiality setting, it can require that **changing secret/high inputs cannot change what public/low observers see**, while public/low inputs and relevant environmental assumptions are held fixed.

For a deterministic computation with public input L and secret input H, a simplified formulation is:

```text
For any h1, h2 and the same public input l:
    LowOutput(Program(l, h1))
      =
    LowOutput(Program(l, h2))
```

This means the public output, within the *selected observation model*, cannot reveal distinctions among the secret inputs. It does **not** mean that the program's internal state cannot change, that every physical side effect is hidden, or that no authorized information release is possible.

Cornell's [information-flow lecture](https://www.cs.cornell.edu/courses/cs513/2005fa/MCinfo01.iflow_lecture_1.html) develops a comparable high/low formulation and separates direct flows from security properties over a program's executions.

## Explicit and implicit information flows

An **explicit flow** occurs when a high or secret value is used to determine a low output directly, such as copying a confidential variable to a public response.

An **implicit flow** arises when control flow, selected by a secret, changes a public result. For example:

```text
public = 0
if secret > 0:
    public = 1
```

Even though `public` is never assigned directly from `secret`, it reveals one bit of information about the sign of the secret under the declared input domain. A rule that only forbids direct assignment from secret to public would miss this dependency.

A program may also leak through **termination behavior** (whether it halts), **timing** (how long computation takes), **resource use**, error messages, caches, power consumption and other effects. Whether those count as violations depends on what the observer is allowed to see. Stronger definitions of noninterference can include some of these observations, but not every named "noninterference" proof covers them.

## Security labels and permitted flow

A confidentiality label could distinguish Public and Restricted information. A policy may allow public data to influence restricted computations but forbid restricted inputs from influencing public outputs. More complex security label systems can form partial orders rather than one linear sensitivity scale.

**Integrity-oriented flow constraints** are not just confidentiality rules with a renamed label. The objective may be that lower-trust data cannot improperly influence protected decisions or high-integrity results. Classical integrity models such as Biba make additional assumptions about subjects, objects, and permitted read/write relationships; they do not describe every modern taint-tracking or validation mechanism.

For label-based models, **declassification** is an explicitly permitted release of some otherwise restricted information according to a trusted rule. It changes which information flows the policy allows; it is not a proof that all other disclosures are blocked. **Endorsement** may be used in integrity-related reasoning where lower-trust information is accepted into a higher-integrity context under special conditions.

## Worked example: same public input, different secret state

Consider a deterministic service taking public value `request = 4` and a protected secret `h`. The intended public response is `request × 2` without using the secret.

**Design A**:

```text
response = request × 2
```

For both h=0 and h=1, the low-observable response is 8. Within the declared model where only `response` is observable and the computation otherwise behaves as specified, this example satisfies the simplified noninterference condition for these runs. **Two examples alone are not a universal proof for all possible high inputs**; proving it generally would require showing the output does not depend on h for all allowed states/inputs.

**Design B**:

```text
response = request × 2
if h != 0:
    response = response + 1
```

With the same public input 4, h=0 produces 8 and h=1 produces 9. The low output differs when only the secret changes, so this is a **counterexample** to the simplified noninterference property.

**Design C** returns 8 in both cases but takes a markedly different amount of time depending on h. It may satisfy a **value-only** public-output model while violating a model that includes observable timing. A security conclusion must identify which observations are considered.

## Side channels and covert channels are different leakage mechanisms

A **side channel** permits information to be inferred from indirect implementation effects, such as timing, resource behavior, electromagnetic emissions or power consumption. A **covert channel** is an unintended or unauthorized channel used by cooperating entities to transmit information contrary to policy. NIST maintains distinct [side-channel](https://csrc.nist.gov/glossary/term/side_channel) and [covert-channel](https://csrc.nist.gov/glossary/term/covert_channel) definitions.

The proposed **SF-04-08** subject owns leakage mechanisms and exposure conditions. This SF-08-09 pilot owns the **policy-level information-flow property and proof obligation**. Hardware or protocol manifestations belong in Endpoint, Network, Industrial, IoT, Cloud and other specialized domains.

The presence of a timing difference is not automatically proof that a meaningful secret is recoverable, nor does the absence of a timing difference in a few trials establish that none exists under other inputs.

## Policy proof, implementation assurance and evidence

A formal proof typically establishes a property **of a specified model** with declared assumptions. The real program or system may diverge from the model due to unmodeled runtime effects, incorrect compiler assumptions, concurrency, hardware differences or imperfect enforcement.

A practical security claim requires evidence connecting the abstract property to the actual target. This may include verified source code, tests designed to reveal side effects, architectural mediation arguments and independent assessment. A passing property check about one output does not establish confidentiality across every interface, process or time horizon.

**Access-control policies** may be one means of limiting information release, but authorization at an object boundary is not an end-to-end proof that every later copy, derivative, log or signal remains protected.

## Canonical relationships and sources

- [Access-Control Policy Models](../trust-identity-authority-principles/access-control-policy-models.md): policy decisions permitting operations, not complete information-flow guarantees.
- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md): protected interests and objectives.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md): enabling conditions for violating security constraints.
- [Fundamentals: Conceptual and Formal Models](../../fundamentals/models-abstraction/conceptual-and-formal-models.md): modeling syntax, semantics, properties and limitations.
- [Fundamentals: Observation](../../fundamentals/scientific-analytical-reasoning/observation.md): epistemic acquisition and limits.
- [Identity Knowledge](../../../identity/README.md): actual identity and authorization controls.
- [Operational Foundations](../../operational-foundations/README.md): security evaluation and engineering practices rather than general conceptual definitions.

**Authoritative source starting points:** [NIST information-flow control](https://csrc.nist.gov/glossary/term/information_flow_control); [Cornell CS 513 Information Flow](https://www.cs.cornell.edu/courses/cs513/2005fa/MCinfo01.iflow_lecture_1.html); [IETF RFC 4949 Security Glossary](https://www.rfc-editor.org/rfc/rfc4949.html); [NIST SP 800-53 Rev. 5 and current release](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls).

**Source and epistemic limits:** High/low examples are intentionally simplified deterministic models. Stronger formal systems, termination-sensitive policies, probabilistic leakage measures and actual product side-channel assurance require separate specifications and evidence. Complete primary-paper verification and independent expert review remain open.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md). This is a **working pilot**, not an approved permanent canonical article, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](../pilots/README.md)
