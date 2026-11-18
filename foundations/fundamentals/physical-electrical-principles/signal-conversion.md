# Signal Conversion

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Signal conversion  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Converting signals changes representation under constraints

**Signal conversion** is the transformation of a physical or modeled signal from one form or representation to another for observation, processing, storage or actuation. Examples include analog-to-digital conversion (**ADC**), digital-to-analog conversion (**DAC**), voltage/current conversion, and transduction between nonelectrical physical quantities and electrical signals.

Conversion is not synonymous with measurement, data encoding, or information-theoretic compression. It can lose, introduce, or transform information under physical constraints. A valid output code does not establish that the underlying physical input was measured faithfully.

[Analog and Digital Signals](analog-and-digital-signals.md) owns signal representation distinctions; [Sensors and Actuators](sensors-and-actuators.md) owns the devices that observe or affect physical quantities. [Information Theory](../information-data/information-theory.md) owns Shannon entropy and channel limits.

## Sampling, quantization, and encoding are distinct steps

A conceptual ADC process may involve:

```text
Analog input → signal conditioning → sample/hold
             → quantization → numeric encoding
```

**Sampling** selects signal values at specific instants. **Quantization** maps a continuum or finely resolved range to a finite or discrete set of levels. **Encoding** maps the selected level to a symbol or bit pattern. An actual converter may combine operations or use a different implementation; the breakdown is conceptual.

A discrete-time sample can retain a continuous-valued mathematical amplitude before quantization. Conversely, a quantized signal can be described as a piecewise-constant continuous-time signal. These are separate representation axes.

[MIT 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) covers sampling, reconstruction and quantization in its lecture sequence. Sampling requires band-limit, filtering and timing assumptions; quantization requires range, resolution and error assumptions.

## Worked example: an ideal twelve-bit quantizer

Suppose an ideal 12-bit ADC partitions the **half-open range [0 V, 4.096 V)** into 4096 equally wide bins, numbered 0 through 4095. Let its quantization rule for in-range input voltage `V` be `code=floor(V/Δ)`, where

```text
Δ = 4.096 V / 4096 = 0.001 V = 1 mV
```

For input `2.500 V`:

```text
code = floor(2.500/0.001) = 2500
```

Under a **lower-edge reconstruction convention**, this code corresponds to `2.500 V`; under a **bin-midpoint convention**, it corresponds to `2.5005 V`. Neither convention proves the original physical voltage exactly equaled the reconstruction value.

The maximum midpoint quantization error inside the ideal input range is at most `Δ/2=0.5 mV`. Inputs at or above 4.096 V or below 0 V fall outside the stated converter range and require an explicit overrange or clipping rule, not an invented code.

A real ADC can have noise, gain/offset error, nonlinearity, missing codes, finite acquisition time and reference instability. **12-bit width is not a guarantee of twelve effective bits of measurement accuracy.**

## Aliasing and frequency limitations

An ideal sampler only obtains values at selected instants; different continuous-time signals can coincide at those instants. Frequencies above half the sample rate may alias into lower apparent frequencies under common uniform-sampling models. The conditions for reconstructing a band-limited signal require appropriate sampling, filtering and other assumptions.

For a chosen 1,000 samples/s clock, the conventional Nyquist frequency is 500 Hz. This does not by itself guarantee lossless reconstruction of every signal below 500 Hz: sufficient band limitation, suitable sampling/reconstruction, and physical design matter.

[Waves and Frequency](waves-and-frequency.md) owns the general frequency and phase mechanics. [MIT Lecture 21: Sampling](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-21-sampling/) illustrates sampling and anti-aliasing.

## DAC and reconstruction

A **digital-to-analog converter** maps digital codes to physical analog output levels or waveforms according to a selected conversion law. The resulting output is not necessarily the continuous original input; it may contain quantization steps, update transitions, reconstruction-filter effects and distortions.

An ideal zero-order hold maintains each output level until an update. This can approximate a waveform but introduces a specific hold response. Additional analog filtering may be used to shape the result.

A sample's numeric representation and the physical output voltage are separate entities. Consumer interfaces must define reference levels, load, permitted update timing, and output range.

## Conversion chains and uncertainty

End-to-end sensor data can experience multiple mappings:

```text
Temperature → sensor voltage → ADC code → reported number
                                       ↓
                                  control decision
                                       ↓
Heater command ← DAC/driver output ← numeric command
```

The chain can accumulate uncertainties, introduce nonlinearities and change timing. Adding a higher-resolution converter cannot recover information already lost in an inaccurate sensor or improperly limited analog front end.

This article owns signal conversion, not all filter design (G-05 remains assigned within existing headings) or the general metrology established by [Measurement](../scientific-analytical-reasoning/measurement.md). No hardware topology or converter brand is mandated.

### Sources

- [MIT 6.003: Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
- [MIT 6.003: Lecture 22 Sampling and Quantization](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-22-sampling-and-quantization/).
- [MIT 6.003: Lecture Notes including Sampling and Quantization](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/).
- [NIST: International System of Units and metrology](https://www.nist.gov/pml).
- [JCGM: International Vocabulary of Metrology](https://jcgm.bipm.org/vim/en/).

**Editorial status:** Substantive Draft. Quantization example, source boundaries and analog conversion claims require an independent scoped model-assisted technical audit before promotion. No new subject headings or assessments are introduced.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
