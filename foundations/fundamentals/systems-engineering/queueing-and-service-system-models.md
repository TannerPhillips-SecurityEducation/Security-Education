# Queueing and Service-System Models

**Knowledge area:** [Systems & Engineering](README.md)  
**Subject ID:** F-11-12  
**Development status:** Reviewed (model-assisted; independent human approval not claimed)  
**Source review:** Core claims checked under [Wave H 24-family scoped technical review](../WAVE-H-TECHNICAL-REVIEW-01.md); full source-passage verification not claimed  
**Inventory authority:** [Coverage & Source Triage 02](../COVERAGE-AND-SOURCE-TRIAGE-02.md)

## Queueing models connect demand, service, delay and capacity

A **queueing system** is a model of entities or work items arriving, waiting when immediate service is unavailable, receiving service, and departing under specified policies and capacities. Its purpose is to reason about occupancy, latency, throughput, loss, congestion and service-resource requirements.

Queues occur in communication links, processor schedulers, database request handlers, manufacturing lines, transportation and human service desks. A queue is not inherently a network buffer or a FIFO data structure. It may have one server or many, waiting-room limits or none, different priority rules, and service interruptions.

[Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns general algorithmic resource costs. [Latency and Throughput](../communication-distributed-systems/latency-and-throughput.md) owns communication-specific delay and rate metrics. This subject owns **general service-system models and their flow laws**.

## A queueing system has a boundary and an accounting unit

A minimal service model identifies:

| Component | Meaning | Example |
| --- | --- | --- |
| Arrivals | Items entering the modeled system | Requests per second |
| Queue or waiting region | Work awaiting service | Pending requests |
| Server(s) | Resources processing work | Processing workers |
| Service time | Time an item occupies a server under the model | Seconds per request |
| Service discipline | Rule for selecting work | FIFO, priority or processor sharing |
| Departure | Completion or removal from the boundary | Completed request |
| Capacity | Limits on waiting and/or service | Maximum buffered requests |

The chosen **system boundary** matters. An item may spend time in a waiting queue and then in active service. **Time in system** includes both in the simplest model; **waiting time** includes only time in queue. An admitted request, completed request, dropped request and retried request are different states and events.

A queue can be studied deterministically, stochastically or by simulation. A service system with a measured arrival rate is not automatically a Markovian queue; arrival patterns and service-time dependencies require evidence.

## Rates, utilization and stability

Let λ be an admitted arrival rate in items per unit time, and let μ be a modeled maximum mean service rate for one continuously available server under a stated queueing model. A commonly used nominal **utilization ratio** for a single-server queue is ρ=λ/μ.

If ρ is near one, the queue may experience long delays and sensitivity to variability. In many models, λ≥μ prevents a stable long-run finite queue, but details depend on admission control, losses, dependencies and the service mechanism. A finite-capacity queue can remain bounded by dropping arrivals; finite occupancy alone does not prove acceptable service quality or zero loss.

For a stable system with admitted throughput equal to long-run arrival rate, average arrival rate 5 items/s and average service capacity 6 items/s suggest a nominal utilization of 5/6≈0.8333 under the simple single-server model. This calculation alone does **not** determine mean waiting time without a suitable variability and service discipline model.

**Backpressure** or admission limits can alter the offered work rate; dropping or retrying work changes the relationship between external demand and admitted throughput. Queue stability must be analyzed with the correct boundary and accounting of items.

## Little's law

A foundational result is **Little's law**:

```text
L = λ W
```

where L is the long-run average number of items in the defined stable system, λ is the corresponding long-run effective arrival/departure rate, and W is the mean time an item spends within the **same** system boundary. Under the appropriate long-run averaging, flow-conservation and stability conditions, Little's law is remarkably independent of detailed arrival and service distributions.

The same relation can apply to a **waiting queue alone**, using Lq, the waiting-queue occupancy, and Wq, the time spent waiting, as long as the accounting is consistent. Mixing L for the full system with Wq for the waiting line is a dimensional and semantic error.

**Worked calculation:** A stable modeled service system completes an average 5 requests/s. Each request spends an average 0.4 s inside the chosen boundary. Then L=5×0.4=2 requests in the system on average. This does not mean exactly two requests are present at every instant. Occupancy may vary greatly around its average.

Units check: (requests/s)×s = requests.

## M/M/1 is a specific stochastic model

The notation **M/M/1** commonly represents a queue with Poisson arrivals (exponentially distributed independent interarrival times), exponentially distributed independent service times, and one server, under additional assumptions such as an infinite waiting room, a suitable service discipline (often FCFS), and a stable regime λ<μ.

For the standard stable M/M/1 FCFS queue, the **mean total time in system** is

```text
W = 1/(μ − λ)
```

and the mean number in system is L=λ/(μ−λ). If λ=5 requests/s and μ=6 requests/s, then W=1 s and L=5 requests under this **particular** stochastic model. These results differ from the earlier Little's-law illustration (W=0.4 s) because that illustration described a different service system. They do not contradict Little's law: 5 requests/s × 1 s = 5 requests.

If the arrival process is bursty, service times are not exponential, capacity is finite, or priorities intervene, the M/M/1 formula is generally not justified. The queue may still satisfy a form of Little's law under suitable conditions.

## Deriving the wait from service time and queue occupancy

The standard stable M/M/1 result \(W=1/(\mu-\lambda)\) is the **mean time inside the whole system**. It consists of two distinct contributions: waiting to start service and the time **being served**. Under the exponential service assumption, the mean service duration is \(1/\mu\). Therefore

\[
W=W_q+\frac{1}{\mu},
\qquad
W_q=\frac{1}{\mu-\lambda}-\frac{1}{\mu}
=\frac{\lambda}{\mu(\mu-\lambda)}.
\]

Applying Little's law separately to the **full system** and to the **waiting queue** gives

\[
L=\lambda W=\frac{\lambda}{\mu-\lambda},
\qquad
L_q=\lambda W_q=\frac{\lambda^2}{\mu(\mu-\lambda)}.
\]

The expected number **in active service** is \(L-L_q=\lambda/\mu=\rho\), not automatically one: a single server is either busy with one item or idle, and in the standard stable M/M/1 model it is busy for fraction \(\rho\) of time.

### Worked comparison: demand approaching the same server's capacity

Assume the same hypothetical M/M/1 FCFS server in both cases, with service rate \(\mu=6\) requests/second, infinite waiting room, Poisson arrivals, independent exponential service times, and steady-state \(\lambda<\mu\). Only the admitted arrival rate changes:

| Quantity | Case A: \(\lambda=3\)/s | Case B: \(\lambda=5\)/s |
| --- | ---: | ---: |
| Utilization \(\rho=\lambda/\mu\) | 50% | 83.33% |
| Mean service time \(1/\mu\) | 0.1667 s | 0.1667 s |
| Mean time in system \(W\) | 0.3333 s | 1.0000 s |
| Mean **waiting** \(W_q\) | 0.1667 s | 0.8333 s |
| Mean **total occupancy** \(L\) | 1.0000 requests | 5.0000 requests |
| Mean **queue-only occupancy** \(L_q\) | 0.5000 requests | 4.1667 requests |

The server's modeled **service time did not change**, yet increasing admitted load from three to five requests per second triples mean total time and increases mean waiting time **fivefold**. This is a property of the stipulated M/M/1 model, **not** a general law that all queues have the same numbers or behavior.

**Independent consistency check:** In Case B, Little's law for the full system yields \(5\ \mathrm{requests/s}\times1\ \mathrm{s}=5\) requests on average. For the queue alone it gives \(5\times(5/6)=25/6\approx4.1667\) requests. The remaining \(5-25/6=5/6\) is the mean number being served, equal to utilization \(5/6\).

**Boundary of the inference:** A bounded buffer might drop excess arrivals. Priority scheduling can change individual delays. Bursty arrivals and non-exponential service change the waiting-time formula. The observed throughput might differ from offered traffic because of admission control and retries. The general lesson is to **identify the accounting boundary and stochastic assumptions before interpreting a mean**.

The derivation of \(W_q\), \(L_q\) and the server-busy contribution follows the [MIT OpenCourseWare 2.854/2.853 M/M/1 Queue notes (2016), pp. 1–2](https://www.ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/927056a1af54772a587fd84ad4951e71_MIT2_854F16_Mm1Queue.pdf), whose rendered source pages were directly inspected for this editorial pass.

## Waiting, latency and rate are not the same property

**Latency** may include transmission, propagation, queuing, processing, scheduling and other components across an end-to-end path. A server can have high raw capacity but poor latency when demand, burstiness, contention or admission rules lead to long waits.

Likewise, high throughput does not guarantee fairness, bounded worst-case delay or acceptable tail latency. Mean waiting time alone can conceal very long delays for some items. Percentile and tail behavior need their own measurement/estimation model and workload boundary.

A queueing simulation can be internally consistent with its arrival/service assumptions while failing to represent a real workload. Validation requires appropriate observation and measurement, not merely a plausible equation.

## Queue disciplines and tradeoffs

- **FIFO/FCFS:** Process items in arrival order under the declared model; simple ordering does not guarantee every job has equal response time.
- **Priority:** Favor selected classes; low-priority work can experience prolonged waiting or starvation unless safeguards are defined.
- **Shortest-job-first variants:** Can reduce mean response under certain assumptions but require job-size information and may disadvantage long work.
- **Processor sharing / round robin:** Split service opportunities, introducing scheduling overhead and different response-time behavior.

An algorithm's correctness, the service discipline, and the physical capacity of the system are separate concerns. [Scheduling](../operating-system-principles/scheduling.md) owns OS execution decisions; queueing here defines the domain-independent service models behind their potential tradeoffs.

## Worked interpretation: queue occupancy is not a traffic count

Suppose an observer measures two pending requests at one instant. That observation is not the same as **an average occupancy of two over an interval**. Similarly, a sample of ten completed requests is not automatically a representative estimate of steady-state service time. Measurement must define when the interval began, whether unfinished work was counted, admission/drop rules, and whether the system had reached the assumed operating regime.

**Unknown without additional evidence:** Whether arrivals are stationary, whether Little's law's averaging conditions hold, whether priorities affect fairness, or whether a specific service architecture delivers the modeled response.

## Source references and boundaries

- [MIT OpenCourseWare: Queues, Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/pages/readings/), Little's law, queueing disciplines, stability and service networks.
- [MIT 6.02: Queueing and Little's Law lecture notes](https://courses.csail.mit.edu/6.02/s2009/handouts/L17.pdf), flow and waiting behavior in a communication example.
- [MIT OCW 2.854: M/M/1 Queue](https://www.ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/927056a1af54772a587fd84ad4951e71_MIT2_854F16_Mm1Queue.pdf), pp. 1–2, visually inspected; derives whole-system versus waiting-only time and occupancy, including (W_q=W-1/\mu) and (L_q=\lambda W_q).
- [MIT OpenCourseWare: Introduction to Queues and Little's Law](https://ocw.mit.edu/courses/1-203j-logistical-and-transportation-planning-methods-fall-2006/pages/calendar/), general systems/service applications.

Canonical related foundations include [Stochastic Processes and Markov Models](../mathematics-logic/stochastic-processes-and-markov-models.md) for random arrivals and dependence; [Temporal Concepts and Models](../models-abstraction/temporal-concepts-and-models.md) for temporal intervals; [Latency and Throughput](../communication-distributed-systems/latency-and-throughput.md) for communication rate/delay; and [Reliability and Failure](reliability-and-failure.md) for robustness of systems and resources.

**Editorial status:** Reviewed (model-assisted) under [Wave H Technical Review 01](../WAVE-H-TECHNICAL-REVIEW-01.md). Complete source-passage verification, independent qualified expert acceptance and Published status remain open.

**Administrative depth pass (November 19, 2026):** The queue-only waiting/occupancy derivations and two-load comparison were recomputed and source-scoped under [Fundamentals Administrative Editorial Pass 01](../ADMINISTRATIVE-EDITORIAL-PASS-01.md). Earlier Wave H evidence remains historical, and this pass does not confer fully Verified, independently accepted or Published status.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
