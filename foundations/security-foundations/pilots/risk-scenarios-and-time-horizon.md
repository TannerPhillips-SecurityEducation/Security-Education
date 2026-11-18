# Risk, Scenarios, and Time Horizon

**Candidate subject:** SF-05-01 · Security Risk & Uncertainty  
**Artifact type:** Working pilot article, not a ratified permanent canonical subject  
**Development state:** Reviewed (model-assisted) · **Source review:** Core claims checked in [Pilot Technical Review 02](../PILOT-TECHNICAL-REVIEW-02.md); five material claim groups; full source verification and qualified independent approval remain pending  
**Architecture:** [Flexible Security Foundations inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md)

## Security risk is conditional on an adverse scenario

**Security risk** concerns possible adverse consequences to protected interests under uncertainty about future or incompletely observed conditions. It has to be interpreted relative to a **defined system boundary**, **stakeholder**, **threat scenario**, **affected interest**, **operating assumptions**, and **time horizon**. Risk is not an intrinsic number carried by a device, vulnerability, threat source or incident.

[NIST SP 800-30 Revision 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) considers risk in terms of likelihood of threat-event occurrence and the adverse impact should it occur. Its guidance concerns federal information systems and organizations, so this article draws general conceptual distinctions from the framework without imposing a specific federal assessment method as universal.

A risk scenario can be decomposed conceptually:

| Element | Example | Not equivalent to |
| --- | --- | --- |
| Protected interest | Availability of a critical scheduling service | A server's market price |
| Threat source | Power failure, natural hazard, or unauthorized actor | A particular event having occurred |
| Threat event | Loss of power to the hosting facility | A proven compromise |
| Predisposing condition | No functioning alternate power path | An exploit by a malicious actor |
| Consequence | Disruption to service users and dependent processes | A generic vulnerability score |
| Likelihood and horizon | Possibility of event/impact within the next year | A timeless property of the system |
| Evidence and uncertainty | Maintenance records, failure statistics, simulations, expert judgment | An exact known future frequency |

Not every scenario includes an adversary or software vulnerability. A storm-related service outage has different causes from unauthorized access. The existence of a threat source does not establish a threat event, nor does an event alone establish harmful impact.

## Likelihood, frequency and probability describe different quantities

**Probability** is a mathematical assignment to events within a defined sample space or model. **Frequency** concerns a number of occurrences per time, trial or other exposure unit. A **likelihood judgment** may be quantitative or qualitative and can incorporate uncertain threat behavior, evidence limitations and applicable preconditions.

"Five incidents last year" is a reported count, not directly a 50% probability of recurrence. A rate estimate depends on whether the counted events are unique, which population or resource was exposed, how incidents were discovered, and whether future conditions resemble the observed period.

An adversarial event can require both **initiation** and **successful effect**. A useful conceptual separation is:

- Probability or degree that a threat event is initiated under a scenario;
- Probability of a relevant adverse impact **given** that event and the exposed system conditions;
- Size and distribution of consequences for the specified protected interests.

NIST SP 800-30 uses analogous distinctions in its risk-factor analysis. Do not simply multiply independent probabilities unless the model actually supports that independence.

## Harm and estimated risk consequence

**Harm** describes undesirable outcomes affecting people, assets, rights, services or other interests. **Risk consequence estimation** asks which harms *might follow* from a specified scenario and how they would matter to the relevant stakeholders.

A loss estimate may be monetary, quantitative without a currency unit, qualitative or multidimensional. Confidentiality violations, safety impacts, service disruptions and legal consequences are not always reducible to one common scalar.

An important boundary in the working inventory is that **SF-02-05** owns general adverse outcomes and affected interests, while **SF-05-03** owns scenario-dependent consequence estimates. Treating the second as a duplicate article would conflate an observed result with a projection.

## One simple expected-loss model and its limitations

Under an explicitly idealized model, assume a single possible adverse event over one year with probability **0.20** and a fixed loss of **100 units** if it occurs. If the other outcome has zero loss, the expected modeled loss is

```text
E[Loss] = 0.20 × 100 + 0.80 × 0 = 20 units per annual scenario.
```

This computation is valid for the stipulated two-outcome probability distribution. It **does not define risk universally**, guarantee the event happens one time in five years, or capture extreme-loss concerns, risk tolerance, dependencies or changes in controls. Two scenarios with equal expected loss may have very different worst-case consequences and therefore differ in acceptability.

If the 100-unit loss itself varies conditional on the event, then using one fixed magnitude hides an additional distribution. **Uncertainty about the parameters** is also distinct from the modeled event variability.

## Inherent, residual and accepted risk

**Inherent risk** and **residual risk** are frequently used to compare conditions before and after specified controls. But the comparison is meaningful only when the **baseline assumptions** and **control effectiveness** have been stated. Inherent risk is not a unique natural state, because different organizations may assume different baseline environments.

A defensive control may reduce the likelihood of successful impact, the severity of its consequence, or both. Another control might improve detection without changing the probability of the underlying event. A control's installation alone provides no measured effectiveness evidence.

**Risk acceptance** is an accountable decision relative to interests, obligations, tolerance and uncertainty. It does not convert the underlying hazard into something harmless or establish that the accepted consequences are ethically or legally permissible.

The operational processes of performing risk assessments, maintaining registers, selecting treatments and obtaining organizational approval belong to [Operational Foundations](../../operational-foundations/README.md). The shared security-specific meanings of scenarios, uncertainty and consequences belong here.

## Correlation and changing conditions

Risks associated with dependent systems can be **correlated**. If two services rely on the same power supply, redundancy at the application layer may not make their failures independent. A simple product of component probabilities can be seriously misleading when the components share common causes.

Likewise, a vulnerability exploitability rating may change after a patch, a newly reachable path, disclosed exploit methods, an attacker capability shift, or a changed operating configuration. Risk evaluations have a **time horizon and review context**, rather than being immutable labels.

A model-based risk result is not an observation of every adverse outcome. It is a conditional conclusion from assumptions and evidence, and its confidence can decay as the environment changes.

## Worked example: same vulnerability, different risk context

Assume two hypothetical organizations use the same vulnerable software version and receive the same published **CVSS Base score**.

- Organization A does not enable the affected component on its production systems.
- Organization B uses the affected component for a critical customer workflow reachable from the relevant threat source.

The CVSS Base score may be identical because it concerns the vulnerability's intrinsic severity under its scoring model. Organizational risk may differ due to **reachability, affected interests, exposure, additional safeguards and possible consequences**. The situation does not justify assigning any specific numerical likelihood or risk score without more evidence.

[FIRST's CVSS v4.0 User Guide](https://www.first.org/cvss/user-guide) explicitly distinguishes **Base severity** from risk. Threat and Environmental metrics provide additional context, but a CVSS result still does not replace a complete scenario-focused organizational risk assessment.

## Canonical relationships

- [Security and Insecurity](security-and-insecurity.md): protected objectives and bounded security claims.
- [Threat Sources and Threat Events](threat-sources-and-threat-events.md): potential sources and event occurrence, not complete risk.
- [Vulnerabilities and Exploitability](vulnerabilities-and-exploitability.md): enabling conditions, preconditions and severity, not automatically loss or likelihood.
- [Security Claims and Assurance Arguments](security-claims-and-assurance-arguments.md): what evidence supports risk-relevant protection claims.
- [Fundamentals: Probability and Statistics](../../fundamentals/mathematics-logic/probability-and-statistics.md): formal probability, distributions, uncertainty and mathematical inference.
- [Fundamentals: Stochastic Processes and Markov Models](../../fundamentals/mathematics-logic/stochastic-processes-and-markov-models.md): time-indexed processes, not universal adversary behavior.
- [Operational Foundations](../../operational-foundations/README.md): risk-assessment and treatment methods.

## Authoritative references

- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), threats, predisposing conditions, likelihood, adverse impact and timeframe.
- [FIRST CVSS v4.0 User Guide](https://www.first.org/cvss/user-guide), Base/Threat/Environmental/Supplemental distinctions and limits on risk interpretation.
- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), stakeholder protection needs and security engineering assumptions.

**Editorial limitation:** The two-outcome model and organizational comparison are invented teaching examples. This article is not a forecast, audit, risk score, financial estimate or operational risk-assessment method. Source-passage verification, independent human review and canonical taxonomy approval remain separate and pending.

**Editorial status:** Reviewed (model-assisted) under [Pilot Technical Review 02](../PILOT-TECHNICAL-REVIEW-02.md). This remains a working pilot, not a ratified canonical path or independently Published reference.

[Security Foundations](../README.md) · [Pilot Register](README.md)
