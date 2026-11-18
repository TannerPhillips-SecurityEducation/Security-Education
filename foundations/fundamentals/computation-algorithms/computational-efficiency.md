# Computational Efficiency

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Computational efficiency  
**Development status:** Draft  
**Source review:** Authoritative references listed; separate scoped technical audit pending

## Efficiency is relative to a workload, resource, and purpose

**Computational efficiency** concerns obtaining a defined computational result while using time, memory, energy, communication, storage or other resources under constraints. What is efficient for one workload or environment may be unsuitable for another.

Theoretical asymptotic bounds are useful but do not supply complete practical performance predictions. **Efficiency** requires a declared resource objective and cost or measurement model, and a defensible comparison of candidate procedures and implementations.

[Complexity](complexity.md) owns formal asymptotic growth and complexity classes. This article owns **practical resource tradeoffs, measurement, bottlenecks and optimization decisions**. [Algorithm Design](algorithm-design.md) owns construction of a correct procedure.

The [MIT 6.172 Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/) course covers performance analysis, caching, parallel programming and optimization in actual systems.

## Define the work before comparing performance

A performance comparison is meaningful only when the alternatives perform equivalent required work. Reducing output quality, silently dropping records or changing a correctness condition can make a program faster while no longer satisfying the task.

Different measures answer different questions:

| Resource or measure | What it characterizes | Limitation |
| --- | --- | --- |
| Latency | Time to complete a specific request or operation | May hide throughput under concurrent load |
| Throughput | Work completed per unit time | May ignore tail latency or fairness |
| Memory footprint | Amount and type of memory consumed | Does not itself describe access patterns |
| Energy | Physical energy transferred or consumed for a workload | Depends on measurement and system boundary |
| Communication | Messages or bytes exchanged under a protocol | Wire volume is not necessarily useful information |
| Computational work | Modeled count of selected primitive operations | Not the same as physical elapsed time |

A benchmark must specify workload, inputs, environment, version, warmup, repetitions and aggregation method when relevant. One measured run can be affected by caching, scheduling, system load, temperature or measurement error.

## Worked example: a crossover between two cost functions

Consider two hypothetical procedures that solve the **same** problem under identical assumptions, with the following toy operation counts for positive integer input size `n`:

```text
Procedure A: C_A(n) = n²
Procedure B: C_B(n) = 50 n log₂(n)
```

At `n=100`, A costs `10,000` units while B costs approximately `33,219.3` units. A is cheaper under the stipulated model. At `n=1,000`, A costs `1,000,000` units while B costs approximately `498,289.2` units, so B is cheaper.

This illustrates why an asymptotically better algorithm may lose to one with lower constants for some practical input sizes. It does **not** establish that either cost function represents an existing implementation, nor that every large input favors B without additional domain/constant conditions.

A model comparison is a derivation from stipulated formulas, not measured performance. Hardware measurements require actual implementations and defined workloads.

## Bottlenecks and resource coupling

A computation may be limited by CPU work, memory bandwidth, storage latency, network transfer, synchronization or another constrained resource. Optimizing a component that does not limit the end-to-end task may have little effect.

Suppose 80% of a normalized workload's elapsed time is attributable to a component and it is made four times faster, while the remaining 20% is unchanged and overhead is ignored. Amdahl's fixed-workload model predicts total speedup:

```text
S = 1 / (0.20 + 0.80/4) = 2.5
```

The result is 2.5×, not 4×. It is an illustrative bound under fixed fractions and no additional overhead, not an actual performance result for any computer. Changing the workload or adding bottlenecks changes the conclusion.

[Concurrency and Parallelism](concurrency-and-parallelism.md) owns the theoretical overlap and simultaneous work mechanisms; efficiency owns how their costs appear in a system-level evaluation.

## Time–space and implementation tradeoffs

Caching can reduce repeated computation or memory access but uses capacity and introduces coherence concerns. Precomputation can shorten later requests while increasing setup work and stored state. Parallelism can reduce latency while increasing total coordination work and energy.

A structure offering constant-time average lookup may have large memory overhead, weaker worst-case guarantees or expensive resizes. An alternative with slower nominal lookup could be preferable when stable worst-case behavior or ordered traversal is important.

[Computational Data Structures](computational-data-structures.md) owns representation invariants and operation costs. [Memory and Storage](../digital-systems-hardware/memory-and-storage.md) owns physical memory systems. [Buses and Interfaces](../digital-systems-hardware/buses-and-interfaces.md) owns hardware transfer constraints.

## Profiling and controlled evaluation

**Profiling** observes where resources are consumed during execution. A profile can identify a hotspot under a particular workload; it does not prove that optimizing the hotspot will yield proportional whole-system speedup.

A defensible optimization process establishes a correct baseline, measures under controlled conditions, identifies a bottleneck, changes one justified mechanism, reruns equivalent work, and checks that correctness remains intact. It may also record statistical variation rather than reporting a single best run.

The [MIT 6.172 course](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/) provides examples of performance engineering and measurement. These are methods to evaluate systems, not a mandatory benchmarking toolchain for the Fundamentals reference.

## Efficiency, sustainability and reliability

Lower energy consumption or resource use may be an engineering objective, but apparent efficiency can hide costs displaced to another machine, network or human operator. Evaluating resource claims requires a relevant system boundary and workload.

An optimization that makes failure recovery expensive or violates a latency requirement may be unacceptable despite lower mean resource consumption. [Requirements](../systems-engineering/requirements.md) owns engineering criteria; [Verification and Validation](../systems-engineering/verification-and-validation.md) owns evidence of meeting them.

This article does not adopt one performance metric, architecture, compiler, profiler or assessment regime.

### Sources

- [MIT 6.172: Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/).
- [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT 6.005: Software Construction](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/).

**Editorial status:** Substantive Draft. Crossover arithmetic and speedup model require a separate scoped technical/source audit. No benchmark, platform, profiler, or learner assessment is mandated.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
