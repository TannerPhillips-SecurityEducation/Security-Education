# Memory Management

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Memory management  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Virtual addresses and physical storage are different

**Operating-system memory management** coordinates allocation, translation, protection and reclamation of memory resources under an execution model. Many systems provide processes with **virtual address spaces**, which do not directly specify the number, location or existence of corresponding physical memory bytes.

Address translation maps selected virtual addresses to physical frames or other backing resources under OS and hardware rules. Some virtual ranges are unmapped; some are shared or mapped to devices; some may be backed by storage rather than resident RAM. The mere numeric range of a process's virtual addresses is therefore not evidence of installed RAM capacity.

[Memory and Storage](../digital-systems-hardware/memory-and-storage.md) owns hardware retention and hierarchy mechanisms. [Processors and Instruction Sets](../digital-systems-hardware/processors-and-instruction-sets.md) owns relevant ISA semantics, while this article owns OS-level mapping and resource control.

## Address spaces, pages and frames

A **page** is a virtual-memory unit in a selected paging model. A **frame** is a corresponding unit of physical memory under that model. Page tables store mappings and attributes; translation caches such as TLBs may speed access.

Page size, alignment, permission bits and multi-level mapping structures are architecture-dependent. A paging system can support multiple page sizes. A virtual page need not be resident in physical memory at every moment.

The [MIT 6.1810 page-table material](https://pdos.csail.mit.edu/6.S081/2026/labs/pgtbl.html) illustrates address translation in an example kernel. Its specific RISC-V design is a teaching instance, not a mandatory implementation.

## Worked example: page number and offset

Suppose a hypothetical system uses **4096-byte pages**, byte-addressed virtual memory, and a simple base-4096 partition of the virtual address. For decimal virtual address `10000`:

```text
virtual page number = floor(10000 / 4096) = 2
page offset         = 10000 - 2×4096 = 1808 bytes
```

If a page table maps virtual page 2 to physical frame 7 of the same size, and the mapped access is permitted, the resulting physical address is `7×4096+1808=30480` under this stipulated translation model.

This calculation does not establish that page 2 is mapped, that the contents are present, that the access is authorized, or that any actual machine has that mapping.

## Permissions and faults

Mapping information can encode whether a page is readable, writable, executable or otherwise accessible in a given execution context. A memory access that violates the contract may cause a trap or fault. A page fault can also occur because a page is valid but not currently resident, depending on the OS's design.

**A page fault is not synonymous with a bug.** It can be part of ordinary demand paging, copy-on-write or lazy allocation, while other faults indicate invalid or unauthorized access.

[System Calls](system-calls.md) owns entry and request semantics; [Execution Contexts](execution-contexts.md) owns the relevant process and privilege state. The OS should not infer a user's intention from a fault alone.

## Allocation, reclamation and sharing

Memory allocators provide and reclaim resources under specific contracts. Internal and external fragmentation can reduce usable capacity. Sharing can reduce copies but requires protection and synchronization of common state.

Copy-on-write arrangements can allow contexts to initially share physical pages until an attempted write requires a private copy. That technique does not imply that all page contents are physically duplicated at process creation.

A process's declared memory request may succeed under overcommit or virtual reservation rules and still fail later when physical backing is needed. Results depend on system policies and workload.

## Limits and performance

TLB misses, page faults, swapping, locality and contention affect practical performance. A large address space can coexist with small resident working sets or with severe memory pressure. Translating an address correctly does not guarantee its data are semantically valid.

[Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns overall resource tradeoffs, and [Resource Management](resource-management.md) owns quotas and global allocation. This article does not mandate a page size, memory allocator, ISA or protection scheme.

### Sources

- [MIT 6.1810: Page Tables](https://pdos.csail.mit.edu/6.S081/2026/labs/pgtbl.html).
- [MIT 6.1810 Operating Systems course](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces, address-space chapters](https://research.cs.wisc.edu/wind/OSTEP/).

**Editorial status:** Substantive Draft. Translation arithmetic, permission semantics and paging claims require scoped technical review. No mandated operating system or learner assessments introduced.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
