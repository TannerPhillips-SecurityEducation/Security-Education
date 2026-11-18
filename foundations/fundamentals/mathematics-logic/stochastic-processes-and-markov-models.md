# Stochastic Processes and Markov Models

**Knowledge area:** [Mathematics & Logic](README.md)  
**Subject ID:** F-01-13  
**Development status:** Draft; newly authored foundational reference  
**Source review:** References listed; scoped technical review pending  
**Inventory authority:** [Coverage & Source Triage 02](../COVERAGE-AND-SOURCE-TRIAGE-02.md)

## Stochastic processes describe uncertain change

A **stochastic process** is a family of random variables indexed by a set, often time. It describes a model in which states, event counts or values can vary according to probabilistic relationships. A stochastic process is more than a single random variable: it includes a dependence structure across multiple indexes.

Write a stochastic process as `{X(t): t∈T}`. The index set T may be discrete, such as nonnegative integers, or continuous, such as nonnegative real time. The **state space** of X may also be discrete or continuous. "Discrete-time" and "discrete-state" are separate classification dimensions.

A **sample path** is one realized sequence or trajectory in the model. A statistical distribution describes possibilities across a model or collection, not certainty about the path that will occur.

[Probability and Statistics](probability-and-statistics.md) owns random-variable definitions, conditional probability, expectation and inference. [Temporal Concepts and Models](../models-abstraction/temporal-concepts-and-models.md) owns the general meaning of time and ordering. This subject owns **stochastic dependence, transitions and process families**.

## Joint distributions and dependence

The probability of X(t₁) alone does not determine how X(t₂) depends on it. Two processes may have identical one-time marginal distributions yet very different persistence, correlation, transition probabilities or path behavior. A complete stochastic model may require finite-dimensional joint distributions, transition kernels, independence assumptions or explicit mechanisms.

**Stationarity** concerns invariance of chosen statistical properties under index shifts. A strictly stationary process has joint distributions invariant under shifts that stay within its index domain. **Weak stationarity** commonly concerns a constant mean and autocovariance depending only on the lag, when suitable moments exist. A stationary process need not consist of independent observations.

A process can be correlated, autocorrelated, periodic, transient or nonstationary. None of those labels by itself establishes why the variation occurs or whether the model adequately represents a physical process.

## The Markov property

A process has the **Markov property** if its modeled future, conditional on its present state, does not depend on the entire earlier state history under the specified formalization. In discrete time:

```text
P(X[n+1]=j | X[n]=i, X[n−1], …, X[0])
  = P(X[n+1]=j | X[n]=i)
```

for histories and conditional probabilities where the expressions are defined.

This property depends on the choice of state representation. If the state omits a relevant hidden condition, the observed sequence may not be Markov even when an enlarged state representation would satisfy that assumption.

A **time-homogeneous Markov chain** has a fixed transition probability matrix P with entries Pᵢⱼ≥0 and each row summing to 1. Time homogeneity is an additional assumption, not the definition of every Markov process.

A Markov model is not the assertion that an actual system has no history. It asserts that the *chosen current state* supplies the relevant conditional information about future transitions in the model.

## Discrete-state transition matrices

Consider two states, A and B, with the transition matrix

```text
             Next A   Next B
Current A      0.8      0.2
Current B      0.4      0.6
```

Each row sums to one. Let the initial distribution be p₀=(1,0), meaning the system begins in A with probability one.

After one modeled step, p₁=p₀P=(0.8,0.2). After a second step:

```text
P(X[2]=B) = 0.8×0.2 + 0.2×0.6
           = 0.16 + 0.12
           = 0.28.
```

Thus p₂=(0.72,0.28). The result is a probability distribution across possible states after two steps, **not** a prediction that 28% of a single observed event occurred.

A **stationary distribution** π satisfies πP=π. For this particular matrix, π=(2/3,1/3) satisfies the equation: (2/3)×0.2=(1/3)×0.4, balancing the two modeled flows. Stationarity of a distribution must not be confused with a guarantee that a finite observed trajectory has converged, or that a real system will always settle into the assumed regime.

## Poisson counting processes

A **homogeneous Poisson process** of rate λ>0 models event counts N(t) with particular properties: N(0)=0, independent increments, stationary increments and Poisson-distributed counts over an interval of length t. Under these assumptions,

```text
P(N(t)=k) = exp(−λt) × (λt)^k / k!,   k=0,1,2,...
```

The expected count in a duration t is λt. For λ=2 events per minute and t=1 minute, the probability of no modeled arrivals is exp(−2)≈0.1353.

The fact that some recorded event count has a mean of two events per minute does **not** prove that arrivals form a Poisson process. Bursts, dependence, changing intensity, observation loss and environmental constraints can violate its assumptions.

## Queueing, reliability and applications

A stochastic-process model can represent arrivals to a service system, component transitions between functioning and failed states, randomized scheduling, environmental noise or changing demand. But the **queue's discipline, capacity, service mechanism and losses** require additional modeling, developed in [Queueing and Service-System Models](../systems-engineering/queueing-and-service-system-models.md).

A Markov decision process adds choices and an objective to a transition model; those decision and planning concerns belong to [Artificial Intelligence Foundations](../computation-algorithms/artificial-intelligence-foundations.md). A Markov chain itself need not represent an agent making decisions.

**Correlation** in a stochastic model is not evidence of causal control. A fitted transition matrix estimated from observations may change under intervention, regime shifts or hidden state, and its uncertainty must be assessed from the evidence.

## Worked distinction: averages are not models of dependence

Consider two sequences whose entries are each zero or one. Both may contain five zeros and five ones, yielding the same empirical mean 0.5. One sequence could alternate 0,1,0,1, while another could contain five consecutive zeros followed by five ones. Their **sample counts and means match**, but their observed temporal patterns differ.

A model that treats each observation as an independent Bernoulli draw cannot automatically describe both dependence structures. The finite sequences do not by themselves establish one correct underlying probabilistic process, either.

## Primary source starting points

- [MIT OpenCourseWare 6.041SC Probabilistic Systems Analysis and Applied Probability](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/resource-index/), especially the Markov-chain and Poisson-process units.
- [MIT 6.041SC resource materials](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), discrete and continuous random variables, stochastic processes and probabilistic systems.
- [MIT 6.041SC Markov Chains, Lecture 17](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/0c7babf5725ef87aa95cf623253a68e4_MIT6_041SCF13_lec17_300k.pdf), an introductory time-homogeneous, finite-state treatment.

**Editorial state:** Draft. The equations and numbers are model illustrations; passage-level source verification, empirical validation, and independent human review remain open. No Knowledge Checks or Practical Assessments.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
