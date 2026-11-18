# Syntax and Semantics

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Syntax and semantics  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Software Batches 03–04 audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md); independent human review pending

## A valid expression and its meaning are different claims

**Syntax** specifies how symbols can form well-structured expressions and programs in a language. **Semantics** specifies what those expressions mean or how their execution behaves under an interpretation. A syntactically valid sequence can have no meaningful result under a particular environment, while a malformed sequence can express an understandable human intention without being a valid program.

In programming, syntax and semantics are usually governed by a language specification. **Pragmatics** concerns how a language is used in context, including conventions, readability, tooling and purposes. This subject concentrates on programming-language rules without claiming to subsume the general Syntax/Semantics/Pragmatics distinction.

[Programming Languages](programming-languages.md) owns language identity and language-level capabilities. [Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns the wider model-versus-interpretation distinction.

## Tokens, grammars, and parse trees

A **token** is a language-recognized lexical unit, such as an identifier, number or operator, under an established tokenization rule. A **grammar** constrains how units can be combined. A **parse tree** records how a sequence matches grammar productions.

For example, a hypothetical expression grammar could be:

```text
Expr   ::= Term ("+" Term)*
Term   ::= Number ("*" Number)*
Number ::= one or more decimal digits
```

The structure gives multiplication a tighter grouping than addition. This is a simplified pedagogical grammar and does not describe every operator, sign, whitespace or grouping rule a real programming language requires.

A grammar can define multiple possible parses for the same token sequence. Such **ambiguity** must be resolved by a rule, parser design or deliberate semantics before evaluating an expression whose grouping affects the result.

[MIT 6.005: Regular Expressions and Grammars](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/17-regex-grammars/index.html) explains productions and parsing, while [MIT 6.035 compiler lectures](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/) describe lexical analysis, grammars and semantic checking.

## Worked example: grouping changes evaluation

Under ordinary exact integer addition and multiplication, evaluate `2+3*4`.

```text
Grammar above: 2 + (3 × 4) = 14
Alternative grouping: (2 + 3) × 4 = 20
```

The unparenthesized token sequence alone does not determine which result is intended in the absence of an agreed grammar and precedence convention. Once the grammar and value semantics are specified, the result is reproducible. Neither result is independently an observation of the physical world.

An abstract syntax tree (AST) can represent the essential structure `Add(2,Multiply(3,4))` without retaining every punctuation token or grammar-production detail. A parse tree and AST are different representations of related syntax.

## Static and dynamic semantics

**Static semantics** captures constraints checked without executing the program's full dynamic behavior, often including types, name binding or permitted operations. **Dynamic semantics** describes what execution or evaluation does: state transitions, values, effects, errors and termination under the chosen model.

A well-formed expression can fail static type checking, or pass static checks and still encounter an error during execution. Not every programming language has a static type checker, and “static” does not mean all relevant facts are knowable before execution.

**Operational semantics** can describe evaluation using transitions. **Denotational semantics** associates program constructs with mathematical meanings. **Axiomatic reasoning** characterizes properties through assertions or proof obligations. These are possible formal approaches; this article does not impose one as the canonical semantic representation of every language.

## Names, environments, and effects

The expression `x+1` might be syntactically valid but require a binding of `x` to a suitable value or location before evaluation. A function call can change state, perform I/O, throw an exception, or diverge rather than returning a value.

Environment, state, effects and evaluation order may affect semantics. One language can specify left-to-right evaluation, another can leave some order unspecified, and a restricted mathematical expression language might have no side effects to order.

[Runtime Environments](runtime-environments.md) owns the resources and execution context supporting actual evaluation. [Error Handling](error-handling.md) owns responses to failures and invalid operations.

## Meaning versus program intention

A program can be semantically correct under its language rules while failing the programmer's intended requirement. For example, computing the mean of **all** records can be a valid query but the intended objective may have been the mean **per device**.

Formal semantics describes what a program means under a specification, not automatically whether that behavior serves the human goal. [Requirements](../systems-engineering/requirements.md) owns specified system needs and [Verification and Validation](../systems-engineering/verification-and-validation.md) owns evaluating the implemented result.

## Scope and boundaries

This article owns programming syntax and semantics, not general natural-language linguistics, every formal model, or the mathematical theory of logic. [Boolean and Predicate Logic](../mathematics-logic/boolean-and-predicate-logic.md) owns logical operators and truth conditions generally, while [Algorithms](../computation-algorithms/algorithms.md) owns procedure correctness.

No particular parser generator, compiler framework, programming language or assessment is prescribed.

### Sources

- [MIT 6.005: Regular Expressions and Grammars](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/17-regex-grammars/index.html).
- [MIT 6.005: Parser Generators](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/18-parser-generators/index.html).
- [MIT 6.035: Computer Language Engineering Lecture Notes](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/).

**Editorial status:** Reviewed (model-assisted) after the scoped [Wave D Software 54-family audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md). Complete source verification, independent expert review and final publication acceptance remain separate outstanding gates.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
