# Attacks, Deception, Abuse, and Misuse

**Candidate subject:** SF-03-04 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Fundamentals-style organization adopted; individual subject names and canonical ownership remain provisional  
**Artifact type:** Substantive security-knowledge working manuscript, not an operational attack playbook or an approved permanent canonical publication  
**Development state:** Draft · **Source-review state:** References listed; primary-source terminology consulted in authoring, **separate material-claim Technical Review 10 pending**  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Established Model Crosswalk](../ESTABLISHED-MODEL-CROSSWALK.md) · [Development and Verification Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)

## An adverse action is not necessarily an attack

Security-relevant actions can be technically permitted, forbidden, accidental, deliberate, deceptive, beneficial, negligent, or harmful. The same visible command or exchange may support very different interpretations depending on the actor's purpose, the intended behavior of a feature, the applicable authority, the system's actual state, and the effects on protected interests.

An **attack** is intentional behavior directed toward circumventing, defeating, manipulating, or otherwise violating a relevant security protection or protected interest. An **attack attempt** need not succeed. **Deception** involves misleading an observer or decision-maker about a fact, identity, authority, state, purpose, or relationship. **Misuse** is use of a resource, privilege, process, or function in a way that departs from an intended or permitted use, potentially deliberately or by mistake. **Abuse** commonly emphasizes exploitation or repurposing of a capability or ordinary functionality to produce an undesirable, harmful, or unauthorized result. These descriptions are **security-analytic working terms**, not four disjoint classes mandated by an external standard.

An action can be **deceptive abuse** and simultaneously an **attack**. A mistaken but authorized action can be misuse without a purposeful attack. A technically valid feature can enable harmful abuse without any software vulnerability in its ordinary implementation. Observing unexpected inputs alone cannot establish the intent needed to classify an actor's behavior as a deliberate attack.

The [OWASP Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) discusses the abuse of expected application features and how such scenarios can motivate security requirements. The [OWASP description of Abuse of Functionality](https://community.owasp.org/attacks/Abuse_of_Functionality) notes that valid features may be used in undesirable ways even without a conventional software flaw. Those sources explain *possible mechanisms*, not that any particular person committed a malicious act.

## Five distinct claims in a description of conduct

| Analytic dimension | What must be established | Unsupported shortcut |
| --- | --- | --- |
| **Observable behavior** | What action, request, response, state change, or representation occurred? | Every anomaly is an attack |
| **Expected or specified use** | Which operations and outcomes does the feature legitimately support? | Technical validity makes any purpose acceptable |
| **Authorization and legitimacy** | Which actor and action are permitted, and for what purpose or context? | An authenticated session can do no harm |
| **Intent or objective** | Which purpose is supported by evidence rather than assumed from consequences? | A harmful outcome proves deliberate malice |
| **Result and consequence** | Was the desired or prohibited effect actually achieved, and who was affected? | An attempted attack means compromise and harm occurred |

The dimensions are related but orthogonal enough that reducing them to a single *benign/malicious* label may discard relevant distinctions. The same operator might take an unauthorized action without understanding the policy; a malicious actor might attempt an attack that is successfully blocked; a properly authorized program might produce a privacy-harming result in ordinary operation.

A useful security assertion identifies the **action**, **relevant protected interest**, **system boundary**, **authority model**, **mechanism**, **observed result**, and **uncertainty about intent**. Such a statement need not be a completed incident investigation. In this repository, [Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns *source versus event*; [Capability, Opportunity, and Intent](capability-opportunity-and-intent.md) owns hypothesized actor means and motives; [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns proof and attribution.

## Attacks and attempted violations

A modeled attack has a **goal** and one or more **proposed means**. The goal might be unauthorized disclosure, false authorization, loss of availability, incorrect action, untrusted influence on a decision, or some other adverse security state. A method might interact with normal interfaces, exploit a vulnerability, deceive a person, or misuse previously granted authority.

The conceptual distinctions are:

- **Threat capability:** The source might be able to cause an adverse event.
- **Attack attempt:** Conduct consistent with a deliberate effort to violate a specified security objective occurs.
- **Successful policy or property violation:** The protected condition is actually breached in its declared scope.
- **Compromise:** Trust in some specified system state, component, principal, information, or control has been lost under a defined model.
- **Harm:** An adverse consequence affects a protected interest; harm can exist without a malicious attack.

Success is **objective-relative**. A denied request can constitute an attempted unauthorized read without a successful disclosure. An unauthorized read can violate confidentiality without proving every record was subsequently copied. A compromised service account can undermine a trust assumption without proving the attacker controlled all systems. An attack can even fail while creating availability problems through excessive legitimate retries.

The [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) risk-assessment framework distinguishes adversarial threat sources, threat events, vulnerabilities, predisposing conditions, and adverse impacts. It does not collapse every proposed attack scenario into evidence that an incident occurred. [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) retains the separate ownership of compromise as an actual trust/protection-state proposition.

## Deception targets judgment and trust

**Deception** changes what a person or system believes about a subject, source, message, authority, or situation. The mechanism may involve impersonation, a false pretext, misrepresented content, or manipulation of trusted context. An attacker need not exploit a software memory error if the target instead makes a normally permitted decision based on deliberately falsified information.

The [NIST social engineering glossary](https://csrc.nist.gov/glossary/term/social_engineering) lists multiple **source-attributed definitions**, including deception intended to elicit information, obtain unauthorized access, or commit fraud by gaining confidence and trust. The entries are not one universal claim that every persuasive message is hostile. [MITRE CAPEC-407: Pretexting](https://capec.mitre.org/data/definitions/407.html) describes a deliberately invented identity or scenario used to solicit information or induce an action. [CAPEC-98: Phishing](https://capec.mitre.org/data/definitions/98.html) classifies one more specific social-engineering attack pattern.

These concepts relate without becoming synonyms:

| Concept | Characteristic | What is not implied |
| --- | --- | --- |
| Deception | Deliberately misleading representation or context | The method must be phishing or involve an email |
| Impersonation | Claimed identity or authority is false | Every authentication system necessarily accepts it |
| Pretexting | Fabricated scenario or role induces action | The action actually succeeded |
| Social engineering | Human trust, judgment, or interaction is manipulated for an adversarial end | A person is morally culpable for being deceived |
| Phishing | A source-defined attack pattern using fraudulent contact or representation | All deceptive activity fits one CAPEC entry |
| Misrepresentation by a faulty system | Incorrect information leads to an incorrect decision | The system was deliberately manipulated |

A legitimate-looking notification might be fraudulent, but an authentic message might also contain a mistake. A request that uses urgent language is not automatically social engineering; legitimate emergencies can require urgency. The intentional **misrepresentation** and its evidence matter.

### Human, organizational and technical boundaries

An access-control rule might enforce that only a designated worker can approve a transaction. If that worker is deceived into performing an approval inconsistent with its intended purpose, the computer may record a valid authenticated action while the wider **authorization or legitimacy claim** has failed. This is not a demonstration that cryptography failed. It is a distinction between checking a credential and establishing that a particular action reflects a justified decision.

Deception can also target automated systems through misleading metadata, forged claims, or inconsistent context. Yet it is analytically incorrect to attribute a human belief state to a parser. The actual mechanism could be data integrity, provenance, authentication, policy interpretation, or a human trust relationship. The system boundary and evidence decide which model applies.

## Abuse of intended functionality

Software is often secure against direct injection or memory corruption while still offering legitimate capabilities that can cause unacceptable effects if used at unanticipated scale, frequency, sequence, audience, or purpose.

An **abuse case** changes the viewpoint from “What should an intended user accomplish?” to “How could the same feature produce an unacceptable outcome?” OWASP emphasizes **business-logic and feature abuse**, including scenarios where each individual request may use a supported interface. A valid API response does not necessarily mean that the cumulative activity, resource use, or effect on another user is acceptable.

Consider a fictional community notice platform. The platform intentionally allows verified coordinators to distribute messages to subscribed residents. Abuse hypotheses may involve a coordinator sending repeated notices to harass recipients, using legitimate messaging privileges to mislead people about an event, or repurposing an emergency channel for unrelated monitoring. Some actions could satisfy the **technical authentication** requirement and still violate purpose, consent, moderation, or other requirements.

This does **not** establish that the platform is vulnerable under every reasonable threat model. It identifies a set of possible **unacceptable uses** that might require system policy, limits, consent rules, separation of duties, or other protective design. Any actual vulnerability, severity, evidence of misconduct, or legal conclusion requires more context.

[OWASP Abuse Case](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) and [Abuse of Functionality](https://community.owasp.org/attacks/Abuse_of_Functionality) are useful starting points. Their examples should not be generalized into a claim that any service capable of sending notifications is inherently insecure.

## Misuse can be accidental, intentional or ambiguous

Suppose an authorized operator sends a production report to the wrong internal destination. The **observable action** is a transfer. The **policy question** is whether the recipient was authorized. The **intent question** is whether the operator meant to disclose it. The **consequence question** is what actually arrived and who could access it.

The same observed transfer may be:
- an honest mistake violating a data-handling rule;
- a policy-permitted operation inconsistent with a stakeholder's privacy expectations;
- a deliberate effort to disclose information;
- an approved test or emergency exception;
- an incomplete log that only *appears* to describe a disclosure.

The categories have different causal and evidentiary implications. **Misuse is not proof of adversarial intent.** Conversely, the absence of a software exploit does not make deliberate abuse benign.

A security report should avoid a leap from “unexpected feature use” to “known hostile actor.” Such a leap confuses observation, normative rule, cause, and attribution. Actor-identity proof belongs in [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md).

## What STRIDE does and does not classify

[Microsoft's STRIDE threat-modeling vocabulary](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) covers **Spoofing**, **Tampering**, **Repudiation**, **Information Disclosure**, **Denial of Service**, and **Elevation of Privilege**. STRIDE groups possible **types of protection failure or threat**; it is not a list of mental states, social relationships, attacker motives, or exhaustive harm classes.

For example, a forged claim of identity may be discussed as *spoofing*, while an unauthorized data change may be discussed as *tampering*. But a manipulation of a person's trust could involve spoofing, information disclosure, or other effects, and an abuse case might evade a simple STRIDE label because the intended system feature itself permits the action.

Microsoft describes STRIDE as an aid to identifying potential threats in designs. The [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) distinguishes STRIDE from **misuse or abuse cases**, which explicitly examine unwanted behaviors of valid workflows. Neither framework states that finding one label constitutes proof of an observed incident.

| View | Distinct question | Limitation |
| --- | --- | --- |
| STRIDE | Which common security-property threat classes might affect a design element? | Does not prove that any attack happened or cover all socio-technical harm |
| OWASP abuse/misuse case | How might intended functionality produce an unacceptable result? | Not automatically a vulnerability or proof of malicious actor intent |
| CAPEC | What reusable attack pattern could fit a mechanism or precondition? | A catalog entry is not evidence a target was attacked |
| MITRE ATT&CK | Which adversarial tactic, technique, or procedure describes behavior? | A technique label is not actor attribution or a required attack sequence |
| Security incident evidence | Which observed acts, violations, and effects can be supported? | Collection gaps and ambiguity may remain |

The **behavior-model vocabulary** and distinction between tactics, techniques, and procedures remain owned by [SF-03-05](adversarial-tactics-techniques-and-procedures.md). **Threat-model assumptions, boundary choices, framework scope, and model-completeness limits** remain owned by [SF-03-07](threat-assumptions-and-models.md).

## Worked case: authorized workflow, unacceptable effect

Consider a fictional document-sharing service with an “invite collaborator” feature. It correctly authenticates the sender and allows invitations to verified email addresses. Its implementation processes each invitation according to specification.

**Observed:** One account issues many invitations to recipients who did not request them.

**Possible system effects:** Messaging volume increases and unsolicited notifications reach recipients.

**Potential policy claim:** The service may lack a purpose/consent condition or a rule limiting repeated contact. That must be established from actual requirements.

**Competing hypotheses:** Ordinary collaboration, mistaken bulk import, automated misconfiguration, authorized testing, deliberate harassment, or an attacker abusing a compromised account.

**Unproven without further context:** Who operated the account; whether the invitation content was deceptive; whether a rule was actually violated; whether recipients suffered harm; whether any computer was compromised.

A well-designed investigation might later substantiate a narrow abuse finding, but the *technical feature's ordinary success* is not evidence of legitimate purpose. Nor is unsolicited notification alone proof of an attacker.

This example is fictitious and is used to separate source, action, expected use, claimed legitimacy, and actual consequence. It is not an exploitation procedure.

## Boundaries, original sources, and review requirements

- [SF-03-01, Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns potential origin versus occurrence, not the taxonomy of misuse.
- [SF-03-02, Adversarial and Non-Adversarial Threat Sources](adversarial-and-non-adversarial-threat-sources.md) owns intentional/nonintentional source classification.
- [SF-03-03, Capability, Opportunity, and Intent](capability-opportunity-and-intent.md) owns motive hypotheses and ability/targeting conditions.
- [SF-03-05, Adversarial Tactics, Techniques, and Procedures](adversarial-tactics-techniques-and-procedures.md) owns technique and behavior categories.
- [SF-03-06, Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md) owns multi-step transitions, not whether a deception was observed.
- [SF-03-07, Threat Assumptions and Models](threat-assumptions-and-models.md) owns model scope, assumptions, and scenario completeness.
- [SF-04-02, Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns the enabling flaw and context, not the actor's purported purpose.
- [SF-02-05, Adverse Outcomes, Consequences, and Harm](../protected-interests-assets-harm/adverse-outcomes-consequences-and-harm.md) owns realized and potential human/organizational harms.
- [SF-10-08, Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns causal evidence and identification.
- [Operational Foundations](../../operational-foundations/README.md) owns the practice of conducting abuse-case reviews, social-engineering defenses, hunts, investigations and incident response.

### Primary source starting points

- [OWASP Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html), legitimate-feature abuse scenarios and negative requirements; an instructional guide, not a universal legal definition.
- [OWASP Abuse of Functionality](https://community.owasp.org/attacks/Abuse_of_Functionality), uses of valid application features and distinctions from conventional vulnerabilities or denial of service.
- [NIST social engineering glossary](https://csrc.nist.gov/glossary/term/social_engineering), multiple source-attributed definitions, including NIST SP 800-82 Rev. 3 and SP 800-63-4; definitions must be interpreted within their sources.
- [MITRE CAPEC-407 Pretexting](https://capec.mitre.org/data/definitions/407.html) and [CAPEC-98 Phishing](https://capec.mitre.org/data/definitions/98.html), examples of particular deception attack patterns, not proof of a specific event.
- [Microsoft STRIDE threat categories](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), design-threat prompts rather than a comprehensive taxonomy of motives.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html), STRIDE and misuse/abuse cases as complementary views.
- [NIST SP 800-30 Rev. 1 (final, 2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final), adversarial sources, events, vulnerabilities and impacts in a federal risk-assessment context.

**Editorial limitations:** The conceptual distinctions and worked examples are **editorial** and hypothetical. An externally published attack-pattern label is neither a determination of actor intent nor proof that actual harm or compromise occurred. The manuscript does not provide actionable exploitation instructions. It is **Draft / References listed**; source passages, mechanism boundaries, counterexamples and the adjacent working article relationships require a separate **Technical Review 10** before any Reviewed promotion. Full source-to-claim verification, independent qualified expert acceptance, canonical taxonomy approval and Published status remain open.

[Security Foundations](../README.md) · [Working area](README.md) · [Development and Verification Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
