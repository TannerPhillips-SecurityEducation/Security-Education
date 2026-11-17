# Graph Theory

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Graph theory  
**Development status:** Reviewed (model-assisted; independent expert acceptance pending)  
**Source review:** Core claims checked in [Wave A Batch 05 audit](../WAVE-A-TECHNICAL-REVIEW-05.md); not independently human verified

## Graphs describe objects and their connections

**Graph theory** studies mathematical structures consisting of vertices and edges. A **vertex** (or node) represents a distinguishable element of a chosen mathematical model. An **edge** represents a connection or relation between vertices under explicitly stated conventions.

A graph does not need to represent a computer network. The same mathematical structure can model a dependency, a family of related entities, an abstract route, a workflow, a communication pattern, or a system decomposition. Its structure is **separate from the real-world meaning** assigned to its vertices and edges.

A common undirected graph is expressed as `G = (V, E)`, where `V` is the vertex set and `E` is the edge set. For a **simple undirected graph**, each edge joins two *distinct* vertices, and at most one edge joins a given pair. Other graph classes allow loops, parallel edges, directed edges or weighted relationships. The model must say which class it is using.

The [MIT Mathematics for Computer Science course](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) covers graphs, coloring, connectivity, trees, and directed acyclic graphs. Its [course readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) separate graph structure from later computational uses.

## What vertices and edges can represent

Consider a simple undirected graph with

```text
V = {A, B, C, D}
E = {{A,B}, {B,C}, {A,C}, {C,D}}
```

A pair such as `{A,B}` is **unordered** in this undirected model. The edge connects A and B without assigning a direction. This **example graph** has four vertices and four edges. It is **not a complete graph**: a simple undirected complete graph on four vertices, denoted `K₄`, has all six possible edges.

In a **directed graph**, by contrast, an edge is an ordered pair. The assertion `(A,B)` need not imply `(B,A)`. A model of command flow might define A→B without any reverse communication.

**Graph structure versus interpretation** matters. If `A` and `B` denote devices, an edge labeled *depends on* could mean something different from an edge labeled *can send messages to*. An unlabeled line between the devices does not prove what kind of relationship exists. The canonical conceptual discussion belongs in [Relationships](../models-abstraction/relationships.md).

## Degree and the handshake principle

In an undirected graph, the **degree** of a vertex is the number of incident edges. Under standard graph-theory conventions, a self-loop contributes two to a vertex's undirected degree; a simple graph has no self-loops.

The **handshake lemma** states:

```text
sum of all vertex degrees = 2 × number of edges
```

For the four-vertex example above:

```text
deg(A) = 2
deg(B) = 2
deg(C) = 3
deg(D) = 1

Total degree = 2+2+3+1 = 8 = 2×4
```

Each undirected edge contributes two incidences, one at each endpoint. In a directed graph, the related rules are `sum(in-degrees) = |E|` and `sum(out-degrees) = |E|`, under the usual directed-edge convention.

A **degree sequence** summarizes local structure but generally does not uniquely determine the graph. More than one nonisomorphic graph can have the same degree sequence. These are mathematical invariants, not automatic measurements of network performance or trust.

## Walks, paths, cycles and connectivity

A **walk** is a sequence of vertices and incident edges that respects the graph's adjacency rules. A **path**, under the common elementary convention, is a walk with no repeated vertices. A **cycle** returns to its starting vertex without repeating other vertices or edges under the relevant graph class.

In the sample graph, A–B–C–A forms a cycle. A–C–D is a path of **length two**, where *length* here means two edges, not the physical distance between modeled objects.

An undirected graph is **connected** when there is a path between every pair of vertices. Otherwise, its maximal connected pieces are its **connected components**.

For directed graphs, distinguish **strong connectivity**, where each vertex is reachable from every other by following edge directions, from **weak connectivity**, where the underlying undirected version is connected. A directed dependency structure can be weakly connected without permitting reverse reachability.

This explains why the presence of a line in a diagram says little about traffic direction or causal influence without the edge semantics.

## Trees are connected and acyclic

A **tree** is a connected acyclic undirected graph. For a finite tree with `n ≥ 1` vertices, there are exactly `n−1` edges, and a unique simple path joins each pair of vertices. Merely having `n−1` edges without connectivity is **not** sufficient to establish that an arbitrary graph is a tree.

Removing the edge `{A,B}` from the four-vertex example leaves

```text
E' = {{A,C}, {B,C}, {C,D}}
```

This has four vertices, three edges, and no cycle, and remains connected. It is therefore a tree.

A tree is an abstraction of a hierarchy or branching structure, but not all real organizations, networks, or taxonomies are strictly trees. Cross-cutting relationships, shared dependencies, cycles or multiple parents may require a general graph.

The distinction matters for this repository: a **directory hierarchy** provides navigation, while the conceptual **knowledge relationships** may form a non-tree graph. See the [Governing Architecture](../ARCHITECTURE.md).

## Directed acyclic graphs and partial order

A **directed acyclic graph (DAG)** has directed edges and no directed cycles. A DAG admits at least one **topological ordering**, a sequence of vertices in which each directed edge `u → v` places `u` before `v`.

For example:

```text
A → C
B → C
C → D
```

A topological order is `A, B, C, D`. The order `B, A, C, D` is also valid because there is no directed path requiring A to precede B or vice versa. The graph does not define one unique ordering unless extra constraints eliminate alternatives.

A graph edge may encode a declared dependency, but a **topological order** only respects the *modeled* edges. It does not prove that all real-world dependencies were identified. The general [Dependencies](../systems-engineering/README.md) topic owns the systems-engineering interpretation of those constraints.

## Weighted graphs and optimization objectives

A **weighted graph** assigns values to edges or vertices according to a model, such as cost, latency, distance, probability, or capacity. A **shortest path** depends on what the weight means and what optimization problem is defined.

Suppose the directed edge `A → C` has cost 5, while `A → B` and `B → C` each have cost 1. The direct route uses **one edge** but has cost 5. The two-edge route through B has cost 2 and is cheaper.

Thus, **fewest edges** and **minimum total weight** need not identify the same route. Negative edge weights, multiple objectives and time-varying costs may demand different algorithms and assumptions. The graph describes the mathematical problem; the procedures for solving it belong in [Computation & Algorithms](../computation-algorithms/README.md).

## Graphs as representations, not guaranteed realities

Graph models necessarily choose which objects and connections matter. A missing edge could mean there is no relationship, the model excluded it, the observation lacked coverage, or the relationship has not been verified. A drawn edge may represent a proposed or inferred connection rather than a directly observed fact.

Similarly, an **undirected graph edge** is symmetric as a representation, but that does not mean the real interaction it represents is physically symmetric. A directed edge does not automatically mean one-way traffic. These are assumptions introduced by modeling decisions.

Graph theory provides **formal objects and theorems**; the [Relationships](../models-abstraction/relationships.md) article provides general interpreted associations, and [Observation](../scientific-analytical-reasoning/observation.md) and [Evidence](../scientific-analytical-reasoning/evidence.md) clarify what is actually supported by records.

## Relationships and authoritative references

[Sets and Relations](sets-and-relations.md) provides mathematical association, [Discrete Mathematics](discrete-mathematics.md) provides proof and counting, [Algebra and Functions](algebra-and-functions.md) explains mappings, and [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) explains system composition. [Network Knowledge](../../../network/README.md) may apply these foundations to network topology and routing.

- [MIT Mathematics for Computer Science: Lecture Readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/), especially Graphs and Coloring, Connectivity and Trees, and Digraphs and DAGs.
- [MIT Mathematics for Computer Science: Lecture Notes](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/), course-level formal graph material.
- [MIT Mathematics for Computer Science: Syllabus](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/syllabus/), scope of discrete graph methods.

**Editorial review note:** Corrected the mistaken label *complete graph* for the four-edge example. The handshake sum, tree conversion, topological order, and route costs were independently checked; the Batch 05 audit records the model-assisted review. General mathematical topology under G-01 remains a separate open issue.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
