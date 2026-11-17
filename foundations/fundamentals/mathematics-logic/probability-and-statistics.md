# Probability and Statistics

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Probability and statistics  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave A Batch 06 audit](../WAVE-A-TECHNICAL-REVIEW-06.md); no independent human review

## Quantifying uncertainty and learning from data

**Probability theory** is a mathematical framework for assigning and reasoning about the likelihood of events under a specified model. **Statistics** develops methods for describing data and making qualified inferences about a population, process, or model using observations and assumptions.

These subjects are connected but distinct. A probability model can be specified without observing new data; statistical inference uses data and modeling assumptions to estimate or assess features of a process. The numerical result of either is meaningful only with its sample space, selection mechanism, and assumptions stated.

The [MIT Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) treat probability, conditional probability, independence, random variables, expectation, variance, and concentration bounds. The [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) connects statistical models with engineering measurement and inference.

## Sample spaces, outcomes, events and probability measures

A **sample space** `Ω` contains possible outcomes under a defined experiment or random process. An **event** is a subset of outcomes. A **probability measure** `P` assigns probabilities to events, subject to axioms including:

- **Nonnegativity:** `P(A) ≥ 0` for an event A.
- **Normalization:** `P(Ω) = 1`.
- **Countable additivity:** For pairwise-disjoint events, the probability of their union equals the sum of their individual probabilities.

In finite settings, these principles imply `P(∅)=0` and `P(Aᶜ)=1−P(A)`. They do **not** imply that all possible outcomes are equally likely. The commonly used rule *favorable outcomes divided by total outcomes* works only when the finite elementary outcomes have equal probabilities.

For a **fair six-sided die** with sample space `Ω={1,2,3,4,5,6}`, `P(even)=3/6=1/2`. A biased die might use the same sample space with different probabilities.

The distinction between the **physical die**, the chosen sample space, and the assigned probability model must be retained. The model does not establish by itself whether the real die behaves as assumed.

## Joint and conditional probability

The probability of `A ∩ B` is the **joint probability** of both events. The **conditional probability** of A given B, when `P(B)>0`, is:

```text
P(A | B) = P(A ∩ B) / P(B)
```

Rearranging gives the multiplication rule:

```text
P(A ∩ B) = P(A | B) · P(B)
```

Conditional probability is **not** automatically causal. A higher probability of A under B than under not-B does not establish that B causes A. Causal assumptions and interventions belong in [Causality and Correlation](../scientific-analytical-reasoning/causality-and-correlation.md).

Two events A and B are **independent** under P when `P(A ∩ B) = P(A)P(B)`. Independence is a property of the probability model, not the same as *no conceptual relation*, *no common history*, or *no apparent association* in a small sample.

Pairwise independence of three events also does **not** necessarily imply mutual independence of all three. The precise collection of independence assumptions matters in statistical models.

## Bayes' theorem as a change of conditioning

For `P(B)>0`, Bayes' theorem follows from the multiplication rule:

```text
P(A | B) = P(B | A) · P(A) / P(B)
```

Suppose a hypothetical instrument flags a defect. Under an invented, simplified model:

| Quantity | Assumed value |
| --- | ---: |
| Prior proportion of defective items, P(D) | 0.02 |
| Flag probability given defect, P(F | D) | 0.90 |
| Flag probability given no defect, P(F | not D) | 0.10 |

The total flag probability is

```text
P(F) = 0.90×0.02 + 0.10×0.98 = 0.116
```

The probability of a defect **conditional on observing a flag** is

```text
P(D | F) = (0.90×0.02) / 0.116 ≈ 0.1552
```

Despite a high flag rate for defective items, the posterior probability of a defect after a flag is approximately **15.5%**, because the modeled defect prevalence is low and false flags occur among many nondefective items.

These are **hypothetical assumptions**, not real inspection performance statistics. The result changes if the base rate, selection mechanism, or conditional probabilities change. Bayes' theorem does not validate those parameters.

## Random variables and probability distributions

A **random variable** `X` is a function mapping outcomes in a probability space to values, usually numerical ones. A **probability distribution** describes how probability is assigned across its possible values.

For a discrete random variable with possible values `x_i` and probabilities `p_i`, its expectation is

```text
E[X] = Σ x_i p_i
```

when the sum is well-defined. The **variance** measures expected squared deviation from the mean:

```text
Var(X) = E[(X−E[X])²] = E[X²] − (E[X])²
```

A fair six-sided die has `E[X]=3.5`, but **3.5 is not a possible single roll**. An expected value summarizes a probability-weighted average, not a guaranteed or most likely observation.

For continuous models, probabilities typically attach to **intervals or measurable sets** rather than to single points under continuous density assumptions. A density can exceed 1 without representing an event probability greater than 1; probabilities are obtained by integrating over intervals.

## Descriptive statistics versus statistical inference

**Descriptive statistics** summarize observed data: counts, frequencies, sample means, medians, variance, quantiles, and distributions. These describe what was recorded under the chosen data scope.

**Statistical inference** uses sample data, sampling assumptions, and a statistical model to draw conclusions about parameters, populations, or hypotheses. The inference can be affected by selection bias, dependent observations, missingness, measurement error, and incorrect distributional assumptions.

For `n` observations `x₁,...,xₙ`, the **sample mean** is

```text
x̄ = (1/n) Σ x_i
```

A commonly used **sample variance** for estimating population variance under appropriate independent, identically distributed assumptions is

```text
s² = [Σ(x_i − x̄)²] / (n−1),  n ≥ 2
```

The denominator `n−1` reflects this particular estimator and its assumptions; another definition of data variance may use `n`. The [NIST handbook on single-population mean comparisons](https://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm) explicitly distinguishes sample mean, sample standard deviation, and population parameters.

A dataset can be described correctly but still be unrepresentative of the population about which a conclusion is made. Numerical precision in software does not eliminate sampling or model uncertainty.

## Confidence intervals and credible intervals are not interchangeable

A **frequentist confidence interval procedure** has a specified long-run coverage interpretation under its model assumptions. A particular 95% confidence interval should not normally be interpreted as assigning a 95% frequentist probability to a fixed parameter already covered or not covered by that realized interval.

A **Bayesian credible interval** expresses probability for a parameter under a specified posterior distribution, which depends on prior and likelihood assumptions. These are different inferential frameworks, even when their numerical intervals happen to resemble each other.

Neither should be confused with a **measurement uncertainty interval**, a software error margin, or an analyst's qualitative confidence judgment. Those interpretation issues are developed in [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) and [Measurement](../scientific-analytical-reasoning/measurement.md).

## Why correlation alone is insufficient

A statistical association between variables can support a description or prediction without establishing causation. For example, a linear correlation coefficient measures a particular kind of association, not a causal mechanism. A well-defined intervention or appropriate causal assumptions are needed for stronger causal claims.

The general mathematics of covariance, correlation and probability distributions belongs here; the analysis of confounders, interventions and counterfactuals belongs under [Causality and Correlation](../scientific-analytical-reasoning/causality-and-correlation.md). Neither area should silently redefine the other's core subject.

## Cross-domain use without domain-specific ownership

Probability and statistics support reliability analysis, network measurements, software testing, industrial process variation, sensor quality, cloud capacity reasoning, and evidence interpretation. These applications do not make any one industry or security workflow the definition of probability.

[Sets and Relations](sets-and-relations.md) supplies sample-space and event-set concepts. [Numbers and Numerical Systems](numbers-and-numerical-systems.md) develops exactness and numerical representation. [Evidence](../scientific-analytical-reasoning/evidence.md) explains support for claims, while [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) addresses interpretation and epistemic limits.

### References

- [MIT Mathematics for Computer Science: probability and random variables](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/).
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/).
- [NIST: One-sample mean tests, sample variance and standard deviation](https://www.itl.nist.gov/div898/handbook/prc/section2/prc22.htm).
- [NIST: What are statistical tests?](https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm).

**Editorial status:** Reviewed (model-assisted) following the scoped [Batch 06 technical audit](../WAVE-A-TECHNICAL-REVIEW-06.md). Not independently human peer reviewed, fully verified, or published.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
