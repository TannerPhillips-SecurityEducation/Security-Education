# Validation and Falsification

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Validation and falsification  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Claims are evaluated against evidence, not merely repeated

**Validation**, in empirical inquiry, is the critical evaluation of whether a claim, interpretation, model, or method is adequately supported for a specified purpose and context. **Falsification** is an attempt to show that a claim is false by confronting it with observations or deductions that would be incompatible with it under stated assumptions. Neither is a universal procedure for declaring all knowledge permanently true or false.

Scientific testing is conditional: interpretation depends on operational definitions, auxiliary assumptions, measurement practices, and the range of possible alternatives. A successful test can increase support without logically guaranteeing a universal empirical claim. A failed test can undermine a claim, but attributing the failure requires examining the test and its assumptions.

The [Stanford Encyclopedia of Philosophy on Scientific Method](https://plato.stanford.edu/entries/scientific-method/) and [Karl Popper](https://plato.stanford.edu/entries/popper/) discuss philosophical foundations and limitations of falsifiability; the latter is a position within philosophy of science, not the only legitimate account of inquiry.

## What exactly is being evaluated?

Distinguish a **claim**, its **operationalized prediction**, the **test arrangement**, observed **results**, and the **inference** from those results.

```text
Claim / model
  -> explicit assumptions + testable prediction
  -> observation or experiment
  -> comparison with prediction
  -> qualified support, revision, rejection, or unresolved result
```

This is a conceptual workflow, not a guarantee that evidence is independent, that a prediction uniquely identifies a model, or that results always force a single decision. Some claims are analytic or mathematical and evaluated by formal proof; some are empirical; some are normative or definitional. Test standards must match the type of claim.

## Falsifiability, falsification, and negative results

A claim is **falsifiable in principle** when some logically possible observations, considered under relevant assumptions, would conflict with it. A **falsifying result** is an observed outcome interpreted as such a conflict. The existence of a possible refuter is not evidence that the refuter occurred.

For the simplified universal hypothesis `All items in collection C have property P`, a verified instance `x ∈ C` with `¬P(x)` is logically incompatible with the universal statement. Yet whether the empirical observation counts as such an instance depends on the reliability of `x`'s identity, inclusion in C, classification of P, and measurement.

A claim like `at least one item in C has P` is not generally refuted by examining a small sample that contains no observed P cases. **Absence from a sample is not logical nonexistence**. Sample coverage and detection capabilities must be evaluated.

## Hypotheses, predictions, and experimental design

A hypothesis is not identical to an observed pattern or a prediction. A prediction follows from a hypothesis together with additional conditions, background theories, and measurement assumptions. Competing hypotheses may make the same prediction.

A rigorous test makes the following explicit:

- The proposition under examination and the scope of generalization.
- The observed or manipulated variables and how they are measured.
- Conditions, controls and expected outcomes under rival explanations.
- Expected sensitivity and potential sources of bias or confounding.
- A comparison criterion chosen before inspecting outcomes when feasible.

[Hypotheses and Experiments](hypotheses-and-experiments.md) owns experimental design; [Causality and Correlation](causality-and-correlation.md) owns causal identification and interventions; [Evidence](evidence.md) owns the relationship between records and support for claims.

## Validation, verification, reproducibility, and replication

The words *verification* and *validation* have discipline-specific meanings. In systems engineering, **verification** commonly asks whether the realized system satisfies specified requirements, and **validation** asks whether it serves intended use or stakeholder needs. These distinctions are developed by [NASA Systems Engineering](https://www.nasa.gov/reference/5-0-product-realization/) and belong canonically to [Systems & Engineering: Verification and Validation](../systems-engineering/README.md).

Empirical claim validation is related but **not synonymous** with engineering acceptance. An implementation can satisfy a formal specification while the specification fails to describe the real-world need. Conversely, evidence may support an empirical model without proving that a constructed system meets its engineering requirements.

**Reproducibility** and **replicability** should be used with a specified convention. The [National Academies report](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science) uses reproducibility for consistent computational results using the same input data, methods and analysis conditions, and replicability for consistent results in separate studies addressing the same question. Other communities may use the terms differently; declare the operative definition.

## Statistical testing does not mechanically prove or disprove hypotheses

A statistical test combines observed data with a model and a decision statistic. A `p`-value is the probability, **under a specified null model and test assumptions**, of observing a result at least as incompatible with the null as the realized one, according to the chosen test statistic. It is **not** automatically the probability that the null hypothesis is true, nor a universal measure of effect size or practical significance.

A non-significant result is not proof that the null is correct. False-positive and false-negative rates, power, sampling, multiple comparisons, and model assumptions all affect test interpretation. The [American Statistical Association statement on p-values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) documents these common misinterpretations; general statistical mechanics belong in [Probability and Statistics](../mathematics-logic/probability-and-statistics.md).

## Worked example: an invalid universal inference

Suppose a researcher asserts: `Every device in a defined batch powers on within five seconds under procedure T.` Ten tested devices all satisfy the threshold.

The ten observations support a limited statement: **ten devices passed under the recorded conditions**. They do not logically prove the universal claim for every device in the batch, unless the ten exhaust the batch and each measurement is reliable under the specified conditions.

Now suppose one additional device is measured at 6.2 s. If the procedure, device membership and timing measurement are all accepted, that result contradicts the universal assertion. If the device was operated under a different power condition, the result may instead expose an uncontrolled auxiliary assumption. Neither explanation should be silently selected.

A revised claim might narrow the population and environmental conditions, or become probabilistic; that revision then requires its own evidential support.

## Robustness, boundaries, and model revision

Testing is most useful when failure modes and rival explanations are made visible rather than hidden. External validity concerns transferring findings across populations and conditions; internal validity concerns whether the design warrants a proposed interpretation; construct validity concerns whether measurements capture intended concepts. Their exact meanings vary by field.

Formal proof establishes consequences of axioms and premises within a formal system; it does not establish that those premises describe the physical world. [Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) develops interpretation and formal guarantees. G-03 formal methods remains within existing approved headings, while general temporality G-04 remains unresolved.

### Sources

- [Stanford Encyclopedia of Philosophy: Scientific Method](https://plato.stanford.edu/entries/scientific-method/).
- [Stanford Encyclopedia of Philosophy: Karl Popper](https://plato.stanford.edu/entries/popper/).
- [National Academies: Reproducibility and Replicability in Science](https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science).
- [American Statistical Association: Statement on p-values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).
- [NASA: Product Realization](https://www.nasa.gov/reference/5-0-product-realization/).

**Editorial status:** Substantive draft; terminology and example claims require a scoped second-pass technical audit. No assessments or operational security methods are introduced.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
