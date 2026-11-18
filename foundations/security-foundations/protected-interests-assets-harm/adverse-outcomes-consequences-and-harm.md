# Adverse Outcomes, Consequences, and Harm

**Candidate subject:** SF-02-05 · Protected Interests, Assets & Harm  
**Working area:** [Protected Interests, Assets & Harm](README.md) · Adopted Fundamentals-style directory; final semantic ownership remains provisional  
**Artifact:** Substantive working reference, not an authorized final canonical publication  
**Development state:** Draft · **Source-review state:** References listed; initial primary-source comparison completed, separate material-claim Technical Review pending  
**History:** The earlier planning candidate **SF-02-06** was consolidated into SF-02-05 by [Architecture Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md). This manuscript does not reintroduce the retired candidate or inherit its review state.

## An event is not its outcome, and an outcome is not automatically harm

An **event** is something that occurs; a **condition** is a state or circumstance; an **outcome** is a resulting state or change associated with some activity or event; and a **consequence** is an effect significant within a specified context. **Harm** is an adverse effect on a protected interest, person, organization, capability, property, environment or other legitimate concern. A given event can cause several consequences for different stakeholders and none, some or all of them may constitute harm under their applicable criteria.

These descriptions are a **cross-domain security editorial model**, not a claim that all standards define the terms identically. [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), for example, uses *harm* in a safety-specific sense concerning injury/damage to health, property or environment. The [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) analyzes harms to individuals arising from problematic data processing. These are overlapping but non-equivalent scopes.

A detected authentication anomaly is neither proof of unauthorized access nor proof of damage. A confirmed unauthorized database read may be a confidentiality violation without immediate measurable financial loss. A correctly authorized data analysis can create harmful discrimination, exclusion or loss of autonomy without any confidentiality breach. **Security failures, adverse outcomes and experienced harms require distinct evidence.**

## Distinguishing the objects of loss and their consequences

[NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), §§3.4–3.7, treats asset loss as contextual and describes its interpretation through both the **effect on the asset** and **effect on those who value it** (Figure 8, printed p. 26).

A useful causal description separates:

| Element | Meaning | An example not interchangeable with it |
| --- | --- | --- |
| Event or condition | Occurrence or state that may produce change | A scheduled storage shutdown |
| Form of loss | What quality, capability, possession, control or availability is altered | Loss of availability of one database |
| Resulting system state | Observable effect on functions, data or components | Queries fail for some users |
| Stakeholder consequence | Effect on a particular party or protected interest | Missed appointments, delayed reporting |
| Harm | Unacceptable detrimental effect under relevant criteria | Denial of necessary care or increased danger |
| Evidence of harm | Observations and records supporting the claimed consequence | Verified service denial, affected-person report |
| Risk estimate | Future-looking uncertain evaluation of possible consequences | A likelihood/severity estimate for next year |

The rows are **not mandatory universal stages**. Consequences can emerge without an identifiable discrete attack event, and some harms occur gradually through repeated authorized use. The same outage can cause inconvenience to one user and severe disruption to someone with a time-critical dependency.

[NIST SP 800-30 Revision 1 (2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final) models risk in terms of possible adverse impacts and likelihood under risk-assessment conditions. The **concept of adverse consequence** belongs here, but **estimation of future likelihood or conditional financial loss** belongs to [Security Risk & Uncertainty](../security-risk-uncertainty/README.md), including its SF-05-03 working candidate. This prevents duplicate, conflicting definitions.

## Harm is multidimensional and stakeholder-relative

Some harms are readily expressed in physical units or financial terms. Others involve rights, dignity, autonomy, trust, opportunity or systemic dependencies and may not admit a legitimate common numerical scale.

| Dimension | Illustrative adverse effect | Essential context |
| --- | --- | --- |
| Safety and health | Physical injury, exposure to a dangerous process, delayed essential care | Persons exposed, hazard, safety mechanisms, severity |
| Availability and continuity | Loss of access to essential capabilities or essential records | Duration, timing, alternatives, dependent users |
| Integrity and correctness | Corrupted balances, modified commands, incorrect decisions | Detection delay, reversibility, downstream use |
| Confidentiality and privacy | Disclosure, surveillance, reidentification, inappropriate inference | Information sensitivity, affected people, allowed purposes |
| Economic and material | Theft, equipment destruction, replacement cost, lost income | Actual ownership, insurer, time and recoverability |
| Social and institutional | Erosion of trust, stigmatization, discriminatory exclusion | Who suffers consequences and how they are substantiated |
| Environmental and public | Unsafe release, disruption of public infrastructure | Exposure path, geography, long-term effects |

These are **illustrative lenses**, not mutually exclusive harm classes approved as an ontology. One action may implicate several. Recording an effect under one category does not erase the others.

A source-specific safety distinction matters: **ISO/IEC Guide 51:2014**, confirmed current after its 2025 review, concerns people, property and environment. It must not be cited as though it defines every form of informational, reputational or economic harm in cybersecurity. Conversely, [NIST's privacy-risk glossary](https://csrc.nist.gov/glossary/term/problematic_data_action) recognizes that data processing can cause harms to individuals, not only organizational financial loss.

## Severity, extent, distribution and reversibility

An adverse consequence can be described by several partly independent properties:

- **Magnitude:** how significant the effect is within the relevant protected interest and measurement system.
- **Extent:** how many systems, records, relationships, capabilities or people are affected.
- **Duration:** how long the adverse state persists, including delayed or cumulative effects.
- **Reversibility:** whether repair, compensation, recovery or correction can restore the affected interest.
- **Distribution:** who bears the consequence and whether harms are concentrated among parties without decision authority.
- **Observability and confidence:** which effects were directly measured, reported or inferred, and what remains unknown.
- **Dependencies:** whether initial damage propagates through shared infrastructure or organizational relationships.

The same number of impacted accounts may represent radically different experiences. An aggregate count does not reveal whether harm is reversible, distributed equally, or borne by people with unequal ability to recover. **Expected financial cost is not an exhaustive substitute for human harm**, and a list of harms is not a computation of their likelihood.

A severity label is valid only within a stated classification or measurement model. [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final) defines **potential** low, moderate and high impacts of loss of confidentiality, integrity and availability in U.S. federal information systems. It does not establish that those outcomes have occurred, or that all protected interests fit into one generic three-level ladder.

## Worked scenario: one corrupted record, several distinct outcomes

Consider an invented public-service appointment system. An authorized administrative process mistakenly changes the time of an appointment.

- **Observation:** the stored appointment time differs from the previously approved schedule.
- **System effect:** the notification service now transmits the incorrect time.
- **Potential consequence:** the person may arrive late or miss a scheduled service.
- **Possible harm:** access to a necessary benefit or medical appointment may be delayed, depending on the service and available alternatives.
- **Evidence limits:** a changed database field and email delivery record do not, by themselves, prove the person read the notification, missed an appointment, incurred a cost, or suffered physical injury.

If the discrepancy is identified and corrected before the appointment, some adverse consequences may never occur. If two people have different communication needs or different service urgency, the same technical error can affect them differently. If the change was made by a validly authenticated operator, it may still violate an integrity requirement, but it is **not necessarily an adversarial exploit**.

The important distinction is not rhetorical. It controls what a report can truthfully claim. “A record was altered” is a statement about system state. “One person was denied service” requires additional evidence. “The event caused harm” adds a causal and evaluative claim.

## Harm from authorized processing and seemingly beneficial controls

Security systems can themselves introduce or shift harm. A monitoring control might reduce the ability of an adversary to remain undetected, while retaining detailed employee behavior data far beyond what the security purpose requires. An aggressive fraud classifier might reduce financial loss but disproportionately block legitimate access.

The [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) distinguishes privacy risk arising from problematic data actions even when the processing is authorized. The source's perspective is on harms to individuals, not solely breaches or penalties borne by organizations. Its [Problematic Data Action glossary entry](https://csrc.nist.gov/glossary/term/problematic_data_action) describes adverse effects from data actions, with source-specific nuances.

A valid access-control decision can coexist with ethically questionable purposes or foreseeable harm. A technically effective defensive control can create new availability, accessibility, safety or privacy consequences. Whether those effects are justified requires a separate assessment of legitimacy, obligations, alternatives and proportionality. [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) owns that normative question.

## Causation, correlation and proof of consequence

A record indicating that an event preceded an adverse state does not uniquely establish a causal mechanism. Other simultaneous changes, missing observations, shared dependencies or incorrect timestamps may explain the relationship.

For an evidentiary claim, distinguish:
- **recorded fact:** what an instrument or system retained;
- **system-state inference:** what that observation supports about changed data or behavior;
- **causal claim:** why one change contributed to a further consequence;
- **stakeholder-impact claim:** whether and how an affected party experienced harm.

These levels need not form a strict hierarchy in every domain. A directly witnessed injury can establish harm without reconstructing every upstream packet. Conversely, a fully validated software defect may coexist with unknown downstream human consequences.

[Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns how records support causal and actor claims. [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) owns the distinction between a violated security property and broader compromised state.

## The boundary between actual harm and risk estimates

A **realized harm** is an adverse effect shown to have occurred within a defined boundary. A **possible harm** is a conditional consequence in a hypothetical or anticipated scenario. A **risk estimate** characterizes uncertainty about possible adverse outcomes and any chosen time horizon.

Even the word *loss* can mean several things:
- loss of information confidentiality without visible financial damage;
- loss of system control without observed physical injury;
- loss of service for a limited period, perhaps followed by full restoration;
- loss of assurance or evidence, leaving the security condition unknown rather than necessarily violated;
- damage to a stakeholder whose interests are not represented in the organization's accounting.

[NIST SP 800-160v1r1 §3.7 and Figure 8](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) support distinguishing different forms of asset loss and their consequences. No single equation universally converts these different forms into one loss value.

The current inventory has **SF-02-05** as the working owner for general adverse outcomes and harm. **SF-05-03** is separately inventoried to own the method of estimating scenario consequences under risk assumptions. Earlier SF-02-06 was consolidated; no additional semantic owner is needed merely because both domains use the word consequence.

## Cross-references and sources

- [Stakeholders and Protection Needs](stakeholders-and-protection-needs.md): whose interests are affected.
- [Assets, Resources, and Protected Interests](assets-resources-and-protected-interests.md): what is protected and why it matters.
- [Value, Criticality, and Dependencies](value-criticality-and-dependencies.md): consequences inherited through dependencies.
- [Protection Priorities and Constraints](protection-priorities-and-constraints.md): conflicts between preventing different forms of harm.
- [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md): related but nonidentical objectives.
- [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md): future risk uncertainty, not proven realized harm.
- [Fundamentals: Causality and Correlation](../../fundamentals/scientific-analytical-reasoning/README.md): general reasoning rather than security-specific consequences.
- [Operational Foundations](../../operational-foundations/README.md): procedures for impact investigation, risk estimation and decision-making.

### Primary references

- [NIST SP 800-160 Vol. 1 Rev. 1 (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), §§3.4–3.7, especially Figure 8, p. 26, on asset, form of loss, stakeholder and consequence.
- [NIST SP 800-30 Rev. 1 (2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final), risk assessment concepts; its **federal organizational risk-assessment guidance** does not prescribe the editorial harm taxonomy here.
- [FIPS 199 (2004)](https://csrc.nist.gov/pubs/fips/199/final), source-specific potential impact ratings for confidentiality, integrity and availability.
- [NIST Privacy Framework 1.0 (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) and [NIST problematic data action glossary](https://csrc.nist.gov/glossary/term/problematic_data_action), possible individual harms from processing.
- [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), current safety-guide scope for people, property, environment; **not** an all-purpose definition of psychological, reputational or informational harm.

**Editorial limitations:** The appointment and monitoring examples are hypothetical; no real incident or legal conclusion is asserted. Harm dimensions are an editorial comparative scheme, not a ratified ontology. This working manuscript is **Draft / References listed**, not separately audited, source-Verified or Published. The next authoring-related work must review all Drafts in this batch with article-specific claim checks, provenance and corrections.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
