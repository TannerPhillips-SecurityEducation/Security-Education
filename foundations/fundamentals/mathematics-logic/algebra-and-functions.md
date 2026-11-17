# Algebra and Functions

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Algebra and functions  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending

## Algebra expresses relationships without committing to an implementation

**Algebra** develops rules for operating on mathematical expressions and for characterizing relationships between values, structures, and operations. An expression such as `2x + 3` describes a value in terms of a symbol `x`; an equation such as `2x + 3 = 11` asserts equality under a specified interpretation. Solving it involves applying valid transformations to find values of `x` satisfying the equality, rather than assuming the text is itself a program.

A **variable** is a symbol whose interpretation can vary across a chosen domain. Its domain matters: `x² = 2` has no rational solution but has two real solutions. Algebra is therefore not simply arithmetic performed with letters. It provides tools to describe **patterns, constraints, dependencies, and transformations** in domain-independent terms.

This article focuses on algebra and functions necessary for technical systems. It is not a declaration that the separate mathematics-breadth question [G-01](../COVERAGE-GAP-DECISIONS.md) has been resolved.

## Expressions, equations, and constraints

An **expression** represents a value or abstract operation under specified rules. An **equation** states that two expressions have equal values. An **inequality** places an ordering constraint on values in an ordered domain.

Consider the expressions:

```text
f(x) = 2x + 3
2x + 3 = 11
2x + 3 ≤ 11
```

The first specifies a rule assigning outputs to inputs; the second asserts a condition satisfied by `x=4`; the third describes a set of permissible values `x≤4` when `x` is real. These are not interchangeable statements.

An **identity**, such as `(a+b)² = a² + 2ab + b²` over commutative real-number algebra, holds for every permitted assignment of the variables. A contingent equation such as `2x+3=11` holds only for selected assignments. The assumptions under which algebraic laws hold must be explicit, especially outside ordinary real-number arithmetic.

For example, matrix multiplication is generally noncommutative: `AB` need not equal `BA`. Treating every algebraic structure as ordinary arithmetic would produce invalid transformations.

## Functions: inputs, outputs, and definitions

A **function** `f: A → B` assigns **exactly one** element of the codomain `B` to each element of its domain `A`. The *range* or *image* `f(A)` comprises values actually attained, and may be a proper subset of the codomain.

For `f: ℝ → ℝ`, `f(x)=2x+3`, every real input has one real output; the range is all real numbers. By contrast, `g: ℝ → ℝ`, `g(x)=x²`, has a range consisting of the nonnegative real numbers, even though its codomain was declared to be all reals.

A function is not the same as an arbitrary relation. The formal relationship to set theory is developed in [Sets and Relations](sets-and-relations.md); the educational treatment of function notation and range is also covered by [OpenStax: Functions and Function Notation](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation).

**Partial functions** may be undefined for some inputs. For example, the expression `h(x)=1/x` does not define a real-valued result at zero. It is either specified as a function with domain `ℝ\{0}`, or treated as a partial rule over a larger set. A system using the formula must make that distinction operationally meaningful rather than silently dividing by zero.

## Composition combines transformations

If `g: A→B` and `f: B→C`, their **composition** `f∘g` applies `g` first and then `f`. The result is `(f∘g)(x)=f(g(x))`.

Let `f(x)=2x+3` and `g(x)=x²` over real numbers:

```text
(f ∘ g)(x) = 2x² + 3
(g ∘ f)(x) = (2x + 3)²
```

They are generally different functions. At `x=1`, the first yields `5` while the second yields `25`. Hence **composition is not generally commutative**.

A composition's domain must also be considered. If `f(y)=√y` and `g(x)=x-3`, then `(f∘g)(x)=√(x-3)` is defined as a real-valued expression only for `x≥3`. [OpenStax: Composition of Functions](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions) explicitly discusses how composition restricts domains.

## Inverse functions and loss of information

An **inverse function** reverses a function's mapping when suitable conditions hold. For a bijection `f: A→B`, the inverse `f⁻¹: B→A` satisfies `f⁻¹(f(x))=x` and `f(f⁻¹(y))=y`.

For `f(x)=2x+3` on the real numbers, `f⁻¹(y)=(y-3)/2`. Substituting this expression recovers the original input.

But `g(x)=x²` is not injective on `ℝ`: the distinct values `3` and `-3` both map to `9`. It therefore has no inverse **function over all real inputs and all of its attained outputs**. Restricting **both the domain and codomain to `[0,∞)`** yields a bijection `g: [0,∞) → [0,∞)`, whose inverse is `g⁻¹(y)=√y`. Simply restricting the domain while retaining codomain `ℝ` would not produce a bijection onto all reals. The [OpenStax treatment of inverse functions](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions) develops the distinction between one-to-one mappings and domain restriction.

This is a useful abstract model of information loss: a many-to-one transformation cannot always recover its original input from the output alone.

## Linear, affine, and nonlinear behavior

In elementary graphing, an expression of the form `f(x)=mx+b` is often called a *linear function*. In the more restrictive language of **linear algebra**, a linear transformation must preserve addition and scalar multiplication. Consequently, `f(x)=mx+b` with `b≠0` is **affine**, not linear in the strict transformation sense.

This distinction matters for systems models. A fixed offset may be part of a calibration function, but a mathematically linear map has additional structural properties. A quadratic function, exponential function, and threshold function describe other kinds of nonlinear behavior.

The word **linear** must therefore be interpreted in its context, not automatically transferred between an elementary straight-line graph and a vector-space transformation.

## Algebraic systems versus execution mechanisms

A function is an abstract mapping. It does not inherently specify an algorithm, programming language, execution time, memory layout, numerical representation, or hardware circuit. A mathematical operation can be implemented using software or electronics, but those are specialized mechanisms.

A formula may also be **exact** in mathematics while its numerical implementation is approximate. See [Numbers and Numerical Systems](numbers-and-numerical-systems.md) for radix and finite precision, and [Measurement](../scientific-analytical-reasoning/measurement.md) for a physically interpreted quantity.

An equation does not automatically establish **causality**, either. The relationship `y=2x+3` can describe how two modeled quantities co-vary, but causal conclusions require a model of mechanisms and supporting evidence.

## Worked illustration: a calibration mapping

Suppose a model assigns a physical quantity from a digital sensor reading `r` using

```text
T(r) = 0.5r - 10
```

For the input `r=50`, the mapped output is `15` in the chosen unit system. If the mapping is bijective over the selected input/output domains, the inverse is `r(T)=2(T+10)`. A second calibration stage applied afterward produces a composition of functions.

This is an **illustrative mathematical mapping**, not a real calibrated sensor specification. Nothing in this equation alone establishes measurement uncertainty, traceability, valid input ranges, or physical accuracy.

## Canonical relationships and references

[Sets and Relations](sets-and-relations.md) formalizes functions as relations; [Numbers and Numerical Systems](numbers-and-numerical-systems.md) provides numerical domains; [Boolean and Predicate Logic](boolean-and-predicate-logic.md) handles logical assertions; [Models & Abstraction](../models-abstraction/README.md) covers model assumptions; [Computation & Algorithms](../computation-algorithms/README.md) develops procedures implementing mappings.

### Sources

- [OpenStax: Functions and Function Notation](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation).
- [OpenStax: Composition of Functions](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions).
- [OpenStax: Inverse Functions](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions).
- [MIT OpenCourseWare: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/).

**Editorial review note:** The inverse-function codomain qualification was corrected, and the example values, composition order, and equation/inequality cases were independently recomputed. These are material-claim checks reported in the Wave A Batch 03 review ledger; they do not imply independently human-verified publication. G-01 and G-02 remain separate coverage questions.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
