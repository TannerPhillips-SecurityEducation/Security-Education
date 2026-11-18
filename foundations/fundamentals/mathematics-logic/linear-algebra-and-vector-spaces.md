# Linear Algebra and Vector Spaces

**Knowledge area:** [Mathematics & Logic](README.md)  
**Subject ID:** F-01-09  
**Development status:** Reviewed (model-assisted; independent human acceptance not claimed)  
**Source review:** Core claims checked; [Wave F 42-family scoped technical audit](../WAVE-F-TECHNICAL-REVIEW-01.md); comprehensive source-level verification not claimed  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Linear algebra describes structure-preserving transformations

**Linear algebra** studies vector spaces, linear transformations, linear systems, and the representations of those structures by matrices. It supplies models for quantities with several coordinates, interacting constraints, and transformations that preserve addition and scalar multiplication. A column of numbers is a common *coordinate representation* of a vector, not the complete definition of a vector.

A **vector space over a field** such as the real numbers consists of a set of vectors, vector addition, and scalar multiplication satisfying axioms that include closure, associativity and commutativity of addition, an additive zero and inverses, and compatibility of scalar multiplication with field operations. Functions, polynomials and signals can also be vectors when the specified operations satisfy those axioms. A vector need not represent a displacement or point in physical space.

[Algebra and Functions](algebra-and-functions.md) owns general expressions and functions; this article owns **vector-space structure and linear maps**. [Geometry and Spatial Reasoning](geometry-and-spatial-reasoning.md) owns spatial lengths, angles, coordinate frames and physical/geometric interpretations.

## Vectors, span, independence and bases

In the coordinate space `R²`, a vector `v = (v₁, v₂)` can be added componentwise and multiplied by a scalar. A **linear combination** of vectors `v₁,…,vₖ` has the form `a₁v₁ + … + aₖvₖ`. Their **span** is the set of all such combinations. The vectors are **linearly independent** when the only combination equal to zero uses all coefficients zero.

A **basis** is a linearly independent spanning set. Its cardinality is the **dimension** for a finite-dimensional vector space. Coordinates depend on a chosen basis; the abstract vector does not change when its coordinate description is converted correctly to a different basis. Coordinate changes must therefore distinguish an underlying object from its representation.

For example, `e₁=(1,0)` and `e₂=(0,1)` form the standard basis of `R²`. The vector `(3,4)` is `3e₁+4e₂`. The pair `(1,1)` and `(2,2)` is *not* a basis of `R²`: the second vector is a multiple of the first, so their span is only one-dimensional.

## Linear transformations and matrices

A map `T:V→W` is **linear** if `T(u+v)=T(u)+T(v)` and `T(av)=aT(v)` for the permitted vectors and scalars. Once bases are chosen in finite-dimensional spaces, a matrix represents `T`; the matrix depends on those bases even though the abstract map does not.

For column-vector convention, a matrix `A` with two rows and two columns maps a coordinate vector `x` to `Ax`. Matrix multiplication composes represented maps when their dimensions and coordinate conventions agree. In general `AB≠BA`; changing the order of transformations may change the result.

A map `x↦Ax+b` is **affine**; if `b≠0`, it is not linear as a map between vector spaces with their chosen zero vectors, even when its graph looks like a straight line. This distinction matters in calibration and geometric transformations.

## Rank, null spaces and solvability

The **kernel** or null space of `T` contains input vectors mapped to zero. The **image** contains attainable outputs. For a finite-dimensional domain, the rank–nullity theorem gives

`dim(V) = rank(T) + nullity(T)`.

If a square matrix has a nonzero determinant, it is invertible; equivalently, its columns are independent, its null space contains only zero, and it has full rank. These equivalences apply to finite square matrices over a field; not every rectangular transformation has an inverse.

The equation `Ax=b` can have no solution, exactly one solution or multiple solutions, depending on whether `b` belongs to the image and whether the kernel is trivial. Numerical software must additionally consider rounding and ill-conditioning; an algebraically invertible matrix can be difficult to solve accurately in finite precision.

## Eigenvalues and invariant directions

For a square linear operator represented by `A`, an **eigenvector** is a nonzero vector `v` for which `Av=λv`. The scalar `λ` is an **eigenvalue**. Such a vector is mapped onto its own span rather than an arbitrary new direction. Matrices need not have all eigenvalues real, and not every matrix is diagonalizable. Eigenstructure depends on the permitted scalar field and must not be used to assume all systems have independent modes.

Eigenvalues can help study repeated transformations and certain linearized dynamical systems; they do not by themselves prove stability of a nonlinear or time-varying real system.

## Worked example: transform a two-coordinate vector

Choose the real matrix

```text
A = [2  1]      x = [4]
    [0  3]          [2]
```

With the standard column-vector convention:

```text
Ax = [2·4 + 1·2] = [10]
     [0·4 + 3·2]   [ 6]
```

The determinant is `2·3−0·1=6`, so the transformation is invertible. Its columns `(2,0)` and `(1,3)` are independent, giving rank 2 and nullity 0. As an upper-triangular matrix, its eigenvalues are the diagonal entries `2` and `3`.

**What the calculation establishes:** Under exact real arithmetic and the declared coordinate convention, `x=(4,2)` maps to `(10,6)` and the linear map is invertible. **What it does not establish:** The meaning, physical units, measured accuracy or causal interpretation of either vector. Those require a mapping to the modeled target and supporting evidence.

## Where linear algebra meets other foundational subjects

[Sets and Relations](sets-and-relations.md) supplies the mathematical set vocabulary; [Algebra and Functions](algebra-and-functions.md) supplies general function composition; [Geometry and Spatial Reasoning](geometry-and-spatial-reasoning.md) supplies geometric interpretations; [Topology and Continuity](topology-and-continuity.md) examines a more general notion of continuity; [Algorithms](../computation-algorithms/algorithms.md) and [Computational Efficiency](../computation-algorithms/computational-efficiency.md) address implementations and numerical costs. [Machine Learning Foundations](../computation-algorithms/machine-learning-foundations.md) uses linear representations in some but not all learning models.

## Sources and limitations

- [MIT OpenCourseWare: Linear Algebra (18.06)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/), including linear systems, vector spaces, eigenvectors and linear transformations.
- [MIT 18.02SC: Vectors and Matrices](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/1.-vectors-and-matrices/), connecting algebraic and geometric vector representations.
- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), mathematical proof and discrete prerequisites.

Definitions and the worked matrix computation use the standard finite-dimensional real-vector-space setting. Extension to complex fields, infinite-dimensional spaces, normed spaces or numerical linear algebra requires extra assumptions and treatment.

**Editorial status:** Reviewed (model-assisted) under the [Wave F scoped technical review](../WAVE-F-TECHNICAL-REVIEW-01.md). Full source-passage verification, independent expert review and final publication acceptance remain open.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
