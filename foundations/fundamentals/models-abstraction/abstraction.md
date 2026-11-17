# Abstraction

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Abstraction  
**Development status:** Reviewed (model-assisted; independent expert acceptance pending)  
**Source review:** Core claims checked in [Wave A Batch 05 audit](../WAVE-A-TECHNICAL-REVIEW-05.md); not independently human verified

## Abstraction chooses which differences matter

**Abstraction** is the deliberate selection of aspects of a subject, structure, behavior, or phenomenon for a particular model or purpose while omitting or suppressing other detail. An abstraction is therefore not merely a shortened description. It is a decision about **which distinctions the explanation needs to preserve**.

Consider one physical device. A mechanical model might represent mass and dimensions, an electrical model might represent voltage and current, and a service model might represent availability. All can concern the same device, yet each selects a different portion of its properties.

The model is not automatically wrong because it ignores properties. It becomes misleading when it omits differences that matter to the **question being answered**, or when its assumptions are forgotten as conclusions are extended beyond its legitimate scope.

The [Stanford Encyclopedia of Philosophy: Models in Science](https://plato.stanford.edu/entries/models-science/) discusses representation, abstraction and idealization, including how a model selects aspects of a target system and can intentionally simplify or distort them. The present article uses that perspective to explain abstraction across technical systems without making a particular scientific or computing technology its organizing principle.

## Target, selection, representation, and interpretation

An abstraction can be described through four conceptual elements:

| Element | Function |
| --- | --- |
| **Target** | The subject, system, phenomenon, or conceptual structure being modeled |
| **Selection** | The properties and distinctions retained for the question |
| **Representation** | The chosen symbols, mathematical structures, categories, diagrams, or other forms |
| **Interpretation** | The meaning and limits of claims made using that representation |

These elements describe an **analytical process**, not a mandatory four-field schema.

For example, a communication system might be represented as a graph in which devices become vertices and links become edges. That abstraction deliberately omits wire shape, connector color, packet content and many timing details. It may be useful for understanding connectivity while remaining insufficient for predicting delay, failure probability or physical energy use.

The abstraction does not prove that an edge exists: the edge is a **modeled assertion** whose basis must come from observation, specification, or evidence. See [Graph Theory](../mathematics-logic/graph-theory.md), [Observation](../scientific-analytical-reasoning/observation.md), and [Evidence](../scientific-analytical-reasoning/evidence.md).

## Levels of abstraction

One subject can be described at multiple **levels of abstraction**, each preserving different structures and operations.

Consider an instrumented heating device:

```text
Physical view
  Sensor, conductor, controller, heater, thermal environment
        ↓
Functional view
  Sense temperature, compare set point, regulate heating
        ↓
State view
  IDLE, HEATING, FAULT
        ↓
Service view
  Requested temperature maintained / not maintained
```

These are alternative **views**, not necessarily a literal sequence in which the physical world is transformed. Higher-level views suppress details, but may introduce additional concepts and assumptions. An abstract system state such as `HEATING` can cover many different physical states.

A level is not automatically more accurate, more useful, or more general than another. Its suitability depends on the question. Hardware defects may require a physical view; a scheduling analysis may need execution states; a user experience review may concern whether a service fulfills its intended function.

The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) discusses whole-system perspectives, decomposition and functional analysis. Their role here is to illustrate why multiple representations of one system can be legitimate without collapsing them into the same description.

## Abstraction versus idealization

**Abstraction**, in one common scientific-philosophy distinction, leaves selected characteristics unspecified so attention can focus on what matters. **Idealization** introduces a deliberately simplified or sometimes counterfactual assumption to make analysis tractable.

Examples:

- An abstraction of a vehicle's movement may retain position and velocity while omitting its paint color.
- An idealized motion model may assume no friction even when the physical surface has some friction.
- A thermal model may treat a component as one uniform temperature, although real internal gradients exist.

The [SEP Models in Science](https://plato.stanford.edu/entries/models-science/) notes that the boundaries between abstraction and idealization are debated. Thus, the distinction above is a **useful working convention**, not a universally agreed categorical law.

A model that omits a fact and a model that asserts a simplifying falsehood can behave differently. Each requires explicit assumptions and a decision about whether its approximations matter for the intended claim.

## Abstraction versus generalization, classification, and encapsulation

Related concepts perform different operations.

**Generalization** identifies patterns or characteristics shared across selected instances. It moves from specific descriptions toward common statements. Such generalization can be empirically uncertain, and it does not follow deductively merely because several cases look alike.

**Classification** places entities into groups under specified criteria. It may use an abstraction, such as selected attributes, but its principal concern is **category membership**.

**Encapsulation** separates implementation details behind an interface or boundary, especially in software and system architecture. It can implement an abstraction without being identical to the general intellectual process of abstraction.

**Aggregation** combines several elements or values into a collection or summary. Aggregation may intentionally lose detail, but summarizing items numerically is a different mechanism from specifying a concept or model of their relevant behavior.

For example, computing the average temperature of a room is an **aggregation** of measurements; using that value as the state of the entire room is a **modeling abstraction** with spatial and temporal assumptions. The result could be inadequate if local hotspots matter.

These distinctions preserve canonical ownership: [Classification](README.md) and [Schemas](README.md) concern model organization, [Data Structures and Formats](../information-data/README.md) concerns representations, and [Software & Programming](../software-programming/README.md) concerns specific implementation techniques.

## Mapping concrete states into abstract states

A more formal abstraction may map a detailed **concrete** state space to a simpler **abstract** state space. Let `S_c` be a set of detailed modeled states and `S_a` a set of abstract states. One possible representation is a function

```text
α : S_c → S_a
```

can assign an abstract description to each concrete state.

Suppose a thermometer produces a measured value `t` in °C and a model uses only three categories:

```text
α(t) =
    LOW      if t < 18
    NORMAL   if 18 ≤ t < 30
    HIGH     if t ≥ 30
```

Under the stated model, `α(21.0)=NORMAL` and `α(28.9)=NORMAL`. These two distinct measurements map to the same abstract state. The mapping is **many-to-one**, so the original measurement cannot generally be recovered from the category alone.

The boundaries `18` and `30` are **chosen thresholds**, not discovered universal laws. The model must specify how missing readings, instrument uncertainty, and values outside validated operating ranges are handled. Those concerns belong in [Boundaries](boundaries.md), [Measurement](../scientific-analytical-reasoning/measurement.md), and [State, Events, and Transitions](state-events-and-transitions.md).

## Abstraction can lose constraints as well as details

Depending on how abstract transitions are defined, suppressing distinctions can create a model that admits behaviors not possible for the underlying detailed system. A many-to-one state mapping **alone** does not establish that the resulting transition model is a sound over-approximation. For example, two concrete states may both map to the abstract state `READY`, although only one can begin an operation. A coarse abstract transition `READY → ACTIVE` does not guarantee that every concrete state represented by READY can execute it.

The reverse problem also exists: if a model fails to include a real possible transition, it can mistakenly exclude a behavior that the actual system can exhibit.

Formal analysis distinguishes **over-approximations**, which may include extra abstract behaviors, from **under-approximations**, which may omit actual behaviors. A correct verification argument must state how abstract and concrete behaviors correspond. The exact soundness requirements depend on the purpose and formalism.

The [MIT Mathematics for Computer Science course](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) includes state machines and invariant reasoning that help explain why proving a property of one chosen model is not identical to validating a physical implementation.

## A worked example: simplifying a telemetry record

Imagine a detailed observation record:

```text
sensor = s17
observed_time = 14:03:12
reported_value = 31.2
unit = °C
calibration_version = v3
measurement_uncertainty = 0.8 °C
quality = valid
```

A reporting view might retain only:

```text
sensor = s17
state = HIGH
```

The simplified record is useful for a high-level presentation. Yet it loses the measured value, timing context, calibration version and stated uncertainty. If a later decision requires knowing whether the physical temperature was **certainly** above 30 °C, the abstract state alone is insufficient.

The appropriate resolution may be to link the abstract result back to its detailed evidence rather than pretend the report retained information it discarded. This is a design choice about **traceability and reversibility**, not a claim that all abstractions must store every original detail.

## Choosing a defensible abstraction

A technical reference can judge an abstraction by asking whether it preserves the properties necessary for its purpose:

- Does it identify the **target** and the selected scope?
- Which important properties, relationships and distinctions are **preserved or omitted**?
- Are transformations or category boundaries **defined**?
- Does it retain enough context to distinguish **observed facts** from **model assumptions**?
- Can a result be related to more detailed supporting evidence when needed?
- Is a conclusion **limited to the circumstances** under which the abstraction is defensible?

These are **editorial inspection criteria**, not questions for learners or a testing platform. They guide responsible source-authoring and model construction.

An abstraction is useful precisely because it simplifies, but its omissions must be made intellectually visible.

## Canonical relationships and references

[Entities and Attributes](entities-and-attributes.md) supplies the modeled subjects and properties; [Identity and Distinction](identity-and-distinction.md) supplies criteria for sameness; [Relationships](relationships.md) supplies association; [Boundaries](boundaries.md) supplies separation and limitation; [Graph Theory](../mathematics-logic/graph-theory.md) supplies one abstract structural representation.

### Sources

- [Stanford Encyclopedia of Philosophy: Models in Science](https://plato.stanford.edu/entries/models-science/), abstraction, idealization, representation and model-target correspondence.
- [NASA Systems Engineering Handbook: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/), system-level perspectives and functional/physical decomposition.
- [MIT Mathematics for Computer Science, 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), discrete state modeling and invariants.

**Editorial review note:** Checked model/target, abstraction/idealization, and the many-to-one mapping examples against SEP's science-model account and independently evaluated threshold cases. Added a qualification: a many-to-one abstraction is not automatically a sound over-approximation without a suitable transition relation. This is a model-assisted scoped review, not independent human publication acceptance.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
