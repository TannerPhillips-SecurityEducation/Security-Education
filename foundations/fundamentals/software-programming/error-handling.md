# Error Handling

**Knowledge area:** [Software & Programming](README.md)  
**Approved subject heading:** Error handling  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Software Batches 03–04 audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md); independent human review pending

## Detecting a problem differs from recovering from it

**Error handling** concerns how software recognizes, represents, communicates and responds to abnormal conditions or failures under a defined contract. It includes input validation, error values, exceptions, state cleanup, rollback, retry, fallback and termination, but no single mechanism is universally correct.

A **defect** is a problem in an implementation or design; an **error condition** is a state or event identified as unacceptable by a contract; an **exception** is one language mechanism for signaling a condition; a **failure** is an inability to meet a required function. These concepts can relate without being synonyms.

[MIT Software Construction's specifications and exception guidance](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/) distinguishes exceptions used for special results, bugs and other conditions. [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns system-level failure criteria.

## Valid inputs, invalid inputs and unexpected conditions

A caller may violate an operation's precondition, a requested resource may not exist, a dependency may become unavailable, or a program may reach a state that its developer assumed impossible. Handling them identically can conceal evidence or make recovery unsafe.

Useful error information can identify the failing operation, relevant context, category, expected contract and what remains known about side effects. It should not indiscriminately disclose private values or internal credentials in user-visible logs.

**Validation failure** is different from **implementation defect**. A user entering an unsupported value does not prove the program is broken; silently accepting the value under a different meaning can still create an implementation defect.

## Return values, exceptions and explicit outcomes

A function can report failure via a distinguished return value, a structured result, an exception, an event or another mechanism. Whatever form is used, callers need to know whether the operation completed and what side effects may already have occurred.

A null result is ambiguous if null can also be an admissible success value. A Boolean success flag can be insufficient when consumers need to distinguish permission errors from missing data and temporary failures.

**Exception handling** does not mean exceptions must be swallowed. Catching every exception and returning a default can hide defects and convert a visible failure into incorrect data.

## Worked example: invalid number input

Suppose an operation requires a string containing a decimal integer in an explicitly defined format and returns its numeric value.

```text
parse_integer("23")   → success, value 23
parse_integer("three")→ invalid-format result
```

Returning numeric zero on every invalid input would be a different contract. It might be indistinguishable from successful parsing of `"0"`, unless the output also identifies whether conversion succeeded. A structured result such as `{ok:false, reason:"invalid-format"}` makes that distinction visible under this toy contract.

This example does not impose JSON, exception classes or one parser implementation. It illustrates why error values and valid data should not be conflated.

## Cleanup, resource release and transactions

A failed operation may have acquired memory, files, locks or other resources. Error handling may need to release them or preserve state so that subsequent operations remain valid. A guarantee of cleanup depends on the execution model, failure type and available facilities.

For a multi-step operation, **rollback** means restoring a defined prior or compensating state under a transaction contract. Compensation may not erase every external effect, such as a message already sent or a physical command already executed.

[Runtime Environments](runtime-environments.md) owns available facilities and execution conditions. [Synchronization](../computation-algorithms/synchronization.md) owns concurrency coordination, including releasing locks under specified invariants.

## Retries, idempotency and ambiguous outcomes

A timeout can mean an operation did not begin, is still in progress or completed without the response reaching the caller. Repeating a request without knowing its semantics can duplicate effects.

A retry policy should consider whether the operation is **idempotent**, whether deduplication persists across failures, whether the operation can safely be repeated, and whether backoff or a deadline matters. Idempotency is a property of a defined effect under specified conditions, not a guarantee that any arbitrary retry is harmless.

[Software Interfaces](software-interfaces.md) owns the operation's observable contract. [Communication & Distributed Systems](../communication-distributed-systems/README.md) owns independent-node transport and partial-failure semantics.

## Diagnostics and uncertainty

Logs, error codes, traces and metrics can support diagnosis; they may also be missing, delayed or incorrect. Recording an error does not automatically establish its cause. A useful investigation separates observation, hypothesis, testing and verified correction.

[Evidence](../scientific-analytical-reasoning/evidence.md) owns how observations support claims. [Testing and Software Lifecycle](testing-and-software-lifecycle.md) owns regression checks and change governance.

## Canonical boundaries

No exception hierarchy, error-code standard, monitoring platform, logging format or recovery strategy is mandatory for Fundamentals. Software error handling is not identical to security incident response or a training assessment.

### Sources

- [MIT 6.005: Specifications and Exceptions](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.005: Debugging and Avoiding Debugging](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/08-avoiding-debugging/).
- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).

**Editorial status:** Reviewed (model-assisted) after the scoped [Wave D Software 54-family audit](../WAVE-D-TECHNICAL-REVIEW-03-04.md). Complete source verification, independent expert review and final publication acceptance remain separate outstanding gates.

[Software & Programming](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
