# Latency and Throughput

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Latency and throughput  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Communication & Distributed Systems 54-family audit](../WAVE-E-TECHNICAL-REVIEW-02.md); independent human review pending

## Time to a result differs from volume of results per unit time

**Latency** is a delay between explicitly defined events, such as request submission and response arrival. **Throughput** measures completed work or transferred information per unit time under a stated boundary. **Bandwidth** and raw signaling rate describe different resource quantities and do not by themselves establish application-level useful throughput.

A system can achieve high throughput while individual requests wait a long time, or provide quick responses at low total volume. Performance claims therefore require measurement location, workload, units and aggregation method.

[Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns practical resource tradeoffs generally. [Transmission and Signaling](transmission-and-signaling.md) owns physical representation; this article owns communication delay and exchange-rate metrics.

## Components of end-to-end latency

A message's end-to-end delay may include **serialization**, **propagation**, **queuing**, **processing**, **retransmission** and application scheduling. These contributions can overlap or occur sequentially, depending on a defined model.

- **Serialization time:** time needed to put a given number of bits on a link at a specified rate.
- **Propagation time:** time for a signal to traverse a physical path.
- **Queuing time:** delay waiting for service or available capacity.
- **Processing time:** time consumed by relevant computing and protocol operations.

A simple sum of independent components can be useful in a single-hop serial model; a multi-hop pipeline may overlap activities and require a more detailed treatment.

## Worked example: transmission plus propagation

Suppose a hypothetical point-to-point path has a raw rate of exactly **10,000,000 bits/s**, a one-way propagation delay of **20 ms**, and no contention, protocol overhead, errors or processing. A sender transmits **5,000,000 payload bytes** continuously.

```text
Payload bits = 5,000,000 × 8 = 40,000,000 bits
Serialization = 40,000,000 / 10,000,000 = 4 seconds
Last-bit arrival = 4 seconds + 0.020 seconds = 4.020 seconds
```

The result is a **last-bit arrival time** measured from starting transmission under the stipulated link model. It is not a claim that an application has consumed or stored the data after 4.020 seconds.

The raw rate of 10 Mb/s and payload size of 5 MB use **decimal** prefixes in this example. Actual transfer times can differ from packet overhead, retransmission, receiver delays and lower rates.

## Round-trip time and bandwidth-delay product

**Round-trip time (RTT)** measures elapsed time between defined request and response events. An empty message round trip over the idealized path would have at least `2×20 ms=40 ms` of propagation delay under symmetric travel, even before software and transport overhead.

For a steady path with rate 10 Mb/s and ideal RTT of 0.040 s, the product is

```text
10,000,000 bits/s × 0.040 s = 400,000 bits = 50,000 bytes
```

This **bandwidth-delay product** is a model quantity relevant to the amount of data that may need to be in flight for some window-based mechanisms to fully utilize the path. It is not proof that 50,000 bytes are currently in flight or that every protocol uses that window size.

## Goodput, measurements and variability

**Goodput** measures useful application data delivered over time under a declared boundary, excluding selected overhead and retransmissions. Raw link rate, protocol throughput and goodput may differ substantially.

A mean latency can hide extreme or tail delays. Percentiles depend on the observed distribution and sample; one measurement does not prove a stable worst-case bound. Caches, contention and scheduling can alter behavior between runs.

[Measurement](../scientific-analytical-reasoning/measurement.md) owns uncertainty and observation scope, while [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns distributions and inference.

## Canonical boundaries

This article introduces no network benchmark, QoS policy, vendor equipment assumption, security analysis or training assessment. It describes fundamental performance relationships without equating link speed with completed application work.

### Sources

- [MIT 6.1800: Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/).
- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293.html).
- [NIST Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).

**Editorial status:** Reviewed (model-assisted) following the [Wave E Communication & Distributed Systems 54-family technical audit](../WAVE-E-TECHNICAL-REVIEW-02.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
