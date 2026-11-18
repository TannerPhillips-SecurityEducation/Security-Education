# Compilation and Interpretation

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Compilation and interpretation  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical/source review pending

## A program can be translated, executed directly, or both

**Compilation** transforms a source representation into another representation intended for analysis or execution, such as machine instructions, bytecode or a different high-level language. **Interpretation** executes or evaluates program representations through an interpreter under a defined language semantics.

These mechanisms are not mutually exclusive. A runtime may compile source to bytecode, interpret bytecode, optimize frequently executed functions into machine code, and later fall back to another execution path. A machine-readable output can also require linking, loading or runtime services.

[MIT 6.035 Computer Language Engineering](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/) covers scanning, parsing, intermediate representations, semantic analysis, code generation, data-flow optimizations and compilation pipelines.

## From source to behavior

A simplified compiler pipeline may contain:

```text
Source characters
  → lexical analysis / tokens
  → parsing / syntax tree
  → semantic and type checks
  → intermediate representation
  → optimization or transformation
  → target code
  → loading and execution
```

This is an **illustrative pipeline** rather than a universal sequence. Some compilers omit certain stages, combine them, or use several intermediate representations. Interpreters also parse and check code; merely doing so does not classify a system as a compiler.

A **front end** focuses on recognizing and analyzing a source language, while a **back end** may generate a target representation and perform target-specific work. The distinction is practical rather than a requirement that implementations use two physically separate programs.

[Syntax and Semantics](syntax-and-semantics.md) owns grammatical and meaning rules. [Processors and Instruction Sets](../digital-systems-hardware/processors-and-instruction-sets.md) owns hardware-visible instruction effects.

## Intermediate representations and optimization

An **intermediate representation (IR)** expresses selected program structure or behavior to support analysis and transformation. An optimizer may eliminate redundant work, simplify expressions or choose a more effective instruction sequence.

Optimization **must preserve the appropriate observable behavior under a specified semantic contract**. An optimization justified for unbounded mathematical integers may not be valid for a language with checked overflow, side effects or unusual evaluation order.

A pass that preserves one set of properties can change others, such as debugging locations, scheduling, numerical rounding or timing. Which changes are permitted depends on language and application requirements.

[Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns assessing practical improvement; compiler optimization implements transformations under constraints.

## Worked example: conditional constant folding

Consider a toy expression language in which integer multiplication and addition are exact and side-effect-free:

```text
Source:       3 * 4 + 2
Folded value: 14
```

A compiler may replace the expression with the literal `14` because the computation is fully determined under the stipulated semantics. This is a simple **constant-folding transformation**.

Now consider an expression `x + 1` when `x` can be a mutable value or an operation with side effects. Replacing it with one compile-time literal is not generally justified. Likewise, reordering floating-point operations can change rounding under some numerical models.

Passing a compiler's syntax and type checks does not establish that the program implements the correct user requirement or that compiled target code is bug-free.

## Interpretation, virtual machines, and JIT

An interpreter may directly evaluate an abstract syntax tree, execute bytecode instructions, or realize another defined execution model. A **virtual machine** is an abstract execution environment and can be implemented by interpretation, compilation, hardware support or combinations.

**Just-in-time compilation (JIT)** creates or optimizes executable representations during execution under specific implementation rules. The terms *compiled language* and *interpreted language* are often oversimplifications because a language is defined by semantics, not a single delivery toolchain.

An implementation's runtime performance depends on workload, optimization, startup and warmup costs, resource management and hardware. JIT use is not an inherent guarantee of high performance.

## Errors and validity boundaries

A compiler can detect malformed syntax or selected static type violations. An interpreter can detect those before or during execution. Neither can generally decide all semantic properties of arbitrary programs, including universal termination, under a Turing-complete model.

An executable may fail because of missing libraries, incompatible runtime assumptions, invalid input or environment conditions. Generated machine code is not a complete proof of deployment readiness.

[Computability](../computation-algorithms/computability.md) owns general undecidability constraints. [Runtime Environments](runtime-environments.md) owns execution resources, loading and lifecycle of code during operation; [Error Handling](error-handling.md) owns reporting and recovery of failures.

## Scope and references

This article does not prescribe a compiler, bytecode format, target ISA, interpreter, build environment or particular programming language. Compilers may target a simulator or virtual machine rather than physical instructions; a target's existence does not guarantee actual hardware compatibility.

### Sources

- [MIT 6.035: Computer Language Engineering](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/).
- [MIT 6.035: Lecture Notes](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/).
- [MIT 6.005: Parser Generators](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/18-parser-generators/index.html).

**Editorial status:** Substantive Draft. The compiler pipeline, JIT interpretation and constant-folding example await separate source and technical review. No assessments or mandatory toolchains are introduced.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
