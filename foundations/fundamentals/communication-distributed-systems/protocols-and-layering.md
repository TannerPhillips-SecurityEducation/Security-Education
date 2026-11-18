# Protocols and Layering

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Protocols and layering  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Protocols give exchanges agreed rules

A **communication protocol** defines rules governing exchanges among participants: message or signal representation, permitted operations, sequencing, state, error handling and expected responses. A protocol can have a published specification even when implementations differ in internal structure or performance.

**Layering** divides responsibilities across interacting interfaces. Each layer can provide a service to a higher layer using services from a lower layer, under the chosen architecture. An actual implementation need not correspond to one physical device or process per layer.

[Software Interfaces](../software-programming/software-interfaces.md) owns general software contracts. [Communication Models](communication-models.md) owns exchange roles and patterns. This subject owns protocol-level rules and architectural separation.

## Representation, state, and behavior

A protocol can specify message fields and constraints, but a syntactically valid message may be inappropriate in its current protocol state. A request might be valid only after initialization, authentication, negotiation or a previous acknowledgment under the relevant protocol.

A protocol's **state machine** can express permitted transitions and response rules. **Conformance** is a claim about an implementation's behavior against a particular specification and scope, not just about having a correct message parser.

Version negotiation, capability discovery and backward compatibility are conditional mechanisms. A shared protocol name does not prove two implementations agree on optional features or interpretation.

## Encapsulation and boundaries

An upper-layer message may be embedded as a lower-layer payload together with additional control information. This is commonly called **encapsulation**. A receiver must remove or interpret the relevant layers to reconstruct the intended information.

Different layers can introduce headers, trailers, checksums, sequence identifiers or framing. Their exact structure is protocol-specific. **Encapsulation overhead** consumes transmission capacity without itself increasing the application payload.

## Worked example: idealized overhead

Suppose an application sends exactly **1000 payload bytes** inside an invented protocol arrangement adding **40 bytes of total overhead** for each payload, with no fragmentation, retransmission or additional lower-layer overhead.

```text
Total transmitted bytes = 1000 + 40 = 1040 bytes
Payload efficiency = 1000 / 1040 ≈ 0.961538 = 96.15%
```

This is an arithmetic ratio for a stipulated message format. It does not describe the header size or delivery efficiency of any particular Internet protocol. If messages were segmented differently or sent with retries, the ratio could change.

## Why layers are not perfect isolation

Layer boundaries can support modularity and replacement, but lower-layer timing, congestion, failure and security properties can be visible to higher layers. A correct transport stream does not prove that the application correctly interprets a message inside it.

A layer may offer byte-stream semantics, while the application requires framed records. The application must provide its own record boundaries unless another component supplies them.

**TCP** is specified in [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) as a reliable, in-order byte-stream service under its contract. That does not imply that one write call always equals one read call or that delivered bytes have already been processed by the application. **UDP**, [RFC 768](https://www.rfc-editor.org/rfc/rfc768), uses datagrams without general delivery guarantees.

These are grounding examples of **different layer services**, not mandates for this repository.

## End-to-end correctness and layering limits

A checksum can detect selected transmission errors; it cannot establish whether source data were physically accurate. A transport acknowledgment does not necessarily certify that an application committed data to durable storage.

Layered protocols can be tested separately, but end-to-end claims require evidence across the intended full path. Protocol documentation should identify which actor guarantees each property and at which boundary.

[Reliability and Ordering](reliability-and-ordering.md) owns delivery and sequence properties; [Latency and Throughput](latency-and-throughput.md) owns performance consequences. [Distributed State](distributed-state.md) owns agreement about replicated results.

## Canonical boundaries

No particular OSI/TCP-IP layer count, network architecture, protocol or vendor product is imposed. Specialized network security mechanisms belong outside Fundamentals.

### Sources

- [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293.html).
- [RFC 768 UDP](https://www.rfc-editor.org/rfc/rfc768).
- [MIT 6.1800 Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).

**Editorial status:** Substantive Draft. Layer/contract distinctions and overhead arithmetic require separate scoped technical review. No assessment content or new headings introduced.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
