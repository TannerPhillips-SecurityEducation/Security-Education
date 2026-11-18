# Conceptual and Formal Models

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Conceptual and formal models  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Batch 07 audit](../WAVE-A-TECHNICAL-REVIEW-07.md); no independent human peer review

## Models represent selected aspects of a target

A **model** is a purpose-dependent representation of some target, system, process or possible world. A **conceptual model** communicates selected entities, relationships, behavior or explanatory structure, often without a fully specified machine-checkable semantics. A **formal model** uses a defined language, mathematical structure or logic with rules for well-formed expressions and interpretation.

A model's usefulness depends on purpose and fidelity, not its complexity alone. A conceptual sketch can be more useful than a formal model for communicating scope; a formal model can make certain claims mechanically checkable that remain ambiguous in natural language. Neither is automatically a faithful account of reality.

[Abstraction](abstraction.md) owns selective omission and representation mappings. This article owns model classes, semantics, assumptions, formalization and interpretation. The [Stanford Encyclopedia of Philosophy: Models in Science](https://plato.stanford.edu/entries/models-science/) surveys multiple accounts of model–target relationships.

## Syntax, semantics, and interpretation

**Syntax** determines which statements are well formed within a modeling language. **Semantics** supplies interpretations or rules for what those statements mean. **Pragmatic use** concerns purposes, decisions, and consequences of applying the model.

For example, the expression `state ∈ {OFF, ON}` may be syntactically valid in a chosen notation. An interpretation connects `ON` to an operational state of a particular modeled device. Observational evidence is still needed to determine whether a real device matches the statement.

A model that is internally consistent can be **externally inaccurate**. A model that fits observed examples can also fail outside its tested scope. Both conditions must be distinguished.

## Formal transition-system example

Consider a simple transition system `M=(S,I,→,L)`, where:

- `S={OFF, ON}` is the set of states.
- `I={OFF}` is the set of initial states.
- `→={(OFF,ON),(ON,OFF)}` is the transition relation.
- `L` supplies propositions true at each state (for example, `powered` is true in `ON`).

This system allows alternation between OFF and ON on executions that follow the stated transitions. Because each state has one outgoing transition, this example admits infinite alternating executions. It does not specify how long transitions take, whether failures can occur, or what physical mechanisms drive the change. Those omissions are **model assumptions and limits**, not proof that the world behaves so simply.

We might add `(ON,ON)` to allow remaining ON for another step. The behavior set changes. Formal precision makes the change explicit, but empirical or design justification is still separate.

## Properties and proof obligations

A formal specification can state properties such as:

- **Safety:** A prohibited state or event never occurs within a stated model and its allowed executions.
- **Liveness:** Some desired progress eventually occurs, usually subject to fairness or environmental assumptions.
- **Invariant:** A predicate holds in all reachable states of the modeled transition system.

For the two-state example, `state ∈ {OFF,ON}` is an invariant by construction. A statement like `the modeled device never fails` does **not** follow from the formal system as a claim about real equipment: failure states were excluded from the model's state space, not proven physically impossible.

A proof or model-checking result is conditional on the formalized system, property, logic and tool correctness. Claims about implementation or reality require separately justified correspondence.

The [Stanford Encyclopedia of Philosophy: Formal Verification](https://plato.stanford.edu/entries/computer-science/#ForVer) and the [TLA+ resources](https://lamport.azurewebsites.net/tla/tla.html) illustrate distinct formal approaches. Neither is adopted as a mandatory project implementation.

## Abstraction mappings and preservation

Let `C` represent concrete states and `A` abstract states. An abstraction function `α:C→A` groups concrete states into abstract descriptions. The function can erase information without preserving every behavioral statement.

Consider concrete states `c1,c2,c3` and abstract states `NORMAL,ALERT` with `α(c1)=α(c2)=NORMAL` and `α(c3)=ALERT`. If `c2→c3` is possible, then a sound may-transition over-approximation should include `NORMAL→ALERT`, even if a modeler only observed transitions from `c1`. Omitting it could make a safety conclusion unsound.

This illustrates a **conditional modeling guarantee**, not a general theorem that every many-to-one map is sound. Preservation of properties depends on the definition of abstraction, transition correspondence, and the logical class of properties being analyzed. The [Abstraction](abstraction.md) reference owns the general selection mechanism.

## Conceptual, mathematical, and executable models

| Model style | Typical role | Limitation |
| --- | --- | --- |
| Conceptual map | Explain relevant concepts and relations | May leave semantics informal |
| Mathematical model | Define relations through equations or structures | Assumptions may not fit a target |
| State-transition model | Represent allowed state changes | May omit timing, concurrency or environment |
| Statistical model | Characterize distributions or inference | Sensitive to sampling and distributional assumptions |
| Executable simulation | Generate traces under implementation rules | Generated behavior is not independent confirmation of reality |

These are **illustrative forms**, not newly approved ontology classes. A model can combine several forms. Formality concerns precise syntax/semantics, while execution is a separate property; not all formal models are executable.

## Established modeling languages and behavioral formalisms

The language chosen to express a model is not the model's target or proof that the target behaves as described. Several established representations illustrate different modeling commitments:

| Representation | Basic structure and intended use | Boundary |
| --- | --- | --- |
| Finite-state transition system | A set of states, initial states and a transition relation; useful for reachability and invariant questions | State abstraction may omit time, probability and physically continuous behavior |
| Petri net | Places, transitions, directed arcs and token markings; useful for reasoning about concurrent enabling, firing and resource dependencies | A marking/firing rule needs explicit arc weights and firing semantics; it is not an empirical execution trace |
| UML | Object Management Group (OMG) Unified Modeling Language for selected software/system structural and behavioral views | A class diagram, activity diagram and state machine emphasize different information; drawing one does not establish correctness |
| SysML | OMG Systems Modeling Language for system requirements, structure and behavior across hardware, software and other system constituents | A SysML model is not automatically a verified implementation; version 1 and version 2 have substantially different language foundations |
| Formal specification / model checker | Formalized state and behavior plus properties checked under a chosen semantics | Model-checker success pertains to the model and checked properties, not all real-world behavior |

For a simple Petri net with one token in place READY, a transition can consume that token and produce one in DONE when enabled. This represents an ordering/resource condition distinct from a general finite-state-machine edge, but neither representation is intrinsically "more true" about a real process. The choice depends on the questions to be answered.

The OMG [UML 2.5.1 specification](https://www.omg.org/spec/UML/2.5.1/) defines one standardized modeling language. OMG [SysML documentation](https://www.omg.org/sysml/) reports both version 1 and the version 2 family, whose 2025 final adoption introduced KerML and systems-modeling API foundations. Not every SysML or UML diagram kind is a separate ontology or Fundamentals subject.

An **architectural view** is a representation selected to address specific concerns; a modeling language can express a view without determining the architecture itself. [Architecture and Composition](../systems-engineering/architecture-and-composition.md) owns the general architecture/description distinction, while [State, Events, and Transitions](state-events-and-transitions.md) owns state/event vocabulary. [Temporal Concepts and Models](temporal-concepts-and-models.md) owns general time and temporal-order descriptions.

## Verification versus empirical validation

**Formal verification** asks whether a property follows from a formal representation under declared assumptions. **Empirical validation** asks whether the representation or derived predictions are adequately supported for an intended real-world purpose. **Engineering verification and validation** evaluate requirements and intended use of an engineered system. These activities intersect but are not synonyms.

A verified model can accurately prove a property that is irrelevant to stakeholders. A statistically predictive model can perform usefully without providing a formal correctness proof. A functioning implementation can violate an abstract model because the correspondence assumptions were false.

[Validation and Falsification](../scientific-analytical-reasoning/validation-and-falsification.md) owns evidence-based criticism of empirical claims; [Systems & Engineering: Verification and Validation](../systems-engineering/verification-and-validation.md) owns engineered-product conformity and intended use; [Schemas](schemas.md) owns representation conformance.

## Boundaries and unresolved coverage

This article does not resolve general temporality [G-04](../COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks), the mathematical breadth decision G-01, or the AI/ML decision G-06. It introduces no mandated formal language, model checker, simulation engine, or additional subject heading.

### Sources

- [OMG: Unified Modeling Language 2.5.1 specification](https://www.omg.org/spec/UML/2.5.1/).
- [OMG: Systems Modeling Language and SysML v2](https://www.omg.org/sysml/).
- [MIT LCS: Petri Net definition and execution concepts](https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-094.pdf).


- [Stanford Encyclopedia of Philosophy: Models in Science](https://plato.stanford.edu/entries/models-science/).
- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- [Stanford Encyclopedia of Philosophy: Philosophy of Computer Science](https://plato.stanford.edu/entries/computer-science/).
- [TLA+ Home and Resources](https://lamport.azurewebsites.net/tla/tla.html).

**Editorial status:** Reviewed (model-assisted) following the [Batch 07 scoped 30-family technical review](../WAVE-A-TECHNICAL-REVIEW-07.md). Complete source verification, independent human peer review and final publication approval remain open.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
