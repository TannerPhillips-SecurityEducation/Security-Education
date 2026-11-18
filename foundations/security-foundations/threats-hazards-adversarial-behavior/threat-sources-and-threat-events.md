# Threat Sources and Threat Events

**Candidate subject:** SF-03-01 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · **Fundamentals-style structure adopted; individual subject placement still provisional**  
**Artifact type:** Substantive working area reference; internal area membership remains **provisional**, not source-Verified or Published.  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md), five material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [v0.3 proposal](../ARCHITECTURE.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)

## A source of possible harm is not the same as an event

A **threat source** is a person, group, natural phenomenon, accident, environmental condition, process or other source capable of initiating or contributing to adverse consequences under a defined security context. A **threat event** is a specific occurrence or scenario involving adverse potential. A threat event can happen without producing a realized security violation, and a source can exist without causing an event.

NIST [SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) distinguishes **adversarial threat sources**, **non-adversarial threat sources**, **threat events**, vulnerabilities and predisposing conditions when assessing risks to systems and organizations. The standard is a source of structured risk-assessment terminology, not a theorem that all hazards are adversarial.

| Concept | Example | What the concept does not establish |
| --- | --- | --- |
| Threat source | External actor capable of unauthorized requests | That the actor has attempted anything |
| Threat event | Attempt to read restricted records using a stolen credential | That access succeeded or caused harm |
| Vulnerability | Policy permits a disallowed action under some context | That any threat source encountered it |
| Exposure | Publicly accessible interface | That the interface necessarily has a vulnerability |
| Security violation | Unauthorized read was performed under the declared policy | The actor's real-world identity or ultimate objective |
| Consequence | Disclosed information harms affected parties | The probability of repetition or aggregate risk |

These elements may influence one another but are **not interchangeable labels for one event**.

## Adversarial and non-adversarial threats

An **adversarial source** may possess goals, capabilities, resources, knowledge and opportunities. Its *intent* is often a hypothesis inferred from evidence rather than a field directly observable in network traffic or logs. Capability describes what an actor could do; opportunity describes enabling circumstances; intent describes an alleged objective. One must not be inferred from another without additional evidence.

**Non-adversarial sources** include mistakes, natural events, equipment faults, process failures and environmental conditions. A flood can interrupt power and availability without any malicious agency. A maintenance error can expose protected records without the person intending unauthorized disclosure.

A model should identify *which* harms are included. If the security study concerns an intentionally compromised web service, a storm may be outside its chosen threat scope; that exclusion is an assumption, not proof that storms cannot affect security.

## Threat events, preconditions and consequences

A threat event is easier to assess when its **trigger**, **relevant preconditions**, **affected interfaces**, **possible security property**, and **scenario boundary** are explicit. For example:

```text
Source:      unauthorized user with a valid but overprivileged account
Precondition: service policy permits unrestricted file enumeration
Event:       user requests restricted files
Possible:    unauthorized disclosure
Observation: returned records or access logs, if present and reliable
Unknown:     user's motive and any out-of-band copying
```

The event may be **attempted** but not successful if a separate control blocks the read. A server-side "200 OK" response may reflect successful HTTP exchange while still failing to prove that any protected content was disclosed. The precise claim depends on what was transmitted and what authority was established.

A threat event can also occur when an asset is robust enough to avoid harm; *absence of consequence* in one trial does not erase the source or event.

## Attack tactics, techniques, stages and events use different models

Several established frameworks describe different aspects of adversarial activity:

- **STRIDE** is a set of threat-identification prompts such as spoofing, tampering and denial of service. It does not prove that a given threat occurred.
- **MITRE ATT&CK** classifies observed or described adversarial behaviors by tactics and techniques. Tactic labels indicate objectives, not a mandatory chronological sequence of steps.
- **Diamond Model** relates possible adversary, infrastructure, capability and victim within a modeled intrusion event. Populating the model from evidence is not proof that the named adversary identity is correct.
- **Unified Kill Chain** presents an attack-progression perspective. An actual episode can branch, omit, repeat or reorder activity.
- **CAPEC** describes reusable attack patterns and differs from a specific exploited weakness, a security event record or a complete incident report.

These are **representational tools with different units of analysis**, not a single taxonomy of threat events. Their *operational application* in threat hunting, analysis and threat modeling belongs to [Operational Foundations](../../operational-foundations/README.md).

## Intent, evidence and attribution

A system's observed behavior can be consistent with multiple explanations. Repeated failed sign-ins may arise from a credential attack, a device with stale credentials, an automated health check or a legitimate user making mistakes. Distinguishing hypotheses requires additional context and evidence.

The old proposed **SF-03-08 Attribution and Intent Uncertainty** was consolidated in [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md): questions about **possible actor goals** belong with threat capability and intent concepts (SF-03-03), while **evidentiary actor attribution** belongs with SF-10-08. This avoids creating two competing owners of the same attribution-inference problem.

The distinction is operationally important: even an otherwise reliable log can show what an authenticated session did without independently proving who physically operated the session. Attack tools, compromised credentials and shared access can create ambiguity.

## Worked comparison: three events around one system

Assume a service provides private documents.

**Scenario A:** An unauthenticated person sends a request for a restricted document. The service returns a denial. There is a possible adversarial source and an attempted security-relevant event, but no demonstrated unauthorized read.

**Scenario B:** A storm causes loss of the service's power supply. Authorized users cannot access the service. There is a non-adversarial source and an availability-related adverse event. Whether it constitutes a violation of a particular availability guarantee depends on the specified requirement and tolerated outage.

**Scenario C:** A user is correctly authenticated but assigned an overbroad role; they download another group's document. A policy/modeling or implementation weakness may have enabled a security violation. The download response and authorization context can support this narrower claim, but an investigator still must establish what records were actually delivered, whether their recipient was unauthorized, and the underlying cause.

None of the scenarios by itself supplies a numeric likelihood, an actor's intent, a reliable estimate of future losses, or proof of compromise of every system component.

## Consequences are not risk scores

NIST's risk vocabulary can relate threat events to vulnerabilities, predisposing conditions, likelihood of adverse impacts and severity of consequences. A **risk assessment** uses assumptions and evidence to estimate or characterize those relationships for specific decisions and horizons. The assessment method belongs to Operational Foundations; the underlying concepts belong to the proposed SF-05 area.

A threat source's technical capability is not a probability of occurrence. The fact that a vulnerability is severe does not establish that the threat source can reach it. This is why a generic framework scoring rubric cannot automatically provide an organization's risk.

## Canonical boundaries and primary sources

- [Security and Insecurity](../security-meaning-objectives/security-and-insecurity.md) owns protection goals and conditional security claims.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns the enabling weakness, preconditions and context.
- [Observable, Observed and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) owns evidence acquisition and what a record can support.
- [Fundamentals: State, Events and Transitions](../../fundamentals/models-abstraction/state-events-and-transitions.md) owns general occurrence/change vocabulary.
- [Identity Knowledge](../../../identity/README.md) owns proofing, authenticators and concrete identity functions.
- [Operational Foundations](../../operational-foundations/README.md) owns threat analysis, hunting, triage and response procedures.

**Authoritative starting points:** [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE CAPEC](https://capec.mitre.org/); [Microsoft STRIDE terminology](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats); [Security Foundations' existing model comparison](../ESTABLISHED-MODEL-CROSSWALK.md).

**Limits:** This is a generalized conceptual article, not a risk-assessment procedure, legal attribution, intelligence report or proof of attacker motive. The model sources are accurately differentiated at the scope level; complete technical/passage verification and independent expert acceptance remain open.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 01](../PILOT-TECHNICAL-REVIEW-01.md). This is a **working pilot**, not an approved permanent canonical article, source-Verified artifact or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](../pilots/README.md)
