# Communication Models

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Communication models  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Communication & Distributed Systems 54-family audit](../WAVE-E-TECHNICAL-REVIEW-02.md); independent human review pending

## Communication requires an exchange contract

A **communication model** describes participants, the information or signals exchanged, the means by which exchanges occur, and the interpretation of the exchange under defined assumptions. A sender, receiver, channel and message are useful roles, but actual systems may involve many senders, brokers, intermediate nodes, observers, shared state or bidirectional interactions.

**Sending**, **acceptance by an intermediate system**, **receipt**, **interpretation** and **completion of an intended action** are distinct claims. A system can faithfully carry a message that is semantically wrong or no longer relevant.

[MIT 6.1800 Computer Systems Engineering](https://catalog.mit.edu/subjects/6/) addresses client-server decomposition, networking, naming and fault-tolerant systems. [Collaboration and Communication](../human-sociotechnical-systems/collaboration-and-communication.md) owns human coordination and meaning; this article owns modeled machine-to-machine or broader technical exchange structures.

## Messages, streams, and interactions

A **message** is a discrete exchange unit under a communication protocol. A **byte stream** presents an ordered sequence of bytes without necessarily preserving application-message boundaries. A **datagram** carries a bounded, separately framed delivery unit under a selected transport model.

A client/server arrangement organizes request and service responsibilities. A publish/subscribe arrangement allows senders to publish information for selected subscribers through a delivery mechanism. A peer-to-peer arrangement distributes interacting responsibilities among peers.

These are explanatory patterns, not exclusive architecture families. A system can use more than one pattern, and the chosen transport does not dictate organizational authority.

[Protocols and Layering](protocols-and-layering.md) owns agreed exchange rules; [Reliability and Ordering](reliability-and-ordering.md) owns lost, duplicated and reordered messages.

## Synchronous and asynchronous expectations

An **asynchronous exchange** may allow a sender to continue without waiting for an immediate response, while a **synchronous interaction** may wait for an answer or established completion condition. These labels apply to the interaction contract, not necessarily to physical transmission timing or the implementation's thread count.

A timeout does not prove that a remote operation failed. It may indicate delayed processing, response loss, queueing or actual nonexecution. Retries must therefore account for potential repeated effects.

## Worked example: request and outcome separation

Suppose a fictional sender issues five update requests labeled A–E. The receiver reports four acknowledgments, for A–D. From this observation, **four acknowledgments were received** and one is missing. It does not prove that only four updates executed: E could have executed while its acknowledgment was lost, or could still be pending.

The ratio `4/5=80%` describes acknowledgment receipt for this **five-request sample**, not a justified general network delivery probability. Missing information about the actual remote state prevents a stronger outcome claim.

An interface that reports “80% successful updates” solely from acknowledgment count would need to define what *successful* means and whether acknowledgments establish completed effects.

## Scope, failure and trust

Communication models can include partial failures: one party remains operational while another becomes inaccessible. Network and process failures may be observationally indistinguishable for a caller without additional information.

Communication can also cross trust and protection boundaries. That does not make every message authentic or authorized. Transport delivery, identity assurance and the validity of a resulting action are different concerns.

[Addressing and Naming](addressing-and-naming.md) owns how endpoints/resources are referenced; [Distributed State](distributed-state.md) owns the interpretation of replicated information under partial failures.

## Canonical boundaries

This article does not mandate a network topology, message broker, API transport, or specific network-security practice. It introduces no additional subject categories or learner assessments.

### Sources

- [MIT 6.1800 Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).
- [MIT 6.5840 Distributed Systems, Spring 2026](https://pdos.csail.mit.edu/6.5840/).
- [RFC 9293, TCP: ordered byte-stream service](https://www.rfc-editor.org/rfc/rfc9293.html).
- [RFC 768, UDP: datagram service](https://www.rfc-editor.org/rfc/rfc768).

**Editorial status:** Reviewed (model-assisted) following the [Wave E Communication & Distributed Systems 54-family technical audit](../WAVE-E-TECHNICAL-REVIEW-02.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
