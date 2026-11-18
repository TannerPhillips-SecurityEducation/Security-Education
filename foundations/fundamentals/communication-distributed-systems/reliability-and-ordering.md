# Reliability and Ordering

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Reliability and ordering  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Message delivery is not the same as successful application action

**Communication reliability** concerns whether an exchange reaches a specified destination or satisfies an explicit delivery contract despite possible losses and faults. **Ordering** concerns which sequence of messages or effects can be observed under the chosen model.

Message loss, corruption, duplication, delay and reordering are distinct possible outcomes. A protocol can promise reliable, ordered delivery of bytes while a recipient application still fails to parse, process or persist those bytes correctly.

[Communication Models](communication-models.md) owns sender/receiver exchange roles, [Protocols and Layering](protocols-and-layering.md) owns protocol rules, and this article owns **delivery guarantees, acknowledgments, sequencing and duplicate effects**.

## Acknowledgments, timeouts and retransmission

An **acknowledgment** reports a condition that the relevant protocol defines, such as receipt of sequence-numbered bytes or acceptance of a request. It does not automatically certify application execution, persistent storage or a physical result.

A missing acknowledgment may indicate lost request, lost response, delayed processing, temporary unavailability or another condition. **Retransmission** can improve delivery under particular loss models but may cause repeated requests or delays.

The [TCP specification in RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) defines a reliable, in-order byte-stream service. This does not mean an application gets one message per read call, or that a server processes a command exactly once. [UDP in RFC 768](https://www.rfc-editor.org/rfc/rfc768) does not supply general reliability and duplicate protection.

## Delivery contracts and effects

A system may describe **at-most-once**, **at-least-once** or **exactly-once** processing under a defined operation and failure model.

- At-most-once processing avoids duplicate effects within its scope, but may omit an effect when a request is lost.
- At-least-once processing attempts eventual completion under stated retry and availability assumptions, while permitting duplicate attempts.
- Exactly-once **effects** require more than a sender retrying messages. A well-defined mechanism may combine stable identifiers, deduplication and atomic state changes within particular boundaries.

An unconditional claim of exactly-once action across arbitrary failures, external side effects and independent services is unjustified.

## Worked example: retry and duplicate side effects

Suppose a sender issues a hypothetical request `add 10 units` with identifier 42. A receiver applies the request once, changing a counter from 0 to 10, but its acknowledgment is lost. The sender retries the same request.

Without deduplication, the receiver can apply it again, resulting in **20**. With a specified durable deduplication record and atomic coordination between the application effect and recording identifier 42, the receiver may instead recognize the retry and preserve the counter at **10**.

```text
No deduplication: 0 → 10 → 20
Correct deduplication under stipulated contract: 0 → 10 → 10
```

This does not prove all deduplication implementations are correct. A crash between effect application and recording the identifier can still cause duplication unless those operations are coordinated appropriately. A recorded identifier may also expire under a bounded retention policy.

[Software Interfaces](../software-programming/software-interfaces.md) owns operation semantics and idempotency; [Distributed State](distributed-state.md) owns the replicated state and agreement assumptions.

## Sequencing and partial orders

A transport may provide an ordered byte sequence on one connection without imposing global order across multiple connections, processes or applications. Messages can also arrive in an order different from their original generation times if independent paths or clocks are involved.

**Sequence numbers** can support detection of gaps, duplicates and relative order under defined wrapping, window and connection rules. They are not a universal source of event timestamps.

A FIFO queue can preserve its own enqueue/dequeue order while the surrounding application observes events from other sources in a different interleaving.

## Failure, progress and recovery

A reliable system needs an explicit failure model, including when it retries, gives up, declares an endpoint unavailable, or reports an ambiguous outcome. A deadline provides a local decision condition, not proof of remote failure.

Retries can improve eventual delivery but can also amplify overload and create duplicate effects. A strong delivery guarantee may require durable state, coordination or additional cost; the chosen guarantees must match the intended system.

[Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns general system failure modeling; this subject owns communication delivery and sequencing.

### Sources

- [RFC 9293: TCP, reliable ordered byte stream](https://www.rfc-editor.org/rfc/rfc9293.html).
- [RFC 768: UDP, no guaranteed delivery or duplicate protection](https://www.rfc-editor.org/rfc/rfc768).
- [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/).

**Editorial status:** Substantive Draft. Retry semantics, deduplication and ordering claims require a separate scoped technical/source audit. No protocol or assessment is mandated.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
