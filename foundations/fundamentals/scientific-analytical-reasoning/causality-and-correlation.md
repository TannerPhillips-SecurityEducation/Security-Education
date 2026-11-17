# Causality and Correlation

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Causality and correlation  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical acceptance pending

## Association is not automatically a causal explanation

**Correlation** is a statistical form of association between variables. When values of one variable vary with values of another under a chosen statistical definition, an association can be described, measured or modeled. **Causality** concerns whether and how changes in one factor help bring about changes in another, under a specified causal model and context.

These ideas overlap, but they are not equivalent. A variable can be associated with an outcome without causing it; a causal influence can exist even when a simple correlation measure is small or zero in the observed sample; and two variables can share a common cause without directly causing one another.

The [Stanford Encyclopedia of Philosophy's Causal Models](https://plato.stanford.edu/entries/causal-models/) distinguishes observational probabilities from probabilities under hypothetical or actual interventions. Its [Probabilistic Causation](https://plato.stanford.edu/entries/causation-probabilistic/) entry demonstrates why regular association and simple probability raising can fail to isolate causal direction or distinguish a shared cause.

This reference introduces **domain-agnostic causal reasoning**. It does not imply that every observed association has a fully identifiable causal mechanism.

## What a correlation coefficient says

For paired quantitative variables, the **sample Pearson correlation coefficient** `r` is a normalized measure of *linear* association, defined when the relevant sample standard deviations are nonzero. The population analogue is usually denoted `ρ` and likewise requires finite, nonzero variances for the conventional definition. Values lie between `−1` and `+1`. A positive value indicates a tendency for larger values of one variable to appear with larger values of the other under the sample or population model; a negative value indicates the opposite linear direction.

**A zero Pearson correlation does not imply independence.** For example, if a nondegenerate random variable `X` is symmetrically distributed about zero, has a finite fourth moment, and `Y=X²` has positive variance, then their population correlation is zero even though `Y` is completely determined by `X`. The relationship is nonlinear and can be missed by a linear measure.

Likewise, a high magnitude correlation does not, on its own, identify which variable causes which, establish a physical mechanism, or justify extrapolation to another population.

Other statistics, such as rank correlations or conditional association measures, capture different aspects. Their mathematical definitions and estimators belong in [Probability and Statistics](../mathematics-logic/README.md), while this article addresses the **interpretation of association and causal claims**.

## Confounding and common causes

A **confounder** in a specified causal model is a variable whose relationships with the candidate cause and outcome can bias an attempted causal comparison if inadequately accounted for. It may create or obscure an association.

A simple model might be represented as:

```text
       Rain
       /  \
      v    v
Umbrella  Wet pavement
```

Rain can influence both umbrella use and wet pavement. Observing an association between open umbrellas and wet pavement does not mean opening an umbrella causes pavement to become wet. The graph is a **proposed causal model** containing arrows whose interpretation requires evidence and assumptions; it is not an observation proving its own edges.

A toy probabilistic demonstration makes the distinction more precise. Assume rain on half the days. Conditional on rain, umbrella use occurs with probability `0.9` and wet pavement with `0.8`. Without rain, the probabilities are `0.1` and `0.2`, respectively. Assume **conditional independence** of the two observations given rain status.

Then:

```text
P(Umbrella) = 0.5
P(Wet pavement) = 0.5
P(Umbrella and Wet) = 0.5×0.9×0.8 + 0.5×0.1×0.2 = 0.37

P(Wet | Umbrella) = 0.37/0.5 = 0.74
P(Wet | No umbrella) = (0.5−0.37)/0.5 = 0.26
```

There is a pronounced **observational association** under these hypothetical parameters: `P(Wet | Umbrella)=0.74` versus `P(Wet | No umbrella)=0.26`. The diagram has no causal arrow from umbrella use to wet pavement, and conditional independence within rain/no-rain strata was assumed. The example illustrates how a common cause can generate association without a direct causal effect. It does not constitute a real meteorological dataset or prove that no other causal interactions could exist.

## Observing versus intervening

**Observation** learns what happened under the system's ordinary process. **Intervention**, under a causal model, changes or sets a factor by a specified action, changing relevant parts of the causal process.

The distinction can be written schematically:

```text
P(Y | X = x)           Observed conditional probability
P(Y | do(X = x))       Intervention probability under a causal model
```

These expressions can differ. The first asks about observations in cases where `X` already had a value. The second asks about an idealized intervention that sets `X` while changing the causal structure as specified by the model.

The [SEP Causal Models entry](https://plato.stanford.edu/entries/causal-models/) describes this intervention interpretation and why it is not equivalent to ordinary probability conditioning. The `do` notation is **one formal modeling language**, not a universal definition of every physical intervention.

A randomized experiment may support causal inference by altering the distribution of treatment assignments, but randomization does not automatically eliminate all measurement error, noncompliance, interference, selection or implementation problems. The canonical general treatment of designs and experimental units belongs in [Hypotheses and Experiments](hypotheses-and-experiments.md).

## Confounders, mediators, and colliders are not interchangeable

A causal diagram can contain structurally different types of third variables:

| Structure | Example diagram | Distinction |
| --- | --- | --- |
| Common cause | `Z → X` and `Z → Y` | Z can create confounding in an observational comparison |
| Mediator | `X → M → Y` | M is on a hypothesized causal path from X to Y |
| Collider | `X → C ← Y` | Conditioning on C can create an association between X and Y, even if they were otherwise independent under assumptions |

This table describes **common causal-graph patterns**. The actual implications of adjustment depend on the complete model. Naively controlling for *every measured variable* can introduce bias, especially when conditioning on a collider or certain post-treatment variables.

A **causal graph** uses arrows with assumed causal semantics. It differs from an undirected graph of statistical associations. Both use mathematical vertices and edges, but the meaning of the edges belongs to the causal model and must be made explicit. The formal combinatorial structure of graphs belongs in [Graph Theory](../mathematics-logic/graph-theory.md).

## Counterfactual questions

A **counterfactual** asks what would have happened under conditions that differ from those actually realized. For example, given an observed device failure, one might ask whether the device would still have failed **had the operating temperature been lower**.

That question cannot usually be answered merely by observing the actual failure record. Counterfactual inference depends on a causal model, assumptions about mechanisms, and potentially evidence from comparable cases or interventions.

An interventional probability and an individual counterfactual claim are also different. The former can describe distributions under a specified policy or intervention; the latter may concern what would have happened to a particular subject under an unrealized condition. Their distinction is discussed by [Causal Models](https://plato.stanford.edu/entries/causal-models/).

## Causal diagrams encode assumptions, not guaranteed truths

Causal graphs are useful because they make hypothesized dependencies explicit. They do **not** infer all arrows merely by drawing a diagram. Their interpretation depends on assumptions about missing causes, causal ordering, intervention effects, and the observed variables.

Temporal precedence may be relevant to causal claims, but being earlier does not alone establish causation. This article does not resolve the broader general-temporality coverage decision [G-04](../COVERAGE-GAP-DECISIONS.md).

**Correlation**, **causal hypothesis**, **experimentally estimated effect**, and **demonstrated mechanism** should be separately named in a technical explanation. A reliable correlation can be an important observation even when its causes remain unknown.

## Connecting evidence and analysis

A useful analytical pattern is:

```text
Observed association
       ↓
Candidate causal structures
       ↓
Check assumptions, confounding and alternatives
       ↓
Acquire discriminating evidence or intervene when feasible
       ↓
Estimate or qualify the effect within a model
       ↓
Report what is supported and what remains uncertain
```

This is a **descriptive reasoning pattern**, not a universal scientific protocol. When interventions are impractical or unethical, observational approaches may still be informative under carefully justified assumptions.

The [Evidence](evidence.md) article owns claim-relative support; [Deduction, Induction, and Abduction](deduction-induction-abduction.md) owns inference modes; [Measurement](measurement.md) owns quantitative acquisition; [Relationships](../models-abstraction/relationships.md) owns interpreted associations.

## References and editorial scope

- [Stanford Encyclopedia of Philosophy: Causal Models](https://plato.stanford.edu/entries/causal-models/), graphical causal models, intervention and counterfactual semantics.
- [Stanford Encyclopedia of Philosophy: Probabilistic Causation](https://plato.stanford.edu/entries/causation-probabilistic/), probability raising, asymmetry, common causes and confounding.
- [Stanford Encyclopedia of Philosophy: Abduction](https://plato.stanford.edu/entries/abduction/), explanatory inference and its limits.
- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), the mathematical graph and probability foundations distinct from causal semantics.

**Editorial review note:** Recomputed the four probabilities in the toy weather model, checked the intervention/conditioning distinction against the SEP causal-model reference, and qualified the zero-correlation counterexample with finite-moment assumptions. This remains an illustration, not an empirical study or an identified real-world causal effect. See the Batch 05 source-review ledger for model-assisted acceptance.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
