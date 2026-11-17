# Bits and Bytes

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Bits and bytes  
**Development status:** Draft  
**Source review:** References listed; separate scoped claim-to-source audit pending

## Digital information as binary distinctions

A **bit** is a binary digit having one of two possible values, conventionally written 0 or 1. A **byte** is a group of eight bits in modern standardized computing terminology. A bit value is an abstract symbol, not intrinsically a particular voltage, magnetization, optical pulse, or physical device. The mechanism that stores or carries a binary distinction depends on the implementation.

The [NIST bit glossary](https://csrc.nist.gov/glossary/term/bit) and [NIST byte glossary](https://csrc.nist.gov/glossary/term/byte) define these units for technical use. [Symbols and Encoding](symbols-and-encoding.md) explains how a representation maps symbols to meanings. [Digital Logic](../digital-systems-hardware/digital-logic.md) describes implementations of Boolean behavior.

## Bit strings and positional values

A **bit string** is an ordered sequence of bits. The eight-bit pattern `00101101` can be interpreted as an unsigned base-two integer:

```text
0·128 + 0·64 + 1·32 + 0·16 + 1·8 + 1·4 + 0·2 + 1·1 = 45
```

This result depends on the convention that the leftmost bit has the highest positional weight. The same eight bits can instead denote a character-code unit, a set of independent flags, a signed integer, or another encoded value under another format. **A bit pattern does not carry its type or meaning by itself.**

An eight-bit unsigned integer can denote 256 distinct patterns, conventionally mapped to integer values 0–255. An ordered sequence of `n` freely selectable binary positions has `2^n` possible bit patterns, before any format restrictions. This is a combinatorial count, **not** an assumption that random bit values are probabilistically independent; an application format may admit fewer patterns.

## Grouping, order, and interpretation

Bytes group bits for organization, storage and exchange. Larger values may span multiple bytes. **Byte order** (endianness) specifies how multi-byte units are arranged in a particular representation. It should not be conflated with bit numbering or transmission order.

For example, the unsigned hexadecimal value `0x1234` may be encoded in two octets:

| Convention | First byte | Second byte |
| --- | --- | --- |
| Big-endian, most-significant byte first | `0x12` | `0x34` |
| Little-endian, least-significant byte first | `0x34` | `0x12` |

Neither layout is intrinsically incorrect. The decoding agreement matters. Network, processor and file formats may choose different byte-order conventions. A declaration of type, length, sign, and endianness is required before interpreting a raw multi-byte sequence.

## Units and capacity

In standard contemporary terminology, `1 B = 8 b`: uppercase B stands for byte, lowercase b for bit. Decimal SI-prefix usage yields `1 kB = 1000 B`, while binary-prefix usage yields `1 KiB = 1024 B`. This distinction follows [NIST guidance on binary prefixes](https://physics.nist.gov/cuu/Units/binary.html).

A rate `8 Mb/s` is eight million bits per second under decimal prefix convention, not eight megabytes per second. The raw arithmetic equivalent is `1 MB/s` if an exactly eight-bit byte and decimal prefixes are stipulated, ignoring protocol overhead and other application-level effects. Observed transfer throughput requires defining measurement boundaries.

## Representation limits

Bits and bytes constrain representational capacity, but **size alone does not establish information content**. Eight bits can encode 256 patterns, while a source always emitting `00000000` has zero Shannon entropy under a deterministic-source model. Conversely, a source uniformly choosing among 256 patterns has eight bits of Shannon entropy per output, given its stated probability model.

This conceptual separation is developed in [Information Theory](information-theory.md). [Numbers and Numerical Systems](../mathematics-logic/numbers-and-numerical-systems.md) owns the underlying positional arithmetic; [Units and Quantities](../mathematics-logic/units-and-quantities.md) owns the general unit/prefix calculus. Bit-level formats and encodings can involve padding, alignment, error detection, and framing; those are contextual design mechanisms, not intrinsic properties of a bit.

## Worked example: a decoding disagreement

A two-byte source transmits `12 34` in hexadecimal. A big-endian consumer interpreting an unsigned 16-bit integer obtains `0x1234 = 4660`; a little-endian consumer obtains `0x3412 = 13330`. Both apply internally consistent rules, but they do not agree on representation semantics.

This does not establish which consumer is correct without the producer's format specification. In diagnostics, preserve both the original bytes and the declared interpretation rather than silently replacing evidence with a decoded value.

## Sources and boundaries

- [NIST: Bit](https://csrc.nist.gov/glossary/term/bit).
- [NIST: Byte](https://csrc.nist.gov/glossary/term/byte).
- [NIST: Binary prefixes](https://physics.nist.gov/cuu/Units/binary.html).

**Editorial status:** Substantive draft. Encoding examples and unit claims require their own documented technical audit before model-assisted Reviewed status. No assessment material or domain-specific ownership is added.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
