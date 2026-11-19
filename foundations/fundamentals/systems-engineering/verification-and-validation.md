# Verification and Validation

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Verification and validation  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 04 audit](../WAVE-B-TECHNICAL-REVIEW-04.md); no independent human peer review

## Conformance and fitness for use are separate claims

Within systems engineering, **verification** evaluates whether a product, element or design satisfies specified requirements under defined criteria. **Validation** evaluates whether the realized system or proposed solution satisfies stakeholder needs and performs appropriately in its intended environment. They are complementary, but one does not imply the other.

The [NASA Product Realization](https://www.nasa.gov/reference/5-0-product-realization/) guidance distinguishes evidence of conformance to requirements from fitness for customer and user expectations. [SEBoK System Verification](https://sebokwiki.org/wiki/System_Verification) develops comparison against the reference that defines an expected result.

This article owns **engineered-system evaluation**. [Validation and Falsification](../scientific-analytical-reasoning/validation-and-falsification.md) owns broader criticism of empirical claims. [Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns consequences derivable within a formal model. A mathematically verified property does not automatically establish an implementation's fitness for use.

## A claim requires a subject, criteria and evidence

A defensible verification record identifies the **item tested**, its **configuration and revision**, the **requirement and expected result**, the **method**, the **actual observed result**, relevant **conditions**, and the qualified **disposition**. Omission of these details can make an apparently precise result uninterpretable.

An evaluation has at least three separable parts:

```text
Declared criterion → selected method and conditions → observed result
                                  ↓
                        comparison and qualified decision
```

A *pass* is a conclusion under selected criteria and available evidence, not a guarantee that no untested fault exists. A failed test may reflect a nonconforming product, an invalid environment, faulty instrumentation, or a misunderstood requirement. The explanation requires further evidence.

## Methods of verification

Engineering verification can use **inspection**, **analysis**, **demonstration**, **test**, or combinations, depending on the organization and item. These are not interchangeable:

| Illustrative method | What it may establish | What it does not automatically establish |
| --- | --- | --- |
| Inspection | Visible or documented characteristic satisfies a criterion | Behavior under all operating conditions |
| Analysis | A modeled property follows from justified calculations | Perfect correspondence between model and system |
| Demonstration | Required operation can be shown in selected conditions | Exhaustive behavior under all conditions |
| Instrumented test | Measured response meets a specified threshold in tested cases | Untested cases cannot fail |

Formal checklists and acceptance categories depend on the governing engineering context; this article does not impose a universal four-method method taxonomy.

A **test** is not equivalent to a learner assessment. This repository remains a technical reference without Knowledge Checks or Practical Assessments.

## Worked example: time-constrained response

Suppose an invented controller requirement states:

```text
For every valid input in the specified operating envelope,
a command must be produced within 200 milliseconds
measured between accepted input and command output.
```

Five instrumented test responses, in milliseconds, are `[120,158,190,205,175]`. Under exact measurements and a decision rule requiring **every tested result** to satisfy the threshold, four measured responses pass and one, `205 ms`, fails. The observed maximum is `205 ms`; the arithmetic mean is `848/5 = 169.6 ms`.

The **mean passes a 200 ms threshold**, but the stipulated per-event requirement is not thereby satisfied. An aggregate statistic cannot replace the required event-level condition. Conversely, five passing cases alone would not establish the universal requirement for all possible valid inputs.

If measurement uncertainty could change the disposition, it must be reported and handled under an explicit decision rule. The results are fictional and not an empirical performance claim about a real controller.

## From a requirement to a defensible disposition

A traceability link can establish *which evidence was intended to evaluate a requirement*, but the link itself does not establish conformance. A complete evaluation must bridge **specified rule, applicable configuration, test conditions, observed results, uncertainty and decision rule**. The distinction becomes visible in the controller example above.

Assume the hypothetical controller is configuration `C1`, tested under procedure `T-200` against requirement `R-200` (each valid response is no more than 200 ms). Treat the five results as **invented exact observations** for now. A compact evaluation trace is:

| Evidence reference | Observation (ms) | Criterion applied | Disposition under exact values |
| --- | ---: | --- | --- |
| `E1` | 120 | `response ≤ 200` | Meets criterion |
| `E2` | 158 | `response ≤ 200` | Meets criterion |
| `E3` | 190 | `response ≤ 200` | Meets criterion |
| `E4` | 205 | `response ≤ 200` | Does not meet criterion |
| `E5` | 175 | `response ≤ 200` | Meets criterion |

The chain can be written `R-200 → T-200 → {E1,...,E5} → evaluation of R-200 on C1`. With exact timings and valid testing, `E4` contradicts the per-response requirement in the tested case. Four conforming observations cannot cancel one failure by averaging. Even if all five passed, the finite sample would not logically establish a universal claim across every valid input and condition. A credible verification report would additionally identify the actual build, environmental envelope, calibrated instruments, input stimuli, timestamp/clock interpretation, procedure version, and any deviation from the procedure.

### A bounded-error counterexample

Now **change the measurement assumption**, not the observed numbers: suppose every instrument-reported time has a stipulated **maximum absolute error of 8 ms** under the tested conditions. This is a hypothetical hard bound, not a statistical confidence interval or a reported calibration result. Each true response time is only known to lie in `[measured − 8, measured + 8]`.

For an upper-limit criterion `t ≤ 200 ms`, a conservative result-level rule is:

- **Demonstrated conforming:** entire possible interval is at most 200 ms, so `measured + 8 ≤ 200`.
- **Demonstrated nonconforming:** entire possible interval exceeds 200 ms, so `measured − 8 > 200`.
- **Indeterminate from this measurement:** interval crosses the limit. Additional calibrated measurement or an approved decision procedure is required.

Under this changed assumption, `E3` becomes `[182,198]` ms and remains demonstrably within the limit. `E4` becomes `[197,213]` ms: it is **indeterminate**, not conclusively failed or passed. The earlier **exact-value** conclusion was valid only under its declared exact-measurement assumption. Different tolerances, probabilistic uncertainty models, customer acceptance rules, or instrument faults need different reasoning. For uncertainty concepts see [Measurement](../scientific-analytical-reasoning/measurement.md).

A reported `pass`, `fail`, `indeterminate`, `waived`, and `accepted` describe different states. A waiver is a governance decision, not a measurement correction. An incomplete set of operating conditions is a *coverage limitation*, not a quantified percentage of the envelope unless that envelope and sampling scheme have been defined.

### Verification evidence is not validation evidence

Even an eventual compliant timing record for `R-200` would not establish that the controller maintains comfortable temperature in the intended building. That distinct stakeholder outcome requires its own definition, representative context, and **end-to-end evidence**: sensing accuracy, actuator capability, heat-loss conditions, feedback behavior, and actual room outcomes may matter. The timing requirement and comfort need can each have traceable evidence while reaching different decisions.

NASA's [Systems Engineering Handbook, §5.3 Product Verification](https://www.nasa.gov/reference/5-3-product-verification/) distinguishes test observations, discrepancy reporting, and the requirement-compliance record; [§5.0 Product Realization](https://www.nasa.gov/reference/5-0-product-realization/) distinguishes requirements conformance from stakeholder fitness in the intended environment. This is an engineering analogy, not a claim that NASA has approved this editorial test matrix. [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns the origin and version history of evidence records, not the requirements-conformance judgment.

## Requirements versus intended operational use

A system can be verified against poorly chosen requirements yet not serve users. For example, a heating controller might satisfy a command-timing requirement but fail to maintain acceptable room temperature because the sensor measures the wrong location or the actuator is undersized.

**Validation** therefore considers stakeholder expectations, use context, operating scenarios and the end-to-end capability. It may include observing representative use, analyzing scenarios, comparing outcomes to measures of effectiveness, or other justified methods. No one demonstration proves suitability in every environment.

[Requirements](requirements.md) owns definition, traceability, quality and allocation. [Architecture and Composition](architecture-and-composition.md) owns the design alternatives being evaluated.

## Qualification, uncertainty and scope

A verification method has a **scope**: selected modes, interfaces, environmental conditions, scenarios, data and configurations. Coverage is limited by what was inspected, modeled, executed or observed.

Simulation output is evidence about behavior **under the simulation model**. Hardware tests produce observations about a particular tested product and environment. Neither should be presented as universal correctness without a justified extrapolation. Human judgment may be involved in assessing whether results satisfy stakeholder intent.

**Regression verification** checks whether previously required behavior is preserved after changes under a stated test scope. A version change can invalidate earlier evidence or make additional evidence necessary. Passing an earlier revision does not automatically verify a later revision.

## Integration, anomalies and acceptance

Element-level verification does not guarantee whole-system integration. The combined product can violate shared timing, resource, interface, safety or usability requirements even when parts independently meet their criteria. Integration tests must define their own scopes and acceptance criteria.

An **anomaly** is a departure from expectation, not necessarily a confirmed defect. An unexpected result can reflect the system, model, procedure or instrumentation. Resolution requires a recorded investigation and evidence; changing a requirement merely to make a failed result pass is not an acceptable inference.

The engineering review process should distinguish a test being executed, an observed result, an evaluator's judgment, an approved waiver and final stakeholder acceptance. These are different statuses and may require different authorities.

## Boundaries and references

[Measurement](../scientific-analytical-reasoning/measurement.md) owns quantitative measurement and uncertainty. [Evidence](../scientific-analytical-reasoning/evidence.md) owns evidentiary quality. [Reliability and Failure](reliability-and-failure.md) owns failure-probability and restoration models. [System Lifecycle](system-lifecycle.md) owns evaluation across revisions and stages.

This reference introduces no mandatory test platform, certification regime, training assessment or repository-wide acceptance policy.

### Sources

- [NASA: Product Realization](https://www.nasa.gov/reference/5-0-product-realization/).
- [NASA: Design Solution Definition](https://www.nasa.gov/reference/4-4-design-solution-definition/).
- [SEBoK: System Verification](https://sebokwiki.org/wiki/System_Verification).
- [NASA: Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/).

**Editorial status:** Reviewed (model-assisted) under the scoped [Wave B Batch 04 technical review](../WAVE-B-TECHNICAL-REVIEW-04.md). Exhaustive source verification, independent expert review and final publication acceptance remain separate, uncompleted gates.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
