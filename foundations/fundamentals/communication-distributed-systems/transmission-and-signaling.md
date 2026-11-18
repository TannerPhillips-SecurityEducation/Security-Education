# Transmission and Signaling

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Transmission and signaling  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Communication & Distributed Systems 54-family audit](../WAVE-E-TECHNICAL-REVIEW-02.md); independent human review pending

## Transmission carries represented information through a medium

**Transmission** is the physical or logical conveyance of represented information from one point or participant to another. **Signaling** uses selected changes in a physical or modeled quantity to represent symbols, boundaries, timing, control or other information.

A bit is an abstract binary distinction. On a physical channel, it may be represented by voltage, light, radio-frequency properties or another measurable mechanism. A physical waveform need not consist of exactly zero or one-valued magnitudes to support digital symbol detection.

[Analog and Digital Signals](../physical-electrical-principles/analog-and-digital-signals.md) owns general continuous/discrete representation. [Waves and Frequency](../physical-electrical-principles/waves-and-frequency.md) owns physical oscillation and propagation. This article owns transmission and signaling as elements of communication systems.

## Symbols, encoding and timing

A **symbol** is a distinguishable unit in an agreed representation. A signaling system maps input bits or symbols into physical patterns and maps received patterns back into decisions under its decoding rules.

One symbol can encode several bits when there are enough reliably distinguishable states. A symbol rate, measured in symbols per second, is therefore not automatically equal to the raw bit rate. Coding overhead, synchronization and error recovery can change useful data throughput.

A receiver needs appropriate symbol boundaries, timing alignment and thresholds or other interpretation rules. Electrical compatibility does not guarantee semantic compatibility.

[Symbols and Encoding](../information-data/symbols-and-encoding.md) owns abstract mapping; [Signal Conversion](../physical-electrical-principles/signal-conversion.md) owns conversion between physical and digital representations.

## Serialization and framing

A physical link may carry a continuous sequence of symbol events, while a protocol introduces frames or packets to delineate exchange units. A frame can contain headers, payload and error-detection fields under a defined format.

**Framing** allows a receiver to locate boundaries, but structural validity does not prove origin authenticity or content truth. An error-detection value may detect selected corruption patterns without guaranteeing perfect recovery.

**Line coding**, modulation and multiplexing solve different representation and resource-sharing problems. The chosen method depends on medium, capacity, noise, compatibility and system requirements.

## Worked example: raw rate versus payload time

Suppose an idealized link carries exactly **8,000,000 raw bits per second** continuously with no overhead or errors. A payload of one mebibyte contains

```text
1 MiB = 1,048,576 bytes
Payload bits = 8 × 1,048,576 = 8,388,608 bits
Ideal minimum transmission time = 8,388,608 / 8,000,000
                                = 1.048576 seconds
```

The result is the time to serialize the stated number of bits at the stipulated raw rate. It excludes framing, coding, retransmission, propagation, receiver processing and application delays. **Raw signaling rate is not end-to-end application throughput.**

The example uses binary `MiB` and decimal millions of bits per second deliberately; confusing units changes the answer.

## Direction, medium and constraints

A transmission medium may permit signals in one direction, alternating directions or both directions under defined rules. A duplex label does not alone specify usable bandwidth, scheduling or concurrent access.

Noise, attenuation, distortion, interference, propagation delay and hardware limitations can affect the received representation. A transmitter sending the correct pattern does not ensure the receiver interpreted it correctly.

[Communication Channels](communication-channels.md) owns channel behavior and capacity limitations; [Latency and Throughput](latency-and-throughput.md) owns end-to-end performance measures.

## Scope and references

This article does not mandate a cabling type, optical transceiver, radio modulation scheme, network protocol or vendor implementation. Signal physics and software exchange contracts keep their own canonical roles.

### Sources

- [MIT 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
- [MIT 6.1800 Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).
- [NIST Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).
- [RFC 9293 TCP Specification](https://www.rfc-editor.org/rfc/rfc9293.html).

**Editorial status:** Reviewed (model-assisted) following the [Wave E Communication & Distributed Systems 54-family technical audit](../WAVE-E-TECHNICAL-REVIEW-02.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
