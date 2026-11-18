# Waves and Frequency

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Waves and frequency  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave C Batch 02 audit](../WAVE-C-TECHNICAL-REVIEW-02.md); no independent human expert review

## Oscillation and propagation describe different behavior

An **oscillation** is a repeated or approximately repeated variation in a quantity around some condition. A **wave** is a disturbance or pattern that propagates through a medium or, for appropriate fields, through space. Oscillation at a fixed location and propagation across locations are related but distinct.

Examples include mechanical waves on strings, sound-pressure variations in air and electromagnetic waves. Their physical mechanisms are not identical. Some waves require a material medium, while electromagnetic waves can propagate through vacuum. A propagating wave can transport energy without requiring net transport of the medium over the same distance.

The [OpenStax University Physics: Traveling Waves](https://openstax.org/books/university-physics-volume-1/pages/16-1-traveling-waves) reference distinguishes amplitude, period, frequency, wavelength and propagation speed.

## Period, frequency, amplitude and phase

**Period** `T` is the time associated with one complete cycle for a periodic signal. **Frequency** `f` is the number of cycles per unit time:

```text
f = 1/T
T = 1/f
```

The coherent SI unit of frequency is hertz, `1 Hz = 1 s⁻¹`, when the quantity refers to cycles per second. **Amplitude** specifies the extent of variation from a reference. **Phase** specifies a position within a cycle relative to a defined reference; phase is not itself a duration, although it can be associated with temporal offsets for a specified frequency.

For a simple harmonic time signal, one common model is `x(t)=A sin(2πft+φ)`, with amplitude `A`, frequency `f` and initial phase `φ`. This is an idealized sinusoid, not a universal equation for every wave or signal.

An aperiodic disturbance need not have a single well-defined fundamental period. Complex waveforms may contain multiple frequency components and can be described through appropriate spectral methods.

## Wavelength, propagation and speed

**Wavelength** `λ` describes spatial repetition in a periodic traveling wave: the distance between equivalent points of consecutive cycles along the propagation direction. For a nondispersive traveling sinusoidal wave:

```text
v = λ f
```

where `v` is its phase propagation speed under the model. In dispersive environments, different frequency components can propagate with different phase velocities; group velocity and signal/energy transport require separate treatment. Do **not** assume that `v` is identical for all wave types or media.

A frequency can remain the same as a wave enters another medium, while wavelength changes because propagation speed changes. The physical boundary conditions matter.

[OpenStax: Mathematics of Waves](https://openstax.org/books/university-physics-volume-1/pages/16-2-mathematics-of-waves) develops the spatial and temporal descriptions used in such models.

## Worked example: a periodic traveling wave

Suppose a stipulated periodic traveling wave propagates at `300 m/s` with frequency `100 Hz` in a uniform, nondispersive medium. Then:

```text
T = 1 / 100 Hz = 0.01 s
λ = v / f = (300 m/s) / (100 s⁻¹) = 3 m
```

Its period is **10 ms**, and its wavelength is **3 m**. These values follow from the stipulated assumptions, not measurements of a specific sound or electromagnetic wave.

For two points separated by `1.5 m` along the propagation direction under this ideal sinusoid, the spatial phase difference is `2π×1.5/3 = π` radians, or 180 degrees, modulo a full cycle. The calculation does not guarantee that actual signals at those points have identical amplitudes or are free of attenuation and reflection.

## Transverse, longitudinal, and standing-wave behavior

A **transverse** wave has the selected oscillating quantity oriented perpendicular to its propagation direction in the applicable physical description. A **longitudinal** wave has the relevant oscillation along the propagation direction. Examples and classifications depend on the physical medium and modeled field.

A **standing wave** can arise from superposition of waves traveling in opposing directions under appropriate coherence and boundary conditions. Nodes and antinodes characterize ideal standing-wave patterns. The existence of a standing pattern does not mean energy transfer is absent in every possible real arrangement.

Wave **superposition** allows disturbances to combine under linear governing equations; nonlinear materials and strong interactions may require more complicated models. Constructive and destructive interference are consequences of relative phase and amplitude under suitable assumptions.

## Frequency is not throughput, clock rate, or information content

Frequency measures repetition. A signal with 100 transitions per second does not automatically convey 100 bits per second, because the encoding may use several transitions per symbol or represent information by duration, phase or other structure. A processor clock frequency also does not determine instructions per second without an architecture and workload model.

[Analog and Digital Signals](analog-and-digital-signals.md) owns representation by physical signals, while [Information Theory](../information-data/information-theory.md) owns entropy and channel limits. [Transmission and Signaling](../communication-distributed-systems/README.md) is the later specialized subject for communication-channel mechanisms. [Timing and Clocks](../digital-systems-hardware/timing-and-clocks.md) owns hardware timing implementation, not the general physical definition of frequency.

## Scope and references

This article does not prescribe a radio band, communications protocol, mechanical medium, propagation model for all settings, or measurement methodology. It establishes no new universal physical taxonomy and does not resolve G-04's general temporality scope decision.

### Sources

- [OpenStax University Physics Volume 1: Traveling Waves](https://openstax.org/books/university-physics-volume-1/pages/16-1-traveling-waves).
- [OpenStax University Physics Volume 1: Mathematics of Waves](https://openstax.org/books/university-physics-volume-1/pages/16-2-mathematics-of-waves).
- [BIPM: The SI Brochure](https://www.bipm.org/en/publications/si-brochure).

**Editorial status:** Reviewed (model-assisted) after the scoped [Wave C Batch 02 technical audit](../WAVE-C-TECHNICAL-REVIEW-02.md). Exhaustive source verification, independent expert peer review and final publication acceptance remain outstanding.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
