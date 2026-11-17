# Wave A Technical Review: Batch 02

**Date:** November 17, 2026  
**Status:** Model-assisted scoped claim/source audit for three previously drafted references.  
**Scope:** Numbers and Numerical Systems; Measurement; Relationships.  
**Result:** 27 of 27 material claim families reviewed with evidence, calculation, or disclosed editorial interpretation. This is **internal technical/editorial acceptance**, not independent human expert validation or a final published release.

## Method and acceptance criteria

The live GitHub text was reopened, checked against original mathematical, metrological, philosophical and RDF materials, and corrected before acceptance. The work reviewed: definitions and scope; distinctions; mechanisms; examples; cross-links; and original authoritative references. Technical checks used Python for radix conversion, two's-complement interpretation, binary fractional values, floating-point approximation, and comparison of a hypothetical measurement interval to a threshold.

**Important distinction:** Checking an author-defined explanatory model for internal consistency does not make it a normative external standard. The accepted conceptual ownership, the 12-area taxonomy, and the unresolved architecture questions remain governed by the existing Fundamentals architecture.

## Material claim-to-source ledger

### Numbers and Numerical Systems

[Reviewed article](mathematics-logic/numbers-and-numerical-systems.md)

| ID | Material claim family | Supporting reference | Review disposition |
| --- | --- | --- | --- |
| NN-01 | Numbers and numerals are distinct; positional base notation is interpreted by radix | [Primary source](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation) | Scope distinction and radix example checked; number concept not equated with machine representation |
| NN-02 | Natural, integer, rational, real and complex domains have different algebraic structure | [Primary source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | Standard domains used; convention for zero in ℕ explicitly acknowledged |
| NN-03 | 13 decimal equals 1101 binary and D hexadecimal | [Primary source](https://docs.python.org/3/library/functions.html#int) | Programmatically evaluated 13=0b1101=0xD |
| NN-04 | Binary 0.101 equals 5/8 equals decimal 0.625 | [Primary source](https://docs.python.org/3/tutorial/floatingpoint.html) | Binary positional fraction recalculated exactly |
| NN-05 | 8-bit two's-complement 11111101 represents -3; unsigned represents 253 | [Primary source](https://docs.python.org/3/library/stdtypes.html#int.from_bytes) | Decoded both signed and unsigned interpretations independently |
| NN-06 | 8-bit signed two's-complement range -128..127 and unsigned range 0..255 | [Primary source](https://docs.python.org/3/library/stdtypes.html#int.from_bytes) | Finite-width range formula recalculated; conditional on explicitly stated encoding |
| NN-07 | Binary 0.1 is inexact and triple-sum may differ from 0.3 | [Primary source](https://docs.python.org/3/tutorial/floatingpoint.html) | Python float example reproduced: 0.30000000000000004 vs 0.3 |
| NN-08 | Decimal or rational arithmetic may exactly represent selected values | [Primary source](https://docs.python.org/3/library/decimal.html) | Python Decimal('0.1') triple sum equals Decimal('0.3') |
| NN-09 | Numeric precision vs metrological precision and accuracy are distinct | [Primary source](https://jcgm.bipm.org/vim/en/2.15.html) | Revised paragraph keeps representation properties separate from repeatability |

### Measurement

[Reviewed article](scientific-analytical-reasoning/measurement.md)

| ID | Material claim family | Supporting reference | Review disposition |
| --- | --- | --- | --- |
| ME-01 | Measurement and measurand are defined by experimental obtaining and intended quantity | [Primary source](https://jcgm.bipm.org/vim/en/2.1.html) | Verified against VIM 2.1 and 2.3; selected quantity and conditions matter |
| ME-02 | Measurement result is not merely indication; may include uncertainty/context | [Primary source](https://jcgm.bipm.org/vim/en/2.9.html) | VIM 2.9/2.10 distinction checked directly |
| ME-03 | Accuracy is a qualitative concept of closeness to true quantity value | [Primary source](https://jcgm.bipm.org/vim/en/2.13.html) | Verified VIM note: not itself a numeric quantity |
| ME-04 | Precision concerns agreement of replicate indications or values under specified conditions | [Primary source](https://jcgm.bipm.org/vim/en/2.15.html) | Direct VIM description; not conflated with accuracy |
| ME-05 | Uncertainty is nonnegative parameter of attributed quantity-value dispersion | [Primary source](https://jcgm.bipm.org/vim/en/2.26.html) | Corrected to VIM's precise definition |
| ME-06 | Measurement error measured minus reference quantity value | [Primary source](https://jcgm.bipm.org/vim/en/2.16.html) | VIM 2.16 verified; systematic/random concepts distinguished |
| ME-07 | Calibration is two-step relationship, not the same as adjustment or verification | [Primary source](https://jcgm.bipm.org/vim/en/2.39.html) | Direct VIM comparison checked |
| ME-08 | Metrological traceability belongs to result and depends on calibration chain | [Primary source](https://jcgm.bipm.org/vim/en/2.41.html) | Direct VIM 2.41; not guarantee of quality or absence of mistakes |
| ME-09 | Hypothetical 8.3±0.5 cm range straddles 8.0 cm threshold | [Primary source](https://jcgm.bipm.org/vim/en/2.26.html) | Arithmetic verified: interval 7.8..8.8; no coverage probability asserted |

### Relationships

[Reviewed article](models-abstraction/relationships.md)

| ID | Material claim family | Supporting reference | Review disposition |
| --- | --- | --- | --- |
| RE-01 | Conceptual relation vs set-theoretic relation distinguished | [Primary source](https://plato.stanford.edu/entries/relations/) | Philosophical relation requires an interpretation; mathematical pair-set a formal representation |
| RE-02 | Two-place and n-ary relations, participant roles and unary property distinction | [Primary source](https://plato.stanford.edu/entries/relations/) | Clarified roles may share a referent; unary relations depend on formal convention |
| RE-03 | Direction and role labels give meaning beyond an unlabeled edge | [Primary source](https://www.w3.org/TR/rdf11-concepts/) | W3C directed predicate semantics support example; not a universal ontology |
| RE-04 | Cardinality constraints stipulate, rather than prove, empirical data integrity | [Primary source](https://www.w3.org/TR/rdf11-primer/) | Modeling distinction; records require external verification |
| RE-05 | Identity differs from equivalence under chosen relation | [Primary source](https://plato.stanford.edu/entries/identity/) | Corrected language to avoid conflating numerical sameness and criterion-based equivalence |
| RE-06 | Direct dependency vs transitive reachability differ | [Primary source](https://plato.stanford.edu/entries/relations/) | Logical counterexample possible; derived relation needs defined semantics |
| RE-07 | RDF 1.1 triples restrict subject to IRI/blank, predicate to IRI, object to IRI/literal/blank | [Primary source](https://www.w3.org/TR/rdf11-concepts/) | Normative RDF 1.1 rule checked |
| RE-08 | A knowledge graph's representation does not prove physical truth of its assertions | [Primary source](https://www.w3.org/TR/rdf11-concepts/) | Distinction between asserting a triple and independently validating its referent |
| RE-09 | Seven-facet conceptual relation anatomy and pump illustration | [Primary source](https://plato.stanford.edu/entries/relations/) | Editorial illustration explicitly labeled nonstandard, not an approved predicate vocabulary |

## Corrections made

- **Numbers:** Replaced an overbroad floating-point comparison with the explicit Python example and distinguished numerical-format precision from measurement precision. Added a functional-reference source to reinforce that numerical values and representations are different.
- **Measurement:** Tightened uncertainty to VIM 2.26's nonnegative dispersion parameter, added direct VIM entries for accuracy, precision, calibration, uncertainty and traceability, and explicitly noted that traceability is not a guarantee of correctness.
- **Relationships:** Distinguished the identity relation from equivalence, allowed multiple roles to refer to the same entity, and clarified unary predicates versus relations in different formalisms. The seven descriptive facets remain an **illustration, not a graph schema**.

## Computational evidence

| Expression / convention | Observed result |
| --- | --- |
| `int('1101',2)`, `int('D',16)` | Both yield `13` |
| `0.101₂` | `0.625₁₀` |
| Unsigned `11111101₂` | `253` |
| Signed eight-bit two's complement `11111101₂` | `-3` |
| Eight-bit signed / unsigned ranges | `-128..127` / `0..255` |
| Python `0.1 + 0.1 + 0.1` | `0.30000000000000004` |
| Python `(0.1+0.1+0.1)==0.3` | `False` |
| `Decimal('0.1')*3 == Decimal('0.3')` | `True` |
| Hypothetical `8.3 ± 0.5` | Illustrative endpoints `7.8` and `8.8`; range spans `8.0` |

These checks establish the stated examples and assumptions. They are not a complete test of all numerical formats or metrological practices.

## Publication disposition

All three references pass the scoped **model-assisted Reviewed** gate and may serve as references in further Wave A development. Their source-review field is **Core claims checked**, not **Verified by an independent human expert**. They are visible GitHub articles, but **final publication acceptance and complete seven-gate Fundamentals closure are not claimed**.

**Inventory unchanged:** 12 approved knowledge areas, 109 original subject headings. G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML remain separate pending architecture decisions.

The next three Wave A articles, once authored, begin as **Draft / References listed** and require this same evidence-led review before promotion. Do not include Knowledge Checks or Practical Assessments.

## Related records

[Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) · [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Fundamentals](README.md)
