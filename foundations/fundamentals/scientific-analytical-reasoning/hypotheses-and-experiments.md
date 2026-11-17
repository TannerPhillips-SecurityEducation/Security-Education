# Hypotheses and Experiments

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Hypotheses and experiments  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending

## A hypothesis proposes an explanation; an experiment creates a discriminating observation

A **hypothesis** is a proposed claim that may describe, explain, or predict a phenomenon. In scientific reasoning, a useful hypothesis specifies what follows under assumptions and what observations or interventions might bear upon its credibility.

An **experiment** is an inquiry deliberately arranged to produce observations relevant to a question. A controlled experiment typically varies selected **factors** or applies treatments to **experimental units**, measures outcomes, and attempts to limit alternative explanations. Not every investigation can manipulate its subject, and not every hypothesis can be tested by a randomized controlled experiment. Observational studies, simulations, natural experiments, and formal analysis require separate assumptions.

The general purpose is not to manufacture confirmation. It is to expose a claim to information that could meaningfully distinguish it from competing explanations.

The [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm) provides engineering guidance on choosing experimental designs, including completely randomized, blocked, factorial, and response-surface designs. This article explains the **conceptual mechanisms**, not a vendor or application-specific experiment procedure.

## The structure of a scientific hypothesis

A hypothesis requires attention to:

| Component | Role |
| --- | --- |
| **Subject / phenomenon** | The event, behavior, quantity, or relationship being investigated |
| **Claim** | What is proposed about that subject |
| **Assumptions** | What the claim presumes about conditions, instruments, and models |
| **Implications / predictions** | What outcomes would be expected if the hypothesis and assumptions hold |
| **Alternative explanations** | Other claims consistent with some or all existing evidence |
| **Evaluation method** | How evidence would be acquired and interpreted |
| **Limitations** | Circumstances in which the inference may fail |

This seven-facet decomposition is **editorial guidance**, not a universal formal hypothesis schema.

A statement can be precisely worded yet poorly testable if key terms have no operational meaning. Conversely, a measurable association can be real without revealing its cause. Clear hypotheses therefore distinguish **measurement**, **association**, and **causal explanation**.

## Experimental units, factors, treatments, and response variables

An **experimental unit** is the smallest unit to which a treatment is independently applied under the design. A **factor** is a condition or explanatory variable whose levels may be varied or compared. A **treatment** is a specified factor level or combination of levels. A **response variable** is what the experiment seeks to observe or measure.

Imagine studying whether fan speed changes how quickly a container cools.

- **Experimental unit:** A cooling run or container-run combination to which a fan setting is independently assigned **under a design that treats runs as units and controls carryover**. Repeating runs on the same physical apparatus may introduce dependence that the design must address.
- **Factor:** Fan speed, with levels `low` and `high`.
- **Response:** Time needed for a specified, consistently defined temperature drop.
- **Potential nuisance factors:** Starting temperature, room temperature, container material, airflow geometry, sensor behavior.

The choice of unit determines the independence assumptions. Several measurements from **one cooling run** are repeated observations of that run, not automatically several independent experimental units. Random assignment alone does not make repeated runs statistically independent if unmodeled carryover, shared drift, or time effects remain. Mistaking repeated measurements for independent replication is a common source of overconfident estimates.

## Randomization, replication, and blocking

Experimental designs use several techniques to prevent systematic factors from masquerading as treatment effects.

**Randomization** allocates treatment conditions to eligible units by a stated random process. It reduces the risk that treatment assignment systematically follows an unmeasured factor, although a particular finite randomized assignment can still be imbalanced.

**Replication** applies treatments to distinct experimental units, allowing the investigator to estimate variability and examine repeatability under the design. Replication should not be confused with merely sampling one run repeatedly.

**Blocking** groups units sharing a relevant nuisance condition, then compares treatments within those groups. For example, grouping experiments by room temperature regime may reduce noise introduced by changing ambient conditions. Blocking controls or models that variation; it does not make all nuisance effects disappear.

**Controls** provide useful baselines or comparison conditions. A comparison need not be a universally fixed treatment called “control”; what matters is that the design supports the intended contrast.

The [NIST/SEMATECH completely randomized design guidance](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm) explains treatment-level assignment and replication, and its [randomized block design guidance](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) explains how nuisance factors can be handled through blocking. Both approaches require well-defined experimental units and analysis assumptions.

## Confounding and causal claims

**Confounding** occurs when effects of factors cannot be separated adequately under the design or analysis. If all low-speed fan runs happen in a cool room and all high-speed runs in a warm room, fan-speed and room-temperature effects could be confounded.

Changing a factor while observing a response is not by itself sufficient to prove the factor caused the result. The inference requires attention to the assignment mechanism, assumptions, controls, measurement quality, time-dependent conditions, and plausible alternatives.

A factorial design can deliberately vary multiple factors to investigate their **main effects** and **interactions**. This can be more informative than changing one factor at a time, but it demands careful definition of the response and assumptions. The [NIST handbook on choosing experimental designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri33.htm) differentiates comparative, screening, and response-surface objectives.

The presence of a correlation or a statistically significant coefficient is not itself a causal mechanism. See the approved subject [Causality and Correlation](README.md) for causal reasoning, which is distinct from experimental setup.

## A worked two-condition design illustration

Suppose eight **independent** cooling runs are possible. Four are randomly assigned `low` fan speed and four `high` fan speed. All use an explicitly defined starting-temperature interval, the same container design, and a consistent measurement method. The resulting cooling times could be:

```text
Low:  16, 15, 17, 16 minutes
High: 11, 12, 10, 11 minutes
```

The sample mean for low speed is `16` minutes; the sample mean for high speed is `11` minutes, a difference of `5` minutes in the observed samples. Under this **hypothetical design**, the data are consistent with faster cooling at the higher fan setting.

The data alone do **not** establish a universal causal effect or a particular confidence level. The sample is small, measurement uncertainty has not been quantified, independence is assumed, and uncontrolled conditions could still matter. The values are fabricated explanatory examples, not experimentally observed data.

A reader should be able to inspect exactly what was varied, how it was assigned, what was measured, and what alternative explanations remain credible.

## Experimental validity, falsification, and reproducibility

**Internal validity** concerns how defensibly a result supports a causal conclusion within the studied conditions. **External validity** concerns how far conclusions may generalize beyond them. Both depend on design and assumptions; high internal validity is not proof of unrestricted generalization.

**Falsification** refers to critically testing whether the predicted consequences of a hypothesis withstand evidence. A failed prediction can be evidence against a hypothesis, but it may also reflect mistakes in an instrument, auxiliary assumption, or model. Conversely, one matching observation does not logically prove a general claim in all contexts.

**Reproducibility** and **replicability** are often used differently across disciplines. The appropriate meaning should be defined in the context rather than presumed. Independent replication of a study is more informative when methods, raw observations, instruments, and analysis decisions are transparent.

Scientific validation, formal proof, software testing, and engineering verification have distinct goals and should be linked, not collapsed into a single word *test*. See [Validation and Falsification](README.md) and [Verification and Validation](../systems-engineering/README.md).

## Observation, evidence, and model assumptions

The conceptual chain can be represented as:

```text
Question and candidate hypotheses
             |
     Experimental design
             |
      Acquisition/measurement
             |
        Results/records
             |
  Comparison with predictions
             |
    Qualified interpretation
```

This is a possible research process, not a mandatory reading order or assessment method. Every stage can introduce selection, measurement, or modeling limitations. Recorded values gain relevance as [Evidence](evidence.md) only in connection with the claim under consideration; [Observation](observation.md) and [Measurement](measurement.md) provide the underlying acquisition vocabulary.

## Sources and current editorial state

- [NIST/SEMATECH: Completely randomized designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm).
- [NIST/SEMATECH: Randomized block designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm).
- [NIST/SEMATECH Engineering Statistics Handbook: Choosing an Experimental Design](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm).
- [NIST: Selecting an Experimental Design](https://www.itl.nist.gov/div898/handbook/pri/section3/pri33.htm).
- [Stanford Encyclopedia of Philosophy: Theory and Observation in Science](https://plato.stanford.edu/entries/science-theory-observation/).

**Editorial review note:** Experimental-unit independence and carryover assumptions were tightened; the fan-speed sample means and differences were independently recalculated. The data remain explicitly hypothetical and do not establish a causal effect or confidence interval. A scoped Wave A Batch 03 source audit records the internal technical review, not external human sign-off.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
