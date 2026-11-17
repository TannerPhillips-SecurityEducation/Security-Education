# State and Behavior

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** State and behavior  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## A system's condition and its evolution are distinct

A **system state** is a selected description of the system's condition at a specified point or stage under a chosen model. **Behavior** describes how that system responds to inputs, interacts with its environment, and changes or maintains state under the model's assumptions. Neither can be inferred completely from a component inventory alone.

[State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) owns the general concepts of state, event and transition. This article develops how those concepts describe **whole-system behavior**, coupling, operating modes, externally observable outputs, and verification-relevant properties.

A physical system has many possible properties. An engineering model selects only the state variables necessary for its intended explanation or prediction. **Omitted properties do not cease to exist**, and a model may need revision when its selected variables fail to distinguish different future behaviors.

## State variables, inputs and outputs

A state-based engineering model can distinguish:

- **State:** retained condition used to explain the system's modeled evolution.
- **Input:** a value or influence received from outside the modeled state update.
- **Output:** a reported or produced value through which behavior is observed or acted upon.
- **Transition rule:** the stated relationship between current state, inputs, and next state.
- **Environment and assumptions:** conditions under which the model is intended to apply.

For a discrete-step example, a possible notation is:

```text
s[k+1] = F(s[k], u[k])
y[k]   = G(s[k], u[k])
```

Here `k` indexes modeled steps, `s` denotes modeled state, `u` an input, and `y` an output. The functions need not be linear. **As written, these functions specify deterministic next-state and output values for each admitted state/input pair**. Probabilistic models instead require probabilities or transition kernels, while nondeterministic models can use relations or sets of possible successors. This illustrative notation does **not** assert that every real system is discrete, deterministic or fully observable.

The general mathematical use of functions belongs in [Algebra and Functions](../mathematics-logic/algebra-and-functions.md), and models and their interpretation in [Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md).

## Behavior includes permitted and actual traces

A **trace** is an ordered description of observations or transitions according to a model. A model can describe several possible traces, while an actual test yields a limited observed record. **One observed trace does not demonstrate that every modeled behavior occurs**, and one successful test trace does not exclude unobserved failures.

A state-machine model may show which transitions are permitted under specified inputs. A system can also exhibit behavior not represented by the model because of unmodeled resources, faults, concurrent interactions, or environment changes.

Different views expose different information:

| View | Hypothetical heating controller |
| --- | --- |
| Structural | Sensor, controller, switch, heater |
| State | Controller mode `OFF` or `ON` |
| Input | Reported temperature |
| Output | Heater command |
| Behavior | State changes when selected thresholds are crossed |

The structural view does not independently determine transition thresholds. The behavioral view does not necessarily specify physical wiring, calibration, or heat-transfer dynamics.

## Worked example: a hysteresis controller

Consider a stipulated controller with state `OFF` or `ON`, receiving one temperature input in degrees Celsius at each step. Its rules are:

```text
if state = OFF and input_temperature <= 18 °C:
    next_state = ON
else if state = ON and input_temperature >= 22 °C:
    next_state = OFF
else:
    next_state = state
```

Starting in `OFF`:

| Step | Input °C | State before | State after |
| ---: | ---: | --- | --- |
| 1 | 17 | OFF | ON |
| 2 | 20 | ON | ON |
| 3 | 23 | ON | OFF |
| 4 | 20 | OFF | OFF |

The two different outcomes at input `20 °C` show **state dependence**: the controller retains the previous mode within the band between its switching thresholds. This illustrates a simplified form of **hysteresis**, not a physical claim that a real room instantly changes temperature when a heater is switched.

The example assumes valid sensor inputs, atomic steps and no faults. Changing those conditions may require additional state variables and rules. In particular, output command and real heater behavior can differ.

## State, status, modes, and observability

A reported **status** is a representation or claim about the underlying system, not automatically a complete state. An observer may see `heater_command=ON` while the heater is physically disconnected, or may see only one sensor value while several internal states could explain it.

**Observability**, in a general sense, concerns whether internal conditions can be distinguished from available outputs under the chosen model and observation mechanism. Specialized control-theoretic definitions require additional assumptions and are developed under [Feedback and Control](README.md).

An **operating mode** can constrain which functions and transitions are permitted, such as normal operation, maintenance, or degraded operation. Mode and state may overlap in some models but need not be synonyms. A mode can itself be represented as a state variable when that serves the purpose.

## Invariants, safety and liveness

An **invariant** is a property specified to hold in every state reachable within a model under its initial conditions and transition rules. For the toy controller, `state ∈ {OFF,ON}` is an invariant by construction. That does not prove that a physical implementation cannot fail or enter an unmodeled condition.

A **safety property** can forbid certain modeled outcomes. A **liveness property** may require eventual progress, often under fairness or environmental conditions. A system satisfying one is not necessarily guaranteed to satisfy the other, and both depend on model correspondence.

[Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns the abstract property and proof concepts. [Verification and Validation](README.md) is a separate approved engineering heading that evaluates specified product requirements and intended use.

## Time, concurrency, and hidden dependencies

Step ordering does not automatically supply real elapsed durations. A timeout, sensor delay, queue, scheduler or concurrent activity may change behavior even if the component list is unchanged. Interleavings and race conditions can introduce multiple possible outcomes from the same partial observation.

**G-04 general temporality remains an open architectural decision.** This article uses time-indexed behavior only in its established systems-engineering scope and does not claim canonical ownership of all time, ordering or simultaneity concepts.

## Boundaries and references

[Dependencies](dependencies.md) covers required resources and conditional propagation. [Architecture and Composition](architecture-and-composition.md) covers system organization and design views. [Feedback and Control](README.md) will own regulation and feedback theory within its separate approved heading.

This article adopts no required state-machine language, real-time scheduling regime, formal logic, or assessment system.

### Sources

- [NASA: Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/).
- [NASA: System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/).
- [SEBoK: Logical Architecture](https://sebokwiki.org/wiki/Logical_Architecture).
- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).

**Editorial status:** Substantive draft. The hysteresis trace, invariant and behavioral claims require a separately documented model-assisted technical review before acceptance.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
