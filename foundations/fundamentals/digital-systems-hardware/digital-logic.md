# Digital Logic

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Digital logic  
**Development status:** Reviewed (model-assisted; not an independently accepted final publication)  
**Source review:** Core claims checked in [50-claim-family audit](../PILOT-CLAIM-SOURCE-AUDIT.md); independent external expert review not performed

## From logical propositions to physical circuits

**Digital logic** concerns physical and abstract circuits that encode, combine, and retain discrete logical states. It is the bridge between a mathematical algebra of truth values and the electrical behavior of real computing hardware.

The formal expression `A AND B` denotes conjunction of logical inputs or propositions under the chosen Boolean interpretation. An electronic logic gate implements a corresponding operation using physical devices and voltage ranges. The mathematical rule does **not** itself specify the circuit's power, voltage thresholds, noise margin, propagation delay, or failure behavior.

That distinction determines canonical ownership: [Mathematics & Logic](../mathematics-logic/README.md) explains Boolean operations and proof rules, while this article explains how **hardware** represents and implements logic.

MIT's [Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/) develops digital systems from transistor circuits through combinational logic, sequential logic, finite-state machines, and processors.

## Binary abstraction and physical states

Digital circuits commonly represent information using two abstract states, often written `0` and `1`. In an electrical circuit those abstract states correspond to **ranges of physical signals**, not universally to an exact voltage of 0 V and 1 V.

Logic families specify how input voltages are recognized and how outputs are driven. A circuit designer must consider supply voltage, noise margins, loading, propagation times, and physical limits. The fact that Boolean algebra has exact truth values does not make every real voltage unambiguous.

A bit, a logical truth value, a wire voltage, and a character `"1"` are distinct representations and must not be confused.

## Combinational logic

A **combinational circuit** ideally computes output values from the **current** input values; the ideal logical function does not depend on past internal state. Examples include AND, OR, NOT, NAND, NOR, XOR, multiplexers, encoders, and adders.

Two-input examples:

| A | B | AND | OR | XOR | NAND |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

The truth table defines the output of an ideal Boolean function for each allowed input combination. Real circuits require time for signals to propagate and settle. Thus, at a transition boundary, a physical output may temporarily differ from the steady-state truth-table value.

NAND and NOR are **functionally complete** gate types: appropriate combinations of either can construct any Boolean function. For instance, `NOT(A) = NAND(A,A)`, and `A AND B` can be realized by inverting `NAND(A,B)`. This is a property of the Boolean implementation model, not a claim that all NAND circuits share identical electrical characteristics.

## Worked example: a half adder

A **half adder** combines two single-bit inputs and produces a one-bit sum and a carry-out:

```text
sum   = A XOR B
carry = A AND B
```

| A | B | Sum | Carry |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

For `A=1` and `B=1`, binary addition produces `10₂`: sum bit 0 and carry bit 1. The half adder demonstrates **combinational** logic: for stable inputs, its stable outputs are determined by those inputs. It does not on its own retain a prior sum.

A full adder adds a carry-in as a third bit; chaining adders makes wider arithmetic possible. The physical circuit introduces delay, so a multi-stage result is not instantaneously valid whenever an input changes.

## Sequential logic and state

**Sequential logic** represents circuits whose output or next behavior depends on stored state as well as current inputs. Storage elements such as latches and flip-flops enable registers, counters, finite-state machines, and many forms of digital control.

A simplified synchronous state-transition description is:

```text
next_state = F(current_state, inputs)
outputs    = G(current_state, inputs)
```

The actual state update is controlled by the circuit's timing rules. An edge-triggered D flip-flop, for instance, captures its input at a specified clock edge and makes the captured value available at its output after a clock-to-output delay. A level-sensitive latch has different enable behavior. The two components should not be treated as synonyms.

A **finite-state machine** can be described mathematically as states and transitions, then physically implemented using state storage plus combinational next-state logic. The general definition of state belongs in [Models & Abstraction](../models-abstraction/README.md), while the physical register, flip-flop, and gate mechanisms belong here.

## Clocking, delays, and reliability limits

Physical digital systems are subject to signal propagation and setup/hold timing constraints. A flip-flop usually requires the input to be sufficiently stable around the relevant sampling edge. Violating these constraints can lead to **metastability**, a condition in which the circuit temporarily does not settle promptly to a valid logical state.

Synchronizers and careful clock-domain design reduce the risk of metastability-related failures, but they do not magically remove all physical timing constraints. Clocked designs must also account for **clock skew**, path delay, and the timing of interfaces between synchronous and asynchronous components.

The MIT [Computation Structures lecture sequence](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/) explicitly distinguishes digital abstraction, combinational logic, gate timing, sequential logic, storage elements, and synchronization. Its [synchronization and metastability resource](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/resources/mit6_004s09_lec07/) provides a focused technical reference for timing-related failure modes.

## Distinctions that matter

**Formal logic versus digital logic:** formal logical validity is a property of mathematical statements; digital logic concerns physical realization with nonzero delays and electrical constraints.

**Combinational versus sequential:** combinational functions depend on present input values in their logical model; sequential circuits include state and timing behavior.

**Clock frequency versus throughput:** operating at a given clock frequency does not alone establish how many useful operations complete per second. Pipeline stages, latency, dependencies, and workloads affect realized performance.

**Circuit description versus built hardware:** a truth table or HDL model describes intended behavior under assumptions; actual implementation has physical constraints and must be designed and verified accordingly.

## Connections across the knowledge base

[Boolean and predicate logic](../mathematics-logic/README.md) supplies algebraic operators; [Electronics](../physical-electrical-principles/README.md) supplies transistor and signal mechanisms; [Timing and clocks](README.md) develops hardware timing; [Processors and instruction sets](README.md) extends digital circuits into programmable computation; [State, events, and transitions](../models-abstraction/README.md) provides general state models.

These broad links lead to approved area inventories unless a canonical article already exists. A document's location is not an ontological parentage statement.

## References and verification status

- [MIT OpenCourseWare: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/).
- [MIT OpenCourseWare: Computation Structures lecture notes](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/), especially digital abstraction, CMOS gates, combinational/sequential logic, finite-state machines, and synchronization.
- [MIT OpenCourseWare: Synchronization, Metastability and Arbitration](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/resources/mit6_004s09_lec07/), a focused lecture reference for metastability.
- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/), for formal mathematical reasoning distinct from physical circuit implementation.
- [MIT Computation Structures: Sequential Logic notes](https://computationstructures.org/notes/sequential_logic/notes.html), for latches, flip-flops, state, propagation, and setup/hold timing.
- [MIT Computation Structures: Finite State Machines](https://computationstructures.org/lectures/fsm/fsm.html), for state-machine implementation and metastability limitations.

**Review record:** The logic-gate and half-adder truth tables were evaluated directly across all four two-input combinations. MIT's published lecture material was checked for the physical-digital-abstraction, sequential-logic, propagation-delay and metastability distinctions. Exact electrical limits remain technology-dependent and have deliberately not been asserted. The article passed the model-assisted scoped acceptance audit; independent human publication approval remains outstanding.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Canonical ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)
