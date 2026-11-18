# Artificial Intelligence Foundations

**Knowledge area:** [Computation & Algorithms](README.md)  
**Subject ID:** F-07-10  
**Development status:** Reviewed (model-assisted; independent human acceptance not claimed)  
**Source review:** Core claims checked; [Wave F 42-family scoped technical audit](../WAVE-F-TECHNICAL-REVIEW-01.md); comprehensive source-level verification not claimed  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Artificial intelligence concerns computational agency, reasoning and problem solving

**Artificial intelligence (AI)** is a broad discipline concerned with designing and understanding computational systems that perform tasks requiring representations, inference, search, planning, perception, learning or context-sensitive decisions under a chosen account of intelligent behavior. There is no single algorithm or universal formal definition covering every AI system. An automated process is not necessarily intelligent, and an AI system need not use a neural network or learn from data.

A common explanatory model is an **agent** interacting with an environment. An agent receives percepts or information, maintains or computes a representation as needed, and selects actions or outputs according to objectives, policies and constraints. An agent model is a useful abstraction, not a claim that the implementation has consciousness, intentions or subjective experience.

[Algorithms](algorithms.md) owns algorithms in general; this subject owns the **AI-specific framing of representation, goals, agents, search, reasoning and planning**. [Machine Learning Foundations](machine-learning-foundations.md) owns mechanisms for fitting or adapting models from data. AI includes methods that do not involve machine learning.

## Agents, environments and objectives

An **agent function** maps percept histories or represented observations to actions. A program implements some approximation or realization of that function using memory, rules, optimization, learned models or other procedures. A **policy** maps states or observations to actions under a specified model. Goals, rewards, utilities, safety constraints and task specifications are related but not interchangeable.

A **fully observable** model assumes relevant state information is available to the agent at decision time; **partial observability** requires decisions under incomplete state knowledge. Deterministic versus stochastic transitions and single-agent versus multi-agent conditions introduce other distinctions.

Choosing an action that is optimal *under a model* does not prove that the action is optimal in reality. A decision rule depends on the quality of the world model, accessible information, available actions, and what the stated objective values or excludes.

## State-space search

A **search problem** usually identifies an initial state, legal actions or successors, a goal condition and sometimes a path cost. **Breadth-first search (BFS)** explores by edge depth and finds a shortest-number-of-edges path in an unweighted graph under its usual finite, unit-cost conditions. **Uniform-cost search** instead explores by accumulated nonnegative path cost and can find a least-cost path when its technical conditions hold.

Heuristic search estimates remaining cost or desirability. **A*** combines accumulated path cost with a heuristic estimate; optimality and efficiency guarantees require conditions such as admissibility and, for common graph-search implementations, consistency or suitable reopening behavior. Naming a heuristic does not demonstrate its reliability.

Search algorithms use representations; they do not automatically prove that an actual environment is faithfully modeled or that a plan remains executable when conditions change.

## Knowledge representation and inference

**Knowledge representation** specifies how propositions, entities, relationships, rules, uncertainty and constraints are encoded for computation. Symbolic representations can use propositional or predicate logic, rule systems, semantic graphs or constraint satisfaction formulations. Probabilistic representations can instead express uncertain dependencies and update beliefs under a chosen probability model.

A valid deduction follows from its premises under a chosen logic. A plausible abductive explanation is not entailed merely because it fits observations. Probabilistic inference depends on specified distributions, evidence and modeling assumptions; it does not prove causation or an unobserved agent's intent.

**Constraint satisfaction** represents variables, domains and constraints. For instance, a scheduling problem can require that two tasks not use the same machine at overlapping times. Satisfying that logical constraint differs from finding a globally optimal schedule under an additional cost objective.

## Planning and sequential decision processes

**Planning** models actions together with preconditions and effects, then searches for a sequence or policy expected to reach a goal. A plan is conditional on the model's state, admissible actions and dynamics. When the environment changes, a valid plan may become invalid.

A **Markov decision process (MDP)** is a formal sequential decision model with states, actions, transition probabilities, rewards and a criterion such as expected cumulative discounted reward. Its Markov assumption says that the chosen state representation is sufficient to specify the future transition distribution given the current action. This is a modeling assumption, not a guaranteed property of arbitrary observations. **Partially observable MDPs** add a model of hidden state and observations.

Reinforcement learning can learn action-selection policies or values from experience in such environments, but planning with a known transition model does not inherently require learning.

## Worked example: cheapest path differs from fewest edges

Suppose a graph contains four nodes with the following directed, nonnegative weighted edges:

```text
A → B : cost 1
B → G : cost 5
A → C : cost 2
C → G : cost 2
```

There are two displayed two-edge paths from A to goal G. Their costs are:

```text
A → B → G : 1 + 5 = 6
A → C → G : 2 + 2 = 4
```

BFS treats both paths as depth two and may return the first one discovered, depending on successor order. It does not guarantee a minimum **weighted** cost here. Uniform-cost search using nonnegative edge costs returns the cost-4 route in this finite example.

**What the example establishes:** An agent's objective and the chosen search strategy determine which path is preferable. **What it does not establish:** That the modeled costs accurately represent real-world distance, energy, reliability or harm. The edge costs were stipulated, not observed measurements.

## Limits, evaluation and human impact

AI system evaluation must reflect the **task**, conditions, operating constraints and error consequences. Winning a board game, predicting labels, following a planning model and producing coherent text are different capabilities; success at one does not prove general-purpose competence or reliability in another.

Model errors, missing observations, distribution changes, unsafe objectives, unrepresentative data and feedback loops may lead to harmful outcomes. Safety, transparency, accountability and responsible use require further sociotechnical treatment. A system's human-like output is not proof of grounded understanding, self-awareness or factual accuracy.

The term **generative AI** describes systems that produce new content according to learned or specified representations; it is not an alternative name for all of AI. Neither AI nor ML is synonymous with a particular technology vendor.

## Canonical relationships and sources

- [Machine Learning Foundations](machine-learning-foundations.md) owns learning algorithms, training, inference, model generalization and dataset-dependent evaluation.
- [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns probabilistic foundations; [Boolean and Predicate Logic](../mathematics-logic/boolean-and-predicate-logic.md) owns formal logical inference.
- [Graph Theory](../mathematics-logic/graph-theory.md) supplies state and relation structures; [Algorithm Design](algorithm-design.md) owns general search and design methods.
- [Models & Abstraction](../models-abstraction/README.md) owns state, knowledge representations and model limitations at the domain-independent level.
- [Datasets, Records, Fields, and Values](../information-data/datasets-records-fields-and-values.md) owns data anatomy; [Human Cognition and Perception](../human-sociotechnical-systems/human-cognition-and-perception.md) owns distinct human capabilities rather than treating AI and human intelligence as identical.

### Authoritative reference starting points

- [MIT OpenCourseWare 6.034 Artificial Intelligence](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/), reasoning, search, problem solving, constraints and learning.
- [Stanford CS221 Artificial Intelligence: Principles and Techniques](https://bulletin-new.stanford.edu/courses/cs-221), search, logic, constraints, probabilistic models and sequential decisions.
- [CS2023 Artificial Intelligence knowledge area](https://csed.acm.org/knowledge-areas/), placement of AI in a recognized computing curriculum; this is source orientation, not an instruction to copy its taxonomy.

The search example and agent terminology illustrate computational models, not a universal operational definition of intelligence. Complete primary-source clause review, independent expert review and publication acceptance remain pending.

**Editorial status:** Reviewed (model-assisted) under the [Wave F scoped technical review](../WAVE-F-TECHNICAL-REVIEW-01.md). Full source-passage verification, independent expert review and final publication acceptance remain open.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
