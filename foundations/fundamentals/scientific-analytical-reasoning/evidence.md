# Evidence

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Evidence  
**Development status:** Reviewed (model-assisted; not independently human-accepted for final publication)  
**Source review:** Core claims checked in [Wave A technical review, Batch 01](../WAVE-A-TECHNICAL-REVIEW-01.md); complete independent expert validation not claimed

## Information becomes evidence in relation to a claim

**Evidence** is information or material considered for the support, criticism or evaluation of a claim. Its significance is **relational**: what supports one hypothesis may be irrelevant, ambiguous or even contrary to another. The concept extends beyond digital records to observations, instrument readings, physical samples, documents, calculations, testimony and experimental results.

Evidence is not equivalent to **truth** or **proof**. A fact can provide some evidential support for a hypothesis without establishing it conclusively, and a valid-looking record may be inaccurate or misleading. The [Stanford Encyclopedia of Philosophy's entry on Evidence](https://plato.stanford.edu/entries/evidence/) documents competing philosophical accounts of what counts as evidence and how it bears upon justified belief. This article uses a pragmatic, claim-relative definition for technical reasoning, not a universal metaphysical resolution.

An observation produces or recognizes information under particular conditions. A record represents information. The same record's **evidential relevance** depends on the question or claim; **reliability** is a distinct consideration that affects the weight we should give the evidence. An unreliable record can still be relevant, and a reliable record can still be irrelevant. The [Observation](observation.md) article develops the observational side of this distinction.

## Claim, evidence, and inference

A structured analysis separates at least three elements:

| Element | Role |
| --- | --- |
| **Claim / hypothesis** | What is proposed to be true |
| **Evidence item** | Material or information considered relevant |
| **Inference** | The reasoning used to connect evidence to the claim |

Additional considerations may include the background assumptions, possible alternative explanations, acquisition mechanism and uncertainty.

Suppose a sensor log records `level = 8.3 cm`. Under a functioning sensor and appropriate unit calibration, that record may support **the claim that the indicated level exceeded 8.0 cm at the sampled time**. It does not, without more, establish a particular cause, precisely when the level crossed 8.0 cm, or that the sensor was physically safe or unsafe.

The evidence item is the same while the claims differ. Evaluating evidence therefore requires stating *what it can and cannot justify*.

## Relevance, reliability, sufficiency, and independence

Four distinctions are particularly important.

**Relevance** concerns whether an item bears on the claim at all. A correct measurement might be irrelevant to a hypothesis about an unrelated component.

**Reliability** concerns reasons to believe the item accurately represents what it purports to represent, given acquisition, calibration, transmission, context and processing limitations. A reliable record can still be irrelevant.

**Sufficiency** concerns whether the assembled evidence and inference warrant the strength of the conclusion. One relevant data point can be insufficient to distinguish among competing explanations.

**Independence** concerns the relationships among evidence items. Two reports copied from the same original source are not automatically two independent observations. Treating correlated information as independent can exaggerate support.

These are **analytic quality dimensions**, not a mandated four-part evidence ontology. Their purpose is to prevent the same piece of information from being mistaken for multiple independent confirmations.

## Confirmation, counterevidence and alternatives

Sound investigation looks for evidence capable of **discriminating** among rival hypotheses.

Imagine two hypotheses for a rising temperature measurement:

- **H1:** The physical environment became warmer.
- **H2:** A sensor offset or calibration error changed.

A single higher sensor reading may be consistent with both. An independently calibrated second sensor, an ambient measurement or a trace of the device's calibration history may help discriminate. Even then, claims should account for uncertainty and the possibility of additional explanations.

**Counterevidence** may weaken a hypothesis, but a failed prediction only refutes a hypothesis under its auxiliary assumptions. If an instrument has failed, the absence of a predicted indication might not mean the phenomenon did not occur. The [Stanford Encyclopedia's Theory and Observation in Science](https://plato.stanford.edu/entries/science-theory-observation/) discusses how observation reports, theories and auxiliary assumptions interact in scientific inquiry.

A technical reference should not equate *not observed* with *did not occur* unless coverage and detection assumptions justify that inference.

## Provenance and transformation

Evidence can be affected by the path from original phenomenon to analytical presentation:

```text
Phenomenon
  -> acquisition mechanism
  -> initial indication
  -> representation or record
  -> transformation / selection
  -> interpreted evidence
  -> qualified conclusion
```

This is an **illustrative analytical sequence**. Not every item of evidence passes through each step, and not all evidence begins as a machine measurement.

A transformed record can remain useful, but each processing step may change precision, context, units, timing, or interpretability. When reconstructing an argument, track what was collected, what changed, and which assumptions justified using the result.

The canonical general treatment of [Data Provenance and Lifecycle](../information-data/README.md) belongs within Information & Data. Domain-specific investigation methods belong in Operational Foundations, not in this article's general definition.

## Quantification and confidence

Probability and statistics can sometimes express the strength of evidential support, but there is no universal numeric conversion from every observation to a degree of belief. Bayesian updating, likelihood comparisons, classical statistical testing and qualitative confidence assessments answer different questions with different assumptions.

A test's low *p*-value, for example, does **not** give the probability that the null hypothesis is true. A *p*-value expresses how extreme specified data or a test statistic would be under a chosen statistical model and null-hypothesis assumptions. The [American Statistical Association's explanation](https://doi.org/10.1080/00031305.2016.1154108) explicitly distinguishes *p*-values from probabilities of hypotheses. Similarly, *high confidence* expressed in a report should communicate the basis and limitations of the judgment, not just a label.

Our [Probability and Statistics](../mathematics-logic/README.md) heading owns the mathematical models, while [Uncertainty and Confidence](README.md) owns interpretation and knowledge limits.

## Worked example: one record, three claims

Assume an instrument correctly records a digital `ON` state at 14:03, but no earlier samples are available.

| Claim | Evidential relevance of this record |
| --- | --- |
| The device was reported ON at 14:03 | Directly relevant, subject to instrument and timestamp reliability |
| The device switched ON at exactly 14:03 | **Insufficient**: the earlier state and transition time are unknown |
| A particular user switched the device ON | **Insufficient**: the record does not identify a causal actor |

The example illustrates that the same data can support a narrow claim while leaving broader explanations unresolved. Identifying a possible alternative is not itself evidence that the alternative occurred.

## Connections to canonical knowledge

[Observation](observation.md) explains acquisition and limitations; [Entities and Attributes](../models-abstraction/entities-and-attributes.md) explains modeled subjects and properties; [Sets and Relations](../mathematics-logic/sets-and-relations.md) supplies formal association language. [Data Provenance and Lifecycle](../information-data/README.md) owns information history; [Hypotheses and Experiments](README.md) owns experimental discrimination; [Uncertainty and Confidence](README.md) owns knowledge qualification.

## References and publication state

- [Stanford Encyclopedia of Philosophy: Evidence](https://plato.stanford.edu/entries/evidence/), multiple epistemic accounts of evidence and its significance.
- [Stanford Encyclopedia of Philosophy: Theory and Observation in Science](https://plato.stanford.edu/entries/science-theory-observation/), observation reports, theory and empirical justification.
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty), instrument-mediated measurement and limitations.
- [American Statistical Association: Statement on *p*-values](https://doi.org/10.1080/00031305.2016.1154108), for correct interpretation of *p*-values and inferential limits.

**Editorial state:** This is an original technical-reference synthesis, not a legally binding evidentiary standard or an assessment activity. The relevance/reliability distinction and statistical language have been corrected against the cited references. The Wave A audit records scope, evidence, and remaining editorial limitations.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Pilot claim audit](../PILOT-CLAIM-SOURCE-AUDIT.md)
