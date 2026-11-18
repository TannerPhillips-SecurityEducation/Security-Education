# Feedback and Control

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Feedback and control  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 04 audit](../WAVE-B-TECHNICAL-REVIEW-04.md); no independent human peer review

## Regulation connects observation to action

**Control** concerns influencing a system's behavior to pursue a specified objective under stated conditions. **Feedback** supplies information about an observed output or state that can influence subsequent actions. In a *closed-loop* control arrangement, a controller uses feedback to adjust an input to a **plant**, the process being influenced. An *open-loop* arrangement issues actions without using the relevant measured outcome to correct them. A system may combine feedback, feedforward prediction, supervision and manual operation.

These concepts are domain-independent: they apply to temperature regulation, motion, economic resource allocation, computing workloads and organizational coordination. Their physical implementations belong in their specialized domains. [MIT OpenCourseWare: Analysis and Design of Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/) provides mathematical treatments of feedback, stability, time response and system models.

## Parts of a control arrangement

A useful conceptual account distinguishes:

- **Reference or objective:** a desired condition, trajectory or performance criterion.
- **Plant or process:** the system whose behavior is being influenced.
- **Measurement:** an observation used to estimate the relevant condition.
- **Controller:** the decision rule producing a control action.
- **Actuator or influence channel:** how the action reaches the process.
- **Disturbance:** an influence not chosen as a control command.
- **Feedback path:** the information that connects observed behavior to subsequent adjustment.

These are roles within a model, not a rule that every engineered system contains seven separate physical devices. One device may perform several roles; the same process may participate in several overlapping loops.

A simplified loop is:

```text
Reference → [Compare] → Error → [Controller] → Action → [Plant] → Output
                ↑                                          |
                └──────── [Measurement / feedback] ────────┘
```

An output observation is not necessarily a perfect measurement of true internal state. Sensor errors, delays, model assumptions and transmission loss affect the controller's information. [Measurement](../scientific-analytical-reasoning/measurement.md) owns metrology; [Components and Interfaces](components-and-interfaces.md) owns interaction contracts.

## Negative feedback is not a guarantee of stability

A controller may apply an action that **reduces a measured error** in some operating conditions. This is commonly described as negative feedback. Positive feedback can amplify a deviation or reinforce a process. These descriptions refer to the sign of influence within a defined loop, not to whether the overall design is morally good or operationally safe.

Negative feedback does **not** automatically ensure convergence. Delay, excessive gain, saturation, changing process dynamics, noisy measurements and interacting loops can cause oscillations or instability. Stability must be assessed for the actual closed-loop model and relevant operating range.

A controller's intended output may differ from the actuator's realized action. A commanded heater setting does not prove heat was delivered. [State and Behavior](state-and-behavior.md) develops state evolution and the distinction between observed status and system reality.

## Worked example: an idealized discrete controller

Suppose a dimensionless, idealized process obeys the rule:

```text
y[k+1] = y[k] + K (r - y[k])
```

where `r` is a constant target, `y[k]` is the observed/model output at step `k`, and `K` is a fixed feedback gain. Assume immediate, exact measurements, no disturbances, no saturation, and that this rule correctly represents the process.

Let `r=20`, `y[0]=16`, `K=0.5`. Then:

| Step | Output before | Error `r-y` | Output after |
| ---: | ---: | ---: | ---: |
| 0 | 16 | 4 | 18 |
| 1 | 18 | 2 | 19 |
| 2 | 19 | 1 | 19.5 |

The error evolves according to `e[k+1]=(1-K)e[k]`. It halves each step for `K=0.5`. For this **specific scalar linear discrete model**, the error converges toward zero if `|1-K|<1`, equivalently `0<K<2`. For `0<K≤1`, a nonzero error in this idealized model approaches zero without changing sign; for `1<K<2`, it converges while alternating sign. At `K=2`, a nonzero error alternates sign with unchanged magnitude, so it does not converge. These statements concern only this scalar model and do not generalize to arbitrary plants, delays, nonlinear dynamics or noisy sensors.

The worked example is a mathematical illustration, not tested equipment performance or an approved controller design.

## Open-loop, feedback, and feedforward

An **open-loop** command can be suitable when the process and environment are sufficiently predictable or when feedback is unavailable or unnecessary. A **feedforward** controller anticipates a known or estimated disturbance before observing the resulting output error. Feedback can compensate for some modeling errors, but it is constrained by sensing quality and available actuation.

A combined controller may rely on a predicted heat demand plus measured temperature error. That combination can improve response under suitable models, but may also worsen behavior if prediction or measurements are wrong. Comparing alternatives therefore requires performance criteria and evidence.

## PID as one controller family, not a universal feedback architecture

A **proportional–integral–derivative (PID)** controller combines current error, accumulated error and error-change rate under a defined time and sign convention. A commonly idealized continuous-time controller is

u(t) = Kp·e(t) + Ki·∫ e(τ)dτ + Kd·de(t)/dt.

The proportional term responds to current error, the integral term accumulates persistent error, and the derivative term responds to its rate of change. Practical implementations may filter derivatives, sample inputs at discrete times, clamp outputs and reset integral state. The sign and interpretation of e(t) must be consistent with the feedback configuration.

**Worked illustration:** With only proportional control Kp=2, a constant error e=3 yields u=6 in the chosen model's command units. If the physical actuator saturates at u=5, the plant receives at most that limited influence. The commanded value 6 is not evidence of a physical effect of size 6, and adding integral control would not automatically remove the saturation constraint.

An integral term can suffer **windup** when commands remain saturated while error accumulates; a derivative term can amplify measurement noise. Stability, overshoot and steady-state behavior depend on controller gains **and** plant dynamics, sampling, delays and disturbances. Neither adding a PID controller nor drawing a negative-feedback loop proves stability.

[MIT feedback-control teaching materials](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/) and [MathWorks PID controller documentation](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html) discuss PID representations and constraints. This subject owns the **abstract controller and loop structure**; [Physical Control Mechanisms](../physical-electrical-principles/physical-control-mechanisms.md) owns actual plant, actuator and energy constraints.

## Control objectives and limits

Control goals can include tracking a target, rejecting disturbances, remaining within safe bounds, minimizing resource use, or balancing competing demands. These are not all equivalent: a faster response may increase overshoot, energy consumption or actuator wear.

**Stability** concerns how the modeled system responds to perturbations. **Robustness** concerns persistence of desired behavior across a defined set of uncertainties. **Observability** concerns whether internal conditions can be distinguished from outputs under a model; **controllability** concerns the ability of admissible inputs to affect reachable states. Formal definitions depend on the class of system and should not be claimed without its assumptions.

[Dependencies](dependencies.md) owns necessary resource relations; [Architecture and Composition](architecture-and-composition.md) owns allocation and interaction views. The separate [Physical Control Mechanisms](../physical-electrical-principles/README.md) heading owns physical implementation context. General temporal concepts remain open under [G-04](../COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks).

## Sources and acceptance boundary

- [MIT OpenCourseWare: Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/).
- [MathWorks: Proportional–Integral–Derivative Controller Representations](https://www.mathworks.com/help/control/ug/proportional-integral-derivative-pid-controllers.html).


- [MIT OpenCourseWare: Analysis and Design of Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/).
- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- [NASA: Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/).

**Editorial status:** Reviewed (model-assisted) under the scoped [Wave B Batch 04 technical review](../WAVE-B-TECHNICAL-REVIEW-04.md). Exhaustive source verification, independent expert review and final publication acceptance remain separate, uncompleted gates.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
