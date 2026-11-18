# Calculus and Differential Equations

**Knowledge area:** [Mathematics & Logic](README.md)  
**Subject ID:** F-01-12  
**Development status:** Reviewed (model-assisted; independent human approval not claimed)  
**Source review:** References listed; separate scoped technical review pending  
**Inventory authority:** [Coverage & Source Triage 02](../COVERAGE-AND-SOURCE-TRIAGE-02.md)

## Calculus describes change and accumulation

**Calculus** studies limits, differentiation and integration, providing a mathematical language for change and accumulation. A **differential equation** relates an unknown function to one or more of its derivatives, thus describing a constraint on the evolution or variation of a quantity under a chosen model. These concepts matter in physical processes, engineering feedback, computational optimization, resource growth and signals.

Calculus is not synonymous with a differential equation. A derivative can be computed for a known function without solving an evolution law; a differential equation asks which function or family of functions satisfies a specified derivative relationship. [Algebra and Functions](algebra-and-functions.md) owns general function notation and algebraic relationships. [Linear Algebra and Vector Spaces](linear-algebra-and-vector-spaces.md) owns linear maps. This subject owns calculus and differential-equation reasoning, while [Feedback and Control](../systems-engineering/feedback-and-control.md) owns controller mechanisms that may use differential models.

## Limits, derivatives and rates

A **limit** concerns the behavior of a function as its input approaches a chosen value, under a specified domain and topology. A function may approach a finite limit without being defined at that input. Continuity is one relevant limit property but does not automatically imply differentiability.

For a real function f, a derivative at t can be defined when the limit exists:

```text
f'(t) = lim[h→0] (f(t+h) − f(t))/h.
```

The derivative is a **local rate of change** in the chosen input and output quantities. If f is a position measured in meters and t is measured in seconds, the derivative has units of meters per second. A derivative may describe a negative rate, a zero local rate or a positive rate. It need not be an average over a finite time interval.

**Example:** If f(t)=t², then f'(t)=2t for real t. At t=3 the instantaneous rate is 6 units of output per unit of input, subject to whatever physical interpretation and units are assigned. The equation alone does not establish that a measured physical quantity actually follows t².

A function can be continuous but fail to be differentiable at a corner, such as f(t)=|t| at zero. Statements about derivatives therefore require differentiability assumptions.

## Integrals and accumulated change

A **definite integral** summarizes a quantity over an interval through a limiting accumulation. Under the usual Riemann-integrable setting, the integral of a rate over time gives a modeled total change. The fundamental theorem of calculus connects differentiation and integration under suitable continuity or integrability conditions.

For the rate r(t)=t from t=0 to t=2:

```text
∫₀² t dt = [t²/2]₀² = 2.
```

The result has **rate × input-unit** dimensions. It is not inherently a count of discrete events or a measurement from a real sensor.

Integration can also describe geometric area, expected quantities and other mathematical operations. A finite sum, numerical integration rule and exact definite integral are distinct: approximation requires error and convergence analysis.

## Differential equations and initial conditions

An **ordinary differential equation (ODE)** involves derivatives of an unknown function of one independent variable, often time. For a scalar state x(t), a first-order autonomous model may have the form

```text
dx/dt = F(x).
```

An **initial condition** x(0)=x₀ selects a candidate solution from a family when a suitable solution exists and is unique. Existence and uniqueness depend on assumptions about F and the problem domain; they are not automatic for every differential equation.

A simple idealized decay model is

```text
dx/dt = −k x,  k > 0,
x(0) = x₀.
```

Its solution is x(t)=x₀ exp(−kt), as can be checked by differentiating the proposed solution. If t is in seconds and x has some quantity unit, k has units of inverse seconds.

A **partial differential equation (PDE)** can involve derivatives with respect to multiple independent variables, for example space and time. PDEs have different mathematical conditions and are not simply ordinary differential equations with longer names.

## Dynamical systems and qualitative behavior

A **dynamical system** models how state develops over an index such as time. An equilibrium x* of dx/dt=F(x) satisfies F(x*)=0. In the simple decay model with k>0, x*=0 is an equilibrium, and trajectories with finite initial values move toward zero as t increases.

This behavior is a property of the **declared mathematical model**, not a guarantee about a physical system with disturbances, discontinuities, actuator limits or unmodeled feedback. Stability can mean several different things, including Lyapunov stability and asymptotic stability, which must be stated relative to a particular model and its assumptions.

Time representation is separately owned by [Temporal Concepts and Models](../models-abstraction/temporal-concepts-and-models.md). The equation's independent variable t need not be a synchronized wall-clock timestamp.

## Numerical approximation and error

Not every differential equation has a convenient closed-form solution. **Numerical methods** approximate solutions with finite steps, introducing discretization and often roundoff errors. Forward Euler for dx/dt=F(x) is

```text
x[n+1] = x[n] + h F(x[n]).
```

For the decay example with x₀=10, k=0.2 s⁻¹ and h=1 s, Euler predicts x₁=10+(1)(−0.2×10)=8. The exact solution at t=1 is 10 exp(−0.2)≈8.1873. The two values differ due to approximation, not necessarily because the differential equation itself is wrong.

Step size, smoothness, integration method, error tolerances and conditioning affect numerical behavior. A small step is not an unconditional guarantee of stability or accuracy.

## Worked illustration: a changing quantity

Assume a nonnegative modeled quantity x obeys dx/dt=−0.2x per second, with x(0)=10. The analytic solution gives x(5)=10 exp(−1)≈3.6788 after five seconds. The result is smaller than x₀ and remains positive, consistent with the sign of the derivative for positive x.

**Derived result:** 3.6788 is the output of the stipulated model under exact arithmetic. **Unknown:** Whether a real system has a constant k, whether the observed quantity obeys the ODE, or whether disturbances and measurement uncertainties alter the trajectory. Model identification and validation require separate evidence.

## Boundaries and related foundations

- [Algebra and Functions](algebra-and-functions.md): function composition, variables and algebraic equations, not evolution-law solution theory.
- [Linear Algebra and Vector Spaces](linear-algebra-and-vector-spaces.md): state vectors and linear operators, useful for systems of linear ODEs.
- [Probability and Statistics](probability-and-statistics.md) and [Stochastic Processes and Markov Models](stochastic-processes-and-markov-models.md): models with uncertainty, not automatic deterministic trajectories.
- [Feedback and Control](../systems-engineering/feedback-and-control.md): feedback, controller design and behavior; [Physical Control Mechanisms](../physical-electrical-principles/physical-control-mechanisms.md): physical plant constraints.
- [Scientific Measurement](../scientific-analytical-reasoning/measurement.md): actual quantity evidence, units, uncertainty and validation.

## Primary reference starting points

- [MIT OpenCourseWare 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/), first-order equations, analytical and numerical models, oscillation and linear systems.
- [MIT 18.03SC syllabus and course goals](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/), prerequisites, modeling, graphical and numerical solutions.
- [MIT Mathematics course catalog: Differential Equations](https://catalog.mit.edu/subjects/18/), scope and distinctions between ordinary, nonlinear and partial differential models.

**Editorial status:** Reviewed (model-assisted) under [Wave H Technical Review 01](../WAVE-H-TECHNICAL-REVIEW-01.md). Complete source-passage verification, independent qualified expert acceptance and Published status remain open.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
