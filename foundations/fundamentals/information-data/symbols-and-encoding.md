# Symbols and Encoding

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Symbols and encoding  
**Development status:** Draft  
**Source review:** Core claims checked (see [pilot technical review](../PILOT-TECHNICAL-REVIEW.md)); final editorial acceptance pending

## Representation is not meaning

A **symbol** is a mark, character, token, or other distinguishable element used in a system of representation. An **encoding** specifies how elements of one representation are mapped into another form so they can be stored, communicated, or processed.

The letter `A`, the number 65, the binary pattern `01000001`, and the byte `0x41` may be related under a chosen encoding. But none of those representations has the same interpretation in every context. When interpreted as ASCII or as a single-byte UTF-8 sequence, a byte with hexadecimal value `41` represents the character `A`; in another data format, the same byte may be an integer value or part of an unrelated binary field.

A representation therefore requires **rules of interpretation**. Without them, a sequence of bytes does not necessarily disclose whether it encodes text, an image, a numeric value, an instruction, or a mixture.

## A layered model of text representation

The following levels must be kept distinct:

| Level | Meaning | Example |
| --- | --- | --- |
| Abstract character | A character identified by a standard, not its visual appearance | LATIN CAPITAL LETTER A |
| Code point | Integer position in the Unicode code space; may be assigned or unassigned | `U+0041` |
| Encoding form | Rules converting code points into code units | UTF-8 |
| Encoded bytes | Concrete octets representing the encoded text | Hex `41` |
| Glyph | Visual shape rendered by a font or rendering system | One drawn shape for A |

**Characters are not glyphs.** A font may display the same character with different visual shapes; rendering can combine multiple characters into one user-perceived text element. Unicode describes more than a list of printable shapes, including character properties and mechanisms for combining sequences. See the [Unicode Standard's principles](https://www.unicode.org/standard/principles.html).

A **Unicode code point** is an integer in the range `U+0000..U+10FFFF`; not all code points are assigned to characters. Unicode scalar values exclude the surrogate code points `U+D800..U+DFFF`. UTF-8 maps scalar values to sequences of one through four bytes; UTF-16 and UTF-32 use different code-unit structures. These forms can represent the same Unicode text while using different byte sequences.

## UTF-8 as an illustrative encoding

UTF-8 is variable length. It uses one byte for ASCII-range code points and two, three, or four bytes for other scalar values. For well-formed UTF-8, the encoded sequences below are examples:

| Text | Unicode code point | UTF-8 bytes (hexadecimal) |
| --- | --- | --- |
| `A` | `U+0041` | `41` |
| `é` (precomposed) | `U+00E9` | `C3 A9` |
| `€` | `U+20AC` | `E2 82 AC` |

UTF-8 encodes sequences of **Unicode scalar values**, not font shapes, linguistic meaning, or the memory layout of an arbitrary program data structure. Its variable width means that counting bytes does not generally tell you the number of Unicode characters, and counting code points does not always tell you the number of user-perceived grapheme clusters.

For example, the canonically equivalent text `é` can be represented by a single code point `U+00E9`, or by `U+0065 U+0301` (Latin small `e` followed by a combining acute accent). Their UTF-8 byte streams differ: `C3 A9` versus `65 CC 81`.

**Unicode normalization** offers standard procedures for bringing canonically equivalent representations into a consistent form where appropriate, including the canonical NFC and NFD normalization forms. The [Unicode Normalization Forms specification (UAX #15)](https://www.unicode.org/reports/tr15/) defines these transformations. Normalization is not the same operation as case folding, translation, or rendering, and applications need to specify which comparisons they intend.

The [Unicode Standard](https://www.unicode.org/versions/latest/) provides the normative character model; [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629) specifies UTF-8 for the Internet standards context and addresses malformed sequences and compatibility.

## Encoding and decoding as transformations

A basic encoder receives a sequence of source symbols and produces encoded units. A decoder applies corresponding rules to recover a sequence, subject to the encoding's assumptions and validity requirements:

```text
Source symbols
    -> Encoding rules
    -> Encoded units / bytes
    -> Decoding rules
    -> Interpreted symbols
```

This diagram is intentionally simplified. An actual representation chain may contain multiple layers: compression, escaping, framing, serialization, and transport. Those layers are different mechanisms and must not be conflated with the character encoding itself.

A **lossless encoding** is reversible within its specified domain. A **lossy representation** discards distinctions. Malformed data or an incorrect decoder can produce an error, replacement symbols, or an unintended interpretation. The policy chosen for invalid inputs is part of the consuming system's behavior, not part of a symbol's inherent meaning.

## Encoding versus syntax and semantics

These three terms answer different questions:

- **Encoding:** How are chosen symbols represented as data?
- **Syntax:** Which sequences or structures are well formed?
- **Semantics:** What do well-formed sequences mean under an interpretation?

Consider the text `2 + 3`. UTF-8 says how to represent its characters as bytes. A programming-language parser determines whether those tokens fit a grammar. Semantic rules determine whether an expression performs numerical addition, string concatenation, or some other operation. An encoding cannot decide that meaning.

A JSON string may contain escaped representations such as `\u0041`. The backslash escape is part of JSON's **serialization syntax** and must be parsed to recover the intended character; it is not itself the UTF-8 byte encoding of an A.

## Why this matters across technical systems

Network communications, application interfaces, endpoint files, cloud databases, industrial telemetry, and IoT messages all rely on representational agreements. A mismatch between the producing and consuming system may create confusing values even when bytes are transported without physical loss.

A useful diagnostic distinction is whether an observed mismatch arose in **capture**, **transport**, **decoding**, **parsing**, or **semantic interpretation**. These different failure modes cannot be repaired merely by choosing a different font or assuming all bytes represent UTF-8 text.

The foundational treatment of [Bits and bytes](README.md) concerns digital units; [Data types](README.md) concerns value domains; [Data structures and formats](README.md) concerns logical and serialized organization. [Syntax and semantics](../software-programming/README.md) supplies the programming-language realization. These links currently point to approved knowledge-area indexes.

## References and verification status

- [The Unicode Standard: Technical introduction and principles](https://www.unicode.org/standard/principles.html).
- [The Unicode Standard: Version history and current references](https://www.unicode.org/versions/), for version-specific and version-independent citations.
- [RFC 3629: UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629).
- [Unicode Standard Annex #15: Normalization Forms](https://www.unicode.org/reports/tr15/), for NFC, NFD and canonical equivalence.
- [Unicode Standard Annex #29: Text Segmentation](https://www.unicode.org/reports/tr29/), distinguishing Unicode code points from user-perceived grapheme clusters.
- [RFC 8259: JSON Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259), for string-escape rules distinct from the UTF-8 byte encoding.
- [W3C: RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/), illustrating how encoded representations can be associated with structured statements and interpretations.

**Review record:** The UTF-8 byte examples, precomposed/decomposed text and NFC normalization were checked programmatically and against RFC 3629 and Unicode's published specifications. The distinction between Unicode scalar values, code points, glyphs, syntax and meaning remains explicit. This is a source-checked draft pending final editorial acceptance.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Concept boundary decisions](../CONCEPT-BOUNDARY-DECISIONS.md)
