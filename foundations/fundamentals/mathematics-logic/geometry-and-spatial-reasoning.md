# Geometry and Spatial Reasoning

**Knowledge area:** [Mathematics & Logic](README.md)  
**Subject ID:** F-01-10  
**Development status:** Draft; substantive article newly authored  
**Source review:** References listed; scoped technical review pending  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Geometry models spatial properties and relationships

**Geometry** studies spatial structures, shapes, positions, distances, angles, transformations and their properties under stated assumptions. **Spatial reasoning** uses those relationships to infer possible positions, overlaps, separations, orientations and movements. A coordinate system is a way to *represent* geometry; it does not create the spatial relationship it encodes.

A geometric model must identify its space and its assumptions. Elementary **Euclidean geometry** uses distances and angle relations appropriate to Euclidean space. Other geometries change the axioms or structures, and conclusions derived in one setting must not be transferred unchanged into another. Physical locations and measured boundaries further require reference frames, units, calibration and uncertainty.

[Linear Algebra and Vector Spaces](linear-algebra-and-vector-spaces.md) owns the general linear mathematics underlying many transformations. This subject owns **geometric meaning, coordinate frames, metric relations and spatial constraints**. [Topology and Continuity](topology-and-continuity.md) owns general open-set structure, connectedness and continuity independently of a specific distance.

## Points, vectors and coordinate frames

A **point** denotes a position within a chosen space; a **vector** can represent a displacement, direction or other vector-space element. In an affine geometric model, points need not themselves constitute a vector space, even though the difference between two points can be represented by a vector. Thus adding a displacement to a point is meaningful under an affine-space convention, while adding two positions is not automatically a coordinate-independent geometric operation.

A **coordinate frame** establishes an origin and basis or axes, and may include units, scale, handedness and orientation. The same physical point can receive different coordinates in different frames. A numerical coordinate without its frame may be uninterpretable or misleading.

For points `p=(x₁,y₁)` and `q=(x₂,y₂)` in a 2D Euclidean coordinate system with orthonormal axes and common length units, the Euclidean distance is

`d(p,q)=√[(x₂−x₁)²+(y₂−y₁)²]`.

This formula is not a universal metric for curved surfaces, geographic coordinates on Earth, anisotropic spaces, or graph-hop distances.

## Distance, angle, orientation and geometric relations

A **metric** `d` supplies a nonnegative distance satisfying identity of indiscernibles, symmetry and the triangle inequality. Euclidean distance is one metric; Manhattan distance is another. The choice changes which points are considered close and which geometric arguments are valid.

The dot product of Euclidean displacement vectors expresses lengths and angles, for example `u·v=||u||||v||cos θ` for nonzero vectors and the standard inner product. Perpendicularity follows when their dot product is zero. Coordinate orientation and handedness matter for signed angles and cross products.

Spatial relations include **inside/outside**, **intersects/disjoint**, **touches**, **contains**, **adjacent**, **aligned**, and **overlaps**. Some are topological, while others require metric distances, directional axes, bounding geometry, temporal context or explicit dimensional models. These relations should not be conflated with informal language. Two shapes can be "close" in one metric and far apart under another.

## Transformations and what they preserve

A geometric **translation** shifts every point by a displacement. A **rotation** changes orientation about a specified center while preserving Euclidean distances and angles. A **reflection** preserves Euclidean distances and angles but reverses orientation in the corresponding setting. A **uniform scaling** multiplies all distances by a factor but does not preserve original lengths except for special scale factors.

A *rigid transformation* preserves pairwise Euclidean distances. An **affine transformation** preserves straight lines and ratios along collinear segments under an invertible affine map, but need not preserve lengths or angles. A **projective transformation** can preserve incidence while changing additional geometric properties. Stating that two models are "the same shape" is incomplete until the permitted transformation class and invariant are specified.

Two-dimensional rotation by 90° counterclockwise about the origin has a standard matrix representation:

```text
R = [ 0  -1 ]
    [ 1   0 ]
```

Applied to a column vector `(x,y)`, it produces `(-y,x)`. A translation by `t` has the form `p↦Rp+t`. That is an affine transformation rather than a linear map when `t≠0`.

## Geometric models and dimensionality

A line, plane, surface and three-dimensional region are not interchangeable models. A 2D drawing of a 3D object may omit depth, hidden surfaces, perspective and physical tolerances. A projection can map multiple source locations to the same image point, so reconstructing 3D geometry from a single projection generally requires assumptions or more evidence.

A **bounding box** is a convenient approximation of an object's extent, not a proof of exact collision geometry. Using axis-aligned boxes may simplify intersection tests but introduce false positives relative to the actual shapes. The underlying geometry, coordinate frame, approximation and error allowance must be explicit.

## Worked example: distance and frame transformation

In a common, 2D orthonormal coordinate frame with units of meters, consider:

```text
p = (1, 2) m
q = (4, 6) m
q - p = (3, 4) m
```

The Euclidean distance is `√(3²+4²)=5 m`. A counterclockwise 90° rotation about the origin maps `p` to `(-2,1) m` and `q` to `(-6,4) m`. The rotated displacement is `(-4,3) m`, whose length is still `√(16+9)=5 m`.

**Conclusion within the model:** The rotation preserves the distance. **Not established:** That physical points have been measured with zero error, that the origin corresponds to a known site or object, or that a coordinate transformation is an actual physical motion. A passive change of frame and an active movement can yield related coordinate expressions but describe different operations.

## Distinctions and cross-knowledge ownership

- [Graph Theory](graph-theory.md) models vertices and edges. Graph adjacency or reachability is not the same as distance or geometric neighborhood.
- [Topology and Continuity](topology-and-continuity.md) studies continuity and connectedness with fewer metric assumptions. A homeomorphism does not generally preserve lengths and angles.
- [Linear Algebra and Vector Spaces](linear-algebra-and-vector-spaces.md) owns linear maps and change-of-basis mathematics; geometry supplies spatial interpretation.
- [Measurement](../scientific-analytical-reasoning/measurement.md) owns observed quantities, instrument limits, calibration and uncertainty.
- [Entities and Attributes](../models-abstraction/entities-and-attributes.md) owns general representational entities; [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) owns physical/system boundaries in engineering contexts.

## Authoritative reference starting points

- [MIT OCW 18.02SC, Vectors and Matrices](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/1.-vectors-and-matrices/), geometric and algebraic vector concepts, lengths, angles and coordinate systems.
- [MIT OCW 18.02SC, Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), parametric curves, geometry and spatial transformations in the Euclidean setting.
- [MIT OCW 18.901, Introduction to Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/), showing where topological properties differ from geometric measures.

The example uses idealized 2D Euclidean geometry. Neither actual sensor uncertainty nor non-Euclidean geospatial projections is solved by its formulas.

**Editorial disposition:** Draft; sources listed, verification pending. No Knowledge Checks or Practical Assessments.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
