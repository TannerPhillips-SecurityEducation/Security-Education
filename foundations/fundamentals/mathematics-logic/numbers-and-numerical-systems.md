# Numbers and Numerical Systems

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Numbers and numerical systems  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending

## Numbers are values; numerals are representations

A **number** is a mathematical object used in counting, ordering, measuring, and describing quantitative relationships. A **numeral** is a written, encoded, or otherwise represented expression for a number. The distinction matters because a number does not change when its representation changes.

For example, the decimal numeral `13`, binary numeral `1101₂`, and hexadecimal numeral `D₁₆` all denote the same integer. They are different strings under different notational systems, not three inherently different quantities.

A **number system** can refer either to a set of mathematical numbers with defined operations or to a **numeral system** for representing them. To avoid ambiguity, this reference separates mathematical number domains from positional notation and finite machine encodings.

## The principal mathematical number domains

Different number domains support different operations, ordering relations, and algebraic properties.

| Domain | Typical notation | Fundamental scope |
| --- | --- | --- |
| Natural numbers | `ℕ` | Counting and ordering nonnegative or positive whole numbers; inclusion of zero depends on convention |
| Integers | `ℤ` | Whole numbers, zero, positive and negative values |
| Rational numbers | `ℚ` | Ratios `p/q` of integers with `q ≠ 0` |
| Real numbers | `ℝ` | Values on the continuous number line, including rational and irrational values |
| Complex numbers | `ℂ` | Values `a + bi` where `a,b ∈ ℝ` and `i² = −1` |

These domains are related but should not be described as equivalent to one another. Rational numbers include values such as `1/10` that may have an infinite expansion in another base; irrational numbers cannot be expressed as a ratio of integers; complex numbers cannot, in general, be ordered in the same way as real numbers while retaining the field's usual operations.

Not all systems treat natural numbers as starting from zero. A mathematical explanation should disclose its convention rather than quietly mix definitions.

## Positional representation and radix

A **positional numeral system** uses a base or **radix** to assign weights to digit positions. In a base `b ≥ 2` system, a finite sequence of digits `dₙ...d₁d₀` represents the value

```text
dₙ · bⁿ + ... + d₂ · b² + d₁ · b + d₀
```

Each digit is selected from an allowed range `0` through `b−1`, with additional symbols beyond 9 needed for bases greater than ten. Common bases include binary (2), decimal (10), and hexadecimal (16). A numeral is meaningful only under its specified convention.

Consider the decimal integer thirteen:

```text
13₁₀    = 1×10 + 3
1101₂   = 1×8 + 1×4 + 0×2 + 1×1
D₁₆     = 13×1
```

All three expressions evaluate to the same mathematical integer. The binary numeral requires four digits, but this does **not** mean the mathematical number intrinsically has four bits.

Positional fractions use negative powers of the radix. For instance:

```text
0.101₂ = 1×(1/2) + 0×(1/4) + 1×(1/8) = 5/8 = 0.625₁₀
```

The binary and decimal strings represent the same rational value under their respective positional rules.

## Signs, zero, and finite representations

A mathematical **negative integer** exists independently of any specific byte encoding. Hardware and software choose particular representations for signed quantities. One widespread finite representation is **two's complement**.

Under an explicitly defined **8-bit two's-complement** convention, the bit pattern `11111101₂` represents `−3`. Under an **8-bit unsigned** interpretation, the same bits represent `253`. The bits have not changed; the agreed interpretation has.

A finite-width machine encoding has a bounded range. The signed 8-bit two's-complement range is `−128` through `127`, whereas unsigned 8-bit binary covers `0` through `255`. These specific limits arise from the chosen representation and width, not the limits of the mathematical integers.

The general meaning of a bit or byte belongs in [Information & Data](../information-data/README.md), while hardware circuits and storage belong in [Digital Systems & Hardware](../digital-systems-hardware/README.md). This article owns the **numerical** distinctions.

## Exactness, approximation, and computation

A rational such as `1/10` is exactly defined mathematically. A finite binary floating-point format generally cannot represent `1/10` exactly, because its binary fraction repeats. This is a property of **representation**, not evidence that `1/10` is mathematically uncertain.

The [Python documentation on floating-point arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html) demonstrates the recurring binary expansion of `0.1` and how a computer stores a nearby representable fraction. It also illustrates why decimal text output can conceal small representation differences.

For ordinary binary floating-point values, `0.1 + 0.1 + 0.1` need not compare exactly equal to `0.3`. This should not be generalized to *every* numeric implementation: arbitrary-precision rational arithmetic and suitable decimal representations can handle some values exactly, subject to their own computational tradeoffs.

**Precision** concerns the discrimination or number of meaningful representable digits, while **accuracy** concerns closeness to an appropriate reference or intended value in a specified context. Rounding, overflow, underflow, truncation, and propagation of numerical errors are separate mechanisms. This article introduces those distinctions; their algorithmic consequences belong to [Computational Efficiency and Algorithm Design](../computation-algorithms/README.md).

## Ordering, equality, and comparison

A numerical comparison assumes a domain and semantics. For exact integers, `13 = 1101₂` is a valid mathematical equality once both notations are interpreted. For approximate floating-point numbers, equality of stored bit patterns, equality under a language's numeric operator, and equality within a selected numerical tolerance may be different questions.

An implementation can also have representations for exceptional conditions, such as infinities or non-number values. These are features of selected numeric formats, not ordinary elements of the mathematical real-number line.

**An identifier that looks numeric is not necessarily a quantity.** For instance, a postal code such as `00501` is a label whose leading zeros may carry format significance; treating it as the integer 501 would discard representational information. Similar distinctions arise for protocol fields and version strings.

## When numerical representation matters

A technical system can move among multiple layers:

```text
Mathematical quantity
    -> chosen numerical domain
    -> representation / radix / precision
    -> stored or transmitted data
    -> interpreted numerical value
    -> comparison or computation
```

Each mapping requires explicit rules. Conversion may preserve exact value, introduce rounding, overflow, or lose metadata such as a leading-zero convention. A different representation does not, by itself, imply a different underlying quantity.

This architecture supports network sizes, program counters, storage capacities, measurements, timestamps, and numerical algorithms without making any one domain the canonical definition of number.

## Cross-knowledge relationships

[Sets and Relations](sets-and-relations.md) supplies membership and ordering structures; [Boolean and Predicate Logic](boolean-and-predicate-logic.md) supplies truth conditions for comparisons; [Symbols and Encoding](../information-data/symbols-and-encoding.md) develops representation conventions. [Measurement](../scientific-analytical-reasoning/measurement.md) develops quantities and uncertainty. [Bits and Bytes](../information-data/README.md) and [Processors and Instruction Sets](../digital-systems-hardware/README.md) are implementation contexts.

Links to uncreated individual articles deliberately resolve to the corresponding approved area indexes.

## Authoritative reference starting points

- [MIT OpenCourseWare: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), mathematical sets, arithmetic, discrete structures, and proof.
- [Python documentation: Floating-Point Arithmetic, Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html), detailed demonstration of binary fractional approximation.
- [Python documentation: Decimal Arithmetic](https://docs.python.org/3/library/decimal.html), examples of exact finite decimal representations in a specified decimal arithmetic model.

**Editorial scope:** This document is a domain-neutral conceptual draft. The 8-bit patterns and radix examples are explicitly defined illustrations; exactness, ranges, and floating-point behavior require format-specific assumptions. No exhaustive survey of numerical analysis is claimed. The G-01/G-02 mathematics coverage questions remain separate from completion of this heading.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
