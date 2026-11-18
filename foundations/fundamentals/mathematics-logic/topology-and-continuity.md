# Topology and Continuity

**Knowledge area:** [Mathematics & Logic](README.md)  
**Subject ID:** F-01-11  
**Development status:** Reviewed (model-assisted; independent human acceptance not claimed)  
**Source review:** Core claims checked; [Wave F 42-family scoped technical audit](../WAVE-F-TECHNICAL-REVIEW-01.md); comprehensive source-level verification not claimed  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Topology describes structure without requiring distance

**Topology** studies structural properties of spaces expressed through open sets, neighborhoods, continuity, connectedness and compactness. In contrast, [Geometry and Spatial Reasoning](geometry-and-spatial-reasoning.md) often studies distances, angles and coordinates, and [Graph Theory](graph-theory.md) treats combinatorial vertices and edges.

The term "topology" in a computer network often means a connection arrangement. Graph topology, physical geometry and mathematical **topological-space structure** are related modeling choices, not interchangeable objects. A network diagram does not prove a continuous spatial property.

## Topological spaces and their axioms

A **topological space** consists of a set X and a collection τ of its subsets, called open sets. The collection must satisfy three axioms: the empty set and all of X are open; arbitrary unions of open sets are open; and finite intersections of open sets are open.

The **usual topology** on the real line consists of unions of open intervals. An interval such as (-1,1) is open in R. The subset [0,1] is not open in R with its usual topology, but it is open relative to itself when considered with its **subspace topology**. The words open and closed must therefore specify the ambient space and topological structure.

A set is **closed** when its complement is open; a subset may be both open and closed, or neither. A **neighborhood** of a point contains an open set that contains the point. Open-set neighborhoods need not be defined by a ruler or a physical separation.

## Continuity and structure-preserving maps

A function f:X→Y between topological spaces is **continuous** if the preimage of every open set in Y is open in X. Under the usual topology of Euclidean spaces, this agrees with the familiar epsilon–delta definition of continuity. A formula alone cannot establish continuity without specifying relevant domain and codomain spaces and their topologies.

A **homeomorphism** is a bijective continuous map whose inverse is also continuous. It preserves topological properties, though not necessarily lengths, angles, areas or geometric shapes under a Euclidean metric. A continuous bijection does not always have a continuous inverse; compactness and separation conditions can yield useful sufficient criteria.

A topological description of a possible state space is not by itself evidence that a real system changes continuously. A sensor that reports 100 samples does not prove the sampled process lacked intermediate discontinuities.

## Connectedness, paths and compactness

A space is **connected** when it cannot be partitioned into two disjoint nonempty subsets that are open in the space. An interval such as [0,1] with its usual subspace topology is connected, while the two-point subset {0,1} of R is disconnected in its subspace topology.

**Path connectedness** requires a continuous map from [0,1] connecting every chosen pair of points. Path connectedness implies connectedness, but the converse need not hold in all topological spaces. The existence of a finite path in a graph is a different, combinatorial statement.

A space is **compact** if each open cover has a finite subcover. In Euclidean space with the usual topology, the Heine–Borel theorem states that a subset is compact if and only if it is closed and bounded. Outside that setting, "closed and bounded" is not a general definition or universal test for compactness. Compactness is also not a synonym for physically small or computationally efficient.

## Invariants and their limits

A **topological invariant** is a property unchanged under homeomorphism. Connectedness and compactness are examples. A circle and an appropriately deformed simple closed loop can be homeomorphic while differing in Euclidean shape. A filled disk and its boundary circle are not homeomorphic, illustrating that suppressing a dimension or interior changes more than just a geometric measurement.

Topological claims are sensitive to the chosen structure. A metric can induce a topology, but a bare topology need not identify a unique metric. Conclusions about distance require additional geometric or metric assumptions.

## Worked example: continuity is not length preservation

Take the usual real-line topology on the source and target of the function f(x)=2x. The preimage of the open interval U=(-1,1) is

```text
f⁻¹(U) = {x: -1 < 2x < 1}
       = (-0.5, 0.5).
```

This is open. More generally, the preimage of any open interval (a,b) is the open interval (a/2,b/2), and inverse images commute with arbitrary unions. Thus f is continuous. Its inverse g(y)=y/2 is also continuous, making f a homeomorphism of the usual real line with itself.

However, the Euclidean distance from 0 to 1 is 1, while the distance from their images 0 and 2 is 2. The map preserves the relevant topology but not Euclidean lengths.

**Supported conclusion:** The two real lines are homeomorphic under the given map. **Unsupported conclusion:** Any physical stretching process perfectly preserves every material property, or an observed signal is continuous merely because the abstract model is.

## Canonical relationships and limits

- [Graph Theory](graph-theory.md) owns vertices, edges and graph connectivity; graph paths are not the definition of topological connectedness.
- [Geometry and Spatial Reasoning](geometry-and-spatial-reasoning.md) owns coordinate frames, metrics and geometric transformations.
- [Linear Algebra and Vector Spaces](linear-algebra-and-vector-spaces.md) owns algebraic linearity; continuity and linearity are distinct properties.
- [State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) owns models of change, including discrete transitions. [Temporal Concepts and Models](../models-abstraction/temporal-concepts-and-models.md) owns generalized event time, intervals and order.
- [Signal Conversion](../physical-electrical-principles/signal-conversion.md) owns physical signal sampling and reconstruction assumptions, not general point-set topology.

## Sources

- [MIT OpenCourseWare 18.901 Introduction to Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/): open sets, continuity, connectedness, compactness and separation.
- [MIT OCW 18.901 Lecture Notes](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/pages/lecture-notes/): reference material for definitions and proofs.
- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/): proof and discrete-math prerequisites.

This is an introductory account of point-set topology, not an exhaustive treatment of algebraic or differential topology. Citations are starting points; independent source-passage verification and human peer review remain pending.

**Editorial status:** Reviewed (model-assisted) under the [Wave F scoped technical review](../WAVE-F-TECHNICAL-REVIEW-01.md). Full source-passage verification, independent expert review and final publication acceptance remain open.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
