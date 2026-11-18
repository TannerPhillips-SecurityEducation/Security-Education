# Filesystems

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Filesystems  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## File abstractions map names to stored information

A **filesystem** provides a defined way to organize, name, access and maintain files and related metadata under an operating-system model. A **file** represents a resource with contents and associated attributes; a **directory** provides naming or organizational relationships; a **path** identifies a resource through a namespace according to system rules.

File names, file identifiers, open handles and underlying storage locations are different. Two paths can sometimes refer to the same underlying file; a path can change while an already-open handle remains usable; a symbolic reference can point to a missing target.

The [MIT 6.1810 operating-systems curriculum](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) covers file systems, logging and crash recovery. [Data Structures and Formats](../information-data/data-structures-and-formats.md) owns data encoding, while this subject owns OS-level file naming, storage and persistence interfaces.

## Files, directories, attributes and handles

A file may expose a byte-oriented interface, records or other semantics depending on the system. Metadata can include size, timestamps, permissions or identifiers. These attributes are reported facts under a filesystem contract, not automatically a complete description of historical events.

Opening a file usually establishes an access context or handle. Read, write and seek operations depend on this context, flags, offsets, permissions and file type. The operation's return value must not be interpreted beyond its contract: a write accepted into a cache is not automatically durable across power loss.

[System Calls](system-calls.md) owns protected request entry; [Resource Management](resource-management.md) owns quotas, handles and storage capacity constraints.

## Worked example: block allocation overhead

Suppose a hypothetical filesystem stores an ordinary, nonsparse file of **6000 bytes** in fixed **4096-byte allocation blocks**, allocates whole blocks exclusively to this file and applies no compression or deduplication. Ignoring separate metadata and sharing:

```text
Blocks needed = ceil(6000/4096) = 2
Allocated block bytes = 2×4096 = 8192
Unused space within allocated data blocks = 8192−6000 = 2192 bytes
```

The difference is **2192 bytes of internal slack in this toy allocation model**. It does not establish actual disk use for a real filesystem, which may employ extents, fragments, sparse files, compression, inline data or shared blocks.

The block size is an implementation property, not the fundamental unit of the file's logical content. [Memory and Storage](../digital-systems-hardware/memory-and-storage.md) owns the physical storage media.

## Atomicity, ordering and recovery

Filesystems can buffer writes, reorder operations and store metadata separately from data. A write syscall completing and an application receiving an acknowledgment do not universally establish crash durability.

**Journaling** or write-ahead logging may help preserve selected consistency properties across crashes, but the guarantees depend on what is logged, write ordering, hardware behavior and recovery procedures. Crash recovery can restore structural integrity without necessarily preserving every recent application-level operation.

Transactions and atomic rename operations may offer particular guarantees under specified filesystem semantics. A backup is not a direct substitute for integrity checking, and a single successful read does not verify a file's provenance.

## Access control and identity

Permissions may depend on owner, group, access-control lists, capabilities, process context or other policy. A name resembling a privileged path does not by itself confer permission. A directory can control whether a pathname can be resolved even if a file's own permission bits would otherwise allow an operation.

Path normalization and symbolic links can affect what resource a name denotes; a caller should not infer object identity solely from textual similarity. [Addressing and Naming](../communication-distributed-systems/README.md) will develop broader distributed naming concepts later.

## Filesystems versus databases and applications

A filesystem stores resources under naming and access rules. A database adds its own data models, indexes, query and transactional semantics. An application's document format determines how the file's contents are interpreted. These layers can interoperate but do not collapse into one concept.

[Databases and Queries](../information-data/databases-and-queries.md) owns logical querying. [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns lineage, history and data management, not OS filesystems.

### Sources

- [MIT 6.1810 Operating System Engineering, file systems and crash recovery](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces, Persistence chapters](https://research.cs.wisc.edu/wind/OSTEP/).
- [POSIX System Interfaces](https://pubs.opengroup.org/onlinepubs/9799919799/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
