# Capability, Opportunity, and Intent

**Candidate subject:** SF-03-03 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Fundamentals-style directory adopted; individual ownership remains provisional  
**Artifact type:** Substantive security-knowledge working article, not an approved permanent canonical publication  
**Development state:** Draft · **Source-review state:** References listed; primary-source terminology examined during authoring, separate scoped technical review pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md) · [Working ownership](../CANONICAL-OWNERSHIP-REGISTER.md)

## What an adversary can do, can reach, and wants are different claims

A defensible adversary description distinguishes **capability**, **opportunity**, **intent**, **targeting**, and **observed conduct**. Those dimensions can be related without being inferred automatically from each other.

**Capability** refers to an actor's ability, knowledge, access, tools, resources or effective means to perform some action under specified conditions. **Opportunity** concerns the circumstances that make an action feasible at a particular place and time, including access, exposure, vulnerable state and available paths. **Intent** concerns what an actor is understood or hypothesized to be trying to accomplish. **Targeting** concerns whether a particular asset, system or stakeholder is selected, considered or actually acted upon.

An actor may possess the technical capability to steal a credential but have no opportunity to access the relevant system. An actor may reach a service accidentally without intending a security violation. An observed malicious action may support a hypothesis about an immediate tactical objective without identifying an ultimate strategic motivation, organization or person.

[NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Task 2-1, printed p. 30 (PDF index 38), explicitly characterizes adversarial threat sources by **capability, intent and targeting**, while treating the *range of effects* of non-adversarial sources separately. This article adds **opportunity** as an editorial relationship between an actor's ability and the circumstances necessary for using it. It does **not** claim that NIST defines capability/opportunity/intent as a formally exhaustive three-part ontology.

## Four distinguishable actor- and system-relative variables

| Dimension | Question | A possible basis for evidence | What it cannot establish alone |
| --- | --- | --- | --- |
| Capability | Could this actor execute the relevant behavior? | Observed use of tools, demonstrated permissions, known expertise or means | Desire to act, or access to the intended target |
| Opportunity | Is the necessary route or situation available in this context? | Reachable interface, credentials, time, network location and preconditions | Actor identity, intent or successful execution |
| Intent | What objective is attributed to the actor? | Communications, plans, conduct and independent contextual evidence | Truth of the alleged objective without adequate corroboration |
| Targeting | Is this specific victim/asset selected or acted upon? | Victim selection, reconnaissance, directed requests or explicit statement | Cause of every event on the target or future success |
| Observed conduct | What action or effect was actually recorded? | Properly scoped telemetry, artifacts and witnesses | Unambiguous identity, motive or complete campaign history |

These dimensions are not constant. An actor can acquire new capabilities, lose credentials, change targets, or encounter changed system exposure. What is an opportunity at one point may cease to be possible after a configuration change.

**Targeting and opportunity can diverge.** An actor may be motivated to access a system that is not reachable. Another may inadvertently encounter an exposed service without having selected it. Conversely, evidence that a source repeatedly accesses a particular service can support a targeting hypothesis without proving broader intent.

## Technical ability is not a property of a tool name

The possession of a tool, public exploit description, credential list, or remote execution component does not by itself establish capability against **this system, with this configuration**. Effective capability depends on the interaction of actor resources, system architecture, defenses, privileges and environmental conditions.

For example, a phishing message template may show an ability to craft messages, but it says little about the sender's access to an internal database. An actor controlling one endpoint may be able to run code there but lack network and identity permissions to access a protected control plane. The presence of a technique in an intelligence report does not show every actor associated with that report can perform it in any environment.

An *observed successful action* can provide evidence of some capability in that circumstance, but it does not reveal its maximum extent. Seeing one account read one file does not prove the ability to read all files, nor does it prove that the actor is a human directly operating the account.

The [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), Figure 1, printed p. 9 (PDF index 8), treats **adversary, capability, infrastructure, and victim** as related features of a modeled *intrusion event*. The model does not turn those features into four independent empirical facts or certify the named adversary's identity.

## Opportunity is composed of necessary conditions

An opportunity may require a relevant interface, required privilege, usable time window and absence of an effective blocking condition. For explanatory purposes, write a simple conjunction:

\[
O = R \land A \land T \land P,
\]

where \(R\) is relevant reachability, \(A\) is required access/authority state, \(T\) is an applicable time condition, and \(P\) is a remaining prerequisite. If all four are required, **losing one makes this particular modeled opportunity unavailable**.

This is an authored Boolean abstraction. It is **not** a probability equation, a real exploit path, or proof that all attacks require exactly those conditions. Another path might satisfy the objective without any one of them; some threats use deception or legitimate access rather than a software vulnerability.

A more complete system may contain alternative opportunities:

\[
O_{\mathrm{total}}=O_1\lor O_2\lor\cdots\lor O_k.
\]

The existence of one possible path does not prove that an actor knows it, chooses it, or succeeds. [Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md) owns the general path structure, including branching, reuse and evolving state; [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns the underlying weakness or context permitting a violation.

### Counterexample: resources without effective opportunity

Assume a fictional actor has expert knowledge of a certain vulnerable interface. The interface is disabled in the target's actual production configuration and no alternative route has been established. Their knowledge may support a capability claim, but the specific exploit opportunity has **not** been demonstrated.

An overly broad threat statement such as “this actor can compromise the organization” requires additional paths, preconditions, identity state and evidence. Similarly, a severe published vulnerability in a disconnected test system is not automatically an opportunity against production infrastructure.

## Intent is not directly observed in packets

Security telemetry records observable interactions, metadata, states and sometimes content. A packet indicating a login request does not contain a reliable universal “attacker's intent” field. Even a message explicitly stating an objective is evidence of a **claim about intent**, and may be a bluff or deception.

Several hypotheses can be consistent with repeated failed sign-ins:

- a malicious password-guessing effort;
- an authorized device using expired credentials;
- an automated service with broken configuration;
- a person repeatedly mistyping a password;
- an internal, authorized test.

The alternatives need not be equally plausible. The correct inference depends on additional evidence, such as request sources, identity context, authorization, timings, surrounding conduct and known administrative activity. **Unknown intent** is a valid conclusion, not an analytic failure.

An identified *tactic* in [MITRE ATT&CK](https://attack.mitre.org/resources/faq/) denotes a **tactical goal** within ATT&CK's behavior vocabulary. It does not by itself prove a human actor's enduring motivation, political affiliation, or knowledge of the target's strategic value. One actor might perform reconnaissance to obtain information for multiple different ultimate objectives.

The former proposed **SF-03-08 Attribution and Intent Uncertainty** was deliberately distributed by [Architecture Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md). **Actor goals and intent hypotheses belong here**. Evidence lineage, confidence, causality and actual actor identification belong to [SF-10-08: Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md). This article must not create a second conflicting attribution theory.

## Targeting is more precise than being in a target's vicinity

**Targeting** can refer to selection, preparation or action toward a particular entity. An externally reachable service could receive internet-wide scans without being specifically selected by a named organization. A deliberately crafted message addressed to a particular account may support a narrower selection claim, though it still may not identify the source's real-world operator.

NIST SP 800-30 Appendix D contains **example assessment scales** for capability, intent and targeting. Such scales are task-specific ordinal judgments; they are not direct probabilities of a successful attack, independently validated measurements of expertise, or universal constants across organizations.

A model can distinguish:
- **potential target:** something an actor might choose;
- **selected target:** something the actor apparently chose;
- **observed action target:** the object or service toward which a recorded action was directed;
- **affected victim:** a stakeholder or system that actually experienced an outcome.

The categories are authored analytic distinctions; no single log automatically resolves them all.

## Capacity, motivation and access can change during an episode

An actor may begin with a minor capability and acquire additional credentials. An infrastructure change may make a new route reachable. A service outage may open a temporary alternative mode. A decision-maker may abandon an objective once its expected benefit changes.

A time-indexed description makes those changes explicit:

\[
C_a(t),\quad O_{a,s}(t),\quad I_a(t),\quad T_{a,s}(t),
\]

where \(a\) is the modeled actor and \(s\) the target system. These functions are **editorial variables**, not necessarily measurable scalars. Intent may be a set of uncertain hypotheses rather than a single known value. Treating them as functions does not imply they are continuous or known at every time.

This distinguishes possible action from observed action: an attacker with capability and opportunity **may** act, but no attack event has been established until appropriate evidence supports occurrence. The probability of action under uncertainty belongs to [Security Risk & Uncertainty](../security-risk-uncertainty/README.md), not to a fictional multiplication of capability and intent scores.

## Worked example: authentication abuse with uncertain motive

Consider a fictional organization where an account performs a sequence of denied requests followed by a permitted read.

**Observed:** The system recorded several denied accesses and a later successful protected-object retrieval associated with the account.

**Derived:** The account had sufficient system authorization for the later read under the observed decision path. The sequence may indicate changed privilege, a separate endpoint, mistaken scope, or use of different tokens.

**Inferred possibilities:** An unauthorized actor may have gained a credential; a legitimate employee may have conducted approved work; an automated process may have used overbroad authority. The record does not yet identify the operator or their goal.

**Not established:** A named person's intent, whether the read violated policy, the entire actor's capability set, the ultimate beneficiary, or any onward disclosure.

The sequence illustrates how **capability and opportunity can be supported more strongly than motive or identity**, while the legal authorization or legitimacy of the read may still be unresolved. It is hypothetical, not a report about a live incident.

## Canonical relationships, sources and limitations

- [Adversarial and Non-Adversarial Threat Sources](adversarial-and-non-adversarial-threat-sources.md) owns the intentional/nonintentional source distinction.
- [Adversarial Tactics, Techniques, and Procedures](adversarial-tactics-techniques-and-procedures.md) owns tactical goal and behavior vocabulary, not a reliable identity or ultimate motive.
- [Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md) owns multi-step relationships and alternative routes.
- [Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns source versus occurrence.
- [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns the strength of supporting records and attribution to real actors.
- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md) owns the target protection interest.
- [Operational Foundations](../../operational-foundations/README.md) owns the actual conduct of threat analysis and intelligence assessment.

**Primary source starting points:** [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Chapter 3 Task 2-1 printed p. 30 and Appendix D (adversarial capability, intent and targeting example criteria); [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) (tactic as tactical goal); [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), Figure 1 printed p. 9, event features and capability relations; [NIST predisposing-condition glossary](https://csrc.nist.gov/glossary/term/Predisposing_Condition).

**Editorial limitations:** No direct source defines the invented Boolean opportunity equation or the time-indexed actor variables. An attacker capability claim must be qualified by context and evidence; this article does not attribute a specific real person, predict a campaign, or compute an organizational risk score. Its state is **Draft / References listed**, requiring independent next-cycle technical review of material claims, examples and primary-source limits before promotion. Source-Verified and Published remain unclaimed.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
