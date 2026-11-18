# Testing and Software Lifecycle

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Testing and software lifecycle  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical/source review pending

## Software is evaluated and revised across time

**Software testing** uses selected inputs, conditions and observations to evaluate whether a program or component behaves as expected under specified criteria. A **software lifecycle** describes activities through which software is conceived, specified, designed, implemented, built, tested, deployed, operated, maintained, revised and eventually retired under an adopted process.

A test that passes gives evidence about the tested conditions, not a universal proof that a program has no defects. Likewise, completing a lifecycle stage does not guarantee technical correctness or fitness for use.

[MIT 6.005 Software Construction](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/syllabus/) covers specifications, testing and coverage, code review, version control, modularity and concurrent programming. [System Lifecycle](../systems-engineering/system-lifecycle.md) owns the broader lifecycle of engineered systems and services.

## Specify expected behavior before assessing outcomes

A **test case** defines input, relevant environment or setup, expected behavior and an observation or decision method. Without an expected result grounded in a specification, observing that a program ran does not establish whether it behaved correctly.

Software verification asks whether the implemented program satisfies stated requirements under the evaluated scope. Software validation concerns whether those requirements and software outcomes meet intended user needs. They are complementary but different.

A **unit test** checks a selected component or function, an **integration test** checks interacting parts, and an **end-to-end test** checks a wider operational path under defined assumptions. These labels describe scopes rather than absolute assurance levels; a single end-to-end test cannot substitute for every relevant unit-level check.

[Verification and Validation](../systems-engineering/verification-and-validation.md) owns general engineering conformance and intended-use evidence, while this article owns software-specific development and evaluation mechanisms.

## Worked example: boundary-value testing

Suppose a fictional function `valid_score(x)` accepts **only integer scores from 0 through 100 inclusive**, under exact integer semantics:

```text
valid_score(x) = true  if x is an integer and 0 ≤ x ≤ 100
               = false otherwise
```

Representative tests might include:

| Input | Expected |
| ---: | --- |
| −1 | false |
| 0 | true |
| 1 | true |
| 100 | true |
| 101 | false |

These five cases exercise the specified lower and upper boundaries. They do not prove the function works for every integer, noninteger value, malformed input or runtime environment. Another program could deliberately produce exactly these five expected results and still fail almost everywhere else.

A complete testing strategy needs to account for the declared input domain, equivalence classes, relevant boundaries, possible state transitions and error conditions.

## Testing levels, regression and test doubles

Automated tests can evaluate selected code paths repeatedly. **Regression testing** checks whether behavior previously accepted under a specification still holds after changes, within the coverage of those tests.

Mocks, stubs and simulators can substitute for dependencies to create controlled conditions. Such a test provides evidence about the modeled interaction; it does not automatically prove that the real dependency behaves identically. A stub returning a fixed sensor value may make a software test deterministic while concealing physical sensor faults.

A passing build, a passing unit-test suite and a successful deployment are separate statuses. None is automatically proof of production readiness.

## Coverage and test selection

**Code coverage** reports which selected code elements or paths were exercised under a measurement scheme. Coverage percentages do not measure correctness by themselves.

For example, a test can execute every statement in a function while failing to check an important branch interaction or edge case. Likewise, observing one correct output from a function can miss state changes or later failures.

Coverage should be interpreted with test quality, oracle correctness, input selection and environment constraints. [Evidence](../scientific-analytical-reasoning/evidence.md) owns the broader strength of observations supporting claims.

## Reviews, versions and change management

**Code review** evaluates selected aspects of a change, such as clarity, contracts, assumptions, failure handling, test evidence and maintainability. It can find defects and improve shared understanding, but reviewers can miss issues.

**Version control** records changes and identifies revisions, branches or merge histories under chosen processes. A commit identifier shows a recorded repository state, not proof that the resulting product is correct or that all deployment artifacts match that revision.

Changing a library, language runtime or configuration can alter behavior even without modifying the application's own source. Software lifecycle decisions need the relevant dependency and configuration records.

[Modules and Dependencies](modules-and-dependencies.md) owns package/version relationships, while [Runtime Environments](runtime-environments.md) owns the execution context.

## Debugging, correction and deployment

**Debugging** seeks to identify and correct the cause of an observed problem. A reproducible failure can help isolate a defect, but an intermittent bug may depend on concurrency, timing, external systems or unavailable data.

A fix requires checking that the intended problem was addressed without violating other requirements. Validation after deployment may consider users, real workloads, monitoring and change impact, not only predeployment tests.

The lifecycle can iterate: operational evidence may lead to changing requirements, design, code, tests, deployment and documentation. No universal one-way waterfall process is mandated.

## Scope and acceptance

Software testing in this article concerns **testing software**, not student Knowledge Checks or Practical Assessments. The Fundamentals repository contains neither. No test framework, CI/CD platform, software lifecycle doctrine, coverage target or certification is approved here.

### Sources

- [MIT 6.005: Software Construction Readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.005: Testing](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/03-testing/).
- [MIT 6.005: Version Control](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/05-version-control/).
- [NASA: Product Realization](https://www.nasa.gov/reference/5-0-product-realization/).

**Editorial status:** Substantive Draft. The boundary-value example, lifecycle and assurance distinctions require a separate scoped claim-to-source review. No learner assessments or tool mandates are introduced.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
