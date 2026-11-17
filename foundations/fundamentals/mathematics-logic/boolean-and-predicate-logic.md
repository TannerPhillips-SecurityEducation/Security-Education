# Boolean and Predicate Logic

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Boolean and predicate logic  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending

## Logic as a discipline of valid reasoning

Logic studies the structures that make conclusions follow from premises. In formal logic, a language specifies expressions, a semantics specifies their interpretations and truth conditions, and a proof system may specify which conclusions can be derived through formal rules. The existence of these multiple layers matters: a syntactically valid expression may be false under an interpretation, and an argument can be logically valid even when its premises happen to be false.

The discussion here concerns **classical two-valued propositional and first-order logic**, not every possible logic. Other systems, including many-valued, temporal, modal and non-classical logics, can use different assumptions. The [Stanford Encyclopedia of Philosophy's Classical Logic](https://plato.stanford.edu/entries/logic-classical/) describes these formal-language and semantic distinctions.

## Boolean logic and propositional operations

A **proposition** is a truth-evaluable statement within a chosen interpretation. In classical propositional logic, the truth values are conventionally **True** and **False**. Logical operators combine truth values according to rules.

| Operator | Notation | When the compound is true |
| --- | --- | --- |
| NOT | `¬P` | When P is false |
| AND | `P ∧ Q` | When both P and Q are true |
| OR (inclusive) | `P ∨ Q` | When at least one is true |
| Conditional | `P → Q` | Unless P is true and Q false |
| Biconditional | `P ↔ Q` | When P and Q have the same truth value |

For example, the conditional `P → Q` in **material implication** is not a claim of physical causation. It is logically false only when P is true and Q is false. A system designer must not read a formal conditional as proof that P *causes* Q.

For `P = True` and `Q = False`, `P ∧ Q = False`, `P ∨ Q = True`, and `P → Q = False`. A **truth table** can enumerate all input combinations for a finite propositional formula.

### Logical equivalence and implication

Two propositional formulas are **logically equivalent** when they have equal truth values under every relevant interpretation. One example is De Morgan's law:

```text
¬(P ∧ Q)  ≡  (¬P ∨ ¬Q)
```

This is stronger than agreement in one observed case. Similarly, `P ∧ Q` logically entails `P`: no truth assignment making the premise true can make the conclusion false.

The symbols `→` and `⊨` distinguish a formula's material conditional from the **meta-level consequence relation**. Written `Γ ⊨ φ`, semantic consequence means every model making all premises in Γ true also makes φ true. The [SEP entry on Logical Consequence](https://plato.stanford.edu/entries/logical-consequence/) explains this model-theoretic preservation criterion and its differences from ordinary causal or statistical inference.

## Predicates and quantification

Propositional logic can represent combinations of whole statements, but it does not express their internal object-and-property structure. **First-order predicate logic** introduces a domain of discourse, variables, predicates, quantifiers and often function and identity symbols.

For a domain of modeled devices, `Connected(x)` is a predicate that may be true of some devices and false of others.

- **Universal quantification:** `∀x Connected(x)` says every element in the relevant domain satisfies the predicate.
- **Existential quantification:** `∃x Connected(x)` says at least one relevant element satisfies it.
- **Negated universal:** `¬∀x Connected(x)` means not every element satisfies it, classically equivalent to `∃x ¬Connected(x)`.

The selected **domain** is essential. Standard classical first-order interpretations ordinarily use a **nonempty domain**. If a quantifier ranges over a set of devices, it does not automatically assert anything about every device anywhere in the world. Domain selection is part of the model's assumptions. In alternative formalisms allowing empty domains, some quantifier behavior and logical theorems require explicit qualification.

Consider the formula `∀x (Heater(x) → HasPowerSource(x))`. It represents a general modeled property of heaters. It says nothing about whether the modeled world satisfies that property until the predicates and domain are interpreted. A **counterexample** is any element for which `Heater(x)` is true and `HasPowerSource(x)` false.

This shows the distinction between logical form and empirical truth: first-order logic provides a way to express and assess consequences of assumptions, not a mechanism for independently checking the physical world.

## Syntax, semantics, proof, and validity

**Syntax** concerns formation rules for expressions. **Semantics** gives those expressions interpretations in models. A **proof** is a sequence of justified formal steps within a specified deductive system. An argument is **semantically valid** when its conclusion is true in every model where its premises are true.

A proof system is **sound** with respect to a semantics if provability implies semantic validity. It is **complete** with respect to that semantics if semantic validity implies provability. The precise theorems depend on the logic and proof calculus; completeness should not be presumed for arbitrary logics. These distinctions are developed in [Classical Logic](https://plato.stanford.edu/entries/logic-classical/) and [Logical Consequence](https://plato.stanford.edu/entries/logical-consequence/).

Neither **logical validity** nor an internally correct proof guarantees that the premises correspond to real-world facts. Conversely, valid inference does not require that the premises actually be true: it preserves truth conditionally.

## The limits of Boolean truth

Classical logic assumes well-defined propositions with two truth values. Real data may be missing, delayed, disputed, noisy or inaccessible. That operational uncertainty does not itself require replacing a two-valued logical language with a new logic. One may instead model uncertainty about which proposition is true. In other settings, multi-valued or partial logics may be appropriate, but those are different frameworks that require explicit semantics.

This distinction prevents three common conflations:

**Truth versus knowledge:** a statement may be true without an observer knowing it.

**Logical implication versus cause:** `P → Q` does not establish a mechanism causing Q. The converse `Q → P` is not established by `P → Q`, nor does the observation of Q justify inferring P.

**Formal validity versus implementation:** a valid Boolean formula does not determine whether electronic gates, software conditions or distributed messages evaluate it correctly.

The abstract mathematical operators belong here; [Digital Logic](../digital-systems-hardware/digital-logic.md) develops their electronic realization, while [Software & Programming](../software-programming/README.md) develops language-specific semantics.

## Example: a conditional requirement

Suppose a system specification contains these statements:

```text
P:  A request has been accepted.
Q:  A confirmation is generated.
Requirement: P → Q
```

The implication constrains the permitted combinations of P and Q in a model. Observing `Q = True` does not establish that P was true, because the implication is also true when P is false. Inferring P from Q would commit **affirming the consequent**. Moreover, the implementation must separately define what counts as acceptance, confirmation and the timing of each observation.

This example illustrates logic without turning it into a security-specific detection rule or an assessment.

## Relationships and references

[Sets and Relations](sets-and-relations.md) supplies formal domains and relations; [Entities and Attributes](../models-abstraction/entities-and-attributes.md) supplies modeling of objects and properties; [Digital Logic](../digital-systems-hardware/digital-logic.md) illustrates a hardware implementation.

### Authoritative reference starting points

- [Stanford Encyclopedia of Philosophy: Classical Logic](https://plato.stanford.edu/entries/logic-classical/), formal languages, classical semantics, quantifiers and proof.
- [Stanford Encyclopedia of Philosophy: Logical Consequence](https://plato.stanford.edu/entries/logical-consequence/), validity, consequence and model-theoretic interpretation.
- [Stanford Encyclopedia of Philosophy: Quantifiers and Quantification](https://plato.stanford.edu/entries/quantification/), first-order quantification and interpretation.
- [MIT OpenCourseWare: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), mathematical proof techniques and logical notation.

**Editorial state:** A substantive authoring draft. The material conditional, De Morgan identity, basic entailment and quantified predicate example have been checked against the cited classical-logic references and exhaustive finite truth assignments. Final scoped technical and editorial acceptance is recorded separately in the Wave A review ledger.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md)
