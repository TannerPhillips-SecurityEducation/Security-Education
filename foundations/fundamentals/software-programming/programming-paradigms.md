# Programming Paradigms

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Programming paradigms  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Software Batches 03–04 audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md); independent human review pending

## A paradigm frames how a computation is expressed

A **programming paradigm** is an approach to organizing and reasoning about programs, including how values, state, control flow, functions, objects, constraints or events are represented. Paradigms emphasize different design concerns, but they are not mutually exclusive classes of languages.

A language may support several paradigms, and a single program may combine them. For example, a program can use pure functions for calculations, mutable objects for device coordination and event-driven callbacks for user interaction.

The [MIT 6.005 Software Construction curriculum](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/syllabus/) covers abstraction, mutable and immutable data, object-oriented patterns, functional programming, and concurrent software. This subject owns the **styles of computational expression**, not a prescribed language-selection doctrine.

## Imperative, declarative and functional views

**Imperative programming** describes computation through operations that update state or direct execution. **Declarative programming** emphasizes the required result, relationships or constraints, potentially delegating execution strategy to an implementation.

The two are a spectrum of descriptions rather than a perfect binary partition. A declarative query may contain procedural extensions, and an imperative program may use declarative subexpressions.

**Functional programming** emphasizes functions as abstractions and may use immutable values and higher-order functions. A **pure function**, under its defined model, produces equivalent results for equivalent inputs without observable side effects. Many practical functional-language programs also perform I/O or use mutable structures, so “functional” does not automatically mean every operation is pure.

[Functions and Algebra](../mathematics-logic/algebra-and-functions.md) owns mathematical functions, while [Algorithms](../computation-algorithms/algorithms.md) owns computational procedures.

## Objects, logic and event-driven programming

**Object-oriented programming** organizes programs around objects with identity, state, methods and/or message interaction under a language-specific model. Encapsulation and abstraction can help control access, but objects do not guarantee clean architecture or absence of shared-state errors.

**Logic and constraint programming** express relationships, rules or conditions from which a solver can derive results under particular inference semantics. Solver completeness, termination and soundness depend on the language and problem class.

**Event-driven programming** responds to events or messages through handlers, callbacks or reactive constructs. It can be combined with functional, imperative and object-oriented styles. An event-driven application does not necessarily have independent execution threads.

These examples are **nonexclusive explanatory paradigms**, not newly approved subject headings or a universal philosophical taxonomy.

## Worked example: one result through two styles

Given the finite sequence `[1,2,3,4]`, calculate the **sum of squares of even values**.

An imperative model can loop over the sequence, test parity, and update a running total:

```text
total = 0
for x in [1,2,3,4]:
    if x is even:
        total = total + x*x
return total
```

A functional/declarative expression can describe:

```text
sum(map(square, filter(is_even, [1,2,3,4])))
```

Both return `2² + 4² = 4+16 = 20` under exact integer arithmetic and equivalent predicate definitions. The two representations do **not** necessarily have identical memory usage, evaluation timing or exception behavior for arbitrary inputs. The functional expression is pseudocode, not a claim that every language has those exact built-in names.

The example demonstrates that a common objective can have distinct styles of expression without ranking one as universally superior.

## State, effects and reasoning obligations

When functions are pure, substituting equivalent expressions can simplify some reasoning. Mutation can make local reasoning harder when aliases reference shared state. Conversely, in-place updates may reduce allocations or suit devices that require state changes.

A style's benefits depend on the problem and implementation. A callback structure can express asynchronous I/O but introduce difficult event ordering. An object abstraction can hide representation details but still expose inconsistent or underspecified behavior.

[Data Types](../information-data/data-types.md) owns type semantics generally. [Concurrency and Parallelism](../computation-algorithms/concurrency-and-parallelism.md) owns overlapping execution, and [Synchronization](../computation-algorithms/synchronization.md) owns coordination rules.

## Architectural boundaries

Programming paradigms describe conceptual approaches to programs. They are not synonyms for software architecture, compiler technology, concurrency mechanism or organizational methods. [Modules and Dependencies](modules-and-dependencies.md) owns program-level packaging and coupling; [Software Interfaces](software-interfaces.md) owns collaboration contracts among software components.

No programming language, framework, paradigm hierarchy, personal preference or learner assessment is mandated.

### Sources

- [MIT 6.005: Software Construction Syllabus](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/syllabus/).
- [MIT 6.005: Map, Filter, Reduce](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/25-map-filter-reduce/).
- [MIT 6.005: Mutability and Immutability](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/09-immutability/).

**Editorial status:** Reviewed (model-assisted) after the scoped [Wave D Software 54-family audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md). Complete source verification, independent expert review and final publication acceptance remain separate outstanding gates.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
