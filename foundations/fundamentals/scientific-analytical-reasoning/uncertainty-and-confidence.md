# Uncertainty and Confidence

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Uncertainty and confidence  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## Knowledge has limits that must be represented

**Uncertainty** describes a limitation in what is known, how precisely a quantity is determined, or which outcomes and explanations remain possible under a specified model. **Confidence** is a judgment about the strength, reliability, or calibration of a conclusion, estimate, or belief under stated criteria.

Neither term has a single numerical meaning for every field. An uncertainty expressed as a **measurement standard uncertainty** is different from uncertainty about a claim's cause, uncertainty arising from a statistical sample, uncertainty about a model's assumptions, or lack of information about whether an event occurred.

Similarly, the word *confidence* might refer to the long-run coverage level of a statistical procedure, a quantified probability under a Bayesian model, or a qualitative analyst judgment. Without context, writing “95% confident” is ambiguous.

The [Stanford Encyclopedia of Philosophy's Epistemology](https://plato.stanford.edu/entries/epistemology/) examines the distinction between belief, justification, evidence and knowledge. The [NIST Measurement Uncertainty guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) documents a specific quantified metrological framework. This reference separates their meanings rather than treating them as interchangeable.

## Sources and types of uncertainty

A useful analytical division is between uncertainty associated with **variability** and uncertainty associated with **limited knowledge**.

| Perspective | Illustrative source | What remains uncertain? |
| --- | --- | --- |
| Outcome variability | Randomized timing or fluctuating process measurements | Which outcome will occur in one realization |
| Measurement uncertainty | Calibration, resolution, environment and method | Which quantity values can reasonably be attributed to a measurand |
| Sampling uncertainty | Finite sample drawn from a larger population | How well sample statistics estimate population properties |
| Model uncertainty | Simplifications, unidentified mechanisms, assumptions | Whether the model adequately represents the target |
| Missing-information uncertainty | Incomplete records or absent observations | Facts not determined from available information |
| Interpretive uncertainty | Ambiguous meanings, attribution or causal explanations | Which interpretation best fits the evidence |

These are **overlapping explanatory perspectives**, not a ratified universal classification taxonomy. One problem may involve several at once.

The terms **aleatory** (often associated with stochastic variability) and **epistemic** (often associated with lack of knowledge) can be useful, but their separation is partly **relative to the model and available information**. A variable described as random under one model may become partly predictable when a previously unavailable causal factor is measured. It is therefore unsafe to claim every uncertainty has an immutable category.

## True, false, and unknown are distinct informational states

A statement has a truth value under a specified logic and interpretation. Separately, an observer or system may or may not **know** its truth value.

For example:

```text
Claim:        The component changed state at 14:03.
Observations: One record says component state = ON at 14:03.
Assessment:   Whether a change occurred at 14:03 is unknown.
```

The record may support the reported state at the observation time, but cannot establish a preceding transition or exact change time without more data. **Unknown does not mean false**, and *not observed* does not mean *did not occur*. The real event may have occurred while its timing or cause remains undetermined.

This is an **epistemic distinction**, not an assertion that classical Boolean truth itself requires a third truth value. See [Boolean and Predicate Logic](../mathematics-logic/boolean-and-predicate-logic.md) for formal truth conditions and [Evidence](evidence.md) for claim-relative support.

## Uncertainty does not automatically supply a probability distribution

Probabilities can quantify uncertainty when a suitable sample space, model and probability assignments are justified. But not every uncertainty can responsibly be converted to a numerical probability.

Some situations have **identified possibilities but unknown probabilities**. Others have ambiguous state definitions, incomplete models, or severe limitations in observations. Assigning an apparently precise number can conceal these limitations.

A qualified report should distinguish whether its stated numerical result was derived from data and an established statistical model, elicited as subjective judgment, or chosen as a scenario assumption.

For example, a forecasting model may give `P(event)=0.7`. This is a claim *under that model*. It does not automatically say the true rate is 70%, that the output is empirically calibrated, or that an individual event will happen. Assessing calibration requires appropriate evaluation over comparable predictions and outcomes.

The mathematical definitions of probability and distributions belong in [Probability and Statistics](../mathematics-logic/probability-and-statistics.md).

## Confidence intervals, credible intervals, and measurement uncertainty

Three commonly confused forms of quantitative uncertainty require separate interpretation.

**Frequentist confidence interval:** A 95% confidence *procedure* is constructed so that, under its stipulated assumptions and repeated application, it covers a fixed population parameter in approximately 95% of repetitions. A realized interval is not generally interpreted as assigning a 95% frequentist probability to that already fixed parameter.

**Bayesian credible interval:** A 95% credible interval can have 95% probability under a specified posterior distribution. That posterior depends on a prior, likelihood, and model assumptions; it is not the same inferential statement as a frequentist coverage guarantee.

**Metrological uncertainty statement:** A reported value plus standard or expanded uncertainty describes values attributed to a measured quantity using a defined metrological procedure. A notation such as `8.3 ± 0.5 cm` is not self-explanatory without the uncertainty type, conditions, and any coverage interpretation.

The [JCGM VIM: Measurement Uncertainty](https://jcgm.bipm.org/vim/en/2.26.html) defines measurement uncertainty as a non-negative parameter describing dispersion of quantity values attributed to a measurand. It is not simply the instrument's observed error.

A measurement procedure, a statistical interval and a qualitative confidence judgment may all be useful for a decision, but one cannot be converted into another without an explicit model.

## The example of a proportion from a sample

Suppose, purely hypothetically, that 100 **independent, representative** items are inspected and 80 meet a specified condition. The **observed sample proportion** is `p̂=80/100=0.80`.

Under a simplified independent Bernoulli sampling model, a plug-in estimate of its standard error is

```text
SE(p̂) ≈ sqrt[p̂(1−p̂)/n]
       = sqrt[0.8×0.2/100]
       = 0.04
```

A naive normal-approximation 95% interval is `0.80 ± 1.96×0.04`, approximately `[0.7216, 0.8784]`.

**This is an illustrative calculation, not a universal or automatically valid confidence interval.** Its coverage relies on sampling and distributional assumptions; alternative interval procedures may give different endpoints and more reliable coverage. The data do not demonstrate that the sample was truly representative or independent. Measurement and classification errors could further affect the meaning of the proportion.

The useful lesson is not a specific percentage. It is that the **assumptions required by a confidence statement must travel with the result**. The [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) develops inferential procedures and their assumptions in more depth.

## Qualitative confidence and evidence quality

Sometimes evidence does not warrant a defensible numeric probability. A qualitative confidence statement may instead communicate how robustly an explanation is supported, but its criteria should be explicitly stated.

A defensible qualitative judgment considers:

- **Source reliability:** Were acquisition and recording mechanisms appropriate and sufficiently checked?
- **Coverage and completeness:** Could the decisive information have been missed?
- **Independence:** Are multiple observations genuinely independent or repetitions of one source?
- **Alternative explanations:** Have plausible rivals been investigated?
- **Model limitations:** Do important conclusions rely on untested assumptions?
- **Consistency and reproducibility:** Do results agree with independent checks under comparable conditions?

These are **review considerations**, not a formally approved ordinal confidence scale. A label such as *high confidence* should not be mistaken for a verified numerical probability. A detailed explanation of evidence strength belongs in [Evidence](evidence.md), and competing explanatory inferences in [Deduction, Induction, and Abduction](deduction-induction-abduction.md).

## Uncertainty, decision-making, and calibration

A decision may be required despite uncertainty. But a decision rule and an evidence statement perform different functions.

A rule such as “act when the estimated risk exceeds a threshold” specifies a **decision criterion**. It does not prove the estimate correct or justify that threshold. Consequences of false positives and false negatives, costs, available alternatives and the feasibility of further observation belong to the decision context.

**Calibration** of probabilistic forecasts means, roughly, that events assigned similar probabilities occur at corresponding frequencies across an appropriate collection of predictions under a stated evaluation approach. Calibration of a **measurement instrument** refers instead to relationships between standards and indications. These uses share a word but describe distinct methods.

No one source of uncertainty can be eliminated simply by labeling a prediction “certain.” Transparent uncertainty reporting is therefore central to technical reasoning, engineering and professional responsibility.

## Canonical relationships

[Observation](observation.md) covers acquisition limitations. [Measurement](measurement.md) owns metrological uncertainty. [Evidence](evidence.md) owns claim-relative support. [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns numerical probability and statistical inference. [Hypotheses and Experiments](hypotheses-and-experiments.md) owns experimental discrimination, and [Causality and Correlation](causality-and-correlation.md) owns causal identification assumptions.

### References

- [Stanford Encyclopedia of Philosophy: Epistemology](https://plato.stanford.edu/entries/epistemology/).
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty).
- [JCGM VIM 2.26: Measurement Uncertainty](https://jcgm.bipm.org/vim/en/2.26.html).
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/).
- [NIST: Sample mean, standard deviation and inference](https://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm).

**Editorial status:** Authoring Draft. The proportion interval is an explicitly limited textbook-style example, not a claim about real inspection results. The terms epistemic, aleatory, confidence, calibration and measurement uncertainty require the documented source distinctions above. A scoped technical acceptance review remains pending.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
