# Software Interfaces

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Software interfaces  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical/source review pending

## Software interfaces specify observable contracts

A **software interface** defines how a consumer can interact with a software component under a stated contract: permitted operations, inputs, results, effects, constraints, errors and sometimes ordering or timing. An interface is not merely a function name, method signature, network endpoint or collection of fields.

An interface can exist between functions, modules, libraries, programs, services, language runtimes and other software elements. Its meaning depends on the context and execution model. [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns general systems contracts; this article owns **software-facing interfaces and their semantics**.

The [MIT Software Construction material on specifications and interfaces](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/) distinguishes declared behavior, abstraction boundaries and representation independence.

## Precondition, postcondition and side effects

A **precondition** states what the caller must establish before an operation can be relied upon to fulfill a contract. A **postcondition** states what the operation promises if invoked under its precondition and any stated execution/failure conditions. Side effects describe changes to external or shared state.

A contract should identify whether an operation can change its arguments, mutate shared state, perform I/O, emit events, allocate resources or fail. A return value alone can omit consequential behavior.

For a function called `convert_temperature`, the type signature `number → number` does not specify the unit, domain or conversion relationship. Two implementations might agree syntactically while disagreeing on meaning.

## Worked example: a unit-sensitive contract

Consider this illustrative contract:

```text
Operation: fahrenheit_to_celsius
Input: finite numeric value representing °F
Output: numeric value representing °C
Postcondition: result = (input − 32) × 5/9
Side effects: none in this toy specification
```

For input `68`, the required output is `(68−32)×5/9 = 20`. A function returning `68` might satisfy a broad numeric output type but violates the declared conversion postcondition.

A caller that supplies `68 °C` while treating it as `68 °F` violates the input meaning, even if the program computes the stipulated numeric formula flawlessly. Unit semantics and the source of values matter.

This example does not claim a particular language's floating-point implementation returns the exact mathematical real number for every input; numerical accuracy and rounding conditions require separate specification.

[Units and Quantities](../mathematics-logic/units-and-quantities.md) owns quantity conversions and [Data Types](../information-data/data-types.md) owns value-domain interpretation.

## Interface versus implementation

Different implementations can provide equivalent observable behavior under a given interface, despite using different algorithms or data representations. **Representation independence** depends on which distinctions are observable to clients and on whether implementations uphold the contract.

For example, a set interface might expose add, remove and contains operations. A hash table and balanced tree can implement them under compatible value semantics while differing in ordering, performance and failure characteristics. If the client contract promises sorted iteration, unordered iteration may violate the interface.

[Computational Data Structures](../computation-algorithms/computational-data-structures.md) owns operation costs and representation invariants; interface equivalence is a contract question, not merely a type-name match.

## Exceptions, failures and asynchronous effects

An operation can return a result, reject a request, signal an exception, time out or initiate work that completes later. The interface contract must distinguish an accepted request from completed and persisted effects when those states matter.

A retry is safe only relative to the operation's semantics. An idempotent operation under a defined model has the same intended state effect when repeated, but network failures, external side effects and poor deduplication can complicate a real implementation.

[Error Handling](error-handling.md) owns the software response to failures; [Communication & Distributed Systems](../communication-distributed-systems/README.md) owns partial failures, messages and delivery semantics across independent nodes.

## Compatibility and evolution

Changing an interface can break consumers through altered names, types, result conventions, side effects, error codes, ordering, performance, or permission requirements. Version numbering can help communicate intended compatibility but does not prove it.

**Backward compatibility** must be defined relative to earlier consumers and the aspects of behavior they depend upon. Adding an optional field might still fail clients that reject unknown fields. Removing a field might be safe for a subset of consumers that never used it.

[Modules and Dependencies](modules-and-dependencies.md) owns dependency declarations and version constraints, while [Testing and Software Lifecycle](testing-and-software-lifecycle.md) owns verifying change effects over time.

## Canonical boundaries

This article does not require a particular API specification, language interface mechanism, RPC scheme, HTTP convention or software platform. Domain-specific network or cloud APIs extend these general interfaces within specialized knowledge areas.

### Sources

- [MIT 6.005: Specifications and Interfaces](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.005: Specifications, Preconditions and Postconditions](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/).
- [MIT 6.005: Interfaces](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/14-interfaces/index.html).
- [MIT 6.005: Abstraction and Representation Independence](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/12-abstract-data-types/).
- [NASA: Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).

**Editorial status:** Substantive Draft. The unit-conversion contract and compatibility discussion require a separately documented technical/source review. No assessments or mandated API conventions are introduced.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
