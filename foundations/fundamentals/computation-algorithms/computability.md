# Computability

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Computability  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## Some precisely stated problems can be computed; others cannot

**Computability** studies which problems can be solved by an effective computational procedure under a specified model of computation. It concerns the **existence of an algorithm**, independently of whether a practical computer could execute that algorithm within an acceptable amount of time or memory.

A problem must have a defined set of inputs and an expected relationship between inputs and outputs before a computability claim is meaningful. A statement such as “understand every situation” is too ambiguous to classify as decidable or undecidable without a formal problem specification.

The [MIT 6.045J Automata, Computability and Complexity](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/) materials introduce automata, Turing machines, decidability, reductions, computational models and limits of computation.

## Computational models and effective procedures

A **computational model** describes permissible operations, state, representation and rules for executing steps. Turing machines, finite automata, register machines and restricted programming languages are examples with different capabilities.

For **general-purpose computability**, an idealized Turing-machine model provides a standard mathematical reference. This does not mean an actual processor physically contains an infinite tape: unlimited tape is part of an abstract model of possible finite computations, not an engineering specification.

The Church–Turing thesis relates an intuitive notion of effective calculation to formal models such as Turing computability. It is a foundational thesis, **not a physical law or theorem derived from a fully formalized universal definition of “effective procedure.”** Stronger claims about the capabilities of every physical process require additional assumptions.

[Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns model syntax/semantics generally; this subject owns computability claims made relative to such models.

## Decision problems and termination

A **decision problem** asks for a yes/no answer to a property of an input. A decision procedure **decides** the problem if it terminates on every input in its specified domain and returns the correct answer.

A **recognizer** for a language must halt and accept every member of that language; for a nonmember, it may halt and reject or run without termination. A **decider** must halt with a correct yes/no answer on both members and nonmembers. Hence **recognizable** does not automatically mean **decidable**. A bounded implementation that halts after a timeout has not thereby solved the original unbounded decision problem.

For an infinite class of inputs, observing success on a finite sample is not a proof that an algorithm halts correctly for all inputs. Correctness and termination require appropriate justification under the model.

## Worked example: finite graph reachability is decidable

Let a finite directed graph have vertices `S={A,B,C,D}` and edges `A→B`, `B→C`, and `D→A`. The question is: **Is C reachable from A?**

A breadth-first or depth-first traversal can systematically visit each reachable vertex while marking already visited vertices. In this example:

```text
Start: A
Visit B from A
Visit C from B
Answer: YES
```

If there are finitely many explicitly represented vertices, the traversal can mark each vertex at most once, so it terminates after a finite number of relevant steps. It returns YES upon reaching C, or NO when no unexplored reachable vertex remains.

This establishes decidability of the **well-defined finite explicit-graph reachability problem**. It does not assert that every reachability question over infinitely many states or arbitrary program behavior is decidable. [Graph Theory](../mathematics-logic/graph-theory.md) owns formal graph structures and [Algorithms](algorithms.md) owns the general procedure contract.

## The halting problem and its limitation

The general **halting problem** asks whether an arbitrary encoded program terminates on a specified input. For a Turing-complete computational model with a suitable effective encoding of programs, no total algorithm correctly decides this for every possible program/input pair.

The standard diagonal argument considers a hypothetical total decider `H(P,x)` that correctly says whether program `P` halts on input `x`. Construct a program `D(P)` that **loops forever if H(P,P) says HALTS, and halts if H(P,P) says DOES NOT HALT**. Asking what `D(D)` does produces a contradiction with the assumed correctness of H. Thus such a universal decider cannot exist under the formal premises.

This result **does not** mean every individual program's termination is unknowable. Specific programs or restricted classes can admit termination proofs. Nor does it mean humans can automatically solve every case that machines cannot.

## Reductions and relative difficulty

A **reduction** transforms instances of one problem into instances of another while preserving the relevant answer under a declared mapping. It can help show that solving one problem would yield a solution to another.

Reduction type matters: many-one computable reductions, polynomial-time reductions and other notions support different conclusions. An **undecidability** argument and an **intractability** argument are not the same. A computable problem may still require impractical resources under available algorithms.

[Complexity](complexity.md) owns asymptotic resource requirements for computations; [Algorithm Design](algorithm-design.md) owns constructive strategies and proof obligations. They should not be conflated with existence/nonexistence of a decider.

## Scope and limitations

Computability does not guarantee the physical executability of arbitrary computations in finite equipment, the truth of the input representation, or meaningful interpretation of a program's output. A mathematical algorithm can be perfectly defined and still be practically unusable due to memory, time or physical constraints.

This article does not settle G-06 artificial intelligence/machine learning scope, prescribe a particular programming language, or introduce a new approved theoretical category.

### Sources

- [MIT OCW 6.045J: Automata, Computability and Complexity](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/).
- [MIT OCW 6.045J: Lecture Notes](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/).
- [MIT 6.045J: Lecture 6, Turing Machines and the Halting Problem](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/d6c18e634cdf3363ecac909bd2958b8b_MIT6_045JS11_lec06.pdf).
- [Stanford Encyclopedia of Philosophy: Turing Machines](https://plato.stanford.edu/entries/turing-machine/).

**Editorial status:** Substantive Draft. Formal statements, the diagonal argument and finite-graph example require a separate scoped technical audit. No Knowledge Checks or Practical Assessments are included.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
