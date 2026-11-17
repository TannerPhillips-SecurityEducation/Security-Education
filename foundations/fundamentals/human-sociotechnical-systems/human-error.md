# Human Error

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Human error  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source technical review pending

## An error occurs in a system of people, tasks and conditions

**Human error**, in a defined operational context, describes an **unintended** action, omission or decision that deviates from a relevant intention or correct plan. An adverse outcome is not itself proof that a particular human error occurred. An **intentional procedural violation** is a distinct category of human failure in common safety-engineering frameworks, rather than an unintentional error. Neither label by itself establishes why the behavior occurred, whether a person was negligent, or whether the system design and procedures were adequate.

Human-system failures can result from interacting causes: workload, ambiguity, equipment state, training, incentives, task design, interruptions, organizational pressures, hidden dependencies, incomplete procedures and individual choices. A meaningful analysis separates **what was observed**, **what was expected**, **what constraints applied**, and **what explanation evidence supports**.

[NASA Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/) addresses human factors, workload, task conditions and design-induced errors. [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration) develops integration of human capabilities into engineered systems.

## Intention, action and result are not interchangeable

An **intention** is what a person aims to accomplish. An **action** is what they actually do or omit. An **outcome** is what happens as the system responds. These can diverge:

```text
Intended: Disable Heater A
Action:   Select nearby control labeled Heater B
Outcome:  Command to Heater B acknowledged
```

The scenario describes a divergence between intention and action. It does **not** establish a unique root cause. Possible influences include button arrangement, labeling, focus state, interruption, competing demands, unfamiliar equipment or simple execution error. It is premature to infer carelessness or incompetence from the trace alone.

If the system later reports Heater A as still enabled, that report is another observation, not proof of a particular cognitive process.

[Human Cognition and Perception](human-cognition-and-perception.md) owns attention and interpretation; [Human-Computer Interaction](human-computer-interaction.md) owns control and feedback design.

## Slips, mistakes, and violations require different evidence

Safety-engineering frameworks such as the [UK Health and Safety Executive's guidance on managing human failures](https://www.hse.gov.uk/humanfactors/topics/humanfail.htm) distinguish **slips** (unintended execution errors), **lapses** (memory-related omissions), **mistakes** (errors in planning or judgment), and **violations** (intentional departures from a rule or procedure). Violations are distinguished from unintentional errors; a violation is not automatically malicious, and identifying one does not by itself establish that the rule was practicable or appropriate.

The same visible outcome can arise through several pathways. Clicking an incorrect button might be a slip, but selecting it intentionally because a label was misunderstood suggests a different mechanism. Choosing to depart from a procedure can reflect pressures, conflicting instructions, a broken procedure or deliberate misconduct. **Classification requires evidence about intention and context**, not just a failed outcome.

The purpose of distinguishing mechanisms is to choose proportionate interventions; it is not to infer someone’s character from a single event.

## Error tolerance and recovery

A **robust human-system design** may make unintended actions less likely, detectable, reversible or less consequential. Potential mechanisms include differentiation of similar controls, feedback confirming the affected object, validation of critical inputs, safe defaults, meaningful undo, staged authorization and well-designed recovery procedures.

These are possible safeguards, not universally effective prescriptions. A confirmation dialog can reduce some errors but also generate alert fatigue. A rigid procedure can prevent one failure mode while creating an unworkable task under unusual conditions. Changes must be tested within the relevant work context.

A **near miss** is an event that could have produced an adverse outcome but did not under the stated criteria. Investigating near misses can reveal latent weaknesses; however, not every recorded deviation is evidence of a serious hazard.

## Worked example: one outcome, multiple explanations

Suppose a technician enters `20` into a field labeled only `Temperature`, while the system interprets the value as degrees Celsius. The technician intended 20 °F.

The entered number is syntactically admissible, but it expresses a different temperature under the two unit conventions. Without further information, the case may involve an unclear interface contract, a misunderstood unit, a deficient procedure, or other causes.

An improved design could display the unit beside the input, show a conversion preview, validate permitted values and record the source interpretation. The improvement hypothesis needs evaluation; none of these steps proves that every future error is eliminated.

[Units and Quantities](../mathematics-logic/units-and-quantities.md) owns conversion mathematics. [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns declared interaction semantics.

## Investigation, accountability and learning

**Accountability** concerns responsibility under specified duties and authority. **Causal explanation** concerns what contributed to an outcome. **Blame** is a normative judgment and may not follow directly from either. Conflating them can discourage reporting or conceal design weaknesses.

A well-grounded review distinguishes observations, missing data, explanations, rejected alternatives, evidence strength and improvement opportunities. It can consider individual choices and organizational conditions without assuming that one excludes the other.

[Organizational Structures](organizational-structures.md) owns authority and role allocation. [Ethics and Professional Responsibilities](ethics-and-professional-responsibilities.md) owns duties and harm-related judgments. [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns system-level failure criteria and models, rather than defining human behavior as a component failure probability.

### Sources

- [UK Health and Safety Executive: Managing Human Failures](https://www.hse.gov.uk/humanfactors/topics/humanfail.htm).
- [NASA: Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).
- [NIST: Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design).

**Editorial status:** Substantive Draft. Both error examples are invented; causal interpretations and terminology require a dedicated scoped review. No blame-based classification or training assessment is introduced.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
