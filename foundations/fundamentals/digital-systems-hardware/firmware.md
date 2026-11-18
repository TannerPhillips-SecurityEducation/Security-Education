# Firmware

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Firmware  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave C Batch 03 audit](../WAVE-C-TECHNICAL-REVIEW-03.md); independent human review pending

## Executable behavior near hardware boundaries

**Firmware** is software or machine-executable instruction content closely associated with controlling, initializing, configuring or operating hardware. It often resides in nonvolatile storage and may run on an embedded controller, peripheral, processor or platform component. The term does **not** imply that code is physically unchangeable or that it always runs before an operating system.

A platform can use firmware for early initialization, device discovery, boot support, configuration, runtime services or specialized control. Other devices use firmware throughout ordinary operation, independent of any general-purpose operating system.

The [NIST SP 800-193 Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final) describe firmware's importance in booting and operating a platform, along with principles for protecting, detecting changes to and recovering the relevant firmware. NIST's platform scope is a particular security context; not all firmware is identical to platform boot firmware.

## Firmware, hardware, drivers and applications

**Hardware** provides physical elements and state. **Firmware** supplies executable behavior on a hardware platform. **Device drivers** are software components that mediate device-specific operations for a computing environment. **Applications** use exposed functionality for user or system tasks.

These categories can overlap in actual implementations. A microcontroller may execute application logic as firmware, while a peripheral controller and operating system driver cooperate on I/O. A machine's processor ISA defines architectural instruction behavior; firmware is one body of software that may execute those instructions.

[Processors and Instruction Sets](processors-and-instruction-sets.md) owns the ISA contract. [Input/Output](input-output.md) owns device interaction. [Hardware Abstraction](hardware-abstraction.md) owns abstract contracts that can hide implementation details.

## Storage, load, execution and configuration

Firmware may reside in flash or another nonvolatile medium and may execute from that medium or be copied into volatile memory, depending on the design. A stored firmware **image** can include executable code, configuration data, metadata and integrity-related information.

The following are different claims:

- The firmware image is **present** in a storage location.
- The image satisfies a **structural format or version rule**.
- The image was **authenticated or integrity-checked** under a defined process.
- The firmware has actually **executed**.
- The hardware and system have reached the **intended operational condition**.

Satisfying one statement does not automatically establish all the others. An authenticated firmware image can still contain defects or implement an inadequate requirement.

## Boot stages and trust boundaries

A boot process can involve hardware reset behavior, initial processor state, early code, memory preparation, device initialization and transfer to a subsequent software stage. The exact sequence varies by processor and platform.

An initial **root of trust**, when present, supplies a basis for selected integrity or authenticity checks. Such a basis is only as trustworthy as its implementation, protected keys, assumptions and update mechanisms. Secure boot, authenticated update and measured boot can have related but different aims; they should not be conflated.

The NIST firmware-resiliency model highlights **protection, detection and recovery** within a defined scope. These are not a universal guarantee that any particular platform is immune to failure or attack.

## Worked example: image capacity versus deployability

Suppose a hypothetical embedded system reserves **128 KiB** of nonvolatile storage for a firmware image, and a candidate firmware package occupies **96 KiB** under its defined file-size convention:

```text
Reserved capacity = 128 × 1024 = 131,072 bytes
Candidate size    = 96 × 1024 = 98,304 bytes
Nominal difference = 32 × 1024 = 32,768 bytes = 32 KiB
```

The image fits the **stated scalar capacity** with 32 KiB remaining. This is **not** proof it can be deployed or booted. An actual platform may reserve space for metadata, multiple banks, recovery code or alignment, require a specific memory layout, or reject the image because of signatures, compatibility, version rules or hardware constraints.

A valid capacity calculation must not be promoted into a deployment-success claim.

## Updates, rollback and recovery

Firmware updates may replace code or configuration that is essential to hardware operation. They can fail because of interruption, incompatible image structure, corrupted data, incorrect device identification or implementation defects.

An update design may use staged activation, multiple image banks, recovery modes, integrity checks and controlled version rollback. These mechanisms have resource and lifecycle tradeoffs. The existence of a rollback file does not guarantee that a device can recover if the boot path or storage itself has failed.

A firmware revision can change physical behavior, latency, interfaces or security characteristics. Regression checks and provenance records must therefore specify which device and revision were evaluated.

[System Lifecycle](../systems-engineering/system-lifecycle.md) owns general configuration evolution; [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns failure consequences and restoration analysis.

## Canonical boundaries

Firmware is not equivalent to the operating system, a hardware schematic, a particular instruction set, or a mandatory security product. This article treats firmware conceptually and does not provide flashing instructions, bypass techniques, manufacturer-specific update commands or certification claims.

### Sources

- [NIST SP 800-193: Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final).
- [MIT 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [NASA: Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave C Batch 03 54-family technical review](../WAVE-C-TECHNICAL-REVIEW-03.md). Full source verification, independent human peer review and final publication acceptance remain separate outstanding gates.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
