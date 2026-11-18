# Communication Channels

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Communication channels  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## A channel describes possible exchange and its limitations

A **communication channel** is a modeled or realized path through which signals or messages can be conveyed between participants under defined conditions. It can refer to a physical medium, a logical transmission service or an abstract stochastic mapping from inputs to outputs. These are not interchangeable levels of description.

A channel model may specify input/output alphabets, probabilities, delays, bandwidth, error mechanisms or environmental conditions. Channel capacity is a mathematical property of the declared communication model, not simply a connector's advertised speed.

[Information Theory](../information-data/information-theory.md) owns Shannon entropy, mutual information and coding limits. [Transmission and Signaling](transmission-and-signaling.md) owns physical representation of bits and symbols; this article owns channels and their exchange constraints.

## Medium, link, and end-to-end route

A **physical medium** carries electromagnetic, optical, mechanical or other signals under physical laws. A **logical channel** may be constructed atop several physical links, queues or protocols. A path between application participants may traverse multiple devices and experience changing routes.

A physical link being connected does not guarantee continuous service. Conversely, a logical service can route around a failed component while preserving some abstract interface.

**Channel occupancy** and **channel capacity** differ. A channel may be capable of a specified peak exchange rate but currently carry little information, or be congested due to competing traffic.

## Noise, loss and delay

Real channels can introduce corruption, loss, duplication, interference, variable propagation time and queueing effects depending on their model and supporting protocol layers. **Noise** is not automatically a lost packet, and **packet loss** is not necessarily evidence of corrupted physical bits.

Error detection and correction use agreed redundancy and decoding rules. They can improve reliability under appropriate assumptions but consume additional symbols or time and do not universally eliminate failure.

[Error Handling](../software-programming/error-handling.md) owns local software reactions; [Reliability and Ordering](reliability-and-ordering.md) owns communication delivery and application-level ordering contracts.

## Worked example: modeled propagation delay

Suppose two endpoints are separated by a modeled path length of **200,000 meters**, and a signal propagates through the stipulated medium at exactly **200,000,000 meters per second**.

```text
One-way propagation delay = distance / speed
                          = 200,000 / 200,000,000
                          = 0.001 second = 1 millisecond
```

This is a pure propagation calculation using invented model values. It excludes serialization, routers, queues, processing and other sources of end-to-end delay. A request and response across the same ideal path have **at least 2 ms of propagation time** if each traverses that full path at the stipulated speed, but actual round-trip time may be longer.

The numeric speed is a model assumption, **not** a measurement of a particular fiber, radio link or device.

## Capacity and probability models

For a **discrete memoryless channel**, the familiar Shannon capacity is the maximum mutual information per channel use over its permitted input distributions. More general channels can require different capacity definitions, coding assumptions and constraints.

A bandwidth number quoted in hertz is not a bit-rate guarantee. A source can carry a variety of symbol encodings, and its usable rate depends on channel noise, signal levels, coding, protocol overhead and physical implementation.

An observed fraction of dropped messages over a sample is not automatically the stationary probability of loss for all future messages. Appropriate statistical modeling and measurement are separate tasks.

## Operational boundaries

A channel can be available yet an application can fail because of naming, authentication, incompatible protocol versions, remote computation or storage. A complete system analysis must separate channel transport from service behavior.

[Protocols and Layering](protocols-and-layering.md) owns exchange rules. [Latency and Throughput](latency-and-throughput.md) owns system-measurement boundaries. [Distributed State](distributed-state.md) owns partially observed replicated state.

### Sources

- [MIT 6.1800 Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/).
- [MIT 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).

**Editorial status:** Substantive Draft. Channel definitions, modeled delay and capacity conditions require separate scoped review. No medium or protocol is mandated.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
