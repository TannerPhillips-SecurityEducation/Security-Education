# Wave A Technical Review: Batch 03

**Status:** Model-assisted scoped technical/editorial review v0.1, November 17, 2026.  
**Knowledge areas:** Mathematics & Logic; Scientific & Analytical Reasoning; Models & Abstraction.  
**Subjects:** Algebra and Functions; Hypotheses and Experiments; Identity and Distinction.  
**Claim groups reviewed:** 24.  
**Outcome:** The three references pass **model-assisted internal review** after correction; **no independent human expert acceptance or final publication** is claimed.

## Review methodology

Live GitHub drafts were reopened. Assertions were checked against directly inspected OpenStax material, NIST/SEMATECH Experimental Design guidance, Stanford Encyclopedia of Philosophy identity/induction sources, and W3C RDF concepts. Numeric examples were independently recomputed with Python. Original illustrative models were distinguished from normative definitions, especially for experimental design and persistence of entity identity.

This scoped audit checks the documented **material claim groups**, not every conceivable application or unstated assumption. A source link does not turn an editorial model into a standard.

## Claim-to-source ledger

### Algebra and Functions

[Reviewed reference](mathematics-logic/algebra-and-functions.md)

| ID | Material claim | Source | Assessment |
| --- | --- | --- | --- |
| AF-01 | Expression, equation, identity, and inequality have distinct logical roles | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation) | Statements and assumptions distinguished; numerical examples checked |
| AF-02 | Function maps each element of a domain to exactly one element of a codomain | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation) | Function vs arbitrary relation and image/codomain distinction preserved |
| AF-03 | f(x)=2x+3 maps reals onto reals; g(x)=x² has nonnegative image | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation) | Algebraic outputs checked |
| AF-04 | Composition f∘g differs in general from g∘f | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions) | At x=1 results 5 vs 25 independently evaluated |
| AF-05 | Composition domain may narrow according to subsequent function domain | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions) | Square-root domain example x≥3 correct |
| AF-06 | Inverse requires appropriate one-to-one mapping, with domain/codomain requirements | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions) | Corrected square to bijection [0,∞)→[0,∞); real-to-real square not invertible |
| AF-07 | Linear transformation vs affine map mx+b with b≠0 | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry/pages/3-1-functions-and-function-notation) | Basic distinction mathematically justified by L(0)=0; not attributed as direct OpenStax formal definition |
| AF-08 | Calibration example T(r)=0.5r−10 is mathematical mapping, not evidence of physical accuracy | [Authoritative reference](https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions) | T(50)=15 and inverse r=2(T+10) calculated; context caveat present |

### Hypotheses and Experiments

[Reviewed reference](scientific-analytical-reasoning/hypotheses-and-experiments.md)

| ID | Material claim | Source | Assessment |
| --- | --- | --- | --- |
| HE-01 | Scientific hypothesis describes testable claim, prediction or explanation | [Authoritative reference](https://plato.stanford.edu/entries/science-theory-observation/) | Generic scientific model, not fixed schema |
| HE-02 | Experimental units, factors and response variables distinguish units from repeated observations | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm) | Corrected run-to-run carryover and independence assumptions |
| HE-03 | Randomized assignment does not guarantee balance for finite samples | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm) | Balanced design and randomization distinguished |
| HE-04 | Replication requires independent experimental units under relevant model assumptions | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm) | No pseudoreplication of within-run measurements |
| HE-05 | Blocking accounts for selected nuisance factor and preserves treatment contrasts within blocks | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) | NIST randomized block design inspected |
| HE-06 | Full factorial and response-surface designs answer different experimental goals | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri33.htm) | NIST objective-based design distinctions |
| HE-07 | Eight fictional cooling measurements yield means 16 and 11 minutes | [Authoritative reference](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm) | Python mean check 16, 11, difference 5; fictional values disclosed |
| HE-08 | A measured association cannot establish universal cause without supporting assumptions | [Authoritative reference](https://plato.stanford.edu/entries/science-theory-observation/) | Validity and confounding caveats explicit |

### Identity and Distinction

[Reviewed reference](models-abstraction/identity-and-distinction.md)

| ID | Material claim | Source | Assessment |
| --- | --- | --- | --- |
| ID-01 | Numerical identity differs from qualitative resemblance | [Authoritative reference](https://plato.stanford.edu/entries/identity/) | Source revised October 2026, distinctions align |
| ID-02 | Numerical identity is reflexive, symmetric and transitive in classical semantics | [Authoritative reference](https://plato.stanford.edu/entries/identity/) | Correct equality properties |
| ID-03 | Congruence modulo 3 defines equivalence without numerical identity | [Authoritative reference](https://plato.stanford.edu/entries/identity/) | 4 and 7 congruent mod 3, 4≠7; checked |
| ID-04 | Converse identity of indiscernibles is contested in metaphysics | [Authoritative reference](https://plato.stanford.edu/entries/identity-indiscernible/) | Separates Leibniz's law from contested converse |
| ID-05 | Identity over time depends on relevant persistence criteria and philosophical assumptions | [Authoritative reference](https://plato.stanford.edu/entries/identity-time/) | Service migration illustration clearly model-relative |
| ID-06 | IRI reference expression and its referent are conceptually distinct | [Authoritative reference](https://www.w3.org/TR/rdf11-concepts/) | RDF concept reference reviewed; does not make a user credential proof |
| ID-07 | Names, addresses and identifiers may change while logical subject persists under chosen rules | [Authoritative reference](https://www.w3.org/TR/rdf11-concepts/) | Technology example explicitly illustrative, not universal mapping rule |
| ID-08 | Entity category and boundary scope affect identity model without establishing authentication | [Authoritative reference](https://plato.stanford.edu/entries/identity/) | Canonical ownership keeps authentication in Security Foundations and Identity Knowledge |

## Corrections recorded before acceptance

- **Algebra:** An inverse of the square function was described with insufficient attention to codomain. The article now explicitly defines the bijection `g:[0,∞)→[0,∞)`, not merely a domain-restricted mapping to all real numbers.
- **Experiment design:** The independence of cooling runs cannot be taken for granted when using a shared apparatus. The article now states assignment and carryover assumptions; NIST randomized and blocked designs replace sources that could not be consistently fetched in this review.
- **Identity:** The article now more explicitly separates all-or-nothing numerical identity from property-based resemblance and clarifies how RDF IRIs denote resources under an interpretation.

## Executed mathematical example checks

| Example | Checked result |
| --- | --- |
| `f(g(1))` for `f(x)=2x+3`, `g(x)=x²` | `5` |
| `g(f(1))` | `25` |
| `g(3)=g(-3)` | Both `9`; no inverse on all real inputs |
| `f(4)` with `f(x)=2x+3` | `11` |
| `T(50)=0.5(50)-10` | `15` |
| Mean of `16,15,17,16` | `16` |
| Mean of `11,12,10,11` | `11` |
| Difference of the sample means | `5` |
| `4 ≡ 7 (mod 3)` but `4 ≠ 7` | True |

Calculations validate these examples under stated mathematical conventions; they do not validate empirical cooling effects, human attribution, or any particular security system.

## Relationship and scope consistency

General function definitions remain in Mathematics & Logic, experimental inference remains in Scientific & Analytical Reasoning, and numerical identity remains in Models & Abstraction. Model implementation, authentication, and vendor-specific procedures are outside this reference's fundamental scope. General temporality (G-04) remains an **open architectural decision**, and a discussion of persistence across time does not close it.

## Disposition

| Subject | Development | Source review | Publication |
| --- | --- | --- | --- |
| Algebra and Functions | **Reviewed (model-assisted)** | **Core claims checked** | Not finally accepted |
| Hypotheses and Experiments | **Reviewed (model-assisted)** | **Core claims checked** | Not finally accepted |
| Identity and Distinction | **Reviewed (model-assisted)** | **Core claims checked** | Not finally accepted |

The three may be used as the **internally reviewed reference-writing baseline** for further Wave A authoring. A later independent human review may supersede these dispositions. The next three approved-heading articles must start as **Draft / References listed** until their own audit passes.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Governing Architecture](ARCHITECTURE.md)
