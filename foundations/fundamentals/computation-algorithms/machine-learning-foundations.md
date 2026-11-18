# Machine Learning Foundations

**Knowledge area:** [Computation & Algorithms](README.md)  
**Subject ID:** F-07-11  
**Development status:** Draft; substantive article newly authored  
**Source review:** References listed; scoped technical review pending  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Machine learning fits models to data or experience

**Machine learning (ML)** studies computational methods that use data or interaction experience to select or adapt model parameters, representations, decision rules or policies according to an objective. A fitted model may perform prediction, classification, ranking, clustering, generation or action selection. ML is a substantial part of [Artificial Intelligence Foundations](artificial-intelligence-foundations.md), but **AI does not require learning** and learning is not restricted to current neural-network architectures.

A common training problem has observations `(xᵢ,yᵢ)` and a parameterized predictor `fθ(x)`. A learning procedure chooses model parameters `θ` using a loss or objective computed from the available data. The learned relationship is a feature of the **chosen hypothesis class, training data, procedure and assumptions**, not a verified law governing all future observations.

[Algorithms](algorithms.md) owns general computational procedures; [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns probability and inference mathematics; this article owns the **learning problem, fitting process, generalization, and evaluation boundary**.

## Learning paradigms

**Supervised learning** uses examples with targets or labels. Common tasks include regression, classification and ranking. **Unsupervised learning** seeks structure or representations from data without the same target-label supervision, such as grouping similar instances or learning lower-dimensional representations. **Self-supervised learning** derives predictive targets from the available data itself; it is often used for representation learning.

**Reinforcement learning (RL)** uses feedback from interaction with an environment, often expressed as rewards or returns, to learn values or policies for sequential decisions. It should not be confused with supervised prediction on independent labeled rows: actions can affect future observations and available rewards.

These are useful families, not mutually exclusive categories for every algorithm. A system may use a pretrained representation, supervised fine-tuning and later reinforcement-learning adaptation. Deep learning describes models with multiple learned representational layers; it is not a fourth mutually exclusive supervision regime.

## Model, features, parameters and objectives

A **feature** is an input representation; a **target** is the value the learning task aims to predict or otherwise explain. **Parameters** are learned values, while **hyperparameters** govern aspects of model construction or training, such as regularization strength or architecture settings.

A model family defines which functions can be represented. For linear regression, a basic predictor can be `fθ(x)=wx+b`; a nonlinear model may represent different relationships. A **loss function** quantifies a chosen mismatch between prediction and target. For a finite dataset, **empirical risk minimization** selects parameters minimizing an aggregate training loss, potentially with regularization or other constraints.

The expression `L(θ)=(1/n) Σᵢ ℓ(fθ(xᵢ),yᵢ)` is a general model of average training loss, not a mandate to use one optimizer, loss, dataset weighting or error distribution. Optimization method, model capacity, data quality and computational resources affect the result. A perfectly minimized training loss does not certify future performance.

## Training, validation, testing and inference

**Training** adapts a model from the chosen data and objective. **Validation** provides evidence for selecting model families, hyperparameters or stopping rules. A final **test** assesses performance on held-out data not used for fitting or selecting the model, under the declared evaluation protocol. After model selection, repeated use of the same test set to guide decisions compromises its independence.

**Inference** uses a fitted model to produce an output on new inputs, without necessarily changing its parameters. This differs from statistical *inference*, which more generally concerns drawing conclusions about distributions or parameters from data; context must clarify the intended meaning.

Random train/test splits can be misleading for temporally ordered or clustered data. A time-dependent prediction task may require an evaluation where training observations precede test observations. Duplicated records, shared entities, future-derived features or preprocessing performed across split boundaries can cause **data leakage** and optimistic performance estimates.

## Generalization, overfitting and data shift

**Generalization** is performance beyond the specific training examples under a defined target distribution or environment. **Overfitting** occurs when the learned model captures training-specific variation that does not transfer as intended, often showing low training error with worse independent evaluation performance.

Generalization depends on the sample, labeling process, hypothesis class, regularization, optimization, validation protocol, and stability of the data-generating conditions. Neither a large dataset nor a complex neural model guarantees sound generalization.

**Distribution shift** occurs when relevant data distributions differ between training and use. It can involve changes in inputs, the relationship between features and targets, task policy, instrumentation or feedback. **Concept drift** is often used for changes in the target relationship over time, but exact usage differs across fields. Drift is not directly proved merely because a score drops; measurement errors and changed evaluation samples can produce similar effects.

## Worked example: fitting an ideal linear relationship

Choose three invented training pairs: `(1,2), (2,4), (3,6)`. Consider the model `f(x)=wx` without an intercept, and mean squared error

`MSE(w) = [(w·1−2)² + (w·2−4)² + (w·3−6)²] / 3`.

For `w=2`, the predicted targets are 2, 4 and 6, so **training MSE is zero**. For `w=1`, the squared residuals are 1, 4 and 9, giving `MSE(1)=14/3≈4.6667`.

```text
w     Predicted y for x=[1,2,3]     Training MSE
1     [1,2,3]                       14/3
2     [2,4,6]                       0
```

The minimum of this sample objective is attained at `w=2`. Yet **a zero training error does not establish that every future observation obeys y=2x**. The relation might fail for other input ranges, measurement conditions or generating processes. A held-out representative evaluation would be needed to assess generalization.

If a deployed model reports a class label rather than a numeric target, metrics must match the task. **Precision** measures the fraction of predicted positives that are actual positives in the evaluation labels; **recall** measures the fraction of actual positives identified. Their denominators differ, and neither alone captures costs, calibration, fairness or downstream outcomes.

## Model evaluation and uncertainty

Evaluation should report data provenance, sampling design, target definition, label quality, missingness, uncertainty and potential feedback effects. Aggregate accuracy may hide poor performance on relevant subgroups, rare conditions, or shifted operating contexts. A confidence score output by a predictor is not automatically a calibrated probability of correctness.

**Causal inference** asks what changes under interventions; predictive association alone does not answer that question. **Explanation** of a model's computation is distinct from evidence that its output is factually correct, causally grounded, or safe to act upon.

A classifier's validation metrics cannot by themselves demonstrate that a security alert is malicious, that a medical conclusion is correct, or that an autonomous action is warranted. Such interpretations require external evidence, context and domain-specific acceptance criteria.

## Canonical relationships and sources

- [Artificial Intelligence Foundations](artificial-intelligence-foundations.md) owns AI agent/search/planning/knowledge-representation concepts shared with, but not limited to, ML.
- [Linear Algebra and Vector Spaces](../mathematics-logic/linear-algebra-and-vector-spaces.md) owns linear representations; [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns distributions, sampling and statistical inference.
- [Algorithms](algorithms.md), [Algorithm Design](algorithm-design.md) and [Computational Efficiency](computational-efficiency.md) own general procedure design and resource analysis.
- [Datasets, Records, Fields, and Values](../information-data/datasets-records-fields-and-values.md) owns data anatomy, [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns origin and changes, and [Measurement](../scientific-analytical-reasoning/measurement.md) owns calibrated physical measurement.
- [Causality and Correlation](../scientific-analytical-reasoning/causality-and-correlation.md) owns the distinction between association and intervention; [Human Cognition and Perception](../human-sociotechnical-systems/human-cognition-and-perception.md) owns human cognition, which must not be defined merely as an ML mechanism.

### Authoritative reference starting points

- [MIT OCW 6.036 Introduction to Machine Learning](https://ocw.mit.edu/courses/6-036-introduction-to-machine-learning-fall-2020/), representation, overfitting, generalization, supervised learning and reinforcement learning.
- [Stanford CS221 Artificial Intelligence: Principles and Techniques](https://bulletin-new.stanford.edu/courses/cs-221), machine learning in the broader AI decision context.
- [CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/), curricular placement of AI and mathematical/statistical foundations; not a machine-learning conformance standard.

The worked data are invented and evaluated under exact arithmetic. They are not measured evidence about a real population, deployed model, or a guarantee of performance. Sources are listed but not yet checked claim by claim.

**Editorial status:** Draft. No Knowledge Checks, Practical Assessments, or graded exercise content.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
