# Analog and Digital Signals

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Analog and digital signals  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## A signal is a varying physical or modeled quantity carrying information

A **signal** is a quantity varying over time, space or another independent variable that can be used to represent or convey information. **Analog** signaling represents information through a varying quantity that may take values in a continuum over a defined range. **Digital** signaling represents information through a discrete set of symbols or states under a defined encoding convention.

The distinction concerns representation, **not an assertion that digital physical voltages only take exactly two values**. Real electronic edges take finite time, exhibit noise and may pass through undefined voltage regions. A decoder interprets selected physical conditions as symbols according to thresholds and timing rules.

The [MIT Signals and Systems course](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) develops continuous-time and discrete-time signals, sampling and system operations. [Symbols and Encoding](../information-data/symbols-and-encoding.md) owns general representation mappings; this article owns physical signal forms and conversion boundaries.

## Continuous time, discrete time, amplitude and quantization

Two separate distinctions matter:

- **Continuous versus discrete time:** whether a signal is modeled over a continuum of times or only specified sampling instants.
- **Continuous versus discrete amplitude:** whether its represented or admissible magnitude values are continuous or restricted to specified levels.

A sampled analog signal may be discrete in time while still having continuous-valued samples. A quantizer maps a continuous-valued input into a finite or countable set of output levels. A digital system commonly combines sampling, quantization and coding, but the mechanisms are separable.

A **binary** representation is one kind of digital representation, not the entire definition of digital information. The real physical implementation may use more than two voltage levels or encode information in pulse timing, phase, frequency or another property.

## Signal features and uncertainty

A signal model may specify **amplitude**, baseline/offset, duration, rise time, frequency content, phase, noise, distortion and bandwidth. These describe different characteristics. A clean-looking waveform does not automatically mean that its recovered data are correct, and a valid digital symbol interpretation does not prove the sensor's physical input was measured correctly.

An analog measurement can be perturbed by noise before conversion. Quantization introduces representational error when the input lies between output levels. Timing uncertainty and sampling-clock differences can alter which value is captured. Each issue should be assessed under an explicit physical and encoding model.

[Measurement](../scientific-analytical-reasoning/measurement.md) owns instrument accuracy and uncertainty. [Data Types](../information-data/data-types.md) owns values and their computational interpretation.

## Worked example: samples and quantization bins

Suppose a hypothetical sensor signal is sampled every 1 millisecond over a **half-open 100-millisecond interval**, at instants `0,1,...,99 ms`:

```text
sampling frequency: f_s = 1 / 0.001 s = 1000 samples/s
sampling instants:  0 ms through 99 ms inclusive
number of samples:  100
```

The endpoint convention matters: including an additional sample at 100 ms would produce 101 samples.

Suppose each sample is then assigned to one of **256 equal-width quantization bins** spanning a hypothetical input range `[0 V, 5 V)`. With 8-bit output codes, a bin width is

```text
Δ = 5 V / 256 = 0.01953125 V
```

This step is about 19.53 mV. A mid-bin reconstruction estimate has a maximum absolute quantization error of `Δ/2≈9.77 mV` **for a finite input strictly within the stated range under an ideal nearest-bin model**. Values outside the range may clip; physical noise, nonlinearity and converter inaccuracies add other errors. The code 255 does not by itself mean the exact input was 5 V.

## Sampling, aliasing and reconstruction conditions

Sampling can make different continuous-time frequencies produce indistinguishable sample sequences, a phenomenon called **aliasing**. For **cosine** waves sampled at 1000 samples/s with the same zero phase, the sequences at 600 Hz and 400 Hz are exactly identical: `cos(2π·600n/1000) = cos(2π·400n/1000)` for every integer sample index `n`. This is a concrete aliasing identity, not a claim that arbitrary phase-shifted waveforms or physical receivers behave identically.

For a suitably band-limited signal, the classical ideal sampling theorem provides reconstruction conditions when the sampling frequency exceeds twice the highest relevant signal frequency, with appropriate reconstruction and assumptions. This is not a guarantee that every real converter reconstructs arbitrary inputs, or that an unbounded signal can be perfectly sampled.

[MIT 6.003 Lecture 21: Sampling](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-21-sampling/) discusses anti-aliasing and reconstruction. Actual anti-alias filters, clocks and converter performance require concrete specifications.

## Digital robustness is conditional

Digital receivers can tolerate some perturbations when the received physical signal stays within valid decision regions, but sufficiently large noise, attenuation, timing error or hardware faults can change decoded symbols. Error detection and correction may address selected errors under specified coding assumptions, not provide an absolute guarantee.

An analog system can be precise within its intended range, and a digital system can be inaccurate because of conversion, calibration or encoding mistakes. Neither representation is inherently universally more truthful, secure or reliable.

## Boundaries and applications

[Waves and Frequency](waves-and-frequency.md) owns the general physical behavior of waves, cycles, wavelength and frequency. [Signal Conversion](README.md) remains a separate approved heading for analog-to-digital and digital-to-analog transduction mechanisms. [Information Theory](../information-data/information-theory.md) owns entropy and information limits, not every physical noise mechanism.

This article introduces no mandated modulation scheme, converter, radio protocol, physical-layer standard or assessment.

### Sources

- [MIT OpenCourseWare: Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
- [MIT 6.003 Lecture 21: Sampling](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-21-sampling/).
- [MIT 6.003: Sampling and Quantization, lecture notes index](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/).
- [OpenStax University Physics Volume 1: Traveling Waves](https://openstax.org/books/university-physics-volume-1/pages/16-1-traveling-waves).

**Editorial status:** Substantive Draft. The sampling and quantization examples are stipulated; theorem conditions, physical caveats and numbers require a separate scoped technical/source review.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
