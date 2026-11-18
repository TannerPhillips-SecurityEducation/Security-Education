# Wave E Technical Review: Batch 01 — Operating System Principles

**Review date:** November 17, 2026  
**Scope:** Kernels; System Calls; Processes and Threads; Scheduling; Memory Management; Filesystems; Drivers and Devices; Execution Contexts; System Initialization; Resource Management.  
**Method:** Second-pass examination of ten committed GitHub articles; six material claim groups per article; comparison with the [MIT 6.1810 Fall 2026 operating-systems course](https://pdos.csail.mit.edu/6.S081/2026/overview.html), [its lecture and lab references](https://pdos.csail.mit.edu/6.S081/2026/schedule.html), the official [Operating Systems: Three Easy Pieces](https://research.cs.wisc.edu/wind/OSTEP/) chapters and selected [POSIX specifications](https://pubs.opengroup.org/onlinepubs/9799919799/); independent recalculation of invented examples; direct GitHub file fetches for every distinct relative Markdown file destination.  
**Disposition:** **60 material claim groups reviewed; all ten articles pass scoped model-assisted technical review**, with source corrections noted. Neither complete source verification nor independent human peer review, implementation certification, physical testing or publication acceptance is claimed.

## Claim-to-source ledger

### Kernels
[Reviewed article](operating-system-principles/kernels.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| K-01 | Kernel, entire operating system and external services are distinct | [MIT 6.1810 overview](https://pdos.csail.mit.edu/6.S081/2026/overview.html); no conflation with every OS utility |
| K-02 | Privileged operations and an application/kernel protection boundary require explicit authorization | [MIT 6.1810 traps lab](https://pdos.csail.mit.edu/6.S081/2026/labs/traps.html); correct boundary caveat |
| K-03 | Monolithic and microkernel structures allocate privileged services differently | [MIT OS organization course schedule](https://pdos.csail.mit.edu/6.S081/2026/schedule.html); neither architecture is automatically correct or secure |
| K-04 | Kernel resource policy, scheduler and driver components have separate responsibilities | [OSTEP virtualization/concurrency/persistence](https://research.cs.wisc.edu/wind/OSTEP/); table explicitly illustrative, not four new system categories |
| K-05 | Toy 100-byte device request: kernel queue acceptance differs from successful transmission | The article makes no ungrounded remote-delivery or durability claim; observed or promised status matters |
| K-06 | Context and privileged-code faults may affect shared system operation | MIT overview; isolation and recovery consequences depend on actual design |

### System Calls
[Reviewed article](operating-system-principles/system-calls.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| SC-01 | A system call is a protected OS-service interface, not every library call | [MIT traps lab](https://pdos.csail.mit.edu/6.S081/2026/labs/traps.html); correct distinction |
| SC-02 | API wrapper, controlled transition, dispatch, argument validation and result are distinct stages | MIT traps lab and [OS overview](https://pdos.csail.mit.edu/6.S081/2026/overview.html); example path not a universal implementation |
| SC-03 | A read request can return fewer bytes than requested | [POSIX System Interfaces](https://pubs.opengroup.org/onlinepubs/9799919799/) and OSTEP files; requesting 100 with successful result 40 must process **40**, not assume 100 |
| SC-04 | Zero read length and error meanings depend on descriptor/resource and selected semantics | Correctly qualified as context-dependent, not universal end-of-file across all device types |
| SC-05 | System-call arguments and buffer permissions require validation at the protection boundary | MIT traps and [MIT page tables lab](https://pdos.csail.mit.edu/6.S081/2026/labs/pgtbl.html); valid address spelling does not grant access |
| SC-06 | Blocking, partial completion and retries create separate behavior claims | The article does not equate submission, process completion and durable external effect |

### Processes and Threads
[Reviewed article](operating-system-principles/processes-and-threads.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| PT-01 | Process resource/address-space context differs from a thread execution context | [MIT thread switching](https://pdos.csail.mit.edu/6.S081/2026/homework/xv6-threads.html) and [OSTEP threads](https://research.cs.wisc.edu/wind/OSTEP/); no fixed OS design mandated |
| PT-02 | Registers, stack and scheduling state may be per-thread while resources are shared | MIT course materials; sharing does not imply thread-safety |
| PT-03 | Runnable, running, blocked and terminated are model states, not a universal kernel enumeration | OSTEP CPU virtualization; state caveat retained |
| PT-04 | Two read–modify–write attempts on one shared counter can lose an increment | Recomputed A reads 0, B reads 0, both write 1; final **1** possible |
| PT-05 | Two correctly completed atomic increments or independent private process counters give different outcomes | Shared atomic: final **2**; private counters: two independent local values of **1**. No false equivalence |
| PT-06 | Context switching and interprocess communication depend on scheduling, isolation and shared resources | MIT 6.1810; no implication that process isolation removes all dependencies |

### Scheduling
[Reviewed article](operating-system-principles/scheduling.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| SG-01 | Scheduling assigns eligible execution opportunities under selected policy | [OSTEP CPU Scheduling](https://research.cs.wisc.edu/wind/OSTEP/); correct separation from thread creation |
| SG-02 | Runnable, blocked, preemptive and cooperative concepts depend on OS contract | OSTEP; a runnable task need not immediately execute |
| SG-03 | Nonpreemptive FCFS toy execution A=4, B=3, C=2 | Waiting times **0,4,7**; mean **11/3≈3.6667** time units |
| SG-04 | Nonpreemptive shortest-job-first on same arrival time | C→B→A; waiting times **0,2,5**; mean **7/3≈2.3333** time units |
| SG-05 | Waiting, response, turnaround and throughput are distinct metrics | OSTEP scheduling; faster mean wait not unconditional best policy |
| SG-06 | Multicore assignment, deadline guarantees, resource contention and fairness need explicit assumptions | OSTEP scheduling; priority does not prove deadline satisfaction |

### Memory Management
[Reviewed article](operating-system-principles/memory-management.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| MM-01 | Virtual address spaces are not direct physical RAM-capacity declarations | [MIT page tables lab](https://pdos.csail.mit.edu/6.S081/2026/labs/pgtbl.html); mapped pages and devices vary |
| MM-02 | Virtual page, physical frame, mapping, protection and translation caching have distinct functions | MIT page tables lab; source and model align |
| MM-03 | 4096-byte page example at virtual address 10000 | Virtual page floor(10000/4096)=**2**; offset **1808** |
| MM-04 | Mapping page 2 to frame 7 under explicitly permitted access | Physical address 7×4096+1808=**30480**; mapping is hypothetical, not asserted about a machine |
| MM-05 | Page fault may implement demand paging or indicate invalid access | MIT page tables plus [copy-on-write lab](https://pdos.csail.mit.edu/6.S081/2026/labs/cow.html); not all faults are bugs |
| MM-06 | Allocation, copy-on-write, fragmentation, virtual reservation and resident resources differ | MIT virtual memory lab; adding COW source strengthens the original claim |

### Filesystems
[Reviewed article](operating-system-principles/filesystems.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| FS-01 | Names, paths, file IDs, handles and physical storage locations differ | [OSTEP Files and Directories](https://research.cs.wisc.edu/wind/OSTEP/); path text is not intrinsic object identity |
| FS-02 | Open handles, metadata, permissions and file content represent distinct concerns | OSTEP files and POSIX interfaces; content encoding belongs separately to Information & Data |
| FS-03 | Six-thousand-byte file under fixed 4096-byte exclusive block allocation | ceil(6000/4096)=**2** blocks and 8192 bytes allocated |
| FS-04 | Internal block slack under the stipulated nonsparse file model | 8192−6000=**2192 bytes**, excluding metadata/compression/sparse/shared effects |
| FS-05 | A buffered write acknowledgment need not imply crash durability | [OSTEP FSCK and Journaling](https://research.cs.wisc.edu/wind/OSTEP/); journal guarantees depend on selected mode, hardware and ordering |
| FS-06 | Filesystems and databases provide distinct naming, persistence and query contracts | OSTEP and [Information & Data: Databases and Queries](information-data/databases-and-queries.md); no assertion that a filesystem is a database engine |

### Drivers and Devices
[Reviewed article](operating-system-principles/drivers-and-devices.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| DD-01 | Driver mediates OS requests and device behavior; location can vary | [MIT 6.1810 device-driver lectures](https://pdos.csail.mit.edu/6.S081/2026/schedule.html); correct qualified definition |
| DD-02 | Driver/OS, hardware I/O and physical effect have different contracts | MIT device drivers and [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); no claim of physical confirmation after queuing |
| DD-03 | Polling, interrupts and DMA are different mechanisms | [OSTEP I/O Devices](https://research.cs.wisc.edu/wind/OSTEP/); DMA does not eliminate every CPU operation |
| DD-04 | Three accepted requests versus two reported completions | Acceptance **3/3=100%**, reported completion **2/3≈66.67%** under the stipulated status log |
| DD-05 | A completion fraction from three requests is not a reliability estimate | Correctly avoids extrapolation to long-run failure rate |
| DD-06 | Resource sharing, kernel fault containment, and device lifecycle are conditional on architecture | MIT 6.1810; no required driver architecture |

### Execution Contexts
[Reviewed article](operating-system-principles/execution-contexts.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| EC-01 | Execution context is the state necessary to resume a computation at a chosen boundary | [MIT thread switching](https://pdos.csail.mit.edu/6.S081/2026/homework/xv6-threads.html); scope varies with runtime/OS |
| EC-02 | Registers, stacks, address mapping and saved state vary by transition and ABI | MIT traps lab; not every register must be saved for every transition |
| EC-03 | Runnable/blocked context and scheduled physical CPU activity are distinct | OSTEP scheduling; preserved context does not guarantee eligibility |
| EC-04 | Toy 3ms task + 0.2ms switch + 4ms task | **7.2 ms** elapsed under exactly one stipulated switch and no other overhead |
| EC-05 | Interrupt handler context and reentrant function behavior need their own constraints | MIT 6.1810 traps; user software signal and hardware interrupt not equated |
| EC-06 | Resuming a saved context need not recreate previously shared system state | MIT 6.1810; changes by other actors can remain observable |

### System Initialization
[Reviewed article](operating-system-principles/system-initialization.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| IN-01 | Initialization is a change toward readiness, not the whole system lifecycle | [MIT 6.1810 OS overview](https://pdos.csail.mit.edu/6.S081/2026/overview.html); stages illustrative |
| IN-02 | Firmware handoff, kernel setup, devices and services have different startup conditions | MIT OS overview and [NIST SP 800-193](https://csrc.nist.gov/pubs/sp/800/193/final); not one universal startup path |
| IN-03 | Loaded, entered, initialized, ready and end-to-end successful are distinct claims | [NASA interface guidance](https://www.nasa.gov/reference/6-3-interface-management/); no “boot complete” assumption without criterion |
| IN-04 | Toy concurrent startup dependency calculation | 2+max(3,5)+1=**8 seconds** with independent stages and unlimited relevant resources |
| IN-05 | Same tasks sequentially | 2+3+5+1=**11 seconds**; not claimed as measured boot times |
| IN-06 | Retrying a startup step and signed firmware can still fail under specified conditions | NIST SP 800-193; authenticity and functionality distinct |

### Resource Management
[Reviewed article](operating-system-principles/resource-management.md)

| ID | Claim group | Grounding and finding |
| --- | --- | --- |
| RM-01 | Allocation, accounting, reservation, quota and utilization are distinct | [OSTEP virtualization/resource discussions](https://research.cs.wisc.edu/wind/OSTEP/); distinctions preserved |
| RM-02 | Exclusive, shared, temporal and virtualized resource use require stated policies | MIT OS engineering; no universal isolation guarantee |
| RM-03 | Toy exclusive pool of ten indivisible units and requests 4,5,3 | Total **12**, exceeding available capacity by **2 units** |
| RM-04 | Selecting requests 4 and 5 leaves one unreserved unit | **9 reserved, 1 unreserved**, not a claim of optimal fairness |
| RM-05 | Fairness, priority, deadlock and starvation are different properties | OSTEP concurrency and scheduling; no automatic policy selection |
| RM-06 | Metrics of current, peak, reserved and physical usage differ | MIT/OSTEP; virtual memory reservation not equal physical RAM consumption |

## Recorded corrections and improvements

1. **Kernels:** Replaced an inaccessible legacy `pdos.lcs.mit.edu` 2026 overview URL with the accessible [MIT 6.1810 Fall 2026 course overview](https://pdos.csail.mit.edu/6.S081/2026/overview.html). Its topic summary explicitly includes kernels, interrupts, system calls, context switches, file systems and hardware interaction.
2. **Memory Management:** Added the MIT 6.1810 Copy-on-Write lab alongside its Page Tables lab, strengthening the grounding for shared physical pages and delayed copying.
3. **No material arithmetic correction** was required. All ten articles' constructed examples and stated caveats passed under their declared models.

## Independently recomputed examples

| Stipulated example | Result |
| --- | --- |
| FCFS scheduler A(4), B(3), C(2) | Mean waiting 11/3≈3.67 |
| SJF scheduler C(2), B(3), A(4) | Mean waiting 7/3≈2.33 |
| Virtual address 10000, 4096-byte pages | Virtual page 2, offset 1808 |
| Virtual page 2 mapped to physical frame 7 | Physical address 30480 |
| 6000-byte file in 4096-byte blocks | 2 blocks, 8192 allocated, 2192 slack |
| Three queued device requests, two reported completed | 100% queued, ≈66.67% reported completed |
| 3ms + 0.2ms switch + 4ms | 7.2ms |
| Initializing kernel 2s, then parallel 3s and 5s, then launch 1s | 8s parallel; 11s sequential |
| Pool ten units, requests 4,5,3 | Demand 12, excess 2; 4+5 leaves one |

## Link integrity and source-review limitations

The ten Operating System Principles articles contain **103 relative Markdown-link occurrences** resolving to **35 distinct local file destinations**. Every one of the **35 file paths was directly fetched through GitHub** in this review: **35/35 found**. This checks destination existence on the default branch, **not** individual fragment anchors, external URL reachability, every link in the corpus, or semantic correctness of every relationship.

Public MIT 6.1810 2026 pages and the OSTEP chapter index were read as source context. MIT's teaching implementation is one example, not a universal kernel contract. The Open Group POSIX specification was linked as a normative reference, but some pages were inaccessible to automated retrieval during this pass; **no complete POSIX conformance review is claimed**. The article examples are stipulated, not empirical measurements of any hardware or OS.

This is a bounded **model-assisted material claim-family review**, corresponding to **Core claims checked**, not full `Verified` source status, independently performed human expert peer review, a production OS audit or final `Published` acceptance.

## Architecture and acceptance disposition

- **All ten Operating System Principles articles pass scoped model-assisted review.** They retain distinct ownership for privileged kernel mediation, syscalls, processes/threads, scheduling, memory, files, drivers, execution state, initialization and OS resource allocation.
- The original **12 approved knowledge areas** and **109 approved headings** remain unchanged.
- With existing 90 reviewed articles from Waves A–D, this audit would bring the corpus to **100 Reviewed, 9 Draft** pending the nine distributed-systems audits.
- G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML remain unresolved. No Knowledge Checks, Practical Assessments, new categories or mandated runtime/vendor tools have been added.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
