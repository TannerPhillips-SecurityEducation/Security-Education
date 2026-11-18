# Protection Priorities and Constraints

**Candidate subject:** SF-02-07 · Protected Interests, Assets & Harm  
**Working area:** [Protected Interests, Assets & Harm](README.md) · Adopted Fundamentals-style article placement; exact working subject and area taxonomy remain provisional  
**Artifact:** Substantive technical working reference, not approved as final canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md), six article-specific material claim groups; full source verification and qualified external acceptance pending  
**Governance:** [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Development plan](../DEVELOPMENT-PLAN.md) · [Ownership boundaries](../OWNERSHIP-BOUNDARIES.md)

## Not every desired protection can be maximized simultaneously

Protection objectives compete for attention, resources and operating conditions. An additional authentication challenge can discourage unauthorized access while making legitimate service harder to reach. Extensive security logging can support accountability while exposing private behavior. Keeping a system running may preserve availability while allowing an unsafe physical process to continue. Restricting all system outputs might reduce disclosure while preventing an essential warning from reaching its intended recipients.

A **protection priority** is the relative precedence assigned to a need or outcome under declared stakeholders, circumstances and obligations. A **protection constraint** is a boundary limiting acceptable designs, actions or outcomes. An **acceptable protection tradeoff** is a justified choice among feasible alternatives that does not silently violate requirements or transfer unexamined harm to affected parties.

The three have distinct meanings. Prioritization helps choose *among* objectives; constraints may remove alternatives *before* comparison; an actual tradeoff is the conditional decision or sacrifice involved. **A conflict is not evidence that one objective must always be sacrificed**: improved engineering can sometimes satisfy both objectives within the same feasible design. A priority is not necessarily a numeric weight, and a constraint is not necessarily flexible.

[NIST SP 800-160 Vol. 1 Rev. 1 (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) §3.7, printed pp. 25–27, explicitly incorporates stakeholder needs, system assets and engineering trades in protection-needs determination. A protection need can be identified from the significance and type of asset loss before assigning the probability of any particular attack. This concept is distinct from estimating a specific security risk scenario.

## What governs a priority?

Relevant considerations include:

| Consideration | Effect on protection priorities | Common misinterpretation |
| --- | --- | --- |
| Protection need | Defines an interest that must be preserved | Every request by a powerful stakeholder is automatically legitimate |
| Consequence and criticality | Describes what failure could do to affected interests | More expensive asset always means more important |
| Safety and rights | Limits choices that would impose unacceptable harm | A good average score makes all negative outcomes acceptable |
| Applicable obligations | May establish mandatory or contractually binding boundaries | A control list resolves all actual protection conflicts |
| Technical feasibility | Identifies what the system can implement or assure | Feasible in code means justified in context |
| Operational dependency | Reveals indirect effects and common-mode failure | Adding a replica automatically eliminates the risk |
| Evidence and uncertainty | Limits confidence that a measure truly protects | No observed incident proves no residual weakness |
| Changing context | Can alter need, exposure, urgency and alternatives | A published priority ranking is permanently correct |

The **existence** of an obligation does not automatically establish its applicability; jurisdiction, contract, affected subjects and system boundary matter. [Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) owns the legitimacy and accountability of protection decisions. The present subject explains the technical structure of the competing needs and constraints.

The [NIST CSF 2.0 Organizational Context category](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters), especially GV.OC-01 through GV.OC-04, relates mission, stakeholders, legal/contractual requirements and essential services. It is an organizational **outcome framework**, not a law that one class of protected interest must always dominate every other.

## Constraints, preferences and decision authority

A **hard constraint** excludes an otherwise attractive option if it fails a mandatory condition. A **preference** ranks feasible alternatives under a stated objective. The label *hard* does not arise from mathematical notation alone: it reflects a properly justified requirement or obligation. **A purported hard constraint can itself be incorrectly specified**, and satisfying a scalar model does not override actual rights, human safety or binding law.

For an abstract design \(x\), let the feasible set be

\[
\mathcal F = \{x \in \mathcal X : g_i(x)\leq b_i \text{ for all required } i\}.
\]

The functions \(g_i\) and limits \(b_i\) are **authored notation**. They might describe performance ceilings, maximum interruption, allowed data processing, access constraints or safety boundaries. Real rights and obligations may not be reducible to a scalar inequality, so the mathematical model must not be mistaken for a complete legitimacy test.

Only **after determining which designs are feasible** can a team compare preferences such as lower latency, reduced maintenance burden, better auditability or less sensitive-data collection. Some choices require authority and stakeholder agreement; a ranking generated by an optimization tool cannot substitute for them.

### Pareto tradeoffs are conditional

Suppose two feasible designs have measured or modeled objectives \(f_1(x)\) and \(f_2(x)\), where smaller is better. A design \(a\) **Pareto-dominates** \(b\) when it is no worse on every specified objective and strictly better on at least one. A Pareto-front set does not define which design is morally, legally or operationally best. It only identifies alternatives not dominated **under the chosen objectives, measurements and feasible region**. A design that violates a hard safety or privacy obligation is not a valid competing point merely because it has an attractive objective value.

This concept is an explanatory borrowing from multiobjective optimization, not a NIST-mandated risk formula. If the model omits privacy, accessibility, critical dependencies or long-term harm, its Pareto frontier cannot account for them.

As an **invented numeric counterexample**, imagine three otherwise feasible notification designs evaluated only by delivery delay (seconds, lower is better) and retention of identifiable location history (days, lower is better, after satisfying any mandatory retention requirement):

| Hypothetical design | Delay (seconds) | Retention (days) | Pairwise conclusion under just these two goals |
| --- | ---: | ---: | --- |
| A | 8 | 30 | Dominated by B |
| B | 6 | 14 | Dominates A; trades off with C |
| C | 4 | 21 | Faster than B, but retains more than B |

**B dominates A** because it improves both modeled objectives (6 < 8 and 14 < 30). **Neither B nor C dominates the other**: C reduces delay, while B reduces retention. If a design fails an independent safety, access or legal condition, it is excluded regardless of its position in this table. These numbers are authored assumptions, not measurements of an emergency system.

A common failure is to combine everything into a single weighted score without establishing that the scores have compatible scales, lawful tradeability, complete stakeholder coverage or defensible weights. A large availability benefit does not automatically compensate for violating a non-negotiable safety requirement.

## Worked comparison: emergency notification designs

Imagine an invented public-warning service choosing among designs to preserve alert delivery, message integrity and individual privacy.

**Design A** sends targeted alerts using extensive continuous location tracking. **Design B** sends signed regional alerts without retaining individual location histories. **Design C** sends minimal messages only when an emergency is formally declared, but cannot reach some devices promptly. These are conceptual designs, not products with measured performance.

The stakeholders include service operators, people requiring urgent warning, people whose locations could be collected, emergency responders, and those indirectly affected by delayed instructions.

A defensible comparison would require at least:
- a stated threshold for acceptable delivery delay under emergency conditions;
- an integrity/authenticity requirement for alerts;
- limitations on collection, retention and secondary use of location data;
- an accessible alternative for recipients without the preferred technology;
- treatment of false warnings, missed alerts and compromised delivery infrastructure;
- the authority and evidence required to choose among designs.

Design A might maximize targeting while imposing an excessive surveillance burden. Design B may offer a different balance but depend on credible regional targeting and verified signing. Design C may preserve some privacy at a cost in timely reach. **None can be ranked absolutely from its description alone.** Actual selection needs evidence about coverage, legal constraints, recipient needs and the harms the service is meant to prevent.

This example does not claim that privacy should always override safety or that every emergency legitimizes intrusive surveillance. Each claim is contextual.

## Conflict types that need different reasoning

Different conflicts require different technical treatment:

**Mutually feasible goals.** Two controls can reinforce each other, such as integrity-protected security logs with appropriate retention and restricted access. Tradeoffs should not be assumed where appropriate engineering could satisfy both.

**Resource conflicts.** Memory, compute, power, bandwidth and labor may constrain levels of protection. A design can be infeasible without making a goal illegitimate.

**Safety-security tensions.** A security rule might reject a command that a safety function requires to prevent injury; or a safety interlock might interrupt normal availability. The correct fail behavior is architecture- and hazard-dependent, not universally “fail open” or “fail closed.”

**Privacy-accountability tensions.** Evidence needed to investigate misuse may reveal behavior beyond the necessary security purpose. Data minimization, separation of duties, deidentification and bounded retention can sometimes improve both without eliminating all tension.

**Short-term/long-term conflicts.** Keeping a vulnerable service active may prevent immediate hardship while preserving exposure. An abrupt shutdown can avoid one harm and cause another. Time matters to the legitimacy and consequence of the choice.

**Distributional conflicts.** Aggregate improvements can conceal concentrated burdens on specific groups. A technically successful control can still be inappropriate where it denies required access or violates legal rights.

[Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md) owns the different harms; this article concerns **how their prevention interacts with legitimate requirements and constraints**.

## Safeguard effectiveness does not settle acceptability

An organization may demonstrate that a monitoring system finds more policy violations after adding invasive data collection. That is evidence of a possible protective effect under tested conditions, not proof that the data collection is necessary, proportionate or lawful.

Conversely, using a low-visibility design can reduce privacy intrusion while weakening detection of certain threats. A complete statement should identify both effects rather than declaring the system “more secure” without specifying which properties and stakeholders are compared.

The [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final) treats privacy problems from data processing as an explicit management concern. [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html) concerns safety aspects affecting people, property and environment, and was confirmed current in 2025. Neither is a universal numerical optimization rule; their source-defined scope must be preserved.

Likewise, the [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final) potential-impact categories concern federal confidentiality, integrity and availability categorization. A high-impact label is a signal for particular security requirements, **not** an automatic waiver of rights or safety obligations.

## When a priority order becomes stale

Priority choices are provisional relative to assumptions, deployment state, dependencies and affected people. A change to a data flow, supply contract, public emergency requirement, trust anchor, system capability or threat model can change the feasible set and the reasons for a prior choice.

A priority that was once justified can be retained only if the necessary evidence and obligations remain applicable. It is possible for an old decision to have been legitimate when made and no longer be appropriate. Reassessing the priority is not evidence that the original harm already occurred.

The **engineering concept** of maintaining conditional priorities belongs here; procedures for governance approvals, risk acceptance, business-impact assessments, legal review and change management belong in [Operational Foundations](../../operational-foundations/README.md).

## Canonical ownership and source references

- [Stakeholders and Protection Needs](stakeholders-and-protection-needs.md): whose interests, expectations and obligations motivate protection.
- [Assets, Resources, and Protected Interests](assets-resources-and-protected-interests.md): the things and interests being protected.
- [Value, Criticality, and Dependencies](value-criticality-and-dependencies.md): indirect importance and common-cause dependence.
- [Adverse Outcomes, Consequences, and Harm](adverse-outcomes-consequences-and-harm.md): effects and potentially incompatible forms of harm.
- [Risk, Scenarios, and Time Horizon](../security-risk-uncertainty/risk-scenarios-and-time-horizon.md): uncertainty and likelihood in a future scenario, not unconditional authority to accept any consequence.
- [Security, Privacy, Safety, and Reliability](../security-meaning-objectives/security-privacy-safety-and-reliability.md): meanings of different objectives that may compete.
- [Fundamentals: Systems & Engineering](../../fundamentals/systems-engineering/README.md): general engineering tradeoffs, feasibility and verification.
- [Operational Foundations](../../operational-foundations/README.md): execution of governance, treatment, prioritization and assessment procedures.

### Primary source starting points

- [NIST SP 800-160 Vol. 1 Rev. 1 (final 2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), §3.7 printed pp. 25–27, stakeholder/system/trades perspectives and protection-needs constraints; Appendix H describes a source-specific engineering process, not this repository's universal procedure.
- [NIST CSF 2.0 (2024)](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), GV.OC outcomes concerning mission, stakeholders, dependencies, legal and contractual obligations.
- [NIST Privacy Framework 1.0 (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final), privacy risk management and individual interests beyond confidentiality failures.
- [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html), safety-specific treatment of potentially unacceptable harm; current following its 2025 review.
- [FIPS 199 (2004)](https://csrc.nist.gov/pubs/fips/199/final), federal potential-impact categorization with defined limits.

**Editorial limitation:** Feasible-set/Pareto notation and all three emergency designs are **hypothetical explanatory constructions**. They do not establish lawful authority, measured protective efficacy, a universal ordering of human interests, or a final risk-acceptance decision. [Technical Review 07](../PILOT-TECHNICAL-REVIEW-07.md) checked six material claim groups, the feasible-set limits and the independently recalculated three-design Pareto example. This working article is **Reviewed (model-assisted) / Core claims checked**, not a legal authority determination, a field-tested optimization, fully source-Verified, permanently canonical-approved or Published. SF-02-07 ownership remains revisionable.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
