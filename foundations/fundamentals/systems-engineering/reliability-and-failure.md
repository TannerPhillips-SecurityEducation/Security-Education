# Reliability and Failure

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Reliability and failure  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 04 audit](../WAVE-B-TECHNICAL-REVIEW-04.md); no independent human peer review

## Dependability depends on conditions and defined success

**Reliability** describes the probability that an item performs its required function without failure for a specified interval under stated operating conditions and a chosen model. A **failure** occurs when an item cannot perform a required function under the relevant conditions. An **error**, **fault**, **defect**, **failure mode**, and **hazard** describe related but not interchangeable concerns.

For example, a latent design defect may exist without producing an observed failure. An internal error may be detected and corrected before an external service fails. A failure mode describes *how* an item fails to meet a requirement; its *effect* describes downstream consequences.

[SEBoK System Reliability, Availability, and Maintainability](https://sebokwiki.org/wiki/System_Reliability%2C_Availability%2C_and_Maintainability) distinguishes reliability, availability, maintainability, and failure. [NASA Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/) addresses adverse scenarios, likelihood, consequences and uncertainty.

## Reliability, availability and maintainability are distinct

**Reliability** concerns failure-free operation over an interval. **Availability** concerns being able to provide the required function at a point in time or over a specified period, under an explicit operational definition. **Maintainability** concerns how readily a failed or degraded item can be restored or serviced under stated resources and procedures.

| Measure | Core question | Necessary context |
| --- | --- | --- |
| Reliability | Will the required function persist without failure over an interval? | Time horizon, environment, failure criterion |
| Availability | Is the required function available when needed? | Downtime definition, repair/operation assumptions |
| Maintainability | How effectively can service be restored or maintained? | Procedures, resources, access and repair conditions |

A repairable system may have frequent failures yet high availability if restoration is rapid. A system may be highly reliable over a short interval yet difficult to repair after its eventual failure. Neither relationship is contradictory.

For a nonrepairable item with time to failure `T`, a conventional reliability function is `R(t)=P(T>t)`, for `t≥0` under the stipulated model. A valid numeric probability requires defensible data or explicit scenario assumptions; an observed failure count alone is not the same as a reliability estimate.

## System composition changes reliability

Consider two hypothetical components, A and B, each with probability 0.9 of working throughout a defined interval, with **independent successes/failures**. Suppose the whole system requires **both** to operate. Its modeled reliability is

```text
P(A works AND B works) = 0.9 × 0.9 = 0.81
```

Now suppose the same idealized components are arranged so that **either one** can provide the required function, with perfect detection/switchover and no additional components or common-cause failures. The modeled reliability is

```text
P(A works OR B works) = 1 - (0.1 × 0.1) = 0.99
```

These are hypothetical **series** and **parallel** reliability structures. The independence assumption matters: common power, shared environmental stress, software defects, operator actions or failed switchover can invalidate the 0.99 result. Merely drawing two boxes does not prove the assumptions.

[Dependencies](dependencies.md) owns the modeled reliance relations; [Architecture and Composition](architecture-and-composition.md) owns alternate system structures; this article owns reliability consequences under their defined failure criteria.

## Failure mechanisms, effects and risk

A **failure mechanism** is a physical, logical or procedural process by which a failure develops. A **failure mode** identifies a way the function can be lost or degraded. A **failure effect** concerns consequences for local elements and the whole system. The same mode can produce different consequences depending on context, safeguards and operational phase.

**Risk** is not synonymous with probability of failure. Engineering risk evaluation may consider adverse scenarios, their likelihoods, consequences, uncertainties, and goals. A rare failure with severe consequences may warrant attention; a frequent minor deviation may warrant a different response.

Some failures are **independent** within a particular statistical model; others share causes or propagate through dependencies. A fault tree, reliability block diagram or simulation formalizes selected relationships, but those diagrams are not observations of reality.

## Restoration and operational availability

For a repairable item alternating between up and down periods in a model with well-defined long-run mean up time `U` and mean down time `D`, with applicable steady-state or renewal assumptions, the long-run availability can be expressed as

```text
A = U / (U + D)
```

Suppose the toy model has mean operational periods of 90 time units and mean downtime of 10 units, with the stated long-run assumptions. The modeled availability is `90/(90+10)=0.90`. This fraction is **not** automatically the probability of surviving 100 units without failure. Whether scheduled maintenance, logistical delay or other sources of downtime count depends on the chosen availability metric.

Do not apply this ratio indiscriminately to nonstationary, censored or correlated data without checking the estimator and model assumptions. [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns inference and distributions.

## Why reliability and availability can have very different percentages

Consider a **hypothetical repairable service** in which each operational period has an exponential time-to-failure distribution with **mean up time 90 hours**. The subsequent restoration periods have mean duration **10 hours**. Assume the operating conditions are stationary, the up/down cycles satisfy the relevant renewal assumptions, restoration returns the service to its modeled operating state, and there is no hidden degraded service condition.

First, *reliability* concerns staying up **without any failure** over a selected interval. The exponential model has constant failure hazard \(\lambda=1/90\) failures per hour, so

\[
R(t)=P(T>t)=e^{-\lambda t}.
\]

For a newly operating item over the next **90 hours**:

\[
R(90)=e^{-(1/90)\cdot 90}=e^{-1}\approx0.3679.
\]

Thus the probability of **no failure at all for 90 hours** is about **36.8%** under this deliberately chosen constant-hazard model. It is not a measurement of any real service, and exponential failure times are not universally appropriate.

Next, *long-run availability* allows failures **followed by restoration**. With mean up time \(U=90\) hours and mean downtime \(D=10\) hours:

\[
A=\frac{U}{U+D}=\frac{90}{90+10}=0.90.
\]

This same model therefore has **90% long-run availability** while offering only **36.8% reliability for a continuous failure-free 90-hour interval**. There is no contradiction: one metric permits restoration between observations and the other asks for an uninterrupted period of correct operation.

| Claim | Quantified result | What counts as success |
| --- | ---: | --- |
| Reliability over 90 h | ~36.8% | No failure during the entire 90-hour window |
| Long-run availability | 90.0% | Service is operational for the modeled fraction of time, allowing repairs |
| Mean up time | 90 h | Modeled duration of an up period |
| Mean downtime | 10 h | Modeled duration of restoration under the specified definition |

**Counterexample to an unsafe inference:** Observing 90% availability does **not** entitle us to claim a 90% chance of surviving 90 consecutive hours without failure. Nor does restoring function necessarily restore **security assurance**, information correctness, or the customer's intended experience. Repair-time distributions, common faults, workloads, censored observations and changing operating modes may invalidate this toy model.

The [NIST Engineering Statistics Handbook: Exponential Reliability Model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm) defines constant-hazard survival \(R(t)=e^{-\lambda t}\) and \(MTTF=1/\lambda\). [SEBoK: System Reliability, Availability, and Maintainability](https://sebokwiki.org/wiki/System_Reliability%2C_Availability%2C_and_Maintainability) distinguishes lifetime survival, repairability and operational availability, including the role of downtime definitions.

## Redundancy, monitoring and restoration are conditional safeguards

Redundancy can provide alternative paths; diagnostics can expose degradation; maintenance can restore a function. However, these mechanisms add interfaces, controls and dependencies that can fail themselves. Effective redundancy requires specifying detection coverage, changeover behavior, capacity and shared dependencies.

Reliability engineering therefore combines design analysis, evidence collection, test planning, operating assumptions and revision. A model-based reliability value is conditional on its parameters. It is not a certification of safety, security or service continuity.

## Boundaries and references

[Verification and Validation](verification-and-validation.md) owns engineering evidence against requirements and intended use. [Requirements](requirements.md) defines specified success conditions. [System Lifecycle](system-lifecycle.md) owns evolution, maintainability planning and retirement context. The general theory of faults in specific software, electrical, industrial or distributed systems belongs to the specialized domain, not to an assumed universal failure implementation.

### Sources

- [SEBoK: System Reliability, Availability, and Maintainability](https://sebokwiki.org/wiki/System_Reliability%2C_Availability%2C_and_Maintainability).
- [NIST Engineering Statistics Handbook: Exponential Lifetime Model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm), constant-hazard survival and mean time-to-failure formulas; used only for the explicitly hypothetical constant-rate example.
- [NASA: Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/).
- [NASA: Design Solution Definition](https://www.nasa.gov/reference/4-4-design-solution-definition/).

**Editorial status:** Reviewed (model-assisted) under the scoped [Wave B Batch 04 technical review](../WAVE-B-TECHNICAL-REVIEW-04.md). Exhaustive source verification, independent expert review and final publication acceptance remain separate, uncompleted gates.

**Administrative depth pass (November 19, 2026):** The added reliability-versus-availability derivation was independently recalculated and checked against NIST and SEBoK under [Fundamentals Administrative Editorial Pass 01](../ADMINISTRATIVE-EDITORIAL-PASS-01.md). The historical Wave B review retains its original scope; this clarification does not establish complete source verification, independent expert acceptance or publication.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
