# Programming Languages

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Programming languages  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Software Batches 03–04 audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md); independent human review pending

## Languages specify how programs can be expressed and interpreted

A **programming language** is a defined system for representing computational instructions, relationships, or declarations, together with rules for constructing valid programs and determining their meaning. A programming language can be used to express algorithms, configure systems, model data, build interfaces, and describe long-running behavior.

A language is not the same thing as a compiler, runtime, editor, processor, or programming paradigm. Implementations and tools may support multiple languages, and a language can have different conforming implementations under its specification.

The [MIT Computer Language Engineering course](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/) distinguishes language specifications from parsers, semantic checking, intermediate representations and code generation. [Algorithms](../computation-algorithms/algorithms.md) owns general computational procedures; this reference owns language-level expression and interpretation.

## Syntax, semantics and execution context

A language specification may establish **lexical rules**, **grammar**, **typing constraints**, **evaluation or execution semantics**, and mechanisms for names, values, scope and effects. These aspects answer different questions:

| Aspect | Question |
| --- | --- |
| Lexical and grammatical syntax | Which sequences of symbols are valid language forms? |
| Static semantics or checking | Which forms satisfy constraints before execution, where applicable? |
| Dynamic semantics | What behavior or result does a valid form express when evaluated? |
| Runtime context | Which values, resources, permissions and external operations are available? |

A program can be syntactically valid and still violate type restrictions, refer to an undefined name, encounter a runtime error or produce an outcome that does not satisfy its intended requirements. Syntax conformance is not evidence of correctness.

[Syntax and Semantics](syntax-and-semantics.md) owns formal construction and meaning rules. [Runtime Environments](runtime-environments.md) owns implementation context.

## Types, values, names and scope

Language **types** constrain values and operations under a chosen type system. An identifier binds a name to a declaration, value, location or other entity depending on language rules. **Scope** defines where the binding can be referenced, while **lifetime** describes how long the associated entity exists in the relevant execution model.

These are related but independent. A variable's name may no longer be in scope while an object it once referenced remains alive. Conversely, a name may still be lexically in scope when accessing the object violates a runtime condition.

**Static checking** can reject selected invalid constructions before execution, while **dynamic checking** detects selected violations during evaluation. The presence of either mechanism does not prove a program is free of every defect.

[Data Types](../information-data/data-types.md) owns general value domains; language-specific type systems extend those concepts under their own rules. [MIT Software Construction: Static Checking](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/01-static-checking/) illustrates the distinction.

## Worked example: same symbols, different operations

Consider the tokens `1`, `+`, and `2`. In a hypothetical numeric-expression language where `+` denotes integer addition, `1+2` evaluates to 3. In a language where the operands are **text strings** and `+` denotes concatenation, `"1"+"2"` evaluates to `"12"`.

The visible plus character does not decide its meaning independently of operand types, grammar and language semantics. Even within one language, operator behavior can depend on types or overload resolution. A calculator display showing `12` does not establish that a numerical addition occurred.

The examples are invented language contracts, not assertions that every mainstream language uses the same operator or conversion rules.

## Language design and tradeoffs

Different languages offer different mechanisms for representing mutable state, functions, objects, errors, concurrency, modules and type contracts. Expressiveness, predictability, readability, interoperability, safety and performance may motivate design choices, but **no language is universally superior**.

A language can support multiple paradigms, and choosing one language does not determine the program's architecture. Safety properties often depend on a combination of language semantics, implementation correctness, libraries, external inputs and development practice.

[Programming Paradigms](programming-paradigms.md) owns alternative styles of structuring computation, while [Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns measured performance objectives.

## Specification versus implementation

A compiler or interpreter attempts to implement a language's required semantics under its version and documented extensions. A program that runs successfully in one implementation may rely on implementation-defined behavior, unavailable libraries or operating-system resources.

Languages can use source-to-source compilation, bytecode, virtual machines, native code generation, interpretation or combinations. These choices are not part of a universal language-versus-language hierarchy. [Compilation and Interpretation](compilation-and-interpretation.md) owns transformation and execution mechanisms, and [Software Interfaces](software-interfaces.md) owns contracts exposed between software elements.

## Canonical boundaries

Programming languages is a domain-agnostic subject, not a recommendation to adopt a particular language, package manager or vendor tool. [Symbols and Encoding](../information-data/symbols-and-encoding.md) retains general symbol-representation ownership; [Computability](../computation-algorithms/computability.md) retains effective-calculation limits.

No new programming-language taxonomy, learner assessment or implementation mandate is introduced.

### Sources

- [MIT 6.035: Computer Language Engineering](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/).
- [MIT 6.005: Software Construction, Static Checking](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/01-static-checking/).
- [MIT 6.005: Software Construction Readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).

**Editorial status:** Reviewed (model-assisted) after the scoped [Wave D Software 54-family audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md). Complete source verification, independent expert review and final publication acceptance remain separate outstanding gates.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
