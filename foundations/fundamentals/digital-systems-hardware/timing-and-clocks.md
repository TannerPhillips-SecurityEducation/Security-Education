# Timing and Clocks

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Timing and clocks  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Timing determines when hardware behavior is evaluated

**Hardware timing** concerns durations, event relationships, signal propagation, and conditions under which digital components can reliably capture or change state. A **clock** often provides a recurring signal used to coordinate sequential logic. The clock is a physical mechanism, not the universal definition of time.

A **synchronous** design generally constrains participating state changes relative to defined clock edges. An **asynchronous** arrangement uses other coordination mechanisms. Some systems contain multiple, partly independent clock domains; not every component shares one global clock.

[Digital Logic](digital-logic.md) owns combinational and sequential logic functions. [Waves and Frequency](../physical-electrical-principles/waves-and-frequency.md) owns physical frequency and phase. This article owns hardware clock implementation, cycle timing and interfaces between timing domains.

## Frequency, period, and cycle counts

For a periodic clock of frequency `f`, its ideal period is `T=1/f`.

```text
f = 100 MHz = 100,000,000 cycles per second
T = 1/f = 0.00000001 s = 10 ns
```

If a stipulated operation takes exactly five **non-overlapping cycles on that clock**, its modeled cycle interval is `5×10=50 ns`. An instruction may take a different number of cycles, overlap execution with others or wait for memory. Thus **five cycles** does not automatically mean any specific processor instruction takes 50 ns on real hardware.

A clock frequency alone does not establish system throughput, instruction latency, or correct sampling of a physical input. [Processors and Instruction Sets](processors-and-instruction-sets.md) owns instruction semantics.

## Setup, hold, propagation, and timing margin

A sequential element may require an input to be stable for a minimum **setup time** before a sampling edge and a minimum **hold time** after it. Logic paths have propagation delays, and clock signals can arrive at different locations at slightly different times.

**Timing closure** refers to achieving the applicable timing constraints across specified paths and operating conditions under an engineering model. A combinational circuit producing the correct logical function can still fail to satisfy timing.

For an idealized register-to-register path, a simplified setup inequality is:

```text
clock period ≥ launch clock-to-Q delay
             + combinational path delay
             + receiving-register setup time
             + relevant clock-skew/uncertainty margin
```

Actual timing analysis may require separate minimum-delay/hold constraints, multiple clock paths, variation and detailed device models. The inequality is an explanatory sketch, not a complete timing signoff method.

## Jitter, drift, skew and synchronization

**Jitter** concerns short-term variation in timing relative to a reference; **drift** concerns longer-term change in rate or phase relative to a reference; **clock skew** concerns the difference in timing at relevant destinations. Exact terminology depends on measurement context.

A value crossing between unrelated clock domains can arrive close to a sampling transition and cause **metastability**, a condition in which a sequential element's output has not resolved promptly to a stable logic level. Synchronization arrangements can reduce the risk of downstream failure but do not make it mathematically zero under all physical conditions.

Crossing multi-bit data requires more than independently synchronizing each bit if coherent multi-bit values must be preserved. Handshakes, FIFOs or other domain-crossing protocols can support correct transfers under declared timing and control contracts.

## Worked example: two different hardware timing claims

Suppose a fictional controller produces one output update every 1,000,000 cycles of an ideal **100 MHz** clock:

```text
Elapsed modeled interval = 1,000,000 / 100,000,000 s
                         = 0.01 s = 10 ms
```

The arithmetic interval is 10 ms under a constant 100 MHz clock and exactly one event per million cycles. It is **not** proof that a physical oscillator runs at exactly 100 MHz, that an external event is detected within 10 ms, or that downstream actuation completes within that interval.

An actual timing claim needs a reference, measurement boundary, tolerance, uncertainty and conditions.

## Clocking versus calendar or event temporality

Hardware clock cycles are an engineering implementation of timing and coordination. They do not by themselves define wall-clock time, timestamps, time zones, event ordering across distributed systems or a global theory of temporality.

The existing **G-04 general temporality** scope decision remains open. This article owns physical clocking and hardware timing only; [State and Behavior](../systems-engineering/state-and-behavior.md) owns modeled state changes and [Communication & Distributed Systems](../communication-distributed-systems/README.md) owns domain-specific coordination and distributed ordering.

## Reliability and engineering interpretation

Hardware can exhibit timing violations because of supply, temperature, process variation, electromagnetic effects or operating conditions. A simulation under nominal parameters is not a universal guarantee of correct physical behavior.

[Verification and Validation](../systems-engineering/verification-and-validation.md) owns evaluation against declared timing requirements and intended use. [Buses and Interfaces](buses-and-interfaces.md) owns transfer contracts, including timing assumptions at device boundaries.

### Sources

- [MIT OpenCourseWare 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [MIT OpenCourseWare 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
- [BIPM: SI Brochure](https://www.bipm.org/en/publications/si-brochure).

**Editorial status:** Substantive Draft. Clock arithmetic, timing-path explanation and metastability limitations require a separate scoped technical audit. No hardware implementation or general-temporality scope change is approved.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
