# Adversarial and Non-Adversarial Threat Sources

**Candidate subject:** SF-03-02 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Fundamentals-style directory pattern adopted; individual area identities and canonical ownership remain provisional  
**Artifact type:** Substantive working knowledge reference, not an approved final canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md), 7 article-specific material claim groups; full source-passage verification and independent expert acceptance pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Coverage and gaps review, SG-06](../COVERAGE-AND-GAPS-REVIEW-03.md) · [Provisional ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)

## Harmful potential does not imply a malicious actor

A **threat source** is a contextual origin of circumstances or activity capable of giving rise to a security-relevant adverse event. Source, event, enabling condition, and consequence are not the same thing. A person may be a threat source without performing any harmful action; a system may experience an adverse event without any person intending harm.

**Adversarial sources** involve agents who can intentionally attempt to defeat, circumvent, misuse or undermine protection. **Non-adversarial sources** may involve accidental human action, technology or process failures, or environmental conditions without an adversarial objective. Whether a situation qualifies as a threat depends on the protected interests, system, time and security property under consideration.

[NIST SP 800-30 Revision 1 (2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final) distinguishes adversarial and non-adversarial threat sources in federal risk assessment. Chapter 3, Task 2-1 (**printed p. 30 / PDF page index 38, visually inspected**), explicitly examines adversarial **capability, intent and targeting** and non-adversarial **range of effects**; Appendix D's scales and taxonomies are *exemplary and tailorable*, not universally measured properties of every source. Its two assessment branches are different: it does **not** define adversarial intent for a storm or a machine failure. [NIST's glossary entry for non-adversarial threat](https://csrc.nist.gov/glossary/term/non_adversarial_threat) identifies accidents, human error, structural failure and environmental causes, citing SP 800-160 Vol. 2 Rev. 1.

The distinction is about **how an event can arise**, not a rule that hostile actors always produce worse consequences than accidents. Either type can defeat confidentiality, integrity, availability, physical safety, or another specified protection objective.

## Anatomy of a source-relative threat assertion

A defensible proposition identifies at least the following elements:

| Element | Adversarial interpretation | Non-adversarial interpretation |
| --- | --- | --- |
| Origin | Agent or cooperating agents with relevant purpose | Human mistake, environment, infrastructure condition, random failure |
| Mechanism | Intentional action, including use of ordinary authorized capabilities | Accidental action, unplanned behavior, defect, natural process |
| Preconditions | Required access, capability, opportunity, authority or exposure | Environmental state, susceptible dependency, operating envelope, process conditions |
| Potential event | Attempted unauthorized change, deceptive action or misuse | Misconfiguration, unplanned power loss, corrupted sensor reading |
| Protected property | Integrity, confidentiality, control, authenticity, safety or availability | The same protected properties may be affected |
| Evidence boundary | Actions and consequences may be observable while actor and intent remain uncertain | System state may be observable while physical or procedural cause remains uncertain |
| Appropriate analytic focus | Capability, opportunity, objectives and observable behavior | Initiating conditions, range of effects and causal dependencies |

These are **editorial dimensions**, not a NIST table copied verbatim. A real scenario may combine both columns: an attacker can deliberately trigger a hardware fault; an equipment failure can make a subsequent attack possible; an employee can make an inadvertent mistake while another person exploits its consequences.

The actor/source category must be explained, not inferred from outcome severity. Serious harm does not, by itself, prove intentional misconduct.

## Threat source, threat event, vulnerability and hazard

The previously Reviewed [Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns the primary **source versus occurrence** distinction; this article deepens the **adversarial/non-adversarial classification**. Related terms remain separate:

- **Threat source:** what may initiate or contribute to an adverse event.
- **Threat event:** an occurrence or situation with potential adverse consequences. The NIST [threat event glossary](https://csrc.nist.gov/glossary/term/threat_event) attributes this meaning to SP 800-30 Rev. 1.
- **Vulnerability:** a context-dependent condition through which a protected security property could be violated.
- **Predisposing condition:** a circumstance increasing or decreasing the chance that a threat event, once initiated, produces an undesirable impact. NIST's [predisposing-condition entry](https://csrc.nist.gov/glossary/term/Predisposing_Condition) makes this influence explicit.
- **Hazard:** a source of potential harm in a selected safety context. Not every hazard is an attacking principal and not every security threat is a safety hazard.
- **Consequence/harm:** what happens to protected interests as a result; the occurrence of a source or event is not equivalent to proof of harm.

An adversarial actor may exploit a weakness, but **not all damaging events require an exploitable software defect**. A regional power failure may interrupt a service because it lacks backup power; a legitimate user may accidentally delete a record under a policy that was appropriate for the user's normal role. Whether those events violate specified security requirements depends on the actual objectives and conditions.

## A combined-cause example

Consider a fictional scheduling application with a shared identity service and a backup power supply.

**Scenario A, non-adversarial:** A utility outage interrupts both the application and its identity dependency. Authorized users cannot obtain sessions. The source is an environmental power condition; the event is loss of availability; the consequence may range from inconvenience to essential service disruption depending on the users and duration.

**Scenario B, adversarial:** A person intentionally attempts to use a credential outside its authorized purpose. This is a potential adversarial event. Without evidence that the credential was accepted and enabled protected behavior, success and harm remain unproven.

**Scenario C, composite:** A misconfigured failover mode temporarily broadens access permissions after the power outage. An actor later uses those permissions deliberately to access another user's record. The initial condition arose without hostile intent, while the later action might be adversarial. Describing the complete episode as exclusively a natural disaster or exclusively an attack would erase important causal differences.

This example is constructed, not a report about an actual system. It demonstrates that **a timeline can contain several kinds of sources and mechanisms**. The presence of a power failure does not establish that the later login was malicious, and the appearance of a suspicious login does not show the power failure was engineered by an adversary. **The category can change with the causal question**: an accidental failure may create an opportunity later exploited deliberately, while the failure itself remains non-adversarial under the assumed facts.

## Multiple sources and one event: the relationship is not one-to-one

NIST SP 800-30 Rev. 1, Task 2-2 (**printed p. 31 / PDF page index 39, visually inspected**), describes **many-to-many relationships** between threat sources and threat events and explicitly notes different possible likelihoods for different source-event pairings. This is a *candidate association in a risk-assessment context*, not a claim that every source/event pairing is plausible or observed. A service disruption might be initiated by an insider, a software error, a power outage or a supplier failure. One adversary might initiate multiple distinct types of threat events.

A simple conceptual relation can be written as:

\[
\mathcal T\subseteq \mathcal S\times\mathcal E,
\]

where \(\mathcal S\) denotes candidate sources, \(\mathcal E\) denotes candidate threat-event types and \(\mathcal T\) represents possible source-event associations. This is **authored set notation**, not a NIST formula. Membership in this relation means a source could be associated with an event under the model; it does **not** prove that it caused a specific observed occurrence.

In an investigation, an observed artifact may support a claim about an event while leaving the source uncertain. For example, a damaged storage block may have resulted from aging hardware, a firmware defect or deliberate tampering. Attribution to a human requires further evidence, not simply a high-consequence outcome.

## Intent is a hypothesis, and absence of intent is also a claim

A human can cause damage negligently, unintentionally, recklessly or deliberately. Those terms can carry different legal and ethical meanings; a technical security reference should not silently adjudicate them from telemetry alone.

A user making repeated password mistakes is **not automatically an attacker**. A process issuing unusual requests is not automatically hostile. Equally, a normally authorized employee might deliberately abuse legitimate access. The same externally visible action may be consistent with several hypotheses.

NIST SP 800-30's *adversarial* category is useful when behavior is modeled as purposeful, but a defender may have **unknown intent** in a particular case. Maintaining an unknown state is often more accurate than forcing the observed activity into “accidental” or “malicious” categories.

[Capability, Opportunity, and Intent](capability-opportunity-and-intent.md) owns detailed distinctions among what an adversary could do, under what opportunity, for what objective, and how those assertions can remain uncertain. [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns the strength of evidence supporting actor identification and causal claims.

## Adversarial behavior is not a mandatory sequence

For an intentional threat source, a model may classify behavior using [MITRE ATT&CK](https://attack.mitre.org/resources/enterprise-introduction/), [CAPEC](https://capec.mitre.org/about/new_to_capec.html), the [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), or the [Unified Kill Chain](https://www.unifiedkillchain.com/). These sources are **different kinds of models** with different units of analysis: behavior categories, attack-pattern descriptions, intrusion-event relations and progression perspectives.

The presence of an ATT&CK tactic or an attack stage does not establish malicious motivation for a specific unknown event. Conversely, non-adversarial sources cannot generally be explained by importing adversarial “tactics” into a storm, failed cooling system or ordinary operator mistake.

The proper use of a model is to clarify **which distinctions the model supports**, not to force every event into its vocabulary. This matters for mixed-source cases, where one *episode* may contain non-adversarial conditions and adversarial actions; the appropriate unit for classification is the source or event being claimed, not the entire episode given one unqualified label. SF-03-05 covers tactics, techniques and procedures. SF-03-06 covers paths, stage assumptions and prerequisite dependencies. This subject owns the source-category boundary.

## Which consequences can a source produce?

The impact of a threat depends on the interaction among the source, system and protected interest. A severe non-adversarial power fault and a deliberately induced denial of service can produce the same immediate availability loss. However, their recurrence mechanisms, control implications, evidence and responsible parties differ.

A useful conditional model is:

~~~text
Threat source / initiating circumstances
                |
                v
          Potential event
                |
          affected conditions
                |
                v
      Protected property at risk
                |
                v
        Possible consequences
                |
                v
      Evidence about actual effects
~~~

The diagram is **illustrative, not a deterministic causal proof**. The event may be blocked, have no effect, or produce unanticipated effects. Sources do not by themselves supply reliable probabilities. [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md) owns scenario-specific uncertainty, likelihood and time horizon. [Adverse Outcomes, Consequences, and Harm](../protected-interests-assets-harm/adverse-outcomes-consequences-and-harm.md) owns actual and possible harms.

## Canonical boundaries and primary sources

- [Threat Sources and Threat Events](threat-sources-and-threat-events.md): shared source-versus-event conceptual distinction.
- [Capability, Opportunity, and Intent](capability-opportunity-and-intent.md): how adversarial capability, context, motives and uncertain targeting differ.
- [Adversarial Tactics, Techniques, and Procedures](adversarial-tactics-techniques-and-procedures.md): model-specific observable adversary behavior.
- [Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md): conditions that connect multiple adverse actions.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md): enabling conditions, not source identity.
- [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md): evidence of lost security properties.
- [Fundamentals: State, Events and Transitions](../../fundamentals/models-abstraction/state-events-and-transitions.md): general event/transition semantics.
- [Operational Foundations](../../operational-foundations/README.md): risk-assessment, threat-modeling and investigation activities.

**Primary reference starting points:** [NIST SP 800-30 Rev. 1 (final 2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Chapter 3 Tasks 2-1 and 2-2 (printed pp. 30–31) and Appendix D; [NIST non-adversarial threat glossary](https://csrc.nist.gov/glossary/term/non_adversarial_threat) citing SP 800-160 Vol. 2 Rev. 1; [NIST threat-event glossary](https://csrc.nist.gov/glossary/term/threat_event); [NIST predisposing-condition glossary](https://csrc.nist.gov/glossary/term/Predisposing_Condition); [NIST threat-source glossary](https://csrc.nist.gov/glossary/term/threat_source), which includes multiple source-attributed definitions and should not be flattened into one universal sentence.

**Editorial limitations:** The categories, relation notation and scenarios are explanatory interpretations of primary-source concepts. The separate [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md) checks seven material claim groups, including the NIST adversarial/non-adversarial assessment branches, the source-event relationship and mixed-cause limitations. **Reviewed (model-assisted) / Core claims checked** does not determine origin or intent of any real incident, quantify organizational risk, verify the complete standards text, establish independent expert acceptance, ratify canonical taxonomy or authorize Published status.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
